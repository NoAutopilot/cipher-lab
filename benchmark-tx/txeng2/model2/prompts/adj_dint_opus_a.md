You are a third, VALUE-BLIND reader settling the places where two earlier blind readers of a cipher transcription disagree. You match hand-drawn signs by SHAPE only; you do not know, and must not try to work out, what any sign means. Read ONLY the files listed here; do not open, list or search any other file or directory.

Crops (in order):
/tmp/claude-0/-home-user-cipher-lab/98b5b21b-1a0b-59d7-9254-31bf1ab2c1c8/scratchpad/adj/adj_dint_opus_a/f128_L02_s1.jpg
/tmp/claude-0/-home-user-cipher-lab/98b5b21b-1a0b-59d7-9254-31bf1ab2c1c8/scratchpad/adj/adj_dint_opus_a/f128_L02_s2.jpg
/tmp/claude-0/-home-user-cipher-lab/98b5b21b-1a0b-59d7-9254-31bf1ab2c1c8/scratchpad/adj/adj_dint_opus_a/f128_L03_s1.jpg
/tmp/claude-0/-home-user-cipher-lab/98b5b21b-1a0b-59d7-9254-31bf1ab2c1c8/scratchpad/adj/adj_dint_opus_a/f128_L03_s2.jpg
/tmp/claude-0/-home-user-cipher-lab/98b5b21b-1a0b-59d7-9254-31bf1ab2c1c8/scratchpad/adj/adj_dint_opus_a/f128_L04_s1.jpg
/tmp/claude-0/-home-user-cipher-lab/98b5b21b-1a0b-59d7-9254-31bf1ab2c1c8/scratchpad/adj/adj_dint_opus_a/f128_L04_s2.jpg
/tmp/claude-0/-home-user-cipher-lab/98b5b21b-1a0b-59d7-9254-31bf1ab2c1c8/scratchpad/adj/adj_dint_opus_a/f128_L05_s1.jpg
/tmp/claude-0/-home-user-cipher-lab/98b5b21b-1a0b-59d7-9254-31bf1ab2c1c8/scratchpad/adj/adj_dint_opus_a/f128_L05_s2.jpg

Crops: each line in two overlapping segments s1 (left) and s2 (right), about 150 px overlap (a sign seen at the end of s1 and the start of s2 is ONE sign); the cipher line is the middle row of each crop; ignore the small gloss writing above it and the next line at the bottom. The sign labels are listed below (from the readers' instructions):

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

Disagreement sheet: /tmp/claude-0/-home-user-cipher-lab/98b5b21b-1a0b-59d7-9254-31bf1ab2c1c8/scratchpad/adj/adj_dint_opus_a/adjudicate_in.tsv

Each row of the sheet is one disputed position: passage (= line) and pos (position in the line counting the agreed signs), context_before / context_after (the agreed neighbouring signs, as labels, so you can find the place on the line crop by counting), candA / candB (what each earlier reader wrote there; "(none)" = that reader saw no sign there), their confidence and notes. For each row look at the crop and decide which reading the ink supports.

Answer with one of the sign labels above, or NEW:<short description>. Write NONE if there is no separate sign at that position (one reader split one sign in two or saw a sign that is not there); write ? only if the ink cannot decide at all. You may give a cell neither reader wrote if the ink clearly shows it.

Output: write exactly one TSV file /tmp/claude-0/-home-user-cipher-lab/98b5b21b-1a0b-59d7-9254-31bf1ab2c1c8/scratchpad/adj/adj_dint_opus_a/adjudicate_out.tsv with the header
passage	pos	sign_id	conf	note
and one row per sheet row (same passage and pos), conf H/M/L, note = a few words on the shape and which candidate you rejected. No other output file. Then report in two sentences: rows settled, how many to candA / candB / other / NONE / ?. Do not decode, do not guess meanings.
