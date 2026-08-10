from __future__ import annotations

PRIMITIVE = "capabilities"

CAPABILITY_FIELDS = (
    "permission",
    "scope",
    "lifetime",
    "audit_trail",
    "approval_policy",
    "revocation",
)

__all__ = ["PRIMITIVE", "CAPABILITY_FIELDS"]
