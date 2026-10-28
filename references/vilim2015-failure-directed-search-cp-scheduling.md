---
title: "Failure-Directed Search for Constraint-Based Scheduling (Vilím, Laborie, Shaw, Michel 2015)"
category: references
tags:
  - paper
  - constraint-programming
  - search
  - scheduling
  - job-shop
  - rcpSP
  - CP-optimizer
aliases:
  - FDS paper
  - Vilím 2015
sources:
  - "[[_papers/vilim2015failuredirected/vilim2015failuredirected-extracted.md]]"
  - "[[_papers/vilim2015failuredirected/vilim2015failuredirected.md]]"
  - "[[_papers/vilim2015failuredirected/images/page_4_image_1.jpg]]"
  - "[[_papers/vilim2015failuredirected/images/page_6_image_0.jpg]]"
  - "[[_papers/vilim2015failuredirected/images/page_8_image_0.jpg]]"
  - "[[_papers/vilim2015failuredirected/images/page_14_image_5.jpg]]"
relationships:
  - target: "[[concepts/failure-directed-search]]"
    type: defines
  - target: "[[concepts/large-neighborhood-search]]"
    type: related_to
  - target: "[[concepts/disjunctive-scheduling-constraint-programming-model]]"
    type: uses
summary: "Vilím et al. (CPAIOR 2015): branch on domain splits by failure likelihood, restart with nogoods, LNS as plan B; closed 535 of 552 open Multi-Mode RCPSP j30."
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-27
tier: supporting
created: 2026-10-27T10:20:00Z
updated: 2026-10-28T20:35:00+07:00
provenance:
  extracted: 1.00
  inferred: 0.00
  ambiguous: 0.00
---

# Failure-Directed Search for Constraint-Based Scheduling (Vilím, Laborie, Shaw, Michel 2015)

> [!tldr] The paper that made FDS part of a production solver
> Petr Vilím, Philippe Laborie, Paul Shaw and Laurent Michel, *Integration of AI and OR Techniques in Constraint Programming* (CPAIOR) 2015, DOI 10.1007/978-3-319-18008-3_30 (Zotero key `PKMNUUUD`). FDS assumes a better solution is absent or very hard to find, so it explores the space systematically by eliminating the assignments most likely to fail first, as the "plan B" after Large Neighborhood Search stops improving. FDS has been an integral part of the CP Optimizer automatic search since version 12.6.0.

## Mechanism: choices, not variables

- FDS does not branch on decision variables directly; it works on a set of **binary choices**, an abstraction of anything that must be decided to reach a solution.
- Branching uses **domain splitting**: a domain is split into two disjoint intervals so that one bound of the domain always changes. The paper motivates this from a scheduling-specific obstacle — the usual `x = n ∨ x ≠ n` branching rarely propagates, because most scheduling propagation (temporal constraint networks, timetable, edge-finding for unary and discrete cumulative resources) only uses domain minima and maxima.
- **Presence choice**: for an interval variable `v`, is `v` present (`⊥ ∉ D_v`) or absent (`D_v = {⊥}`)? Used only for optional interval variables.
- **Start time choice**: for a present interval variable `v` and a time `t`, is `startOf(v) ≤ t` or `startOf(v) > t`? Applied only once `v` is present, so a presence choice must be applied first.
- At the top level FDS "knows only a set of choices that needs to be decided: it is ignorant of what the choices are doing."
- The first-fail principle is applied to **branch ordering** as well: from the two branches of a choice, the one that fails most is explored first.

## Node types and ratings

![[_papers/vilim2015failuredirected/images/page_4_image_1.jpg]]
*Fig. 1. Types of internal nodes*

