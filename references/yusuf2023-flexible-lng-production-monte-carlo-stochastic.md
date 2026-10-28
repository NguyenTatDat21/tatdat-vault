---
title: "Strategic and flexible LNG production under uncertain future demand and natural gas prices"
summary: "Four-step framework valuing AP-X LNG flexibility in Qatar: mean-reverting jump-diffusion Henry Hub prices, 10,000 Monte Carlo paths, demand scenarios at 5/6/7.8 MTPA, hedging by LTC plus spot mix."
type: reference
tags: ["LNG-flexibility", "stochastic-price-modelling", "real-options", "monte-carlo-simulation", "long-term-contracts", "spot-selling"]
provenance:
  base: 0.00
  extracted: 0.86
  inferred: 0.12
  ambiguous: 0.02
tier: supporting
base_confidence: 0.67
created: "2026-10-28T21:30:00+07:00"
updated: "2026-10-28T21:30:00+07:00"
lifecycle: draft
lifecycle_changed: "2026-10-28"
sources:
  - "[[_papers/yusuf2023strategic/yusuf2023strategic.md]]"
  - "[[_papers/yusuf2023strategic/yusuf2023strategic-extracted.md]]"
  - "[[_papers/yusuf2023strategic/images/page_5_chart_11.jpg]]"
  - "[[_papers/yusuf2023strategic/images/page_8_image_18.jpg]]"
  - "[[_papers/yusuf2023strategic/images/page_9_chart_10.jpg]]"
  - "[[_papers/yusuf2023strategic/images/page_11_chart_9.jpg]]"
relationships:
  - target: "[[concepts/monte-carlo-simulation]]"
    type: uses_method
  - target: "[[concepts/mean-reversion-jump-diffusion-price-model]]"
    type: uses_method
  - target: "[[concepts/real-options-in-system-design]]"
    type: applies_to
  - target: "[[concepts/jensens-law-uncertainty-valuation]]"
    type: cites
---
# Strategic and Flexible LNG Production under Uncertain Demand and Prices (Yusuf et al. 2023, Heliyon)

> [!tldr] Yusuf et al. (2023, Heliyon) value the flexibility of an AP-X liquefaction train in Qatar with a four-step framework: AHP technology selection, deterministic NPV, Monte-Carlo ENPV over mean-reverting jump-diffusion Henry Hub prices, and a diversified long-term-contract plus spot selling strategy tested under demand scenarios.

## Summary

The paper is a techno-economic valuation of embedding production flexibility in an LNG project at the pre-final-investment-decision stage, using the AP-X technology (Air Products) for a single-train brownfield plant in Qatar with a 25-year lifetime (5 construction, 20 production years).
Liquefaction is the most capital- and energy-intensive part of the chain, where 40-50% of capital expenditure is spent, and 72% of global capacity used APCI technologies in 2018^[inferred], so the paper links that technical flexibility to the shift away from oil-indexed long-term contracts.
The four-step methodology is: deterministic selection and evaluation of a baseline technology; stochastic evaluation under Henry Hub prices at fixed production; stochastic evaluation under three demand levels with a capacity-expansion real option; and a sensitivity test of the diversified selling strategy^[inferred].
The mean-reverting geometric Brownian motion with jump diffusion dlog(P_t) = (θ^gas − α^gas log(P_t)) dt + σ^gas dW + J dN is simulated 10,000 times in Python to produce 10,000 NPV estimates, and ENPV = (1/N) Σ NPV_n is compared with the deterministic NPV.

## Key ideas

