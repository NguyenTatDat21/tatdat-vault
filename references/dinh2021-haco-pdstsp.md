---
title: Hybrid Ant Colony Optimization for PDSTSP (Dinh et al., 2021)
category: references
tags: [paper, drones, pdstsp, metaheuristics]
relationships:
  - target: "[[concepts/parallel-drone-scheduling-traveling-salesman-problem]]"
    type: uses
  - target: "[[references/dellamico2020-matheuristics-pdstsp]]"
    type: related_to
  - target: "[[concepts/min-cost-parallel-drone-scheduling-vrp]]"
    type: related_to
  - target: "[[references/nguyen2022-min-cost-pdsvrp]]"
    type: related_to
sources:
  - _papers/dinh2021ants/dinh2021ants-extracted.md
  - _papers/dinh2021ants/dinh2021ants.md
summary: >-
  HACO metaheuristic for PDSTSP using dual pheromone trails and a fast split-by-DP
  decoder, outperforming prior PDSTSP metaheuristics on benchmark classes.
provenance:
  extracted: 0.89
  inferred: 0.09
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T23:45:17Z
updated: 2026-10-22T23:45:17Z
---

# Hybrid Ant Colony Optimization for PDSTSP (Dinh et al., 2021)

> [!tldr] The paper introduces a hybrid ant-colony method for PDSTSP that combines two pheromone systems, a dynamic-programming split decoder, and targeted local search to improve solution quality within practical runtimes.

## Problem & Contribution

The problem is PDSTSP: one truck tour plus multiple depot-based drone trips, minimizing completion time.

Main contribution:
- first ant-colony style metaheuristic tailored to PDSTSP,
- dual pheromone structure for assignment and sequencing decisions,
- efficient split procedure controlling quality/speed via label granularity.

## Method / Architecture

HACO components:
1. **Assignment pheromone** for truck-vs-drone customer allocation.
2. **Sequence pheromone** for giant-tour construction.
3. **Split-by-DP decoding** on acyclic graph to produce feasible truck/drone schedules.
4. **Local search** operators (truck-drone and drone-drone swaps).
5. **Smooth max-min pheromone updates** to stabilize exploration.

The `nb_l` label parameter controls the runtime-quality trade-off in the split phase.

## Results

- HACO outperforms the two state-of-the-art metaheuristics it is compared against (the paper's SDFGQ18 and DMN20) in both running time and solution quality.
- Instances are typically solved in under 200 s per run; the fair comparison runs HACO 10 times at 300 s per instance.
- 23 new best known solutions found out of the 90 benchmark instances considered.

## Limitations

- Performance is parameter-sensitive (pheromone bounds/evaporation, ant count, split granularity).
- Results are benchmark-centric and may require recalibration for new geography or operating regimes. ^[inferred]

## Related

- [[concepts/parallel-drone-scheduling-traveling-salesman-problem]]
- [[references/dellamico2020-matheuristics-pdstsp]]
- [[concepts/min-cost-parallel-drone-scheduling-vrp]]
- [[references/nguyen2022-min-cost-pdsvrp]]
- [[references/ha2018-min-cost-tsp-d]]

## Bibliographic Record

- Citation key: `dinh2021ants`
- DOI: `10.1145/3449639.3459342`
- Canonical URL: <https://doi.org/10.1145/3449639.3459342>
- Publication: *Proceedings of the Genetic and Evolutionary Computation Conference (GECCO)*, June 2021
- Authors: Quoc Trung Dinh; Duc Dong Do; Minh Hoàng Hà
- Companion metadata note: [[_papers/dinh2021ants/dinh2021ants.md]]

## Sources

- [[_papers/dinh2021ants/dinh2021ants-extracted.md]]
- [[_papers/dinh2021ants/dinh2021ants.md]]
