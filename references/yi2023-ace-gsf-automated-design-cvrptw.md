---
title: Yi & Qu 2023 — Automated Design of Search Algorithms based on Reinforcement Learning
summary: "Actor-Critic with Entropy (ACE) over the GSF design space: evolution operators + selection heuristics for CVRPTW. Learning on both components beats evolution-operator-only design; ACE LAS is the best variant."
tags: reinforcement-learning, automated-algorithm-design, hyper-heuristics, vrptw, evolutionary-computation, max-entropy
provenance:
  extracted: 0.82
  inferred: 0.14
  ambiguous: 0.04
base_confidence: 0.67
tier: supporting
created: 2026-10-29T18:10:00Z
updated: 2026-10-29T18:10:00Z
sources:
  - _papers/yi2023automated/yi2023automated.md
  - _papers/yi2023automated/yi2023automated-extracted.md
  - _papers/yi2023automated/images/page_8_image_4.jpg
  - _papers/yi2023automated/images/page_11_image_0.jpg
  - _papers/yi2023automated/images/page_11_image_1.jpg
  - _papers/yi2023automated/images/page_11_image_2.jpg
  - _papers/yi2023automated/images/page_11_image_5.jpg
  - _papers/yi2023automated/images/page_11_image_6.jpg
  - _papers/yi2023automated/images/page_11_image_7.jpg
  - _papers/yi2023automated/images/page_11_image_8.jpg
  - _papers/yi2023automated/images/page_11_image_10.jpg
  - _papers/yi2023automated/images/page_11_image_11.jpg
  - _papers/yi2023automated/images/page_11_image_13.jpg
  - _papers/yi2023automated/images/page_11_image_14.jpg
  - _papers/yi2023automated/images/page_13_image_0.jpg
  - _papers/yi2023automated/images/page_19_image_4.jpg
  - _papers/yi2023automated/images/page_21_chart_1.jpg
  - _papers/yi2023automated/images/page_21_chart_3.jpg
  - _papers/yi2023automated/images/page_21_chart_5.jpg
  - _papers/yi2023automated/images/page_21_chart_7.jpg
  - _papers/yi2023automated/images/page_21_chart_9.jpg
  - _papers/yi2023automated/images/page_21_chart_10.jpg
  - _papers/yi2023automated/images/page_21_chart_12.jpg
  - _papers/yi2023automated/images/page_21_chart_13.jpg
  - _papers/yi2023automated/images/page_21_chart_14.jpg
  - _papers/yi2023automated/images/page_21_chart_16.jpg
  - _papers/yi2023automated/images/page_21_chart_18.jpg
  - _papers/yi2023automated/images/page_21_chart_20.jpg
  - _papers/yi2023automated/images/page_21_chart_22.jpg
  - _papers/yi2023automated/images/page_21_chart_26.jpg
  - _papers/yi2023automated/images/page_21_chart_29.jpg
  - _papers/yi2023automated/images/page_21_chart_31.jpg
  - _papers/yi2023automated/images/page_27_chart_0.jpg
  - _papers/yi2023automated/images/page_27_chart_2.jpg
  - _papers/yi2023automated/images/page_27_chart_4.jpg
  - _papers/yi2023automated/images/page_27_chart_5.jpg
  - _papers/yi2023automated/images/page_27_chart_8.jpg
  - _papers/yi2023automated/images/page_27_chart_9.jpg
  - _papers/yi2023automated/images/page_27_chart_10.jpg
  - _papers/yi2023automated/images/page_27_chart_11.jpg
  - _papers/yi2023automated/images/page_27_chart_13.jpg
  - _papers/yi2023automated/images/page_27_chart_15.jpg
  - _papers/yi2023automated/images/page_27_chart_17.jpg
  - _papers/yi2023automated/images/page_27_chart_19.jpg
  - _papers/yi2023automated/images/page_27_chart_21.jpg
  - _papers/yi2023automated/images/page_27_chart_24.jpg
  - _papers/yi2023automated/images/page_27_chart_27.jpg
  - _papers/yi2023automated/images/page_27_chart_30.jpg
  - _papers/yi2023automated/images/page_33_chart_0.jpg
  - _papers/yi2023automated/images/page_33_chart_2.jpg
  - _papers/yi2023automated/images/page_33_chart_4.jpg
  - _papers/yi2023automated/images/page_33_chart_5.jpg
  - _papers/yi2023automated/images/page_33_chart_8.jpg
  - _papers/yi2023automated/images/page_33_chart_9.jpg
  - _papers/yi2023automated/images/page_33_chart_10.jpg
  - _papers/yi2023automated/images/page_33_chart_11.jpg
  - _papers/yi2023automated/images/page_33_chart_13.jpg
  - _papers/yi2023automated/images/page_33_chart_15.jpg
  - _papers/yi2023automated/images/page_33_chart_17.jpg
  - _papers/yi2023automated/images/page_33_chart_19.jpg
  - _papers/yi2023automated/images/page_33_chart_21.jpg
  - _papers/yi2023automated/images/page_33_chart_24.jpg
  - _papers/yi2023automated/images/page_33_chart_27.jpg
  - _papers/yi2023automated/images/page_33_chart_30.jpg
  - _papers/yi2023automated/images/page_41_chart_0.jpg
  - _papers/yi2023automated/images/page_41_chart_2.jpg
  - _papers/yi2023automated/images/page_41_chart_4.jpg
  - _papers/yi2023automated/images/page_41_chart_6.jpg
  - _papers/yi2023automated/images/page_42_chart_0.jpg
  - _papers/yi2023automated/images/page_42_chart_2.jpg
  - _papers/yi2023automated/images/page_42_chart_4.jpg
  - _papers/yi2023automated/images/page_42_chart_6.jpg
  - _papers/yi2023automated/images/page_43_image_0.jpg
  - _papers/yi2023automated/images/page_43_image_2.jpg
  - _papers/yi2023automated/images/page_43_image_4.jpg
  - _papers/yi2023automated/images/page_43_image_6.jpg
