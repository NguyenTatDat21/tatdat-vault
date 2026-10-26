---
title: >-
  Ratio Analysis and Equity Valuation: From Research to Practice
category: references
aliases: [Nissim & Penman 2001, Review of Accounting Studies 2001, ratio documentation]
tags: [accounting, equity-valuation, ratio-analysis, financial-statement-analysis, residual-earnings, profitability, growth, mean-reversion, compustat, forecasting]
relationships:
  - target: "[[concepts/residual-earnings-equity-valuation]]"
    type: uses
  - target: "[[concepts/ratio-hierarchy-for-profitability-and-growth]]"
    type: uses
  - target: "[[concepts/operating-and-financial-leverage-spreading]]"
    type: uses
  - target: "[[concepts/ratio-mean-reversion-and-continuing-value-benchmarks]]"
    type: uses
  - target: "[[concepts/predictive-to-prescriptive-analytics]]"
    type: related_to
  - target: "[[concepts/cash-based-operating-profitability]]"
    type: related_to
  - target: "[[references/pincus2007-accrual-anomaly-international-evidence]]"
    type: related_to
  - target: "[[references/brown2007-negative-book-equity-stocks]]"
    type: related_to
  - target: "[[references/kim2020-profitability-asean-stocks]]"
    type: related_to
  - target: "[[concepts/fama-macbeth-two-stage-cross-sectional-regression]]"
    type: related_to
sources:
  - _papers/nissim2001ratio/nissim2001ratio-extracted.md
  - _papers/nissim2001ratio/nissim2001ratio.md
  - _papers/nissim2001ratio/images/page_20_table_2.jpg
  - _papers/nissim2001ratio/images/page_20_table_5.jpg
  - _papers/nissim2001ratio/images/page_23_table_2.jpg
  - _papers/nissim2001ratio/images/page_24_table_3.jpg
  - _papers/nissim2001ratio/images/page_25_chart_2.jpg
  - _papers/nissim2001ratio/images/page_25_chart_3.jpg
  - _papers/nissim2001ratio/images/page_25_chart_4.jpg
  - _papers/nissim2001ratio/images/page_26_chart_2.jpg
  - _papers/nissim2001ratio/images/page_26_chart_3.jpg
  - _papers/nissim2001ratio/images/page_26_chart_4.jpg
  - _papers/nissim2001ratio/images/page_28_chart_2.jpg
  - _papers/nissim2001ratio/images/page_28_chart_3.jpg
  - _papers/nissim2001ratio/images/page_28_chart_4.jpg
  - _papers/nissim2001ratio/images/page_29_chart_2.jpg
  - _papers/nissim2001ratio/images/page_31_chart_2.jpg
  - _papers/nissim2001ratio/images/page_31_chart_3.jpg
  - _papers/nissim2001ratio/images/page_31_chart_4.jpg
  - _papers/nissim2001ratio/images/page_32_chart_2.jpg
  - _papers/nissim2001ratio/images/page_32_chart_3.jpg
  - _papers/nissim2001ratio/images/page_32_chart_4.jpg
  - _papers/nissim2001ratio/images/page_33_chart_2.jpg
  - _papers/nissim2001ratio/images/page_34_chart_2.jpg
  - _papers/nissim2001ratio/images/page_34_chart_3.jpg
  - _papers/nissim2001ratio/images/page_34_chart_4.jpg
  - _papers/nissim2001ratio/images/page_35_chart_2.jpg
  - _papers/nissim2001ratio/images/page_36_chart_2.jpg
  - _papers/nissim2001ratio/images/page_36_chart_3.jpg
  - _papers/nissim2001ratio/images/page_36_chart_4.jpg
  - _papers/nissim2001ratio/images/page_37_table_5.jpg
  - _papers/nissim2001ratio/images/page_38_table_7.jpg
  - _papers/nissim2001ratio/images/page_38_table_9.jpg
summary: >-
  Nissim & Penman (Review of Accounting Studies 2001): ratio analysis rebuilt from accounting-based valuation, then documented 1963–1999 medians, correlations and fade rates.
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-26T05:12:09Z
tier: supporting
created: 2026-10-26T05:12:09Z
updated: 2026-10-26T05:12:09Z
---

