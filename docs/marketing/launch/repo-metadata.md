# Repo metadata — ready to paste

GitHub "About" descriptions (≤350 chars), suggested topics, and README hero snippets for each repo. Copy verbatim from `product-messaging.md`; all wording checked against `reality-check.md`. Set the "About" field via each repo's ⚙️ (top-right of the repo page) → Description + Topics.

---

## rencora  (ACT)

**Description**
> Personal desktop AI agent (Windows/macOS/Linux) with real-time voice, screen perception, and system control — integrating the Renker capability-security core so agent actions are scoped, auditable, and revocable rather than all-or-nothing.

**Topics:** `ai-agent` `desktop-agent` `capability-security` `prompt-injection` `llm` `automation` `security` `renker`

**README hero**
> **Rencora** is a personal AI agent that can actually operate your computer — voice, screen, files, apps — built around the idea that "can act" and "may act" should be two different, separately-enforced questions. Security-conscious, locally run where you want it, honest about what's not yet audited.

---

## renkervault  (SECURE)

**Description**
> End-to-end encrypted identity and communication infrastructure — Double Ratchet, post-quantum-hybrid handshake, zero-knowledge relay, built-in intrusion detection. Designed for people, AI agents, and services alike, not as a standalone messenger product.

**Topics:** `end-to-end-encryption` `double-ratchet` `post-quantum` `ml-kem` `zero-knowledge` `secure-messaging` `identity` `renker`

**README hero**
> **RenkerVault** is the identity and secure-communication layer of the Renker platform: end-to-end encryption, a relay that structurally cannot read your content, and an intrusion-alarm system as a core feature — built to work for agents and services as naturally as it works for people.

---

## continuum  (LEARN)

**Description**
> Phase 0 prototype of an evidence-verified autonomous research architecture — every system claim tagged experimental/predicted/literature and traceable to a source. Runs today on simulated materials-science data; no AGI claims, no real-lab connection yet.

**Topics:** `autonomous-research` `evidence-based` `bayesian-optimization` `world-model` `ai-safety` `governance` `phase-0` `renker`

**README hero**
> **Continuum** is a research architecture that will not let a claim through without saying where it came from. Phase 0 software prototype, running on simulated data — this is what evidence-based autonomous research could look like, built and tested before it's pointed at anything real.

---

## renker-core-authz  (public authorization core)

**Description**
> Deterministic capability + policy + tamper-evident audit for autonomous agent actions — the public authorization core of the Renker platform. Zero runtime dependencies, Apache-2.0, 88 tests.

**Topics:** `authorization` `capability-based-security` `audit-log` `ai-agents` `policy-engine` `zero-dependency` `apache-2` `renker`

**README hero**
> **renker-core-authz** decides whether an agent's requested action runs — outside the model, from trusted grants only, never from what the agent claims. Every decision is recorded in a tamper-evident audit log. Zero dependencies, 88 tests, and a security model section that tells you exactly what this does *not* protect against.

---

## renker-core  (shared foundation)

**Description**
> The shared identity, capability, permission, policy, and audit foundation of the Renker platform. Its public authorization subset ships independently as renker-core-authz.

**Topics:** `renker` `platform` `identity` `capabilities` `audit` `policy`

---

## Website (`/site`)

The platform landing page is a single self-contained `site/index.html` — no build step, no external requests, no data collected. Serve it any static way:

- **GitHub Pages:** Settings → Pages → deploy from a branch → `/site` folder. (This repo is currently private; a public Pages site needs Pages enabled and, on some plans, a public repo — or host it from one of the public repos instead.)
- **Local preview:** `python -m http.server -d site` then open http://localhost:8000
- Every numeric claim on the page (test count, CI checks) mirrors `reality-check.md`; when a status changes, update `reality-check.md` first, then the page.
