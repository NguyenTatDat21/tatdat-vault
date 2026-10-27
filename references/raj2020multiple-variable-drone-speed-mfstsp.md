---
title: >-
  The multiple flying sidekicks traveling salesman problem with variable drone speeds (Raj & Murray, 2020)
category: references
tags: [paper, mfstsp, variable-drone-speed, truck-drone-synchronization, makespan, uav-power-model, uav-endurance, heuristic, three-phase-heuristic, last-mile-delivery, payload-weight, local-search, customer-density]
relationships:
  - target: "[[concepts/multiple-flying-sidekicks-traveling-salesman-problem]]"
    type: extends
  - target: "[[references/murray2020-multiple-flying-sidekicks-tsp]]"
    type: extends
  - target: "[[concepts/drone-speed-selection-in-routing]]"
    type: implements
  - target: "[[references/liu2017power]]"
    type: uses
  - target: "[[concepts/nonlinear-drone-energy-function-in-routing]]"
    type: uses
  - target: "[[concepts/payload-induced-drone-battery-consumption-rate]]"
    type: uses
  - target: "[[references/murray2015flying]]"
    type: related_to
  - target: "[[concepts/parallel-drone-scheduling-traveling-salesman-problem]]"
    type: related_to
  - target: "[[concepts/vehicle-routing-with-synchronization-constraints]]"
    type: related_to
sources:
  - _papers/raj2020multiple/raj2020multiple-extracted.md
  - _papers/raj2020multiple/raj2020multiple.md
  - _papers/raj2020multiple/images/page_2_chart_2.jpg
  - _papers/raj2020multiple/images/page_2_chart_4.jpg
  - _papers/raj2020multiple/images/page_2_chart_7.jpg
  - _papers/raj2020multiple/images/page_2_image_10.jpg
  - _papers/raj2020multiple/images/page_2_image_12.jpg
  - _papers/raj2020multiple/images/page_5_image_5.jpg
  - _papers/raj2020multiple/images/page_13_chart_2.jpg
  - _papers/raj2020multiple/images/page_13_chart_4.jpg
  - _papers/raj2020multiple/images/page_13_chart_7.jpg
  - _papers/raj2020multiple/images/page_14_chart_2.jpg
  - _papers/raj2020multiple/images/page_14_chart_4.jpg
  - _papers/raj2020multiple/images/page_16_chart_4.jpg
  - _papers/raj2020multiple/images/page_16_chart_6.jpg
summary: >-
  mFSTSP-VDS: truck + heterogeneous UAV fleet, cruise speed a decision variable, Liu 2017 power model. Three-phase heuristic; up to 22.2% makespan savings vs max speed.
provenance:
  extracted: 0.88
  inferred: 0.10
  ambiguous: 0.02
base_confidence: 0.67
tier: core
lifecycle: draft
lifecycle_changed: 2026-10-26T10:43:50Z
created: 2026-10-26T10:43:50Z
updated: 2026-10-27T06:00:00Z
---

# The multiple flying sidekicks TSP with variable drone speeds (Raj & Murray, 2020)

*Transportation Research Part C: Emerging Technologies, 2020. DOI: 10.1016/j.trc.2020.102813.*

## Problem & motivation

Raj & Murray extend the [[concepts/multiple-flying-sidekicks-traveling-salesman-problem|mFSTSP]] of Murray & Raj (2020) into the **mFSTSP-VDS**: one truck plus a fleet $V$ of **heterogeneous UAVs** (differing payload capacity $\kappa_v$, battery power, maximum speed $\nu_v^{\max}$) deliver parcels to customers $C=\{1,\dots,c\}$ (parcel weight $w_j$), starting and ending at depots 0 and $c+1$ (which may be physically distinct), minimizing total mission time (makespan). The novel twist: **UAV cruise speeds are decision variables** — the first truck-and-UAV makespan model where speeds are chosen during the solution process, with different legs of the same UAV flying at different speeds (carrying a parcel vs flying empty).

The motivation is physical: with the [[references/liu2017power|Liu et al. (2017) multi-rotor power model]], power consumption is nearly flat at low speed and grows nonlinearly at high speed, so endurance falls nonlinearly and range is an increasing function of speed at low speeds, decreasing at high speeds. Under the standard fixed-endurance assumption, the literature concludes that faster UAVs never hurt (Murray & Chu 2015; Agatz 2018; Boysen 2018; Poikonen 2019; Schermer 2019) — that conclusion collapses once endurance depends on speed and payload. Only Dukkanci et al. (2019) had treated speed as a decision variable before, in a cost-minimization model where the truck never delivers; mFSTSP-VDS is the first where both truck and drones deliver. ^[inferred]

