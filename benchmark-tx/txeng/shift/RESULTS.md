# TXE-N results: a second crop set shifted half a line and half a segment, third look only where the reads disagree (M20)

LANE TX-ENGINEER, account 4, Opus 5.5; 9 Oct 2026, 08:00-08:2x UTC by date -u. Brief
`.claude/briefs/runs/2026-10-09-account4-txe-n.md`; pre-registration `PREREG.md` (pushed dfe56d060 before any read; binds with
`benchmark-tx/PREREG-txeng-2.md`, gate p < 0.01).

**Verdict: FAIL on the registered dev gate; no eval read (looks 0).** shift vs pass A on dev_tune (343 signs): fixed 13 /
broken 7, p 0.263 (err 0.070 -> 0.055). S0 alone vs A 9 / 8, p 1.0 (err 0.070 -> 0.070). S1 alone vs A 15 / 9, p 0.31
(err 0.055). The reads agree on 95.2% of columns; 17 disagreements, which hold 9 of S0's 22 errors -- the other 13 S0 errors
are the same wrong sign in both reads, invisible to a disagreement filter by construction.

## Crop sets (read-free checks, before any read)
- S0 (`s0/`) = the TXE-B geometry (`--band-extent 0.1 --mask-neighbours`, 1250 px, 3 segments, overlap 425 px).
- S1 (`s1/`) = the same with `--shift-bands 0.5 --shift-segments 0.5` (new options on `tools/iiif_lines.py`, test item 9):
  bands down 68 px (half of pitch 137), the mask keeps the own and next line whole, a red triangle in a 40 px white margin
  marks the line to read; cut points moved 412 px, 4 segments (838, 1250, 1250, 838 px), overlap 425-426 px.
- Commands: `s0/cmd.log`, `s1/cmd.log` (the command lines are in PREREG.md).

| set | f178v boxes | cut (ink rule) | admitted to another band | note |
|---|---|---|---|---|
| S0 | 675 | 4 (0.6%) | 9 (1.3%) | = TXE-B |
| S1 | 675 | 13 (1.9%); 1 on L01-12 | 646 (95.7%) | by design: each S1 crop carries the next line; the marker says which to read |

Both debug overlays (`s*/f178v_lines_debug.jpg`) and one S1 crop (L05_s2) were checked by eye before the reads.

## Reads (4 blind Opus 5.5 calls, value-blind)
- Task texts: `s0/reader_task_01-06.md`, `s0/reader_task_07-12.md`, `s1/reader_task_01-06.md`, `s1/reader_task_07-12.md`.
  Each is the unchanged `harvest/blind_pass_brief_1572.md` + the set's generated `crops_note.md` + sheet + crop list +
  output path. The subagent prompt: "Your complete task is written in <task file>. Read that file first and follow it
  exactly. Open no file other than that task file, the sign sheet and the crop images it names; write only the one TSV it
  names."
- Raw reads `s0/passV_s0_raw_*.tsv` (353 signs), `s1/passV_s1_raw_*.tsv` (354), committed before any score. Normalised (line
  `f178v_Lnn`, pos, sign = sign_id, every row kept) -> `benchmark-tx/outputs/birago1572-no87/passV_s0_dev_tune.tsv`,
  `passV_s1_dev_tune.tsv`.
- One S1 reader joined the four segments into one strip itself (in its scratchpad) before reading; it reports overlaps of
  852/848/852 px at 2x, matching the note.

## Reconcile and third look
- `tools/reconcile_passes.py passV_s0 passV_s1 --out-dir recon/`: 338/355 columns agree (95.2%), **17 disagreements**
  (14 substitutions, 3 indels) -- `recon/disagreements.tsv`.
- `tools/tx_shift_look.py build` (new tool, test `tools/tests/test_tx_shift_look.py`): the same NW alignment, one row per
  disagreement, view a = S0 crop window, view b = S1 crop window, +-130 px around the position estimated from the atlas
  boxes' geometry, +-110 px tall, 4x, red caret; options 1/2 seeded order (seed 20, `look/key.tsv`); neighbours = the
  nearest agreed signs. Sheet `look/sheet_01.md`, rows `look/rows/`, task text `look/reader_task.md`.
- **Deviation from PREREG:** 17 rows exceed one 16-row sheet. The brief allows dev 5 vision calls (4 reads + ONE third
  look), the PREREG's "sheets of 16, at most 3 calls" contradicted that; one call was made, and row 17 (L12 col 4, S0 T51 /
  S1 gap) kept the S0 reading as the PREREG's overflow rule says.
- Picks (`look/answers_01.tsv`, `look/picks.tsv`): option for S0 9, for S1 7, a third cell 0, ? 0; overflow 1 -> S0.
- On the 14 scored disagreement positions: S0 wrong 9, S1 wrong 4, shift wrong 4.

