---
title: >-
  Ratio Mean Reversion and Continuing-Value Benchmarks
category: concepts
aliases: [central tendency of ratios, fade rate, continuing value selection, portfolio tracking, survivorship]
tags: [mean-reversion, forecasting, continuing-value, time-series, rankings, survivorship, benchmarks, priors, fade-rate, cost-of-capital]
relationships:
  - target: "[[concepts/residual-earnings-equity-valuation]]"
    type: uses
  - target: "[[concepts/ratio-hierarchy-for-profitability-and-growth]]"
    type: extends
  - target: "[[concepts/operating-and-financial-leverage-spreading]]"
    type: uses
  - target: "[[concepts/fama-macbeth-two-stage-cross-sectional-regression]]"
    type: related_to
  - target: "[[concepts/statistical-investigation-lifecycle]]"
    type: related_to
  - target: "[[concepts/predictive-to-prescriptive-analytics]]"
    type: related_to
  - target: "[[references/nissim2001-ratio-analysis-equity-valuation]]"
    type: derived_from
sources:
  - _papers/nissim2001ratio/nissim2001ratio-extracted.md
  - _papers/nissim2001ratio/nissim2001ratio.md
summary: >-
  Drivers fade toward economy-wide levels: RE rank corr. 0.55→0.18 over 5 years, RNOA var. ratio 0.127 at t=5, FLEV 0.937 at t=1 — so CV2/CV3, not CV1, are the typical case.
provenance:
  extracted: 1.00
  inferred: 0.00
  ambiguous: 0.00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-26T05:12:09Z
tier: supporting
created: 2026-10-26T05:12:09Z
updated: 2026-10-26T05:12:09Z
---

# Ratio Mean Reversion and Continuing-Value Benchmarks

> [!tldr] Rank firms on a driver in year 0, follow the median of each portfolio for five years. **Extreme values become typical values**: correlations with the lagged ratio decay and variance ratios collapse. This is the evidence that tells you which [[concepts/residual-earnings-equity-valuation|continuing-value rule]] to use, and what level to set it at.

## Method

Ratios ranked in a base year, firms sorted into ten portfolios, the median tracked for five following years. Base years **1964, 1969, 1974, 1979, 1984, 1989, 1994**; figures report the mean over the seven replications. Firms that cease to exist drop out, so ex post averages may be biased relative to ex ante for going concerns (survivorship).

## Fade rates (Table 3, Spearman $corr_t$ and portfolio variance ratio $var_t/var_0$)

| Ratio | t=1 | t=2 | t=3 | t=4 | t=5 | $var_5/var_0$ |
|---|---|---|---|---|---|---|
| Residual Earnings (RE) | 0.551 | 0.372 | 0.257 | 0.200 | 0.176 | 0.209 |
| Operating Residual Earnings (ReOI) | 0.653 | 0.496 | 0.397 | 0.349 | 0.327 | 0.568 |
| FLEV | 0.937 | 0.846 | 0.781 | 0.735 | 0.700 | 0.526 |
| ROCE | 0.618 | 0.425 | 0.311 | 0.253 | 0.230 | 0.067 |
| RNOA | 0.665 | 0.485 | 0.377 | 0.320 | 0.298 | 0.127 |
| Growth in CSE | 0.659 | 0.307 | 0.190 | 0.129 | 0.105 | 0.020 |
| Growth in NOA | 0.584 | 0.165 | 0.074 | 0.051 | 0.051 | 0.006 |
| Core Sales PM | 0.828 | 0.725 | 0.664 | 0.628 | 0.605 | 0.534 |
| Other Core Items/NOA | 0.663 | 0.533 | 0.451 | 0.406 | 0.367 | 0.195 |
| Unusual Items/NOA | 0.376 | 0.284 | 0.223 | 0.212 | 0.189 | 0.020 |
| ATO | 0.947 | 0.894 | 0.857 | 0.830 | 0.808 | 0.602 |
| Growth in Sales | 0.309 | 0.115 | 0.103 | 0.106 | 0.115 | 0.007 |
| ΔCore Sales PM | −0.039 | −0.083 | −0.059 | −0.043 | −0.012 | 0.001 |
| ΔATO | 0.166 | −0.100 | −0.082 | −0.039 | −0.009 | 0.003 |

