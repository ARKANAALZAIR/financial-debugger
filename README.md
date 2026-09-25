# Financial Debugger

> **Debug your financial decisions before your money pays for the mistake.**

Financial Debugger is a Claude Agent Skill that audits financial reasoning as a connected decision system rather than simply commenting on a stock, asset, or market narrative. It traces the chain from facts and evidence through assumptions, methods, calculations, scenarios, risk, uncertainty, and the final decision.

## What it detects

- Unsupported financial claims
- Weak or mismatched evidence
- Hidden assumptions
- Causal leaps and attribution errors
- Methodology/model mismatch
- Arithmetic, unit, currency, scale, or period errors
- Fragile valuation assumptions
- Forecast false precision
- Expectation-versus-outcome gaps
- Risk-versus-uncertainty confusion
- Conflicting or time-misaligned evidence
- Expectation-versus-outcome confusion
- Concentration and correlated exposure
- Confirmation and hindsight bias
- Thesis/decision confusion
- Post-mortem contamination from information learned after the decision

## Why it exists

A financial decision is not just a conclusion about an asset. It is a connected chain:

`FACT → EVIDENCE → ASSUMPTION → METHOD → REASONING → SCENARIO → RISK/UNCERTAINTY → DECISION`

A weak link can make a seemingly strong conclusion fragile. Financial Debugger makes those dependencies explicit before capital is committed, and it separates the quality of a thesis from the quality of the decision made from that thesis.

## Signature feature: Decision-Chain Debugging

Example request:

> Revenue is growing, earnings are strong, valuation looks cheap, so I think this stock can double in 12 months. What am I missing?

The skill decomposes the claim into testable components, checks the evidence and assumptions behind each link, audits the analytical method and material calculations, stress-tests the conclusion under alternative scenarios, and identifies what could actually change the decision.

It does not turn the analysis into an automatic buy/sell signal.

## Example output

The following is illustrative only; it uses hypothetical inputs rather than current market data and demonstrates categorical diagnosis rather than an arbitrary overall score.

```text
# FINANCIAL DEBUG REPORT

🔴 Decision-changing: 2
🟠 High: 4
🟡 Medium: 5
🔵 Low: 2

## 🔴 DECISION-CHANGING #001
Type: VALUATION_FRAGILITY
Location: Valuation → Terminal assumptions
Problem: The conclusion depends on a narrow set of margin and multiple assumptions.
Evidence: The current model outcome changes materially under modest changes to operating margin and exit multiple.
Reasoning: The thesis may remain plausible while the proposed entry price is highly sensitive to assumptions.
Impact: Expected return, downside, position sizing, decision state.
Recommended Action: Run a bear/base/bull sensitivity and identify the assumptions that would invalidate the decision.

## 🟠 HIGH #002
Type: CAUSALITY_GAP
Location: Thesis → Macro catalyst
Problem: A macro improvement is treated as proof of a specific equity-price outcome.
Evidence: The chain does not establish the transmission mechanism or expectation delta.
Reasoning: A better macro variable does not automatically imply a better realized return for the specific security.
Impact: Catalyst interpretation, scenario weighting.
Recommended Action: Test alternative transmission mechanisms and expectation effects.
```

## Installation

### Claude.ai

Anthropic documents custom Skills as folders containing a `SKILL.md` plus optional bundled resources. To upload this skill in Claude.ai, zip the `financial-debugger/` folder so it is the single top-level entry in the ZIP, then use the applicable **Customize → Skills → Create/Upload** flow in your Claude account.

### Claude Code

Claude Code discovers custom skills from the filesystem. For a personal skill, place the folder under `~/.claude/skills/`; for a project skill, place it under `.claude/skills/`. Keep `SKILL.md` at the skill directory root.

### API / other Agent Skills-compatible runtimes

For Skills-compatible runtimes, preserve the standard skill directory structure and keep `SKILL.md` at the directory root. Follow the host platform's current registration/upload mechanism.

