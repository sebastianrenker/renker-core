# RENKER 30-Day Launch Plan

Structure follows the brief: Week 1 explains RENKER, Week 2 shows Rencora, Week 3 shows renker-core/security, Week 4 shows the whole system plus community feedback. Every "Content" item maps to a specific artifact in `developer-content-plan.md`, `social-posts.md`, or `demo-scenarios.md` — nothing here requires new writing beyond what's already planned. Weekends are lighter by design (engagement/reply days, not new content) to keep this sustainable for one person.

Legend: **CTA** = the single action you want the reader to take. **Material needed** = what must exist before that day (demo recording, code snippet, diagram, etc.) — build these a few days ahead, not same-day.

## Week 1 — Explain RENKER

| Day | Content | Platform | Goal | CTA | Material needed |
|---|---|---|---|---|---|
| 1 | Launch post: "RENKER is infrastructure for AI systems that act, learn, and communicate" | X + LinkedIn | Introduce the platform-level story | Read the reality-check | Ecosystem diagram, links to all 4 repos, `reality-check.md` published |
| 2 | Long-form: "The problem isn't intelligence anymore, it's permissions" (brand.md core argument) | Blog / dev.to | Establish the core thesis before showing products | Read full post | brand.md draft turned into a post |
| 3 | Thread: "Guardrails inside an LLM can be talked around" (prompt injection vs. capability security) | X | Technical hook, differentiate from prompt-engineering "safety" | Reply/discuss | Content idea #2 from developer-content-plan.md |
| 4 | "Why three products share one foundation" — architecture explainer | LinkedIn | Explain ACT/LEARN/SECURE + renker-core structure | Star/follow the repos | Ecosystem diagram |
| 5 | Reddit post: "Sharing a reality-check doc alongside our marketing — here's what's real vs. planned across 4 repos" | r/opensource-style community | Credibility-first community intro | Feedback on the doc | reality-check.md link |
| 6 | Engagement day — reply to comments/questions from the week, no new content | X + Reddit | Build relationships, gather objections | — | — |
| 7 | Recap + preview: "This week: what RENKER is. Next week: watching Rencora actually run." | X + LinkedIn | Bridge into product week | Follow for the demo | — |

## Week 2 — Show Rencora

| Day | Content | Platform | Goal | CTA | Material needed |
|---|---|---|---|---|---|
| 8 | Demo GIF: Demo 1 (Safe Agent, ALLOW) — Rencora reads a file it's scoped to read | X + LinkedIn | Show the capability model working, not just described | Watch the demo | Screen recording of Demo 1 (see demo-scenarios.md) |
| 9 | Demo GIF: Demo 2 (Capability Boundary, DENY) — Rencora blocked from writing outside scope | X | Show the negative case — this is the credible half | Read how the guard integration works | Screen recording of Demo 2 |
| 10 | Technical post: "Agent sandboxing with AST analysis" (how generated automation code is checked before it runs) | Blog / dev.to | Depth for technical readers | Read the code | Content idea #4 |
| 11 | Demo GIF: Demo 3 (Prompt Injection blocked) | X + LinkedIn | The most viscerally convincing demo — a webpage trying to manipulate the agent and failing | Try it yourself | Screen recording of Demo 3 |
| 12 | Build-in-public post: "What I learned building Rencora's guard integration" (the fallback-import pattern, honest about partial coverage today) | LinkedIn | Credibility through candor about what's not done yet | Discuss | Content idea #14 |
| 13 | Engagement day | X + Reddit | Reply, collect questions for an FAQ | — | — |
| 14 | Recap + preview: "This week: Rencora acting under explicit boundaries. Next week: the core underneath it." | X + LinkedIn | Bridge into renker-core-authz week | Follow | — |

## Week 3 — Show renker-core / Security

