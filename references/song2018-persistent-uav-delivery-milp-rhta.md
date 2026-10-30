---
title: "Song 2018 – Persistent UAV Delivery Logistics: MILP and Receding Horizon Task Assignment"
category: references
tags: [drones, drone-routing, milp, heuristics, time-windows]
aliases:
  - Persistent UAV logistics RHTA
  - UAVRP
sources:
  - "[[_papers/song2018persistent/song2018persistent-extracted.md]]"
  - "[[_papers/song2018persistent/song2018persistent.md]]"
  - "[[_papers/song2018persistent/images/page_7_image_2.jpg]]"
  - "[[_papers/song2018persistent/images/page_10_chart_2.jpg]]"
relationships:
  - target: "[[concepts/payload-induced-drone-battery-consumption-rate]]"
    type: related_to
  - target: "[[concepts/cooperative-multi-agent-uav-routing]]"
    type: related_to
  - target: "[[concepts/set-team-orienteering-problem-with-time-windows]]"
    type: derived_from
  - target: "[[concepts/min-cost-parallel-drone-scheduling-vrp]]"
    type: extends
summary: "Song et al. (C&IE 2018) model persistent UAV delivery with payload-weighted flight time; CPLEX fails at 15 tasks, RHTA solves 40 cases in under 0.4 s with 0.175–2.252% loss."
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-27
tier: supporting
created: 2026-10-27T07:35:00Z
updated: 2026-10-30T17:41:00Z
provenance:
  extracted: 1.00
  inferred: 0.00
  ambiguous: 0.00
---

> [!tldr] Payload weight is a flight-time multiplier, and a petal heuristic fixes CPLEX's collapse
> The MILP maximizes `w1·w2·Σ Y_ikr − (1−w1)·Σ D_ij·X_ikr` with the flight time from i to j weighted by `f_ijk(N_ikr) = 1 + (Ul−1)/C_k · N_ikr`. On the island example CPLEX returns optimal 8535.3 with 4647 m of travel covering all 10 tasks; at 15 tasks CPLEX runs out of memory in 8 of 10 cases, while the RHTA heuristic solves all 40 cases in under 0.4 seconds with 0.175%, 2.224% and 2.252% average loss for 5, 10 and 15 tasks.

## Three UAV constraints that ground VRP does not have

- Commercial UAVs are limited in flight duration and loadable capacity, so they cannot serve long-duration delivery without replenishing battery charge **and** delivery products at stations.
- Flight time depends delicately on the amount of loaded product, so the weight–flight-time relation must be in the model (Mikrokopter 2017 reports flight time decreasing roughly linearly as payload rises).
- UAVs must not sit on the ground between tasks — idle time risks loss or damage — so they keep flying between a take-off and a landing at a designated station.
- UAVs share multiple service stations distributed in the field, visiting any station to recharge and reload, which is what makes the service *persistent*.

## Model

- Each station carries two indices: `Q_SS = {N_J+1, N_J+3, …, N_J+2·N_STA−1}` for flight-start stations and `Q_SE = {N_J+2, N_J+4, …, N_J+2·N_STA}` for flight-end stations; `Ω_A = Ω_J ∪ Q_SS ∪ Q_SE`. Recharge/reload time `P_i` at a station is constant, assumed independent of remaining consumables on arrival.
- Decision variables: `X_ikr` (arc from task/station i to j by UAV k on its r-th flight), `Y_ikr` (task i assigned), `C_ikr` (start time), `N_ikr` (loaded product remaining after task i, integer, upper bounded by `C_k`).
- Objective (2) balances covered tasks against total traveling distance with `w1` and a scaling factor `w2`.
- Constraint structure: (3) each UAV starts its first flight at its initial station; (4)–(5) every flight starts at a start-station index and ends at an end-station index; (6) if flight r ends at station s, flight r+1 starts at index s−1; (7) a flight cannot end at a task; (8) a flight cannot end at a start-station index; (9) per-task assignment ≤ 1, so unserved tasks are allowed, and idle UAVs are forced to stay at a station; (10) flight r's finish time equals flight r+1's start time; (11) task start times with the weighted flight time; (12) each flight finishes within `Q_k`, which forces UAVs to keep flying during service; (13)–(15) linking, zero-value handling and the time window `E_i ≤ C_ikr ≤ L_i`; (16) assigned demand ≤ `C_k`; (17) load at the start station equals the flight's total assigned demand; (18) `N_ikr` decreases as deliveries proceed; (19)–(22) domain declarations.
- NP-hardness: the problem reduces to the multi-depot VRP with time windows by four successive reductions — remove fuel restrictions, remove the payload effect on flight time, set `N_R = 1` for every UAV, and forbid station sharing so each UAV has a single home depot.

