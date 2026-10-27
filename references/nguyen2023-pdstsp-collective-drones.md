---
title: >-
  The Parallel Drone Scheduling Traveling Salesman Problem with Collective Drones (Nguyen & Hà, 2023)
category: references
aliases: [PDSTSP-c, collective drone TSP, Nguyen 2023 Transportation Science]
tags: [paper, pdstsp, collective-drone, makespan, milp, branch-and-cut, ruin-and-recreate, synchronization, dag-topological-sort, peukert-law, cart-sensitivity, last-mile-delivery, phenikaa]
relationships:
  - target: "[[concepts/collective-drone-delivery]]"
    type: uses
  - target: "[[concepts/peukert-law-battery-discharge]]"
    type: uses
  - target: "[[concepts/dag-topological-sort-scheduling-move-evaluation]]"
    type: uses
  - target: "[[concepts/parallel-drone-scheduling-traveling-salesman-problem]]"
    type: extends
  - target: "[[concepts/vehicle-routing-with-synchronization-constraints]]"
    type: related_to
  - target: "[[concepts/multirotor-power-model-components]]"
    type: uses
  - target: "[[concepts/large-neighborhood-search]]"
    type: uses
  - target: "[[concepts/drone-speed-selection-in-routing]]"
    type: uses
  - target: "[[references/nguyen2022-min-cost-pdsvrp]]"
    type: derived_from
  - target: "[[references/murray2015flying]]"
    type: related_to
  - target: "[[references/montemanni2024-parallel-collective-drones]]"
    type: related_to
  - target: "[[concepts/multi-objective-metaheuristic-tuning-validation]]"
    type: related_to
sources:
  - _papers/nguyen2023parallel/nguyen2023parallel-extracted.md
  - _papers/nguyen2023parallel/nguyen2023parallel.md
  - _papers/nguyen2023parallel/images/page_2_image_2.jpg
  - _papers/nguyen2023parallel/images/page_8_image_6.jpg
  - _papers/nguyen2023parallel/images/page_11_image_2.jpg
  - _papers/nguyen2023parallel/images/page_18_image_3.jpg
  - _papers/nguyen2023parallel/images/page_19_chart_2.jpg
  - _papers/nguyen2023parallel/images/page_21_image_5.jpg
  - _papers/nguyen2023parallel/images/page_22_image_2.jpg
  - _papers/nguyen2023parallel/images/page_23_image_2.jpg
  - _papers/nguyen2023parallel/images/page_28_image_10.jpg
  - _papers/nguyen2023parallel/images/page_31_chart_3.jpg
  - _papers/nguyen2023parallel/images/page_32_image_2.jpg
  - _papers/nguyen2023parallel/images/page_33_image_4.jpg
  - _papers/nguyen2023parallel/images/page_34_chart_7.jpg
summary: >-
  Nguyen & Hà define PDSTSP-c, where coupled depot drones serve heavy parcels; two-index flow MILP + RnR with a DAG topological-sort move evaluation; 23.47% average gain.
provenance:
  extracted: 0.89
  inferred: 0.08
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-26T05:12:09Z
tier: supporting
created: 2026-10-26T05:12:09Z
updated: 2026-10-26T05:12:09Z
---

# The Parallel Drone Scheduling Traveling Salesman Problem with Collective Drones

> [!tldr] **Nguyen & Hà (Transportation Science, 2023, DOI 10.1287/trsc.2022.1192)** formalize **PDSTSP-c**: multiple homogeneous drones at the depot can be *coupled* into a [[concepts/collective-drone-delivery|collective drone]] (c-drone) to carry parcels too heavy or too distant for a single drone. A two-index flow MILP solved by branch-and-cut handles small instances; a [[concepts/large-neighborhood-search|Ruin-and-Recreate]] metaheuristic with a [[concepts/dag-topological-sort-scheduling-move-evaluation|DAG topological-sort move evaluation]] scales to 200 customers. Across 1000 sensitivity samples c-drones improve makespan by **23.47%** on average (best leaf **32.33%**, best individuals **58.78%**, worst leaf **10.33%**) and cut truck mileage by **33.21%** on average.

## Problem & motivation

![[_papers/nguyen2023parallel/images/page_2_image_2.jpg]]
*Figure 1 A top-down view of a collective drone configuration in Paczan et al. (2016)*

The standard assumption in truck-drone literature is that a single drone's payload and range are hard-capped by battery capacity — Amazon's delivery drone drops 5 lb within 10 miles of a fulfillment centre (Boyle 2016). Paczan et al. (2016) patent a **collective UAV**: several drones couple into one body, sharing power and operating instructions. Coupling has two effects: (i) payload and range are pooled, so "virtually any size, weight or quantity of items" can be flown; (ii) coupled units may *reduce motor rotational speed*, borrowing lift from the collective body, which lowers energy per unit. A side effect is safety: the coupled body is larger, generates a bigger radar/object signature, and is more detectable by ground radar and air-traffic controllers.

Endurance is not constant. Power consumption is nonlinear in speed and payload, so a drone's achievable range *increases* with speed at low speeds and *decreases* at high speeds (Raj et al. 2021). The paper adds two further endurance effects beyond Raj et al. (2021): the **[[concepts/peukert-law-battery-discharge|Peukert effect]]** (a faster discharge yields less usable capacity) and a **maximum discharge current** threshold that protects battery lifespan, plus an efficiency-loss factor for wind resistance and battery degradation. Cruise speeds are *not* decision variables: they are pre-computed per (payload, distance, k) to minimize flight time subject to the battery constraints.

