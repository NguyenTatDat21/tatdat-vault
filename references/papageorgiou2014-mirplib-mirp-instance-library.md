---
title: "MIRPLib – A Library of Maritime Inventory Routing Problem Instances: Survey, Core Model, and Benchmark Results"
category: references
tags: [paper, maritime, inventory-routing, benchmark-library, mixed-integer-programming, time-space-network, lotsizing, discrete-time, survey, maritime-transportation]
relationships:
  - target: "[[concepts/maritime-inventory-routing-problem]]"
    type: related_to
  - target: "[[concepts/mirp-modeling-continuous-vs-discrete-time]]"
    type: related_to
  - target: "[[concepts/time-space-network-ship-flow-model]]"
    type: uses
  - target: "[[references/goel2012-large-neighborhood-search-lng-inventory-routing]]"
    type: related_to
  - target: "[[references/gronhaug2010-branch-and-price-lng-irp]]"
    type: related_to
  - target: "[[references/christiansen2013-ship-routing-scheduling-new-millennium]]"
    type: related_to
  - target: "[[references/fagerholt2023-maritime-inventory-routing-survey]]"
    type: related_to
  - target: "[[concepts/annual-lng-delivery-program]]"
    type: uses
sources:
  - _papers/papageorgiou2014mirplib/papageorgiou2014mirplib-extracted.md
  - _papers/papageorgiou2014mirplib/papageorgiou2014mirplib.md
  - _papers/papageorgiou2014mirplib/images/page_6_image_18.jpg
  - _papers/papageorgiou2014mirplib/images/page_11_image_23.jpg
  - _papers/papageorgiou2014mirplib/images/page_14_table_3.jpg
  - _papers/papageorgiou2014mirplib/images/page_13_table_4.jpg
summary: >-
  First public deep-sea MIRP benchmark library: arc-flow MILP core model on a time-space network, a 29-paper survey, unified bound techniques, and best-known gaps for 38 instance sets.
provenance:
  extracted: 0.90
  inferred: 0.07
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-26T09:12:06Z
tier: core
created: 2026-10-26T09:12:06Z
updated: 2026-10-26T09:12:06Z
---

# MIRPLib – A Library of Maritime Inventory Routing Problem Instances

> [!tldr] The first publicly available test-instance library for deep-sea maritime inventory routing: a general arc-flow MILP core model on a time-space network, a literature survey, a unified treatment of bound-improvement techniques, and best-known objective values, bounds, and optimality gaps for every instance.

## Problem & Motivation

In 2011 the international shipping industry handled over 80% of the volume of world trade; of the nearly 9 billion tons of goods in international seaborne commerce, bulk goods such as coal, crude oil, iron ore, and liquefied natural gas accounted for well over 50% and represented several hundreds of billions of US dollars (UNCTAD, 2012). The [[concepts/maritime-inventory-routing-problem]] (MIRP) is the planning problem in which an actor is responsible both for inventory management at one or both ends of the maritime transportation legs and for the ships' routing and scheduling (the definition of Christiansen et al., 2013), and IRP research grew out of vendor-managed inventory (Campbell et al., 1998).

The paper's driving complaint: despite growing interest in combined routing and inventory management, no publicly available data sets existed, which is "a significant 'barrier to entry' for those interested in related research"; Andersson et al. (2010) and Christiansen & Fagerholt (2011) both urged the community to publish benchmark data. MIRPLib was created in the spirit of TSPLib (Reinelt, 1991), MIPLib (Koch et al., 2011), ORLib (Beasley, 1990), MineLib (Espinoza et al., 2013), and LINER-LIB (Brouer et al., in press), and is maintained at mirplib.scl.gatech.edu/.

Scope is the deterministic, single-product, finite-horizon deep-sea MIRP with inventory tracking at every port: vessel travel times between ports are significantly longer than time spent in port, so port operations are not explicitly modeled; inventory bounds must hold in every time period at every loading and discharging port; the model is split-pickup and split-delivery. Strategic (1–20 years), tactical (months), and operational (weeks) planning levels, industrial, tramp, and liner shipping environments, and deep-sea vs. short-sea shipping are the three classification axes; the paper targets strategic and tactical deep-sea problems. Time-window formulations are out of scope, and ports whose inventory bounds are ignored are modeled by setting bounds to -1 and +1.

