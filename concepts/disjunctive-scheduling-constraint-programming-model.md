---
title: >-
  Disjunctive Scheduling Constraint-Programming Model
category: concepts
tags: [constraint-programming, scheduling, cumulative-functions, interval-variables, modeling-pattern]
relationships:
  - target: "[[references/goel2015-constraint-programming-lng-ship-scheduling]]"
    type: derived_from
  - target: "[[concepts/cp-sat-hint-start]]"
    type: related_to
  - target: "[[concepts/cumulative-volume-lower-bound-cp-search]]"
    type: related_to
  - target: "[[concepts/mirp-modeling-continuous-vs-discrete-time]]"
    type: related_to
  - target: "[[concepts/time-space-network-ship-flow-model]]"
    type: related_to
  - target: "[[references/hendel2022-adaptive-lns-for-mip]]"
    type: related_to
  - target: "[[references/christiansen2008-maritime-inventory-routing-problems]]"
    type: related_to
  - target: "[[references/furini2016-two-dimensional-guillotine-cutting-ip]]"
    type: related_to
  - target: "[[references/ku2016-mixed-integer-programming-job-shop]]"
    type: related_to
  - target: "[[references/isik2023-constraint-programming-hybrid-flow-shop]]"
    type: related_to
  - target: "[[references/jimenez-piqueras2023-constraint-programming-premarshalling]]"
    type: related_to
  - target: "[[concepts/auxiliary-decision-variable-model-strengthening]]"
    type: related_to
  - target: "[[concepts/search-combinators-meta-search]]"
    type: related_to
  - target: "[[concepts/encoding-preservation-under-composition-and-merging]]"
    type: related_to
  - target: "[[concepts/bound-tightening-relaxation-networks]]"
    type: related_to
  - target: "[[concepts/dag-topological-sort-scheduling-move-evaluation]]"
    type: related_to
  - target: "[[references/vilim2015-failure-directed-search-cp-scheduling]]"
    type: related_to
sources:
  - _papers/goel2015constraint/goel2015constraint-extracted.md
  - _papers/goel2015constraint/goel2015constraint.md
  - _papers/goel2015constraint/images/page_2_chart_15.jpg
  - _papers/goel2015constraint/images/page_2_chart_16.jpg
  - _papers/goel2015constraint/images/page_2_chart_19.jpg
  - _papers/ku2016mixed/ku2016mixed-extracted.md
  - _papers/ku2016mixed/ku2016mixed.md
  - _papers/isik2023constraint/isik2023constraint-extracted.md
  - _papers/isik2023constraint/isik2023constraint.md
  - _papers/jimenez-piqueras2023constraint/jimenez-piqueras2023constraint-extracted.md
  - _papers/jimenez-piqueras2023constraint/jimenez-piqueras2023constraint.md
summary: >-
  Interval variables, sequences and cumul functions express scheduling with capacity coupling; encoding choice dominates, with disjunctive evidence from JSP, HFSP and premarshalling papers.
provenance:
  extracted: 0.80
  inferred: 0.15
  ambiguous: 0.05
base_confidence: 0.97
lifecycle: draft
lifecycle_changed: 2026-10-25
tier: core
created: 2026-10-24T03:00:25Z
updated: 2026-10-30T14:38:55Z
---

# Disjunctive Scheduling Constraint-Programming Model

> [!tldr] The CP representation of a scheduling-plus-inventory problem built from interval variables, `SequenceVar`/`NoOverlap` disjunctive constraints, cumul functions (`pulse`, `stepAtEnd`, `step`, `alwaysIn`, `alwaysEqual`) and presence/sequence primitives (`Alternative`, `First`, `typeOfNext`). Goel et al. show the encoding choice matters: the **task-perspective** model (CP1) uses 215,290 variables and 1.9 GB on the P14 instance and cannot find a feasible solution, while the **resource/ship-perspective** model (CP2) uses 15,375 variables and 203 MB on the same instance.

