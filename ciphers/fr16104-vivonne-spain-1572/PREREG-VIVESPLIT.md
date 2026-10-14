# PREREG-VIVESPLIT (14 Oct 2026, 01:5x UTC by date -u; account-4 worker VIV-ESPLIT for LANE VIV-KEYSTONE)

Brief: `.claude/briefs/runs/2026-10-13-acct4-keystone-viv-jobs.md`, "Wave 4", "VIV-ESPLIT". Pushed before any held-out score.
What was looked at before writing this: the per-label counts of the truth files' `plain` column at reader-label e / y positions
(counts only, below) and VIV-CLS's map coverage of those positions (how many have a single 1:1 tile). No tile has been
classified, no feature computed, no accuracy seen.

## Question
Do the reader labels e and y each hide several distinct signs that an image classifier, trained on this hand's own
known-answer leaves, can tell apart on a leaf it has not seen? Only a label whose split passes may be split in ink 63.

## Data (three truth leaves of this hand)
- f.102r `benchmark-tx/vivonne1573-f102r-dev2.truth.tsv`, f.103r `...-f103r-confirm2.truth.tsv`, f.201r `...-f201r-dev.truth.tsv`.
- Items: every truth row whose `ref_sign` (the reader label on the truth skeleton) is `e` or `y` and whose `plain` (the clerk
  letter the alignment places there) is non-empty. Class = `plain`. No confidence filter (the truth files carry none at these
  rows); alignment noise in `plain` is part of what the gate measures.
- Counts seen (plain at ref_sign y): f102r 73 (l 33, h 6, t 5, r 4, s 4, e 3, o 3, u 3, other 12), f103r 47 (a 4, h 4, l 4, r 4, ...),
  f201r 37 (r 11, l 9, e 4, n 4, h 3, u 2, a, m, o). At ref_sign e: f102r 2 (f, p), f103r 8 (i 2, e, l, m, n, r, s), f201r 5 (m 4, s).
- **Class rule (per label):** a class is a plain letter with >= 8 pooled items over the three leaves and present on >= 2 leaves;
  items of other letters are dropped. Label y -> classes {l, r, h, e, n} (pooled 46, 19, 13, 9, 8 before tiling).
  Label e -> **no letter reaches 8 (m has 5)**: the supervised gate cannot be run for e; it is logged "untestable on the truth
  leaves at this N" and gets no classifier, no ink-63 split and no key row in this job (see "Label e" below).

## Tiles
- Tile source: tools/glyph_atlas.py segment atlas of the three leaves exactly as VIV-CLS built it (tx/vivcls/seg.py; same
  crops, regenerated: f.201r by the manifest "vivcls" commands, 1 openapi.bnf.fr request; counts 1,655 / 1,835 / 1,139 reproduced).
- Token -> boxes map: tools/box_token_align.py round-2 label-aware maps against each leaf's truth `ref_sign` skeleton:
  f102r / f103r = VIV-CLS's committed `tx/vivcls/train/map_r2_<leaf>.tsv`; f201r = the same recipe built now against the f201r
  truth skeleton with the top-k from a classifier fit on f102r + f103r round-2 labels (glyph_atlas classify, hog / none / k 5,
  as VIV-CLS's round-1 top-k). The map reads reader labels only, never `plain`.
- Tile per item, by tier (each item's tier is reported): **T1** token has exactly one box at op 1:1 -> that box; **T2** token
  covered by >= 1 boxes at op 2:1 / unsure -> union bounding box of its boxes; **T3** a box shared with a neighbour (op 1:2) ->
  that box cut at its x-midpoint, left half to the earlier token. Items with no box (skiptok) are dropped. This replaces the
  brief's token-count x-window (a width-only position estimate, the BOXMAP-RESCORE failure) with the map's own box geometry.
- Bitmap: the box region of the line crop, binarised with glyph_atlas.binarise, 48x48 by glyph_atlas.bitmap.
- Features: HOG (glyph_atlas._hog) -> standardise -> PCA 20 fitted on the training fold only; plus glyph_atlas.zone_topo_feats
  (29) with geo (rh, rw = box h, w over the leaf's median box h; dy 0), standardised on the training fold.
- Model (one setting, no grid): sklearn LinearDiscriminantAnalysis(solver='lsqr', shrinkage='auto').

## Gate, per label (leave-one-leaf-out)
- Three folds: train on two leaves, predict the held-out leaf's items. Pooled held-out accuracy acc over all items.
- Baseline p0: the pooled accuracy of predicting each held-out item as its training fold's majority class.
- **(G1)** one-sided binomial P(X >= k | n, p0) < 0.05, k = correct held-out items.
- **(G2) permuted-label control:** 200 runs (seed 20261014 + i), class labels permuted within each training fold, same
  pipeline; real acc > the permuted p95; and the permuted mean is "near chance": <= max(p0, c_prop) + 0.10, c_prop =
  sum_c p_train(c) p_test(c) pooled over folds. If the permuted mean misses that band, G2 fails (the control is not a control).
- **(G0) positive control (decides whether a FAIL is a test):** the same pipeline on five distinct KEYED reader labels at
  scored truth positions where ref_sign is in the truth set (labels m, o, d, tz, g -- the five most frequent distinct keyed labels present on all three leaves; x is too rare), class = the
  reader label, sampled (seed 20261014) to y's per-leaf per-class counts after tiling (class i of y -> label i of the control by
  rank of pooled size). G0 passes if its LOLO acc clears its own G1. If G0 fails, a y FAIL is logged "non-test at this N with
  these tiles" (rule 3), not a negative.
- **Label y passes step 1 iff G0, G1 and G2 all pass.** Reported in every case: acc, p0, k/n, p, permuted mean/p95, per-class
  confusion, per-fold acc, tier counts.

## Step 2 (only if y passes): ink 63
- Crops: images/p63/manifest.json regions re-fetched from openapi.bnf.fr (<= 3 requests, take/release lines; the pages with the
  most label-y tokens first), cut with the manifest's own params, segmented the same way; token -> box map against the
  committed reconciliation (tx/rec_f19x / the files viv63_decode.py reads), reader labels only.
- Classifier refit on all three truth leaves; per ink-63 label-y token: sub-label, posterior; written to tx/viv63_esplit/.
- Provisional decode: y_<class> -> <class letter> for tokens with posterior >= 0.6, others stay y (key value h, M); gates as
  VIV-KEY's (tx/vivkey gates: b2 order and 200 wrong-key specificity) under seeds 20261014ES-*, plus decode_key.py --try per
  sub-sign. Judge score and longest clean run reported, not gated.
- Step 3 (key edit) only if steps 1 and 2 pass, exactly as the brief; otherwise no edit to key.tsv, the ciphertext files or any
  committed reading.

## Label e
No class on the truth leaves reaches the class rule, so no held-out gate exists for e. Descriptive only (licenses nothing):
VIV-KEYV's three shape groups (A) e-loop + n, (B) hooked c before 6, (C) large looped g-like sign; if ink-63 crops are fetched
for step 2, the ink-63 label-e tile ids are written to tx/viv63_esplit/owner_questions.tsv with their context (next label) for a
later sorter ask; no page is built.

## Stop rule
Stop at cap 10, 80% of the 120-minute box (03:22 UTC), or the brief met. One look per label at the held-out numbers; no
re-tuning of features, model, classes or tiers after the look. Any deviation is an addendum pushed before the number it
affects, and reported as post-hoc.
