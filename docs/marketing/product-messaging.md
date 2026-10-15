# RENKER Product Messaging

All wording below is checked against `docs/marketing/reality-check.md`. Where a capability is partial or planned, the copy says so explicitly rather than implying it's fully shipped.

---

## Rencora — ACT

**Core idea:** A desktop AI agent being built around explicit capabilities, permissions, and controlled execution — today a capable personal assistant with an integrated authorization layer; the fully-enforced capability runtime is the direction, not yet the complete current state.

### One-liner
A desktop AI agent that can actually operate your computer — with a capability-security layer standing between what it wants to do and what it's allowed to do.

### Short description
Rencora is a personal, local-first desktop AI agent for Windows, macOS, and Linux: real-time voice, screen and camera perception, system control, and persistent memory in a native app. Unlike a general assistant with blanket access, Rencora integrates with the Renker authorization core so filesystem and other actions can be evaluated against explicit, scoped, revocable grants instead of implicit trust.

### Long description
Rencora is Renker's ACT pillar: the agent that operates a computer on your behalf. It combines real-time voice interaction, screen and webcam perception, multi-step task planning, and persistent memory into a single native desktop app — with a choice of cloud (Gemini) or fully local (Ollama / RencoraLM) models for the reasoning layer.

What makes Rencora part of a security-first platform rather than "another assistant with system access" is its integration with `renker-core-authz`, the platform's authorization core: guarded filesystem operations can be evaluated through capability grants (who granted what, to whom, scoped to what path, for how long) instead of an all-or-nothing permission model. Generated automation code is statically checked before it runs (AST analysis blocking dangerous imports and calls), content read from the web or files is treated as untrusted data rather than instructions, and risk-classified actions require explicit confirmation before they execute.

This is a security-conscious personal project, not an externally audited production system — that's stated plainly in its own `SECURITY.md`, and the capability-enforcement path is actively being widened rather than complete.

### Problem
General-purpose AI assistants that can control a computer are only as safe as "the model decided it was a good idea." There's no layer that says, independent of what the model reasons its way into, exactly what it's allowed to touch.

### Solution
Route Rencora's higher-risk actions through an authorization layer that evaluates explicit, scoped grants — not the agent's own claims — and requires confirmation for anything risk-classified, with untrusted content walled off from being treated as instructions.

### Differentiator
Most desktop AI agents ship security as prompting ("please don't do dangerous things"). Rencora is integrating a deterministic, out-of-model authorization core (the same one that ships standalone as `renker-core-authz`, with 88 passing tests) instead of relying on the model to police itself.

### Developer value proposition
You can read the authorization decision path yourself — it's not a black box. The guard integration (`core/renker_guard.py`) is a small, inspectable adapter; you can see exactly what happens when the authorization core is present versus absent, and extend capability enforcement to new action types.

### Security value proposition
Even if a prompt injection convinces the model something dangerous is a good idea, the action still has to clear a policy check against actual granted capabilities — and destructive or high-risk actions require your explicit confirmation regardless of what the model argues for.

### Demo pitch
"Watch Rencora try to write outside its granted folder scope and get denied — then watch a webpage try to talk it into running a destructive command, and watch that fail too."

### GitHub description (repo tagline, ≤350 chars)
Personal desktop AI agent (Windows/macOS/Linux) with real-time voice, screen perception, and system control — integrating the Renker capability-security core so agent actions are scoped, auditable, and revocable rather than all-or-nothing.

### README hero text
> **Rencora** is a personal AI agent that can actually operate your computer — voice, screen, files, apps — built around the idea that "can act" and "may act" should be two different, separately-enforced questions. Security-conscious, locally run where you want it, honest about what's not yet audited.

---

## RenkerVault — SECURE

**Core idea:** Identity and secure-communication infrastructure for people, agents, devices, and services — not a Signal or WhatsApp competitor.

### One-liner
Zero-knowledge identity and secure-communication infrastructure — built so the relay never sees more than ciphertext, whether the endpoint is a person or an agent.

### Short description
RenkerVault is an end-to-end encrypted communication prototype — Double Ratchet, post-quantum-hybrid handshake, per-device identity, zero-knowledge relay — designed as infrastructure for secure identity and communication between people, AI agents, devices, and services, not as a consumer messenger competing on chat features.

