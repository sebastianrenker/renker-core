# renker-core

> A small, deterministic **security decision kernel** for autonomous AI agents.
> An agent makes a request; renker-core verifies its identity, checks capabilities and policy, weighs
> context and risk, and produces one **explainable, auditable decision** — ALLOW, DENY, or REQUIRE_APPROVAL.

## 1. What is renker-core?
A dependency-free Python library that answers a single question well: *should this actor be allowed to
perform this action on this resource, right now?* The answer is a first-class, immutable, serializable
`Decision`. The security decision lives **outside** the LLM by construction.

## 2. Why does it exist?
Autonomous agents get real capabilities (files, processes, network). A manipulated agent (prompt injection,
a poisoned tool result) can be talked into harmful actions. Guardrails inside the model can be talked around.
renker-core makes the decision deterministic, capability-scoped, fail-closed, and recorded — so injection can
change *what is requested*, never *what is allowed*.

## 3. 30-second example
```python
from datetime import datetime, timezone
from renker_core import (
    Identity,
    Action,
    Resource,
    Context,
    Capability,
    CapabilityStore,
    PathScope,
    Policy,
    StaticPolicyEngine,
    Authorizer,
    AuthorizationRequest,
    InMemoryAuditSink,
)

store = CapabilityStore()
store.grant(
    Capability(
        capability="filesystem.write",
        scope=PathScope(base="~/project/drafts"),
        granted_to="agent:session-1",
        granted_by="human:owner",
        issued_at=datetime.now(timezone.utc),
        expires_at=None,
    )
)

authorizer = Authorizer(StaticPolicyEngine(store, Policy("default", "1")), InMemoryAuditSink())

decision = authorizer.authorize(
    AuthorizationRequest(
        subject=Identity("agent", "session-1"),
        action=Action("filesystem", "write"),
        resource=Resource("file", "~/project/drafts/note.md"),
        context=Context(environment="development", user_present=True),
    )
)
print(decision.effect.value, "-", decision.reason)  # ALLOW - within capability scope...
```

## 4. Architecture
```
Agent Request -> Identity -> Capability -> Context -> Policy -> Risk -> Decision
                                                                          |
                                                           ALLOW / DENY / REQUIRE_APPROVAL
                                                                          |
                                                               EXECUTE / APPROVAL -> AUDIT
```
`Authorizer` orchestrates the flow (fail-closed). `PolicyEngine` (a `Protocol`) makes the decision;
`StaticPolicyEngine` is the built-in implementation. `RBAC/ABAC/Remote/Composite` engines are documented
extension points, not built (see `docs/EXTENSION_POINTS.md`).

## 5. Security model
- **Fail closed.** Invalid/expired identity, unknown capability, unauthorized resource, expired/replayed
  approval, unknown policy, or any evaluation error resolve to **DENY**. Errors never become ALLOW.
- **Decision is outside the LLM.** The engine reads only trusted grants + actor/action/resource/context —
  never a request-supplied "authorized" or "risk" flag.
- **Least privilege.** Capabilities are actor-bound, scoped, time-bound, revocable, immutable.
- **Scope safety.** Resource matching resolves paths and compares `os.path.normcase` parts — traversal,
  prefix confusion, and case tricks are rejected.
- **Replay protection.** Requests carry `request_id`/`nonce`/`issued_at`; `ReplayGuard` rejects stale or
  reused nonces. Approvals are one-time and bound to a specific `decision_id` + subject/action/resource.
- **Auditability.** Every decision is recorded via an `AuditSink` (tamper-evident sha256 hash chain).
- **No home-grown crypto.** Signature verification is an interface (`crypto_interface`), not an
  implementation (see `docs/EXTENSION_POINTS.md`). No dummy security, no `return True` in authz code.

Details and honest non-guarantees: [`docs/THREAT_MODEL.md`](docs/THREAT_MODEL.md),
[`SECURITY_ATTACKS.md`](SECURITY_ATTACKS.md).

## 6. Core primitives (semantics)
| Primitive | Meaning |
|---|---|
| **Identity** | *Who* is asking (kind + identifier, optional expiry/attributes). Validated, **not** authenticated. |
| **Action** | *What* verb in a namespace, e.g. `Action("filesystem","write")`. |
| **Resource** | *On what*, e.g. `Resource("file","/home/u/x")`. |
| **Capability** | A grant to a subject: *may do this action within this scope*, time-bound + revocable. |
| **Permission** | The (Action + ResourcePattern) pair a capability grants — "what on which resource". |
| **Policy** | Versioned conditions (`policy_id`, `version`, ordered `Rule`s) that can only **restrict**. |
| **Context** | Environment signals (environment, user_present, network). Cannot loosen a decision. |
| **Decision** | The immutable, serializable result: effect + subject/action/resource + policy id/version + reason + obligations + timestamp + decision_id. |
| **Approval** | A real request/approve/consume model for REQUIRE_APPROVAL, one-time, expiring, replay-protected. |
| **Audit** | A structured, decision-linked, tamper-evident event chain via an `AuditSink`. |

These words are **not** synonyms: a Capability grants Permissions to a subject; a Policy governs conditions.

## 7. Installation
```bash
pip install -e ".[dev]"
```
Python ≥ 3.10, **zero runtime dependencies** (standard library only).

## 8. API
Import everything from the top level:
```python
from renker_core import (
    Identity,
    Action,
    Resource,
    ResourcePattern,
    Context,
    Capability,
    Permission,
    CapabilityStore,
    PathScope,
    Policy,
    Rule,
    PolicyEngine,
    StaticPolicyEngine,
    Effect,
    Decision,
    RiskAssessment,
    Authorizer,
    AuthorizationRequest,
    ReplayGuard,
    Approval,
    ApprovalRequest,
    ApprovalStore,
    AuditLog,
    AuditSink,
    InMemoryAuditSink,
    AuditEvent,
)
```
The public surface is frozen in `renker_core.__all__` and guarded by `tests/test_public_api.py`.

## 9. Tests
```bash
ruff format --check . && ruff check . && mypy && pytest -q
```
132 tests: unit, integration (full flow), security (invalid/expired identity, unknown capability,
unauthorized resource, traversal, replay, expired/replayed approval, malformed input, policy failure),
property-based (hypothesis) invariants, and the tamper-evident audit chain.

## 10. Roadmap / status
| Area | Status |
|---|---|
| Identity, Capability, Permission, Policy, Context, Decision, Risk, Approval, Replay, Audit, Authorizer | **CURRENT** |
| Signed identities / signature verification | **PROPOSED** — interface only (`docs/EXTENSION_POINTS.md`) |
| RBAC / ABAC / Remote / Composite policy engines | **PROPOSED** — extension point |
| Evidence / Provenance primitive | **PROPOSED** — documented, deliberately not built |
| `protocol` wire serialization, memory/tasks/events | **PROPOSED** |

## Platform context
- The shipped, black-box-verified public authorization core is [`renker-core-authz`](https://github.com/sebastianrenker/renker-core-authz)
  (Apache-2.0); this repo (`renker-core`, private) is the next-generation kernel that will re-supersede it.
- Wiki (in-repo): [`docs/wiki/Home.md`](docs/wiki/Home.md) · Vision: [`RENKER_VISION.md`](RENKER_VISION.md)
- ADRs: [`docs/adr/`](docs/adr/) · Versioning: [`docs/VERSIONING.md`](docs/VERSIONING.md)

## License
Proprietary — "All rights reserved" (see [`LICENSE`](LICENSE)). Confirm or change before any distribution.
