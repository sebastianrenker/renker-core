# SECURITY_ATTACKS — renker-core vertical slice

The security boundary is **empirically testable**. Every attack below has an executable
regression test in [`tests/test_security_attacks.py`](tests/test_security_attacks.py) (unless noted).
Run them with `pytest -q tests/test_security_attacks.py`.

The loop for each feature is: builder implements → attacker attempts bypass → failure discovered →
regression test added → fix → repeat. Below, each row is a bypass that is **currently blocked**,
with the test that proves it.

| # | Attack | Attacker goal | Expected | Regression test |
|---|---|---|---|---|
| 1 | **Path traversal** — `drafts/../secret.txt` | escape the scoped directory | DENY, not executed | `test_attack_path_traversal` |
| 2 | **Prefix confusion** — scope `Documents`, target `Documents2/x` | reuse a scope for a sibling dir with a shared string prefix | DENY | `test_attack_prefix_confusion` |
| 3 | **Expired capability** | use a grant past its `expires_at` | DENY (`reason` contains `expired`) | `test_attack_expired_capability` |
| 4 | **Wrong actor (confused deputy)** — agent B uses agent A's grant | act under someone else's authority | DENY | `test_attack_wrong_actor` |
| 5 | **Wrong operation** — read grant, write attempt | escalate read→write | DENY | `test_attack_wrong_operation` |
| 6 | **Wrong target** — grant for `drafts`, request `elsewhere` | act outside the granted path | DENY | `test_attack_wrong_target` |
| 7 | **Revocation mid-lifetime** | keep using a capability after it is revoked | DENY (`reason` contains `revoked`) | `test_attack_revocation_mid_lifetime` |
| 8 | **Malformed actor identity** — `agent` + `../../etc/passwd` | smuggle a path into the actor id | `IdentityError` at construction | `test_attack_malformed_actor_is_rejected` |
| 9 | **Silent decision (no audit)** | perform an action without leaving a trace | every allow/deny emits exactly one audit event; chain verifies | `test_every_decision_produces_audit_event` |
| 10 | **Audit modification** | edit a recorded reason after the fact | `verify()` raises (hash mismatch) | `test_detects_modified_entry` (`test_audit.py`) |
| 11 | **Audit tail truncation** | drop the last decisions | `verify()` raises (head anchor mismatch) | `test_detects_tail_truncation` (`test_audit.py`) |
| 12 | **Audit full deletion** | empty the log but keep the anchor | `verify()` raises | `test_detects_full_deletion` (`test_audit.py`) |
| 13 | **Policy bypass via no grant** | act with no capability at all | DENY (safe default) | `test_deny_no_capability` (`test_policy.py`) |

## Known, documented limitations (attacks NOT closed)

These are intentionally out of scope for this slice and are stated honestly in `docs/THREAT_MODEL.md`:

- **Forged trusted actor.** The caller supplies the `Actor`. renker-core validates its shape and
  matches `granted_to`, but does not cryptographically authenticate it. A caller that fabricates a
  trusted `Actor` is not stopped here.
- **Replay within lifetime.** A valid capability may be reused until it expires or is revoked; there is
  no per-use nonce.
- **Full host compromise.** An attacker who can rewrite **both** the audit log and its `.head` anchor
  can erase history undetectably. The chain is *tamper-evident*, not *tamper-proof*.
- **Bypassing the guard.** Enforcement applies only to actions routed through `GuardedFilesystem`.
  Direct OS calls are not constrained by renker-core.

New bypasses discovered in future sessions should be added here **with a failing test first**, then fixed.
