---
title: "Benchmark Instance Design for Inventory Routing"
summary: "IRP benchmark instance design: 270 instances from real fleets, sine demands, clustered positioning, depot bounds, triangle-preserving distances, feature-space projection."
type: concept
tags: [paper, benchmark-instances, instance-generation, inventory-routing, instance-space-analysis, matilda, feature-analysis, vehicle-routing]
provenance:
  extracted: 0.90
  inferred: 0.10
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
  - target: "[[concepts/phase-transition-instance-generation]]"
    type: related_to
  - target: "[[concepts/branch-and-cut]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-search]]"
    type: related_to
  - target: "[[references/poikonen2020-k-mvdrp]]"
    type: derived_from
  - target: "[[references/fagerholt2023-maritime-inventory-routing-survey]]"
    type: derived_from
  - target: "[[references/mutlu2016-lng-annual-delivery-program]]"
    type: derived_from
  - target: "[[references/tamke2023-vrpd-dss]]"
    type: derived_from
  - target: "[[references/goel2015-constraint-programming-lng-ship-scheduling]]"
    type: derived_from
  - target: "[[references/halvorsen-weare2013-lng-routing-berth-inventory]]"
    type: derived_from

---
> [!tldr] New benchmark instances are built by combining real vehicle fleets, non-stationary sine demands, clustered positioning, depot capacity bounds, higher inventory variance, and triangle-inequality-preserving distances, then placed in a feature space to show the original benchmarks leave regions uncovered.

Existing IRP benchmarks have features that tailored methods exploit: inventory capacities as integer multiples of demands, abundant vehicle capacity, stationary demands, and long horizons that allow repeating distribution patterns. The new set avoids overfitting by using non-stationary demands, real-life fleets, higher inventory-capacity variance, an explicit depot capacity bound, random/clustered/mixed positions, depot-minimal inventory costs, and distances rounded to satisfy the triangle inequality.

Instances are pallet-transport based, generic for road transport, with three real vehicle types: small truck 8 EUR-pallets, truck 18, trailer truck 38, and a homogeneous fleet scaled to customers and demand; the vehicle capacity is the most constrained feature in practice, so the fleet comes first. Demand comes from a sine trajectory per customer, mean = B_i K_i sin(θ_i t + φ_i) + K_i, coefficients from uniform distributions, realized demand drawn from a uniform distribution centered on the trajectory with symmetric support a from 0,1, rounded to nearest integer; depot production is constant, S_t = ceil(sum of demands / periods). Inventory capacity follows a minimum visiting frequency F from [1, |T|], I_i = ceil(max(max_t D_it, sum D_it / F)); depot capacity is drawn from [max(S_t, max_i sum_t D_it), sum of all demand], initial customer inventory from [0, min(D_i1 + D_i2, L_i)], initial depot inventory from [sum of first-period customer demand, min(S_1 + S_2, L_0)]; customer inventory marginal cost is drawn from [0.0, 0.3] with economies of scale at the depot. ^[inferred]

Nodes sit on a 500 × 500 grid, urban 0.1 km per unit, rural 0.5 km; C_ij = floor(0.1 E_ij + 1) urban and floor(0.5 E_ij + 1) rural, Euclidean distance E_ij; rounding plus one keeps the triangle inequality valid, which matters because many algorithms work well only when it holds. Clustered positioning draws a center uniformly, then an angle uniform, a radius from an exponentially decaying distribution p(x|λ) = λ e^{−λr}, λ = 50 tested as a city or town; random-clustered positioning places 50% randomly, the rest clustered. Transport cost is 1 euro per km, below the reported freight rates of 1.52 euros/km and 1.58 euros/km for trailer trucks.

The naming is A-P-N-Q-T: area (rural/urban), positioning (R/C/RC), customers (10, 25, 50, 100, 200), capacity (8/18/38), periods (6/9/12); varying attributes one at a time yields 270 instances. Thirteen features are defined: customers, periods, vehicles, demand standard deviation, inventory capacity standard deviation, edge cost standard deviation, inventory-to-edge cost ratio, demand-to-inventory ratio, demand-to-vehicle-capacity ratio, inventory-to-vehicle ratio, depot-customer inventory cost ratio, demand-to-initial-inventory ratio, initial-inventory-to-capacity ratio. MATILDA auto-selects the 10 least overlapping features correlated with the gap criterion, then projects to z1, z2 coordinates; new instances (red) and original instances (blue) occupy distinct areas, so the new set complements the original.

Feature plots show demand standard deviation much larger for new instances, edge cost standard deviation varying more across the three location structures, demand-to-inventory ratio taking three to four distinct levels for original instances matching the two-and-three multiples structure while new instances show continuous transition, new instances with lower demand-to-initial-inventory ratio so fewer customers can be served in the first period from initial inventory, lower initial-inventory-to-capacity ratio so customers start emptier, few vehicles on the left of the space, many vehicles on the right. Eighteen new instances share customers, vehicles and periods with original instances, 40 original instances share with new ones; the new features make the instances harder, not easier, so the seven other features do not make the new instances easier.

## Related

- [[concepts/phase-transition-instance-generation]] - the phase transition crossing that clustered instances produce.
- [[concepts/branch-and-cut]] - the exact method measured on the new set.
- [[concepts/large-neighborhood-search]] - the heuristic method measured on the new set.
- [[references/pisinger2019-large-neighborhood-search]] - the LNS/ALNS chapter providing the framework the new matheuristic is compared with.
- [[references/poikonen2020-k-mvdrp]] — shares paper + vehicle-routing tags with this page
- [[references/fagerholt2023-maritime-inventory-routing-survey]] — shares inventory-routing + paper tags with this page
- [[references/mutlu2016-lng-annual-delivery-program]] — shares inventory-routing + paper tags with this page
- [[references/tamke2023-vrpd-dss]] — shares paper + vehicle-routing tags with this page
- [[references/goel2015-constraint-programming-lng-ship-scheduling]] — shares inventory-routing + paper tags with this page
- [[references/halvorsen-weare2013-lng-routing-berth-inventory]] — shares inventory-routing + paper tags with this page

## Sources

- `[[_papers/skalnes2024new/skalnes2024new-extracted.md]]`
- `[[_papers/skalnes2024new/skalnes2024new.md]]`
