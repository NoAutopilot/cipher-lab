# PREREG TXE3-1: which questions should the owner's sorter ask first? (account 3, Fable, session_01NGr4EgD9Bhbmri2omj7nn5; written 11 Oct 2026 06:0x UTC by date -u, BEFORE any score)

One of ten TXE3 transcription experiments launched by the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M) on 11 Oct 2026.
Read-free: no image, no reader, no model call; the benchmark truth plays the owner only inside `tools/tx_sorter_curve.py`
and is scored only through `tools/tx_bench.py`. Nothing is published, no owner page is touched, no truth file is edited.
Frozen confirm items (vivonne1573-f103r-confirm2 and every row marked confirm or single look) are not opened.

## Nearest prior and what is different
TXE2-SORT X6 (`benchmark-tx/txeng2/sorter/RESULTS.md`, `tools/tx_sorter_curve.py`, 9 Oct 2026) measured the sorter value
curve on no.87 from L (labels.tsv) under four orders -- (a) tx_doubt n_signals, (b) atlas cluster size, (c) random 10 seeds,
(d) greedy oracle -- and three propagation models, and found: whole-cluster propagation on the 140-cluster atlas is destructive
(77% majority share; every non-oracle order ends worse than the base), pile x cluster propagation is about neutral, per tile is
safe; the doubt feed finds a third to two thirds of what a perfect ranking finds in 20 decisions. What is different here: three
orders the brief names and X6 did not run -- the live sorter's own `--rank-lattice` value, the two readers' disagreement alone,
and the atlas classifier's margin -- against the same random control at 20 seeds, from the reconciled read C (passC.tsv, the
pipeline's own output, err_true 0.051 / 0.038 x) rather than L, with the endpoint the brief fixes (err_true after 10, 20, 50,
100 questions; questions to 3% and 2%) and the owner minutes it implies. The orders are added as options on the shared tool.

## Hypothesis
An informed question order (lattice value, reader disagreement or classifier margin) drives err_true down faster than a random
order of the same tiles under the same propagation model, and one of the three is the order the live sorter's "Check these
first" box should use. The null (none beats random on eval) is a result.

## Material (all on disk, all truth-free except the oracle)
- Truth: `benchmark-tx/birago1572-no87.truth.tsv` (flag column from TX-TRUTH-VERIFY; `--exclude-flagged` = x, else m).
- Base: `benchmark-tx/outputs/birago1572-no87/passC.tsv` (reconciled two passes, C). Same 853 positions as labels.tsv.
- Units: dev_tune = `benchmark-tx/txeng/units/labels_dev_tune.tsv` (f178v L01-12; tuning only); eval_heldout =
  `benchmark-tx/txeng/units/labels_eval_heldout.tsv` (f178v L13-23 + f179r L01-03; the report). f178r has no box map and
  span-excluded truth, not in any unit (as X6).
- Box<->position map `ciphers/nevers-birago-fr3251-1572/atlas/no87_box_token.tsv` (sid, line, pos, op; 1:1 rows only; its
  truth column is never read); clusters `atlas/clusters.tsv` (140-cluster over-split, unsupervised).
- Order inputs: (a) the two-pass lattice on the C skeleton `ciphers/nevers-birago-fr3251-1572/harvest/tx_decode/no87_topk.tsv`
  (TX-DECODE from-passes: passes A and B, confusion_1572 spread; no truth), the printed key `harvest/key_1572_sheet.tsv`, the
  it16dip letter LM (the LM every lattice run on this family used: TXE-E, TXE-O); (b) the `disagree` column of
  `benchmark-tx/txeng/doubt/{dev_tune,eval_heldout}_signals.tsv` (tx_doubt: passes A and B differ at the position; truth-blind);
  (c) `atlas/topk/no87_heldout.tsv` columns d1, d2 (glyph_atlas classify --topk 3 with the held-out lines kept out of the vote).
  On dev_tune the atlas labels carry known-answer per-tile overrides from those very lines (309, TX-ATLAS-B72), so the dev
  margin order is truth-contaminated and is reported as a sanity check only; the eval margin is clean.

