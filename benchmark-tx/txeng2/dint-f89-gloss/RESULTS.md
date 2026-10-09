# TXP-D89 results: dint-f89-gloss built and read once with today's pipeline (9 Oct 2026, 15:51-16:1x UTC by date -u)

LANE TX-ENGINEER-2 round 0b item 1 (PREREG `benchmark-tx/PREREG-txeng2-0.md` 0b + Amendment 1; brief
`.claude/briefs/runs/2026-10-09-account4-txp-gloss.md`, row TXP-D89, split dev). Leaf BnF fr.3619 f.89 (DECODE 9440, Dinteville
to Nevers, Langres, Nov 1591), DECODE copy `IMG_R9440_I44624_P.jpg`, **1600 x 2264 px** (manifest: 1653 px PNG original).
Order kept: crops bc634558f; passA/passB parts committed as each landed, joined (norm_passes.py); reconcile + queue; Sonnet
adjudication (failed, kept as adjud_out_first.tsv); Opus adjudication + **passZ committed before any gloss read**; then
gloss crops read (glossA/glossB), gloss.tsv, truth build, score.

## Headline (this leaf only)
```
dint-f89-gloss [dev] err_true 0.042 (10/240) 95% 0.023-0.075 | wrong 10 deleted 0 inserted 0 | excluded 333
  flagged excluded 0.015 (2/138) [102 flagged align-conflict]
```
| output | err_true (95%) | flagged excluded | paired vs passZ (fixed/broken, p) |
|---|---|---|---|
| **passZ_pipeline (baseline, reference; home advantage)** | **0.042 (10/240) 0.023-0.075** | 0.015 (2/138) | -- |
| passA (Opus, blind) | 0.079 (19/240) 0.051-0.120; wrong 11, inserted 8 | 0.080 (11/138) | 0 / 1, p 1.0 |
| passB (Opus, blind) | 0.121 (29/240) 0.086-0.168; wrong 23, deleted 1, inserted 5 | 0.116 (16/138) | 0 / 14, p 0.0001 |

passZ scores 0 on segmentation by construction (it is the reference sequence) but NOT on identity: the truth is the gloss, so a
passZ sign that is not in the letter's GOOD-sign set counts wrong (10 such). Baseline errors E = 10 (the pool gain).
tx_power (1000 draws, seed 1): the unit alone has no power (clean 30% fixer passes p<0.01 in 0.004 of draws); it counts only in
the pool.

## Counts
573 positions (passZ, non-dot signs), **240 scored, 333 excluded**: low-agree 119, gloss-unread 98, ambiguous-sign 44,
off-sheet 43 (X_*, NEW, ?), unaligned 23, key-conflict 4, multi-letter 2. Flag align-conflict on 102 scored.
Pair agreement A/B 595/660 = **90.2%** (nw; dots dropped by the tool default, see below); 65 disagree + 106 agreed-uncertain.
Gloss reads: letters agreed 493 of 625 = 0.789 (letter difflib); the 132 split letters became '?' (gloss-unread).
Alignment control: interlinear_align agrees 349/573 = 0.609; GAPS4 statistic rebuilt key 0.525 vs 200 value-shuffled keys mean
0.047, max 0.105, rank 1 of 201.
Leaf key rebuilt (`key_leaf.tsv`): 38 signs, 13 GOOD (single letter, count >= 2, agree >= 0.75, key_print-consistent); key_print
overlap 25 signs, **21 agree** with key_print's meaning (# c, 0 e, 1 e, 3 d, 4 l, + l, L i, c r, f n, m u, sq s, v a, w r, y o,
z m, 9 g ...; conflicts include T: leaf a vs key_print h, v': s vs a, a': n vs q, z': ene vs m, all count 1-2).

