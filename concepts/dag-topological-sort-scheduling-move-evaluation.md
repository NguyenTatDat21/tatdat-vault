---
title: >-
  DAG Topological-Sort Move Evaluation for Synchronized Schedules
category: concepts
aliases: [topological order move evaluation, DAG-based schedule repair, insertion cost under synchronization]
tags: [dag, topological-sort, move-evaluation, scheduling, synchronization, large-neighborhood-search, ruin-and-recreate, complexity, heuristic]
relationships:
  - target: "[[references/nguyen2023-pdstsp-collective-drones]]"
    type: derived_from
  - target: "[[concepts/large-neighborhood-search]]"
    type: related_to
  - target: "[[concepts/drone-swarm-synchronization]]"
    type: uses
  - target: "[[concepts/disjunctive-scheduling-constraint-programming-model]]"
    type: related_to
  - target: "[[references/nguyen2022-min-cost-pdsvrp]]"
    type: related_to
  - target: "[[references/montemanni2023-cp-pdsvrp]]"
    type: related_to
sources:
  - _papers/nguyen2023parallel/nguyen2023parallel-extracted.md
  - _papers/nguyen2023parallel/nguyen2023parallel.md
summary: >-
  Represent a synchronized schedule as a DAG, repair arcs on insertion, re-topologically sort in O(|V|+|E|) and replay to get exact makespan cost for every candidate move.
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.00
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-26T05:12:09Z
tier: supporting
created: 2026-10-26T05:12:09Z
updated: 2026-10-26T05:12:09Z
---

# DAG Topological-Sort Move Evaluation for Synchronized Schedules

> [!tldr] When services must be **synchronized** (several vehicles jointly serve one request), a schedule is a directed acyclic graph. Inserting a request into the middle of a tour propagates delays through every downstream tour, so a single-tour insertion cost is not computable in constant time. Fix: keep a DAG per solution, splice arcs around the insertion point, re-topologically sort in $O(|V|+|A|)$, and replay the order to get the exact makespan cost.

## Why constant-time evaluation fails

In a plain single-vehicle tour, inserting a request costs the tour-length delta, computable in $O(1)$. Under synchronization the insertion has a **chain reaction**: the paper's example inserts request 8 into drones 3 and 4 at time $t$, which postpones requests 2, 3, 4, 5 and in turn delays 6 and 7 on drones 1, 2, 5. Constant-time evaluation is available only when the request goes after the last request of a tour. Skipping the evaluation entirely is exactly what the "RnR-fast" variant does, and it costs up to **14.96%** solution quality on large instances, at runtimes below 14 s versus up to 373.43 s for the evaluated version.

## Graph representation

Maintain a per-solution DAG $\bar{\mathcal{G}}=(\bar V,\bar A)$ built from the ordering indicator $y_{ij}$ and the unit-flow $f_{ij}$ of the two-index MILP: vertices are the drone-serviced requests, arcs carry the number of drone units flowing between them. An ordering constraint of the form "start $j$ only after every predecessor $i$ has finished" (a big-$M$ constraint $T_j+M(1-y_{ij})\ge T_i+\tau_j$) is what makes the graph acyclic — no directed cycle is possible.

**Arc surgery at insertion.** For each selected unit $k\in K$, find the precedent $v_j$ and the successive $v_j'$ with $FT(v_j)\le t\le FT(v_j')$ (finish time bracketing the insertion time $t$); delete arc $(v_j,v_j')$, add inbound arc $(v_j,v_i)$ and outbound arc $(v_i,v_j')$. Boundary cases: if no request follows $t$, only the inbound arc is added; if no request precedes $t$, only the outbound arc. ^[inferred]

**Cost computation.** Re-topologically order $\bar{\mathcal{G}}'$ with a DFS-based sort, complexity $O(|\bar V|+|\bar A|)$, then recompute the makespan by inserting requests consecutively in that order.

## Extraction from an MILP solution

Given a feasible $(y,f)$, build $\bar{\mathcal{G}}=(V^*,E^*)$ where $V^*$ is the set of vertices serviced by drones and $E^*$ contains arcs with cost $f_{ij}$; topological order via DFS-based sort; process nodes in that order:

- assigned tours $D_i$ = tours containing any parent $j\in P_i$ (any empty drone when $j=0$);
- start time $t_i=\max_{k\in D_i}\sigma_k$;
- configuration $dc_i$ = the $k$ with $z_i^k=1$;
- append $i$ to each tour in $D_i$ and set $\sigma_k=t_i+\tau_i^{dc_i}$.

Returns complete drone tours plus start times per request. The same routine doubles as the schedule-structure update after a drone removal.

## Pairing with [[concepts/large-neighborhood-search|ruin-and-recreate]] insertion

Candidate start times $F=\{0\}\cup\{$ completion times of serviced requests $\}$; the c-drone size $k$ is drawn uniformly in $[q_i,p_i]$; for each $t\in F$ the $k$ best drones are chosen by **rank-based roulette-wheel selection** (Whitley 1989) to preserve diversity when several drones share the same slack value. The cheap screening estimate of resulting tour time is

$$T_k'=T_k+\max(0,\ \tau_i-\delta(t))$$

where $\delta(t)=ST(j)-t\ge0$ is slack time when $t$ falls in an idle interval before the next request $j$, and $\delta(t)=ST(l)-t<0$ is extra delay when $t$ falls inside an ongoing delivery $l$. The example shows why the estimate matters: a drone with the shortest total service time can be the expensive choice, while a drone with a long total service time is much cheaper thanks to its slack. The accepted move uses the exact makespan from the DAG evaluation, tie-broken by total service time across carriers.

**Block removal as the matching destroy operator.** Dispersed removals leave isolated idle-time gaps that are hard to refill without degrading quality. Sorting drone requests by service start time and removing a contiguous time block (a random interval containing at least $q_d$ services, taken from the start time onward) keeps the repaired region compact — the operators and the evaluation must be designed together. ^[inferred]

**Local search scope.** Composite neighborhood with first-improvement acceptance, using Relocate, Swap and 2-Opt on the truck tour only, because drone-schedule moves are too expensive to use as local-search operators.

## Related

- [[references/nguyen2023-pdstsp-collective-drones]] — Algorithm 1, Section 4.3, and the RnR vs RnR-fast numbers ^[inferred]
- [[concepts/large-neighborhood-search]] — destroy-and-repair family this evaluation serves
- [[concepts/drone-swarm-synchronization]] — the synchronization constraint that creates the DAG
- [[concepts/disjunctive-scheduling-constraint-programming-model]] — the job-shop disjunctive graph that topological replay is standard in
- [[references/nguyen2022-min-cost-pdsvrp]] — source of the sweep removal and the RnR frame
- [[references/montemanni2023-cp-pdsvrp]] — CP route to the same synchronization constraints

## Sources

- [[_papers/nguyen2023parallel/nguyen2023parallel-extracted.md]]
- [[_papers/nguyen2023parallel/nguyen2023parallel.md]]