![[_papers/goel2015constraint/images/page_2_chart_15.jpg]]
![[_papers/goel2015constraint/images/page_2_chart_16.jpg]]
![[_papers/goel2015constraint/images/page_2_chart_19.jpg]]
*Fig. 1 (verbatim): Example of three elementary cumul functions. Here, $x$ is an interval variable, and $k$, $t$ are integers.* Subfigures (a) `pulse(x,k)`, (b) `stepAtEnd(x,k,kmin,kmax)`, (c) `step(t,k)` — the primitives used to write inventory profiles as cumulative curves over interval variables.

## Encoding Primitives

Task-perspective (CP1, per terminal $j$):

- `c^J_{j,i}` = interval for cargo $i$ at $j$, domain $[t^{EC}_{j,i},\,t^{LC}_{j,i}+1)$
- `c^{JV}_{j,i,v}` = the cargo carried by ship $v$; `Alternative(c^J, {c^{JV}}_v)`
- presence chain `presenceOf(c^J_i) ⇒ presenceOf(c^J_{i-1})`
- `startOf(c^J_{i-1}) + τ_j ≤ startOf(c^J_i)`
- berth capacity `Σ_i pulse(c^J,1) ≤ b_j`
- alternation of loading/discharging, per-ship, via a cumul function
- inventory: $\tilde p_j$, $\tilde d_j$ as `step` profiles, $\tilde z_j=\sum_{v,i}\text{stepAtEnd}(c^{JV},\gamma^V_v)$, $\tilde l_j$ from daily loss intervals `slt_{j,t}` with `alwaysIn` bounds, and `alwaysEqual` complementarity constraints linking loss intervals to daily losses

Ship-perspective (CP2): variables are maximal ship visits $c^V_{v,i}$ with domain $[t^{EV}_{v,i},\,t^{LV}_{v,i})$, split by `Alternative` into cargo copies $c^{VJ}_{v,i,j}$; presence propagates $c^V_{v,i}\Rightarrow c^V_{v,i-1}$; `First(seq_v, a_v)` handles unavailability; `typeOfNext` with the transition matrix $M(j,\varphi_1)=1$, $M(j,\varphi_2)=0$, and `NoOverlap(seq_v, M)` enforces that a service day occupies a berth.

**Alternation inside the domains**: set $J^V_{v,i}=\{j\in J\}$, $J^L_{v,i}=\{j\in L\}$, $J^R_{v,i}=\{j\in R\}$, $J^V_{v,i}=J^L_{v,i}$ and $J^V_{v,i+1}=J^R_{v,i}$ when ship $v$ starts at a production terminal (the reverse when it starts at a regasification terminal). Full-load/full-discharge alternation is then guaranteed by the variable domains, so CP1's explicit alternation constraint is not needed — at the cost of not supporting split deliveries.

```mermaid
flowchart TD
  A["Define interval variables per task (cargo) or per resource (ship visit)"] --> B["Link copies with Alternative; propagate presence along the sequence"]
  B --> C["SequenceVar + NoOverlap with transition matrix M = disjunctive resource capacity (berth)"]
  C --> D["Cumul functions: step / stepAtEnd / pulse = inventory and cumulative volume profiles"]
  D --> E["alwaysIn / alwaysEqual bounds tie cumulative profiles to daily flows and losses"]
  E --> F["Objective: demand shortfall + time-weighted losses (paper Eq. 41)"]
```

$$\tilde z_j=\sum_{v\in V}\sum_{i\in I_v}\text{stepAtEnd}\big(c^{VJ}_{v,i,j},\ \gamma^V_v\big)$$

## Variable Counts

Model sizes (paper Table 1):

| Instance $(|L|,|R|,|V|)$ | MIP 0-1 vars | CP1 vars (memory) | CP2 vars (memory) | CP2/CP1 vars |
|---|---|---|---|---|
| P13 (1,8,40) | 132,995 | 54,588 (503 MB) | 10,077 (141 MB) | 0.18 |
| P14 (1,10,69) | 232,856 | 215,290 (1.9 GB) | 15,375 (203 MB) | 0.07 |
| P18 (1,13,56) | 320,988 | 128,152 (1.2 GB) | 19,112 (272.3 MB) | 0.15 |
| P20 (1,18,100) | 476,426 | 337,155 (3.0 GB) | 26,783 (380 MB) | 0.08 |

