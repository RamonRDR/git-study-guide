"""Fixed read-only predicate evaluator for trusted disposable QA fixtures only.

No CLI, arbitrary command execution, untrusted repository intake or learner submission
runner. The caller owns the isolated fixture and supplies the Git/read callbacks.
"""
if __package__:
    from .assessment_pilot import valid_check
else:
    from assessment_pilot import valid_check


def evaluate(check, run, read_file):
    if not valid_check(check):
        raise ValueError("Invalid state predicate")
    kind = check["kind"]

    def output(*args):
        result = run(*args)
        return result.stdout if result.returncode == 0 else None

    def ref(name, object_type="commit"):
        return output("rev-parse", "--verify", name + "^{" + object_type + "}")

    def content(revision, path):
        return output("show", revision + ":" + path)

    if kind == "clean":
        return output("status", "--porcelain=v1") == b""
    if kind == "branch":
        return output("symbolic-ref", "--short", "HEAD") == (check["value"] + "\n").encode()
    if kind in {"head-content", "index-content", "ref-content", "work-content"}:
        path = check["file"]
        if kind == "work-content":
            actual = read_file(path)
        elif kind == "index-content":
            actual = content("", path)
        else:
            actual = content(check.get("ref", "HEAD"), path)
        return actual == (check["value"] + "\n").encode("ascii")
    if kind == "tracked":
        return output("ls-files", "--error-unmatch", "--", check["file"]) is not None
    if kind == "untracked":
        return output("ls-files", "--others", "--exclude-standard", "--", check["file"]) == (
            check["file"] + "\n").encode()
    if kind == "ancestor":
        return run("merge-base", "--is-ancestor", check["older"], check["newer"]).returncode == 0
    if kind in {"same-ref", "different-ref", "same-tree"}:
        object_type = "tree" if kind == "same-tree" else "commit"
        a, b = ref(check["left"], object_type), ref(check["right"], object_type)
        if a is None or b is None:
            return False
        return a != b if kind == "different-ref" else a == b
    if kind in {"commit-count", "ref-commit-count"}:
        return output("rev-list", "--count", check.get("ref", "HEAD")) == (str(check["value"]) + "\n").encode()
    if kind == "parent-count":
        value = output("rev-list", "--parents", "-1", "HEAD")
        return value is not None and len(value.split()) - 1 == check["value"]
    if kind == "tag-type":
        return output("cat-file", "-t", "refs/tags/" + check["tag"]) == (check["value"] + "\n").encode()
    if kind == "no-unmerged":
        return output("ls-files", "-u") == b""
    raise ValueError("Unsupported state predicate")
