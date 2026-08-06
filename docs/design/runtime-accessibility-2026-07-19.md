# MHToolkit website runtime and accessibility evidence — 2026-07-19

## Runtime

The worktree was served without any game, emulator, account, or restricted asset:

```text
rtk proxy python3 -m http.server 8765 --bind 127.0.0.1
rtk proxy curl --fail --silent --show-error http://127.0.0.1:8765/ -o /tmp/mhtoolkit-web-index.html
```

The HTTP smoke request exited `0`; the fetched document SHA-256 was
`716c77de84c4f880f7c61920056430ae237d92dbf3deb3fda0ee77afdc32af4b`.

Playwright CLI opened `http://127.0.0.1:8765/` in Chrome, reloaded after the semantic
contract change, and captured the full scrollable page at both target viewports.

| Artifact | Viewport | SHA-256 |
| --- | --- | --- |
| `apple-design-desktop-runtime-full.png` | 1440x1000 | `10952f588c0ac7e68c2e65559257080ed60d4904b0fc1d0646657b8629b233e8` |
| `apple-design-mobile-runtime-full.png` | 390x844 | `4faf143970c69fcc0708e5dca01d9983b184730fb9542ee23aa03d51612929e5` |

## Semantic/accessibility tree

The captured Playwright accessibility snapshot is checked in at
`docs/design/accessibility-tree-2026-07-19.yml` (SHA-256
`00b9b913eb69cd293f66f40f80108db9967ba0df3c8d600a43b0816cb9286dc5`). It confirms:

- document title `MH Toolkit`, language `en`, and banner/main/contentinfo landmarks;
- explicit `Project navigation` navigation landmark;
- labelled `Project areas` region with five article entries and links for Nemessix, MH Overlay,
  MH Save Sync, MH Field Map, and Coordinated releases;
- a `status` live region containing the fail-closed compatibility state;
- all 11 links exposed as keyboard focusable controls.

The browser-side computed-style probe confirmed each project link uses
`display: inline-flex` and `min-block-size: 44px`. The static contract also covers focus-visible,
reduced-motion, reduced-transparency, and increased-contrast states.

## Verification

```text
rtk test python -m unittest discover -s tests -p 'test_*.py'  # 3 passed
rtk git diff --check                                      # exit 0
```

