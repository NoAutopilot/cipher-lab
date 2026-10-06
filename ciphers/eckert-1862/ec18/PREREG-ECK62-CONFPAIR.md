# PREREG-ECK62-CONFPAIR (R7C-ECK62C, 6 Oct 2026 02:3x UTC, written and pushed before any number)

Question: R7B-ECK62 found that for the 18 neither-book mssEC 18 entries the dated OR match is the right telegram or close to
it (0 wrong, 7 right, 11 undecided). If a code table not covered by key.md / key-no2.md was in use, the same code word should
stand opposite the same printed word in two different entries. Is there more such cross-entry consistency among their
CONFLICT pairs than chance gives?

Input (committed, no network): `align_free_tokens.tsv` (each entry under its aligned book, as R7B-ECK62 left it),
`align_free_entries.tsv`, `wrongtel_entries.tsv`. Script `ec18_confpair.py --write|--check` -> `confpair_pairs.tsv`,
`confpair_summary.tsv`. Seeded (seed 0), deterministic.

Pairs: every target-side token row with status CONFLICT and kind `word` or `plain-replaced` (code word, printed span).
Code word normalised lower-case. Printed content set = printed-span words of >= 4 letters not in ec18.STOP.
Two pairs agree when their content sets intersect.

Statistic S (per pool): number of distinct code words that occur in >= 2 distinct entries of the pool with at least one
agreeing pair between two different entries. Within-entry repeats do not count (one context).

Null (per pool): printed spans permuted at random across all pairs of the pool (code words and entries fixed), 2000 shuffles;
p = (1 + #{S_shuf >= S}) / 2001. Can differ from S: the shuffle breaks the code-word/printed-word pairing the statistic counts.

Positive control (rule 3, power at the target's N): AGREE word pairs (kind `word`, status AGREE: code word, printed span) from
the entries of align_free_tokens.tsv that are not among the 18 targets -- a real table, same instrument. 200 subsamples: draw
whole entries in random order until the pair count reaches the target pool's pair count (truncate to it), compute S and its
own shuffle p (500 shuffles per subsample). Power = share of subsamples with p <= 0.05.
Gate (instrument): power >= 0.80 at the primary pool's N. If it fails: no target verdict; logged untested-by-this-tool at this N.

Primary pool: the 7 right-telegram entries (9669.5, 9762.135, 9808.202, 9958.527, 9969.543, 9985.563, 9987.565).
Verdict (only if the gate passes): p <= 0.05 -> "cross-entry consistency above chance" (a third table or a systematic
transcription variant; each agreeing code word listed as a candidate, grade C only where two entries' printed words agree,
nothing written into key.md / key-no2.md); p > 0.05 -> "no cross-entry consistency at this N" (not a refutation of a third
table: the pool is small).
Secondary pool, descriptive, same statistic, own power run: all 18 targets. Also listed, not gated: every code word recurring
across >= 2 target entries with its printed spans, and the months of the entries.
