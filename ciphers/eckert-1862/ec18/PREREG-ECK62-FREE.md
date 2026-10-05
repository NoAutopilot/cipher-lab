# PREREG-ECK62-FREE (RUN6-ECK62, 5 Oct 2026, account-1 worker for LANE-RUN6): print-free book assignment

Written and pushed before any number below is computed. Follows RUN3-ECK62's retired print-agreement rule (PREREG-ECK62 c,
control failed 41/78 vs 38/78).

Data: vol18.json (sha256 cb162574..., pilot1864/manifest.tsv); corpus = the 8 IA `_djvu.txt` files of OR ser. I 1862
volumes RUN3-ECK62 used as DIR62 (vols. 7, 9, 10 pt 1-2, 11 pt 1/3, 12 pt 1/3); none can print a 1864-65 telegram, so no
entry's own print is used. Decode as the committed outputs: `--possessive --guard DIR62`.

Statistic (ec18.py `--assign-free DIR62`): corpus bigram counts over lowercased [a-z]+ words. Marker words (ec18.N1 | N2)
are deleted from every entry's text before decoding, for every entry. Decode the entry with key.md and with key-no2.md.
For each keyed word-kind token (a bracketed meaning that ec18.meaning_words keeps), it is "supported" when
count(left neighbour word, first meaning word) >= 2 or count(last meaning word, right neighbour word) >= 2 (neighbours:
the adjacent plain word or adjacent meaning's word; {braces} are boundaries). score_bk = supported tokens. Decide
book 1 if s1 - s2 >= 2, book 2 if s2 - s1 >= 2, else '?'.

Known answer: every marker-known entry (book '1' or '2' by ec18.book), markers deleted: accuracy among decided.
Control (shuffled key; can differ because it changes only the code-word -> meaning pairing, keeping each key's code-word
list, coverage and meaning inventory): 20 seeds (0-19), within each key permute the meanings among kind=='word' rows
(numerals, punctuation, time and other kinds fixed); recompute known-answer accuracy per seed.
Gate (all four): real accuracy >= 0.85; real decided >= 20; real accuracy > max shuffled accuracy; real accuracy minus
mean shuffled accuracy >= 0.15. Pass -> each '?' entry (all 192, not only print-matched) gets its decision written as
`1f`/`2f` (assigned print-free; the book is S, tokens keep the assigned key row's grade; H only where mssEC 41/47 gives the
value). Fail -> every '?' entry stays '?' and the instrument is logged as failing its control. Outputs assign_free.tsv,
assign_free_summary.tsv; `--check` regenerates.
