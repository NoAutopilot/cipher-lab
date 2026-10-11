# PREREG TXE3-6 UNIT: box in pen strokes or in signs? (account 3, Fable, session_0168bM3qJgyNJdKy6fE6dMAr; written 11 Oct 2026 05:5x-06:0x UTC by date -u, committed BEFORE any segment, classify or score of this experiment)

One of ten TXE3 transcription experiments (account-3 parent session_0198Cv8ypBfBVfRToKVWx33M, 11 Oct 2026). Work in
benchmark-tx/txeng3/6/. Nothing below is loosened after a result is seen; amendments are appended, dated.

## Question

The owner boxed joined shapes as one symbol ("no lift off of the pen", L74 rule 1). Two blind passes on Vivonne f.102r
(benchmark-tx/txeng2/oracle1/answers/vivonne/joined/) found 9 of 16 such shapes likely hold several signs. Which unit gives
lower downstream err_true when the same classifier and decode run on both: (a) pen units (connected ink, joins kept) or
(b) sign units (the truth-free segmenter's split)?

## Item (fixed from counts, not scores)

- no.87 does not join: on the 12 ORACLE-LOCATION-1 lines f178v_L01-L12 the pen-unit boxes number 340 signs against 354 truth
  positions (343 scored), and the owner's own box check merged 0 and re-cut 4 of 343 tiles (answers/birago/summary.json).
  Vivonne f.102r does join: 516 sign boxes against 610 truth positions on its 12 oracle lines (-15%).
- **Item: vivonne1573-f102r-dev2** (split dev; truth sha256 007a8be9a280ff441f0da22eec66276fd36c808fe9a7ab57990e3ddaccb11714;
  36 truth lines f102r_L01-L36, 1848 positions, 1234 scored; clerk period decipherment under the published Tomokiyo key).
  **No eval report is possible**: the only eval/confirm item in a joining hand is vivonne1573-f103r-confirm2 (frozen, single
  look, never scored here). The hold-out is a within-item line split, declared below; the result is a dev result.
- **Test lines** (reported): the even-numbered lines NOT in the oracle manifest: f102r_L02, L04, L08, L10, L14, L16, L18,
  L20, L24, L28, L30, L32, L34, L36 (14 lines). **Train lines** (labels and parameter choice only): the other 22 truth lines,
  which include all 12 oracle manifest lines (L03, L06, L09, L11, L12, L15, L17, L21, L22, L23, L26, L27).
- Blind rules: nothing is written under benchmark-tx/txeng2/oracle1/; no truth or value goes into any owner page; the
  owner's answers (settled.tsv, merges.tsv, recuts.tsv) are not read into this experiment. BENCHMARK-TX.tsv and every
  truth file are read only.

## Box sets (same crops for all three: ciphers/fr16104-vivonne-spain-1572/images/c105_f102r_L??_s{1,2}.jpg, one crop = one
`glyph_atlas.py segment` page; boxes mapped to line coordinates by the crop's manifest x0; in the s1/s2 overlap a box is
kept from the crop whose side of the overlap midpoint holds its centre (the OL1-BOXES rule); reading order = ascending
centre x; detached marks are attached to the sign below by the tool and are NOT tokens in any condition; no ghost rule)

- (a) **pen units**: `glyph_atlas.py segment` default mode as it stands (8-connected components, x-overlap merge; it never
  splits a component) -- the no.87 atlas recipe, exactly what OL1-BOXES gave the owner.
- (b) **sign units**: default mode plus the new option `--split-wide W` (with `--piece P`): after the merge, a sign box
  wider than W x the page's median sign height mh is split into k = max(2, round(w / (P x mh))) pieces at the column-ink
  minimum within +-0.35 piece of each equal-width cut -- the --cursive step-5 rule made available in default mode (Usage 8:
  a shared-tool option with an offline test in tools/tests/test_glyph_atlas.py). W and P are chosen on the TRAIN lines
  only, from the grid W in {1.2, 1.5, 1.8, 2.2}, P in {0.7, 0.85, 1.0, 1.2}, minimising the sum over train lines of
  |sign boxes - truth positions (all statuses)|; ties go to the larger W, then the P nearest 1.0. Truth COUNTS only, no
  value; test lines never enter the choice.
