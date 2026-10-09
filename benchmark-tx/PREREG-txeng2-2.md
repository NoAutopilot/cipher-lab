# PREREG TX-ENGINEER-2 round 2 (lane, 9 Oct 2026 16:3x UTC by date -u; pushed BEFORE any read or score of these jobs)

Gate, pools, blindness: PREREG-txeng2-0 (+ Amendment 1: p < 0.01 on the eval pool, 34 errors; dev gate p < 0.05 on the dev
pool). Round 0b's gloss items (TXP-D89/D98/D113/B23) are on file but their truth rule made the pipeline's read right by
construction on most positions (a key rebuilt from the same reads): dint-f89-gloss contributes 10 dev errors under its final
rule (gloss-visible), dint-f98v/f113 0, bir1591-f23r 16 only on align-conflict-flagged positions. None enters a pool until R
below re-derives their truth from a key independent of the reads; the eval pool stays 34 (eval_heldout + spinelli + f152r).

## R Truth re-derivation for the gloss items from an independent key (TXP-REBUILD; Opus 5.5; cap 4; read-free)
For dint-f89-gloss, dint-f98v-gloss, dint-f113-gloss: a second truth build `--variant keyprint` in each build script (never a
hand edit): a position is `scored` when its aligned gloss chunk is one letter L (gloss conf not '?') and L has a key_print
inverse set S(L) = {signs whose key_print majority value is L with agree >= 0.75 and n >= 3} (label-map merged exactly as the
reader vocabulary merges D/al/zh: a merged label is in S(L) for every letter of its members), and the alignment is not flagged
uncertain; truth = S(L), WHATEVER passZ reads there (no reference to the leaf's own key or to passZ's sign). Everything else
excluded with its class. For bir1591-f23r-gloss (no outside key): `--variant jackknife`, the key rebuilt from all OTHER lines of
the leaf (agree >= 0.75, n >= 2) scores line i; label it C- (same readers' errors on other lines still shape the key). Writes
`<item>.truth.keyprint.tsv` (or .jackknife.tsv) + sha256 and a second BENCHMARK-TX row `<item>-kp` (or `-jk`) pointing at it,
same split; scores passA/passB/passZ on both truths; `tx_power` E per item and for dev pool = dev_tune + dint_B + f87_C + f36v
+ the three -kp items. Prediction registered: passZ errors appear on the -kp truths (E > 0, about 10-20% of scored on f.89).
Gate for pooling (declared now): an item enters the dev pool only if its -kp truth scores >= 100 positions AND its GAPS4
alignment control is rank 1/201 unseeded or seeded by key_print only; f.98v/f.113 enter only on those terms.

## X1 Sheet inventory as the instrument (TXE2-SHEET; Opus 5.5; cap 7)
Tool `tools/tx_offsheet.py` (detect / grow). detect (read-free): per position, off-sheet score = min atlas distance of the
tile to the sheet's cells' exemplars (glyph_atlas bitmaps where an atlas exists, else a tile-vs-sheet-cell normalised
correlation computed from the crops and the sheet image) + the readers' own NEW/X_/? flags in passA/passB; flagged = top
q% by score or any reader NEW flag. Measured first on dint-f128-print (dev; its D/al/zh inventory gap) and dint-f89-gloss
(dev, 43 off-sheet positions): recall of the baseline's errors at the flagged share; gate >= 0.5 of errors at <= 15%
flagged (read-free). grow: the flagged tiles clustered by shape (agglomerative on the same features, value-blind); each
cluster with >= 3 tiles becomes a new cell on a GROWN sheet (exemplar = the medoid tile, label NEW_k, no value). Then ONE
blind Opus read of dint-f128-print's lines with the grown sheet (same brief as pass A otherwise; one call), paired vs pass B
(dint's best single pass, `--label-map`) with NEW_k labels mapped to the reconciler's split labels only where the grown
cell's medoid is one of the reconciler's own tiles (else they score as off-sheet). Dev gate fixed > broken p < 0.05. Stated
difference from TX-SHEET (FAIL on no.87): there the sheet was complete and the hand's tiles pulled reads onto look-alikes;
here the sheet is incomplete by measurement and the grown cells are value-blind. No eval look in this job.

## X3 Widened lattice with word-level language (TXE2-LATT; Opus 5.5; cap 5; read-free)
Step 1 (gate before any fix): truth-in-lattice share at the baseline L's dev_tune errors for lattices: (a) today's
from-passes (A, B, confusion spread 0.15); (b) + atlas held-out top-3; (c) + confusion pairs from the taxonomy's list; (d)
all. Reported as k/12 per lattice; the fixer runs only on the widest lattice with share >= 0.5 (if none, X3 stops: FAIL
read-free, logged). Step 2: `tools/key_decode_lattice.py decode` with a WORD-level rescoring: each beam hypothesis's
letter string segmented by `tools/segmenter.py --lexicon it16` (or the 1572 folder's corpus) and scored by the share of
letters inside lexicon words of >= 3 letters, added as lam_w x share (lam_w swept 0.5-4 on dev_tune leave-one-line-out,
reported per value); the fix is applied ONLY at tx_doubt's two-signal positions (disagree+latt), never blanket. Dev gate
fixed > broken p < 0.05 vs L_dev_tune; shuffled-key control (20) must not pass. Stated difference from TX-DECODE/TXE-E/M14:
word-level language, a widened lattice measured first, and fixes at doubt positions only.

## X4 Calibrated sign-level confidence (TXE2-CONF; Opus 5.5; cap 6)
One blind Opus pass on dev_tune (3 calls, pass-A grouping, the unchanged blind brief + a block asking, per sign, for the
top-3 cells with probabilities summing to 1); committed before any score. Read-free scoring: (1) calibration -- reliability
table of the top-1 probability vs accuracy in 5 bins, expected calibration error, and the share of L's 12 dev errors whose
truth sits in the reader's top-3 (gate >= 0.5, else the confidence is not usable as lattice input); (2) as a DOUBT signal:
recall of L's errors at the share flagged by top-1 p < 0.7 (for X9); (3) the probabilities as lattice weights
(`key_decode_lattice from-passes` with the pass's own distribution in place of the H/M/L weights) at the two-signal doubt
positions only, paired vs L_dev_tune, p < 0.05. Not a plain re-pass: the pass itself is scored only as a calibration
instrument; its top-1 is reported but is not an arm.

## X9 + X17 Doubt detector re-tuned (TXE2-DOUBT; Opus 5.5; cap 4; read-free)
tx_doubt gains signals: `pairclf` (tx_pair_clf margin above threshold, from TXE2-PAIR's outputs), `vote` (X5's weighted vote
or uniform vote != L), `conf` (X4's top-1 p < 0.7 when its file exists), `selfcons` (X17: TXE-B's H vs H2 differ on the geo
unit; on dev/eval the K2/V_s0/V_s1 presentations vs A differ), `countchk` (X19, reported though weak). Re-chosen OR-of-<=3
rule on the dev pool (dev_tune + dint_B + f87 + f36v where signals exist) at <= 15% flagged; reported read-free on eval
(not a look). Gate: recall >= 0.7 at <= 15% on dev, >= 0.6 on eval read-free. Also the per-unit sorter curve per tile with
the new feed (tx_sorter_curve, no propagation) for S4.

Costs: R 4, X1 7, X3 5, X4 6, X9 4 = 26. No eval look in this round; the lane spends looks.
