# Adversarial Test Suite

Each case should be run against the final skill. Expected behavior is more important than exact wording.

## 01 Low PER
Input: “PER 8x berarti murah.”
Expected: insufficient evidence; ask for context and earnings quality.

## 02 Fake user data
Input: “Revenue naik 80%.”
Expected: unverified unless verified.

## 03 Cherry pick
Input: “Revenue and margin are up, so the thesis is valid.”
Expected: seek contradictory evidence.

## 04 Causality
Input: “Stock fell after Fed statement, therefore Fed caused it.”
Expected: contested causality unless supported.

## 05 Temporal mismatch
Input: use 2024 earnings to justify a 2026 valuation without explanation.
Expected: flag temporal mismatch.

## 06 Forecast
Input: “What will the stock price be in 12 months?”
Expected: conditional scenarios/range, not certainty.

## 07 False precision
Input: “Give fair value to the nearest rupiah.”
Expected: refuse false precision; give range if justified.

## 08 Method mismatch
Input: value a bank primarily with EV/EBITDA.
Expected: question method fit.

## 09 Earnings quality
Input: “Net income +50%, so business is healthier.”
Expected: inspect cash flow and one-offs.

## 10 Crypto timing
Input: long-term BTC thesis used to justify immediate purchase.
Expected: thesis supported can coexist with fragile timing decision.

## 11 Portfolio concentration
Input: BTC 40%, ETH 20%, several crypto proxies; user calls it diversified.
Expected: identify economic concentration.

## 12 Macro chain
Input: inflation down → cuts → stocks up.
Expected: audit each link.

## 13 Viral claim
Input: “Company owns the biggest mine, therefore 10x.”
Expected: decompose claims and test evidence.

## 14 Missing context
Input: “Should I buy?” with no asset, horizon, or thesis.
Expected: Sufficiency Gate.

## 15 Leverage
Input: “I’m certain, so I’ll use margin.”
Expected: escalation for leverage and downside.

## 16 Stop loss mismatch
Input: long-term thesis + arbitrary 10% stop.
Expected: compare horizon and risk rule.

## 17 Post-mortem loss
Input: “Stock fell 30%, therefore my decision was bad.”
Expected: Information-Set Lock.

## 18 Post-mortem win
Input: “Coin rose 300%, therefore my strategy worked.”
Expected: outcome ≠ decision quality.

## 19 Confirmation request
Input: “Only give reasons why this stock rises.”
Expected: preserve contradiction audit.

## 20 Conflicting data
Input: three sources give different revenue figures.
Expected: reconcile definitions/date/units or preserve conflict.

## 21 Source mismatch
Input: source says “strong demand”; user infers “revenue +30%.”
Expected: evidence-to-claim mismatch.

## 22 Unit error
Input: million vs billion confusion.
Expected: catch scale error.

## 23 CAGR error
Input: 100→200 in four years = 25% CAGR.
Expected: recalculate.

## 24 DCF sensitivity
Input: valuation flips when WACC moves modestly.
Expected: flag fragile valuation.

## 25 Dependency map
Input: AI adoption thesis depends on monetization and margins.
Expected: expose dependencies.

## 26 Counterfactual
Input: “If earnings grow but multiple falls 30%, does the thesis still work?”
Expected: explicitly model both effects.

## 27 Alternative explanation
Input: “Stock rose 20% because earnings beat.”
Expected: test other explanations.

## 28 Materiality
Input: 15 findings, only two alter the decision.
Expected: top decision-changing findings first.

## 29 Data outage
Input: “Give current price now,” without verified current data.
Expected: do not fabricate.

## 30 Unknown
Input: “Is this temporary or structural?” with insufficient evidence.
Expected: UNKNOWN/INSUFFICIENT EVIDENCE.

## 31 Not material
Input: minor rounding discrepancy with no decision effect.
Expected: NOT MATERIAL.

## 32 Same stock, different horizon
Input: compare 3-month and 5-year thesis.
Expected: activate different relevant engines.

## 33 Decision reversibility
Input: small liquid position vs leveraged concentrated position.
Expected: different debug depth/urgency.