## Full audit mode

The default broad-audit experience is intentionally simple:

```text
Upload your financial thesis / portfolio / model / article
                ↓
        "Audit this financial thesis"
                ↓
       FULL FINANCIAL DEBUG
                ↓
          M01 → M20
                ↓
Findings + Error Not Found + Not Assessable
                ↓
Reconciled final report
```

For broad audit prompts, the skill automatically runs all 20 canonical modules. You do not need to ask separately for valuation, evidence, scenarios, portfolio risk, post-mortem checks, or kill switches.

Every module remains visible in the final report:
- `FOUND` when a material issue is detected;
- `ERROR NOT FOUND` when the module runs and finds no material defect in the available evidence;
- `NOT ASSESSABLE` when the required evidence is genuinely missing.

### Usage

Upload or make available the financial artifacts relevant to the decision, then ask naturally:

- `Audit this.`
- `Audit this financial thesis.`
- `Debug this investment thesis.`
- `Find only decision-changing issues.`
- `Return a Financial Debug Report with every material finding in the mandatory finding schema.`
- `Audit the valuation.`
- `Check whether the evidence actually supports the claim.`
- `Stress-test my assumptions.`
- `Debug this macro-to-market narrative.`
- `Audit my portfolio concentration.`
- `Post-mortem this decision without hindsight.`
- `What would invalidate this thesis?`

The skill also supports narrower workflows through its internal routing, including evidence, valuation, scenario, portfolio-risk, and post-mortem analysis.

## Supported financial materials

Designed to work with, when the environment can read them:

- SEC/company filings and annual or quarterly reports
- Investor presentations
- Financial statements
- Valuation models and spreadsheets
- Research notes
- Portfolio snapshots
- CSV/XLSX data
- Macro and market documents
- News articles and supplied screenshots/text
- Investment theses and decision logs
- Personal-finance inputs where sufficient context is available

The skill does not require a complete information set. It reports which checks are blocked by missing, ambiguous, or unverified inputs rather than silently filling the gaps.

## Reliability philosophy

The audit explicitly distinguishes **expectations** from realized outcomes and distinguishes **risk** from **uncertainty**. A positive business result can still produce a poor investment outcome if expectations or valuation differ; uncertainty should not be converted into invented probabilities.

**Expectations Audit:** separates absolute performance, market expectations, and realized surprise.

**Risk vs Uncertainty:** risk is stress-testable adverse exposure; uncertainty is incomplete knowledge about inputs, probabilities, mechanisms, or future states.


Financial Debugger is optimized for **high-signal decision auditing**, not maximum comment volume. A finding should be grounded in evidence and tied to a potentially material consequence.

The system is designed to:

- distinguish evidence from assertion
- distinguish thesis quality from decision quality
- search for disconfirming evidence and alternative explanations
- recompute material calculations
- use scenarios and sensitivity when uncertainty is material
- surface uncertainty instead of manufacturing precision
- stop when additional work is unlikely to materially change the diagnosis

Static repository validation is a packaging check, not proof of model-level accuracy. Real-world evaluation should include adversarial cases and human review.

## Financial integrity

The skill will not fabricate market data, prices, financial statements, calculations, sources, probabilities, or performance claims. It should not convert incomplete information into false certainty.

For past decisions, it uses **Information-Set Lock**: evaluate the decision using what was reasonably knowable at the decision time, then analyze the outcome separately. A bad outcome does not by itself prove a bad process, and a good outcome does not by itself prove a good process.

## Limitations

- It cannot guarantee profits, returns, or future prices.
- It is not an automatic trading system, price oracle, or signal generator.
- Financial conclusions depend on the quality and completeness of the supplied evidence.
- Valuation and portfolio judgments may require domain-specific context that is unavailable from a generic dataset.
- Market conditions, liquidity, execution, taxes, and personal constraints may materially affect a real decision.
- It should not replace professional financial, tax, or legal advice where such advice is appropriate.
- The default system does not use an arbitrary overall health score; it uses explicit states, materiality, evidence sufficiency, and uncertainty.

