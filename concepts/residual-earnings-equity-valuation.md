---
title: >-
  Residual Earnings Valuation (Clean-Surplus Excess-Return Model)
category: concepts
aliases: [residual income, RPE model, Edwards-Bell-Ohlson, clean surplus relation]
tags: [valuation, residual-income, clean-surplus, book-value, cost-of-capital, continuing-value, forecasting, dividends, discount-rate]
relationships:
  - target: "[[concepts/ratio-hierarchy-for-profitability-and-growth]]"
    type: uses
  - target: "[[concepts/operating-and-financial-leverage-spreading]]"
    type: uses
  - target: "[[concepts/ratio-mean-reversion-and-continuing-value-benchmarks]]"
    type: related_to
  - target: "[[concepts/predictive-to-prescriptive-analytics]]"
    type: related_to
  - target: "[[concepts/cash-based-operating-profitability]]"
    type: related_to
  - target: "[[references/pincus2007-accrual-anomaly-international-evidence]]"
    type: related_to
  - target: "[[references/nissim2001-ratio-analysis-equity-valuation]]"
    type: derived_from
  - target: "[[references/almgren2004-optimal-portfolios-ordering-information]]"
    type: related_to
  - target: "[[references/sloan1996-accruals-cash-flow-stock-prices]]"
    type: related_to
sources:
  - _papers/nissim2001ratio/nissim2001ratio-extracted.md
  - _papers/nissim2001ratio/nissim2001ratio.md
summary: >-
  Equity value = book value + discounted residual earnings; RE_t = CNI_t − (ρ_E−1)CSE_{t−1} with clean surplus, three continuing-value rules, drivers = PM, ATO, leverage.
provenance:
  extracted: 0.90
  inferred: 0.10
  ambiguous: 0.00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-26T05:12:09Z
tier: core
created: 2026-10-26T05:12:09Z
updated: 2026-10-30T14:38:55Z
---

# Residual Earnings Valuation

> [!tldr] Value equity as **book value of common equity plus discounted residual earnings**. A residual earning is the excess of comprehensive income over the capital charge on the prior period's book value, and the **clean surplus relation** ties the two together so that drivers of future residual earnings are drivers of current value.

## The model

$$V_0^E=CSE_0+\sum_{t=1}^{\infty}\rho_E^{-t}\Big[CNI_t-(\rho_E-1)\,CSE_{t-1}\Big]$$

where $CSE$ = book value of common equity at time $t$, $CNI$ = comprehensive net income accruing to common shareholders, $\rho_E = 1+$ the equity cost of capital, and

$$RE_t=CNI_t-(\rho_E-1)\,CSE_{t-1}$$

is the residual earnings (abnormal, excess) of period $t$. Only the income over the **required** return on book value contributes value; the capital charge is an opportunity cost, not an accounting expense. Lineage in the source: Preinreich (1938), Edwards & Bell (1961), Kay (1976), Ohlson (1995), with the Feltham–Ohlson model (1995) as the theoretical base, and applications in Brief & Lawson (1992), Frankel & Lee (1998), Lee/Myers/Swaminathan (1999), Penman & Sougiannis (1998), Francis/Olsson/Oswald (2000), Abarbanell & Bernard (2000).

The single behavioural assumption is the dividend-valuation relation: $V_0^E=\sum_{t=1}^{\infty}\rho_E^{-t}d_t$ with $d_t$ = dividends to shareholders, and **clean surplus** $CSE_t=CSE_{t-1}+CNI_t-d_t$ (dividends include repurchases net of share issues). Combining them removes dividends and yields the model above; the model therefore prices the **unreceived dividends** implied by the book value. ^[inferred]

## Finite horizon and continuing value

$$V_0^E=CSE_0+\sum_{t=1}^{T}\rho_E^{-t}RE_t+\frac{CV_T}{\rho_E^T},\qquad CV_T=\hat V_T^E-CSE_T$$

Three continuing-value rules for the forecast horizon $T$:

- **CV1** = 0 ⇒ $V_0^E=CSE_0$ (book value as value; a no-growth scenario).
- **CV2** = $RE_{T+1}/(\rho_E-1)$ ⇒ $V_0^E=CSE_0+\sum_{t=1}^{T}\rho_E^{-t}RE_t+\frac{1}{\rho_E^{T}}\cdot\frac{RE_{T+1}}{\rho_E-1}$ (constant residual earnings from $T+1$ onward).
- **CV3** = $RE_{T+1}/(\rho_E-g)$ with growth $g$ ⇒ the same expression with the $g$-denominator; CV2 is CV3 with $g=0$.

CV1 is the conservative benchmark; the source's empirical evidence makes CV2/CV3 the typical case, since residual earnings settle to nonzero central values.

## Driving residual earnings

Expressing income through the operating/financing split,

$$RE_t=\big[ROCE_t-(\rho_E-1)\big]\cdot CSE_{t-1},\qquad ROCE_t=\frac{CNI_t}{CSE_{t-1}}$$

