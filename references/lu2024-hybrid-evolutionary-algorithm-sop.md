---
title: Hybrid Evolutionary Algorithm for the Set Orienteering Problem (Lu et al.)
category: references
tags: [paper, orienteering, metaheuristics]
relationships:
  - target: "[[concepts/set-orienteering-problem]]"
    type: related_to
  - target: "[[concepts/tabu-search]]"
    type: related_to
  - target: "[[references/gendreau2019-handbook-metaheuristics]]"
    type: related_to
  - target: "[[concepts/transformer-seq2seq-routing-solver]]"
    type: related_to
  - target: "[[references/archetti2018-set-orienteering-problem]]"
    type: related_to
  - target: "[[references/archetti2023-branch-and-cut-sop]]"
    type: related_to
  - target: "[[references/nguyen2025set]]"
    type: related_to
  - target: "[[references/yu2024-sarl-stoptw]]"
  - target: "[[references/yu2024-sarl-stoptw]]"
    type: related_to
  - target: "[[concepts/multi-objective-metaheuristic-tuning-validation]]"
    type: related_to
  - target: "[[concepts/hybridization-evolutionary-local-search]]"
    type: related_to
sources:
  - _papers/lu2024effective/lu2024effective-extracted.md
  - _papers/lu2024effective/lu2024effective.md
  - _papers/lu2024effective/images/page_0_image_8.jpg
  - _papers/lu2024effective/images/page_3_image_2.jpg
  - _papers/lu2024effective/images/page_6_image_2.jpg
  - _papers/lu2024effective/images/page_8_image_2.jpg
  - _papers/lu2024effective/images/page_17_chart_5.jpg
  - _papers/lu2024effective/images/page_17_chart_7.jpg
summary: Presents a hybrid evolutionary algorithm for SOP with cluster-aware crossover and two-phase local refinement, reporting strong benchmark performance.
provenance:
  extracted: 0.9
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-24
tier: core
created: 2026-10-22T11:22:57Z
updated: 2026-10-31T19:26:46Z
---

# Hybrid Evolutionary Algorithm for the Set Orienteering Problem (Lu et al.)

> [!tldr] This paper introduces a hybrid evolutionary algorithm (HEA) for SOP that combines cluster-based crossover, randomized mutation, and two-phase local refinement; it reports strong results on 192 large benchmark instances.

## Problem & Contribution

[[references/archetti2018-set-orienteering-problem|The Set Orienteering Problem]] (SOP) maximizes collected cluster profit under a travel-time budget. Vertices are grouped into clusters, and a cluster contributes profit if at least one of its vertices is visited.

![[_papers/lu2024effective/images/page_3_image_2.jpg]]

*Fig. 1. An example of a SOP tour.* (`_papers/lu2024effective/lu2024effective-extracted.md:69-71`)

The paper proposes an HEA tailored to SOP and positions it against existing SOP heuristics.

## Method

The HEA combines:

1. randomized population initialization,
2. cluster-based crossover,
3. randomized mutation,
4. two-phase local refinement (feasible + infeasible search),
5. population update with quality/diversity control.

The two-phase refinement uses tabu-search style move control and explicitly explores infeasible regions to escape local traps before returning to feasibility.

Construction orders non-visited clusters by decreasing profit-to-extra-time ratio and inserts a cluster vertex only while the budget holds (`_papers/lu2024effective/lu2024effective-extracted.md:181`):

$$
\text{visit } C_g \text{ in order of } \frac{p_g}{e_v}, \qquad t(S) + e_v \le T_{max}, \qquad v \in C_g
$$

Boxplot comparisons use the normalized average quality, which is the basis of the Wilcoxon and t-test statements (`:421, 629`):

$$
y = 100 \times \frac{f_{BK} - f_{avg}}{f_{BK}}
$$

Parameter values were set by F-race on 24 large instances, 1000 runs (`:372-385`):

| Parameter | Meaning | Tuned value |
| --- | --- | --- |
| `p` | population size | 5 |
| `L` | local-search depth | 400 |
| `α` | tabu-tenure factor | 0.05 |
| `u_c` | tour-improvement frequency | 30 |
| `u_p` | `φ`-update frequency | 5 |
| `η` | mutation strength | 5 |
The cluster-based crossover is the evolutionary analogue of the clustering + masked-construction pipeline of learned routing policies [[concepts/transformer-seq2seq-routing-solver]]: both exploit cluster structure under a travel-time budget, one by population operators, one by a state-conditioned policy. ^[inferred]

