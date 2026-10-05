# PREREG-DEF1DAV -- blind letter-sign labelling of 168 f.247r/v (c510-511) against Tomokiyo's letter table
Written 5 Oct 2026, 21:1x UTC by worker DEF1-DAV (account 1, LANE DEFAULT-account-1-20261005-2039), before any pass is run or read.

## Instrument (different from the retired F2-fit/F1-hold-out alignment of N9-BAL2/N9-BAL3)
One blind Sonnet subagent call per canvas: it sees only line crops already on disk and images/louisxiii_davaux.png (Tomokiyo's table,
letter row "a ... z" with 1-4 signs under each letter), transcribes every cipher token in reading order, and labels every
letter-substitute sign `L:x` with the letter it sits under in the table (forced choice; `L:x|y` allowed, scored on x). It is never shown
gloss.tsv, ciphertext.txt, F1/F2, or any earlier pass. Prompt: def1dav/prompt.txt (same for all three calls, file list only differs).
Calls: (C) control = Baluze 167 f.157 (c320) crops b167f157_run1_L03/L04 + run2_L02 (s1/s2); (T1) c510 = b168f247_L01/L02;
(T2) c511 = b168f247v_run1, run2, run3, run3b, run45, run5b crops.

## Gate 1 (control first; CLAUDE.md rule 3 / family_run order)
Known answer: the 15 letter-sign positions of 167f157 L03 / R2 whose value the period interlinear gloss fixes (known_answer.py EXPECTED:
L03 e u o u n i x; R2 n s i n n a b s). Scorer def1dav/score.py aligns the control pass to ciphertext.txt's control lines (difflib on token
class + numeral) and counts label == expected at those 15 positions; a position the pass missed or did not label counts wrong.
**Gate: letter accuracy >= 0.80 (>= 12/15).** Shuffle floor reported beside it (labels permuted among the pass's own letter-sign
positions, 2000 draws). If the control misses the gate, T1/T2 are still recorded as transcription but **not decoded or scored**; the
result is logged as a non-test for this instrument at this hand, not a negative.
Caveat fixed now: the control hand (Paris secretary, 1637) is not the f.246-248 hand (d'Avaux's side); a pass on the control licenses
the labeller, not the transfer of shapes between hands.

## Gate 2 (target, only if gate 1 passes)
Decode T2 run 2 (rows of c511 run 2) with key.tsv (numerals by key, L:x -> x; unknown -> nothing). Statistic S = LCS(decoded run-2
letters, F2 letters) / len(F2), letters a-z only, u/v and i/j merged. Null: the pass's L: labels permuted among its own letter-sign
positions, 2000 draws, seed 1 (numerals fixed). **Pass: S > null p99.** Secondary (reported, not gating): S for F1 against each other
run (c510 run, c511 runs 1, 3, 4, 5) with the same null.
Power check reported beside it (not gating): the same S/null on the control's own decode vs its gloss.
No threshold is changed after any pass is read.
