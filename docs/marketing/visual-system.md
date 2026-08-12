# RENKER Visual System

Built from what already exists rather than invented from scratch: RenkerVault's own README already documents a real design language ("Dunkles Graphit/Anthrazit-HUD mit Smaragdgrün/Cyan als Akzent — bewusst kein Violett, eigenständig gegenüber Rencora"), which implies Rencora already occupies a violet/purple identity. This system extends that existing logic platform-wide instead of replacing it.

## Principles

- Technical, serious, quiet — reads like engineering documentation that happens to look good, not a product marketing site.
- No neon cyberpunk overload, no glowing circuit-board textures, no generic "AI brain/network" stock imagery.
- Every diagram should look like it could appear in a security whitepaper. If it looks like a keynote slide, it's wrong for this brand.
- Color is used to differentiate pillars, not to decorate. Red is reserved — in RenkerVault it already means "alarm state" specifically; don't dilute that by using red decoratively elsewhere in the system.

## Color

| Role | Color | Notes |
|---|---|---|
| RENKER base / neutral | Graphite / anthracite (`#1a1a1a`–`#2a2a2a`) | Shared background across all platform-level materials (diagrams, site chrome) |
| ACT (Rencora) | Violet (`#6d5dfc`-family, matching Rencora's existing in-app identity) | Reserve for Rencora-specific material only |
| SECURE (RenkerVault) | Emerald green / cyan (matching RenkerVault's existing in-app theme) | Reserve for RenkerVault-specific material only |
| LEARN (Continuum) | A third, distinct hue not yet claimed by the other two — recommend a muted amber/gold, since it reads as "evidence/measurement" without competing with the alarm-red reservation | Confirm against Continuum's actual UI if/when one exists; none was found in this repo, so this is a proposal, not a documented existing choice |
| Alarm / risk state | Red — reserved exclusively for actual alarm/danger states (RenkerVault's existing convention) | Never use red for general emphasis or CTAs anywhere in the platform |
| Text / body | Off-white / light gray on dark backgrounds | High contrast, no pure white-on-black (harsh) |

## Typography

- A monospace or semi-monospace face for anything code-adjacent (diagrams, terminal captures, capability/permission examples) — reinforces "this is real code," not decoration.
- A clean, technical sans-serif (e.g., Inter, IBM Plex Sans, or similar) for body copy and headings — avoid anything geometric/futuristic-display that reads as "sci-fi" rather than "technical."
- Avoid italic for emphasis in technical contexts; use weight instead.

## Diagram style

- Flat, boxed, hierarchical — the ecosystem diagram in `ecosystem-diagram.md` is the reference style: simple boxes, straight connecting lines, minimal color, generous whitespace.
- No 3D effects, drop shadows, or gradients on diagram elements.
- Every diagram element that represents a real repo/component should be labeled with its actual name (not a codename or abstraction) so a reader can map it directly to something on GitHub.
- Status qualifiers (prototype / private / Phase 0) belong directly on the diagram, in small type — never omitted for visual cleanliness.

## Code-screenshot style

- Plain, high-contrast syntax highlighting on a dark background (graphite base) — avoid "hacker green terminal" clichés.
- Screenshots should show real, runnable output (like the verified outputs in `demo-scenarios.md`), never mocked-up or edited text pretending to be terminal output.
- Crop tightly to the relevant lines; don't show a full IDE chrome unless the point is specifically about tooling/CI.

## GitHub banner / social cards

- Consistent template across all repos: dark graphite background, project name in the technical sans-serif, one-line value proposition beneath it, small ACT/LEARN/SECURE pillar tag in the project's assigned accent color, RENKER wordmark small in a corner (platform, not the hero).
- No screenshots of UI crammed into the banner — keep it typographic and diagram-based, consistent with the "engineering doc, not a poster" principle.

## Project icons

- Simple, geometric, single-color-per-project (using each pillar's assigned accent), abstract rather than literal (e.g., not a literal padlock for RenkerVault, not a literal robot for Rencora) — geometric forms that could plausibly appear in a technical diagram: a bounded box/scope shape for Rencora (capability boundary), a shielded node for RenkerVault (zero-knowledge relay), a small branching/tree shape for Continuum (hypothesis tournament).
- Full spec (exact SVG paths, pixel grid) is a follow-on design task once the palette above is confirmed — this document defines the system, not final assets.

## What to explicitly avoid

- Stock "AI" imagery: glowing brains, circuit-pattern humanoid heads, abstract neural network globs.
- Overpromising visual metaphors (e.g., a shield icon implying "unhackable" — RenkerVault's own README explicitly disclaims that framing).
- Excessive gradient/glow effects that read as generic 2023-era "AI startup" aesthetic rather than a considered, specific identity.
- Emoji in official brand materials (READMEs already use a couple sparingly — e.g. 🛡 in RenkerVault, 🚨 for alarms — that's fine as functional signaling, but shouldn't expand into decorative use in marketing material).
