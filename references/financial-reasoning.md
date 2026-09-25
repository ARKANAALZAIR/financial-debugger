# Financial Reasoning Framework

## Core chain
FACT → EVIDENCE → ASSUMPTION → METHOD → REASONING → SCENARIO → RISK/UNCERTAINTY → DECISION

## Reasoning tests

### 1. Validity
Does the conclusion actually follow from the premises?

### 2. Causality
Does the evidence establish a causal mechanism, or only a correlation/temporal sequence?

### 3. Completeness
What material variable is missing?

### 4. Comparability
Are the compared figures defined over the same period, accounting basis, currency, and business scope?

### 5. Base rates
Is the claim consistent with historical frequencies or sector/business constraints?

### 6. Alternative explanation
What else could explain the observation?

### 7. Counterfactual
Would the decision still make sense if the key assumption failed?

### 8. Sensitivity
How much does the decision change if a key assumption moves modestly?

### 9. Reversibility
How costly is it to change the decision later?

## Decision states

- SUPPORTED: core reasoning is adequately supported for the scope tested.
- FRAGILE: conclusion depends heavily on uncertain or sensitive assumptions.
- CONTESTED: meaningful evidence points in opposing directions.
- INSUFFICIENT EVIDENCE: critical evidence is missing.
- INVALID: core claim, input, or method is demonstrably invalid for the question.
- NOT MATERIAL: identified issue is unlikely to change the decision.

## Useful decomposition

A financial claim often decomposes into:

Observation → Interpretation → Mechanism → Outcome → Decision

The debugger should not allow the user to silently jump from Observation to Decision.
