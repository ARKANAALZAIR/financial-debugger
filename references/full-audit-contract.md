# Full Financial Debug Contract

## Purpose

This contract defines deterministic behavior for broad financial audit prompts. It makes a short prompt such as **"audit this"** trigger a complete, traceable financial reasoning audit without requiring the user to list individual checks.

## Canonical modules

| ID | Module | Core question |
|---|---|---|
| M01 | Intent & Decision Context | What financial question or decision is actually being tested? |
| M02 | Sufficiency & Input Verification | Are the necessary inputs present, identified, and usable? |
| M03 | Claim Extraction & Statement Classification | What are the atomic claims and what epistemic type is each statement? |
| M04 | Evidence & Source Integrity | Does the evidence support the exact claim, with appropriate source quality and freshness? |
| M05 | Contradiction & Alternative Explanation Audit | What adverse evidence or competing mechanisms could explain the observation? |
| M06 | Assumption Registry | Which assumptions materially drive the thesis and what would invalidate them? |
| M07 | Methodology / Model Fit | Is the chosen analytical method appropriate for the asset and question? |
| M08 | Numerical Integrity | Are calculations, units, dates, signs, denominators, and scales reproducible? |
| M09 | Valuation Audit | Is the valuation method appropriate and how sensitive is value to assumptions? |
| M10 | Forecast & Scenario Analysis | What conditional outcomes follow from explicit assumptions? |
| M11 | Sensitivity & Dependency Analysis | Which assumptions or dependencies can change the conclusion? |
| M12 | Expectations Audit | Does business performance actually translate into return potential given expectations? |
| M13 | Risk & Uncertainty Audit | What is stress-testable risk versus unresolved uncertainty? |
| M14 | Portfolio Exposure & Concentration Audit | What economic exposures and correlations affect the decision? |
| M15 | Reversibility & Capital-at-Risk Audit | How costly and irreversible is being wrong? |
| M16 | Thesis State Audit | Is the thesis supported, fragile, contested, insufficient, invalid, or not material? |
| M17 | Decision State & Materiality Audit | Does the thesis actually justify the proposed decision given constraints? |
| M18 | Post-Mortem / Information-Set Lock | For prior decisions, what was knowable at the decision cutoff? |
| M19 | Decision Kill Switches | What observable conditions should trigger reassessment? |
| M20 | Next Best Action / Stop Gate | What smallest next action reduces uncertainty, and when should analysis stop? |

## Status semantics

### FOUND
The module materially evaluated its scope and identified at least one material defect, gap, or unresolved diagnostic issue supported by available evidence.

### ERROR NOT FOUND
The module materially evaluated its scope and found no material error or diagnostic defect within the evidence available. This does not mean the overall thesis is proven or error-free.

### NOT ASSESSABLE
A required core input is absent or outside the supplied evidence, so the module cannot reliably determine its diagnostic state. Do not convert missing evidence into a negative finding.

## Finding identity

Every material finding has one `Primary Module`, optional `Related Modules`, and one stable `ID: FD-NNN`. Only the primary module owns the global finding count. Related modules reference the same ID rather than creating another finding.

## Reconciliation requirements

Before final response:
- all 20 modules appear;
- every finding ID is unique;
- every finding has one primary module;
- every finding severity appears exactly once in the global count;
- global severity totals equal the actual unique finding list;
- module finding IDs point to existing findings;
- no module is missing because another module found a blocker.

## Broad prompt examples

These should trigger the full sweep when financial material is supplied:
- `Audit this.`
- `Audit this thesis.`
- `Debug this investment thesis.`
- `Run a full financial debug.`
- `Audit my portfolio.`
- `Debug this macro thesis.`

Explicit narrow prompts may route only to the relevant module(s).


## Final hardening additions

- Use `PARTIAL` when a module can still answer its core question but some sub-checks are blocked; reserve `NOT ASSESSABLE` for missing core inputs.
- For `DECISION-CHANGING` findings, state the explicit decision linkage and the condition that would change the decision state.
- Every material calculation must be reproducible or explicitly marked `UNREPRODUCIBLE`.
- Material evidence must be distinguishable as user input/unverified, verified source/date, derived calculation, assumption, or missing.
- Final `Audit Integrity Check` must include module counts, unique findings, severity/materiality reconciliation, primary-module reconciliation, evidence-provenance check, and decision-changing-link check.


## Final-hardening additions (v1.9.2)

### Source verification record
For every material externally verified claim, retain: publisher/institution, source title or stable identifier, publication date, retrieval date when freshness matters, exact claim supported, relevant period, source quality/type, and known source lineage. If any of these are materially missing, do not label the claim fully VERIFIED.

### Synthesis/action status semantics
M16 Thesis State, M17 Decision State, M19 Kill Switches, and M20 Next Best Action are synthesis/action modules. Their successful completion is `COMPLETED`, not `FOUND`, unless the implementation explicitly identifies a separate diagnostic defect. M18 is `NOT APPLICABLE` for clearly forward-looking pre-decision audits.

### Arithmetic vs forecast validity
A correct compounding calculation does not validate the assumed return path. Report arithmetic correctness separately from forecast/assumption support.

### Recovery-duration traceability
Claims about historical recovery time, drawdown duration, or repeated recovery require explicit date/definition/source traceability. Otherwise mark them UNVERIFIED and do not use them as established historical evidence.