relationships:
  - {target: "concepts/actor-critic-entropy-automated-algorithm-design", type: related_to}
  - {target: "concepts/state-features-rl-algorithm-design", type: related_to}
  - {target: "concepts/entropy-coefficient-adjustment-schemes", type: related_to}
  - {target: "concepts/rl-component-analysis-designed-algorithms", type: related_to}
  - {target: "concepts/hyper-heuristics", type: supports}
lifecycle: source
lifecycle_changed: 2026-10-29T18:10:00Z
---

> [!tldr] Yi & Qu 2023 (*Information Sciences* 2023-09-01, DOI 10.1016/j.ins.2023.119639, Zotero key `I57FD6C6`): **Actor-Critic with Entropy (ACE-GSF)** learns selection heuristics, evolution operators, and their combinations inside the GSF, on CVRPTW. Learning on selection heuristics alone is weak; learning on **both** selection heuristics and evolution operators beats evolution-operator-only design. ACE LAS (linear entropy coefficient `α_t+1 = α_t · 0.9998`) is the best variant and transfers its R101 policy to C101, C201, R105, R201, RC101, RC201.

## Source
- [[_papers/yi2023automated/yi2023automated]] — sidecar, Zotero key `I57FD6C6`, library-id 11058526, item-version 4677, citationKey `yi2023automated`, Wenjie Yi & Rong Qu, journalArticle, *Information Sciences*, date 2023-09-01, DOI 10.1016/j.ins.2023.119639, tags #Automated_algorithm_design #Reinforcement_learning #Vehicle_routing_problem_with_time_windows.
- [[_papers/yi2023automated/yi2023automated-extracted]] — extracted text (1,098 lines).

## Overview
Wenjie Yi (CVRPTW experiments in the GSF built in Java with IntelliJ IDEA 2020.3.3) and Rong Qu (Automated Design of Search Algorithms based on Reinforcement Learning, *Information Sciences*, 2023-09-01, DOI 10.1016/j.ins.2023.119639). Funding: School of Computer Science, University of Nottingham, UK.

