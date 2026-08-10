# crypto_interface

**Primitiv:** Crypto-Boundary (Teil von Security)

**Zweck:** Definiert **ausschließlich Schnittstellen und Typen** für kryptografische Operationen (`Encryptor`, `Signer`, `Verifier`) — z. B. „verschlüssle diesen Payload für diesen Empfänger" oder „verifiziere diese Signatur". Es wird hier **keine** kryptografische Implementierung abgelegt.

> ⚠️ **Wichtiger Sicherheitshinweis — keine eigene Kryptografie implementieren.**
> Die tatsächliche Krypto-Implementierung gehört in ein separates, minimales, streng auditiertes Modul (idealerweise unter RenkerVault oder einem eigenen `renker-crypto`-Repo), gebaut auf etablierten, geprüften Primitiven wie **libsodium/NaCl** oder Signal-Protokoll-Bausteinen — niemals als Eigenentwicklung. Die Trennung von Interface und Implementierung hält die Angriffsfläche klein und macht externe Audits realistisch (siehe Vision, Abschnitt 4.3).

**Genutzt von:** primär RenkerVault; die Interfaces sind produktübergreifend nutzbar.

> Sicherheitsrelevantes Modul. Änderungen hier durchlaufen den Builder→Attacker→Reviewer-Zyklus aus `CONTRIBUTING.md`.

**Hinweis zur Struktur:** Die Vision (Abschnitt 4.1) notiert diesen Ordner als `crypto-interface/`. Da Python-Importpfade keinen Bindestrich zulassen und die Vorgabe „lauffähig importierbar" lautet, ist er hier als `crypto_interface/` umgesetzt.
