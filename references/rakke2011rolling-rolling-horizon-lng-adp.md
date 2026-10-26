---
title: >-
  A rolling horizon heuristic for creating a liquefied natural gas annual delivery program (Rakke et al., 2011)
category: references
tags: [paper, lng, annual-delivery-program, maritime-inventory-routing, rolling-horizon-heuristic, mixed-integer-programming, solution-space-reduction, improvement-heuristic, heterogeneous-fleet, spot-market, berth-capacity, parameter-testing, branch-and-bound]
relationships:
  - target: "[[concepts/annual-lng-delivery-program]]"
    type: implements
  - target: "[[concepts/maritime-inventory-routing-problem]]"
    type: uses
  - target: "[[references/gronhaug2010-branch-and-price-lng-irp]]"
    type: related_to
  - target: "[[references/gronhaug2009-supply-chain-optimization-lng]]"
    type: related_to
  - target: "[[references/fagerholt2023-maritime-inventory-routing-survey]]"
    type: related_to
  - target: "[[concepts/time-space-network-ship-flow-model]]"
    type: related_to
  - target: "[[references/halvorsen-weare2013-lng-routing-berth-inventory]]"
    type: related_to
sources:
  - _papers/rakke2011rolling/rakke2011rolling-extracted.md
  - _papers/rakke2011rolling/rakke2011rolling.md
  - _papers/rakke2011rolling/images/page_1_image_10.jpg
  - _papers/rakke2011rolling/images/page_2_image_17.jpg
  - _papers/rakke2011rolling/images/page_7_image_13.jpg
summary: >-
  Rolling horizon heuristic for the LNG annual delivery program: MIP over a priori scheduled voyages, central+forecasting windows, SSR, improvement heuristic; 10.33% avg gap.
provenance:
  extracted: 0.85
  inferred: 0.12
  ambiguous: 0.03
base_confidence: 0.67
tier: supporting
lifecycle: draft
lifecycle_changed: 2026-10-26T10:43:50Z
created: 2026-10-26T10:43:50Z
updated: 2026-10-26T10:43:50Z
---

# A rolling horizon heuristic for creating an LNG annual delivery program (Rakke et al., 2011)

*Transportation Research Part C: Emerging Technologies, 2011. DOI: 10.1016/j.trc.2010.09.006.* Received 2009-12-05; accepted 2010-09-16.

## Problem & motivation

Rakke, Stålhane, Moe, Christiansen, Andersson, Fagerholt and Norstad (NTNU / MARINTEK) tackle the **annual delivery program (ADP)** planning problem of one of the world's largest LNG producers: a single liquefaction plant with storage tanks feeding one loading port with limited berths per gas type, a heterogeneous fleet (up to 46 ships), and 17 long-term contracts of 20–30 years to regasification terminals worldwide (monthly demands, or volume "fairly evenly spread" over the year). The ADP is the tactical one-year schedule stating, for every scheduled voyage, which ship sails, which LNG type (RLNG/LLNG), which contract, and the loading/unloading days. Objective: minimize transportation and penalty costs minus spot-market revenue minus the value of LNG left in tanks at the horizon end. Context: the spot market is projected at 15–20% of LNG trade; EIA sees demand +52% by 2030; the IEA forecasts ~400 LNG ships by 2015 (double 2007). Three planning levels: strategic (contract portfolio, fleet investment), tactical (the ADP), operational (ADP within 3 months). The ADP must be built in under 2 h — a producer specification.

LNG physics constraints: volume reduced ×600, boiling at −160 °C, **boil-off 0.11–0.13% of cargo per day** (fixed per ship), a 24 h purge/cool-down after maintenance consuming ship time and a berth, ~24 h loading-port operations, **at most 2 chartered spot ships loaded per day** (one per gas type), ships leave the loading port fully loaded (no partial loads), no inventory management at the receiving terminals, maintenance modeled as a contract $C^M$ with fixed windows. Spot cargoes are assumed shipped to the most distant terminal to make the ADP robust; spot price fixed at **USD 150/m³**.

![[_papers/rakke2011rolling/images/page_1_image_10.jpg]]

Fig. 1. Map showing some of the main sailing lanes.

![[_papers/rakke2011rolling/images/page_2_image_17.jpg]]

Fig. 2. The LNG supply chain. The elements considered in this paper are highlighted.

## MIP formulation

Sets: gas types $\mathcal{G}$; contracts $\mathcal{C} = \mathcal{C}^{LT} \cup \mathcal{C}^{S} \cup \mathcal{C}^{M}$; ships $\mathcal{V} = \mathcal{V}^P \cup \mathcal{V}^S$ with maintenance set $\mathcal{V}^M \subset \mathcal{V}^P$ and serving set $\mathcal{V}_c$; days $\mathcal{T} = \{1..\overline{T}\}$; overlapping partitions $\mathcal{P}$ (months, quarters, whole horizon). Constants: transport cost $C^T_{cv}$, over/under-delivery penalties $C^{D+}_{cp}, C^{D-}_{cp}$, spot revenue $R^S_{ct}$, end-inventory value $R^I_g$, capacity $L_v$, voyage time $T_{cvt}$, demand $D_{cp}$, accumulated production $P_{gt}$, berths $B_g$, inventory bounds $\overline{I}_{gt}, I_{gt}$. Decision variables: binary $x_{cvt}$ (ship $v$ starts a voyage for contract $c$ on day $t$) and continuous $y^+_{cp}, y^-_{cp}$.

