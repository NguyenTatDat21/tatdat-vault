---
title: "Zhao 2025 – Large Neighborhood and Hybrid Genetic Search for Inventory Routing"
category: references
tags:
  - inventory-routing
  - large-neighborhood-search
  - dynamic-programming
  - hybrid-genetic-search
  - stock-out-penalty
  - benchmarks
  - paper
aliases:
  - HGS-IRP
sources:
  - "[[_papers/zhao2025large/zhao2025large-extracted.md]]"
  - "[[_papers/zhao2025large/zhao2025large.md]]"
  - "[[_papers/zhao2025large/images/page_22_chart_3.jpg]]"
  - "[[_papers/zhao2025large/images/page_24_chart_2.jpg]]"
relationships:
  - target: "[[concepts/large-neighborhood-search]]"
    type: uses
  - target: "[[concepts/maritime-inventory-routing-problem]]"
    type: related_to
  - target: "[[concepts/adaptive-large-neighborhood-search-for-mip]]"
    type: related_to
  - target: "[[references/goel2012-large-neighborhood-search-lng-inventory-routing]]"
    type: related_to
summary: "Zhao, Archetti, Pham & Vidal (EJOR 2025): DP operator reinserts all visits to one retailer across the horizon. HGS-IRP sets 365 new bests on 1,040 benchmarks and improves 191 of 270 SAHS instances by 18.21 on average."
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-27
tier: supporting
created: 2026-10-27T07:10:00Z
updated: 2026-10-27T07:10:00Z
provenance:
  extracted: 0.96
  inferred: 0.04
  ambiguous: 0.00
---

> [!tldr] One operator, whole-horizon reinsertion
> The delivery-schedule (DS) operator removes **every** visit to one retailer across the planning horizon and reoptimizes visit days and quantities by dynamic programming, jointly accounting for routing and inventory cost. Inside Hybrid Genetic Search it produced 365 new best-known solutions on 1,040 benchmark instances, and improved the best known solution on 191 of 270 hard instances by 18.21 on average.

## Model

- Multi-day IRP: choose delivery quantities per retailer per day and vehicle routes per day. Cost = supplier holding + retailer holding + stock-out penalty `ρ h_i B_i^t` + transportation.
- Stock-out-allowed (SOA) model with no backlogging: unmet demand is lost, not deferred — the authors' rationale is fast-moving consumer goods, pharmaceuticals and seasonal delivery, where lost sales are the real outcome.
- Extends the Archetti et al. (2007) formulation with `B_i^t` and the penalty term.

## The DS operator

- Removes all visits to a chosen retailer, then computes the optimal delivery schedule for that retailer over the whole horizon, minimizing routing plus inventory cost.
- Implementation: DP over piecewise-linear cost-to-go functions `C_t`, with preprocessing of `F_t(q_i^t)` and acceleration. Worst case `O(U_i K H)` per retailer; the most expensive step is the convolution of `C_{t-1}` and `F_t`, `O(U_i K)`.
- Two mechanisms keep the piece count small in practice: **range-based pruning** (drop segments outside `[0, U_i − d_i^t]` and segments covering no integer inventory) and **optimality-based merging** (keep only the cheapest segment per interval). On a 50-customer, high-holding-cost instance with `K = 5`, `H = 10` and `U_i` between 22 and 294, piece counts rise early and then stabilize or fall.
- The operator is metaheuristic-independent — it needs only an incumbent solution — so the authors note it can be embedded in ILS, adaptive LNS, or other frameworks, and it computes reinsertion schedules in microseconds. ^[inferred]

![[_papers/zhao2025large/images/page_22_chart_3.jpg]]
*Figure 6 Boxplots of the number of pieces in $C_t$ from Day 1 to Day 10. Each box represents the distribution across different instances. The box spans from the 25th to the 75th percentile, with the median shown as a horizontal line.*

## Results

- Stopping criteria: 100,000 iterations, 10,000 iterations without improvement, or 2,400 s (small) / 7,200 s (large and SAHS). Single Intel Xeon Gold 6336Y core; code and solutions at github.com/vidalt/HGS-IRP/.
- Benchmarks: Archetti et al. (2007) small set (800 instances, H = 3 or 6, n from 10 to 50, K 2–5, low and high inventory cost) and Archetti et al. (2012) large set (240 instances, H = 6, n ∈ {50, 100, 200}).
- Against CCJ (Chitsaz et al. 2019 decomposition matheuristic), KS (Archetti et al. 2021 kernel search) and BCHeu (Skålnes et al. 2023, DIMACS 2022 IRP winner): average gap to BKS **−0.15%** for HGS-IRP vs 0.17% BCHeu, 2.66% KS, 2.84% CCJ; average time 1,989.4 s vs 7,200.0 s for BCHeu.
- 768 instances reach the best-known value, 365 of them new: 187 new on the 800 small instances, 178 new on the 240 large ones; on the small 3-day set 37 new, 320 matched, 43 slightly worse; on the small 6-day set 150 new and 83 matched.
- SAHS instances (Skålnes et al. 2024, n 10–200, H 6/9/12, multi-type fleet with 8, 18, 38 EUR-pallet capacities, variable demand): best known improved on 191 of 270, matched on 25, average improvement 18.21 within the same two-hour limit. At n = 100 the branch-and-cut gap is 101.61% while HGS-IRP is 31.94% below the previous BKS.
- Stock-out penalties `ρ = 50, 100, 300, 1,000,000`: higher ρ raises cost and runtime; on the tested instance no stock-out occurs once ρ exceeds 91, so every ρ ≥ 92 gives the same plan.

![[_papers/zhao2025large/images/page_24_chart_2.jpg]]
*Figure 7 Trade-off between stock-out amount and routing/inventory cost for a specific instance (15 customers and 5 vehicles) under varying stock-out penalties ρ, which varies from 1 to 300 in integer increments.*

## Related

- [[concepts/large-neighborhood-search]] — the DS operator is a destroy-and-repair neighbourhood, with the repair solved exactly by DP.
- [[concepts/maritime-inventory-routing-problem]] — same inventory-and-routing coupling, with multi-day cost trade-offs instead of vessel constraints.
- [[concepts/adaptive-large-neighborhood-search-for-mip]] — the authors name adaptive LNS as a natural host framework for this operator.
- [[references/goel2012-large-neighborhood-search-lng-inventory-routing]] — earlier LNS for inventory routing, with ship-pair destruction rather than whole-horizon reinsertion.

## Limitations

- No standard benchmark exists for the stock-out-allowed variant; results come from modified small and large IRP sets.
- Deterministic demand and travel; the authors point to two-stage stochastic and dynamic IRP as the open direction.
- Captions are quoted from extracted markdown; the model cannot inspect images, so figure mapping follows extractor label order.

## Sources

- [[_papers/zhao2025large/zhao2025large-extracted.md]] — Zhao, Archetti, Pham & Vidal, *European Journal of Operational Research*, received 2025-05-27, accepted 2025-11-14, zotero-key D29BZRNE, DOI 10.1016/j.ejor.2025.11.021.
