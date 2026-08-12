# The problem isn't intelligence anymore. It's permissions.

*Launch post for RENKER — publish-ready (blog / dev.to). Every claim here is traceable to a repository, a test run, or a documented limitation; see [reality-check.md](../reality-check.md).*

---

For most of the last few years, the hard question about AI was capability: *can the model actually do this?* In 2026 that question is quietly answering itself. Models can operate a computer, send a message, call a tool, run an experiment. The interesting problem has moved.

The open question now is what happens *around* that capability:

- **Permissions** — what is a given agent actually allowed to do, and who decided that?
- **Identity** — which actor (human, agent, service, device) is making a request?
- **Security** — what happens when untrusted content — a webpage, an email, a file — tries to manipulate the agent?
- **Verification** — how do you know a claim the system makes is backed by evidence, not a plausible-sounding guess?
- **Accountability** — after something happens, can you reconstruct exactly who did what, when, and why?

Guardrails built *inside* a model can be talked around — that is precisely what prompt injection is. If the thing deciding whether an action is allowed is the same model being asked to police itself, the decision is only as strong as the model's current mood about a cleverly-worded input.

**RENKER's premise is simple: the decision of what an agent is allowed to do should live in a small, deterministic, auditable layer *outside* the model — one that reads only trusted grants, never the agent's own claims about what it should be allowed to do.**

## Three problem domains, one foundation

RENKER is organized around three concrete questions, each mapped to a project, all sharing one foundation of identity, capability, permission, policy, and audit primitives.

- **ACT — [Rencora](https://github.com/sebastianrenker/rencora).** A desktop AI agent that can operate your computer — voice, screen, files, apps — with a capability-security layer between what it wants to do and what it's allowed to do. Today it's a capable personal assistant with an *integrated* authorization layer; full capability enforcement for every action is the direction, not yet the complete current state. Personal, non-commercial use.
- **LEARN — [Continuum](https://github.com/sebastianrenker/continuum).** An autonomous research architecture where every claim the system makes carries an explicit evidence category — `EXPERIMENTAL`, `PREDICTED`, or `LITERATURE` — enforced in code, not policy. It's a Phase 0 prototype running against simulated data, not real lab hardware, and the repo says so on its front page.
- **SECURE — [RenkerVault](https://github.com/sebastianrenker/renkervault).** Zero-knowledge identity and secure-communication infrastructure: end-to-end encryption over a relay that only ever sees ciphertext, designed for agents and services as first-class participants alongside people. A working prototype with a documented internal security-hardening review — not an externally audited production system.

Underneath all three sits **renker-core**, the shared foundation. Its authorization slice ships publicly and independently as [`renker-core-authz`](https://github.com/sebastianrenker/renker-core-authz): a zero-dependency, Apache-2.0 Python library that decides `ALLOW` / `DENY` / `REQUIRE_APPROVAL` from stored grants alone, records every decision in a tamper-evident, hash-chained audit log, and ships with 88 passing tests and CI that runs format, lint, type-check, tests, build, and a dependency audit on every push.

```bash
pip install git+https://github.com/sebastianrenker/renker-core-authz
```

## Why I'm publishing a reality-check alongside this

Every RENKER repository already carries its own "honest limitations" section. Rather than soften that for a launch, I'm leaning into it: there's a single [reality-check document](../reality-check.md) that checks every marketing claim across all four repos against actual code, test runs, and CI output — marking each one `REAL`, `PARTIAL`, or `PLANNED` with the evidence next to it.

It includes the gaps: no project has had an independent third-party audit; not every repo ran its tests in CI at launch; renker-core itself is a private repository, so claims about it are limited to what's visible through its public consumers. A security claim you can't falsify isn't worth much — so here are the receipts.

If a claim about RENKER isn't in that document with evidence behind it, don't believe it yet.

---

**Explore the code:** [Rencora](https://github.com/sebastianrenker/rencora) · [Continuum](https://github.com/sebastianrenker/continuum) · [RenkerVault](https://github.com/sebastianrenker/renkervault) · [renker-core-authz](https://github.com/sebastianrenker/renker-core-authz) · [reality-check.md](../reality-check.md)
