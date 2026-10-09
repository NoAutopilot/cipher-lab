# TXP-D98 results: dint-f98v-gloss (fr.3619 f.98v, DECODE 9441 P2), 9 Oct 2026, 15:52-16:1x UTC by date -u

LANE TX-ENGINEER-2 round 0b item 1 (brief `.claude/briefs/runs/2026-10-09-account4-txp-gloss.md`). Order kept, each step
committed before the next: crops + brief 6c8853b80; passB, passA; reconcile + queue 27a738d2d; adjudication + passZ 3142a2f6f
(pushed) -- all before the gloss crops were opened; then gloss crops, glossA/B + splits, gloss.tsv, truth, score.

## Headline
```
passZ_pipeline  err_true 0.000 (0/53) 95% 0.000-0.068 | excluded 193 | flagged-excluded identical (0 flagged)
passA (Opus)    err_true 0.057 (3/53) 95% 0.019-0.154 | wrong 1 (s <- sq') inserted 2 | paired vs passZ fixed 0 broken 1
passB (Opus)    err_true 0.019 (1/53) 95% 0.003-0.099 | inserted 1                    | paired vs passZ fixed 0 broken 0
```
**passZ scores 0 here by construction, not by merit:** a position is scored only where passZ's own sign is gated by this
leaf's rebuilt key, and every scored passZ sign's gated value equals the gloss letter there (ref-off-key 0). The item's
baseline errors E = 0, so it adds nothing to the pool's power (tx_power: E 0, N 53, power 0.000); it is a dev item for
passA/passB-style outputs only. The brief's hoped-for ~40 baseline errors did not materialise: the gloss read and the
alignment were too weak to pin more than 8 signs.

## Counts
- 246 passZ positions (L01 20, L02 42, L03 54, L04 49, L05 50, L06 31); 53 scored; 193 excluded: unaligned 70, low-agree 77,
  multi-letter 15, gloss-unread 11, n<2 9, off-sheet (NEW:*) 7, letter-no-gated-sign 4. Flags: 0.
- Pair agreement A/B 206/246 = 83.7% (nw); 40 disagreements + 40 agreed-uncertain -> 80-row Sonnet adjudication, 17 changed
  from the first candidate (mostly 0 -> o, v' -> v); no NONE rows.
- Key rebuilt from the alignment: 30 sign rows, 8 gated (count >= 2, agree >= 0.75): + l, 0 e, c r, f n, m u, p i, sq s, w r;
  all 8 agree with key_print.tsv -- partly circular, since key_print is the EM prior (below).
- Alignment control: align agrees 100/246 = 0.407; GAPS4 rebuilt key 0.207 vs 200 value-shuffled keys mean 0.041, max 0.104,
  rank 1 of 201.

## Deviations (stated)
1. **key_print as EM prior.** With the brief's settings alone (align_print syl: floor 100, null -1, max_chunk 3, seg_bonus 0,
   len_prior 1, + wildcard '.') the alignment did not converge: align agrees 50/246, GAPS4 0.062 vs shuffled max 0.099, rank
   25/201, 0 gated, 0 scored. A key_print decode of passZ visibly tracks the gloss (L05 "...eronlieu...nsieur" under "cheron
   lyeutenant de monsr"; L06 "...able au ...eral" under "...able au general"), so the failure is the unseeded EM on 246 noisy
   signs, not a mismatched key. Settings otherwise unchanged. Sensitivity (not chosen by yield): max_chunk 2 -> 69 scored
   (ref-off-key 3), max_chunk 1 -> 38, null_cost -3 -> 13.
2. **Scoring rule.** Truth = the homophone set of the gloss letter among gated signs; a position whose passZ sign is NOT gated
   is excluded (never charged); a passZ sign gated to another letter would stay scored (flag ref-off-key) -- none occurred,
   so the figure equals the brief's literal rule.
3. **G03's first two words** ("?e Suoillem", the name written beside L03's run, over no sign) are dropped in the build by
   rule; gloss.tsv is as reconciled.
4. **Crops.** The DECODE copy on disk is 1600x2264 px (the manifest's PNG is 1653x2339). Lines rise ~2.9 deg left to right
   with gloss rows ~18 px above each cipher row (pitch ~17 px); --deskew/--follow-slope tracking jumped rows, so the page was
   rotated -2.9 deg once (src_f98v_rot-2.9.jpg, PIL bicubic, angle = max row-profile variance) and cut with --centres. Crops
   at --max-width 700 (not 1250: a 1300 px line at native is ~40 px tall, unreadable small) and shown to readers at 2x
   (crops/read/, LANCZOS; crops_note at --note-scale 2). Gloss masked: cipher crops keep only edge fragments of gloss strokes,
   no legible gloss word (both readers said they ignored stray top-edge strokes) -> gloss-visible: no.
5. Readers were told L01 begins and L06 ends with prose; both found a prose stretch inside L02 too and skipped it.

## Crops (pasted)
`python3 tools/iiif_lines.py --image benchmark-tx/txeng2/dint-f98v-gloss/src_f98v_rot-2.9.jpg --region 180,912,1300,236 --out benchmark-tx/txeng2/dint-f98v-gloss/crops --prefix f98v --max-width 700 --overlap 100 --band-extent 0.1 --mask-neighbours --overlap-note --note-scale 2 --debug --centres 12,31,47,66,87,100,127,140,160,175,195,215 --only-lines 2,4,6,8,10,12`
(bands 2,4,..,12 = cipher L01..L06, renamed in crops/read/; gloss rows: same command with --band-extent 0.3 --only-lines
1,3,5,7,9,11 --out .../gloss_crops --prefix f98v_gl.) crops_note.md:
> - f98v: segments of a line overlap by 100 native px (the images you read are at 2x, so 200 px in each image), about 9 signs (median sign width 11 px, ink-run median); a sign at the right edge of s1 and the left edge of s2 is ONE sign: the last 200 px of s1 and the first 200 px of s2 show the same ink, read it once.

## Gloss
Two blind Opus reads agreed on 1/4, 5/12, 2/10, 3/12, 4/11, 3/6 words per row (gloss_splits.tsv); the Sonnet reconcile
(gloss.tsv) rates G02-G04 L. The low gloss quality is what limits the item: the next step that would raise it is a native
(Gallica) re-cut of the gloss rows, or a person's read of the six gloss rows.

## Calls and cost
7 vision subagents: 2 Opus cipher passes (+1 Opus launch stopped within seconds, before writing anything, because its prompt
lacked the brief), 1 Sonnet adjudication, 2 Opus gloss reads, 1 Sonnet gloss reconcile. Dollar figure: the orchestrator's
get_session reading.