## RHTA heuristic

- Five steps: enumerate every feasible petal per UAV (a sequence of tasks the UAV can serve and still return to a station) and its travel distance; solve a MILP (23)–(24) selecting one petal per UAV, maximizing the same weighted objective subject to each task in the list being selected at most once; assign each UAV's first selected task and update charge, load and location; send charge- or product-insufficient UAVs to a station and repeat while tasks remain; park any UAV not at a station.
- RHTA was introduced by Alighanbari (2004) for UAV scheduling, used by Kim & Morrison (2014) to co-design a UAV system and schedule, by Song et al. (2016) for any fleet status enabling real-time dynamic scheduling, and by Lee & Morrison (2015) for search-area and tracking tasks — all for patrolling, not delivery.
- Because the petal enumeration carries the nonlinear weight function, the heuristic can use any nonlinear flight-time function that the full MILP would struggle to encode.

![[_papers/song2018persistent/images/page_7_image_2.jpg]]
*Figure 4. UAV logistics system*

![[_papers/song2018persistent/images/page_10_chart_2.jpg]]
*Figure 3. Linear weight function imposed on flight time* (extracted label keeps the paper's numbering slip: the weight-function figure is labelled "Figure 3", the layout figure "Figure 4")

## Island experiment

- Two stations at (832, 317, 85) and (666, 59, 0), three UAVs at each; station service time 5 minutes; `N_R = 5`, `w1 = 0.9`, `w2 = 1000` in every experiment, set so that serving more customers outweighs minimizing distance.
- Six UAVs, speeds 180 / 150 / 120, `Q_k` = 40 / 30 / 20 min, `C_k` = 8 units each. Island A's demand exceeds one UAV's capacity, so its task is split into two tasks sharing location and time constraint.
- Optimal objective **8535.3** with travel distance **4647 m** and all 10 tasks covered: UAV 1 `Station 1→3→8→Station 1`, UAV 2 `Station 1→6→9→10→Station 1`, UAV 4 `Station 2→1→4→7→Station 2`, UAV 5 `Station 2→2→5→Station 2`; UAVs 3 and 6 unused. Island A is served jointly by UAVs 1 and 5.
- Hardware and software: Intel Core i7-3770 at 3.40 GHz with 4.00 GB RAM, ILOG CPLEX 12.6.2, NetBeans IDE 8.0 with JDK 1.8, 40 cases with 5, 10, 15 and 30 tasks, 3 stations, 6 UAVs.
- CPLEX CPU time runs from 0.72–1.95 s at 5 tasks to 40.78–748.06 s at 10 tasks, 4587 s and 5107.31 s for the two solvable 15-task cases, and out-of-memory failures in 8 of 10 15-task cases (best feasible solutions marked `*`; experiment 27 and every 30-task case give CPLEX no feasible solution at all).
- RHTA times: 0.092–0.096 s (5 tasks), 0.106–0.288 s (10), 0.121–0.312 s (15), 0.135–0.325 s (30) — under 0.4 s in every case, with gaps 0.175%, 2.224%, 2.252% average for 5, 10, 15 tasks; individual 15-task gaps range 0.295% to 5.178%.
- The authors place this against Gendreau et al. (2002): "Typically, classical methods yield solution values between 2% and 10% above the optimum (or the best known solution value), while the best metaheuristic implementation is often less than 0.5%", and note RHTA is a classical heuristic (petal-based), so its speed suits real-time UAV operation.

## Related

- [[concepts/payload-induced-drone-battery-consumption-rate]] — the linear payload weight on flight time is this paper's central modelling assumption.
- [[concepts/cooperative-multi-agent-uav-routing]] — cooperating UAVs that share stations for recharge and reload.
- [[concepts/set-team-orienteering-problem-with-time-windows]] — the time-window task-selection pattern RHTA's petal enumeration inherits.
- [[concepts/min-cost-parallel-drone-scheduling-vrp]] — parallel scheduling under per-vehicle cost and budget limits, the same shape as the RHTA petal MILP.

## Limitations

- 30-task cases have no CPLEX optimum, so the 30-task RHTA results (8028.5–22933.1) have no published gap.
- Demand exceeding capacity is handled by splitting a task, and the model assumes recharge time is independent of remaining consumables.
- Only the 10-task island instance is reported with schedules; the 40-case study reports objective values, not routes.

## Sources

- [[_papers/song2018persistent/song2018persistent-extracted.md]] — Song, Park, Kim, *Computers & Industrial Engineering*, accepted 2018-05-08 (received 2017-02-16, revised 2018-01-03), PII S0360-8352(18)30214-6, DOI 10.1016/j.cie.2018.05.013, reference CAIE 5219; accepted-manuscript version. zotero-key B8C2C5YV.
