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

