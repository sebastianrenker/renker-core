# RENKER Social Posts — final, copy-paste ready

Real repository links filled in. `[MEDIA: …]` marks where a screenshot/GIF must be attached before posting — re-run the demo the same week so it matches current behavior (see `demo-scenarios.md`). No invented numbers, no "audited" claims, no fake urgency. Suggested posting order in the 30-day sequence is in `launch-plan.md`.

**Links used**
- renker-core-authz — https://github.com/sebastianrenker/renker-core-authz
- Rencora — https://github.com/sebastianrenker/rencora
- RenkerVault — https://github.com/sebastianrenker/renkervault
- Continuum — https://github.com/sebastianrenker/continuum
- reality-check — https://github.com/sebastianrenker/renker-core/blob/main/docs/marketing/reality-check.md
- all repos — https://github.com/sebastianrenker

---

## X / Twitter

**1.** Guardrails built inside an LLM can be talked around. That's the whole premise behind `renker-core-authz`: what an agent *can* do is decided outside the model, in a small deterministic function that reads only trusted grants — never the agent's own claims. 88 tests, zero deps.
https://github.com/sebastianrenker/renker-core-authz

**2.** Prompt injection can change what an agent *requests*. It can't change what it's *allowed* to do — if that decision doesn't live in the model. That's the one-line pitch for RENKER's authorization core.
https://github.com/sebastianrenker/renker-core-authz

**3.** Shipped: a tamper-evident audit log with a SHA-256 hash chain and a `verify()` you can actually run. Not "trust us" — check it yourself.
`[MEDIA: code screenshot of audit/log.py verify()/query()]`
https://github.com/sebastianrenker/renker-core-authz

**4.** Rencora can operate your computer — voice, screen, files, apps. The interesting part isn't that it can. It's what stops it from doing something you didn't grant it permission to do.
`[MEDIA: Demo GIF — capability boundary DENY]`
https://github.com/sebastianrenker/rencora

**5.** RenkerVault's relay only ever sees ciphertext, account IDs, and device metadata. The demo UI has a button (CT) that shows you the exact ciphertext the server sees for a message you just sent.
`[MEDIA: screenshot of CT / ciphertext view]`
https://github.com/sebastianrenker/renkervault

**6.** Continuum won't let a claim through without tagging it EXPERIMENTAL, PREDICTED, or LITERATURE, with a source you can trace. That rule is enforced in code (`ClaimChecker`), not just written in a doc.
https://github.com/sebastianrenker/continuum

**7.** Every RENKER repo README has a section on what it does *not* protect against. Not because we have to — because a security claim you can't falsify isn't worth much.
https://github.com/sebastianrenker/renker-core-authz#security-model-honest

**8.** Post-quantum today, honestly scoped: RenkerVault's initial handshake combines X25519 with ML-KEM-768. The ongoing ratchet isn't PQ-secured yet — and the README says so, not just the fine print.
https://github.com/sebastianrenker/renkervault

**9.** Building infrastructure for autonomous AI means answering boring questions well: who is this actor, what are they allowed to do, who granted that, can I prove what happened after the fact. That's `renker-core`.
`[MEDIA: ecosystem diagram]`
https://github.com/sebastianrenker/renker-core-authz

**10.** New: `renker-core-authz` — the public authorization core behind Rencora. Apache-2.0, zero runtime dependencies, CI that runs format/lint/type-check/tests/dependency-audit on every push.
`pip install git+https://github.com/sebastianrenker/renker-core-authz`

---

## LinkedIn

**1.** AI models are getting good enough to act — not just answer. That shifts the hard problem from "is the model smart enough" to "what happens around it": permissions, identity, verification, accountability. That's the layer I'm building at RENKER — three projects (Rencora for agent execution, RenkerVault for identity and secure communication, Continuum for evidence-based autonomous research), one shared foundation of capability and audit primitives.
→ https://github.com/sebastianrenker

**2.** I just finished writing an honest reality-check across all four RENKER repositories — every marketing claim checked against actual code, test runs, and CI output, not against what I intended to build. The result: some things are further along than the docs suggested, some are earlier. Publishing both is the point.
→ https://github.com/sebastianrenker/renker-core/blob/main/docs/marketing/reality-check.md

**3.** The authorization core behind RENKER's agent runtime, `renker-core-authz`, is public: 88 automated tests, CI-enforced formatting/linting/type-checking/dependency auditing, zero runtime dependencies, Apache-2.0. It decides whether an agent's requested action runs — based only on grants that were actually issued, never on what the agent itself claims it should be allowed to do.
→ https://github.com/sebastianrenker/renker-core-authz

**4.** A pattern I keep coming back to while building RENKER: security guardrails that live inside a language model can be reasoned around, because the model is the thing being asked to police itself. Moving the decision outside the model — into a small, deterministic, testable function — is a very different (and much more checkable) guarantee.

