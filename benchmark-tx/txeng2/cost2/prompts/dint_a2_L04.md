You are a blind reader in a transcription test. Follow the brief below exactly. Read ONLY the image files listed here; do not open, list or search any other file or directory.

Crops (in order):
/tmp/claude-0/-home-user-cipher-lab/5813f79d-1ade-59e9-a4dc-2013f41ead53/scratchpad/r/dint_a2_L04/f128_L04_s1_q1.png
/tmp/claude-0/-home-user-cipher-lab/5813f79d-1ade-59e9-a4dc-2013f41ead53/scratchpad/r/dint_a2_L04/f128_L04_s1_q2.png
/tmp/claude-0/-home-user-cipher-lab/5813f79d-1ade-59e9-a4dc-2013f41ead53/scratchpad/r/dint_a2_L04/f128_L04_s1_q3.png
/tmp/claude-0/-home-user-cipher-lab/5813f79d-1ade-59e9-a4dc-2013f41ead53/scratchpad/r/dint_a2_L04/f128_L04_s1_q4.png
/tmp/claude-0/-home-user-cipher-lab/5813f79d-1ade-59e9-a4dc-2013f41ead53/scratchpad/r/dint_a2_L04/f128_L04_s2_q1.png
/tmp/claude-0/-home-user-cipher-lab/5813f79d-1ade-59e9-a4dc-2013f41ead53/scratchpad/r/dint_a2_L04/f128_L04_s2_q2.png
/tmp/claude-0/-home-user-cipher-lab/5813f79d-1ade-59e9-a4dc-2013f41ead53/scratchpad/r/dint_a2_L04/f128_L04_s2_q3.png
/tmp/claude-0/-home-user-cipher-lab/5813f79d-1ade-59e9-a4dc-2013f41ead53/scratchpad/r/dint_a2_L04/f128_L04_s2_q4.png

You read line L04 only.

Output file: /tmp/claude-0/-home-user-cipher-lab/5813f79d-1ade-59e9-a4dc-2013f41ead53/scratchpad/r/dint_a2_L04/read.tsv

---- BRIEF ----

# TXE2-COST arm a brief (per-line call, 2x crops)

Leaf: BnF fr.3621 f.128r (Gallica btv1b52524472n canvas f265), Dinteville to Nevers, Langres, 1 July 1592.
French letter with an inline cipher passage of 4 lines; a period hand wrote the decipherment (gloss) in small
letters ABOVE each cipher line, word by word. Some gloss words are abbreviated; the decipherer wrote "+" or "|" where
he left a sign unexpanded. Clear French words are also written inside the cipher lines ("et", "Il ha laisse", the
opening "...a Mr de Gondy qui sert de Florance", the closing word at the end of line 5).

Crops: you are given ONE cipher line, rendered at 2x. The line was cut in two overlapping halves s1 = left, s2 = right (about 150 px
native overlap: the last signs of s1 reappear at the start of s2), and each half again into four pieces q1..q4 left to right, neighbours
sharing about 150 px at this scale (75 px native). Read q1,q2,q3,q4 of s1 then of s2, and transcribe each sign ONCE (skip the repeated
overlap). In each piece the cipher line is the middle row; the gloss for it is the small writing directly above it; writing at the very
bottom belongs to the NEXT line, ignore it.
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
