---
title: "Operating Profitability and Expected Stock Returns in ASEAN Markets"
category: references
tags: [asset-pricing, profitability, emerging-markets, asean, famamacbeth, factor-investing]
relationships:
  - target: "[[concepts/fama-macbeth-two-stage-cross-sectional-regression]]"
    type: derived_from
  - target: "[[concepts/cash-based-operating-profitability]]"
    type: related_to
  - target: "[[references/ball2016-accruals-cash-flows-operating-profitability]]"
    type: related_to
  - target: "[[references/fama1973-risk-return-equilibrium-empirical-tests]]"
    type: related_to
  - target: "[[concepts/ratio-hierarchy-for-profitability-and-growth]]"
    type: related_to
  - target: "[[references/novy-marx2013-other-side-of-value]]"
    type: related_to
  - target: "[[concepts/gross-profitability-premium]]"
    type: related_to
  - target: "[[concepts/operating-and-financial-leverage-spreading]]"
    type: related_to
  - target: "[[references/nissim2001-ratio-analysis-equity-valuation]]"
    type: related_to
sources:
  - _papers/kim2020profitability/kim2020profitability-extracted.md
  - _papers/kim2020profitability/kim2020profitability.md
summary: >-
  Operating profitability (OP/book equity and OP/book assets) raises expected stock returns across ASEAN markets 2010-2019; factor-adjusted decile spreads are significant.
provenance:
  extracted: 0.79
  inferred: 0.14
  ambiguous: 0.07
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-25
tier: core
created: 2026-10-25T11:47:49Z
updated: 2026-10-30T14:38:55Z
---

# Operating Profitability and Expected Stock Returns in ASEAN Markets

> [!tldr] Kim and Hoang show operating profitability sorted by book equity (OP/BE) and book assets (OP/BA) positively predicts expected returns in Indonesia, Thailand, Malaysia, Philippines and Vietnam, 2010-2019.

## Problem & Contribution

- ASEAN-5 sample: Indonesia (128), Thailand (275), Malaysia (444), Philippines (98), Vietnam (65) non-financial firms — 1,010 firms, 121,200 firm-month observations, Jan 2010 - Dec 2019, S&P Market Intelligence. Singapore, Myanmar, Cambodia excluded for data limits.
- OP = gross profit − SG&A − interest expense; ratios OP/BE and OP/BA; hypotheses test whether profitability raises expected returns and whether Fama-French factors predict in ASEAN.
- First joint ASEAN profitability study, following Berggrun et al. (Latin America) and Cakici et al. (Asian crisis) lines.

## Method

$$(R_i - R_F)_t = a_0 + \beta_1 (OP/BE)_i + \beta_2 ME + \beta_3 B/M + \beta_4 MOM + \varepsilon_i$$

Fama-MacBeth regressions (Eq. 3, and Eq. 4 for OP/BA) with size, book-to-market and momentum controls; Newey-West corrections. Decile portfolios P1-P10 tested with Fama-French three-factor regressions (Eq. 2) using factors from the Fama/French Emerging 5 Factors database; 1% winsorization. Country risk-free rates proxied by local government bond series (e.g. GIDN1YR for Indonesia, GTTHB2YR for Thailand).

## Results

| Spec (OP/BE, FM) | Coefficient (p) |
|---|---|
| Univariate | 0.0415 (0.000) |
| + size | 0.0366 (0.000) |
| + size, B/M | 0.0196 (0.000) |
| + size, B/M, momentum (full) | 0.0228 (0.000); ME −0.0017***, B/M −0.0160*, MOM ns |
| OP/BA, Table 6 col. 4 | 0.0339 (narrative-cited) |

- Decile returns (OP/BE): P1 avg −0.0013, P10 avg 0.0149; P10 factor-adjusted intercept 0.0115, P1-P10 spread 0.0171 with p = 0.000.
- The paper's text claims P10−P1 is "not statistically different" and intercepts ascend monotonically, which contradicts the reported decile table significances. ^[ambiguous]
- SMB and HML factors do not predict ASEAN returns, contrary to the Fama-French 1993 result.

## Limitations

- Only a 3-factor model; SMB/HML come from a 26-country emerging-factor database, one risk-free proxy per market.
- 2010-2019 window and single-region sample; OP here is accrual-laden accounting profit, not the cash-based measure of Ball et al., so it is not the same signal as cash-based operating profitability. ^[inferred]
- Extending the global profitability literature into ASEAN markets suggests the signal survives in weaker institutions and disclosure standards. ^[inferred]

## Related

- [[concepts/fama-macbeth-two-stage-cross-sectional-regression]]
- [[concepts/cash-based-operating-profitability]]
- [[references/ball2016-accruals-cash-flows-operating-profitability]]
- [[concepts/ratio-hierarchy-for-profitability-and-growth]] — the ratio system these profitability measures sit in
- [[references/novy-marx2013-other-side-of-value]] — the U.S. gross-profitability premium that this ASEAN OP evidence parallels

## Bibliographic Record

- Citation key: kim2020profitability — Kim, So Young; Hoang, Phan, "Operating Profitability and Expected Stock Returns in ASEAN Markets", SSRN preprint 3926614, 2020-12-25.
- DOI: none (preprint). Canonical URL: https://papers.ssrn.com/abstract=3926614
- Authors: Kim (Pusan National University), Hoang (Duy Tan University).
- Companion metadata: [[_papers/kim2020profitability/kim2020profitability.md|kim2020profitability metadata]]

## Sources

- [[_papers/kim2020profitability/kim2020profitability-extracted.md]]
- [[_papers/kim2020profitability/kim2020profitability.md]]
