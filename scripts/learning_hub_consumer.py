"""Reference build-time consumer for a trusted local SHA-1 Git object database.

Do not import or execute snapshot code, checkout filters, learner submissions or
untrusted repository configuration. No network, deployment or runtime integration.
"""
import hashlib
import os
from pathlib import Path
import re
import stat
import subprocess
import tempfile

if __package__:
    from . import learning_hub_contract as contract
    from . import validate as v
else:
    import learning_hub_contract as contract
    import validate as v

OID = re.compile(r"[0-9a-f]{40}")
MAX_FILES = 3000
MAX_BYTES = 32 * 1024 * 1024
LOCK = {"guide_id": "git-study-guide", "manifest_version": "1.0.0",
        "assessment_version": 1, "command_catalog_version": 1}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_lock(text):
    value = contract.strict_json(text)
    require(isinstance(value, dict) and set(value) == set(LOCK) | {"revision"}, "Invalid lock fields")
    require(isinstance(value["revision"], str) and bool(OID.fullmatch(value["revision"])),
            "A full lowercase SHA-1 commit ID is required")
    require(contract.canonical({k: value[k] for k in LOCK}) == contract.canonical(LOCK),
            "Unsupported guide or schema version")
    return value


def git(repo, *args, input_bytes=None):
    env = {k: value for k, value in os.environ.items() if not k.upper().startswith("GIT_")}
    env.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_COUNT="0",
               GIT_TERMINAL_PROMPT="0", GIT_NO_LAZY_FETCH="1", GIT_ALLOW_PROTOCOL="")
    result = subprocess.run(["git", "--no-replace-objects", "-C", str(repo), *args],
                            input=input_bytes, env=env, capture_output=True, timeout=60)
    require(result.returncode == 0, "Unable to read trusted local Git object")
    return result.stdout


def blob_id(data):
    header = b"blob " + str(len(data)).encode("ascii") + b"\0"
    return hashlib.sha1(header + data, usedforsecurity=False).hexdigest()


def tree_inventory(repo, revision):
    require(isinstance(revision, str) and bool(OID.fullmatch(revision)), "Invalid revision")
    require(git(repo, "rev-parse", "--show-object-format").strip() == b"sha1", "Unsupported object format")
    require(git(repo, "cat-file", "-t", revision).strip() == b"commit", "Revision is not a commit")
    require(git(repo, "rev-parse", "--verify", revision + "^{commit}").strip().decode("ascii") == revision,
            "Revision did not resolve to the exact commit")
    listing = git(repo, "ls-tree", "-r", "-l", "-z", "--full-tree", revision)
    inventory, folded = {}, {}
    total = 0
    for entry in listing.split(b"\0"):
        if not entry:
            continue
        meta, raw_path = entry.split(b"\t", 1)
        mode, object_type, raw_oid, raw_size = meta.split()
        path, oid = raw_path.decode("utf-8"), raw_oid.decode("ascii")
        require(mode == b"100644" and object_type == b"blob" and OID.fullmatch(oid),
                "Nonregular or executable tree entry")
        require(contract.safe_path(path) and path not in inventory, "Invalid or duplicate tree path")
        size = int(raw_size)
        require(size >= 0, "Invalid blob size")
        parts = path.split("/")
        for i in range(1, len(parts)+1):
            prefix = "/".join(parts[:i])
            value = (prefix, i == len(parts))
            key = prefix.casefold()
            require(key not in folded or folded[key] == value, "Case or file/directory collision")
            folded[key] = value
        inventory[path] = (oid, size)
        total += size
        require(len(inventory) <= MAX_FILES and total <= MAX_BYTES, "Snapshot exceeds fixture bounds")
    require(bool(inventory), "Empty snapshot")
    return inventory


def export_snapshot(repo, inventory, root):
    require(root.is_dir() and not root.is_symlink() and not any(root.iterdir()), "Expected empty staging directory")
    require(all(contract.safe_path(path) for path in inventory), "Unsafe export path")
    objects = {}
    for oid, size in inventory.values():
        require(OID.fullmatch(oid) and type(size) is int and size >= 0, "Invalid export object")
        require(oid not in objects or objects[oid] == size, "Inconsistent blob size")
        objects[oid] = size
    data = git(repo, "cat-file", "--batch", input_bytes=b"".join(
        oid.encode("ascii") + b"\n" for oid in objects))
    offset, blobs = 0, {}
    for oid, size in objects.items():
        end = data.find(b"\n", offset)
        require(end >= offset, "Missing blob header")
        require(data[offset:end] == (oid + " blob " + str(size)).encode("ascii"), "Unexpected blob header")
        start = end + 1
        content = data[start:start+size]
        offset = start + size
        require(len(content) == size and data[offset:offset+1] == b"\n" and blob_id(content) == oid,
                "Invalid blob bytes")
        offset += 1
        blobs[oid] = content
    require(offset == len(data), "Unexpected batch output")
    for path, (oid, _) in inventory.items():
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as handle:
            handle.write(blobs[oid])


def verify_stage(root, inventory):
    require(root.is_dir() and not root.is_symlink(), "Invalid staging directory")
    seen = set()
    expected_dirs = {"/".join(path.split("/")[:i]) for path in inventory
                     for i in range(1, len(path.split("/")))}
    for directory, dirs, files in os.walk(root, followlinks=False):
        for name in dirs:
            p = Path(directory) / name
            require(p.relative_to(root).as_posix() in expected_dirs and not p.is_symlink()
                    and not getattr(p, "is_junction", lambda: False)(),
                    "Unexpected or symbolic staging directory")
        for name in files:
            p = Path(directory) / name
            path = p.relative_to(root).as_posix()
            require(contract.safe_path(path) and path in inventory and stat.S_ISREG(p.lstat().st_mode),
                    "Unexpected or nonregular staged file")
            oid, size = inventory[path]
            require(p.stat().st_size == size and blob_id(p.read_bytes()) == oid, "Staged blob mismatch")
            seen.add(path)
    require(seen == set(inventory), "Missing staged path")


def consume(repo, lock_text, trusted_root=v.ROOT):
    """Return validated manifest and provenance, without changing an active pin."""
    lock = read_lock(lock_text)
    inventory = tree_inventory(repo, lock["revision"])
    with tempfile.TemporaryDirectory(prefix="git-study-guide-consumer-") as temp:
        root = Path(temp).resolve()
        export_snapshot(repo, inventory, root)
        verify_stage(root, inventory)
        paths = set(inventory)
        # Compare parsed schema data to the trusted consumer's supported schemas.
        # Normal checkout line-ending conversion does not change JSON semantics.
        for name in contract.SCHEMAS:
            path = "schemas/" + name + ".schema.json"
            actual = contract.json_file(root, paths, path)
            trusted = contract.strict_json((trusted_root / path).read_text(encoding="utf-8"))
            require(contract.canonical(actual) == contract.canonical(trusted), "Unsupported schema contents")
        require(not v.check_structure(root, paths), "Invalid snapshot structure")
        require(not v.check_locales(paths), "Invalid locale inventory")
        require(not v.check_navigation(root, paths), "Invalid source navigation")
        require(not v.check_links(root, paths), "Invalid source links")
        require(not v.check_command_catalog(root, paths), "Invalid generated command reference")
        require(not v.check_assessment_pilot(root, paths), "Invalid generated assessment pages")
        manifest = contract.validate_manifest(root, paths)
        return {"revision": lock["revision"], "schema_version": manifest["schema_version"], "manifest": manifest}
