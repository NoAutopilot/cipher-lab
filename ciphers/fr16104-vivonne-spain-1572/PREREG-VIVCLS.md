# PREREG VIV-CLS: a supervised sign classifier trained on two truth leaves of the Saint-Gouard clerk hand, one look at the third

Worker VIV-CLS (Opus, account 4) for LANE VIV-KEYSTONE (account 4, parent session_01D7XWmthshMVqxumdDvitPh); written 14 Oct 2026
00:4x UTC by date -u, pushed in its own commit BEFORE any tile of f.201r is classified or scored. Brief:
`.claude/briefs/runs/2026-10-13-acct4-keystone-viv-jobs.md` "Wave 2", "VIV-CLS". Nothing below is loosened after a result is seen;
any amendment is appended, dated, and says whether it was written before or after the f.201r look. Measurement only: key.tsv,
reading_piece63.tsv, status.json and every committed reading untouched.

## Items (all split=dev, BENCHMARK-TX.tsv)
- TRAIN: vivonne1573-f102r-dev2 (f.102r, ink 40) and vivonne1573-f103r-confirm2 (f.103r, ink 40). Truth opened for labels and CV only.
- TEST (one look): vivonne1573-f201r-dev (f.201r, ink 67, a different letter ten days after ink 63). Its truth file is opened only
  by the scoring step (step 5), once, after every choice below is frozen and the f.201r output files are written and hashed.
  Note: confirm2 is used here as TRAINING data. Its role as a frozen confirm item for reader pipelines is unchanged by that
  (no reader is tuned here), but any later job that trains on it must say so beside a confirm2 score.

## Images (no image file goes into git)
f.102r: images/c105_f102r_L*_s{1,2}.jpg; f.103r: images/c106_f103r_L*_s{1,2}.jpg (on disk, manifest.json "iiif_lines").
f.201r: re-cut 14 Oct 2026 00:4x UTC with VIV-67's exact commands (one native region fetch via openapi.bnf.fr, c206
4100,350,3650,5350; then `tools/iiif_lines.py --image <src> --region 680,1500,2970,3700 --out images/p67/cut --prefix c206_f201r
--follow-slope 400 --distance 70 --max-width 1560 --overlap 150 --debug`): 25 bands x 2 crops, overlay checked by eye
(L01 = fourth plain line, L02-L25 cipher), untracked.

## Step 1. Tiles (pen units, default segmenter)
`tools/glyph_atlas.py segment`, default mode (pen units; TXE3-6 found the --split-wide sign units no better than random cuts on
f.102r), one page per line crop, all three leaves in ONE atlas directory, `--median-h pool`. Boxes are mapped to line
coordinates by the crop's manifest x0 and the s1/s2 overlap deduped at its midpoint (TXE3-6 seg.py rule, OL1-BOXES). Marks are
not tokens. Written to tx/vivcls/atlas/ (signs.tsv, bitmaps.npz, boxes.tsv per leaf). No truth read.

## Step 2. The map (tools/box_token_align.py; truth-blind)
- Round 1: width-only DP (`--lam 0`), boxes -> tokens of a line read.
- Round 2: label-aware (`--lam 1.5 --neutral 0.5`, leave-one-out guard on, the tool's defaults) with `--topk` from the round-1-fitted
  classifier: on f.102r the classifier fitted on f.103r's round-1 labels and vice versa (cross-leaf, so no tile steers its own
  place with its own label); on f.201r the classifier fitted on both training leaves' round-1 labels.
- Line read: on f.102r and f.103r the truth file's own ref_sign skeleton (line, pos, ref_sign: the reconciliation's token
  sequence, which is where the truth positions live); on f.201r passA (benchmark-tx/outputs/vivonne1573-f201r-dev/passA.tsv),
  the baseline the gate compares against. (Coverage against f.201r's ref_sign skeleton is reported too, at step 5 only.)
- A position is COVERED when exactly one box maps to it with op `1:1` in the round-2 map (unsure, 2:1, 1:2, skiptok: not covered).
- Coverage per leaf = covered scored truth positions / scored truth positions; segmentation failures (no 1:1 tile) are reported
  separately from classification errors.

## Step 3. Labels (training leaves only)
For a covered SCORED truth position: label = ref_sign if ref_sign is in the truth set (the reconciliation's visual label, value
confirmed by the clerk); else the truth set's only member if it has one; else dropped (a multi-sign set with the reconciliation
outside it does not say which glyph is on the page). Excluded positions are never labels. Deviation from the brief's literal
"labels = ref_sign", declared here: a ref_sign outside the truth set is a known reader error and would teach the classifier the
readers' confusion. Labels for round 2 come from the round-2 map (the round-1 labels only feed the round-2 top-k).

