from __future__ import annotations

import re

import renker_core

EXPECTED_PUBLIC_API = {
    "__version__",
    "PRIMITIVES",
    "Actor",
    "IdentityError",
    "Capability",
    "CapabilityError",
    "PathScope",
    "CapabilityStore",
    "Decision",
    "PolicyResult",
    "evaluate",
    "AuditLog",
    "AuditEvent",
    "AuditError",
    "GuardedFilesystem",
    "GuardResult",
}


def test_all_declares_expected_surface():
    assert set(renker_core.__all__) == EXPECTED_PUBLIC_API


def test_every_public_name_is_importable():
    for name in renker_core.__all__:
        assert hasattr(renker_core, name), name


def test_version_is_semver():
    assert re.fullmatch(r"\d+\.\d+\.\d+", renker_core.__version__)


def test_no_accidental_extra_exports():
    public = {n for n in dir(renker_core) if not n.startswith("_")}
    declared = set(renker_core.__all__) | set(renker_core.PRIMITIVES)
    leaked = public - declared - {"annotations"}
    assert leaked <= {
        "audit",
        "capabilities",
        "identity",
        "integration",
        "policy",
    }
