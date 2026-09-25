# Pass B summary — blind transcription of body cipher runs

Independent pass B, worked only from the three named full-resolution images, no reference to any
other file in the repository, no web search, no coordination with pass A.

Found **4 cipher runs across all 3 leaves** (both m0179 and m0180 carry one run each; m0276 carries
two runs, separated by a stretch of plain Portuguese). No leaf had zero cipher.

- **m0179** (foliated "80", dated "Londres 28 de Abril de 1713"): one run, `m0179-r1`, 19 tokens,
  introduced by "...que naõ hé mais q.e" and followed by "e algua coisa mais á manhaã...". All
  tokens digits except one glyph (position 16) transcribed as `ff?` — a two-stroke symbol with a
  small loop/curl at the top of each stroke that does not read cleanly as either a numeral or an
  ordinary lowercase letter; flagged uncertain. One further digit (position 9) is flagged `7?`
  because the shape (a bare top stroke + diagonal, no mid crossbar) is genuinely ambiguous between
  numeral "7" and letter "z" in this hand.
- **m0180** (foliated "81", dated "Londres 2 de Maio de 1713"): one run, `m0180-r1`, 22 tokens,
  introduced by "...darei a memoria por que" and followed by the plain word "tudo." then "Naõ
  referi o Diario...". All tokens digits, including one instance (position 8) of a numeral "7"
  written with a clear horizontal crossbar through the diagonal stroke (the continental
  crossed-7 convention) — read with reasonable confidence, not flagged. Position 20 (`8?`) is a
  compressed loop shape most consistent with "8" but a "2" reading cannot be excluded; flagged
  uncertain.
- **m0276** (a later body letter, no page/foliation number visible on this leaf — the cipher text
  begins at the very top of the leaf's legible writing with no plaintext salutation above it,
  consistent with this leaf continuing a letter begun on the previous folio): two runs. `m0276-r1`
  (17 tokens) opens the leaf and ends just before the plaintext "mas isto hé imposivel, nem o tempo
  o permite, e só serve"; `m0276-r2` (20 tokens) begins right after that plaintext phrase and ends
  just before "Cá naõ cuido de dizer que o novo Enviádo...". This leaf mixes single roman-letter
  code symbols (d, f, z, x, y, e, t, m, a) freely with digit groups — the letters are visually
  distinct from surrounding cursive prose by their isolation inside period-separated tokens. One
  glyph in `m0276-r1` (position 10) is the same two/three-parallel-diagonal-stroke shape seen on
  m0179 and is likewise transcribed `ff?`, flagged uncertain; it may or may not be the same symbol
  as the m0179 occurrence — the m0179 version showed a small loop at the top of each stroke while
  the m0276 version showed plain unlooped strokes, so I record both as best-guess `ff?` without
  claiming they are identical.

Total: 78 token rows across 4 runs, written to `body_passB.tsv`. Three tokens are flagged uncertain
with a trailing "?" (m0179 positions 9 and 16; m0180 position 20); everything else was read at
reasonable confidence directly from the image at high zoom (crops at 6x-14x native resolution were
used throughout to resolve individual strokes).
