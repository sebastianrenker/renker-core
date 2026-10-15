# RENKER Developer Content Plan

35 content ideas, grouped by category. Each idea lists the primary source repo/evidence it draws on, so nothing here requires inventing material — every idea is traceable to something already in `reality-check.md`. Format suggestion (blog / thread / video) is a starting point, not a constraint.

## Technical (12)

1. **Capability security for AI agents** — walk through `renker-core-authz`'s `Capability`/`PathScope`/`evaluate()` model with real code. Source: renker-core-authz.
2. **Prompt injection vs. capability security: why they're different problems** — show a prompt-injection attempt that changes *what's requested* but not *what's allowed*, using Rencora's untrusted-content marking + the authz core. Source: rencora SECURITY.md §5, renker-core-authz README "Why".
3. **What a tamper-evident audit log actually looks like** — dissect the SHA-256 hash chain + `verify()`/`query()` in `renker_core_authz/audit/log.py`. Source: renker-core-authz.
4. **Agent sandboxing with AST analysis** — how Rencora statically checks generated automation code before running it, with restricted builtins. Source: rencora SECURITY.md §4.
5. **Designing a "security model (honest)" section** — why stating what a system does *not* protect against is more credible than a badge, using renker-core-authz's README as the example. Source: renker-core-authz README.
6. **Secure agent-to-agent communication, not just agent-to-human** — RenkerVault's zero-knowledge relay and why it's designed for agents/services as participants. Source: renkervault wiki, README.
7. **Post-quantum hybrid handshakes for messaging apps** — the ML-KEM-768 + X25519 handshake in RenkerVault, and honestly, what it does *not* yet cover (the ongoing ratchet). Source: renkervault SECURITY.md §4b.
8. **Evidence-based AI research: tagging every claim with its provenance** — Continuum's `Evidence` enum (`EXPERIMENTAL`/`PREDICTED`/`LITERATURE`) enforced via `ClaimChecker`. Source: continuum verification/evidence.py.
9. **Autonomous experimentation with a governance gate** — how Continuum's `safety/governance.py` logs every simulated experiment approval, and why that pattern needs to be correct *before* Phase 1 hardware. Source: continuum CLAUDE.md, safety/governance.py.
10. **A Bayesian world model for experiment selection** — the Gaussian-process surrogate model in Continuum, what "calibrated uncertainty" buys you. Source: continuum worldmodel/surrogate.py.
11. **Zero-dependency security libraries: why `renker-core-authz` ships with no runtime dependencies** — the tradeoffs of a stdlib-only authorization core. Source: renker-core-authz pyproject.toml, README.
12. **What CI actually enforces: reading a real security-library pipeline** — walk through renker-core-authz's `ci.yml` (format, lint, mypy, pytest, build, pip-audit) end to end. Source: renker-core-authz .github/workflows/ci.yml.

## Build in Public (10)

13. **Building RENKER from scratch: why three projects share one foundation** — the decision to split ACT/LEARN/SECURE with a shared `renker-core` instead of three siloed products.
14. **What I learned building Rencora's guard integration** — the fallback-import pattern (`renker_core_authz` → `renker_core` → none) and what it's like retrofitting capability security into an existing assistant.
15. **Why I built renker-core-authz as a standalone, zero-dependency package** — the decision to make the authorization core independently installable and auditable rather than bundled.
16. **Building an AI agent security layer: the parts that were harder than expected** — candid post on scope-confusion / path-traversal edge cases found while hardening (`tests/test_hardening.py`).
17. **Breaking my own agent: adversarial testing Rencora and RenkerVault** — using `tests/test_security_attacks.py` / `tests/test_trust_boundary.py` and the RenkerVault "self-found and fixed timing side-channel" as the story.
18. **The RenkerVault security-hardening review: what FINDINGS.md actually contains** — walk through the format (severity, fix, regression test) of a real internal review, and why it's dated and versioned instead of a one-time badge claim.
19. **Using Claude Code for adversarial testing** — process post on the Builder→Attacker→Reviewer cycle mentioned in the Rencora wiki, with a concrete before/after example.
20. **Why Continuum enforces "no unverified claim" in code, not just in docs** — the engineering decision to make `ClaimChecker` a hard gate rather than a guideline.
21. **What "Phase 0" actually means and why I'm not skipping to Phase 1** — Continuum's phase-discipline rule and the Go/No-Go criteria in ROADMAP.md, as a case study in resisting scope creep.
22. **A week of shipping across four repos: what stayed in sync and what didn't** — honest retro referencing the actual gap found in this reality-check (Rencora's wiki roadmap listing capability security as not-yet-done while the code already has a working integration).

## Educational (10)

23. **What is capability security? (for people who've only heard "prompt injection")**
24. **Why AI agents need an identity primitive, not just an API key**
25. **Why permissions matter more than "alignment" for the things an agent can already do today**
26. **How prompt injection actually works, with a minimal reproducible example**
27. **Why AI actions need auditability — what "who did what, when, why" buys you when something goes wrong**
28. **Why autonomous research needs evidence tagging, not just confidence scores**
29. **Deterministic vs. model-based security decisions: why "outside the model" matters**
30. **What a zero-knowledge relay actually knows (and doesn't)** — using RenkerVault's `docs/METADATA.md` field-by-field breakdown as source material.
31. **Reading a threat model: a walkthrough of RenkerVault's `docs/THREAT_MODEL.md`**
32. **What "tamper-evident" means vs. "tamper-proof" — and why that distinction matters for audit logs**

## Founder story (3)

33. **Building RENKER independently** — grounded version: *"I'm building RENKER independently while using AI-assisted development and systematic research to iterate faster — Claude Code as a pair programmer, not a replacement for understanding what I'm shipping."* Mirror the tone already used in the RenkerVault README's own "Über dieses Projekt" section (age stated plainly, no overclaiming, explicit ownership of every part of the codebase).
34. **What changed after the RenkerVault security-hardening review** — a concrete story of finding and fixing a real issue (the documented timing side-channel), told as a lesson in the value of adversarial self-review rather than as a credential claim.
35. **Why "not yet audited" is on every README** — the reasoning behind treating unqualified security claims as a liability rather than a selling point, and what changes once each project actually gets reviewed by someone external.

## Guardrails for every piece (apply before publishing)

- No claim in any piece should say more than the matching row in `reality-check.md`.
- Never say "audited" for internal reviews — say "internal security-hardening review" and name the date/doc.
- Every technical post should link to the actual file/test it describes, so a skeptical reader can verify in under a minute.
- Founder-story content stays factual and specific ("I'm 18, building this independently, using Claude Code as a pair programmer") — never "I invented the future of AI" framing.