## Why It Matters

- CP has no time discretization, so a daily-grid MIP and a continuous CP model of the same problem can be solved in the same framework; the MIP model here is [[concepts/time-space-network-ship-flow-model]].
- Modeling assumptions the representation inherits: one full day loading/discharging occupies a berth, integer travel days, no seasonality, fixed discharge volume = load − nominal boil-off, fixed regas rates. The paper's extensions relax these: split loads, variable discharge, seasonality, berth availability, and multi-period planning.
- The cumul-function inventory profiles are what make the cumulative lower bound in [[concepts/cumulative-volume-lower-bound-cp-search]] expressible.
- The CP literature's hinting capability (CP-SAT `AddHint`) is the natural bridge from an incumbent MIP solution to CP search; see [[concepts/cp-sat-hint-start]].
- The same disjunctive machinery appears in classic job shop MIP: Manne's big-M and Liao's surplus-variable models, plus time-indexed and rank-based variants, are benchmarked in [[references/ku2016-mixed-integer-programming-job-shop]]; solver presolving can eliminate the surplus variables and flip which model wins.
- Interval-sequence encodings with setup matrices, `endAtStart` for no-wait and `startOfNext` tricks for blocking carry the disjunctive pattern to hybrid flow shops: [[references/isik2023-constraint-programming-hybrid-flow-shop]].
- The container premarshalling CP series shows CP quality driven by added groups of decision variables, not by disjunctive size alone: [[references/jimenez-piqueras2023-constraint-programming-premarshalling]]; see [[concepts/auxiliary-decision-variable-model-strengthening]].

## Related
- [[concepts/encoding-preservation-under-composition-and-merging]] — shares constraint-programming + scheduling tags with this page
- [[concepts/search-combinators-meta-search]] — shares constraint-programming + scheduling tags with this page

- [[concepts/cumulative-volume-lower-bound-cp-search]]
- [[concepts/cp-sat-hint-start]]
- [[concepts/auxiliary-decision-variable-model-strengthening]]
- [[references/ku2016-mixed-integer-programming-job-shop]]
- [[references/isik2023-constraint-programming-hybrid-flow-shop]]
- [[references/jimenez-piqueras2023-constraint-programming-premarshalling]]
- [[concepts/time-space-network-ship-flow-model]]
- [[concepts/mirp-modeling-continuous-vs-discrete-time]]
- [[references/goel2015-constraint-programming-lng-ship-scheduling]]
- [[references/goel2012-large-neighborhood-search-lng-inventory-routing]]
- [[references/hendel2022-adaptive-lns-for-mip]]
- [[references/christiansen2008-maritime-inventory-routing-problems]]

## Limitations

- CP1 reaches 1.2–3.0 GB memory and cannot find a feasible solution on P14 (69 ships), P18 (56), P20 (100), so only CP2 is usable at those sizes.
- CP2 cannot represent split delivery/split load; the encoding choice is a modeling commitment, not a tuning knob.
- The paper compares CP against a specialized MIP heuristic, not against an exact MIP bound, so "4–10× faster" is a heuristic-to-heuristic statement. ^[ambiguous]
- The transition matrix formulation requires full-load/full-discharge services with fixed duration. ^[inferred]

## Sources

- [[_papers/goel2015constraint/goel2015constraint-extracted.md]]
- [[_papers/goel2015constraint/goel2015constraint.md]]
- [[_papers/goel2015constraint/images/page_2_chart_15.jpg]]
- [[_papers/goel2015constraint/images/page_2_chart_16.jpg]]
- [[_papers/goel2015constraint/images/page_2_chart_19.jpg]]
- [[_papers/ku2016mixed/ku2016mixed-extracted.md]]
- [[_papers/ku2016mixed/ku2016mixed.md]]
- [[_papers/isik2023constraint/isik2023constraint-extracted.md]]
- [[_papers/isik2023constraint/isik2023constraint.md]]
- [[_papers/jimenez-piqueras2023constraint/jimenez-piqueras2023constraint-extracted.md]]
- [[_papers/jimenez-piqueras2023constraint/jimenez-piqueras2023constraint.md]]
