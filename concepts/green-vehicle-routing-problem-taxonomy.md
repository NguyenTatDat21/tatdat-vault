---
title: Green Vehicle Routing Problem Taxonomy
category: concepts
tags: [green-logistics, vehicle-routing, taxonomy, sustainability]
relationships:
  - target: "[[references/asghari2021-green-vrp-state-of-the-art-review]]"
    type: derived_from
  - target: "[[concepts/vehicle-routing-with-synchronization-constraints]]"
    type: related_to
  - target: "[[concepts/hyper-heuristics]]"
    type: related_to
  - target: "[[references/ganjia2026-multiobjective-sustainable-supply-chain-scheduling]]"
    type: uses
sources:
  - _papers/asghari2021green/asghari2021green-extracted.md
  - _papers/asghari2021green/asghari2021green.md
  - _papers/ganjia2026multiobjective/ganjia2026multiobjective-extracted.md
  - _papers/ganjia2026multiobjective/ganjia2026multiobjective.md
  - _papers/ganjia2026multiobjective/images/page_20_chart_6.jpg
  - _papers/ganjia2026multiobjective/images/page_24_chart_5.jpg
summary: >-
  Structured map of Green-VRP variants by vehicle technology, objective type, operational scenario, and solver family for comparing environmental-routing models.
provenance:
  extracted: 0.84
  inferred: 0.14
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-24
tier: supporting
created: 2026-10-22T19:33:55Z
updated: 2026-10-24T04:15:00Z
---

# Green Vehicle Routing Problem Taxonomy

Green-VRP research spans multiple fleet technologies and modeling assumptions, so a taxonomy is needed to compare papers without mixing incompatible problem settings.

## Key Dimensions

- **Vehicle stream:** ICEV, AFV, HEV.
- **Objective family:** emissions, fuel/energy use, cost, service quality, or multi-objective combinations.
- **Scenario design:** charging/refueling infrastructure, uncertainty assumptions, fleet composition, and policy constraints.
- **Solver class:** exact optimization, heuristics, and metaheuristics.

- **Emission coupled to scheduling:** Ganjia et al. fold fuel + emission cost into one freight objective — the emission term is linear in vehicle weight + load, quadratic in average speed $\times$ distance — decided jointly with batch-delivery routing on a heterogeneous VRPTW; Taguchi-tuned NSGA-II cut freight + emission cost 45% (126.2 to 69.3 MLCU) and tardiness 96% (23,950 to 858 h), MOPSO 32% and 96% [[references/ganjia2026-multiobjective-sustainable-supply-chain-scheduling]].
## Why It Matters

- Prevents false apples-to-oranges comparisons across Green-VRP studies.
- Clarifies which constraints are technology-specific versus generally routing-specific.
- Makes research-gap detection easier when one stream is overrepresented. ^[inferred]
- Green fleets where emissions enter as an objective share the ganjia lever: gains come from parameter tuning on the cost/tardiness front, not from a reported CO$_2$ percentage — the -16% CO$_2$ deferral figure is not in the ganjia source, which reports fuel/emission **cost**, not mass. ^[inferred]

## Related

- [[references/asghari2021-green-vrp-state-of-the-art-review]]
- [[concepts/vehicle-routing-with-synchronization-constraints]]
- [[concepts/hyper-heuristics]]
- [[concepts/large-neighborhood-search]]

- [[references/ganjia2026-multiobjective-sustainable-supply-chain-scheduling]]
## Open Questions

- Which taxonomy dimensions best predict whether exact methods remain practical?
- How should hybrid ICEV/AFV/HEV fleets be normalized for fair cross-paper comparison? ^[inferred]

## Sources

- [[_papers/asghari2021green/asghari2021green-extracted.md]]
- [[_papers/asghari2021green/asghari2021green.md]]
- [[_papers/ganjia2026multiobjective/ganjia2026multiobjective-extracted.md]]
- [[_papers/ganjia2026multiobjective/ganjia2026multiobjective.md]]
- [[_papers/ganjia2026multiobjective/images/page_20_chart_6.jpg]]
- [[_papers/ganjia2026multiobjective/images/page_24_chart_5.jpg]]
