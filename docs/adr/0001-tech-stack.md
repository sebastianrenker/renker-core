# ADR 0001 — Tech-Stack für renker-core

- **Status:** Akzeptiert
- **Datum:** 2026-08-10
- **Entscheider:** Sebastian Renker (Architekt, letzte Instanz)

## Kontext

`renker-core` ist das gemeinsame Fundament für die drei Produktsäulen der Renker-Plattform. Es muss von allen dreien konsumierbar sein, ohne deren Business-Logik zu enthalten. Die Sprachwahl soll die Reibung für die *primären* Konsumenten der ersten Primitive (Identity, Permissions, Audit — Vision, Abschnitt 14) minimieren.

Ist-Zustand der drei bestehenden Produkt-Repos (verifiziert am 2026-08-10, Details in [`../status/repo-audit.md`](../status/repo-audit.md)):

| Repo | Sprache/Stack |
|---|---|
| **rencora** (ACT) | Python (`requirements.txt`, `main.py`, PyInstaller via `main.spec`) |
| **continuum** (LEARN) | Python (`pyproject.toml`, `src/`) |
| **renkervault** (SECURE) | TypeScript/React + Tauri (Rust) Client, Node.js Relay-Server |

Der Stack ist also **nicht** vollständig einheitlich: zwei von drei Repos sind Python, eines ist TypeScript/Rust.

## Entscheidung

**renker-core wird in Python (>=3.10) umgesetzt.**

Begründung:

1. **Primäre Konsumenten sind Python.** Die ersten konkret benötigten Primitive (Identity, Permissions, Audit) dienen zuerst Rencora — und Rencora ist Python. Continuum, der zweite große Konsument von Memory/Evidence/Experiments, ist ebenfalls Python.
2. **Mehrheit + Charakter des Codes.** Zwei der drei Repos sind Python, und es sind genau die agenten- und reasoning-lastigen (ACT, LEARN). Die Vision-Heuristik lautet: „Python, wenn ML-/Agent-Reasoning-Bausteine dominieren" — das trifft hier zu.
3. **Interoperabilität statt Monosprache.** renker-core definiert produktübergreifend auch ein `protocol/`-Wire-Format. Die eigentliche produktübergreifende Kompatibilität läuft über dieses Format, nicht über eine gemeinsame Implementierungssprache. RenkerVault (TS/Rust) konsumiert die Primitive daher über das Protokoll/Schema, nicht durch direkten Python-Import.

## Betrachtete Alternativen

- **TypeScript/Node.js.** Vorteil: RenkerVault ist bereits TS, und die Vision-Heuristik nennt TS für „plattformübergreifende CLI-/Browser-/OS-Automatisierung". Nachteil: Die zwei primären, zuerst zu bedienenden Konsumenten (rencora, continuum) sind Python; ein TS-Core würde für sie eine Sprachgrenze bei jedem Aufruf einziehen. **Abgelehnt**, weil es die Reibung bei den unmittelbaren Meilensteinen erhöht.
- **Rust.** Vorteil: Nähe zum Tauri-Teil von RenkerVault, starke Sicherheitsgarantien für ein sicherheitskritisches Fundament. Nachteil: höchste Einstiegs- und Iterationskosten in einer Phase, in der schnelle, testgetriebene Iteration zählt; keiner der Python-Konsumenten profitiert direkt. **Zurückgestellt** — bleibt eine Option für ein späteres, eng abgegrenztes `renker-crypto`-Modul.

## Konsequenzen

- **Positiv:** rencora und continuum können renker-core direkt importieren; schnelle Iteration; einheitliches Test-/Lint-Tooling (`pytest`, `ruff`).
- **Negativ / zu beachten:** RenkerVault kann renker-core nicht direkt importieren. Die produktübergreifende Grenze verläuft über `protocol/` (Wire-Format/Schema). Sobald RenkerVault Primitive direkt braucht, muss entweder ein sprachneutrales Schema (z. B. JSON Schema / Protobuf) oder ein dünner Sprach-Port gepflegt werden.
- **Krypto bleibt außen vor.** `crypto_interface/` enthält nur Interfaces; die Implementierung bleibt bewusst außerhalb dieses Repos (Vision, Abschnitt 4.3), was die Sprachwahl von renker-core für die Krypto-Sicherheit irrelevant macht.