A general combinatorial optimisation problem (GCOP) model defines the design of search algorithms itself as a COP, whose solutions are new general-purpose algorithms composed of basic algorithmic components. GSF has five modules, of which **Selection for Evolution, Evolution, and Selection for Replacement** contribute most to algorithm performance. The paper investigates the three key automated-design issues (learning on evolution operators, on selection heuristics, and on both) and proposes ACE — a maximum-entropy RL technique — on CVRPTW.  ^[inferred]

The stated contributions: systematic exploration of the design space within GSF modules against the ad hoc design space; ACE for a new learning problem with a continuous state space and a high-dimensional discrete action space; and comprehensive CVRPTW experiments demonstrating effectiveness and generality. ^[inferred]

## Design space (GSF)
- Three issues: **learning on evolution operators** (decision variables = evolution operators, Evolution module fixed elsewhere); **learning on selection heuristics** (Selection for Evolution/Replacement modules, Evolution fixed); **learning on both** (actions = pairs of evolution operators and selection heuristics). ^[inferred]
- Evolution operators `O_E` (Table 1, from GSF ref [5]): `ochg_in` (exchange m and n nodes in the same route), `ochg_bw` (exchange nodes from different routes), `oins_in` (insert m nodes into other positions of the same route), `oins_bw` (insert m nodes into other routes), `oruin_recreat` (remove m nodes within a distance d to base customer x, d set from x-to-furthest-node distance, insert at the minimum waiting time if feasible routes exist, otherwise create a new route), `otwo_opt` (exchange two nodes in the same route), `otwo_opt*` (swap the end sections of two routes, m nodes each). ^[inferred]
- Selection-for-Evolution heuristics `H_SE` (Table 2): `h1tb/h1tw` tournament selection of the best/worst of v ∈ {1,...,nPop} individuals (v = 1 random, v = nPop greedy, p_i = 1/nPop); `h2` random selection (v = 1); `h3` rank selection of the best previous position from each individual's personal archive (v = nPop); `h4` proportionate roulette wheel selection proportional to fitness; `h5` ranking selection proportional to rank (ascending fitness); `h6` select the current individual itself as parent. ^[inferred]
- Selection-for-Replacement heuristics `H_SR` (Table 3): `h7` comma-selection (nPop, λ — select nPop individuals only from the offspring population A_O); `h8` plus-selection (nPop, μ+λ — select from both the parent population A_P and the offspring population A_O). ^[inferred]
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_8_image_4.jpg]] — Figure 1: Solution encoding of a CVRPTW with nine customers and three vehicles
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_11_image_0.jpg]] — (a) `o_chg_in (m = n = 1)`, `o_two_opt`
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_11_image_1.jpg]] — (b) `rho_chg_bw` (m = n = 1)
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_11_image_2.jpg]] — Figure 2: Illustration of evolution operators in Table 1
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_11_image_5.jpg]] — (c) `o_in_in (m = 2)`
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_11_image_6.jpg]] — (d) `o_ins_bw (m = 2)`
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_11_image_13.jpg]] — (f) `o_two_opt* (m = 2)`

- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_13_image_0.jpg]] — Figure 3: Proposed reinforcement learning method (ACE) for automated algorithm design within GSF
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_19_image_4.jpg]] — Figure 4: Solution decoding of a CVRPTW with nine customers and three vehicles