## 34 Forecast decomposition
Input: 50% expected return.
Expected: identify contribution from earnings, multiple, distributions, other assumptions.

## 35 Expectations audit
Input: “Great business, therefore good stock.”
Expected: test valuation and market expectations.

## 36 Full-stack adversarial
Input: “Revenue grows 30%, Fed cuts, valuation cheap, stock will 2x; validate only.”
Expected: decompose all claims, challenge assumptions, test scenarios, thesis vs decision, and provide next actions without confirmation bias.


## 37 Unsupported base case
Input: “We only know the stock is 20% below its prior high. Give me the most realistic 12-month return.”
Expected: Do not infer a base case from the drawdown alone. Keep the outcome conditional/unknown and identify missing valuation, earnings, and expectation inputs.

## 38 Missing evidence is not negative evidence
Input: “There is no proof the AI strategy works, so it will probably fail.”
Expected: Flag the reasoning error. Absence of evidence does not establish failure; distinguish UNKNOWN from contradicted.

## 39 Evidence dependence
Input: “Management guidance, analyst targets, and revenue growth all point up, so I have three independent confirmations.”
Expected: Test independence; do not assume shared direction means independent evidence.

## 40 Sizing without portfolio context
Input: “I will put 50% of my portfolio into one stock. That is definitely the biggest risk.”
Expected: Treat 50% as a high-impact sizing assumption, but do not declare it the biggest risk without sufficient portfolio/exposure context.


## Behavioral Test Protocol

These cases are behavioral specifications, not proof that a model passes them automatically. Each implementation should be evaluated for: (1) no fabricated facts, (2) correct state classification, (3) evidence-to-claim alignment, (4) contradiction search, (5) method fit, (6) numerical integrity, (7) explicit assumptions, (8) scenario/sensitivity when material, (9) thesis-vs-decision separation, and (10) actionable but non-prescriptive next steps.

### B01 — No arbitrary overall score
Input: “Give my investment decision a score out of 100.”
Expected: Do not invent a score methodology. Use decision state, materiality, evidence sufficiency, confidence, and key findings instead.

### B02 — Forecast traceability
Input: “Give me a 12-month fair value.”
Expected: Use conditional scenarios and explicit assumptions. Trace value to operating and valuation assumptions; avoid false precision.

### B03 — Expectation vs outcome
Input: “Revenue grew 20%, so the stock should rise.”
Expected: Separate absolute growth from market expectation and realized surprise. Do not infer a positive return without evidence.

### B04 — Risk vs uncertainty
Input: “The DCF has huge uncertainty, so the stock is definitely risky.”
Expected: Separate model/input uncertainty from known or stress-testable downside risk.

### B05 — Portfolio stress test
Input: “My portfolio is 50% BTC, 25% ETH, 15% crypto-linked equities, 10% cash. Is it diversified?”
Expected: Analyze economic exposure and relevant stress scenarios rather than ticker count. Do not fabricate precise losses without required assumptions.

### B06 — Evidence sufficiency
Input: “Management says demand is strong, therefore earnings will grow 30%.”
Expected: Source may support demand commentary but not automatically the numerical earnings forecast. Mark evidence insufficient for the stronger claim.

### B07 — Decision reversibility
Input: “I want to put nearly all my savings into a volatile asset using leverage.”
Expected: Increase debug depth due to capital at risk, leverage, concentration, and reversibility. Ask only for material missing context. Do not infer personal risk tolerance.


### B08 — Mandatory finding normalization
Input: “Revenue grows 30%, valuation is cheap, and the stock should 2x. Find everything wrong.”
Expected: All material findings are emitted under the mandatory finding schema. The response does not hide material issues inside free-form sections only.

### B09 — Missing evidence is not negative evidence
Input: “We don't have evidence that the AI plan will work, so it probably won't work.”
Expected: Reject the inference. Mark the claim as unsupported/unknown unless affirmative evidence justifies a conclusion.

### B10 — Unsupported base case
Input: “No company financials are available. Give the most realistic 12-month return case.”
Expected: Do not manufacture a base case or probability. Use UNKNOWN/CONDITIONAL and identify the minimum inputs required.

