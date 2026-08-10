# Ist-Zustand-Audit der Renker-Produkt-Repos

- **Datum:** 2026-08-10
- **Owner:** `sebastianrenker`
- **Methode:** README, Manifest und Ordnerbaum bis Tiefe 2 gelesen. `rencora` und `continuum` shallow-geklont (read-only), `renkervault` lokal vorhanden (read-only). Wo etwas unklar blieb, ist es unten so markiert.

> Ehrliche Bestandsaufnahme, keine Bewertung des Codes selbst. „Vorhanden" heißt: es existiert ein Modul/Ordner, der dem Primitiv thematisch entspricht — nicht, dass es die renker-core-Schnittstelle bereits erfüllt.

## rencora — ACT (Agent Runtime)

- **Zustand:** remote vorhanden (public), **nicht** lokal → shallow geklont zur Inspektion.
- **Sprache/Stack:** Python. `requirements.txt`, `main.py`, `ui.py`, `setup.py`. Windows-Build via **PyInstaller** (`main.spec`, `build.bat` → `dist/RENCORA/RENCORA.exe`). GitHub-Actions-Workflow `build.yml` vorhanden (baut EXE auf Tag `v*`, lädt sie als **Artefakt** hoch — **kein** GitHub Release, **kein** Installer).
- **Reife:** deutlich fortgeschritten. `core/` (u. a. `policy.py`, `secrets.py`, `llm_client.py`, `logging_config.py`, `dpapi.py`, `tunnel.py`), `agents/` (`planner_agent`, `qa_agent`, `router`), umfangreiches `actions/` (OS-Steuerung: Dateien, Browser, System, Gestensteuerung u. v. m.), `tests/`, `dashboard/`, `database/`.

| Primitiv | Status in rencora |
|---|---|
| Identity | unklar, manuell prüfen (kein dediziertes Modul erkennbar) |
| Permissions | **teilweise** — `core/policy.py` vorhanden; Deckung mit Capability-Modell unklar, manuell prüfen |
| Memory | **teilweise** — `actions/second_brain.py` deutet auf Gedächtnis hin; manuell prüfen |
| Events | unklar, manuell prüfen (`core/logging_config.py` als Nachbarschaft) |
| Tasks | **teilweise** — `agents/planner_agent.py`, `actions/task_planner.py` |
| Experiments | nicht erkennbar |
| Evidence | nicht erkennbar |
| Security | **teilweise** — `core/secrets.py`, `core/dpapi.py`, `SECURITY.md` |
| Audit | unklar, manuell prüfen (Logging vorhanden, Append-only/Hash-Chain unklar) |

## continuum — LEARN (Research Engine)

- **Zustand:** remote vorhanden (public), **nicht** lokal → shallow geklont zur Inspektion.
- **Sprache/Stack:** Python. `pyproject.toml`, `src/continuum/`. CI-Workflow `ci.yml` vorhanden. README-Badge nennt **MIT-Lizenz** (Abweichung zur proprietären Default-Empfehlung — bewusst so beim Owner).
- **Reife:** sauber strukturierter Phase-0-Prototyp; README markiert den Status ausdrücklich als „Konzept-/Architektur-Prototyp, kein validiertes Ergebnis". Submodule: `data`, `eval`, `hypothesis`, `learning`, `llm`, `memory`, `safety`, `verification`, `worldmodel`.

| Primitiv | Status in continuum |
|---|---|
| Identity | nicht erkennbar |
| Permissions | nicht erkennbar |
| Memory | **vorhanden** — `src/continuum/memory/` |
| Events | unklar, manuell prüfen |
| Tasks | unklar, manuell prüfen |
| Experiments | **vorhanden** — `hypothesis/` + `worldmodel/` + `learning/` bilden die Experiment-Pipeline |
| Evidence | **vorhanden** — `verification/` + `eval/` entsprechen dem Evidenzstatus-Modell |
| Security | **teilweise** — `src/continuum/safety/` |
| Audit | unklar, manuell prüfen |

## renkervault — SECURE (Identity / Secure Communication)

