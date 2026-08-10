# ADR 0005 — Dependency direction: consumers depend on core, never the reverse

- **Status:** Accepted
- **Date:** 2026-08-10

## Context
The platform has a private foundation (`renker-core`) and public products (`rencora`, `renkervault`,
`continuum`). If core depended on a product, or a product coupled tightly to core internals, the foundation
would stop being reusable and releases would block each other.

## Decision
- `renker-core` depends on **nothing product-specific** and has **zero runtime dependencies** (stdlib only).
- Products depend on core, not the reverse. Today `rencora` consumes core through an **optional, lazy**
  adapter (`core/renker_guard.py`) that degrades to a no-op when core is absent, so rencora's public CI and
  shipped build are unaffected.
- Cross-language consumers (renkervault, TS/Tauri) integrate through a wire `protocol` (planned), not by
  importing Python internals.
- Only the names in `renker_core.__all__` are public API; everything else is internal.

## Consequences
- Core stays small, auditable, and independently testable.
- The trade-off: enforcement in the shipped rencora `.exe` is currently a no-op because core is not bundled
  there. Making core installable to rencora (a public authz subset — "Option B") is the path to real
  enforcement in distribution, and is deliberately deferred.
