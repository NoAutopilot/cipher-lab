# DIN-FIRM step 2 pre-registration (account-3 in-session worker, 3 Oct 2026, written ~08:31 UTC before any occurrence is read)

Brief: `.claude/briefs/runs/2026-10-03-acct3-din-firm.md`, step 2. Disclosure: before writing this I saw only the
`grep` lines of `f128/print_align/align_print.tsv` naming the four conflict positions (sq->x at L03.1:30 and L05.1:51;
m->t at L04.1:43 and L04.1:54); I have not looked at the print words, the gloss or the neighbouring signs around them.

Rows under test: `sq` (s 7/9, x 2) and `m` (u 8/10, t 2) in `f128/print_align/key_print.tsv`.

For each conflicting occurrence, record: the cipher signs of the segment, the print span (print_pairs.tsv), the gloss
span (gloss_pairs.tsv), and the aligner's chunk for every sign of the segment. Classify it as exactly one of:

- **spelling** -- the print word and the period spelling differ at this letter, and the period spelling puts the key
  value (s for sq, u for m) on this sign. Evidence required: the f.128 interlinear gloss over the same segment has the
  key value letter at that place, OR the word written with the key value is a 16th-century spelling attested in
  `tools/data/fr16` (grep count >= 1 of the variant word), and the rest of the segment still parses under the key.
- **slip** -- with every other sign of the segment held at its key_print value, a hand alignment of the same print
  word puts the key value on this sign and the conflicting letter (x / t) on a neighbouring sign whose key value is that
  letter, or on no sign (a letter the cipher omits / a null), so the segment parses with no more mismatches than the
  aligner's own parse. The aligner's chunking was a DP artefact, not evidence against the row.
- **unexplained** -- neither of the above.

Promotion rule: a row is promoted to C-eligible under the strict rule (VERIFY-DIN2's `strict_no_conflict`: agree >= 2
and no conflicting print alignment) only if **every** one of its conflicts is spelling or slip. A row with any
unexplained conflict stays M. No other row is touched by this job.

Regrade: recompute VERIFY-DIN2's strict count with the promoted rows' explained conflicts removed (script
`firm/firm_grades.py`, with `--check`), and add a decode.json job carrying the strict grades per row
(`f130/print/key_dk_strict.tsv`) so `tools/decode_key.py --check` reproduces the strict counts. Token conf rule unchanged
(C only on a sign read H). Report both the old strict figure (C 177 M 311 U 39) and the new one.

## Addendum: rows `0` and `a` (DIN-LEFT, account-1 worker, 3 Oct 2026, written ~09:28 UTC before any occurrence is read)

Brief `.claude/briefs/runs/2026-10-03-acct1-din-left.md` step 1. The rule above is applied **unchanged** (same three
classes, same evidence requirements, same promotion rule: a row is promoted only if every one of its conflicts is
spelling or slip; any unexplained conflict keeps it M) to the two remaining minority-conflict rows of
`f128/print_align/key_print.tsv`: `0` (e 11/18; s 4, p 2, c 1 -- 7 conflicting occurrences) and `a` (q 4/5; ul 1 -- 1
conflicting occurrence). For `a` the key value is q; a print chunk "ul" can only be spelling or slip if the gloss or a
neighbouring sign accounts for both letters. Disclosure: before writing this I have seen only the key_print.tsv row counts
quoted here and AUDIT.md's summary of them; no occurrence, print word, gloss word or neighbouring sign. Results append to
`firm/conflicts.tsv`; `firm/firm_grades.py` is re-run unchanged (it already reads every row in conflicts.tsv).
