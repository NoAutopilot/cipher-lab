# PREREG-BRANDT-062B (9 Oct 2026, written 04:2x UTC by date -u, before either blind pass is run and before any score below is computed)

Amendment to PREREG-BRANDT-062.md. Job BRANDT-REGRADE, LANE FAMILY-A2f (account 2). Why: V-BRANDT (AUDIT.md, 9 Oct 2026) found that a
known-answer gate scored on a gloss settled by a reader who knew values_gate.tsv is not independent evidence; BRANDT-062's gloss placement
and two of its words ("König", "gulden[?]") were settled by the worker with the values on disk. This amendment re-scores the same gate on
gloss text read BLIND, once per blind pass, the worker never settling the gloss.

## Unchanged from PREREG-BRANDT-062
Data: `ciphertext_0062.tsv` group sequence per line (62 groups, 6 lines; the cipher groups, not the gloss column). Statistic: per cipher line,
LCS between the C-letter sequence of that line's groups (non-C groups removed) and the concatenated gloss letters of that line, summed over
the 6 lines. Normalisation: lowercase, ä->ae ö->oe ü->ue ß->ss, [?] dropped, a-z only. Control: uniform random permutation of the letters among
the C values, n = 2000, seed 20261009. Gate: PASS if real > control p99 AND p = (1 + #{control >= real}) / 2001 < 0.01. Non-test if fewer than
10 C-value tokens.

## What changes
1. Key: `values_gate.tsv` C rows AFTER this job's regrade (V-BRANDT item 4: 46 = d C -> M; no other value changed): 15 C values.
2. Gloss input: instead of the gloss column of ciphertext_0062.tsv, the per-line gloss text of each blind pass separately:
   `gloss62_blindA.tsv` and `gloss62_blindB.tsv` (columns line, gloss_text). Each pass is one Sonnet call over the six committed crops
   `crops62/b62_L01..L06.jpg` (crop paths only; the reader is not shown gloss_*.txt, ciphertext_0062.tsv, passA62/passB62, values_gate.tsv,
   any decode or the other blind pass). Pass A reads L01->L06, pass B L06->L01. The reader is asked to transcribe only the small interlinear
   writing above the numeral groups, and to put any word written in the main numeral line itself (clear text) in a separate field, which is
   not scored. The worker copies the reader's gloss field verbatim into the TSV; no correction, completion, re-placement or deletion. A line
   the reader leaves blank scores against an empty gloss (LCS 0 for that line).
3. Score each pass separately with `score_062b.py` (same LCS, control and gate code as score_062.py; reads only values_gate.tsv,
   ciphertext_0062.tsv and the one gloss62_blind file named on its command line).

## What each outcome licenses
- PASS on BOTH blind passes: the tokens BRANDT-062 graded C stay C, minus any token whose value is now M (46); all others M.
- FAIL or non-test on EITHER pass: every 0062 token is M; the 0062 gloss is recorded as M observations only. values_gate.tsv is not
  changed by this test either way.
Reference numbers (reported, not a gate): the PREREG-BRANDT-062 statistic on the worker gloss with the 15 regraded C values.
