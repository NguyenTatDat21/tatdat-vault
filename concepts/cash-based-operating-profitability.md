---
title: Cash-Based Operating Profitability
category: concepts
tags: [asset-pricing, profitability, accruals, factor-investing]
relationships:
  - target: "[[references/ball2016-accruals-cash-flows-operating-profitability]]"
    type: derived_from
  - target: "[[concepts/ordering-information-portfolio-selection]]"
    type: related_to
  - target: "[[references/almgren2004-optimal-portfolios-ordering-information]]"
    type: related_to
  - target: "[[references/kakinuma2020-empirical-profitability-thailand]]"
    type: related_to
  - target: "[[references/kim2020-profitability-asean-stocks]]"
    type: related_to
  - target: "[[concepts/ratio-hierarchy-for-profitability-and-growth]]"
    type: extends
sources:
  - _papers/ball2016accruals/ball2016accruals-extracted.md
  - _papers/ball2016accruals/ball2016accruals.md
  - _papers/kakinuma2020empirical/kakinuma2020empirical-extracted.md
  - _papers/kakinuma2020empirical/kakinuma2020empirical.md
  - _papers/kim2020profitability/kim2020profitability-extracted.md
  - _papers/kim2020profitability/kim2020profitability.md
summary: >-
  Profitability signal based on cash-flow components; Thai cash-flow evidence (Kakinuma) and accrual-heavy ASEAN OP results (Kim & Hoang) refine its cross-market boundaries.
provenance:
  extracted: 0.80
  inferred: 0.14
  ambiguous: 0.06
base_confidence: 1.0
lifecycle: draft
lifecycle_changed: 2026-10-25
tier: supporting
created: 2026-10-22T19:33:55Z
updated: 2026-10-25T11:47:49Z
---

# Cash-Based Operating Profitability

Cash-based operating profitability (CbOP) isolates profitability from accrual adjustments, focusing on cash-generating operating performance as a return-prediction signal.

## Key Ideas

- Traditional operating profitability mixes cash and accrual components.
- CbOP keeps the cash component and removes accrual effects.
- In the cited evidence, CbOP retains strong predictive power while accruals lose significance in joint tests.
- Kakinuma's FCF = cash flow from operations over market cap in Thailand (June 2002-June 2019) behaves like CbOP: it predicts returns and gives the most consistent top-quintile performance (Sharpe 0.61 vs market 0.32, information ratio 2.45). ^[extracted]
- Kim & Hoang find that accrual-heavy OP (gross profit − SG&A − interest expense) also predicts ASEAN returns, so cash-basis dominance is not universal across all markets. ^[inferred]

## Why It Matters

- Provides a cleaner profitability factor for cross-sectional stock-return models.
- Reduces overlap between profitability and accrual-anomaly signals.
- Supports simpler factor design with stronger risk-adjusted performance in the tested sample.

## Related

- [[references/ball2016-accruals-cash-flows-operating-profitability]]
- [[concepts/ordering-information-portfolio-selection]]
- [[references/almgren2004-optimal-portfolios-ordering-information]]
- [[references/kakinuma2020-empirical-profitability-thailand]]
- [[references/kim2020-profitability-asean-stocks]]
- [[concepts/ratio-hierarchy-for-profitability-and-growth]] — the accrual-based driver system this cash-based measure complements

## Open Questions

- How stable is CbOP under different accounting regimes and disclosure standards?
- Does CbOP retain edge after transaction costs and implementation frictions? ^[inferred]

## Sources

- [[_papers/ball2016accruals/ball2016accruals-extracted.md]]
- [[_papers/ball2016accruals/ball2016accruals.md]]
- [[_papers/kakinuma2020empirical/kakinuma2020empirical-extracted.md]]
- [[_papers/kakinuma2020empirical/kakinuma2020empirical.md]]
- [[_papers/kim2020profitability/kim2020profitability-extracted.md]]
- [[_papers/kim2020profitability/kim2020profitability.md]]