$$\min z = \sum_{c \in \mathcal{C}} \sum_{v \in \mathcal{V}_c} \sum_{t \in \mathcal{T}_v} C_{cv}^T x_{cvt} + \sum_{c \in \mathcal{C} \setminus \mathcal{C}^M} \sum_{p \in \mathcal{P}} C_{cp}^{D+} y_{cp}^+ + \sum_{c \in \mathcal{C} \setminus \mathcal{C}^M} \sum_{p \in \mathcal{P}} C_{cp}^{D-} y_{cp}^- - \sum_{c \in \mathcal{C}^S} \sum_{v \in \mathcal{V}_c} \sum_{t \in \mathcal{T}_v} R_{ct}^S L_v x_{cvt} - \sum_{g \in \mathcal{G}} R_g^I \left( P_{g\overline{T}} - \sum_{c \in \mathcal{C}_g \setminus \mathcal{C}^M} \sum_{v \in \mathcal{V}_c} \sum_{t \in \mathcal{T}_v} L_v x_{cvt} \right) \tag{5.1}$$

Berth constraints (5.2) count loading voyages plus the cool-down return days of maintenance voyages; inventory bounds (5.3) are modeled as **knapsack constraints** so the solver generates stronger valid inequalities ("extensive testing shows that this improves the performance"); contract balance (5.4); one voyage per ship per day (5.5); one maintenance per ship (5.6); binary and non-negative domains (5.7), (5.8). Differences vs. Stålhane et al. (2009): over-delivery cost added, spot revenue, day-dependent sailing times.

## Rolling horizon heuristic (RHH)

The full MIP is too large for commercial solvers — even finding a feasible solution is time-consuming. The RHH repeatedly solves the MIP for short time windows $TW_k = TP_k^C \cup TP_k^F$ (central period, implemented; forecasting period, simplified), freezing the binary $x_{cvt}$ in $TP_k^C$ after each solve, shifting the window, and **transferring demand deviations** from $TP_k^C$ to $TP_k^C$ of the next iteration (under-delivery increases the next central demand). Algorithm 1 (RHH, K time windows): `k=0; while (k=k+1) ≤ K: solve model for TP_k^C, TP_k^F; freeze binary x_cvt in TP_k^C; if k < K: for all c ∈ C^LT transfer deviations from TP_k^C to TP_{k+1}^C`.

![[_papers/rakke2011rolling/images/page_7_image_13.jpg]]

Fig. 3. The rolling horizon heuristic.

Design choices: **freezing** all decisions from the central period (the Mercé & Fontan 2003 strategy of freezing only production periods is not implementable at this problem size); the **forecasting period uses continuous** $0 \le x_{cvt} \le 1$ to cut computational effort (binary restrictions are re-imposed when the window shifts); the forecasting period must be short enough to be efficient yet long enough to interact with central decisions. **Solution space reduction (SSR)**: input integer $N$ generates only $1/N$ of the variables per contract, created when (day + contract number) mod $N$ = 0 — contract 3 with $N=4$ gets start days 1, 5, 9, …; this kills almost-symmetric solutions (Zanakis et al. 1989 strategy).

**Improvement heuristic**: the RHH's ADP is input to a reduced version of the model with variables only from (6.1) long-term scheduled voyages with ship swaps allowed, (6.2) spot voyages of gas $g$ re-routable to under-delivered long-term contracts $\mathcal{C}^{U*}$, (6.3) all maintenance variables, plus (6.4) $\sum_{v \in V_c} x_{cvt} = |\mathcal{S}^*_{ct}|$ keeping the number of scheduled voyages constant, solved by branch-and-bound.

Settings: central period 1 month, forecasting period 2 months (3-month window), time limits 500 s per window and 1000 s for the improvement heuristic (total < 2 h for the largest instances). Penalty design: USD **25/m³** for monthly deviations and **USD 175/m³** for annual deviations in the full model; RHH sub-problems add time-window and time-interval penalties swept from 100 to 200 in steps of 25; the best setting is **[100, 100]** (best overall in Tables 3–4, ranked with and without SSR), and SSR was slightly better, so SSR + [100,100] was used for the final tests. The improvement heuristic gave **average improvements from 2.44% to 10.20%** over all eight tested instances.

## Computational study

