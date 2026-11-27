"""Integration contract positive and negative fixtures. No snapshot code execution."""
import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from scripts import learning_hub_contract as c
from scripts import learning_hub_consumer as consumer
from scripts import validate as v


class ManifestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.paths = v.tracked_paths(v.ROOT)
        cls.baseline = c.validate_manifest(v.ROOT, cls.paths)
        temp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(temp.cleanup)
        cls.root = Path(temp.name).resolve()
        # Only tracked source files are copied; never import them.
        for path in cls.paths:
            dest = cls.root / path
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(v.ROOT / path, dest)

    def test_inventory(self):
        modules = self.baseline["modules"]
        chapters = [ch for m in modules for ch in m["chapters"]]
        self.assertEqual(len(modules), 18)
        self.assertEqual(len(chapters), 141)
        self.assertEqual(len({ch["id"] for ch in chapters}), 141)
        self.assertEqual(len({p for ch in chapters for p in ch["content"].values()}), 423)
        self.assertIsNone(chapters[0]["previous_id"])
        self.assertIsNone(chapters[-1]["next_id"])
        for a, b in zip(chapters, chapters[1:]):
            self.assertEqual(a["next_id"], b["id"])
            self.assertEqual(b["previous_id"], a["id"])
        self.assertIn("learning-hub-contract", v.CHECKS)

    def test_typed_associations(self):
        chapters = [ch for m in self.baseline["modules"] for ch in m["chapters"]]
        for field, expected in (("quiz_ids", 36), ("exercise_ids", 12), ("interview_ids", 24),
                                ("mock_ids", 3), ("command_ids", 120)):
            self.assertEqual(len({i for ch in chapters for i in ch[field]}), expected)
        self.assertEqual(sum(ch["execution"] == "local_only" for ch in chapters), 9)
        self.assertTrue(all(ch["execution"] != "browser_compatible" for ch in chapters))

    def test_bad_manifest_rejected(self):
        def chapter(data):
            return data["modules"][0]["chapters"][0]
        cases = (
            lambda m: m.update(schema_version="2.0.0"),
            lambda m: m.update(association_status="pending"),
            lambda m: chapter(m)["content"].update(en="../outside"),
            lambda m: chapter(m)["title"].pop("es"),
            lambda m: m["modules"][0]["chapters"][1].update(id=chapter(m)["id"]),
            lambda m: chapter(m)["quiz_ids"].append("quiz-missing"),
            lambda m: chapter(m).update(next_id=None),
            lambda m: chapter(m).update(execution="browser_compatible"),
            lambda m: chapter(m).update(order=False),
            lambda m: m["banks"]["quizzes"].update(schema_version=True),
        )
        target = self.root / c.MANIFEST
        original = target.read_bytes()
        try:
            for i, mutate in enumerate(cases):
                with self.subTest(case=i):
                    data = copy.deepcopy(self.baseline)
                    mutate(data)
                    target.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
                    with self.assertRaises(ValueError):
                        c.validate_manifest(self.root, self.paths)
        finally:
            target.write_bytes(original)
        self.assertEqual(c.validate_manifest(self.root, self.paths), self.baseline)

    def test_missing_path(self):
        paths = self.paths - {self.baseline["modules"][0]["chapters"][0]["content"]["es"]}
        with self.assertRaises(ValueError):
            c.validate_manifest(self.root, paths)

    def test_strict_json_and_paths(self):
        for value in ('{"a":1,"a":2}', '{"a":NaN}', '{"a":Infinity}', '{"a":1.0}'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                c.strict_json(value)
        for p in ("../x", "/x", "C:/x", "x\\y", "x/%2e%2e/y", "x/.GIT/config", "x/CON.txt", "x//y"):
            self.assertFalse(c.safe_path(p), p)
        self.assertTrue(c.safe_path("getting-started/01-install-git/README.pt-BR.md"))

    def test_current_immutable_revision_consumer(self):
        # The caller supplies the full checked-out revision externally, never from the manifest.
        revision = consumer.git(v.ROOT, "rev-parse", "HEAD").strip().decode("ascii")
        lock = json.dumps({**consumer.LOCK, "revision": revision})
        loaded = consumer.consume(v.ROOT, lock)
        self.assertEqual(loaded["revision"], revision)
        self.assertEqual(loaded["manifest"], self.baseline)


    def test_consumer_rejects_unsupported_schema_contents(self):
        with tempfile.TemporaryDirectory() as temp:
            trusted = Path(temp)
            (trusted / "schemas").mkdir()
            for name in c.SCHEMAS:
                path = "schemas/" + name + ".schema.json"
                shutil.copyfile(v.ROOT / path, trusted / path)
            target = trusted / "schemas/curriculum-manifest.schema.json"
            data = c.strict_json(target.read_text(encoding="utf-8"))
            data["title"] = "Unsupported schema"
            target.write_text(json.dumps(data), encoding="utf-8")
            revision = consumer.git(v.ROOT, "rev-parse", "HEAD").strip().decode("ascii")
            with self.assertRaisesRegex(ValueError, "Unsupported schema contents"):
                consumer.consume(v.ROOT, json.dumps({**consumer.LOCK, "revision": revision}), trusted)


class SnapshotTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name).resolve()
        self.repo = self.root / "repo"
        self.repo.mkdir()
        self.git("init", "-b", "main")
        self.git("config", "user.name", "Study Guide Example")
        self.git("config", "user.email", "learner@example.invalid")
        self.git("config", "commit.gpgsign", "false")
        self.git("config", "core.autocrlf", "false")
        self.git("config", "core.hooksPath", str(self.root / "no-hooks"))
        self.git("config", "core.fsmonitor", "false")
        self.first = self.commit(b"first\n")
        self.second = self.commit(b"second\n")

    def git(self, *args, input_bytes=None):
        return consumer.git(self.repo, *args, input_bytes=input_bytes)

    def commit(self, data):
        (self.repo / "notes.txt").write_bytes(data)
        self.git("add", "notes.txt")
        self.git("commit", "-m", "docs: update notes")
        return self.git("rev-parse", "HEAD").strip().decode("ascii")

    def export(self, revision, name):
        root = self.root / name
        root.mkdir()
        inventory = consumer.tree_inventory(self.repo, revision)
        consumer.export_snapshot(self.repo, inventory, root)
        consumer.verify_stage(root, inventory)
        return root, inventory

    def test_pinned_update_and_rollback(self):
        first, inv = self.export(self.first, "first")
        second, _ = self.export(self.second, "second")
        self.assertEqual((first / "notes.txt").read_bytes(), b"first\n")
        self.assertEqual((second / "notes.txt").read_bytes(), b"second\n")
        rolled, rolled_inv = self.export(self.first, "rollback")
        self.assertEqual(rolled_inv, inv)
        self.assertEqual((rolled / "notes.txt").read_bytes(), b"first\n")
        # A working-tree edit is not part of either pinned commit.
        (self.repo / "notes.txt").write_bytes(b"uncommitted\n")
        old, _ = self.export(self.first, "old")
        self.assertEqual((old / "notes.txt").read_bytes(), b"first\n")

    def test_mixed_missing_and_extra_stage(self):
        root, inv = self.export(self.first, "stage")
        path = root / "notes.txt"
        path.write_bytes(b"second\n")
        with self.assertRaises(ValueError):
            consumer.verify_stage(root, inv)
        path.unlink()
        with self.assertRaises(ValueError):
            consumer.verify_stage(root, inv)
        path.write_bytes(b"first\n")
        (root / "extra.txt").write_bytes(b"extra\n")
        with self.assertRaises(ValueError):
            consumer.verify_stage(root, inv)

    def test_extra_directory_and_unsafe_export(self):
        root, inv = self.export(self.first, "stage")
        (root / "unexpected").mkdir()
        with self.assertRaises(ValueError):
            consumer.verify_stage(root, inv)
        empty = self.root / "empty"
        empty.mkdir()
        with self.assertRaises(ValueError):
            consumer.export_snapshot(self.repo, {"../escape.txt": inv["notes.txt"]}, empty)
        self.assertFalse((self.root / "escape.txt").exists())

    def test_invalid_revision_and_lock(self):
        for rev in ("main", self.first[:12], "0"*40):
            with self.subTest(rev=rev), self.assertRaises(ValueError):
                consumer.tree_inventory(self.repo, rev)
        valid = {**consumer.LOCK, "revision": self.first}
        self.assertEqual(consumer.read_lock(json.dumps(valid)), valid)
        for field, value in (("manifest_version", "2.0.0"), ("assessment_version", True),
                             ("command_catalog_version", 2), ("revision", "main")):
            with self.subTest(field=field), self.assertRaises(ValueError):
                consumer.read_lock(json.dumps({**valid, field: value}))

    def test_symbolic_tree_entry_rejected(self):
        oid = self.git("hash-object", "-w", "--stdin", input_bytes=b"notes.txt").strip().decode("ascii")
        self.git("update-index", "--add", "--cacheinfo", "120000," + oid + ",link.txt")
        self.git("commit", "-m", "test: symbolic entry")
        revision = self.git("rev-parse", "HEAD").strip().decode("ascii")
        with self.assertRaises(ValueError):
            consumer.tree_inventory(self.repo, revision)


if __name__ == "__main__":
    unittest.main()
