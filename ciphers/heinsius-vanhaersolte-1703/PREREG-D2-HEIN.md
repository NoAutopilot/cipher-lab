# PREREG D2-HEIN (8 Oct 2026, written before any of the 70 target pages was fetched)

Job: re-grep the 70 Deel 2 OCR pages A2P4-HAER read (Haersolte hits on printed pp.81-600, list in `haersolte_hits.tsv`)
for small-number runs of letter 1017's kind, which A2P4's 140-199 grep could not catch. Script: `small_runs.py`.

Candidate run (defined before running):
1. Page text = OCR html with tags stripped, one string per page. Dropped before tokenising: the first line (running page
   number); every line from the first footnote line on (a line opening `NNN. N.` or `NNNN. N.`, or a bare ` N. ` footnote
   continuation after it); letter headings (a line opening with a letter number, spaced or not, then `.`); years 16xx/17xx
   written solid or digit-spaced by the OCR (`1 7 0 3`); `H.A. NNN` archive references.
2. Token = a standalone 1-3 digit integer. A token counts as *small* if 1 <= n <= 70 and it is not excluded:
   preceded within 8 characters by p./pp./blz./n./nr./no./n°/fol./f./art./§; or followed (next word) by a month name or
   abbreviation (Dutch, French, Latin, English), a money or measure word (gl, gulden, fl, guldens, rd, rds, rijksd, ryksd,
   ducat(en), dukaten, st, stuyvers, pond, livres, ecus/écus, thaler, daelders, mijl(en), uur, uren, dagen, weken, maanden,
   jaren, man, mannen, bataillon(s), escadron(s), regiment(en), compagnie(n), stukken, schepen, kanonnen, pieces) or by `e`/`ste`/`de`
   as an ordinal word.
3. A **candidate run** is any set of >= 3 small tokens inside a 40-character window. Tokens 140-199 inside the run are listed
   too (mixed runs, the 1017 shape), but a run needs the 3 small tokens.

Controls (both run before the 70 pages are scored; gate = both must hold, else the 70-page result is reported as a non-test):
- Positive: letter 1017's own page, Deel 2 p.398 (`32 30 1 7 15 14`, `29 1 18 1 7 39 26 39 36 5 1 70`) must fire at least once.
- Negative: three Deel 2 pages with full-text Haersolte letters and no cipher (R11A-HEIN2): pp.17 (no.41), 60 (no.155),
  473 (no.1197), plus p.397 (letter 1017's first page, no cipher, digit-spaced years and letter numbers): must fire 0 times.
  The negatives can differ from the positive on this statistic (dates, quantities and spaced years are on them).
Hits on the 70 pages are reported with page and letter number and eye-read from text only.
