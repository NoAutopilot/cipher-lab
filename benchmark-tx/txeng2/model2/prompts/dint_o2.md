You are a blind reader transcribing cipher signs from manuscript crops. Read ONLY the files listed below; do not open, list or search any other file or directory. Do not resize the crops (look at them as they are; you may zoom by viewing, but write no image files).

Crops (one page, all lines, in order):
/tmp/claude-0/-home-user-cipher-lab/98b5b21b-1a0b-59d7-9254-31bf1ab2c1c8/scratchpad/dint_o2/f128_L02_s1.jpg
/tmp/claude-0/-home-user-cipher-lab/98b5b21b-1a0b-59d7-9254-31bf1ab2c1c8/scratchpad/dint_o2/f128_L02_s2.jpg
/tmp/claude-0/-home-user-cipher-lab/98b5b21b-1a0b-59d7-9254-31bf1ab2c1c8/scratchpad/dint_o2/f128_L03_s1.jpg
/tmp/claude-0/-home-user-cipher-lab/98b5b21b-1a0b-59d7-9254-31bf1ab2c1c8/scratchpad/dint_o2/f128_L03_s2.jpg
/tmp/claude-0/-home-user-cipher-lab/98b5b21b-1a0b-59d7-9254-31bf1ab2c1c8/scratchpad/dint_o2/f128_L04_s1.jpg
/tmp/claude-0/-home-user-cipher-lab/98b5b21b-1a0b-59d7-9254-31bf1ab2c1c8/scratchpad/dint_o2/f128_L04_s2.jpg
/tmp/claude-0/-home-user-cipher-lab/98b5b21b-1a0b-59d7-9254-31bf1ab2c1c8/scratchpad/dint_o2/f128_L05_s1.jpg
/tmp/claude-0/-home-user-cipher-lab/98b5b21b-1a0b-59d7-9254-31bf1ab2c1c8/scratchpad/dint_o2/f128_L05_s2.jpg

Leaf: BnF fr.3621 f.128r (Gallica btv1b52524472n canvas f265), Dinteville to Nevers, Langres, 1 July 1592.
French letter with an inline cipher passage of 4 lines; a period hand wrote the decipherment (gloss) in small
letters ABOVE each cipher line, word by word. Some gloss words are abbreviated; the decipherer wrote "+" or "|" where
he left a sign unexpanded. Clear French words are also written inside the cipher lines ("et", "Il ha laisse", the
opening "...a Mr de Gondy qui sert de Florance", the closing word at the end of line 5).

Crops (each line cut in two overlapping segments s1 = left, s2 = right; about 150 px of overlap, so the last signs
of s1 reappear at the start of s2 -- transcribe each sign ONCE): in each crop, the cipher line is the middle row;
the gloss for it is the small writing directly above it; the writing at the very bottom of a crop belongs to the
NEXT line, ignore it.
  L02: only the right part of L02 is cipher (after "et"); its gloss is above it ("ma dit").
  L03, L04, L05: whole line cipher (L05 ends in a clear word).

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

Output: write ONE file, TSV, header exactly:
line	seg	order	gloss	signs	note
One row per gloss word (or per clear word, or per run of signs with no gloss above), left to right:
  line: L02..L05; seg: s1 or s2 (the segment where the word mostly sits); order: 1,2,3... within the line
  gloss: the gloss word as written above, letters only, keep the period spelling (u/v, i/j as written); a clear
         word written in the cipher line itself goes as CLEAR:<word>; signs with no gloss above them: gloss = -
  signs: the cipher sign labels lying directly under that gloss word, space-separated, in order
  note: anything uncertain, e.g. "gloss word partly lost", "sign 3 could be z"
Do not guess what the plaintext "should" be from the gloss; record what the image shows under each word.

Write the file to: /tmp/claude-0/-home-user-cipher-lab/98b5b21b-1a0b-59d7-9254-31bf1ab2c1c8/scratchpad/dint_o2/out.tsv
Then report in two sentences: sign count per line and the hardest look-alikes. Do not decode.
