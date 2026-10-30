---
title: "AlphaZero: A General RL Algorithm that Masters Chess, Shogi and Go through Self-Play"
category: references
tags: [reinforcement-learning, monte-carlo-tree-search, self-play, game-ai, neural-network, paper]
sources:
  - "[[_papers/silver2018general/silver2018general-extracted.md]]"
  - "[[_papers/silver2018general/silver2018general.md]]"
  - "[[_papers/silver2018general/images/page_3_chart_1.jpg]]"
  - "[[_papers/silver2018general/images/page_7_chart_0.jpg]]"
relationships:
  - target: "[[concepts/inverse-soft-q-imitation-learning]]"
    type: related_to
  - target: "[[concepts/generative-adversarial-imitation-learning]]"
    type: related_to
  - target: "[[concepts/duration-objective-depot-discretization]]"
    type: uses
  - target: "[[concepts/first-in-first-out-property-in-time-dependent-travel]]"
    type: uses
summary: "Silver et al. 2018 (Science): AlphaZero, one RL algorithm trained from random play with only the rules, beats Stockfish 155-6-1000, Elmo 91.2%, AlphaGo Zero 61%; same net and MCTS in all three games."
base_confidence: 0.67
lifecycle: draft
lifecycle_changed: 2026-10-27
tier: supporting
created: 2026-10-27T06:40:00Z
updated: 2026-10-30T14:08:41Z
provenance:
  extracted: 1.00
  inferred: 0.00
  ambiguous: 0.00
---

> [!tldr] One algorithm, three games, no human knowledge
> AlphaZero starts from random play, knows only the rules, and defeats the 2016 TCEC chess champion Stockfish, the 2017 CSA shogi champion Elmo, and AlphaGo Zero — with the same network architecture, hyperparameters and MCTS in all three games.

![[_papers/silver2018general/images/page_3_chart_1.jpg]]
*Figure 1: Training AlphaZero for 700,000 steps. Elo ratings were computed from games between different players where each player was given one second per move. (A) Performance of AlphaZero in chess, compared with the 2016 TCEC world-champion program Stockfish. (B) Performance of AlphaZero in shogi, compared with the 2017 CSA world-champion program Elmo. (C) Performance of AlphaZero in Go, compared with AlphaGo Lee and AlphaGo Zero (20 blocks over 3 days).* Panel A is the chess curve.

## Algorithm

- A single deep neural network `f_θ(s)` maps a board position to move probabilities `p` and a scalar value `v ≈ E[z|s]`. AlphaZero optimizes the **expected outcome** rather than win probability, because chess and shogi can end in draws.
- Loss: `l = (z − v)² − πᵗ log p + c‖θ‖²`, i.e. mean-squared error on the outcome plus cross-entropy on the search policy, with L2 regularization; z is −1 (loss), 0 (draw), +1 (win).
- Search is a general-purpose MCTS: each simulation picks the move with low visit count, high move probability and high value, and returns a distribution π over moves at the root. No alpha-beta, no handcrafted evaluation, no move-ordering heuristics.
- Differences from AlphaGo Zero: no symmetry assumptions (chess and shogi rules are asymmetric, so no data augmentation and no board transformation during MCTS); a **single** network continuously updated, rather than replacing the best player when a new one wins by a 55% margin; hyperparameters reused across games without game-specific tuning (only exploration noise and learning-rate schedule differ).

## Training

700,000 steps in mini-batches of 4,096 positions, starting from random parameters: 5,000 first-generation TPUs for self-play, 16 second-generation TPUs for training. Training time: **9 hours** in chess, **12 hours** in shogi, **13 days** in Go. AlphaZero first outperformed Stockfish after **4 hours (300,000 steps)**, Elmo after **2 hours (110,000 steps)**, and AlphaGo Lee after **30 hours (74,000 steps)**; independent runs reached similar performance.

## Results

- Chess: **155 wins, 6 losses out of 1,000** games against the 2016 TCEC season 9 champion Stockfish; AlphaZero also won convincingly from the 2016 TCEC opening positions, against the latest development Stockfish, and against a Stockfish variant with a strong opening book.
- Shogi: **98.2%** wins playing black, **91.2%** overall against the 2017 CSA champion Elmo; it also won under CSA world-championship time controls and against Aperyqhapaq.
- Go: **61%** of games against the published AlphaGo Zero — a general method recovering a symmetry-exploiting algorithm that generated eight times as much data.
- Search efficiency: AlphaZero evaluates **60,000** positions per second, versus 60 million for Stockfish and 25 million for Elmo; it still beat Stockfish with **1/10** the thinking time, and won **46%** of games against Elmo with **1/100** the time. The authors state this calls into question the belief that alpha-beta search is inherently superior in these domains.
- Common human openings were discovered independently during self-play and played frequently; in shogi AlphaZero plays one of the two most common human openings but rarely the second, deviating on the first move. Several chess games show piece sacrifices for long-term advantage, which the authors read as a more fluid, context-dependent positional evaluation.

![[_papers/silver2018general/images/page_7_chart_0.jpg]]
*Figure 3: Matches starting from the most popular human openings. AlphaZero plays against (A) Stockfish in chess and (B) Elmo in shogi. In the left bar, AlphaZero plays white, starting from the given position; in the right bar AlphaZero plays black. Each bar shows the results from AlphaZero's perspective: win (green), draw (grey), loss (red). The percentage frequency of self-play training games in which this opening was selected by AlphaZero is plotted 8 against the duration of training, in hours.*

## Limitations

- Time controls (3 hours per game plus 15 seconds per move) and hardware differ between opponents: Stockfish and Elmo used 44 CPU cores, AlphaZero and AlphaGo Zero used one machine with four first-generation TPUs plus 44 CPU cores.
- Figure captions and panels are quoted verbatim; image crops are mapped by their position in the extracted markdown, not verified against a PDF (the vault holds none).
- Elo comparisons measure play at one second per move, not full-match time controls.

## Related

- [[concepts/inverse-soft-q-imitation-learning]] — soft-Q policies: a different route from a learned value/policy network to a search policy.
- [[concepts/generative-adversarial-imitation-learning]] — self-imitation from a agent's own high-reward trajectories, the same self-generated-data motive.
- [[concepts/duration-objective-depot-discretization]] — shares   + , + - tags with this page
- [[concepts/first-in-first-out-property-in-time-dependent-travel]] — shares   + , + - tags with this page

## Sources

- [[_papers/silver2018general/silver2018general-extracted.md]] — Silver et al., "A general reinforcement learning algorithm that masters chess, shogi and Go through self-play", *Science*, 2018-12-07, DOI 10.1126/science.aar6404.
