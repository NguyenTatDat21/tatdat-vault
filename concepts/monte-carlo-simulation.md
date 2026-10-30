---
title: "Monte Carlo Simulation of Project Economics"
category: concepts
tags: [monte-carlo-simulation, stochastic-simulation, npv-distribution, decision-measures, sampling]
relationships:
  - target: "[[concepts/mean-reversion-jump-diffusion-price-model]]"
    type: uses
  - target: "[[concepts/jensens-law-uncertainty-valuation]]"
    type: related_to
  - target: "[[concepts/real-options-in-system-design]]"
    type: related_to
  - target: "[[references/yusuf2023-flexible-lng-production-monte-carlo-stochastic]]"
    type: related_to
sources:
  - "[[_papers/yusuf2023strategic/yusuf2023strategic-extracted.md]]"
  - "[[_papers/yusuf2023strategic/yusuf2023strategic.md]]"
summary: "Monte Carlo simulation samples 10,000 price paths, computes one NPV per path, and reports ENPV, median, standard deviation, skew and kurtosis as the decision measures for a project."
provenance:
  extracted: 0.87
  inferred: 0.13
  ambiguous: 0.00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-28
tier: supporting
created: "2026-10-28T21:30:00+07:00"
updated: 2026-10-30T14:08:41Z
---

# Monte Carlo Simulation of Project Economics

> [!tldr]
> **Definition:** Monte Carlo simulation (MCS) approximates the joint probability distribution of a set of uncertain variables by sampling many independent realizations, computing the system's outcome for each sample, and reporting the whole distribution instead of one average case.
> **Why it matters here:** the mean result of a nonlinear objective is not the result of the means, so an expected-value plan underprices the spread; MCS recovers the spread and turns it into decision measures.

The source uses MCS as the engine of its stochastic economic evaluation: "MCS is mainly used to approximate the probability distribution of all possible random variables to analyse the uncertainties of a certain scenario or a system", and "simulating the scenarios of a system by considering the joint properties of probabilistic distributions of uncertain variables".
Python in Visual Studio Code with the Anaconda distribution generates a sample of 10,000 price paths, and the same simulated prices are used to compute 10,000 NPV estimates at fixed capital and operational costs, risk-free interest rate and project lifetime, so the 10,000 pairs are one random draw per path, not one per parameter. ^[inferred]
The ENPV is the mean of the simulated outcomes, ENPV = (1/N) Σ NPV_n, and the resulting histogram is the project's NPV probability distribution; the deterministic NPV is then compared against it.

## Procedure

1. Fit a stochastic process to historical data (the mean-reverting jump-diffusion price model) and take the parameters as the sampling distribution, so the simulation is calibrated, not assumed.
2. Sample N independent paths (N = 10,000 in the source), each path a sequence of yearly prices over the 20 production years.
3. For each path, evaluate the cash-flow equation to get one NPV; fixed costs, discount rate, and lifetime stay at their constant values across all samples.
4. Report the distribution: mean (ENPV), median, standard deviation, skewness, and kurtosis.
5. Compare ENPV against the deterministic NPV, and compare candidate strategies on the distribution, not on the mean alone.

The paper reports the median alongside the mean for every scenario, so the median NPV $2.83 billion for scenario 1, $2.63 billion for scenario 2, and $2.85 billion for option b scenario 1 are read together with the ENPV.
Skewness is read as tail direction: positive skewness means a heavier right tail, negative skewness means a heavier left tail, so the right tail is the profitable region and the left tail is the risk region.
Kurtosis above 3 means tails heavier than a normal distribution, so "the highly profitabile opportunities associated with the right tail, and the high risks associated with the left tail", and the source notes that investors hedge the left tail with put options and other tail-risk strategies.
Sampling complexity is the practical limit: the 10,000-path sample size must be large enough for the tails to be stable, and the source does not report a convergence check on its sample size. ^[inferred]

The method is independent of the pricing system, so the same engine applies to Henry Hub, TTF, NBP and JKM, and to any of the 4 pricing systems the source tracks, including the TTF, NBP, JKM and Henry Hub series.
The same simulation applies to a fixed production level, so MCS is applied in step 2 to 7.8 MTPA at fixed production, and in step 3 to the two capacity options, i.e. 5 MTPA expanded to 7.8 MTPA, with 65% of capacity contracted for 20 years and 2.8 MTPA sold spot, so the sampling only changes the price series. ^[inferred]

## Sources

- [Yusuf et al. 2023, Strategic and flexible LNG production under uncertain future demand and natural gas prices, Heliyon, DOI 10.1016/j.heliyon.2023.e16358](https://doi.org/10.1016/j.heliyon.2023.e16358) — the MCS description, the 10,000 path sample, the ENPV formula, and the median/std/skew/kurtosis reporting.
- [Reid 2015, Random Walks Down Wall Street, Stochastic Processes in Python](http://www.turingfinance.com/random-walks-down-wall-street-stochastic-processes-in-python/) — the Python implementation the source cites for the simulation.
- [Shaffie & Jaaman 2016, Monte Carlo on net present value for capital investment in Malaysia, Procedia 219, 688-693, DOI 10.1016/j.sbspro.2016.05.052](https://doi.org/10.1016/j.sbspro.2016.05.052) — the MCS-on-NPV application the source cites.

## Related

- [[concepts/mean-reversion-jump-diffusion-price-model]] is the sampling distribution the simulation uses.
- [[concepts/jensens-law-uncertainty-valuation]] is the inequality MCS is invoked to satisfy.
- [[concepts/real-options-in-system-design]] is the decision layer the distribution feeds.
- [[references/yusuf2023-flexible-lng-production-monte-carlo-stochastic]] is the page documenting this instance.
