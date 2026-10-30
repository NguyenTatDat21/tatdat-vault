---
title: >-
  Hierarchical Ratio System for Profitability and Growth
category: concepts
aliases: [ratio hierarchy, operating-financial split, core income, drivers of ROCE, drivers of growth]
tags: [ratio-analysis, profitability, growth, drivers, core-income, unusual-items, forecasting, parsimony, clean-surplus, hierarchy]
relationships:
  - target: "[[concepts/residual-earnings-equity-valuation]]"
    type: derived_from
  - target: "[[concepts/operating-and-financial-leverage-spreading]]"
    type: related_to
  - target: "[[concepts/ratio-mean-reversion-and-continuing-value-benchmarks]]"
    type: related_to
  - target: "[[concepts/predictive-to-prescriptive-analytics]]"
    type: related_to
  - target: "[[concepts/cash-based-operating-profitability]]"
    type: extends
  - target: "[[concepts/negative-book-equity-style-classification]]"
    type: related_to
  - target: "[[concepts/ordering-information-portfolio-selection]]"
    type: related_to
  - target: "[[concepts/fama-macbeth-two-stage-cross-sectional-regression]]"
    type: uses
  - target: "[[references/nissim2001-ratio-analysis-equity-valuation]]"
    type: derived_from
  - target: "[[concepts/gross-profitability-premium]]"
    type: related_to
  - target: "[[references/kim2020-profitability-asean-stocks]]"
    type: related_to
  - target: "[[references/novy-marx2013-other-side-of-value]]"
    type: related_to
sources:
  - _papers/nissim2001ratio/nissim2001ratio-extracted.md
  - _papers/nissim2001ratio/nissim2001ratio.md
summary: >-
  ROCE's seven drivers (Sales PM, ATO, Other Items, FLEV, NBC, OLLEV, MSR) and growth's three (Sales, ATO, FLEV) form a hierarchy: lower ratios are finer info about higher ones.
provenance:
  extracted: 1.00
  inferred: 0.00
  ambiguous: 0.00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-26T05:12:09Z
tier: core
created: 2026-10-26T05:12:09Z
updated: 2026-10-30T14:38:55Z
---

# Hierarchical Ratio System for Profitability and Growth

> [!tldr] Ratio analysis rebuilt as the **drivers of [[concepts/residual-earnings-equity-valuation|forecasted residual earnings]]**. Everything is split into **operating** and **financial** activity; each driver is split into **core** (expected to repeat) and **unusual** items; and the ratios form a hierarchy in which lower ratios are finer information about higher ones — so forecasting a high ratio means forecasting the lower ones.

## The accounting identities

All income measures are after tax, and the two clean-surplus relations drive the system:

$$CNI_t=OI_t-NFE_t,\qquad CSE_t=NOA_t-NFO_t\ (-\ MI_t\ \text{with minority interest})$$

$$NOA=OA-OL,\qquad NFO=FO-FA,\qquad Total\ Assets=OA+FA,\qquad Total\ Liab.+Pref.=OL+FO$$

$OI$ = operating income, $NFE$ = net financial expense, $OA$ = operating assets, $FA$ = financial assets, $OL$ = operating liabilities, $FO$ = financial obligations (debt + preferred stock), $CNI$ = comprehensive net income available to common. **Preferred dividends are financial expense and preferred stock is a financial obligation.** Comprehensive income (FASB Statement 130, plus 115 and 133) is required because income from transactions with owners (treasury stock gains, LIFO equity adjustments, revaluation, translation adjustments, minimum pension liability) must enter value calculations. Financial assets are excluded from operating assets, so asset turnover excludes them; operating liabilities are excluded, so turnover is overstated when they are large.

## The profitability hierarchy

$$ROCE=\frac{CNI}{CSE_{t-1}}=RNOA+FLEV\cdot SPREAD=PM\cdot ATO+FLEV\cdot SPREAD$$
$$ROCE=Sales\ PM\cdot ATO+\frac{Other\ Items}{NOA}+FLEV\cdot SPREAD$$

with $RNOA=OI/NOA_{t-1}$, $NBC=NFE/NFO_{t-1}$, $SPREAD=RNOA-NBC$, $FLEV=NFO/CSE$, $PM=OI/Sales$, $ATO=Sales/NOA$, $Sales\ PM=(OI\ \text{from Sales})/Sales$. The operating side decomposes further:

$$RNOA=ROOA+OLLEV\cdot OLSPREAD,\qquad ROOA=\frac{OI+io}{OA},\quad OLLEV=\frac{OL}{NOA},\quad OLSPREAD=ROOA-\frac{io}{OL}$$

with $io$ = **implicit interest** on operating liabilities (estimated with the short-term borrowing rate). Minority interest: $ROTCE=(CNI+MI\ \text{share})/(CSE+MI)$, $ROCE=ROTCE\cdot MSR$, $MSR=[CNI/(CNI+MI\ \text{share})]/[CSE/(CSE+MI)]$. Traditional return on total assets (equation 17, comparable with the literature):

