# H and Hx sheets: built for the record, NEVER read

The purity gate (PREREG-txeng4-1.md addendum) FAILED on parts (i) and (ii): 24 machine-agreed tiles on 13 of the 40 tokens,
7 tokens with 2 or more tiles. H and Hx did not run (declared non-test). These sheets were built after the gate, with the
patched tool (benchmark-tx/txeng4/1/glyph_atlas.patch) on the kept tokens.tsv, only to show what the pipeline produces on
this hand; no reader was given them. H/: `--from-tokens tokens.tsv --canonical-boxes glyphs/boxes_tomokiyo_v1.tsv
--canonical-dir sources/cryptiana/web --codes @codes40.txt --per 4 --spread --trim 0.2 --rows-per-sheet 10`; Hx/: the same
with `--shuffle-rows 20261012` (tiles_from column in sheet_hand.tsv names the row each tile came from).
