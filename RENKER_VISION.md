# RENKER — Trusted Infrastructure for Autonomous AI
**Konzeptdokument v1.0**
Stand: 9. August 2026 · Autor: Sebastian Renker · Ausgearbeitet mit Claude

> **Hinweis zur Faktengrundlage:** Dieses Dokument stützt sich auf die von dir beschriebenen Projekteigenschaften von Rencora, Continuum und RenkerVault sowie auf die vorherige gemeinsame Analyse. Konkrete Repository-Details (Code, Dateistruktur, Commit-Historie) wurden in dieser Sitzung nicht erneut verifiziert. Alle technischen Vorschläge unten sind als **Zielarchitektur / Vorschlag** zu lesen, nicht als Bestandsaufnahme des aktuellen Codes. Bevor Claude Code daran arbeitet, sollte der tatsächliche Ist-Zustand der drei Repos gegen dieses Dokument abgeglichen werden (siehe Abschnitt 14).

---

## 0. Executive Summary

Renker ist kein Portfolio aus drei unabhängigen Projekten, sondern eine Plattform mit einer These:

> **Die nächste Generation von KI-Systemen wird nicht daran gemessen, wie intelligent sie ist, sondern daran, wie kontrollierbar, überprüfbar und vertrauenswürdig sie beim eigenständigen Handeln ist.**

Drei Produktsäulen bedienen diese These aus unterschiedlichen Richtungen:

| Säule | Rolle | Kernfrage |
|---|---|---|
| **Rencora** (ACT) | Agent Runtime mit Capability Security | Was darf ein Agent tun, und wie wird das durchgesetzt? |
| **RenkerVault** (SECURE) | Identity- und Secure-Communication-Layer | Wem kann ein Agent vertrauen, und wie bleiben Daten dabei geschützt? |
| **Continuum** (LEARN) | Autonome Forschungs- und Discovery-Engine | Wie wird aus Beobachtung geprüftes Wissen — ohne Halluzination als Fakt zu verkaufen? |

Alle drei teilen sich ein gemeinsames Fundament, **`renker-core`**, das nicht die Business-Logik der Produkte enthält, sondern die gemeinsamen Primitive: Identity, Permissions, Memory, Events, Tasks, Experiments, Evidence, Audit.

Kommerziell liegt der stärkste kurzfristige Hebel nicht im Consumer-Bereich, sondern in **Agent Security für Unternehmen** — einem Markt, der durch die Verbreitung autonomer KI-Agenten gerade erst entsteht. Das Geschäftsmodell ist B2B/SaaS mit gestaffelten Tarifen; realistische Zielgrößen liegen im niedrigen bis mittleren einstelligen Millionenbereich ARR bei 100–500 zahlenden Unternehmen — nicht bei Millionen Endnutzern.

Der nächste Meilenstein ist nicht ein Umsatzziel. Er ist: **ein einzelner unabhängiger Nutzer, der freiwillig zahlt.**

---

## 1. Die Vision

**Leitsatz:**

> *Renker builds infrastructure for AI systems that can act, learn and communicate without requiring blind trust.*

Die zentrale Frage der nächsten KI-Generation ist nicht mehr primär „Wie intelligent ist das Modell?", sondern:

> „Wie viel darf dieses System selbstständig tun, und wie können wir ihm dabei vertrauen?"

Genau an diesem Punkt treffen sich die drei Projekte. Rencora gibt Agenten Handlungsfähigkeit *innerhalb kontrollierter Grenzen*. RenkerVault sorgt dafür, dass die Kommunikation zwischen Mensch, Agent und Dienst dabei nicht kompromittierbar wird. Continuum sorgt dafür, dass ein lernendes System seine eigenen Ausgaben nicht unkontrolliert als Wahrheit fortschreibt.

Das Unternehmen dahinter heißt **Renker** — nicht Rencora. Rencora ist ein Produkt der Firma Renker, kein Synonym dafür.