PDSTSP-c is materially harder than the PDSTSP of Murray & Chu (2015). In PDSTSP the order in which a drone serves its customers is irrelevant; here a **[[concepts/drone-swarm-synchronization|synchronization constraint]]** requires all k units of a c-drone to be assembled at the depot before launch, so the order of services in one drone tour changes the start times available to other tours. A change in one drone tour propagates to others, which is the main reason the PDSTSP heuristics must be redesigned. ^[inferred]

**Contributions** (verbatim list): a new PDSTSP variant using collective drones; a MILP solved to optimality on small instances; the Ruin-and-Recreate metaheuristic; and the first PDSTSP-c benchmark set (published at `http://orlab.com.vn/home/download`).

Positioning in the scheduling literature: multiprocessor task scheduling with parallel tasks (MTSP, Kwok & Ahmad 1999; Blazewicz et al. 1986) and the vehicle routing problem with synchronization constraints (VRPSC — Afifi, Dang & Moukrim 2016; Grimault et al. 2017; Liu, Tao & Xie 2019; Hà et al. 2020). VRPSC differs: it carries time windows, minimizes total operating cost, allows at most two synchronized vehicles, and synchronizes at customer locations, whereas PDSTSP-c synchronizes at the depot and minimizes makespan. ^[inferred]

Predecessor heuristics for PDSTSP: Mbiadou Saleu et al. (2018, coding/decoding with a bi-criteria shortest path via dynamic programming), Dell'Amico, Montemanni & Novellani (2020, matheuristic using an MILP decoder), Dinh, Do & Hà (2021, HACO on a giant tour with dynamic programming under controllable states), Nguyen et al. (2022, Ruin-and-Recreate — the best PDSTSP metaheuristic, also for a min-cost multi-truck variant). Raj et al. (2021) handles multiple trucks with three MILP formulations, branch-and-price and a BAP heuristic, on instances up to 229 customers. ^[inferred]

## Model and formulation

Graph $\mathcal{G}=(\mathcal{N},\mathcal{E})$ with $\mathcal{N}=\{0,1,\dots,n\}$; node 0 is the depot, $\mathcal{C}$ is the customer set, parcel $i$ weighs $w_i$. One driver-operated truck (one closed tour, unlimited capacity and range, average speed $V_t=30$ km/h, Manhattan travel) and $m$ homogeneous drones at the depot (battery capacity $C_{nom}$, Euclidean flight, back-and-forth depot-to-customer trips). $\mathcal{C}_F\subseteq\mathcal{C}$ is the drone-eligible request set (distance and weight suitable), $\mathcal{C}_T=\mathcal{C}\setminus\mathcal{C}_F$ is truck-only, $\mathcal{C}_{F0}=\mathcal{C}_F\cup\{0\}$. A "k-unit c-drone" covers both a single drone ($k=1$) and at least two coupled drones ($k>1$); the payload is evenly distributed, so each unit carries $\bar w_i=w_i/k$. Each drone serves one parcel per flight.

**Flight time.** A sortie has six phases (takeoff, cruise in, landing, parcel delivery, takeoff, cruise out, landing); vertical speed is not controllable through MAVLink, so $v^{to}$ and $v^{ld}$ are fixed at 2 m/s over the 100 m cruise altitude.

$$\tau_j^k = t'_C + (\tau^{to} + \tau_{jk}^{in} + \tau^{ld}) + (\tau^{to} + \tau_{jk}^{out} + \tau^{ld}),\qquad \tau_{jk}^{in}=\frac{d_{0j}}{v_{jk}^{in}},\ \tau_{jk}^{out}=\frac{d_{0j}}{v_{jk}^{out}} \tag{1}$$

with $t'_C$ the coupling time, not added when $k=1$. The text states $t'_C = 1$ minute; Table 5 lists "C-drone preparation time | s | 1", which conflicts with the text — a unit mismatch in the paper's own tables. ^[ambiguous]

![[_papers/nguyen2023parallel/images/page_8_image_6.jpg]]
*Figure 2 Different flight phases consume different powers*

**Endurance feasibility (constraints 2–4).** With $I_i = P_i/V_{nom}$ per phase $i$:

- (2) $I_i \le I_{max}$ for all $1\le i\le 6$ — protects battery lifespan; blocks overloaded parcels and excessive speeds.
- (3) **Peukert's law** (Doerffel & Sharkh 2006): $C_d=\sum_{i=1}^{6} I_{eff,i}\Delta t_i=\sum_{i=1}^{6}\left[I_i\left(\frac{I_i}{I_{nom}}\right)^{p-1}\Delta t_i\right]$, with Peukert exponent $p=1.1$ and $I_{nom}$ the nominal current of the manufacturer capacity (1C rate).
- (4) $C_d \ge \beta\,C_{nom}$ with efficiency-loss factor $\beta<1$ (set to 0.9 in experiments).

If (2) or (4) is violated, that k-unit configuration cannot transport the parcel.

**Two-index MILP.** A three-index formulation over (edge, drone) was rejected in preliminary experiments: too many variables plus symmetry among identical drones makes branch-and-bound perform poorly. Decision variables:

| Variable | Meaning |
|---|---|
| $x_{ij}\in\{0,1\}$, $i<j$ | truck uses edge $(i,j)$ |
| $z_j^k\in\{0,1\}$ | request $j$ served by a k-unit c-drone, $k\in[q_j,p_j]$ (min required / max allowed, e.g. by safety regulation) |
| $u_i\in\{0,1\}$ | node $i$ served by the truck |
| $y_{ij}\in\{0,1\}$ | $i$ is serviced before $j$ in some drone schedule |
| $f_{ij}\in\mathbb{R}^+$ | number of drone units flowing from $i$ to $j$ |
| $T_i\in\mathbb{R}^+$ | time request $i$ begins to be serviced (right before coupling, battery swap and loading) |
| $Z\in\mathbb{R}^+$ | makespan |

