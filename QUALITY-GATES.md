# Quality Gates

Financial Debugger is ready for release only when the following gates pass.

## Repository integrity

- `SKILL.md` exists at repository root.
- `README.md` exists at repository root.
- `references/`, `templates/`, `examples/`, and `tests/` exist.
- Repository documentation describes the same product and release version.

## Skill integrity

- YAML frontmatter contains `name`, `description`, and `version`.
- Skill name is `financial-debugger`.
- Skill version matches the intended release version.
- No instructions require fabricated data, sources, calculations, or certainty.
- Forecasting remains conditional.

## Evidence and reasoning integrity

- User-provided data is treated as unverified until verified or explicitly labeled.
- Contradictory evidence and alternative explanations are considered.
- Material calculations are reproducible.
- Method fit is audited before applying valuation or analytical formulas.
- Thesis quality is distinguished from decision quality.
- Post-mortems use Information-Set Lock.

## Test coverage

- `tests/test-cases.md` contains adversarial cases covering evidence, causality, valuation, calculations, uncertainty, portfolio risk, forecasting, and post-mortems.
- `scripts/validate.py` passes.

## Release gate

Do not publish a release when a critical gate fails. Document known limitations rather than silently bypassing a failed gate.


## v1.9.0 Full-Audit Gates

- Broad short prompts trigger `FULL FINANCIAL DEBUG` when financial material is supplied.
- M01–M20 are all executed and displayed in full-audit mode.
- Each module has `Execution`, `Status`, `Coverage`, `Finding IDs`, and `Evidence/Notes`.
- `ERROR NOT FOUND` is used only when the module actually executed and no material defect was found in available evidence.
- `NOT ASSESSABLE` is used when required inputs are genuinely absent.
- Every material finding has exactly one primary module and optional related modules.
- Finding IDs and severity totals reconcile with the displayed findings.
- A blocker in one module does not suppress the remaining module sweep.

## v1.8.2 Behavioral Gates

- Material findings use the mandatory schema.
- Missing evidence is never treated as negative evidence.
- Unsupported base cases/probabilities remain UNKNOWN or CONDITIONAL.
- Finding counts are not converted to arbitrary overall scores.
- Portfolio-sizing conclusions remain conditional when risk-context inputs are missing.


## v1.9.1 Final Hardening Gates

- `NOT ASSESSABLE` is used when a core diagnostic input is absent; `ERROR NOT FOUND` requires a materially assessable module.
- DECISION-CHANGING findings include an explicit decision linkage and supported condition for change.
- Material calculations preserve inputs, formula, units, period, result, and rounding or are marked UNREPRODUCIBLE.
- Evidence provenance is explicit for material claims.
- Cross-module duplicate root causes are represented by one finding ID and one Primary Module.
- Final Audit Integrity Check reconciles module counts, finding IDs, ownership, severity/materiality, and evidence provenance.
- `scripts/validate.py` passes.
