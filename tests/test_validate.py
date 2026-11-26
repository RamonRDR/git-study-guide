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

    def test_structure_file_directory_collision(self):
        self.write("scripts/curriculum.json", "{}")
        # Synthetic tracked paths avoid creating an impossible layout on Windows.
        self.paths.add("scripts/Curriculum.json/notes.txt")
        self.assertTrue(any("Case-colliding" in e and "directory" in e and "file" in e
                            for e in v.check_structure(self.root, self.paths)))

    def test_structure_directory_case_collision(self):
        self.paths.update({"docs/Topic/a.md", "docs/topic/b.md"})
        self.assertTrue(any("Case-colliding" in e and "directory" in e
                            for e in v.check_structure(self.root, self.paths)))

    def test_structure_shared_directory_allowed(self):
        self.write("docs/topic/a.md", "")
        self.write("docs/topic/b.md", "")
        self.assertFalse(any("Case-colliding" in e
                             for e in v.check_structure(self.root, self.paths)))

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

    def test_examples_reject_all_files_until_protocol(self):
        self.write("scripts/example_manifest.json", "[]")
        for path, content in (
            ("getting-started/examples/run.bash", "#!/bin/sh\necho test"),
            ("getting-started/examples/run.txt", "#!/bin/sh\necho test"),
            ("getting-started/examples/unknown.xyz", "test"),
            ("getting-started/examples/notes.txt", "inert text"),
            ("getting-started/Examples/run.txt", "test"),
        ):
            with self.subTest(path=path):
                self.write(path, content)
                self.assertIn("Unapproved example file: " + path,
                              v.check_examples(self.root, self.paths))

    def test_secret_redaction(self):
        synthetic = "gh" + "p_" + "A" * 36
        self.write("docs/a.md", synthetic)
        errors = v.check_secrets(self.root, self.paths)
        self.assertEqual(errors, ["Potential secret: docs/a.md:1"])
        self.assertNotIn(synthetic, str(errors))

    def test_secret_file(self):
        self.write("docs/.env", "example")
        self.assertTrue(v.check_secrets(self.root, self.paths))

    def navigation_fixture(self):
        """All reserved modules plus chapters at the beginning, boundary and end."""
        modules = [{"slug": s, "chapters": []} for s in v.SLUGS]
        modules[0]["chapters"] = ["01-start", "02-finish"]
        modules[1]["chapters"] = ["01-only"]
        modules[-1]["chapters"] = ["01-final"]
        self.write("scripts/curriculum.json", json.dumps({"modules": modules}))
        for suffix in v.SUFFIXES:
            readme = "README" + suffix + ".md"
            index = "docs/learning-path" + suffix + ".md"
            self.write(index, "\n".join(
                "[Module](../" + m["slug"] + "/" + readme + ")" for m in modules))
            for document, entries, chapters in v.navigation_entries(modules, suffix):
                line = v.navigation_line(document, entries)
                selector = " · ".join(
                    "[Language](" + Path(p).name + ")" for p in v.locale_group(document))
                body = "# Title\n\n" + selector + "\n\n"
                body += "<!-- navigation -->\n" + line + "\n<!-- /navigation -->\n\n"
                body += "Lesson text.\n"
                if chapters is not None:
                    body += "\n<!-- chapters -->\n"
                    body += "\n".join("[Chapter](" + c.split("/", 1)[1] + ")" for c in chapters)
                    body += "\n<!-- /chapters -->\n"
                body += "\n---\n\n<!-- navigation-footer -->\n" + line
                body += "\n<!-- /navigation-footer -->\n"
                self.write(document, body)
        return modules

    def test_navigation_continuous_all_locales(self):
        self.navigation_fixture()
        self.assertEqual(v.check_navigation(self.root, self.paths), [])
        cases = (
            ("getting-started/01-start/README.md",
             "— · [Index](../README.md) · [Next](../02-finish/README.md)"),
            ("getting-started/02-finish/README.pt-BR.md",
             "[Anterior](../01-start/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo módulo](../../fundamentals/README.pt-BR.md)"),
            ("fundamentals/01-only/README.es.md",
             "[Módulo anterior](../../getting-started/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../git-architecture/README.es.md)"),
            ("exercises/01-final/README.md",
             "[Previous module](../../practical-projects/README.md) · [Index](../README.md) · —"),
            ("git-architecture/README.pt-BR.md",
             "[Anterior](../fundamentals/README.pt-BR.md) · [Índice](../docs/learning-path.pt-BR.md) · [Próximo](../basic-commands/README.pt-BR.md)"),
        )
        for path, expected in cases:
            with self.subTest(path=path):
                content = v.read_text(self.root, path)
                self.assertEqual(v.navigation_body(content, "navigation"), expected)
                self.assertEqual(v.navigation_body(content, "navigation-footer"), expected)

    def test_navigation_missing_footer(self):
        self.navigation_fixture()
        path = "getting-started/01-start/README.md"
        content = v.read_text(self.root, path)
        self.write(path, content.split("<!-- navigation-footer -->")[0])
        self.assertIn("Invalid navigation block: " + path, v.check_navigation(self.root, self.paths))

    def test_navigation_divergent_footer(self):
        self.navigation_fixture()
        path = "getting-started/02-finish/README.pt-BR.md"
        content = v.read_text(self.root, path)
        top, footer = content.split("<!-- navigation-footer -->")
        self.write(path, top + "<!-- navigation-footer -->" +
                   footer.replace("../../fundamentals/README.pt-BR.md", "../../fundamentals/README.md"))
        self.assertIn("Incorrect footer navigation: " + path, v.check_navigation(self.root, self.paths))

    def test_navigation_wrong_boundary_both_blocks(self):
        self.navigation_fixture()
        path = "fundamentals/01-only/README.es.md"
        content = v.read_text(self.root, path)
        self.write(path, content.replace("../../git-architecture/README.es.md",
                                         "../../branches/README.es.md"))
        errors = v.check_navigation(self.root, self.paths)
        self.assertIn("Incorrect navigation: " + path, errors)
        self.assertIn("Incorrect footer navigation: " + path, errors)

    def test_navigation_language_and_order(self):
        self.navigation_fixture()
        path = "getting-started/02-finish/README.pt-BR.md"
        content = v.read_text(self.root, path)
        self.write(path, content.replace("README.pt-BR.md) · [Índice]", "README.es.md) · [Índice]"))
        self.assertIn("Incorrect navigation: " + path, v.check_navigation(self.root, self.paths))
        line = v.navigation_body(content, "navigation")
        self.write(path, content.replace(line, " · ".join(reversed(line.split(" · ")))))
        self.assertIn("Incorrect navigation: " + path, v.check_navigation(self.root, self.paths))

    def test_navigation_duplicate_and_reversed_footer(self):
        self.navigation_fixture()
        path = "getting-started/README.md"
        content = v.read_text(self.root, path)
        footer = "<!-- navigation-footer -->" + content.split("<!-- navigation-footer -->")[1]
        for changed in (content + footer, content.replace("<!-- navigation-footer -->", "<!-- swap -->")
                        .replace("<!-- /navigation-footer -->", "<!-- navigation-footer -->")
                        .replace("<!-- swap -->", "<!-- /navigation-footer -->")):
            self.write(path, changed)
            self.assertIn("Invalid navigation block: " + path, v.check_navigation(self.root, self.paths))

    def test_navigation_footer_must_end_page(self):
        self.navigation_fixture()
        path = "getting-started/README.md"
        content = v.read_text(self.root, path)
        for extra in ("More content.\n", chr(96) * 3 + "\nexample\n" + chr(96) * 3 + "\n"):
            self.write(path, content + extra)
            self.assertIn("Incorrect navigation footer placement: " + path,
                          v.check_navigation(self.root, self.paths))

    def test_navigation_footer_in_fence(self):
        self.navigation_fixture()
        path = "getting-started/README.md"
        content = v.read_text(self.root, path)
        self.write(path, content.replace("<!-- navigation-footer -->",
                         chr(96) * 3 + "\n<!-- navigation-footer -->") + chr(96) * 3 + "\n")
        self.assertIn("Invalid navigation block: " + path, v.check_navigation(self.root, self.paths))

    def test_navigation_header_placement(self):
        self.navigation_fixture()
        path = "getting-started/README.md"
        content = v.read_text(self.root, path)
        self.write(path, content.replace("<!-- navigation -->", "Extra text.\n\n<!-- navigation -->"))
        self.assertIn("Incorrect navigation header placement: " + path,
                      v.check_navigation(self.root, self.paths))

if __name__ == "__main__":
    unittest.main()
