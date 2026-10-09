# Blind sign pass, BnF fr.3619 f.89 (TXP-D89, 9 Oct 2026)

You transcribe the cipher signs of a French letter of 1591, line by line, from line crops. You open ONLY this brief and
the crop files named in your task; nothing else in the repository, no other file, no web. You do not know and must not
guess what the signs mean: label each sign by its SHAPE with the labels below.

The crops: one crop per manuscript line (`f89_L01.jpg` ... `f89_L14.jpg`), each about 1290 px wide and 40-60 px tall at
the scan's own resolution (small: you may make enlarged copies in your own scratchpad, e.g. with Python PIL, 3x LANCZOS,
cut into halves, and read those). Each line is cut as one crop (no segments, no overlap). The main line runs through the
middle of the crop. Small writing ABOVE or BELOW the main line (fragments of other lines, or later small writing between
the lines) is NOT part of the line: ignore it completely and transcribe only the signs on the main line.

Each line mixes ordinary handwritten French words (clear text, e.g. "faisant", "de sa majesté") with runs of cipher
signs. For a clear word write ONE row with sign_id CLEAR and the word as best you read it in the note. For every cipher
sign write one row.

Sign labels (use these exact labels; if a sign fits none, write NEW:<short description>; unreadable = ?):
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

Output: TSV, header exactly
passage	pos	sign_id	alt	conf	note
  passage: the line id from the crop name (L01 ... L14); pos: 1, 2, 3 ... left to right within the line, counting CLEAR
  rows too; sign_id: a label above, CLEAR, NEW:<desc> or ?; alt: a second-choice label if you hesitate, else empty;
  conf: H (sure), M (probable), L (guess); note: anything uncertain ("could be z", "ink blot", the clear word).
Read every sign once, in order, without skipping; a sign you cannot identify is a row with ?, never left out.
Write nothing but your output file.