- **0-fails**: neither branch fails — the number of open branches grows, a disappointment to the tree builder, but unavoidable near the root.
- **2-fails**: both branches fail; the choice is a **closing choice**, the best outcome, and a search tree cannot be fully explored without closing choices.
- **1-fail**: one branch fails; the branch is not closed, but no new branch is opened, and propagation tightened bounds, improving the odds of closing it later.
- Ratings: for each available choice `c`, `rating⁺[c]` and `rating⁻[c]` are both initialised to 1.0, and `rating[c] = rating⁺[c] + rating⁻[c]` (equation 1); smaller ratings are preferred, and the algorithm picks the available choice with the best rating. Each depth `d` carries an `avgRating[d]`, also initialised to 1.0.
- Impact-based search estimates the reduction in search effort as `R = (|D'_{x1}| × … × |D'_{xn}|)/(|D_{x1}| × … × |D_{xn}|)`; FDS uses the same `R` inside `localRating := 0` if the branch fails immediately, else `1 + R` (equation 2) — the paper notes this places much greater emphasis on failures than impact-based search, making FDS far more aggressive in seeking immediate failures.
- `localRating` is normalised by depth: `rating⁺/⁻[c] := α · rating⁺/⁻[c] + (1 − α) · localRating / avgRating[d]` (equation 3), with `α` controlling decay; typical `α` values range from 0.9 to 0.99. Because ratings decay by `α`, they reflect recent behaviour, and can move quickly when closing decisions appear.

## Choice states and the search procedure

![[_papers/vilim2015failuredirected/images/page_6_image_0.jpg]]
*Fig. 2. Choice states and data structures*

- **Unchecked**: not picked for branching in the current branch; all choices start unchecked, stored in a heap giving fast access to the best rating.
- **Decided**: picked, found applicable, one branch applied; kept on a stack to make backtracking fast, until the search backtracks past the decision.
- **Resolved**: picked, found already resolved — for example the choice `startOf(v) ≤ 5` versus `startOf(v) > 5` when `startOf(v)` is already known inside `[7, 12]`; kept on the stack until the search backtracks above the point where it was found resolved.
- **Waiting**: a choice that cannot split `v`'s domain into two disjoint subsets because `v` absent is possible in both branches, so the choice is applied only when `v` is present; it monitors `v`'s status, and when `v` becomes present the choice returns to the heap as unchecked.
- Algorithm 1: take the best-rated choice from the heap; skip it if waiting (let it monitor its interval variable) and take another; add it to the stack; skip it if resolved; apply the branch with the better rating; propagate to a fixed point; update the branch rating; if the subproblem is not infeasible pick again. On a dead end, backtrack: find the last choice on the stack with an open branch, return all choices above it to the heap, apply the unexplored branch, propagate. If the heap is empty, a solution is found: add an improving objective cut and go to backtrack. If no choice with an open branch exists, terminate — the whole search space was explored.

![[_papers/vilim2015failuredirected/images/page_8_image_0.jpg]]
*Fig. 3. Consider present interval variable v with duration p_v, earliest starting time est_v and latest completion time lct_v. If lct_v − est_v < 2p_v then v always occupies interval [lct_v − p_v, est_v + p_v]. This interval is called mandatory part.*

- The initial choice set need not be complete. Inspired by square-packing search, the initial set only guarantees that if all choices are decided, every interval variable is absent or has a **mandatory part**; when all choices are decided but variables remain unfixed, the search completes with a traditional depth-first approach or generates more choices at that point.
- **Restarts and nogoods**: the search restarts for the first time after 100 backtracks, and the restart limit grows by 15% after each restart (the CP Optimizer defaults `RestartFailLimit` and `RestartGrowthFactor`). Nogoods from restarts are recorded and propagated in the same way as for integer search inside CP Optimizer. FDS assumes it will be restarted many times, and the only thing that survives a restart is the set of nogoods — shorter nogoods are easier to apply, which is why FDS explores the branch most likely to fail first.
- **Strong branching and shaving**: ratings are estimates, and they are most imprecise exactly where choices matter most, at the top of the tree. At the root of each restart FDS pre-evaluates a limited number of the best applicable choices by trying both branches, updates their ratings, then branches on the choice with the best `localRating` from equation 2. If an evaluated choice has an infeasible branch, the opposite branch is applied immediately and the pre-evaluation continues with the reduced set — the same effect shaving aims for, and the analogue of strong branching in MIP solvers. If propagation moves a variable in the same direction in both branches (e.g. minimum start time raised from 0 to 7 in one, to 10 in the other), the smaller change is applied at once.

## Coupling with LNS

FDS finds solutions only "by a happy accident", so it suits the infeasible-or-hard case; with many easy solutions it may not work well. The production pairing is therefore plan A = self-adapting Large Neighborhood Search (Laborie & Godard 2007) — continual relaxation and re-optimization of a first solution, portfolios of large neighborhoods and completion strategies, machine learning to converge on the best neighborhoods, and linear-relaxation-guided completion strategies for non-regular objectives such as earliness costs — with FDS as plan B once LNS can no longer improve.

