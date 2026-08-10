# Roadmap — 12 Monate

## Monate 1–3: Fundament

**Rencora**
- [ ] Capability-/Permission-System (Schema, Speicherung, Prüfung)
- [ ] Sandboxing für Tool-Ausführung
- [ ] Audit-Log (append-only, abfragbar)
- [ ] Erste Prompt-Injection-Testsuite

**RenkerVault**
- [ ] Protokollspezifikation (schriftlich, versioniert)
- [ ] Bedrohungsmodell (explizit dokumentiert, mit Out-of-Scope)
- [ ] Testvektoren für die Krypto-Schicht
- [ ] Fuzzing-Setup
- [ ] Externes oder strukturiertes internes Krypto-Review

**Continuum**
- [ ] Benchmark-Suite definieren
- [ ] Baselines festlegen
- [ ] Reproduzierbare Experiment-Pipeline
- [ ] Evaluationsframework (inkl. Evidenzstatus-Feldern)

*Definition of Done (Monat 3):* Alle drei Repos haben ein lauffähiges, testbares Minimalsystem — nicht „fertig", aber demonstrierbar.

## Monate 4–6: Stabilisierung
- [ ] Rencora: Permission-System und Sandbox laufen im Zusammenspiel
- [ ] RenkerVault: stabiles Protokoll v1, eingefroren für externe Reviews
- [ ] Continuum: erste reproduzierbare Research-Benchmarks veröffentlicht

## Monate 7–9: Realität testen
- [ ] Echte externe Nutzer (nicht Freunde, nicht nur GitHub-Stars)
- [ ] Menschen mit echten eigenen Problemen testen an eigenen Anwendungsfällen
- [ ] Systematisch einsammeln: Wo bricht Nutzung ab? Wofür würde jemand zahlen? Was wird ignoriert?

## Monate 10–12: Richtung festlegen
- [ ] Auswertung: Für welchen Teil zahlt tatsächlich jemand?
- [ ] Fokussierung für Jahr 2 ableiten (voraussichtlich Rencora/Agent Security als Kern)

---

### renker-core — unmittelbar nächster Schritt (Monat-1-Meilenstein)
- [ ] Identity, Permissions, Audit als lauffähige, kommentarfreie Module (gemäß Vision 5.1/5.2)
- [ ] Permission-Objekt-Schema implementieren
- [ ] Append-only Audit-Log mit Hash-Chain
