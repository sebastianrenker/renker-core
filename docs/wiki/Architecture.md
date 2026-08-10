# Architecture

## Gesamtbild

Die Renker-Plattform trennt bewusst **Primitive** (gemeinsam) von **Business-Logik** (produktspezifisch). Rencora weiß nichts von Continuum-Experimenten und umgekehrt — beide sprechen aber dasselbe Vokabular für „Wer bin ich", „Was darf ich", „Was ist passiert" und „Was ist belegt".

Das vermeidet zwei Fallen:

- **Monolith-Falle:** alles in eine App pressen → Fokusverlust, blockierende Releases.
- **Silo-Falle:** drei getrennte Codebasen, die Sicherheit/Identität dreimal (dreifach fehleranfällig) neu erfinden.

## Die drei Säulen

- **Rencora (ACT):** „A personal AI agent that can actually operate your computer — while being controlled by explicit security boundaries." Kern ist die *kontrollierbare Agent Runtime*, unabhängig vom denkenden LLM.
- **RenkerVault (SECURE):** kein Signal-Ersatz, sondern eine sichere Kommunikations- und Identity-Layer für Agenten und Menschen. Sichert auch Agent-zu-Agent- und Agent-zu-Mensch-Kommunikation. Prinzip: *der Server bekommt so wenig Vertrauen wie möglich* (Relays transportieren idealerweise nur Ciphertext).
- **Continuum (LEARN):** bewusst zurückhaltend als *Autonomous Research & Discovery Engine* positioniert, nicht als „AGI".

## renker-core — das Fundament

Ein viertes Repository, damit die drei Produkte **nicht** eigene, inkompatible Versionen von Identität, Berechtigung und Historie bauen. Die neun Primitive:

| Primitiv | Zweck |
|---|---|
| **Identity** | Überprüfbare Identität für Mensch, Agent, Gerät, Dienst |
| **Permissions** | Capability-Modell, generisch nutzbar |
| **Memory** | Episodisches + semantisches Gedächtnis mit Quellenverweisen |
| **Events** | Append-only Event-Log als Rückgrat für Audit/Reaktivität |
| **Tasks** | Einheitliche Repräsentation von „zu Erledigendem" |
| **Experiments** | Hypothese → Design → Ausführung → Ergebnis |
| **Evidence** | Evidenzstatus-Modell, auch für Rencora-Aktionen |
| **Security** | Bedrohungsmodell, Sandbox-Grenzen, Krypto-Schnittstellen |
| **Audit** | Unveränderliches, abfragbares Protokoll |

(Plus `protocol/` als Wire-Format zwischen Produkten/Geräten.)

## Die Crypto-Boundary

Bewusster Designentscheid: Kryptografie-**Implementierung** wandert *nicht* in Core. `crypto_interface/` enthält nur Schnittstellen. Die echte Implementierung bleibt in einem eigenen, minimalen, streng auditierten Modul auf Basis etablierter Primitive (libsodium/NaCl, Signal-Protokoll) — nie als Eigenentwicklung. So bleibt die Angriffsfläche klein und externe Audits realistisch (siehe [[Agent-Security]]).

## Tech-Stack

renker-core ist in **Python** umgesetzt — Begründung und Alternativen in [`docs/adr/0001-tech-stack.md`](../adr/0001-tech-stack.md). Kurz: die zwei primären Erstkonsumenten (Rencora, Continuum) sind Python; RenkerVault (TS/Tauri) konsumiert über das `protocol/`-Wire-Format.
