---
title: 'Multi-Visit Drone Routing Problem for Pickup and Delivery (MDRP-PD)'
category: references
tags: [drone-routing, pickup-delivery, multi-visit, load-dependent-energy, simulated-annealing, vehicle-routing]
relationships:
  - target: "[[references/poikonen2020-k-mvdrp]]"
    type: extends
  - target: "[[concepts/k-multi-visit-drone-routing-problem]]"
    type: extends
  - target: "[[concepts/payload-induced-drone-battery-consumption-rate]]"
    type: uses
  - target: "[[concepts/large-neighborhood-search]]"
    type: related_to
sources:
  - _papers/meng2023multivisit/meng2023multivisit-extracted.md
  - _papers/meng2023multivisit/meng2023multivisit.md
  - _papers/meng2023multivisit/images/page_1_image_8.jpg
  - _papers/meng2023multivisit/images/page_4_image_19.jpg
  - _papers/meng2023multivisit/images/page_22_chart_2.jpg
  - _papers/meng2023multivisit/images/page_22_chart_3.jpg
summary: >-
  MDRP-PD: K truck-drone pairs serve pickup-and-delivery customers at minimum truck distance + load-dependent drone energy cost; the MP-ISA heuristic is near-exact on small instances.
provenance:
  extracted: 0.8
  inferred: 0.15
  ambiguous: 0.05
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-25
tier: peripheral
created: 2026-10-25T10:55:07Z
updated: 2026-10-30T14:08:41Z
---

# Multi-Visit Drone Routing Problem for Pickup and Delivery (MDRP-PD)

> [!tldr] A fleet of K homogeneous truck-drone pairs serves customers with simultaneous pickup and delivery demands; the objective is truck travel cost plus energy-proportional drone cost. A maximum-payload construction plus improved simulated annealing (MP-ISA) matches the optimal solver on small instances, with a combined truck-drone mode that saves 24% cost over truck-only delivery.

## Problem & Contribution

- Each truck carries exactly one drone; a pair is activated at fixed cost $22 (truck $20 + drone $2) and serves one route of customers, the truck by road, its drone by multi-customer flights launched and retrieved at the same truck node.
- Customers have pickup and delivery demands (e.g., returning online purchases); customers whose demands exceed the drone capacity (3 kg) must be served by the truck.
- The drone's flight time depends on the payload it carries at each node, so energy is consumed proportionally to distance times carried weight; the battery is fully replaced at every retrieval, and a drone arriving before the truck hovers, consuming power.
- The drone may leave a launch node before its truck finishes serving there (prejudgment rule), unlike earlier multi-visit models. ^[inferred] Positioning: this is the first joint treatment of multi-visit drone flights with simultaneous pickup and delivery over a truck-drone-pair fleet, and the first to price the drone by consumed energy rather than by per-km cost.
- Contributions: full MILP with three families of valid inequalities, two analytical results on the maximum number of drone flights, a sufficient condition for the combined mode to beat truck-only, and the MP-ISA heuristic.

![[_papers/meng2023multivisit/images/page_1_image_8.jpg]]
"Fig. 1. Truck-drone routes in opposite directions."

## Method

Objective (eq. 1): truck distance cost + drone energy cost (flight, hovering, launch service time at power P) + pair fixed costs:

$$\min\ c^{T}\sum_{k}\sum_{(i,j)\in A\setminus\{(0,n+1)\}}(x^{0k}_{ij}+x^{1k}_{ij})r_{ij}\ +\ c^{F}\sum_{k}\Big(\sum_{A} e^{k}_{ij}+P\sum_{i}z^{2k}_{i}u^{\prime}_{i}+P\sum_{i}t^{k}_{h,i}\Big)+\ c^{0}\sum_{k}(1-x^{0k}_{0,n+1})$$

Core load-dependent energy model (extended from Liu et al. 2020 and Xiao et al. 2012):