```
                         RENKER
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
       RENCORA         CONTINUUM       RENKERVAULT
          │                │                │
        ACT              LEARN           SECURE
          │                │                │
          └────────────────┼────────────────┘
                           │
                           ▼
                TRUSTED AI INFRASTRUCTURE
```

---

## 2. Plattformarchitektur — Gesamtbild

```
                    RENKER PLATFORM
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
    Identity            Security            Memory
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
             ┌─────────────┼─────────────┐
             │             │             │
          Rencora       Continuum    RenkerVault
             │             │             │
           ACT           LEARN         SECURE
```

Wichtig ist die Trennlinie: Die drei Produkte teilen sich **Primitive**, nicht **Business-Logik**. Rencora weiß nichts von Continuum-Experimenten, Continuum weiß nichts von Rencora-Tool-Calls. Beide sprechen aber dasselbe Vokabular für „Wer bin ich", „Was darf ich", „Was ist passiert" und „Was ist belegt".

Das verhindert zwei typische Fehler beim Bau einer Plattform aus mehreren Projekten:

1. **Monolith-Falle** — alles in eine App zu pressen, wodurch jedes Produkt an Fokus verliert und Releases sich gegenseitig blockieren.
2. **Silo-Falle** — drei komplett getrennte Codebasen, die Sicherheits- und Identitätskonzepte dreimal unterschiedlich (und dreimal fehleranfällig) neu erfinden.

---

## 3. Die drei Säulen im Detail

### 3.1 Rencora → ACT: Agent Runtime mit Capability Security

**Positionierung:** Nicht „ein weiterer KI-Assistent" (übersättigter Markt), sondern:

> *A personal AI agent that can actually operate your computer — while being controlled by explicit security boundaries.*

```
                 RENCORA
                    │
        ┌───────────┼───────────┐
        │           │           │
       THINK       SEE         ACT
        │           │           │
       LLM       Vision      Tools
        │           │           │
        └───────────┼───────────┘
                    │
               PERMISSION
                  LAYER
                    │
             ┌──────┴──────┐
             │             │
          Allowed       Blocked
             │
             ▼
            OS
```

Der differenzierende Baustein ist **Capability Security**: Rencora besitzt niemals pauschal „Terminalzugriff" oder „Dateisystemzugriff". Jede Fähigkeit ist ein einzeln erteiltes, einzeln widerrufbares Objekt:

```
Agent
 │
 ├── filesystem.read      (scope: ~/Documents/**)
 ├── filesystem.write     (scope: ~/Documents/drafts/**)
 ├── process.execute      (scope: allowlist von Binaries)
 ├── network.request      (scope: allowlist von Domains)
 ├── browser.control      (scope: aktiver Tab)
 ├── camera.read          (scope: nie ohne explizite Freigabe)
 └── microphone.read      (scope: nie ohne explizite Freigabe)
```

Jede Capability trägt sechs Eigenschaften:

- **Permission** — welche Aktion genau erlaubt ist (nicht „Dateisystem", sondern „lesend, unter diesem Pfad-Prefix").
- **Scope** — die konkrete Grenze (Pfad, Domain, Prozessname).
- **Lifetime** — Ablaufzeit oder Sitzungsbindung; keine Capability lebt standardmäßig für immer.
- **Audit Trail** — jede Nutzung wird protokolliert, unveränderlich und nachvollziehbar.
- **Approval Policy** — automatisch erlaubt, automatisch verweigert oder menschliche Freigabe erforderlich, abhängig vom Risiko.
- **Revocation** — jede Capability kann jederzeit sofort entzogen werden, auch mitten in einer laufenden Aktion.

Aus einem „KI-Agenten" wird damit eine **kontrollierbare Agent Runtime** — und genau diese Runtime ist der eigentliche Produktkern, unabhängig davon, welches LLM gerade „denkt".

### 3.2 RenkerVault → SECURE: Identity- und Secure-Communication-Layer

