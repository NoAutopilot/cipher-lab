# PREREG TXE-N (M20): a second crop set shifted half a line and half a segment, read only where the two sets disagree

Written 9 Oct 2026, 08:2x UTC by date -u, by TXE-N (LANE TX-ENGINEER, account 4, Opus 5.5), pushed BEFORE any read.
Binds with `benchmark-tx/PREREG-txeng-2.md` (units, blindness, Amendment: single-instrument gate p < 0.01, one eval look).
Brief `.claude/briefs/runs/2026-10-09-account4-txe-n.md`.

## Crop sets (dev_tune = f178v L01-12; source `harvest/f178v/src_ark_12148_btv1b9060248g_f182_1703_848_2900_3452.jpg`, `--image`, no fetch)
- **S0** (`s0/`): the TXE-B geometry. `tools/iiif_lines.py --image SRC --out benchmark-tx/txeng/shift/s0 --prefix f178v
  --max-width 1250 --band-extent 0.1 --mask-neighbours --only-lines 1..12 --check-boxes atlas/signs.tsv --overlap-note
  --note-scale 2 --debug`. 3 segments a line, overlap 425 native px.
- **S1** (`s1/`): the same plus `--shift-bands 0.5 --shift-segments 0.5` (new options, tested in
  `tools/tests/test_iiif_lines.py` item 9). Every band moved down half a pitch (68 px of 137), so each crop holds the
  marked line in its upper part and the next line below it; the mask keeps both lines' components whole (mask rows = own
  band top .. next band bottom), so no sign of the marked line is masked away at the band edge. A red triangle in a
  40 px white left margin marks the line to read. Segment cut points moved half a step (412 px): 4 segments a line
  (838, 1250, 1250, 838 px), overlap 425-426 px, so a sign at an S0 segment edge is central in S1 and vice versa.
- Read-free checks (done before this file, both sets; `s0/band_check.tsv`, `s1/band_check.tsv`, `*/cmd.log`):
  S0 f178v 675 boxes, ink rule cut 4 (0.6%), admitted 9 (1.3%) (= TXE-B). S1: cut 13 (1.9%) page-wide, 1 on L01-12 (L05);
  admitted 646 (95.7%) -- by design (each S1 crop carries the next line; the marker says which to read). Both debug
  overlays checked by eye (blue band edges sit on the gaps in S0, through the line bodies' lower half in S1); one S1 crop
  (L05_s2) checked by eye: marked line whole incl. ascenders and the tilde marks, next line whole below.
- Reader images: 2x LANCZOS PNG of each crop (`crops2x/`, gitignored, regenerable), as for pass A and TXE-B.

## Reads (blind, value-blind; Opus 5.5 subagents, `model: opus`)
- Per set two calls (L01-06, L07-12): the unchanged `harvest/blind_pass_brief_1572.md` + `sign_sheet_blind_1572.png` +
  that set's generated `crops_note.md` (S1's note carries the generated marker sentence). Raw reads committed per set
  (`s0/passV_s0_raw_*.tsv`, `s1/passV_s1_raw_*.tsv`) and pushed before any score. Normalised (line `f178v_Lnn`, pos,
  sign = sign_id, every row kept incl. X_ and ?) -> `benchmark-tx/outputs/birago1572-no87/passV_s0_dev_tune.tsv`,
  `passV_s1_dev_tune.tsv`.
- Reconcile: `tools/reconcile_passes.py passV_s0 passV_s1` -> disagreements.tsv = the doubtful positions (positional
  substitutions and indels both). Third look: ONE Opus call on the disagreements only; each row shows the S0 crop window
  and the S1 crop window around the position side by side (4x, one neighbour each side), the two readings numbered 1/2 in
  a seeded random order with exemplar-free cell images from the blind sheet; question "which of the two readings, a third
  cell, or ?". If the disagreements exceed 16 rows they go on sheets of 16, at most 3 calls (dev cap 5 vision calls);
  beyond that the remainder keeps the S0 reading (stated in RESULTS). Resolve -> `passV_shift_dev_tune.tsv`: agreed
  positions keep the agreed sign; a disagreement takes the third look's pick (a third cell -> that cell; ? -> the S0 sign;
  an indel: the third look says whether the sign is there).
- Counts reported: disagreements, the third look's picks (S0 / S1 / third / ?).

## Gate (fixed now)
`python3 tools/tx_bench.py passV_shift_dev_tune.tsv --bench BENCHMARK-TX.tsv --item birago1572-no87 --paired
benchmark-tx/txeng/units/passA_dev_tune.tsv`: fixed > broken with two-sided sign test **p < 0.01** -> PASS dev, then
eval_heldout ONCE (S0+S1 cut of f178v L13-23 + f179r L01-03, same reads, same third look; counted as the eval look in
research/TX-IDEAS-2026-10-09.md); else FAIL, no eval. Reported, not gating: shift vs labels_dev_tune.tsv (L); S0 alone vs A
(the geometry instrument's own dev read, which TXE-B never took on dev_tune); S1 alone vs A; S0 vs S1.
Band-cut positions (tx_taxonomy band_edge cut), wrong in A / S0 / S1 / shift, after commit.

## Predictions
1. S0 alone vs A on dev_tune: small or no gain (dev_tune has few band-cut / tail positions; TXE-B's gain was the sloped tail).
2. Disagreements S0 vs S1: 8-15% of positions (A vs B agreed 91%); they hold more than half of S0's errors.
3. The third look fixes more than it breaks on the disagreements; whether that reaches p < 0.01 vs A on 343 signs is open.
