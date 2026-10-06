# PREREG-D1VIV53K (6 Oct 2026, D1-F16104K, account-1 worker for LANE DEFAULT-account-1-20261006-1240)

Committed and pushed before any scored run. Target: ink 53 (fr.16104 ff.170r-171v), reading R7A-VIV53 G (reading_piece53_G.tsv).
Question (AUDIT 4 / D1-F16104I): the decode has no f, m, p; do the key image's f, m, p (and neighbouring) cells account for the U labels?

## (i) Candidate cells, fixed from the key image alone (sources/cryptiana/web/henryiii_Vivonne1.png, viewed at 3x and 5x)
Read by shape against the passes' label descriptions (tx/SIGNS.md, tx/viv53L_windows.py), before any context scoring:
| U label (n in G) | candidate | key cell, shape |
|---|---|---|
| e (16) | f | col f row 1: script g/e-like sign with a long tail |
| o (33) | p | col p row 1: small round o with a stroke above |
| II (4) | m | col m row 1: "II" (pi-like; key.tsv already reads label P as a, noting this ambiguity) |
| Z (4) | m | col m row 2: z with a bar |
| 2 (28) | m | col m row 2 (same sign, read as a digit 2) |
| r (32) | n | col n row 2: wave stroke |
| c (31) | o | col o row 2: open hook, c-like |
| V (16) | x | col x row 2: long downward stroke |
H (2, col f row 4 "H"-like) is named but not tested: below the n >= 3 floor.

## (ii) Statistic and control
Statistic: fr16 4-gram model score (tools/judge_plaintext.NgramModel on viv63_test.FR16, the same model as the b2 gates) of the whole ink-53
G token stream decoded with key.tsv plus ONE label -> letter overlay (all other U labels dropped, as in the gates).
Control (wrong-cell assignment): the same label assigned each of the other 21 letters of the key's alphabet
(a b c d e f g h i l m n o p q r s t u x y z). It changes the decoded letters at exactly the positions the candidate does, so it can vary on the statistic.
## (iii) Pass rule, per label
PASS if the candidate letter's score ranks 1st of the 22 assignments (one-sided p = 1/22 = 0.045 under the null that the cell is no better than
any other) AND beats the current decode (label dropped). Both numbers (candidate score, best wrong-cell score and the rank) are reported for every label.
## (iv) Key change
Only PASS labels enter an ink-53-only overlay (key53_overlay.tsv; key.tsv untouched, so inks 54 and 63 do not move), graded M (cell read by shape
from the published key, not settled on the manuscript image). Combined overlay then re-runs the whole-piece gates of tx/viv53G_decode.py (b2 and the
200 wrong-key draws, seed "20261053K"): the overlay is kept only if both still PASS. Reported beside them: the registered V_strict stretch top-1
before and after (20 before). No depth claim is made here; any change goes to a verifier.
If no label PASSes, nothing is changed and the result is logged as a negative for this instrument (shape-read cell + n-gram rank).
