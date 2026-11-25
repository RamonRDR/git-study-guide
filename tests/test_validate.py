"""Positive and negative fixtures; no operations on the guide repository."""
import json
from pathlib import Path
import tempfile
import unittest
from scripts import validate as v

class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.paths = set()

    def write(self, path, text):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        self.paths.add(path)

    def test_locale_complete(self):
        self.assertEqual(v.check_locales(set(v.locale_group("README.md"))), [])

    def test_locale_missing(self):
        self.assertIn("Missing locale: docs/localized/README.es.md", v.check_locales({"README.md", "docs/localized/README.pt-BR.md"}))

    def test_locale_unexpected_name(self):
        self.assertTrue(v.check_locales({"docs/topic.en.md", "docs/topic.md", "docs/topic.pt-BR.md", "docs/topic.es.md"}))

    def test_paths(self):
        for path in ("../x", "/x", "x\\y", "C:/x", "x/../y", "x/CON.txt", "x//y"):
            with self.subTest(path=path):
                self.assertFalse(v.portable_path(path))
        self.assertTrue(v.portable_path("docs/README.pt-BR.md"))

    def test_link_resolution(self):
        self.assertEqual(v.resolve_link("docs/a.md", "../README.md#title"), "README.md")
        self.assertIsNone(v.resolve_link("docs/a.md", "https://example.com"))
        self.assertIsNone(v.resolve_link("docs/a.md", "#title"))
        with self.assertRaises(ValueError):
            v.resolve_link("docs/a.md", "../../outside")

    def test_broken_link(self):
        self.write("docs/a.md", "[good](../LICENSE)\n[bad](missing.md)")
        self.write("LICENSE", "test")
        self.assertEqual(v.check_links(self.root, self.paths), ["Broken local link: docs/a.md -> docs/missing.md"])

    def test_fenced_code_ignored(self):
        self.write("docs/a.md", chr(96)*3 + "\n[example](missing.md)\n" + chr(96)*3)
        self.assertEqual(v.check_links(self.root, self.paths), [])

    def test_structure_case_collision(self):
        self.write("docs/A.md", "")
        # Paths are tested even on a case-insensitive filesystem.
        self.paths.add("docs/a.md")
        self.assertTrue(any("Case-colliding" in e for e in v.check_structure(self.root, self.paths)))

    def test_manifest_order(self):
        self.write("scripts/curriculum.json", json.dumps({"modules": [{"slug": s, "chapters": []} for s in v.SLUGS]}))
        self.assertEqual(len(v.load_modules(self.root)), 18)
        self.write("scripts/curriculum.json", json.dumps({"modules": []}))
        with self.assertRaises(ValueError):
            v.load_modules(self.root)

    def test_chapter_duplicate_number(self):
        modules = [{"slug": s, "chapters": []} for s in v.SLUGS]
        modules[0]["chapters"] = ["01-start", "01-next"]
        self.write("scripts/curriculum.json", json.dumps({"modules": modules}))
        with self.assertRaises(ValueError):
            v.load_modules(self.root)

    def test_navigation_block(self):
        text = "<!-- navigation -->\n[Previous](../a/README.md) · [Index](README.md)\n<!-- /navigation -->"
        self.assertEqual(v.block_targets(text, "navigation", "b/README.md"), ["a/README.md", "b/README.md"])
        with self.assertRaises(ValueError):
            v.block_targets(text + text, "navigation", "b/README.md")

    def test_missing_navigation(self):
        self.write("scripts/curriculum.json", json.dumps({"modules": [{"slug": s, "chapters": []} for s in v.SLUGS]}))
        self.write("getting-started/README.md", "# No navigation")
        self.assertIn("Invalid navigation block: getting-started/README.md", v.check_navigation(self.root, self.paths))

    def test_examples_unapproved(self):
        self.write("scripts/example_manifest.json", "[]")
        self.assertEqual(v.check_examples(self.root, self.paths), [])
        self.write("getting-started/examples/run.sh", "echo safe")
        self.assertTrue(v.check_examples(self.root, self.paths))
        self.write("scripts/example_manifest.json", '["getting-started/examples/run.sh"]')
        self.assertTrue(v.check_examples(self.root, self.paths))

    def test_secret_redaction(self):
        synthetic = "gh" + "p_" + "A" * 36
        self.write("docs/a.md", synthetic)
        errors = v.check_secrets(self.root, self.paths)
        self.assertEqual(errors, ["Potential secret: docs/a.md:1"])
        self.assertNotIn(synthetic, str(errors))

    def test_secret_file(self):
        self.write("docs/.env", "example")
        self.assertTrue(v.check_secrets(self.root, self.paths))

if __name__ == "__main__":
    unittest.main()
