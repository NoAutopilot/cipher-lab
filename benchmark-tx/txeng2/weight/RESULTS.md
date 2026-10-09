# TXE2-WEIGHT results (LANE TX-ENGINEER-2 round 1, X5 + X19; 9 Oct 2026, 15:53-16:0x UTC by date -u)

PREREG `benchmark-tx/PREREG-txeng2-1.md` X5/X19 (binding, 143bf31e4). Read-free: no vision call, no reader. Order kept: the
X5 dev output, the uniform control and the five permuted-truth controls were committed (a50175ef7) before tx_bench scored
anything; the X19 count files were committed (8a216c937) before `recall` opened the truth. No truth file was edited.

## X5 learned per-reader-per-sign weighting (`tools/tx_weighted_vote.py`, test `tools/tests/test_tx_weighted_vote.py`)

Readers on dev_tune: A, B, E (sheet), F (Fable), K2 (sr4), V_s0, V_s1 (`benchmark-tx/outputs/birago1572-no87/`). Weights
w(r,s,t) learnt leave-one-line-out (12 dev_tune lines), add-0.5 smoothing over the 1572 key's 51 signs + X_CE.
One implementation choice stated in the tool's docstring before scoring: the VOTE aligns each reader to the base read L
(`labels_dev_tune.tsv`), not to the truth, so the voted file never sees a truth (an eval file aligned to the eval truth
would leak it); `learn` aligns to the truth exactly as tx_taxonomy does. The vote changes signs only (no indels).

Scored with `tx_bench.py OUT --item birago1572-no87 --paired benchmark-tx/txeng/units/labels_dev_tune.tsv --exclude-flagged`:

| output | changed vs L | fixed | broken | p | err_true as measured / flagged excluded |
|---|---|---|---|---|---|
| L (base) | | | | | 12/343 on common positions |
| **X5 weighted (LOO)** | 32 | **3** | **7** | 0.3438 | 0.047 (16/343) / 0.033 (11/338) |
| uniform (plain majority, same frame) | 25 | 3 | 4 | 1.0000 | 0.038 (13/343) / 0.024 (8/338) |
| permuted truth seed 1 | 82 | 5 | 58 | 0.0000 (against) | 0.201 / 0.192 |
| seed 2 | 83 | 2 | 65 | 0.0000 | 0.219 / 0.207 |
| seed 3 | 78 | 4 | 59 | 0.0000 | 0.195 / 0.186 |
| seed 4 | 95 | 3 | 77 | 0.0000 | 0.257 / 0.246 |
| seed 5 | 85 | 3 | 61 | 0.0000 | 0.204 / 0.192 |

**Dev gate FAIL** (fixed > broken and p < 0.05 needed). Every permuted control fails (as required), so the controls hold;
the real weighting is far better than permuted weights but worse than L and no better than the plain vote. **No
`passX5_weighted_eval_heldout.tsv` was written** (brief step 3).

What moved (`breakdown.py` -> `breakdown.md`, run after scoring): of 32 changes, 22 are homophone swaps inside the truth
set (e.g. X_CE -> T92, T95 -> T51: both right). Fixed 3: f178v_L06 18 (T98->T18, 4/7 readers right), L10 1 (T92->T53,
5/7), L11 29 (T60->T86, 6/7) -- the same three the uniform vote fixes. Broken 7, the mechanism: **rare signs under
leave-one-line-out**. At f178v_L02 19 six readers read T81 and A read T83; T81 occurs 6 times in all of dev_tune, so with its
own line held out most readers have no T81 count and their vote is uniform (no effect), and A's one confident T83 wins.
Same shape at L06 22 (all 7 read T27; T27 has 7 dev occurrences), L11 11 (all 7 T56), L02 23 (all 7 T64 -> T13: T64 reads
are T13 in truth 9 of 24 times on dev, the T13/T64 look-alike, summed over seven correlated readers), L01 13 and L12 10 (one
reader's T76 outweighs six T26 reads), L05 7. The independence assumption in sum_r w adds correlated readers' errors.

Registered predictions: (1) "B's r<-T24 and F's m<-X_NEW biases are down-weighted": **not testable on dev_tune** -- B read
T24 three times there, all truth T24; F read X_NEW once (truth T42), so no dev evidence of either bias exists to learn.
(2) "all-same-wrong positions do not move": **held** -- L's three all-same-wrong errors (f178v_L02 12 T36, L05 4 T90, L09 4
T96) are unchanged by X5 and by the uniform vote; the all-wrong-split L05 9 moved T64 -> T13 (still wrong).

Rule 3 reading: a learned confusion weighting over 12 lines is data-starved for a 52-sign inventory; a change of smoothing
(e.g. a diagonal prior) would be the same instrument with one knob turned and is not proposed; the plain vote (TX-VIEWS)
already shows no gain here, and X5 adds none over it. Logged untested-by-this-tool at this N.

## X19 read-free count check (`tools/tx_count_check.py`, test `tools/tests/test_tx_count_check.py`)

Line strip rebuilt from the segment crops at their manifest boxes; Otsu ink, row band >= 30% of the row-ink peak, ink
columns >= 2 px, specks < 3 px dropped, runs merged across gaps < gap_frac x median run width. gap_frac tuned on no.87
dev_tune only: **0.10, mean |expected - truth line length| 2.42 signs** (`x19_tune.tsv`). Flag = |expected - read| >= 1.

| item / pass | lines | lines with deleted/inserted | flagged | recall |
|---|---|---|---|---|
| no.87 passA geo | 6 | 1 | 5 (83%) | 1.00 |
| no.87 passA dev_tune | 12 | 1 | 10 (83%) | 0.00 |
| no.87 L geo / L dev_tune | 6 / 12 | 0 / 0 | 5 / 10 (83%) | n/a |
| no.87 passB geo / dev_tune | 6 / 12 | 2 / 3 | 5 / 10 (83%) | 1.00 / 1.00 |
| dint f128 passA / passF | 4 / 4 | 4 / 3 | 4 / 4 (100%) | 1.00 / 1.00 |
| spinelli passZ | 10 | 7 | 10 (100%) | 1.00 |

Recall is near 1 only because the flag fires on 83-100% of lines: a count error of ~2.4 signs per line on the tuning
lines is larger than the one-sign deletion it is meant to see, and the Birago-tuned gap fraction does not transfer
(dint lines miss by 50-80 runs, i.e. the f128 hand's letters split into many runs; spinelli by 1-21). Shelf grade
**weak** (needs recall >= 0.7 at <= 30% flagged; best share flagged here is 83%). Not a usable doubt signal for X9 at this
calibration.

## Files
`tools/tx_weighted_vote.py`, `tools/tx_count_check.py` (+ tests); `benchmark-tx/outputs/birago1572-no87/passX5_weighted_dev_tune.tsv`,
`passX5_uniform_dev_tune.tsv`, `passX5_perm{1..5}_dev_tune.tsv`; `benchmark-tx/txeng2/weight/changes_dev_tune.tsv`,
`breakdown.py`, `breakdown.md`, `x19_tune.tsv`, `x19_count_*.tsv`.
