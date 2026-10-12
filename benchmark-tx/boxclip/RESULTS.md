# BOXCLIP results (12 Oct 2026)

Scored once with the frozen method of `PREREG-BOXCLIP.md`; run at 2026-10-12 01:01 UTC (machine clock). Script: `run_boxclip.py`; flags and IoU per box: `scores.tsv`.

- frozen file `tools/box_clip_check.py` sha256 1032ae740361c465: **matches PREREG**
- frozen file `benchmark-tx/boxclip/run_boxclip.py` sha256 21d5345cba78b804: **matches PREREG**

## Verdict: **FAIL** (pooled gate, every line must hold)

| gate line | number | threshold | result |
|---|---|---|---|
| recall on positives | 0.419 | >= 0.70 | **FAIL** |
| false-alarm rate on negatives | 0.381 | <= 0.30 | **FAIL** |
| balanced accuracy vs small-box baseline | 0.519 vs 0.552 (margin -0.033) | margin >= +0.10 | **FAIL** |
| permutation p, flags shuffled over all labelled boxes | 0.4970 | < 0.05 | **FAIL** |
| permutation p, flags shuffled within each sorter | 0.5312 | < 0.05 | **FAIL** |
| median IoU gain, grown vs machine box, on positives | 0.329 vs 0.347 (gain -0.017) | gain >= +0.15 | **FAIL** |

## Labels

| sorter | positives (owner re-cut) | negatives (looked at, not re-cut) | boxes on the page(s), all given to the tool |
|---|---|---|---|
| modena | 21 | 10 | 31 |
| matignon | 22 | 11 | 333 |
| **pooled** | **43** | **21** | |

## Pooled confusion table (the method, 25% rule)

| | flagged | not flagged |
|---|---|---|
| positive (owner re-cut) | 18 | 25 |
| negative (looked at, not re-cut) | 8 | 13 |

recall 0.419, false-alarm rate 0.381, balanced accuracy 0.519.

## Controls

**(b) Small-box baseline** (flag every box whose area is below the median machine-box area of its page; all boxes of the page set the median):

| | flagged | not flagged |
|---|---|---|
| positive (owner re-cut) | 27 | 16 |
| negative (looked at, not re-cut) | 11 | 10 |

recall 0.628, false-alarm rate 0.524, balanced accuracy 0.552.

**(a) Random-flag null** (the flags shuffled over the labelled boxes, 10000 shuffles, seed 20261012): observed balanced accuracy 0.519; p = 0.4970 with the flags shuffled over all 64 labelled boxes (the registered shuffle), p = 0.5312 with the flags shuffled only within each sorter (added to the gate in the pre-registration because the share of positives differs by sorter).

## IoU on positives

| | median IoU with the owner box |
|---|---|
| machine box, all 43 positives | 0.347 |
| grown box (machine box where unflagged), all 43 positives | 0.329 |
| machine box, the 18 flagged positives only | 0.391 |
| grown box, the 18 flagged positives only | 0.349 |

## Per sorter (same lines, controls recomputed inside the sorter)

### modena: 21 positives, 10 negatives

| | flagged | not flagged |
|---|---|---|
| positive (owner re-cut) | 18 | 3 |
| negative (looked at, not re-cut) | 8 | 2 |

small-box baseline: recall 0.429, false-alarm 0.500, balanced accuracy 0.464.

| gate line | number | threshold | result |
|---|---|---|---|
| recall on positives | 0.857 | >= 0.70 | PASS |
| false-alarm rate on negatives | 0.800 | <= 0.30 | FAIL |
| balanced accuracy vs small-box baseline | 0.529 vs 0.464 (margin +0.064) | margin >= +0.10 | FAIL |
| permutation p, flags shuffled over all labelled boxes | 0.5245 | < 0.05 | FAIL |
| median IoU gain, grown vs machine box, on positives | 0.375 vs 0.399 (gain -0.023) | gain >= +0.15 | FAIL |

IoU on the 18 flagged positives: machine 0.391, grown 0.349.

### matignon: 22 positives, 11 negatives

| | flagged | not flagged |
|---|---|---|
| positive (owner re-cut) | 0 | 22 |
| negative (looked at, not re-cut) | 0 | 11 |

small-box baseline: recall 0.818, false-alarm 0.545, balanced accuracy 0.636.

| gate line | number | threshold | result |
|---|---|---|---|
| recall on positives | 0.000 | >= 0.70 | FAIL |
| false-alarm rate on negatives | 0.000 | <= 0.30 | PASS |
| balanced accuracy vs small-box baseline | 0.500 vs 0.636 (margin -0.136) | margin >= +0.10 | FAIL |
| permutation p, flags shuffled over all labelled boxes | 1.0000 | < 0.05 | FAIL |
| median IoU gain, grown vs machine box, on positives | 0.291 vs 0.291 (gain +0.000) | gain >= +0.15 | FAIL |

