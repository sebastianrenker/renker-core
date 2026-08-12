# RENKER GitHub Social Preview Images

Five 1280×640 PNG social preview images were generated for this task (not just specced) — see the files in this folder: `renker.png`, `rencora.png`, `renkervault.png`, `continuum.png`, `renker-core-authz.png`. They follow `visual-system.md`: graphite background, per-pillar accent color, technical sans-serif type, no stock AI imagery, status-accurate one-line value propositions pulled from `product-messaging.md`.

## Specs (for regenerating or hand-building alternates)

| Repo | Title | Subtitle | Accent | Value proposition | Tag |
|---|---|---|---|---|---|
| RENKER (org-level) | RENKER | Trusted Infrastructure for Autonomous AI | Neutral gray `#8b8b8b` | Permissions, identity, security and audit for AI systems that act, learn, and communicate. | PLATFORM |
| rencora | Rencora | ACT — Desktop AI Agent | Violet `#7c6cf6` | Voice, screen and system control with an integrated capability-security layer. | ACT |
| renkervault | RenkerVault | SECURE — Identity & Communication | Emerald `#2fbf8f` | End-to-end encrypted messaging with a zero-knowledge relay and post-quantum handshake. | SECURE |
| continuum | Continuum | LEARN — Evidence-Verified Research | Amber `#d1a13a` | Autonomous research architecture where every claim carries its evidence category. | LEARN |
| renker-core-authz | renker-core-authz | Public Authorization Core | Steel blue `#4a90d9` | Deterministic capability + policy + tamper-evident audit. 88 tests, zero dependencies. | CORE |

All cards: dark graphite radial-gradient background (`#232323` → `#101010`), 1280×640px (GitHub's required social-preview size), 10px accent-colored left border, small "RENKER" wordmark top right, tag pill top left in the pillar's accent color, repo URL bottom left, "ACT · LEARN · SECURE" wordmark bottom right for cross-navigation context.

## How to apply

GitHub → repo → Settings → General → Social preview → Upload an image. Use the matching PNG for each repository (`renkervault.png` for the renkervault repo, etc.). The `renker.png` card is meant for the org profile or a future platform-level landing page rather than any single repo.

## Regenerating

The cards were built as plain HTML/CSS and rendered with Playwright/Chromium at 1280×640. To regenerate with updated copy or colors, rebuild an HTML file per card following the layout described above (graphite background, accent bar, tag pill, title/subtitle/value stack, bottom row with URL + pillar wordmark) and screenshot it at exactly 1280×640 — any headless-browser screenshot tool works.