## Deviations and corrections (stated)
- **Crops.** The leaf's lines fan (slope -0.03 to -0.05) and the gloss sits 15-18 px above each cipher line. The page region
  (150,600,1290,700) was rotated -2.12 deg first (`src_f89_R9440_rot-2.12_150-600-1290-700.jpg`), then cut with --follow-slope;
  one crop per line (1290 px < reading limit; `--max-width 1250 --overlap 300` would have made two segments overlapping 1210 px).
  Final command (pasted):
  `python3 tools/iiif_lines.py --image benchmark-tx/txeng2/dint-f89-gloss/src_f89_R9440_rot-2.12_150-600-1290-700.jpg --out benchmark-tx/txeng2/dint-f89-gloss/crops --prefix f89 --centres 62,90,115,131,147,165,183,202,220,237,256,272,289,306,325,343,362,377,397,410,435,452,470,488,510,527,547,562,580,600,635 --only-lines 4,6,8,10,12,14,16,18,20,22,24,26,28,30 --follow-slope 100 --max-width 1300 --band-extent 0.15 --mask-neighbours --mask-keep 0.3 --overlap-note --debug`
  (31 rows given by eye: 14 cipher, 14 gloss, 3 clear; band files renamed f89_L01-L14 in order). crops_note.md:
  > - f89: each line is one crop (no segments, no overlap).
- **gloss-visible (Amendment 1).** Tighter settings (band-extent 0.0, mask-keep 0.75) erased real cipher signs and the tracker
  followed the gloss row on L14 (checked on the overlay and stacked crops); the kept settings keep every cipher sign but leave
  gloss letters legible in most crops. Readers were told only that small writing above/below is not part of the line.
- **Pass B notes spilled into rows** (sign_id 'form', 'stem', 'through' ...): folded back into the note by `norm_passes.py`
  (mechanical); each reader's NEW: labels mapped to shared X_ codes by description (table in the script).
- **Adjudication.** The Sonnet call (171 rows) returned every row unadjudicated (first candidate, viewed=no; its own report);
  kept as `adjud_out_first.tsv`, not used. Retry: one Opus call on the 65 disagreements only, with 3x zoom halves
  (`zoom/`), 65 viewed, 25 changed; the 106 agreed-uncertain rows keep the agreed reading.
- **Dots dropped.** `tools/reconcile_passes.py` drops '.' without `--keep-dots`; passZ was built that way before the gloss read
  and not rebuilt after, so the item covers non-dot signs only (A/B outputs drop their '.' rows: 39 / 36). A rebuilt item with
  dots needs a fresh reconcile + adjudication before any gloss look.
- **Gloss calls.** One Opus call per gloss pass (14 lines each), not two, and no Sonnet look at the splits (splits -> '?'
  mechanically, `gloss_reconcile.py`): both to stay under the 80% cap line after the extra adjudication call.
- **Truth rule, built in three steps after the first score (all three runs reported here, rule 3 transparency).** First build
  excluded every position whose letter was not passZ's sign's majority: passZ scored 0.000 (0/230), which contradicts the
  brief (wrong-sign positions must count). Second build scored any one-letter chunk with a GOOD sign for it: passZ 0.102
  (26/256), A 0.137, B 0.176 -- but the top confusions were label collisions, not reads: '4' -> a x7 (the reader vocabulary's
  '4' is both key_print '4' = l and 'D' = a, merged by dint128_label_map) and '1' -> i x7 ('1' reads e 26 / i 7 on this leaf).
  Final build excludes a position when passZ's sign is not GOOD and the letter is one of its repeated (>= 2) values
  (ambiguous-sign, 44) or its own majority (low-agree): the figures in the headline. The 10 remaining passZ errors are
  single-occurrence confusions (# for d/e, 0' for n/s, + for i, 1 for r, 0 for i, 4 for i ...), plausible reader errors.
- Not done: the postscript cipher line (bottom, no gloss) is out of the item.

## Calls and cost
8 vision subagents: 4 Opus reader calls (2 passes x 2 halves), 1 Sonnet adjudication (unusable), 1 Opus adjudication, 2 Opus
gloss reads. Dollar figure: the orchestrator's get_session reading.
