# PHASE_2_REPORT — From portfolio to a working platform slice

- **Date:** 2026-08-10
- **Repo:** renker-core (private)
- **Scope:** first vertical slice — `Identity → Capability → Policy → Decision → Execute/Audit`.

## What changed

New, self-contained authorization slice in renker-core (stdlib-only, comment-free code):

- `renker_core/identity/` — validated `Actor` + urn.
- `renker_core/capabilities/` — `Capability`, `PathScope` (traversal- and prefix-safe), `CapabilityStore`
  with revocation.
- `renker_core/policy/` — deterministic, explainable `evaluate()` → `ALLOW` / `DENY` / `REQUIRE_APPROVAL`.
- `renker_core/audit/` — structured `AuditEvent`, sha256 hash-chain + `.head` anchor, `verify()`.
- `renker_core/integration/` — `GuardedFilesystem`, the executor that runs the whole pipeline on a real
  file read/write.
- `tests/` — 40 tests (unit + adversarial), all passing.
- `demo/demo_slice.py` — runnable ALLOW + DENY end-to-end narrative with a verified audit trail.
- Docs: `RENKER_PLATFORM_AUDIT.md`, `docs/THREAT_MODEL.md`, `SECURITY_ATTACKS.md`, `RENKER_LEARNING/`.

## What was deliberately NOT changed

- **rencora, renkervault, continuum source** — untouched. No existing behavior modified.
- **renker-core primitives memory/tasks/events/experiments/evidence/protocol** — left as placeholders;
  not needed by the slice (Audit answer 12).
- **No crypto implemented** in renker-core (interfaces only, per the crypto boundary).
- **No REQUIRE_APPROVAL UI**, no network/browser/camera capabilities, no distributed audit, no scoring
  engine — all explicitly deferred.

## Tests

- `pytest -q` → **40 passed**.
- `ruff check .` → clean.
- Adversarial suite proves: path traversal, prefix confusion, expired, wrong actor, wrong operation,
  wrong target, revocation, malformed identity, silent-decision, audit modification/truncation/deletion
  are all blocked/detected. Mapping in `SECURITY_ATTACKS.md`.

## Security findings

- The slice enforces confinement, least privilege, explainability, auditability, tamper-evidence, and a
  safe default — as claimed in `docs/THREAT_MODEL.md §5`, no more.
- Honest non-guarantees are documented (§6): no cryptographic actor authentication, replay within
  lifetime is possible, full host compromise defeats the audit anchor, and **enforcement only applies to
  actions routed through the guard**.

## Known limitations

- Identity is validated, not authenticated.
- The audit log is tamper-**evident**, not immutable.
- The guard is not yet wired into rencora's live action dispatch (see next step).

## Architecture decisions

- renker-core = authorization foundation, stdlib-only; crypto stays out; `protocol` (cross-language) not
  needed yet.
- Deterministic rules over scoring (auditability).
- One action verb + one scope per capability (least privilege by construction).
- Integration modeled as a guarded executor performing the *same* operation rencora's `file_controller`
  performs, so the pipeline is real, not mocked.

## Learning completed

`RENKER_LEARNING/` curriculum with the `Learn → Recall → Explain → Apply → Attack → Debug` loop and
code-backed modules (Identity, Capabilities/Least-Privilege, Policy, Path-Traversal, Audit) plus
conceptual sections (Authn-vs-Authz, Threat Modeling, Prompt Injection, Rencora Security Architecture).
Reference answers are placed after the questions so they are not seen first.

## Demo status

`python demo/demo_slice.py` shows: ALLOW (write into `drafts/`), ALLOW (read it back), DENY
(read `.ssh/config`, out of scope), DENY (write via `..`), then a verified tamper-evident audit trail.
Output is reproducible and only shows functionality that actually works.

## Rencora integration — DECIDED: Option A (optional adapter), implemented

Sebastian chose **Option A**. Implemented additively in rencora (no existing file changed):

- `rencora/core/renker_guard.py` — `RencoraFileGuard` + helpers. Lazily imports `renker_core`; if it is
  not installed, `is_available()` is `False` and the module is a harmless no-op (the PyInstaller build and
  all existing behavior are unchanged).
- `rencora/tests/test_renker_guard.py` — skips when `renker_core` is absent; when present, verifies
  ALLOW (write into scope), DENY (outside scope), DENY (traversal). Verified locally: 4 passed with
  renker_core installed, 1 skipped without it.

**Live wiring point (deliberate, not yet applied):** to enforce on real rencora file writes, construct a
`RencoraFileGuard` from `config/renker_capabilities.json` at agent-session start and call `guard.write(
session_id, path, content)` before `actions/file_controller` performs the write; deny → skip the write and
surface the reason. This is a small, opt-in change to the dispatch path and is left for a focused,
reviewed follow-up so existing rencora behavior is not altered in this phase.

Grant config shape (`config/renker_capabilities.json`, optional):
```json
{ "grants": [
  { "capability": "filesystem.write", "scope": "~/Documents/drafts", "granted_to": "agent:<session-id>" }
] }
```

### Original decision record (for history)

The choice hinged on renker-core being **private** while rencora's CI is **public**.

```
Decision required:
  How should the public rencora repo consume the private renker-core authorization slice?

Options:
  A) Optional adapter (CURRENT-safe): add one additive module to rencora that imports renker_core
     lazily; if it is installed on the host, file actions are guarded, otherwise rencora behaves as
     today. rencora CI stays green (test skips when renker_core is absent). No repo made public.
  B) Extract a public "renker-core-authz" subset (identity/capabilities/policy/audit only) that rencora
     can pip-install; keep the rest of renker-core private.
  C) Make renker-core public and add it as a normal dependency of rencora.
  D) Git submodule / vendored copy of the authz subset inside rencora.

Recommendation:
  A now (reversible, additive, nothing exposed), moving to B for the real product.

Reason:
  A proves the seam without a packaging commitment or exposure; B is the clean long-term boundary
  (public authorization core, private everything else) that matches the Vision's open-source ebene.

Security impact:
  A/B keep the enforcement code reviewable and small. C exposes all of renker-core (currently only the
  bootstrap + this slice) prematurely. D risks code drift between the copy and the source.

Long-term impact:
  B is the path the product portfolio (Vision §6, "Free / Open Source" ebene) already anticipates.
```

Until this is decided, no rencora source is modified.
