# Blind transcription pass, fr.3619 f.98v cipher lines (TXP-D98, 9 Oct 2026)

You are one of two independent readers of the cipher signs on line crops of a 16th-century French letter
(Dinteville to the Duke of Nevers, BnF fr.3619 f.98v). The pass is VALUE-BLIND: you label each hand-drawn sign by
shape with the label table below. You do not know, and must not look up, what any sign means.

Read ONLY the 12 crop files named in your task. Do not open any other file in this repository; the pass is void if you do.

## Crops
Six cipher lines, L01..L06, each cut into two segments s1 (left) and s2 (right), shown at 2x native size.
- Segments of a line overlap by 100 native px (the images you read are at 2x, so 200 px in each image), about 9 signs; a sign at the right edge of s1 and the left edge of s2 is ONE sign: the last 200 px of s1 and the first 200 px of s2 show the same ink, read it once. Continue the sign count across segments, counting an overlap-duplicated sign once.
- Each crop holds its line along the middle; ignore broken fragments of other writing at the top or bottom edge.
- L01 begins with ordinary French handwriting (prose) before the cipher run starts (the run starts after the prose); skip the prose words. L06 ends with prose after the run; skip it. If a clear French word sits inside a cipher run, skip it and say so in the note of the next sign.

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

- `passage`: L01..L06. `pos`: 1-based position within the line's cipher run.
- `sign_id`: a label from the table, NEW:<description>, or `?`.
- `alt`: a second candidate label if two fit, else blank.
- `conf`: H (clear), M (plausible, one look-alike), L (guess).
- `note`: a few words on the shape when useful; on the first row of each passage write "line start" (or quote the prose
  word before the run) and on the last row "line end" (or the prose word after it).

No other output file. When done, report in a short paragraph: sign count per line, how many NEW and ? rows, which labels
were hardest to tell apart. Do not decode, do not guess at meanings, do not describe the letter's content.
