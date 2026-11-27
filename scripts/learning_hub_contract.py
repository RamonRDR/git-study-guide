"""Trusted, dependency-free authoring and consumer validation for Git manifest v1."""
import argparse
import json
import re
from pathlib import Path, PurePosixPath

if __package__:
    from . import validate as v
    from . import command_catalog as catalog
    from . import assessment_pilot as assessments
else:
    import validate as v
    import command_catalog as catalog
    import assessment_pilot as assessments

MANIFEST = "curriculum/manifest.json"
VERSION = "1.0.0"
LOCALES = ("en", "pt-BR", "es")
SUFFIX = dict(zip(LOCALES, ("", ".pt-BR", ".es")))
SCHEMAS = ("curriculum-manifest", "assessment-bank", "command-catalog", "revision-lock")
BANKS = {"quizzes": ("01-quizzes", "quiz_ids"), "exercises": ("02-challenges", "exercise_ids"),
         "interviews": ("03-interviews", "interview_ids"), "mocks": ("04-mock-assessments", "mock_ids")}
REASON = {"en": "Native Git practice requires an isolated local Git environment; browser execution is not verified.",
          "pt-BR": "Prática Git nativa exige ambiente Git local isolado; execução no navegador não verificada.",
          "es": "Práctica Git nativa requiere entorno Git local aislado; ejecución en navegador no verificada."}
IMAGE_SUFFIXES = {".svg", ".png", ".jpg", ".jpeg", ".webp"}
ENTRY = re.compile(r"^- (?:\d{2} )?\[([^\]\n]+)\]\(([^)]+)\)(?: \(\d+\))?$")


def fail(message):
    raise ValueError(message)


def strict_json(text):
    return json.loads(text, object_pairs_hook=catalog.unique_keys,
                      parse_constant=lambda _: fail("Non-finite JSON number"),
                      parse_float=lambda _: fail("Fractional JSON numbers are unsupported"))


def canonical(value):
    # Unlike Python object equality, this distinguishes true from 1.
    return json.dumps(value, sort_keys=True, ensure_ascii=False, allow_nan=False, separators=(",", ":"))


def safe_path(path):
    return (v.portable_path(path) and
            all(re.fullmatch(r"[A-Za-z0-9_.-]+", p) and p.casefold() != ".git"
                for p in path.split("/")))


def checked_file(root, paths, path):
    catalog.require(safe_path(path) and path in paths, "Unsafe or untracked source path: " + str(path))
    target = root / path
    catalog.require(target.is_file() and not target.is_symlink() and
                    all(not p.is_symlink() for p in target.parents if p != root and root in p.parents),
                    "Missing or symbolic source path: " + path)
    return target


def json_file(root, paths, path):
    return strict_json(checked_file(root, paths, path).read_text(encoding="utf-8"))


def localized_path(prefix):
    return {locale: prefix + "/README" + suffix + ".md" for locale, suffix in SUFFIX.items()}


def index_titles(root, paths, module, order):
    titles, chapters = {}, {c: {} for c in module["chapters"]}
    for locale, path in localized_path(module["slug"]).items():
        text = checked_file(root, paths, path).read_text(encoding="utf-8")
        lines = text.splitlines()
        match = re.fullmatch(r"# " + str(order).zfill(2) + r" (.+)", lines[0]) if lines else None
        catalog.require(match is not None, "Invalid module title: " + path)
        titles[locale] = match[1]
        # Preserve the localized index label, excluding only the display number/count.
        catalog.require(text.count("<!-- chapters -->") == text.count("<!-- /chapters -->") == 1,
                        "Invalid chapter index: " + path)
        body = text.split("<!-- chapters -->", 1)[1].split("<!-- /chapters -->", 1)[0]
        entries = [ENTRY.fullmatch(line) for line in body.splitlines() if line.strip()]
        catalog.require(len(entries) == len(module["chapters"]) and all(entries),
                        "Invalid chapter entries: " + path)
        for slug, entry in zip(module["chapters"], entries):
            expected = slug + "/README" + SUFFIX[locale] + ".md"
            catalog.require(entry[2] == expected, "Wrong chapter path/order: " + path)
            chapters[slug][locale] = entry[1]
    catalog.require(catalog.locale_map(titles) and all(catalog.locale_map(t) for t in chapters.values()),
                    "Invalid localized titles")
    return titles, chapters