MIRP differs from road-based IRP: no single central depot, vessels travel long distances around the clock, planning horizons are longer, and vessels typically visit 3 or fewer ports in succession. MIRP differs from cargo routing, which fixes loading/discharging time windows and quantities; in a MIRP the number of port calls, quantities per call, and pickup-delivery pairings are not in the data, so the solution space — and the computational challenge — is larger.

## Core Model: Arc-Flow MILP on a Time–Space Network

The core model is a discrete-time arc-flow MILP over a time-space network first introduced in Song & Furman (2013). Nodes are port-time pairs $(j,t)$ plus a source node $n_0$ and sink node $n_{T+1}$; the node set is shared by all vessels while each vessel $v$ has its own arc set $\mathcal{A}^v$. Arc types: source arcs (vessel arrives at its initial destination), sink arcs (vessel exits the system), waiting arcs (vessel stays at the same port across consecutive periods), and travel arcs $(j_1,t_1) \to (j_2,t_2)$, $j_1 \neq j_2$; travel duration is the arc length $t_2 - t_1$ and may be time-dependent. Vessel–port incompatibilities are handled by omitting the relevant arcs. Data: berths $B_j$, arc costs $C_a^v$, per-period production/consumption bounds $D_{j,t}^{\min}, D_{j,t}^{\max}$, per-period single-vessel load/discharge bounds $F_{j,t}^{\min}, F_{j,t}^{\max}$, vessel capacity $Q^v$, unit revenue $R_{j,t}$, inventory bounds $S_{j,t}^{\min}, S_{j,t}^{\max}$, initial inventories, and the indicator $\Delta_j = +1$ for loading ports, $-1$ for discharging ports. Decision variables: production/consumption $d_{j,t}$, vessel throughput $f_{j,t}^v$, port inventory $s_{j,t}$, vessel inventory $s_t^v$, binary arc-use $x_a^v$, and binary load/discharge attempt $z_{j,t}^v$.

$$\max \sum_{n=(j,t)\in\mathcal{N}} \sum_{v\in\mathcal{V}} R_{j,t} f_{j,t}^v - \sum_{v\in\mathcal{V}} \sum_{a\in\mathcal{A}^v} C_a^v x_a^v \tag{1a}$$

$$s_{j,t} = s_{j,t-1} + \Delta_j d_{j,t} - \sum_{v\in\mathcal{V}} \Delta_j f_{j,t}^v \tag{1c}$$

Constraints (1b) vessel flow balance on every node; (1d) vessel inventory balance; (1e) berth limit $\sum_v z_{j,t}^v \le B_j$ (more vessels can sit at a port than there are berths — a berth is occupied only during loading/discharging); (1f) a vessel can attempt to load/discharge only at the node it occupies; (1g) $F_{j,t}^{\min} z \le f \le F_{j,t}^{\max} z$; (1h) production/consumption within $[D^{\min}, D^{\max}]$; (1i) port inventory within $[S^{\min}, S^{\max}]$; (1j) $0 \le s_t^v \le Q^v$; (1k)–(1l) $x,z$ binary.

The model monitors inventories only at the end of each period, with production assumed to occur before loading and consumption after discharging in a period. The paper's illustrative coarseness example: a discharging port consuming 25 units per period with capacity 250 can receive 275 units in one period (25 to cover demand, 250 to fill capacity). Objective variants appear across the literature: revenue counted at consumption ($R_{j,t} d_{j,t}$, as in Andersson et al. 2010 and Grønhaug et al. 2010), pure cost minimization (Agra et al. 2013, Al-Khayyal & Hwang 2007, Engineer et al. 2012, Uggen et al. 2013), and penalties for inventory-bound violations (Goel et al. 2012, Papageorgiou et al. submitted, Ronen 2002); inventory costs are excluded because the shipper owns both production and consumption sites.

## Side Constraints and Extensions

