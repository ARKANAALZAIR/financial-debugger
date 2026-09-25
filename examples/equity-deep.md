# Example — Equity Deep Debug

User: “Revenue AI masih tumbuh, earnings kuat, valuation murah, jadi saham X bisa naik 2x dalam 12 bulan. Gue mau masuk Rp200 juta.”

Expected diagnosis:
- Depth: DEEP
- Thesis state and decision state are evaluated separately.
- The long-term business thesis can be partially supported while the 12-month 2x decision remains fragile.
- “Cheap” must be demonstrated using appropriate valuation context, not a single multiple.
- Build an explicit Assumption Registry for revenue growth, margins, valuation multiple, macro assumptions, and the 2x outcome.
- Forecast through operating outlook → earnings/cash flow → valuation → implied value → return decomposition.
- Build bear/base/bull scenarios and identify the assumptions that cause the largest sensitivity.
- Audit whether the expected improvement is already reflected in valuation/market expectations when evidence exists.
- Search for contradictory evidence and alternative explanations.
- Evaluate the Rp200m position relative to the user’s stated portfolio and economic exposure.
- Produce Top 3 decision-changing findings, kill switches, and next-best actions.

Important: do not invent current company numbers. Use verified inputs or mark them unverified.
