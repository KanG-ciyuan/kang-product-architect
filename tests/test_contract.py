import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class ContractTests(unittest.TestCase):
    def test_package_identity_and_scope(self):
        m = json.loads((ROOT / "manifest.json").read_text())
        s = (ROOT / "SKILL.md").read_text()
        self.assertEqual(m["name"], "kang-product-architect")
        self.assertIn("Do not use for coding", s)

if __name__ == "__main__":
    unittest.main()
