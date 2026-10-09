# Blind gloss read, fr.3619 f.113 (TXP-D113, 9 Oct 2026)

You are one of two independent readers of a period decipherment written between the lines of a French letter of 1591 (BnF
fr.3619 f.113). Above each line of cipher symbols, a decipherer wrote the clear text in small cursive letters, word by word.
Your job is to transcribe that small writing, letter by letter, as written. You do not need to read the cipher symbols.

Read ONLY the five crop files named in your task (and enlarged copies you make of them, PIL 3x LANCZOS, in your own scratch
directory outside the repository). Do not open any other file in this repository; the read is void if you do.

The crops (the source was rotated 1.78 degrees to level the lines) each show a cipher line with the gloss row above it, plus
pieces of the neighbouring rows. Each crop is cut at 1220 px wide or less; read the whole width.
- `f113ge_L02` (340 px wide, the right end of a line): the cipher run is the few symbols at the right of the bottom row, after
  a prose word ending in -y; its gloss is the small writing directly above those symbols (two or three short words).
- `f113g_L03`: the cipher line is the upper full-width row of symbols; its gloss is the row of small writing directly above it
  (the second row from the top, running the full width to the right edge).
- `f113g_L05`: the cipher line is the LOWEST full-width row of symbols; its gloss is the row of small writing between the two
  symbol rows (running the full width).
- `f113g_L07`: the cipher line is the run of symbols that follows the prose word "estant" (middle row, right of centre) and
  continues across the right half; its gloss is the small writing directly above that run (only above the symbols, not above
  the prose "la trouue ... estant"; on the right half it is the row just above the symbols).
- `f113g_L09`: the cipher line is the short run of symbols at the bottom left, before the prose "et nayant point"; its gloss is
  the small writing directly above it.

## Output

Write exactly one TSV file at the path your task names, header:

    line	text	conf	note

One row per cipher line, in the order above (`line` = f113e_L02, f113_L03, f113_L05, f113_L07, f113_L09 -- note f113e, not
f113ge, and f113, not f113g). `text`: the gloss letters as written, left to right, words separated by single spaces, period
spelling kept (u/v, i/j, y as written), no punctuation, abbreviations as written (no expansion). Write `+` for a cipher symbol
the decipherer copied into the gloss unexpanded (or a gap he left), `?` for each letter you cannot read. `conf`: H / M / L for
the line. `note`: doubtful words, e.g. "word 5 could be 'ces' or 'les'".

No other output file. When done, report in a short paragraph: words per line and the doubtful words. Do not open any other file;
do not try to read the cipher symbols.