Objective $\min Z$ with constraints (6)–(22):

$$\min\ Z \tag{5}$$
$$Z \ge \sum_{i<j} t_{ij}x_{ij} \tag{6}$$
$$Z \ge T_j+\sum_{q_j\le k\le p_j}\tau_j^k z_j^k\quad \forall j\in\mathcal{C}_F \tag{7}$$
$$u_j+\sum_{q_j\le k\le p_j}z_j^k=1\quad\forall j\in\mathcal{C}_F \tag{8}$$
$$u_j=1\quad\forall j\in\mathcal{C}_T\cup\{0\} \tag{9}$$
$$\sum_{i<j}x_{ij}+\sum_{j<k}x_{jk}=2u_j\quad\forall j\in\mathcal{C}_F \tag{10}$$
$$|S|\sum_{i\in S,\,j\notin S}x_{ij}\ge 2\sum_{l\in S}u_l\quad\forall S\subseteq\mathcal{C},\ |S|\ge 3 \tag{11}$$
$$\sum_{j\in\mathcal{C}_F}f_{0j}\le m \tag{12}$$
$$\sum_{i\in\mathcal{C}_{F0},\,i\ne j}f_{ij}=\sum_{q_j\le k\le p_j}k\,z_j^k\quad\forall j\in\mathcal{C}_F \tag{13}$$
$$\sum_{i\in\mathcal{C}_{F0},\,i\ne j}f_{ji}=\sum_{q_j\le k\le p_j}k\,z_j^k\quad\forall j\in\mathcal{C}_{F0} \tag{14}$$
$$\frac{f_{ij}}{m}\le y_{ij}\le f_{ij}\quad\forall(i,j)\in\mathcal{C}_{F0},\ i\ne j \tag{15}$$
$$T_j+M(1-y_{ij})\ge T_i+\sum_{q_j\le k\le p_j}\tau_j^k z_j^k\quad\forall i\in\mathcal{C}_{F0},\ j\in\mathcal{C}_F,\ i\ne j \tag{16}$$

with $0\le f_{ij}\le m$, binary $u,x,z,y$, $T_i\ge 0$ (17)–(22), and $M$ a sufficiently large constant. Constraint (11) is the subtour elimination (at least two edges between $S$ and $V\setminus S$ for every set containing a truck-visited vertex); (12) is the fleet limit leaving the depot; (13)–(14) are flow conservation; (15) links the ordering indicator to the flow; (16) is the **synchronization/ordering** constraint — $j$ cannot start before every predecessor $i$ has finished.

The drone part is read as a directed acyclic flow graph:

![[_papers/nguyen2023parallel/images/page_11_image_2.jpg]]
*Figure 3 An graph-based representation of a drone schedule*

In the paper's example, arcs $(0,2),(0,1),(0,3)$ start at $t=0$; $f_{01}=2$ means node 1 needs two drones; services at 4 (needs 1 and 2 finished) and 5 (needs 1 and 3 finished) are synchronized; node 6 receives $f_{56}=2$ and $f_{46}=1$, i.e. three drones; returns are $f_{40}=1$, $f_{60}=3$; the makespan is $\max(10+7,\,17+6)=23$.

**Solution extraction (Algorithm 1).** Build $\bar{\mathcal{G}}=(V^*,E^*)$ from $(y,f)$, where $V^*$ is the set of vertices serviced by drones and $E^*$ contains arcs with cost $f_{ij}$; constraint (16) guarantees it is a DAG. Topologically order it with a depth-first-search sort; for each node $i$ in that order, the assigned tours $D_i$ are those containing any parent $j\in P_i$ (any empty drone if $j=0$); the start time $t_i=\max\sigma_k$ over $k\in D_i$; $dc_i$ is the $k$ with $z_i^k=1$; append $i$ to each tour in $D_i$ and set $\sigma_k=t_i+\tau_i^{dc_i}$. Returns the drone tours and start times.

**Power model (Eqs. 23–25, coefficients from Liu, Sengupta & Kurzhanskiy 2017 via Raj et al. 2021).**

$$P^{tl}(\bar w,v_v)=k_1(W+\bar w)g\Big[\frac{v_v}{2}+\sqrt{\Big(\frac{v_v}{2}\Big)^2+\frac{(W+\bar w)g}{k_2^2}}\Big]+c_2\big((W+\bar w)g\big)^{3/2} \tag{23}$$

$$P^{c}(\bar w,v_h)=(c_1+c_2)\big[((W+\bar w)g-c_5(v_h\cos\alpha)^2)^2\big]^{3/4}+c_4v_h^3 \tag{24}$$

$$\tan\alpha\big[(W+\bar w)g-c_5(v_h\cos\alpha)^2\big]=c_4v_h^2 \tag{25}$$

$W$ = drone frame + battery weight, $\alpha$ = forward tilt (angle of attack), solved by simple iteration.

**Optimal cruise speeds (Algorithm 2).** Initialize $(v^*_{in},v^*_{out})=\text{null}$, $\bar w_i=w_i/k$; evaluate the four vertical takeoff/landing phases first (loaded outbound, empty inbound), and return null immediately if a battery constraint is violated; then enumerate every pair $(v_{in},v_{out})$ in $[v_{min},v_{max}]=[4.00,28.00]$ m/s with a 0.2 m/s step, keeping the pair that minimizes $d_{0i}/v_{in}+d_{0i}/v_{out}$ among battery-feasible pairs.