## Simulation (tools/tx_sorter_curve.py, X6's oracle, unchanged)
A question shows one tile (one C position); the truth names its sign. Propagation models, all three run and reported:
- **pile** (PRIMARY, X6 reading 4: "never propagate an owner decision to a whole atlas cluster on this family; propagate within
  pile x cluster at most"): the decision sets the undecided tiles of the atlas cluster whose current sign equals the shown tile's.
- **cluster** (the brief's literal model, TRANSCRIPTION.md item 6): the first decision on a cluster sets every undecided tile of it.
- **none**: per tile.
Only 1:1 mapped boxes propagate; unmapped positions move alone.

## Orders compared (the registered comparison)
- (a) `lattice`: sign_sorter.value_from_lattice score = reader weight on the runner-up x decode letters changed when the
  runner-up is forced (lam 1, beam 64, the live `--rank-lattice` defaults), descending; positions with no alternative last, in
  reading order. Dev may also run lam 4 (TX-DECODE's tuned value); the rule, fixed now: eval uses the lam with the lower dev
  err_true at k=20 under pile (x), lam 1 on a tie. No other knob.
- (b) `disagree`: A != B first (the signal column), ties in reading order; then the rest in reading order.
- (c) `margin`: d2 - d1 ascending (smallest gap first); a box with no k2 counts as infinitely confident (last among mapped);
  positions with no 1:1 box after them, in reading order.
- (d) `random`: 20 seeds (0-19), mean and min-max band. THE CONTROL.
Exploratory, declared now, outside the registered comparison: `disagree_margin` (disagree first, ties and the rest by margin),
because (b) alone has about 36 of 354 dev and 22 of 402 eval positions flagged and needs a tiebreak for a 50- or 100-question
session. X6's a_doubt, b_size and d_oracle run beside for continuity (the oracle is the upper bound within the model).

## Endpoint
err_true (position errors: wrong-or-deleted / scored) after k = 10, 20, 50, 100 questions, and the number of questions to reach
3% and 2%; each under m (as measured) and x (flagged excluded), both always, never x alone. At each k in {10, 20, 50, 100} the
simulated output is written to disk and scored by `tools/tx_bench.py --exclude-flagged` with Wilson 95% (the brief's figure).

## Control and its proof that it can vary
The random order at 20 seeds varies on the endpoint by construction: different seeds show different tiles, so err_true at a
given k and questions-to-3% differ across seeds (X6's eval band at k=20 under pile spanned 0.8 to 1.5 errors removed, under
cluster -60 to -24; the offline test `tools/tests/test_tx_sorter_curve.py` asserts seeds differ). It is matched: the same base,
units, truth, propagation model and showable set as every informed order; only the order changes, which is the manipulation the
statistic (err_true vs k) measures. Rule 3's cannot-differ shape does not apply.

## Gate (fixed now)
Primary: eval_heldout, pile, x. An informed order BEATS random when its err_true at k=20 is below the random 20-seed minimum
at k=20 AND its questions-to-3% is at or below the random median (seeds not reaching count as kmax). Winner among the informed
orders: lowest err_true at k=20; tiebreak err_true at k=10, then questions-to-3%, then k=50. The m convention and the other two
propagation models are reported beside and must not reverse the winner for the recommendation to stand unqualified; if they do,
the recommendation is qualified by model. If no order beats random: "no informed order beats random on no.87 eval at this N",
and the live sorter keeps its current feed. Owner minutes: questions x 0.086 min (8.6 min per 100 flagged boxes, the owner's L74
Vivonne box check, 10 Oct 2026 -- a BOX-CHECK rate, not a sorter rate, flagged as such wherever used).

## Stop rule
Cap USD 15 / 2 h from 05:47 UTC (box ends 07:47, 80% line 07:23 UTC / USD 12). Dev first; eval run once per declared
configuration after the dev choice is written here; no re-tuning after an eval number is seen. Stop before starting a unit that
would cross 80% of either figure. No follow-ups.
