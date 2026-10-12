# PREREG-BOXCLIP (account 3, written 12 Oct 2026, 01:0x UTC by `date -u`; committed before any score was computed)

Owner's question (12 Oct 2026): machine boxes on the sorter pages often hold only part of a sign (a g's tail, a t's top)
while connected ink leads to the rest, and he fixes them one by one with "Fix the cut". Would a script that flags such
boxes (and proposes the grown box) help? His wording: run it "if we think it'll help, but don't do it if it's just
theatre". So this is a test that can fail, against two controls, and a FAIL is reported as a FAIL.

Script only: no model reading of images, no vision call, no network. Nobody (human or model) looked at an image of any
box while this was written.

## What was looked at before this was frozen

Only: the label files and counts (below); that every `old` box in the owner's recut records equals the machine box in the
page's `signs.tsv` (it does, 21 of 21 Modena, 22 of 22 Matignon); that every box lies inside its page image; the page image
sizes; and, for all 31 + 333 machine boxes with NO labels attached and NO flags computed, the share of ink pixels in the
registered crop after the registered binarisation (a check that Otsu was not degenerate): Modena 0.106-0.226 (median 0.162),
Matignon 0.035-0.341 (median 0.100), no empty crop. No parameter was changed as a result. The method was developed and
tested on a synthetic page only (`tools/tests/test_box_clip_check.py`, six cases with known answers).

## Data

- **Modena** (decode-1162, DECODE R1162 p.1 and R1168 f.12r): the 31 boxes of `ciphers/decode-1162-modena-ambung-1492/sorter/signs.tsv`
  (native 2592 x 3888 coordinates). Images: the half-size grey JPEGs (1296 x 1944, quality 70) embedded in
  `sorter/modena-gq-sorter.html` (`pages` object), so `--scale 0.5`. Only the g/q descender signs have boxes on this page.
- **Matignon f.110** (BnF fr.15572): the 333 boxes of `ciphers/matignon-mayenne-1586/sorter/signs.tsv`, in the coordinates of the
  five strip pages `sorter/pages/f110_W1..W5.jpg` (3330 x 93 px, native), `--scale 1`.

## Labels (the owner's behaviour; exact counts)

- **Positive** = a box the owner re-cut with "Fix the cut": Modena 21 (`sorter/recuts.tsv`, 21 rows, 21 distinct tiles); Matignon 22
  (`owner_db_2026-10-12_partial/recuts/*.json`). **43 positives.**
- **Negative** = a box the owner demonstrably looked at in the card and did not re-cut: Modena **10** (the 31 tiles minus the 21 re-cut:
  the owner sorted the whole 31-tile page and said done); Matignon **11** (16 tiles carry a `checked/` doc, "Right pile: keep it"; 5 of
  those 16 also carry a recut doc and are positives, not negatives: f110_W1_16, _59, W3_15, _35, W5_56). **21 negatives.**
- Pooled 43 positives, 21 negatives (64 labelled boxes). Boxes the owner never looked at (300 of the 333 Matignon boxes) are unlabelled and not scored;
  they are given to the tool because its neighbour rule needs every box of a page.
- The owner's new box is the record's `x,y,w,h` (Matignon: the bounding box of his quad; Modena: `new_x..new_h`).
  Matignon's `moves/` docs (64) are not used as labels.

## Method (frozen; full text in the `tools/box_clip_check.py` docstring)

1. Box in image pixels: floor of x,y times the scale, ceil of x+w, y+h times the scale, clipped to the image.
2. Crop = the box plus a margin of 1.5 x its own width left and right and 1.5 x its own height above and below (ceil, clipped).
3. Ink = darker than the Otsu threshold (`skimage.filters.threshold_otsu`, 256 bins, of the crop after a Gaussian blur of sigma 1.0 px). A
   crop whose 1st-99th percentile grey range is under 20 levels has no ink.