**Cutting planes.** Solve the LP relaxation of (5)–(22) without connectivity constraints (11); search for violated (11), add them, reoptimize; branch on fractional variables. Subtour separation is heuristic: from LP values $u^*,x^*$ build $G^*=(V^*,E^*)$ with $V^*=\{i:u_i^*>0\}$, $E^*=\{(i,j):x^*_{ij}>0\}$; the parametric connectivity procedure of Applegate et al. (2003) records relevant sets $S\subseteq\mathcal{C}$ in a disjoint-set structure; if at least two sets exist, every set not containing the depot yields a SEC (11). Implementation: C++ GCC 9.3.0, branch-and-cut around CPLEX 12.10; Kubuntu 20.04, AMD Ryzen 3700X @ 4.0 GHz, 32 GB RAM.

## Ruin-and-Recreate metaheuristic

RnR extends Large Neighborhood Search (Shaw 1998) and the ruin-and-recreate principle (Schrimpf et al. 2000), with **Threshold Acceptance**:

$$|C_r| = q_t+q_d=\lfloor U(1,\lambda|C_s^{truck}|)\rfloor+\lfloor U(1,\lambda|C_s^{drone}|)\rfloor \tag{26}$$

one random truck removal operator plus one random drone removal operator per iteration; accept the recreated solution if $\mathrm{cost}(s)<\mathrm{cost}(s^*)\cdot(1+\Delta)$, then run local search; cool $\Delta\leftarrow\Delta\cdot\varepsilon$; stop at $Iter_{max}$ / time limit.

Six removal operators. Truck: **random** (keep the order of the rest), **worst** (remove the $q_t$ requests with the most expensive insertion cost, insertion cost = objective difference with/without the request), **string** (a sub-string of $q_t$ requests from a random seed position, wrapping around when the string runs past the end, removing two portions). Drone: **random** (the whole schedule structure is updated after each removal), **sweep** (from Nguyen et al. 2022: depot as pole, random seed angle $\theta_{seed}\in U(0^\circ,360^\circ)$, sort drone requests by polar angle to the seed line, remove the $q_d$ closest) and **block** — a new operator motivated by the observation that dispersed removals leave isolated idle-time gaps that are hard to refill without degrading quality: sort drone requests by service start time, pick a random time interval containing at least $q_d$ services, and remove requests from the start time onward, which removes a block that is adjacent in the schedule.

![[_papers/nguyen2023parallel/images/page_18_image_3.jpg]]
*Figure 4 An example of Sweep Removal*

![[_papers/nguyen2023parallel/images/page_19_chart_2.jpg]]
*Figure 5 An illustration of Block Removal in comparison with Random Removal*

**Recreation (Algorithm 4).** Shuffle the ejected requests; for each, find the cheapest truck position and, if drone-eligible, the cheapest drone position, and insert at the cheaper; insertion cost $=\max(T_i')-Z$ where $T_i'$ is the tour completion time after insertion. Solution construction is the same procedure with all requests ejected.

**Drone insertion (Algorithm 5).** Candidate start times $F=\{0\}\cup\{$ completion times of serviced requests $\}$; choose $k$ randomly in $[q_i,p_i]$; for each $t\in F$ select the $k$ best drones by **rank-based roulette-wheel selection** (Whitley 1989) to keep diversity when several drones share the same slack; approximate the resulting tour time

$$T_k' = T_k+\max(0,\ \tau_i-\delta(t)) \tag{27}$$

where $\delta(t)=ST(j)-t\ge 0$ is slack time when $t$ falls in an idle interval before the next request $j$, and $\delta(t)=ST(l)-t<0$ is extra delay when $t$ falls inside an ongoing delivery $l$. Best move = shortest resulting makespan, tie-broken by the shortest total service time of all carriers.

![[_papers/nguyen2023parallel/images/page_21_image_5.jpg]]
*Figure 6 An illustration of δ(t) values in two insertion scenarios*

In the figure's example, drone 2 has the shortest total service time, but inserting at $t$ delays request $l$ seriously; drone 1 is far cheaper thanks to its slack time even though it has the longest total service time.

**Move evaluation.** Inserting a synchronized request postpones many later services across several tours (a chain reaction): inserting request 8 into drones 3 and 4 at $t$ postpones requests 2, 3, 4, 5, which in turn delay 6 and 7 on drones 1, 2, 5. Constant-time evaluation is only possible after the last request of a tour, so the algorithm maintains a per-solution DAG $\bar{\mathcal{G}}=(\bar V,\bar A)$: for each $k\in K$ find the precedent $v_j$ and successive $v_j'$ with $FT(v_j)\le t\le FT(v_j')$; delete arc $(v_j,v_j')$, add inbound arc $(v_j,v_i)$ and outbound arc $(v_i,v_j')$; if no request follows $t$ only the inbound arc is added, if none precedes $t$ only the outbound arc. Re-topologically order $\bar{\mathcal{G}}'$ by a DFS-based sort in $O(|\bar V|+|\bar A|)$ and recompute the makespan by replaying the requests in that order.

![[_papers/nguyen2023parallel/images/page_22_image_2.jpg]]
*Figure 7 An example of inserting a synchronized request into the middle of a drones' schedule*

![[_papers/nguyen2023parallel/images/page_23_image_2.jpg]]
*Figure 8 A demonstration of the move evaluation procedure*

**Local search.** Composite neighborhood with first-improvement acceptance, using Relocate, Swap and 2-Opt on the **truck tour only** — drone-schedule moves are too expensive to use as local-search operators. It terminates when no improving move exists. Parameters are tuned with **irace** (López-Ibáñez et al. 2016, default setting, at most 1000 algorithm runs during tuning) on instances perturbed by 10% in $x,y$ coordinates and parcel weight $w_i$, over ranges $\lambda,\Delta_{init}\in[0.1,0.8]$, $\varepsilon\in[0.99,0.99995]$, $Iter_{max}\in[5000,50000]$.