| line.pos | truth set | S0 | S1 | shift | band edge (A's crops) |
|---|---|---|---|---|---|
| L01.3 | T13/T51/T58/T95 | T51 | T95 | T51 | cut |
| L01.8 | T13/T51/T58/T95 | T51 | T95 | T51 | cut |
| L01.13 | T26 | T26 | T76 | T76 | cut |
| L01.23 | T57/T92/T95/T98/X_CE | T50 | T92 | T92 | in |
| L01.26 | T13/T51/T58/T95 | T13 | T64 | T13 | in |
| L03.4 | T57/T92/T95/T98/X_CE | T50 | T92 | T50 | in |
| L04.4 | T57/T92/T95/T98/X_CE | T50 | T92 | T92 | in |
| L05.7 | T17/T42/T54 | X_NEW | T51 | X_NEW | in |
| L05.25 | T57/T92/T95/T98/X_CE | T50 | T92 | T50 | in |
| L06.23 | T25/T52/T80/T96 | (deleted) | T80 | T80 | in |
| L07.13 | T36/T50 | T27 | T36 | T36 | cut |
| L10.22 | T60/T76 | T60 | T86 | T60 | - |
| L10.31 | T36/T50 | T18 | T36 | T36 | cut |
| L11.5 | T45/T66/T86 | T76 | T66 | T66 | cut |

**Third-look reader slips (found after scoring, not used for the gate):** rows 6 (L03.4) and 10 (L05.25) were answered
"2" with the note "C-with-inner-loop omega form, as row 16's T92 neighbour", but option 2 on those rows was T50 (the order is
seeded per row); the note and the pick disagree. Resolved by the note, the shift read would be 15 wrong (fixed 15 / broken 7
vs A, p 0.13 by the same test) -- still a FAIL at p < 0.01; recorded only as a layout lesson (put the cell id beside the
option number in the answer, or ask for the cell id, not the number). The reader also says six rows were decided by the
neighbour labels in the table (agreed reader readings, not truth) rather than by the sheet: the neighbour column works as
an exemplar, which the layout did not intend.

## Score (tx_bench, after every dev read was committed and pushed)
```
birago1572-no87 [eval] err_true 0.055 (19/343) 95% 0.036-0.085 | wrong 17 deleted 0 inserted 2 | excluded 11 | lines missing 17
paired passV_shift_dev_tune.tsv vs passA_dev_tune.tsv on birago1572-no87: 343 common scored signs; base wrong 23, output wrong 17; fixed 13, broken 7; sign test p = 0.2632
paired passV_shift_dev_tune.tsv vs labels_dev_tune.tsv on birago1572-no87: 343 common scored signs; base wrong 14, output wrong 17; fixed 6, broken 9; sign test p = 0.6072
birago1572-no87 [eval] err_true 0.070 (24/343) 95% 0.048-0.102 | wrong 21 deleted 1 inserted 2 | excluded 11 | lines missing 17   (S0)
paired passV_s0_dev_tune.tsv vs passA_dev_tune.tsv on birago1572-no87: 343 common scored signs; base wrong 23, output wrong 22; fixed 9, broken 8; sign test p = 1.0000
paired passV_s0_dev_tune.tsv vs labels_dev_tune.tsv on birago1572-no87: 343 common scored signs; base wrong 14, output wrong 22; fixed 4, broken 12; sign test p = 0.0768
birago1572-no87 [eval] err_true 0.055 (19/343) 95% 0.036-0.085 | wrong 17 deleted 0 inserted 2 | excluded 11 | lines missing 17   (S1)
paired passV_s1_dev_tune.tsv vs passA_dev_tune.tsv on birago1572-no87: 343 common scored signs; base wrong 23, output wrong 17; fixed 15, broken 9; sign test p = 0.3075
paired passV_s1_dev_tune.tsv vs labels_dev_tune.tsv on birago1572-no87: 343 common scored signs; base wrong 14, output wrong 17; fixed 6, broken 9; sign test p = 0.6072
paired passV_s1_dev_tune.tsv vs passV_s0_dev_tune.tsv on birago1572-no87: 343 common scored signs; base wrong 22, output wrong 17; fixed 8, broken 3; sign test p = 0.2266
```
S0 alone vs A is the geometry instrument's own dev read (TXE-B never read dev_tune): 9 / 8, no movement off the sloped tail.

## Band-cut positions (tx_taxonomy band_edge = cut on A's crops; 57 of 343)
| A | S0 | S1 | shift | L |
|---|---|---|---|---|
| 5 | 5 | 3 | 3 | 5 |

## Taxonomy (`tools/tx_taxonomy.py`, A, S0, S1, shift, L; `taxonomy_dev.tsv`, `taxonomy_dev.md`)
- Wrong-or-deleted: A 23, S0 22, S1 17, shift 17, L 14. Unanimous A&S0&S1 wrong: 8.
- Band cut: 5/5/3/3/5 (above). Segment overlap: A 4, S0 5, S1 3, shift 3, L 2. Thin tercile: A 12, S0 10, S1 7, shift 8, L 6.
- S0 and S1 share 14 errors, 13 with the same wrong sign: look-alike misreads (class 1: T64 for l x4-5, T50 for the omega
  family) that no crop placement changes; the disagreement filter cannot see them.

## Predictions
1. S0 alone vs A, small or no gain: HOLDS (9/8).
2. Disagreements 8-15% of positions, holding more than half of S0's errors: DOES NOT HOLD (4.8%, 9 of 22).
3. The third look fixes more than it breaks on the disagreements: HOLDS (S0 9 wrong -> 4), but the gain over A is 13/7,
   p 0.26, and the shift read equals S1 alone (17 wrong each): the third look added nothing over simply taking S1.

## Calls and cost
5 Opus vision calls (4 reads about 127-150k subagent tokens each, 1 third look about 146k); 0 eval calls; 0 hosts.

## Follow-ups (one line each, not started)
- S1 alone (marked line at the top edge, next line visible) beat S0 by 8/3 on the same reader kind; whether "the next line in
  view" or "the marked line off-centre" helps is a read-free-designable question for the lane, not tested here.
- A third-look layout should take the answer as a cell id, not an option number (the two slips above).
