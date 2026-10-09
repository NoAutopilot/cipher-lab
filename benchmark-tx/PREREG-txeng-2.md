# PREREG TX-ENGINEER round 2 (9 Oct 2026, 07:1x UTC by date -u; LANE TX-ENGINEER, account 4, Fable; pushed BEFORE any read or score)

Brief `.claude/briefs/runs/2026-10-09-account4-lane-tx-engineer.md` round 2. Taxonomy that chose the instruments:
`research/TX-TAXONOMY-2026-10-09.md` (Birago 1572 classes: 1 inventory look-alike pairs, 2 crop geometry, 3 thin strokes).
Three instruments, three workers (Opus 5.5; reader subagents Opus 5.5, a Fable arm only where stated). Every instrument
is a tool in `tools/` with `--help` and an offline test, a shelf row and a SYSTEM.md row.

## Units and baselines (fixed; files in `benchmark-tx/txeng/units/`, lines listed in its README.md)

| unit | lines | scored | pass A | L (today's best: C + relabels) |
|---|---|---|---|---|
| dev_tune | f178v L01-12 (the atlas's cluster-naming lines) | 343 | 0.070 (24) | 0.041 (14) |
| eval_heldout | f178v L13-23 + f179r L01-03 (the atlas held-out lines) | 376 | 0.048 (18) | 0.040 (15) |
| geo | f178r L01-03 + f178v L05, L10, L22 (the tail and the band-cut lines) | 169 | 0.136 (23: 15 wrong, 8 deleted) | 0.089 (15) |

Scoring: `python3 tools/tx_bench.py OUT.tsv --bench BENCHMARK-TX.tsv --item birago1572-no87 --paired <baseline unit file>`
(fixed / broken / two-sided exact sign test; insertions stay in err_true). A gain is a gain only when fixed > broken with
p < 0.05 on the paired count, never on overlapping intervals. Tune on dev_tune (or the read-free dev named below), then eval
ONCE on eval_heldout; a second eval run of the same instrument after a change is a dev run and is reported as such.

Blindness: a reader subagent sees sheets or crops only. These files carry truth and are NEVER given to a reader, and the
worker opens them only after the reads for that split are committed: `benchmark-tx/*.truth.tsv`,
`benchmark-tx/taxonomy/*`, `ciphers/nevers-birago-fr3251-1572/atlas/no87_box_token.tsv` (truth column),
`atlas/labels.json` "override" (309 per-tile truth overrides on the tune lines), `harvest/align87/`, any decode.
Atlas candidates for a no.87 box come from a classify run that holds out ALL of no.87
(`--holdout f178r_ --holdout f178v_ --holdout f179r_`), so no tune tile votes for itself; exemplar tiles shown to a reader
come from non-no.87 pages (`atlas/sheet_truth/`, built with `--exclude-leaf` on no.87, or boxes of other pages).

## Instrument A: compare, don't recall (TXE-A, class 1; worker brief 2026-10-09-account4-txe-a.md)
Tool `tools/tx_compare.py` (build / resolve). For each position of a unit, candidates = the line read's sign (L) plus the
atlas top-3 cluster codes (held-out classify). A position is SHOWN to the reader only when top-1 != L's sign, or the atlas
top-1 share < 0.6, or L's merged confidence is M/L (passC_agreement.tsv); the others keep L unread. A shown row = the sign's
tile in context (4x, +-1 neighbour) beside 2 exemplar tiles per candidate, candidates numbered 1..k in a seeded random order
(code names hidden; the row -> code map is written to a file the reader never gets). Question per row: "which numbered
candidate matches, or none". Resolve: pick -> that code; none / ? -> keep L. Sheets of at most 16 rows, one subagent call
each, Opus 5.5 reader (`model: opus`), value-blind.
Prediction registered: the shown set holds most of class 1 (d/s, p/t, n/e, h/l); the 9 unanimous floor positions move only
if the atlas top-3 carries the truth there.
Gate: dev_tune fixed > broken, p < 0.05 vs L_dev_tune. If met: eval_heldout once vs L_eval_heldout. Secondary (reported,
not gating): picks fed as weights into `key_decode_lattice.py decode` (lam 4) and scored the same way. Fable arm: only if
the Opus dev gate is met and the worker is under 60% of its cap -- the same sheets read once by a Fable subagent, eval only,
reported beside Opus. Fails three fixes -> retired (rule 3 third-attempt clause).

## Instrument B: crop geometry (TXE-B, class 2; worker brief 2026-10-09-account4-txe-b.md)
`tools/iiif_lines.py` gains (1) `--band-extent`: band edges grown from the midpoint to the ink-profile minima with a
descender margin (a fraction of pitch, default 0.35), combined with `--mask-neighbours` so grown bands carry no
neighbour-line ink; (2) `--check-boxes signs.tsv`: a read-free report of the share of a page's atlas boxes cut by the bands
and the share of other-line boxes inside each band; (3) `--overlap-note`: the manifest's actual segment overlap in native
px and in signs (page median sign width), written to OUT/crops_note.md for the pass brief, never typed by hand (the 1572
brief says "about 100 px at 2x"; the manifest overlap is 425 native px, class 2c).
Read-free dev gate (f178v, old bands cut 14% of boxes): new bands cut <= 3% of boxes and admit <= 2% other-line boxes.
Then ONE blind Opus 5.5 pass on the re-cut geo unit (f178r with `--follow-slope`/`--deskew` on L03; f178v L05/L10/L22 with
`--band-extent`), the unchanged `harvest/blind_pass_brief_1572.md` + `sign_sheet_blind_1572.png` plus the generated
crops_note.md. Prediction registered: the 8 L03 tail deletions (pos 24-34) are read; band-cut T18/T98/T76 positions move.
Gate: geo unit fixed > broken, p < 0.05 vs passA_geo (the same single-pass reader kind on the old crops); vs L_geo
reported. Band parameters are tuned on the read-free gate only, never on the read.

## Instrument C: thin-stroke targeted re-read (TXE-C, class 3; worker brief 2026-10-09-account4-txe-c.md)
Tool `tools/tx_pair_reread.py` (select / build / resolve). Select, truth-blind: boxes of the unit whose erosion-survival
share is in the page's thin tercile (the `tx_taxonomy.py` measure, computed from the page image and signs.tsv only) AND
whose L sign is in a listed pair: T18/T98, T90/T53, T76/T66, T76/T86, T76/T45, T64/T95, T64/T51, T50/T36, T92/T95, T92/T98,
T83/T24, T60/T86, T13/T64. Each row: the sign at 4x with autocontrast and +-1 context, exemplar row A (3 secure tiles of the
L sign from non-no.87 pages), exemplar row B (3 of the partner), A/B order seeded random per row; question "A, B or
neither". Resolve: A/B -> that code; neither / ? -> keep L. Sheets of at most 16 rows, Opus 5.5 reader, value-blind.
Never a whole re-pass (TX-VIEWS: re-passes repeat A's errors, phi 0.71-0.76).
Gate: dev_tune fixed > broken, p < 0.05 vs L_dev_tune; if met, eval_heldout once vs L_eval_heldout.

## Costs (Fable floor rule: Opus floor 2.5 + about 1-1.5 per Opus vision call)
TXE-A cap 10 / box 120 min (about 6 Opus calls: dev 3, eval 3; Fable arm 3 more only under the 60% rule). TXE-B cap 7 / box
90 (2 Opus calls). TXE-C cap 8 / box 100 (about 4 Opus calls). Round total 25. Each worker stops before a sheet that would
cross 80% of its cap or box.

## What counts
Adopted into round 3 only an instrument whose eval_heldout paired count is fixed > broken, p < 0.05. An instrument whose
dev gate fails is reported as a FAIL with both numbers and is not run on eval. Readers never see truth; the worker scores
only after the split's reads are committed; no `*.truth.tsv` is edited.