$$t^{k}_{ij}=\frac{\alpha\,(w_{0}+w^{k}_{i})\,r'_{ij}}{P},\qquad e^{k}_{ij}=\alpha\,(w_{0}+w^{k}_{i})\,r'_{ij}$$

- Proposition 1 (upper bound on drone flights): if the truck serves at most half of its customers, $|D^{k}| \le \lceil n^{k}/2 \rceil$.
- Proposition 2 (when the combined mode beats truck-only): sufficient condition $0<c^{F}<(\Delta R^{k}\cdot c^{T}-c^{F0})/(E\cdot\lceil n^{k}/2\rceil)$, with the analogous bound using $(n^{k}-\hat{n}^{k})$ when the truck serves more than half. ^[ambiguous]
- MP-ISA stage 1, maximum payload: $mp_{N_c}=\sum d_i+\sum\max\{0,p_i-d_i\}$; route built by Gurobi TSP (MP_GR), Clarke-Wright + SA (MP_CL), or capacity-aware greedy + SA (MP_MP), then drone flights are split out and inserted in truck-visit order.
- MP-ISA stage 2, improved SA: 16 neighborhood operators in 4 structures (6 single-relocation SR1-6, 6 two-exchange TE1-6, multiple-relocation, 3 block-exchange), taboo list, cooling $T=T_0\beta$ with tuned $T_0=100$, Iter = 15, $\beta=0.95$; regional-setting acceleration cuts launch/retrieval combinations from $(m^k+1)^2$ to $(m^k-|D^k|+1)^2$.
- Feasibility test for each drone flight checks load, and hovering: max tolerable hovering time $T^{k}_{f}=(E-e^{k}_{f})/P$ is compared with the truck-drone arrival gap at retrieval nodes.

![[_papers/meng2023multivisit/images/page_4_image_19.jpg]]
"Fig. 2. A feasible solution to an MDRP-PD problem with 33 customers."

## Results

Parameters: truck capacity 90 kg at 30 km/h, drone 6 kg curb weight + 3 kg payload, $\alpha=3.5$ Wh/(kg·km), $E=504$ Wh, $P=1008$ W, flight time $\le$ 0.5 h; $c^T=\$0.78$/km, $c^F=\$2.48\text{e-3}$/Wh; 43 instances adapted from Augerat A/P sets.

| Comparison | Result | Evidence (lines of extracted md) |
|---|---|---|
| MP-ISA vs Gurobi, 10 n=8 instances | MP-ISA finds the optimum on all; avg 52.35 s vs 299.74 s (no VI) / 89.41 s (VI) | Table 6, line 755 |
| n=10 / n=11 small instances | avg gaps −0.10 / 0.29 and −0.05 / 0.02; Gurobi fails 4/10 C-n11 in 2 h | Table 6, lines 739–788 |
| Valid inequalities | 2 h-unsolved instances drop from 7 to 4 | lines 739–788 |
| Final vs initial solution, sets A / P | cost −18.15% / −25.18%; truck distance −23.25% / −34.97% | Table 7 avg rows, lines 793, 799 |
| Combined mode vs truck-only | total cost −24.31%, truck distance −44.01% on average | line 807 |
| MP-ISA vs IG / [[concepts/large-neighborhood-search|LNS]] baselines | avg best-solution gaps IG 13.94%, LNS 4.90% — MP-ISA best | Table 8, line 850 |
| Multi-visit vs single-visit mode | SV loses 37.90% drone-served customers, +22.65% cost, +38.60% truck distance | Table 9, line 902 |
| Sensitivity, 96 scenarios | cost flattens once W > 6 kg or E > 500 Wh; at σ=10 MP-ISA saves 22.03% vs SV 16.90% | lines 940–1000 |

![[_papers/meng2023multivisit/images/page_22_chart_2.jpg]]
![[_papers/meng2023multivisit/images/page_22_chart_3.jpg]]
"Fig. 7. Best solution for instance A-n33-k5: (left) initial solution and (right) final solution."

## Limitations

- At most one launch and one retrieval location per customer is allowed; power output is fixed and not optimized; demands are deterministic. Stated future work: power optimization, multiple launch/retrieval locations, stochastic demands.
- The MP-ISA feasibility/insertion machinery is heuristic; exactness is only demonstrated on n ≤ 8 and small n = 10/11 instances, where Gurobi needed hours. ^[inferred]
- Cost comparisons hinge on the chosen $c^T/c^F$ ratio: a higher truck-cost ratio is required for the combined mode to be worthwhile (Proposition 2).

## Related

- [[concepts/k-multi-visit-drone-routing-problem]] — single-truck multi-visit ancestry; MDRP-PD adds pickup-and-delivery and a pair fleet
- [[references/poikonen2020-k-mvdrp]] — predecessor multi-visit model with time objective
- [[concepts/payload-induced-drone-battery-consumption-rate]] — the load-dependent energy model used here

## Bibliographic Record

- Citation key: `meng2023multivisit`
- DOI: 10.1016/j.tre.2022.102990
- Canonical URL: https://www.sciencedirect.com/science/article/pii/S1366554522003672
- Publication: Transportation Research Part E: Logistics and Transportation Review, 2023
- Authors: Shanshan Meng, Xiuping Guo, Dong Li, Guoquan Liu
- Metadata companion: [[_papers/meng2023multivisit/meng2023multivisit.md|meng2023multivisit metadata]]

## Sources

- [[_papers/meng2023multivisit/meng2023multivisit-extracted.md]]
- [[_papers/meng2023multivisit/meng2023multivisit.md]]
- [[_papers/meng2023multivisit/images/page_1_image_8.jpg]]
- [[_papers/meng2023multivisit/images/page_4_image_19.jpg]]
- [[_papers/meng2023multivisit/images/page_22_chart_2.jpg]]
- [[_papers/meng2023multivisit/images/page_22_chart_3.jpg]]
