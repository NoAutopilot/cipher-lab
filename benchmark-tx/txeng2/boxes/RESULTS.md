# TXE2-BOXES: per-sign boxes for the sorter feed focus tiles (PREREG-txeng2-5 P1; 9 Oct 2026, 18:38-18:4x UTC by date -u)

LANE TX-ENGINEER-2, account 4, Opus worker. Brief `.claude/briefs/runs/2026-10-09-account4-txe2-round5.md` row TXE2-BOXES.
A product step, no experiment, no gate. **Read-free: no reader, no subagent, no vision call on a read, no host, no truth file
opened, no decision resolved, no cluster propagation, nothing published.** The only things taken from a line read (passZ)
are each focus tile's line and position and each line's position count. No value, no machine pick and no top-1 label is in
any sorter input: every boxed tile sits in one neutral pile `unsorted`; the question per tile is the feed's own (it names
the candidate piles in sorted order, never which one a read chose).

## Counts

| unit | tiles listed (feed focus) | tiles boxed (overlay check yes) | not boxed |
|---|---|---|---|
| birago1572-f152r | 4 | **4** | 0 |
| spinelli-c1519-confirm | 22 | **5** | 17 (overlay check no; reason per tile in `spinelli/boxes.tsv`) |
| total | 26 | **9** | 17 |

## Recipe (value-blind, named)

- **f152r: the atlas boxes already on the page** (`ciphers/nevers-birago-fr3251-1572/atlas/signs.tsv`, page f152r, 218
  boxes; `tools/glyph_atlas.py segment` default mode, the no.87 atlas recipe), on the same region image the f152r line
  crops came from. Atlas lines 3/4/5 = passZ L02/L03/L04 (lines 1-2 hold the plain text and L01). Before ordering by x:
  drop edge specks (w < 10 px at the region edges) and boxes under 0.65 x the page median sign height whose x-range overlaps
  a taller box (a tick or stroke fragment over/under a sign). Then box counts equal position counts on L02 (31/31) and L03
  (33/33), mapped by order; L04 (27 boxes / 25 positions) is **end-anchored**: its focus position 25 is the last position,
  mapped to the last box before the plain text that ends the line -- only that anchor is checked.
- **Spinelli: "atlas default segment on the line crops, joined at the overlap midpoint"**: `tools/glyph_atlas.py segment`
  (default mode = the no.87 atlas recipe: background-normalised binarisation, 8-connected components, x-overlap merge, marks
  above attached) on the 20 confirm line crops (`benchmark-tx/txeng/confirm/crops/p1c|p2c_Lnn_s1|s2.jpg`, the crops the
  passes saw; byte-different copies in `ciphers/spinelli-beinecke-c1515/images/` were not used), `--median-h 55` (the crops
  are speck-dominated: own median 4-7 px); then `spin_join.py`: keep an s1 box left of the s1/s2 overlap midpoint and an s2
  box right of it, drop boxes whose longer side is under 0.45 x 55 px, drop bleed-through (darkest 10% of the box lighter
  than 0.45 x the crop median grey), order by x. Line counts after the cut (boxes/positions): L01 23/20, L02 25/29, L03
  24/28, L04 35/29, L05 28/21, L06 26/26, L07 26/27, L08 21/21, p2c L01 26/32, p2c L02 16/19. A connected-component cut
  joins and splits this hand's signs, so a tile is mapped by order and kept **only where the overlay shows every box from
  the line start to the tile is one whole sign** (or the errors before it are visibly one speck plus one two-sign box, L05
  pos 10). A row-ink-profile column cut on the region images was tried first and dropped (box counts 13-18 per line against
  20-32 positions). One mark is unioned into its tile box on the check (p1c_L08_3, the ring above: `overlay_checks.tsv`
  union_k).

## Files (benchmark-tx/txeng2/boxes/)

- `<unit>/signs.tsv` (sid, page, x, y, w, h; `tools/sign_sorter.py --signs`), `<unit>/labels.tsv` (all `unsorted`),
  `<unit>/focus.tsv` (the feed's question rows for the boxed tiles), `<unit>/pages.txt` (the --pages argument:
  `ciphers/nevers-birago-fr3251-1572/atlas/pages.json` for f152r, `benchmark-tx/txeng/confirm/crops` for Spinelli, page =
  crop name), `<unit>/boxes.tsv` (per tile: line, position, box id, source crop/image, x, y, w, h, mapping, overlay check
  yes/no, note -- all 26 tiles).
- `overlays/` (2.4 MB, under 30 MB): f152r_L02-L04 and every Spinelli focus-line segment crop, every candidate box numbered,
  focus boxes thick with their position. `overlay_checks.tsv` holds the by-eye box check (segmentation only, no value).
- `build.sh` regenerates everything (`spin_join.py`, `build_boxes.py`; needs opencv-python-headless). Format check: both
  units built with `tools/sign_sorter.py --title T --signs --labels --pages --focus --no-preflight --no-register` into
  scratch: f152r 1 pile 4 tiles 0 skipped; Spinelli 1 pile 5 tiles 0 skipped (not committed, not published).

## Commits (sha256, first 16 hex)

Commit 04073a33b: f152r/boxes.tsv 8ba71cb88eefd964, f152r/focus.tsv 4add4aa793ad035b, f152r/labels.tsv e86ede788538e70f,
f152r/signs.tsv 5a03bb3624589b3f, spinelli/boxes.tsv 9cb544981f300962, spinelli/focus.tsv a90a29e177fe2c41,
spinelli/labels.tsv 6422eb6d5bfe51d2, spinelli/signs.tsv 14dafed5bc0b9216, overlay_checks.tsv aa5da6f27cf18374,
spinelli_lineboxes.tsv 8bb39403be4d0ae7, build_boxes.py da83099d54b7952a, spin_join.py 49b4eeb825ed2432, build.sh
bbec369d4f78908e.

## Gaps (one line each, not started)
- Spinelli 17 tiles unboxed: the cut needs a per-line segmentation this hand tolerates (a person's box pass in the sorter's
  recut, or a learned cut checked on an overlay); p1c L01 and p2c L02 also need a rule for the plain-text prefix / the
  left flourish before order mapping.
- No tool in tools/ was added or changed (target-local scripts only), so no SYSTEM.md or tool_shelf row.

Openings of eval truth: 0