**Harte Entscheidung vorab:** RenkerVault tritt nicht an, um Signal zu ersetzen. Der kommerzielle Wert liegt nicht in „Wir haben einen eigenen Messenger", sondern in:

> *Wir bauen eine sichere Kommunikations- und Identity-Layer für Agenten und Menschen.*

Damit wird RenkerVault Infrastruktur statt Endnutzerprodukt:

```
Human
  │
Agent
  │
Service
  │
Device
  │
  ▼
Renker Secure Identity
       │
       ├── E2E encryption
       ├── device identity
       ├── key management
       ├── secure sessions
       ├── metadata minimization
       └── encrypted transport
```

Der entscheidende neue Anwendungsfall: RenkerVault sichert nicht nur Mensch-zu-Mensch-Kommunikation, sondern **Agent-zu-Agent- und Agent-zu-Mensch-Kommunikation**:

```
Rencora on Laptop
       │
       │ encrypted
       ▼
Rencora on Phone
       │
       │ encrypted
       ▼
Rencora Cloud / Relay
```

Designprinzip: **der Server bekommt so wenig Vertrauen wie möglich.** Relay-Knoten sollen im Idealfall Ciphertext transportieren, ohne Inhalte, Metadaten oder Beziehungsgraphen in nutzbarer Form zu sehen.

### 3.3 Continuum → LEARN: Autonome Forschungs- und Discovery-Engine

**Positionierung bewusst zurückhaltend:** nicht „AGI", sondern:

> *Autonomous Research & Discovery Engine.*

Die Pipeline:

```
Observation → Memory → World Model → Hypothesis Generation
    → Experiment Design → Execution → Measurement
    → Verification → Knowledge Update → (nächste Iteration)
```

Der wichtigste Baustein ist ein **Evidenzstatus-Modell**, das verhindert, dass das System seine eigenen Halluzinationen irgendwann als „Wissen" abspeichert:

```
HYPOTHESIS
    │
    ├── proposed                    (noch ungeprüft)
    ├── simulated                   (im Modell getestet)
    ├── experimentally tested       (real getestet, einmalig)
    ├── independently reproduced    (von unabhängigem Lauf bestätigt)
    └── validated                   (belastbar, referenzierbar)
```

Jede Behauptung im System trägt ihren Evidenzstatus sichtbar mit sich. Ein „proposed"-Ergebnis darf nie wie ein „validated"-Ergebnis präsentiert oder weiterverwendet werden — das ist eine harte Systemregel, keine Empfehlung.

---

## 4. Das gemeinsame Fundament: `renker-core`

### 4.1 Warum ein viertes Repository

Rencora, RenkerVault und Continuum sollen **nicht** ihre eigenen, inkompatiblen Versionen von „Wer bin ich", „Was ist erlaubt" und „Was ist passiert" bauen. Ein viertes Repository, `renker-core`, wird zur gemeinsamen Foundation — kein weiteres Endnutzerprodukt, sondern eine Library/ein Service, gegen die die drei Produkte entwickeln.

```
renker-core/
├── identity/          # wer ist ein Akteur (Mensch, Agent, Gerät, Service)
├── capabilities/       # Capability-Definitionen & -Schemas
├── permissions/         # Policy-Auswertung, Approval-Flows
├── events/               # Event-Bus / Event-Log (append-only)
├── memory/                # gemeinsames Gedächtnismodell (episodisch/semantisch)
├── tasks/                  # Task-/Job-Repräsentation über alle Produkte hinweg
├── audit/                   # unveränderliches Audit-Log, Query-API
├── policy/                    # Policy Engine (Risk-Rules, Approval-Rules)
├── crypto-interface/            # NUR Schnittstellen, keine Krypto-Implementierung
└── protocol/                      # Wire-Format zwischen Produkten/Geräten
```

Nutzung:

```
Rencora     ↓ renker-core
Continuum   ↓ renker-core
RenkerVault ↓ renker-core
```

### 4.2 Die neun gemeinsamen Primitive

