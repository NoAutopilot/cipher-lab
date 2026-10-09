# TXE-P: ink-density profiles to split glued digit groups, Dinteville f.128 (LANE TX-ENGINEER, idea M8; account 4, Opus 5.5; cap 4, box 60 min; no vision call)

Read `.claude/briefs/runs/2026-10-09-account4-txe-COMMON.md` first, then `benchmark-tx/PREREG-txeng-2.md` (blindness,
Amendment) and research/TX-IDEAS-2026-10-09.md row M8 and research/TX-TAXONOMY-2026-10-09.md section 3 (Dinteville: the
Fable pass inserted 9 signs and pass A deleted 2 -- segmentation of glued digit groups is that hand's third class; on the
Birago hand glued pairs are not a class, 1 error in 22). Why this job exists: the register promised every idea a test; this
one is cheap and read-free, and it is the only instrument aimed at the dev item whose readers disagree on the COUNT of
signs, not their identity.

## Build `tools/tx_split_groups.py` (--help; test tools/tests/test_tx_split_groups.py; disk only)
Input: the dint-f128-print line crops (`ciphers/fr3621-dinteville-1592/images/f128_L02..L05_s1,s2.jpg`, BENCHMARK-TX.tsv
row dint-f128-print; its README names the segment layout) and the two blind passes `benchmark-tx/outputs/dint-f128-print/
passA.tsv`, `passB.tsv` (and passF_fable.tsv). Per line: the column ink-density profile over the core rows (the
`iiif_lines.py --groups` logic -- import or call it, do not copy), valleys at runs of blank columns; count the ink pieces per
line under a sweep of the gap parameter (2..12 px) and report, read-free, the gap at which the piece count equals pass A's
sign count, pass B's, and F's, per line. Then, for each pass, list the positions where the pass's sign count between two
agreed anchors differs from the piece count (a candidate glued pair or over-split): `benchmark-tx/txeng/split/flags.tsv`.
Commit it BEFORE any truth is opened.

## Measure (opens truth after the commit; label-mapped as the benchmark prescribes)
With `tools/tx_bench.py ... --item dint-f128-print --label-map benchmark-tx/dint128_label_map.tsv --json`, the per-pass
deleted and inserted counts, and whether the flagged positions coincide with the deletions/insertions tx_bench reports
(recall of the flags against the pass's deleted+inserted positions; flag share). Registered gate for the instrument to be
worth a reader's time: recall >= 0.6 of pass F's 9 insertions + pass A's 2 deletions at <= 15% of positions flagged, on
this one dev item (no eval item has this hand: say so). Met or not, no read in this job; a PASS makes the flag a column
in the reconciliation queue (reconcile_passes.py disagreements.tsv) for digit hands, which the lane briefs separately.

## Report
`benchmark-tx/txeng/split/RESULTS.md`: the gap sweep per line, the flag table, the recall at flag share, 0 vision calls.
Shelf and SYSTEM rows (grade from the result); Results-log row in research/TX-IDEAS-2026-10-09.md (id M8; rebase before
editing). Offline test: a synthetic line of five digit groups, two of them glued (one 2-px gap): the sweep finds 4 pieces at
gap 3 and 5 at gap 1, and the flag names the glued pair. Cap 4; stop at 80% of cap or box. Report in a short paragraph
(first line: recall at flag share) and stop.
