import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]


class AppleDesignWebTests(unittest.TestCase):
    def test_shared_semantic_tokens_and_accessibility_states_are_wired(self):
        html = (ROOT / "index.html").read_text()
        tokens = (ROOT / "assets/design-tokens.css").read_text()

        self.assertIn('href="assets/design-tokens.css"', html)
        self.assertIn("--surface-window", tokens)
        self.assertIn("--state-warning", tokens)
        self.assertIn("prefers-reduced-motion", tokens)
        self.assertIn("prefers-reduced-transparency", tokens)
        self.assertIn("prefers-contrast", tokens)
        self.assertIn(":focus-visible", tokens)

    def test_project_navigation_exposes_all_user_products(self):
        html = (ROOT / "index.html").read_text()
        tokens = (ROOT / "assets/design-tokens.css").read_text()
        for product in ("Nemessix", "MH Overlay", "MH Save Sync", "MH Field Map"):
            self.assertIn(product, html)
        self.assertIn('aria-label="Project navigation"', html)
        self.assertIn('role="navigation"', html)
        self.assertIn(".project-link h2 a", tokens)
        self.assertIn("min-block-size: var(--target-minimum)", tokens)
        self.assertIn('data-state="planning"', html)


if __name__ == "__main__":
    unittest.main()
