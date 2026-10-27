---
title: "The Orienteering Problem with Drones (Morandi, Leus & Yaman, 2024)"
category: references
tags: [paper, orienteering, truck-drone-routing, milp, exact-algorithm]
relationships:
  - target: "[[concepts/set-orienteering-problem]]"
    type: related_to
  - target: "[[concepts/multiple-flying-sidekicks-traveling-salesman-problem]]"
    type: extends
  - target: "[[references/murray2015flying]]"
    type: derived_from
sources:
  - _papers/morandi2024orienteering/morandi2024orienteering-extracted.md
  - _papers/morandi2024orienteering/morandi2024orienteering.md
  - _papers/morandi2024orienteering/images/page_6_image_0.jpg
  - _papers/morandi2024orienteering/images/page_24_image_0.jpg
  - _papers/morandi2024orienteering/images/page_27_image_0.jpg
summary: >-
  Morandi, Leus & Yaman define the OP-mD (truck + battery-limited drones, prize-collecting) and solve it with a compact MILP, separation scheme, valid inequalities and symmetry breaking.
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-25
tier: supporting
created: 2026-10-25T17:01:33Z
updated: 2026-10-27T06:00:00Z
---

# The Orienteering Problem with Drones (OP-mD)

> [!tldr] A truck collects prizes by visiting customers; m homogeneous battery-limited drones ride with the truck and collect prizes by launching at one customer, serving exactly one drone-only customer, and landing at a different customer where the truck rendezvous and waits; total completion time (truck travel + truck waiting) is capped by T.

## Problem & Contribution

The OP-mD (Orienteering Problem with multiple drones) unifies the prize-collecting orienteering problem with the flying-sidekick drone paradigm^[inferred] (the FSTSP introduced in [[references/murray2015flying]]). It strictly generalizes both: truck-route prizes with per-vehicle budgets like the orienteering problem ([[concepts/set-orienteering-problem]] lineage), and truck-drone synchronization from the FSTSP family, but allows multiple drones, drone prizes distinct from truck prizes, and open truck routes. Node i yields prize p_i if visited by the truck, q_i = β·p_i if served by a drone; q_i < p_i models disaster relief (unreachable victims get reduced credit), q_i > p_i models surveillance.

Contributions: (1) a compact MILP formulation with connectivity constraints lifted by sortie variables; (2) a separation scheme for the exponentially many lifted constraints at fractional and integral solutions; (3) valid, lifted and symmetry-breaking inequalities; (4) an "independent waiting times policy" that strictly enlarges the solution space relative to the FSTSP-with-multiple-drones formulation of Cavani, Iori & Roberti (2021) — their implicit policy forces an early drone to wait for a later drone before taking off;^[inferred] Figure 5 shows an optimal solution infeasible under that policy;^[inferred] an earlier takeoff shortens completion time by two time units.^[inferred]

## Method

Sortie (h_{i,k,j}): drone launches at i, serves one customer k, lands at j ≠ i, requiring ℓ'_{ik} + ℓ'_{kj} ≤ L (drone battery endurance; drone speed α, t'_{ij} = ℓ'_{ij}/α; truck unit speed, Manhattan truck times). Objective:

$$\max \sum_{i \in S_f} p_i + \sum_{h \in H_f} q_h = \sum_{d \in M} \sum_{h \in H} q_h z_h^d + \sum_{i \in N} p_i y_i$$

The core lifted connectivity constraint (10) requires, for every depot-free subset S (2 ≤ |S| ≤ n−2) and k ∈ S:

$$x(N \setminus S, S) \ge y_k + \sum_d z^d(H_{S,k} \cup H_{\cdot,k}^{S})$$

