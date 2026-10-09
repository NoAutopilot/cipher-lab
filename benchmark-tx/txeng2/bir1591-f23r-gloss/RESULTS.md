# TXP-B23 results: bir1591-f23r-gloss (fr.3623 f.23r, DECODE 9452) built and read once (9 Oct 2026, 15:52-16:1x UTC by date -u)

LANE TX-ENGINEER-2 round 0b item 1 (PREREG `benchmark-tx/PREREG-txeng2-0.md` 0b + Amendment 1). Order kept, each step committed
before the next: crops + reader brief 6969bc522, passA b59f6ed97, passB 5ec7f0a91, reconcile + queue f7852cb60, adjudication +
passZ f4a6170f6. Only after that: gloss crops 20c91b386, gloss reads (a9f2474d4 B, then A), gloss reconcile 6e2c6c431, then the
truth build and score b0d5cb04b. No reader saw the gloss, the truth, another pass or a decode.

## Headline (this leaf only, split eval)
| output | err_true (95%) | flagged excluded (strict recipe) | paired vs passZ (fixed/broken) |
|---|---|---|---|
| **passZ_pipeline (baseline)** | **0.079 (16/203) 0.049-0.124** | 0.000 (0/187) | -- |
| passA (Opus) | 0.084 (17/203) 0.053-0.130 | 0.005 (1/187) | 0 / 1 |
| passB (Opus) | 0.103 (21/203; 19 wrong, 2 deleted) 0.069-0.153 | 0.032 (6/187) | 1 / 6, p = 0.125 |

Top confusions on passZ (truth value <- read): e<-Q x3, a<-DTRIS x3, t<-M x2, then one each of d<-TRIS, i<-OS, d<-PSI, t<-O, c<-O.

**Read this before using the number.** The key is rebuilt from this leaf's own alignment to passZ (no outside key), so the
brief's recipe ("scored only when the chunk is the sign's majority value") makes passZ correct by construction on every
unflagged position: passZ's identity errors can only appear on the 16 positions where the gloss letter differs from the
passZ sign's majority value. The build scores those 16 too (flag `align-conflict`; the gloss letter has a supported
homophone set, so a wrong passZ sign or a decipherer slip). That interpretation is mine, not the brief's: under the strict
recipe (`--exclude-flagged`) passZ scores 0/187. So the unit's baseline E is 16 if the flagged positions are accepted as
truth, 0 if not. A verifier look at the 16 flagged positions in the crops would settle which; none was done here.

## Counts
330 positions (passZ). 203 scored (16 of them flagged align-conflict). 127 excluded: unaligned 68 (no gloss letter, e.g. the
struck sign L01.33 and stretches where the gloss is shorter than the cipher), low-agree 31 (ALPHA 0.36, CUP 0.40, XI, DOT, I,
NEW:phi 0.50: shape labels that lump two cipher signs), off-sheet NEW/? 24 (NEW:loop-x-tail, a frequent sign outside the seed
vocabulary, 15 aligned, rebuilt agree 0.93; plus NEW:phi, NEW:h-shaped hook, NEW:hook-crossed-tail, NEW:small-s),
multi-letter 3, key-conflict 1.
Pair agreement A/B 266/330 = 80.6% (nw); 64 disagreements + 83 agreed-uncertain went to the adjudicator (147 rows, 10 changed
from the first candidate). Part of the 19.4% is labelling convention, not reading: A wrote NEW:loop-x-tail where B wrote X for
the same looped x (20 disagreement rows); the adjudicator settled that by shape.
Alignment control (truth build): interlinear_align agrees 220/330 = 0.667; GAPS4 statistic real rebuilt key 0.559 vs 200
value-shuffled keys mean 0.040, max 0.091, rank 1 of 201.
Key rebuilt: 30 rows, 21 supported (n >= 2, agree >= 0.75, one letter, on-sheet) -> `key_rebuilt.tsv`. No key_print check
(rebuild only, per the brief).
Gloss: two blind Opus reads, difflib 57/67 words agree; 9 splits settled by one Sonnet look (gloss_splits_out.tsv), 4 of them
at conf L (G02 le/lle, G04 "q otto", G06 "Rialoni pougi", G08 numeral). Words written above another word (G01 Seri>uoce, G04
a>q) are kept in gloss.tsv's `above` column, not aligned.

