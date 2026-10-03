# PREREG-VILL-TX2 (A1B-VILL-TX2, account 1, 3 Oct 2026, written before any pass B read or score)

Pass A = Bourdeau's ct_f148r.txt + ct_f148v_149r.txt (one unmeasured pass, 22 Sept 2026), unchanged.
Pass B = one blind Sonnet read per canvas block of native line crops (tools/iiif_lines.py), given only the label legend
(the code descriptions in Bourdeau's file headers, which are the settled inventory used by VILL-SIGNS/VILL-NOMEN), never
Bourdeau's tokens.

1. Alignment: per cipher run (Bourdeau's run labels, B's reads grouped into the same runs by the clear words that bound
   them), tools/reconcile_passes.py (method nw). Agreement rate = aligned columns where A == B / aligned columns
   (gaps count as disagreement). err_2reader = 1 - agreement.
2. Gate (TRANSCRIPTION.md / CLAUDE.md Usage 6): err_2reader > 0.10 -> no third machine pass; the split sign pairs go to a
   focus list for the owner's sign sorter.
3. Settled sample: stratified random sample (seed 3993) of disagreement columns, at most 40, strata = substitution
   (digit-digit, digit-symbol, symbol-symbol) and indel, proportional with >= 4 per non-empty stratum. The worker settles
   each on the native crop as A right / B right / both wrong / cannot settle. Plus a control sample of 20 agreed columns
   (seed 3993), settled the same way, to bound error hidden inside agreement.
4. Bourdeau per-sign error estimate: err_A = d * p_dis + (1 - d) * p_agr, where d = disagreement share, p_dis = share of
   settled disagreement columns where A is wrong (A wrong = B right or both wrong), p_agr = share of settled agreed
   columns where A is wrong; "cannot settle" excluded and counted. 95% interval: Wilson on each p, combined by the
   extreme-corner bound (conservative). This is err vs a worker adjudication, not err_true (no known answer exists for
   this hand): reported as err_adjudicated, and no BENCHMARK-TX.tsv row is added (that file needs an independent known
   answer).
5. Rule 3 bracket: compare the interval with the reader-error levels the prior negatives' controls used (read from
   NOTES.md/HYPOTHESES.md); state covered / not covered.