- **Travel-at-capacity** (2a/2b): vessels travel full from loading to discharging regions and empty from discharging to loading; justified by scarce capacity, shown not always optimal (Fodstad et al. 2010); virtually all MIRPs assume full discharge before reloading, unlike liner shipping.
- **Solution tie-breaking** (3): a negligible cost $-(t\epsilon_z) z_{j,t}^v$ prefers loading/discharging as few times as possible and as early as possible; a reward $\rho$ per unit time for early exit is built into the sink-arc cost.
- **Soft inventory bounds and spot market** (4): a per-period spot-market variable $\alpha_{j,t}$ (purchase at discharging ports, sale at loading ports) rewrites the inventory balance; single-period bound $\alpha_{j,t} \le \alpha_{j,t}^{\max}$ (5a) and cumulative bound $\sum_t \alpha_{j,t} \le \alpha_j^{\max}$ (5b) (5a/5b) cap violations. Soft bounds help with conservative data, discretization coarseness (9.5-day travel modeled as 10 days), and fleet-mix experiments.
- **Draft limits** (6a/6b): maximum permissible draft $\mathrm{DRAFT}_j^{v,\mathrm{in}}$ / $\mathrm{DRAFT}_j^{v,\mathrm{out}}$ before inlet and outlet operations, restricting which harbors fully loaded large vessels can enter.
- **Cruising speed as a decision variable**: fuel is typically 15–20% of a vessel's total annual cost (Stopford, 2008) and as much as 60% of daily cost (Ronen, 1993); a 20% speed reduction cuts daily fuel consumption by 50% (Ronen, 1993). Additional inter-port arcs spanning the travel-time interval $[\tau_{ij}^{\min}, \tau_{ij}^{\max}]$ let the solver pick the fuel-optimal average speed; the core model then solves "as-is".
- **Multiple products** (7a–7c, 8): product-specific $d, f, s$ variables with linking sums; aggregate bounds kept at port, vessel, and load/discharge levels.
- The instance data assume each port belongs to a same-type prespecified region; triangle inequality holds in the instance data (direct travel is cheaper than two legs), and a port fee is paid once per visit even across multiple attempt periods.

## Bound-Improvement Techniques

**Advanced branching.** Branching on $x$ and $z$ variables is often ineffective because of solution symmetry (a blocked arc just shifts travel to the next period). Priority branching (first applied to a MIRP by Christiansen & Nygreen, 1998) targets higher-level decisions: the number of vessels visiting a port in a time interval (Grønhaug et al. 2010, Papageorgiou Keha et al. submitted), the number of visits by a given vessel to a port (Agra et al. 2013), and the number of voyages between region pairs. Implementation: auxiliary integer variables with high branching priority, or a solver callback that writes local cuts when the visit count is fractional.

**Lot-sizing-based constraints.** The LP relaxation of the core model is weak; the standard capacitated lot-sizing set $s_{t-1} + x_t = d_t + s_t$, $0 \le x_t \le C_t y_t$, $y_t \in \{0,1\}$, $0 \le s_t \le s^{\max}$ (9a–9d) arises naturally at any single-berth discharging port with fixed demand, constant $F^{\max}$, and constant capacity. Summing over an interval gives the lot-sizing relaxation (10a–10c). Three options:
1. Continuous 0–1 knapsack set (drop the $s_t \le s^{\max}$ bound): strong valid inequalities are known (Pochet & Wolsey, 2006), but no application to MIRP is reported; a solver may use MIR cuts, flow cover cuts, and flow path cuts.
2. Binary interval inequalities (11): $\sum_{u=t_1}^{t_2} y_u \ge \lceil (d_{[t_1,t_2]} - s_{t_1-1}^{\max}) / C_{[t_1,t_2]}^{\max} \rceil$ — a minimum number of load/discharge attempts in each time interval, previously derived by logic deduction (Engineer et al. 2012, Grønhaug et al. 2010, Persson & Göthe-Lundgren 2005); the Chvátal–Gomory generalization is (12). Agra, Andersson et al. (2013) use vessel capacities $Q^v$ as coefficients.
3. Mixing-set inequalities: the mixing set $X_K^{MIX} = \{(s,y) \in \mathbb{R}_+ \times \mathbb{Z}^K : s + y_k \ge b_k\}$ (13) has $K$ simple mixed-integer rounding (SMIR) inequalities $s + f_{b_k} y_k \ge f_{b_k} \lceil b_k \rceil$ (14), valid and facet-defining but not sufficient for the convex hull when $K > 1$ — mixing inequalities are needed. The constant-capacity lot-sizing relaxation is a mixing set with network-form side constraints, so the mixing inequalities are its nontrivial facets. Engineer et al. (2012) applied a subset of SMIR inequalities ("port capacity cuts") and tightened the bound; to the authors' knowledge, no attempt at applying the mixing inequalities has been made.

