---
title: An Efficient Hybrid Genetic Algorithm for the Quadratic Traveling Salesman Problem
category: references
tags: [metaheuristics, genetic-algorithm, quadratic-tsp, ruin-and-recreate, double-bridge, matheuristics]
relationships:
  - target: "[[concepts/large-neighborhood-search]]"
    type: derived_from
  - target: "[[references/pisinger2019-large-neighborhood-search]]"
    type: related_to
  - target: "[[concepts/metaheuristic-hybridization]]"
    type: related_to
sources:
  - _papers/pham2023efficient/pham2023efficient-extracted.md
  - _papers/pham2023efficient/pham2023efficient.md
  - _papers/pham2023efficient/images/page_2_image_0.jpg
  - _papers/pham2023efficient/images/page_4_image_0.jpg
  - _papers/pham2023efficient/images/page_4_image_9.jpg
  - _papers/pham2023efficient/images/page_4_image_11.jpg
  - _papers/pham2023efficient/images/page_7_chart_8.jpg
summary: >-
  A biased-fitness genetic algorithm with a restricted double-bridge local search finds new best-known solutions on 437 of 450 quadratic TSP benchmark instances and closes the gap to the state-of-the-art matheuristic at every tested size.
provenance:
  extracted: 0.88
  inferred: 0.09
  ambiguous: 0.03
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-25
tier: supporting
created: 2026-10-25T14:33:00Z
updated: 2026-10-25T14:33:00Z
---

# An Efficient Hybrid Genetic Algorithm for the Quadratic Traveling Salesman Problem

> [!tldr] The Quadratic TSP costs arcs by node triples, so TSP heuristics fail on it; a hybrid genetic algorithm with a corrected O(n^2) restricted double-bridge beats the best published matheuristic on all four benchmark families.

## Problem & Motivation

In the Quadratic Traveling Salesman Problem the cost of visiting node i after visiting j depends on the predecessor of i: a tour sigma of n nodes is paid as \(\sum_{i=0}^{n-1} c_{\sigma(i)\sigma(i+1)\sigma(i+2)}\) (Eq. 1, with sigma(0)=sigma(n), sigma(n+1)=sigma(1)). The problem is NP-hard: Angle-TSP (Aggarwal et al. 2000) admits only an O(log n) approximation, and Angle-Distance-TSP models Dubins-vehicle turning costs (Savla 2008); the asymmetric 2-TSP equals an optimal Permuted Markov model used for binding-site modelling in bioinformatics (Jäger & Molitor 2008). Exact work stops early: branch-and-bound solves at most 26 nodes (about three weeks), polyhedral branch-and-cut up to 30 nodes (Fischer & Helmberg 2013), Fischer 2014 reaches 2-TSP n≤40 in under 10 seconds, and the TSP-R transformation turns a 15-node QTSP into a 420-node TSP, practical to 20 nodes. Simple TSP heuristics (CI, nearest-neighbor, k-Opt) give tours nearly twice the optimum. The prior state of the art is Stanek et al. (2019, Computers & Operations Research 108:97-111), a matheuristic whose worst optimal gap is slightly over 10%; deep reinforcement learning (Zhang et al. 2022, Transformer) sometimes exceeds 30%.

![[/home/tatdatnguyen/tatdat-vault/_papers/pham2023efficient/images/page_2_image_0.jpg]]

*Figure 1: Overview of HGA metaheuristic*

## Method / Architecture

The Hybrid Genetic Algorithm (HGA) is inspired by the Hybrid Genetic Search for vehicle routing (Vidal et al. 2012, Operations Research 60(3):611-624) and is the first strong metaheuristic for the QTSP.

- Population management: individuals scored by biased fitness (Eq. 2) combining cost with normalized diversity contribution; diversity dc averages the broken-pair distance \(\delta(P_i,P_j)=\Phi(P_i,P_j)/n\) (Eqs. 3-4) to the closest \(|N_{close}|=2\) individuals; binary tournament selects parents twice; growth to \(\mu+\lambda\), remove \(\lambda\) by clones + biased fitness; after \(It_{div}=4000\) non-improving iterations, diversification keeps only \(\mu/3\) best.
- Crossover: ordered crossover (OX), a permutation operator that keeps arc information meaningful.
- Mutation: ruin-and-recreate (Schrimpf et al. 2000) with probability \(p_{mut}=0.9\) — the mutation's goal is diversification, not improvement, so the offspring is not necessarily better than the parent (in contrast to LNS, Shaw 1998). Removal: worst removal (cost-saving probability-weighted, Ropke & Pisinger 2006) or block removal (p consecutive nodes, Veenstra et al. 2017); insertion: random or cheapest insertion (Fischer et al. 2014); one pair chosen uniformly at random.
- Local search, two phases: (1) first-improvement over neighborhoods N1 Relocate1, N2 Relocate2, N3 Swap1-1, N4 Swap1-2, N5 Swap2-1, N6 Swap2-2, N7 2-Opt, scanned over a granular candidate list L(u) of the \(\Gamma=20\) closest neighbors w.r.t. \(\pi(u,v)=c_{w,u,v}\) (w = predecessor of u), complexity \(O(\Gamma n)\); (2) when phase 1 finds nothing, a restricted double-bridge with probability \(p_{4Opt}=0.3\).

