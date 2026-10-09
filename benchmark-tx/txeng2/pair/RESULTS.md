# TXE2-PAIR results (LANE TX-ENGINEER-2 round 1, experiment X2; 9 Oct 2026, 15:33-15:4x UTC by date -u)

PREREG `benchmark-tx/PREREG-txeng2-1.md` X2 (binding). Tool `tools/tx_pair_clf.py` (test `tools/tests/test_tx_pair_clf.py`).
Read-free: no vision call, no reader. Backend: zones + raw 32x32 + HOG (scikit-image 0.26.0, installed this session with
pip), logistic regression (scikit-learn 1.9.1, installed this session). Usability rule, margin and threshold rule were
fixed in the tool's docstring before any apply (>= 3 tiles per side and >= 2 leaves; t from {0..0.9} maximising
leave-one-leaf-out accuracy of decided tiles at >= 25% coverage; disabled if not above chance).

Order kept: dev_tune output and the five controls committed (f0ce196d1) before tx_bench scored anything; the truth
was opened only by tx_bench and, after scoring, by `per_pair.py` for the breakdown below.

## Training (non-no.87 S-grade secure tiles; `train.tsv`, controls `train_ctrlN.tsv`)

| pair | tiles a/b | leaves | LOLO acc at t | chance | t | enabled |
|---|---|---|---|---|---|---|
| T18/T98 | 5/18 | 9 | 1.000 | 0.783 | 0.0 | yes |
| T90/T53 | 8/43 | 10 | 1.000 | 0.843 | 0.0 | yes |
| T76/T86 | 18/24 | 8 | 0.952 | 0.571 | 0.0 | yes |
| T76/T45 | 18/42 | 11 | 1.000 | 0.700 | 0.0 | yes |
| T50/T36 | 6/20 | 8 | 1.000 | 0.769 | 0.0 | yes |
| T60/T86 | 43/24 | 10 | 0.970 | 0.642 | 0.2 | yes |
| T76/T66, T64/T95, T64/T51, T92/T95, T92/T98, T83/T24, T13/T64 | one side < 3 tiles | | | | | no (never move) |

Shuffled-label controls (labels permuted within each pair, seeds 1-5): 1-3 pairs enabled per seed, LOLO 0.62-0.92 against
chance 0.57-0.84 (control (b): real LOLO is well above both chance and the shuffled LOLO).

## Dev gate (dev_tune, paired vs L = `benchmark-tx/txeng/units/labels_dev_tune.tsv`, `--exclude-flagged`)

| output | positions considered | changed | fixed | broken | p | err_true (as measured / flagged excluded) |
|---|---|---|---|---|---|---|
| L (base) | | | | | | 12/343 wrong on common positions |
| **X2 real** | 119 | 13 | **1** | **11** | 0.0063 (against) | 0.064 (22/343) / 0.050 (17/338) |
| ctrl seed 1 | 60 | 13 | 0 | 13 | 0.0002 | 0.073 / 0.059 |
| ctrl seed 2 | 44 | 22 | 0 | 20 | 0.0000 | 0.099 / 0.086 |
| ctrl seed 3 | 70 | 25 | 1 | 24 | 0.0000 | 0.102 / 0.089 |
| ctrl seed 4 | 41 | 18 | 1 | 17 | 0.0001 | 0.082 / 0.071 |
| ctrl seed 5 | 74 | 37 | 3 | 30 | 0.0000 | 0.119 / 0.106 |

**Dev gate FAIL** (needs fixed > broken, p < 0.05): the real classifier breaks 11 for 1 fixed. No eval_heldout file was
written (brief step 3). The controls do not pass either (control (a) holds).

Per pair, real (`per_pair.py`): T53->T90 broken 3; T90->T53 broken 2; T86->T76 broken 3; T60->T86 broken 2; T86->T60 broken
1; T98->T18 fixed 1, both-wrong 1. Prediction registered ("class-1 look-alikes move, d/s and p/t first"): T90/T53 (t/p) moved
5 times, all broken.

## Reading

Near-perfect leave-one-leaf-out accuracy on the secure tiles (0.95-1.00) did not transfer to no.87: of 13 disagreements
with L, L was right on 11. Likely causes, not tested here: the secure tiles are the cleanly segmented, confidently read
signs (a selection the no.87 boxes at L's errors do not share), and no.87's ink and scan scale differ from the training
leaves (README: atlas top-1 already err_true 0.32 on no.87 held-out vs line reads 0.056). The real classifier breaks
fewer than every shuffled control (11 vs 13-30), so it carries some signal, but well below L's own accuracy at these
positions. A margin threshold fixed on training leaves cannot be re-tuned on no.87 under the PREREG; a further
attempt needs a different instrument (e.g. a no.87-domain calibration set), not another threshold.
