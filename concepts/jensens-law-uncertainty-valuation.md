---
title: "Jensen's Law in Project Valuation"
category: concepts
tags: [jensens-law, npv-vs-enpv, convexity, distribution-valuation, risk-pricing]
relationships:
  - target: "[[concepts/monte-carlo-simulation]]"
    type: related_to
  - target: "[[concepts/real-options-in-system-design]]"
    type: related_to
  - target: "[[concepts/mean-reversion-jump-diffusion-price-model]]"
    type: related_to
  - target: "[[references/yusuf2023-flexible-lng-production-monte-carlo-stochastic]]"
    type: related_to
sources:
  - "[[_papers/yusuf2023strategic/yusuf2023strategic-extracted.md]]"
  - "[[_papers/yusuf2023strategic/yusuf2023strategic.md]]"
summary: "The value at the mean is less than the expected value over the distribution; deterministic NPV is a lower bound, so ENPV above it is option value, below it is a mean-based plan that underprices risk."
provenance:
  extracted: 0.81
  inferred: 0.13
  ambiguous: 0.06
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-28
tier: supporting
created: 2026-10-28T14:30:00Z
updated: 2026-10-30T14:08:41Z
---

# Jensen's Law in Project Valuation

> [!tldr]
> **Definition:** for a convex payoff the value computed at the expected input is less than the expected value over the input distribution, so the spread of the distribution — not its mean — drives the project's true value.
> **Why it matters here:** the deterministic NPV is the benchmark every stochastic case is compared to, so the sign of the gap tells you whether a strategy is option-rich or option-poor.

The source states the law directly: "the value resulting from the joint distribution of uncertainties does not equal the value associated with the average, which can be represented mathematically by Jensen's Law", and "the net present value (NPV) based on expected demand and prices is generally less than or equal to the expected NPV based on the actual demands and prices".
The consequence for evaluation: "evaluation should technically map the entire distribution of uncertainties into the economic performance of a project", which is why the deterministic mean case is a lower bound and the full distribution is the answer.
The observed sign of the gap is a diagnostic: ENPV $3.58 billion negative for the spot-only full-capacity strategy is a loss, and the paper reads the pattern as Henry Hub prices tending, with greater probability, to fall below the $3.06/MMBTU forecast, so the convexity of the payoff is what makes the spot-only case lose.
The paper reports three cases where ENPV exceeds deterministic NPV, satisfying Jensen's law: scenario 3 in option a, ENPV $2.82 billion against deterministic $2.54 billion, 11% greater; scenario 3 in option b, ENPV $2.85 billion against deterministic $2.70 billion, 5.6% greater; and the option a scenario 1 gap. ^[inferred]

The cases where ENPV falls below deterministic NPV are option a scenario 1 (ENPV $2.88 billion, deterministic $2.68 billion, so the ENPV is above, not below) and option a scenario 2 (ENPV $2.73 billion against deterministic $3.35 billion, so ENPV is below), and option b scenario 1 (ENPV $2.90 billion against deterministic $2.97 billion, about 2% less), so the sign of the gap varies across scenarios and strategies. ^[ambiguous]
The paper also cites the same sign pattern in a published comparison where "the calculated ENPV was less than the deterministic NPV", which is treated as evidence that the full distribution matters for valuation.
The practical reading: a strategy whose distribution has a fat right tail is worth more than its mean NPV suggests, because the right tail is the option value, so the deterministic NPV is the exercise price of the option, not the value of the project. ^[inferred]

## Sources

- [Yusuf et al. 2023, Strategic and flexible LNG production under uncertain future demand and natural gas prices, Heliyon, DOI 10.1016/j.heliyon.2023.e16358](https://doi.org/10.1016/j.heliyon.2023.e16358) — the Jensen's-law statement, the ENPV-vs-deterministic-NPV comparisons, and the sign diagnostics.
- [Davidz & Martin 2015, Improving the lifecycle performance of engineering projects with flexible strategies, Syst. Eng. 18, 253-268, DOI 10.1002/sys](https://doi.org/10.1002/sys.20295) — the Jensen-based evaluation framing the source cites.
- [Cardin et al. 2015, Design catalogs: systematic approach to design and value flexibility, Syst. Eng. 18, 453-471](https://doi.org/10.1002/sys.20295) — the ENPV-less-than-NPV comparison the source cites as evidence.

## Related

- [[concepts/monte-carlo-simulation]] produces the distribution the law compares.
- [[concepts/real-options-in-system-design]] values the right tail of the distribution.
- [[concepts/mean-reversion-jump-diffusion-price-model]] generates the spread.
- [[references/yusuf2023-flexible-lng-production-monte-carlo-stochastic]] documents this instance.
