---
title: Hot Cache
updated: 2026-10-26T04:55:43Z
pages: 383
generated_by: obsidian-wiki memory hot
---

# Hot Cache

*Generated snapshot of recent vault activity. Rebuilt by `obsidian-wiki memory hot` — edits to the generated sections are overwritten, so put durable prose in `## Key Takeaways`, which survives every rebuild.*

## Recent Activity

- [2026-10-26] INGEST source=_papers/murray2015flying/murray2015flying-extracted.md pages_created=1 pages_updated=0 ...
- [2026-10-26] CROSS_LINK pages_scanned=1 links_added=2 typed_relations_written=0 ...
- [2026-10-26] INGEST source=_papers/nguyen2025set/nguyen2025set-extracted.md pages_created=1 pages_updated=0 ...

## Active Threads

*No open threads.*

## Key Takeaways

STOP: clusters with cluster-level profits, m vehicles, budget T_max; generalizes SOP (Archetti 2018) and STOPTW; MILP vars y_k/x_ij/s_i + set-partitioning master over routes; B&P with bucket DP over labels (reduced cost/last node/time/collected clusters, dominance by dominance rule), ng-route relaxation Delta_N=8, heuristic pricing + exact fallback, stabilization sigma 0.9, strong branching alpha=3/4, Two-Phase Simplex for infeasible reformulations, preprocessing by time-triangle filters; LNS on cluster permutations with DP feasibility g/h vectors cutting 75%, 5 removal + 9 insertion operators, SA acceptance T0=-mu f0/ln(0.5), removal range [4,max(4,min(eta K,40))], 100000 iterations, IRACE-tuned over 100000 experiments; results: B&P proves optimal on 379/612 SOP instances = 61.9% vs 30.4% prior, valid bounds on 491 (80.2%); LNS finds 595/612 best-known incl 40 new, reaches 378 of 379 B&P optima, beats HEA on 144 large Set1 instances 137 vs 122; STOP 612 m=2 / 612 m=3 configs: B&P total gaps 0.32% (m=2) 0.17% (m=3), LNS optimal in all 442+515 certified; 174 new instances up to 1084 customers 217 clusters, B&P 112 optima incl 29 hardest m=1 |C|=200 group ~20000s, LNS max gap 0.23% 11.69s; LNS beats VNS on 22/29 Solomon c1/c2 rows ties 7, mean -1.87%; LNS avg time 27.94s (1 veh) 16.80 (2) 9.86 (3) fastest method in every size group, 67% faster than BRKGA at >1000 nodes

## Flagged Contradictions

*None flagged.*