- (c) **control, random splits**: `--split-random SEED`: the same W, the same boxes selected, the same k per box, but the
  k-1 cuts are drawn uniformly at random over the box's columns (sorted; each at least 0.2 x P x mh from the edges and from
  each other), seeds 1, 2, 3. Proof the control can vary on the statistic (rule 3): a cut moved off the ink minimum puts
  different ink in the two pieces, so their 48x48 bitmaps, kNN features, top-k labels and hence the S/D/I counts differ;
  the share of (c) boxes whose pixel content differs from the (b) box at the same place is reported as the check that
  the manipulation actually moved the statistic's input. It is the same count of boxes as (b) by construction, so a
  difference between (b) and (c) is cut placement, not box count.

## Classifier and decode (identical across (a), (b), (c))

- One labelled exemplar set, frozen before any test box is classified, from the TRAIN lines' (b) boxes:
  round 0: a train line whose (b) sign-box count equals its truth position count is labelled 1:1 in order; label = ref_sign
  when it is in the truth set, else the truth set's first member (scored positions); an excluded position gets ref_sign if
  it is a key code, else the box is dropped. Round 1 runs only if round 0 yields fewer than 400 labelled boxes: the other
  train lines' boxes are kNN-classified from round 0, the top-1 string is aligned to the line's ref_sign string by
  difflib, and 'equal' positions plus equal-length 'replace' blocks are labelled 1:1 from the truth. Unlabelled train boxes
  are dropped from the voting set. The set is written once (labels_train.tsv) and used unchanged in all conditions.
- `glyph_atlas.py classify --page all --knn 5 --topk 3 --pca-scale unit`, exemplars via --train-labels, every test page
  held out from voting (--holdout). Top-1 = `code`. Each condition's classify directory = the frozen train boxes + that
  condition's test boxes (PCA is fitted per directory; noted, not controlled).
- Decode: `tools/key_decode_lattice.py decode` on the top-3 lattice (cand k1..k3, score s1..s3; '_' candidates kept as
  unknown at the tool's unk_cost), key = the folder's key.tsv C and M rows as sign/value, --lang fr16, --lam 4 (the
  on-file no.87 value, TX-DECODE; not tuned here), --shuffles 100, --seed 1. Decode quality = the real key's rank and z
  among the shuffled keys, and err_true of the decoded sequence.

## Endpoint, scoring, gate

- Scoring: `tools/tx_bench.py` against benchmark-tx/txeng3/6/bench_test.tsv, a copy of the dev2 benchmark row whose truth
  file is the test lines' rows of the committed truth, byte-identical (truth_test.tsv; the source sha256 is recorded in
  its header) -- a scoring convenience so that train lines are not counted as deleted, not a truth change. Reported per
  condition: err_true as measured AND --exclude-flagged (never the latter alone), Wilson 95%, the standard SER with S, D, I;
  --paired per line for (b) vs (a) and for each (c) seed vs (b).
- **Primary endpoint**: err_true as measured, top-1 (before decode), on the 14 test lines. Secondary: after the lattice
  decode; the decode's rank/z.
- **Gate (sign units adopted)**: err_true(b) < err_true(a) AND paired fixed > broken with the tool's exact p < 0.05 AND
  err_true(b) below every one of the three (c) seeds. If (b) beats (a) but not the control, splitting helps through box
  count, not sign boundaries ("split anywhere"). If (a) <= (b): pen units stand; a null is a result. The recommendation to
  TX-ENGINEER-2 names which case obtained.

## Stop rule and budget

- Cap USD 15 and 2 h (05:48-07:48 UTC); no unit starts past 80% (06:24 of elapsed = 07:24 UTC). Units: tool option +
  offline test; segment + grid; labels; classify x5; decode x5; scoring + RESULTS. If time runs short the decode units are
  dropped first and the top-1 comparison is reported alone, saying so.
- No subagent and no model read anywhere in this design (kNN only); the account's rate-limit status at start was
  `allowed_warning` (BUDGETS.md scaling rule: no new workers), which this design satisfies.
