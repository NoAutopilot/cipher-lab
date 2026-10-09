# PREREG-UNA-PISA (9 Oct 2026, written 06:47 UTC by date -u, before any tile is shown to a reader)

Job: UNA-PISA, brief .claude/briefs/runs/2026-10-09-account4-orch-unassigned-jobs.md. Target: key86 cells T45 (o), T47 (m), T57 (la);
hypothesis from PIS1-KEY's retired remap and PIS1-302's witnesses: the page signs carrying these labels on f.275r/f.301v/f.302v are
T45 -> u, T47 -> f, T57 -> n. A per-token crop compare can say which *table cell* a page sign looks like; it can show a transcription
label slip (the sign is really another cell), it cannot show that the table copy gives a cell the wrong value.

## Material (disk only, no network)
- Table cells: 22 cells of sources/cryptiana/web/henryiii_Vivonne5.png (688 px copy) cut with tools/iiif_lines.py at key86 cell_xy
  (command pasted in NOTES): the target cells T45 T47 T57; every other cell whose value is one of o, m, u, f, n (T13 T33; T11 T31; T19 T38
  T46 T51; T06 T27 T42; T12 T32 T48); and the control cells' own and look-alike cells T36 T17 T49 (s) and T16 T35 (r). Shown 4x under
  neutral letters A-V in a seeded shuffle (seed 20261009); the map stays in una_pisa/cells_map.tsv, never shown to the reader.
- Known-answer tiles (5; the cell is settled at C on these pages by an earlier job, crops already committed and located):
  K-T36a f.275r L09 i3 (pis2/tok, R12A-PISRS C), K-T36b f.275r L14 i28 (same), K-T17 f.302v L02 i16 (pissd S1, C), K-T16 f.302v L02 i15
  (pissd M1, C), K-T46 f.302v L03 i6 (pissd Y1, C). Answer = the tile's own cell (T36, T36, T17, T16, T46).
- Target tiles: every T45/T47/T57 token in reading_f275r_tokens.tsv (17), reading_f301v_tokens.tsv (15), reading_f302v_tokens.tsv (10),
  located by eye on line strips (una_pisa/strips.py, una_pisa/ruler.py is a locating aid only), PIL crops at full strip height.
  A token not located with confidence is excluded and listed.

## Staging (cost control; decided before any reply)
- Stage 1 (call 1): the 5 known-answer tiles alone, under shuffled ids, against the 22-cell sheet. One blind Opus call. The reader
  gets no key values, no copy text, no transcription labels, and is not told any tile has a known answer.
- Gate GK: known-answer tiles whose best cell is the tile's own cell >= 4 of 5 (D07-PIST40's control shape). A reply naming a
  different cell of the same value (e.g. T49 for a T36 tile) is a miss.
- If GK FAILs: the run is a NON-TEST. No target tile is cut or shown. Logged: the 688 px table copy is not discriminating for these
  cells either (Opus reader, 22-cell set); the only reopener is a higher-resolution key witness. Stop.
- If GK PASSes: stage 2, one blind Opus call per page (<= 2 more calls, cap permitting), each with that page's target tiles mixed with
  the same 5 known-answer tiles re-shuffled (seed 20261009 + page index), same sheet. GK is re-applied per call; a page call whose
  controls miss GK is a non-test for that page.
- Stage 2 rule per target token: SETTLED-<cell> when the reader's best cell is given at medium or high confidence; else UNSETTLED.
  A token SETTLED to a cell other than its label is a label-slip candidate. A key-cell correction is a candidate only if >= 3 tokens of
  one label settle on one other cell of the hypothesised value (T45 -> a u cell, T47 -> an f cell, T57 -> an n cell) and none settle on
  the labelled cell; it is then tested as its own pre-registered kp86 re-score with the shuffled-key control (separate PREREG), never
  applied here.
- Nothing in key86.tsv, the transcriptions, readings or grades changes in this job.

## Scorer
una_pisa/una_pisa.py parses the verbatim replies (una_pisa/blind/reply_*.txt) by the format the prompt asks for and writes
una_pisa/result.tsv; `--check` exits non-zero if result.tsv is stale.