![[_papers/raj2020multiple/images/page_2_chart_2.jpg]]

(a) UAV power consumption

![[_papers/raj2020multiple/images/page_2_chart_4.jpg]]

(b) UAV endurance with fixed battery capacity

Battery Capacity = 500 kJ

![[_papers/raj2020multiple/images/page_2_chart_7.jpg]]

(c) UAV range with fixed battery capacity

Fig. 1. UAV power consumption, endurance, and range as functions of speed and payload.

**Maximum-range speeds** are defined as the minimum of the maximum allowable speed and the speed maximizing flight range for a given payload. The naive 25-customer Seattle example shows why optimizing speeds beats both baselines:

Table 1. Comparison of important metrics for the 25-customer example problem.

| Metric | Max drone speeds | Max-range drone speeds | Variable drone speeds |
|---|---|---|---|
| Makespan [hr:min:sec] | 2:29:01 | 2:04:17 | 1:59:07 (20.4% & 4.2% improvements) |
| # UAV customers | 10 | 12 | 13 |
| # Truck customers | 15 | 13 | 12 |
| Avg. UAV speed | 30.0 m/s | 16.1 m/s | 16.7 m/s (44% slower & 4% faster) |
| Total truck distance | 118.8 km | 92.8 km | 89.6 km (25% & 3.5% shorter) |

![[_papers/raj2020multiple/images/page_2_image_10.jpg]]

(a) mFSTSP with 3 UAVs

![[_papers/raj2020multiple/images/page_2_image_12.jpg]]

(b) mFSTSP-VDS with 3 UAVs

Fig. 2. A comparison of routes for a 25-customer problem in Seattle.

Assumptions: one parcel per flight (UAV lands to deliver, as in DHL Parcelcopter / Amazon Prime Air); the driver launches/retrieves one UAV at a time (queueing at truck locations, never during parcel delivery); a UAV is retrieved at a location different from its launch; the truck may serve customers while a UAV is airborne; both vehicles may wait at the retrieval node; a fresh battery before every launch; ground power during parcel delivery is negligible. Launch time $s^L_{vi}$, retrieval time $s^R_{vk}$, truck delivery $\sigma_k$, UAV delivery $\sigma'_{vk}$.

## UAV flight time and endurance