Reading: current residual earnings forecast residual earnings out to five years; the decay in correlations and the variance ratios show convergence to central values, so **extremes become typical**. Book-value growth fades fastest (growth in NOA rank correlation 0.58 at t=1, 0.05 at t=5, variance ratio 0.006), so high growth in NOA cannot be extrapolated. Core profit margins are the most persistent of the operating drivers (0.83 at t=1, 0.60 at t=5, variance 0.53); asset turnover is the most persistent overall (0.95 → 0.81). Unusual items fade quickly, consistent with the definition. Changes in drivers (ΔCore Sales PM, ΔATO) show almost no persistence; the portfolio with the largest negative change in Core Sales PM in year 0 shows the largest positive changes in later years, consistent with "big bath" write-offs, and changes in asset turnover mean-revert rapidly (a high turnover in one year implies low turnover the next).

## Continuing-value implications

- Permanent levels are **not zero** for many portfolios ⇒ CV2/CV02 (or CV3/CV03) are the typical case, not CV1/CV01; the long-run growth in residual earnings is **slightly positive**, so CV3 may improve on CV2.
- Long-run positive residual earnings are explained by persistent nonzero NPV investing, or by conservative accounting (expensing intangibles), so the average firm is expected to have long-run $RE$/$ReOI$ positive and $ROCE$/$RNOA$ above its cost of capital. That implies the assumed **6% equity risk premium** (cost of equity = 1-year treasury + 6%) is probably too high; Claus & Thomas (2001), O'Hanlon & Steele (1998), Gebhardt/Lee/Swaminathan (2000) impute lower premiums.
- A temporary spike in leverage produces temporary residual earnings even at a "normal" $RNOA$; mean reversion in $FLEV$ forecasts that such residual earnings become typical. Forecasting $ReOI$ avoids forecasting leverage-driven changes in the discount rate.
- The majority of firms show **negative** $RE$/$ReOI$ by year 5 — partly an artifact of the cost-of-capital assumption.
- Forecasting is easier for the drivers than for residual earnings: leverage, asset turnover, and core margins are stable; growth rates are not.

## Survivorship (Table 4)

Five-year survivorship by residual-earnings portfolio, Panel A: portfolio 10 (high RE) 97.84% (year 1), 94.66, 91.74, 89.30, **85.45%**; portfolio 1 (low RE) 94.13, 89.90, 84.83, 80.58, **75.94%**. Panel B (share of terminations due to merger/acquisition): portfolio 10 → 78.00, 87.33, 88.71, 89.93, 88.73%; portfolio 1 → 66.57, 71.23, 74.20, 75.78, 72.73%. High-residual-earnings firms survive best and are mostly acquired; low-residual-earnings firms disappear in larger numbers, so ex post medians for the bottom portfolio are biased upward.

## Time-series patterns (Figures 3–6 medians)

- **FLEV** is fairly constant for all portfolios except the highest; the highest-leverage portfolio fades down, the lowest fades up. Median Debt/Equity rose more than median FLEV over the sample, driven by growth in operating liabilities; median $OLLEV$ shows a slight upward trend (recognition of employee benefit liabilities in the late 1980s/1990s).
- **ROCE** and **RNOA** fade toward common levels; growth in $CSE$ and growth in $NOA$ fade fastest, which is what drives residual earnings back to central values (mean reversion in profitability documented in Freeman, Ohlson & Penman 1982; Penman 1991; Fama & French 2000).
- **Core Sales PM** differences perpetuate; **ATO** stays fairly constant except the highest portfolio; **unusual items** fade; **Other Core Items** fade slowly; **sales growth** shows almost no persistence.
- **ROTA consistently understates RNOA** and the two move together over time; **Core RNOA** is below RNOA except in some 1990s years (restructurings and charges produce large negative unusual charges); the sample shifts from turnover-driven in the early years to margin-driven in the last 15 years.
- The pattern is robust across base periods, and the results are not sensitive to using averages of beginning/ending balance-sheet values for income measurement (the ratio literature's convention, Penman 1988, 1991; Sloan 1996; Lakonishok, Shleifer & Vishny 1994).

## Related

- [[concepts/residual-earnings-equity-valuation]] — the model whose CV rule these benchmarks settle
- [[concepts/ratio-hierarchy-for-profitability-and-growth]] — the drivers being tracked
- [[concepts/operating-and-financial-leverage-spreading]] — the leverage and spread terms that fade
- [[concepts/fama-macbeth-two-stage-cross-sectional-regression]] — the cross-sectional method this evidence informs
- [[concepts/statistical-investigation-lifecycle]] — the out-of-sample discipline this study applies
- [[concepts/predictive-to-prescriptive-analytics]] — the forecasting stance these priors support
- [[references/nissim2001-ratio-analysis-equity-valuation]] — the source paper for the fade rates and survivorship tables

## Sources

- [[_papers/nissim2001ratio/nissim2001ratio-extracted.md]]
- [[_papers/nissim2001ratio/nissim2001ratio.md]]