1. Fixed design yields 40-50% of project capital expenditure in the liquefaction process^[inferred], so production flexibility has to be embedded in the early design to change capacity efficiently in cost and time.
2. Jensen's law is the analytic core of the paper: the NPV built from expected demand and prices is less than or equal to the expected NPV over the full distribution, so the value of flexibility is the value of that spread.
3. Flexibility in engineering systems improves net life-cycle performance by 10-30% compared to a standard fixed design.
4. Long-term contracts (LTCs) lasting 20-25 years use a take-or-pay clause that transfers volume risk to the buyer, so 842.5 MTPA of capacity was in pre-FID in 2018^[inferred].
5. Henry Hub is chosen over TTF, NBP and JKM as the pricing system, because only HH prices are available from 1990 and the hub is the most liquid.
6. The price model parameters are taken from Lucheroni & Mari (2018) fitted on Henry Hub data 1990-2013, a period containing the 2001-2002 supply spikes, Hurricane Katrina and Rita in 2005, and the 2008-2009 recession^[inferred].
7. AP-X is chosen over C3MR, DMR and MFC by an Analytic Hierarchy Process scored on a 0-4 scale with a random consistency check: AP-X scores 0.558, and is designed to raise capacity from 5 to 7.8 MTPA by adding a nitrogen expander.
8. Production can only be run at 5 MTPA (C3MR) or 7.8 MTPA (AP-X): operating at any level between the two is technically infeasible, which is what turns a capacity decision into a binary real option.
9. LNG sold on the spot market is priced as 1.15 × Henry Hub + liquefaction fees, while long-term contracted volumes are sold at a fixed $8.76/MMBTU and low-income-market volumes at a fixed $3.00/MMBTU.
10. The sensitivity table shows that raising the interest rate from 10% to 15% is the strongest single shock: scenario 1 ENPV drops from 2.89 to 0.471 (x10^9 $), scenario 2 from 2.73 to 0.257, scenario 3 from 2.85 to 0.362^[inferred].

## Tables

Verbatim numeric rows of Table 1 (mean-reverting GBM and jump-diffusion parameters, Lucheroni and Mari 2018):

| Parameter | Notation | Value |
|---|---|---|
| Mean-reversion parameters | θ^gas | 0.0432 |
| Mean-reversion parameters | α^gas | 0.0292 |
| Jumps intensity | λ^Jump | 0.2542 |
| Standard deviation for Poisson process | σ^jump | 0.1258 |
| Volatility of gas prices | σ^gas | 0.0737 |
| Mean for Poisson process | μ^Jump | 0.0100 |

Verbatim numeric rows of the sensitivity table (ENPV, standard deviation, skewness and kurtosis for scenarios 1-3 under interest rate 10%/15%, capex ±7.5% at $660/$760/tpa, and initial Henry Hub price ±10%):

| Input condition | Scenario 1 | Scenario 2 | Scenario 3 |
|---|---|---|---|
| ENPV at r = 10% / r = 15% (x10^9 $) | 2.89 / 0.471 | 2.73 / 0.257 | 2.85 / 0.362 |
| Standard deviation (x10^9 $) | 0.386 / 0.228 | 0.543 / 0.260 | 0.566 / 0.295 |
| Skewness | 0.867 / 0.883 | 1.222 / 1.318 | 1.148 / 1.073 |
| Kurtosis | 1.628 / 1.517 | 2.629 / 3.051 | 2.396 / 2.332 |
| ENPV, low capex / high capex (x10^9 $) | 3.21 / 2.59 | 3.02 / 2.42 | 3.15 / 2.53 |
| ENPV, low Henry Hub price / high Henry Hub price (x10^9 $) | 2.70 / 3.09 | 2.57 / 2.72 | 2.86 / 2.84 |
| Standard deviation (x10^9 $) | 0.351 / 0.428 | 0.483 / 0.584 | 0.505 / 0.613 |

The kurtosis row for scenario 3 under low capex reads 11.067, a value inconsistent with the other skewness rows in the same block, so that cell is treated as an OCR artifact. ^[ambiguous]
Scenario 3 is the most robust case: its ENPV moves by 0.4% when the initial Henry Hub forecast is raised 10%, and it has the lowest ENPV change across input parameters.
All three NPV distributions are skewed to the right with heavier right tails, so the paper reads that as higher probability of profitable opportunities.

## Figures

![[_papers/yusuf2023strategic/images/page_5_chart_11.jpg]]
Fig. 1. Natural gas prices from 1990 to 2019.

![[_papers/yusuf2023strategic/images/page_8_image_18.jpg]]
Fig. 4. AHP results for selecting a baseline technology.

![[_papers/yusuf2023strategic/images/page_9_chart_10.jpg]]
Fig. 5. NPV distribution of an AP-X technology with initial forecasted Henry Hub natural gas spot price of $3.06/MMBTU.