| Day | Content | Platform | Goal | CTA | Material needed |
|---|---|---|---|---|---|
| 15 | Launch post: `renker-core-authz` is public — 88 tests, zero deps, Apache-2.0 | X + LinkedIn + Reddit | Drive installs/stars of the most-verifiable repo | `pip install` / star the repo | README already updated; code sample from README |
| 16 | Demo GIF: Demo 5 (Audit) — show WHO/WHAT/WHEN/WHY/DECISION/OUTCOME for a real decision | X | Make "auditable" concrete, not abstract | Read the audit log code | Screen recording / terminal capture of `AuditLog.query()` |
| 17 | Technical post: "What a tamper-evident audit log actually looks like" (hash chain, verify()) | Blog / dev.to | Deep technical credibility piece | Read the code | Content idea #3 |
| 18 | Demo GIF: Demo 6 (Revocation) — capability revoked mid-session | X + LinkedIn | Show the "jederzeit widerrufbar" claim is real, not aspirational | Try it | Screen recording of Demo 6 |
| 19 | Reddit/dev-community post: "What does a real security-model section look like?" using renker-core-authz's honesty section as the example | r/cybersecurity-style community | Position as a documentation-practice discussion, not a pitch | Discuss/critique | Link to README "Security model (honest)" |
| 20 | Engagement day | X + Reddit | Reply, address any security critiques directly and openly | — | — |
| 21 | Recap + preview: "This week: the core that decides ALLOW/DENY/REQUIRE_APPROVAL. Next week: the whole system, and what you think." | X + LinkedIn | Bridge into system-level week | Follow | — |

## Week 4 — Whole system + community feedback

| Day | Content | Platform | Goal | CTA | Material needed |
|---|---|---|---|---|---|
| 22 | RenkerVault demo: two clients messaging through a zero-knowledge relay, CT button showing ciphertext | X + LinkedIn | Introduce SECURE pillar with a concrete demo | Try the demo build | Screen recording (see demo-scenarios.md Demo 8) |
| 23 | Continuum demo: hypothesis proposed → tested against simulated lab → evidence-tagged | X | Introduce LEARN pillar without overclaiming (Phase 0, simulated) | Read the roadmap | Screen recording (see demo-scenarios.md Demo 7) |
| 24 | System-level post: full ecosystem diagram + "here's how the three pillars and the core fit together" | LinkedIn | Tie the month together into one coherent picture | Explore the platform docs | Ecosystem diagram, website.md if live |
| 25 | "Ask me anything about RENKER's security model" — open thread | X + Reddit | Direct community feedback, surface real objections | Ask questions | Prior week's Q&A notes |
| 26 | Publish a "what we heard this month" post — genuine summary of pushback/questions and what changes as a result | LinkedIn | Close the feedback loop publicly; this is where trust compounds | Read the response | Collected feedback from days 6/13/20/25 |
| 27 | Founder-story post: building RENKER independently, AI-assisted development, systematic research | LinkedIn | Humanize the project, grounded framing | Follow the journey | Content idea #33 |
| 28 | Engagement day | X + Reddit | Reply, thank early testers/reviewers by name (with permission) | — | — |
| 29 | "One month in: what's real, what's next" — links back to an updated reality-check.md reflecting any status changes | X + LinkedIn | Reinforce the truth-first pattern as an ongoing habit, not a launch stunt | Read the updated reality-check | Updated reality-check.md |
| 30 | Roadmap post: what the next 30 days focus on, informed by community feedback | X + LinkedIn | Convert launch momentum into an ongoing cadence | Follow for updates | Updated priorities from marketing-status.md |

## Operating notes

- Don't post a demo GIF you haven't personally re-run that week — code changes, and a stale demo that no longer matches current behavior is exactly the kind of gap `reality-check.md` exists to prevent.
- Two engagement-only days per week (weekends) are load-bearing, not filler — this plan fails if there's no time to actually answer the security questions serious readers will ask.
- If a claim in a queued post stops being true (a test starts failing, a limitation gets fixed, a status changes), update `reality-check.md` first, then the post.
