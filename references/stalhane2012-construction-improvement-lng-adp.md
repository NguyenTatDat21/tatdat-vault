---
title: "Stålhane 2012 – Construction and Improvement Heuristic for an LNG Inventory Routing Problem"
category: references
tags: [lng, maritime-inventory-routing, local-search, berth-and-inventory, paper]
aliases:
  - CIH for LNG ADP
  - Stålhane construction improvement heuristic
sources:
  - "[[_papers/stalhane2012construction/stalhane2012construction-extracted.md]]"
  - "[[_papers/stalhane2012construction/stalhane2012construction.md]]"
  - "[[_papers/stalhane2012construction/images/page_6_chart_2.jpg]]"
  - "[[_papers/stalhane2012construction/images/page_8_chart_2.jpg]]"
relationships:
  - target: "[[concepts/annual-lng-delivery-program]]"
    type: extends
  - target: "[[references/rakke2011rolling-rolling-horizon-lng-adp]]"
    type: derived_from
  - target: "[[concepts/maritime-inventory-routing-problem]]"
    type: related_to
  - target: "[[references/halvorsen-weare2013-lng-routing-berth-inventory]]"
    type: related_to
  - target: "[[concepts/iterated-local-search]]"
    type: related_to
summary: "Stålhane et al. (C&IE 2012) build an LNG ADP by a multi-start construction heuristic plus first-improvement local search and a reduced MIP; 20 real instances, average gap 11.58% in 372 s."
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-27
tier: core
created: 2026-10-27T07:50:00Z
updated: 2026-10-30T17:41:00Z
provenance:
  extracted: 0.98
  inferred: 0.02
  ambiguous: 0.00
---

> [!tldr] A deterministic multi-start construction heuristic beats XpressMP on the large, tight-inventory LNG cases
> The CIH builds an annual delivery program day by day with a contract ranking parameter `α`, an inventory control parameter `β` and a look-ahead `κ_g = ⌊(Ī_g − I̲_g)/P_g⌋ + σ_g`, then improves it by first-improvement local search over five operators and by solving a reduced MIP. Average across 20 real instances: CON-LS-3 reaches 11.58% optimality gap in 372.5 CPU s, and all CIH variants beat XpressMP in equal time on every instance except D3 with CON-LS-3.

## The planning setting

- The producer has committed to long-term contracts of 10–25 years, each stating an annual LNG volume and the regasification terminal for delivery, with volumes specified per month or required to be fairly evenly spread over the year.
- Production often exceeds contractual demand, so excess LNG can be sold on the spot market at known prices.
- The fleet is heterogeneous and fixed for the horizon; the producer controls 35 ships, all ships may carry either gas type but only one type at a time, and ships are always fully loaded at the loading port.
- Company practice is to visit only one regasification terminal per voyage; a port stay is approximated as one day for all ships and ports; sailing time of a voyage is known.
- Every ship needs maintenance at least once every fifth year, rule-of-thumb within the last month before the deadline, performed at a drydock along the voyage's sailing lane, and the ship occupies one loading-port berth for one extra day for purge and cool-down.
- Compatibility restrictions limit which ships may visit which terminals, from port acceptance policies and from ships owned by customers.
- Customer-side storage is assumed infinite and customer berthing capacity is not modelled, since the producer is not the sole supplier to many customers.
- The ADP is a complete annual sailing plan of scheduled voyages, each ship typically undertaking 5–30 voyages, and the producer needs a tool that produces good ADPs within 30 minutes for what-if analyses (new contract, production schedule change, chartering out a ship, customer negotiations), which is why the initial ADP should be evenly spread and likely to be accepted.

## Mathematical model

