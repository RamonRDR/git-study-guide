"""Sprint 17 internal assessment records. Never execute learner input."""
import re

if __package__:
    from .command_catalog import locale_map, read_json, require, token, unique_strings
else:
    from command_catalog import locale_map, read_json, require, token, unique_strings

LOCALES = ("en", "pt-BR", "es")
BANKS = {"01-quizzes": "quiz", "02-challenges": "challenge",
         "03-interviews": "interview", "04-mock-assessments": "mock"}
DIFFICULTIES = ("easy", "medium", "hard")
TARGETS = {"quiz": 12, "challenge": 4, "interview": 8, "mock": 1}
COMMON = {"id", "difficulty", "prerequisites", "title", "prompt", "hints", "explanation"}
EXTRA = {"quiz": {"type", "choices", "answer"},
         "challenge": {"estimated_minutes", "setup", "solution", "checks", "execution", "execution_reason"},
         "interview": {"expected_answer", "rubric", "follow_ups"},
         "mock": {"duration_minutes", "quiz_ids", "challenge_ids", "interview_ids", "rubric"}}
CHECK_FIELDS = {"clean": set(), "branch": {"value"}, "head-content": {"file", "value"},
                "index-content": {"file", "value"}, "work-content": {"file", "value"},
                "tracked": {"file"}, "untracked": {"file"}, "ancestor": {"older", "newer"},
                "same-ref": {"left", "right"}, "commit-count": {"value"},
                "parent-count": {"value"}, "tag-type": {"tag", "value"}, "no-unmerged": set()}
FILES = {"notes.txt", "review.txt", "catalog.txt", "ignored.txt", ".gitignore", "future.txt"}
REF = re.compile(r"(?:HEAD(?:\^[12])?|main|feat/[a-z0-9-]+|recovery/[a-z0-9-]+|v[0-9]+\.[0-9]+\.[0-9]+)")
VALUES = {"status: draft", "status: ready", "status: reviewed", "status: recovered",
          "review: done", "status: experiment", "future work", "ignored.txt"}

def local_list(items):
    return isinstance(items, list) and bool(items) and all(locale_map(item) for item in items)

def positive_int(value):
    return type(value) is int and value > 0

def valid_ref(value):
    return isinstance(value, str) and bool(REF.fullmatch(value))

def valid_check(check):
    if not isinstance(check, dict) or not isinstance(check.get("kind"), str) or check["kind"] not in CHECK_FIELDS:
        return False
    kind = check["kind"]
    if set(check) != CHECK_FIELDS[kind] | {"kind"}:
        return False
    for key, value in check.items():
        if key == "file" and (not isinstance(value, str) or value not in FILES):
            return False
        if key in {"older", "newer", "left", "right", "tag"} and not valid_ref(value):
            return False
        if key == "value":
            if kind in {"commit-count", "parent-count"}:
                if type(value) is not int or not 0 <= value <= 20:
                    return False
            elif kind == "branch":
                if not valid_ref(value) or value.startswith(("HEAD", "v")):
                    return False
            elif kind == "tag-type":
                if value not in ("tag", "commit"):
                    return False
            elif not isinstance(value, str) or value not in VALUES:
                return False
    return True

def validate_record(record, kind, chapters):
    require(isinstance(record, dict) and set(record) == COMMON | EXTRA[kind], "Invalid assessment fields")
    require(token(record["id"]) and record["id"].startswith(kind + "-"), "Invalid assessment ID")
    require(record["difficulty"] in DIFFICULTIES, "Invalid difficulty")
    require(unique_strings(record["prerequisites"], lambda p: isinstance(p, str) and p in chapters),
            "Invalid prerequisite")
    for name in ("title", "prompt", "explanation"):
        require(locale_map(record[name]), "Invalid locale map: " + name)
    require(local_list(record["hints"]), "Invalid hints")
    if kind == "quiz":
        require(record["type"] == "single-choice", "Unsupported quiz type")
        choices = record["choices"]
        require(isinstance(choices, list) and len(choices) == 3, "Expected three quiz choices")
        require(all(isinstance(c, dict) and set(c) == {"id", "text"} and token(c["id"])
                    and locale_map(c["text"]) for c in choices), "Invalid quiz choice")
        ids = [c["id"] for c in choices]
        require(len(ids) == len(set(ids)) and record["answer"] in ids, "Invalid quiz answer or duplicate choice")
        for locale in LOCALES:
            require(len({c["text"][locale] for c in choices}) == len(choices), "Duplicate localized choice")
    elif kind == "challenge":
        require(positive_int(record["estimated_minutes"]), "Invalid estimated time")
        require(record["execution"] == "local_only" and locale_map(record["execution_reason"]),
                "Invalid challenge execution")
        require(locale_map(record["setup"]) and local_list(record["solution"]), "Invalid solution/setup")
        require(isinstance(record["checks"], list) and bool(record["checks"]) and
                all(valid_check(c) for c in record["checks"]), "Invalid state check")
    elif kind == "interview":
        require(locale_map(record["expected_answer"]) and local_list(record["rubric"])
                and local_list(record["follow_ups"]), "Invalid interview rubric")
    elif kind == "mock":
        require(positive_int(record["duration_minutes"]) and local_list(record["rubric"]), "Invalid mock rubric")
        for field in ("quiz_ids", "challenge_ids", "interview_ids"):
            require(unique_strings(record[field], token), "Invalid mock references")

def load_assessments(root, paths, modules):
    chapters = {m["slug"] + "/" + c for m in modules if m["slug"] != "exercises" for c in m["chapters"]}
    module = next(m for m in modules if m["slug"] == "exercises")
    require(module["chapters"] == list(BANKS), "Assessment bank order mismatch")
    expected = {"exercises/" + slug + "/records.json" for slug in BANKS}
    require({p for p in paths if p.startswith("exercises/") and p.endswith(".json")} == expected,
            "Assessment bank paths mismatch")
    grouped, records = {}, {}
    for slug, kind in BANKS.items():
        path = "exercises/" + slug + "/records.json"
        data = read_json(root, path)
        require(isinstance(data, dict) and set(data) == {"schema_version", "kind", "records"}
                and type(data["schema_version"]) is int and data["schema_version"] == 1
                and data["kind"] == kind and isinstance(data["records"], list), "Invalid assessment bank")
        require(len(data["records"]) == 3 * TARGETS[kind], "Incorrect bank size: " + kind)
        for difficulty in DIFFICULTIES:
            require(sum(isinstance(r, dict) and r.get("difficulty") == difficulty for r in data["records"])
                    == TARGETS[kind], "Incorrect difficulty distribution: " + kind)
        for record in data["records"]:
            validate_record(record, kind, chapters)
            require(record["id"] not in records, "Duplicate assessment ID")
            records[record["id"]] = (kind, record)
        grouped[slug] = data["records"]
    for record in grouped["04-mock-assessments"]:
        for kind in ("quiz", "challenge", "interview"):
            for ref in record[kind + "_ids"]:
                require(ref in records and records[ref][0] == kind and
                        records[ref][1]["difficulty"] == record["difficulty"], "Invalid mock reference")
    return grouped

def grade_quiz(record, choice_id):
    """Exact comparison; no fuzzy or AI grading."""
    return isinstance(choice_id, str) and choice_id == record["answer"]
