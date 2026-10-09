# TXE-B results: crop geometry (LANE TX-ENGINEER round 2, instrument B; 9 Oct 2026, 07:15-07:3x UTC by date -u)

Brief `.claude/briefs/runs/2026-10-09-account4-txe-b.md`; pre-registration `benchmark-tx/PREREG-txeng-2.md` "Instrument B".
Taxonomy class addressed: 2 (crop geometry), `research/TX-TAXONOMY-2026-10-09.md`.

**Verdict: FAIL on the registered gate.** The read-free dev gate was met. On the geo unit (169 signs), pass H vs pass A:
fixed 12, broken 4, two-sided sign test p = 0.0768. The gate needs p < 0.05. err_true fell from 0.136 to 0.089, the same
error count as L (today's best). A gain here would count only for this unit, and the paired test does not establish one.

## Tool (tools/iiif_lines.py, test tools/tests/test_iiif_lines.py, all pass)
- `--band-extent [FRAC]` (default 0.1): each band edge moves from the midpoint to the row-profile minimum when that lies
  farther out, then grows FRAC x pitch, clamped to the neighbouring centre. Manifest key `band_extent`. On a sloped cut, the
  strip's half-height is the larger of the band's two reaches from its centre.
- `--check-boxes signs.tsv [--check-page P] [--check-only]`: a read-free report written to OUT/band_check.tsv. It has two
  rules. The **ink rule** applies to fixed bands: it simulates each band's crop on the page pixels with the real
  `--mask-neighbours` component mask. A box is cut when under 90% of its ink survives in its own band. A box is admitted
  to another band when at least `--mask-keep` of its ink survives there. The **box rule** (box height as a proxy) applies
  to sloped bands, on the fit each crop was cut on.
- `--overlap-note [--note-scale K]` writes one sentence per prefix to OUT/crops_note.md. It gives the real segment overlap
  in native px, in the reader's image px, and in signs.
- Changes made along the way, all needed for a clean crop:
  - `--mask-neighbours` now whitens a 2 px rim around each removed component and fills with the local paper shade (the mean
    of non-ink pixels within 20 px). Before this, the removed neighbour ink left ghost outlines and white silhouettes on
    shaded paper, which a reader could take for signs (seen on f178r).
  - `--debug` draws the sloped strips in green.
- **Deviation from the PREREG:** the default FRAC is 0.1, not 0.35. At 0.35 the grown bands admitted 34% of other-line
  boxes on f178v.

## Read-free dev gate (f178v, 675 atlas boxes; gate: cut <= 3%, admitted <= 2%)

| bands | ink rule cut | ink rule admitted | box-proxy cut | box-proxy admitted |
|---|---|---|---|---|
| old midpoint bands (as cut 2 Oct) | 7.7% (52) | 0.1% (1) | 17.3% (117) | 0.0% |
| `--mask-neighbours` only | 1.6% (11) | 0.4% (3) | 0.1% | 0.0% |
| `--band-extent 0.05 --mask-neighbours` | 0.7% | 0.9% | 0.1% | 0.6% |
| **`--band-extent 0.1 --mask-neighbours` (chosen)** | **0.6% (4)** | **1.3% (9)** | 0.0% | 1.9% |
| `--band-extent 0.15 --mask-neighbours` | 0.6% | 2.4% | 0.0% | 2.5% |
| `--band-extent 0.35 --mask-neighbours` | 0.3% | 34.1% | 0.0% | 37.5% |

- **How the configuration was chosen:** the lowest cut that still meets the admitted gate, tuned on this table only, before
  any read.
- **Why the old figure differs from the taxonomy's 14%:** the taxonomy counted mapped token positions with the box rule.
  This table counts all atlas boxes. The box proxy overstates cuts, because a box edge a few px out that carries little
  ink still counts as cut.
- **What the mask alone shows:** `--mask-neighbours` alone already passes, so most of the gain comes from the existing mask
  (its margin keeps a descender whole). `--band-extent` adds a further 1.0 point off the cut at the cost of 0.9 point
  more admitted.
- **Files:** `gate_old/`, `gate_new/`.

**f178r is not checkable by the box rule.** The atlas's line labels on f178r follow fixed y, so on the sloping right half:
- its line 1 carries the prose above ("magno ... strepito");
- its line 2 is line 1's continuation;
- its line 3 interleaves line 2's continuation with the line-3 tail.

The 34% "cut" there is the atlas, not the crop. The f178r cut was checked by eye on `crops/f178r_lines_debug.jpg` (green
strips) and on a contact sheet: three lines, each whole in its strip, and the L03 tail level in s3.

## The read (one call)
- **Crops:** `crops/` (commands in README.md). f178r L01-03 were cut with `--deskew 300 --slope-local --band-extent 0.1
  --mask-neighbours`, and f178v L05/L10/L22 with `--band-extent 0.1 --mask-neighbours`. All use 1250 px and 3 segments,
  the original layout. The reader saw 2x LANCZOS PNGs (`crops2x/`, gitignored), as `harvest/make_2x.py` made them for
  pass A.
- **Reader:** one blind Opus 5.5 subagent (`model: opus`), 18 crops in one call, not truncated. Raw read is
  `passH_raw.tsv` (187 rows), committed and pushed before scoring. Normalised output is
  `benchmark-tx/outputs/birago1572-no87/passH_geo.tsv`.
- **Task text:** in full in `reader_task.md`. It is the unchanged `harvest/blind_pass_brief_1572.md`, followed by the
  generated crops_note.md (quoted below), the sheet path, the 18 crop paths and the output path.
- **Reader's own report:** 187 signs; 9 X_ rows (1 X_K, 2 X_S, 6 X_NEW); no `?` rows. Hardest pairs were T60/T86,
  T45/T90, T51/T95, T52/T56 and T18/T36/T65.

Crops note as pasted:
> - f178r: segments of a line overlap by 350 native px (the images you read are at 2x, so 700 px in each image), about 6 signs (median sign width 60 px, from the atlas boxes); a sign at the right edge of s1 and the left edge of s2 is ONE sign: the last 700 px of s1 and the first 700 px of s2 show the same ink, read it once.
> - f178v: segments of a line overlap by 425 native px (the images you read are at 2x, so 850 px in each image), about 6 signs (median sign width 66 px, from the atlas boxes); a sign at the right edge of s1 and the left edge of s2 is ONE sign: the last 850 px of s1 and the first 850 px of s2 show the same ink, read it once.

(The unchanged brief above it still says "about 100 px at the 2x scale" and "f.178v, a page that is cipher throughout",
as it did for pass A.)

## Score (tx_bench)
```
birago1572-no87 [eval] err_true 0.089 (15/169) 95% 0.054-0.141 | wrong 15 deleted 0 inserted 0 | excluded 19 | lines missing 23
paired passH_geo.tsv vs passA_geo.tsv on birago1572-no87: 169 common scored signs; base wrong 23, output wrong 15; fixed 12, broken 4; sign test p = 0.0768
paired passH_geo.tsv vs labels_geo.tsv on birago1572-no87: 169 common scored signs; base wrong 15, output wrong 15; fixed 5, broken 5; sign test p = 1.0000
```
Pass A on its own: err_true 0.136 (23/169), 15 wrong and 8 deleted.

## Registered predictions
1. **The 8 L03 tail positions (24-34) that A deleted are read: HOLDS.** All 8 were read (deletions 8 -> 0) and 5 of them
   correctly (pos 24, 25, 26, 30, 33). Pos 31, 32 and 34 were read wrong (T27, X_NEW and T90).
2. **The band-cut T18/T98/T76 positions on L05/L10/L22 move: DOES NOT HOLD.** On the 14 positions the old bands cut, A
   was wrong at 5 and H is wrong at 5: fixed 1 (L10.31, T98 -> T36), broken 1 (L22.11, T27 -> T76). L05.1 and L10.4 stay
   wrong: A, H and L all read T76 at L10.4, and H reads X_NEW at L05.1.

## Which taxonomy class moved (`tools/tx_taxonomy.py`, A vs H vs L; `taxonomy_geo.tsv`, `taxonomy_geo.md`)
- **Class 2a, deletions and "pixels never seen" on f178r L03, moved.** Line-index L+3 (f178r L03) went from 10/31 wrong
  in A to 4/31 in H. The deletions went from 8 to 0.
- **Class 2b, band-cut descenders on f178v, did not move.** At the old band-cut positions the error rate is 35.7% in A,
  H and L alike. Those errors are look-alike misreads of a sign now fully visible, not missing pixels.
- **Class 2c, overlap de-duplication:** no deletions in H. In the overlap zone H has 2 errors against A's 1.

## Calls and cost
1 Opus vision call (about 134k subagent tokens). No hosts were contacted: every image came from disk.

## Follow-ups (one line each, not started)
- Make `--check-boxes` able to judge f178r: the atlas's line labels on sloped leaves are not usable for it, so the boxes
  need re-labelling by the slope fit first (a `glyph_atlas.py` change, not this instrument).
- Test whether the gain survives on more than this unit: the 12/4 split on 169 signs comes almost wholly from the L03
  tail. A second sloped-tail unit (another leaf with a sloping line end) would test that without re-reading this one.
