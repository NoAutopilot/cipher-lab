# TXE-T: audit the floor -- the 20 no.87 positions wrong in every pass, against the truth source (LANE TX-ENGINEER round 3; account 4, Opus 5.5; cap 6, box 75 min; read-free, no vision call)

Read `.claude/briefs/runs/2026-10-09-account4-txe-COMMON.md` first, then research/TX-TAXONOMY-2026-10-09.md section 1 ("The
floor": 20 of 803 scored positions wrong in all six full passes A, B, C, L, E, F; 9 read with the same sign by every reader),
`benchmark-tx/build_birago87.py` (how the truth was built: the clerk clear sheet of no.87, canvas 182, aligned sign by sign
in NEVBIR-87ALIGN, `ciphers/nevers-birago-fr3251-1572/harvest/align87/align_real.tsv`, forced through the printed 1572 key
plus the clerk C rows, with the key-conflict acceptances T95 s|l and T52 i|o and X_CE s) and the orchestrator's ask (ROOM
08:2x UTC 9 Oct): how many of the 20 are truth-doubtful (an alignment slip, a clerk-sheet reading, a homophone the key
list lacks) versus genuinely reader-wrong? If any are alignment slips the floor is lower than measured. This job writes a
FLAG column, never an edit to a truth file (CLAUDE.md: never edit a *.truth.tsv; a verifier decides).

## Do (read-free: scripts and your own eyes on the alignment tables; no model reads a crop)
1. List the 20 positions from `benchmark-tx/taxonomy/no87_positions.tsv` (err_A..err_F all 1) with: line, pos, plain,
   truth set, ref_sign, each pass's read, band_edge, stroke.
2. For each, trace the truth back: the `align_real.tsv` row (clerk letter, alignment op, any 1:2 / 2:1 chunking near it),
   the key rows that make the truth set (`harvest/key_1572_sheet.tsv`, clerk C rows, `sign_id_map_1572.json`), the clerk
   sheet's letter at that position as the alignment recorded it, and the atlas box (`atlas/signs.tsv`, `no87_box_token.tsv`
   -- this file carries truth; you may read it, you are the auditor). Classify each position as one of:
   `reader-wrong` (the alignment is clean, the clerk letter is clear, the key lists the sign for that letter, and every
   reader chose a sign the key gives another value), `alignment-doubtful` (a 1:2/2:1 chunk, an insertion/deletion within
   two positions, or a run where the clerk and the reads shift by one), `key-doubtful` (the readers' unanimous sign has no
   key value for the clerk's letter but the pair is a known conflict or a plausible unlisted homophone -- cite the
   conflict rows), `clerk-doubtful` (the clerk's letter at that position is itself questioned in align87 notes or
   contradicts the line's decoded word). Give the reasoning per position in one line.
3. Write `benchmark-tx/taxonomy/no87_floor_audit.tsv` (line, pos, plain, truth, unanimous_read, class, reason, source rows
   cited) and `benchmark-tx/taxonomy/FLOOR-AUDIT.md` with the class counts and the "floor if the doubtful ones are
   excluded" figure: err_true of L on the 803 minus the doubtful count (both numbers, never a replacement of the benchmark's).
4. Propose, do not apply: a `flag` column for `birago1572-no87.truth.tsv` listing the doubtful positions and their class,
   as a patch file `benchmark-tx/taxonomy/truth_flags_proposed.tsv` for a verifier; do not touch the truth file or
   BENCHMARK-TX.tsv.

## Report
Results-log row in research/TX-IDEAS-2026-10-09.md (id FLOOR; rebase before editing). No tool unless a helper is needed
(then add it to tools/tx_taxonomy.py as `--floor` with a test, not a private script). 0 vision calls, no host. Cap 6; stop at
80% of cap or box. Report in a short paragraph (first line: counts per class and the two floor figures) and stop.
