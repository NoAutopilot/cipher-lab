# TXE-F: per-cut quality gate (tools/tx_tile_gate.py) -- RESULTS (9 Oct 2026, 07:30-07:38 UTC by date -u; account 4, Opus)

Verdict: **FAIL on the read-free gate (dev_tune)** -- the non-good labels hold 6 of L's 14 wrong positions (recall 0.429)
at 66 of 343 positions flagged (19.2%); registered gate recall >= 0.50 at <= 15% flagged: NOT MET on both terms. Eval_heldout
(read-free, no reader, so no eval look is spent): 5 of 15 (recall 0.333) at 18.4% flagged, NOT MET. **No reader call was
made** (brief step 4: gate not met -> no read). `recut` is built, run on dev_tune into the scratchpad (69 tiles, 3 sheets,
not committed, never read) and tested offline. Calls: 0 vision. Looks at eval: 0 (the eval table is read-free).

Gate source: brief `.claude/briefs/runs/2026-10-09-account4-txe-f.md` step 2 (>= 50% of L's wrong positions at <= 15%
flagged). research/TX-IDEAS-2026-10-09.md row O3 says "<= 10% flagged"; the brief's 15% is the looser of the two and the
result fails both.

## Order of work (blindness)
1. `score` written and run on f178v and f179r from the page images and atlas boxes only; tiles_f178v.tsv / tiles_f179r.tsv
   committed and pushed (70c379923) before any truth was opened.
2. `gate` then opened truth only through `tools/tx_bench.py` position_errors (BENCHMARK-TX truth of birago1572-no87, L =
   benchmark-tx/txeng/units/labels_<unit>.tsv, pass A = passA_<unit>.tsv). Box -> position map label-blind
   (tools/tx_compare.py box_map, the no87_map.py width DP; box_pos.tsv here, regenerated for all line-read lines after a
   bug, see below). The rule thresholds were not changed after
   the truth was opened.

## Label counts (rule fixed before truth; `score`)
| page | boxes | joined | bad-crop | blot | good | Otsu | median w x h |
|---|---|---|---|---|---|---|---|
| f178v | 675 | 6 (0.9%) | 117 (17.3%) | 0 | 552 (81.8%) | 147 | 66 x 65 |
| f179r | 144 | 9 (6.2%) | 28 (19.4%) | 0 | 107 (74.3%) | 153 | 58 x 60 |

Every bad-crop on both pages comes from the band-cut term (tx_taxonomy band_edge rule): edge contact never exceeds 0.27
(f178v max), so the `edge > 0.3` term fires on no real box. No real box is a blot (max ink mass 0.617, and none meets the
size/shape terms together). So on this hand the classifier is, in effect, "band-cut" plus 15 wide multi-valley boxes.

## Flag vs wrong, dev_tune (343 scored positions; L wrong 14, pass A wrong 23 -- position_errors counts wrong + deleted,
insertions are not positions, so A shows 23 where PREREG's 24 includes one insertion)
| label | flagged | % of positions | L wrong held | L precision | L recall | A wrong held | A precision | A recall |
|---|---|---|---|---|---|---|---|---|
| joined | 7 | 2.0 | 1 | 0.143 | 0.071 | 1 | 0.143 | 0.043 |
| bad-crop | 59 | 17.2 | 5 | 0.085 | 0.357 | 5 | 0.085 | 0.217 |
| blot | 0 | 0.0 | 0 | - | 0.000 | 0 | - | 0.000 |
| good | 277 | 80.8 | 8 | 0.029 | 0.571 | 17 | 0.061 | 0.739 |
| non-good | 66 | 19.2 | 6 | 0.091 | 0.429 | 6 | 0.091 | 0.261 |
| no box | 0 | 0.0 | 0 | - | 0.000 | 0 | - | 0.000 |
registered gate (non-good hold >= 50% of L wrong at <= 15% flagged): recall 0.429, flagged 0.192 -> NOT MET

