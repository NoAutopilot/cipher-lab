# Blind transcription pass brief, fr2980-gramont (sign transcription only)

You transcribe cipher signs from images. You do not decode, and you never open ciphertext.txt, reconciliation.md,
key.tsv, legend.tsv, NOTES.md, or the other pass's file.

Inputs (read with the image reader):
- `legend_sheet.png`: 70 reference signs, each labelled with a neutral code k01-k70. The drawings come from other
  manuscripts in the same cipher; the hand on our leaves differs somewhat, so match by structure, not by exact look.
- `sheets/sheet01.jpg` ... `sheet23.jpg`: each sheet shows manuscript lines as rows labelled e.g. `f29r_L01a`,
  `f29r_L01b` (a = left part of the line, b = right part, no overlap). Transcribe only the ink in the
  middle band of each row; loops and strokes poking in from the lines above and below are not part of the row.

Output: one TSV file, one row per labelled row, in sheet order:
`row_id<TAB>tokens separated by single spaces`
Token rules:
- each sign is one legend code (`k17`); if no legend code fits, invent a code `n01`, `n02`... and use it
  consistently; define every invented code in a footer line `# n01 = <short shape description>, first seen <row_id>`.
- a small mark written above a sign (dots, a superscript r, a tilde, a small letter): write it as its own token
  `^<description>` right after the sign it sits on, e.g. `k17 ^two-dots`. If the mark is clearly part of how the legend
  sign itself is drawn, do not add it.
- a free-standing dot on the baseline or mid-height between signs: token `.`
- uncertain reading: append `?` (`k41?`), or give two candidates `k41|k09`. Illegible sign: `[?]`.
- keep going through all 23 sheets; save the file after every sheet (append), so nothing is lost if you stop.
Finish with a footer: `# signs: <total tokens>, rows: <n>, invented codes: <list>`.
Report in five lines: rows done, total tokens, invented codes, rows you found hardest, anything odd on the leaves.