## Results on open benchmarks

Machine: Intel Core i7 2.60 GHz (4 cores, hyperthreading), 16 GB RAM, IBM ILOG CP Optimizer 12.6.1 with minor performance improvements. Two configurations: **LNS+FDS** (standard automatic search, `Workers=2`, `FailureDirectedSearchEmphasis=0.99`; both threads start in LNS, and when LNS stops improving for a time determined by auto-tuning, one thread switches to FDS) and **DestructLB** (one thread, FDS started immediately, proving best-known lower bounds wrong iteratively; the per-iteration time limit is the benchmark limit, total time unlimited, and the current best lower bound is confirmed before any improvement attempt). Version 12.6.1 has no public API to run FDS directly. Detailed results at http://ibm.biz/FDSearch.

| Benchmark | Open instances | Lower-bound improvements | Upper-bound improvements | Closed instances |
| --- | --- | --- | --- | --- |
| JobShop | 48 | 40 | 3 | 15 |
| JobShopOperators | 222 | 107 | 215 | 208 |
| FlexibleJobShop | 107 | 67 | 39 | 74 |
| RCPSP | 472 | 52 | 1 | 0 |
| RCPSPMax | 58 | 51 | 23 | 1 |
| MultiModeRCPSP (j30) | 552 | No reference | 3 | 535 |
| MultiModeRCPSPMax | 85 | 84 | 77 | 85 |

*Table 1. Results summary*

- **Job Shop (J | | C_max)**: open instances from Taillard `tail*` (32), abz\* (3), swv\* (9), yam\* (4), bounds from published job-shop and genetic-algorithm benchmark pages. Time limit 30,000 s for LNS+FDS with two threads, 10 minutes per DestructLB iteration; prior upper-bound work had used 30,000 s with a dedicated local search. DestructLB improved lower bounds on 40 of 48 instances and closed 4 (improving the upper bound for 2 of them); LNS+FDS closed 15 including those 4. Solve times ranged from 50 minutes (`tail12`) to 7.5 hours (`tail21`).
- **tail19 trace**: LNS reaches makespan 1352 at 388 s — 1.5% from the optimum 1332 — which tightens the space for FDS; FDS finds 1351 at 1061.2 s; LNS improves it to 1350 in 0.32 s; LNS reaches the optimum 1332 at 8518 s; FDS keeps exploring with the new upper bounds and at 12,853 s total proves no better solution exists. FDS helps LNS escape local minima by supplying a possibly totally different solution as a new starting point, and LNS supplies tight upper bounds so FDS need not guide toward solutions.
- **Job Shop with Operators** (each operation also needs an operator, one operation at a time, all operators as one discrete cumulative resource; 222 open instances): time limit 600 s for LNS+FDS, 300 s per DestructLB iteration; 208 instances closed, 107 lower and 215 upper bounds improved.
- **Flexible Job Shop (FJ | | C_max)**: 107 open instances, LNS+FDS closes 74 (indirectly improving 61 lower bounds among them) and improves 39 upper bounds with time limits up to 8 h; DestructLB at 3600 s per iteration improved 10 more lower bounds.
- **RCPSP**: 472 open PSPLib instances, same limits as the comparable lower-bound work (10 minutes for LNS+FDS and 10 minutes per DestructLB iteration), on the same-speed machine, allowing direct comparison. DestructLB improved 52 lower bounds (by 1, 2, or 3), proved the same lower bound for 330 instances, and could not prove it within the limit for 90. FDS reaches comparable lower-bound results without using explanations. Upper bounds: LNS+FDS improved only 1 and matched only 78, and no open RCPSP instance was closed.
- **RCPSP/max** (minimal and maximal time lags, 58 open instances): DestructLB at 10 minutes improved the lower bound for 56 of 57 and proved optimality for `psp j30 73`; LNS+FDS improved upper bounds for 23, matched 10, produced a poorer bound for 25, and also proved `psp j30 73` optimal; one instance closed and the average gap `(UB − LB)/UB` fell from 23.37% to 13.62%.
- **Multi-Mode RCPSP**: j30\* PSPLib instances, all 552 feasible (bounds published as upper bounds only), 3600 s for LNS+FDS, 600 s per DestructLB iteration; 535 instances closed — almost 97% — and 3 upper bounds improved.
- **Multi-Mode RCPSP/max**: 85 open instances (7 in mm50, 79 in mm100). DestructLB at 300 s improved 53 lower bounds; LNS+FDS at 1800 s improved 73 upper bounds; the two combined closed 10. The renewable (cumulative) resources turned out not to be the hardest part, so a two-stage approach was built: a CPLEX 12.6.1 MIP with start-time variables `s_i` and mode-selection booleans `m_ij`, relaxing renewable resources by basic energy reasoning over the horizon, gives an optimal makespan that is a lower bound on the original problem; CP Optimizer then solves the RCPSP/max problem using that optimal mode allocation, and for 83 of 85 instances the optimal makespan equals the MIP lower bound, so it is optimal for the original problem. The remaining 2 instances had their RCPSP/max optimum re-injected as a warm start into the full Multi-Mode RCPSP/max model, and LNS+FDS reached the MIP lower bound — all 85 open instances closed.

