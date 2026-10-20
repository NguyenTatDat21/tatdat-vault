---
zotflow-locked: true
zotero-key: U7V4TDDQ
library-id: 11058526
item-version: 4678
item-tree: bf22ac47
library-version: 4818
citationKey: hendel2022adaptive
title: Adaptive large neighborhood search for mixed integer programming
itemType: journalArticle
creators:
  - Gregor Hendel
publication: Mathematical Programming Computation
date: 2022-06-01
year: 2022
url: https://doi.org/10.1007/s12532-021-00209-7
doi: 10.1007/s12532-021-00209-7
tags:
  - "#90C10"
  - "#90C11"
  - "#90C90"
  - "#Large_neighborhood_search"
  - "#Mixed_integer_programming"
  - "#Multi_armed_bandit_problem"
  - "#Primal_heuristics"
---
# Adaptive large neighborhood search for mixed integer programming
## Abstract
> Large Neighborhood Search (LNS) heuristics are among the most powerful but also most expensive heuristics for mixed integer programs (MIP). Ideally, a solver adaptively concentrates its limited computational budget by learning which LNS heuristics work best for the MIP problem at hand. To this end, this work introduces Adaptive Large Neighborhood Search (ALNS) for MIP, a primal heuristic that acts as a framework for eight popular LNS heuristics such as Local Branching and Relaxation Induced Neighborhood Search (RINS). We distinguish the available LNS heuristics by their individual search spaces, which we call auxiliary problems. The decision which auxiliary problem should be executed is guided by selection strategies for the multi armed bandit problem, a related optimization problem during which suitable actions have to be chosen to maximize a reward function. In this paper, we propose an LNS-specific reward function to learn to distinguish between the available auxiliary problems based on successful calls and failures. A second, algorithmic enhancement is a generic variable fixing prioritization, which ALNS employs to adjust the subproblem complexity as needed. This is particularly useful for some LNS problems which do not fix variables by themselves. The proposed primal heuristic has been implemented within the MIP solver SCIP. An extensive computational study is conducted to compare different LNS strategies within our ALNS framework on a large set of publicly available MIP instances from the MIPLIB and Coral benchmark sets. The results of this simulation are used to calibrate the parameters of the bandit selection strategies. A second computational experiment shows the computational benefits of the proposed ALNS framework within the MIP solver SCIP.

## Attachments
- [Hendel 2022 - Adaptive large neighborhood search for mixed integer programming.pdf](obsidian://zotflow?type=open-attachment&libraryID=11058526&key=SRPZDB2J)

## Notes