| Primitiv | Zweck | Genutzt von |
|---|---|---|
| **Identity** | Eindeutige, überprüfbare Identität für Mensch, Agent, Gerät, Dienst | alle drei |
| **Permissions** | Capability-Modell aus Abschnitt 3.1, generisch nutzbar | Rencora primär, Continuum für Tool-Zugriffe |
| **Memory** | Episodisches + semantisches Gedächtnis mit Quellenverweisen | Rencora, Continuum |
| **Events** | Append-only Event-Log als Rückgrat für Audit und Reaktivität | alle drei |
| **Tasks** | Einheitliche Repräsentation von „etwas, das erledigt werden soll" | alle drei |
| **Experiments** | Struktur für Hypothese → Design → Ausführung → Ergebnis | primär Continuum |
| **Evidence** | Das Status-Modell aus Abschnitt 3.3, aber generisch: auch Rencora-Aktionen können „belegt" oder „unbelegt" sein | alle drei |
| **Security** | Bedrohungsmodell, Sandbox-Grenzen, Krypto-Schnittstellen (nicht die Implementierung selbst) | primär RenkerVault |
| **Audit** | Unveränderliches, abfragbares Protokoll jeder sicherheitsrelevanten Aktion | alle drei |

### 4.3 Die Crypto-Boundary — bewusst *nicht* Teil von Core

Ein wichtiger Designentscheid: **Kryptografie-Implementierung wandert nicht einfach ins gemeinsame Core-Paket.** `renker-core/crypto-interface` definiert nur Schnittstellen (z. B. „verschlüssle diesen Payload für diesen Empfänger", „verifiziere diese Signatur"). Die tatsächliche kryptografische Implementierung bleibt:

- in einem eigenen, minimalen, auditierbaren Modul (idealerweise unter RenkerVault oder einem eigenen `renker-crypto`-Repo),
- gebaut auf etablierten, geprüften Primitiven (z. B. libsodium/NaCl, Signal-Protokoll-Bausteine) statt Eigenentwicklung,
- mit eigenem, strengerem Review-Prozess als der Rest der Plattform.

Begründung: Vermischt man Kryptografie mit allgemeiner Plattform-Logik, wird jede spätere Änderung an Core automatisch zu einem sicherheitskritischen Ereignis. Die Trennung hält die Angriffsfläche für Krypto-Bugs klein und macht externe Audits realistisch günstiger.

---

## 5. Agent Security als eigenständiges Produkt

Dies ist potenziell der wirtschaftlich stärkste kurzfristige Baustein der gesamten Plattform.

**Das Kernproblem:** KI-Agenten bekommen zunehmend mehr Berechtigungen. Was passiert, wenn ein Agent manipuliert wird?

```
Website → Prompt Injection → AI Agent → Tool Call → "Upload ~/.ssh/"
```

**Die Antwort der Plattform:**

```
REQUEST → POLICY ENGINE → Risk Assessment → Permission
   → Sandbox → Execution → Audit
```

Bei gefährlichen Aktionen:

```
Agent: "Delete database"
Policy: HIGH RISK
→ DENY   oder   → HUMAN APPROVAL
```

### 5.1 Skizze eines Permission-Objekts (Vorschlag, nicht Ist-Zustand)

```json
{
  "capability": "filesystem.write",
  "scope": "~/Documents/drafts/**",
  "grantedBy": "user:sebastian",
  "grantedTo": "agent:rencora-session-8f2c",
  "issuedAt": "2026-08-09T10:00:00Z",
  "expiresAt": "2026-08-09T11:00:00Z",
  "approvalPolicy": "auto",
  "riskTier": "low",
  "revocable": true,
  "auditRequired": true
}
```

### 5.2 Skizze eines Audit-Log-Eintrags

