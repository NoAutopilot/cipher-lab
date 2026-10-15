# PREREG PIS-INT (15 Oct 2026, written 16:5x UTC by date -u, before any pass is read or any decode run)

Job: .claude/briefs/runs/2026-10-15-acct4-default-1634-jobs.md "PIS-INT" (LANE DEFAULT-A4-1634-15, account 4).
Item: BnF fr.16045 f.121 (canvas 252, btv1b9060906j), the small interlinear glosses written above cipher groups in the body (not the margin blocks
PIS-121/121B scored). Table: key.tsv (Tomokiyo's 1585 table; f.121 is a 1585 letter). key86.tsv is run as a secondary, labelled comparison only.

Units: two blind Sonnet passes, one crop per Read call (gloss + the cipher group under it, value-blind, key-blind); one blind reconcile.
Pairs: (group, gloss) from the reconciled read; a pair whose group or gloss the reconcile marks unreadable is listed and excluded before scoring.

Primary statistic (pis_int/score.py): per pair, sim = 1 - lev(D, G)/max(|D|,|G|), where G = gloss letters (accents folded, i/j, u/v folded,
non-letters dropped) and D = the table's decode of the group, choosing for each multi-valued sign the alternative that best matches G
(dynamic programming over alternatives; word signs S57-S67 expand to their word; nulls drop; unknown/`?` signs = one wildcard letter scoring 0.5).
A pair "decodes to its gloss" if sim >= 0.60. M = number of such pairs.
Control (rule 3, same axis): shuffled pairs -- each gloss dealt to a different group (random derangement, 2,000 draws, seed 1585); the statistic
depends on which gloss sits over which group, so the control can differ from the target. Pass: M_real > p95 of M_shuffled AND M_real >= 2.
Power control: each gloss enciphered with key.tsv (random homophone per letter), then 25% of signs replaced by random signs; 5 seeds; must pass
by the same rule, else the test is a non-test.
Tool run (required by the brief, secondary, not the gate): tools/interlinear_align.py align with --code-prefix @ --prior key.tsv --shuffle 200;
its CONSISTENT real vs p95 is reported as given.
Outcomes: PASS -> per-pair agreement logged, no key.tsv or ciphertext edit, every token stays M. FAIL with power PASS -> a miss on these pairs,
logged with per-pair numbers; a pair that disagrees is logged, not resolved. Too few pairs (< 3 readable) -> non-test.
