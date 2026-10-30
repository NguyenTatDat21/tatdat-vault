---
title: Multiple Flying Sidekicks Traveling Salesman Problem (mFSTSP)
category: concepts
tags: [truck-drone-routing, synchronization, makespan, heuristics]
relationships:
  - target: "[[references/murray2020-multiple-flying-sidekicks-tsp]]"
    type: derived_from
  - target: "[[concepts/k-multi-visit-drone-routing-problem]]"
    type: related_to
  - target: "[[concepts/min-cost-parallel-drone-scheduling-vrp]]"
    type: related_to
  - target: "[[references/raj2020multiple-variable-drone-speed-mfstsp]]"
    type: extends
  - target: "[[references/nguyen2023-pdstsp-collective-drones]]"
    type: derived_from
  - target: "[[concepts/multi-drop-flying-sidekick-traveling-salesman-problem]]"
    type: related_to
    note: "Reciprocal - concepts/multi-drop-flying-sidekick-traveling-salesman-problem references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/morandi2024-orienteering-problem-with-drones]]"
    type: related_to
    note: "Reciprocal - references/morandi2024-orienteering-problem-with-drones references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/murray2015flying]]"
    type: related_to
    note: "Reciprocal - references/murray2015flying references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
  - target: "[[references/windrasmara2022-alns-multi-drop-fstsp]]"
    type: related_to
    note: "Reciprocal - references/windrasmara2022-alns-multi-drop-fstsp references this page."
    confidence: 0.7
    basis: observed
    since: "2026-10-30T14:38:55Z"
sources:
  - _papers/murray2020multiple/murray2020multiple-extracted.md
  - _papers/murray2020multiple/murray2020multiple.md
summary: mFSTSP models one truck coordinated with multiple UAVs, with launch/retrieval synchronization and payload-dependent endurance, minimizing overall completion time.
provenance:
  extracted: 0.88
  inferred: 0.1
  ambiguous: 0.02
base_confidence: 0.77
lifecycle: draft
lifecycle_changed: 2026-10-29T17:15:00Z
tier: core
created: 2026-10-22T11:39:28Z
updated: 2026-10-30T14:38:55Z
---

# Multiple Flying Sidekicks Traveling Salesman Problem (mFSTSP)

mFSTSP is a truck-and-drone routing model where **one truck** coordinates with **multiple UAVs** to serve customers and minimize mission completion time.

The mFSTSP-VDS variant ([[references/raj2020multiple-variable-drone-speed-mfstsp|Raj & Murray, 2020]]) adds UAV cruise speeds as decision variables on top of this model.

## Key Ideas

- Customers are assigned to truck or UAV service.
- UAV sorties launch from and return to truck rendezvous points.
- UAV feasibility depends on endurance and payload-dependent energy limits.
- Launch/retrieval events create synchronization constraints that materially affect schedule quality.
- Objective is makespan minimization (not route-cost minimization).

## Practical Algorithmic Pattern

A useful pattern from this line of work is:

1. build an initial truck/UAV partition,
2. generate feasible UAV sorties with priority on hard-to-serve nodes,
3. solve a timing/synchronization subproblem to schedule truck motion and UAV operations,
4. iterate with tighter truck-customer lower bounds.

This decomposition captures most of the value while avoiding full-model MILP blowups on practical instance sizes. ^[inferred]

## Why It Matters

mFSTSP is one of the clearest templates for moving from single-UAV routing abstractions to operationally realistic **multi-UAV coordination**, and it shows both:

- strong gains versus truck-only baselines,
- diminishing marginal gains from adding more UAVs.

That tradeoff is important for fleet sizing decisions. ^[inferred]

## Open Questions

- How does mFSTSP behavior change when customer requests arrive online rather than being known upfront?
- What is the best way to co-optimize UAV count, endurance class mix, and automation investment under capital constraints? ^[inferred]

## Related

- [[references/murray2020-multiple-flying-sidekicks-tsp]]
- [[references/windrasmara2022-alns-multi-drop-fstsp]] — multi-drop FSTSP ALNS, multiple drones per truck sortie.
- [[concepts/k-multi-visit-drone-routing-problem]]
- [[concepts/min-cost-parallel-drone-scheduling-vrp]]
- [[concepts/vehicle-routing-with-synchronization-constraints]]
- [[references/poikonen2020-k-mvdrp]]
- [[references/nguyen2023-pdstsp-collective-drones]] — shares makespan + synchronization tags with this page

## Sources

- [[_papers/murray2020multiple/murray2020multiple-extracted.md]]
- [[_papers/murray2020multiple/murray2020multiple.md]]