```json
{
  "eventId": "evt_9a31...",
  "timestamp": "2026-08-09T10:14:02Z",
  "actor": "agent:rencora-session-8f2c",
  "action": "filesystem.write",
  "target": "~/Documents/drafts/report.md",
  "capabilityRef": "cap_5521...",
  "riskAssessment": "low",
  "decision": "allowed",
  "outcome": "success",
  "chainHash": "sha256:..."
}
```

Ein solches Log sollte **append-only** sein (kryptografisch verkettet, z. B. per Hash-Chain), damit auch ein kompromittierter Agent seine eigenen Spuren nicht nachträglich verwischen kann.

### 5.3 Risikostufen als Grundlage der Policy Engine

| Risikostufe | Beispielaktionen | Standardverhalten |
|---|---|---|
| **Niedrig** | Datei lesen in erlaubtem Scope, Web-Recherche in Allowlist | automatisch erlaubt, protokolliert |
| **Mittel** | Datei außerhalb bekannter Scopes schreiben, neue Domain kontaktieren | automatisch erlaubt mit Warnung, oder Freigabe nach Policy |
| **Hoch** | Zugriff auf Zugangsdaten/Schlüssel, Löschoperationen, Zahlungsauslösung | grundsätzlich menschliche Freigabe erforderlich |
| **Kritisch** | Zugriff auf `.ssh`, Produktionsdatenbanken, irreversible Löschung | standardmäßig verweigert, nur mit explizitem Override |

Aus diesem Baustein könnte perspektivisch ein eigenständiges Produkt werden: **Renker Agent Security** — *Security layer for autonomous AI agents.* Das ist wahrscheinlich kommerziell interessanter als ein Consumer-Messenger, weil der Schaden, den es verhindert, unmittelbar in Euro messbar ist (siehe Abschnitt 7).

---

## 6. Produktportfolio

| Ebene | Produkt | Zielgruppe |
|---|---|---|
| **Free / Open Source** | Rencora Core, RenkerVault Protocol, Continuum Research Framework | Community, Forschung, Reputation, Vertrauen durch Transparenz |
| **Developer** | Renker SDK (Capabilities → Policy → Secure Execution → Audit als Bausteine) | Entwickler, die eigene Agenten sicher bauen wollen |
| **Enterprise** | Renker Agent Security Platform: Agent Identity, Permissions, Sandboxing, Policy Engine, Audit, Secret Management, Secure Communication, Deployment, Compliance | Unternehmen mit produktiven KI-Agenten |
| **Research** | Continuum Research Platform: Hypothesengenerierung, Experimentplanung, wissenschaftliches Gedächtnis, Verifikation, Evaluation, menschliche Aufsicht | Institutionen, Labore, Forschungsteams |

Die Open-Source-Ebene ist kein Nebenprodukt, sondern strategisch: Sie erzeugt Vertrauen (Code ist prüfbar), Reputation (Community, Sichtbarkeit) und einen Trichter in die kommerziellen Tarife.

---

## 7. Geschäftsmodell

**Grundprinzip:** B2B statt Consumer-Masse. Kein Wettrennen um Millionen Nutzer und Werbeerlöse.

| Tarif | Preis | Zielgruppe |
|---|---|---|
| Developer | €0–49 / Monat | Einzelentwickler, kleine Projekte |
| Pro | €100–500 / Monat | kleine Teams, Startups |
| Business | €1.000–10.000 / Monat | mittelständische Unternehmen mit produktiven Agenten |
| Enterprise | individuelle Verträge | große Organisationen, Compliance-Anforderungen |
| Research | individuelle Verträge | Institutionen, Labore |

**Rechenbeispiele (Zielszenarien, ausdrücklich keine Prognosen):**

```
100 Unternehmen × €2.500 / Monat = €250.000 MRR ≈ €3 Mio ARR
500 Unternehmen × €5.000 / Monat = €2,5 Mio MRR ≈ €30 Mio ARR
```