![[_papers/yusuf2023strategic/images/page_11_chart_9.jpg]]
Fig. 7. NPV distribution of an AP-X technology with initial forecasted Henry Hub natural gas spot price of $3.06/MMBTU under different demand scenarios and a diversified selling strategy (Option 2: deciding to increase the capacity and sell the remaining to low-income markets): (a) scenario 1, (b) scenario 2, and (c) scenario 3.

The remaining Fig. 2, 3, 6, 8 crops are table/chart crops not embedded here, so they are not listed in sources.

## Results in the source

Selling the full 7.8 MTPA capacity under long-term contracts at the fixed $8.76/MMBTU gives a deterministic NPV of $5.82 billion, while selling the full capacity on the spot market at the average $3.06/MMBTU forecast gives a negative NPV of $1.31 billion.
Stochastic simulation of the spot-only strategy yields an ENPV of $3.58 billion loss, and the paper reads this as Henry Hub prices falling below the $3.06/MMBTU forecast with high probability over the project lifetime.
Option a (no capacity increase) gives ENPV $2.88 billion for scenario 1 against a deterministic NPV of $2.68 billion, ENPV $2.73 billion for scenario 2 against a deterministic $3.35 billion, and ENPV $2.82 billion for scenario 3 against a deterministic $2.54 billion, 11% above the deterministic case.
Option b (capacity increase plus sales of the remaining 1.8 MTPA to low-income markets at $3.00/MMBTU) gives ENPV $2.90 billion in scenario 1 against a deterministic $2.97 billion, and ENPV $2.85 billion in scenario 3 against a deterministic $2.70 billion, 5.6% above the deterministic case.
The paper concludes that contracting the full capacity under long-term contracts is the most secure and most probable profitable strategy, that dedicating the full capacity to spot sales is a great loss, and that a hybrid selling strategy with flexible production is what hedges the risks.
Future work in the paper points to ARIMA and co-integration time-series forecasting for prices and demand, to utility prices and other pricing hubs (TTF, NBP), and to the Optimized Cascade technology.

## Sources

- [Yusuf et al. 2023, Strategic and flexible LNG production under uncertain future demand and natural gas prices, Heliyon, DOI 10.1016/j.heliyon.2023.e16358](https://doi.org/10.1016/j.heliyon.2023.e16358) — the full source of the extracted markdown, the four figures embedded above, and all numeric rows.
- [Lucheroni & Mari 2018, Risk shaping of optimal electricity portfolios in the stochastic LCOE theory, Comput. Oper. Res. 96, 374-385, DOI 10.1016/j.cor.2018.02.011](https://doi.org/10.1016/j.cor.2018.02.011) — the mean-reversion, volatility and jump-intensity parameters reproduced in Table 1.
- [Steuer 2019, Outlook for Competitive LNG Supply, DOI 10.26889/9781784671310](https://doi.org/10.26889/9781784671310) — capital costs of $660-$760/tpa for brownfield Qatar plants, the $710/tpa mid-value, the $2.0/MMBTU gas supply and $1.69/MMBTU liquefaction costs for 2025, and the $8.76/MMBTU contracted price and $3.06/MMBTU spot forecast.
- [Air Products / Pearsall & Schmidt 2012, The AP-X Process, DOI 10.1016/b978-0-444-59496-9.50047-3](https://doi.org/10.1016/b978-0-444-59496-9.50047-3) — the three cooling cycles of AP-X and the 5 to 7.8 MTPA capacity design.
- [International Gas Union, World LNG Report 2019, 126](https://www.igu.org) — 842.5 MTPA of pre-FID capacity in 2018, 72% APCI share, 31% non-long-term share of global trade, and 68% APCI share forecast for 2024.

## Related

- [[concepts/monte-carlo-simulation]] — the method the paper uses to generate 10,000 price paths.
- [[concepts/mean-reversion-jump-diffusion-price-model]] — the Henry Hub price process it simulates.
- [[concepts/real-options-in-system-design]] — the frame for the capacity-expansion decision.
- [[concepts/jensens-law-uncertainty-valuation]] — the inequality the paper tests on NPV.
