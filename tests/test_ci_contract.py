import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]


class CiContractTests(unittest.TestCase):
    def test_ci_workflow_runs_contract_and_static_site_tests(self):
        workflow = (ROOT / ".github" / "workflows" / "ci.yml").read_text()

        self.assertIn("python -m unittest discover -s tests -p 'test_*.py'", workflow)
        self.assertIn("python -m http.server", workflow)
        self.assertIn("curl --fail", workflow)


if __name__ == "__main__":
    unittest.main()
