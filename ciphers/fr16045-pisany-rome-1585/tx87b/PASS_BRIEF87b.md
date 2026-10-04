# Blind transcription of ONE LINE, fr16045 f.302v (PIS1-302, 4 Oct 2026)

You are one of two independent readers. Do not read any file in ciphers/fr16045-pisany-rome-1585 except the ones named in
your instructions; never read key86.tsv, key.tsv, NOTES.md or anything under kp86*/, kp87a/, kp87b/, tx86*/, tx87/, tx87b/ (other than your sheet and crops) (values must stay hidden).

Inputs: the reference sheet ciphers/fr16045-pisany-rome-1585/tx87b/SIGNSHEET86.png (73 labelled cells T01-T73 cut from a
published table of this cipher; ignore faint circles or "?" marks drawn in a cell, and parts of neighbouring cells at a cell's
edge), and the two crops of your one line, s1 then s2 (s2 repeats about the last 100 px of s1: start s2 after the last sign
you already read from s1).

Task: read every cipher sign of the line in the middle of the crop, left to right, and write its label.
- Ignore the edges of the lines above and below, small writing between lines, and handwriting fragments at the far left edge
  (a margin note).
- Ordinary handwriting is not cipher. Line L01 is handwriting "qui ne qu'elle commandera" followed by cipher signs: read only
  the cipher signs after it. Every other line is cipher only; stop at the page edge on the right.
- Use the closest Txx label. A sign matching no cell: `?` plus a short shape name in brackets, no spaces, e.g. `?[hook]`.
  Unsure between labels: best label with a trailing `?` (e.g. `T41?`).
- A slanted stroke `/` between signs: write `/` as its own token.
- Two-part cells (e.g. T52, T53, T59, T60, T61 look like two characters): prefer the compound label when the strokes sit
  together as in the cell.
- Do not guess the language or normalise; the content is unknown to you. Open only the sheet and your two crops.

Output: write ONE line to the file path given in your instructions: `Lnn<TAB>T12 T40 / T31 ...` (no header). Reply with
only: the path, the sign count, the `?` count.
