# DEB-SWARM-G log (Portuguese / Spanish / Latin, homophonic letter substitution)

Worker DEB-SWARM-G, 29 Sept 2026. Tools: `gg.py` (front end) + `hsa.c` (annealer core, `gcc -O3 -o /tmp/claude-0/hsa hsa.c -lm`).
Language models (`gg.py model LANG`, conditional interpolated quadgrams, a-z): pt = Camilo *O sangue* 1868 + Eca *Prosas
barbaras* (1866-67) + Garrett *Folhas cahidas* 1853 verse; ptv = Camilo x2 + Eca (Garrett held out); es = Galdos *Dona
Perfecta* 1876 (Tristana held out); la = Zaluski t.1-2 (tools/data/la18; t.3 held out). Sources `corpus/MANIFEST.tsv`.
None contains Camoes (the PT-HOMO plaintext), so the control cannot be won by memorising it.
Times: `date -u` read at each LOG write; rows are bounded by that reading, not estimated (rule 6).
Controls: hand-planted ones are made by `gg.py control` from each model's held-out file (plaintext never written);
harness controls are scored only by `../score.py --control` (sealed answers never opened).

| time (UTC) | method | parameters | control result | real held-out pct | why it failed / note |
|---|---|---|---|---|---|
| before 03:23 | hsa, ptv, X and punct dropped | hand-planted PT (Garrett verse held out), N 547 K 121 (c2 shape), 16x1M, 4 seeds | 30.7 mean clean (16-53); 33.3 Zipf variants; 20.4 at 10 pct noise | -- | multiplicity K/N 0.22 too high at c2 size |
| before 03:23 | same | hand-planted N 107 K 54 (c1 shape) | 9.1 clean; 16.4 at 10 pct noise | -- | c1 alone is pure overfit, as README's reachability note says |
| before 03:23 | hsa, ptv, pooled fit on harness control | PT-HOMO (N 790, K 136, X kept as a sign), 16 restarts x 1.5M, seeds 1-3 | **84.3 / 81.1 / 83.4 recovery (bar 70: met)** | -- | Phase 1 met clean |
| before 03:23 | same | PT-HOMO-N15, seeds 1-3 | 12.8 / 39.2 / 21.3 | -- | 15 pct noise breaks the anneal; needs a noise-tolerant score |
| before 03:26 | hsa, clipped loss (log P floored at -5/-6/-7, `gg.py model ptv --floor`) | PT-HOMO-N15, 16x1.5M, seeds 1-3 | f5 46.6/47.6/32.2; f6 48.4/47.0/15.3; f7 31.9/29.6/48.6 | -- | floor -5 kept; restart variance dominates |
| 03:26 | f5, 64 restarts x 2M | PT-HOMO-N15 seeds 1-3; PT-HOMO seed 1 | N15 29.5/55.2/30.3; clean **90.3** | -- | best score -> best recovery, so search depth is the limit |
| 03:31 | f5 + iterated restarts (`HSA_PERTURB` 0.1/0.2/0.3, `HSA_T0` 0.3), 128x1.5M; plain 256x2M | PT-HOMO-N15 | ILS 48.6/**63.0**/57.5; plain 256 48.4 | -- | ILS p 0.2 kept as the method |
| 03:33 | f5 + ILS 0.2, held-out on the control (fit one part, test the other, score.py --control --fit --test) | PT-HOMO and PT-HOMO-N15 | clean c2->c1 78.0 rec, pt_quad 100/100 beats_all both nulls; clean c1->c2 11.3 rec, pt_quad 99.6/93.7 (fails); **N15 c1->c2 34.2 rec, pt_quad beats_all both nulls; N15 c2->c1 54.6 rec, pt_quad beats_all both nulls** | -- | the bar is reachable on the control at real noise in both directions (one seed; c1->c2 success is seed luck, cf. clean 11.3) |
| 03:42 | Phase 2 fits, `phase2_fit.sh` (seed 11, ILS 0.2, 128x1.5M), ptall/esall/laall floor -5, X as sign (xs) or X null (xn) | 12 keys, fitted on c1 only or c2 only | (Phase 1 above) | scored after commit, next row | keys committed before scoring |
| 03:45 | Phase 2 held-out scoring, `phase2_score.sh` (after commit c08268a2) | 12 keys (seed 11) | control at the same noise: N15 c2->c1 pt_quad beats_all both nulls (54.6 rec); N15 c1->c2 beats_all both (34.2) | **no key passes.** Best in own language: pt xs c2->c1 pt_quad 99.7 / strat 91.4, c1->c2 87.2/59.4; pt xn c2->c1 93.3/36.0, c1->c2 80.9/79.8; es xn c2->c1 es_quad 99.8/82.7, xs 69.6/11.3; la xn c2->c1 la_quad 99.8/83.9, xs 74.5/32.2; every c1->c2 row below 99.7 plain | stratified null is where every real key falls short; the plain-null 99.x values are the frequency-match artefact README documents (a frequency-only key reaches 99.9 on NULL). Numbers per key in keys/KEY_fit_*.heldout.json |
