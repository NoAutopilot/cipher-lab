# TXE-J: jitter stability as a per-position prior in the lattice (LANE TX-ENGINEER, idea M11; account 4, Opus 5.5; cap 4, box 60 min; no vision call)

Read `.claude/briefs/runs/2026-10-09-account4-txe-COMMON.md` first, then `benchmark-tx/PREREG-txeng-2.md` (units, blindness,
Amendment), research/TX-IDEAS-2026-10-09.md row M11 and the Results log (TXE-E: a confusion-matrix flip never cleared the
lattice's floor; TX-DECODE: the lattice at lam 1 raises error, lam 4 gains ~2 tokens; TX-ALTS: only 27 of 97 errors have the
truth in the lattice). Why this job exists: the lattice today has no per-position measure of how sure the IMAGE is, only the
readers' stated confidence. A tile whose atlas top-1 flips under a 2-px shift or a 5% rescale is a tile the readers are
likely to split on; that stability can gate how far the lattice is allowed to override the line read.

## Build, as an option on `tools/glyph_atlas.py classify` and `tools/key_decode_lattice.py` (tests extended; disk only)
1. `glyph_atlas.py classify ... --jitter N [--jitter-px 2 --jitter-scale 0.05]`: classify each box N times (default 5) under
   small perturbations of its crop (±px shifts, ±scale, seeded), and add columns `stab` (share of jitters whose top-1 equals
   the unjittered top-1) and `k1_j` (the majority top-1 over jitters). Holding out ALL of no.87 as in TXE-A
   (`--holdout f178r_ --holdout f178v_ --holdout f179r_`).
2. `key_decode_lattice.py from-passes ... --stability STAB.tsv [--stab-floor 0.6]`: a per-position prior: at a position whose
   box stability < floor, the lattice keeps the readers' candidates as they are (the doubtful tile); at a position with
   stability >= floor, the top-1 reader candidate's weight is raised toward 1 (the image is sure; the lattice must not
   override it). Boxes map to positions label-blind (`tools/tx_compare.py map`; never no87_box_token.tsv's truth).
3. Read-free test on dev_tune, as TXE-E ran it (inputs from `benchmark-tx/txeng/conf/run_conf.py dev`: passes A/B of f178v,
   skeleton passC, printed key, it16dip LM, beam 64, lam 4): decode with and without `--stability`;
   `benchmark-tx/outputs/birago1572-no87/passR_stab_dev_tune.tsv`; score `tools/tx_bench.py ... --paired
   benchmark-tx/txeng/units/labels_dev_tune.tsv` (gate fixed > broken, p < 0.01) and `--paired` the plain lam-4 lattice
   (reported). Control (rule 3): the same with a permuted stability vector (seeded) must not pass. Met -> eval_heldout once
   (the eval look); not met -> FAIL, no eval. Also report: does stability predict L's wrong positions on dev_tune
   (precision/recall of stab < floor against tx_bench.position_errors), read-free, since a predictor of doubt feeds the
   sorter's focus even when the lattice gains nothing.

## Report
`benchmark-tx/txeng/stab/RESULTS.md`: stability distribution, the paired lines, the control, the doubt-prediction table,
0 vision calls. Shelf and SYSTEM rows (grade from the result); one Results-log row in research/TX-IDEAS-2026-10-09.md (id
M11; rebase before editing). Offline test: a synthetic tile set where one box flips top-1 under a 2-px shift and another does
not: `stab` 0.4 vs 1.0; the lattice option keeps the flipping box's candidates and sharpens the stable one. Cap 4; stop at
80% of cap or box. Report in a short paragraph (first line: dev fixed/broken/p vs L and the doubt recall) and stop.
