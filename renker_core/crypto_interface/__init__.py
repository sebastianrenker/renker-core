from __future__ import annotations

from typing import Protocol, runtime_checkable

PRIMITIVE = "crypto_interface"


@runtime_checkable
class Encryptor(Protocol):
    def encrypt(self, plaintext: bytes, recipient: str) -> bytes:
        """Encrypt ``plaintext`` for ``recipient``."""

    def decrypt(self, ciphertext: bytes, recipient: str) -> bytes:
        """Decrypt ``ciphertext`` addressed to ``recipient``."""


@runtime_checkable
class Signer(Protocol):
    def sign(self, payload: bytes, key_id: str) -> bytes:
        """Sign ``payload`` with the key identified by ``key_id``."""


@runtime_checkable
class Verifier(Protocol):
    def verify(self, payload: bytes, signature: bytes, key_id: str) -> bool:
        """Return True if ``signature`` is valid for ``payload`` under ``key_id``."""


__all__ = ["PRIMITIVE", "Encryptor", "Signer", "Verifier"]