### Long description
RenkerVault is Renker's SECURE pillar: the identity and secure-communication layer the rest of the platform builds on. It is not trying to replace Signal or WhatsApp — its value isn't "another encrypted chat app," it's a communication and identity substrate that treats agents and services as first-class participants alongside people.

Concretely, it provides end-to-end encrypted 1:1 messaging (Double Ratchet over an X3DH-hybrid handshake using audited primitives), group messaging with per-epoch keys, a post-quantum hybrid handshake (X25519 + ML-KEM-768, the same approach as Signal's PQXDH) for the initial key exchange, a zero-knowledge relay that only ever handles ciphertext and connection metadata, and passwordless Ed25519 challenge-response authentication. An intrusion-detection layer (brute-force lockout, new-device alerts, local-database tamper detection, a duress PIN with a fake view) is a core, working feature, not an afterthought.

It ships today as a functioning prototype/MVP with a documented internal security-hardening review (dated 2026-08-10, findings and fixes tracked in `docs/FINDINGS.md`) — not an externally audited production system, and it says so in its own README.

### Problem
As AI agents start communicating with each other, with services, and with people, that communication needs the same security properties end-to-end encrypted messaging built for humans — but most agent-to-agent communication today has none of it: no forward secrecy, no verified identity, no protection from an intermediary reading traffic.

### Solution
A zero-knowledge relay and end-to-end encrypted protocol stack that doesn't assume the participants are human — identity, device management, and encrypted channels designed to extend to agents and services using the same primitives used for people.

### Differentiator
Built from audited cryptographic primitives with the protocol composition itself openly documented and honestly scoped (the README states plainly which parts are, and are not, independently audited) — and designed from the start as infrastructure other systems consume, not a standalone chat product competing for users.

### Demo pitch
"Two RenkerVault clients exchange messages through a relay that only ever sees ciphertext — click the CT button to see exactly what the server sees. Then simulate an intrusion and watch the alarm system, lockout, and audit log fire in real time."

### GitHub description (repo tagline, ≤350 chars)
End-to-end encrypted identity and communication infrastructure — Double Ratchet, post-quantum-hybrid handshake, zero-knowledge relay, built-in intrusion detection. Designed for people, AI agents, and services alike, not as a standalone messenger product.

### README hero text
> **RenkerVault** is the identity and secure-communication layer of the Renker platform: end-to-end encryption, a relay that structurally cannot read your content, and an intrusion-alarm system as a core feature — built to work for agents and services as naturally as it works for people.

---

## Continuum — LEARN

**Core idea:** Autonomous research and discovery infrastructure with explicit evidence and verification — a Phase 0 software prototype today, deliberately positioned without AGI or discovery claims.

### One-liner
An autonomous research architecture where every claim the system makes carries an explicit evidence category — experimental, predicted, or literature-derived — enforced in code, not just policy.

### Short description
Continuum is a Phase 0 software prototype of a continuously learning autonomous research system, instantiated against simulated materials-science data. It's an architecture demonstration for how evidence-tagged, verifiable autonomous research could work — not a validated scientific result and not yet connected to real lab hardware.

### Long description
Continuum is Renker's LEARN pillar: infrastructure for autonomous research that refuses to assert things it hasn't actually verified. Its central mechanism is a hard rule enforced in code — every claim the system produces about a material, a hypothesis, or a model result must be tagged with exactly one evidence category (`EXPERIMENTAL`, `PREDICTED`, or `LITERATURE`), a calibrated confidence score, and a traceable source reference. Code that produces an untagged claim doesn't pass review.

Around that core, Continuum runs a working four-layer memory system (working / episodic / semantic / procedural, with tested consolidation), a Bayesian world model (Gaussian process with calibrated uncertainty) that proposes the next experiment to run, a multi-agent hypothesis tournament that runs end-to-end today against a mock LLM (no API key required), a governance gate that every simulated experiment approval must pass with a full audit log, and a hazard-screening scaffold flagged explicitly as an example rule set that needs domain-expert review before any real-world use.

Today this all runs against `data/simulated_materials.py`, a placeholder for real lab hardware — that's Phase 0 of a defined four-phase roadmap. Real weight-level continual learning (LoRA-based) and real lab integration are later phases, scaffolded as interfaces in the code today but not functional yet, by design ("phase discipline" is a non-negotiable project rule).

### Problem
Autonomous research systems built on LLMs inherit LLMs' core failure mode: they can state something false with the same confidence as something verified. In a research context, that's not a minor UX issue — it corrupts the record you're trying to build.

### Solution
Make evidence provenance a structural property of every claim the system emits, enforced by a verification layer that a claim simply cannot bypass, alongside a governance gate that logs every experiment-approval decision.

### Differentiator
Most "autonomous research agent" projects lead with the discovery story. Continuum leads with the verification story: the interesting engineering problem it solves is trustworthy evidence-tracking under autonomy, demonstrated first in a domain-agnostic core that's meant to transfer beyond materials science later.

### Demo pitch
"Watch Continuum's hypothesis tournament propose an experiment, run it against the simulated lab, and refuse to promote the result to a stated fact until it's tagged with the right evidence category and a source you can trace."

### GitHub description (repo tagline, ≤350 chars)
Phase 0 prototype of an evidence-verified autonomous research architecture — every system claim tagged experimental/predicted/literature and traceable to a source. Runs today on simulated materials-science data; no AGI claims, no real-lab connection yet.

### README hero text
> **Continuum** is a research architecture that will not let a claim through without saying where it came from. Phase 0 software prototype, running on simulated data — this is what evidence-based autonomous research could look like, built and tested before it's pointed at anything real.

---

## renker-core — shared foundation

**Core idea:** Shared identity, capability, permission, policy, and audit primitives that Rencora, RenkerVault, and Continuum all consume — currently a private repository; its public authorization subset ships as `renker-core-authz`.

### One-liner
The shared security and identity primitives underneath every Renker project — deterministic, auditable, and (in its public form) fully open source.

### Short description
`renker-core` is the platform's foundation: identity, capabilities, permissions, policy, audit, events, evidence, tasks, and memory primitives shared across Rencora, RenkerVault, and Continuum. Its authorization core ships publicly and independently as `renker-core-authz` — a zero-dependency, Apache-2.0 Python library with 88 passing tests and CI-enforced format/lint/type/dependency checks on every change.

### Long description
Every Renker project needs to answer the same handful of questions: who is this actor, what are they allowed to do, who decided that, and can we prove what happened afterward. `renker-core` is where those answers live once, instead of being reinvented per project.

Concretely, the primitives are: **Identity** (who is acting — human, agent, service, device), **Capabilities** (a specific permission, scoped to a specific target, with a lifetime and a revocation path), **Permissions/Policy** (the deterministic function that turns a requested action plus the actor's granted capabilities into ALLOW / DENY / REQUIRE_APPROVAL), **Audit** (a tamper-evident, hash-chained log of every decision), and platform-level concepts — **Events**, **Evidence**, **Tasks**, **Memory** — that Continuum and Rencora each consume differently.

The authorization slice of this (`Actor`, `Capability`, `CapabilityStore`, `evaluate`, `AuditLog`, `GuardedFilesystem`) is public today as `renker-core-authz`, with an explicit "security model (honest)" section stating what it does and does not provide. `renker-core` itself remains private while the platform is under active development; the public package is the verifiable, checkable version of the same ideas.

### Problem
Security and identity logic that's duplicated per-project drifts — one project fixes a scope-confusion bug, another doesn't, because they never shared the code in the first place.

### Solution
One deterministic, tested authorization core that every product in the platform imports rather than reimplements, with the public subset independently installable and auditable by anyone.

### GitHub description (repo tagline, ≤350 chars) — for renker-core-authz, the public face of this layer
Deterministic capability + policy + tamper-evident audit for autonomous agent actions — the public authorization core of the Renker platform. Zero runtime dependencies, Apache-2.0, 88 tests.

### README hero text (for renker-core-authz)
> **renker-core-authz** decides whether an agent's requested action runs — outside the model, from trusted grants only, never from what the agent claims. Every decision is recorded in a tamper-evident audit log. Zero dependencies, 88 tests, and a security model section that tells you exactly what this does *not* protect against.
