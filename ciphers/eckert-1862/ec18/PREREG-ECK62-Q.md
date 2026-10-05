# PREREG-ECK62-Q (D2-ECK62M, 5 Oct 2026, written and pushed before any number)

Target: the 113 mssEC 18 entries still '?' after RUN6-ECK62 (`assign_free.tsv`, assigned '?').
Instrument: `ec18.py DATA --print-q ORDIR --write|--check`, ORDIR = OR ser. I vols. 32.1-49.2 (the 48 `_djvu.txt` of
`or_volumes.tsv`, sha256 checked, not committed). No 1862 guard (DIR62 not fetched): possessive on, guard off, for every
run below alike.

1. Each entry, markers deleted (MARK, as RUN6-ECK62), is decoded with key.md (book 1) and key-no2.md (book 2); each
   reading is matched by ec18.py's own `match` (5-grams, >= 4 in one 400-word block, the entry's date within 1,500
   words before the block). g1, g2 = matched 5-grams under each book (0 when no dated match).
2. Decision: book k when gk >= 4 and gk - g(other) >= 2; '?p' when a dated match exists but the margin is < 2;
   '?' when no dated match.
3. Known answer: the same rule on the marker-known entries (book '1' or '2' by markers, markers deleted). Report decided
   count and precision per class.
4. Control (rule 3): the '?' entries with dates permuted among them (seed 18, 20 permutations); the count of dated
   matches (either book) must fall, real > max permuted.
5. Gate: known-answer precision >= 0.90 on >= 20 decided, and real > max permuted. A failed gate: no book is written
   to any entry, the numbers are logged, the step is logged untested-by-this-tool.
6. Alignment (the brief's second step): every dated match from `print_free.tsv` (25 class 'not' + the 2 already
   aligned in prose by DEF1-ECK62P) and every gated decision here is aligned with ec18_align.py's own `align` and its
   same-week control window, written to `align_free_{tokens,entries,summary}.tsv`. AGREE tokens -> C; others keep
   their key grade capped at S (book S) for 1f/2f, and for '?'-decided entries the book is C (print decides it).
