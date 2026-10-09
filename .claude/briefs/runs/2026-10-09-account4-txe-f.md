# TXE-F: per-cut quality gate (LANE TX-ENGINEER, idea O3 = owner's item 3; account 4, Opus 5.5; cap 8, box 100 min)

Read `.claude/briefs/runs/2026-10-09-account4-txe-COMMON.md` first, then `benchmark-tx/PREREG-txeng-2.md` (units, blindness,
Amendment: gate p < 0.01), then research/TX-IDEAS-2026-10-09.md row O3 and research/TX-TAXONOMY-2026-10-09.md. Why this
job exists: the owner asked (lane brief Amendment 1, item 3) for a classifier that labels every cut tile good / bad crop /
two signs joined / blot before any reader sees it, with the joined and bad-crop tiles re-cut and the blots dropped and
logged, and the gate measured on the benchmark truth. The taxonomy says where the mass is: on Birago no.87 the line band
cuts 14% of boxes (error 9.5% there vs 5.2% inside), the segmenter's 2:1 glued boxes are 3% of positions, and the 20 unanimous
wrong positions are in part shape ambiguities a crop cannot fix -- so the measured question is which flags predict a wrong
read, and whether a re-cut of the flagged tiles fixes any.

## Build `tools/tx_tile_gate.py` (subcommands score, recut; --help; test tools/tests/test_tx_tile_gate.py; disk only)
Inputs: `ciphers/nevers-birago-fr3251-1572/atlas/signs.tsv` (boxes, rh/rw/dy), `atlas/marks.tsv`, `atlas/bitmaps.npz`, the
page images (harvest `src_*.jpg`; origins per `tools/tx_taxonomy.py` load_geometry), the crop manifests
(`harvest/<leaf>/manifest.json` band boxes). Never `atlas/no87_box_token.tsv` (truth column) nor `labels.json` overrides.
1. `score --page f178v --out DIR/tiles.tsv`: per box, features computed from the page image: ink mass (ink pixels / box
   area), aspect (h/w), relative height and width (signs.tsv rh/rw), connected-component count inside the box at the page
   threshold, edge contact (share of the box perimeter touched by ink of the box's own component), band contact (the box's
   top or bottom outside its crop band: the tx_taxonomy `band_edge` cut rule), erosion share (`tx_taxonomy.erosion_share`,
   import it), neighbour touch (ink of the box's component extending into the neighbouring box), and a rule label fixed
   before any truth is opened: `joined` when width > 1.8 x the page median sign width with >= 2 ink valleys, `bad-crop`
   when band contact is cut or edge contact > 0.3, `blot` when ink mass > 0.6 with component count 1 and aspect within
   0.7-1.4 and height < 0.6 x median, else `good`. Print the label counts per page.
2. Gate measurement (opens truth; commit tiles.tsv first): map boxes to positions label-blind (sequence alignment to L by
   order and x as atlas/no87_map.py does; your own box_pos.tsv), then on dev_tune compare the flags with the positions L
   gets wrong (`tx_bench.position_errors` on labels_dev_tune.tsv): per label, flagged count, how many of L's 14 wrong
   positions it holds, precision and recall; the same for pass A's 24. Registered gate for the flags to be worth a re-cut:
   the non-good labels together hold >= 50% of L's wrong positions at <= 15% of positions flagged (write the number either
   way). Also report the same table on eval_heldout (read-free, no reader involved, so it costs no eval look -- say so).
3. `recut --labels joined,bad-crop`: for each flagged box, a re-cut tile: joined -> split at the deepest ink valley into two
   tiles; bad-crop -> the box grown to its own component's full ink extent plus 10%, taken from the page (not the band
   crop), with the neighbouring lines masked (`iiif_lines.py --mask-neighbours` logic; import or reuse, do not copy); blot
   -> dropped, logged with its features. Tiles at 2x with one neighbour of context each side, sheets of at most 24 rows,
   `DIR/<unit>/sheet_NN.png` + key TSV (row, line, pos, original L sign) not given to the reader.
4. If the gate in 2 is met on dev_tune: ONE Opus 5.5 reader call per dev sheet with the unchanged blind brief's sign sheet
   (`harvest/sign_sheet_blind_1572.png`) and the task "for each numbered row, the cell T## of the sheet that matches the boxed
   sign, or X_NEW / ?; row, sign_id, conf"; raw reads committed; `resolve` -> `benchmark-tx/outputs/birago1572-no87/
   passN_gate_dev_tune.tsv` (flagged positions take the re-read sign; others keep L). Score `tools/tx_bench.py ... --paired
   benchmark-tx/txeng/units/labels_dev_tune.tsv`; gate fixed > broken, p < 0.01. Met -> eval_heldout once (the eval look);
   not met -> FAIL, no eval. If the gate in 2 is NOT met: no read at all; the result is the flag table (a negative with
   numbers), and `recut` is still built and tested offline.

## Report
`benchmark-tx/txeng/gate/RESULTS.md`: label counts, the flag-vs-wrong table on dev (and eval, read-free), the read's lines if
taken, `tools/tx_taxonomy.py` on passN vs L (after the reads are committed), reader task text, calls. Shelf and SYSTEM rows
(grade from the result). One row in the Results log of research/TX-IDEAS-2026-10-09.md (id O3; rebase before editing).
Offline test: a synthetic page with a wide two-valley box (joined), a box cut by its band (bad-crop), a small round blob
(blot) and a normal sign (good): score labels each as named; recut splits the joined one into two and grows the cut one.
Vision calls: at most 2 dev + 2 eval x about 1.5; cap 8; stop before a call that crosses 80% of cap or box. Report in a
short paragraph (first line: the flag table's recall/precision and, if read, fixed/broken/p) and stop.
