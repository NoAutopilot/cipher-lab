# PREREG-TUSC-XM -- screen of Tomokiyo's two Tuscan tables against f.25 (14 Oct 2026, 22:5x UTC by date -u)

Worker TUSC-XM (Opus) for LANE DEFAULT-A2-2209-14 (account 2). Written and pushed before any score is computed.
Tables: `ciphers/_keys/tuscany-guicciardini/key_tomokiyo_guicciardini1.tsv` (T1, Guicciardini-Sillery 1593, after
Speziali 1955) and `..._guicciardini2.tsv` (T2, ca.1590, after Monts de Savasse 1997); arrangement and identification
S. Tomokiyo, Cryptiana guicciardini.htm (rule 8). Script: `q7test/tusc_xm/tusc_xm.py` (built on tools/key_crossmatch.py's
own `shuffled_key_by_class`, `decode_with`, `coverage_of`; first alternative of an `a|b` cell, the tool's convention).

**Target text.** `ciphertext.tsv` lines f25_L01..L06 only (NOT ciphertext_v2.tsv, unmeasured per BNF-Q7-ERR), `?` marks
removed, lines joined in order into one digit stream. Every result is conditional on this transcription: measured error
0.115 adjudicated (Wilson upper 0.160), and a looped sign (~12 occurrences, probably the period 8) that ciphertext.tsv
never renders as 8 (BNF-Q7-ERR). L00 (~29 digits) is not in the file and not used.

**Segmentation.** Non-overlapping two-figure groups, in frame 0 (from the first digit) and frame 1 (one digit in). Pairs
the table lacks contribute nothing (coverage reported). T2's single figures 1-9 are not segmented as such (fixed pairing);
the power check below enciphers T2 with and without them so that this limit is measured, not assumed.

**Statistic.** T = max over the two frames of the mean 4-gram log-probability (tools/judge_plaintext.py NgramModel, n=4)
of the decoded letter stream. Model: tools/data/it16/*.txt except `lettereinedited01cibrgoog.txt`, which is held out as
the synthetic plaintext source for the power check; the same model scores target, nulls and synthetics.

**Nulls (rule 3).** (a) shuffled key: 1000 class-shuffled-value keys (key_crossmatch.shuffled_key_by_class, seed 0), T
computed identically (max over frames); p_key = (1 + #{null T >= T}) / 1001. (b) shuffled target: 200 token-order
shuffles of the frame-0 and frame-1 pair streams, decoded with the real key, T computed identically; o99 = their 99th pct.

**Gate (per table).** PASS iff p_key <= 0.005 (0.01 Bonferroni over the two tables) AND T > o99. A PASS is a lead for an
image check and a human read, never a reading, never a key edit. A FAIL licenses "no fit" only where the power check
below holds; otherwise it is logged as a NON-TEST.

**Power check (must pass or the screen is a non-test).** 100 synthetic texts per condition per table, each plaintext a
window of the held-out Italian file, enciphered with the table until the cipher reaches 260 digits (greedy: at each
position a syllable code whose meaning matches the next letters is used with probability 0.5 when one exists, else a
letter code; homophone chosen uniformly among codes whose any alternative fits; j->i, k->c, w/v->u, x->s, y->i, z->s
where the table lacks them). Conditions: C0 no error; C1 digit error 0.115; C2 digit error 0.160 (error mix S:I:D =
19:12:7, the BNF-Q7-ERR measured mix); C3 "8-loss": every 8 rendered as 6, 3, 01 or dropped (equal odds, as
ciphertext.tsv renders the looped sign) plus random error 0.07 (0.115 minus the ~12/260 the looped sign accounts for).
T2 is run twice: T2a enciphered with two-figure codes only, T2b with the single figures 1-9 allowed (decoded by fixed
pairing either way). For power the null is 200 shuffled keys and 50 order shuffles per synthetic text; a synthetic
passes iff no shuffled key reaches its T (p <= 1/201) and T > its order-shuffle p99.
Licence: a target FAIL is a control-backed "no fit, conditional on the transcription" for a table only if power >= 0.8
at C2 AND at C3 (for T2: T2b, the realistic encipherment); else NON-TEST for that table. Power at C0/C1 is reported.
A synthetic-specificity line is also reported: T1-enciphered synthetics scored with T2 and vice versa (C0), share passing.

No key edit, no reading, no novelty class. Rows go to HYPOTHESES.md with both numbers (control power, target p).
