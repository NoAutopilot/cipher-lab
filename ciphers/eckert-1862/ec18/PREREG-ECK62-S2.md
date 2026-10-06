# PREREG-ECK62-S2 (R10-ECK62T, 6 Oct 2026 10:46 UTC by date -u, written and pushed before any split2 flip, wrongtel or confpair number)

Question: R10-ECK62S regenerated the ec18 cascade under the split2 entry splitter (`--split2`, outputs in `s2/`) but
stopped at the wrong-telegram and conflict-pair tests, whose prereg pool sizes (18 targets, 14 positives) no longer hold.
This file names the split2 pools mechanically, runs the same three instruments on them, and states in advance the rule for
adopting `s2/` as the committed cascade. Legacy outputs and their prereg files are not edited.

Pools, mechanical, from committed `s2/` files (selection only; no flip, wrongtel or confpair number read):
1. Flip selection, PREREG-ECK62-FLIP rule 1 applied to `s2/align_free_entries.tsv` (scored >= 5, agree_rate <= 0.10,
   conflict >= 1): 17 entries (the legacy 18 of today's file minus 9985.564, which split2 cuts into three undated '?'
   parts; 9991.571, flipped by print in legacy, is book 1 by marker under split2 at 0.400 and is not selected).
   Rows: `s2/align_flip_rows.tsv` = those rows of `s2/align_free_rows.tsv` with the book swapped and source `flip-<source>`.
   Flip control (FLIP rule 2): the s2 entries with scored >= 5 and agree_rate >= 0.75, flipped the same way ->
   `s2/align_flipctl_rows.tsv`: 16 entries. Writer: `ec18_fliprows.py --split2 --write|--check`.
2. Instrument `ec18_align.py --split2 --rows s2/align_flip_rows.tsv` (and `_flipctl_`), unchanged. FLIP rule 3 gate:
   pooled flipped-control AGREE rate <= 0.15; rule 4 accepts flips as in `ec18.flips()`.
3. Wrong-telegram targets = the 17 minus rule-4 accepted flips; positive control = the 16 (agree_rate >= 0.75, scored >= 5);
   negative control = same-week other-telegram windows of positives + targets. Statistic, window, gate (pos median >= 0.50,
   neg median <= 0.25, pos p10 > neg p90) and classes exactly PREREG-ECK62-WRONGTEL. `ec18_wrongtel.py --split2` asserts
   these counts instead of 18/14.
4. Conflict-pair test, statistic, null (2000 shuffles), positive control (200 x 500, power at the pool's N) and gate
   (power >= 0.80) exactly PREREG-ECK62-CONFPAIR, seed 0. Primary pool under split2 = the targets the split2 wrongtel run
   classes `right-telegram` (not the legacy fixed list of 7, which named 9985.564's merged text); secondary, descriptive:
   all split2 targets, and the strict variant.

Adopt-s2 decision, stated before the run. Adopt `s2/` as the cascade later steps read (NOTES Remaining gaps quote s2
numbers; legacy files kept, each still `--check` current, nothing deleted or overwritten) only if all hold:
- A1 every split2 output `--split2 --check` current, including the three new runs; every legacy `--check` current.
- A2 the split known answer (9985.564 separates at "Hon CA Dana Richmond Va  Washn Apl 5 1865") PASS.
- A3 no known-answer metric worse than legacy by more than 0.01 (assign known rate, assign_free known rate,
  print_q known precision) and the align_free AGREE-minus-control margin not smaller by more than 0.02.
  Stated honestly: A3's numbers were already on file from R10-ECK62S (all four improve) when this was written; A3 is a
  floor, not a blind test.
- A4 (blind) the split2 FLIP gate and the split2 wrongtel gate both PASS. If either fails on s2 while it passed on legacy,
  the instrument does not carry to split2 and s2 is not adopted (logged with both numbers).
The confpair outcome (p, S) is a target result, not an instrument check: it does not enter the decision either way.
No key file, book, grade or reading claim is changed by this test; candidate code words stay ungraded unless the
pre-registered primary gate passes, and even then only C where two entries' printed words agree, outside key files.
