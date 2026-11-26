"""Dependency-free repository checks. Never execute educational submissions."""
from pathlib import Path, PurePosixPath
import argparse
import json
import re
import subprocess
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SUFFIXES = ("", ".pt-BR", ".es")
ROOT_DOCS = {"README", "AGENTS", "AUTHORS", "CONTRIBUTING", "CODE_OF_CONDUCT", "SECURITY", "SUPPORT"}
SLUGS = (
    "getting-started", "fundamentals", "git-architecture", "basic-commands",
    "branches", "merge-and-conflicts", "remote-repositories", "history-and-recovery",
    "github", "gitlab", "ci-cd", "professional-workflows", "security",
    "advanced-git", "git-internals", "command-reference", "practical-projects", "exercises",
)
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)|!\[[^\]\n]*\]\(([^)\n]+)\)")
FENCE = re.compile(r"(?ms)^[ \t]*(`{3,}|~{3,})[^\n]*\n.*?^[ \t]*\1[ \t]*$")
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{30,}\b"),
    re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{15,}\b"),
    re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{24,}\b"),
)
TEXT_SUFFIXES = {".md", ".py", ".json", ".yml", ".yaml", ".txt", ".sh", ".ps1", ".bat", ".cmd", ".svg", ".toml", ".ini", ".cfg", ".js", ".ts", ".html", ".css"}

def tracked_paths(root):
    result = subprocess.run(["git", "ls-files", "-z"], cwd=root, check=True, stdout=subprocess.PIPE)
    return set(result.stdout.decode("utf-8").rstrip("\0").split("\0")) - {""}

def portable_path(path):
    if not isinstance(path, str) or not path or "\\" in path or ":" in path:
        return False
    return all(part not in ("", ".", "..") and not part.endswith((".", " "))
               and not any(c in part for c in '<>:"|?*')
               and not re.fullmatch(r"(?i)(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(?:\..*)?", part)
               for part in path.split("/"))

def locale_group(path):
    p = PurePosixPath(path)
    stem = re.sub(r"\.(pt-BR|es|en)$", "", p.stem)
    if p.parent.as_posix() == "docs/localized" and stem in ROOT_DOCS:
        return tuple([stem + ".md"] + ["docs/localized/" + stem + s + ".md" for s in SUFFIXES[1:]])
    if p.parent.as_posix() == "." and stem in ROOT_DOCS:
        return tuple([stem + ".md"] + ["docs/localized/" + stem + s + ".md" for s in SUFFIXES[1:]])
    if p.parent.as_posix() == "docs/ai-assisted-development" and stem == "README":
        return tuple("docs/ai-assisted-development/README." + loc + ".md" for loc in ("en", "pt-BR", "es"))
    return tuple(str(p.with_name(stem + s + ".md")) for s in SUFFIXES)

def read_text(root, path):
    return (root / path).read_text(encoding="utf-8")

def check_structure(root, paths):
    errors = []
    folded = {}
    allowed_roots = set(SLUGS) | {"docs", "scripts", "tests", "assets", ".github"}
    required = {"LICENSE", ".gitignore", "scripts/curriculum.json", "scripts/example_manifest.json",
                "scripts/validate.py", "tests/test_validate.py", ".github/workflows/quality.yml"}
    required.update(n + ".md" for n in ROOT_DOCS)
    for missing in sorted(required - paths):
        errors.append("Missing required path: " + missing)
    for path in sorted(paths):
        if not portable_path(path):
            errors.append("Non-portable repository path: " + path)
            continue
        parts = path.split("/")
        for length in range(1, len(parts) + 1):
            prefix = "/".join(parts[:length])
            kind = "file" if length == len(parts) else "directory"
            key = prefix.casefold()
            previous = folded.get(key)
            if previous is not None and previous != (prefix, kind):
                errors.append("Case-colliding paths: " + prefix + " (" + kind + ") and "
                              + previous[0] + " (" + previous[1] + ")")
            else:
                folded[key] = (prefix, kind)
        p = root / path
        if not p.is_file() or p.is_symlink() or any(parent.is_symlink() for parent in p.parents if parent != root and root in parent.parents):
            errors.append("Missing, non-file or symbolic tracked path: " + path)
        if "/" in path and path.split("/")[0] not in allowed_roots:
            errors.append("Unexpected top-level directory: " + path)
        if "/" not in path and path not in required:
            errors.append("Unexpected root file: " + path)
    return errors

def check_locales(paths):
    errors = []
    groups = {locale_group(p) for p in paths if p.endswith(".md")}
    for group in sorted(groups):
        for p in group:
            if p not in paths:
                errors.append("Missing locale: " + p)
    for path in sorted(p for p in paths if p.endswith(".md")):
        if path not in locale_group(path):
            errors.append("Unexpected locale naming: " + path)
    return errors

