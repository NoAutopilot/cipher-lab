# PREREG R11A-BRO (6 Oct 2026, 13:53 UTC, committed and pushed before any neighbouring-leaf transcription exists)

Question: does the clear prose of letter 134's neighbours (m0277 = rest of letter 134; m0272 = letter of 22 Oct 1713;
m0278 = letter 135, 29 Oct 1713) contain text the letter-134 candidate decode (reading_body_tokens.tsv, rows m0275-r1,
m0276-r1, m0276-r2) matches beyond what same-writer clear prose from non-adjacent letters matches?

Script: `scripts/21_crib_gate.py` (written after this file, before the transcriptions are scored; it implements exactly this).

Statistic T(text): letters-only, lower-case, accents stripped, folded v->u, j->i, y->i. Candidate k-grams: every
distinct 5-letter substring of a run of consecutive C-graded tokens in the candidate (Span A = m0275-r1 + m0276-r1,
one run across the page break; Span B = m0276-r2; M and U tokens break a run). T = number of those distinct 5-grams that
occur anywhere in the folded text.

Target: each of the three leaves' transcription separately (one Sonnet blind pass per leaf, grade M, from line crops in
images/crib/), lines marked illegible dropped.

Matched control (non-adjacent clear prose, same writer, office and register): the `deciffrada_line` column of
plaintext_appendix.tsv (the period clear text of Cartas 13-123, none of them letter 133-135), abbreviations left as
written, concatenated in file order, same folding. For each target leaf of folded length L: every window of length L
at stride 25 (wrapping round the end if L exceeds the control's length is NOT allowed: if L > control length, windows
are drawn from the control repeated at most twice and the fact is reported). Control can vary on T (T depends on text
content only), so it is not a non-test by construction.

Gate (Bonferroni over three leaves): a leaf PASSes if its T is strictly above the control windows' 98.33rd percentile
(1 - 0.05/3) at its own L, AND T >= 3. The test PASSes if any leaf passes. Also reported, not gating: per-leaf T with
the 5-grams hit, the control median/p98.33/max, and the same statistic for a letter-shuffled candidate (seed 7) as a
second null.

Consequence fixed in advance: no change to key.tsv or reading_body_tokens.tsv grades unless the gate PASSes. A
qualitative list of sentences that restate or bear on the coded content is written regardless; it licenses nothing on
its own. If the gate FAILs, the paraphrase-crib gap is logged as run (not refuted: a paraphrase need not share exact
5-grams; the instrument's limit is stated).

Known limit, stated before running: exact 5-gram overlap can only see a near-verbatim restatement; a paraphrase in
different words is invisible to it, which is why the qualitative list is kept beside it.