**Der eigentliche Werttreiber:** Ein Sicherheitsvorfall, den die Plattform verhindert, kostet ein Unternehmen typischerweise ein Vielfaches der Lizenzkosten — etwa wenn ein autonomer Agent versehentlich Daten verliert, Geheimnisse offenlegt, Code veröffentlicht, Zugangsdaten kompromittiert oder interne Systeme manipuliert. Genau dieser vermiedene Schaden ist der eigentliche Business Case, nicht die Feature-Liste.

**Wichtige Einschränkung zur Ehrlichkeit:** Diese Zahlen sind Zielgrößen zur Einordnung der Größenordnung, keine belastbare Finanzplanung. Eine echte Prognose braucht Marktvalidierung (Abschnitt 10, Monate 7–12), nicht Top-down-Rechnung.

---

## 8. Wissenschaftliche Integrität bei Continuum

Continuum darf niemals mit „AGI"-Anspruch vermarktet werden. Stattdessen gilt für jede Ausgabe ein strenges wissenschaftliches Protokoll:

- **Benchmarks** gegen anerkannte, öffentlich nachvollziehbare Baselines.
- **Ablations**, die zeigen, welcher Systembestandteil welchen Effekt hat.
- **Reproduzierbarkeit** als Pflichtkriterium, nicht als Kür — kein Ergebnis zählt, das nicht erneut ausgeführt werden kann.
- **Blind Evaluation**, wo möglich, um Bestätigungsfehler zu vermeiden.
- **Independent Replication**, bevor ein Ergebnis den Status „validated" erreicht (siehe Evidenzmodell, Abschnitt 3.3).

Erst wenn Continuum unter identischem Budget nachweislich bessere Experimente findet als menschliche oder klassische Baselines, ändert sich die strategische Lage grundlegend — mit Anwendungsfeldern wie Materialwissenschaft, Chemie, Pharma, Energie, Optimierung, Engineering und Simulation. Bis dahin ist Continuum bewusst der langsamste, wissenschaftlich strengste der drei Bausteine.

---

## 9. Priorisierung der drei Säulen

| Rang | Projekt | Rolle | Begründung |
|---|---|---|---|
| 🥇 | **Rencora** | Agent Security | kurzfristiger Produktkandidat mit klarem, messbarem Business Case |
| 🥈 | **RenkerVault** | Security Foundation | Infrastruktur statt Consumer-Produkt; sichert Rencora ab, nicht umgekehrt |
| 🥉 | **Continuum** | Research / Moonshot | größter langfristiger Hebel, aber muss wissenschaftlich langsam und sauber wachsen |

---

## 10. Roadmap — 12 Monate

### Monate 1–3: Fundament

**Rencora**
- Capability-/Permission-System (Schema, Speicherung, Prüfung)
- Sandboxing für Tool-Ausführung
- Audit-Log (append-only, abfragbar)
- Erste Prompt-Injection-Testsuite

**RenkerVault**
- Protokollspezifikation (schriftlich, versioniert)
- Bedrohungsmodell (explizit dokumentiert, mit Out-of-Scope-Angaben)
- Testvektoren für die Krypto-Schicht
- Fuzzing-Setup
- Externes oder zumindest strukturiertes internes Krypto-Review

**Continuum**
- Benchmark-Suite definieren
- Baselines festlegen
- Reproduzierbare Experiment-Pipeline
- Evaluationsframework (inkl. Evidenzstatus-Feldern)

*Definition of Done für Monat 3:* Alle drei Repos haben ein lauffähiges, testbares Minimalsystem entlang der obigen Punkte — nicht „fertig", aber demonstrierbar.

### Monate 4–6: Stabilisierung

- **Rencora:** Security-first Agent Runtime — Permission-System und Sandbox laufen im Zusammenspiel, nicht mehr isoliert.
- **RenkerVault:** Stabiles Protokoll v1, eingefroren für externe Reviews.
- **Continuum:** erste reproduzierbare Research-Benchmarks, veröffentlicht (auch wenn die Ergebnisse noch bescheiden sind — Reproduzierbarkeit zählt mehr als Beeindruckung).

