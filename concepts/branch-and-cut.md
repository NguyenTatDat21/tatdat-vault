---
title: "Branch-and-Cut for the Inventory Routing Problem"
summary: "Branch-and-cut on aggregated IRP MILP: dynamic subtour separation, capacity, disjoint route and Coelho-Laporte inequalities, h-DR omitted for large instances, schedule formulation to 6 periods."
type: concept
tags: [paper, branch-and-cut, inventory-routing, valid-inequalities, subtour-elimination, gurobi, mip]
provenance:
  extracted: 0.75
  inferred: 0.25
  ambiguous: 0.00
base_confidence: 0.67
created: "2026-10-28T22:52:00+07:00"
updated: 2026-10-30T14:39:22Z
tier: core
category: concepts
lifecycle: draft
lifecycle_changed: "2026-10-28"
sources:
  - "[[_papers/skalnes2024new/skalnes2024new-extracted.md]]"
  - "[[_papers/skalnes2024new/skalnes2024new.md]]"
relationships:
  - target: "[[concepts/branch-and-price-column-generation]]"
    type: related_to
  - target: "[[references/archetti2023-branch-and-cut-sop]]"
    type: related_to
  - target: "[[concepts/benchmark-instance-design]]"
    type: related_to
  - target: "[[references/fagerholt2023-maritime-inventory-routing-survey]]"
    type: derived_from
  - target: "[[references/mutlu2016-lng-annual-delivery-program]]"
    type: derived_from
  - target: "[[references/goel2015-constraint-programming-lng-ship-scheduling]]"
    type: derived_from
  - target: "[[references/cheng2020-drone-routing-energy-function]]"
    type: derived_from
  - target: "[[references/halvorsen-weare2013-lng-routing-berth-inventory]]"
    type: derived_from
  - target: "[[references/hendel2022-adaptive-lns-for-mip]]"
    type: derived_from
  - target: "[[concepts/phase-transition-instance-generation]]"
    type: related_to

---
> [!tldr] The B&C method of this paper solves the aggregated IRP MILP with dynamic subtour cuts, three families of valid inequalities and a root-node-only separation policy; h-DR inequalities are dropped for large instances, the schedule formulation is kept to six periods.

The model is the aggregated form of Skålnes et al. 2022, objective transport cost plus inventory cost, one inventory-balance equation per customer and one for the depot, limits between lower and upper inventory, the delivered quantity bounded by K times the depot-visit variable δ_0t, the max-level policy q_it ≤ L_i − s_i(t−1), delivery allowed only when a customer is visited through min(L_i − I_it, Q) δ_it, degree constraints, flow balance, subtour elimination, capacitated subtour elimination, domain constraints. ^[inferred]

The branch-and-cut solver takes the linear relaxation of constraints 7-15 and 18-21, adds subtour constraints dynamically as the search finds them, and separates three inequality families: the capacity inequalities of Desaulniers et al. 2016, the simple disjoint route inequalities of Avella et al. 2018, and the Coelho & Laporte 2014 valid inequalities. The h-DR inequalities are omitted because separation with h = 8 is too expensive for 100-200 customer instances, so capacity and DR inequalities are separated exactly only in the root node. ^[inferred]

The customer schedule formulation is not used because enumeration is too slow for 9 and 12 periods, and is considered suitable only for six periods or less. B&C time limit is 7,200 seconds, single thread, C++ with Gurobi 9.5 default settings. Feasible solutions were found on 133 of 270 instances, 13 instances solved to optimality, all with 10 customers. The B&C performs best on small trucks (capacity 8), and solution quality drops as vehicle capacity rises, plausibly because a large capacity makes the linear relaxation weaker under the delivery constraint, a large Q needs less arc flow, so the bound is worse.

The paper concludes that branch-cut-and-price is favored when routes have few visits, consistent with the route-length observation: small trucks visit one customer in over 75% of routes, so B&C gets good gaps on small trucks; the new set with large vehicles favors commodity-flow formulations, which scale well with many vehicles and periods.

## Related

- [[references/archetti2023-branch-and-cut-sop]] - the branch-and-cut for the Set Orientation Problem, a sibling cut-and-branch family.
- [[concepts/branch-and-price-column-generation]] - column generation in branch-and-price, the family favored when routes have few visits.
- [[concepts/benchmark-instance-design]] - the instance space that the B&C is measured on.
- [[concepts/large-neighborhood-search]] - the neighborhood family the matheuristic comparison uses alongside B&C.
- [[references/fagerholt2023-maritime-inventory-routing-survey]] — shares inventory-routing + paper tags with this page
- [[references/mutlu2016-lng-annual-delivery-program]] — shares inventory-routing + paper tags with this page
- [[references/goel2015-constraint-programming-lng-ship-scheduling]] — shares inventory-routing + paper tags with this page
- [[references/cheng2020-drone-routing-energy-function]] — shares branch-and-cut + paper tags with this page
- [[references/halvorsen-weare2013-lng-routing-berth-inventory]] — shares inventory-routing + paper tags with this page
- [[references/hendel2022-adaptive-lns-for-mip]] — shares mip + paper tags with this page

## Sources

- `[[_papers/skalnes2024new/skalnes2024new-extracted.md]]`
- `[[_papers/skalnes2024new/skalnes2024new.md]]`