| Parameter | RnR-fast | RnR |
|---|---|---|
| $\lambda$ | 0.55403 | 0.21540 |
| $\Delta_{init}$ | 0.67317 | 0.39909 |
| $\varepsilon$ | 0.99889 | 0.99876 |
| $Iter_{max}$ | 45496 | 46138 |

**RnR-fast** is the reference variant that skips the move evaluation, inserting requests only after the last request of a drone tour.

## Instance families

Generated following Uchoa et al. (2017) and Nguyen et al. (2022): $n\in[15,200]$, small set $15\le n\le 30$, large set $50\le n\le 200; requests in a 15×15 square with three distributions — Random (r), Clustered (c), Random-Clustered (rc); depot Central (c) at $(15/2,15/2)$ or Eccentric (e) at $(\min x,\min y)$; $m\in[3,6]$ small, $m\in[5,10]$ large. 30 instances per problem set, named `n-rd-dp`. Truck 30 km/h with Manhattan distance, drones Euclidean, coupling 1 minute, battery swap / loading / unloading negligible, travel times rounded up to the nearest integer. Exact method limited to 1 hour (3600 s); each heuristic run 30 times per instance.

### Small instances (Table 2)

Rows whose label ends with "-" are the 10 instances where the exact method fails to match the best heuristic solution. Gap for heuristics is $100(Z'/Z_{best}-1)$; `gap_i` is the average gap of initial solutions.

| Data | MILP Z | MILP gap % | MILP time s | RnR-fast Z | gap % | time s | RnR Z | gap % | time s | gap_i % |
|---|---|---|---|---|---|---|---|---|---|---|
| 15-r-e | 92 | 0.00 | 8.65 | 92 | 0.00 | 0.32 | 92 | 0.00 | 0.95 | 13.95 |
| 15-rc-c | 44 | 38.64 | 3600.00 | 44 | 0.15 | 0.43 | 44 | 0.00 | 1.46 | 43.18 |
| 16-c-c | 60 | 0.00 | 2.61 | 60 | 0.00 | 0.52 | 60 | 0.00 | 2.14 | 20.94 |
| 16-r-e | 112 | 0.00 | 63.86 | 112 | 0.00 | 0.55 | 112 | 0.00 | 1.52 | 10.06 |
| 18-rc-c | 57 | 50.88 | 3600.00 | 58 | 4.80 | 0.54 | 57 | 0.00 | 2.40 | 52.75 |
| 18-c-c | 56 | 44.64 | 3600.00 | 56 | 0.00 | 0.42 | 56 | 0.00 | 1.86 | 48.27 |
| 18-r-e | 96 | 10.42 | 3600.00 | 96 | 0.00 | 0.59 | 96 | 0.00 | 1.79 | 34.06 |
| 19-c-c | 44 | 56.82 | 3600.00 | 44 | 0.00 | 0.48 | 44 | 1.36 | 1.81 | 58.79 |
| 20-r-c | 64 | 15.62 | 3600.00 | 64 | 0.00 | 0.43 | 64 | 0.00 | 1.91 | 36.20 |
| 20-c-c- | 44 | 41.99 | 3600.00 | 43 | 1.47 | 0.60 | 43 | 0.00 | 2.54 | 51.94 |
| 20-rc-e | 100 | 0.00 | 88.78 | 100 | 0.00 | 0.46 | 100 | 0.00 | 1.09 | 11.97 |
| 20-rc-c | 96 | 0.00 | 0.90 | 96 | 0.00 | 0.41 | 96 | 0.00 | 2.37 | 14.79 |
| 20-r-e- | 88 | 40.59 | 3600.00 | 82 | 4.50 | 0.62 | 80 | 0.83 | 2.00 | 37.42 |
| 21-c-c- | 64 | 53.12 | 3600.00 | 62 | 2.15 | 0.48 | 62 | 1.77 | 2.25 | 18.82 |
| 21-r-e- | 100 | 68.00 | 3600.00 | 85 | 2.78 | 0.59 | 85 | 0.90 | 1.74 | 28.27 |
| 23-r-c | 88 | 0.00 | 3293.16 | 88 | 0.00 | 0.42 | 88 | 0.04 | 1.83 | 23.18 |
| 23-c-e | 80 | 37.58 | 3600.00 | 80 | 0.00 | 0.60 | 80 | 0.00 | 2.49 | 5.58 |
| 24-rc-c- | 88 | 26.47 | 3600.00 | 72 | 1.41 | 0.73 | 71 | 1.27 | 4.06 | 41.88 |
| 24-r-e | 112 | 23.01 | 3600.00 | 112 | 0.00 | 0.52 | 112 | 0.00 | 1.57 | 23.99 |
| 24-c-e | 84 | 7.14 | 3600.00 | 84 | 0.00 | 0.79 | 84 | 0.00 | 2.50 | 25.60 |
| 25-rc-e- | 100 | 49.28 | 3600.00 | 92 | 2.86 | 0.71 | 92 | 1.23 | 2.25 | 38.66 |
| 25-r-e- | 120 | 57.67 | 3600.00 | 106 | 3.78 | 0.96 | 104 | 3.11 | 3.14 | 34.94 |
| 25-c-c | 56 | 50.00 | 3600.00 | 56 | 0.00 | 0.60 | 56 | 0.00 | 2.92 | 42.80 |
| 26-r-c- | 128 | 34.37 | 3600.00 | 103 | 0.78 | 0.53 | 103 | 0.13 | 2.58 | 32.56 |
| 27-c-e | 68 | 61.76 | 3600.00 | 68 | 0.00 | 0.72 | 68 | 0.00 | 6.27 | 4.71 |
| 27-c-c | 84 | 0.93 | 3600.00 | 84 | 0.00 | 0.49 | 84 | 0.00 | 2.18 | 4.92 |
| 27-rc-e- | 100 | 68.00 | 3600.00 | 84 | 0.00 | 0.79 | 84 | 0.00 | 2.70 | 30.91 |
| 27-rc-c | 100 | 0.00 | 721.25 | 100 | 0.00 | 0.77 | 100 | 0.00 | 5.30 | 17.13 |
| 29-rc-e- | 124 | 26.91 | 3600.00 | 116 | 0.00 | 0.72 | 116 | 0.00 | 1.69 | 30.14 |
| 30-c-c | 96 | 14.58 | 3600.00 | 96 | 0 | 0.65 | 96 | 0 | 3.76 | 4.65 |

Exact method: competitive on 20 instances, optimal on 7 (gap 0.00: 15-r-e, 16-c-c, 16-r-e, 20-rc-e, 20-rc-c, 23-r-c, 27-rc-c), fails on 10. Largest MILP gaps at the 3600 s limit: 68.00% (21-r-e, 27-rc-e), 61.76% (27-c-e), 57.67% (25-r-e), 56.82% (19-c-c), 53.12% (21-c-c), 50.88% (18-rc-c), 50.00% (25-c-c). RnR gaps are always below 5% (max 3.11%); RnR beats RnR-fast on 4 instances (20-c-c, 20-r-e, 24-rc-c, 25-r-e); average runtime under 6 s for RnR and under 1 s for RnR-fast; initial-solution gaps range from 4.65% (30-c-c) to 58.79% (19-c-c). The authors read this as a **ceiling effect**: small instances are too easy to separate the two heuristics.

### Large instances (Table 3)

`gap` for RnR-fast is the average gap of its best solutions to the best solutions found by all methods over 30 runs; RnR's `gap` is reported because the paper prints gap values for both, with bold Z marking the winner.

| Data | RnR-fast Z | gap % | gap_i % | time s | RnR Z | gap % | time s | gap_i % |
|---|---|---|---|---|---|---|---|---|
| 50-r-e | 120 | 3.45 | 7.93 | 2.45 | **116** | 6.21 | 20.00 | 45.89 |
| 53-r-e | 136 | 3.03 | 6.36 | 2.23 | **132** | 2.45 | 15.17 | 48.31 |
| 66-rc-e | 128 | 3.23 | 6.24 | 3.13 | **124** | 4.95 | 16.61 | 47.66 |
| 67-c-c | 76 | 0.00 | 0.00 | 2.32 | 76 | 0.92 | 29.05 | 18.60 |
| 68-rc-c | 79 | 3.95 | 8.99 | 2.12 | **76** | 0.00 | 20.45 | 79.87 |
| 76-c-c | 52 | 0.00 | 0.00 | 2.15 | 52 | 0.00 | 10.46 | 11.79 |
| 82-c-e | 64 | 0.00 | 0.00 | 2.63 | 64 | 0.00 | 18.07 | 6.46 |
| 82-rc-c | 108 | 3.85 | 5.77 | 2.65 | **104** | 2.95 | 27.42 | 68.78 |
| 88-c-e | 108 | 0.00 | 0.00 | 3.56 | 108 | 0.00 | 9.62 | 11.11 |
| 91-r-c | 128 | 3.23 | 6.99 | 3.64 | **124** | 0.86 | 72.49 | 57.39 |
| 99-rc-c | 108 | 8.00 | 11.73 | 3.64 | **100** | 6.13 | 51.21 | 72.67 |
| 101-r-c | 124 | 3.33 | 7.83 | 3.98 | **120** | 0.89 | 99.71 | 59.58 |
| 103-rc-c | 128 | 3.23 | 6.88 | 4.38 | **124** | 4.41 | 94.25 | 50.54 |
| 105-rc-e | 124 | 3.33 | 4.81 | 5.78 | **120** | 1.78 | 62.71 | 53.47 |
| 108-rc-e | 144 | 5.88 | 7.60 | 5.56 | **136** | 2.45 | 61.71 | 63.46 |
| 114-rc-c | 100 | 4.17 | 9.55 | 4.69 | **96** | 4.31 | 62.73 | 73.68 |
| 121-rc-e | 128 | 3.23 | 9.84 | 6.41 | **124** | 6.56 | 68.74 | 61.51 |
| 126-r-c | 161 | 0.63 | 6.25 | 5.89 | **160** | 2.50 | 120.93 | 51.42 |
| 126-rc-e | 148 | 2.78 | 3.59 | 7.38 | **144** | 1.94 | 71.04 | 51.83 |
| 144-rc-c | 132 | 3.12 | 6.46 | 6.52 | **128** | 6.25 | 172.75 | 58.96 |
| 154-c-c | 72 | 0.00 | 0.00 | 7.17 | 72 | 0.00 | 62.96 | 2.04 |
| 165-r-c | 176 | 7.32 | 13.17 | 7.61 | **164** | 1.54 | 280.18 | 60.39 |
| 167-r-e | 200 | 6.38 | 9.61 | 10.55 | **188** | 3.12 | 228.31 | 55.67 |
| 173-rc-c | 144 | 8.27 | 11.68 | 9.22 | **133** | 4.59 | 135.20 | 64.36 |
| 173-r-c | 180 | 9.76 | 14.96 | 8.64 | **164** | 5.45 | 373.43 | 63.35 |
| 181-r-e | 232 | 3.57 | 8.02 | 11.20 | **224** | 1.90 | 196.09 | 45.85 |
| 185-c-c | 96 | 0.00 | 0.00 | 11.26 | 96 | 0.00 | 61.53 | 5.97 |
| 187-rc-e | 200 | 2.04 | 7.70 | 12.67 | **196** | 3.27 | 119.95 | 49.56 |
| 198-c-c | 64 | 0.00 | 0.00 | 11.38 | 64 | 0.00 | 94.12 | 11.46 |
| 200-r-e | 224 | 5.66 | 10.66 | 13.88 | **212** | 2.14 | 368.97 | 53.40 |

RnR finds the best solution on **23 of 30** instances; RnR-fast's best-solution gap reaches **14.96%** (173-r-c: 180 vs 164). RnR runtimes reach **373.43 s** (173-r-c) and **368.97 s** (200-r-e) — over six minutes on 200-request instances — while RnR-fast never exceeds **14 s** (13.88 s at 200-r-e). Initial-solution gaps exceed 70% (79.87% at 68-rc-c, 73.68% at 114-rc-c, 72.67% at 99-rc-c, 68.78% at 82-rc-c), confirming the impact of the move evaluation; on clustered instances the initial gaps are much smaller (2.04% at 154-c-c, 5.97% at 185-c-c, 6.46% at 82-c-e). **RnR-fast is recommended when decisions must be made quickly.**

## Sensitivity analysis (CART)

Five research questions: which (weight, distance) requests are c-drone eligible; how competitive c-drone systems are against the truck + single-drone system and how the benefit varies; how large the depot coverage area suitable for c-drone operations is; whether adding extra drones is necessary for the boost; whether improving battery capacity helps significantly.

![[_papers/nguyen2023parallel/images/page_28_image_10.jpg]]
*Figure 9 The process of sensitivity analysis using CART method*

**Why CART (Breiman, Friedman, Olshen & Stone 1984) rather than one-factor-at-a-time:** OFAT varies one variable at a time, so it cannot detect interaction effects between predictors, and its factorial-design basis becomes impractical for multiple factors. CART grows a binary decision tree that exposes interactions. Predictor variables: $D$ (depot coverage dimension), $b$ (battery model), $m$ (number of drones), and the $(w,d)$ request profile. Classification is run with scikit-learn's `DecisionTreeClassifier` after the energy model labels every request; regression uses `DecisionTreeRegressor` on the performance gain ^[inferred]

$$\text{gain}=100\cdot\frac{Z-Z'}{Z}$$

where $Z'$ is the makespan with c-drones and $Z$ the makespan of the equivalent system without them. Truck mileage reduction is $100(X/X_c-1)$, $X_c$/$X$ being truck distance with and without c-drones.

![[_papers/nguyen2023parallel/images/page_31_chart_3.jpg]]
*Figure 10 Visualization of the three considered package weight distributions*

**Data.** Cruise speeds $[4.00, 28.00]$ m/s from Algorithm 2; truck 30 km/h (day-average speed of medium-duty urban trucks, Sanchez-Diaz et al. 2020) with Manhattan distance, drones Euclidean; one minute of coupling regardless of the number of units; commercial operation under FAA rules — UPS obtained Part 135 authority (Etherington 2019), Part 135 permits drone + cargo above 25 kg (FAA 2019), and Part 107 safety rules cap the combined weight at 25 kg, so the largest c-drone has 6 units. Fleet size $m$ varies 5–20; request count per instance is drawn from $[50,400]$; locations are clustered randomly in a $D\times D$ km grid with the depot at the centre $(D/2,D/2)$. Package weight distributions: Amazon (86% of parcels ≤ 2.27 kg, Bezos via Guglielmo 2013) and the Commodity Flow Survey (U.S. Census Bureau 2015) restricted to "Electronic shopping and mail-order houses", truck mode, shipments ≤ 68 kg (150 lb); both are right-skewed, CFS heavier on the tail.

| Model ID | Capacity (Ah) | Weight (kg) | Max discharge current (A) | Nominal voltage (V) |
|---|---|---|---|---|
| 0 | 7.5 | 1.08 | 15 | 12.8 |
| 1 | 12 | 1.55 | 24 | 12.8 |
| 2 | 20 | 2.80 | 40 | 12.8 |
| 3 | 30 | 3.44 | 45 | 12.8 |

Constants (Table 5): c-drone preparation time 1 s (see the unit conflict noted above ^[ambiguous]); maximum c-drone size 6 units; maximum combined weight 25 kg; drone frame weight 1.2 kg; 4 propellers; rotor blade radius 0.15 m; Peukert constant 1.1; cruise altitude 100 m; vertical takeoff speed 2 m/s; vertical landing speed 2 m/s.

**Request classification (6.3).** 186 184 requests sampled from 1000 generated instances, split into truck-only, single-drone, c-drone.

![[_papers/nguyen2023parallel/images/page_32_image_2.jpg]]
*Figure 11 Request classification*

Single drones can carry parcels below **0.81 kg** provided $C_{nom}\ge 12$ Ah; the 7.5 Ah model is suitable only below **0.28 kg** (Node 3); capacity ≥ 12 Ah covers nearly all single-drone deliveries below 0.81 kg within a flight range of **12.59 km** and slightly beyond. In the band **0.81 kg < w < 6.91 kg** nearly every request is c-drone-eligible (Nodes 10, 11); in **6.91 kg < w < 10.82 kg** more than half must go by truck; above **10.82 kg** the parcel must be truck-served regardless of distance.

**Overall impact (6.4).** Over 1000 samples the average c-drone gain is **23.47%**, the best leaf **32.33%**, the best individuals up to **58.78%**, and the worst leaf still **10.33%**. Average truck mileage reduction **33.21%**.

![[_papers/nguyen2023parallel/images/page_33_image_4.jpg]]
*Figure 12 Visualization of the regression tree generated by dtreeviz library Terence and Prince (2020)*

**Fleet size $m$ is the most decisive factor**: the root split of the tree is on $m$, $m\le 11.5$ giving 18.45% average gain versus $m>11.5$ giving 27.26%, and the same pattern recurs at Nodes 1, 3, 13; at the third level the gain rises from 18.09% to 21.58% as $m$ increases. $D$ and battery capacity act at lower levels with roughly equal, local effects. The authors recommend **at least 12 drones** for a drastic benefit; Node 2 still yields a 10.33% average gain with only 5 units.

![[_papers/nguyen2023parallel/images/page_34_chart_7.jpg]]
*Figure 13 Boxplot of sampled data at Node 10 in Figure 12*

**Battery model (6.6).** At Node 10 ($m>12$), aggregate gains by battery: 7.5 Ah → **26.68%**, 12 Ah → **29.69%**, 20 Ah → **27.95%**, 30 Ah → **25.05%**. Going from 7.5 to 12 Ah helps, then the gain gradually drops from the 20 Ah model, which also shows more variance (lower average, lower whisker, taller box, longer tails). The explanation is that extra battery weight raises the discharge drain, neutralizing the longer life: under the 25 kg cap a 30-Ah drone weighing 4.64 kg leaves a 4-unit c-drone at most **6.44 kg** of payload and a 5-unit c-drone at most **1.8 kg**. **12 Ah is the most consistent choice** from a cost/effectiveness perspective.

**Coverage area (6.7).** $D$ appears at the third level of the tree: gain correlates slightly positively in $[5.00,16.18)$ km, then declines steadily in $[16.18,25.00]$ km. Split points **10.5 km** and **16.18 km** partition Node 5 into gains of **21.48%**, **24.66%**, **19.63%**; the right branch (Nodes 11, 15) favours **7.14–15 km** with gains separated at 7.14 km. Recommendation: a depot coverage area of **7–15 km** for c-drone operations.

## Limitations

- Drones fly back-and-forth from the depot only (PDSTSP restriction): no multi-visit drone tours, no truck-carried drone, no simultaneous pickup. ^[inferred]
- The two-index formulation scales only to 15–30 customers; the exact method never solves the large set, so the quality of large-instance solutions is unproven (no lower bound). ^[inferred]
- Speeds are pre-computed, not optimized jointly with the schedule, so the fleet-level optimum cannot exploit a slower, energy-cheaper flight to serve more customers. ^[inferred]
- Battery assumptions are strong: fully charged before every launch, negligible swap/loading time, Peukert exponent 1.1 and $\beta=0.9$ fixed, and one commercial LiFePO4 product family (Power Tech, 2022) as the battery population.
- The reported benefit is measured against the equivalent single-drone system, not against truck-only delivery, and includes no operating cost, energy cost, safety, noise, or air-traffic constraint.
- Coupling time is stated as 1 minute in the text and as 1 s in Table 5; results are reported with the 1-minute assumption. ^[ambiguous]
- Regulatory framing (FAA Part 135/107, UPS authorisation, 25 kg cap, 6 units) is a snapshot of 2019–2022 rules, not a model of certification and traffic-management constraints. ^[inferred]

## Related

- [[concepts/collective-drone-delivery]] — the c-drone eligibility, gains, fleet-size and battery tradeoffs this paper measures ^[inferred]
- [[concepts/peukert-law-battery-discharge]] — the discharge model behind constraints (3)–(4)
- [[concepts/dag-topological-sort-scheduling-move-evaluation]] — the DAG/topological-sort machinery for extraction and move evaluation
- [[concepts/parallel-drone-scheduling-traveling-salesman-problem]] — the base problem that PDSTSP-c extends
- [[concepts/vehicle-routing-with-synchronization-constraints]] — the synchronization-with-time-windows family PDSTSP-c is compared against
- [[concepts/multirotor-power-model-components]] — the induced/profile/parasite power model used in Eqs. 23–25
- [[concepts/large-neighborhood-search]] — the destroy-and-repair family that Ruin-and-Recreate extends
- [[concepts/drone-speed-selection-in-routing]] — pre-computed energy-optimal cruise speeds
- [[references/nguyen2022-min-cost-pdsvrp]] — the Ruin-and-Recreate and sweep operator this paper builds on
- [[references/murray2015flying]] — defines PDSTSP, the base variant
- [[references/montemanni2024-parallel-collective-drones]] — collective drones in the PDSVRP setting
- [[concepts/multi-objective-metaheuristic-tuning-validation]] — irace-based parameter tuning practice

## Sources

- [[_papers/nguyen2023parallel/nguyen2023parallel-extracted.md]]
- [[_papers/nguyen2023parallel/nguyen2023parallel.md]]
- [[_papers/nguyen2023parallel/images/page_2_image_2.jpg]]
- [[_papers/nguyen2023parallel/images/page_8_image_6.jpg]]
- [[_papers/nguyen2023parallel/images/page_11_image_2.jpg]]
- [[_papers/nguyen2023parallel/images/page_18_image_3.jpg]]
- [[_papers/nguyen2023parallel/images/page_19_chart_2.jpg]]
- [[_papers/nguyen2023parallel/images/page_21_image_5.jpg]]
- [[_papers/nguyen2023parallel/images/page_22_image_2.jpg]]
- [[_papers/nguyen2023parallel/images/page_23_image_2.jpg]]
- [[_papers/nguyen2023parallel/images/page_28_image_10.jpg]]
- [[_papers/nguyen2023parallel/images/page_31_chart_3.jpg]]
- [[_papers/nguyen2023parallel/images/page_32_image_2.jpg]]
- [[_papers/nguyen2023parallel/images/page_33_image_4.jpg]]
- [[_papers/nguyen2023parallel/images/page_34_chart_7.jpg]]
