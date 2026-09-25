# Changelog

## v1.9.1 — Final Hardening Pass

- Tightened `ERROR NOT FOUND` vs `NOT ASSESSABLE` semantics and coverage handling.
- Added explicit decision-changing evidence linkage and severity/materiality calibration.
- Added evidence provenance categories so user inputs are not silently treated as verified current data.
- Added reproducibility rules for material calculations.
- Added root-cause ownership precedence and stronger deduplication rules.
- Added final Audit Integrity Check coverage for module counts, finding IDs, ownership, evidence provenance, and decision-changing links.
- Expanded behavioral tests for status semantics, severity calibration, current-data limits, calculation traceability, and audit integrity.

v1.9.0

- Added `FULL FINANCIAL DEBUG` as the canonical broad-audit mode.
- Added short-prompt auto-trigger behavior for supplied financial artifacts.
- Added canonical modules M01–M20.
- Required all 20 modules to appear in full-audit output.
- Added explicit `ERROR NOT FOUND` and `NOT ASSESSABLE` module states.
- Added primary-module and related-module finding identity.
- Added global finding/severity reconciliation requirements.
- Added full-audit contract and report template.
- Expanded adversarial tests for auto-triggering, module completeness, stopping behavior, status semantics, and count consistency.


## v1.8.2

- Added a mandatory Financial Debug Report output contract.
- Required every material finding to use a normalized finding schema with severity, evidence, reasoning, impact, and recommended action.
- Prevented free-form audit sections from silently replacing material findings.
- Added strict epistemic rules: missing evidence is not negative evidence; unsupported base cases and probabilities must remain UNKNOWN/CONDITIONAL.
- Refined evidence-dependence handling so correlated signals are not automatically declared to be the same evidence.
- Strengthened valuation-method neutrality and portfolio-sizing language when context is incomplete.
- Added output-normalization and overclaim-prevention behavioral tests.

## v1.8.1

- Hardened evidence-to-claim alignment and evidence sufficiency.
- Expanded Assumption Registry with type, scenario impact, and kill conditions.
- Strengthened conditional forecast decomposition and expectation-vs-outcome auditing.
- Added explicit risk-vs-uncertainty separation and portfolio stress-test rules.
- Removed arbitrary overall decision-health scoring from the default output.
- Strengthened materiality, Top 3 decision-changing findings, and Next Best Action behavior.
- Added behavioral test protocol cases while preserving the existing GitHub repository structure.
- Preserved Thesis Debugger-style README section order and repository presentation.

## v1.6.0

- Production-oriented financial reasoning audit workflow.
- Adaptive Light, Standard, and Deep debug depth.
- Evidence, assumption, contradiction, methodology, numerical, valuation, scenario, sensitivity, expectations, risk, and reversibility audits.
- Thesis-versus-decision distinction.
- Post-mortem Information-Set Lock.
- Decision Kill Switches and Next Best Action outputs.
- Reusable references, templates, examples, adversarial tests, and repository validation.