A sortie is a four-tuple $\langle v,i,j,k\rangle$ (launch $i \in N_0$, delivery $j: w_j \le \kappa_v$, retrieval $k \in N_+$) with eight phases (Table 2): vertical takeoff ($\tau^t = h/\nu^t$), cruise $i\to j$ ($\tau^c_{vij} = d_{ij}/\nu^c_{vij}$, **decision variable**), landing, parcel delivery (stationary $\sigma'_{vj}$), takeoff, cruise $j\to k$ (decision), hover-wait $\tau^h_{vk}$ (**decision**), landing. Takeoff/landing speeds are parameters (MAVLink controllers give no speed option; these phases consume little power).

$$T_{vijk}^{\min} = \tau_{vi}^t + \tau_{vij}^c + \tau_{vj}^l + \sigma_{vj}' + \tau_{vj}^t + \tau_{vjk}^c + \tau_{vk}^l \tag{1}$$

![[_papers/raj2020multiple/images/page_5_image_5.jpg]]

Fig. 3. A UAV sortie with different flight phases.

Energy with phase-specific power functions $P^{\mathrm{tl}}(w,\nu)$ (takeoff/landing), $P^{\mathrm{c}}(w,\nu)$ (cruise), $P^{\mathrm{h}}(w)$ (hover):

$$E_{vijk}^{\min} = \tau_{vi}^t P^{\mathrm{tl}}(w_j,\nu_{vi}^t) + \tau_{vij}^c P^{\mathrm{c}}(w_j,\nu_{vij}^c) + \tau_{vj}^l P^{\mathrm{tl}}(w_j,\nu_{vj}^l) + \tau_{vj}^t P^{\mathrm{tl}}(0,\nu_{vj}^t) + \tau_{vjk}^c P^{\mathrm{c}}(0,\nu_{vjk}^c) + \tau_{vk}^l P^{\mathrm{tl}}(0,\nu_{vk}^l) \tag{2}$$

The sortie is feasible only if $E_{vijk}^{\min} \le E_v^{\mathrm{avail}}$; leftover energy buys hover time at the retrieval node:

$$\tau_{vk}^h \le \frac{E_v^{\mathrm{avail}} - E_{vijk}^{\min}}{P^{\mathrm{h}}(0)} \tag{3} \qquad e_{vijk} = \begin{cases} T_{vijk}^{\min} + \frac{E_v^{\mathrm{avail}} - E_{vijk}^{\min}}{P^{\mathrm{h}}(0)} & \text{if } E_{vijk}^{\min} \le E_v^{\mathrm{avail}} \\ 0 & \text{otherwise} \end{cases} \tag{4}$$

## Three-phased heuristic

No MILP is given: the mFSTSP (fixed speeds) is NP-hard, its MILP solved only 8-customer instances to optimality, and Sacramento et al.'s (2019) related VRP IP handled up to 12 customers; variable speeds add nonlinearity. Code: github.com/optimatorlab/mFSTSP-VDS. The outer loop iterates the **lower truck limit** $\mathrm{LTL}_0 = \left\lceil \frac{|C|-|V|}{|V|+1} \right\rceil$ up to $|C|$ (e.g. $|C|=8, |V|=2 \Rightarrow$ LTL 2), and initializes cruise speeds to $\nu^{init} \in \{\nu_{vw}^{\mathrm{maxrange}},\ \nu_{vw}^{\mathrm{maxrange}} + 10\}$ — the max-range speed reaches distant customers, the +10 variant delivers fast when endurance is not binding.

**Phase 1 — partition + truck TSP tour.** Build the feasible-sortie set $P$ (endurance-filtered), put truck-only customers in truckCust, solve the truck TSP to optimality with Gurobi lazy constraints, then exchange customers between truckCust/UAVcust by savings moves until no improvement or the tour repeats. Feasibility is checked with a no-objective IP ($r_{ij}$: launch $j$ from $i$; at most $|V|$ launches per location, exactly one launch per UAV customer); infeasibility is repaired via a Gurobi **IIS** (irreducible inconsistent subsystem) — insert the customer that frees the most infeasCust, and Algorithm 5 forces tour uniqueness by swap, subtour reversal, or full tour reversal (cheapest chosen).

**Phase 2 — assign sorties.** Parameter $s$ = max truck customers between launch and retrieval, $s \in \{0,1,2,3\}$; candidate sorties $support_{sj}$ require $t_k - t_i - \sigma_k \le e_{vijk}$. Rule 1 minimizes truck waiting ($T_{vijk}^{\min} - (t_k - t_i)$), Rule 2 minimizes UAV waiting; UAV customers are processed in order of increasing sortie-option count; 4 × 2 = 8 candidate solutions per truck tour. Unassignable customers trigger insertion back into the truck tour with insertion cost $insCost$ added to the lower bound.

**Phase 3 — schedule activities & re-time speeds.** At each truck node: order = retrievals (sorted by UAV arrival) + parcel delivery + launches (P3Rule 1: decreasing sortie time $T^{\min}$; Rule 2: decreasing endurance $e$; Rule 3: decreasing remaining endurance $e - T^{\min}$); timings computed sequentially with $\max$ of previous-activity end and UAV arrival; the order is then reshuffled to kill truck waiting. Algorithm 10 raises the $j\to k$ then $i\to j$ cruise speed of any UAV that caused truck waiting, using leftover energy until (i) no energy, (ii) no waiting, (iii) max speed. A **local search** replaces a truck-waiting sortie $\langle v,i,j,k\rangle$ with $\langle v,i,j,z\rangle$ (retrieval shifted to the next truck node) and re-runs Phase 3.

## Numerical study

Instances (Seattle area, truck times from pgRouting + OpenStreetMap; $\sigma_k$ 30 s, $\sigma'_{vk}$ 60 s, launch 60 s, retrieval 30 s, payload cap 5 lbs, weights 1–5 lbs for 85% of customers, remaining truck-restricted): **Set 1** — 40 instances, fixed area 918.0 km², 10/25/50/100 customers (5 center + 5 peripheral depot per level). **Set 2** — 4 area levels (57.4, 229.5, 516.4, 918.0 km²) × 10 instances, 50 customers each. Each instance runs with 1, 2, 3, 4 UAVs × max speeds 10, 20, 30, 40 m/s (FAA limit 100 mph = 44.7 m/s) → **1280 test instances**; identical UAVs within an instance. Computing: 8-core Intel i7-6700, 16 GB RAM, Ubuntu 14.04, Python 2.7.6. Liu et al. power model (Table 4: $k_1$=0.8554, $k_2$=0.3051, $c_1$=2.8037, $c_2$=0.3177, $c_4$=0.0296, $c_5$=0.0279; UAV frame weight $W$=1.5 kg, angle of attack 10°, $g$=9.8 m/s², takeoff 10 m/s, landing 5 m/s, battery 500 kJ):

$$P^{\mathrm{tl}}(w,\nu_{\mathrm{ve}}) = k_1 (W+w) g \left[ \frac{\nu_{\mathrm{ve}}}{2} + \sqrt{\left(\frac{\nu_{\mathrm{ve}}}{2}\right)^2 + \frac{(W+w)g}{k_2^2}} \right] + c_2 ((W+w)g)^{3/2} \tag{8}$$

$$P^{\mathrm{c}}(w,\nu_{\mathrm{ho}}) = (c_1+c_2)\left[ \left((W+w)g - c_5(\nu_{\mathrm{ho}}\cos\alpha)^2\right)^2 + (c_4 \nu_{\mathrm{ho}}^2)^2 \right]^{3/4} + c_4 \nu_{\mathrm{ho}}^3 \tag{9}$$

$$P^{\mathrm{h}}(w) = (c_1+c_2)((W+w)g)^{3/2} \tag{10}$$

**Impact of maximum allowable speed** (Table 5, avg. makespan / avg. # UAV customers): savings of the variable-speed case over max speed were **0.0% at 10 m/s, 1.6% at 20 m/s, 11.9% at 30 m/s, 22.2% at 40 m/s**; over the max-range speed **4.1% at 20, 5.5% at 30, 5.4% at 40 m/s** — at 20 m/s the max-range speed performed *worse* than max speed, at 30–40 m/s it performed better; variable speed beat both in every setting. Extremes from Table 5: 10 customers at max speed 40 m/s: 1:49:50 → 1:20:47 (26.5% saved), UAV customers 0.6 → 5.1 (+787%); 25 customers: 2:59:42 → 2:12:19 (26.1%); 50: 3:59:46 → 3:04:37 (22.8%); 100: 5:34:59 → 4:50:06 (13.3%). Savings shrink as customer count grows (density rises in a fixed area).

![[_papers/raj2020multiple/images/page_13_chart_2.jpg]]

(a) Improvement over maximum allowable speed

![[_papers/raj2020multiple/images/page_13_chart_4.jpg]]

(b) Improvement over maximum-range speed

Fig. 4. Comparison of improvements afforded by variable drone speeds for different maximum allowable speeds. Numbers above each boxplot represent the mean value.

![[_papers/raj2020multiple/images/page_13_chart_7.jpg]]

Fig. 5. UAV range at various speeds.

![[_papers/raj2020multiple/images/page_14_chart_2.jpg]]

(a) 50-customer problems

![[_papers/raj2020multiple/images/page_14_chart_4.jpg]]

(b) 100-customer problems

Fig. 6. Comparison of improvements afforded by maximum drone speeds, maximum-range drone speeds, and variable drone speeds over optimal TSP solutions without any drones.

**Speeds, cost, energy** (Tables 6–8): VDS average speed sits between the two fixed cases (with parcel: e.g. 100 customers at 40 m/s — MS 40.0, MRS 18.8, VDS 23.2 m/s; empty: 40.0 / 14.0 / 20.1). VDS average speed barely moves when max speed rises from 20 to 40 m/s → investing in fast UAVs is not always worthwhile; speeds are higher with a parcel because max-range speed grows with payload. Truck distance falls up to **30.7%** vs max speed and **10.5%** vs max range (best cells: 25 customers at 40 m/s 151.5 → 105.0 km; 100 at 40 m/s 205.9 → 162.9 km); average truck-distance savings of 9.5 miles/day vs max speed and 3.9 miles vs max range translate, on the quoted UPS $50M-per-mile-per-driver rule, to **$475M and $195M annually**. Truck waiting drops vs max range in all cases (up to 52.7%) and vs max speed in most. UAV energy per sortie falls vs max speed (up to 25.6%, 100 customers at 40 m/s: 389.8 → 289.9 kJ; max range is always most efficient), and UAV loiter time falls vs both fixed cases (up to 64.1%) — less noise and vandalism exposure for hovering drones. ^[inferred]

![[_papers/raj2020multiple/images/page_16_chart_4.jpg]]

(a) Comparison against maximum allowable speed

![[_papers/raj2020multiple/images/page_16_chart_6.jpg]]

(b) Comparison against maximum-range speed

Fig. 7. Comparison of improvements afforded by variable drone speeds for different service areas with 50 customers. Numbers above each boxplot represent the mean value.

**Customer density** (Set 2, Fig. 7): savings over max speed grow with service area — in dense regions launch/retrieval points are close, so max-speed UAVs never run out of battery; in sparse regions slower flight buys the range to reach distant customers. Savings over max range also grow with area, because in large regions max-range-speed sorties take long and cause truck waiting that the VDS heals by speeding up. ^[inferred]

**Heuristic performance on mFSTSP** (Table 9, 1600 public Murray & Raj instances, cruise speeds fixed to disable Phase-3 speed edits): average improvement 1.93% (8c), 1.93% (10c), 1.20% (25c), 0.77% (50c), 1.13% (100c); better-or-equal solutions on 141/241, 172/278, 176/185, 178/178, 202/202 of 320 instances (strict/bolded counts as printed: e.g. 10c: 172 better, 278 better-or-equal); run time is lower for 50-customer (28.07 s vs 39.55 s) and 100-customer (394.28 s vs 582.25 s) problems, higher for small ones (0.18 vs 0.10 s at 8c). Against the 212 optimal 8-customer solutions: average gap **2.3% vs 5.0%**, max gap **23.3% vs 44.2%**, **61 of 212 vs 51 of 212** optima found — the new heuristic is the state of the art for both mFSTSP and mFSTSP-VDS. ^[ambiguous] — Table 9's "(241)"-style second numbers are printed parenthetically in the source; their exact semantics (better vs better-or-equal split) is as rendered.

## Conclusions & future work

Variable speed helps whenever the maximum allowable speed exceeds the maximum-range speed (in the experiments, ≥ 20 m/s); flying at max-range speed alone is not enough; more customers shift to UAV service, shortening truck tours; energy per sortie and loiter time drop; dense customer distributions negate the benefit. Future work: no IP formulation exists for mFSTSP-VDS (exact methods/tight bounds needed), extension to multi-truck problems, the PDSTSP [[concepts/parallel-drone-scheduling-traveling-salesman-problem]], non-customer launch/retrieval locations, and variable-speed trucks with an emissions objective.

## Related

- [[references/murray2020-multiple-flying-sidekicks-tsp]] — the mFSTSP base paper this extends.
- [[concepts/drone-speed-selection-in-routing]] — the speed-as-decision-variable concept this paper implements. ^[inferred]
- [[references/liu2017power]] — the multi-rotor power model underlying the endurance equations.
- [[concepts/nonlinear-drone-energy-function-in-routing]], [[concepts/payload-induced-drone-battery-consumption-rate]] — energy-model genealogy.
- [[references/murray2015flying]] — FSTSP/PDSTSP origin of the family.

## Sources

- [[_papers/raj2020multiple/raj2020multiple-extracted]]
- [[_papers/raj2020multiple/raj2020multiple]]
- [[_papers/raj2020multiple/images/page_2_chart_2.jpg]], [[_papers/raj2020multiple/images/page_2_chart_4.jpg]], [[_papers/raj2020multiple/images/page_2_chart_7.jpg]]
- [[_papers/raj2020multiple/images/page_2_image_10.jpg]], [[_papers/raj2020multiple/images/page_2_image_12.jpg]]
- [[_papers/raj2020multiple/images/page_5_image_5.jpg]]
- [[_papers/raj2020multiple/images/page_13_chart_2.jpg]], [[_papers/raj2020multiple/images/page_13_chart_4.jpg]], [[_papers/raj2020multiple/images/page_13_chart_7.jpg]]
- [[_papers/raj2020multiple/images/page_14_chart_2.jpg]], [[_papers/raj2020multiple/images/page_14_chart_4.jpg]]
- [[_papers/raj2020multiple/images/page_16_chart_4.jpg]], [[_papers/raj2020multiple/images/page_16_chart_6.jpg]]
