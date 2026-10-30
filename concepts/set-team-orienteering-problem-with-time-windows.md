---
title: Set Team Orienteering Problem with Time Windows (STOPTW)
category: concepts
tags: [orienteering, time-windows, clustered-routing, heuristics]
relationships:
  - target: "[[references/yu2024-sarl-stoptw]]"
    type: derived_from
  - target: "[[concepts/set-orienteering-problem]]"
    type: extends
  - target: "[[concepts/tabu-search]]"
    type: related_to
sources:
  - _papers/yu2024simulated/yu2024simulated-extracted.md
  - _papers/yu2024simulated/yu2024simulated.md
summary: STOPTW extends SOP/TOPTW by assigning profits to customer clusters while enforcing customer and depot time windows over multiple tours.
provenance:
  extracted: 0.84
  inferred: 0.14
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-22
tier: core
created: 2026-10-22T11:29:44Z
updated: 2026-10-30T14:08:41Z
---

# Set Team Orienteering Problem with Time Windows (STOPTW)

STOPTW is a clustered orienteering variant where profit is collected at the **cluster** level (not per individual stop), and all served customers must respect time-window constraints.

## Key Ideas

- Customers are partitioned into clusters.
- Visiting at least one customer in a cluster earns that cluster’s profit.
- Multiple tours (vehicles/routes) are allowed.
- Every selected customer visit must satisfy time windows for customer and depot.
- Objective: maximize total collected cluster profit under feasibility constraints.

## Algorithmic Pattern (Yu et al.)

A practical pattern for STOPTW is:

1. represent route/cluster decisions as a two-part encoding,
2. decode the encoding into full itineraries, checking customer/depot time windows, vehicle endurance, and total time limits as the solution is built, ^[inferred]
3. improve via neighborhood moves (swap/insertion/reversion/customer-switch),
4. use adaptive move-selection (ε-greedy) inside simulated annealing.

This gives a robust heuristic profile on large clustered instances under short solve budgets. ^[inferred]

## Open Questions

- How well does STOPTW transfer when cluster structure is data-driven rather than synthetic benchmark grouping?
- Which move-selection policy remains best when real-time travel-time uncertainty is added? ^[inferred]

## Related

- [[references/yu2024-sarl-stoptw]]
- [[concepts/set-orienteering-problem]]
- [[concepts/tabu-search]]
- [[references/lu2024-hybrid-evolutionary-algorithm-sop]]

- [[references/song2018-persistent-uav-delivery-milp-rhta]] — persistent UAV delivery with payload-weighted flight time, solved by a receding-horizon petal heuristic in under 0.4 s
## Sources

- [[_papers/yu2024simulated/yu2024simulated-extracted.md]]
- [[_papers/yu2024simulated/yu2024simulated.md]]