def resolve_link(source, raw):
    """Resolve URL paths using POSIX semantics; return None for external links/fragments."""
    url = urlsplit(raw.strip().strip("<>"))
    if url.scheme or url.netloc or not url.path:
        return None
    target = unquote(url.path)
    if target.startswith("/") or "\\" in target:
        raise ValueError("absolute or backslash path")
    parts = source.split("/")[:-1]
    for segment in target.split("/"):
        if segment in ("", "."):
            continue
        if segment == "..":
            if not parts:
                raise ValueError("path escapes repository")
            parts.pop()
        else:
            parts.append(segment)
    return "/".join(parts)

def check_links(root, paths):
    errors = []
    for path in sorted(p for p in paths if p.endswith(".md")):
        text = FENCE.sub("", read_text(root, path))
        for match in LINK.finditer(text):
            raw = match.group(1) or match.group(2)
            try:
                target = resolve_link(path, raw)
            except ValueError:
                errors.append("Invalid local link in " + path)
                continue
            if target is not None and target not in paths and not any(p.startswith(target + "/") for p in paths):
                errors.append("Broken local link: " + path + " -> " + target)
    return errors

def load_modules(root):
    data = json.loads(read_text(root, "scripts/curriculum.json"))
    if not isinstance(data, dict) or set(data) != {"modules"} or not isinstance(data["modules"], list):
        raise ValueError("invalid curriculum object")
    modules = data["modules"]
    if any(not isinstance(m, dict) or set(m) != {"slug", "chapters"} for m in modules):
        raise ValueError("invalid module record")
    if tuple(m["slug"] for m in modules) != SLUGS:
        raise ValueError("module order or slugs differ from roadmap")
    for m in modules:
        chapters = m["chapters"]
        if not isinstance(chapters, list) or any(not isinstance(c, str) or not re.fullmatch(r"[0-9]{2}-[a-z0-9]+(?:-[a-z0-9]+)*", c) for c in chapters):
            raise ValueError("invalid chapter slug")
        if chapters != sorted(chapters) or len({c[:2] for c in chapters}) != len(chapters):
            raise ValueError("chapter order or duplicate number")
    return modules

def block_targets(text, name, source):
    start, end = "<!-- " + name + " -->", "<!-- /" + name + " -->"
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError("missing/duplicate " + name + " block")
    middle = text.split(start, 1)[1].split(end, 1)[0]
    if text.index(start) > text.index(end):
        raise ValueError("reversed " + name + " block")
    return [resolve_link(source, m.group(1) or m.group(2)) for m in LINK.finditer(middle)]

def navigation_entries(modules, suffix):
    """Map each curriculum page to its three ordered navigation slots."""
    readme = "README" + suffix + ".md"
    index = "docs/learning-path" + suffix + ".md"
    module_paths = [m["slug"] + "/" + readme for m in modules]
    labels = {
        "": ("Previous", "Index", "Next", "Previous module", "Next module"),
        ".pt-BR": ("Anterior", "Índice", "Próximo", "Módulo anterior", "Próximo módulo"),
        ".es": ("Anterior", "Índice", "Siguiente", "Módulo anterior", "Siguiente módulo"),
    }[suffix]
    previous, middle, following, previous_module, next_module = labels
    for pos, module in enumerate(modules):
        path = module_paths[pos]
        before = module_paths[pos - 1] if pos else None
        after = module_paths[pos + 1] if pos + 1 < len(modules) else None
        chapters = [module["slug"] + "/" + c + "/" + readme for c in module["chapters"]]
        yield path, ((previous, before), (middle, index), (following, after)), chapters
        for j, chapter in enumerate(chapters):
            yield chapter, (
                (previous if j else previous_module, chapters[j - 1] if j else before),
                (middle, path),
                (following if j + 1 < len(chapters) else next_module,
                 chapters[j + 1] if j + 1 < len(chapters) else after),
            ), None


def navigation_line(document, entries):
    """Canonical localized Markdown; relative paths use POSIX on every OS."""
    from posixpath import relpath
    return " · ".join(
        "[" + label + "](" + relpath(target, str(PurePosixPath(document).parent)) + ")"
        if target is not None else "—"
        for label, target in entries
    )


def navigation_body(text, name):
    start, end = "<!-- " + name + " -->", "<!-- /" + name + " -->"
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError("missing/duplicate " + name + " block")
    a, b = text.index(start), text.index(end)
    if a >= b:
        raise ValueError("reversed " + name + " block")
    return text[a + len(start):b].strip()


