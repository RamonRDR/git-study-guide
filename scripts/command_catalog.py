"""Internal command reference pilot; validation only, never execute catalog commands."""
import json
import re
from pathlib import PurePosixPath
from urllib.parse import urlsplit

LOCALES = ("en", "pt-BR", "es")
SUFFIX = {"en": "", "pt-BR": ".pt-BR", "es": ".es"}
MODULE = "command-reference"
REGISTRY = "scripts/command_catalog_categories.json"
MINIMUM = 101
KINDS = {"native-command", "subcommand", "option-usage", "workflow", "external-tool", "platform-operation"}
LEVELS = {"beginner", "intermediate", "advanced"}
RISKS = {"read-only", "state-change", "destructive", "history-rewrite", "remote-change", "sensitive"}
EFFECTS = {"unchanged", "changes", "conditional", "not-applicable"}
EFFECT_KEYS = {"working_tree", "index", "history", "remote", "other"}
LOCAL_FIELDS = {"purpose", "prerequisites", "options", "when_to_use", "when_to_avoid",
                "expected_state", "effect_notes", "common_errors", "alternatives", "recovery", "requirements"}
FIELDS = LOCAL_FIELDS | {"id", "command", "kind", "category", "level", "intent_tags",
                         "syntax", "examples", "effects", "risk", "related_chapters", "references"}
ID = re.compile(r"[a-z0-9]+(?:[.-][a-z0-9]+)*")
SLUG = re.compile(r"[0-9]{2}-[a-z0-9]+(?:-[a-z0-9]+)*")
CHAPTER = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*/[0-9]{2}-[a-z0-9]+(?:-[a-z0-9]+)*")
OFFICIAL_HOSTS = {"git-scm.com", "docs.github.com", "cli.github.com", "docs.gitlab.com",
                  "gitlab.com", "github.com"}

def require(condition, message):
    if not condition:
        raise ValueError(message)

def unique_keys(pairs):
    obj = {}
    for key, value in pairs:
        require(key not in obj, "Duplicate JSON key: " + key)
        obj[key] = value
    return obj

def read_json(root, path):
    return json.loads((root / path).read_text(encoding="utf-8"), object_pairs_hook=unique_keys)

def plain(value):
    return isinstance(value, str) and bool(value.strip()) and value == value.strip() and not any(
        ord(c) < 32 or c in "<>" for c in value)

def technical(value):
    return isinstance(value, str) and bool(value.strip()) and value == value.strip() and all(
        ord(c) >= 32 and c != "\x7f" for c in value) and "\x60" not in value

def locale_map(value):
    return isinstance(value, dict) and set(value) == set(LOCALES) and all(plain(v) for v in value.values())

def unique_strings(values, predicate):
    return isinstance(values, list) and bool(values) and all(predicate(v) for v in values) and len(set(values)) == len(values)

def token(value):
    return isinstance(value, str) and bool(ID.fullmatch(value))

def official_url(value):
    if not isinstance(value, str):
        return False
    try:
        url = urlsplit(value)
        if url.scheme != "https" or url.netloc not in OFFICIAL_HOSTS or not url.path or url.path == "/":
            return False
        if url.netloc == "github.com":
            return url.path.startswith(("/git/git/", "/cli/cli/"))
        if url.netloc == "gitlab.com":
            return url.path.startswith("/gitlab-org/")
        return True
    except ValueError:
        return False

def categories(root):
    data = read_json(root, REGISTRY)
    require(isinstance(data, dict) and set(data) == {"schema_version", "categories"} and
            type(data["schema_version"]) is int and data["schema_version"] == 1, "Invalid category registry")
    items = data["categories"]
    require(isinstance(items, list) and len(items) == 14, "Expected 14 categories")
    for i, item in enumerate(items, 1):
        require(isinstance(item, dict) and set(item) == {"slug", "title", "target"}, "Invalid category")
        slug = item["slug"]
        require(isinstance(slug, str) and SLUG.fullmatch(slug) and slug.startswith(f"{i:02d}-"), "Invalid category order")
        require(locale_map(item["title"]), "Invalid category titles")
        require(type(item["target"]) is int and item["target"] > 0, "Invalid category target")
    require(sum(item["target"] for item in items) == 120, "Invalid approved target total")
    return items

