"""Validate the internal assessment pilot and representative malformed records."""
import copy
import unittest
from pathlib import Path

from scripts import assessment_pilot as p
from scripts import render_assessments as renderer
from scripts import validate as v

ROOT = Path(__file__).resolve().parents[1]


class AssessmentPilotTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.modules = v.load_modules(ROOT)
        cls.chapters = {m["slug"] + "/" + c for m in cls.modules
                        if m["slug"] != "exercises" for c in m["chapters"]}
        cls.paths = v.tracked_paths(ROOT)
        cls.banks = p.load_assessments(ROOT, cls.paths, cls.modules)

    def test_all_banks_and_rendering(self):
        self.assertEqual([len(x) for x in self.banks.values()], [36, 12, 24, 3])
        self.assertEqual(renderer.check_assessments(ROOT, self.paths), [])
        self.assertIn("assessment-pilot", v.CHECKS)

    def test_all_quiz_choices(self):
        for quiz in self.banks["01-quizzes"]:
            with self.subTest(quiz=quiz["id"]):
                for choice in quiz["choices"]:
                    self.assertEqual(p.grade_quiz(quiz, choice["id"]), choice["id"] == quiz["answer"])
                self.assertFalse(p.grade_quiz(quiz, None))
                self.assertFalse(p.grade_quiz(quiz, "unknown"))

    def test_bad_answer(self):
        q = copy.deepcopy(self.banks["01-quizzes"][0])
        q["answer"] = "unknown"
        with self.assertRaises(ValueError):
            p.validate_record(q, "quiz", self.chapters)

    def test_duplicate_choices(self):
        q = copy.deepcopy(self.banks["01-quizzes"][0])
        q["choices"][1]["id"] = q["choices"][0]["id"]
        with self.assertRaises(ValueError):
            p.validate_record(q, "quiz", self.chapters)

    def test_missing_locale(self):
        q = copy.deepcopy(self.banks["01-quizzes"][0])
        del q["prompt"]["es"]
        with self.assertRaises(ValueError):
            p.validate_record(q, "quiz", self.chapters)

    def test_unknown_prerequisite(self):
        q = copy.deepcopy(self.banks["01-quizzes"][0])
        q["prerequisites"] = ["../outside"]
        with self.assertRaises(ValueError):
            p.validate_record(q, "quiz", self.chapters)

    def test_unsafe_state_checks(self):
        for c in ({"kind": "shell", "command": "git status"},
                  {"kind": "work-content", "file": "../notes.txt", "value": "status: ready"},
                  {"kind": "same-ref", "left": "--help", "right": "main"},
                  {"kind": "commit-count", "value": True},
                  {"kind": "clean", "extra": "unexpected"}):
            with self.subTest(check=c):
                self.assertFalse(p.valid_check(c))

    def test_no_unregistered_bank(self):
        with self.assertRaises(ValueError):
            p.load_assessments(ROOT, self.paths | {"exercises/other.json"}, self.modules)

    def test_mock_references_and_rubrics(self):
        for mock in self.banks["04-mock-assessments"]:
            self.assertEqual([len(mock[key]) for key in ("quiz_ids", "challenge_ids", "interview_ids")],
                             [4, 1, 2])
            self.assertEqual(len(mock["rubric"]), 3)
        for interview in self.banks["03-interviews"]:
            self.assertEqual(len(interview["rubric"]), 2)


if __name__ == "__main__":
    unittest.main()
