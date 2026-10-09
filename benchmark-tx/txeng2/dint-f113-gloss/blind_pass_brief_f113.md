# Blind transcription pass, fr.3619 f.113 cipher lines (TXP-D113, 9 Oct 2026)

You are one of two independent readers of the cipher signs on line crops of a French letter of 1591 (BnF fr.3619 f.113).
The pass is VALUE-BLIND: you label each hand-drawn sign by shape with the labels below. You do not know, and must not look
up, what any sign means.

Read ONLY the five crop files named in your task. Do not open any other file in this repository (no NOTES.md, no key, no
other pass, no other image); the pass is void if you do. You may make enlarged copies of the crops (e.g. PIL resize 3x,
LANCZOS) in your own scratch directory outside the repository and read those.

## What to transcribe

- Each crop is one whole manuscript line (the source was rotated 1.78 degrees to level the lines; one crop per line, no
  segments, no overlap). The line you transcribe runs along the middle of the crop. Fragments of small handwriting from
  the neighbouring rows above or below may show at the top or bottom edge or touch a sign: ignore them, transcribe only
  the signs of the middle row.
- Ordinary French handwriting (prose) is also written on these lines: f113e_L02 begins with prose and the cipher run is
  at its right end; f113_L07 begins with prose and the cipher run starts after the word "estant"; f113_L05 ends with
  prose after the cipher run; f113_L09 has a short cipher run at its start, then prose. Skip the prose words.
- A raised or baseline dot written between signs is a sign of its own (label `.`). Take every mark in a cipher run as a
  sign unless it is clearly a pen slip.

## Sign labels (use these exact labels; if a sign fits none, write NEW:<short description>; unreadable = ?)

  II   two vertical strokes (Roman two)          #    double-barred cross / hash
  1    single vertical stroke                    .    a raised or baseline dot written between signs (a separate sign)
  0    round zero / o, full size                 o    small round o (clearly smaller than 0)
  0'   zero with a stroke or accent over it      +    plus / cross
  t    cross with a lower bar (like a dagger †)   T    pi/tau shape (bar with two legs, like π)
  a    alpha/a shape                             c    c shape
  3    figure 3                                  z    z shape (small)   Z  large z
  4    figure 4 / open triangle with flag (Δ)    9    figure 9
  f    f with a cross-bar (like ƒ / £)           p    p / rho with a loop (sometimes written xp)
  y    psi/phi shape (Y with a cross stroke)     w    w / omega shape (ϖ)
  m    m with a z-tail (ɱ / m3)                  v    v / downward triangle (∇)
  sq   small square (□)                          L    inverted T / ⊥
  x    x shape                                   -:-  division sign (÷)
Overbars or dots that sit on a sign as part of it: write them as a suffix ' (prime), e.g. 0' or v'.

## Output

Write exactly one TSV file at the path your task names, with this header and one row per sign:

    passage	pos	sign_id	alt	conf	note

- `passage`: the crop's line id: `f113e_L02`, `f113_L03`, `f113_L05`, `f113_L07`, `f113_L09`.
- `pos`: 1-based position within the passage.
- `sign_id`: the label from the table, `NEW:<description>`, or `?`.
- `alt`: a second candidate label if two fit, else blank.
- `conf`: H (clear), M (plausible, one look-alike), L (guess).
- `note`: a few words on the shape; on the first row of each passage quote the prose word just before the run (or
  "line start") and on the last row the prose word just after it (or "line end").

No other output file. When done, report in a short paragraph: sign count per passage, how many NEW and ? rows, which
labels you found hardest to tell apart. Do not decode, do not guess at meanings, do not describe the letter's content.
