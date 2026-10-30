---
title: >-
  An Adaptive Large Neighborhood Search Heuristic for the Pickup and Delivery Problem with Time Windows
category: references
tags: [adaptive-large-neighborhood-search, pickup-and-delivery, vrptw, metaheuristics, simulated-annealing, ruin-and-recreate, regret-insertion, adaptive-weights, vehicle-minimization, heuristics]
relationships:
  - target: "[[concepts/large-neighborhood-search]]"
    type: extends
  - target: "[[concepts/adaptive-large-neighborhood-search-for-mip]]"
    type: related_to
  - target: "[[concepts/simulated-annealing-metropolis-cooling]]"
    type: uses
  - target: "[[concepts/variable-neighborhood-search]]"
    type: related_to
  - target: "[[references/pisinger2019-large-neighborhood-search]]"
    type: related_to
  - target: "[[references/hendel2022-adaptive-lns-for-mip]]"
    type: related_to
  - target: "[[references/goel2012-large-neighborhood-search-lng-inventory-routing]]"
    type: related_to
  - target: "[[references/phanduc2025-pareto-front-grid-fairness-dpdptw]]"
    type: related_to
  - target: "[[references/ha2020-vrp-synchronization-lp-alns]]"
    type: related_to
  - target: "[[references/ganjia2026-multiobjective-sustainable-supply-chain-scheduling]]"
    type: related_to
  - target: "[[references/pham2023-efficient-ga-quadratic-tsp]]"
    type: related_to
  - target: "[[references/nguyen2025set]]"
    type: related_to
  - target: "[[references/li2024drone]]"
    type: related_to
  - target: "[[concepts/large-neighborhood-ship-pair-destroy-repair]]"
    type: related_to
  - target: "[[concepts/alns-destroy-repair-operator-suite]]"
    type: related_to
  - target: "[[references/sacramento2019-vrp-d-truck-drone-alns-cost]]"
    type: related_to
  - target: "[[references/santini2018-alns-acceptance-criteria]]"
    type: related_to
  - target: "[[references/windrasmara2022-alns-multi-drop-fstsp]]"
    type: related_to
sources:
  - _papers/ropke2006adaptive/ropke2006adaptive.md
  - _papers/ropke2006adaptive/ropke2006adaptive-extracted.md
  - _papers/ropke2006adaptive/images/page_8_chart_11.jpg
summary: >-
  ALNS competes among several removal and insertion subheuristics, choosing each by roulette wheel on
  adaptive segment scores, and beats prior PDPTW heuristics on over half of 354 Li-and-Lim instances.
provenance:
  extracted: 0.92
  inferred: 0.05
  ambiguous: 0.03
base_confidence: 0.77
tier: core
lifecycle: draft
lifecycle_changed: 2026-10-29T17:15:00Z
created: "2026-10-26T12:26:00Z"
updated: 2026-10-30T14:38:55Z
---

# Ropke & Pisinger 2006 — Adaptive Large Neighborhood Search for the PDPTW

## Sections

### Problem and mathematical model

The pickup and delivery problem with time windows (PDPTW) serves a set of transportation requests T using a
limited number of vehicles; each request moves goods from a pickup node to a delivery node, the pair must be
on the same route, and the pickup must precede the delivery, subject to time window and capacity constraints.
Two time windows are assigned per request (pickup and delivery), each pickup and delivery has a service time,
a vehicle may arrive before a window opens and must wait, and may never arrive after it closes. Each request
has a set of feasible vehicles (e.g. a request needing a freezing compartment), and requests with K_i ≠ K are
called special requests. Vehicles start and end at given terminals, which need not be the same, and two
vehicles can have different start and end terminals; each vehicle has a start time (when it must leave) and an
end time (latest allowable arrival at its end terminal), and leaves at the specified start time even if that
creates waiting at the first location. Requests that cannot be assigned go to a virtual request bank.

