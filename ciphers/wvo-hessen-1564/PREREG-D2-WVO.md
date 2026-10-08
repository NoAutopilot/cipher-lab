# PREREG-D2-WVO -- per-row eye alignment of the 33 conflict/unaligned C tiles (f.23)

Written 8 Oct 2026, before any montage panel is built or looked at. Worker D2-WVO (account 2, LANE DEFAULT-account-2-20261008-0710).

Targets: the 33 tiles in `realign/tile_letters.tsv` with `grade_after` = C and `gloss_letter_realign` != `value_after`
(19 conflicts, 14 with no aligned letter). Image: `images/01109_p3_400full.jpg`; tile boxes from `sorter/signs.tsv`
(page x = 550 + x, page y = strip_y0 + y, `sorter/bands.tsv`).

Known-answer control (rule 3; it can differ from the target, since the reader does not know which panels are which):
10 decoy tiles drawn with `random.Random(1564).sample` from the 159 AGREE tiles (C, realign gloss letter = key value).
Decoys and targets are shuffled together (seed 1564) into one montage of 43 panels labelled P01-P43 only. Each panel:
the tile boxed in red, about 1.5 tile widths of context left and right, the German gloss row above it. No key value,
pile, gloss transcription or class is shown or given to the reader.

Reader: one Opus vision subagent call on the montage, blind (asked only "which letter of the German row stands directly
above the red box; '-' if none; '?' if illegible"), then this worker's own reconciliation against the same panels (2 units).

Classes per target tile (final = reconciled read):
- AGREE: read letter = `value_after` (the key value).
- CONFLICT: read letter is a definite other letter.
- NONE: '-' or '?'.

Gate: the eye read is usable only if the subagent's blind read matches the AGREE letter on >= 8 of 10 decoys.
Below 8/10: report the counts, no class used, "eye alignment non-test at this reader accuracy".

Key change rule (single leaf, so the rule-3 per-unit merge clause has one unit; it is applied as: no value enters
key.tsv from tiles that have not cleared this job's own decoy gate): a C key row changes value only if >= 2 target tiles
of that sign, in >= 2 different rows, are read CONFLICT with the same letter AND the decoy gate passes. Otherwise
findings are logged only; settled/key.tsv and the top-level key.tsv are not edited.

Reported figure: eye-adjusted AGREE = 159 + targets read AGREE (out of 257), beside 159/257, with the decoy score.
Out of scope: the crib-placement test.