## ACE method
- MDP `M = (S, A, p, r)`; modified soft actor-critic (SAC) for discrete action space. Objective = **accumulated reward + entropy of the policy**: `r_π(s_t,a_t) = r(s_t,a_t) + α · H[π(·|s_t)]` (Eq. 1). Higher α gives more chances to rarely selected actions (exploration); lower α emphasizes actions with good historical performance (exploitation). ^[inferred]
- **α adjustment schemes**: FS (fixed, α = 0.5); **LAS** (`α_{t+1} = α_t · 0.9998`); NLAS (decrease α nonlinearly, via a neural network). ^[inferred]
- Actor-critic architecture: one policy network (Actor), two critic networks `Q_ω1`, `Q_ω2` with the same structure, exporting min(Q_ω1, Q_ω2) to eliminate overestimation; experience replay buffer breaks correlations between stored experiences `(s_t, a_t, r_t, s_{t+1})` and reuses them. ^[inferred]
- Critic loss `L = (1/J) Σ_j (y_j − Q_ωi(s_j,a_j))²` (Eq. 2); TD target `y_j = r_j + γ(min_{i=1,2} Q_ωi⁻(s_{j+1},a_{j+1}) − α log π_θ(a_{j+1}|s_{j+1}))` (Eq. 3); actor loss `L_π(θ) = (1/J) Σ_j (α log π_θ(a_j|s_j) − min_i Q_ωi(s_j,a_j))` (Eq. 4); soft target update `ω⁻ ← τ ω + (1−τ) ω⁻` with τ close to 1. ^[inferred]
- Algorithm 1: for each episode k, for each timestep t: observe state `s_t` from state features, select `a_t = π_θ(s_t)`, execute it on the population (a combination of components from the three main GSF modules), observe reward and store the experience in D, sample a minibatch of J, update two critics and the actor, update α by FS/LAS/NLAS, every N timesteps update the target critic networks. ^[inferred]
- Reward scheme (Eqs. 5–6): `f_1 = f_current / f_initial`; `r_π = −f_1 + α·H` if f_1 > C, and `−f_1 − log_10(f_1) + α·H` if f_1 ≤ C — a larger reward for the same fitness improvement, via a log function, when population fitness is above threshold C (later stages of evolution). ^[inferred]

## State features
Ten search-dependent features (search stage, fitness improvement, the standard deviation/mean/skewness/kurtosis/amplitude of fitness, lower Q1/median Q2/upper Q3 quartiles of fitness) and seven instance-dependent features (number of available vehicles, vehicle capacity, average customer demand, average service time, average time-window size, average time-window overlap between customers, percentage of time-constrained customers), from ref [34] (PPO with identified features, ESWA 216 (2023) 119461), same problem domain. ^[inferred]

## Problem definition
CVRPTW objective `Min f(s) = c × NV + TD` (Eq. 7), penalty weight factor c = 1000 giving the first objective higher priority, vehicles serve every customer within their time windows while satisfying capacity constraints. Solomon benchmark dataset, six groups R1, R2, C1, C2, RC1, RC2 (random / clustered / mixed, narrow vs wide time windows, small vs large capacity). Selected instances: R1, R2, RC1, RC2. **Type-C1 and type-C2 are excluded because the method always achieved the best-known solutions in preliminary experiments.**  ^[inferred]

- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_21_chart_1.jpg]] — Figure 5: Performance comparison during the training process (learning on selection for evolution heuristics, i.e. se)
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_21_chart_3.jpg]] — (b) R102
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_21_chart_5.jpg]] — (c) R103
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_21_chart_7.jpg]] — (d) R104
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_21_chart_9.jpg]] — Figure 5 continued: (e) R201
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_21_chart_12.jpg]] — (f) R202
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_21_chart_14.jpg]] — Figure 5 continued: (g) R203
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_21_chart_16.jpg]] — Figure 5 continued: (h) R204
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_21_chart_20.jpg]] — Figure 5 continued: (i) RC101
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_21_chart_22.jpg]] — Figure 5 continued: (m) RC201
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_21_chart_26.jpg]] — Figure 5 continued: (n) RC202
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_21_chart_29.jpg]] — Figure 5 continued: (o) RC203
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_21_chart_31.jpg]] — Figure 5 continued: (p) RC204
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_27_chart_0.jpg]] — Figure 6: Performance comparison during the training process (learning on selection for replacement heuristics, i.e. sr)
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_27_chart_2.jpg]] — (b) R102
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_27_chart_4.jpg]] — (c) R103
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_27_chart_8.jpg]] — Figure 6 continued: (e) R201
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_27_chart_13.jpg]] — Figure 6 continued: (f) R202
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_27_chart_15.jpg]] — Figure 6 continued: (g) R203
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_27_chart_17.jpg]] — Figure 6 continued: (h) R204
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_27_chart_19.jpg]] — Figure 6 continued: (i) RC101
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_27_chart_21.jpg]] — Figure 6 continued: (m) RC201
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_27_chart_24.jpg]] — Figure 6 continued: (n) RC202
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_27_chart_27.jpg]] — Figure 6 continued: (o) RC203
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_27_chart_30.jpg]] — Figure 6 continued: (p) RC204
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_33_chart_0.jpg]] — Figure 7: Performance comparison during the training process (learning on evolution operators vs. learning on both selection heuristics and evolution operators)
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_33_chart_2.jpg]] — (b) R102
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_33_chart_4.jpg]] — (c) R103
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_33_chart_8.jpg]] — Figure 7 continued: (e) R201
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_33_chart_13.jpg]] — Figure 7 continued: (f) R202
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_33_chart_15.jpg]] — Figure 7 continued: (g) R203
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_33_chart_17.jpg]] — Figure 7 continued: (h) R204
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_33_chart_19.jpg]] — Figure 7 continued: (i) RC101
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_33_chart_21.jpg]] — Figure 7 continued: (m) RC201
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_33_chart_24.jpg]] — Figure 7 continued: (n) RC202
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_33_chart_27.jpg]] — Figure 7 continued: (o) RC203
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_33_chart_30.jpg]] — Figure 7 continued: (p) RC204
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_41_chart_0.jpg]] — Figure 8: The most adapted algorithmic components of the best designed search algorithms obtained by ACE LAS both, Selection for Evolution heuristics
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_41_chart_2.jpg]] — (b) R102 se
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_41_chart_4.jpg]] — (c) R103 se
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_41_chart_6.jpg]] — (d) R104 se
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_42_chart_0.jpg]] — Figure 9: The most adapted algorithmic components of the best designed search algorithms obtained by ACE LAS both, Evolution Operators
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_42_chart_2.jpg]] — (b) R102 op
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_42_chart_4.jpg]] — (c) R103 op
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_42_chart_6.jpg]] — (d) R104 op
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_43_image_0.jpg]] — Figure 10: The most adapted algorithmic components of the best designed search algorithms obtained by ACE LAS both, Selection for Replacement heuristics
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_43_image_2.jpg]] — (b) R102 sr
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_43_image_4.jpg]] — (c) R103 sr
- ![[/home/tatdatnguyen/tatdat-vault/_papers/yi2023automated/images/page_43_image_6.jpg]] — (d) R104 sr

## Experiments
Hardware: Intel Xeon W-2123 CPU @ 3.60 GHz, 32.0 GB memory; Java with IntelliJ IDEA 2020.3.3 — Java chosen because HyFlex and other frameworks in the relevant literature use it.  ^[inferred]

**Learning on Selection for Evolution (se).** Components fixed elsewhere: `o_ins_bw` for Evolution and `h8` for Selection for Replacement — the most frequently called evolution operator and the most adopted selection-for-replacement heuristic in the literature. Figure 5 shows that learning on selection-for-evolution heuristics alone has **no significant impact** during training: with the Evolution module fixed there is limited scope for evolution, supporting human experience in algorithm design, i.e. selection heuristics have less impact on performance, so there is no need to focus on designing them. Tables 4–7: ACE variants are slightly, not significantly, better than the non-learning method in testing. ^[inferred]

