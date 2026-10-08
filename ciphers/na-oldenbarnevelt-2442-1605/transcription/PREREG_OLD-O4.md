# PREREG OLD-O4 (8 Oct 2026, written and pushed before the re-score was computed)

Job: OLD-O4 (account 2, LANE FAMILY, brief .claude/briefs/runs/2026-10-08-ytbiz-family-1909-jobs.md "### OLD-O4"), step (o4):
the pass-notation fix for the S rule on the scan 10 block (L10). No new vision; same files as OLD-S10
(transcription/passK_OLDS10_L10_{A,B}.tsv, transcription/reconciled_L10_OLDS10.tsv, digit_key.json + 5=s, 6=b).

1. Folds (the S-test normaliser only, `fold_o4`, applied after diff_pass2.norm_tok):
   (a) `v` -> `r` (both blind passes write this hand's cursive r as v; the reconciliation writes it r);
   (b) `(` -> `l` (pass A writes l as `(`).
   No other fold. Case is already lowered by norm_tok.
2. Applied alike to BOTH blind passes' tokens AND the reconciled (key/reading-side) tokens, everywhere the S test compares
   them: the best-matching-line choice (decode_L457.best_line) and the in_A / in_B membership test. A genuine v on the
   reconciled side (e.g. L10 "7v38d7", "d8v8^a") is folded to r on both sides alike, so it cannot gain or lose a match by
   the fold alone.
3. Not folded: the decode itself and the lexicon test (the decode is of the raw reconciled token under the fixed key, as
   OLD-S10). So reading_L10.txt's words do not change; only grades (S/M) can change.
4. Grade rule otherwise unchanged (PREREG_OLD-S10 item 5): S = normalised token in the best-matching line of both passes
   AND decode in the es1600 + Don Quijote lexicon; M otherwise; no H, no C.
5. Matched control under the same normalisation (can differ from the target: depends on the key). For each of the 120
   permutations of the vowel map {2,3,4,7,8} -> {u,i,a,o,e} (5=s, 6=b fixed): the S share of cipher tokens (V.S. excluded)
   computed exactly as item 4 with the folds of item 1. The both-pass membership part is key-independent; the lexicon part
   depends on the key, so a wrong key can score lower or higher than the fixed key. Reported: fixed-key S share, permutation
   mean, max, rank. Pass mark: fixed key ranks 1 of 120 and beats the best permutation. The OLD-S10 lexicon-hit-share
   control is also re-run and reported; it does not involve the passes, so it is identical by construction under this fold
   (stated as such, not counted as a test of the fold).
6. Numbers reported (not ruled): S/M counts of cipher tokens, S share of digit tokens, longest contiguous S stretch in digit
   tokens (same rule as PREREG_OLD-S10 item 7), beside OLD-S10's registered 15.7% / 6 and its unregistered sensitivity
   26.3% / 7. A figure that differs from the 26.3% sensitivity is reported as computed, not adjusted.
7. The OLD-S10 grading stays reproducible: `scripts/decode_L10.py --norm s10` prints the OLD-S10 counts; the committed
   reading_L10*.txt/tsv carry the OLD-O4 grades, and `--check` tests them.
