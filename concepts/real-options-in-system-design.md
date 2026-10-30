---
title: "Real Options in Engineering System Design"
category: concepts
tags: [real-options, flexibility, design-flexibility, capacity-expansion, managerial-flexibility]
relationships:
  - target: "[[concepts/monte-carlo-simulation]]"
    type: related_to
  - target: "[[concepts/mean-reversion-jump-diffusion-price-model]]"
    type: related_to
  - target: "[[concepts/jensens-law-uncertainty-valuation]]"
    type: related_to
  - target: "[[references/yusuf2023-flexible-lng-production-monte-carlo-stochastic]]"
    type: related_to
sources:
  - "[[_papers/yusuf2023strategic/yusuf2023strategic-extracted.md]]"
  - "[[_papers/yusuf2023strategic/yusuf2023strategic.md]]"
summary: "Flexibility as a financial real option: the right not the obligation to change the system; on-system and in-system flexibility, call and put framing, and the 5 to 7.8 MTPA AP-X capacity option."
provenance:
  extracted: 0.89
  inferred: 0.11
  ambiguous: 0.00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-28
tier: supporting
created: 2026-10-28T14:30:00Z
updated: 2026-10-30T14:08:41Z
---

# Real Options in Engineering System Design

> [!tldr]
> **Definition:** flexibility is treated as a financial real option — the right, not the obligation, to change the system in response to exogenous uncertainty — so design decisions are evaluated by the value of the response, not by the plan.
> **Why it matters here:** a fixed design commits capital at time 0 and sells the option; a flexible design keeps the option and is evaluated on the price distribution, which is why a project with 40-50% of capex in liquefaction needs the option.

Flexibility exists "on the system" as flexible managerial decisions, and "in the system" as technical capacity adaptation, and "compared to a standard fixed design, flexibility has been found to improve the net life-cycle performance of an industrial system by 10-30%".
The financial real-option framing: flexibility "provides the investor with the 'right' but not the obligation to change the system in response to exogenous uncertainties", accounting for flexibility "minimises the possible undesirable outcomes and financial losses (known as a call option), and maximises the possibility of seizing opportunities and increasing profits (known as a put option)".
The AP-X case is a concrete option exercise: the investor buys a 7.8 MTPA AP-X train at project start, or buys a 5 MTPA C3MR train and exercises the expansion by adding the nitrogen expander when the market develops, and "there are no technical limitations that restrict changing the production levels from 5 MTPA to 7.8 MTPA and vice versa".
The binding technical constraint is the shape of the option: "operating at any production level between the two capacities is technically infeasible", so the exercise is binary, and the option price is the spread between the 5 MTPA and 7.8 MTPA economics. ^[inferred]

The diversification side of the option is the selling strategy: option a produces only the contracted 5 MTPA at the fixed $8.76/MMBTU, option b expands to 7.8 MTPA and sells the extra 2.8 MTPA at Henry Hub index and the remaining 1.8 MTPA at the fixed $3.00/MMBTU to low-income markets.
The ENPV of option b, $2.90 billion in scenario 1, is higher than the ENPV of option a, $2.88 billion, so the option is exercised when the expected value of the extra sales exceeds the cost of capacity, and the paper notes the difference in ENPVs between the two options is small. ^[inferred]
The paper's own limitation is that demand levels are assumed, not forecast, so the option is priced on fixed scenarios, and forecasting demand with time-series models is named as the upgrade path.

## Sources

- [Yusuf et al. 2023, Strategic and flexible LNG production under uncertain future demand and natural gas prices, Heliyon, DOI 10.1016/j.heliyon.2023.e16358](https://doi.org/10.1016/j.heliyon.2023.e16358) — the on-system/in-system distinction, the 10-30% figure, the call/put framing, and the AP-X capacity option.
- [Trigeorgis 1996, Real Options: Managerial Flexibility and Strategy in Resource Allocation, MIT Press](https://mitpress.mit.edu/9780262041236/real-options/) — the real-options foundation the source cites.
- [De Neufville & Scholtes 2011, Flexibility in Engineering Design, MIT Press](https://mitpress.mit.edu/9780262144639/flexibility-engineering-design/) — the 10-30% life-cycle improvement claim.
- [Hu & Cardin 2015, Generating flexibility in the design of engineering systems, Res. Eng. Des. 26, 121-143, DOI 10.1007/s00163-015-0189-9](https://doi.org/10.1007/s00163-015-0189-9) — the four-step flexibility design framework.
- [Roberts et al. 2002, Large capacity single train AP-X hybrid LNG process, Gastech Conf.](https://doi.org/10.1016/B978-0-444-59496-9.50047-3) — the AP-X capacity flexibility the option is priced on.

## Related

- [[concepts/monte-carlo-simulation]] is the pricing engine for the option value.
- [[concepts/mean-reversion-jump-diffusion-price-model]] is the underlying price process.
- [[concepts/jensens-law-uncertainty-valuation]] is the rule that makes the option valuable.
- [[references/yusuf2023-flexible-lng-production-monte-carlo-stochastic]] documents this instance.
