# PREREG-COL26-C33 (account 2, LANE DEFAULT-A2-0911-14, 14 Oct 2026): word-grain test of 20 = i on canvas 33

Registered before any pairing of canvas 33 exists and before any score on it. Script: `siblings/word_c33.py` (its docstring is the full
rule). Logged: stage 0 (the power bound, no pairing, no hit count of 20) was run once at 09:5x UTC before this file was pushed; its
output is reproduced unchanged by the script.

**Why c33.** D2-COL26 (8 Oct) tested 20 = i at line grain on the glossed sibling units outside every value-choice unit for 20 and missed
its gate narrowly (8/10, P 0.0093 vs 0.05/6 = 0.0083). c33 is one of those units and is held out from every value choice for 20
(R10-COL26B's units; DA1-COL/COL2/COL3 paired other canvases). This step moves c33 to word grain.

**Instrument.** siblings/word_col3.py's statistic, hit rule, Control W (word texts permuted over the unit's spans, 10000 draws) and power
rule, unchanged; seed 20261014 + 911; one unit (c33, rows T1-T4, B1-B5, siblings/c33_reconciled.tsv). Positive control = the C codes of
siblings/key_f23_preDA1COL.tsv (22 codes; 20 is M there). TEST: 20 -> i only; alpha 0.05/6 = 0.00833 (D2-COL26's family gate unchanged).

**Stage 0** (COL26-WP's power rule): N 6, H_ideal 6, 4 of 45 gloss words with i at offset 0/1, P_min < 1e-5 -> live.

**Stage 1.** Crops cut with `tools/iiif_lines.py --image images/crops/canvas33_full.jpg` (command pasted in NOTES.md), committed. Two
blind Sonnet passes (separate calls, neither sees the other's spans), each given the line crops, the settled groups with indices and the
gloss words per row, no key value; horizontal placement only. Mechanical reconciliation (in-row, ordered, non-overlapping; offending
row dropped) -> siblings/word_pairs_c33_p1.tsv, _p2.tsv. Each pass is scored separately.

**Gate.** Instrument check on EACH pass: positive-control C-code occurrences H > p95 and P < 0.05. If either pass fails -> 20 = i
NON-TEST at this N, and since this is the third failure of the word-pairing instrument check in this folder (COL26-WP, COL26-11B on
canvas 20-21), word pairing is [retired] for this folder (rule 3 third-attempt clause), reopened only by new material or a different
instrument. If both clear: 20 = i PASS iff on BOTH passes H > p95 and P < 0.00833; otherwise FAIL (FAIL-LOWPOWER if power at N < 0.5 on
either pass). Pooled exact-agreement spans and reader agreement are reported as a diagnostic, never gating.

**Merge rule.** No key file is edited by the script. On PASS the worker runs `tools/decode_key.py ciphers/colbert26-lathuillerie-1644
--try 20=i` and reports it; key_f23.tsv is not edited by this job (brief: no key.tsv edit); a grade change goes to a verifier.