so valuation is driven by $ROCE$ and $CSE$. Forecasting as **scenario analysis** ($E[xy]=E[x]E[y]$ holds only if the two drivers are uncorrelated), the drivers are $ROCE$, $CSE$, and the number of shares outstanding. Substituting the leverage decomposition (see [[concepts/operating-and-financial-leverage-spreading]]) gives the drivers that are forecast directly: **core sales profit margin**, **asset turnover**, **other core items**, **financial leverage**, **net borrowing cost**, **operating liability leverage**, **minority-share ratio**. A constant $ROCE$ equal to the cost of capital ⇒ $RE_t=0$ ⇒ $V_0^E=CSE_0$.

For the operating side alone the model reduces to enterprise value: with $\rho_W$ = unlevered (weighted-average) cost of capital,

$$V_0^E=CSE_0+\sum_{t=1}^{T}\rho_W^{-t}\big[OI_t-(\rho_W-1)\,NOA_{t-1}\big]+\frac{CV_T^{NOA}}{\rho_W^T},\qquad V_0^E=V_0^{NOA}-V_0^{NFO}$$

with $ReOI_t=OI_t-(\rho_W-1)NOA_{t-1}$ and $ReNFE_t=NFE_t-(\rho_D-1)NFO_{t-1}$. This reduction is valid only when financial assets and liabilities are at **fair value** (FASB Statement 115; FASB 107 fair-value footnote), which is precisely the conservative reporting the model favours. The relation $\rho_E=\rho_W+(V_0^{NFO}/V_0^E)(\rho_W-\rho_D)$ means $\rho_W$ is a weighted combination of the equity and debt costs. ^[inferred]

## Growth and cash flow

Growth in operating residual earnings:

$$\frac{ReOI_t}{ReOI_{t-1}}-1=\frac{(RNOA_t-\rho_W+1)\,NOA_{t-1}}{(RNOA_{t-1}-\rho_W+1)\,NOA_{t-2}}-1$$

so if $RNOA$ is constant, growth in $ReOI$ = growth in net operating assets; if profit margin and asset turnover are constant, growth in $ReOI$ = sales growth. Growth in $CSE$/$NOA$ is driven by cash flow:

$$\Delta NOA_t=OI_t-(C_t-I_t),\qquad \Delta NFO_t=d_t+NFE_t-(C_t-I_t)$$

$$C_t-I_t=NOA_{t-1}\Big[RNOA_t-\Big(\frac{NOA_t}{NOA_{t-1}}-1\Big)\Big],\qquad d_t=(C_t-I_t)-NFE_t+\Delta NFO_t$$

$C_t-I_t$ is cash from operations, $d_t$ dividends. Because cash flow and residual earnings share the same drivers, the same analysis serves discounted cash flow and dividend-discount valuation; the source notes free cash flow treats growth in net operating assets as a negative driver, while residual earnings treats the same investment as positive — the main difference between the two framings.

## Why the model needs ratios

Residual earnings are a **scenario forecast**, so a valuation is a forecast of the drivers, not a one-number estimate. The hierarchical ratio system (see [[concepts/ratio-hierarchy-for-profitability-and-growth]]) supplies those drivers, and the documented central tendency of those drivers (see [[concepts/ratio-mean-reversion-and-continuing-value-benchmarks]]) sets the priors. A constant $ROCE$ at the cost of capital ⇒ zero residual earnings; conservative accounting (expensing R&D, goodwill, advertising) yields a **permanent positive** residual earning even when projects are zero-NPV, so long-run residual earnings are positive for the average firm (Feltham & Ohlson 1995; Beaver & Ryan 2000; Zhang 2000). A constant, nonzero residual earning implies a normal P/E of $\rho_E/(\rho_E-1)$; growth in residual earnings implies an above-normal P/E, so the P/E ratio is an inverse measure of residual earnings. ^[inferred]

## Related

- [[concepts/ratio-hierarchy-for-profitability-and-growth]] — the drivers that fill in the model
- [[concepts/operating-and-financial-leverage-spreading]] — the decomposition that turns drivers into $ROCE$
- [[concepts/ratio-mean-reversion-and-continuing-value-benchmarks]] — the evidence that picks CV1/CV2/CV3
- [[references/sloan1996-accruals-cash-flow-stock-prices]] — the accrual-versus-cash-flow persistence evidence that disciplines the earnings forecasts

- [[concepts/predictive-to-prescriptive-analytics]] — the forecasting stance the model embodies
- [[concepts/cash-based-operating-profitability]] — the cash-based complement to accrual-based profitability
- [[references/pincus2007-accrual-anomaly-international-evidence]] — accruals-based cross-market evidence in the same lineage
- [[references/nissim2001-ratio-analysis-equity-valuation]] — the paper that operationalizes this model for ratio analysis

## Sources

- [[_papers/nissim2001ratio/nissim2001ratio-extracted.md]]
- [[_papers/nissim2001ratio/nissim2001ratio.md]]
