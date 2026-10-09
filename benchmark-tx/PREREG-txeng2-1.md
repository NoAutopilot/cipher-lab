# PREREG TX-ENGINEER-2 round 1 (first experiments; lane, 9 Oct 2026 15:2x UTC by date -u; pushed BEFORE any read or score)

Gate, pools, blindness: `benchmark-tx/PREREG-txeng2-0.md` (fixed). The eval pool is still being grown (0b live); every
experiment below runs its DEV phase now and takes its single eval look only after the pool branch is fixed by the
campaign's first eval look (p < 0.01 at >= 32 errors, else p < 0.05 at >= 24; whichever branch the first look uses holds for
every later experiment). No eval look is taken by a round-1 worker: it commits a dev result and stops; the lane spends looks.

## X2 Pair classifiers from known answers (TXE2-PAIR; Opus 5.5; cap 5; read-free)
Tool `tools/tx_pair_clf.py` (train / apply / control). For each look-alike pair P of the Birago 1572 hand -- {T18,T98},
{T90,T53}, {T76,T66}, {T76,T86}, {T76,T45}, {T64,T95}, {T64,T51}, {T50,T36}, {T92,T95}, {T92,T98}, {T83,T24}, {T60,T86},
{T13,T64} (the taxonomy's and TXE-C's list) -- a small classical classifier (zoned pixel features on the tile bitmap resized
to a fixed box, plus HOG if scikit-image is importable; logistic regression or kNN; nothing learned) trained ONLY on the
family's S-grade secure tiles from leaves other than no.87 (`atlas/secure_tokens.tsv` x `atlas/bitmaps.npz` / `signs.tsv`,
`atlas/sheet_truth`), with the decision threshold (margin) chosen by leave-one-leaf-out among those training leaves, never on
no.87. Applied ONLY at no.87 positions whose L read is a member of P (the box<->position map `atlas/no87_box_token.tsv`:
columns sid, fol, line, pos, sign, op only -- the `truth` column is never read before scoring, enforced by the tool reading
named columns); at such a position the output sign is the classifier's class when its margin exceeds the leave-one-leaf-out
threshold, else L's sign. Nothing else changes. Prediction registered: class-1 look-alikes move (d/s and p/t first); the
all-same-wrong floor positions move only if the classifier's margin is large there.
Dev gate: dev_tune paired fixed > broken, p < 0.05 vs L_dev_tune (`benchmark-tx/txeng/units/labels_dev_tune.tsv`). Controls:
(a) shuffled-label classifier (labels permuted within each pair's training set, 5 seeds) applied the same way must not pass;
(b) leave-one-leaf-out accuracy on the training leaves vs the pair's chance rate reported. If the dev gate passes, the worker
writes the eval_heldout output file WITHOUT scoring it (`passX2_pair_eval_heldout.tsv`, committed), and the lane takes the
look. Different from MQS-CLASSIFY-ROUNDS (whole-inventory top-1 retrain) and from every compare layout (no reader, no
exemplar shown): a measured classifier on the hand's own ink at the pair's positions only.

## X6 Sorter value curve + X20 owner decisions on file (TXE2-SORT; Opus 5.5; cap 5; read-free; S4 measurement, no gate)
X6: `tools/tx_sorter_curve.py`: with the benchmark truth as an oracle for the owner, simulate sorter sessions on no.87 (whole,
and per unit) and on each dev item that has an atlas or cluster map: at each decision the oracle names the true value of the
tile shown, and the decision propagates to every tile of the same atlas cluster on the leaf (TRANSCRIPTION.md item 6; an
impure cluster breaks its minority), the order of tiles shown being (a) tx_doubt's signal count (the sorter feed today),
(b) atlas cluster size descending, (c) random (10 seeds), (d) oracle-best (upper bound). Output: err_true after k decisions
(k = 0..200) per ordering, and decisions-to-2% per leaf; a table and a plot-free markdown. Where no cluster map exists the
curve is per tile (no propagation) and says so.
X20: apply the owner's 4 Oct 2026 sorter decisions (`sorter/owner-sort-2026-10-04/`, through `tools/sign_sorter_apply.py
--atlas-labels` or the folder's apply_labels.tsv, cluster-level, exactly as TRANSCRIPTION.md's "owner sorts are reused
family-wide" rule says) on top of L for no.87; score paired vs L on dev_tune ONLY (dev result; the eval_heldout output is
written, committed, not scored -- the lane takes the look). Prediction registered: a few positions move; the owner's labels
are one strong reader, not truth (TRANSCRIPTION.md).

## Costs
TXE2-PAIR cap 5 / box 60 min; TXE2-SORT cap 5 / box 60 min. No vision call in either. Readers: none.

## X5 Reader diversity with a learned weighting + X19 deletion detector (TXE2-WEIGHT; Opus 5.5; cap 6; read-free; added 15:5x UTC, before any score)
X5: tool `tools/tx_weighted_vote.py` (learn / vote / control). Readers = the passes on disk that cover the unit: on dev_tune A, B,
E (sheet), F (Fable), K2 (sr4), V_s0, V_s1 (and the T_ordered/T_shuffled lines where present); on eval_heldout A, B, E, F. For
each reader r and read sign s, w(r, s, t) = P(truth = t | r read s), estimated from the dev_tune lines with add-0.5 smoothing
over the key's signs, LEAVE-ONE-LINE-OUT (a line's own truth never trains the weights that vote on it); per position the chosen
sign = argmax_t sum_r w(r, s_r, t) (readers that deleted the position contribute a uniform weight); positions are tx_bench's
aligned truth positions (the same alignment as the taxonomy tool; a reader's read at a position is its aligned sign). Output
`passX5_weighted_dev_tune.tsv`; gate paired fixed > broken p < 0.05 vs L_dev_tune. Controls: (a) uniform weights (plain
majority, the TX-VIEWS family) reported beside; (b) weights learnt on permuted truth (5 seeds) must not pass. Prediction
registered: B's r<-T24 and F's m<-X_NEW biases are down-weighted; all-same-wrong positions do not move. If dev passes: weights
learnt on ALL dev_tune lines, applied to eval_heldout's A/B/E/F, `passX5_weighted_eval_heldout.tsv` written, NOT scored. Stated
difference from TX-VIEWS (retired plain re-passes): no new read, a learned per-reader-per-sign weighting of reads that exist.
X19: `tools/tx_count_check.py`: expected sign count per line from the crop's ink column profile (connected ink runs along x after
a row-band mask, split at gaps >= a fraction of the median run width, tuned on the dev lines of no.87 only) vs the read's count;
a line is flagged when |expected - read| >= 1. Read-free measure: recall of lines carrying a deletion or insertion error
(tx_bench's deleted/inserted) in passA/passB/passZ of no.87 geo + dev_tune, dint passA/F, spinelli passZ, at the share of
lines flagged; no gate (a doubt signal for X9); shelf row `weak` unless recall >= 0.7 at <= 30% of lines flagged.