The model has n requests and m vehicles: P = {1, …, n} is the pickup set, D = {n+1, …, 2n} the delivery set,
request i is represented by nodes i and i+n, K is the vehicle set with |K| = m, K_i the vehicles able to serve
request i, P_k ⊆ P and D_k ⊆ D the pickups and deliveries vehicle k can serve, so that k ∈ K_i ⇔ i ∈ P_k ∧
i ∈ D_k. The start and end terminal nodes of vehicle k are τ_k = 2n + k and τ'_k = 2n + m + k, the graph is
G = (V, A) with V = N ∪ {τ_1, …, τ_m} ∪ {τ'_1, …, τ'_m} and A = V × V, and each vehicle has a subgraph
G_k = (V_k, A_k). Distances and times are nonnegative, d_ij ≥ 0 and t_ij ≥ 0, times satisfy the triangle
inequality t_ij ≤ t_il + t_lj, and the model assumes t_{i, n+i} + s_i > 0 so that subtour elimination and the
pickup-before-delivery constraint are easy to express. Each node i has service time s_i and time window
[a_i, b_i]; l_i is the goods loaded at node i, with l_i ≥ 0 for i ∈ P and l_i = −l_{i−n} for i ∈ D, and C_k
is vehicle k's capacity. Four decision variable types are used: binary x_ijk (edge i→j used by vehicle k),
nonnegative integer S_ik (start of service at i by k), nonnegative integer L_ik (an upper bound on the load
of vehicle k after servicing i, defined only when k visits i), and binary z_i, one when request i is in the
request bank. The objective (eq. 1) minimizes α·distance + β·(time spent by each vehicle, defined as arrival
at the end terminal minus its start time) + γ·(number of requests in the request bank), weighted by α, β, γ;
normally a high value is assigned to γ to serve as many requests as possible. Constraints (2)–(16): (2) each
pickup is visited or its request goes to the bank; (3) the delivery is visited by the same vehicle when the
pickup is; (4) and (5) every vehicle leaves its start terminal and enters its end terminal; (6) flow
conservation at each node; (7) the sequencing and time-window constraints, which also make subtours ^[inferred]
impossible; (9) pickup before delivery; (10), (11), (12) the load variable is set correctly and capacity is
respected, with L_{τ_k,k} = L_{τ'_k,k} = 0; (13)–(16) the binary and nonnegativity conditions. The model is
not written on integer-linear form because the problem is solved heuristically; the problem is NP-hard since
it contains the traveling salesman problem as a special case. The work was inspired by a real-life problem of
transporting raw materials and goods between production facilities of a major Danish food manufacturer, whose
data cannot be published for confidentiality reasons.

### LNS core: large moves, not small ones

Local search built on small standard moves (moving one request between routes, exchanging two requests, as in
Nanry and Barnes 2000 and Li and Lim 2001) evaluates a huge number of solutions quickly but changes the
current solution very little per iteration, and the authors believe such heuristics struggle to move between
promising regions on tightly constrained problems. Instead of relaxing constraints to visit infeasible
solutions (as Cordeau, Laporte and Mercier 2001 do), the heuristic uses very large moves that can rearrange up
to 30%–40% of all requests in a single iteration; the price is that evaluating moves is much slower, so the
number of solutions examined per time unit is a fraction of what a standard heuristic examines. The [[concepts/large-neighborhood-search|LNS]]
heuristic is due to Shaw (1997), applied to the VRPTW with good results (Shaw 1997, 1998; Bent and Van
Hentenryck 2004), applied to PDPTW by Bent and Van Hentenryck (2003a), and similar to the ruin-and-recreate
heuristic of Schrimpf et al. (2000). Algorithm 1 keeps a best solution, copies s to s', removes q requests,
reinserts them, updates the best when f(s') < f(s_best), and accepts s' by a criterion; the loop runs until a
stop criterion, implemented as a fixed number of iterations. Lines 5 and 6 (remove, reinsert) are the
interesting part, and performance depends heavily on the removal and insertion procedures. Earlier LNS work
used near-optimal reinsertion by truncated branch-and-bound; here simple insertion heuristics are used, and
the quality of the overall heuristic is very good precisely because the bad moves they generate diversify the
search. q ∈ {0, …, n}: q = 0 means no search at all, q = n resolves the problem from scratch each iteration;
larger q makes it easier to move around the solution space, slows each insertion, and can give bad results
when a heuristic is used for insertion. LNS also fits the very-large-scale neighborhood definition of Ahuja et ^[inferred]
al. (2002) — neighborhoods that grow exponentially with problem size, or that are too large to search
explicitly — with the important difference that most such heuristics examine a huge number of solutions
implicitly, while this heuristic examines a relatively low number. The process can equivalently be seen as
fix-optimize operations: fix a number of variables at their current values, then reoptimize under that
fixation, which makes the method applicable where remove-insert is not intuitive.

### Removal heuristics

Three removal heuristics take a solution and an integer q and output a solution with q requests removed; Shaw
and worst removal also have a determinism parameter p that controls randomization (a low p corresponds to much
randomness). Shaw removal removes related requests, since similar requests can be shuffled into better
solutions, whereas removing very different requests may only allow reinsertion at the original or at bad ^[inferred]
positions. Relatedness is measured by R(i, j) = φ(d_{A(i),A(j)} + d_{B(i),B(j)}) + χ(|T_{A(i)} − T_{A(j)}| + ^[inferred]
|T_{B(i)} − T_{B(j)}|) + ψ|l_i − l_j| + ω(1 − |K_i ∩ K_j| / min{|K_i|, |K_j|}) (eq. 17), where A(i) and B(i)
are the pickup and delivery locations of request i and T_i is the visit time of location i; the four terms
measure distance, temporal connectedness, capacity demand difference, and how many vehicles can serve both
requests (a high relatedness when few vehicles are shared). d_ij, T_x and l_i are normalized to [0, 1] so that
0 ≤ R(i, j) ≤ 2(φ + χ) + ψ + ω. R(i, j) cannot be computed if i or j is in the request bank. Algorithm 2
picks a random request first, then repeatedly picks a request r from the removed set D, sorts the remaining
requests by R(r, ·), draws y in [0, 1), and adds L[y^p |L|] to D; the sort in Line 7 can be replaced by a
linear time selection algorithm (Cormen et al. 2001). Random removal selects q requests uniformly and is a
special case of Shaw removal with p = 1, implemented separately because it runs faster. Worst removal uses the ^[inferred]
cost of a request, cost(i, s) = f(s) − f_{−i}(s), where f_{−i}(s) is the cost of the solution with request i
removed completely (not moved to the bank), and repeatedly takes the request at position y^p |L| of the list
sorted by descending cost, randomized so the same requests are not removed over and over. Shaw removal is
biased toward requests that can easily be exchanged, worst removal toward requests that appear to be in the
wrong position.

### Insertion heuristics and the regret class

Insertion heuristics for vehicle routing split into sequential (one route at a time) and parallel (several
routes at once) classes, discussed in Potvin and Rousseau (1993); all heuristics here are parallel, and they
are given partial routes plus requests to insert, so they seldom build a solution from scratch. The basic
greedy heuristic performs at most n iterations, inserting one request each time. Δf_{i,k} is the change in
objective when request i is inserted into route k at its best position, set to ∞ when insertion in route k is
impossible, and c_i = min_k{Δf_{i,k}} is the cost of inserting i at its best position overall; the request
minimizing min_{i∈U} c_i (eq. 18) over the unplanned set U is inserted at its minimum cost position. Only one
route changes per iteration, which is exploited for speed. The obvious weakness is that hard requests (large
c_i) are postponed to the last iterations, when most routes are full. The regret heuristic adds look-ahead:
x_ik indicates the route with the kth lowest insertion cost, and the regret value c*_i = Δf_{i,x_i2} −
Δf_{i,x_i1} is the difference between inserting the request in its best and second-best route; each iteration
inserts the request maximizing max_{i∈U} c*_i (ties broken by lowest insertion cost), i.e. the insertion that
would be regretted most if not done now. The regret-k family maximizes max_{i∈U} Σ_{j=1..k}(Δf_{i,x_ij} −
Δf_{i,x_i1}) (eq. 19); when some requests cannot be inserted in at least m − k + 1 routes, the request
insertable in the fewest routes (but at least one) is inserted. The basic heuristic is regret-1 and the
regret-2 heuristic is the one above. Regret heuristics with k > 2 discover earlier that insertion
possibilities are limited. Potvin and Rousseau (1993) used a regret-k heuristic with k = m for the VRPTW,
evaluating insertions with a special cost function rather than the change in objective, and regret heuristics
also apply outside vehicle routing, e.g. to the generalized assignment problem of Martello and Toth (1981).

### Adaptive weight adjustment

All removal and insertion heuristics are used in the same search, because, for example, regret-2 may suit one
instance type while regret-4 suits another, so alternating makes the heuristic more robust. Heuristic j is
selected by roulette wheel with probability w_j / Σ_i w_i (eq. 20), and the insertion heuristic is chosen
independently of the removal heuristic. Setting weights by hand is involved when many subheuristics are used,
so the search is divided into segments of 100 iterations; the score of every heuristic is reset to zero at the
start of each segment, and a heuristic's score increases by σ_1, σ_2 or σ_3 according to Table 1: σ_1 when the
last remove-insert produced a new global best solution, σ_2 when it produced a solution never accepted before
that is better than the current solution, and σ_3 when it produced a never-accepted solution that is worse
than the current solution but was accepted. Only unvisited solutions are rewarded, tracked by giving each
solution a hash key stored in a hash table, to encourage exploration. Both heuristics in an iteration receive
the same score increment, because it cannot be attributed to removal versus insertion. At the end of segment j ^[inferred]
the weight for segment j+1 is w_{i,j+1} = w_{ij}(1 − r) + r·π_i/θ_i, where π_i is the score obtained in the
last segment, θ_i the number of attempts to use heuristic i, and r the reaction factor; r = 0 keeps the initial
weights, r = 1 lets the last segment decide the weight. In the first segment all heuristics are weighted
equally.

![[_papers/ropke2006adaptive/images/page_8_chart_11.jpg]]
Figure 1 The Figure Shows an Example of How the Weights for the Three Removal Heuristics Progressed During One Application of the Heuristic

Figure 1 shows the weights of the three removal heuristics over one run; the plots decrease because the
simulated annealing acceptance criterion means only good moves are accepted near the end, making high scores
harder to obtain. The caption's Notes state that on this instance random and Shaw removal performed virtually
equally well while the worst heuristic performed worst, so the worst heuristic is used less often.

### Acceptance, noise, and vehicle minimization

Acceptance uses [[concepts/simulated-annealing-metropolis-cooling|simulated annealing]]: solution s' is accepted from current s with probability
e^{−(f(s') − f(s))/T}, T > 0 being the temperature; T starts at T_start and decreases each iteration as
T = T·c with 0 < c < 1 the cooling rate. Rather than fixing T_start, it is computed from the initial solution:
the cost z' of the initial solution is calculated with γ set to zero, then T_start is set so that a solution w%
worse than the current one is accepted with probability 0.5; γ is zeroed here because it is typically large and
would push the starting temperature too high if the initial solution had requests in the bank. w is the start
temperature control parameter. Because the insertion heuristics are myopic, a noise term is added to the
objective: for each insertion cost C a random number in [−max N, max N] is drawn and C' = max{0, C + noise};
each iteration decides whether to use C or C', and that decision is tracked by the same adaptive mechanism,
counting how often noise insertions and "clean" insertions succeed. max N = η·max_{i,j∈V} d_ij, with η
controlling the amount of noise, tied to distances because distances are an important part of the objective in
all problems considered. The authors argue that noise is needed even inside the simulated annealing framework
because the neighborhood is searched by the insertion heuristics rather than randomly sampled, supported by the
experiments in Table 4.

Minimizing the number of vehicles used is often the first priority in vehicle routing. The heuristic handles
it with a two-stage algorithm (also used by Bent and Van Hentenryck, who used different neighborhoods and
metaheuristics per stage, whereas here the same heuristic runs in both stages): an initial feasible solution is
built by a sequential insertion method constructing one route at a time; the number of vehicles it uses is the
initial estimate. Then one route is removed, its requests go to the request bank, and the LNS heuristic solves
the resulting problem with a high γ so requests are moved out of the bank if possible; if all requests are
served, a new candidate minimum vehicle count has been found, the heuristic is stopped immediately, one more
route is removed, and the process repeats. If no all-served solution is found, the algorithm steps back to the ^[inferred]
last solution serving all requests, which becomes the starting point of the second stage, normal LNS. The
vehicle minimization stage works only for homogeneous fleets with an unlimited number of vehicles. To bound
running time, the stage is capped at a total iteration budget, and the LNS heuristic is stopped when five or
more requests are unplanned and no improvement in the number of unplanned requests has been found in the last
2,000 LNS iterations. In the experiments the total budget was set to 25,000 and the 2,000 threshold as stated.
The request bank matters because it lets the search visit infeasible solutions in a transition stage; in the
problems of §4 solutions with unscheduled requests are not accepted. Several removal and insertion heuristics
can be seen as local search with several neighborhoods, which the authors believe was new in the LNS
literature; the related [[concepts/variable-neighborhood-search|Variable Neighborhood Search]] of Mladenović and Hansen (1997) uses a parameterized
family of neighborhoods, typically one neighborhood searched with variable depth, whereas ALNS uses several
unrelated neighborhoods. Simulated annealing was chosen at the top level because ALNS already contains random
sampling.

### Tuning and construction heuristics

Parameters: Shaw removal is controlled by φ, χ, ψ, ω and p; worst removal by p_worst; random removal has no
parameters; insertion heuristics are parameter-free once the regret degree is chosen; acceptance uses w and c;
the weight adjustment uses σ_1, σ_2, σ_3 and r; noise rate η and parameter ξ control how many requests are
removed, by drawing a random ρ with 4 ≤ ρ ≤ min(100, ξn) and removing ρ requests; the search stops after
25,000 LNS iterations, which gave a fair trade-off between time and quality. The tuning set has 16 instances:
LR1_2_1, LR202, LRC1_2_3 and LRC204 from the Li and Lim benchmark, containing between 50 and 100 requests,
with the number of vehicles set to one more than Li and Lim report so that solutions with an empty request bank
are easier to find, plus 12 randomly generated instances of 50 requests each, covering single-depot and
multidepot problems and requests servable only by a subset of the fleet. Tuning proceeds from an ad hoc
trial-and-error setting found during development, then sweeps one parameter at a time keeping the others
fixed, applying the heuristic 5 times to each test problem and choosing the setting with the best average
deviation from the best known solutions; the process was stopped after one pass, and because it starts from an
initial guess and then sweeps, the calibration order plays a minor role. In subsequent papers solving 11
variants of the vehicle routing problem, only a few parameters were retuned, so a complete tuning appears to be
needed only once.

Construction heuristics regret-1, regret-2, regret-3, regret-4 and regret-m were tested once per tuning
instance (Table 2): average gap 407, 303, 263, 260, 277 percent with the decimal separator lost in the OCR, ^[inferred]
fails 3, 3, 3, 2, 0, and times 0.02, 0.02, 0.02, 0.02, 0.03 s on a 1.5 GHz Pentium IV. Basic greedy is the
worst, the regret heuristics are comparable, and regret-m stands out because it served all requests in all
problems (0 fails). The heuristics are fast but very imprecise, and it is surprising that such imprecise
construction heuristics can be the foundation of a precise local search — which the results confirm.

Parameter ξ was swept from 0.05 to 0.5 in steps of 0.05 (Table 3), giving average gaps of 1.75, 1.65, 1.21,
0.97, 0.81, 0.71, 0.81, 0.49, 0.57, 0.57 percent: too low and the heuristic cannot move far per iteration and
is more likely to be trapped; too high and it moves freely but stretches the insertion heuristics, which work
well inserting a limited number of requests into a partial solution but cannot build a good solution from
scratch. ξ = 0.4 is a good choice, and the heuristic gets slower as ξ rises, so the comparison in Table 3 is
not completely fair. The tuned parameter vector (φ, χ, ψ, ω, p, p_worst, w, c, σ_1, σ_2, σ_3, r, η, ξ) = (9, 3,
2, 5, 6, 3, 0.05, 0.99975, 9, 13, 0.1, 0.025, 0.4). The vehicle minimization algorithm improved when (w, c)
were set to 0.35 and 0.9999,^[ambiguous] i.e. a higher start temperature and slower cooling, indicating that
minimizing vehicles needs more diversification than minimizing distance.

Simple LNS configurations using one removal and one insertion heuristic were compared with the full ALNS
(Table 4, configurations 1–14, noise added in 50% of insertions; configuration 15 is ALNS with noise controlled
adaptively). The gaps reported are the digit runs of the extracted table, with the decimal separator lost: 27, ^[inferred]
26, 54, 32, 20, 16, 22, 16, 18, 13, 20, 13, 18, 17, 13.^[ambiguous] Shaw removal performs best, worst removal
second, random removal worst; all insertion heuristics perform quite well and are hard to distinguish, with
regret-3 and regret-4 coupled with noise slightly better, and noise helping in all experiments. The basic
insertion heuristic performs nearly as well as the regret heuristics inside the LNS framework, which is
surprising given how badly it scored in Table 2, indicating that LNS is robust with respect to the insertion
method. ALNS is on par with the two best simple approaches, not better, so the authors' hypothesis is that its
value is robustness: a simple configuration may fail on other problem types while ALNS continues to perform.
All experiments ran on a 1.5 GHz Pentium IV PC with 256 MB internal memory under Linux, using double precision
floating point numbers for travel times and distances.

### Results on Li and Lim (Table 5)

The Li and Lim data set contains 354 instances with between 100 and 1,000 locations, available from SINTEF;
these are single-depot problems constructed from VRPTW problems, in which all requests must be served and all
vehicles can serve all requests. The Nanry and Barnes instances are not reported because they are easy to solve
due to their size. Distance-driven is the objective in §4.4.2 (distance minimization makes comparison easier and
is the heuristic's original objective), with the number of vehicles set to the minimum values reported by Li and
Lim, and the heuristics applied 10 times to instances with 400 or fewer locations and 5 times to larger ones.
Verbatim table rows (locations, problems, best-known-solution counts, average gap, average time in seconds, ^[inferred]
fails, in ALNS then LNS order): 100, 56, 52, 50, 0.19, 0.50, 49, 55, 0, 0; 200, 60, 49, 15, 0.72, 1.41, 305,
314, 0, 0; 400, 60, 52, 6, 2.36, 4.29, 585, 752, 0, 0; 600, 60, 54, 5, 0.93, 3.20, 1069, 1470, 0,
0;^[ambiguous] 800, 60, 46, 5, 1.73, 3.27, 2025, 3051, 0, 2;^[ambiguous] 1,000, 58, 47, 4, 2.26, 4.22, 2916,
5252, 0, 1.^[ambiguous] ALNS performs better on all four terms, and becomes more attractive as problem size
increases; LNS spends more time for the same number of iterations because the Shaw removal it uses is more time
consuming than the other removal heuristics.

### New multidepot instances (Tables 6 and 8)

New randomly generated instances add features absent from Li and Lim: multiple depots, routes with different
start and end terminals, and special requests servable by a subset of vehicles (each special request servable by
between 30% to 60% of the vehicles), with α = β = 1 so distance and time are weighted equally, and no vehicle
minimization because the fleet is inhomogeneous. Three geographic distributions are generated — locations
uniform in the plane, in 10 clusters, and 50% of locations in 10 clusters with 50% uniform — inspired by
Solomon's R, C and RC problems, for 50, 100, 250 and 500 requests, all multidepot, 12 problems per size
combining the three features, so 48 problems, each run 10 times. Table 6, verbatim: requests 50, problems 12,
best-known 8 ALNS and 5 LNS, gap 1.44 and 1.86, time 23 and 34 s; 100, 12, 11, 1, 1.54, 2.18, 83, 142; 250, 12,
7, 5, 1.39, 1.62, 577, 1,274; 500, 12, 9, 3, 1.18, 1.32, 3,805, 8,146; sum 48, 35, 14, 5.55, 6.98, 4,488,
9,596. ALNS is still superior, with a smaller quality gap and a larger running-time difference than on Li and
Lim, and small instances of this class appear harder to solve than Li and Lim instances. Table 8 gives average
solution quality by feature, ALNS then LNS: uniform 1.04 and 1.50, clustered 1.89 and 2.09, semiclustered 1.23
and 1.64, normal requests 1.24 and 1.47, special requests 1.54 and 2.02, and the route-type row printed as the
concatenated runs 1.591.19 for ALNS and 2.041.45 for LNS.^[ambiguous] Clustered problems are hardest, uniform
easiest, special requests make the problem slightly harder, and routes with different start and end terminals
are easier than routes starting and ending at the same location, because the fixed start and end give
information about the area the route should cover; no feature made LNS better than ALNS.

### Comparison with existing heuristics (Tables 7, 9, 10)

Four heuristics had been applied to the Li and Lim benchmarks: Li and Lim (2001), Bent and Van Hentenryck
(2003a, the BH heuristic, probably the best overall so far), and the commercial SINTEF and TetraSoft A/S
heuristics, whose detailed results are not available. In the literature the primary objective is minimizing
vehicles and the secondary minimizing distance, so the vehicle minimization algorithm of §3.7 was used, with
ALNS applied 10 times to instances with 200 or fewer locations and 5 times to larger ones; w had to be
decreased and c increased for the 1,000-location instances, otherwise the same parameter setting was used.
Verbatim Table 7 rows (best known 2003 vehicles and distance, then BH vehicles, distance, average time-to-best,
average time, then ALNS best-of-10-or-5 vehicles, distance, average time, then ALNS best vehicles and distance):
100 locations, 402, 58,060, 402, 58,062, 68, 3,900, 402, 58,060, 66, 402, 56,060; 200, 615, 178,380, 614,
180,358, 772, 3,900, 606, 180,931, 264, 606, 180,419; 400, 1,183, 421,215, 1,188, 423,636, 2,581, 6,000,
1,158, 422,201, 881, 1,157, 420,396; 600, 1,699, 873,850, 1,718, 879,940, 3,376, 6,000, 1,679, 863,442, 2,221,
1,664, 860,898; 800, 2,213, 1,492,200, 2,245, 1,480,767, 5,878, 8,100, 2,208, 1,432,078, 3,918, 2,181,
1,423,063; 1,000, 2,698, 2,195,755, 2,759, 2,225,190, 6,174, 8,100, 2,652, 2,137,034, 5,370, 2,646, 2,122,922.
Each row corresponds to a set of problems with the same size, between 56 and 60 instances. BH was tested on a
1.2 GHz Athlon, and the running times should be comparable because the authors believe the Athlon is at most
20% slower than their machine. ALNS dominates BH overall, especially at larger sizes, improves considerably on
the previously best known solutions, and the simple vehicle minimization algorithm works very well. The last two
columns summarize best results over several parameter settings, showing ALNS results can be improved further.
Table 9 (problems strictly better, then at least as good, for best-of-10-or-5, then ALNS best): 100, 56
problems, 0, 54, 0, 55; 200, 60, 22, 42, 27, 57; 400, 60, 40, 47, 41, 55; 600, 60, 41, 45, 51, 57; 800, 60, 37,
42, 48, 53; 1,000, 58, 50, 54, 51, 55 — ALNS improves more than half of the solutions and is at least as good as
the previously best known for 80% of the problems. Table 10 reports the average number of vehicles and average
distance: 403, 58249, 608, 181707, 1168, 425817, 1686, 867930, 2223, 1432321, 2677,
2129032,^[ambiguous] whose thousands separators are lost in the OCR. The average solution sometimes has a lower
distance than the best-of-10-or-5 solution (the last row), because the heuristic finds solutions using more than
the minimum number of vehicles, which usually allows shorter distances. Tables 11–16 give per-instance best
results for the six Li and Lim families R1, R2, C1, C2, RC1, RC2 with bold numbers marking best known
solutions; in the extracted markdown the vehicle counts and distances collapse into single digit runs (for
example 165080 for problem 1 of R1 at 100 locations), so those cells cannot be split verbatim.^[ambiguous] Two
entries in Table 16 are missing because the corresponding problem instances no longer exist.

The computational tests met all three objectives: the adaptive heuristic that combines several removal and
construction heuristics is superior to a simple LNS with one removal and one insertion heuristic; certain
problem characteristics influence performance, but none made LNS better than ALNS; and the heuristic finds
good-quality solutions in reasonable time, outperforming previously proposed heuristics. Testing on large
instance sets matters because the LNS–ALNS difference only becomes apparent on large instances, and real-world
problems often have dimensions comparable to or greater than the largest solved here. A simple LNS appears more
sensitive to the choice of removal heuristic than to the choice of insertion heuristic, and it is open whether
this holds for other problems. The conclusion notes the heuristic discovered new best solutions for standard
VRPTW, multidepot VRP and other vehicle routing benchmarks (Pisinger and Ropke 2005; Ropke and Pisinger 2006),
and that the [[concepts/adaptive-large-neighborhood-search-for-mip|ALNS framework]] is easily applicable to most combinatorial optimization problems thanks to the many
robust and fast construction heuristics designed in earlier decades. Acknowledgements: Jakob Birkedal Nielsen
for discussions, Emilie Danna for criticism, and three anonymous referees.

## Related
- [[concepts/large-neighborhood-search]] — this paper is the PDPTW instantiation that Shaw's LNS made into a family: many ruin heuristics, simple greedy repair, simulated annealing acceptance, adaptive weights. ^[inferred]
- [[concepts/adaptive-large-neighborhood-search-for-mip]] — the ALNS framework in MIP form, with a fixed-solution destroy operator, is the same adaptive-weights machinery applied to MIP.
- [[references/windrasmara2022-alns-multi-drop-fstsp]] — multi-drop FSTSP ALNS built directly on this canonical ALNS.
- [[concepts/simulated-annealing-metropolis-cooling]] — the accept criterion, the multiplicative cooling rate c, and the w-controlled start temperature are the Metropolis loop used here.
- [[concepts/variable-neighborhood-search]] — the paper contrasts ALNS with VNS: several unrelated neighborhoods versus one parameterized family searched at variable depth. ^[inferred]
- [[references/pisinger2019-large-neighborhood-search]] — the handbook chapter by Pisinger on the LNS family that this paper founded.
- [[references/hendel2022-adaptive-lns-for-mip]] — a later ALNS application whose destroy/repair and weight-update structure traces back to this paper.
- [[references/goel2012-large-neighborhood-search-lng-inventory-routing]] — LNS applied to inventory routing, the same destroy-and-repair design in a continuous-time setting.
- [[references/santini2018-alns-acceptance-criteria]] — the SA acceptance criterion used here is one of three top criteria in that comparison; RRT was statistically undominated
- [[references/phanduc2025-pareto-front-grid-fairness-dpdptw]] — modern multiobjective PDPTW work whose ruin-and-repair metaheuristic inherits this problem model and objective structure.
- [[references/ha2020-vrp-synchronization-lp-alns]] — ALNS combined with an LP/ALNS layer for synchronized VRP, downstream of the subheuristic-competition design.
- [[references/ganjia2026-multiobjective-sustainable-supply-chain-scheduling]] — a multiobjective scheduling metaheuristic whose subheuristic competition and acceptance logic follow this ALNS template.
- [[references/pham2023-efficient-ga-quadratic-tsp]] — a GA hybrid that uses worst removal exactly as defined here (cost-saving probability-weighted, citing Ropke & Pisinger 2006).
- [[references/nguyen2025set]] — set-based VRP whose removal/insertion operator set is IRACE-calibrated on the same ALNS template.
- [[references/li2024drone]] — drone VRP whose weight rule and acceptance constants are the ALNS scheme of this paper with renamed symbols.
- [[concepts/large-neighborhood-ship-pair-destroy-repair]] — the destroy/repair instance used in industry, whose scheme follows the ALNS line begun here.

## Sources
- [[_papers/ropke2006adaptive/ropke2006adaptive.md]] — Zotero sidecar: Ropke, Stefan; Pisinger, David (2006), Transportation Science, 2006-11, doi:10.1287/trsc.1050.0135, with the paper's own abstract quoted. ^[inferred]
- [[_papers/ropke2006adaptive/ropke2006adaptive-extracted.md]] — full extracted text (765 lines), read in windows 1–300, 301–600, 601–765.
- [[_papers/ropke2006adaptive/images/page_8_chart_11.jpg]] — Figure 1 (removal-heuristic weight progression), the only embedded figure; the other 40 crops are INFORMS title-page logos (page_0_image_3, page_0_image_14), equation crops, and table crops with no caption anchor, so they are not embedded and the tables are transcribed as text. ^[inferred]
-^[ambiguous] The vault contains no PDFs, so `pdftotext` cannot be run: the extracted markdown is the only authority. Digit runs where thousands separators and decimal points are lost in the OCR (Table 2, Table 4, the Table 8 route-type row, Table 10, Table 5's time columns, and Tables 11–16) are recorded verbatim as printed and flagged; no value is rounded, normalized, or reconstructed beyond what the text shows.