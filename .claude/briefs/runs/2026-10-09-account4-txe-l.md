# TXE-L: read the signs out of order (LANE TX-ENGINEER, idea M7; account 4, Opus 5.5; cap 7, box 90 min)

Read `.claude/briefs/runs/2026-10-09-account4-txe-COMMON.md` first, then `benchmark-tx/PREREG-txeng-2.md` (units, blindness,
Amendment: gate p < 0.01) and research/TX-IDEAS-2026-10-09.md (row M7 and the Results log: nine instruments so far, none past
the gate; the recurring shape is that the reader's errors sit in the glyph, and every layout that showed it something
beside the glyph made it worse). Why this job exists: a line read carries a sequence prior -- the reader has seen the
neighbours and, even value-blind, tends toward a run that "looks like a line". The taxonomy's 34 agreed-wrong positions
(both readers, the same wrong sign) and the 20-position floor may be partly sequence-driven. A read of the SAME tiles in a
seeded shuffled order, with no neighbours, has no sequence to lean on; if it fixes more than it breaks against the in-order
read of the same tiles, the prior is a cause; if it breaks more, context is doing work the floor needs.

## Pre-registration (write `benchmark-tx/txeng/shuffle/PREREG.md` and push it BEFORE any read)
- Tiles: every mapped box of dev_tune (f178v L01-12; `tools/tx_compare.py map` for the label-blind box<->position map;
  never no87_box_token.tsv's truth), cut from the page at the box grown 25% (no neighbour), scaled so the sign is about
  90 px tall (TXE-A's ctx rule), autocontrast. Two arms, the SAME tiles: (a) in line order, 24 tiles per sheet with the
  line id and position printed under each; (b) seeded shuffled order across the whole unit, 24 per sheet, each tile labelled
  only by a running number; the number -> (line, pos) key written to `benchmark-tx/txeng/shuffle/key.tsv`, never given to
  the reader. Sheets: `benchmark-tx/txeng/shuffle/{ordered,shuffled}/sheet_NN.png` (about 15 sheets per arm for ~340
  tiles -- too many at 1.5 a call: SUBSAMPLE. Take the 8 dev lines with the most A/B disagreements (passC_agreement.tsv),
  which is about 230 tiles = 10 sheets per arm; state the lines in PREREG).
- Reader: one Opus 5.5 subagent call per sheet, with `harvest/sign_sheet_blind_1572.png`, task "for each numbered tile the
  sheet cell T## that matches, or X_NEW / ?; tile, sign_id, conf". Raw reads committed per arm before scoring.
- Resolve: per arm, `benchmark-tx/outputs/birago1572-no87/passT_ordered_dev.tsv` and `passT_shuffled_dev.tsv` (line, pos,
  sign for the subsampled lines; unmapped positions take L's sign and are listed).
- Gate (fixed now): primary, shuffled vs ordered paired on the same positions (`tools/tx_bench.py passT_shuffled_dev.tsv
  --paired passT_ordered_dev.tsv`): fixed > broken, p < 0.01 means the sequence prior hurts; broken > fixed at p < 0.01 means
  context helps (also a finding: the floor needs context, not less of it). Secondary, each arm vs
  `benchmark-tx/txeng/units/labels_dev_tune.tsv` and vs passA_dev_tune.tsv. No eval look unless the primary gate is met in
  the "shuffled fixes" direction AND the shuffled arm beats L on dev (p < 0.01); then eval_heldout once, both arms.
- Report the 34 agreed-wrong-class positions separately (positions where A and B read the same wrong sign, from
  benchmark-tx/taxonomy/no87_positions.tsv -- open it only after both arms' reads are committed): how many does each arm
  get right?

## Report
`benchmark-tx/txeng/shuffle/RESULTS.md`: the gate lines, per-arm err_true, the agreed-wrong table, `tools/tx_taxonomy.py` on
both arms vs L (after commit), reader task text, calls (about 20 Opus). Tool: the sheet builder as a subcommand of
`tools/tx_compare.py` (`tiles --order ordered|shuffled`) or `tools/tx_tile_sheets.py` with --help and an offline test; shelf
and SYSTEM rows (grade from the result). Results-log row in research/TX-IDEAS-2026-10-09.md (id M7; rebase before editing).
Cap 7 at about 1.5 a call means roughly 4 sheets per arm fit inside 80% of cap: if the subsample still needs more than 4
sheets per arm, cut to the 4 lines with the most disagreements and say so in PREREG before any read. Stop before a call
that crosses 80% of cap or box. Report in a short paragraph (first line: shuffled vs ordered fixed/broken/p, each arm vs L) and
stop.
