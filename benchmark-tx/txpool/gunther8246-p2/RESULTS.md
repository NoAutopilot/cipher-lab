# TX-POOL-LEAF results: gunther8246-p2 (WVO 8246 MS p.2) built and read once (9 Oct 2026, 20:41-21:0x UTC by date -u)

Brief .claude/briefs/runs/2026-10-09-account4-tx-pool-leaf.md (TX-RED F21 route a), PREREG-txeng2-0 section 0b. Built by account 1
outside LANE TX-ENGINEER-2; the lane pools it (or not) under its own Amendment. Order kept, each step committed before the next:
CANDIDATES.md c4dad42c8; crops + calibration sheet + reader brief 41eafd7aa; passA bb0c659b6; passB 97bcb8da2; reconcile + queue
853e77acc; adjudication + passZ 7e5fbd474. Only after that: the Japikse print read, the truth build, the scores. No reader saw the
print, the key, the decode, the truth or another pass.

## Headline (this leaf only, split eval)
| output | err_true as measured (95%) | flagged excluded (95%) | paired vs passZ (fixed/broken) |
|---|---|---|---|
| **passZ_pipeline (baseline)** | **0.057 (18/317) 0.036-0.088** | **0.017 (5/302) 0.007-0.038** | -- |
| passA (Opus) | 0.060 (19/317; 18 wrong, 1 inserted) 0.039-0.092 | 0.020 (6/302) | 1 / 1, p = 1.0 |
| passB (Opus) | 0.063 (20/317; 19 wrong, 1 inserted) 0.041-0.095 | 0.020 (6/302) | 1 / 2, p = 1.0 |
| committed (G1/F1 reference, home advantage) | 0.047 (15/317) | 0.000 (0/302) | -- |

Top confusions on passZ (truth value <- read): t<-d6 x2, c<-d6 x2, o<-th x2, then one each of h<-aa, o<-Ib+, g<-b, e<-th,
n<-34, f<-88x, f<-NEW:x-dotted.

**Read this before using the number.** Baseline E is **18 as measured, 5 flagged-excluded**: 13 of passZ's 18 errors sit on the
15 `align-conflict` positions, where the committed reference sign is itself keyed to another letter than the print forces (p2_L05.14
th/e, L06.9 34/n, L06.12 88x/f, L08.17 Ib/s, L11.1 x/f, L11.2 or/o, L11.13 Ib/s, L12.5 d6/c, L15.12 th/o, L17.13 x/f, L21.11 th/o,
L22.1 34/l, L22.3 th/o, L22.11 d6/c, L24.12 Ib/i). They repeat by label (th=o x3, Ib=s x2, d6=c x2, x=f x2): most likely a shape
label that lumps two glyphs (a key gap in the 5109-only key) or an encipherer's slip, not a misread -- the two blind readers
agree with the committed sign at most of them. The flag was set by the build, before any reader was scored. **Under the brief's
>= 8 rule this item meets it as measured (18) and misses it flagged-excluded (5)**: the hand reads at about 2-6%, well under the
8-25% range the brief expected, so it adds little headroom to the pool. The named next step, if the lane wants more: the same
build on MS p.1 and p.3 (582 more committed signs; two blind passes + one adjudication, about 2/3 of this job's cost), same script.

## Counts
372 positions (committed p.2). 317 scored (15 flagged align-conflict). 55 excluded: off-key 39 (signs outside the 5109 key: b x7,
od, sqt, Ol, aa, t, ut, 58, 67, Ib+, BLOT and the other U codes), unaligned 9, letter-unkeyed 7.
Pair agreement A/B 364/374 = 97.3% (nw); 10 disagreements + 42 agreed-uncertain went to the Sonnet adjudicator (52 rows, 4 changed).
Alignment control (truth build): share of keyed committed signs whose key value equals the aligned print letter, whole letter
(953 signs): real 0.900 vs 20 letter-shuffled texts mean 0.276, max 0.311.
Truth sha256 6bd499d8a053886ff717589ac15cdcc8d5a16a99f919d7a1d5435bbd0817a249 (`python3 benchmark-tx/build_gunther8246p2.py --check`).

## Crops (pasted)
`python3 tools/iiif_lines.py --image ciphers/gunther-van-schwarzburg-1561/images/08246_p2.jpg --region 150,100,1050,1480 --out
benchmark-tx/txpool/gunther8246-p2/crops --prefix p2 --max-width 1250 --band-extent 0.05 --mask-neighbours --mask-keep 0.5
--follow-slope 150 --slope-local --overlap-note --debug` -> 25 bands = the 25 committed lines; crops_note.md (manifest-generated,
pasted into the reader brief): "p2: each line is one crop (no segments, no overlap)." Calibration sheet: MS p.1 cipher lines
p1L02-L11 cut the same way (sheet/, region 150,945,1050,590) with the committed labels as shape names (sheet/calibration.tsv);
p.1 is not scored.

## Caveats
- Label vocabulary = the committed transcription's code names, described by shape by the builder (the brief's label list) plus the
  p.1 calibration sheet; a description error would show as a systematic confusion. None of the top confusions is a pure label-name
  mismatch except possibly `Ib+` vs `Ib` (Ib+ is unkeyed).
- Known text is a 1934 modern print of a decipherment (Koot), grade C, not a period clear sheet; normalisations declared in the
  build script (umlauts, w -> u, König -> code 4000, editorial '(!)'/'(o)' dropped). The print's 'Wüfden' misprint left verbatim.
- Reference = the committed single reading (home advantage on segmentation, as spinelli and no.87).
- Requests 0 (images on disk); subagent calls: 2 Opus reader passes (one page each) + 1 Sonnet adjudication.
