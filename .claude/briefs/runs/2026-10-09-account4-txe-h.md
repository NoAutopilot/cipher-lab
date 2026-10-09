# TXE-H: pair hints in the reader's brief (LANE TX-ENGINEER, idea M17; account 4, Opus 5.5; cap 6, box 90 min)

Read `.claude/briefs/runs/2026-10-09-account4-txe-COMMON.md` first, then `benchmark-tx/PREREG-txeng-2.md` (units, blindness,
Amendment: gate p < 0.01), research/TX-TAXONOMY-2026-10-09.md class 1 and research/TX-IDEAS-2026-10-09.md rows M17, M1
(TXE-A's result: showing exemplars beside the sign made the reader swap right reads for look-alikes, fixed 4 / broken 16;
the thin-only pair re-read, TXE-C, selected too few positions). This job tests the cheapest form of the same knowledge: the
reader keeps the ordinary blind line read, but the brief names, for each taxonomy pair, the one feature that decides it.

## Build `tools/tx_pair_hints.py` (--help; test tools/tests/test_tx_pair_hints.py; disk only)
1. `derive --pairs PAIRS --exemplars atlas/sheet_truth/sheet.tsv --atlas DIR --out hints.md --sheet hints_sheet.png`: for
   each listed pair (T18/T98, T90/T53, T76/T66, T76/T86, T76/T45, T64/T95, T64/T51, T50/T36, T92/T95, T92/T98, T83/T24,
   T60/T86), take the secure tiles of each code on non-no.87 pages (never a no.87 tile, never labels.json overrides), compute
   three shape statistics per tile (descender depth below the x-line as a share of height, loop count = holes in the ink
   component, crossbar count = horizontal ink runs wider than 0.6 x width), and write the statistic that separates the two
   codes best (largest standardised mean difference) as ONE plain sentence per pair ("T18 vs T98: T98's tail goes below the
   line by about a third of its height; T18's does not"), plus a hints sheet: one row per pair, 3 secure tiles of each code
   side by side with the two code names. Hints are derived by the script from the tiles, so no truth of no.87 enters them.
   Print the per-pair separation (d') so a pair with d' < 1 is dropped from the hints (say which).
2. The reader's brief for this job = the unchanged `harvest/blind_pass_brief_1572.md` + `sign_sheet_blind_1572.png` + the
   generated hints.md and hints_sheet.png appended as a section "Pairs that are easy to confuse: what decides them". Nothing
   else changes: same crops, same call grouping as pass A.

## Reads and gate (PREREG-txeng-2 rules; the gate as amended, p < 0.01)
Dev: ONE blind Opus 5.5 pass on dev_tune (f178v L01-12 crops, harvest/f178v/f178v_L01..L12_s?.jpg) in two calls (L01-06,
L07-12) with the hinted brief; raw to `benchmark-tx/txeng/hints/passP_raw_dev.tsv`, commit, normalise as build_birago87.py
does for pass A -> `benchmark-tx/outputs/birago1572-no87/passP_hints_dev_tune.tsv`; score paired vs
`benchmark-tx/txeng/units/passA_dev_tune.tsv` (the same reader kind, unhinted; this is the instrument's own baseline) with
gate fixed > broken p < 0.01, and vs labels_dev_tune.tsv (reported). Also report, per pair, how many positions in the pair
changed each way. If the dev gate is met: eval_heldout once (f178v L13-23 + f179r L01-03, two calls), paired vs
passA_eval_heldout.tsv and labels_eval_heldout.tsv -- the single eval look. Not met -> FAIL, no eval. Readers see crops,
sheet and hints only; the worker opens truth only through tx_bench after the split's reads are committed.

## Report
`benchmark-tx/txeng/hints/RESULTS.md`: the derived hints with their d', the tx_bench lines, `tools/tx_taxonomy.py` on passP
vs A and L (after commit), reader task text, calls. Shelf and SYSTEM rows (grade from the result); one Results-log row in
research/TX-IDEAS-2026-10-09.md (id M17; rebase before editing). Offline test: a synthetic pair of tile sets (one with a
descender, one without) yields the descender sentence and d' > 1; a pair with identical sets is dropped. Vision calls: dev 2,
eval 2 at most, x about 1.5; cap 6; stop before a call that crosses 80% of cap or box. Report in a short paragraph (first
line: dev and eval fixed/broken/p vs A) and stop.
