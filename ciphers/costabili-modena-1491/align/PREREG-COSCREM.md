# PREREG-COSCREM (FAM-COSCREM, 10 Oct 2026, written 09:2x UTC by date -u, before any comparison is scored)

Question: does the Este reconstruction of Beatrice's 1486 cipher (Cremonini 2017 cifrario n.1, plate 10.1) share sign-to-value assignments with the
R1166 P1-P2 key (align/key_n9cos2.tsv)? A known-keys rung, not this letter's key.

Disclosure: this worker cut the crops and so has seen both the n.1 plate (with values) and the R1166 key. The worker therefore does not match;
the matcher is a separate Sonnet subagent that sees only (i) images/cremonini_n1/n1_signs_only_rows.png (plaintext column cut away; rows R1-R24,
no values) and (ii) the R1166 label shape descriptions from align/labels.tsv (shapes only, no R1166 values). The worker's read of the n.1 values
(images/cremonini_n1/n1_values_worker.tsv) is committed in this same commit, before the match, and is not changed after it.

Procedure: for each of the 11 R1166 C-grade labels (+ T a b c d g o y z W) and the 7 M labels (4 8 L TT Z q x), the matcher names the one n.1 sign
(row R#, position in row) whose shape best matches, or "none" when no n.1 sign is a plausible shape match. One call, no retry.
Statistic: hits = number of the 11 C labels whose matched n.1 row value equals our C value (a "none" is a miss).
Control (rule 3): the matcher's row assignments held fixed, the n.1 row values permuted across the 19 non-empty rows 1000x (seed 1); hits recomputed
each time. The control can differ from the target (hits depend on which value sits in which row). Report real, null mean, null p95.
Design control (descriptive, no gate): the R1166 C values are compared with the n.1 value table by letter (does the n.1 sign for letter X look like
the R1166 sign for X?) is NOT run separately -- it is the same statistic read the other way.
Decision: PASS if hits >= 3 AND hits > null p95. On PASS, each M label whose matched n.1 value is a letter is tried with
`tools/decode_key.py ciphers/costabili-modena-1491 --try CODE=VALUE` (never writes key.tsv; any accepted value stays M). On FAIL, no --try, and
the n.1 table is logged as a non-matching design for R1166 (known-keys rung tried), not as evidence about R1166's own values.