# Ratio Analysis and Equity Valuation: From Research to Practice

> [!tldr] **Doron Nissim & Stephen H. Penman, Review of Accounting Studies (2001), DOI 10.1023/A:1011338221623.** Traditional financial statement analysis is ad hoc; this paper rebuilds it on **[[concepts/residual-earnings-equity-valuation|accounting-based valuation]]** research and then **documents** what the ratios look like. Standard profitability analysis is extended, growth analysis added as a complement, the operating activities are separated from financing, and the perspective is **forecasting payoffs to equity**. Ratios are the building blocks of the payoff forecast, ordered in a hierarchy: lower ratios are finer information about higher ones.

![[../_papers/nissim2001ratio/images/page_20_table_2.jpg]]
![[../_papers/nissim2001ratio/images/page_20_table_5.jpg]]

*Table 1. Panel A: Drivers of ROCE. Panel B: Drivers of Growth in Residual Earnings. Panel B numbers for Core NBC, UFE/NFO, Core Spread based on 1994–1999 only.*

## Problem & motivation

Graham, Dodd & Cottle (1962) describe conventional financial statement analysis as "essentially ad hoc": ratios picked by convention, not derived from anything, with no documentation of typical values. The paper's answer is to derive the ratios from the theory of how equity value is calculated. Ohlson (1995) shows current book values and residual income are value-relevant; comprehensive income (FASB Statement 130, plus 115, 133) makes the clean-surplus calculation operational. The paper has two parts: **identifying** the ratios, then **documenting** typical values 1963–1999. The documented values are priors for forecasting, part of contextual analysis, inputs to econometric forecasting, and a guide for research on what to forecast.

## The valuation chain

Residual earnings valuation:

$$V_0^E=CSE_0+\sum_{t=1}^{\infty}\rho_E^{-t}\big[CNI_t-(\rho_E-1)\,CSE_{t-1}\big],\qquad RE_t=CNI_t-(\rho_E-1)\,CSE_{t-1}$$

and, finite horizon with continuing value $CV_T=\hat V_T^E-CSE_T$: $CV1=0$, $CV2=RE_{T+1}/(\rho_E-1)$, $CV3=RE_{T+1}/(\rho_E-g)$. Drivers:

$$ROCE=\frac{CNI}{CSE_{t-1}}=RNOA+FLEV\cdot SPREAD=Sales\ PM\cdot ATO+\frac{Other\ Items}{NOA}+FLEV\cdot SPREAD$$

$$RNOA=ROOA+OLLEV\cdot OLSPREAD,\qquad CSE=Sales\cdot\frac{1}{ATO}\cdot\frac{1}{1+FLEV}$$

[[concepts/ratio-hierarchy-for-profitability-and-growth|Seven drivers of profitability]] (**core sales PM, ATO, other core items, financial leverage, net borrowing cost, operating liability leverage, minority-share ratio**), three of book-value growth (**sales, asset turnover, financial leverage**). The unlevered reduction $ReOI_t=OI_t-(\rho_W-1)NOA_{t-1}$ drops the financial drivers when financial items are at fair value. Growth in operating residual earnings is driven by $RNOA$ and growth in net operating assets; cash-flow identities (equations 12–15) tie the same drivers to free cash flow and dividends, so the analysis applies to discounted cash flow and dividend-discount valuation as well.

## Ratio documentation: 1963–1999

Sample: U.S. GAAP firms on the combined CRSP/COMPUSTAT industrial file (NYSE + AMEX), 37 years, non-surviving firms included; balance-sheet values as averages of beginning and end; all income after tax; cost of equity = 1-year treasury + 6% risk premium; medians as representative values, means/SDs excluding top and bottom 1%.

**Panel A (drivers of ROCE; Obs / median / SD / 95% / 5%):** ROCE 64,060 / **12.2%** / 16.2% / 31.0% / −21.5%; ROTCE 64,076 / 12.2%; MSR 55,750 / 1.00; RNOA 64,522 / **10.0%** / 12.8%; ROTA 65,098 / 6.8%; RNOA−ROTA 64,522 / 2.9%; OLLEV 64,545 / **0.35**; OLSPREAD 65,080 / **3.4%**; FLEV 64,098 / **0.40** (Debt/Equity 64,073 / 1.19); NBC 65,099 / 5.2%; SPREAD 64,515 / **3.9%** (SD 20.3%); PM 64,957 / 5.5%; ATO 64,545 / 1.94.

