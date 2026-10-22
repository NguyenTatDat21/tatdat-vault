---
title: Hybrid Evolutionary Algorithm for the Set Orienteering Problem (Lu et al.)
category: references
tags: [paper, orienteering, evolutionary-algorithm, metaheuristics]
relationships:
  - target: "[[concepts/set-orienteering-problem]]"
    type: uses
  - target: "[[concepts/tabu-search]]"
    type: uses
  - target: "[[references/gendreau2019-handbook-metaheuristics]]"
    type: related_to
sources:
  - _papers/lu2024effective/lu2024effective-extracted.md
  - _papers/lu2024effective/lu2024effective.md
summary: Presents a hybrid evolutionary algorithm for SOP with cluster-aware crossover and two-phase local refinement, reporting strong benchmark performance.
provenance:
  extracted: 0.9
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.57
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T11:22:57Z
updated: 2026-10-22T11:29:44Z
---

# Hybrid Evolutionary Algorithm for the Set Orienteering Problem (Lu et al.)

> [!tldr] This paper introduces a hybrid evolutionary algorithm (HEA) for SOP that combines cluster-based crossover, randomized mutation, and two-phase local refinement; it reports strong results on 192 large benchmark instances.

## Problem & Contribution

The Set Orienteering Problem (SOP) maximizes collected cluster profit under a travel-time budget. Vertices are grouped into clusters, and a cluster contributes profit if at least one of its vertices is visited.

The paper proposes an HEA tailored to SOP and positions it against existing SOP heuristics.

## Method

The HEA combines:

1. randomized population initialization,
2. cluster-based crossover,
3. randomized mutation,
4. two-phase local refinement (feasible + infeasible search),
5. population update with quality/diversity control.

The two-phase refinement uses tabu-search style move control and explicitly explores infeasible regions to escape local traps before returning to feasibility.

## Results

From the source text:

- Extensive experiments are reported on 192 large SOP benchmark instances.
- The abstract reports improved best-known solutions for 54 instances and matches for 133 instances.
- Comparative sections also report stronger counts against selected baselines (e.g., 81 improved and 107 matched), suggesting results depend on comparison protocol/reporting slice. ^[ambiguous]
- A Wuhan one-day trip case study reports average gain of about 5.72% versus a greedy heuristic.

## Limitations

- Performance evidence is benchmark-heavy; real deployment quality depends on travel-time and clustering calibration. ^[inferred]
- Reported improvement counts vary by section and benchmark slice, so exact headline counts should be interpreted with the comparison setup in mind. ^[ambiguous]

## Bibliographic Record

- Citation key: `lu2024effective`
- DOI: `10.1016/j.ins.2023.119813`
- Canonical URL: https://www.sciencedirect.com/science/article/pii/S0020025523013981
- Publication: *Information Sciences* (2024)
- Authors: Yongliang Lu, Una Benlic, Qinghua Wu
- Companion metadata note: [[_papers/lu2024effective/lu2024effective.md]]

## Related

- [[concepts/set-orienteering-problem]]
- [[concepts/tabu-search]]
- [[concepts/hyper-heuristics]]
- [[references/gendreau2019-handbook-metaheuristics]]
- [[_papers/lu2024effective/lu2024effective-extracted]]

## Sources

- [[_papers/lu2024effective/lu2024effective-extracted.md]]
- [[_papers/lu2024effective/lu2024effective.md]]
