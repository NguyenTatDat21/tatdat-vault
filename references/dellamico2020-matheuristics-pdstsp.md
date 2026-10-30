---
title: Matheuristic Algorithms for PDSTSP (Dell'Amico et al., 2020)
category: references
tags: [paper, drones, pdstsp, matheuristics]
relationships:
  - target: "[[concepts/parallel-drone-scheduling-traveling-salesman-problem]]"
    type: related_to
  - target: "[[references/dinh2021-haco-pdstsp]]"
    type: related_to
  - target: "[[references/nguyen2022-min-cost-pdsvrp]]"
    type: related_to
  - target: "[[concepts/min-cost-parallel-drone-scheduling-vrp]]"
    type: related_to
  - target: "[[references/ha2018-min-cost-tsp-d]]"
    type: related_to
  - target: "[[references/mbiadousaleu2022parallel]]"
    type: related_to
  - target: "[[references/murray2015flying]]"
    type: related_to
  - target: "[[references/shaabani2023-multiproduct-mirp-matheuristic]]"
    type: related_to
  - target: "[[references/windrasmara2022-alns-multi-drop-fstsp]]"
    type: related_to
sources:
  - _papers/dellamico2020matheuristic/dellamico2020matheuristic-extracted.md
  - _papers/dellamico2020matheuristic/dellamico2020matheuristic.md
summary: >-
  Introduces a simplified branch-and-cut MILP and Fast/RRLS matheuristics for
  PDSTSP, proving optimality on all 20-customer instances and improving many
  large-instance best-known solutions.
provenance:
  extracted: 0.84
  inferred: 0.11
  ambiguous: 0.05
base_confidence: 0.77
lifecycle: draft
lifecycle_changed: 2026-10-29T17:15:00Z
tier: core
created: 2026-10-22T23:45:17Z
updated: 2026-10-30T14:38:55Z
---

# Matheuristic Algorithms for PDSTSP (Dell'Amico et al., 2020)

> [!tldr] The paper proposes a stronger PDSTSP MILP solved in branch-and-cut mode plus a family of matheuristics (`Fast`, `Fast-2`, `Fast-3`, `RRLS`) that trade off speed and quality, with competitive large-instance performance.

## Problem & Scope

The Parallel Drone Scheduling Traveling Salesman Problem (PDSTSP) splits customers between:
- a truck tour from depot to depot,
- multiple depot-launched drone round trips,

with objective on overall completion time (makespan) and feasibility constraints on drone eligibility.

## Method / Architecture

The paper contributes:
1. a simplified MILP (`PDS`) with dynamic subtour-cut separation in branch-and-cut, ^[inferred]
2. sequence-restricted matheuristics that solve TSP first and let MILP optimize drone assignment,
3. RRLS random-restart local-search framework with time-limited MILP subsolves for scalability.

Design pattern:
- use route-order constraints to keep MILP tractable,
- keep enough flexibility for reassignment,
- restart around improved sequences.

## Results

- The MILP proves optimality for all benchmark instances with 20 customers.
- On larger instances, `Fast` is very fast (often seconds) but lower quality, while `RRLS` improves solution quality with longer runtimes.
- The paper reports **28 improved best-known solutions** on large benchmark sets.

## Limitations

- Performance depends on solving repeated restricted MILPs; parameter tuning (time caps, neighborhood windows) is important. ^[inferred]
- Reported quality/runtime trade-offs vary by instance family and hardware normalization assumptions. ^[ambiguous]

## Related

- [[concepts/parallel-drone-scheduling-traveling-salesman-problem]]
- [[references/windrasmara2022-alns-multi-drop-fstsp]] — multi-drop FSTSP ALNS in the matheuristic lineage.
- [[references/dinh2021-haco-pdstsp]]
- [[references/nguyen2022-min-cost-pdsvrp]]
- [[references/shaabani2023-multiproduct-mirp-matheuristic]] — the same fix-and-optimize pattern: a heuristic fixes arcs, then a solver optimizes the remaining model
- [[concepts/min-cost-parallel-drone-scheduling-vrp]]
- [[references/ha2018-min-cost-tsp-d]]

## Bibliographic Record

- Citation key: `dellamico2020matheuristic`
- DOI: `10.1007/s10479-020-03562-3`
- Canonical URL: <https://doi.org/10.1007/s10479-020-03562-3>
- Publication: *Annals of Operations Research* (2020)
- Authors: Mauro Dell'Amico; Manuel Iori; Sergio Novellani; Andrea Subramanian
- Companion metadata note: [[_papers/dellamico2020matheuristic/dellamico2020matheuristic.md]]

## Sources

- [[_papers/dellamico2020matheuristic/dellamico2020matheuristic-extracted.md]]
- [[_papers/dellamico2020matheuristic/dellamico2020matheuristic.md]]
