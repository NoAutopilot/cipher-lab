# TXE2-PAIR2 results (LANE TX-ENGINEER-2 round 3, experiment X2b; 9 Oct 2026, 17:23-17:3x UTC by date -u)

PREREG `benchmark-tx/PREREG-txeng2-3.md` X2b (binding). Tool `tools/tx_pair_clf.py --train-domain dev_tune --loo-lines`
(test `tools/tests/test_tx_pair_clf.py::test_x2b_dev_tune_loo_lines`). Read-free: no vision call, no reader, no host.
Features and pair list as X2 (zones + raw 32x32 + HOG, logistic regression C=0.1 balanced; scikit-image 0.26.0 and
scikit-learn 1.9.1 were missing in this container and were pip-installed this session).

Order kept: rules fixed in the tool docstring and pushed (1a40eed28) before any apply; dev_tune output, the five
permuted-label controls and the per-fold train/touched reports committed (4a00e9256) before tx_bench scored anything.
Truth was read only by `read_truth_lines` (training lines of each fold; the test asserts the applied line is never among
them) and by tx_bench. Disclosure: before writing the code, one diagnostic counted usable training tiles per pair over all
12 dev_tune lines (counts only, per pair; no position inspected, no rule changed by it).

## Rules (fixed before apply)
Training tiles of pair a/b = training-line positions with a 1:1 box whose L sign is a or b, labelled by which member the
truth homophone set contains (both or neither: excluded); usable when >= 3 tiles per side over >= 2 lines. Threshold t per
pair and fold: inner leave-one-line-out on the 11 training lines, t in {0..0.9} maximising net = fixed - broken of the
would-be flips (ties -> larger t); disabled when max net <= 0. Apply: L sign in an enabled pair, flip when margin > t.

## Training (`train_dev_tune.tsv`, 12 folds x 13 pairs)
Enabled pair-folds 44/156: T18/T98 11 folds, T76/T66 9, T76/T86 12, T76/T45 12; every other pair disabled in every fold
(too few tiles of one side, or inner net <= 0; T90/T53 and T60/T86, the pairs X2 broke on, never enabled). Controls
enabled 42-55 pair-folds.

## Dev gate (dev_tune, paired vs L = `benchmark-tx/txeng/units/labels_dev_tune.tsv`, `--exclude-flagged`, 343 common)

| output | considered | changed | fixed | broken | p | err_true as measured / flagged excluded |
|---|---|---|---|---|---|---|
| L (base) | | | | | | 12/343 wrong |
| **X2b real (LOLO)** | 71 | 4 | **3** | **0** | 0.25 | 0.026 (9/343) / 0.012 (4/338) |
| ctrl seed 1 | 89 | 32 | 2 | 26 | 0.0000 (against) | 0.114 / 0.101 |
| ctrl seed 2 | 83 | 34 | 3 | 27 | 0.0000 | 0.108 / 0.095 |
| ctrl seed 3 | 88 | 36 | 4 | 31 | 0.0000 | 0.114 / 0.104 |
| ctrl seed 4 | 97 | 35 | 3 | 30 | 0.0000 | 0.117 / 0.104 |
| ctrl seed 5 | 87 | 31 | 3 | 26 | 0.0000 | 0.108 / 0.098 |
| X2 secure-tile classifier (control b, committed f0ce196d1) | 119 | 13 | 1 | 11 | 0.0063 (against) | 0.064 / 0.050 |

**Dev gate FAIL** (needs fixed > broken AND p < 0.05; 3-0 gives p 0.25, and four moves cannot reach 0.05 two-sided even
at 4-0). No eval_heldout file written. Control (a) holds: no permuted seed passes, all break 26-31.

Moves (`touched_dev_tune.tsv`): f178v L05.1 T76->T45, L10.4 T76->T86, L11.5 T76->T86 (pair T76/T86 or T76/T45, margins
0.94-1.00 against t 0.7-0.9), L10.31 T98->T18 (0.999 vs 0.9). Three of the four are scored fixes; the fourth is not a
broken one (both wrong, or off the common/scored set; not inspected further).

## Reading
Calibrating on the hand's own ink reversed X2's sign: the secure-tile classifier broke 11 for 1, this one fixed 3 and broke
none, and the permuted-label controls break 26-31, so the labels carry the signal. But the instrument is conservative by
construction (only 4 of 13 pairs ever enable on 11 lines of training, thresholds 0.7-0.9) and moves 4 of L's 12 errors'
neighbourhood; the gate is not reachable at this N. What would settle it is more labelled no.87-hand tiles (another leaf
of the same hand with a known answer), not a looser threshold on the same 12 lines (rule 3, third-attempt clause: this is
the second attempt with a different instrument, logged as a dev FAIL in the right direction, not a refutation).