**Panel B (growth):** Core Sales PM 64,905 / 5.1%; Sales PM 64,943 / 5.4%; Other It./NOA 64,531 / 0.0%; UOI/NOA 64,484 / 0.3%; Core RNOA 64,470 / 9.4%; Core NBC (1994–99) 12,622 / 5.2%; UFE/NFO (1994–99) 12,622 / 0.0%; Core SPREAD (1994–99) 12,448 / 3.8%; Growth in RE 31,217 / **−11.8%** (SD 396.1%); Growth in ReOI 24,688 / −13.5% (SD 422.9%); Growth in CSE 59,844 / 9.0%; Growth in NOA 60,211 / 8.9%; FCF/NOA 64,522 / 2.1% (negative in ~40% of firm-years).

![[../_papers/nissim2001ratio/images/page_23_table_2.jpg]]
![[../_papers/nissim2001ratio/images/page_24_table_3.jpg]]

*Table 2. Correlations among drivers of ROCE.*

Spearman cross-sectional correlations (from Table 2): $RNOA$–$ROTA$ 0.94, $RNOA$–$OLSPREAD$ 0.93, $RNOA$–$Core\ RNOA$ 0.91, $RNOA$–$FLEV$ −0.42, $FLEV$–$SPREAD$ −0.38, $FLEV$–$OLLEV$ −0.26, $OLLEV$–$ATO$ 0.60, $OLLEV$–$PM$ −0.21, $OLLEV$–$OLSPREAD$ 0.15, $OLLEV$–$Growth\,NOA$ −0.10, $SPREAD$–$Core\ SPREAD$ 0.92, $NBC$–$Core\ NBC$ 0.98, $PM$–$Sales\ PM$ 0.99, $Sales\ PM$–$Core\ Sales\ PM$ 0.91, $Core\ Sales\ PM$–$ATO$ −0.40, $Core\ NBC$–$RNOA$ −0.08, $Core\ NBC$–$FLEV$ 0.28, $ROCE$–$RNOA$ 0.89, $ROCE$–$OLSPREAD$ 0.86, $ROCE$–$Core\ SPREAD$ 0.66, $ROCE$–$Growth\,RE$ 0.67, $ROCE$–$Growth\,ReOI$ 0.62, $ROCE$–$Growth\,CSE$ 0.55, $ROCE$–$Growth\,NOA$ 0.27, $ROCE$–$FCF/NOA$ 0.16, $MSR$–$ROCE$ 0.08.

![[../_papers/nissim2001ratio/images/page_25_chart_2.jpg]]
![[../_papers/nissim2001ratio/images/page_25_chart_3.jpg]]
![[../_papers/nissim2001ratio/images/page_25_chart_4.jpg]]

*Figure 1. (a) Median ROCE, one-year treasury rate and the assumed cost of equity capital. (b) Median ROCE, RNOA and NBC over time. (c) Median FLEV, OLLEV and debt/equity over time. (d) Median ROTA and RNOA over time. (e) Median RNOA and its components over time. (f ) Median core RNOA and its components over time.*

![[../_papers/nissim2001ratio/images/page_26_chart_2.jpg]]
![[../_papers/nissim2001ratio/images/page_26_chart_3.jpg]]
![[../_papers/nissim2001ratio/images/page_26_chart_4.jpg]]

*Figure 1. (Continued )*

