---
title: >-
  Multi-Drop Flying Sidekick Traveling Salesman Problem (AN/AM solution
  representation)
category: concepts
tags: [drones, delivery, tsp, heuristics]
summary: The multi-drop FSTSP where the truck+drone route is decoded from a
  node permutation array AN and action-code array AM, launching drones that
  serve several customers in one sortie.
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.00
base_confidence: 0.67
tier: supporting
lifecycle: draft
created: 2026-10-29T17:12:00Z
updated: 2026-10-30T14:39:22Z
sources:
  - "_papers/windrasmara2022adaptive/windrasmara2022adaptive-extracted.md"
relationships:
  - target: "[[references/windrasmara2022-alns-multi-drop-fstsp]]"
    type: extends
  - target: "[[concepts/multiple-flying-sidekicks-traveling-salesman-problem]]"
    type: extends
  - target: "[[concepts/k-multi-visit-drone-routing-problem]]"
    type: related_to
  - target: "[[references/murray2015flying]]"
    type: related_to
lifecycle_changed: 2026-10-29T17:12:00Z
---

# Multi-Drop Flying Sidekick Traveling Salesman Problem
The multi-drop FSTSP is the FSTSP in which the truck-borne drone serves multiple customers in a single sortie.^[inferred] The truck route, drone sortie, launch node, retrieval node, truck array C and drone array D encode a valid operation `OP_k = {T_k, D_k}` with `C ∩ D = ∅` in one of five valid forms, with the drone endurance constraint `τ_i→D1 + Σ τ_Di→Di+1 + τ_D|D|→j + w_r^D ≤ ε` and operation cost `t_k = max{t(T_k), t(D_k)}`.
^m1
The solution representation is a `[(n+2),2]` matrix of the node-permutation array AN (depot first and last, `LastPos_Truck`/`LastPos_Drone` tracking, four decode rules, Algorithm 1) and the action-code array AM with 0 = truck+drone together (retrieval node when a drone is in the sortie), 1 = drone-only visit, 2 = truck call-the-truck. The scheme is more compact than Ponza 2016's `[(n+2),3]` launch/retrieval lists `TT`,`DD`,`DR`, and copes with the two prohibited conditions of the benchmark.
^m2

## Figures (source image)
![Fig. 3 — Solution representation scheme and the derived solution.](/images/2432354792093189397564762615771111542531736220353451335424152753.jpg)

![Fig. 4 — Two Prohibited Conditions (Ponza, 2016).](/images/1827514754515313653342715256363631347131202263206352117433616276.jpg)

![Fig. 8 — The procedure for solution adjustment.](/images/15116254243262455323523544223242415242536165326432233222241313566.jpg)

## Related
- [[references/windrasmara2022-alns-multi-drop-fstsp]] — the ALNS paper that introduced the representation.
- [[concepts/multiple-flying-sidekicks-traveling-salesman-problem]] — sibling single-vehicle families.
- [[concepts/k-multi-visit-drone-routing-problem]] — multi-visit routing.
- [[references/murray2015flying]] — FSTSP lineage.

## Sources

- `_papers/windrasmara2022adaptive/windrasmara2022adaptive-extracted.md`
