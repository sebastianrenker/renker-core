# Agent Security

Potenziell der wirtschaftlich stärkste kurzfristige Baustein der Plattform.

## Das Kernproblem

KI-Agenten bekommen immer mehr Berechtigungen. Was passiert, wenn ein Agent manipuliert wird?

```
Website → Prompt Injection → AI Agent → Tool Call → "Upload ~/.ssh/"
```

## Die Antwort: Capability Security

Kein Akteur besitzt pauschale Rechte. Jede Fähigkeit ist ein einzeln erteiltes, einzeln widerrufbares Objekt mit sechs Eigenschaften: **Permission, Scope, Lifetime, Audit Trail, Approval Policy, Revocation.**

Der Fluss jeder Aktion:

```
REQUEST → POLICY ENGINE → Risk Assessment → Permission → Sandbox → Execution → Audit
```

Bei gefährlichen Aktionen: `HIGH RISK → DENY` oder `→ HUMAN APPROVAL`.

## Permission-Objekt (Skizze)

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

## Audit-Log-Eintrag (Skizze)

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

Das Log ist **append-only** und kryptografisch verkettet (Hash-Chain), damit auch ein kompromittierter Agent seine Spuren nicht verwischen kann.

## Risikostufen (Grundlage der Policy Engine)

| Stufe | Beispiele | Standard |
|---|---|---|
| **Niedrig** | Lesen im Scope, Web-Recherche in Allowlist | auto erlaubt, protokolliert |
| **Mittel** | Schreiben außerhalb bekannter Scopes, neue Domain | erlaubt mit Warnung / Freigabe nach Policy |
| **Hoch** | Zugangsdaten/Schlüssel, Löschen, Zahlungen | menschliche Freigabe |
| **Kritisch** | `.ssh`, Produktions-DB, irreversibles Löschen | verweigert, nur mit explizitem Override |

Daraus kann ein eigenständiges Produkt werden: **Renker Agent Security** — *Security layer for autonomous AI agents*. Der Business Case ist der **vermiedene Schaden**, unmittelbar in Euro messbar.