## Unit power (tools/tx_power.py, 1000 draws, seed 1)
```
| b23 | 16 | 203 | 0.3 | 0.080 | 0.347 | ... |
| b23 | 16 | 203 | 0.5 | 0.592 | 0.893 | ... |
```
Alone (E 16) a clean 30% fixer passes p < 0.01 in 0.080 of draws: it counts in the eval pool, not alone, and only if the
16 flagged positions are accepted (E = 0 under the strict recipe).

## Crops (pasted)
Source: the DECODE 9452 copy `sources/decode/nevers-1590s-2026-10-09/IMG_R9452_I44643_P.jpg` (1600 x 2292); slip region
220,720,1200,590 (1200 px wide, signs about 20-25 px). The crops already on disk (`ciphers/fr3621-dinteville-1592/f3623/
f23r_L??_s?.jpg`) came from a Gallica native region (2950 px wide, higher resolution) but carry the gloss in full (two rows per
crop), so they were not used. Final command:
`python3 tools/iiif_lines.py --image sources/decode/nevers-1590s-2026-10-09/IMG_R9452_I44643_P.jpg --region 220,720,1200,590 --out benchmark-tx/txeng2/bir1591-f23r-gloss/crops --prefix f23r --max-width 1250 --overlap 300 --band-extent 0.05 --mask-neighbours --mask-keep 0.5 --follow-slope 150 --slope-local --overlap-note --debug --centres 45,80,127,145,177,203,237,255,297,313,347,383,400,437,463,493,520 --only-lines 3,5,7,9,11,13,15,17`
(17 centres given by eye = every gloss row and every cipher row as its own line; the cipher lines are bands 3..17 odd.)
crops_note.md:
> - f23r: each line is one crop (no segments, no overlap).

**gloss-visible: yes** (Amendment 1). The gloss is written tight above each cipher line and touches its signs. At
--mask-keep 0.6 or 0.75 the gloss went, but so did whole cipher signs joined to gloss strokes (e.g. a sign after "u" in
L04 and the first sign of L02). At 0.5 every cipher sign I checked stays, and gloss fragments ("lei", "q", "ando", "ronta",
"suur", "su la", "et", "den") stay legible above or below the signs. The readers were told that handwriting is not cipher.
Suggestion (not done, Usage 7): re-cut from the Gallica native region already on disk (2950 px), where gloss and cipher
strokes may separate better, then re-read.

## Protocol notes (deviations stated)
- Reader vocabulary: a value-blind shape list of 29 labels I drew from the scout row (blind_pass_brief_f23r.md) + NEW:<desc>;
  not the Birago 1572 sign sheet. The readers were told to label shape only and given no values.
- Adjudicator (Sonnet, adjud_task.txt): it reported that it viewed all 8 crops at 3x but did not inspect each of the 147
  signs individually; its `viewed` column says yes on every row, which it says overstates the check; where unsure it kept
  the first candidate (reader A's reading on disagreements). passZ therefore leans on passA.
- Gloss readers saw the cipher (the gloss crops and the slip image show both); the gloss is the truth side, so this does not
  leak anything to a cipher reader.
- Scoring the align-conflict positions is my reading of the brief's two sentences (the recipe vs "passZ's wrong-sign
  positions count"); the strict figure is beside it.
- Key family / split: entered as eval per the brief. Whether the fr.3623 1591 key is the Dinteville 1592 key (dev) or the
  Birago 1572 key (eval) was not checked: if it is the Dinteville key, the split straddles a family and the item moves to dev.

## Calls and cost
6 vision subagents: 2 Opus cipher passes (about 157k and 141k tokens), 1 Sonnet adjudication (about 119k), 2 Opus gloss
reads (about 118k, 128k), 1 Sonnet gloss look (about 106k). Dollar figure: the orchestrator's get_session reading.
