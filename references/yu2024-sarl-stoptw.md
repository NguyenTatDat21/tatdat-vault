---
title: Simulated Annealing with Reinforcement Learning for STOPTW (Yu et al.)
category: references
tags: [paper, orienteering, simulated-annealing, reinforcement-learning]
relationships:
  - target: "[[concepts/set-team-orienteering-problem-with-time-windows]]"
    type: uses
  - target: "[[concepts/set-orienteering-problem]]"
    type: extends
  - target: "[[references/lu2024-hybrid-evolutionary-algorithm-sop]]"
    type: related_to
  - target: "[[references/nguyen2025set]]"
    type: related_to
    note: "Reciprocal - references/nguyen2025set references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
sources:
  - _papers/yu2024simulated/yu2024simulated-extracted.md
  - _papers/yu2024simulated/yu2024simulated.md
  - _papers/yu2024simulated/images/page_0_image_8.jpg
  - _papers/yu2024simulated/images/page_5_image_7.jpg
  - _papers/yu2024simulated/images/page_6_image_2.jpg
  - _papers/yu2024simulated/images/page_6_image_4.jpg
  - _papers/yu2024simulated/images/page_9_chart_2.jpg
  - _papers/yu2024simulated/images/page_9_chart_4.jpg
  - _papers/yu2024simulated/images/page_9_chart_6.jpg
  - _papers/yu2024simulated/images/page_9_chart_8.jpg
summary: Introduces SA_RL for STOPTW and reports strong gains over CPLEX and baseline SA on large clustered time-window orienteering instances.
provenance:
  extracted: 0.9
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: supporting
created: 2026-10-22T11:29:44Z
updated: 2026-10-30T14:38:55Z
---

# Simulated Annealing with Reinforcement Learning for STOPTW (Yu et al.)

> [!tldr] This paper formulates the Set Team Orienteering Problem with Time Windows (STOPTW) and proposes SA_RL, where SA neighborhood choice is guided by an ε-greedy learning policy.

## Problem & Contribution

The paper introduces **STOPTW**, a clustered extension of team orienteering with customer time windows. Cluster profit is collected if one member customer is visited within feasible timing.

Main contributions:

1. MILP formulation for STOPTW.
2. SA_RL metaheuristic (SA with reinforcement-style move selection).
3. Benchmark generation for large STOPTW instances.
4. Empirical comparison against CPLEX and vanilla SA.

## Method

SA_RL combines:

- SA acceptance (`exp(-Δ/T)` for worsening moves),
- four neighborhood operators (swap, insertion, reversion, customer-change-in-cluster),
- ε-greedy operator selection with online fitness updates.

Reported tuned parameters include `T0=1.0`, `I_iter=6000`, `α=0.98`, `ε=0.6`.

## Results

From the reported experiments:

- On small instances A[100,20,2], SA and SA_RL both found 8 optimal and 12 better-than-CPLEX solutions within much shorter run times.
- On large instances, SA/SA_RL outperform CPLEX on most instances under short heuristic budgets.
- SA_RL generally improves robustness vs SA and is reported to outperform SA on 13 large benchmark instances.
- Vehicle-count sensitivity shows diminishing profit gains per added vehicle: `+265.24`, `+235.14`, `+197.74`.

## Limitations

- Gains are benchmark-driven; deployment benefit depends on how well clusters and time windows reflect real operating constraints. ^[inferred]
- Relative wins between SA_RL and SA vary by setting, so the advantage is robust but not universal. ^[ambiguous]

## Bibliographic Record

- Citation key: `yu2024simulated`
- DOI: `10.1016/j.eswa.2023.121996`
- Canonical URL: https://www.sciencedirect.com/science/article/pii/S0957417423024983
- Publication: *Expert Systems with Applications* (2024)
- Authors: Vincent F. Yu, Nabila Yuraisyah Salsabila, Shih-Wei Lin, Aldy Gunawan
- Companion metadata note: [[_papers/yu2024simulated/yu2024simulated.md]]

## Related

- [[concepts/set-team-orienteering-problem-with-time-windows]]
- [[concepts/set-orienteering-problem]]
- [[concepts/tabu-search]]
- [[references/lu2024-hybrid-evolutionary-algorithm-sop]]
- [[_papers/yu2024simulated/yu2024simulated-extracted]]

## Sources

- [[_papers/yu2024simulated/yu2024simulated-extracted.md]]
- [[_papers/yu2024simulated/yu2024simulated.md]]
- [[_papers/yu2024simulated/images/page_0_image_8.jpg]]
- [[_papers/yu2024simulated/images/page_5_image_7.jpg]]
- [[_papers/yu2024simulated/images/page_6_image_2.jpg]]
- [[_papers/yu2024simulated/images/page_6_image_4.jpg]]
- [[_papers/yu2024simulated/images/page_9_chart_2.jpg]]
- [[_papers/yu2024simulated/images/page_9_chart_4.jpg]]
- [[_papers/yu2024simulated/images/page_9_chart_6.jpg]]
- [[_papers/yu2024simulated/images/page_9_chart_8.jpg]]
