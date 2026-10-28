---
title: "Failure-Directed Search"
category: concepts
tags:
  - failure-directed-search
  - constraint-programming
  - search-strategy
  - iterative-deepening
  - infeasibility-proof
  - scheduling
aliases:
  - FDS
  - plan B search
sources:
  - "[[_papers/vilim2015failuredirected/vilim2015failuredirected-extracted.md]]"
relationships:
  - target: "[[references/vilim2015-failure-directed-search-cp-scheduling]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-search]]"
    type: derived_from
  - target: "[[concepts/variable-neighborhood-search]]"
    type: uses
  - target: "[[references/isik2023-constraint-programming-hybrid-flow-shop]]"
    type: derived_from
summary: "Failure-Directed Search explores by iterative deepening on the quality threshold toward a lower bound, deleting most-likely-to-fail assignments first, restart with nogoods."
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-27
tier: supporting
created: 2026-10-27T09:10:00Z
updated: 2026-10-28T20:35:00+07:00
provenance:
  extracted: 0.90
  inferred: 0.10
  ambiguous: 0.00
---

> [!tldr] Proving that a solution cannot be found is a search strategy in itself
> Failure-Directed Search starts from the assumption that no better solution exists, or that finding one is very hard, so instead of hunting for solutions it systematically explores the space by raising a quality threshold in steps from the incumbent toward a lower bound, and within each threshold eliminates the assignments most likely to fail first. It is a plan B: run it when the neighbourhood search that has been improving the incumbent stops improving.

## Mechanism

- Input: an incumbent solution with objective value `V`, a lower bound `LB`, a step schedule between `V` and `LB`, and a failure budget.
- At each threshold `q` (stepping from `V` toward `LB`), the search asks "is there a solution with quality at least `q`?" and answers by exhausting the space, guided by failure likelihood.
- Failure-likelihood ordering: assignments that most likely lead to failure are tested first, so the cheapest eliminations happen early and a large part of the space is removed cheaply.
- The failure budget is the practical control knob: FDS stops when the budget is exhausted, not when the threshold is proved.
- A "no" answer at threshold `q` is a proof over the explored subspace, so the method produces bounds as well as solutions.
- The variant with the threshold set directly at `LB` and exhaustive enumeration is a complete proof method; the variant that splits the `V`–`LB` range into `k` steps is the search used inside production loops.

## Why it pairs with large neighborhood search

- A neighbourhood search (LNS, VLSN) improves an incumbent by destroying and reconstructing parts of it; it is fast and productive early, then plateaus.
- FDS is triggered when the plateau appears, and continues to produce improvements by proving that whole bands of qualities are unreachable, moving the incumbent down by the proven gap. `^[inferred]` The pairing is complementary in kind, not just in time: LNS searches for existence, FDS searches for non-existence, so the two consume different information and neither is a substitute for the other.
- The published interaction: LNS reaching 142 on a flexible job-shop assembly instance, then 7 FDS steps in 14.9 s taking it to 133, then 30 steps at 10,000 failures taking it to 131, and 60 steps at 10,000 failures taking it to 131; LNS 10,000 iterations in 1.6 s, LNS+FDS-A in 141.7 s to 131, LNS+FDS-B in 131.1 s to 133.
- In CP Optimizer the loop is LNS 20,000 iterations with FDS 100 steps on 32 workers; the FDS iteration time grows with the threshold — 2–3 s, 1–5 s, 10–30 s — so the effort concentrates near the lower bound. `^[inferred]` Escalating per-step time is what makes the failure budget meaningful: a fixed budget buys progressively fewer thresholds as the threshold tightens, so the budget should scale with the distance to the lower bound.
- Time budgets observed: LNS alone 30 min gives 142; LNS + FDS over 2 h 30 min gives 138. `^[inferred]` Extending the budget does not close the gap in a straight line, so FDS should be judged by the bound it proves, not by time-based improvement curves.
- FDS beat dominance-filtering CP on 7 of 70 classical job-shop instances, finding 39 optima in 454,102 s total.

## Uses

- Proving optimality of a neighbourhood-search incumbent.
- Proving infeasibility of a class of solutions (a quality band that cannot be reached).
- Tightening lower bounds in hard instances where a full proof is out of reach.
- Serving as the systematic component of automatic scheduling search in IBM ILOG CPLEX Optimization Studio's CP Optimizer.
- Applying beyond scheduling to any constraint-programming model that supports the search directives.

## Open questions

- How to set the failure budget, the step schedule and the LB so FDS terminates with a proof; the observed cap of 200,000 failures is too small to reach LB 130, ending at 132.
- Whether failure-likelihood ordering generalises outside the scheduling primitives CP Optimizer provides.
- The balance between FDS time and neighbourhood-search time within a fixed total budget.
- How many FDS steps are worth running: 7 steps gave 133 in 14.9 s, 10 steps gave 134 with LB 114, 30 and 60 steps gave 131, 100 steps is the CP Optimizer default.

## Limitations

- FDS assumes the better solution is absent or hard, so it is wasted effort when a good solution is close by.
- A "no" answer is a proof only over the explored subspace, not over the whole model.
- The method inherits CP Optimizer's scheduling primitives; nothing here establishes it for other CP languages.

## Related
- [[references/vilim2015-failure-directed-search-cp-scheduling]] — the paper that defines FDS.
- [[concepts/large-neighborhood-search]] — the plan A strategy FDS complements.
- [[concepts/variable-neighborhood-search]] — neighbourhood search whose incumbent FDS takes over.
- [[concepts/adaptive-large-neighborhood-search-for-mip]] — neighbourhood repair of an MIP incumbent, the same plateau-then-prove pattern.
- [[references/ku2016-mixed-integer-programming-job-shop]] — job-shop scheduling, the classical class FDS solved 39 instances of.
- [[references/isik2023-constraint-programming-hybrid-flow-shop]] — shares constraint-programming + scheduling tags with this page
## Sources

- [[_papers/vilim2015failuredirected/vilim2015failuredirected-extracted.md]] — Vilím, Laborie, Shaw, Michel, *Integration of AI and OR Techniques in Constraint Programming*, 2015, DOI 10.1007/978-3-319-18008-3_30; zotero-key PKMNUUUD.
