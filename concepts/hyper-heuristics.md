---
title: >-
  Hyper-Heuristics
category: concepts
tags: [metaheuristics, hyper-heuristics, optimization]
relationships:
  - target: "[[concepts/large-neighborhood-search]]"
    type: related_to
  - target: "[[references/yi2023-ace-gsf-automated-design-cvrptw]]"
    type: related_to
  - target: "[[concepts/parallel-metaheuristics-cooperative-search]]"
    type: related_to
  - target: "[[concepts/variable-neighborhood-search]]"
    type: related_to
  - target: "[[references/gendreau2019-handbook-metaheuristics]]"
    type: derived_from
  - target: "[[concepts/actor-critic-entropy-automated-algorithm-design]]"
    type: related_to
  - target: "[[concepts/adaptive-large-neighborhood-search-for-mip]]"
    type: related_to
  - target: "[[concepts/green-vehicle-routing-problem-taxonomy]]"
    type: related_to
  - target: "[[concepts/metaheuristic-hybridization]]"
    type: related_to
  - target: "[[concepts/multi-objective-metaheuristic-tuning-validation]]"
    type: related_to
  - target: "[[concepts/set-orienteering-problem]]"
    type: related_to
  - target: "[[concepts/simulated-annealing-metropolis-cooling]]"
    type: related_to
  - target: "[[concepts/swarm-intelligence-pso-aco]]"
    type: related_to
  - target: "[[concepts/transformer-seq2seq-routing-solver]]"
    type: related_to
  - target: "[[references/asghari2021-green-vrp-state-of-the-art-review]]"
    type: related_to
  - target: "[[references/fuertes2023-transformer-multi-uav-routing]]"
    type: related_to
  - target: "[[references/hendel2022-adaptive-lns-for-mip]]"
    type: related_to
  - target: "[[references/pisinger2019-large-neighborhood-search]]"
    type: related_to
  - target: "[[references/santini2018-alns-acceptance-criteria]]"
    type: related_to
sources:
  - _papers/gendreau2019handbook/gendreau2019handbook-extracted.md
summary: >-
  Hyper-heuristics optimize over heuristics rather than direct solutions, mainly via heuristic selection or generation with online, offline, or no learning.
provenance:
  extracted: 0.78
  inferred: 0.19
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T08:35:02Z
updated: 2026-10-30T14:38:55Z
---

# Hyper-Heuristics

A hyper-heuristic does not directly edit a candidate solution. Instead, it chooses or constructs low-level heuristics that then operate on solutions.

## Key Ideas

- Two broad classes: **heuristic selection** and **heuristic generation**.
- Learning modes: **online learning**, **offline learning**, or **no learning**.
- Low-level heuristics may be constructive or perturbative, which affects acceptance and termination behavior.
- Hyper-heuristics are meant to improve cross-domain generality by separating control policy from problem-specific move operators.
- In routing contexts, ALNS destroy/repair operators are common low-level heuristics that a selector can manage. ^[inferred]

Related pages: [[concepts/large-neighborhood-search]], [[concepts/parallel-metaheuristics-cooperative-search]], [[concepts/variable-neighborhood-search]], [[references/gendreau2019-handbook-metaheuristics]], and [[references/montemanni2024-pdsvrp-collective-drones]].

## Open Questions

- Which state features are most predictive for selecting low-level heuristics in collaborative truck-drone routing?
- How much domain-specific engineering is still required before a hyper-heuristic policy transfers reliably? ^[inferred]

## Related

- [[references/yi2023-ace-gsf-automated-design-cvrptw]] — ACE learns hyper-heuristic component choices by reinforcement.
- [[references/santini2018-alns-acceptance-criteria]] — ALNS as a hyper-heuristic: 9 acceptance criteria ranked on CVRP, CMST and QAP

## Sources

- [[_papers/gendreau2019handbook/gendreau2019handbook-extracted.md]]
