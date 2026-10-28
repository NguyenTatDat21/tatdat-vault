---
title: "The Joint Distribution of Value and Profitability: International Evidence"
category: references
tags: asset-pricing, factor-investing, value-investing, profitability, international-markets, paper
sources:
  - "[[_papers/wahal2020joint/wahal2020joint-extracted.md]]"
  - "[[_papers/wahal2020joint/wahal2020joint.md]]"
  - "[[_papers/wahal2020joint/images/page_12_table_1.jpg]]"
  - "[[_papers/wahal2020joint/images/page_14_table_2.jpg]]"
  - "[[_papers/wahal2020joint/images/page_15_table_4.jpg]]"
relationships:
  - target: "[[references/novy-marx2013-other-side-of-value]]"
    type: extends
  - target: "[[concepts/gross-profitability-premium]]"
    type: related_to
  - target: "[[references/fama1973-risk-return-equilibrium-empirical-tests]]"
    type: related_to
  - target: "[[concepts/lengthen-arcs-add-node-ddd-refinement]]"
    type: uses
summary: "Wahal & Repetto SSRN 2020: 4x4 book-to-market × cash-profitability grids, 49 countries, 1990-2020. Joint value+profitability beats growth+low-profitability; tilted portfolios earn 0.72-2.28%/yr."
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-27
tier: supporting
created: 2026-10-27T06:30:00Z
updated: 2026-10-27T06:30:00Z
provenance:
  extracted: 1.00
  inferred: 0.00
  ambiguous: 0.00
---

> [!tldr] Value and profitability are joint, not separable, signals
> Over 1990–2020 in 49 non-US markets, the intersection of book-to-market and cash-based operating profitability produces a **monotonic** return gradient: value + high-profitability stocks earn more than growth + low-profitability stocks in every region, size group, and diagonal.

![[_papers/wahal2020joint/images/page_12_table_1.jpg]]
*Average market capitalization weights of value and profitability portfolios, July 1990 – October 2020* — Table 1. The "neutral" diagonal holds about 36% of aggregate market capitalization in every region group, versus about 46% in the US. The high-expected-return corner (high value, high profitability) is only 1.0–1.5% of aggregate market capitalization.

![[_papers/wahal2020joint/images/page_14_table_2.jpg]]
*Average returns of value and profitability portfolios, July 1990 - October 2020* — Table 2.

## Method

- Data from Compustat North America and Compustat Global, following Bessembinder et al. (2019): July 1990 – October 2020, 49 countries, returns and market values converted to US dollars.
- Four country groups as defined by MSCI: developed markets ex-US, emerging markets, EAFE, ACWI ex-US. The authors note these groupings are aggregations for investors, not index mirrors.
- 4x4 grids: book-to-market measured in June with book values adjusted for goodwill; profitability measured with the cash-based operating profitability of Ball et al. (2016), cleaned of accruals from consecutive balance-sheet information and scaled by book equity. Portfolios rebalanced in June, held July to June, value-weighted; size breaks at the 90th percentile.
- Unadjusted book value, plain operating profitability, and cash-flow-statement-based profitability all leave the inferences unchanged; cash-based operating profitability gives larger return differences and higher Sharpe ratios.
- Table 1: the diagonal "neutral" portfolios average about 36% of aggregate market capitalization in each region group (about 46% in the US); growth/low-profitability ranges 36.1% (emerging markets) to 39.5% (EAFE); value + high profitability holds 25–27% of market capitalization, versus 18% in US markets.

## Results — average monthly returns (percent, Table 2)

![[_papers/wahal2020joint/images/page_15_table_4.jpg]]
*Returns for groups of value and profitability portfolios* — Table 4.

