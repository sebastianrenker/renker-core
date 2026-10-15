# RENKER SEO Notes

Keyword direction, not keyword-stuffing copy. Use these as a checklist when writing titles/headings/meta descriptions naturally — never as a density target to hit inside prose.

## Primary keyword clusters

**AI agent security**
`AI agent security`, `AI agent permissions`, `AI agent sandboxing`, `secure AI agents`, `agent capability security`, `capability-based security AI`

**Identity & access**
`AI agent identity`, `AI agent authentication`, `agent-to-agent communication security`, `zero-knowledge identity infrastructure`

**Autonomous systems governance**
`autonomous AI security`, `AI audit logs`, `AI accountability`, `trusted AI infrastructure`, `AI action verification`, `deterministic AI authorization`

**Research/evidence**
`autonomous research AI`, `AI experimentation platform`, `evidence-based AI research`, `AI hypothesis generation`, `scientific integrity AI`

**Prompt injection / model-adjacent**
`prompt injection defense`, `prompt injection vs capability security`, `AI tool call security`, `LLM agent guardrails`

## Where these map to real RENKER content (so copy stays natural, not stuffed)

- `renker-core-authz` README/pages: "AI agent security," "capability-based security," "deterministic AI authorization," "AI audit logs" — this repo is the strongest, most literally-true match for these terms (real tests, real ALLOW/DENY/REQUIRE_APPROVAL semantics).
- Rencora pages: "AI agent sandboxing," "AI agent permissions," "prompt injection defense" — backed by the AST-based code check and trust-boundary handling in SECURITY.md.
- RenkerVault pages: "zero-knowledge identity infrastructure," "agent-to-agent communication security," "secure AI agents" (communication angle specifically, not the authorization angle).
- Continuum pages: "autonomous research AI," "evidence-based AI research," "scientific integrity AI," "AI hypothesis generation" — and explicitly *not* "AI discovers new materials" or similar, since that's not what Phase 0 does.

## Title / meta description guidance

- Repo/page titles should contain one primary keyword phrase naturally, matching what the page actually delivers (e.g. `renker-core-authz — Deterministic Capability Security for AI Agents`, not a broader claim than the repo supports).
- Meta descriptions: one sentence of real value proposition + one qualifier if relevant status matters (e.g. "...a Phase 0 research prototype" for Continuum pages) — search engines and readers both penalize a page whose meta description overpromises relative to content.
- Avoid keyword-stuffed headers like "Best AI Agent Security Solution 2026" — RENKER's credibility angle depends on specific, checkable language, and that tone reads as exactly the kind of unverifiable marketing this project is trying not to produce.

## Structured content that helps organically

- `reality-check.md` itself, if published on a website, is strong SEO content almost by accident: it's exactly the kind of specific, evidence-linked, long-form technical page that ranks well for "AI agent security" style searches, precisely because it isn't written as SEO content.
- Individual technical blog posts from `developer-content-plan.md` (e.g. "What is capability security?", "How prompt injection works") are better organic-search assets than product pages, since they answer a specific question a searcher actually has.
- Internal cross-linking: every product page linking to the shared `renker-core-authz` repo and vice versa helps search engines understand the platform structure — this is also just accurate, since that's the real dependency relationship.

## What to avoid

- No hidden text, no doorway pages, no artificial backlink schemes.
- No keyword variations stuffed into alt text or headings beyond what reads naturally to a human.
- Don't target keywords implying capabilities RENKER doesn't have yet (e.g. "AI agent marketplace," "enterprise AI compliance platform") just because they're high-volume — mismatched intent traffic doesn't convert and undermines the credibility-first positioning.
