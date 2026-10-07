# PREREG DA1-COL2 (account 1, LANE DEFAULT-account-1-20261007-1440, 7 Oct 2026, written ~15:2x UTC before any score)

Second blind word-pairing pass on c50, c3940, c47 (the units of DA1-COL), made by three Sonnet subagent calls (one per unit) on line crops
re-cut with the recorded A2-COL13/14/15 `tools/iiif_lines.py` commands, shown only the crops, the committed *_reconciled.tsv groups and
gloss; neither this worker nor the subagents read siblings/word_pairs_da1.tsv, word_da1_out.txt or key_f23_word_da1.tsv before the pass
was written. Reconciliation is mechanical only (order/overlap repair inside a row), no boundary moved by key knowledge.

1. Re-score: `siblings/word_col2.py` = word_da1.py unchanged (statistic, Control W, seed, Bonferroni gate, power rule, 2-unit rule), with
   the pairs file swapped and the key read from the pre-DA1-COL snapshot `siblings/key_f23_preDA1COL.tsv` (key_f23.tsv at eff0df6fd), so
   the C positive-control set and the 26 test codes are exactly DA1-COL's.
2. Agreement: `siblings/compare_col2.py` (group-level and exact-span agreement per unit; six-code span listing).
3. Decision rule for the six codes DA1-COL merged at C (16 se, 20 i, 46 ce, 67 leur, 81 me, 96 que): a code whose word_col2.py verdict
   is not PASS is lowered to M in key_f23.tsv with a NOTES line (it has the support of one pass only). If the instrument check clears no
   unit on this pass, the re-score is a NON-TEST: nothing is lowered on the score, and the six stay as they are pending a third pass,
   noted. Nothing is raised: a code that PASSes here but did not PASS on DA1-COL's pass is reported, not merged (both passes must support).