![[/home/tatdatnguyen/tatdat-vault/_papers/pham2023efficient/images/page_4_image_0.jpg]]

*Figure 2: An illustration of double-bridge move*

![[/home/tatdatnguyen/tatdat-vault/_papers/pham2023efficient/images/page_4_image_9.jpg]]

*Figure 3: An illustration of disconnecting 2-Opt move*

![[/home/tatdatnguyen/tatdat-vault/_papers/pham2023efficient/images/page_4_image_11.jpg]]

*Figure 4: A special case of double-bridge move with $i_1 = i_2 - 1$*

## Key Equations

- Eq. (1): \(cost(\sigma)=\sum_{i=0}^{n-1} c_{\sigma(i)\sigma(i+1)\sigma(i+2)}\).
- Eq. (2): biased fitness \(BF(P_i)=f^C(P_i)+(1-\frac{\mu_{ELITE}}{|P|})f^D(P_i)\).
- Eq. (5): double-bridge gain \(\Delta(i_1,i_2,j_1,j_2)=\Delta^2O^D(i_1,j_1)+\Delta^2O^D(i_2,j_2)\); Eq. (6) expands \(\Delta^2O^D\) as four new triple costs minus four old ones.
- Eq. (7) of Pacheco et al. (2022) is **incorrect for the QTSP** when \(i_1=i_2-1\), \(j_1=i_2+1\), or \(j_1=j_2-1\): the term \(c_{\sigma(j_1),\sigma(i_1+1),\sigma(j_2+1)}\) is missing. Corrected full enumeration costs \(O(n^3)\) for QTSP (vs \(O(n^2)\) for TSP). The paper's restricted neighborhood covers case 1 (all gaps ≥2, via DP \(F(i_2,j_1)=\min_{i_1\le i_2-2}\Delta^2O^D\) and recursive Eqs. 12-13, \(O(n^2)\)) and case 3 (≥2 adjacencies, \(O(n^2)\)), skipping case 2 (exactly one adjacency, \(O(n^3)\)).
- Tuned parameters (Table 1, IRACE): \(p_{mut}=0.9\), \(It_{max}=50000\), \(\mu_{ELITE}=5\), \(|N_{close}|=2\), \(p_{min}=5\), \(p_{max}=\min(40,n/3)\), \(\Gamma=20\), \(p_{4Opt}=0.3\), \(\mu=25\), \(\lambda=40\), \(It_{div}=4000\).

## Results

Head-to-head against the Stanek matheuristic (MH), mean over instances, Gap = mean % over optimum, #Best = count of runs hitting the optimum:

| Family | |V| | HGA Gap / Avg / Time / #Best | MH Gap / Avg / Time / #Best |
|---|---|---|---|
| Angle-opt | 5-75 | 0.00 / 0.004 / 87.41 / 150 | 0.92 / 27.14 / 83 / — |
| Angle-hard | 80-200 | −2.61 / −1.83 / 831.05 / 250 | 1.02 / 462.96 / 152 / — |
| Angle-dis-opt | 5-100 | 0.00 / 0.00 / 130.94 / 200 | 0.33 / 26.99 / 115 / — |
| Angle-dis-hard | 105-200 | −0.46 / −0.46 / 945.44 / 200 | 0.47 / 354.45 / 33 / — |

- 437 new best-known solutions among 450 instances with no proved optimum (800 instances total, 10 runs each); negative gaps mean HGA beats published optima.
- Ablation (Angle-hard): full HGA Gap −2.608 / 250 best; without restricted double-bridge −2.540 / 249; without mutation −1.437 / 223; without both −1.062 / 204 — mutation is the more vital operator, the double-bridge is needed to reach every optimum.
- Scaling: 400-node instances solve in under 2 hours; running time follows a quadratic function (Figure 5); stability (gap vs own best) grows from 0.00% at n=50 to 1.91% at n=400.

![[/home/tatdatnguyen/tatdat-vault/_papers/pham2023efficient/images/page_7_chart_8.jpg]]

*Figure 5: The growth in the running time of HGA*

## Limitations

- Running-time comparison with MH is declared unfair by the authors: HGA ran single-CPU on a Ryzen 7 3700X, MH multi-thread on an i7-4790 about 16% slower.
- Heuristic: no optimality guarantee, and stability degrades with size (1.91% mean gap at n=400).
- Future work stated: exact algorithms for larger instances.

## Related

- [[concepts/large-neighborhood-search]] — the ruin-and-recreate mutation is LNS-style destruction, adapted to a genetic setting where mutation is for diversification, not improvement.
- [[references/pisinger2019-large-neighborhood-search]] — the LNS/ALNS chapter that defines destroy-repair design principles HGA borrows; the paper also cites Ropke & Pisinger 2006 for worst removal.
- [[concepts/metaheuristic-hybridization]] — HGA is a population metaheuristic hybridized with local search and ruin-and-recreate operators.

## Sources

- [[_papers/pham2023efficient/pham2023efficient-extracted.md]]
- [[_papers/pham2023efficient/pham2023efficient.md]]
- Bibliographic record: Pham, Lau, Hà, Vu (2023), ICAPS 2023, DOI 10.1609/icaps.v33i1.27212, https://ojs.aaai.org/index.php/ICAPS/article/view/27212. Zotero: Pham 2023 PDF, key W3LWQDH9.
