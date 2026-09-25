# RENKER Marketing Status

Stand: 2026-08-11. This is the wrap-up report for the marketing/developer-adoption pass across all four RENKER repositories. Everything referenced here was verified against actual code, tests, or CI during this pass — see `reality-check.md` for the full evidence table.

## Current positioning

**RENKER builds trusted infrastructure for autonomous AI** — permissions, identity, security, verification, and accountability for AI systems that act, learn, and communicate. Three pillars (ACT/Rencora, SECURE/RenkerVault, LEARN/Continuum) on one shared foundation (renker-core, public authorization subset: renker-core-authz). No AGI claims, no "unhackable" claims, no unqualified superlatives — every project already disclaims these itself in its own README/SECURITY.md, and the new marketing material carries that discipline forward rather than diluting it. Full statement: `brand.md`.

## Project status (condensed from reality-check.md)

| Project | Real & verified today | Notable gap |
|---|---|---|
| **renker-core-authz** | 88 tests passing, full CI (format/lint/type/test/build/dependency-audit), deterministic ALLOW/DENY/REQUIRE_APPROVAL, tamper-evident audit log | Not yet on PyPI; no external audit |
| **Rencora** | Real desktop agent, DPAPI secret handling, AST-sandboxed code execution, untrusted-content trust boundary, optional guard integration with renker-core-authz | Capability enforcement is partial/optional, not yet the default path for every action; tests exist but aren't wired into CI |
| **RenkerVault** | Real E2E encryption (Double Ratchet, PQ-hybrid handshake), zero-knowledge relay, 51 documented security tests, dated internal hardening review with tracked findings | No CI pipeline at all (`.github/workflows/` doesn't exist); protocol composition not externally audited (stated in its own README) |
| **Continuum** | Real 4-layer memory, Bayesian world model, evidence-tagged claims enforced in code, governance-gated experiment approval, 32 tests + CI | Phase 0 only — simulated data, no real lab hardware, no real continual learning yet (by design, documented) |
| **renker-core** | Referenced consistently as the shared foundation by all three public repos | **Private** — unverifiable from outside; no specific feature claims about it should be made beyond what's independently visible through renker-core-authz |

## Marketing assets produced this pass

`reality-check.md` · `brand.md` · `product-messaging.md` · `ecosystem-diagram.md` · `developer-content-plan.md` (35 ideas) · `social-posts.md` (30 posts) · `launch-plan.md` (30-day plan) · `demo-scenarios.md` (10 demos, 5 independently verified by running real code) · `website.md` · `visual-system.md` · `social-previews/` (5 generated 1280×640 PNG images + spec) · `seo.md` · this status report.

## GitHub status

Additive README updates were made to all four public repos (renkervault, rencora, continuum, renker-core-authz): each now has a "RENKER-Plattform" / "Related RENKER projects" section cross-linking the sibling repos and the ecosystem diagram, placed without touching any existing content. No badges, benchmarks, user counts, audits, or customers were invented anywhere — see `reality-check.md`'s explicit "not belegt" (unsupported) rows for what was deliberately excluded.

**Important constraint:** this session has read-only, unauthenticated access to your GitHub repos (public HTTPS clone only — no push credentials, no `gh` auth, no admin access to repo settings). That means:
- The README edits exist as local changes in this session's workspace and have **not** been pushed. They need to be applied by you (patches/diffs available on request, or I can walk through applying them if you connect a way to push).
- Repo descriptions, topics, and the GitHub social-preview image upload are Settings-level changes I cannot make remotely — `social-previews/README.md` has exact instructions for applying the generated images yourself.
- `renker-core` itself was not reachable at all (private, no token provided) — everything about it in this pass is inferred from how the three public repos reference it, not from its own contents.

## Content plan

30-day launch plan in `launch-plan.md` (Week 1: platform story, Week 2: Rencora demos, Week 3: renker-core-authz/security, Week 4: whole system + community feedback), backed by 35 evergreen content ideas in `developer-content-plan.md` and 30 ready-to-adapt posts in `social-posts.md`.

## Best demos

The five demos independently executed against real code during this pass (`demo-scenarios.md`, Demos 1/2/4/5/6, all inside `renker-core-authz`) are the safest to lead with — allow → deny → require-approval → audit → revoke, all runnable live in under a minute with zero external dependencies. Demo 3 (prompt injection) is backed by an existing passing test (`test_tool_output_claiming_authorization_has_no_effect`) rather than a live run in this pass, but is equally real. Demos 8–10 (RenkerVault, Continuum, Rencora sandboxing) are real and documented in their own repos but require more setup to demo live — better captured as recordings.

## The Claude-Code marketing loop

For every new feature going forward, run this checklist before calling it "done":

```text
BUILD → TEST → VERIFY → DOCUMENT → DEMO → PUBLISH → COLLECT FEEDBACK → BUILD AGAIN
```

Concretely, per feature: (1) can it be demonstrated with a real, runnable example — not a mock? (2) is it documented in the relevant README/SECURITY.md/wiki page? (3) does `reality-check.md` need a new or updated row? (4) is there a genuine educational angle (add to `developer-content-plan.md`)? (5) does it warrant a launch post (add to `social-posts.md`/`launch-plan.md`)? (6) does the README hero section need updating? If a feature can't clear "can it be demonstrated with a real, runnable example," it isn't ready to be marketed yet — build/test/verify first.

## Unproven claims (do not use until evidenced)

- Any claim of an **external/third-party security audit** for any project (only internal reviews exist today).
- **"Production-grade" / "production system"** for Rencora or RenkerVault (both explicitly disclaim this themselves).
- **AGI, "discovers new materials," or any real-lab result** for Continuum (Phase 0, simulated data only).
- **Cryptographic actor authentication** for renker-core-authz (README states identity is validated, not authenticated).
- **CI-enforced testing** for Rencora or RenkerVault (tests exist locally; only renker-core-authz and Continuum have it wired into CI today).
- Any **specific feature claim about renker-core itself** beyond what's independently visible via renker-core-authz (the repo is private and unverifiable from outside).
- **User counts, customer names, or benchmark numbers** — none exist anywhere in the current repos; do not introduce them.

---

## Prioritization

### DO NOW (max 5)
1. Decide and publish one canonical public sentence clarifying the relationship between `renker-core` (private) and `renker-core-authz` (public) — right now that relationship is implied, not stated, and it's the single biggest clarity gap found in this pass.
2. Apply the additive README changes already prepared in this session to the four public repos (or ask me to walk through applying them) and upload the five generated social-preview images via each repo's Settings page.
3. Wire `pytest`/`npm test` into CI for Rencora and RenkerVault — both have real, substantial test suites that simply aren't running automatically yet; this closes the biggest credibility gap in `reality-check.md` for the least effort.
4. Publish `reality-check.md` itself somewhere public (even just linked from each README) — it's your strongest trust asset and currently only exists in this session's output.
5. Record the Demo 1→2→6→5 sequence (renker-core-authz allow/deny/revoke/audit) as a short screen-capture — it's fully verified, requires no setup, and is ready to publish today.

### DO NEXT (max 10)
1. Ship Week 1 of `launch-plan.md` (platform-story posts + reality-check-first Reddit post).
2. Update the Rencora wiki's `Roadmap.md` to reflect that a capability-guard integration already exists (currently reads as not-started, which undersells real progress).
3. Fix the Week-4 launch-plan reminder loop: re-verify every demo the week you post it, since code changes.
4. Publish PyPI package for `renker-core-authz` (README already promises this "once published").
5. Add a CI workflow to RenkerVault (currently has none at all).
6. Build the five product-page skeletons from `website.md` even before a real site exists, as a shareable set of docs.
7. Record Demos 8–10 (RenkerVault relay/alarm, Continuum evidence loop, Rencora sandboxing) as videos for Weeks 3–4.
8. Draft the founder-story post (`developer-content-plan.md` #33) — grounded, factual version, ready for Week 4.
9. Set up the recurring "what we heard this month" feedback-loop habit (Week 4, Day 26) as an ongoing monthly practice, not a one-off.
10. Commission or schedule an actual external security review for at least one project (RenkerVault or renker-core-authz are the strongest candidates) — this is the one item on this whole list that changes what's *true*, not just what's communicated.

### LATER
Everything else in `developer-content-plan.md` (remaining 20+ content ideas), the full `website.md` build-out, the full `visual-system.md` icon/logo asset production, Continuum real-lab partnership (explicitly a separate future project per its own ROADMAP.md), Phase 1+ work on any project, SEO content buildup, and any paid/growth channel work — none of this is urgent relative to the DO NOW/DO NEXT items, which are about making sure the foundation (CI, canonical renker-core statement, published reality-check) is solid before scaling content volume.