Four cases: A and B reflect the current situation (fewer/smaller ships, lower production, lots of excess LNG for the spot market, seasonal demands, destinations closer); C and D a future situation with all production trains, ships and docks completed; B and D are reduced versions of A and C. 16 instances (Table 1): A1–A4 = 34 ships, 5 LLNG + 3 RLNG contracts, 4 LLNG + 1 RLNG berths, horizons 366/244/182/121 days, 310–350 / 200–230 / 140–170 / 100–120 voyages needed; B1–B4 = 16 ships, 1 LLNG + 3 RLNG, 2+1 berths, same horizons, 110–140 / 75–90 / 50–70 / 40–50; C1–C4 = 46 ships, 6 LLNG + 11 RLNG, 4+1 berths, 365/243/181/120 days, 310–350 / 200–240 / 160–200 / 100–130; D1–D4 = 30 ships, 4+4 contracts, 4+1 berths, 200–240 / 130–160 / 100–130 / 70–100. Implementation: Xpress Mosel 2.4.0 with Xpress 19.00.00, single-thread, on an HP DL160 G5 cluster (Xeon QuadCore E5472 3.0 GHz, 16 GB RAM, Linux); a Dell Latitude 630 Core 2 Duo 2.5 GHz / 3.5 GB RAM / XP laptop served as the reference machine.

**Exact solution method (ESM)** ran 24 h (86,400 s) per instance with heuristics at each B&B node; no instance was solved to optimality. Table 2: gaps A1 **396.64%** (UB−LB 54,641 kUSD), A2 20.62% (20,141), A3 22.28% (8,700), A4 3.44% (2,492), B1 12.24% (2,985), B2 6.23% (3,279), B3 6.06% (1,387), B4 10.63% (2,371), C1 7.77% (112,224), C2 3.66% (37,209), C3 0.68% (5,514), C4 0.45% (2,476), D1 8.66% (74,957), D2 3.39% (21,499), D3 1.53% (7,581), D4 0.51% (1,677).

**Solution quality (Table 5)**: ESM avg gap 31.55% / avg UB−LB 22,452; RHH **10.33% / 18,873**; CIH 12.48% / 14,217. Key rows: A1 ESM 396.64% vs RHH 33.07% vs CIH 51.91%; C1 ESM 7.77% (112,224) vs RHH 6.07% (87,694) vs CIH 1.84% (26,643); D1 ESM 8.66% vs RHH 3.95% vs CIH 1.59%; B1 ESM 12.24% (2,985) vs RHH 37.27% (7,431) vs CIH 18.92%. RHH is better than CIH on 8 of 16 instances, and on 6 of the 8 real-data-based instances (cases A and C). The ESM found the best known solution on 9 of 16 instances (explained by its 86,400 s budget vs < 7200 s for RHH), but on all 12-month instances except B1 the heuristics win. Relative gaps look worse for A/B because spot revenue pushes their bounds near zero.

**Running time (Table 6)**: ESM always 86,400 s; RHH 2,015–6,626 s (A1 6,626, C1 5,854, D1 5,174, B4 2,015); CIH 23–1,587 s (fastest: B4 23 s, B3 42 s). Time until ESM beats RHH: 5 instances never (>86,400), 23,577 s (A4), 325 (B1), 207 (B2), 2,932 (B3), 128 (B4), 42,149 (C2), 14,348 (C3), 349 (C4), 82,392 (D2), 54 (D3), 326 (D4). Counting time, RHH outperforms ESM in **10 of 16** instances, and 3 of 4 on one-year horizons.

## Conclusions & future work

Five success factors for the RHH: (1) penalties are critical (extensive parameter testing); (2) central-period voyage variables should stay binary, forecasting-period ones continuous; (3) forecasting period = twice the central period; (4) SSR improves both time and quality; (5) the improvement heuristic adds 2–10%. The RHH produces high-quality ADPs for real instances in a relatively short, user-controllable time, making it well suited to a decision support system (the faster CIH of Stålhane et al. 2009 remains valuable when little time is available). Future work: exact methods with decomposition and problem-specific cuts, stronger formulations against symmetry, re-optimization of a partially fixed ADP after disruptions, robust ADPs against disruptions, contract-portfolio and asset-investment planning. Funded by the Research Council of Norway (OPTIMAR, DOMinant, Desimal Projects).

## Related

- [[concepts/annual-lng-delivery-program]] — the planning object this paper's heuristic constructs.
- [[concepts/maritime-inventory-routing-problem]] — the routing-and-inventory family this ADP model belongs to.
- [[references/gronhaug2010-branch-and-price-lng-irp]] and [[references/gronhaug2009-supply-chain-optimization-lng]] — the exact/arc-path LNG IRP work the model builds on.
- [[references/halvorsen-weare2013-lng-routing-berth-inventory]] — decomposition approach for the same loading-port ADP.
- [[concepts/time-space-network-ship-flow-model]] — related day-indexed ship-flow modeling.
- [[references/fagerholt2023-maritime-inventory-routing-survey]] — survey covering this rolling-horizon application.
- Not in the vault: the Stålhane et al. (2009) construction-and-improvement heuristic (CIH) comparison baseline.

## Sources

- [[_papers/rakke2011rolling/rakke2011rolling-extracted]]
- [[_papers/rakke2011rolling/rakke2011rolling]]
- [[_papers/rakke2011rolling/images/page_1_image_10.jpg]], [[_papers/rakke2011rolling/images/page_2_image_17.jpg]], [[_papers/rakke2011rolling/images/page_7_image_13.jpg]]