The population keeps `p = 5` individuals while `L = 400`-depth tabu search handles intensification, so the evolutionary part contributes diversity rather than search power — the improvement comes from the combination [[concepts/hybridization-evolutionary-local-search]]. ^[inferred]

From the source text:

- Extensive experiments are reported on 192 large SOP benchmark instances.
- The abstract reports improved best-known solutions for 54 instances and matches for 133 instances (`:25`).
- §5.4 counts 81 improved and 107 matched against the three recent heuristics on the same 192 instances (`:412`), and Table 7 reports 47, 47, 46 and 48 best-solution wins for HEA per `w` group (`:445`). The abstract's 54/133 and §5.4's 81/107 use different denominators (new best-known solutions vs. wins against the three heuristics), so they are not the same quantity. ^[ambiguous]

Table 7 (best-solution wins out of 48 per `w`, average gap, average time):

| `w` | MA-SOP | VNS-SOP | BRKGA | HEA |
| --- | --- | --- | --- | --- |
| 0.4 | 25/48, 0.52 %, 220.1 s | 26/48, 1.60 %, 56.9 s | 29/48, 0.32 %, 32.6 s | 47/48, 0.00 %, 63.2 s |
| 0.6 | 22/48, 0.38 %, 123.3 s | 16/48, 1.97 %, 97.3 s | 23/48, 0.70 %, 54.6 s | 47/48, 0.01 %, 63.2 s |
| 0.8 | 23/48, 0.30 %, 93.0 s | 18/48, 1.27 %, 144.7 s | 17/48, 1.21 %, 75.6 s | 46/48, 0.01 %, 63.2 s |
| 1.0 | 22/48, 0.19 %, 224.6 s | 26/48, 0.23 %, 208.3 s | — | 48/48, 0.00 %, 64.2 s |

Against AMMH under the long time limit `n × m / 400` s, HEA was better/equal/worse on 37/102/5 of 144 instances (`:463`); the t-test p-values were below 0.05 for every group, and the two-phase tabu search (TS12) beat both single-phase variants on the `w = 0.8` group (`:639-643`, Fig. 5).
- A Wuhan one-day trip case study reports average gain of about 5.72% versus a greedy heuristic.

## Limitations

- Performance evidence is benchmark-heavy; real deployment quality depends on travel-time and clustering calibration. ^[inferred]
- Reported improvement counts vary by section and benchmark slice, so exact headline counts should be interpreted with the comparison setup in mind. ^[ambiguous]

## Bibliographic Record

- Citation key: `lu2024effective`
- DOI: `10.1016/j.ins.2023.119813`
- Canonical URL: https://www.sciencedirect.com/science/article/pii/S0020025523013981
- Publication: *Information Sciences* (2024)
- Authors: Yongliang Lu, Una Benlic, Qinghua Wu
- Companion metadata note: [[_papers/lu2024effective/lu2024effective.md]]

## Related

- [[concepts/set-orienteering-problem]]
- [[concepts/tabu-search]]
- [[concepts/hyper-heuristics]] — HEA is a population-based metaheuristic whose operators are fixed rather than selected, so it sits outside the hyper-heuristic frame while sharing the same problem and budget.
- [[references/gendreau2019-handbook-metaheuristics]]
- [[concepts/transformer-seq2seq-routing-solver]]
- [[_papers/lu2024effective/lu2024effective-extracted]]

## Sources

- [[_papers/lu2024effective/lu2024effective-extracted.md]]
- [[_papers/lu2024effective/lu2024effective.md]]
- [[_papers/lu2024effective/images/page_0_image_8.jpg]]
- [[_papers/lu2024effective/images/page_3_image_2.jpg]]
- [[_papers/lu2024effective/images/page_6_image_2.jpg]]
- [[_papers/lu2024effective/images/page_8_image_2.jpg]]
- [[_papers/lu2024effective/images/page_17_chart_5.jpg]]
- [[_papers/lu2024effective/images/page_17_chart_7.jpg]]
