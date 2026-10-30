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
  - target: "[[references/novy-marx2013-other-side-of-value]]"
    type: related_to
  - target: "[[concepts/gross-profitability-premium]]"
    type: related_to
  - target: "[[concepts/negative-book-equity-style-classification]]"
    type: related_to
  - target: "[[concepts/operating-and-financial-leverage-spreading]]"
    type: related_to
  - target: "[[concepts/residual-earnings-equity-valuation]]"
    type: related_to
  - target: "[[references/beatty2014-financial-accounting-in-banking]]"
    type: related_to
  - target: "[[references/black1992-global-portfolio-optimization]]"
    type: related_to
  - target: "[[references/brown2007-negative-book-equity-stocks]]"
    type: related_to
  - target: "[[references/nissim2001-ratio-analysis-equity-valuation]]"
    type: related_to
  - target: "[[references/pincus2007-accrual-anomaly-international-evidence]]"
    type: related_to
  - target: "[[references/sloan1996-accruals-cash-flow-stock-prices]]"
    type: related_to
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
base_confidence: 0.87
lifecycle: draft
lifecycle_changed: 2026-10-25
tier: core
created: 2026-10-22T19:33:55Z
updated: 2026-10-30T14:38:55Z
---

# Cash-Based Operating Profitability

Cash-based operating profitability (CbOP) isolates profitability from accrual adjustments, focusing on cash-generating operating performance as a return-prediction signal.

## Key Ideas

- Traditional operating profitability mixes cash and accrual components.
- CbOP keeps the cash component and removes accrual effects.
- In the cited evidence, CbOP retains strong predictive power while accruals lose significance in joint tests.
- Kakinuma's FCF = cash flow from operations over market cap in Thailand (June 2002-June 2019) behaves like CbOP: it predicts returns and gives the most consistent top-quintile performance (Sharpe 0.61 vs market 0.32, information ratio 2.45). ^[extracted]
- Kim & Hoang find that accrual-heavy OP (gross profit − SG&A − interest expense) also predicts ASEAN returns, so cash-basis dominance is not universal across all markets. ^[inferred]
- Gross-level profitability is the complement of this cash-based signal: [[references/novy-marx2013-other-side-of-value|Novy-Marx 2013]] shows gross profits-to-assets keeps its Fama-MacBeth power after controls for accruals and R&D, so gross-profitability and cash-based signals are distinct measures, not substitutes. ^[inferred]

## Why It Matters

- Provides a cleaner profitability factor for cross-sectional stock-return models.
- Reduces overlap between profitability and accrual-anomaly signals.
- Supports simpler factor design with stronger risk-adjusted performance in the tested sample.

## Related

- [[references/sloan1996-accruals-cash-flow-stock-prices]] — the accrual/cash-flow split and the 10.4% hedge behind the CbOP literature

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
