# Blind transcription pass, fr16045 f.275r, ONE LINE (RUN5-PIS3, 4 Oct 2026)

You are one of two independent readers. You read ONE line of ONE page. Do not read any file in
ciphers/fr16045-pisany-rome-1585 except the ones named in your instructions; do not read key86.tsv, key.tsv, NOTES.md,
HYPOTHESES.md or anything under kp86*/, tx86*/ other than the sign sheet (values must stay hidden).

Inputs (paths in your instructions):
- Reference sheet: tx86e/SIGNSHEET86.png (73 labelled cells T01-T73 cut from a published table of this cipher; a cell may
  show a faint circle or a "?" drawn by the table's author -- ignore those marks, read only the sign; parts of neighbouring
  cells sometimes show at a cell's edge).
- The line's crops: images/f275rL_Lnn_s1.jpg and _s2.jpg (one line in two segments; s2 repeats about the last 100 px of
  s1, so start s2 after the last sign you already read from s1).

Task: read every cipher sign of the line in the MIDDLE of the crop, left to right, and write its label. Rules:
- Ignore the edges of the neighbouring lines above and below, and any small writing between lines (small letters above
  the signs are a later hand: skip them). Ignore left-margin notes.
- Ordinary handwriting is not cipher; read only cipher signs (your instructions say where handwriting is on your line).
- Use the closest Txx label. If a sign matches no cell, write `?` followed by a short shape name in brackets with no
  spaces, e.g. `?[hook]`. If unsure between labels, write the best label with a trailing `?` (e.g. `T41?`).
- A slanted stroke `/` between signs: write `/` as its own token.
- Two-part cells (e.g. T52, T53, T59, T60, T61 look like two characters): prefer the compound label when the strokes sit
  together as in the cell.
- Do not guess the language or normalise; the content is unknown to you.
- Look at the sheet first, then each crop; zoom by re-reading if needed. Do not open any other image.

Reply with exactly one line and nothing else: `Lnn<TAB>T12 T40 / T31 ...` (use a real tab or a single space after Lnn).