4. Components = 8-connected ink components. A component TOUCHES the box if any of its pixels lies inside it. Components under
   max(3 px, 2% of the box's pixel area) are ignored.
5. Neighbours = every other machine box of the same page whose vertical extent overlaps this box's by at least half the shorter of
   the two heights. A touching component is ignored when it has more pixels (inside the crop) in one single neighbour box than in this box.
6. FLAGGED CLIPPED when, over the kept touching components, ink outside this box and outside every neighbour box is >= 25% of their total ink
   (all their pixels in the crop). A touching component's outside ink is joined to its inside ink by construction.
7. GROWN box = the bounding box of the pixels of the kept touching components that have such outside ink, with pixels inside a
   neighbour box removed first; an unflagged box's grown box is the machine box. Reported in the page's own box units (divided by the scale, rounded).

Known limitations, stated now and not corrected afterwards: (i) the Modena page boxes only g/q signs, so unboxed neighbouring letters are
invisible to rule 5 there and their joined ink can count as the sign's own; (ii) Modena crops are about 15 x 28 px at half size; (iii) a
Matignon strip is 93 px tall, so a sign cut by the strip's top or bottom edge cannot be seen as clipped, and a grown box cannot leave the strip;
(iv) the crop edge truncates any component that is longer than the margin. After scoring I will report how many positives have an owner box that
leaves the strip or page image (a diagnostic, not a filter).

## Controls (rule 3)

- (a) **Random-flag null.** The flags are shuffled over the labelled boxes 10,000 times (seed 20261012, `numpy.random.RandomState`); p =
  (k + 1) / 10,001, k = the number of shuffles whose balanced accuracy (mean of recall and 1 - false-alarm rate) is >= the observed one.
  The registered shuffle is over all 64 labelled boxes. ADDED here (a deliberate tightening, not in the brief): the same p with the flags
  shuffled only within each sorter, because the share of positives differs by sorter (Modena 21 of 31, Matignon 22 of 33) and a rule that merely
  tracked the sorter could otherwise pass a pooled shuffle.
- (b) **Small-box baseline.** Flag every box whose pixel-unit area (w x h) is below the median area of all machine boxes on its page (all boxes
  of the page, labelled or not; a page is `R1162_p1`, `R1168_f12r`, `f110_W1`..`W5`). Its recall, false-alarm rate and balanced accuracy are
  computed on the same labelled boxes.

## Gate (all lines must hold, pooled over both sorters)

| # | line | threshold |
|---|---|---|
| 1 | recall on the 43 positives | >= 0.70 |
| 2 | false-alarm rate on the 21 negatives | <= 0.30 |
| 3 | balanced accuracy minus the small-box baseline's | >= +0.10 |
| 4 | permutation p, flags shuffled over all labelled boxes | < 0.05 |
| 4b | permutation p, flags shuffled within each sorter (added) | < 0.05 |
| 5 | median IoU(grown box, owner box) minus median IoU(machine box, owner box), over all 43 positives (grown = machine where unflagged) | >= +0.15 |

Also reported, per sorter (Modena, Matignon): the same lines with the controls recomputed inside the sorter, and the median IoU on the flagged
positives only. A pooled PASS that one sorter fails is reported as exactly that. The pooled gate decides step 3 (the live flags); the per-sorter
lines do not change the pooled verdict but are stated beside it. Small N (10 and 11 negatives) is stated, not hidden: it is why p and the
false-alarm line are read together.

## Ruled out as theatre

Tuning any parameter after seeing a score (the blur, the margin, the 25%, the minimum component, the neighbour rule); reading the owner's boxes
inside the method (they are read only in `run_boxclip.py`, for IoU); scoring unlabelled boxes; reporting only the pooled number; changing the
label rule after seeing which boxes are positive. The only thing allowed after scoring is a table clearly labelled "sensitivity (not the test)"
of the 25% rule at 15% and 35% (and one exploratory IoU variant), which changes nothing.

## Order of work and frozen files

1. This file is committed first. 2. The tool, its offline test and the scorer are committed second. 3. The scorer is run once; `RESULTS.md` and
`scores.tsv` are committed third. `run_boxclip.py` prints whether its two frozen files match the hashes below.

FROZEN tools/box_clip_check.py sha256 1032ae740361c465f277ff023feff15509155c7294a62bfab263b64b0de47929
FROZEN benchmark-tx/boxclip/run_boxclip.py sha256 21d5345cba78b804b93c098f6f3ea42d616bf0903e431c7eeb81341959cbaf67

Step 3 (the frozen check over every box of the live sorter pages that the owner has not finished) runs only if the gate above passes.
