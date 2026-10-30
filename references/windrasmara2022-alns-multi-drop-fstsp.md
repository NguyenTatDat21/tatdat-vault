---
title: >-
  An Adaptive Large Neighborhood Search Heuristic for the Flying Sidekick
  Traveling Salesman Problem with Multiple Drops
category: references
tags: [paper, drones, delivery, alns, heuristic, tsp]
summary: ALNS heuristic for the multi-drop FSTSP; the new formulation adds
  launch and retrieve times, and the heuristic beats IG and Ha et al. on
  case-study, Ha, and TSPLIB instances.
provenance:
  extracted: 0.85
  inferred: 0.12
  ambiguous: 0.03
base_confidence: 0.67
tier: core
lifecycle: source
created: 2026-10-29T17:10:00Z
updated: 2026-10-29T17:10:00Z
sources:
  - "obsidian://zotflow?type=open-attachment&libraryID=11058526&key=ELF2KI54"
  - "_papers/windrasmara2022adaptive/windrasmara2022adaptive-extracted.md"
  - "_images/2df84d324428b4250493123294693145161d651b6e76347d6094057413321379.jpg"
  - "_images/e284b495679425d5883d24fe2c52f47128166346660467564473093224714276.jpg"
  - "_images/2432354792093189397564762615771111542531736220353451335424152753.jpg"
  - "_images/1827514754515313653342715256363631347131202263206352117433616276.jpg"
  - "_images/1665176176425222214243222476422415222221636552643425215235653345.jpg"
  - "_images/1222625533534312324132622554432452456473134232442432231515644511.jpg"
  - "_images/15522432243221234233242254245141642564234254243135256523522661466.jpg"
  - "_images/15116254243262455323523544223242415242536165326432233222241313566.jpg"
  - "_images/15622624434645353622524423352356325355242435236252335225535313446.jpg"
  - "_images/13425622462445322635432235424253246363552232225432223244523312543.jpg"
  - "_images/16233262242542245224632463653425644452324342523462323464322235263.jpg"
relationships:
  - target: "[[references/murray2015flying]]"
    type: related_to
  - target: "[[references/murray2020-multiple-flying-sidekicks-tsp]]"
    type: related_to
  - target: "[[references/poikonen2020-k-mvdrp]]"
    type: related_to
  - target: "[[references/ha2018-min-cost-tsp-d]]"
    type: related_to
  - target: "[[references/sacramento2019-vrp-d-truck-drone-alns-cost]]"
    type: related_to
  - target: "[[references/ropke2006-adaptive-large-neighborhood-search-pdptw]]"
    type: related_to
  - target: "[[references/santini2018-alns-acceptance-criteria]]"
    type: related_to
  - target: "[[references/dellamico2020-matheuristics-pdstsp]]"
    type: related_to
  - target: "[[concepts/multi-drop-flying-sidekick-traveling-salesman-problem]]"
    type: extends
  - target: "[[concepts/alns-destroy-repair-operator-suite]]"
    type: uses
  - target: "[[concepts/large-neighborhood-ship-pair-destroy-repair]]"
    type: related_to
  - target: "[[concepts/multiple-flying-sidekicks-traveling-salesman-problem]]"
    type: related_to
  - target: "[[concepts/k-multi-visit-drone-routing-problem]]"
    type: related_to
  - target: "[[concepts/adaptive-large-neighborhood-search-for-mip]]"
    type: uses
lifecycle_changed: 2026-10-29T17:10:00Z
---

# An Adaptive Large Neighborhood Search Heuristic for the Flying Sidekick Traveling Salesman Problem with Multiple Drops

> [!tldr] ALNS for the multi-drop FSTSP
> The paper extends the Flying Sidekick TSP to **multi-drop** operation: a
> truck and drone route is decoded from a two-row matrix of node permutations
> (AN) and action codes (AM), with launch and retrieve times added to the
> endurance constraint. An ALNS heuristic with four destroy operators and six
> repair operators beats the iterated-greedy benchmark by −3.6 % to −38.6 %
> objective, and yields up to 71 % time reduction against single-drop
> benchmarks.

