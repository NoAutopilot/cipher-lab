# Blind transcription pass, fr16045 f.244v / f.245r (RUN4-PIS1, 4 Oct 2026)

You are one of two independent readers of ONE page. Do not read any file in ciphers/fr16045-pisany-rome-1585 except the
ones named here; do not read key86.tsv, key.tsv, NOTES.md or anything under kp86/, kp86b/, tx86/ (values must stay hidden).

Inputs:
- Reference sheet: ciphers/fr16045-pisany-rome-1585/tx86b/SIGNSHEET86.png (73 labelled cells T01-T73 cut from a
  published table of this cipher; a cell may show a faint circle or a "?" drawn by the table's author -- ignore those
  marks, read only the sign; parts of neighbouring cells sometimes show at a cell's edge).
- Line crops, named in your instructions (each line in two segments s1/s2; s2 repeats about the last 100 px of s1, so
  start s2 after the last sign you already read from s1). f.244v also has a one-segment crop f244v_L00_L01.jpg: ordinary
  handwriting "...fait." then cipher signs -- read only the signs after the full stop, as line L00.

Task: for each line, read every cipher sign of the line in the middle of the crop, left to right, and write its label.
Rules:
- Ignore the edges of the neighbouring lines above and below, and any small writing between lines (small letters above
  the signs are a later hand: skip them).
- Ignore ordinary handwriting at a line's start or end (f.245r L07 ends in "A tant je prie" after a full stop: stop there).
- Use the closest Txx label. If a sign matches no cell, write `?` followed by a short shape name in brackets with no
  spaces, e.g. `?[hook]`. If unsure between labels, write the best label with a trailing `?` (e.g. `T41?`).
- A slanted stroke `/` between signs: write `/` as its own token.
- Two-part cells (e.g. T52, T53, T59, T60, T61 look like two characters): prefer the compound label when the strokes
  sit together as in the cell.
- Do not guess the language or normalise; the content is unknown to you.
- Read each crop image (Read tool), one crop at a time; do not open any full page image.

Output: one tab-separated file, no header: `L01<TAB>T12 T40 / T31 ...`, one row per line, at the path given in your
instructions. Then reply with: the file path, the total sign count, the count of `?` signs, and the 5 labels you found
hardest to tell apart. Nothing else.
