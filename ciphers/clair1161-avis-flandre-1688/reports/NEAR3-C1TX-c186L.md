## NEAR3-C1TX-c186L (4 Oct 2026)

Account 2 worker for LANE-NEAR3, brief `.claude/briefs/runs/2026-10-04-ytbiz-near3-wave1.md`; clock 01:16 UTC at claim.
Written here, not in NOTES.md, per the brief (five clair1161 jobs in parallel); the lane folds it in.

**Leaf.** c186L = IIIF f187, left mounted leaf, native region 100,50,3400,2000 (ark btv1b90010063; NOTES.md "IMG-GALLICA1").
It is a whole short block, not only "the lower part" as IMG-GALLICA1 guessed from the thumbnail: **9 lines** of cipher
(2 lines, a gap, then 7 lines), no clear words, no heading or gloss visible in the region.

**Route and crop command** (pasted before any subagent call):
`python3 tools/iiif_lines.py --ark btv1b90010063 --canvas 187 --region 100,50,3400,2000 --out ciphers/clair1161-avis-flandre-1688/images --prefix c186L --bottom-margin 75 --debug`
found 10 bands, two of them wrong (a spurious band on the leaf's top edge, and the close-set first two lines -- pitch ~85 px
against ~140 px below -- merged into one centred on line 2's descenders). Re-cut from the cached source with centres read by
eye from the overlay: `... --centres 548,633,984,1126,1271,1394,1528,1668,1808 --top-margin 15 --bottom-margin 75
--max-width 1300 --overlap 100 --debug` -> 9 lines x 3 segments = 27 crops `images/c186L_L01..L09_s1..s3.jpg` + overlay
`images/c186L_lines_debug.jpg`, re-encoded JPEG q75 at the same dimensions (1.8 MB). The `src_*` native region was deleted
after cropping; its URL stays in `images/manifest.json` (each c186L entry carries a `source_file_note`). Stale manifest rows
from the first cut (L10) removed.

**Requests:** gallica.bnf.fr 1 (one native region, descriptive UA, no challenge). **Subagent calls (Sonnet): 2** (pass A,
pass B; each saw only the 27 crop paths and `tx/labels_v2.md`; B worked bottom-up). Reconciliation by this worker from 9
crop views (the third priced unit). Glyph atlas (TRANSCRIPTION.md step 2) not run: the brief names the line-read fallback
for this job; the family atlas belongs with the pooled job once all four leaves are cut.

**Signs and error.**

| | lines | signs | vs reconciled |
|---|---|---|---|
| pass A | 9 | 247 (raw) | 13/246 = 0.053 |
| pass B | 9 | 246 | 0/246 (see note) |
| reconciled `tx/c186L_rec.tsv` | 9 | **246** | -- |

**err_2reader = 13/248 aligned columns = 0.052** (`tools/reconcile_passes.py`, nw; 235 agree, 13 split; per line 0.889-1.000).
Below 0.10, so no look-alike pass was run. err_true not measurable: no benchmark item of this hand. Note: every one of the 13
splits was settled from the crop in B's favour (L05 col 8: B's extra `iii` kept), so "B vs reconciled = 0" is not an
independent accuracy figure; it says A's errors were mostly segmentation of compound signs (`z e` for one `K`, an extra `e`
after a `z`) and `z` for the blob-centred cross `dia` (3 of 13).

Settlements (line/col of `tx/c186L_rec/disagreements.tsv`): L01 9-10 `z e`->`K` (one sign); L01 26 A's extra `e` dropped;
L04 8 `e`; L04 24 `4`; L05 4 and 14 `dia`; L05 8 `iii` (the "um" after `to` = `w iii`, M); L06 4 `dia`; L06 20 `eloop` (same
shape as the agreed `eloop` later in the line, not `L`); L07 14 and L08 23 `iii` (three strokes with a bar; labels_v2 puts
barred and unbarred three-strokes under `iii` -- they may be two signs, see below); L07 21 `4` (M).

**Shapes outside labels_v2.**
- `s` (both passes wrote it as NEW: a small flat-topped s, mostly paired `s s` at line ends, and before `z` as `s z`):
  normalised to `s`, the symbol already in `tx/stream_all.txt` (21 occurrences) and `tx/c185R_rec.tsv`, which labels_v2's
  table omits. 7 occurrences (L01 x2, L04 x3, L05, L08).
- **`NEW1`** (provisional): a small v / rotunda hook followed by a long horizontal bar, `v—`. 3 occurrences: L03 col 1
  (line start), L05 col 5 (before `to`), L06 col 25 (before `eloop`); crops `c186L_L03_s1`, `c186L_L05_s1`/`s2`,
  `c186L_L06_s3`. It may be the `vdash` of c185R pass B (2 occurrences in stream_all, keyed `t` after READ2-C1161B) --
  not merged here; the pooled job or the sorter decides.
- For the split test / sorter: the three-stroke sign appears both bare (`iii`, L05, L07 col 13) and with a long bar through
  it (L07 col 14, L08 col 23); labels_v2 lumps them.

**Decode for information only** (`tx/c186L_decode_info.txt`, key.tsv as committed, ungraded, not a reading; NEW1 = `?`):
letter runs such as `aultres` (L01), `peuple` (L02), `princ` (L03), `port` (L04), `leurs` (L07), `encore`, `aussi` (L09)
appear unprompted; the rest is not word-segmentable. No judge run (not a reading).

**Not done:** no edit to `ciphertext.tsv`, `key.tsv`, `tx/stream_all.txt`, NOTES.md or NEAR.md (the pooled job merges);
no look-alike pass (err_2reader under 0.10).
