---
title: "Vilím 2015 – Failure-Directed Search for Constraint-Based Scheduling"
category: references
tags:
  - failure-directed-search
  - constraint-programming
  - large-neighborhood-search
  - job-shop-scheduling
  - flexible-job-shop
  - cp-optimizer
  - iterative-deepening
  - paper
aliases:
  - FDS for constraint-based scheduling
  - Vilim Laborie Shaw Michel FDS
sources:
  - "[[_papers/vilim2015failuredirected/vilim2015failuredirected-extracted.md]]"
  - "[[_papers/vilim2015failuredirected/vilim2015failuredirected.md]]"
relationships:
  - target: "[[concepts/failure-directed-search]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-search]]"
    type: uses
  - target: "[[references/pisinger2019-large-neighborhood-search]]"
    type: derived_from
summary: "Vilím et al. (CPAIOR 2015) define Failure-Directed Search: iterative deepening on the quality threshold that explores the search space by eliminating the assignments most likely to fail; FDS-B finds 133 in 131 s where LNS alone stalls at 142 for 30 min."
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-27
tier: supporting
created: 2026-10-27T09:05:00Z
updated: 2026-10-27T09:05:00Z
provenance:
  extracted: 0.88
  inferred: 0.12
  ambiguous: 0.00
---

> [!tldr] Plan B for scheduling: enumerate failures when the neighborhood search stalls
> Failure-Directed Search assumes that no better solution exists, or that finding one is very hard, so it explores the search space systematically by raising a quality threshold step by step from the incumbent toward a lower bound, eliminating first the assignments most likely to fail. Paired with Large Neighborhood Search in CP Optimizer, FDS-B on the FSCS instance 33 takes **14.9 s** at 7 steps after LNS reaches 142, and reaches **133** in 131.1 s total where LNS alone reaches 142 in 30 minutes.

## What FDS is

- FDS is the "plan B" strategy used once a less systematic "plan A" — LNS — can no longer improve the incumbent.
- The search proceeds by **iterative deepening on the quality threshold**: from the incumbent objective value toward a lower bound, in steps, checking at each threshold whether a solution at least that good exists; the answer "no" is a proof over the explored subset.
- The order of exploration is by likelihood of failure, not likelihood of success: assignments most likely to fail are eliminated first, which makes proving infeasibility cheap. `^[inferred]` That reframes infeasibility proofs as the productive work of the search: each failure eliminated is a chunk of the space removed, so FDS can be a proof-producing method, not just a search method.
- FDS was designed for the broad scheduling class CP Optimizer supports, and is implemented in IBM ILOG CPLEX Optimization Studio.
- FDS-A enumerates exhaustively with the quality threshold set directly at the lower bound, making it a complete proof method: on FSCS 33 it proved 133 in 420 s with 140,000 failures.
- FDS-B splits the range into 7 steps (142, 141, …, 136) and spent 14.9 s with 633,800 failures, producing the same 133 with 17 failures found per step.
- The failure budget is the practical control: with a cap of 200,000 failures at LB 130, the loop ended at 132; 200,000 is too small to reach the LB.
- FDS-B with 10 steps and LB 114 improved LNS to 134.
- FDS-A has two uses: proving optimality of an LNS incumbent, and proving infeasibility of a class of solutions.

## The scheduling problem FDS targets

- FSCS extends flexible job shop scheduling with sequence-dependent setup times, time lags, and optional activities (a job in FSCS is a full assembly with alternatives, each consisting of activities with setup times). It covers job shop, flexible job shop, RCPSP, RCPSP/max, multi-mode RCPSP, multi-mode RCPSP/max, simple assembly line scheduling, parallel assembly with product variants, planning and scheduling.
- Jobs are defined in a disjunctive graph; the incumbent in the paper was produced by LNS with 1,500 CPU cores and 57,338,000 iterations (10,000 iterations in 200 CPU ms), value 154, LB 114, with a gap of 40 time units.
- 17 improvements from 154 were achieved and 11 new bests obtained, including 5 new lower bounds.
- FDS improved 23 FSCS instances in 30 min, finding new optima on FSCS 1, 4, 7, 11, 27, 28, 31, 34, 36 (with 134 on 34, 36); the FDS-optimized solution on 33 is 133.

## Search loop and parameters

- CP Optimizer 12.4, 32 workers, LNS 20,000 iterations, FDS 100 steps.
- FDS runs inside the LNS loop, triggered when LNS stops improving: a full FDS iteration on 33 takes 2–3 s, 1–5 s, 10–30 s as the threshold tightens. `^[inferred]` The escalation in time per step is the signature of iterative deepening: cheap thresholds are disposed of quickly, and the work concentrates on the last few thresholds near the LB.
- FDS-B steps use the objective values between the incumbent and the LB, so the number of steps is the resolution of the threshold ladder.
- FDS-B at 10 steps with LB 114 reached 134; FDS-A with LB 130 ended at 132; LNS alone for 30 min reached 142, LNS+FDS for 2 h 30 min reached 138.
- FDS-A is a complete proof method when the threshold is set at the LB. `^[inferred]` The FDS-A/FDS-B trade-off reads as completeness versus time: FDS-A proves (133 in 420 s on 33), FDS-B is the search used in production LNS loops, where 30 steps at 10,000 failures and 60 steps at 10,000 failures each yielded 131.

## Results in numbers

- FDS-B 7 steps, 14.9 s, 633,800 failures on FSCS 33, from LNS 142 to 133.
- FDS-A, threshold 133, 420 s, 140,000 failures, proving 133 optimal on 33.
- LNS 10,000 iterations in 1.6 s; LNS+FDS-A 141.7 s to 131; LNS+FDS-B 131.1 s to 133.
- 10,000 iterations in 200 CPU ms.
- 30,000 failures in 300 s.
- 420 s, 58,395 failures, 133, 4,000 failures per step.
- 623,000 failures in 610 s.
- 36,000 failures in 20 min, 36,000 per step.
- LNS 20,000 iterations, FDS 10 steps, LB 114, LNS alone 142, LNS+FDS 134, 2h30, 138.
- FDS 36,000 failures in 20 min, 36,000 per step, 200,000, 132, LB 130.
- On 81 classical JSSPs FDS found 39 optima, dominance filtering 32, total time 454,102 s. `^[inferred]` FDS winning 7 of the 70 JSSP head-to-heads shows the enumeration-by-failure order transfers beyond FSCS.
- 14 improvements, 18 new bests, 54,353,000 iterations, 100,000 failures.
- 12,341,000 iterations, 200,000 failures, 136, 2,152 failures, 660 s.
- 33,219,000 iterations, 10,000 failures, 132.
- 131, 12,341,000, 10,000, 10,000, 142, 131.

## Related
- [[concepts/failure-directed-search]] — the algorithm class this paper defines.
- [[concepts/large-neighborhood-search]] — the plan A strategy FDS supplements.
- [[references/pisinger2019-large-neighborhood-search]] — the LNS/ALNS chapter collection this CP search is derived from.
- [[references/ropke2006-adaptive-large-neighborhood-search-pdptw]] — adaptive destroy-and-repair, the same plateau-then-search pattern.
- [[references/ku2016-mixed-integer-programming-job-shop]] — job-shop scheduling as an MIP, the problem class FSCS extends.
## Sources

- [[_papers/vilim2015failuredirected/vilim2015failuredirected-extracted.md]] — Vilím, Laborie, Shaw, Michel, *Integration of AI and OR Techniques in Constraint Programming*, 2015, DOI 10.1007/978-3-319-18008-3_30; zotero-key PKMNUUUD.
