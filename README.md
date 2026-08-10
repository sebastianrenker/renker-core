# renker-core

> **Renker builds infrastructure for AI systems that can act, learn and communicate without requiring blind trust.**

`renker-core` ist das gemeinsame Fundament der **Renker**-Plattform. Es enthält **nicht** die Business-Logik der einzelnen Produkte, sondern die produktübergreifenden Primitive, gegen die alle drei Säulen entwickeln:

| Säule | Rolle | Repo |
|---|---|---|
| **Rencora** | ACT — Agent Runtime mit Capability Security | [rencora](https://github.com/sebastianrenker/rencora) |
| **RenkerVault** | SECURE — Identity- und Secure-Communication-Layer | [renkervault](https://github.com/sebastianrenker/renkervault) |
| **Continuum** | LEARN — autonome Forschungs- und Discovery-Engine | [continuum](https://github.com/sebastianrenker/continuum) |

Die These der Plattform: Die nächste Generation von KI-Systemen wird nicht daran gemessen, wie intelligent sie ist, sondern daran, wie **kontrollierbar, überprüfbar und vertrauenswürdig** sie beim eigenständigen Handeln ist.

## Die neun Primitive

`identity` · `capabilities` · `permissions` · `events` · `memory` · `tasks` · `audit` · `policy` · `crypto_interface` · `protocol`

Jedes Primitiv liegt als eigenes Unterpaket unter [`renker_core/`](renker_core/) mit eigenem `README.md`. Die Vision (Abschnitt 4.1) skizziert diese als flachen Ordnerbaum; hier sind sie als importierbares Python-Paket `renker_core` realisiert.

Dieser Stand ist ein **Bootstrap** — importierbare, getestete Platzhalter ohne Geschäftslogik. Der nächste Schritt ist die Umsetzung von Identity/Permissions/Audit als lauffähige Module (Monat-1-Meilenstein).

## Dokumentation

- 📖 **Wiki (in-repo):** [`docs/wiki/Home.md`](docs/wiki/Home.md) — Vision, Architektur, Agent-Security, Roadmap, Glossar. *(renker-core ist privat; GitHub-Wikis sind für private Repos im aktuellen Plan nicht verfügbar, daher liegen die Wiki-Seiten als Markdown im Repo.)*
- 🧭 **Vision (Volltext):** [`RENKER_VISION.md`](RENKER_VISION.md)
- 🧱 **Tech-Stack-Entscheidung:** [`docs/adr/0001-tech-stack.md`](docs/adr/0001-tech-stack.md)
- 🔎 **Ist-Zustand-Audit der Produkt-Repos:** [`docs/status/repo-audit.md`](docs/status/repo-audit.md)
- 🔐 **Sicherheitsmodell:** [`SECURITY.md`](SECURITY.md)
- 🤝 **Mitwirken (Builder→Attacker→Reviewer):** [`CONTRIBUTING.md`](CONTRIBUTING.md)

## ⬇️ Renker für Windows herunterladen

Der nutzerseitige Desktop-Agent der Plattform ist **Rencora**. Windows-Installer:
**https://github.com/sebastianrenker/rencora/releases/latest**

## Entwicklung

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
```

## Lizenz

Proprietär — „All rights reserved" (siehe [`LICENSE`](LICENSE)). **Hinweis:** Diese Lizenz wurde als Standard für ein kommerzielles Vorhaben gewählt. Bitte bestätige sie bewusst oder ersetze sie, falls du (ganz oder in Teilen) einen Open-Source-Weg gehen willst — insbesondere für die im Produktportfolio (Vision, Abschnitt 6) vorgesehenen Open-Source-Ebenen.