- Sets: gas types `G`, contracts `C`, long-term contracts `C^LT` (each with one defined regasification terminal), artificial spot contracts `C^S` (one per gas type, so spot sales are scheduled as voyages), artificial maintenance contracts `C^M` (one per gas type, to decide which berth type is used for purge and cool-down), ships `V`, ships allowed to serve contract `V_c`, producer-operated ships `V^P`, ships needing maintenance `V^M`, time periods `T`, time intervals `P` with earliest `T̲_p` and latest `T̄_p`, periods of interval `T_p`, ship availability `T_v`, maintenance start windows `T_v^M`.
- Parameters: `T_cv` total voyage time (also the maintenance duration for `C^M`; for spot contracts `T_cv = max_{c'∈C^LT} T_{c'v}` since the spot destination is unknown in advance, which the authors call the most robust choice); `C^T_cv` transport and port cost, including time-charter cost for chartered spot ships; loading capacity `L_v`; berths `B_g` for gas type g; production `P_gt`; storage limits `I_gt` and `Ī_gt`; residual value `R^I_g` of gas left on the last day; spot revenue per unit `R^S_c`; demand `D_cp` per interval, penalty `C^D_cp` for under-delivery.
- Variables: binary `x_cvt` for a scheduled voyage by ship v serving contract c starting on day t (defined only for days the ship is available), inventory `i_gt`, under-delivery `y_cp ≥ 0`.
- Objective (4.1) minimizes transport and port costs + under-delivery penalties − spot revenue − residual inventory value.
- Constraints: (4.2) berths — the maintenance term is shifted by `T_cv + 1` periods because a maintenance voyage occupies a berth after the ship returns; (4.3)–(4.4) inventory balance and limits; (4.5) soft contract demand per interval; (4.6) at most one voyage per ship per day; (4.7) exactly one maintenance per ship in `V^M`; (4.8)–(4.9) domains.
- **Boil-off is pre-calculated**: because of the one-terminal voyage structure, the daily evaporation in ship tanks can be folded into `D_cp`, so boil-off — a major challenge in Grønhaug et al. (2010) — never appears in the model.
- The under-delivery penalty must exceed spot revenue so long-term contracts are served, and the horizon-wide penalty must be much larger than each shorter interval's penalty, to even out deviations over the horizon.
- Feasibility vocabulary used throughout the paper: an ADP is **berth-feasible** if it satisfies (4.2), **inventory-feasible** if it satisfies (4.3)–(4.4), **routing-feasible** if it satisfies (4.6). Time period = one day; intervals = every month plus one interval for the whole horizon.

## Construction heuristic (Algorithm 1, `CreateADP(α, β, κ)`)

