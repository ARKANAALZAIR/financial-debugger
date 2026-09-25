# Financial Audit Integrity & Reconciliation Rules

## 1. Module-state semantics

Use one of these module statuses, according to module role:

- `FOUND` — a diagnostic module materially evaluated its scope and found at least one supported defect, gap, or diagnostic issue.
- `ERROR NOT FOUND` — a diagnostic module materially evaluated its scope and found no material defect within the evidence available.
- `NOT ASSESSABLE` — a required core input is absent, so the diagnostic state cannot be reliably determined. Missing evidence is not negative evidence.
- `NOT APPLICABLE` — the module's subject does not apply to the decision state being audited. Example: a post-mortem module on a clearly forward-looking pre-decision audit.
- `COMPLETED` — a synthesis/action module successfully produced its output from the audited state. Use for M16, M17, M19, and M20 when their function can be completed.

Coverage is independent:

- `FULL` — core checks materially supported.
- `PARTIAL` — core diagnosis can run but some sub-checks are blocked.
- `LIMITED` — the evidence boundary is too narrow for reliable core diagnosis.

Typical mapping:

| Evidence state | Status | Coverage |
|---|---|---|
| Diagnostic core inputs present + material issue found | FOUND | FULL/PARTIAL |
| Diagnostic core inputs present + no material issue found | ERROR NOT FOUND | FULL/PARTIAL |
| Diagnostic core input absent | NOT ASSESSABLE | LIMITED |
| Module does not apply | NOT APPLICABLE | LIMITED |
| Synthesis/action function completed | COMPLETED | FULL/PARTIAL |

Do not use `ERROR NOT FOUND` just because the module was called. Do not use `FOUND` for a synthesis state merely because the resulting state is FRAGILE/CONTESTED.

**M02:** a material missing input is itself a sufficiency finding, so M02 should normally be `FOUND` when the gap materially limits the decision audit.

## 2. Finding ownership and deduplication

Each unique material issue gets exactly one `ID: FD-NNN` and exactly one `Primary Module`. Related modules reference the same ID.

Deduplicate when root cause, evidence/location, and corrective action materially match. Keep separate IDs when the underlying cause or next action differs.

Default root-cause ownership:

- evidence/source integrity → M04
- contradictions/alternative mechanisms → M05
- assumptions → M06
- methodology/model fit → M07
- arithmetic/unit errors → M08
- valuation → M09
- scenario construction → M10
- dependency/sensitivity → M11
- expectations → M12
- risk/uncertainty → M13
- portfolio exposure → M14
- reversibility/capital at risk → M15
- thesis state → M16
- decision/materiality → M17
- post-mortem information-set contamination → M18
- kill switches → M19
- action/stop gate → M20

Use this as a default owner, not a reason to merge genuinely different problems.

## 3. Severity and materiality calibration

Financial Debugger uses severity labels plus decision materiality. They are related but not identical.

- `DECISION-CHANGING` requires evidence that the finding could change the stated decision under the supplied constraints or a supported sensitivity.
- `HIGH` requires a material decision/reasoning consequence with strong evidence or a well-supported unresolved issue.
- `MEDIUM` is consequential but bounded.
- `LOW` is localized and unlikely to change the decision by itself.

Do not call a finding decision-changing merely because it sounds important. Show the decision link: which assumption/claim changes, which decision variable changes, and what condition would flip the state.

A low-confidence issue cannot become DECISION-CHANGING solely because the hypothetical downside is large.

## 4. Evidence provenance

For each material claim, distinguish:

- `USER INPUT / UNVERIFIED`
- `VERIFIED SOURCE / DATE`
- `PARTIALLY VERIFIED / REQUIRES SOURCE VERIFICATION` when provenance or exact-claim support is incomplete
- `DERIVED CALCULATION`
- `ASSUMPTION`
- `MISSING`

Never silently upgrade a user-supplied number to verified market data. Do not claim current price, current filing data, or current macro conditions without current/dated evidence.

## 5. Numerical integrity

For every material calculation, preserve:

`inputs → formula → units → period → result → rounding`

If any essential input is missing, label the calculation `UNREPRODUCIBLE` or `NOT ASSESSABLE` instead of filling the gap.

## 6. Forecast/scenario discipline

A scenario is conditional. The base case may be `UNKNOWN` or `CONDITIONAL`. Never infer probability or “most realistic” state from a single anchor such as prior price, one multiple, or one headline.

## 7. Final audit-integrity gate

Before returning the report:

```text
[ ] M01–M20 appear exactly once
[ ] Every module has Execution, Status, Coverage, Finding IDs, Evidence/Notes
[ ] Diagnostic missing core inputs produce NOT ASSESSABLE; material input gaps in M02 are recorded as findings
[ ] Synthesis/action modules use COMPLETED when their function is successfully produced
[ ] Contextually irrelevant modules use NOT APPLICABLE
[ ] Every finding ID is unique and has exactly one Primary Module
[ ] Related-module references point to existing finding IDs
[ ] Global finding totals equal the unique finding list
[ ] Severity/materiality totals reconcile
[ ] No blocker suppresses remaining modules
[ ] Material calculations are reproducible or explicitly UNREPRODUCIBLE
[ ] Evidence provenance is explicit for material claims
[ ] Verified sources expose publisher/title/date/retrieval/claim-supported when applicable
[ ] Recovery-duration or historical-range claims have explicit traceability or are labeled unverified
[ ] Decision-changing findings show an explicit decision linkage
[ ] No unsupported probability/base-case/ranking is introduced
[ ] Final Audit Integrity Check matches the displayed module matrix
```
