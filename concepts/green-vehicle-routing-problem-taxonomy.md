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
sources:
  - _papers/asghari2021green/asghari2021green-extracted.md
  - _papers/asghari2021green/asghari2021green.md
summary: >-
  Structured map of Green-VRP variants by vehicle technology, objective type, operational scenario, and solver family for comparing environmental-routing models.
provenance:
  extracted: 0.86
  inferred: 0.12
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T19:33:55Z
updated: 2026-10-22T19:33:55Z
---

# Green Vehicle Routing Problem Taxonomy

Green-VRP research spans multiple fleet technologies and modeling assumptions, so a taxonomy is needed to compare papers without mixing incompatible problem settings.

## Key Dimensions

- **Vehicle stream:** ICEV, AFV, HEV.
- **Objective family:** emissions, fuel/energy use, cost, service quality, or multi-objective combinations.
- **Scenario design:** charging/refueling infrastructure, uncertainty assumptions, fleet composition, and policy constraints.
- **Solver class:** exact optimization, heuristics, and metaheuristics.

## Why It Matters

- Prevents false apples-to-oranges comparisons across Green-VRP studies.
- Clarifies which constraints are technology-specific versus generally routing-specific.
- Makes research-gap detection easier when one stream is overrepresented. ^[inferred]

## Related

- [[references/asghari2021-green-vrp-state-of-the-art-review]]
- [[concepts/vehicle-routing-with-synchronization-constraints]]
- [[concepts/hyper-heuristics]]
- [[concepts/large-neighborhood-search]]

## Open Questions

- Which taxonomy dimensions best predict whether exact methods remain practical?
- How should hybrid ICEV/AFV/HEV fleets be normalized for fair cross-paper comparison? ^[inferred]

## Sources

- [[_papers/asghari2021green/asghari2021green-extracted.md]]
- [[_papers/asghari2021green/asghari2021green.md]]