— the truck must enter S through a node visited by a drone serving k. Waiting-time consistency uses big-M constraints W_i ≥ w_i^d. Additional families: sortie incompatibility via the Δ^S_ij slack (constraints (27)-(28), eliminating same-drone sorties sharing truck arcs, see Fig. 3's incompatible-sortie comparison), prefix/suffix bounds (29)-(30), and symmetry breaking by drone flight-time ordering and (33)-(35).^[extracted] Separation: at fractional solutions, support-graph components (Fischetti et al. 1998 style); at integral solutions, checks in the order (30),(29),(28),(27). Compute: Gurobi 9, 1-hour limit, 12-core laptop.^[extracted]

## Results

Instances poi-x-y from the Poikonen-Golden-Wasil (2019) FSTSP benchmark; 1800 instances: N ∈ 10-50, α ∈ {1,2}, β ∈ {0.67,1.00,1.33}, L ∈ {⌊AVG/2⌋, ⌊AVG⌋}, T ∈ TSP/3, 2TSP/3, m ∈ {1,2,3}.^[extracted]

| Group (solved of 120, avg GAP, avg CPU) | m=1 | m=2 | m=3 |
|---|---|---|---|
| N=20, L=⌊AVG/2⌋ (180 per L) | 180 solved, 0.39 s | 180, ~0.5 s | 180, ~0.6 s |
| N=20, L=⌊AVG⌋ (180 per L) | 180, 12.4 s | 180, ~14 s | 180, ~17 s |
| N=30 | 108, GAP 6%, 97 s | 105, 12%, 87 s | 106, 29%, 108 s |
| N=40 | 109, 7%, 154 s | 106, 22.5%, 239 s | 106, 29.5%, 355 s |
| N=50 | 63, 25%, 621 s | 49, 42%, 457 s | 47, 51%, 445 s |

(The N=20 rows aggregate the four α/β/T subgroups with the same L; exact per-subgroup means in Tables 4-5 of the paper.) Headline: 94% of instances up to 40 nodes and 44% of 50-node instances solved within 1 h.^[extracted] The adapted Cavani et al. compact model (MTZ, node copies, poi-7-1 only) solves 40/48 instances in 1 h; the branch-and-cut (with all strengthenings) solves 48/48, all 7-node instances in fractions of a second.^[extracted] Against Cavani et al.'s published FSTSP-with-multiple-drones B&C (2-h single-thread limit, 35% faster CPU): at |N|=20, L/MAX=0.2 both solve 10/10, ours in 1.6-2.7 s vs 4-11 s; at |N|=25, L/MAX=0.4, m=2 Cavani solve 8 instances (GAP 9.6%) vs ours 4 (GAP 8.7%) — caveats on waiting policy, CPU limits, threads and α definition apply.^[extracted]

Figure 1 — feasible OP-mD solution:

![[_papers/morandi2024orienteering/images/page_6_image_0.jpg]]
*Figure 1: A feasible solution for the instance poi-20-1 described in Section 5.1 and the input parameters shown on the right.*

Figure 4 — prize-equal, completion-time-equal optimal solutions differ in truck waiting:

![[_papers/morandi2024orienteering/images/page_24_image_0.jpg]]
*Figure 4: Comparison of two optimal solutions for the instance poi-30-1 described in Section 5.1, with $α=1, β=1.33, L=41, T=86$, and two drones. Only nodes visited by the truck or a drone are shown. Both solutions collect a total prize of 779, but they have different completion and total waiting times (83 and 14, respectively, for the solution on the left, and 85 and 2, respectively, on the right).*

Figure 5 — the independent waiting times policy matters:

![[_papers/morandi2024orienteering/images/page_27_image_0.jpg]]
*Figure 5: An optimal solution for the instance poi-20-1 described in Section 5.1: This solution would be infeasible if we did not adhere to the independent waiting times policy.*

## Limitations

Fractional separation is heuristic-limited by big-M constants;^[inferred] extensions to closed truck walks and multi-customer drone sorties need branch-and-cut-and-price (no efficient pricing exists).^[extracted] Comparison against Cavani et al. is not apples-to-apples (time limits, threads, CPU frequency, α definition).^[ambiguous]

## Related

- [[concepts/multiple-flying-sidekicks-traveling-salesman-problem]] — FSTSP lineage the OP-mD extends to multiple drones and prizes
- [[references/murray2015flying]] — origin of the truck-plus-UAV sortie structure
- [[concepts/set-orienteering-problem]] — prize-collecting routing with per-vehicle budgets
- [[references/murray2020-multiple-flying-sidekicks-tsp]]

## Bibliographic Record

- **Citation key**: morandi2024orienteering
- **DOI**: 10.1287/trsc.2023.0003
- **URL**: https://pubsonline.informs.org/doi/10.1287/trsc.2023.0003
- **Publication**: Transportation Science (INFORMS), 2024-01
- **Authors**: Nicola Morandi; Roel Leus; Hande Yaman
- **Companion metadata**: [[_papers/morandi2024orienteering/morandi2024orienteering.md|morandi2024orienteering metadata]]
- **Instance data**: https://github.com/nm05119/OP-mD (instances, prizes, solutions)

## Sources

- [[_papers/morandi2024orienteering/morandi2024orienteering-extracted.md]]
- [[_papers/morandi2024orienteering/morandi2024orienteering.md]]
- [[_papers/morandi2024orienteering/images/page_6_image_0.jpg]]
- [[_papers/morandi2024orienteering/images/page_24_image_0.jpg]]
- [[_papers/morandi2024orienteering/images/page_27_image_0.jpg]]