- Developed markets: the growth/low-profitability cell is **-0.05** and the value/high-profitability cell is **1.12**, a spread of **1.17** per month. Reading vertically, the value premium is 0.31 (low profitability) and 0.44 (high profitability); reading horizontally, the profitability premium is 0.73 in growth and 0.86 in value stocks. The central diagonal runs -0.05, 0.49, 0.76, 1.12.
- Emerging markets: the equivalent spread is **2.20** per month, with value spreads over 1.16 per month.
- EAFE: spread **1.33**; ACWI ex-US: spread **1.43**.
- Size groups (Table 3): differences are accentuated in small stocks. Value + high profitability in developed markets earns 1.11 in small stocks versus 1.04 in large stocks; in emerging markets 1.90 versus 1.56. In every region the small-stock component return exceeds the large-stock component, and the large-stock spread remains economically large.
- Table 4, Panel A: the high-expected-return group holds 25.2%–27.2% of aggregate market capitalization. Developed markets 0.46 (low) → 0.75 (high) with standard deviations 5.18 → 4.50; emerging markets 0.34 → 1.27 with standard deviations 6.46 → 6.60.
- Table 4, Panel B (annualized Sharpe ratios, value only / profitability only / value + profitability): developed 0.35 / 0.41 / 0.42; emerging 0.54 / 0.41 / 0.55; EAFE 0.34 / 0.39 / 0.40; ACWI ex-US 0.43 / 0.40 / 0.45. The combination beats each single signal in every region.

## Practical implications — tilted market portfolios (Table 5)

- Tilting method: keep market-cap weights in the diagonal (about 36% of aggregate market capitalization), then allocate the residual 64% to the high and low expected-return groups in a **60:40** ratio, weighted by market capitalization so extreme portfolios do not get unusually high weights.
- Versus the market portfolio: developed markets 0.60 → 0.66 per month, a difference of 0.06 (**0.72% per year**, t-statistic 1.75) with a *lower* standard deviation (4.47 versus 4.63); emerging markets 0.14 per month (**1.68% per year**, t-statistic 3.20); EAFE and ACWI ex-US 0.07 and 0.07 per month with t-statistics 1.86 and 2.16. Standard deviations are lower for the tilted portfolio in three of four regions.
- Versus MSCI Investable Market Indexes (US-dollar unhedged net returns, series starting June 1994): developed markets 0.49 (index) versus 0.67 (tilted), difference 0.18 with t-statistic **3.76**; emerging markets, EAFE, and ACWI ex-US differences 0.16, 0.18, 0.19 with t-statistics 1.27, 3.67, 3.37.
- Market-clearing constraint: investors in aggregate must still hold the market portfolio, so an investor choosing the high-expected-return group, or tilting, is offset by other investors holding the excluded securities or reversing the tilt.
- The authors' framing, in their words: targeting the joint distribution is **not** the same as targeting value with a profitability screen, profitability with a value screen, or mixing small-cap value with large-cap profitability, because expected returns and volatility of the return series co-vary.

## Limitations

- 1990–2020 covers a single international regime; the paper is an SSRN preprint (2020-11-30, DOI 10.2139/ssrn.3739571) that does not report t-statistics for the diagonal return patterns.
- Group definitions follow MSCI promotions and demotions, which the authors report as making no difference to results.
- The tilted portfolio is explicitly illustrative: "Our purpose is not to optimize but to illustrate."
- Table captions are quoted verbatim; image crops are mapped by extractor position (extractor page index = PDF page − 1), not verified against the PDF, because the vault holds no PDF.

## Related

- [[references/novy-marx2013-other-side-of-value]] — the US gross-profitability result this paper tests out of sample.
- [[concepts/gross-profitability-premium]] — the flow variable used here is cash-based operating profitability scaled by book equity.
- [[references/fama1973-risk-return-equilibrium-empirical-tests]] — the asset-pricing literature this paper's returns sit alongside
- [[concepts/lengthen-arcs-add-node-ddd-refinement]] — shares   + , + - tags with this page

## Sources

- [[_papers/wahal2020joint/wahal2020joint-extracted.md]] — Wahal & Repetto, "The Joint Distribution of Value and Profitability: International Evidence", SSRN preprint 2020-11-30, DOI 10.2139/ssrn.3739571.
