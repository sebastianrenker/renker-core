# Sicherheitsmodell — renker-core

`renker-core` stellt die Primitive bereit, mit denen die Renker-Plattform autonomes Handeln **kontrollierbar, überprüfbar und widerrufbar** macht. Dieses Dokument fasst das Capability- und Risikostufen-Modell zusammen (Vollfassung: `RENKER_VISION.md`, Abschnitt 5).

## Capability Security

Kein Akteur besitzt pauschale Rechte („Terminalzugriff", „Dateisystemzugriff"). Jede Fähigkeit ist ein einzeln erteiltes, einzeln widerrufbares Objekt mit sechs Eigenschaften:

- **Permission** — welche Aktion genau erlaubt ist (nicht „Dateisystem", sondern „lesend, unter diesem Pfad-Prefix").
- **Scope** — die konkrete Grenze (Pfad, Domain, Prozessname).
- **Lifetime** — Ablaufzeit oder Sitzungsbindung; keine Capability lebt standardmäßig für immer.
- **Audit Trail** — jede Nutzung wird unveränderlich protokolliert.
- **Approval Policy** — `auto` / `deny` / `human`, abhängig vom Risiko.
- **Revocation** — jederzeit sofort entziehbar, auch mitten in einer laufenden Aktion.

## Risikostufen

| Stufe | Beispielaktionen | Standardverhalten |
|---|---|---|
| **Niedrig** | Datei lesen in erlaubtem Scope, Web-Recherche in Allowlist | automatisch erlaubt, protokolliert |
| **Mittel** | Datei außerhalb bekannter Scopes schreiben, neue Domain kontaktieren | erlaubt mit Warnung oder Freigabe nach Policy |
| **Hoch** | Zugriff auf Zugangsdaten/Schlüssel, Löschoperationen, Zahlungsauslösung | menschliche Freigabe erforderlich |
| **Kritisch** | Zugriff auf `.ssh`, Produktionsdatenbanken, irreversible Löschung | standardmäßig verweigert, nur mit explizitem Override |

## Audit-Log

Sicherheitsrelevante Aktionen werden append-only und kryptografisch verkettet (Hash-Chain über `sha256`) protokolliert, sodass auch ein kompromittierter Agent seine Spuren nicht nachträglich verwischen kann.

## Kryptografie

`renker_core/crypto_interface/` enthält **nur Schnittstellen**. Es wird keine eigene Kryptografie implementiert; die Umsetzung erfolgt in einem separaten, streng auditierten Modul auf Basis etablierter Primitive (libsodium/NaCl, Signal-Protokoll). Siehe Vision, Abschnitt 4.3.

## Meldung von Schwachstellen

Sicherheitslücken bitte **nicht** über öffentliche Issues melden, sondern vertraulich an den Repository-Eigentümer. Da dieses Repo privat ist, genügt vorerst eine direkte Kontaktaufnahme.
