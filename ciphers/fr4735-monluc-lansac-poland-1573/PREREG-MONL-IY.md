# PREREG-MONL-IY (MONL-EYE, 14 Oct 2026, account 4, for LANE DEFAULT-A4-2135-14)

Written and pushed before any run with the option. Baseline = align_c268.py on ciphertext_c268.tsv as committed after the
MONL-EYE reverts (L04:6, L04:8, L04:23, L05:12 back to K12), default seed 140, 200 draws.

Option: `align_c268.py --fold-iy` additionally folds y -> i in the clear text, the table values and the f.139 control text
(the existing fold is i/j, u/v). Everything else (scores, span, controls, seed, draws) unchanged. Without the flag the script's
outputs are byte-for-byte what they are now (`--check` must still pass).

Numbers reported, with and without the option: real confirm count and share (confirmed/keyed); shuffled-clear mean, p95, max and
count of draws at or above the real share (200 draws, seed 140, the option applied to every draw); f.139 control share.

Registered line: the option is kept (made the committed default for the c268 job outputs) only if, with the option,
(1) the shuffled-clear control max stays under 0.50, and
(2) 0/200 shuffled draws reach the real share, and
(3) the real share minus the shuffled-clear mean is no smaller than without the option.
Any one failing: the option stays in the script as off-by-default, the outputs stay unfolded, and the result is logged as is.
The 4 K53 = i tokens facing clear y (L01:22, L03:3, L03:21; L05:4 faces s) are expected to move from contradict to confirm; that
expectation is not part of the gate.