A single-commodity fixed-charge network-flow reformulation with $f$ variables on arcs is much tighter than the node-based arc-flow model (Agra, Andersson, et al., 2013).

## Library Design: Formats, Data, Naming

Each instance is provided in three formats — "data only", LP, and MPS — as five files covering four data objects: metadata, loading-port data, discharging-port data, vessel-class data, and vessel data. Inventory and capacities are measured in kilotons; objective coefficients in US \$1000. All data index from 0, not 1. In all instances $\eta$ = 24 hours per period; a stated $|\mathcal{T}| = 360$ means data are defined for up to 360 periods. Metadata fields: number of periods, loading/discharging regions and ports per region, vessel classes and vessels per class, hours per period $\eta$, spot-market price $P^{\mathrm{spot}}$ and discount factor $\gamma^{\mathrm{spot}}$ (penalty $P_t = (\gamma^{\mathrm{spot}})^t P^{\mathrm{spot}}$ decreases in $t$, so spot purchases are always cheaper later), attempt cost $\epsilon_z$, reward for finishing early $\rho$, and the spot-market constants $\kappa_\alpha^1$ (per-period, $\alpha_{j,t}^{\max} = \kappa_\alpha^1 d_{j,t}$) and $\kappa_\alpha^{\mathrm{sum}}$ (cumulative, $\alpha_j^{\max} = \kappa_\alpha^{\mathrm{sum}} d_{j,0}$), e.g. 0.5 and 1, applied by pseudocode rules; a missing parameter is treated as 0.

![[_papers/papageorgiou2014mirplib/images/page_11_image_23.jpg]]

Fig. 2. Data objects.

Port data: index, type, region, x/y coordinates (Euclidean distance between ports), port fee $\pi_j \in \{10, \ldots, 100\}$ charged per visit (a visit-return-visit pattern inside a region incurs fees $\pi_j + \pi_k + \pi_j$), berth limit (discharging ports always have $B_j = 1$; fewer berths make instances more challenging), fixed $F_j^{\min}$ (roughly 50 units at discharging ports), $F_j^{\max}$ almost always greater than half the largest vessel class's capacity (and possibly larger than $S_j^{\max}$), minimum inventory 0, per-period rate lists $\{d_{j,t}\}$, revenue lists $\{R_{j,t}\}$ at discharging ports. Capacity-to-rate ratios $S_j^{\max}/\bar{d}_j$ are distinct integer values within a region to prevent periodic same-vessel visitation patterns; instances with two loading regions were built to avoid decomposable solutions.

![[_papers/papageorgiou2014mirplib/images/page_6_image_18.jpg]]

Fig. 1. Example of time–space network structure for a single vessel.

Vessel-class data: capacity $Q^{vc}$, design speed $\sigma^{vc}$ in knots, travel cost $C_{km}^{vc}$ per km, empty-leg discount $\gamma^{vc}$. Travel time $\tau_{ij}^{vc} = \lceil \eta \delta_{ij} / \sigma^{vc}_{km/h} \rceil$, where $\sigma^{vc}_{km/h}$ is the design speed converted from knots to km/h; the conversion factor occurs only as an equation crop (page_10_equation_*.jpg), not as extracted text. ^[ambiguous] Arc costs (Table 2): source arc $\pi_j$; sink arc $-(|\mathcal{T}| - t)\rho$; waiting arc 0; inter-port arc $C_{km}^{vc} \delta_{j_1,j_2} + \pi_{j_2}$, discounted by $(1-\gamma^{vc})$ on discharging-to-loading legs (a $\gamma^{vc} = 0.2$ discount trims the travel component by 20%). Calibration: a 15-knot vessel travels about 667 km/day; at US \$50,000 per day operating cost, travel cost per km is roughly US \$75. Vessels carry an initial inventory, a starting port, and a first availability time (a positive availability time means the vessel is en route); vessels starting in loading regions begin empty, those in discharging regions begin full. Voyage-chartered vessels are not in the current instances.