**Source**: Windras Mara, Setyo; Rifai, Achmad Pratama; Sopha, Bertha Maya.
"An adaptive large neighborhood search heuristic for the flying sidekick
traveling salesman problem with multiple drops." *Expert Systems with
Applications*, 2022-11-01, DOI 10.1016/j.eswa.2022.117647. Authors: the
Department of Mechanical and Industrial Engineering, Universitas Gadjah Mada,
Yogyakarta 55284, Indonesia.

## Overview
The paper proposes a new mathematical formulation for the multi-drop FSTSP and an ALNS heuristic, demonstrated on a real delivery case in Indonesia. The truck carries a drone; the drone launches, serves multiple customers, retrieves, and the truck recovers. Existing single-drop FSTSP work restricts one sortie; multi-drop lets the drone serve several nodes in a sortie, following the multi-drop capability of delivery trucks.
^mar1

The heuristic outperforms the state-of-the-art iterated-greedy (IG) benchmark, and multi-drop schedules reduce time, truck distance, and cost substantially over single-drop plans. ^mar2

## Model: the multi-drop FSTSP
^mar3
The graph is `G=(V,A)`, `V={0..n}` with depot 0, and `Vd ⊆ V` the drone-eligible nodes. Truck road distance `d^T` follows the directed road network; drone distance `d^D` is straight-line Euclidean; truck/drone travel times `τ^T`/`τ^D` are derived. Each operation `OP_k` = pair of paths `{T_k,D_k}` with decode `[i,j,C,D]` — launch node i, retrieval node j, truck array C, drone array D, `C∩D=∅`, in one of the five valid forms in Fig. 2. Endurance constraint (eq. 1):
`τ_i→D1 + Σ τ_Di→Di+1 + τ_D|D|→j + w_r^D ≤ ε`
The operation cost is `t_k = max{t(T_k), t(D_k)} = M` when a drone node is present, else `t(T_k)` (eq. 2); the drone time is
`τ_i→D1 + Σ τ_Di→Di+1 + τ_D|D|→j + w_r^D`
and the truck time includes the launch setup `s^L` and retrieve `s^R` (eqs. 3–4); these two times are neglected in Gonzalez-R et al. 2020's truck-drone-team logistics (TDTL) — the multi-drop FSTSP is TDTL with `s^L` and `s^R`.
^mar4
The set-partitioning MIP follows Agatz 2018 and Poikonen & Golden 2020, using operation subsets `K(v)`, start-node sets `K^T(v)`, `K^D(v)`, and active indicator `x_k`/start-node `Y_v`; the objective minimises total mission time `M = Σ t_k x_k` (eq. 5, 50–15 customer constraints, 16–20 node constraints, 21–30 depot constraints). The objective minimises mission time `M` (the truck and drone finish simultaneously), the truck must be back at depot 0.
^mar5
The MIP was solved with Gurobi 9.0 (Python 3.6) for `n ≤ 8`: memory intractable for `n > 8`, so the heuristic is used. FSTSP is NP-hard; optimal benchmarks reach 6 nodes (Murray & Chu), 12 nodes TSP-D (Agatz), 14 nodes B&B (Dell'Amico 2021).
^mar6

## ALNS heuristic
^mar7
The ALNS is built on Røpke & Pisinger 2006 with Shaw 1998's LNS as backbone. Random initial solution; destroy/repair cycles; Metropolis acceptance (eq. 16): `Pr = exp(−(M'−M)/(BZ×T_c))` when `M'−M>0`, else 1. Cooling `T_c ← α×T_c`, `0<α<1`. Roulette wheel selection `Pr(c−) = ω_c−/Σ`, `Pr(c+) = ω_c+/Σ`; weight update `ω_{i+1}− = λ(ω_i−) + (1−λ)(η_i)`; score `η_i` by outcome Ω1 (`M_i ≤ M*`), Ω2 (`M_i ≤ M_{i−1}`), Ω3 (`M_i>M_{i−1} ∧ U(0,1)<Pr`), Ω4. Archive `AR_s` stores elite solutions; the worst is removed when `M' ≤ M^AR_s`.
^mar8
Destroy operators: **RD** (random removal), **WTD** (worst truck distance, truck-served nodes only), **WDD** (worst drone distance, reduces drone time to satisfy endurance), **BD** (block destroy: delete a contiguous interval from `AN`, `AM`, or both). Repair operators: **RR** (random), **AR** (archive repair, Algorithm 3: `rand ≤ 0.33` insert `AM_j` of archive solution, `0.33–0.67` `AN_j`, else both), **LDR-1** (least distance `d_{i−1→i}`, Algorithm 4), **LDR-2** (successor variant `d_{i→i+1}`), **HR** (hill-climbing swap of removed nodes). The destroy factor is `f_c = f_1 − (f_1−f_0)(i_c/I)`, number destroyed `ND_c = n(f_c)`. Solution adjustment (Fig. 8): redundant `AN` values reassigned to unassigned customers; `AM` first/last values `1|2` → `0`.
^mar9
The solution representation is a `[(n+2),2]` matrix of AN (node permutation, depot first and last) and AM ∈ {0,1,2}: 0 = truck+drone together (0 is the retrieval node when a drone is in the sortie), 1 = drone-only visit, 2 = truck call-the-truck move. The decode rules (four rules, Algorithm 1, `LastPos_Truck`/`LastPos_Drone` tracking) are verbatim in the extracted source.
^[inferred]
This is more compact than Ponza 2016's `[(n+2),3]` scheme with launch/retrieval lists `TT`,`DD`,`DR`, and copes with the two prohibited conditions of Ponza 2016.
^mar10

## Experiment and results
^mar11
Setting: heuristics in MATLAB R2019a, MIP via Gurobi 9.0 on Python 3.6, Intel Core i7-10700 2.90 GHz, 32 GB DDR4, single core; IG benchmark in Gonzalez-R et al. 2020, benchmark time limit = ALNS time. Table 1 parameters: `T_1=200`, `T_0=1`, `α=0.99999`, `BZ=0.1`, `Ω_1,Ω_2,Ω_3=0.3,0.15,0.0`, `λ=0.9`, `f_1=0.75`, `f_0=0.25`; IG `T_1 = (1×(Σ τ^T + Σ τ^D))/(n−1)`, `T_0=0`, `α=0.995`.
^mar12
Case study: retail company in Yogyakarta, Indonesia, one depot + 100 retail branches, all retailers drone-eligible, small-size package demands, multi-visit sorties; drone 35 km/h, truck 50 km/h, battery 24 min, launch 30 s, retrieve 40 s (de Freitas & Penna 2020). Ha et al. 2018 dataset: 65 instances of sizes 10/50/100, speeds 40 km/h, 24 min, 30/40 s. TSPLIB 25 instances, 51–200 nodes (de Freitas & Penna 2020, Reinelt 1991), 35/50 km/h, 24 min, 30/40 s. 10 repetitions per instance; gap `Δ_{M*} = (M_ALNS* − M_Z*)/M_Z*`.
^mar13
Operator-removal paired t-tests on the Ha dataset (Table 2, objective deltas) show destroy operator **BD** most impactful (25.98 %, p 4.7e−14), repair operator **LDR-1** most impactful (22.43 %, p 2.2e−24); WDD 8.21 % (p 2.3e−13), WTD 7.23 % (p 1.2e−12), RD 9.25 % (p 1.0e−12), RR 9.43 % (p 4.5e−17), HR 16.35 % (p 8.7e−25), LDR-2 12.03 % (p 5.4e−17), AR 5.55 % (p 4.2e−8). Running-time effects: HR −11.24 % (fastest removal), LDR-1 −2.01 %, BD +1.00 %, WTD −5.24 %. Destroy-mechanism removal (Table 3): deleting `AN` destroy raises objective 29.12 % (time −0.53 %), `AM` 17.52 % (+12.27 %), `AN+AM` 17.27 % (−18.91 %).
^mar14
Case study (Table 4): for `n ≤ 15` all heuristics reach the Gurobi optimum (0.0 % gap); ALNS vs IG `Δ_M*` of −3.6 % to −38.6 % on 50–100-size instances, average −10.6 %; Gurobi memory intractable beyond `n=8`. Ha dataset: average −17.6 % over Ha et al., −10.8 % over IG, −9.6 % average objective; TSPLIB: average −46.2 % over Ha, −12.9 % over IG, −15.7 % average objective. Paired t-tests (Table 7): case study `Δ_M*` p=2.1×10⁻⁸, `Δ_M` p=0.003; Ha p=1.6×10⁻⁵ both; TSPLIB p=2.3×10⁻¹⁷ and 1.1×10⁻²⁰ — all null hypotheses rejected, ALNS is better.
^mar15
Managerial insights (Table 8, n=6..100): TSP single-drop time 163.32 min vs multi-drop 47.23 min → up to **71.08 % time reduction**; truck distance 66.7 % less in multi-drop, total distance 153.32 km → 51.06 km = 24.37 % shorter; naive cost `dist_GV + 0.1×dist_UAV` (Sacramento et al. 2019 drone travel cost ≈ 10 % of truck) → 62.46 % cheaper than TSP cost; average #sortie 2.87, #drone nodes 31.56, 72.61 % of nodes are drone-eligible. Amazon packages <2.3 kg (Poikonen & Golden 2020). IG's constructive initial solution gives faster convergence; ALNS needs 100 iterations for eil51 and >300 for kroB100 in equal time.
^mar16
Multi-drop margin 17.6 %–46.2 % over single-drop benchmarks (Ha et al. 2020 HGA) reflects real drone endurance limits in a real case study.
^[inferred]

## Figures (source images)
![Fig. 1 — FSTSP with sorties.](/images/2df84d324428b4250493123294693145161d651b6e76347d6094057413321379.jpg)

![Fig. 2 — Valid forms of operations.](/images/e284b495679425d5883d24fe2c52f47128166346660467564473093224714276.jpg)

![Fig. 3 — Solution representation scheme and the derived solution.](/images/2432354792093189397564762615771111542531736220353451335424152753.jpg)

![Fig. 4 — Two Prohibited Conditions (Ponza, 2016).](/images/1827514754515313653342715256363631347131202263206352117433616276.jpg)

![Fig. 5 — Example cases of TSP and FSTSP (de Freitas and Penna, 2020).](/images/1665176176425222214243222476422415222221636552643425215235653345.jpg)

![Fig. 6 — Demonstration of the proposed scheme in the example case.](/images/1222625533534312324132622554432452456473134232442432231515644511.jpg)

![Fig. 7 — Demonstration of benchmark scheme on the example case.](/images/15522432243221234233242254245141642564234254243135256523522661466.jpg)

![Fig. 8 — The procedure for solution adjustment.](/images/15116254243262455323523544223242415242536165326432233222241313566.jpg)

![Fig. 9 — Illustration of solution for the case study with n = 7 (blue dot depot, red dots customer, blue truck, green drone lines).](/images/15622624434645353622524423352356325355242435236252335225535313446.jpg)

![Fig. 10 — Convergence curves on TSPLIB instances: (a) eil51, (b) kroB100.](/images/13425622462445322635432235424253246363552232225432223244523312543.jpg)
Fig. 10 subcaptions as rendered: (a), (b).

Tables: Table 1 Parameter settings. / Table 2 Impact of removing each operator in ALNS. / Table 3 Impact of removing each destroy mechanism in ALNS. / Table 4 Results for the case study dataset. / Table 5 Results for Ha et al. (2018) dataset. / Table 6 Results for TSPLIB dataset. / Table 7 Results of paired t-tests. / Table 8 Results of experiments for managerial insights.

## Related
- [[references/murray2015flying]] — FSTSP single-drop baseline.
- [[references/murray2020-multiple-flying-sidekicks-tsp]] — multiple sidekicks.
- [[references/poikonen2020-k-mvdrp]] — K-MVDRP set-theoretical model.
- [[references/ha2018-min-cost-tsp-d]] — min-cost TSP-D, Ha benchmark.
- [[references/sacramento2019-vrp-d-truck-drone-alns-cost]] — VRP-D ALNS, drone cost 10 %.
- [[references/ropke2006-adaptive-large-neighborhood-search-pdptw]] — ALNS foundation.
- [[references/santini2018-alns-acceptance-criteria]] — ALNS acceptance criteria.
- [[references/dellamico2020-matheuristics-pdstsp]] — matheuristic lineage.
- [[concepts/multi-drop-flying-sidekick-traveling-salesman-problem]] — the problem family.
- [[concepts/alns-destroy-repair-operator-suite]] — the operator suite.
- [[concepts/large-neighborhood-ship-pair-destroy-repair]] — destroy/repair pattern.
- [[concepts/multiple-flying-sidekicks-traveling-salesman-problem]] — multi-sidekick family.
- [[concepts/k-multi-visit-drone-routing-problem]] — multi-visit routing.
- [[concepts/adaptive-large-neighborhood-search-for-mip]] — ALNS applied to MIP.
