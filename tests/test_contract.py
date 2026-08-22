import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ContractTests(unittest.TestCase):
    def test_identity_version_and_resources(self):
        manifest = json.loads((ROOT / "manifest.json").read_text())
        skill = (ROOT / "SKILL.md").read_text()
        self.assertEqual(manifest["name"], "kang-product-architect")
        self.assertEqual(manifest["version"], "0.2.0")
        self.assertIn('version: "0.2.0"', skill)
        self.assertTrue((ROOT / "references/architecture-rubric.md").exists())
        self.assertTrue((ROOT / "evals/output_cases.json").exists())

    def test_professional_contract(self):
        skill = (ROOT / "SKILL.md").read_text()
        rubric = (ROOT / "references/architecture-rubric.md").read_text()
        for phrase in ["Required inputs", "Output contract", "Stop and escalate", "simpler alternative"]:
            self.assertIn(phrase, skill)
        for phrase in ["Evidence labels", "Decision priority", "Severity", "Quality gates"]:
            self.assertIn(phrase, rubric)

    def test_generic_scope_and_eval_coverage(self):
        skill = (ROOT / "SKILL.md").read_text().lower()
        self.assertNotIn("enterprise ai process diagnosis", skill)
        cases = json.loads((ROOT / "evals/trigger_cases.json").read_text())
        self.assertGreaterEqual(len(cases["should_trigger"]), 5)
        self.assertGreaterEqual(len(cases["should_not_trigger"]), 3)
        self.assertGreaterEqual(len(cases["near_neighbor"]), 3)


if __name__ == "__main__":
    unittest.main()
