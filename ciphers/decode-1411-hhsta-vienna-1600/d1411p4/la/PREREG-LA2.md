# PREREG-LA2: per-number tile re-read of the p.4 4/5 forms (written 7 Oct 2026 01:0x UTC by date -u, before any tile is read)

Job D07-D1411 (LANE DEFAULT-account-1-20261007-0042). Re-run of R12A-D1411LA (PREREG-LA.md, cafba26e3/f376b6b96), whose
line-crop re-read was void (83/83 '?', reader could not see the digits). The scoring pre-registration PREREG-D1411P4.md
(afc9de42d) is re-used unchanged: same frozen tables (T21r, T21r_h12, T21r_h22), same de1600 coverage statistic, same
shuffled-target and shifted-table controls, same PASS rule, same letter and gloss tests. No control, gate or table is
changed after this file. Only the instrument changes:

1. Tiles: the same 83 numbers of la/tiles.tsv (same mask column). Each is cut on its own from its native-resolution line
   crop (images/d1411p4_crops/<line>.jpg, cut from IMG_R1411_I6598_P4.png at native resolution by iiif_lines.py in
   R12A-D1411P4), with x-ranges placed by the worker on a ruler overlay (la2/boxes.tsv; the worker places boxes, does not
   read shapes), a 12 px margin, full line height, enlarged 4x (LANCZOS) by la2/cut_tiles.py into la2/tiles/<line>_<pos>.png.
   A tile may include a neighbour's edge; the prompt names how many digits the target number has and which are masked.
2. Prompt (la2/prompt.md): same shape vocabulary as PREREG-LA (X cross, R r-form, O other digit, ?), value-blind: for each
   tile only the masked pattern (e.g. '#6', '##') is shown, never the committed value, a table, a gloss or a decode.
3. Pilot: 5 tiles (the first five rows of la/tiles.tsv in file order) in one Sonnet call. If 3 or more of the 5 come back
   with any '?', stop: the instrument is logged void at this resolution, no full read, no rescore.
4. Full read: the remaining 78 tiles, split into two Sonnet calls (~39 tiles each); the 5 pilot answers are kept as they are.
5. Rule (unchanged from PREREG-LA, tools/lookalike_pass.py's 2-of-3): a firm re-read (every '#' answered X/R/O, none '?')
   whose value equals pass A's or pass B's token settles the number at that value; otherwise UNSETTLED, keeps its committed
   value. X -> 4, R -> 5, O -> the committed digit. Grades unchanged (a settled number whose value changes stays M).
   Residual = unsettled / 83 (agreement, not error).
6. Output la2/numbers_la2.tsv; scored by la2/score_la2.py (score_p4.py with only input/output paths changed), seed 1411.
   Verdict read by the afc9de42d rule; the change against the committed T21r 0.581 is reported beside it, not as a gate.
   The number of changed values and the agreement of the re-read with pass A, pass B and the committed token are reported.