def expected_manifest(root, paths):
    root = root.resolve()
    # Validate strict JSON before passing the exact same files to trusted existing validators.
    json_file(root, paths, "scripts/curriculum.json")
    modules = v.load_modules(root)
    catalog.require(all(m["chapters"] for m in modules), "Empty module in published contract")
    for p in (catalog.REGISTRY, catalog.INTENT_REGISTRY):
        json_file(root, paths, p)
    for m in modules:
        if m["slug"] == "command-reference":
            for slug in m["chapters"]:
                json_file(root, paths, f"command-reference/{slug}/catalog.json")
    banks = {}
    for kind, (slug, _) in BANKS.items():
        path = f"exercises/{slug}/records.json"
        json_file(root, paths, path)
        banks[kind] = {"schema_version": 1, "records": path, "schema": "schemas/assessment-bank.schema.json"}
    for name in SCHEMAS:
        data = json_file(root, paths, "schemas/" + name + ".schema.json")
        catalog.require(isinstance(data, dict) and data.get("$schema") == "https://json-schema.org/draft/2020-12/schema",
                        "Unsupported structural schema")
    grouped_commands = catalog.load_catalog(root, paths, modules)
    grouped_assessments = assessments.load_assessments(root, paths, modules)
    for r in grouped_assessments["03-interviews"]:
        catalog.require(len(r["rubric"]) == 2, "Interview rubric count")
    for r in grouped_assessments["04-mock-assessments"]:
        catalog.require([len(r[k]) for k in ("quiz_ids", "challenge_ids", "interview_ids", "rubric")] == [4, 1, 2, 3],
                        "Mock scoring shape mismatch")
    categories = [{"id": category["slug"], "path": f"command-reference/{category['slug']}/catalog.json"}
                  for category, _ in grouped_commands]
    ids = [m["slug"] + "." + c for m in modules for c in m["chapters"]]
    catalog.require(len(ids) == len(set(ids)), "Duplicate chapter ID")
    manifest = {"schema_version": VERSION, "guide_id": "git-study-guide", "default_locale": "en",
                "supported_locales": list(LOCALES), "association_status": "complete",
                "assets": sorted(p for p in paths if p.startswith("assets/") and
                                 PurePosixPath(p).suffix.lower() in IMAGE_SUFFIXES),
                "banks": banks, "command_catalog": {"schema_version": 1, "registry": catalog.REGISTRY,
                "intent_registry": catalog.INTENT_REGISTRY, "schema": "schemas/command-catalog.schema.json",
                "categories": categories}, "modules": []}
    for path in manifest["assets"]:
        checked_file(root, paths, path)
    by_id = {}
    for order, m in enumerate(modules):
        slug = m["slug"]
        title, titles = index_titles(root, paths, m, order)
        item = {"id": slug, "order": order, "slug": slug, "title": title,
                "index": localized_path(slug), "chapters": []}
        for position, chapter in enumerate(m["chapters"]):
            id_ = slug + "." + chapter
            i = ids.index(id_)
            prefix = slug + "/" + chapter
            content = localized_path(prefix)
            for path in content.values():
                text = checked_file(root, paths, path).read_text(encoding="utf-8")
                catalog.require(text.startswith("# ") and bool(text.splitlines()[0][2:].strip()),
                                "Missing chapter heading: " + path)
            extra = sorted(p for p in paths if p.startswith(prefix + "/") and p not in content.values())
            for path in extra:
                checked_file(root, paths, path)
            assets = [p for p in extra if PurePosixPath(p).suffix.lower() in IMAGE_SUFFIXES]
            local_only = slug == "practical-projects" or (slug == "exercises" and chapter == "02-challenges")
            record = {"id": id_, "order": position, "slug": chapter,
                      "kind": {"command-reference": "reference", "practical-projects": "project",
                               "exercises": "assessment"}.get(slug, "lesson"),
                      "title": titles[chapter], "content": content, "assets": assets,
                      "resources": [p for p in extra if p not in assets],
                      "previous_id": ids[i-1] if i else None, "next_id": ids[i+1] if i+1 < len(ids) else None,
                      "exercise_ids": [], "quiz_ids": [], "interview_ids": [], "mock_ids": [], "command_ids": [],
                      "execution": "local_only" if local_only else "unverified"}
            if local_only:
                record["execution_reason"] = REASON.copy()
            by_id[id_] = record
            item["chapters"].append(record)
        manifest["modules"].append(item)
    def associate(id_, field, record):
        values = by_id[id_][field]
        if record not in values:
            values.append(record)
    for category, entries in grouped_commands:
        for entry in entries:
            for id_ in ["command-reference." + category["slug"]] + [
                    p.replace("/", ".") for p in entry["related_chapters"]]:
                associate(id_, "command_ids", entry["id"])
    for kind, (slug, field) in BANKS.items():
        for record in grouped_assessments[slug]:
            for id_ in ["exercises." + slug] + ([] if kind == "mocks" else [
                    p.replace("/", ".") for p in record["prerequisites"]]):
                associate(id_, field, record["id"])
    return manifest


def validate_manifest(root, paths):
    actual = json_file(root.resolve(), paths, MANIFEST)
    expected = expected_manifest(root, paths)
    catalog.require(canonical(actual) == canonical(expected),
                    "Manifest differs from validated source inventory/relationships")
    return actual


def check_manifest(root, paths):
    try:
        validate_manifest(root, paths)
    except (ValueError, OSError, TypeError, KeyError, IndexError, StopIteration) as exc:
        return ["Learning Hub contract: " + str(exc)]
    return []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    root = v.ROOT
    paths = v.tracked_paths(root)
    if args.write:
        data = expected_manifest(root, paths)
        target = root / MANIFEST
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        return 0
    errors = check_manifest(root, paths)
    for error in errors:
        print(error)
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
