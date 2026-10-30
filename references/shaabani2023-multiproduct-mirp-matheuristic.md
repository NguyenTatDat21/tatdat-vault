---
title: "Shaabani 2023 – Matheuristic for the Multi-Product Maritime Inventory Routing Problem"
category: references
tags: [maritime-inventory-routing, matheuristic, mixed-integer-programming, simulated-annealing, long-planning-horizon, natural-gas-logistics, paper]
aliases:
  - multi-product MIRP matheuristic
sources:
  - "[[_papers/shaabani2023matheuristic/shaabani2023matheuristic-extracted.md]]"
  - "[[_papers/shaabani2023matheuristic/shaabani2023matheuristic.md]]"
  - "[[_papers/shaabani2023matheuristic/images/page_13_chart_7.jpg]]"
  - "[[_papers/shaabani2023matheuristic/images/page_14_chart_2.jpg]]"
relationships:
  - target: "[[concepts/maritime-inventory-routing-problem]]"
    type: related_to
  - target: "[[concepts/simulated-annealing-metropolis-cooling]]"
    type: related_to
  - target: "[[references/dellamico2020-matheuristics-pdstsp]]"
    type: related_to
  - target: "[[references/goel2012-large-neighborhood-search-lng-inventory-routing]]"
    type: related_to
summary: "Shaabani, Hoff, Hvattum & Laporte (COPR 2023): fixed-arc SA plus CPLEX solve 60-day multi-product MIRP, 6x faster than CPLEX and 33.74% better on instance G."
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-27
tier: core
created: 2026-10-27T07:00:00Z
updated: 2026-10-30T14:08:41Z
provenance:
  extracted: 0.96
  inferred: 0.04
  ambiguous: 0.00
---

> [!tldr] Products, not ports, drive the cost
> A two-phase matheuristic solves multi-product maritime inventory routing over a 60-day horizon. It is about six times faster than CPLEX and beats CPLEX's 43,200-second solutions on the largest instances. The comparison of single-product, two-product and four-product versions shows the number of **products** and the **structure** of ports, not the port count, is what makes the problem expensive.

## Problem and model

- Multi-product MIRP: vessel routes are planned while port inventories stay inside bounds; a port can consume one product and produce another.
- Four traits separate MIRP from land IRP: no depot to return to; the number of visits per port matters; load/unload quantities are a large share of vessel capacity, so a vessel visits only a few ports between production visits; travel times are much longer.
- The model is largely Agra et al. (2015), with two differences: a deterministic horizon cap (constraints 28–29) and inventory constraints for production ports (39–45), which the stochastic version did not need.
- Size: constraints and continuous variables `O(|N|² m̄² |V| |K|)`, binary variables `O(|N|² m̄² |V|)`. Instances above 2,000 constraints and 600 binary variables count as large. Instance H has 11,677 rows, 11,688 columns and 2,183 discrete variables.
- Objective: vessel sailing cost, port operation cost, and penalty costs for backlog and overstocking.

## The matheuristic

- **Phase 1** generates candidate routes with a simulated-annealing loop over a pool of current solutions, controlled by six parameters: initial temperature `T0`, iterations per temperature `SubIt`, cooling rate `α`, iteration growth `β`, pool size `nSol`, solutions generated per incumbent `φ`.
- **Phase 2** selects an arc subset Ω from the current solutions, fixes Ω in the MIP, and solves it with CPLEX.
- If the objective improves, the obtained routes seed the next Phase 1. On the first non-improvement, arcs from all previous runs are fixed and the most frequently unvisited nodes are excluded; if that helps, the best Phase 2 run is then solved to optimality.
- Parameters tuned with a **Taguchi** design `L27(3⁶)`, smaller-the-better S/N ratio: T0=100, SubIt=16, α=0.96, β=0.998, nSol=5, φ=4.

## Results

![[_papers/shaabani2023matheuristic/images/page_13_chart_7.jpg]]
*Fig. 8. Main effects plot for SN ratios.*

![[_papers/shaabani2023matheuristic/images/page_14_chart_2.jpg]]
*Fig. 9. Main effects plot for Means.*

- Table 5 (objective, CPLEX vs matheuristic): A 271.63, B 241.33, C 332.99, D 368.10 — all four small instances solved to optimality by both; the matheuristic reached D's optimum more than four times faster (224.8 s vs 925.6 s).
- On the four large instances CPLEX reports optimality gaps of 85.81% (E), 99.15% (F), 99.66% (G) after 43,200 s, and finds **no feasible solution** for H. The matheuristic matches E (4,963.25), is 0.001% worse on F, and improves G by 33.74% (121,537.16 vs 183,432.86), reaching H at 1,356,842.55. Total matheuristic times run 11.6 s to 8,110.2 s; Phase 2 dominates on large instances (e.g. 5,512.8 s of H's 8,110.2 s).
- Products: merging four products into two and then one lowers run time sharply — instance group I1, 16 ports, 4 vessels: 3,688 s with 4 products, 323 s with 2, 8 s with 1.
- Ports: reducing 24 ports to 16 then 8 changes the optimality gap for most tests; 16-port instances take far longer than 8-port ones. In tests I2 and I4 the matheuristic hit the 43,200 s limit with 6.21% and 3.92% optimality gaps.

The decisive factor is instance structure: when a port is limited to at most one product, run time collapses, and the authors attribute the high cost of multi-product MIRP to that, not to raw port count. The authors' stated next steps target uncertainty, better post-processing, and the effect of planning-horizon length. ^[inferred]

## Related

- [[concepts/maritime-inventory-routing-problem]] — the problem family; this paper adds multi-product coupling and a 60-day horizon.
- [[concepts/simulated-annealing-metropolis-cooling]] — Phase 1 is a temperature-driven search over a solution pool.
- [[references/dellamico2020-matheuristics-pdstsp]] — same matheuristic pattern: a heuristic proposes a subgraph, an exact solver optimizes inside it.
- [[references/goel2012-large-neighborhood-search-lng-inventory-routing]] — LNS for a single-product LNG inventory routing problem, the heuristic comparator for the same family.
- [[references/santini2018-alns-acceptance-criteria]] — the acceptance-criteria ranking that informs how a temperature-based acceptance rule is tuned.

## Limitations

- Benchmark instances are **modified** versions of published MIRP benchmarks, so numbers are not comparable to published literature.
- The model is deterministic: sailing times, port times, demand and prices are fixed.
- Captions are quoted from the extracted markdown; the model cannot inspect images, so figure-to-caption mapping follows the extractor's label order.

## Sources

- [[_papers/shaabani2023matheuristic/shaabani2023matheuristic-extracted.md]] — Shaabani, Hoff, Hvattum & Laporte, *Computers & Operations Research*, 2023-06-01, zotero-key Y4VYW2JD, DOI 10.1016/j.cor.2023.106214.
