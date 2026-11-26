"""Negative fixtures for the internal catalog; no command execution."""
import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import command_catalog as cc

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
