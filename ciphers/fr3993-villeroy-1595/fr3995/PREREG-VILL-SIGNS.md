# PREREG VILL-SIGNS (3 Oct 2026, committed before the score it governs; sign certification already done, no score run yet)

Key: keys/key_f159_full.tsv = the f159 figures (key_f159_letters.tsv) + target signs certified SAME by both readers:
L (lambda) = r, w (omega) = m, + = x. LIKE-only signs are not used. All other target signs are dropped, as before.
Scorer: signs_score.py, which reuses strips_score.py unchanged except that the certified sign tokens are kept as codes
(segmentation otherwise identical: two-figure-first when the pair is a key code, 'o' = 0).
Gate 1 coverage (figure + certified sign tokens / all tokens) >= 0.5.
Gate 2 power control FIRST: 20 synthetic French texts (fr16 corpus via judge_plaintext LANG_CORPORA["fr"], as strips_score.py)
at the target's length and coverage, enciphered with this key (signs included as sign codes), corrupted at the table's
measured reader error (share of I-graded cells, as strips_score.py), each ranked against 200 value-shuffled keys;
power = count at rank 1. Power < 16/20 => non-test: stop, no target score, no judge run.
Gate 3 (only if powered): target rank 1/201 and z >= 3 vs 200 value-shuffled keys => PASS, then judge_plaintext fr16 on
the decode pasted; else FAIL = control-backed negative for this key's figures+certified signs. No reading committed unless PASS.
