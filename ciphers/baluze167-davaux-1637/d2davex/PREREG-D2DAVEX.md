# PREREG-D2DAVEX -- exemplar-sheet letter-sign labeller, control before target (168 f.247, c510-511)
Written 5 Oct 2026, 23:3x UTC (date -u 23:3x) by worker D2-DAVEX (account 1, LANE DEFAULT-account-1-20261005-2217), before any labelling
call is made and before any exemplar is shown to a reader.

## Instrument (differs from DEF1-DAV, which labelled against Tomokiyo's printed table and scored 0/15)
References are this hand's own letter signs whose value the period interlinear gloss fixes: the 15 known-answer letter-sign positions of
Baluze 167 f.157 (known_answer.py EXPECTED; ciphertext.txt rows `167f157 L03` and `167f157 R2`), cut as single-sign crops from
images/crops/b167f157_run1_L03_s2, run1_L04_s1, run2_L02_s1/s2 (d2davex/cut_exemplars.py; boxes chosen by eye, listed in the script).
f.110r is not used: N9-BAL3 fixed only one letter-sign value there (s:x = u) and its other glossed signs conflict.

## Gate 1 (control; rule 3 order)
Leave-one-out: each of the 15 positions is labelled from the other 14 exemplars (forced choice of a letter). Gate: letter accuracy
>= 0.80 (>= 12/15), as briefed, beside a shuffled-label floor.
**Pre-run ceiling check (mechanical, d2davex/ceiling.py, run before any call):** an oracle labeller that always returns the right letter
whenever at least one *other* exemplar carries that letter scores (positions whose letter has >= 2 exemplars) / 15. If that oracle
ceiling is below 0.80, gate 1 cannot pass by construction; the control is then a non-test (CLAUDE.md rule 3: a control that cannot pass
licenses nothing), no labelling call is made, and the target is not labelled.

## Gate 2 (target; only if gate 1 passes)
One subagent call per canvas (c510 = b168f247_L01/L02; c511 = the b168f247v_run* crops) labels each letter sign against the full 15-sign
sheet, + 1 reconciliation; decode with key.tsv and score F2 vs c511 run 2 exactly as PREREG-DEF1DAV gate 2 (LCS / len(F2) > p99 of the
label-permutation null, 2000 draws, seed 1). No threshold changes after any result is read.