Instance naming (example LR2_12_DR3_123_VC4_V14c): LR2 = two loading regions, 12 = one port in the first loading region and two in the second; DR3 = three discharging regions with 1, 2, 3 ports; VC4 = four vessel classes; V14 = 14 vessels total, at least one per class; a trailing letter distinguishes sibling instances.

## Instances and Best-Known Results

Two instance groups. **Group 1**: 14 instances with 45- and 60-period horizons (tactical planning, studied with the Zoom algorithm in Papageorgiou, Keha, et al. submitted), small cumulative spot-market allowance making feasibility an issue. **Group 2**: 24 instances with 120-, 180-, and 360-period horizons (strategic planning, Papageorgiou, Cheon, et al. submitted), a single loading port, discharging ports in distinct regions, out-and-back voyages only, revenues zero (goal: minimize travel cost and spot-market usage), and infinite cumulative spot allowance. All instances enforce travel-at-capacity constraints (2a)/(2b) and use soft inventory constraints (4)/(5) in lieu of (1i). Relative gap is $(z - z^{\mathrm{Bound}})/z$; Table 3 objectives come from the Zoom algorithm, Table 4 objectives from Gurobi 5.0 for 24 hours with feasibility emphasis warmstarted by the ADP approach; best bounds for all instances come from Gurobi 5.0 for 24 hours with default emphasis and are described as "currently rather weak and, therefore, open to improvement".

![[_papers/papageorgiou2014mirplib/images/page_14_table_3.jpg]]

Best known results for Group 1 instances with a 45- and 60-period planning horizon. ^[ambiguous] Crop-to-table mapping inferred from crop naming and page order; all values are also rendered as text below.

Group 1, 45 periods (all 14 rows verbatim; Objval, Bound, Rel. Gap %, Abs. Gap):

| Instance | Objval | Bound | Rel. Gap % | Abs. Gap |
| --- | --- | --- | --- | --- |
| LR1_1_DR1_3_VC1_V7a | -13,272 | -14,410 | 8.57 | 1138 |
| LR1_1_DR1_4_VC3_V11a | -11,239 | -12,994 | 15.61 | 1755 |
| LR1_1_DR1_4_VC3_V12a | -10,732 | -12,329 | 14.89 | 1598 |
| LR1_1_DR1_4_VC3_V12b | -9069 | -9578 | 5.62 | 509 |
| LR1_1_DR1_4_VC3_V8a | -5106 | -6153 | 20.51 | 1047 |
| LR1_1_DR1_4_VC3_V9a | -6891 | -8242 | 19.60 | 1351 |
| LR1_2_DR1_3_VC2_V6a | -11,134 | -12,763 | 14.63 | 1629 |
| LR1_2_DR1_3_VC3_V8a | -12,010 | -13,625 | 13.45 | 1615 |
| LR2_11_DR2_22_VC3_V6a | -9718 | -10,802 | 11.16 | 1084 |
| LR2_11_DR2_33_VC4_V11a | -14,017 | -16,445 | 17.32 | 2428 |
| LR2_11_DR2_33_VC5_V12a | -18,423 | -20,668 | 12.18 | 2245 |
| LR2_22_DR2_22_VC3_V10a | -24,789 | -27,803 | 12.16 | 3014 |
| LR2_22_DR3_333_VC4_V14a | -21,952 | -27,216 | 23.98 | 5264 |
| LR2_22_DR3_333_VC4_V17a | -21,286 | -27,628 | 29.79 | 6342 |

Group 1, 60 periods: gaps range from 7.03% (LR1_1_DR1_3_VC1_V7a, -16,675 / -17,847, abs 1172) to 28.90% (LR1_1_DR1_4_VC3_V8a, -5191 / -6691, abs 1500); the largest absolute gap is 6909 on LR2_22_DR3_333_VC4_V17a (-27,000 / -33,909, 25.59%); the largest objective magnitude is -32,627 with bound -35,873 (gap 9.95%, abs 3246) on LR2_22_DR2_22_VC3_V10a.

![[_papers/papageorgiou2014mirplib/images/page_13_table_4.jpg]]

Best known results for Group 2 instances solved with a 120-, 180-, and 360-period planning horizon. ^[ambiguous] Crop-to-table mapping inferred from crop naming and page order; key values are rendered as text below.