$$ROTA=\frac{NI+Interest\ Expense\cdot(1-t)+MI\ \text{share}}{Total\ Assets}$$

**Seven drivers of $ROCE$**: core Sales PM, ATO, Other Items/NOA, FLEV, NBC, OLLEV, MSR. **Three drivers of growth in book value** (equation 8, $CSE=Sales\cdot(1/ATO)\cdot(1/(1+FLEV))$): Sales, ATO, FLEV. Under the unlevered reduction the drivers collapse to core Sales PM, ATO, Other Items/NOA, OLLEV plus Sales and ATO.

## Core vs unusual items

$$RNOA=Core\ RNOA+\frac{UOI}{NOA},\qquad NBC=Core\ NBC+\frac{UFE}{NFO}$$

$$ROCE=Core\ Sales\ PM\cdot ATO+\frac{Core\ Other\ Items}{NOA}+\frac{UOI}{NOA}+FLEV\Big(Core\ SPREAD+\frac{UOI}{NOA}-\frac{UFE}{NFO}\Big)$$

"Unusual" = not expected to repeat — currency gains, pension non-service income, revaluation, restructuring, goodwill amortization — the definition of "core" is the **forecast**, not accounting rarity. The hierarchy is parsimony: forecasting a higher ratio (residual earnings) reduces to forecasting the drivers.

## Documented benchmarks (U.S. GAAP, NYSE + AMEX, 1963–1999, 37 years)

Medians (means and SDs exclude the top and bottom 1%; ratios with nonpositive denominators excluded, and Core NBC / UFE/NFO / Core SPREAD measured only 1994–1999):

| Ratio | Obs | Mean | SD | 95% | 75% | **Median** | 25% | 10% | 5% |
|---|---|---|---|---|---|---|---|---|---|
| ROCE | 64,060 | 10.2% | 16.2% | 31.0% | 17.6% | **12.2%** | 6.3% | −4.8% | −21.5% |
| ROTCE | 64,076 | 10.3% | 16.0% | 30.9% | 17.6% | **12.2%** | 6.3% | −4.6% | −21.0% |
| MSR | 55,750 | 1.00 | 0.02 | 1.02 | 1.00 | **1.00** | 1.00 | 1.00 | 0.98 |
| RNOA | 64,522 | 10.8% | 12.8% | 33.7% | 15.6% | **10.0%** | 6.0% | −0.5% | −9.9% |
| ROTA | 65,098 | 6.6% | 6.4% | 16.7% | 9.9% | **6.8%** | 4.3% | 0.0% | −5.9% |
| RNOA − ROTA | 64,522 | 4.1% | 7.1% | 17.9% | 5.6% | **2.9%** | 1.2% | −0.6% | −3.9% |
| ROOA-related OLLEV | 64,545 | 0.44 | 0.35 | 1.16 | 0.52 | **0.35** | 0.24 | 0.16 | 0.12 |
| OLSPREAD | 65,080 | 3.2% | 8.4% | 17.4% | 6.9% | **3.4%** | 0.1% | −5.2% | −11.9% |
| FLEV | 64,098 | 0.60 | 0.87 | 2.32 | 0.93 | **0.40** | 0.05 | −0.23 | −0.42 |
| Debt/Equity | 64,073 | 1.56 | 1.39 | 4.38 | 1.99 | **1.19** | 0.69 | 0.39 | 0.27 |
| NBC | 65,099 | 5.3% | 8.5% | 17.3% | 7.3% | **5.2%** | 3.2% | −0.7% | −6.2% |
| SPREAD | 64,515 | 5.3% | 20.3% | 40.9% | 10.3% | **3.9%** | −0.5% | −10.4% | −24.4% |
| PM | 64,957 | 6.2% | 8.6% | 21.3% | 9.5% | **5.5%** | 2.8% | −0.3% | −6.4% |
| ATO | 64,545 | 2.33 | 1.83 | 6.32 | 2.86 | **1.94** | 1.18 | 0.55 | 0.38 |
| Sales PM | 64,943 | 6.0% | 8.5% | 20.9% | 9.3% | **5.4%** | 2.7% | −0.4% | −6.5% |
| Core Sales PM | 64,905 | 5.7% | 7.0% | 18.5% | 8.6% | **5.1%** | 2.7% | 0.3% | −4.0% |
| Other Items/NOA | 64,531 | 0.2% | 0.6% | 1.6% | 0.0% | **0.0%** | 0.0% | 0.0% | 0.0% |
| UOI/NOA | 64,484 | 0.3% | 4.0% | 6.5% | 1.2% | **0.3%** | −0.1% | −2.6% | −6.6% |
| Core RNOA | 64,470 | 10.5% | 10.8% | 30.2% | 14.7% | **9.4%** | 5.7% | 0.9% | −6.0% |
| Core NBC (1994–99) | 12,622 | 5.2% | 7.9% | 15.6% | 7.0% | **5.2%** | 3.5% | −0.2% | −4.7% |
| Core SPREAD (1994–99) | 12,448 | 5.3% | 19.6% | 40.8% | 10.4% | **3.8%** | −1.0% | −11.0% | −26.1% |
| Growth in RE | 31,217 | −56.8% | 396.1% | 397.7% | 48.9% | **−11.8%** | −103.9% | −322.0% | −696.4% |
| Growth in ReOI | 24,688 | −66.4% | 422.9% | 411.8% | 47.8% | **−13.5%** | −111.7% | −351.2% | −743.9% |
| Growth in CSE | 59,844 | 11.3% | 19.6% | 50.5% | 17.3% | **9.0%** | 2.7% | −6.9% | −18.0% |
| Growth in NOA | 60,211 | 12.9% | 22.2% | 59.5% | 20.6% | **8.9%** | 0.8% | −8.6% | −17.0% |
| FCF/NOA | 64,522 | −0.1% | 23.7% | 36.2% | 11.1% | **2.1%** | −8.6% | −27.2% | −47.3% |

