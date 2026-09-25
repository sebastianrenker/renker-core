# RENKER Website Concept

Information architecture for a possible renker.dev (or similar) site. Copy below is aligned to `brand.md` and checked against `reality-check.md` — nothing here claims more maturity than the repos support today.

## Site map

```text
/                    Home
/problem             The problem RENKER addresses
/architecture         Platform architecture (ACT / LEARN / SECURE / core)
/rencora              Product page
/continuum            Product page
/renkervault           Product page
/core                 renker-core + renker-core-authz
/security             Security & disclosure
/research             Continuum research approach & evidence model
/docs                 Documentation hub (links out to GitHub docs/wikis)
/github               Links to all repos
/roadmap              Public roadmap (phase status per project)
```

## Home

```text
RENKER

Trusted Infrastructure
for Autonomous AI.

AI systems are becoming capable of acting.
RENKER builds the infrastructure that makes those actions
controllable, verifiable, and accountable.

[Explore RENKER]     [View on GitHub]
```

Below the fold, in order:
1. **Three-pillar strip** — ACT / LEARN / SECURE, one line each, linking to their product pages. Each card carries its real status qualifier (e.g. "Rencora — desktop agent, personal use" / "Continuum — Phase 0 prototype").
2. **"Not another AI pitch" block** — a short paragraph and a direct link to `reality-check.md`, framed as: "Every claim on this site is checked against actual code, tests, and CI. Here's the receipts." This is a genuine differentiator given how rare it is — lead with it, don't bury it in a footer.
3. **Live proof point** — the renker-core-authz test count and CI status, pulled from the actual repo (badge or a small "88 tests passing" stat with a link to the workflow run — never a static/typed-in number that can drift from reality).
4. **Ecosystem diagram** — the Mermaid/ASCII diagram from `ecosystem-diagram.md`, rendered.
5. **CTA row** — GitHub, docs, roadmap.

## /problem

Prose page expanding `brand.md`'s "problem RENKER addresses" section: permissions, identity, security, verification, accountability, autonomous execution — each with one paragraph and, where possible, a link to the specific RENKER component addressing it.

## /architecture

The ecosystem diagram plus a short explanation of each shared primitive (Identity, Capabilities, Permissions/Policy, Audit, Events, Evidence, Tasks, Memory) drawn from `product-messaging.md`'s renker-core section. Link each primitive to where it's consumed (e.g. Capabilities → Rencora's guard integration).

## Product pages (/rencora, /continuum, /renkervault)

Each follows the same template, populated from `product-messaging.md`:
1. One-liner + status badge (e.g. "Personal use, security-conscious, not externally audited")
2. Problem / Solution / Differentiator (three short blocks)
3. Embedded demo (GIF or short video) from `demo-scenarios.md`
4. "What works today" / "What's planned" — pulled directly from the corresponding reality-check.md rows, kept in sync
5. Install / quickstart, copied verbatim from the repo README so it never drifts
6. Link to full README and SECURITY.md on GitHub

## /core

Splits into two clearly labeled sections: **renker-core-authz** (public, installable, with live test count) as the primary content, and a short, honest note about **renker-core** ("the platform's private shared foundation; its public authorization subset is renker-core-authz above") — no feature claims about renker-core beyond what's independently visible.

## /security

Aggregates the SECURITY.md files' key points across all projects in one place, with direct links to each project's full SECURITY.md rather than restating and risking drift. Includes a disclosure-policy section (how to report a vulnerability, pulled from renker-core-authz/rencora's existing "report a vulnerability" guidance) and a standing note: "No RENKER project has undergone an independent third-party security audit yet. Internal hardening reviews are documented per-project (see links)."

## /research

Continuum-specific page explaining the `EXPERIMENTAL`/`PREDICTED`/`LITERATURE` evidence model and the phase roadmap, sourced from `product-messaging.md` and Continuum's own `ROADMAP.md`.

## /docs and /roadmap

Thin aggregator pages — mostly links out to each repo's own docs/wiki and ROADMAP.md, rather than duplicating content that will drift. Roadmap page pulls each project's current phase/status directly from its wiki Roadmap.md.

## Build notes

- Static site (no user data collected, no login) is sufficient for this stage — there's no product requiring accounts yet.
- Every numeric claim on the site (test counts, "X repos," etc.) should be sourced from something automatable (a GitHub Actions badge, a small script pulling live repo stats) rather than hand-typed, specifically to avoid the site drifting out of sync with `reality-check.md` the way READMEs and wikis have occasionally drifted from code (see reality-check.md finding on rencora's wiki roadmap).
- Defer building this until at least the Week-1/Week-2 launch content exists — the site's strongest asset is the reality-check transparency angle, and that reads better once there's an actual audience checking it.