## Step 4. Fit and CV (on f.102r and f.103r ONLY)
Model: `tools/glyph_atlas.py classify --only-train-labels --train-labels <labels> --topk 3` (kNN over labelled tiles only; HOG ->
PCA 40 -> unit + size; PCA fitted unsupervised on all atlas tiles, f.201r's included -- no label of f.201r is used). Grid, 8 settings:
`--features` {hog, hog+zone+topo} x `--metric` {none, lda} x `--knn` {5, 15}. CV: two folds by leaf (fit on f.102r labels, score
f.103r labelled tiles; and the reverse). Criterion: mean top-1 error over the two folds (ties: the simpler setting, in the order
hog < hog+zone+topo, none < lda, knn 5 < 15). The chosen setting is written into this file's Addendum A before step 5 runs.
If a supervised option is missing from glyph_atlas.py, it is added there with an offline test in tools/tests/ (Usage 8).

## Step 5. One look at f.201r
Fit the chosen setting on BOTH training leaves' labels; classify every f.201r tile; build the round-2 map against passA with that
top-k. Output in pass format: tx/vivcls/f201r_cls_hybrid.tsv = passA with the classifier's top-1 substituted at every covered passA
token (every other token as passA read it), and tx/vivcls/f201r_cls_top3.tsv (line, pos, k1, k2, k3 per covered token). Hash them
(sha256 in RESULTS) before the truth is opened. Then:
- `python3 tools/tx_bench.py tx/vivcls/f201r_cls_hybrid.tsv --bench BENCHMARK-TX.tsv --item vivonne1573-f201r-dev --paired
  benchmark-tx/outputs/vivonne1573-f201r-dev/passA.tsv --exclude-flagged` (as measured and flagged-excluded, both printed).
- Per covered scored position (passA's own tx_bench alignment to the truth): classifier top-1 right/wrong, passA right/wrong,
  and among passA's WRONG covered positions the share whose truth set meets {k1, k2, k3}.

## Gate (both clauses reported whether they pass or fail)
(a) On covered scored positions: classifier top-1 err (as measured) BELOW passA's err on the same positions, AND tx_bench's paired
    per-line headline (hybrid vs passA, as measured) lines improved > worsened with the exact sign test p < 0.05.
(b) truth-in-top-3 >= 0.50 of passA's wrong covered scored positions (the lattice ceiling the readers failed: 0.124 on f.103r).
Control (rule 3; it CAN differ from the real fit, since only the labels move): the same chosen setting fitted once on the training
labels permuted across tiles (numpy seed 20261014), the whole of step 5 rerun with it (its own round-2 map). It must score near
chance: chance = 1 - sum_c p_train(c) p_test(c) over covered f.201r positions' truth-consistent labels is reported; "near" =
permuted top-1 err >= chance - 0.05. If the control is NOT near chance, the real numbers license nothing (stated as such).
A gate pass is a dev result on one leaf: it licenses a later lattice job (VIV-LAT's runner fed the top-3) with its own PREREG,
never a reading change. A fail is logged with the numbers; if coverage is under 0.5 on f.201r, the fail is stated as bounded by
segmentation (pen units on a joining hand), not as a classifier negative.

## Stop rule
Stop at cap 12, at 80% of the 150-minute box (02:36 UTC), or when step 5 and the control are reported, whichever first.
f.201r's truth is looked at once; nothing is re-fitted after it.

## Addendum A (14 Oct 2026 00:5x UTC by date -u; written BEFORE step 5 -- no f.201r tile classified for the gate, f.201r truth unopened)
- Round-1 classifier (feeds only the round-2 top-k): glyph_atlas defaults `--features hog --metric none --knn 5`, as the PREREG
  left it unnamed; cross-leaf for the training leaves.
- Tiles (tx/vivcls/seg.py): 1,655 / 1,835 / 1,139 pen-unit tiles on f.102r / f.103r / f.201r.
- Training-leaf maps (tx/vivcls/train_report.json): round 1 covered scored 877 / 1,234 (f.102r), 661 / 1,068 (f.103r); round 2
  622 / 1,234 = **0.504** and 496 / 1,068 = **0.464**; round-2 labels 538 (24 codes) and 423 (23 codes).
- CV grid (fit one leaf, score the other; err1 = top-1 error on the other leaf's labelled tiles, mean of the two folds):
  hog/none/5 0.369, hog/none/15 0.391, hog/lda/5 0.361, hog/lda/15 0.381, hzt/none/5 0.359, hzt/none/15 0.388,
  **hog+zone+topo/lda/5 0.354 (chosen)**, hzt/lda/15 0.365; top-3 miss of the chosen setting 0.267; majority-class error 0.839 / 0.842.
- Frozen for step 5 and the control: `--features hog+zone+topo --metric lda --knn 5`, fitted on labels_r2_both.tsv (961 tiles).
- Tooling note: the pass-format output (hybrid, top-3) is written by tx/vivcls/run.py for this look; no glyph_atlas.py option was
  needed for the fit (`classify --only-train-labels --features --metric --topk` already does it).