## Analysis of FDS behaviour

![[_papers/vilim2015failuredirected/images/page_14_image_5.jpg]]
*Fig. 4. Reusing closing choices*

- FDS produces **unbalanced search trees**: left branches often fail immediately, or are explored much faster than right branches, and long chains of 1-fail nodes ending in a closing node are common.
- Once a closing choice is found it is likely to be reused immediately after the backtrack, several times before it stops being closing, so the search escapes from deep depths quickly; 1-fail choices are also reused quickly, behaviour the paper compares to quick shaving.
- A choice picked at the root after a restart is most likely one that was recently closing, and such choices are unbalanced, for example `start time in [1,4]` versus `[5,100]`. When the left root branch is proved infeasible, the domain improves only from `[1,100]` to `[5,100]` — a small change, but probably important, because accumulating such small improvements and nogoods reduces the space and makes propagation stronger.
- **Heading first into conflict**: proving no solution with makespan ≤ 1832 on `tail50` takes 465 s; keeping the same choice order but switching to worse-rating-first branching takes 1023 s. The paper attributes the difference to restarts — exploring low-rating branches first yields shorter, easier-to-apply nogoods.
- **Preferring immediate failures**: replacing `1 + R` with `R` in equation 2 makes `localRating` resemble impact-based search; the proof that took 465 s then does not finish within 24 hours.

## Conclusions

FDS improved state-of-the-art results across benchmarks covering disjunctive and cumulative resources, minimum and maximum lags, and multiple modes, and FDS plus the CP Optimizer automatic search (LNS+FDS) can compete with, and sometimes outperform, specialized algorithms. FDS has been an integral part of the CP Optimizer automatic search since version 12.6.0.

## Related

- [[concepts/failure-directed-search]] — the mechanism this paper defines.
- DestructLB, the lower-bound-by-refutation procedure, is described in full in [[references/vilim2015-failure-directed-search-cp-scheduling]].
- [[concepts/large-neighborhood-search]] — the plan A strategy FDS is coupled to.
- [[concepts/disjunctive-scheduling-constraint-programming-model]] — the scheduling primitives FDS branches over.
- [[references/ku2016-mixed-integer-programming-job-shop]] — job-shop scheduling solved with MIP plus CP, the same benchmark family.

## Sources

- [[_papers/vilim2015failuredirected/vilim2015failuredirected-extracted.md]] — the paper text; 457 lines, 12 sidecar tags (#CP_optimizer, #CPLEX, #Constraint_programming, #Flexible_job_shop, #Job_shop, #Job_shop_with_Operators, #Multi-mode_RCPSP, #Multi-mode_RCPSP/max, #RCPSP, #RCPSP/max, #Scheduling, #Search).
- [[_papers/vilim2015failuredirected/vilim2015failuredirected.md]] — Zotero sidecar, zotero-key `PKMNUUUD`, conferencePaper, *Integration of AI and OR Techniques in Constraint Programming*, 2015, DOI 10.1007/978-3-319-18008-3_30; creators Petr Vilím, Philippe Laborie, Paul Shaw, Laurent Michel. The paper header lists only Vilím, Laborie and Shaw. `^[ambiguous]`
- Image files `page_4_image_1.jpg`, `page_6_image_0.jpg`, `page_8_image_0.jpg`, `page_14_image_5.jpg` in `_papers/vilim2015failuredirected/images/`, captioned verbatim in the text above.
