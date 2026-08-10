# Working with Claude Code

Der eigentliche Hebel liegt nicht nur im Produkt, sondern in der Art, wie es gebaut wird: Trial-and-Error wird zu einem systematischen Prozess.

## Die Grundschleife

```
DU (Hypothese)
   ↓
CLAUDE (Implementierung)
   ↓
AUTOMATISIERTE TESTS
   ├── PASS → fertig
   └── FAIL → CLAUDE ATTACKER → GEGENBEISPIEL → CLAUDE FIX → (zurück zu den Tests)
```

## Erweiterte Schleife für sicherheitskritische Bausteine

Für alles unter `permissions/`, `capabilities/`, `crypto_interface/` (und die RenkerVault-Krypto-Schicht) gilt nie „Builder → fertig", sondern:

```
Builder Agent → Attacker Agent → Reviewer Agent → Test Generator → Human Decision
```

## Konkrete Praxis

1. **Jede Aufgabe bekommt eine klare Definition of Done**, bevor Code geschrieben wird — abgeleitet aus der [[Roadmap]].
2. **Sicherheitsrelevante Änderungen** durchlaufen immer den Builder→Attacker→Reviewer-Zyklus.
3. **Der Attacker-Agent** bekommt explizit den Auftrag, das Feature zu *brechen* (z. B. „umgehe mit einer manipulierten Website-Payload eine Capability-Grenze"). Das ist mehr als ein Code-Review.
4. **Du bleibst Architekt und letzte Instanz** — besonders bei Policy-Entscheidungen wie „Was zählt als kritisches Risiko?". Das ist eine Produkt-/Wertentscheidung.
5. **`RENKER_VISION.md`** liegt als Referenzdatei in den Repos, damit Architekturfragen nicht in jeder Session neu erfunden werden.

Siehe auch [`CONTRIBUTING.md`](../../CONTRIBUTING.md).
