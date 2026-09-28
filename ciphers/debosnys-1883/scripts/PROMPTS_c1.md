# H2: cryptogram 1, third blind pass and adjudication rule

Written 28 Sept 2026 21:2x UTC by DEBOSNYS-RUNNER-3 (session_018qnyJQbVSd2NyPvDVApXqS) BEFORE any per-sign
crop was cut or looked at, and committed before the reader was spawned (CAMPAIGN.md H2). The reader is a
separate Fable subagent that receives only crop paths and the inventory sheet tiles; it never sees passA_c1.tsv,
passB_c1.tsv, ciphertext_c1_draft.tsv, disagreements_c1_passB.tsv or this file's adjudication section.

## What the reader gets

- Unit: the physical box (both passes read the same 136 pre-cut boxes, identical per-line counts), so the disputed set is
  the positions where passA_c1.tsv and passB_c1.tsv differ (`scripts/h2_disputed_positions.tsv`, computed before any crop
  was cut; GOLD-4E's 52 aligned columns include 4 alignment-gap artefacts of the Needleman-Wunsch step on L01 and L05).
  For each disputed position:
  a per-sign crop from `images/Debosnys-Cryptogram-1.png` (the Schmeh PNG's own pixels, 1111x481, the only
  resolution on disk: "native" here means no re-encoding, upscaled 6x with Lanczos for legibility, the box padded
  by 6 px each side), and a line-context strip with the target box outlined in red.
- The 160-id inventory sheet `glyphs/inventory.png` cut into tiles (`scripts/h2_crops/inv_NN.png`), each tile
  captioned with the sign ids it shows, plus `glyphs/inventory.tsv`'s id list.
- Every crop is a real box; the reader may still answer MULTI or `_` for it.

## Reader prompt (per call, one call per two lines, three calls)

"You are reading a hand-drawn 1883 cipher. For each numbered crop below, name the ONE inventory id from the
attached sheet tiles that best matches the sign inside the red box in the context strip, with a confidence
H (unmistakable), M (best match, one plausible alternative) or L (guess), and your best alternative id. If the
box holds more than one sign write MULTI; if it holds no sign (dust, bleed-through, a stray stroke) write `_`.
Do not describe what the sign might mean. Write one line per crop: <crop id> <TAB> <sign id> <TAB> <H/M/L> <TAB>
<alt id> <TAB> <five-word shape note>. Read every crop; never skip one."

## Adjudication rule (fixed before looking; applied by scripts/h2_adjudicate.py, which prints the counts)

1. For each column, C = the reader's id. Settled full id = the id named by at least two of A, B, C.
   Grade H when all three agree or when C's confidence is H and one of A/B agrees; otherwise M.
2. If no two agree on the full id but two agree at family level (`glyphs/inventory.tsv` `family` column, then
   `glyphs/base_mark.tsv`'s base fold), the column is settled at the family/base value with the mark of the
   majority (or none), graded M, flagged `family-settled`, and counts as settled only in the family-level number.
3. A three-way split stays unsettled (M, all three values kept in `alt`).
4. A MULTI or `_` verdict from C on a box the other two read as a sign is a segmentation flag: recorded, graded M,
   the column stays unsettled unless one of A/B also has MULTI/`_`.
5. Numbers reported, all computed by the script, none by hand: (a) pairwise blind agreement on the disputed
   positions, A-C and B-C, full id and family level (the honest independent numbers); (b) the settled count after
   majority and the new agreement (already-agreed + settled) over 136 boxes, full id and family level;
   (c) the remaining unsettled positions; (d) the type-noise estimate the settled draft carries: unsettled/136
   as the floor, and (unsettled + family-settled)/136 as the ceiling, read against the GOLD-D2 base-level
   curve (0.816 at 2.5 pct, 0.385 at 5 pct).
6. Gate: 80 pct full-id agreement over the 136 boxes after adjudication licenses writing cryptogram 1 into
   `ciphertext.txt` from `ciphertext_c1_draft.tsv` (settled columns H/M as graded, unsettled M with alts);
   below 80 pct the draft is updated and `ciphertext.txt` stays as it is.
7. Nothing in this pass is a reading of the cipher; grade S/M throughout, 0 H-from-key, 0 C-from-plaintext.

## H7 (28 Sept 2026, written before the reader was spawned): the verse's first line, c4a0

Band: images/Debosnys-Cryptogram-4a.png @ 280,372,740,436 (under the "monographe. verse." title, above GOLD-4A's c4a box),
segmented with tools/glyph_atlas.py segment alongside the six original pages (deterministic: their boxes reproduce
exactly), 16 boxes, kNN read with `classify --exclude-page` against labels_box.json (pass K). One value-blind Fable eye
pass (pass E) on the 16 crops with the same prompt as H2's readers. Rule: label = E's id; grade H when K = E and E's
confidence is H, else M; K's id kept in `alt`; E's MULTI / `_` verdict stands (segmentation). The rows are appended to
glyphs/box_labels.tsv as page c4a, line 0 (sids c4a_00_NNN, source `eye:h7-c4a0|knn:<K id>`), and lines.tsv gets
c4a_L00; scripts/gold4c_inventory.py then rebuilds passA.tsv and ciphertext_draft.tsv from box_labels.tsv as before.

## H21 (28 Sept 2026, written before pass B landed and before any disputed crop was cut): cryptogram 2

Pass B: five value-blind Sonnet calls on the numbered line strips of c2a (17 lines) and c2b (9 lines) rendered by
`tools/glyph_atlas.py classify --strips` (2x copies), against the inventory tiles, box counts per line given in the
brief; never a pass file. Reconciliation: by position (both passes read the same boxes), disputed = positions where
passA.tsv and pass B differ. Third pass C: value-blind Fable calls on per-sign 6x crops of the disputed positions
only (scripts/h21_pipeline.py crops, about 15 crops per call, the H2 prompt). Adjudication: the H2 rule (rules 1-7 of
this file's first section) applied to c2, with the same numbers reported; gate 80 pct full id over the 734 boxes
licenses writing the cryptogram 2 sections of ciphertext.txt in inventory ids. A pass-B line whose row count differs
from the box count is realigned by position from the left and flagged; nothing is read.

## H23 (28 Sept 2026, written before pass B landed): cryptograms 3 and 4

The H21 recipe on c3 (4 lines, 118 boxes), c4a (14 lines, 214) and c4b (5 lines, 69): four value-blind Sonnet
pass-B calls on the numbered strips, position reconcile, value-blind Fable third pass on the disputed boxes, the H2
rule; c4a0 (verse line 1, 16 boxes) keeps its H7 eye+kNN labels (two witnesses already) and is not re-read. Bourdeau's
verse read (H26 concordance) is a fourth vote on c4 three-way splits only, applied after the three-pass rule, graded
M, flagged `bourdeau-vote` -- never as pass B. `scripts/h21_pipeline.py --pages c3,c4a,c4b` with pass files
passB_c34.tsv / passC_c34.tsv writes ciphertext_c34_draft.tsv and, at the 80 pct gate, the cryptogram 3 and 4
sections of ciphertext.txt.