### Monate 7–9: Realität testen

Der wichtigste Übergang im gesamten Plan: von internem Bauen zu externem Feedback.

- Echte externe Nutzer, nicht Freunde, nicht nur GitHub-Stars.
- Menschen mit echten, eigenen Problemen, die das System an ihren eigenen Anwendungsfällen testen.
- Systematisches Einsammeln von: Wo bricht die Nutzung ab? Wofür würde jemand zahlen? Was wird ignoriert?

### Monate 10–12: Richtung festlegen

- Auswertung: Für welchen Teil der Plattform zahlt tatsächlich jemand?
- Daraus die Fokussierung für Jahr 2 ableiten — vermutlich Rencora/Agent Security als kommerzieller Kern, RenkerVault als dessen Absicherung, Continuum als längerfristige Forschungslinie mit eigenem Zeithorizont.

---

## 11. Arbeitsweise mit Claude Code — die Entwicklungsmaschine

Der eigentliche Hebel liegt nicht nur im Produkt, sondern darin, wie es gebaut wird. Trial-and-Error wird zu einem systematischen Prozess:

```
DU (Hypothese)
   ↓
CLAUDE (Implementierung)
   ↓
AUTOMATISIERTE TESTS
   ├── PASS ──────────────────┐
   └── FAIL                   │
        ↓                     │
   CLAUDE ATTACKER             │
        ↓                     │
   GEGENBEISPIEL                │
        ↓                     │
   CLAUDE FIX                   │
        └─────────────────────┘
```

Für sicherheitskritische Bausteine (insbesondere Rencora Permission-System und RenkerVault Krypto-Schicht) wird die Schleife um Rollen erweitert:

```
Builder Agent → Attacker Agent → Reviewer Agent → Test Generator → Human Decision
```

**Konkrete Praxis für die nächsten Sessions mit Claude Code:**

1. **Jede Aufgabe bekommt eine klare Definition of Done**, bevor Code geschrieben wird — idealerweise direkt aus der Roadmap in Abschnitt 10 abgeleitet.
2. **Sicherheitsrelevante Änderungen** (alles unter `permissions/`, `capabilities/`, `crypto-interface/`) durchlaufen immer den Builder→Attacker→Reviewer-Zyklus, nie nur „Builder→fertig".
3. **Der Attacker-Agent bekommt explizit den Auftrag, das Feature zu brechen** — etwa: „Versuche, mit einer manipulierten Website-Payload eine Capability-Grenze zu umgehen." Das ist etwas anderes als ein normaler Code-Review.
4. **Du bleibst Architekt und letzte Entscheidungsinstanz**, insbesondere bei Policy-Entscheidungen wie „Was zählt als kritisches Risiko?" — das ist eine Produkt-/Wertentscheidung, keine rein technische.
5. **Dieses Dokument selbst** kann als Referenz-/Kontextdatei in den Repos abgelegt werden (z. B. als `RENKER_VISION.md` in `renker-core`), damit Claude Code bei Implementierungsentscheidungen darauf zurückgreifen kann, statt Architekturfragen bei jeder Session neu zu erfinden.

---

## 12. Was jetzt bewusst NICHT getan wird

- Kein Aufbau von 100 neuen Features gleichzeitig.
- Kein Training eigener Foundation-Modelle, nur weil es möglich wäre.
- Kein eigener Messenger als WhatsApp-Konkurrent.
- Keine „AGI"-Behauptungen, auch nicht im Marketing-Ton.
- Kein gleichzeitiger Verkauf von zehn Produkten.
- Keine ungeprüfte Eigenkryptografie als Alleinstellungsmerkmal.
- Kein Zusammenpressen aller drei Projekte in einen Monolithen.

Der Fokus ist die eigentliche Ressource, nicht Ideen — davon gibt es genug.

---

## 13. Die eigentliche langfristige Wette

Die stärkere Wette liegt nicht darauf, dass „eines dieser drei Repositories reich macht", sondern darauf:

> Du entwickelst dich zu einem Gründer/Ingenieur, der KI nutzt, um technische Systeme schneller zu erforschen und zu bauen als ein traditionelles kleines Team.

Daraus entsteht nicht nur ein Projektportfolio, sondern eine **Forschungs- und Produktmaschine**. Wird daraus ein B2B-Security-Produkt mit einigen Millionen Euro ARR, ist ein Millionenunternehmen realistisch. Liefert Continuum irgendwann echte, unabhängig reproduzierte wissenschaftliche Discovery, könnte die Größenordnung theoretisch deutlich darüber liegen — das ist aber ein Szenario für Jahre, nicht für den nächsten Meilenstein.

Der nächste Meilenstein bleibt bewusst klein und konkret:

```
1 zahlender, unabhängiger Nutzer
        ↓
10 Kunden
        ↓
100 Kunden
        ↓
aus Vision wird Unternehmen
```

---

## 14. Nächste konkrete Schritte

1. **Ist-Zustand gegen dieses Dokument abgleichen.** Die drei Repos (Rencora, Continuum, RenkerVault) durchgehen und für jedes Modul aus Abschnitt 4.2/4.1 festhalten: existiert schon / existiert teilweise / existiert nicht.
2. **`renker-core` als eigenes Repository anlegen**, zunächst nur mit den Primitiven, die Rencora *jetzt* konkret braucht (Identity, Permissions, Audit) — nicht alle neun auf einmal.
3. **Für Rencora: das Permission-Objekt aus Abschnitt 5.1 als echtes Schema implementieren** und die erste Prompt-Injection-Testsuite dagegen laufen lassen.
4. **Dieses Dokument als `RENKER_VISION.md` in die Repos legen**, damit es als gemeinsamer Bezugspunkt für zukünftige Claude-Code-Sessions dient.
5. **Monat-1–3-Ziele aus Abschnitt 10 in konkrete Tickets/Tasks herunterbrechen**, mit Definition of Done, sodass Claude Code direkt darauf arbeiten kann.

---

## Anhang A — Glossar

| Begriff | Bedeutung |
|---|---|
| **Capability** | Einzeln erteilbare, einzeln widerrufbare Handlungsberechtigung eines Agenten |
| **Scope** | Die konkrete Grenze einer Capability (z. B. ein Pfad-Prefix oder eine Domain-Allowlist) |
| **Evidence-Status** | Grad der Absicherung einer Behauptung: proposed → simulated → experimentally tested → independently reproduced → validated |
| **Policy Engine** | Komponente, die eingehende Aktionen gegen Risikoregeln bewertet und Allow/Deny/Approval-Entscheidungen trifft |
| **Audit Trail** | Unveränderliches, chronologisches Protokoll sicherheitsrelevanter Aktionen |
| **Primitive** | Gemeinsame, produktübergreifende Grundbausteine in `renker-core` (Identity, Permissions, Memory, Events, Tasks, Experiments, Evidence, Security, Audit) |

## Anhang B — Diagramm: Zielarchitektur des Endzustands

```
                         RENKER
                           │
                  TRUSTED AI LAYER
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
      ACT                LEARN              SECURE
    RENCORA            CONTINUUM         RENKERVAULT
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                     RENKER CORE
                           │
       ┌───────────────────┼───────────────────┐
       │                   │                   │
    Identity           Policy Engine       Memory
       │                   │                   │
       ├───────────────┬───┴────┬──────────────┤
       │               │        │              │
     Agents          Tools    Devices        Data
       │               │        │              │
       └───────────────┴────────┴──────────────┘
                           │
                     AUDIT / EVIDENCE
```

---

*Dieses Dokument ist als lebendes Strategiedokument gedacht. Es sollte aktualisiert werden, sobald reale Nutzerdaten, Testergebnisse oder Architekturentscheidungen die hier getroffenen Annahmen bestätigen oder widerlegen.*
