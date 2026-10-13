# PREREG-COL26-11B (account 2, LANE DEFAULT-A2-2013, 13 Oct 2026): second blind word-pairing pass, canvas 20-21, for 11 = le

Registered before pass 2 exists and before any score on it. The instrument is PREREG-COL26-WP.md / `interlinear/c20c21_word_wp.py`
UNCHANGED (sha256 473d985208891a0d6de22f5a649a59b2ef1b4dd4218c555f07358dfdbe3906d3, from 82122f874): same units, values, Control W,
seed, instrument check (83 de + 31 que pooled, H > p95 and P < 0.05), alpha 0.05/44, power rule, PASS rule. Only the pairing file changes.

**Pass 2.** One blind Sonnet subagent call per canvas on the committed crops `images/c20c21wp/` only (no new fetch). It is told the task
(pair each small-hand gloss word to the span of settled cipher groups beneath it, by horizontal placement) and given the settled groups
with indices and the gloss words per unit, exactly what pass 1 got; never a key value, never pass 1's spans. Output
`interlinear/c20c21_word_pairs_p2_raw.tsv`; mechanical reconciliation as COL26-WP (in-row, ordered, non-overlapping: a row out of order
or overlapping the previous row in its unit is dropped; indices outside the unit dropped) -> `interlinear/c20c21_word_pairs_p2.tsv`.

**Pooling rule (gating).** Pooled file `interlinear/c20c21_word_pairs_pool.tsv` = the word spans on which pass 1
(`c20c21_word_pairs.tsv`) and pass 2 agree exactly (same unit, same normalised word, same first and last group); every other word is
left unpaired. `interlinear/c20c21_word_wp_pool.py` copies the unchanged script, `c20c21_reconciled.tsv` and `key_period.tsv` into a
scratch tree with the pooled file as `c20c21_word_pairs.tsv` and runs `--stage 1`. Score 11 = le only if the instrument check CLEARS on
the pooled file; otherwise 11 is NON-TEST. Pass 2 alone through the same wrapper is reported as a diagnostic, not gating.
Reader agreement is reported: share of words both passes paired whose spans match exactly, and within one group at each end.

**Rule 3.** This is the second attempt at this instrument (COL26-WP's instrument check failed on one pass). If the pooled instrument check
fails again, the instrument is logged untested-by-this-tool for 11 at this N, and the next step needs new material (a further glossed
mixed-system leaf), not a third pass. No key edit unless PASS, then only through `tools/decode_key.py --try`, grade M unless --try's own
control passed.
