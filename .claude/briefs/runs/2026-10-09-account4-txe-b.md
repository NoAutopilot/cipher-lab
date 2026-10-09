# TXE-B: crop geometry (LANE TX-ENGINEER round 2, instrument B; account 4, Opus 5.5; cap 7, box 90 min)

Read `.claude/briefs/runs/2026-10-09-account4-txe-COMMON.md` first, then `benchmark-tx/PREREG-txeng-2.md` "Instrument B".
Why this job exists: a third of pass A's errors on Birago no.87 are pixels the reader never saw (research/TX-TAXONOMY-2026-10-09.md
class 2): the f.178r L03 tail (pos 24-34) slopes out of the fixed band and every blind reader deletes it; the line band cuts
14% of the hand's boxes top or bottom (error 9.5% there vs 5.2% inside; half of the d T18 / s T98 confusions sit on cut
descenders); and the pass brief says the s1/s2/s3 segments "overlap by about 100 px at 2x" while the manifest boxes overlap
425 native px (5-6 signs), which made the Fable reader de-duplicate by sequence and over-delete 10 signs on L01-L02.

## Build, as options on `tools/iiif_lines.py` (never a new crop script; test tools/tests/test_iiif_lines.py extended)
1. `--band-extent [FRAC]` (default 0.35): after line centres are found, each band's top and bottom edge is grown from the
   midpoint toward the neighbouring centre to the row-profile minimum, plus FRAC x pitch of margin, so descenders and
   ascenders stay inside; combined with `--mask-neighbours` so a grown band carries no neighbour-line ink. Band height is
   recorded in the manifest entry (`band_extent`).
2. `--check-boxes signs.tsv [--check-page NAME]`: read-free report, for the page's atlas boxes (`atlas/signs.tsv`, page
   coordinates = canvas minus the source region origin, see `tools/tx_taxonomy.py` load_geometry): share of boxes whose
   top or bottom lies outside their own band, and share of boxes whose centre line is another line but which lie inside
   this band. Printed and written to OUT/band_check.tsv. This is the dev gate; it never sees a truth file.
3. `--overlap-note`: from the manifest's segment boxes, the actual overlap in native px and in signs (page median box
   width from signs.tsv when given, else the ink-run median), written to OUT/crops_note.md as one sentence to paste into a
   pass brief ("segments of a line overlap by N native px, about k signs; a sign at the right edge of s1 and the left edge
   of s2 is ONE sign").
Source images are on disk: `harvest/f178r/src_*.jpg` (region origin 4700,3720 on canvas 181), `harvest/f178v/src_*.jpg`
(1703,848, canvas 182); use `--image FILE`, no fetch, no host. Old crop parameters are in each harvest manifest.json
(`centres_given`, box geometry); the earlier sloped re-crop of f178r L03 is in `harvest/f178r/slope/` (read its manifest for
the slope that worked; `--follow-slope`/`--deskew --only-lines 3` is the tool route).

## Dev gate, read-free (PREREG): on f178v, old bands cut 14% of boxes. With `--band-extent` (+ `--mask-neighbours`) the new
bands must cut <= 3% of the boxes and admit <= 2% other-line boxes (`--check-boxes atlas/signs.tsv`). Tune FRAC and the mask
on this number only. Record old and new figures in RESULTS.md.

## The one read (only if the dev gate is met)
Re-cut the geo unit into `benchmark-tx/txeng/geo/crops/`: f178r L01-03 (`--follow-slope` or `--deskew`, with `--band-extent`),
f178v L05, L10, L22 (`--band-extent --mask-neighbours`), same `--max-width` and segment layout as the originals (1250 px,
3 segments), `--overlap-note` on, `--debug` overlay checked by you before any read. ONE blind Opus 5.5 subagent pass over
these 18 crops with the unchanged `harvest/blind_pass_brief_1572.md` and `harvest/sign_sheet_blind_1572.png`, plus the
generated crops_note.md pasted after the brief (the only change to the reader's text; quote it in RESULTS.md). Pass A read
f178r in one call with f179r; keep to one call for all 18 crops (two if the first returns truncated). Raw read to
`benchmark-tx/txeng/geo/passH_raw.tsv`; commit and push before scoring. Normalise as `benchmark-tx/build_birago87.py` does
for pass A (line ids f178r_L01.. f178v_L05.., pos renumbered 1..n per line) into
`benchmark-tx/outputs/birago1572-no87/passH_geo.tsv`.

## Score (PREREG)
`tools/tx_bench.py passH_geo.tsv --bench BENCHMARK-TX.tsv --item birago1572-no87 --paired benchmark-tx/txeng/units/passA_geo.tsv`
(gate: fixed > broken, p < 0.05 against the same reader kind on the old crops) and `--paired .../labels_geo.tsv` (reported).
Registered predictions to check and state: the 8 L03 tail positions 24-34 deleted by A are read; the band-cut T18/T98/T76
positions on L05/L10/L22 move. Then `tools/tx_taxonomy.py` on passH vs A and L (after the read is committed) to name which
class moved. A gain here is a gain only on this unit (169 signs); say so.

Offline test: a synthetic page with two lines whose descenders cross the midpoint: `--band-extent` keeps every synthetic
box inside its band, `--check-boxes` reports 0% cut, and `--overlap-note` states the configured overlap. Shelf and SYSTEM
rows (grade from your own result). Vision calls: 1-2 Opus x about 1.5; cap 7; stop before a call that crosses 80% of cap or
box. Report in a short paragraph (first line: dev gate numbers and the paired fixed/broken/p) and stop.