**5.** RenkerVault's README states plainly what its cryptography does and doesn't cover: audited primitives, yes; an externally audited protocol composition, not yet. That kind of precision is what makes a security claim actually mean something, instead of just being a badge.
→ https://github.com/sebastianrenker/renkervault

**6.** Continuum, the research pillar of RENKER, enforces something simple but strict in code: no system-generated claim about a material or hypothesis is allowed through without being tagged experimental, predicted, or literature-derived, with a traceable source. It's Phase 0 — running on simulated data, not real lab hardware yet — and that's stated on the front page of the repo, not buried.
→ https://github.com/sebastianrenker/continuum

**7.** Building RENKER independently, using AI-assisted development (Claude Code as a pair programmer) and systematic research to iterate faster across four repositories at once. I can explain and justify every part of each codebase — that's the standard I'm holding myself to, especially on the security-relevant parts.

**8.** If you're evaluating an "AI security" claim from any project (including mine), the fastest useful question is: what's the test count, does CI actually run it, and what does the project itself say it does *not* protect against? Those three things tell you more than any amount of marketing copy.

**9.** Three products, one foundation: Rencora (agent execution with capability security), RenkerVault (identity and secure communication), Continuum (evidence-verified autonomous research) — all built on shared identity/capability/permission/policy/audit primitives.
`[MEDIA: ecosystem diagram]`
→ https://github.com/sebastianrenker

**10.** Publishing a full accounting of what's real vs. planned across RENKER's four repositories — including the gaps (no external audit yet, one repo still private). Marketing that can't survive a reality-check isn't marketing I want to publish.
→ https://github.com/sebastianrenker/renker-core/blob/main/docs/marketing/reality-check.md

---

## Reddit / developer communities

Lead with substance, invite critique, one community per post — no cross-posting the same text.

**1. r/programming / r/netsec-style** — "I built a deterministic capability-security library for AI agents — outside the model, 88 tests, zero deps. Here's the security model and what it explicitly does *not* protect against." Lead with the README's own honesty section, invite people to poke holes.
https://github.com/sebastianrenker/renker-core-authz

**2. r/selfhosted / r/privacy-style** — "RenkerVault: a self-hosted, zero-knowledge E2E encrypted chat prototype with a post-quantum hybrid handshake. Prototype/MVP, not audited — here's exactly what that means." Mention the Tor hidden-service hosting option as a concrete detail worth discussing.
https://github.com/sebastianrenker/renkervault

**3. r/MachineLearning / r/artificial-style** — "An autonomous research architecture that refuses to let a claim through without evidence tagging (experimental/predicted/literature) — Phase 0, simulated data, full roadmap public." Ask specifically for feedback on the evidence-taxonomy design.
https://github.com/sebastianrenker/continuum

**4. r/cybersecurity-style** — "What does a real (not marketing) 'security model' section look like? Sharing renker-core-authz's approach — explicit ALLOW/DENY/REQUIRE_APPROVAL semantics, a tamper-evident audit log, and a documented list of what it does NOT provide." Frame as a documentation-practice discussion.
https://github.com/sebastianrenker/renker-core-authz

**5. r/opensource-style** — "Four related repos, one shared security core, and an experiment in publishing an honest 'reality check' doc alongside the marketing." Link the reality-check itself as the interesting artifact.
https://github.com/sebastianrenker/renker-core/blob/main/docs/marketing/reality-check.md

---

## Launch-day posts

**1. Platform (X thread + LinkedIn).** RENKER is infrastructure for AI systems that act, learn, and communicate — built around the idea that capability shouldn't imply permission. Today: three working prototypes (Rencora, RenkerVault, Continuum) and one open-source authorization core (renker-core-authz, 88 tests, Apache-2.0). Here's what's real, what's not yet, and where to look at the code.
Repos: https://github.com/sebastianrenker · reality-check: https://github.com/sebastianrenker/renker-core/blob/main/docs/marketing/reality-check.md

**2. Authz core (technical).** Launching the public authorization core of RENKER: `renker-core-authz`. Deterministic capability + policy + tamper-evident audit for AI agents, decided outside the model.
`pip install git+https://github.com/sebastianrenker/renker-core-authz`

**3. Transparency.** Why I'm publishing a reality-check alongside every RENKER launch post: every claim about these four repos, checked against actual test runs and CI output, in one document. If a claim isn't in there with evidence, don't believe it yet.
https://github.com/sebastianrenker/renker-core/blob/main/docs/marketing/reality-check.md

**4. RenkerVault.** RenkerVault prototype is live: end-to-end encrypted messaging with a post-quantum hybrid handshake and a zero-knowledge relay, built as identity infrastructure for people *and* agents. Not a Signal competitor — infrastructure the rest of RENKER builds on.
`[MEDIA: Demo GIF]`
https://github.com/sebastianrenker/renkervault

**5. Continuum.** Continuum Phase 0 is running: a research architecture where every claim carries its evidence category, tested against simulated data, with a defined roadmap to real lab integration. The LEARN pillar of RENKER — no AGI claims, just a verification-first architecture.
https://github.com/sebastianrenker/continuum