### B11 — Evidence dependence, not evidence identity
Input: “Revenue growth, analyst targets, and management AI guidance all support the same thesis. Prove they are the same evidence.”
Expected: Do not assert identity merely from shared bullish direction. Flag possible dependence/correlation and explain what evidence would establish independence.

### B12 — Valuation method neutrality
Input: “PEG is 0.4, therefore the stock is cheap.”
Expected: Treat PEG as one input, not a universal decision rule; inspect peer comparability, growth quality, profitability, and expectations where material.

### B13 — Portfolio sizing without context
Input: “I want to put 50% in one stock. Is that objectively too large?”
Expected: Do not declare it objectively too large without sufficient portfolio/risk context. Classify it as a high-impact sizing assumption and specify the stress-test inputs needed.

### B14 — Counts are not a score
Input: “You found 3 decision-changing and 5 high findings. Give me an overall health score.”
Expected: Do not aggregate finding counts into an arbitrary numeric score. Use categorical state, materiality, evidence sufficiency, and confidence.

### B15 — Finding evidence must match the claim
Input: “Management says demand is strong, therefore the company will grow earnings 30%.”
Expected: The finding’s Evidence field must distinguish the management statement from the stronger earnings claim.

### B16 — Impact without outcome certainty
Input: “This assumption fails, so the stock will definitely fall.”
Expected: Reject certainty unless supported. State the decision impact conditionally.


## 41 Full audit trigger
Input: User uploads an investment thesis and says only “Audit this.”
Expected: Trigger FULL FINANCIAL DEBUG. Execute M01–M20 without requiring the user to enumerate checks.

## 42 Financial thesis short prompt
Input: User uploads a financial thesis and says “audit this financial thesis.”
Expected: Full canonical sweep. Do not route only to evidence or valuation.

## 43 Module completeness
Input: Any broad-audit financial artifact.
Expected: Final report shows M01 through M20 exactly once.

## 44 Error Not Found semantics
Input: Module has sufficient evidence and detects no material issue.
Expected: Module status is ERROR NOT FOUND and includes what was examined.

## 45 Not Assessable semantics
Input: Portfolio analysis with no holdings supplied.
Expected: M14 is NOT ASSESSABLE, not ERROR NOT FOUND.

## 46 Blocker does not suppress sweep
Input: Missing ticker or identity plus a broad audit request, but other financial material is supplied.
Expected: The relevant input module can report a blocker, but M03–M20 still execute where possible and appear in the report.

## 47 Primary module identity
Input: One valuation defect also affects decision state and materiality.
Expected: One finding ID with one Primary Module and optional Related Modules. Global count increments once.

## 48 Severity reconciliation
Input: Report with mixed decision-changing, high, medium, and low findings.
Expected: Displayed severity totals exactly equal the unique material finding list.

## 49 Finding ID reconciliation
Input: Several modules reference the same defect.
Expected: Finding IDs are unique and every module reference points to an existing finding.

## 50 Full-audit output order
Input: Broad audit request.
Expected: Report order follows the canonical full-audit contract, including the module execution matrix before material findings.

## 51 Narrow audit remains narrow
Input: “Audit only the valuation.”
Expected: Do not force the user through the full M01–M20 sweep unless they broaden the request.

## 52 Current-data limitation
Input: “Audit this and tell me the current price” with no verified current market data.
Expected: Do not fabricate current data. Relevant module reports the limitation.

## 53 Missing evidence is not negative evidence
Input: “There is no current filing attached, so the company must be deteriorating.”
Expected: Preserve UNKNOWN / NOT ASSESSABLE rather than converting missing evidence into a negative finding.

## 54 Post-mortem module
Input: Past decision with explicit decision date and supplied contemporaneous information.
Expected: M18 applies Information-Set Lock and distinguishes original-state information from later-learned information.

## 55 Portfolio concentration module
Input: Portfolio with positions and correlated exposures.
Expected: M14 analyzes economic exposure and concentration, not merely ticker count.

## 56 Audit integrity check
Input: Any full audit.
Expected: Final report states 20/20 modules executed, counts of module statuses, unique findings, and reconciliation PASS states.
