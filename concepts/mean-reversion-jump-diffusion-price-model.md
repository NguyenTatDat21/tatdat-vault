---
title: "Mean-Reverting Jump-Diffusion Price Model"
category: concepts
tags: [mean-reversion, jump-diffusion, geometric-brownian-motion, gas-price-modelling, poisson-jumps]
relationships:
  - target: "[[concepts/monte-carlo-simulation]]"
    type: related_to
  - target: "[[concepts/jensens-law-uncertainty-valuation]]"
    type: related_to
  - target: "[[concepts/real-options-in-system-design]]"
    type: related_to
  - target: "[[references/yusuf2023-flexible-lng-production-monte-carlo-stochastic]]"
    type: related_to
sources:
  - "[[_papers/yusuf2023strategic/yusuf2023strategic-extracted.md]]"
  - "[[_papers/yusuf2023strategic/yusuf2023strategic.md]]"
summary: "dlog(P_t) = (theta - alpha log P_t) dt + sigma dW + J dN: Henry Hub log-price mean reversion plus Poisson jumps; 6 fitted parameters from Henry Hub data 1990-2013."
provenance:
  extracted: 0.88
  inferred: 0.12
  ambiguous: 0.00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-28
tier: supporting
created: 2026-10-28T14:30:00Z
updated: 2026-10-30T14:08:41Z
---

# Mean-Reverting Jump-Diffusion Price Model

> [!tldr]
> **Definition:** dlog(P_t) = (θ − α log(P_t)) dt + σ dW + J dN, a log-price process that drifts back toward a long-run mean, adds continuous Brownian volatility, and adds Poisson-driven jumps that model shocks.
> **Why it matters here:** mean reversion captures the normal gas-price cycle, jump diffusion captures the crises (2001-2002, Katrina/Rita 2005, 2008-2009, COVID-2020), and the two parts together drive the ENPV distribution a project is evaluated on.

The Henry Hub spot price process is written as dlog(P_t) = (θ^gas − α^gas log(P_t)) dt + σ^gas dW + J dN with the model parameters taken from data on 1990-2013, where W is a standard Brownian motion with zero mean and variance t, N is the Poisson jump process with jump amplitude J and intensity λ^Jump, and N and W are independent processes.
The mean-reverting part "describes the normal fluctuations in natural gas prices only", and the jump diffusion "describes the abnormal fluctuations due to shocks caused by different factors such as shocks in oil prices, sudden increase in demand, seasonality, disruptions in production, or global pandemics".
Henry Hub prices are "mean reverting, in which the prices frequently move up and down around a long-term equilibrium mean natural gas price", so a plain GBM with a mean-reversion factor is the natural baseline, and adding jump diffusion is the refinement.

## Parameters (Lucheroni & Mari 2018, fitted on Henry Hub 1990-2013)

| Parameter | Notation | Value |
|---|---|---|
| Mean-reversion | θ^gas | 0.0432 |
| Mean-reversion | α^gas | 0.0292 |
| Jumps intensity | λ^Jump | 0.2542 |
| Standard deviation for Poisson process | σ^jump | 0.1258 |
| Volatility of gas prices | σ^gas | 0.0737 |
| Mean for Poisson process | μ^Jump | 0.0100 |

The parameter values "were considered to be efficient in terms of capturing these shocks", so a fitted model is used as the sampling law, not as a forecast, and the price series 1990-2019 with only Henry Hub available from 1990 is the reason Henry Hub is chosen over TTF (early 2000s), NBP (1996) and JKM.

The model is calibrated on a window that includes the price spikes of 2001-2002, Hurricanes Katrina and Rita in 2005, and the 2008-2009 recession, so the fitted jump intensity 0.2542 already encodes the historical crisis frequency, which is what makes the simulated left tail heavy. ^[inferred]
Henry Hub dropped 21% in 2020 to $2.03/MMBTU, hit $1.63/MMBTU in June 2020 as the lowest monthly average in decades, recovered to a projected $2.89/MMBTU in 2021, dropped 56% in 2009 after the 2008 recession, fell 31% in 2012 versus 2011, and averaged $3.73/MMBTU in 2014 and $4.37/MMBTU in 2015, so the historical path is mean-reverting with real jump episodes, not a smooth series.
The LNG price mapping from gas price to sale price is LNG price ($/MMBTU) = 1.15 × Henry Hub + liquefaction fees, so the jump-diffusion path enters the project valuation through this linear mapping, and a price path that falls below the $3.06/MMBTU forecast drives the spot sale loss. ^[inferred]

## Sources

- [Yusuf et al. 2023, Strategic and flexible LNG production under uncertain future demand and natural gas prices, Heliyon, DOI 10.1016/j.heliyon.2023.e16358](https://doi.org/10.1016/j.heliyon.2023.e16358) — the model form, the Henry Hub data, the historical shock narrative, and the price mapping.
- [Lucheroni & Mari 2018, Risk shaping of optimal electricity portfolios in the stochastic LCOE theory, Comput. Oper. Res. 96, 374-385, DOI 10.1016/j.cor.2018.02.011](https://doi.org/10.1016/j.cor.2018.02.011) — the parameter values fitted from Henry Hub 1990-2013.
- [Mason & Wilmot 2014, Jump processes in natural gas markets, Energy Econ. 46, S69-S79, DOI 10.1016/j.eneco.2014.09.015](https://doi.org/10.1016/j.eneco.2014.09.015) — the jump-process model the source cites.
- [Ranjbari et al. 2013, Stochastic models of natural gas prices, 6, 50-65](https://doi.org/10.1002/978-1-4614-2011-4) — the mean-reversion claim the source cites.

## Related

- [[concepts/monte-carlo-simulation]] is the engine that turns this model into 10,000 paths.
- [[concepts/jensens-law-uncertainty-valuation]] is the valuation rule the distribution is compared against.
- [[concepts/real-options-in-system-design]] consumes the simulated prices for the capacity decision.
- [[references/yusuf2023-flexible-lng-production-monte-carlo-stochastic]] documents this instance.