IoU on the 0 flagged positives: machine nan, grown nan.

## Sensitivity (not the test)

Nothing below changes the verdict above: the registered threshold is 25%. The table only shows how the pooled numbers move if the outside-ink threshold were 15% or 35% (all else frozen), plus one exploratory IoU variant (the grown box united with the machine box). None of the three thresholds meets the recall (>= 0.70), balanced-accuracy-margin (>= +0.10) or IoU-gain (>= +0.15) line.

| outside-ink threshold | recall | false-alarm | balanced acc | small-box BA | IoU gain (grown vs machine) | IoU gain (grown united with machine) | p (pooled shuffle) |
|---|---|---|---|---|---|---|---|
| 0.15 | 0.465 | 0.381 | 0.542 | 0.552 | -0.020 | -0.006 | 0.3615 |
| 0.25 (registered) | 0.419 | 0.381 | 0.519 | 0.552 | -0.017 | -0.006 | 0.4970 |
| 0.35 | 0.395 | 0.333 | 0.531 | 0.552 | -0.017 | -0.006 | 0.4257 |

## Diagnostics (not the test)

Written after the verdict above was committed (`diagnostics.py`). It explains the FAIL; it changes no threshold and proposes none.

| sorter | positives | owner box leaves the page image (registered diagnostic) | owner growth that lies inside another machine box: median share of (owner box minus machine box) | positives whose growth is more than half inside other machine boxes |
|---|---|---|---|---|
| modena | 21 | 0 | 0.00 (n=21 with growth) | 0 |
| matignon | 22 | 0 | 0.33 (n=22 with growth) | 6 |

| sorter | positives: median outside_frac | negatives: median outside_frac | rank AUC (0.5 = no separation) | boxes with outside_frac > 0 |
|---|---|---|---|---|
| modena | 0.530 | 0.638 | 0.405 | 31 of 31 |
| matignon | 0.000 | 0.000 | 0.500 | 0 of 33 |
| pooled | 0.000 | 0.000 | 0.484 | 31 of 64 |

| sorter | flagged boxes | median grown area / machine area | median grown width / machine width | median grown height / machine height |
|---|---|---|---|---|
| modena | 26 | 2.79 | 2.42 | 1.15 |
| matignon | 0 | - | - | - |

Exploratory, not registered: the same frozen check with each labelled box alone on its page (the neighbour rule off, so a neighbour's joined ink counts as outside).

| sorter | flagged positives | flagged negatives | recall | false-alarm | balanced acc | rank AUC of outside_frac | median outside_frac, positives / negatives |
|---|---|---|---|---|---|---|---|
| modena | 19 of 21 | 9 of 10 | 0.905 | 0.900 | 0.502 | 0.414 | 0.535 / 0.638 |
| matignon | 11 of 22 | 0 of 11 | 0.500 | 0.000 | 0.750 | 0.795 | 0.260 / 0.000 |

## Step 3 (live flags): not run

The pooled gate FAILED, so the frozen check was not run over the live sorter pages (Matignon f.110, Pisany, Vivonne, Oldenbarnevelt, Baluze). `live_flags.tsv` was not written and no sorter page or labels file was touched.

## Reading (hand-written after the diagnostics; re-running `diagnostics.py` removes this section)

- **Registered result: FAIL on every line.** Recall 0.419 (18 of 43), false-alarm 0.381 (8 of 21), balanced accuracy 0.519 against the small-box baseline's 0.552, permutation p 0.497 (0.531 within sorter), median IoU gain -0.017 (the grown box is slightly worse than the machine box). The trivial small-box rule beats it.
- **Modena:** the check flags 26 of 31 boxes. Every one of the 31 has connected ink outside it (median outside share 0.53 on re-cut boxes, 0.64 on boxes the owner left; rank AUC 0.405, i.e. no separation and if anything backwards), because the g/q signs sit in running text and their ink joins unboxed neighbouring letters (limitation i, stated before scoring). Grown boxes are 2.4 x wider than the machine boxes they replace.
- **Matignon:** 0 of 33 flagged, outside share exactly 0 for all 33. Registered rules 5-7 take out every pixel inside a neighbouring tile; the tiles abut along the strip and the owner's additions lie partly under the next tile (median 33% of the area he added, more than half for 6 of 22 re-cut boxes). Taking neighbour-box pixels out of the "outside ink" count was a detail chosen in the pre-registration, not in the brief's wording.
- **Exploratory, not registered, seen only after the verdict:** with the neighbour rule off, Matignon flags 11 of 22 re-cut boxes and 0 of 11 checked boxes (balanced accuracy 0.750, rank AUC 0.795) while Modena stays saturated (19 of 21 and 9 of 10). That is a lead for a second, re-registered test on labels not used here (these 64 boxes have now been seen), not a result of this one.
- The verdict stands: FAIL as registered.