## Flag vs wrong, eval_heldout (read-free: no reader, no eval look spent; 376 scored; L wrong 15, A wrong 18)
| label | flagged | % of positions | L wrong held | L precision | L recall | A wrong held | A precision | A recall |
|---|---|---|---|---|---|---|---|---|
| joined | 6 | 1.6 | 0 | 0.000 | 0.000 | 0 | 0.000 | 0.000 |
| bad-crop | 63 | 16.8 | 5 | 0.079 | 0.333 | 6 | 0.095 | 0.333 |
| blot | 0 | 0.0 | 0 | - | 0.000 | 0 | - | 0.000 |
| good | 307 | 81.6 | 10 | 0.033 | 0.667 | 12 | 0.039 | 0.667 |
| non-good | 69 | 18.4 | 5 | 0.072 | 0.333 | 6 | 0.087 | 0.333 |
| no box | 0 | 0.0 | 0 | - | 0.000 | 0 | - | 0.000 |
registered gate (non-good hold >= 50% of L wrong at <= 15% flagged): recall 0.333, flagged 0.184 -> NOT MET

Descriptive only (not a registered gate): the non-good flags are enriched for L's errors -- precision 0.091 vs a base rate of
0.041 on dev (hypergeometric P(>= 6 of 14 in 66 of 343) = 0.034), 0.072 vs 0.040 on eval (P(>= 5 of 15 in 69 of 376) = 0.12).
That is the taxonomy's band-cut finding again (class 2b: 9.5% vs 5.2%), not a new signal, and too thin for a re-cut to be
worth a read: even a perfect re-read of every flagged dev tile could fix at most 6 of 14, while 8 of L's 14 dev errors sit
on tiles labelled good (the shape-ambiguity floor a crop cannot fix).

Per-position flags: flags_dev_tune.tsv, flags_eval_heldout.tsv (line, pos, label, L_wrong, A_wrong). Raw gate output:
gate_dev_tune.txt, gate_eval_heldout.txt.

## recut (built, not read)
`recut --labels joined,bad-crop --unit dev_tune` on f178v: 69 tiles (bad-crop 61, joined split 4 x a/b) on 3 sheets of
<= 24 rows, 0 blots dropped. Bad-crop tiles are grown to the own component's full ink extent + 10% from the page image,
neighbouring lines whited out with tools/iiif_lines.mask_neighbours; one neighbour of context each side, 2x. Checked by
eye on sheet 1 rows 1-3 (target framed, neighbours visible, other-line ink masked). Sheets were written to the scratchpad
only and never given to a reader.

## Reader task text (prepared, NOT used -- gate not met)
"For each numbered row of sheet_NN.png, the cell T## of harvest/sign_sheet_blind_1572.png that matches the boxed sign, or
X_NEW / ?; write row, sign_id, conf to reads_NN.tsv."

## tx_taxonomy on passN vs L
Not run: no passN exists (no read was taken).

## Fixes made during the job (none touches a threshold or a label rule)
- box_pos.tsv was first written for the dev lines only and reused for eval (the first eval table came out all "no box");
  fixed to map every line of the line read once. The dev table was identical before and after.
- Otsu on a pure two-level image (the offline test page) has a flat optimum and returned 0; it now takes the plateau's
  middle. Re-scoring both real pages after the fix gave byte-identical tiles TSVs (cmp).
- Sheet rows are now numbered from 1 on every sheet inside make_sheets.

## Notes for the rule set (from the offline test, not from truth)
- The registered order (joined, bad-crop, blot) means a box drawn tight on a solid round blob touches ~40% of its perimeter
  and is labelled bad-crop, not blot; the test blob carries a 1 px margin as the segmenter's boxes do.
- "valleys >= 2" is read literally: interior minima of the smoothed column profile below half the lower flanking maximum;
  a clean two-sign join with one gap has one valley and stays good unless its signs have internal valleys.

Follow-up (one line, not done): the only predictive term here is band-cut, which TXE-B's `--band-extent` bands are built to remove at
the source (its registered gate: cut share <= 3%); a tile gate on top of those bands has nothing left to flag on this hand.
