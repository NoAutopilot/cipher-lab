# PREREG TX-ENGINEER-2 round 3 (lane, 9 Oct 2026 17:1x UTC by date -u; pushed BEFORE any read or score of these jobs)

Gate, pools, blindness: PREREG-txeng2-0 (+ Amendment 1). Round 2 results (dev only, no eval look): X1 detector 0/21 FAIL; X3
4/5 FAIL though the widened lattice holds the truth at 10 of 12 dev errors; X4 3/12 truth-in-top-3 FAIL, 2/9 as weights; X9
dev 10/12 at 14% PASS, eval read-free registered rule FAIL (inputs missing), substitute 9/15 at 2.9%. Eval pool stays 34.

## R2 Homophone-complete truth variant for the gloss items (TXP-KP2; Opus 5.5; cap 3; read-free)
TXP-REBUILD's diagnostic (declared after its scores): 61 of f.89's 87 passZ "errors" on the key_print truth are signs whose
key_print majority value IS the gloss letter but below the 0.75 / n >= 3 qualification -- notation, not reads (CLAUDE.md rule 3,
PX-BRODEC: normalise both sides before diffing). Variant `kp2`, declared here before it is scored: S(L) = every key_print sign
with value L at share >= 0.3 and n >= 2 (a multi-valued sign belongs to every such L; label-map merged as before); scored
positions as in R otherwise. Pool rule (fixed now): dint-f89-gloss-kp2 enters the DEV pool only if it scores >= 100 positions,
its GAPS4 control is rank 1/201 unseeded, and passZ's err_true on it is <= 0.25 (above that the truth is still charging
notation, and the item stays out); f98v/f113 (< 100 scored) and bir1591-f23r (jackknife C-, 32/46 self-supported) stay out of
every pool. Report kp, kp2 and passZ/passA/passB on each; tx_power on the dev pool with and without f89-kp2.

## X7 Same-sign retrieval strip (TXE2-SAME; Opus 5.5; cap 7)
At the X9 combo feed's dev_tune positions (latt+vote+selfcons, ~48 positions), a sheet row = the tile at 4x with +-1 context
and, for each candidate sign (L's sign; the lattice runner-up; the taxonomy pair partner if any), a STRIP of up to 6 other
occurrences of that sign on the SAME page as L reads them (atlas boxes of f178v, cut from the page image; never from another
leaf, never a printed cell). Question per row: "which strip does the tile belong to, or neither" (strips in seeded random
order, sign names hidden; row->sign map never shown). Opus 5.5 reader, <= 16 rows per call (3 calls), value-blind; resolve
pick -> that sign, neither/? -> keep L; output committed before scoring; paired vs L_dev_tune, dev gate p < 0.05. Control
(registered): strips SWAPPED between candidates (seed 1, one call on the same rows) must not pass. Stated difference from the
retired compare family: every exemplar is the hand's own page as read, so a wrong-way result retires the show-rule family for
good; a right-way result says the pull came from foreign exemplars.

## X12 Count-then-read (TXE2-COUNT; Opus 5.5; cap 6)
Items: dint-f128-print (dev; pass A 2 deletions) and ceppo-f87-S (dev). Step 1: one Opus call per leaf that COUNTS the signs
per line (no identities), from the leaf's crops; read-free score: share of lines within +-1 of the truth line length (gate >=
0.8, else stop: FAIL read-free). Step 2 (if met): one blind Opus read per leaf with the counts in the brief ("line N has K
signs; if you find K+-1, say which position is doubtful"), same crops/vocabulary as pass A; committed before scoring; paired vs
pass B (dint, --label-map) / pass A (f87); dev gate fixed > broken p < 0.05 on the pooled two items; deletions and insertions
counted (tx_bench err_true includes insertions).

## X13 Lattice-proposed cells, image-checked at 4x, no exemplar (TXE2-CELLS; Opus 5.5; cap 6)
At the same X9 dev_tune positions: a row = the tile at 4x with +-1 context and the NAMES of two cells (L's sign and the
widened lattice's top alternative from X3's lattice d), the blind sign sheet as the only reference; question "cell A, cell B
or neither". Opus 5.5, <= 16 rows per call (3 calls); resolve as X7; paired vs L_dev_tune, p < 0.05. Control (registered):
alternative replaced by a random cell (seed 1, one call) must not pass. Different from TXE-C (selection by the doubt feed,
candidates from the lattice, no exemplar rows).

## X8 Cost at equal error (TXE2-COST; Opus 5.5; cap 8; S5 measurement, no gate)
dint-f128-print (85 scored, 4 lines): (a) one Opus call per LINE at 2x line crops (4 calls); (b) one Opus call for the whole
page (1 call); same vocabulary and brief otherwise; readers blind. err_true per arm (--label-map) with CI, paired vs pass B,
and per arm the subagent-reported input/output token counts as the cost proxy -> cost per 100 signs at the arm's error;
reported beside the first campaign's figures (TRANSCRIPTION.md target 8).

Costs: R2 3, X7 7, X12 6, X13 6, X8 8 = 30. No eval look in this round.

## X2b Pair classifier calibrated on the hand's OWN ink (TXE2-PAIR2; Opus 5.5; cap 5; read-free; added 17:2x UTC, before any score)
Nearest prior: X2 / TXE2-PAIR (secure tiles of other leaves, LOLO 0.95-1.00, dev 1/11 wrong way; its own reading: "a no.87-domain
calibration set would be a different instrument"), MQS-CLASSIFY-ROUNDS (whole-inventory retrain on owner piles). What is
different: the training tiles are no.87's own dev_tune boxes with their truth value (new information: the hand's ink at the
scan scale where the errors live), trained LEAVE-ONE-LINE-OUT across the 12 dev_tune lines (a line's own tiles never train the
classifier that votes on it), the same feature set and pair list as X2, threshold per pair from the leave-one-line-out margin
curve on the 11 training lines; applied only at positions whose L sign is a pair member, override above threshold. Dev gate
paired fixed > broken p < 0.05 vs L_dev_tune. Controls: (a) permuted truth labels within pair (5 seeds) must not pass; (b) the
X2 secure-tile classifier's result reported beside. If dev passes: train on ALL dev_tune lines, apply to eval_heldout, commit
the file, do NOT score it (the lane spends the look). Amendment 1 item (4): this brings new information (the hand's own
labelled ink), not a re-weighting of the same passes. The truth column of no87_box_token.tsv / the truth file is read ONLY
by the training step for the training lines and by tx_bench at scoring; never by the apply step.

## N1 Colour master of no.87 (M25 / O4, deferred): Gallica probe at 17:2x UTC 9 Oct answered <code below>; a colour fetch is
allowed from 10 Oct 00:00 UTC (lane rule 7). If it answers then: one `iiif_lines.py --ark ark:/12148/btv1b9060248g --canvas
182/183/184` fetch at native colour, then tx_prep.py channel/sep/false and tx_recovery.py bleed-through under the read-free atlas
proxy (the TXE-D harness), ONE blind read of dev_tune at the best rendering paired vs pass A, dev gate p < 0.05. Nearest prior:
O1/O2/O4/M4 (TXE-D, greyscale sources: a non-test for colour), O5 (TXE-G). What is different: a colour source where every prior
rendering test was greyscale by construction.