| instance | best-known | ACE FS se BEST | GAP | ACE NLAS se BEST | GAP | ACE LAS se BEST | GAP | Non-learning BEST | GAP |
| R101 | 20645.79 | 20918.92 | 1.32% | 20887.4 | 1.17% | 20914.45 | 1.30% | 20901.02 | 1.24% |
| R102 | 18486.12 | 18706 | 1.19% | 18660.31 | 0.94% | 18669.80 | 0.99% | 18675.05 | 1.02% |
| R103 | 14292.68 | 14437.66 | 1.01% | 14459.78 | 1.17% | 15345.42 | 7.37% | 14448.89 | 1.09% |
| R104 | 10007.24 | 11083.57 | 10.76% | 11082.82 | 10.75% | 11098.03 | 10.90% | 11085.36 | 10.77% |
| R201 | 5252.37 | 5398.13 | 2.78% | 5392.77 | 2.67% | 5413.81 | 3.07% | 5481.47 | 4.36% |
| R202 | 4191.7 | 4317.59 | 3% | 4316.40 | 2.97% | 4307.61 | 2.77% | 5287.09 | 26.13% |
| R203 | 3939.54 | 4111.00 | 4.35% | 4087.81 | 3.76% | 4111.65 | 4.37% | 4184.90 | 6.23% |
| R204 | 2825.52 | 3891.49 | 37.73% | 3878.91 | 37.28% | 3891.72 | 37.73% | 3989.41 | 41.19% |
| RC101 | 15696.94 | 16734.77 | 6.61% | 16758.36 | 6.76% | 16766.4 | 6.81% | 16745.33 | 6.68% |
| RC102 | 13554.75 | 14627.56 | 7.91% | 14619.93 | 7.86% | 14557.79 | 7.4% | 14597.72 | 7.69% |
| RC103 | 12261.67 | 12342.64 | 0.66% | 12364.56 | 0.84% | 12347.93 | 0.70% | 12341.12 | 0.65% |
| RC104 | 12135.487 | 11223.87 | 0.79% | 11190.65 | 0.50% | 11197.41 | 0.56% | 11171.26 | 0.32% |
| RC201 | 5406.91 | 5538.27 | 2.43% | 5550.42 | 2.65% | 5580.24 | 3.21% | 5594.09 | 3.46% |
| RC202 | 4367.09 | 5400.92 | 23.71% | 5382.51 | 23.29% | 5332.49 | 22.15% | 5347.23 | 22.48% |
| RC203 | 4049.62 | 4172.10 | 3.02% | 4173.24 | 3.05% | 4159.75 | 2.72% | 4163.38 | 2.81% |
| RC204 | 3798.41 | 3934.86 | 3.59% | 3928.85 | 3.43% | 3924.74 | 3.32% | 3905.85 | 2.83% |

Best-known sources: R101 [36], R102 [37], R103 [38], R104 [39], R201 [40], R202 [41], R203 [42], R204 [43], RC101/102 [44], RC103 [45], RC104 [46], RC201 [39], RC202/203 [47], RC204 [39]. ^[inferred]

**Learning on Selection for Replacement (sr).** Components fixed as `o_ins_bw` and `h1` (most frequently called evolution operator and most adopted selection-for-evolution heuristic). Figure 6: ACE learns on sr throughout training, and Tables 8–11 show the RL methods are **slightly, not significantly** better than non-learning on all instances, indicating sr has little impact on performance, consistent with the training findings. Explanation: the action space is relatively small, presenting limited scope for learning. ^[inferred]

**Learning on both.** Despite a worse starting point, all ACE variants on the both-space outperform those on the operator-only space during training (Figure 7), demonstrating positive synergy between selection heuristics and evolution operators: proper collaboration significantly improves performance. Human expertise that fixes components other than evolution operators leads to a better starting point in a limited design space, but machine learning outperforms within a larger design space. ACE LAS both performs best; ACE FS both and ACE NLAS both are competitive during training. ACE LAS both's advantage over ACE NLAS both is that the simple linear coefficient adjustment is much less time-consuming, leaving more computational time to evolve the population. ^[inferred]

Testing (Tables 12–15): ACE LAS both attains better solution quality than the other two variants on most instances. The only difference between ACE variants is the entropy coefficient adjustment scheme, so the linear scheme is useful in striking the balance between exploration and exploitation, particularly on the large design space. ^[inferred]

Time-windows density: R101/R102 = 100%/75% of customers with time windows, R103/R104 = 50%/25%. With lower density (looser constraints) the starting points of all ACE variants increase, indicating ACE learns better on looser instances, because the solution space contains more feasible candidates that help learning techniques discover knowledge or patterns. ^[inferred]

