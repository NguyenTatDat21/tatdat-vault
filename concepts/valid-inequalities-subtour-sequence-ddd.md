---
title: Valid Inequalities for Subtours and Infeasible Sequences in DDD
summary: Location-based valid inequalities in DDD, subtour at most |M| - 1, infeasible
  sequence at most |M| - 2, valid for every network, low runtime impact.
type: concept
tags: [valid-inequalities, subtour-elimination, infeasible-sequences, dynamic-discretization, integer-programming, location-based]
provenance:
  extracted: 0.91
  inferred: 0.09
  ambiguous: 0.0
base_confidence: 0.57
created: '2026-10-28T23:10:00+07:00'
updated: 2026-10-30T19:12:06Z
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
  - target: '[[concepts/partially-time-expanded-network-lower-bound]]'
    type: related_to
  - target: '[[concepts/primal-arc-sets-ddd-two-networks]]'
    type: related_to
  - target: '[[concepts/lengthen-arcs-add-node-ddd-refinement]]'
    type: related_to
  - target: '[[concepts/first-in-first-out-property-in-time-dependent-travel]]'
    type: related_to
  - target: '[[concepts/duration-objective-depot-discretization]]'
    type: related_to
  - target: '[[concepts/dynamic-discretization-discovery]]'
    type: related_to
  - target: "[[references/vu2020-ddd-td-tsptw-time-expanded-network]]"
    type: related_to

---

> [!tldr] DDD adds location-based valid inequalities, subtour ≤ |M| − 1, infeasible sequence ≤ |M| − 2, defined on locations, so they apply to every time-expanded network, ruling out all timed copies, and they barely change runtime.

When the solution of TD-TSPTW(D_T) contains a subtour (v_i, …, v_k) with v_i = v_k and distinct consecutive locations, M is the set of locations visited, and constraint 7, the sum of x over arcs in A ∩ (M × M) over all time-indexed arcs in A_T, at most |M| − 1, is added to the IP in every subsequent iteration, M is defined by locations in N, not by timed nodes in N_T, so the inequality rules out all timed copies of a subtour on M.

When the solution prescribes a location sequence (v_i, …, v_k) that cannot appear in a feasible TD-TSPTW solution, the path-based inequality, the sum over the sequence arcs of x, at most |M| − 2, is added, again defined by locations in N, valid for any network D_T, forbidding all timed copies of the sequence.

Few inequalities are added, 5.08 subtour-based and 14.93 infeasible-sequence inequalities per instance on Set 1, 2.34 and 10.97 on w100, valid inequalities do not significantly impact DDD performance, configurations Base + VI 948/110.42/15.99 vs Base 950/101.19/17.46 on Set 1, 960/4.09/9.65 vs 960/3.94/9.97 on w100, so valid inequalities are necessary together with primal IPs for fastest runtimes. ^[inferred]

Inequalities are location-based, so they remain valid as the network is refined, arcs lengthened, nodes added. They target sets of solutions with similar attributes, not only the current solution, the same mechanism rules out sequences that violate time windows under true travel times.

## Related

- [[concepts/partially-time-expanded-network-lower-bound]] - the inequalities live in the partial IP, Properties 1-5, the lower bound.
- [[concepts/primal-arc-sets-ddd-two-networks]] - the primal networks solved with the inequalities added.
- [[concepts/lengthen-arcs-add-node-ddd-refinement]] - lengthening removes the current solution from the feasible region, the inequalities rule out its location sequence family.
- [[concepts/first-in-first-out-property-in-time-dependent-travel]] - FIFO makes infeasible sequences detectable under true travel times.
- [[concepts/duration-objective-depot-discretization]] - the inequalities are added to the duration networks.
- [[concepts/dynamic-discretization-discovery]] - DDD's valid-inequality pattern, ruling out timed copies by location families.
- [[concepts/first-in-first-out-property-in-time-dependent-travel]] - FIFO.

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
