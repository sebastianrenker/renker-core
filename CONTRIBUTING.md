# Mitwirken an renker-core

`renker-core` ist das sicherheitskritische Fundament der Renker-Plattform. Beiträge folgen einem bewusst strengen Ablauf.

## Grundregeln

- **Kein Code-Kommentar-Stil.** Code in diesem Repo enthält keine Inline-Kommentare, Docstrings, JSDoc oder `TODO`-Marker. Verständlichkeit entsteht durch klare Benennung. Dokumentation gehört in `README.md`-Dateien, ADRs und das Wiki.
- **Keine Secrets committen.** Keine API-Keys, Tokens oder `.env`-Dateien.
- **Kein Force-Push** auf gemeinsame Branches.
- **Tests und Lint müssen grün sein** (`pytest`, `ruff check`), bevor gemergt wird.

## Der Builder → Attacker → Reviewer-Zyklus

Für **sicherheitsrelevante Änderungen** — alles unter `renker_core/permissions/`, `renker_core/capabilities/` und `renker_core/crypto_interface/` — reicht „Builder → fertig" **nicht**. Diese Änderungen durchlaufen immer:

1. **Builder** — implementiert das Feature mit klarer Definition of Done.
2. **Attacker** — bekommt explizit den Auftrag, das Feature zu **brechen** (z. B. „umgehe mit einer manipulierten Website-Payload eine Capability-Grenze"). Das ist kein normaler Code-Review, sondern eine gezielte Angriffssimulation.
3. **Reviewer** — bewertet Implementierung und Angriffsergebnisse und entscheidet über Nachbesserungen.
4. **Test Generator** — leitet aus dem Gegenbeispiel dauerhafte Regressionstests ab.
5. **Human Decision** — Policy-Entscheidungen (z. B. „Was zählt als kritisches Risiko?") bleiben beim Menschen als letzter Instanz.

Details siehe `RENKER_VISION.md`, Abschnitt 11.

## Crypto-Boundary

In `renker_core/crypto_interface/` werden **ausschließlich Schnittstellen** definiert — niemals kryptografische Implementierungen. Siehe `renker_core/crypto_interface/README.md` und `SECURITY.md`.
