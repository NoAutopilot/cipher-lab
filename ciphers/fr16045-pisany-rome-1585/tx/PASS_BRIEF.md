# Blind transcription pass, fr16045 f.75 (PIS-T, 4 Oct 2026)

You are one of two independent readers. Do not read any other file in ciphers/fr16045-pisany-rome-1585 except the ones
named here, and do not read key.tsv (it holds the values; this pass must be value-blind).

Inputs:
- Reference sheet: ciphers/fr16045-pisany-rome-1585/tx/SIGNSHEET.png (67 labelled cells S01-S67, cut from a published
  table of this cipher) and its shape list tx/SIGNS.md. S07 = S04 and S08 = S05 (same shapes): use S04 / S05.
- Line crops: ciphers/fr16045-pisany-rome-1585/images/f75_L01_s1.jpg, f75_L01_s2.jpg, ... f75_L22_s2.jpg
  (22 manuscript lines, each in two segments; s2 repeats about the last 140 px of s1, so do not count the shared
  signs twice: start s2 after the last sign you already read from s1).

Task: for each line L01..L22, read every cipher sign left to right and write its label. Rules:
- Use the closest Sxx label. If a sign matches no cell, write `?` followed by a short shape name in brackets with no
  spaces, e.g. `?[colon-bar]`. If you are unsure between labels, write the best label with a trailing `?` (e.g. `S41?`).
- Multi-stroke signs: some cells are two-part shapes (S25 "x o", S26, S57, S59, S60-S67). Prefer the compound label when
  the strokes sit together as in the cell.
- Superscript strokes and the small dots-with-bar (S31) count as signs.
- Ignore page stains; do not normalise or guess language; the content is unknown to you.
- Read each crop image (Read tool); one crop at a time; do not open the full page image.

Output: write one file, tab-separated, no header: `L01<TAB>S12 S40 S31 ...` one line per manuscript line (22 rows),
to the path given in your instructions. Then reply with: the file path, the total sign count, the count of `?` signs,
and the 5 labels you found hardest to tell apart. Nothing else.
