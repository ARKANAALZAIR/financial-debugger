# FULL FINANCIAL DEBUG REPORT

## EXECUTIVE STATE
Audit Mode: FULL FINANCIAL DEBUG

Thesis State:
Decision State:
Confidence:
Sufficiency:

## MODULE EXECUTION MATRIX

| ID | Module | Execution | Class | Status | Coverage | Finding IDs |
|---|---|---|---|---|---|
| M01 | Intent & Decision Context | COMPLETE | DIAGNOSTIC |  |  |  |
| M02 | Sufficiency & Input Verification | COMPLETE | DIAGNOSTIC |  |  |  |
| M03 | Claim Extraction & Statement Classification | COMPLETE | DIAGNOSTIC |  |  |  |
| M04 | Evidence & Source Integrity | COMPLETE | DIAGNOSTIC |  |  |  |
| M05 | Contradiction & Alternative Explanation Audit | COMPLETE | DIAGNOSTIC |  |  |  |
| M06 | Assumption Registry | COMPLETE | DIAGNOSTIC |  |  |  |
| M07 | Methodology / Model Fit | COMPLETE | DIAGNOSTIC |  |  |  |
| M08 | Numerical Integrity | COMPLETE | DIAGNOSTIC |  |  |  |
| M09 | Valuation Audit | COMPLETE | DIAGNOSTIC |  |  |  |
| M10 | Forecast & Scenario Analysis | COMPLETE | DIAGNOSTIC |  |  |  |
| M11 | Sensitivity & Dependency Analysis | COMPLETE | DIAGNOSTIC |  |  |  |
| M12 | Expectations Audit | COMPLETE | DIAGNOSTIC |  |  |  |
| M13 | Risk & Uncertainty Audit | COMPLETE | DIAGNOSTIC |  |  |  |
| M14 | Portfolio Exposure & Concentration Audit | COMPLETE | DIAGNOSTIC |  |  |  |
| M15 | Reversibility & Capital-at-Risk Audit | COMPLETE | DIAGNOSTIC |  |  |  |
| M16 | Thesis State Audit | COMPLETE | SYNTHESIS |  |  |  |
| M17 | Decision State & Materiality Audit | COMPLETE | SYNTHESIS |  |  |  |
| M18 | Post-Mortem / Information-Set Lock | COMPLETE | DIAGNOSTIC |  |  |  |
| M19 | Decision Kill Switches | COMPLETE | SYNTHESIS |  |  |  |
| M20 | Next Best Action / Stop Gate | COMPLETE | SYNTHESIS |  |  |  |

## SEVERITY DISTRIBUTION

🔴 Critical: N
🟠 High: N
🟡 Medium: N
🔵 Low: N

## MATERIALITY DISTRIBUTION

🔴 Decision-changing: N
🟠 High materiality: N
🟡 Medium materiality: N
🔵 Low materiality: N

## ALL MATERIAL FINDINGS

Use this exact field sequence for every finding:

```text
## [severity] FD-NNN
ID:
Severity:
Materiality:
Type:
Primary Module:
Related Modules:
Decision-Changing:
Decision Link:
Location:
Problem:
Evidence:
Reasoning:
Impact:
Recommended Action:
Verification Needed:
```

## EVIDENCE MAP

## ASSUMPTION REGISTRY

## SCENARIO / SENSITIVITY

## THESIS STATE

## DECISION STATE

## CONFIDENCE

## NEXT BEST ACTION

## KILL SWITCHES

## REMAINING UNKNOWNS / STOP GATE

## AUDIT INTEGRITY CHECK

```text
Modules Executed: 20/20
Diagnostic Modules With Findings: [N]
Diagnostic Modules Error Not Found: [N]
Modules Not Assessable: [N]
Modules Not Applicable: [N]
Synthesis/Action Modules Completed: [N]
Unique Material Findings: [N]
Severity Count Reconciled: PASS | FAIL
Materiality Count Reconciled: PASS | FAIL
Finding ID Reconciliation: PASS | FAIL
Primary-Module Reconciliation: PASS | FAIL
Evidence Provenance Reconciliation: PASS | FAIL
Decision-Link Reconciliation: PASS | FAIL
Overall: PASS | FAIL
```

### State rule

Diagnostic M01–M15 and M18 use only FOUND / ERROR NOT FOUND / NOT ASSESSABLE / NOT APPLICABLE. Synthesis/action M16/M17/M19/M20 use only COMPLETED / NOT ASSESSABLE / NOT APPLICABLE. Never emit FOUND for a synthesis module.


`ERROR NOT FOUND` = diagnostic core assessable + no material defect.
`NOT ASSESSABLE` = required core evidence absent.
`NOT APPLICABLE` = module does not materially apply; use Coverage `N/A`.
`FOUND` = diagnostic issue found.
`COMPLETED` = synthesis/action function successfully produced.
`PARTIAL` coverage may pair with diagnostic or completed states when some sub-checks are blocked.