Group 2, 120 periods (all 24 rows): two instances close at 0.00% gap (LR1_DR02_VC01_V6a at 33,809 and LR1_DR02_VC02_V6a at 74,982, bound equal to objective, abs 0); LR1_DR02_VC03_V8a at 43,721 / 43,717 (0.01%, abs 4). Remaining gaps: 4.86% (VC03_V7a, 40,446 / 38,482), 0.91% (VC04_V8a), 1.59% (VC05_V8a), 16.68% (DR03_VC03_V10b, 92,941 / 77,436, abs 15,505), 4.98% (VC03_V13b), 13.56% (VC03_V16a, abs 11,232), 2.38% and 13.41% (DR04_VC03_V15a/V15b), 2.10% and 21.71% (DR04_VC05_V17a: 72,876 / 71,343; V17b: 108,061 / 84,602, abs 23,459), 2.44% and 9.76% (DR05_VC05_V25a/b), 4.92%/5.34%/6.07% (DR08_VC05_V38a, V40a, V40b), 2.93%/5.25% (DR08_VC10_V40a/b), 4.27%/4.80% (DR12_VC05_V70a/b) and 3.38%/3.47% (DR12_VC10_V70a/b; largest objectives 279,526–308,555).

Group 2, 180 periods: gaps from 1.38% (LR1_DR02_VC04_V8a, 66,144 / 65,233, abs 911) to 24.61% (LR1_DR03_VC03_V16a, 159,435 / 120,195, abs 39,240); largest objective 491,160 (LR1_DR12_VC05_V70b, gap 6.16%, abs 30,280). Group 2, 360 periods: gaps from 1.15% (LR1_DR02_VC01_V6a, 108,141 / 106,901, abs 1240) to 28.54% (LR1_DR03_VC03_V10b, 261,970 / 187,202, abs 74,768); largest objective 1,093,013 (LR1_DR12_VC05_V70b) with the largest absolute gap in the library, 112,603 (bound 980,410, gap 10.30%); the tightest 360-period bound is 1,002,624 on LR1_DR12_VC10_V70a (1,024,399, gap 2.13%).

Solver barometer on the 60-period Group 1 instances, run on a Linux machine with kernel 2.6.18, a 64-bit x86 processor with two Intel Xeon E5520 chips at 2.27 gigahertz, and 48 gigabytes of RAM: Gurobi 5.0 with default emphasis on the MPS files found no feasible solution to any instance within 24 hours; after modifying the model to allow unlimited spot-market purchase with a high penalty (as in Group 2), Gurobi found truly feasible solutions to five of the instances, while the others purchased more spot-market units than permitted. The stated purpose: the core model is not ideal for generating solutions and bounds on large instances, and better models and methods are hoped for.

## Literature Survey (Table 1)

Table 1 categorizes 29 papers^[inferred] on MIRPs with inventory tracking at all ports by affiliation, application, planning level, time discretization, model family (arc-flow/path-flow), solution method, branching and valid-inequality use, and instance size (vessels $|V|$, ports $|J|$, loading/discharging ports, time periods, time unit, products). Over two-thirds of the papers are affiliated with NTNU, SINTEF, MARINTEK, ExxonMobil, or Georgia Tech; more than half connect to the petrochemical industry (crude, fuel oil, bitumen, VGO, LNG); arc-flow models are far more common than path-flow models (the authors attribute this to the enormous number of routes per vessel when no time windows exist); most instances in the literature involve fewer than 5 vessels and no more than 10 ports; roughly one-third of applications involve multiple products. Largest reported parameters include: Al-Khayyal & Hwang (2007) branch-and-price, 3+ vessels, 27 ports, 147 periods of 8 hours, 30 products; Bilgen & Ozkarahan (2007) genetic algorithm, 5 vessels, 61 ports, 28 days, 11 products; Dauzère-Pérès et al. (2007) memetic algorithm, 17 vessels, 11 ports, 84 days, 16 products; Goel et al. (2012) ADP, 70 vessels, 13 ports, 360 days; Papageorgiou, Cheon, et al. (submitted) MILP-based local search, 69 vessels, 11 ports, 365 days; Fodstad et al. (2010) and Shao et al. (submitted) instances of 181 days; Grønhaug et al. (2010) instances up to 75 time periods (with branch-and-price where the master problem handles inventory management and port capacity and subproblems generate ship-route columns). Key literature anchors: continuous-time arc-flow, [[references/christiansen2013-ship-routing-scheduling-new-millennium]], [[references/fagerholt2023-maritime-inventory-routing-survey]], [[references/goel2012-large-neighborhood-search-lng-inventory-routing]], [[references/gronhaug2010-branch-and-price-lng-irp]].

