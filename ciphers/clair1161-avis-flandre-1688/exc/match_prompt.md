You are one blind sign matcher. Work alone. Open ONLY these two images:
- SHEET: /home/user/cipher-lab/sources/cyphersolver/2026-10-14-lasry/clair1161/lasry_p073_1.png -- a key sheet for a cipher manuscript: one
  column per plaintext letter (a b c d e f g h i l m n o p q r s t u/v x y z) with 1-4 exemplar sign images stacked under each letter
  (row 1 = top exemplar); below, a nomenclature table (digit pairs and one sign '###' -> words) and two null signs ('///' and an x-blot).
- MONTAGE: {MONTAGE} -- several rows, each headed by an id in blue (e.g. {EX}). Each row shows 1-3 windows cut from the cipher manuscript;
  in each window the TARGET sign is the one directly between the two small red ticks (top and bottom edge). All windows in a row are meant
  to be the same sign; neighbouring signs are context only.
Task: for EVERY row id, say which single sheet exemplar shows the same sign shape as the row's target, as `<column>:<row>` (e.g. `s:3`,
`u/v:2`), or a nomenclature/null entry (`nom:###`, `nom:<digit pair>` if the target is a digit forming part of a listed pair, `null:///`,
`null:x`), or `none` if no exemplar on the sheet is the same sign. Judge by shape only; do not guess letters from context. If the windows in
a row disagree, answer for the majority and say so in the note.
Write a TSV to {OUT} with header `id<TAB>sheet<TAB>confidence<TAB>note` (confidence high/med/low; note <= 12 words describing the target's
shape), one row per id. Reply with only the file path.