def check_navigation(root, paths):
    errors = []
    try:
        modules = load_modules(root)
    except (ValueError, OSError, TypeError, KeyError):
        return ["Invalid curriculum manifest"]
    expected_docs = set()
    for suffix in SUFFIXES:
        readme = "README" + suffix + ".md"
        index = "docs/learning-path" + suffix + ".md"
        module_paths = [m["slug"] + "/" + readme for m in modules]
        if index not in paths:
            errors.append("Missing learning index: " + index)
        else:
            text = read_text(root, index)
            actual = [resolve_link(index, m.group(1) or m.group(2)) for m in LINK.finditer(text)]
            actual = [p for p in actual if p in module_paths]
            if actual != module_paths:
                errors.append("Learning index order/coverage: " + index)
        for document, entries, expected_chapters in navigation_entries(modules, suffix):
            expected_docs.add(document)
            if document not in paths:
                errors.append("Missing curriculum document: " + document)
                continue
            try:
                text = read_text(root, document)
                expected = navigation_line(document, entries)
                # Remove fenced examples so navigation cannot be hidden inside code.
                visible = FENCE.sub("", text)
                top = navigation_body(text, "navigation")
                bottom = navigation_body(text, "navigation-footer")
                if (top != navigation_body(visible, "navigation")
                        or bottom != navigation_body(visible, "navigation-footer")):
                    raise ValueError("navigation hidden in code")
                if top != expected:
                    errors.append("Incorrect navigation: " + document)
                if bottom != expected:
                    errors.append("Incorrect footer navigation: " + document)
                # Header immediately follows title and locale selector; footer ends page.
                header = visible.split("<!-- navigation -->", 1)[0].strip().splitlines()
                if (len([line for line in header if line.strip()]) != 2
                        or not header[0].startswith("# ")
                        or not set(locale_group(document)).issubset(
                            {resolve_link(document, m.group(1) or m.group(2))
                             for m in LINK.finditer(header[-1])})):
                    errors.append("Incorrect navigation header placement: " + document)
                if not text.rstrip().endswith("<!-- /navigation-footer -->"):
                    errors.append("Incorrect navigation footer placement: " + document)
                if visible.index("<!-- /navigation -->") > visible.index("<!-- navigation-footer -->"):
                    errors.append("Incorrect navigation block order: " + document)
                if expected_chapters is not None and block_targets(visible, "chapters", document) != expected_chapters:
                    errors.append("Incorrect chapter index: " + document)
                links = {resolve_link(document, m.group(1) or m.group(2)) for m in LINK.finditer(visible)}
                if not set(locale_group(document)).issubset(links):
                    errors.append("Missing locale selector: " + document)
            except (ValueError, IndexError):
                errors.append("Invalid navigation block: " + document)
    for p in sorted(paths):
        if p.split("/")[0] in SLUGS and re.search(r"(^|/)README(?:\.pt-BR|\.es)?\.md$", p) and p not in expected_docs:
            errors.append("Unregistered module/chapter README: " + p)
    return errors

def check_examples(root, paths):
    """No arbitrary execution. Until the first labs, manifest is intentionally empty."""
    try:
        manifest = json.loads(read_text(root, "scripts/example_manifest.json"))
    except (ValueError, OSError):
        return ["Invalid example manifest"]
    if manifest != []:
        return ["Executable example protocol not implemented; manifest must remain empty until reviewed"]
    errors = []
    for p in sorted(paths):
        parts = PurePosixPath(p).parts
        if any(part.casefold() == "examples" for part in parts[:-1]):
            errors.append("Unapproved example file: " + p)
    return errors

def check_secrets(root, paths):
    errors = []
    for path in sorted(paths):
        if PurePosixPath(path).name in (".env", "id_rsa", "id_ed25519") or (PurePosixPath(path).name.startswith(".env.") and PurePosixPath(path).name != ".env.example"):
            errors.append("Potential secret file: " + path)
        if PurePosixPath(path).suffix.lower() not in TEXT_SUFFIXES or path == "scripts/validate.py":
            continue
        for number, line in enumerate(read_text(root, path).splitlines(), 1):
            if any(pattern.search(line) for pattern in SECRET_PATTERNS):
                errors.append("Potential secret: " + path + ":" + str(number))
    return errors

CHECKS = ("structure", "locales", "links", "navigation", "examples", "secrets")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", choices=CHECKS + ("all",), default="all")
    args = parser.parse_args()
    paths = tracked_paths(ROOT)
    checks = dict(structure=lambda: check_structure(ROOT, paths), locales=lambda: check_locales(paths),
                  links=lambda: check_links(ROOT, paths), navigation=lambda: check_navigation(ROOT, paths),
                  examples=lambda: check_examples(ROOT, paths), secrets=lambda: check_secrets(ROOT, paths))
    failed = False
    for name in CHECKS if args.check == "all" else (args.check,):
        try:
            errors = checks[name]()
        except (OSError, ValueError, UnicodeError, TypeError, KeyError):
            errors = ["Unable to validate " + name + "; inspect input files"]
        print(name + ": " + ("FAIL" if errors else "PASS"))
        for error in errors:
            print("  " + error)
        failed |= bool(errors)
    return int(failed)

if __name__ == "__main__":
    raise SystemExit(main())