Case studies: Omya calcium carbonate slurry delivery to ten tank farms in Northern Europe (memetic algorithm); a cement producer with multi-compartment ships and non-mixable products (construction heuristic in a genetic framework); Södra Cell pulp with trucks, trains, barges, and chartered vessels (path-flow, branch-and-price); ExxonMobil VGO tramp shipping with spot charters (rich arc-flow MILP, 2-vessel local search over up to $|V|$ iterations, BPGS parallelized on four processors finding high-quality solutions in 30 minutes); Petrobras crude from platforms to terminals with full-load direct deliveries (reformulation exploiting discrete lot-sizing structure, cascading-knapsack-style tightening); Cape Verde short-sea fuel oil over 12 days with port opening-hour time windows.

## Limitations

- Best-known bounds are weak by construction; dual bounds lag primal solutions, so gaps overstate suboptimality.
- Instances are synthetic, inspired by real-world characteristics but not representing any real data set.
- Port operations, time windows, draft, speed, multi-product, and voyage chartering are modeling extensions, not part of the core instance set.
- A finite horizon invites end effects; real operations continue indefinitely.
- Deterministic data; demand rates and travel times in reality are uncertain (stochastic programming and robust optimization named as future directions; vessel speed as a lever against disruptions).
- The results snapshot reflects Gurobi 5.0-era solver power (2013); the library reports best known values, updated on the website as solutions improve.
- Sidecar date 2014-06-01 (EJOR issue date) vs. the extracted paper's "Available online 18 December 2013" and "© 2013 Elsevier" — recorded; title, authors, journal, and DOI (10.1016/j.ejor.2013.12.013) agree between sidecar and extracted.

## Related

- [[concepts/maritime-inventory-routing-problem]] — the problem class this library benchmarks; this page is its first instance source (related_to)
- [[concepts/mirp-modeling-continuous-vs-discrete-time]] — the core model is the discrete-time, end-of-period-balance side of that modeling choice (related_to)
- [[concepts/time-space-network-ship-flow-model]] — the core model is built on the time-space network introduced in Song & Furman (2013) (uses)
- [[references/goel2012-large-neighborhood-search-lng-inventory-routing]] — 70-vessel, 360-period LNG arc-flow instance family whose local-search method feeds Group 2 warmstarts (related_to)
- [[references/gronhaug2010-branch-and-price-lng-irp]] — branch-and-price for LNG-IRP with the master handling inventory and port capacity (related_to)
- [[references/christiansen2013-ship-routing-scheduling-new-millennium]] — the survey that defines the MIRP the library targets
- [[references/fagerholt2023-maritime-inventory-routing-survey]] — the later survey of the same model class
- [[concepts/annual-lng-delivery-program]] — shares inventory-routing + maritime tags with this page

## Sources

- _papers/papageorgiou2014mirplib/papageorgiou2014mirplib-extracted.md — full 841-line extracted paper text (primary)
- _papers/papageorgiou2014mirplib/papageorgiou2014mirplib.md — Zotero sidecar (title, creators, journal, date, DOI)
- _papers/papageorgiou2014mirplib/images/page_6_image_18.jpg — Fig. 1 time-space network crop
- _papers/papageorgiou2014mirplib/images/page_11_image_23.jpg — Fig. 2 data objects crop
- _papers/papageorgiou2014mirplib/images/page_14_table_3.jpg — Table 3 crop (mapping inferred)
- _papers/papageorgiou2014mirplib/images/page_13_table_4.jpg — Table 4 crop (mapping inferred)
- 53 image crops exist in _papers/papageorgiou2014mirplib/images/ (50 equation crops and page_3_table_3.jpg, page_3_table_5.jpg, page_5_table_10.jpg, page_11_table_22.jpg, page_11_table_24.jpg, page_13_table_4.jpg, page_13_table_15.jpg, page_14_table_3.jpg); all equations and tables are rendered as text in the extracted markdown, so only the four crops with caption anchors are embedded.