Findings: median $ROCE$ 12.2% ≈ the historical average equity return of about 12.5% (Ibbotson & Sinquefield 1983), which may be too high as an ex post measure of required return (Brown, Goetzmann & Ross 1995); $RNOA$ exceeds $ROTA$ at mean and median, with $|RNOA-ROTA|>3\%$ in almost half of firm-years; median $ROCE$ 12.2% > median $RNOA$ 10.0% (financial leverage amplifies); median $FLEV$ 0.40 vs Debt/Equity 1.19, and financial leverage is negative for about 20% of firms; median $OLLEV$ 0.35 with median $OLSPREAD$ 3.4% ⇒ operating liability leverage is typically favorable; median $NBC$ 5.2% after tax; $SPREAD$ negative in about 30% of firm-years; median $FCF/NOA$ 2.1% with free cash flow negative in about 40% of firm-years; median growth in $CSE$ 9.0% and in $NOA$ 8.9%.

## Cross-sectional correlations (Table 2, Spearman)

$RNOA$–$ROTA$ 0.94, $RNOA$–$OLSPREAD$ 0.93, $RNOA$–$Core\ RNOA$ 0.91, $RNOA$–$FLEV$ −0.42, $FLEV$–$SPREAD$ −0.38, $FLEV$–$OLLEV$ −0.26, $OLLEV$–$ATO$ 0.60, $OLLEV$–$PM$ −0.21, $OLLEV$–$OLSPREAD$ 0.15, $OLLEV$–$Growth\,NOA$ −0.10, $SPREAD$–$Core\ SPREAD$ 0.92, $NBC$–$Core\ NBC$ 0.98, $PM$–$Sales\ PM$ 0.99, $Sales\ PM$–$Core\ Sales\ PM$ 0.91, $Core\ Sales\ PM$–$ATO$ −0.40, $Core\ NBC$–$RNOA$ −0.08, $Core\ NBC$–$FLEV$ 0.28, $ROCE$–$RNOA$ 0.89, $ROCE$–$OLSPREAD$ 0.86, $ROCE$–$Core\ SPREAD$ 0.66, $ROCE$–$Growth\,RE$ 0.67, $ROCE$–$Growth\,ReOI$ 0.62, $ROCE$–$Growth\,CSE$ 0.55, $ROCE$–$Growth\,NOA$ 0.27, $ROCE$–$FCF/NOA$ 0.16, $MSR$–$ROCE$ 0.08 (near-decorative).

## Forecasting discipline

Multivariate regressions of future ratios on current drivers gave **large t-statistics and decent $R^2$ but failed in out-of-sample validation**; coefficients are not stable across firms and time, so ratios are **contextual** — industry, going-concern, stage-of-development, financing structure, and the firm's financial policy (dividend, investment, financing, operating liability) must be analyzed qualitatively. The relation between a current driver and its future value is **non-linear** ⇒ descriptive benchmarks (documented typical values and typical time patterns) rather than mechanical extrapolation; the same drivers determine cash flow, so the analysis applies to DCF and dividend-discount valuation as well.

## Related

- [[concepts/residual-earnings-equity-valuation]] — the valuation model the drivers feed
- [[concepts/operating-and-financial-leverage-spreading]] — the leverage/spread half of the hierarchy
- [[concepts/ratio-mean-reversion-and-continuing-value-benchmarks]] — the time-series behavior of these drivers
- [[concepts/predictive-to-prescriptive-analytics]] — the forecasting stance this system implements
- [[concepts/cash-based-operating-profitability]] — the cash-based profitability measure this hierarchy extends
- [[concepts/negative-book-equity-style-classification]] — profitability styles in the cross section
- [[concepts/ordering-information-portfolio-selection]] — using such information in portfolio construction
- [[concepts/fama-macbeth-two-stage-cross-sectional-regression]] — the regression machinery these drivers were tested with
- [[references/nissim2001-ratio-analysis-equity-valuation]] — the source paper for this hierarchy and its benchmarks

## Sources

- [[_papers/nissim2001ratio/nissim2001ratio-extracted.md]]
- [[_papers/nissim2001ratio/nissim2001ratio.md]]
