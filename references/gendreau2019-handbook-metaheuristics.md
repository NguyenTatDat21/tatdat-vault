---
title: >-
  Handbook of Metaheuristics (Gendreau & Potvin, 2019)
category: references
tags: [book, metaheuristics, operations-research, optimization]
relationships:
  - target: "[[concepts/tabu-search]]"
    type: uses
  - target: "[[concepts/variable-neighborhood-search]]"
    type: uses
  - target: "[[concepts/large-neighborhood-search]]"
    type: uses
  - target: "[[concepts/parallel-metaheuristics-cooperative-search]]"
    type: uses
  - target: "[[concepts/hyper-heuristics]]"
    type: uses
  - target: "[[references/montemanni2024-pdsvrp-collective-drones]]"
    type: related_to
sources:
  - _papers/gendreau2019handbook/gendreau2019handbook-extracted.md
  - _papers/gendreau2019handbook/gendreau2019handbook.md
  - _papers/gendreau2019handbook/images/page_20_image_3.jpg
  - _papers/gendreau2019handbook/images/page_20_image_4.jpg
  - _papers/gendreau2019handbook/images/page_26_image_2.jpg
  - _papers/gendreau2019handbook/images/page_47_image_7.jpg
  - _papers/gendreau2019handbook/images/page_85_image_2.jpg
  - _papers/gendreau2019handbook/images/page_123_image_2.jpg
  - _papers/gendreau2019handbook/images/page_257_image_2.jpg
summary: >-
  Distilled handbook-level patterns for tabu search, VNS, LNS/ALNS, cooperative parallel search, and hyper-heuristics used in routing and combinatorial optimization.
provenance:
  extracted: 0.74
  inferred: 0.23
  ambiguous: 0.03
base_confidence: 0.57
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T08:35:02Z
updated: 2026-10-22T18:14:03Z
---

# Handbook of Metaheuristics (Gendreau & Potvin, 2019)

This handbook consolidates core metaheuristic design patterns and compares how they are applied across combinatorial optimization domains, including routing and scheduling.

## Key Ideas

- Metaheuristics differ mainly by how they balance intensification and diversification under fixed compute budgets.
- Memory-based control (e.g., tabu search), neighborhood-change control (VNS), and destroy/repair control (LNS/ALNS) are reusable design families.
- Cooperative parallel search improves robustness and often solution quality when exchanges preserve diversity and avoid premature convergence.
- Hyper-heuristics move control one level up: they search over heuristics instead of directly searching over candidate solutions.
- Together, these families provide a shared vocabulary for designing routing solvers across truck-only and truck-drone settings. ^[inferred]

## Chapter Signals Relevant to Routing

- **Tabu Search (Chapter 2):** explicit treatment of tabu tenure, aspiration, and candidate-list strategies.
- **Variable Neighborhood Search (Chapter 3):** formal neighborhood-change logic (VND, RVNS, BVNS).
- **Large Neighborhood Search (Chapter 4):** destroy/repair framing and ALNS-style adaptive operator control.
- **Parallel Metaheuristics (Chapter 13):** cooperative multi-search taxonomies and communication design trade-offs.
- **Hyper-Heuristics (Chapter 14):** updated classification by selection/generation and online/offline/no learning.

## Bibliographic Record

- Citation key: `gendreau2019handbook`
- DOI: `10.1007/978-3-319-91086-4`
- Canonical URL: <http://link.springer.com/10.1007/978-3-319-91086-4>
- Publication: *Springer International Publishing* (2019)
- Authors: Michel Gendreau; Jean-Yves Potvin
- Companion metadata note: [[_papers/gendreau2019handbook/gendreau2019handbook.md]]

## Related

- [[concepts/tabu-search]]
- [[concepts/variable-neighborhood-search]]
- [[concepts/large-neighborhood-search]]
- [[concepts/parallel-metaheuristics-cooperative-search]]
- [[concepts/hyper-heuristics]]
- [[references/montemanni2024-pdsvrp-collective-drones]]
- [[concepts/pdsvrp-c]]
- [[_papers/ropke2006adaptive/ropke2006adaptive-extracted]]
- [[_papers/lourenco2019iterated/lourenco2019iterated-extracted]]
- [[_papers/pisinger2019large/pisinger2019large-extracted]]

## Open Questions

- Which handbook patterns transfer best to collaborative truck-drone routing without heavy retuning?
- What communication policy gives the best robustness/compute trade-off in cooperative search for large VRP variants?

## Sources

- [[_papers/gendreau2019handbook/gendreau2019handbook-extracted.md]]
- [[_papers/gendreau2019handbook/gendreau2019handbook.md]]
- [[_papers/gendreau2019handbook/images/page_20_image_3.jpg]]
- [[_papers/gendreau2019handbook/images/page_20_image_4.jpg]]
- [[_papers/gendreau2019handbook/images/page_26_image_2.jpg]]
- [[_papers/gendreau2019handbook/images/page_47_image_7.jpg]]
- [[_papers/gendreau2019handbook/images/page_85_image_2.jpg]]
- [[_papers/gendreau2019handbook/images/page_123_image_2.jpg]]
- [[_papers/gendreau2019handbook/images/page_257_image_2.jpg]]
