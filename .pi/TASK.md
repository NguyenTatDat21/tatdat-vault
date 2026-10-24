# TASK — Full Papers Re-Ingest via `wiki-ingest`

## Objective
Run a **full content ingest** for all papers under `./_papers` using the `wiki-ingest` skill.

> Scope: global
> Mode intent: full semantic re-ingest (not metadata-only backfill)

## Ground Rules (from skill)
1. Follow `wiki-ingest` + `llm-wiki` requirements for frontmatter, provenance, relationships, and Sources.
2. Apply **Paper Extraction Frame** for each paper page:
   - problem + novelty
   - method/pipeline (figure or Mermaid)
   - 1–3 core equations in `$$...$$`
   - setup + headline results table
   - ablations + limitations
3. Use `cache-update` for manifest updates (avoid hand-edit races).
4. Use `memory sync INGEST` for `index.md` / `log.md` / `hot.md` updates.
5. Run `qmd update` (and `qmd embed` when needed) after each wave.

## Baseline Snapshot
- `./_papers/*-extracted.md`: **117**
- Sidecar `.md` present: **117 / 117**
- Existing `references/*.md`: **17**
- `OBSIDIAN_MAX_PAGES_PER_INGEST=15`
- `WIKI_STAGED_WRITES=false`
- `QMD_WIKI_COLLECTION=tatdat-vault`
- `QMD_PAPERS_COLLECTION=_papers`

## Execution Model
Use **5-paper waves** (safe with `max_pages_per_ingest=15`).

- Total waves: **24**
- Waves 1–23: 5 papers each
- Wave 24: 2 papers

### Per-Wave Checklist
- [ ] Select wave files (`*-extracted.md` + sidecars)
- [ ] Read sources and distill content (Paper Extraction Frame)
- [ ] Update/create `references/` and required `concepts/` pages
- [ ] Ensure required frontmatter + provenance markers + `## Sources`
- [ ] `obsidian-wiki cache-update` for extracted/sidecar/(used images)
- [ ] `obsidian-wiki memory sync INGEST ...`
- [ ] `qmd update`
- [ ] `qmd embed` if vectors are pending
- [ ] `qmd get` verification on at least one updated page
- [ ] Wave `cache-check` shows unchanged for processed sources

## Wave Tracker
- [x] **W01** `_papers/ahmadi-javid2022delivery/...` → `_papers/archetti2018set/...`
  - ✅ Completed 2026-10-22T19:26Z — pages_created=6, pages_updated=3; cache-check unchanged (10/10); qmd update+embed+verify complete.
  - ⚠️ Note: `_papers/almgren2004optimal/almgren2004optimal-extracted.md` contains NUL bytes; extraction was read via a temporary cleaned copy for drafting, while manifest/cache used the original source file.
- [x] **W02** `_papers/archetti2023new/...` → `_papers/bar-noy2004efficient/...`
  - ✅ Completed 2026-10-22T19:36Z — pages_created=8, pages_updated=1; cache-check unchanged (10/10); qmd update+embed+verify complete.
- [x] **W03** `_papers/barnhart1998branchandprice/...` → `_papers/black1992global/...`
  - ✅ Completed 2026-10-22T19:58Z — pages_created=7, pages_updated=0; cache-check unchanged (10/10); qmd update+embed+verify complete.
- [x] **W04** `_papers/boland2017continuoustime/...` → `_papers/chen2010shrinkage/...`
  - ✅ Completed 2026-10-22T20:41Z — pages_created=9, pages_updated=0; cache-check unchanged (10/10); qmd update+embed+verify complete.
- [x] **W05** `_papers/cheng2020drone/...` → `_papers/christiansen2020liner/...`
  - ✅ Completed 2026-10-22T23:22Z — pages_created=6, pages_updated=2; cache-check unchanged (10/10); qmd update+embed+verify complete.
- [x] **W06** `_papers/clautiaux2018combining/...` → `_papers/dorling2017vehicle/...`
  - ✅ Completed 2026-10-22T23:54Z — pages_created=7, pages_updated=2; cache-check unchanged (10/10); qmd update+embed+verify complete.
- [x] **W07** `_papers/dossantos2024multiobjective/...` → `_papers/furini2016modeling/...`
  - ✅ Completed 2026-10-24T01:31Z — pages_created=12, pages_updated=7; cache-check unchanged (10/10); qmd update+embed+verify complete.
  - ⚠️ Note: `fama1973risk` extracted markdown has no image links, so its page is text-only; equation/table image files exist on disk but their page-to-content mapping is unverified, and no image was embedded.
  - ⚠️ Deferred to a follow-up wave: adding back-links from `references/poikonen2020-k-mvdrp`, `references/lu2024-hybrid-evolutionary-algorithm-sop`, and `references/murray2020-multiple-flying-sidekicks-tsp` into the new UAV routing concept pages.
