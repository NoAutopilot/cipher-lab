# PREREG-BRANDT-MARGIN (9 Oct 2026, written before any score; LANE FAMILY-A2f, account 2)

Question: does BRANDT-UP's known-answer test (PREREG-BRANDT-UP.md) pass when the 0020 margin gloss is read blind, with lines 1-2
re-read by readers never shown values_gate*.tsv, the ciphertext, the worker gloss or any prior pass (V-BRANDT item 3)?

Inputs (fixed now): blind passes `margin20_blindA.txt` (top-down) and `margin20_blindB.txt` (bottom-up), already on disk and committed with
this file. Two gloss inputs, one per pass, each 6 lines:
- G_A = margin20_blindA.txt lines 1-2 + glossA20u.txt lines 3-6 (BRANDT-UP's blind pass A, unchanged)
- G_B = margin20_blindB.txt lines 1-2 + glossB20u.txt lines 3-6 (BRANDT-UP's blind pass B, unchanged)
`[?]` marks are stripped by score_up.py's own norm(); the reader's text is otherwise used verbatim.

Procedure: `score_up.py` run UNCHANGED (same key values_gate_v0.tsv C rows, same 0020u/0021 ciphertext, same 0021 gloss column, seed 20261009,
2000 value-permutation controls) in a scratch copy of dk131_brandt/ whose gloss_0020u.txt is replaced by G_A, then by G_B. Output to
`score_margin.out`.

Gate (PREREG-BRANDT-UP's, unchanged): PASS if real > control p99 AND p = (1 + #{control >= real}) / 2001 < 0.01, per input, separately.

Consequence: this job changes no grade either way (brief). PASS on both inputs: reported to the lane as grounds for a verifier to restore
BRANDT-UP's LCS-matched C grades. FAIL on either: BRANDT-UP's 52 tokens stay M, and the blind-vs-worker difference on lines 1-2 is logged.
Control check: the permutation control re-assigns letters to values and so changes the letter sequence matched against the fixed gloss;
it can differ from the target on the LCS statistic.
