# TXP-D113 results: dint-f113-gloss (fr.3619 f.113, DECODE 9443) built and read once (9 Oct 2026, 15:52-16:1x UTC by date -u)

LANE TX-ENGINEER-2 round 0b item 1, brief `.claude/briefs/runs/2026-10-09-account4-txp-gloss.md` (PREREG txeng2-0 0b + Amendment 1).
Order kept: crops a87658a84; build script drafted 4bd0b58b4 (reads no gloss); passB eb44908a7, passA next commit; reconcile + queue
99433a892; adjudication + passZ a9efc6e6f (16:05 UTC) -- all before any gloss crop was cut or read; gloss crops, two gloss reads,
splits, gloss.tsv, then truth and score.

## Headline
| output | err_true (95%) | wrong / deleted / inserted | paired vs passZ (fixed/broken) |
|---|---|---|---|
| **passZ_pipeline (reference)** | **0.000 (0/81) 0.000-0.045** | 0/0/0 | -- |
| passA (Opus) | 0.012 (1/81) 0.002-0.067 | 0/1/0 (one "." dropped, e) | 0 / 1 |
| passB (Opus) | 0.025 (2/81) 0.007-0.086 | 2/0/0 (n <- #, x2) | 0 / 2, p = 0.50 |

**Baseline errors E = 0 (pool gain 0).** By the brief's own rule (a position is scored only when the gloss letter is the reference
sign's leaf-majority value at n >= 2, agree >= 0.75, and key_print-consistent) passZ's sign is in the truth set at every scored
position, so passZ scores 0 by construction on identity as well as segmentation; its misreads cannot be scored wrong, they land
in the excluded classes (low-agree 14, key-conflict 22). The brief's line "passZ's wrong-sign positions count" does not hold under
this recipe -- the truth is the gloss only through the leaf's own key, which is built from passZ. This unit adds nothing to the
pool's E; it is useful only for scoring other outputs (passA/passB above) on 81 positions. tx_power: E 0, no power (as expected).

## Counts
186 positions (passZ), 81 scored, 105 excluded: unaligned 51, key-conflict 22, low-agree 14, off-sheet 11 (NEW:d-shape, a round
bowl with a rising stroke that the f128 reader table has no label for; both readers and the adjudicator agreed it is one shape;
the decode suggests it is key_print's "D", not tested), multi-letter 6, gloss-unread 1. Flag align-conflict on 55 of 81 scored
(rule: a neighbour at +-1 is conflict or unaligned; with 51 unaligned positions it over-fires, so the flagged-excluded figure,
0/26, is weak; the rule was fixed before scoring and not tuned after).
Cipher pass agreement A/B 162/186 = 87.1% (nw, --keep-dots); 24 disagreements + 47 agreed-uncertain = 71 rows to the Sonnet
adjudicator, all viewed, 5 changed from the first candidate. Gloss reads A/B: character agreement 0.75 / 0.81 / 0.73 / 0.84 / 1.00
per line (L02, L03, L05, L07, L09); 14 word splits settled by one Sonnet look. The gloss reads are the weak side of this item
(e.g. L05 "presage de nost sime"), but a misread gloss letter is excluded by the key_print / leaf-majority rule, not scored.

## Key rebuilt (key_rebuilt.tsv)
24 sign rows rebuilt from this leaf; 14 kept (n >= 2, agree >= 0.75): - :- b, . e, 0 e, 3 d, 4 l, L i, c r, f n, sq s, v a, w r,
y o, z m (+ one more, see file); all 14 in key_print and all agree with it (by rule; none dropped for a key_print conflict among
rows that otherwise passed). Not kept: # (d 6/9, key_print c), 1 (e 4/11), m (u 3/5), v' (a 1/5), NEW:d-shape, singletons.

## Alignment and its control (deviation stated)
Pre-registered settings (align_print.py syl: floor 100, null_cost -1, max_chunk 3, seg_bonus 0, len_prior 1, FOLD_FS off;
gloss + | ? as wildcard): FAILED -- 0 scored, align agrees 51/186 = 0.274, GAPS4 real 0.022 vs 200 value-shuffled keys mean
0.071, max 0.161, rank 200 of 201. Five whole-line pairs (f128 aligned per gloss word) give the hard-EM no anchor.
Build as committed: the same settings with the first E-step SEEDED by key_print.tsv counts (meaning: agree + others); later
iterations use this leaf's counts only. Align agrees 91/186 = 0.489; GAPS4 real 0.350 vs 200 value-shuffled keys mean 0.063,
max 0.128, rank 1 of 201. The seed makes the key_print check partly circular; a scored position still needs this leaf's own
gloss letter as the sign's leaf majority at n >= 2 and agree >= 0.75. A verifier may prefer to treat this item as
"truth = gloss through key_print" rather than an independent leaf key.
Bug fixed before scoring: the build's comment-skipping TSV reader dropped key_print's "#" row (it starts with "#"); fixed
(comments=False for key_print), raising scored 77 -> 81.

## Crops (pasted)
The block slopes ~1.8 deg and the gloss rows sit ~18 px from the cipher rows (DECODE copy 1600 x 2264 px, signs ~10-12 px tall);
--follow-slope on the unrotated region jumped onto gloss rows, so the block was rotated once (PIL bicubic, -1.78 deg about (40,150))
into src_f113_rot178.jpg (= IMG_R9443_I44629_P.jpg region 180,1260,1220,300), then:
`python3 tools/iiif_lines.py --image benchmark-tx/txeng2/dint-f113-gloss/src_f113_rot178.jpg --region 0,70,1220,200 --out benchmark-tx/txeng2/dint-f113-gloss/crops --prefix f113 --max-width 1250 --overlap 300 --band-extent 0.1 --mask-neighbours --overlap-note --debug --centres 25,52,78,91,98,122,145,162,180 --follow-slope 250 --only-lines 3,7,9`
`python3 tools/iiif_lines.py --image .../src_f113_rot178.jpg --region 0,70,1220,200 --out .../crops --prefix f113 --max-width 1250 --overlap 300 --band-extent 0.1 --mask-neighbours --overlap-note --debug --centres 25,52,77,91,106,122,142,162,183 --only-lines 5` (follow-slope tracked L05 onto its gloss row; fixed band used)
`python3 tools/iiif_lines.py --image .../src_f113_rot178.jpg --region 880,70,340,200 --out .../crops --prefix f113e --max-width 1250 --overlap 300 --band-extent 0.1 --mask-neighbours --overlap-note --debug --centres 22,42,62 --only-lines 2` (the 6-sign run at the end of the clear line above)
crops_note.md:
> - f113: each line is one crop (no segments, no overlap).
> - f113e: each line is one crop (no segments, no overlap).
Overlays checked (f113_lines_debug_slope.jpg, _fixedL05.jpg, f113e_lines_debug.jpg) and every crop viewed. **gloss-visible**:
gloss ink that touches cipher signs survives the mask (one connected component); --mask-keep 0.7 erased real signs, so the
default 0.5 was kept. Readers were told to ignore "fragments of small handwriting from neighbouring rows", never what they are.
Gloss crops: same commands with --top-margin 22, --band-extent 0.3, no mask, prefixes f113g / f113ge (the gloss rows are too
close to cut alone).

## Calls and cost
6 vision subagents: 2 Opus cipher passes (~144k, ~137k tokens), 1 Sonnet adjudication (~158k), 2 Opus gloss reads (~114k,
~116k), 1 Sonnet gloss split look (~107k). The brief's price was 5 calls (cap 8); this ran 6 (the gloss reconciliation needed its
own Sonnet look, as the brief's step 4 says) -- likely over the 8 cap; dollar figure: the orchestrator's get_session reading.