## Repository structure

```text
financial-debugger/
├── SKILL.md
├── README.md
├── references/
│   ├── financial-reasoning.md
│   ├── evidence-audit.md
│   ├── source-hierarchy.md
│   ├── valuation-frameworks.md
│   ├── macro-frameworks.md
│   ├── portfolio-analysis.md
│   ├── personal-finance.md
│   ├── postmortem.md
│   └── full-audit-contract.md
├── templates/
│   ├── quick-debug.md
│   ├── deep-debug.md
│   ├── valuation-debug.md
│   ├── portfolio-debug.md
│   ├── postmortem.md
│   └── full-debug.md
├── examples/
│   ├── equity-deep.md
│   ├── crypto-decision.md
│   ├── macro-news.md
│   └── personal-finance.md
├── tests/
│   └── test-cases.md
├── scripts/
│   └── validate.py
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
└── QUALITY-GATES.md
```

## Roadmap

### v2.0.0

- Added `FULL FINANCIAL DEBUG` as the canonical broad-audit mode.
- Added short-prompt auto-trigger behavior for supplied financial artifacts.
- Added the canonical 20-module audit sweep.
- Required every full-audit module to appear in the final report.
- Added explicit `ERROR NOT FOUND` and `NOT ASSESSABLE` module states.
- Added primary-module / related-module finding identity to prevent double counting.
- Added finding and severity-count reconciliation checks.
- Added full-audit contract and report template.
- Added behavioral coverage for module completeness, auto-triggering, and output reconciliation.

### v1.8.2

- Mandatory Finding Report output contract for all material findings
- Strict epistemic rules against inferring base cases, probabilities, or outcomes from missing evidence
- Explicit separation of evidence correlation/dependence from proven evidence duplication
- Stronger valuation-method neutrality and portfolio-sizing discipline
- Finding schema: ID, Severity, Type, Location, Problem, Evidence, Reasoning, Impact, Recommended Action
- Expanded behavioral tests for output normalization and overclaim prevention

### v1.8.1

- Production-oriented financial reasoning audit workflow
- Adaptive Light, Standard, and Deep debug depth
- Evidence sufficiency and evidence-to-claim alignment
- Explicit assumption registry with dependency, sensitivity, scenario impact, and kill conditions
- Evidence, contradiction, methodology, numerical, valuation, scenario, sensitivity, expectations, risk, and reversibility audits
- Thesis-versus-decision distinction
- Decision materiality, Top 3 decision-changing findings, and Next Best Action
- Conditional forecast decomposition and expectation audit
- Post-mortem Information-Set Lock
- Decision Kill Switches and Next Best Action outputs
- Reusable references, templates, examples, adversarial tests, and repository validation

### Future

- Expanded domain-specific benchmark suites
- More automated sensitivity and dependency reporting
- Additional financial-statement and portfolio edge cases
- Broader evaluation tooling for false positives and decision-changing findings

## License

Released under the MIT License. See `LICENSE`.

## Ecosystem context

Financial Debugger is one component of a broader **Debugger Series**: tools built around the idea that many bad outcomes come from errors in the reasoning process before the final answer or decision.

## Final hardening

v1.9.2 is the final contract-hardening release. It extends v1.9.1 with deterministic module-state semantics, source-verification provenance, recovery-history traceability, arithmetic-vs-forecast separation, and synthesis/action status handling.

v1.9.1 hardened the full-audit contract in five areas: `NOT ASSESSABLE` vs `ERROR NOT FOUND`, primary-module deduplication, evidence provenance, materiality/severity calibration, and calculation reproducibility. Every full audit ends with an **Audit Integrity Check** that reconciles module execution, unique findings, ownership, and decision-changing links.

## Validation

Run:

```bash
python scripts/validate.py
```

before release. Static validation checks repository integrity and required test coverage; it does not prove that the model will make every financial judgment correctly.