def validate_entry(entry, category, chapter_ids):
    require(isinstance(entry, dict) and set(entry) == FIELDS, "Invalid command fields")
    require(token(entry["id"]), "Invalid command ID")
    require(technical(entry["command"]) and technical(entry["syntax"]), "Invalid command or syntax")
    require(entry["category"] == category, "Invalid category reference")
    require(entry["kind"] in KINDS and entry["level"] in LEVELS, "Invalid kind or level")
    require(unique_strings(entry["intent_tags"], token), "Invalid intent tags")
    for key in LOCAL_FIELDS:
        require(locale_map(entry[key]), "Invalid localized field: " + key)
    effects = entry["effects"]
    require(isinstance(effects, dict) and set(effects) == EFFECT_KEYS and all(v in EFFECTS for v in effects.values()),
            "Invalid state effects")
    risk = entry["risk"]
    require(isinstance(risk, dict) and set(risk) == {"class", "notes"} and risk["class"] in RISKS
            and locale_map(risk["notes"]), "Invalid risk")
    if risk["class"] == "read-only":
        require(all(v in {"unchanged", "not-applicable"} for v in effects.values()), "Read-only risk contradicts effects")
    require(unique_strings(entry["related_chapters"], lambda v: isinstance(v, str) and
                           bool(CHAPTER.fullmatch(v)) and v in chapter_ids), "Invalid related chapter")
    require(unique_strings(entry["references"], official_url), "Invalid official references")
    examples = entry["examples"]
    require(isinstance(examples, dict) and set(examples) == {"basic", "professional"}, "Missing example")
    for example in examples.values():
        require(isinstance(example, dict) and set(example) == {"command", "context"} and
                technical(example["command"]) and locale_map(example["context"]), "Invalid example")

def load_category(root, item, chapter_ids):
    slug = item["slug"]
    path = f"{MODULE}/{slug}/catalog.json"
    data = read_json(root, path)
    require(isinstance(data, dict) and set(data) == {"schema_version", "category", "entries"} and
            type(data["schema_version"]) is int and data["schema_version"] == 1 and data["category"] == slug,
            "Invalid catalog header: " + slug)
    entries = data["entries"]
    require(isinstance(entries, list) and bool(entries), "Empty category: " + slug)
    for entry in entries:
        try:
            validate_entry(entry, slug, chapter_ids)
        except (ValueError, TypeError) as exc:
            label = entry.get("id", "?") if isinstance(entry, dict) else "?"
            raise ValueError(f"{slug}/{label}: {exc}") from exc
    return entries

def load_catalog(root, paths, modules):
    registry = categories(root)
    require(REGISTRY in paths, "Untracked category registry")
    chapter_ids = {m["slug"] + "/" + c for m in modules for c in m["chapters"] if m["slug"] != MODULE}
    expected = {f"{MODULE}/{item['slug']}/catalog.json" for item in registry}
    actual = {p for p in paths if p.startswith(MODULE + "/") and p.endswith(".json")}
    require(actual == expected, "Missing or unregistered catalog files")
    module = next(m for m in modules if m["slug"] == MODULE)
    require(module["chapters"] == [item["slug"] for item in registry], "Catalog curriculum mismatch")
    grouped = [(item, load_category(root, item, chapter_ids)) for item in registry]
    entries = [entry for _, records in grouped for entry in records]
    require(len(entries) >= MINIMUM, "Catalog contains fewer than 101 entries")
    require(len({e["id"] for e in entries}) == len(entries), "Duplicate catalog ID")
    require(len({" ".join(e["command"].split()) for e in entries}) == len(entries), "Duplicate command or operation")
    for entry in entries:
        for chapter in entry["related_chapters"]:
            for suffix in SUFFIX.values():
                require(f"{chapter}/README{suffix}.md" in paths, "Missing related chapter locale")
    return grouped
