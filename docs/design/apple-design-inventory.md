# MHToolkit website Apple Design inventory

## Real UI entry points

- `index.html`: global navigation, hero, project/release navigation, status surface, responsive layout.
- `assets/design-tokens.css`: semantic surface/label/state/motion/accessibility mapping.

## State and accessibility inventory

- The release status is a persistent `role=status` surface with an explicit `data-state`.
- Project navigation needs visible focus, 44px targets, reduced-motion behavior, reduced-transparency fallback, increased-contrast tokens, and mobile reflow.
- The site must not infer compatibility from a repository link; copy remains fail-closed.

## Verification

- Contract: `rtk test python -m unittest tests/test_apple_design.py`
- Runtime: serve the repository root and capture desktop/mobile screenshots with Playwright.
- Static gate: `rtk git diff --check`.