Median $ROCE$ exceeds the risk-free rate in every year of the sample except 1982, and falls below the assumed cost of equity in a majority of years — which the authors read as evidence that the 6% premium is too high (Claus & Thomas 2001; O'Hanlon & Steele 1998; Gebhardt/Lee/Swaminathan 2000). $ROTA$ consistently understates $RNOA$; $Core\ RNOA$ is below $RNOA$ except in some 1990s years; the profitability drivers shift from turnover-driven in the early sample to margin-driven in the last 15 years; median Debt/Equity rose more than median $FLEV$, induced by growth in operating liabilities.

![[../_papers/nissim2001ratio/images/page_28_chart_2.jpg]]
![[../_papers/nissim2001ratio/images/page_28_chart_3.jpg]]
![[../_papers/nissim2001ratio/images/page_28_chart_4.jpg]]
![[../_papers/nissim2001ratio/images/page_29_chart_2.jpg]]

*Figure 2. (a) Median FLEV on median SPREAD. (b) Median OLLEV on median OLSPREAD. (c) Median core sales PM on median ATO. (d) Median RNOA on median growth in NOA.*

The $FLEV$–$SPREAD$ relation is negative (rank correlation −0.38; $FLEV$–$RNOA$ −0.42); $OLLEV$–$OLSPREAD$ is +0.15 and $OLLEV$–$RNOA$ +0.28 (operating liability leverage works favourably on average); iso-$RNOA$ lines in the $Core\ Sales\ PM$–$ATO$ plane are convex and downward sloping with correlation −0.40 (replicating Selling & Stickney 1989 with a refined profit margin and an NOA-based turnover); $RNOA$ and growth in $NOA$ are positively related (+0.24).

![[../_papers/nissim2001ratio/images/page_31_chart_2.jpg]]
![[../_papers/nissim2001ratio/images/page_31_chart_3.jpg]]
![[../_papers/nissim2001ratio/images/page_31_chart_4.jpg]]

*Figure 3. (a) Evolution of RE over time. (b) Evolution of ReOI over time. (c) Evolution of FLEV over time.*

![[../_papers/nissim2001ratio/images/page_32_chart_2.jpg]]
![[../_papers/nissim2001ratio/images/page_32_chart_3.jpg]]
![[../_papers/nissim2001ratio/images/page_32_chart_4.jpg]]

*Figure 4. (a) Evolution of ROCE over time. (b) Evolution of RNOA over time. (c) Evolution of growth in CSE over time. (d) Evolution of growth in NOA over time.*

![[../_papers/nissim2001ratio/images/page_33_chart_2.jpg]]

*Figure 4. (Continued )*

![[../_papers/nissim2001ratio/images/page_34_chart_2.jpg]]
![[../_papers/nissim2001ratio/images/page_34_chart_3.jpg]]
![[../_papers/nissim2001ratio/images/page_34_chart_4.jpg]]

*Figure 5. (a) Evolution of core sales PM over time. (b) Evolution of other core items/NOA over time. (c) Evolution of UOI/NOA over time. (d) Evolution of ATO over time.*

![[../_papers/nissim2001ratio/images/page_35_chart_2.jpg]]

*Figure 5. (Continued )*

![[../_papers/nissim2001ratio/images/page_36_chart_2.jpg]]
![[../_papers/nissim2001ratio/images/page_36_chart_3.jpg]]
![[../_papers/nissim2001ratio/images/page_36_chart_4.jpg]]

*Figure 6. (a) Evolution of sales growth rate PM over time. (b) Evolution of change in core sales profit margin over time. (c) Evolution of change in ATO over time.*

![[../_papers/nissim2001ratio/images/page_37_table_5.jpg]]

*Table 3. Summary measures for the evolution of ratios.*

![[../_papers/nissim2001ratio/images/page_38_table_7.jpg]]
![[../_papers/nissim2001ratio/images/page_38_table_9.jpg]]

*Table 4. Percentage survivorship rates for residual earnings portfolios.*

Fade rates: rank correlation of a ratio with its $t$-lagged value, and the portfolio variance ratio $var_t/var_0$ (Table 3; see [[concepts/ratio-mean-reversion-and-continuing-value-benchmarks]] for the full table). Survivorship (Table 4): high-residual-earnings portfolios retain 97.84% → 85.45% over five years, the lowest portfolio 94.13% → 75.94%, and 66–97% of terminations are mergers/acquisitions.

## Contributions and limitations

Contributions as stated: comprehensive income in ratio analysis; the forecasting perspective (ratios as drivers of the residual earnings payoff); predictive ability of ratios as a hierarchy; parsimony in forecasting; explicit treatment of growth; an extended set of profitability drivers; explicit minority interest; a clean operating/financing separation (and a new leverage measure $FLEV$); recognition of operating liability leverage; and the documentation of typical values and typical time patterns. Limitations: single-country U.S. GAAP sample (financial institutions excluded — for them financial items are operating), COMPUSTAT aggregation limits core/unusual splits, the cost-of-capital premium is conjectural (medians of growth in RE/ReOI are negative, partly an artifact), coefficients are unstable so the analysis stays contextual, and ex post medians carry survivorship bias.

## Related

- [[concepts/residual-earnings-equity-valuation]] — the valuation model the paper builds on
- [[concepts/ratio-hierarchy-for-profitability-and-growth]] — the driver hierarchy and benchmark values
- [[concepts/operating-and-financial-leverage-spreading]] — the FLEV/SPREAD and OLLEV/OLSPREAD decomposition
- [[concepts/ratio-mean-reversion-and-continuing-value-benchmarks]] — the fade-rate and continuing-value evidence
- [[concepts/predictive-to-prescriptive-analytics]] — the forecasting-to-valuation stance
- [[concepts/cash-based-operating-profitability]] — the cash-based complement to this accrual-based system
- [[references/pincus2007-accrual-anomaly-international-evidence]] — cross-market accruals evidence in the same lineage
- [[references/brown2007-negative-book-equity-stocks]] — profitability/leverage classes in the cross section
- [[references/kim2020-profitability-asean-stocks]] — profitability ratios applied internationally
- [[concepts/fama-macbeth-two-stage-cross-sectional-regression]] — the regression machinery the drivers were tested with

## Sources

- [[_papers/nissim2001ratio/nissim2001ratio-extracted.md]]
- [[_papers/nissim2001ratio/nissim2001ratio.md]]
- [[_papers/nissim2001ratio/images/page_20_table_2.jpg]]
- [[_papers/nissim2001ratio/images/page_20_table_5.jpg]]
- [[_papers/nissim2001ratio/images/page_23_table_2.jpg]]
- [[_papers/nissim2001ratio/images/page_24_table_3.jpg]]
- [[_papers/nissim2001ratio/images/page_25_chart_2.jpg]]
- [[_papers/nissim2001ratio/images/page_25_chart_3.jpg]]
- [[_papers/nissim2001ratio/images/page_25_chart_4.jpg]]
- [[_papers/nissim2001ratio/images/page_26_chart_2.jpg]]
- [[_papers/nissim2001ratio/images/page_26_chart_3.jpg]]
- [[_papers/nissim2001ratio/images/page_26_chart_4.jpg]]
- [[_papers/nissim2001ratio/images/page_28_chart_2.jpg]]
- [[_papers/nissim2001ratio/images/page_28_chart_3.jpg]]
- [[_papers/nissim2001ratio/images/page_28_chart_4.jpg]]
- [[_papers/nissim2001ratio/images/page_29_chart_2.jpg]]
- [[_papers/nissim2001ratio/images/page_31_chart_2.jpg]]
- [[_papers/nissim2001ratio/images/page_31_chart_3.jpg]]
- [[_papers/nissim2001ratio/images/page_31_chart_4.jpg]]
- [[_papers/nissim2001ratio/images/page_32_chart_2.jpg]]
- [[_papers/nissim2001ratio/images/page_32_chart_3.jpg]]
- [[_papers/nissim2001ratio/images/page_32_chart_4.jpg]]
- [[_papers/nissim2001ratio/images/page_33_chart_2.jpg]]
- [[_papers/nissim2001ratio/images/page_34_chart_2.jpg]]
- [[_papers/nissim2001ratio/images/page_34_chart_3.jpg]]
- [[_papers/nissim2001ratio/images/page_34_chart_4.jpg]]
- [[_papers/nissim2001ratio/images/page_35_chart_2.jpg]]
- [[_papers/nissim2001ratio/images/page_36_chart_2.jpg]]
- [[_papers/nissim2001ratio/images/page_36_chart_3.jpg]]
- [[_papers/nissim2001ratio/images/page_36_chart_4.jpg]]
- [[_papers/nissim2001ratio/images/page_37_table_5.jpg]]
- [[_papers/nissim2001ratio/images/page_38_table_7.jpg]]
- [[_papers/nissim2001ratio/images/page_38_table_9.jpg]]
