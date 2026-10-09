# Gloss read, fr.3623 f.23r (TXP-B23, 9 Oct 2026)

A late-16th-century Italian letter (BnF fr.3623 f.23r) is written in a symbol cipher in 8 lines; a period hand wrote the
decipherment in ordinary Italian handwriting in the space ABOVE each cipher line (an interlinear gloss). Your job is to
transcribe that gloss, letter by letter, as written. You are one of two independent readers.

Read ONLY: this brief, `gloss_crops/f23r_slip.jpg` (the whole slip, about 1200 px wide; enlarge it, e.g. 3x with PIL, into
your own scratch directory, never into the repository) and the line crops `gloss_crops/f23r_L01.jpg, L02, L04, L06, L08,
L10, L12, L14, L16.jpg` (each centred on one gloss row; they also show pieces of the cipher lines; use them as close-ups,
the slip image decides which row is which). Open no other file in the repository.

Which gloss belongs to which cipher line (the cipher lines are the rows of symbols; the gloss is the handwriting just above
each): G01 = above the 1st cipher row (begins "dopo"; a few small words are written higher still, above this row's words,
as corrections or additions -- see below), G02 = above the 2nd cipher row, ... G08 = above the 8th (last) cipher row. The
closing formula and the signature at the bottom right of the slip are NOT gloss: skip them. The folio number at top right
is not gloss.

Rules:
- One output row per gloss line G01..G08: the words left to right, separated by single spaces, period spelling exactly as
  written (u/v and i/j as written, no accents added, no modern corrections, no expansion of abbreviations you are not sure
  of). Keep word breaks as the writer made them.
- A word written higher, above another gloss word (a correction or insertion): put it in the `above` column with the word
  it sits over, e.g. `Seri>uoce`; do not merge it into the text.
- A sign the decipherer left unexpanded, or a mark you cannot resolve to letters: `+`. A letter you cannot read: `?` (one
  per letter). A numeral: write the digits.
- conf: H (all clear), M (one or two letters doubtful), L (much doubtful); note: which words are doubtful.

Output: one TSV at the path your task names, header exactly `line	text	above	conf	note`, rows G01..G08. No other file
in the repository; run no git. When done, report in two lines: words per line, and the doubtful words.
