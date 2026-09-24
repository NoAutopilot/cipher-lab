# Reconciliation, BnF fr.2980 f.29r-f.30v (transcription + key worker, 24 Sept 2026, 00:05-00:45 UTC)

## Inputs
- Images: full-resolution Gallica IIIF regions (images/manifest.json, `full_resolution_2026-09-24`), cut into
  69 lines (f.29r 14 cipher lines, f.30r 35, f.30v 20; pitch from the ink-projection autocorrelation, counts
  checked by eye) by `crop.py`, and into 23 pass sheets of 6 half-lines by `sheets.py`.
- Legend: `legend_sheet.png`, 70 neutral codes k01-k70, cut by connected components from Lasry's table
  (`sources/cryptiana/web/GL/BnF_fr3071_f17.png`) and Tomokiyo's table (`francisGramont.png`). The letter value of
  each is set by the pixel x-centre of its column header (`legend.py` -> `legend.tsv`; Tomokiyo's table separately by
  `tomokiyo_columns.py` -> `tomokiyo_columns.tsv`), not by eye (LESSONS.md, Raince 1526). The passes saw codes only.
- Pass A (`passA.tsv`) and pass B (`passB.tsv`, sheets read in reverse order): Sonnet subagents, blind, 138 rows each.

## Result of the passes: not usable as a primary transcription
| | Pass A | Pass B |
|---|---|---|
| rows | 138 | 138 |
| sign tokens (excluding `^marks` and dots) | 2,574 | 2,547 |
| invented codes (no legend match) | 31 | 65 |

Aligned row by row (difflib on codes), the passes agree on 753 of 2,620 sign positions (28.7%). The disagreement is
far above the one-tenth threshold on every row, so a third pass on the same design would not help. The cause is
the legend: the hand of fr.2980 is not the fr.3071 hand of Lasry's drawings, and a model matching by shape to an
unfamiliar reference drawing assigns different codes to the same sign. Decoding either pass with the key gives no
French (tested on f.29r rows 1-4: pass A `IFO#IEESEVGPOTC...`, pass B `#D#OV#S###D...`).

## What was done instead (f.29r only)
The reconciler (Opus) read f.29r line by line from the full-resolution crops, identifying each sign against both
tables and naming it with a descriptive code (`key.tsv`: shape, value, table source). Passes A and B were consulted
only for sign counts per row and for the free-standing dots. Every sign value comes from the Lasry or Tomokiyo table
(grade H) except those marked M in key.tsv (shape uncertain, or a value chosen by context between two table values)
and five U signs not in either table. Decoding the result gives continuous French on all 14 lines (reading.txt),
which is the check that the sign identifications are right; it is not an independent second transcription.

Sign identities fixed from context while reading (recorded in key.tsv, grade M or noted):
- `g` reads V (both tables) but also E in `portevr`, `combien`, `que` (Bourdeau's note that g serves V, E and B).
- `9`/`q` read E (Tomokiyo), once B (`baille`, L01), as in Lasry's table.
- `zb` (z with a bar) opens the closing null run on L14 and reads as a null in L01 (`bai·lle`); value R in Tomokiyo.
- `4t` (4 with a crossed t) read ET (Tomokiyo's "et?"); S (Lasry's S) not excluded.
- L14 ends with Tomokiyo's nulls in order (m-x, circle with dot, t, bracket), as his table predicts.

## Not done (stopped at cap)
f.30r (35 lines) and f.30v (20 lines), item 22, are not reconciled: ciphertext.txt holds f.29r only. The next
worker should transcribe them the same way (reconciler reads against both tables, codes as in key.tsv), and should
not rerun shape-matching passes with this legend. A better blind-pass design would give the passes a legend cut from
f.29r itself (key.tsv codes, one glyph each from the full-resolution crops), since that hand is now identified.