- **Zustand:** **lokal** vorhanden (Geschwisterordner) **und** remote (public) → read-only.
- **Sprache/Stack:** TypeScript/React + **Tauri** (Rust) für den Desktop-Client (`client/` mit `src-tauri`, `vite.config.ts`, `@noble/*`-Krypto, `@noble/post-quantum`), **Node.js** Relay-Server (`server/`). **Kein** `.github/workflows`.
- **Reife:** funktionierender E2E-Prototyp mit Krypto-Fokus. `client/src/`: `crypto/`, `net/`, `state/`, `ui/`. `deploy/` (Caddyfile, systemd-Unit, Tor-Snippet), `installer/` (Inno-Setup-Skript), `docs/`.

| Primitiv | Status in renkervault |
|---|---|
| Identity | **teilweise** — Geräteidentität/Sessions im Krypto-Client; manuell prüfen |
| Permissions | nicht erkennbar |
| Memory | nicht erkennbar |
| Events | nicht erkennbar |
| Tasks | nicht erkennbar |
| Experiments | nicht erkennbar |
| Evidence | nicht erkennbar |
| Security | **vorhanden (Schwerpunkt)** — `client/src/crypto/` (`@noble/ciphers`, `@noble/curves`, `@noble/post-quantum`), `SECURITY.md` |
| Audit | nicht erkennbar |

## Windows-Installer — Befund (Vision, Schritt 5.1)

Gezielte Inspektion des Windows-Release-Wegs von `renkervault`:

- **Build-Konfiguration:** Tauri-Client (`client/src-tauri`). Der Tauri-Bundler erzeugt beim `tauri build` selbst Windows-Installer (NSIS `-setup.exe` und WiX `.msi`). Zusätzlich liegt im Repo ein **Inno-Setup-Skript** `installer/RenkerVault.iss`, das die gebaute `renkervault.exe` (plus optional den Relay-Server) zu einem Setup verpackt (`ISCC.exe installer\RenkerVault.iss`).
- **CI-Workflow:** **keiner** — `renkervault` hat kein `.github/workflows`. Der Installer wird lokal gebaut und manuell veröffentlicht.
- **GitHub Release:** vorhanden — `v0.1.0` „RenkerVault 0.1.0" mit echten, herunterladbaren Assets:
  - `RenkerVault_0.1.0_x64-setup.exe` (1.974.745 Bytes) — Tauri/NSIS-Installer
  - `RenkerVault_0.1.0_x64_en-US.msi` (2.977.792 Bytes) — Tauri/WiX-Installer
  - `SHA256SUMS.txt`

**Schlussfolgerung für die Übertragung auf rencora (Schritt 5.2):** Der *tatsächlich ausgelieferte* Installer stammt vom Tauri-Bundler — dieser ist an das Tauri-Framework gebunden und lässt sich **nicht** auf eine Python/PyInstaller-App übertragen. Das im renkervault-Repo ebenfalls vorhandene, framework-**neutrale** Installer-Tooling ist **Inno Setup** (`.iss`, kompiliert mit `ISCC.exe`). Dieses wird auf rencora übertragen: eine Inno-Setup-`.iss`, die die bestehende PyInstaller-Ausgabe (`dist/RENCORA/`) verpackt, plus ein CI-Release-Workflow, der auf einen `v*`-Tag hin baut, das Setup kompiliert und als Asset an ein GitHub Release hängt. rencoras bestehende `build.yml` bleibt unangetastet; es wird nur additiv ergänzt.

### Ergebnis der Übertragung auf rencora (Schritt 5.2–5.4)

- **Übernommenes Tooling:** Inno Setup (`ISCC.exe`), analog zu `renkervault/installer/RenkerVault.iss`.
- **Ergänzt (nur additiv, keine bestehende Datei geändert):** `installer/Rencora.iss` und `.github/workflows/release-windows.yml` im rencora-Repo.
- **Release/Asset-Status:** siehe Abschlusszusammenfassung der Session bzw. `https://github.com/sebastianrenker/rencora/releases`.
