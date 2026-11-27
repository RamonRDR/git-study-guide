"""Negative fixtures for the internal catalog; no command execution."""
import json
import tempfile
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import command_catalog as cc
import render_command_reference as render
from scripts import validate as validator

CATEGORY = "01-setup-and-configuration"
CHAPTER = "basic-commands/01-init-config-help"

def localized(text="Example text"):
    return {locale: text for locale in cc.LOCALES}

def entry():
    value = {key: localized() for key in cc.LOCAL_FIELDS}
    value.update(id="git-status", command="git status", kind="native-command",
                 category=CATEGORY, level="beginner", intent_tags=["inspect"],
                 syntax="git status", effects={key: "unchanged" for key in cc.EFFECT_KEYS},
                 risk={"class": "read-only", "notes": localized()},
                 related_chapters=[CHAPTER], references=["https://git-scm.com/docs/git-status"],
                 examples={key: {"command": "git status", "context": localized()} for key in ("basic", "professional")})
    return value

class CommandEntryTests(unittest.TestCase):
    def test_catalog_check_registered(self):
        self.assertIn("command-catalog", validator.CHECKS)
        with tempfile.TemporaryDirectory() as directory:
            errors = validator.check_command_catalog(Path(directory), set())
            self.assertTrue(any(error.startswith("Invalid command catalog:") for error in errors))

    def validate(self, value):
        cc.validate_entry(value, CATEGORY, {CHAPTER})

    def test_valid(self):
        self.validate(entry())

    def test_missing_required_field(self):
        value = entry()
        del value["purpose"]
        with self.assertRaises(ValueError):
            self.validate(value)

    def test_missing_locale(self):
        value = entry()
        del value["purpose"]["es"]
        with self.assertRaises(ValueError):
            self.validate(value)

    def test_extra_locale(self):
        value = entry()
        value["purpose"]["fr"] = "Unexpected"
        with self.assertRaises(ValueError):
            self.validate(value)

    def test_empty_locale(self):
        value = entry()
        value["purpose"]["en"] = " "
        with self.assertRaises(ValueError):
            self.validate(value)

    def test_invalid_id(self):
        value = entry()
        value["id"] = "../invalid"
        with self.assertRaises(ValueError):
            self.validate(value)

    def test_id_rejects_dot_for_stable_github_anchor(self):
        value = entry()
        value["id"] = "git.status"
        with self.assertRaises(ValueError):
            self.validate(value)

    def test_invalid_category(self):
        value = entry()
        value["category"] = "other"
        with self.assertRaises(ValueError):
            self.validate(value)

    def test_invalid_kind(self):
        value = entry()
        value["kind"] = "unknown"
        with self.assertRaises(ValueError):
            self.validate(value)

    def test_invalid_level(self):
        value = entry()
        value["level"] = "unknown"
        with self.assertRaises(ValueError):
            self.validate(value)

    def test_duplicate_intent(self):
        value = entry()
        value["intent_tags"] = ["inspect", "inspect"]
        with self.assertRaises(ValueError):
            self.validate(value)

    def test_invalid_effect(self):
        value = entry()
        value["effects"]["history"] = "unknown"
        with self.assertRaises(ValueError):
            self.validate(value)

    def test_inconsistent_read_only(self):
        value = entry()
        value["effects"]["history"] = "changes"
        with self.assertRaises(ValueError):
            self.validate(value)

    def test_invalid_risk(self):
        value = entry()
        value["risk"]["class"] = "unknown"
        with self.assertRaises(ValueError):
            self.validate(value)

    def test_dangling_chapter(self):
        value = entry()
        value["related_chapters"] = ["basic-commands/99-missing"]
        with self.assertRaises(ValueError):
            self.validate(value)

    def test_unofficial_reference(self):
        value = entry()
        value["references"] = ["https://example.invalid/docs"]
        with self.assertRaises(ValueError):
            self.validate(value)

    def test_missing_professional_example(self):
        value = entry()
        del value["examples"]["professional"]
        with self.assertRaises(ValueError):
            self.validate(value)

    def test_duplicate_json_keys(self):
        with self.assertRaises(ValueError):
            cc.unique_keys([("id", "a"), ("id", "b")])

class CatalogIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.paths = set()
        self.registry = cc.categories(render.ROOT)
        self.intent_labels = {"inspect": localized("Inspect")}
        self.write(cc.REGISTRY, {"schema_version": 1, "categories": self.registry})
        self.write(cc.INTENT_REGISTRY, {"schema_version": 1, "intents": self.intent_labels})
        self.modules = [
            {"slug": "basic-commands", "chapters": ["01-init-config-help"]},
            {"slug": cc.MODULE, "chapters": [c["slug"] for c in self.registry]},
            {"slug": "practical-projects", "chapters": []},
        ]
        self.paths.update(CHAPTER + "/README" + suffix + ".md" for suffix in cc.SUFFIX.values())
        self.records = {}
        n = 0
        for item in self.registry:
            slug = item["slug"]
            records = []
            for _ in range(item["target"]):
                n += 1
                record = entry()
                record.update(id=f"fixture-{n}", command=f"git fixture-{n}", category=slug)
                records.append(record)
            self.records[slug] = records
            self.save(slug)

    def write(self, path, data):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        self.paths.add(path)

    def save(self, slug):
        self.write(f"{cc.MODULE}/{slug}/catalog.json",
                   {"schema_version": 1, "category": slug, "entries": self.records[slug]})

    def load(self):
        return cc.load_catalog(self.root, self.paths, self.modules)

    def test_valid_catalog_count(self):
        self.assertEqual(sum(len(records) for _, records in self.load()), 120)

    def test_catalog_below_minimum(self):
        for slug in self.records:
            self.records[slug] = self.records[slug][:7]
            self.save(slug)
        with self.assertRaisesRegex(ValueError, "fewer than 101"):
            self.load()

    def test_category_below_target(self):
        slug = self.registry[0]["slug"]
        self.records[slug].pop()
        self.save(slug)
        with self.assertRaisesRegex(ValueError, "Category below approved target"):
            self.load()

    def test_unregistered_uppercase_catalog(self):
        self.paths.add(f"{cc.MODULE}/99-invalid/catalog.JSON")
        with self.assertRaisesRegex(ValueError, "Missing or unregistered"):
            self.load()

    def test_duplicate_id(self):
        slug = self.registry[1]["slug"]
        self.records[slug][0]["id"] = self.records[self.registry[0]["slug"]][0]["id"]
        self.save(slug)
        with self.assertRaisesRegex(ValueError, "Duplicate catalog ID"):
            self.load()

    def test_duplicate_command(self):
        slug = self.registry[1]["slug"]
        self.records[slug][0]["command"] = self.records[self.registry[0]["slug"]][0]["command"]
        self.save(slug)
        with self.assertRaisesRegex(ValueError, "Duplicate command"):
            self.load()

    def test_missing_catalog(self):
        self.paths.remove(f"{cc.MODULE}/{self.registry[0]['slug']}/catalog.json")
        with self.assertRaisesRegex(ValueError, "Missing or unregistered"):
            self.load()

    def test_unregistered_catalog(self):
        self.paths.add(f"{cc.MODULE}/99-invalid/catalog.json")
        with self.assertRaisesRegex(ValueError, "Missing or unregistered"):
            self.load()

    def test_missing_chapter_locale(self):
        self.paths.remove(CHAPTER + "/README.es.md")
        with self.assertRaisesRegex(ValueError, "Missing related chapter locale"):
            self.load()

    def test_unregistered_intent(self):
        slug = self.registry[0]["slug"]
        self.records[slug][0]["intent_tags"] = ["unregistered"]
        self.save(slug)
        with self.assertRaisesRegex(ValueError, "Unregistered intent"):
            self.load()

    def test_curriculum_mismatch(self):
        self.modules[1]["chapters"].pop()
        with self.assertRaisesRegex(ValueError, "curriculum mismatch"):
            self.load()

    def test_generated_pages_deterministic_and_stale(self):
        grouped = self.load()
        output = render.render_all(grouped, self.modules, self.intent_labels)
        self.assertEqual(len(output), 45)
        self.assertEqual(output, render.render_all(grouped, self.modules, self.intent_labels))
        for path, text in output.items():
            target = self.root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text, encoding="utf-8")
            self.paths.add(path)
        self.assertEqual(render.compare_generated(self.root, self.paths, output), [])
        path = cc.MODULE + "/README.es.md"
        (self.root / path).write_text("stale", encoding="utf-8")
        self.assertEqual(render.compare_generated(self.root, self.paths, output),
                         ["Stale generated catalog page: " + path])