- [x] **W08** `_papers/ganjia2026multiobjective/...` → `_papers/goel2015constraint/...`
  - ✅ Completed 2026-10-24T04:05Z — pages_created=10, pages_updated=5; cache-check unchanged (10/10); qmd update (10 new/6 updated) + embed (176 chunks/16 docs) + `qmd get` verify complete; 88 wikilinks resolve, frontmatter/YAML fields present, summaries ≤200 chars, all YAML sources exist on disk, all 10 new pages in `index.md`.
  - New: `references/goel2012-large-neighborhood-search-lng-inventory-routing`, `references/goel2015-constraint-programming-lng-ship-scheduling`, `references/ganjia2026-multiobjective-sustainable-supply-chain-scheduling`, `references/garg2022-iq-learn-inverse-soft-q`; `concepts/time-space-network-ship-flow-model`, `concepts/large-neighborhood-ship-pair-destroy-repair`, `concepts/cumulative-volume-lower-bound-cp-search`, `concepts/disjunctive-scheduling-constraint-programming-model`, `concepts/inverse-soft-q-imitation-learning`, `concepts/multi-objective-metaheuristic-tuning-validation`.
  - Updated: `references/gendreau2019-handbook-metaheuristics`, `concepts/large-neighborhood-search`, `concepts/variable-neighborhood-search`, `concepts/mirp-modeling-continuous-vs-discrete-time` (base_confidence 0.67→0.87), `concepts/maritime-inventory-routing-problem` (duplicate typeless relationship entry removed).
  - ⚠️ Caveat: `gendreau2019handbook-extracted.md` is 1.8 MB and was read in chapter windows (LNS, VNS, TS), so non-routing chapters of the handbook are not distilled.
  - ⚠️ Deferred (15-page cap): `concepts/annual-lng-delivery-program`, `concepts/tabu-search`, `concepts/hyper-heuristics`, `concepts/parallel-metaheuristics-cooperative-search`, `concepts/adaptive-large-neighborhood-search-for-mip`, `concepts/green-vehicle-routing-problem-taxonomy`, `concepts/nonlinear-drone-energy-function-in-routing`, `concepts/payload-induced-drone-battery-consumption-rate`, `concepts/multi-objective-maritime-cargo-routing-scheduling`.
  - ⚠️ Note: subagent frontmatter timestamps (e.g. `created: 2026-10-24T12:10:00Z`) run ahead of the `memory sync` log times (03:00Z); index/hot/log are generated by the CLI, so the drift is cosmetic.
- [ ] **W09** `_papers/gronhaug2009supply/...` → `_papers/ha2020new/...`
- [ ] **W10** `_papers/hadjsalem2023mathematical/...` → `_papers/he2002intuition/...`
- [ ] **W11** `_papers/hendel2022adaptive/...` → `_papers/jimenez-piqueras2023constraint/...`
- [ ] **W12** `_papers/kakinuma2020empirical/...` → `_papers/ledoit2004wellconditioned/...`
- [ ] **W13** `_papers/li2024drone/...` → `_papers/mbiadousaleu2022parallel/...`
- [ ] **W14** `_papers/meng2023multivisit/...` → `_papers/montemanni2024combining/...`
- [ ] **W15** `_papers/montemanni2024parallel/...` → `_papers/mutlu2016comprehensive/...`
- [ ] **W16** `_papers/nguyen2022mincost/...` → `_papers/novy-marx2013other/...`
- [ ] **W17** `_papers/ogryczak2014fair/...` → `_papers/pesant2015principles/...`
- [ ] **W18** `_papers/pham2023efficient/...` → `_papers/poikonen2020multivisit/...`
- [ ] **W19** `_papers/qian2001conditional/...` → `_papers/ropke2006adaptive/...`
- [ ] **W20** `_papers/sacramento2019adaptive/...` → `_papers/skalnes2024new/...`
- [ ] **W21** `_papers/sloan1996stock/...` → `_papers/torabbeigi2020drone/...`
- [ ] **W22** `_papers/vilim2015failuredirected/...` → `_papers/windrasmara2022adaptive/...`
- [ ] **W23** `_papers/xinyingchen2023guide/...` → `_papers/yusuf2023strategic/...`
- [ ] **W24** `_papers/zhang2021energy/...` + `_papers/zhao2025large/...`

## Definition of Done
- [ ] All 117 extracted papers fully ingested (content-level)
- [ ] Sidecar metadata integrated for all 117
- [ ] References expanded/updated with valid provenance and sources
- [ ] Manifest/cache stable (`cache-check` unchanged on processed sources)
- [ ] QMD refreshed and verified

## Next Action
Start **W09** (`_papers/gronhaug2009supply/...` → `_papers/ha2020new/...`) and log deltas (created/updated pages, QMD status, blockers) in this file. Carry over: the UAV back-links listed under W07, the concept pages deferred by W08, and the un-distilled non-routing chapters of the Gendreau & Potvin handbook.
