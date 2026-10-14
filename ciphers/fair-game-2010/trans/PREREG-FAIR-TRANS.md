# PREREG-FAIR-TRANS (account 1, LANE DEFAULT-A1-1840-14, 14 Oct 2026, written before any score)

Hypothesis: the 67 visible marked letters (68 positions with the unknown at line 1 position 4) are English plaintext
under a pure letter transposition (no substitution): keyed columnar widths 2-12 in both orientations, or a keyless
route (unkeyed columnar / column boustrophedon / clockwise spiral at widths 2-34, rail fence 2-12 rails), each
inverted and on the reversed ciphertext. Instrument: `tools/families/transposition.py` via `tools/family_run.py`
(offline test `tools/tests/test_transposition_family.py`). Already covered elsewhere, not repeated: whole reversal,
decimation, two-line interleave (marker/marker_sweep.py, D2-FAIR).

Data: `test2/order_scroll.txt` / `order_column.txt` (GF4-BATCH22 image-checked) with `?` restored at line 1 pos 4:
`trans/scroll68.txt`, `trans/column68.txt` (primary, N=68, two lines of 34); `trans/scroll67.txt`, `column67.txt`
(secondary, `?` dropped as earlier tests did; a dropped letter shifts every later grid cell, so 67 is the weaker form).

G0 (letter counts, independent of the solver): a transposition keeps every letter's count. `trans/unigram_check.py`
scores the target's letter counts by log-likelihood under the en corpus unigram and ranks it among 2000 English
67-letter word-start windows from the same corpus. Reported as a percentile; below p01 = "the letter counts alone
disfavour English transposition at this N". Informational, does not gate G1.

G1 (control gate): `family_run.py specs/fair-game-2010.json --family transposition --cipher trans/scroll68.txt
--tokens space --seeds 28 --restarts 4` (default en corpus, Holmes + Moby-Dick), one control per design (colK
w2-12, colKi w2-12, 6 route designs), N=68 with `?` masked at the target's own position. Recovery = share of truth
letters in common runs >= 6 letters (block6; strict shift measure printed beside it). Gate: control mean >= 0.80.
Headroom: a blind (no-transposition) reading of a transposition reads ~0 by block6, so the gate is not at ceiling
by construction. Control below gate -> CONTROL BELOW GATE, logged, target not scored.

G2 (target): if G1 is met, the target is scored in both orders, N=68 and N=67; each decode through
tools/judge_plaintext.py (en; EN-FOLDS caveat: unknown reliability). Shuffle floor: --shuffle-target seeds 7-16
on scroll68. A target decode counts as "worth a verifier" only if it PASSes the judge AND every shuffled decode
FAILs; otherwise it is a control-backed negative for this family at this N, conditional on the en judge.
