---
title: Duration Objective with Depot Discretization
summary: Duration objective in DDD, depot nodes for every departure time up to ebar0,
  zero-cost waiting arcs, arcs from depot cost -t, l0 = z - 1 + t0, network sizes
  double.
type: concept
tags: ['[duration-objective', depot-discretization, waiting-arcs, time-expanded-networks, dynamic-discretization, 'enumeration]']
provenance:
  extracted: 0.9
  inferred: 0.1
  ambiguous: 0.0
base_confidence: 0.67
created: '2026-10-28T23:10:00+07:00'
updated: 2026-10-30T14:08:41Z
tier: core
category: concepts
lifecycle: draft
lifecycle_changed: '2026-10-28'
sources:
- '  - "[[_papers/vu2020dynamic/vu2020dynamic-extracted.md]]"'
- '  - "[[_papers/vu2020dynamic/vu2020dynamic.md]]"'
- '  - "[[_papers/vu2020dynamic/images/page_9_image_3.jpg]]"'
- '  - "[[_papers/vu2020dynamic/images/page_9_image_5.jpg]]"'
- '  - "[[_papers/vu2020dynamic/images/page_12_image_1.jpg]]"'
- '  - "[[_papers/vu2020dynamic/images/page_18_image_1.jpg]]"'
- '  - "[[_papers/vu2020dynamic/images/page_18_image_3.jpg]]"'
- '  - "[[_papers/vu2020dynamic/images/page_22_chart_1.jpg]]"'
- '  - "[[_papers/vu2020dynamic/images/page_23_chart_1.jpg]]"'
- '  - "[[_papers/vu2020dynamic/images/page_27_image_5.jpg]]"'
relationships:
  - target: "[[references/wahal2020-joint-value-profitability-international]]"
    type: derived_from
  - target: '[[concepts/first-in-first-out-property-in-time-dependent-travel]]'
    type: uses
  - target: '[[concepts/partially-time-expanded-network-lower-bound]]'
    type: uses
  - target: '[[concepts/primal-arc-sets-ddd-two-networks]]'
    type: uses
  - target: '[[concepts/lengthen-arcs-add-node-ddd-refinement]]'
    type: uses
  - target: '[[concepts/valid-inequalities-subtour-sequence-ddd]]'
    type: uses
  - target: '[[concepts/dynamic-discretization-discovery]]'
    type: uses

---

> [!tldr] Duration objective: DDD adds depot nodes for every feasible departure time up to ē_0 = min_i max_t {Δ_0i(t) ≤ l_i}, waiting arcs at the depot with zero cost, arcs from the depot with cost −t, l_0 = z − 1 + t_0, and network sizes double over makespan.

Duration minimizes t_{n+1} − t_0, the objective is return time minus departure time. Depot departure is flexible, so the latest feasible departure ē_0 = min over locations i of max over t with Δ_0i(t) ≤ l_i is computed, and nodes (0, t) for t = e_0 + ε, e_0 + 2ε, …, ē_0 are added to N_T, ε is the unit of depot waiting, example, with two locations, l_1 = 5, l_2 = 7, τ_01(·) = 1, τ_02(·) = 2, ē_0 = 4. Waiting arcs (0, t), (0, t') between consecutive depot times have cost 0, arcs from the depot have c_0i(t) = −t, so the depot cost underestimate is exact, the lower-bound lemma is adapted by restricting the induction base to feasible tours, arcs leaving the depot have accurate costs.

Adaptations, primal networks D̄¹ and D̄² solved with the duration objective, a sub-tour-free solution from the lower-bound network is evaluated for every possible depot departure by enumerating departure times, the greedy evaluation works because waiting at non-depot locations is not needed in an optimal duration solution, when a new feasible solution z is found, l_0 is set to z − 1 + t_0, t_0 being that solution's departure time, followed by re-preprocessing.

Results: Set 1, makespan 952 solved, 10.94 s, 4.62 iterations vs duration 930 solved, 143.45 s, 9.77 iterations, w100 makespan 960/1.22/4.11 vs duration 955/106.20/9.87. Running two hours solves all instances, the remaining 22 Set 1 instances average 3,647.47 s, the 5 w100 instances 3,688.40 s. Network sizes, initial/final for makespan 53.34/188.80, 53.50/191.15, for duration 111.88/452.24, 94.50/438.89, the final-to-initial ratio is about the same, duration numbers about double. The future scheme should add depot nodes dynamically, not a priori, by enumeration. ^[inferred]

## Related

- [[concepts/first-in-first-out-property-in-time-dependent-travel]] - FIFO makes depot waiting the only beneficial waiting, so enumerating depot departure times suffices.
- [[concepts/partially-time-expanded-network-lower-bound]] - the depot-node set, waiting arcs, the lemma adapted to feasible tours.
- [[concepts/primal-arc-sets-ddd-two-networks]] - primal networks solved with the duration objective, tour durations over depot departures.
- [[concepts/lengthen-arcs-add-node-ddd-refinement]] - pruning, l_0 = z − 1, the duration case l_0 = z − 1 + t_0.
- [[concepts/valid-inequalities-subtour-sequence-ddd]] - inequalities apply to the duration networks, location-based.
- [[concepts/dynamic-discretization-discovery]] - DDD, the depot enumeration is the known DDD pattern with an extra node family.
- [[concepts/first-in-first-out-property-in-time-dependent-travel]] - FIFO.
- [[references/wahal2020-joint-value-profitability-international]] — shares   + , + - tags with this page

## Sources

- `- "[[_papers/vu2020dynamic/vu2020dynamic-extracted.md]]"`
- `- "[[_papers/vu2020dynamic/vu2020dynamic.md]]"`
- `- "[[_papers/vu2020dynamic/images/page_9_image_3.jpg]]"`
- `- "[[_papers/vu2020dynamic/images/page_9_image_5.jpg]]"`
- `- "[[_papers/vu2020dynamic/images/page_12_image_1.jpg]]"`
- `- "[[_papers/vu2020dynamic/images/page_18_image_1.jpg]]"`
- `- "[[_papers/vu2020dynamic/images/page_18_image_3.jpg]]"`
- `- "[[_papers/vu2020dynamic/images/page_22_chart_1.jpg]]"`
- `- "[[_papers/vu2020dynamic/images/page_23_chart_1.jpg]]"`
- `- "[[_papers/vu2020dynamic/images/page_27_image_5.jpg]]"`
