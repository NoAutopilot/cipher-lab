# TXE-N: a second crop set shifted half a line, read only where the two sets disagree (LANE TX-ENGINEER, idea M20; account 4, Opus 5.5; cap 8, box 100 min)

Read `.claude/briefs/runs/2026-10-09-account4-txe-COMMON.md` first, then `benchmark-tx/PREREG-txeng-2.md` (units, blindness,
Amendment: gate p < 0.01), `benchmark-tx/txeng/geo/RESULTS.md` and `RESULTS-B2.md` (crop geometry is the one instrument that
moved: `--band-extent 0.1 --mask-neighbours` + `--follow-slope` on f178r L03, pooled 27/8 p 0.0019 on the geo unit, with the
gain on the sloped tail and the f178v band-cut lines unmoved) and research/TX-IDEAS-2026-10-09.md row M20. Why this job
exists: the brief's own idea -- two crop sets with boundaries shifted by half a line give every sign one rendering where it
is central and one where it sits at a band edge; where the two reads disagree, the position is doubtful by construction
(not by a model's say-so), and only those positions get a third look. This extends the one instrument that worked to the
band-cut class it did not move.

## Pre-registration (write `benchmark-tx/txeng/shift/PREREG.md` and push it BEFORE any read)
- Crop sets on dev_tune (f178v L01-12, harvest/f178v/src_*.jpg, `--image`, no fetch): set S0 = the TXE-B geometry
  (`--band-extent 0.1 --mask-neighbours`, 1250-px segments, 3 per line, `--overlap-note`); set S1 = the same with every
  band boundary shifted by half a pitch AND every segment boundary shifted by half a segment (`iiif_lines.py --shift-bands
  0.5 --shift-segments 0.5`, new options with tests; S1's bands are centred on the gaps, so each S1 crop holds the lower
  half of one line and the upper half of the next -- state in the brief that the reader transcribes the FULL line whose
  centre is marked, and mark it with a tick in the margin). Check both debug overlays before any read; `--check-boxes
  atlas/signs.tsv` for both sets, read-free.
- Reads: one blind Opus 5.5 pass per set (two calls each, L01-06 and L07-12), the unchanged brief + sheet + the generated
  crops notes. Raw reads committed per set; normalise -> `benchmark-tx/outputs/birago1572-no87/passV_s0_dev_tune.tsv`,
  `passV_s1_dev_tune.tsv`.
- Reconcile: `tools/reconcile_passes.py passV_s0 passV_s1` (its disagreements.tsv = the doubtful positions); the third
  look = ONE Opus call on the disagreement positions only, each shown as BOTH crops' windows side by side (4x, one neighbour
  each side), question "which of the two readings, a third cell, or ?"; resolve -> `passV_shift_dev_tune.tsv` (agreed
  positions keep the agreed sign; disagreements take the third look). Count the disagreements and the third look's picks.
- Gate (fixed now): `passV_shift_dev_tune.tsv --paired benchmark-tx/txeng/units/passA_dev_tune.tsv` fixed > broken, p <
  0.01 (the same reader kind on the old crops); vs labels_dev_tune.tsv reported; also S0 alone vs A (this is the geometry
  instrument's own dev read, which TXE-B never took on dev_tune -- report it as such) and S1 alone vs A. Met -> eval_heldout
  once (the eval look). Not met -> FAIL, no eval. Also report the band-cut positions (tx_taxonomy band_edge cut, after
  commit): wrong in A / S0 / S1 / shift.

## Report
`benchmark-tx/txeng/shift/RESULTS.md`: the check-boxes tables, the gate lines, the disagreement count and third-look table,
the band-cut table, `tools/tx_taxonomy.py` on the shift read vs A and L, reader task texts, calls (about 5 Opus). Tool
options on `tools/iiif_lines.py` with tests; shelf and SYSTEM rows (grade from the result); Results-log row in
research/TX-IDEAS-2026-10-09.md (id M20; rebase before editing). Vision calls: dev 5, eval 5 at most; cap 8; stop before a
call that crosses 80% of cap or box. Report in a short paragraph (first line: shift vs A fixed/broken/p, S0 vs A, S1 vs A,
disagreement count) and stop.