- Monthly demand is carried forward: `D*_{c(m+1)} = D_{c(m+1)} + [D*_cm − Σ delivered in month m]`, because every cargo is a full shipload so monthly demands are almost never met exactly and deviations would otherwise accumulate.
- Contract ranking `α` compares two contracts in month m on remaining percentage `ρ_cm`; if `|ρ_{c1m} − ρ_{c2m}| ≤ α` it picks the contract maximizing `ρ_cm · D*_cm` (remaining volume), otherwise the contract with the larger remaining percentage. Monthly demand is used rather than horizon demand so seasonal variations are respected.
- Inventory control `β`: one artificial spot contract per gas type is inserted into the ranked contract set, with demand `β` times the difference between total production and total adjusted contractual demand for the month, so `β` controls inventory at the start of the next month and spreads spot cargoes (only a subset of ships can take spot cargoes, and spreading them avoids chartering extra ships).
- Ship ranking `V_c^Q`: ships in increasing order of the number of contracts they can serve, ties broken by increasing cost-to-capacity ratio, following Ronen (1986), so less flexible and cheaper ships are used first.
- Maintenance rule: a ship cannot be assigned a normal voyage ending after the last day of its maintenance window unless maintenance is already scheduled; once maintenance is scheduled, it is scheduled as early as possible.
- Scheduling step: `T^E = max{T_v^RF, T^IF_cv}` (first routing-feasible day for the ship, first berth- and inventory-feasible day to load the contract's gas); if `T^E ≤ min{t + κ, T̄_m}` the voyage `(c, v, T^E)` is added, `T_v^RF = T^E + T_cv`, and inventory and berth capacities are updated, checking that gas is available on `T^E` and that the tank cannot exceed capacity between `t` and `T^E`.
- Objective (5.2) is the five-term restatement: voyage costs, monthly under-delivery penalties, horizon under-delivery penalty, spot revenue, residual inventory value.

![[_papers/stalhane2012construction/images/page_6_chart_2.jpg]]
*Fig. 2. Flowchart showing the different modules of the CIH and how they interact.*

## Five local-search operators, first improvement

1. **Change contract**: `(c, v, t) → (c′, v, t)`
2. **Change ship**: `(c, v, t) → (c, v′, t)`
3. **Swap contracts**: `(c, v, t), (c′, v′, t′) → (c′, v, t), (c, v′, t′)`
4. **Swap ships**: `(c, v, t), (c′, v′, t′) → (c, v′, t), (c′, v, t′)`
5. **Remove a scheduled voyage**

- Operators are applied in first-improvement fashion until no more improvements are found, so the order in which voyages are tested matters: each operator sorts voyages by contract ranking `C^0_{αβ}` then chronologically, and operator 2 orders ship insertions by `V_c^Q`; every candidate is checked for berth-, inventory- and routing-feasibility.
- Extra spot voyages at the end of the horizon are added by dynamic programming on a multiple-knapsack problem, feasible because only non-polynomial algorithms are known for it and the variable count is small; by construction gas is left in the tanks at the end only if every long-term contract for that gas type is satisfied.

## Reduced MIP heuristic

- Variables are generated only from the input ADP: (5.3) keeps contract and day fixed for each long-term voyage and lets any ship in `V_c` sail it; (5.4) lets spot voyages be re-routed to a long-term contract when profitable; (5.5) generates every maintenance variable, because maintenance affects roughly a fifth of the ships and moving it by a few days can matter greatly. This limits the problem to a very small fraction of its original size.
- Added constraints (5.6) `Σ_{v∈V_c} x_cvt = |S_ct|` for long-term contracts (the number of scheduled voyages stays constant) and (5.7) with `≤` for spot contracts, because variables created by (5.4) sit outside them and the ADP would otherwise become inventory-infeasible.
- Objective (4.1) and constraints (4.2)–(4.7) are kept; (4.8)–(4.9) variable generation is replaced by (5.3)–(5.5). Archetti, Bertazzi, Speranza & Hertz (2011) use a similar approach to improve tabu-search solutions for VRP with inventory constraints, and the same MIP heuristic is part of Rakke et al. (2011)'s rolling horizon heuristic.

![[_papers/stalhane2012construction/images/page_8_chart_2.jpg]]
*Fig. 3. Graph showing the variation in the minimal objective value for each j value, compared to the best found objective value, for each of the four instances.*

## Instances and implementation

- 20 instances from four real cases A–D. A1: 34 ships, 5 LLNG + 3 RLNG contracts, 366 days, 4 LLNG + 1 RLNG berths, I/P 9.21 / 6.17, 310–350 voyages. B1: 16 ships, 1 + 3 contracts, 366 days, 2 + 1 berths, I/P 44.60 / 11.35, 110–140 voyages. C1: 46 ships, 6 + 11 contracts, 365 days, 4 + 1 berths, I/P 6.05 / 6.07, 310–350 voyages. D1: 30 ships, 4 + 4 contracts, 365 days, 4 + 1 berths, I/P 9.08 / 9.37, 200–240 voyages. A1–A5 horizons 366/244/182/121/91 days; B 366/244/182/121/91; C 365/243/181/120/90; D 365/243/181/120/90.
- I/P ratio = storage-tank size ÷ average daily production, the tightness measure taken from Halvorsen-Weare & Fagerholt (2009); case A is tight on RLNG inventory, case C is tight on both gas types, case B has over a month of maneuvering room for LLNG.
- Cases A and B reflect the producer's current situation, C and D a future situation with planned production trains, ships and loading docks completed; C and D have more and larger ships, higher production, less excess LNG, and destinations farther away; B and D are down-scaled versions of A and C. All cases are also used by Rakke et al. (2011).
- Implementation: Java 6.0 in Eclipse Ganymede; the full model and the MIP heuristic in Xpress-IVE 1.19.00 with Xpress-Mosel 2.4.0 solved by Xpress-Optimizer 19.00.00; HP DL160 G5, Intel Xeon QuadCore E5472 3.0 GHz, 16 GB RAM, Linux, single-threaded runs for comparable times.

## Parameters: look-ahead from the I/P ratio

- Parameter testing on instances A3, B3, C3, D3 with `α ∈ [0,1]` step 0.025, `β ∈ [0,1]` step 0.025, `κ ∈ {1,…,31}`; instance C3 proved very sensitive to the look-ahead value.
- Best look-ahead values correspond to the I/P ratio — for A3 (I/P 9.05 and 5.98) the best ADPs came from look-ahead values 4–10 — so look-ahead is set as `κ_g = ⌊(Ī_g − I̲_g)/P_g⌋ + σ_g` with `σ_g ∈ {−5,…,2}`, replacing the single look-ahead in Algorithm 1; the I/P ratio is the number of days before an empty tank fills up, i.e. the frequency at which voyages must be scheduled. Testing gave no clear combination rule, so the same value is used for both gas types.
- Low `β` values are inferior, so `β` is limited to [0.25, 1]: instances with much excess LNG need shipments out to stay inventory-feasible, and instances with little excess LNG are insensitive to `β` because the artificial spot demand is too small to be served. `α` showed no superior range and stays in [0,1].

## Six variants and their results

- CON-LS-1 (parameter granularity 0.1), CON-LS-2 (0.05), CON-LS-3 (0.025), each with `σ ∈ {−5,…,2}`; CON-MIP (construction only, then MIP), CON-LS-1-MIP, CON-LS-2-MIP. Each variant runs all parameter combinations and returns the best ADP.
- Exact method (XpressMP, 24 h = 86,400 s per instance) proved no instance optimal: Table 2 gaps A1 396.64% (UB−LB 54,641 in 1000 USD), C1 7.77% (112,224), D1 8.66% (74,957), C5 0.22% (877), D5 0.47% (1132). Cases A and B show large percentage gaps because spot income is roughly equal to total costs, so objective values sit near zero; A1, the largest percentage gap, is much closer to optimal in absolute value than C1 and C2.
- CON-LS-3 averages 372.5 CPU s, 11.58% gap, UB−LB 13,249; CON-LS-2 98.45 s, 12.87%, 14,591; CON-LS-1 25.6 s, 14.11%, 15,100. CON-LS-3 beats CON-LS-2 in 11 of 20 instances and is on average 1.3 million USD closer to the lower bound, with improvements over 4 million USD on A2, C2, C3.
- MIP tests: CON-MIP average 30.14% / 17,655; CON-LS-1-MIP 10.68% / 12,634; CON-LS-2-MIP 11.17% / 12,084. CON-LS-2-MIP beats LS-only in 12 of 20 instances in equal time, CON-LS-1-MIP in 13 of 20, on different instances. Starting from a better ADP does not guarantee a better MIP result, because CON-LS-1 uses less time and leaves more for branch-and-bound, and a worse starting solution may have more improvement potential — so applying the MIP heuristic to several local minima would likely be better, but is too time-consuming here.
- Table 5 (time for XpressMP to beat the CIH): with the exception of D3 under CON-LS-3, all three CIH variants find better solutions than XpressMP in the same time on all instances; XpressMP beat the CIH on every case-B instance, and could not beat the CIH on the 8- and 12-month instances even after 24 h. Commercial solvers may be preferable on small instances when time is not a constraint.
- Against Rakke et al. (2011)'s rolling horizon heuristic the CIH is much faster, with mixed quality: RHH is better on average for cases A and B, the CIH better for C and D — on average more than 12 million USD better on C and D, about 3 million USD worse on A and B, and more than 60 and 20 million USD better on the largest instances C1 and D1.

## Why the CIH suits a decision support system

- The CIH contains no random components, which the authors call decisive: users unfamiliar with operations research are sceptical of a DSS that gives different results on two runs with the same input. `^[inferred]` This deterministic behaviour is what makes the 30-minute what-if requirement usable in negotiations with customers, where the plan must be both reproducible and evenly spread.
- Conclusions state the CIH creates high-quality solutions to real-world instances in short time, especially for large instances with tightly constrained inventories, and is attractive as a DSS component for testing a new contract, chartering out a ship, or changing the production schedule.
- With far more time, better solutions could be obtained by running the MIP improvement on several instances and adding random components to the construction phase in a GRASP fashion.
- Future work named by the authors: disruption management (ship breakdown, production stop) requiring a new feasible ADP that minimizes customer inconvenience and producer cost, and robustness of an ADP to unforeseen events across a full year.

## Related

- [[concepts/annual-lng-delivery-program]] — the planning object this heuristic produces.
- [[references/rakke2011rolling-rolling-horizon-lng-adp]] — shares the cases, the MIP heuristic, and the head-to-head comparison.
- [[concepts/maritime-inventory-routing-problem]] — the problem class with storage, berth and routing constraints coupled.
- [[references/halvorsen-weare2013-lng-routing-berth-inventory]] — source of the I/P tightness ratio reused for the look-ahead parameter.
- [[concepts/iterated-local-search]] — multi-start with first-improvement local search over a small operator set.

## Limitations

- No instance was proven optimal, so gaps are against a lower bound of unknown quality.
- Customer-side storage and berthing are unmodelled; production rates are fixed except for maintenance-driven variation.
- Only single-threaded runs were used, so the multi-core hardware is not exploited.
- The 13 figure images captured by the extractor have captions in the extracted markdown, so caption-to-image mapping here is unverified; the paper's main text references the tables, not the images.

## Sources

- [[_papers/stalhane2012construction/stalhane2012construction-extracted.md]] — Stålhane, Rakke, Moe, Andersson, Christiansen, Fagerholt, *Computers & Industrial Engineering*, 2012-02-01, DOI 10.1016/j.cie.2011.09.011; zotero-key B37DKVTY.

> [!tldr] A deterministic multi-start construction heuristic beats XpressMP on the large, tight-inventory LNG cases
> The CIH builds an annual delivery program day by day with a contract ranking parameter `α`, an inventory control parameter `β` and a look-ahead `κ_g = ⌊(Ī_g − I̲_g)/P_g⌋ + σ_g`, then improves it by first-improvement local search over five operators and by solving a reduced MIP. Average across 20 real instances: CON-LS-3 reaches 11.58% optimality gap in 372.5 CPU s, and all CIH variants beat XpressMP in equal time on every instance except D3 with CON-LS-3.

## The planning setting

- The producer has committed to long-term contracts of 10–25 years, each stating an annual LNG volume and the regasification terminal for delivery, with volumes specified per month or required to be fairly evenly spread over the year.
- Production often exceeds contractual demand, so excess LNG can be sold on the spot market at known prices.
- The fleet is heterogeneous and fixed for the horizon; the producer controls 35 ships, all ships may carry either gas type but only one type at a time, and ships are always fully loaded at the loading port.
- Company practice is to visit only one regasification terminal per voyage; a port stay is approximated as one day for all ships and ports; sailing time of a voyage is known.
- Every ship needs maintenance at least once every fifth year, rule-of-thumb within the last month before the deadline, performed at a drydock along the voyage's sailing lane, and the ship occupies one loading-port berth for one extra day for purge and cool-down.
- Compatibility restrictions limit which ships may visit which terminals, from port acceptance policies and from ships owned by customers.
- Customer-side storage is assumed infinite and customer berthing capacity is not modelled, since the producer is not the sole supplier to many customers.
- The ADP is a complete annual sailing plan of scheduled voyages, each ship typically undertaking 5–30 voyages, and the producer needs a tool that produces good ADPs within 30 minutes for what-if analyses (new contract, production schedule change, chartering out a ship, customer negotiations), which is why the initial ADP should be evenly spread and likely to be accepted.

## Mathematical model

- Sets: gas types `G`, contracts `C`, long-term contracts `C^LT` (each with one defined regasification terminal), artificial spot contracts `C^S` (one per gas type, so spot sales are scheduled as voyages), artificial maintenance contracts `C^M` (one per gas type, to decide which berth type is used for purge and cool-down), ships `V`, ships allowed to serve contract `V_c`, producer-operated ships `V^P`, ships needing maintenance `V^M`, time periods `T`, time intervals `P` with earliest `T̲_p` and latest `T̄_p`, periods of interval `T_p`, ship availability `T_v`, maintenance start windows `T_v^M`.
- Parameters: `T_cv` total voyage time (also the maintenance duration for `C^M`; for spot contracts `T_cv = max_{c'∈C^LT} T_{c'v}` since the spot destination is unknown in advance, which the authors call the most robust choice); `C^T_cv` transport and port cost, including time-charter cost for chartered spot ships; loading capacity `L_v`; berths `B_g` for gas type g; production `P_gt`; storage limits `I_gt` and `Ī_gt`; residual value `R^I_g` of gas left on the last day; spot revenue per unit `R^S_c`; demand `D_cp` per interval, penalty `C^D_cp` for under-delivery.
- Variables: binary `x_cvt` for a scheduled voyage by ship v serving contract c starting on day t (defined only for days the ship is available), inventory `i_gt`, under-delivery `y_cp ≥ 0`.
- Objective (4.1) minimizes transport and port costs + under-delivery penalties − spot revenue − residual inventory value.
- Constraints: (4.2) berths — the maintenance term is shifted by `T_cv + 1` periods because a maintenance voyage occupies a berth after the ship returns; (4.3)–(4.4) inventory balance and limits; (4.5) soft contract demand per interval; (4.6) at most one voyage per ship per day; (4.7) exactly one maintenance per ship in `V^M`; (4.8)–(4.9) domains.
- **Boil-off is pre-calculated**: because of the one-terminal voyage structure, the daily evaporation in ship tanks can be folded into `D_cp`, so boil-off — a major challenge in Grønhaug et al. (2010) — never appears in the model.
- The under-delivery penalty must exceed spot revenue so long-term contracts are served, and the horizon-wide penalty must be much larger than each shorter interval's penalty, to even out deviations over the horizon.
- Feasibility vocabulary used throughout the paper: an ADP is **berth-feasible** if it satisfies (4.2), **inventory-feasible** if it satisfies (4.3)–(4.4), **routing-feasible** if it satisfies (4.6). Time period = one day; intervals = every month plus one interval for the whole horizon.

## Construction heuristic (Algorithm 1, `CreateADP(α, β, κ)`)

- Monthly demand is carried forward: `D*_{c(m+1)} = D_{c(m+1)} + [D*_cm − Σ delivered in month m]`, because every cargo is a full shipload so monthly demands are almost never met exactly and deviations would otherwise accumulate.
- Contract ranking `α` compares two contracts in month m on remaining percentage `ρ_cm`; if `|ρ_{c1m} − ρ_{c2m}| ≤ α` it picks the contract maximizing `ρ_cm · D*_cm` (remaining volume), otherwise the contract with the larger remaining percentage. Monthly demand is used rather than horizon demand so seasonal variations are respected.
- Inventory control `β`: one artificial spot contract per gas type is inserted into the ranked contract set, with demand `β` times the difference between total production and total adjusted contractual demand for the month, so `β` controls inventory at the start of the next month and spreads spot cargoes (only a subset of ships can take spot cargoes, and spreading them avoids chartering extra ships).
- Ship ranking `V_c^Q`: ships in increasing order of the number of contracts they can serve, ties broken by increasing cost-to-capacity ratio, following Ronen (1986), so less flexible and cheaper ships are used first.
- Maintenance rule: a ship cannot be assigned a normal voyage ending after the last day of its maintenance window unless maintenance is already scheduled; once maintenance is scheduled, it is scheduled as early as possible.
- Scheduling step: `T^E = max{T_v^RF, T^IF_cv}` (first routing-feasible day for the ship, first berth- and inventory-feasible day to load the contract's gas); if `T^E ≤ min{t + κ, T̄_m}` the voyage `(c, v, T^E)` is added, `T_v^RF = T^E + T_cv`, and inventory and berth capacities are updated, checking that gas is available on `T^E` and that the tank cannot exceed capacity between `t` and `T^E`.
- Objective (5.2) is the five-term restatement: voyage costs, monthly under-delivery penalties, horizon under-delivery penalty, spot revenue, residual inventory value.

![[_papers/stalhane2012construction/images/page_6_chart_2.jpg]]
*Fig. 2. Flowchart showing the different modules of the CIH and how they interact.*

## Five local-search operators, first improvement

1. **Change contract**: `(c, v, t) → (c′, v, t)`
2. **Change ship**: `(c, v, t) → (c, v′, t)`
3. **Swap contracts**: `(c, v, t), (c′, v′, t′) → (c′, v, t), (c, v′, t′)`
4. **Swap ships**: `(c, v, t), (c′, v′, t′) → (c, v′, t), (c′, v, t′)`
5. **Remove a scheduled voyage**

- Operators are applied in first-improvement fashion until no more improvements are found, so the order in which voyages are tested matters: each operator sorts voyages by contract ranking `C^0_{αβ}` then chronologically, and operator 2 orders ship insertions by `V_c^Q`; every candidate is checked for berth-, inventory- and routing-feasibility.
- Extra spot voyages at the end of the horizon are added by dynamic programming on a multiple-knapsack problem, feasible because only non-polynomial algorithms are known for it and the variable count is small; by construction gas is left in the tanks at the end only if every long-term contract for that gas type is satisfied.

## Reduced MIP heuristic

- Variables are generated only from the input ADP: (5.3) keeps contract and day fixed for each long-term voyage and lets any ship in `V_c` sail it; (5.4) lets spot voyages be re-routed to a long-term contract when profitable; (5.5) generates every maintenance variable, because maintenance affects roughly a fifth of the ships and moving it by a few days can matter greatly. This limits the problem to a very small fraction of its original size.
- Added constraints (5.6) `Σ_{v∈V_c} x_cvt = |S_ct|` for long-term contracts (the number of scheduled voyages stays constant) and (5.7) with `≤` for spot contracts, because variables created by (5.4) sit outside them and the ADP would otherwise become inventory-infeasible.
- Objective (4.1) and constraints (4.2)–(4.7) are kept; (4.8)–(4.9) variable generation is replaced by (5.3)–(5.5). Archetti, Bertazzi, Speranza & Hertz (2011) use a similar approach to improve tabu-search solutions for VRP with inventory constraints, and the same MIP heuristic is part of Rakke et al. (2011)'s rolling horizon heuristic.

![[_papers/stalhane2012construction/images/page_8_chart_2.jpg]]
*Fig. 3. Graph showing the variation in the minimal objective value for each j value, compared to the best found objective value, for each of the four instances.*

## Instances and implementation

- 20 instances from four real cases A–D. A1: 34 ships, 5 LLNG + 3 RLNG contracts, 366 days, 4 LLNG + 1 RLNG berths, I/P 9.21 / 6.17, 310–350 voyages. B1: 16 ships, 1 + 3 contracts, 366 days, 2 + 1 berths, I/P 44.60 / 11.35, 110–140 voyages. C1: 46 ships, 6 + 11 contracts, 365 days, 4 + 1 berths, I/P 6.05 / 6.07, 310–350 voyages. D1: 30 ships, 4 + 4 contracts, 365 days, 4 + 1 berths, I/P 9.08 / 9.37, 200–240 voyages. A1–A5 horizons 366/244/182/121/91 days; B 366/244/182/121/91; C 365/243/181/120/90; D 365/243/181/120/90.
- I/P ratio = storage-tank size ÷ average daily production, the tightness measure taken from Halvorsen-Weare & Fagerholt (2009); case A is tight on RLNG inventory, case C is tight on both gas types, case B has over a month of maneuvering room for LLNG.
- Cases A and B reflect the producer's current situation, C and D a future situation with planned production trains, ships and loading docks completed; C and D have more and larger ships, higher production, less excess LNG, and destinations farther away; B and D are down-scaled versions of A and C. All cases are also used by Rakke et al. (2011).
- Implementation: Java 6.0 in Eclipse Ganymede; the full model and the MIP heuristic in Xpress-IVE 1.19.00 with Xpress-Mosel 2.4.0 solved by Xpress-Optimizer 19.00.00; HP DL160 G5, Intel Xeon QuadCore E5472 3.0 GHz, 16 GB RAM, Linux, single-threaded runs for comparable times.

## Parameters: look-ahead from the I/P ratio

- Parameter testing on instances A3, B3, C3, D3 with `α ∈ [0,1]` step 0.025, `β ∈ [0,1]` step 0.025, `κ ∈ {1,…,31}`; instance C3 proved very sensitive to the look-ahead value.
- Best look-ahead values correspond to the I/P ratio — for A3 (I/P 9.05 and 5.98) the best ADPs came from look-ahead values 4–10 — so look-ahead is set as `κ_g = ⌊(Ī_g − I̲_g)/P_g⌋ + σ_g` with `σ_g ∈ {−5,…,2}`, replacing the single look-ahead in Algorithm 1; the I/P ratio is the number of days before an empty tank fills up, i.e. the frequency at which voyages must be scheduled. Testing gave no clear combination rule, so the same value is used for both gas types.
- Low `β` values are inferior, so `β` is limited to [0.25, 1]: instances with much excess LNG need shipments out to stay inventory-feasible, and instances with little excess LNG are insensitive to `β` because the artificial spot demand is too small to be served. `α` showed no superior range and stays in [0,1].

## Six variants and their results

- CON-LS-1 (parameter granularity 0.1), CON-LS-2 (0.05), CON-LS-3 (0.025), each with `σ ∈ {−5,…,2}`; CON-MIP (construction only, then MIP), CON-LS-1-MIP, CON-LS-2-MIP. Each variant runs all parameter combinations and returns the best ADP.
- Exact method (XpressMP, 24 h = 86,400 s per instance) proved no instance optimal: Table 2 gaps A1 396.64% (UB−LB 54,641 in 1000 USD), C1 7.77% (112,224), D1 8.66% (74,957), C5 0.22% (877), D5 0.47% (1132). Cases A and B show large percentage gaps because spot income is roughly equal to total costs, so objective values sit near zero; A1, the largest percentage gap, is much closer to optimal in absolute value than C1 and C2.
- CON-LS-3 averages 372.5 CPU s, 11.58% gap, UB−LB 13,249; CON-LS-2 98.45 s, 12.87%, 14,591; CON-LS-1 25.6 s, 14.11%, 15,100. CON-LS-3 beats CON-LS-2 in 11 of 20 instances and is on average 1.3 million USD closer to the lower bound, with improvements over 4 million USD on A2, C2, C3.
- MIP tests: CON-MIP average 30.14% / 17,655; CON-LS-1-MIP 10.68% / 12,634; CON-LS-2-MIP 11.17% / 12,084. CON-LS-2-MIP beats LS-only in 12 of 20 instances in equal time, CON-LS-1-MIP in 13 of 20, on different instances. Starting from a better ADP does not guarantee a better MIP result, because CON-LS-1 uses less time and leaves more for branch-and-bound, and a worse starting solution may have more improvement potential — so applying the MIP heuristic to several local minima would likely be better, but is too time-consuming here.
- Table 5 (time for XpressMP to beat the CIH): with the exception of D3 under CON-LS-3, all three CIH variants find better solutions than XpressMP in the same time on all instances; XpressMP beat the CIH on every case-B instance, and could not beat the CIH on the 8- and 12-month instances even after 24 h. Commercial solvers may be preferable on small instances when time is not a constraint.
- Against Rakke et al. (2011)'s rolling horizon heuristic the CIH is much faster, with mixed quality: RHH is better on average for cases A and B, the CIH better for C and D — on average more than 12 million USD better on C and D, about 3 million USD worse on A and B, and more than 60 and 20 million USD better on the largest instances C1 and D1.

## Why the CIH suits a decision support system

- The CIH contains no random components, which the authors call decisive: users unfamiliar with operations research are sceptical of a DSS that gives different results on two runs with the same input. `^[inferred]` This deterministic behaviour is what makes the 30-minute what-if requirement usable in negotiations with customers, where the plan must be both reproducible and evenly spread.
- Conclusions state the CIH creates high-quality solutions to real-world instances in short time, especially for large instances with tightly constrained inventories, and is attractive as a DSS component for testing a new contract, chartering out a ship, or changing the production schedule.
- With far more time, better solutions could be obtained by running the MIP improvement on several instances and adding random components to the construction phase in a GRASP fashion.
- Future work named by the authors: disruption management (ship breakdown, production stop) requiring a new feasible ADP that minimizes customer inconvenience and producer cost, and robustness of an ADP to unforeseen events across a full year.

## Related

- [[concepts/annual-lng-delivery-program]] — the planning object this heuristic produces.
- [[references/rakke2011rolling-rolling-horizon-lng-adp]] — shares the cases, the MIP heuristic, and the head-to-head comparison.
- [[concepts/maritime-inventory-routing-problem]] — the problem class with storage, berth and routing constraints coupled.
- [[references/halvorsen-weare2013-lng-routing-berth-inventory]] — source of the I/P tightness ratio reused for the look-ahead parameter.
- [[concepts/iterated-local-search]] — multi-start with first-improvement local search over a small operator set.

## Limitations

- No instance was proven optimal, so gaps are against a lower bound of unknown quality.
- Customer-side storage and berthing are unmodelled; production rates are fixed except for maintenance-driven variation.
- Only single-threaded runs were used, so the multi-core hardware is not exploited.
- The 13 figure images captured by the extractor have captions in the extracted markdown, so caption-to-image mapping here is unverified; the paper's main text references the tables, not the images.

## Sources

- [[_papers/stalhane2012construction/stalhane2012construction-extracted.md]] — Stålhane, Rakke, Moe, Andersson, Christiansen, Fagerholt, *Computers & Industrial Engineering*, 2012-02-01, DOI 10.1016/j.cie.2011.09.011; zotero-key B37DKVTY.