GAP (BEST) for the six `both` variants, R1 and R2 rows (ACE FS both / ACE NLAS both / ACE LAS both, plus ACE X operator, Non-learning): R101 0.04% / 0.04% / 0.03% / FS 0.04% / Non-learning 1.24%; R102 0.20% / 0.08% / 0.03% / 0.07% / 1.02%; R103 2.24% / 0.40% / 0.39% / 6.65% / 1.09%; R104 10.41% / 10.37% / 10.14% / 10.52% / 10.77%; R201 0.49% / 0.60% / 0.48% / 0.87% / 4.36%; R202 22.77% / 22.38% / 1.52% / 4.06% / 26.13%; R203 1.81% / 1.71% / 1.52% / 1.48% / 6.23%; R204 34.37% / 34.74% / 34.71% / 33.89% / 41.19%; RC101 6.25% / 6.43% / 6.06% / 6.27% / 6.68%; RC102 7.13% / 7.36% / 7.10% / 7.46% / 7.69%; RC103 1.49% / 0.49% / 0.85% / 8.49% / 0.65%; RC104 9.35% / 9.30% / 0.3% / 1.01% / 0.32%; RC201 1.33% / 0.78% / 0.99% / 1.24% / 3.46%; RC202 19.22% / 19.54% / 19.34% / 20.14% / 22.48%; RC203 1.71% / 1.96% / 1.10% / 2.03% / 2.81%; RC204 1.17% / 1.73% / 1.18% / 1.30% / 2.83%. ^[inferred]

**Component analysis (R1, ACE LAS both).** All Selection-for-Evolution heuristics, all Evolution Operators, and all Selection-for-Replacement heuristics are called during the optimisation process, with different appearance counts — distinct algorithmic components can help improve performance. `h8` (plus-selection) is the most frequently called selection-for-replacement heuristic, consistent with manually designed algorithms in the literature. ^[inferred]

**Generality.** The policy trained on R101 is applied to C101, C201, R105, R201, RC101, RC201 (20 runs, Table 16): GAP < 3% on most instances apart from RC101. ACE LAS both attained best AVG, BEST and GAP on most instances. C101 and C201 GAP = 0 (SD of the best-known = 3.64E-12, 4.44E-13). RC101 GAP 6.0%, R105 0.29% (ACE LAS both), R201 0.69%, RC201 0.81%. ^[inferred]

## Conclusions and future work
The study systematically investigates two research issues in automated algorithm design with machine learning: the impact of individual algorithmic components and the synergy of multiple components, within a unified general search framework. Selection heuristics have less impact on performance, supporting human experience in algorithm design and findings reported in the literature. Learning on the synergy of multiple components shows proper collaboration among selection heuristics and evolution operators can significantly improve algorithm performance, and machine learning overtakes human experience when the design space is larger than human experts can explore. Future work: multi-objective search algorithms with the extended multi-objective GSF; more complex VRP variants and real-world problems (multi-depot VRP [48], stochastic VRP [49], time-dependent green VRPTW [50]); transfer reusable knowledge from small-scale VRPs to large-scale VRPs and other COPs. ^[inferred]

## Related pages
- [[concepts/actor-critic-entropy-automated-algorithm-design]] — ACE-GSF: actor-critic, dual critics, entropy objective, α schemes.
- [[concepts/state-features-rl-algorithm-design]] — the ten search-dependent and seven instance-dependent features.
- [[concepts/entropy-coefficient-adjustment-schemes]] — FS / LAS / NLAS: fixed, linear, non-linear α.
- [[concepts/rl-component-analysis-designed-algorithms]] — ACE LAS both component analysis and the R101 policy transfer (Table 16).
- [[concepts/hyper-heuristics]] — automated algorithm design and adaptive operator selection.

## Page index
- page 8: Figure 1 (`page_8_image_4.jpg`); page 11: Figure 2 (`page_11_*`); page 13: Figure 3; page 19: Figure 4; page 21: Figure 5; page 27: Figure 6; page 33: Figure 7; page 41: Figure 8; page 42: Figure 9; page 43: Figure 10.
