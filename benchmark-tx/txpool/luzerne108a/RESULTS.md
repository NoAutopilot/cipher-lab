# TX-POOL-LEAF-2 results: luzerne108a-p1 (Huntington mssDE 108(A) p.1) built and read once (9 Oct 2026, 21:4x-22:0x UTC by date -u)

Brief .claude/briefs/runs/2026-10-09-account4-tx-pool-leaf-2.md (Amendment 1 of the TX-POOL-LEAF brief: the other solvers' solved
items), PREREG-txeng2-0 section 0b. Built by account 1 outside LANE TX-ENGINEER-2; the lane pools it (or not) under its own
Amendment. Credit: S. Tomokiyo (Cryptiana blog, 23 Sept 2021, "Decoded but not Identified Code of Luzerne", the Jan 1781 La Luzerne
code) and D. Bourdeau (dbourdeau/cyphersolver destaing/NOTES.md l.13, the same 1199-figure code); key and 108(B) gloss transcription
are this repository's own folder work. Order kept, each step committed before the next: CANDIDATES.md d5d849f65; crops + reader
brief d88823207; passA 8d9f02f69; passB 884537199; reconcile + queue 744cd84f5; adjudication + passZ 411685122. Only after that:
the truth build and the scores. No reader saw the gloss, the key, the decode, the truth or another pass.

## Headline (this leaf only, split eval)
| output | err_true as measured (95%) | flagged excluded (95%) | paired vs passZ |
|---|---|---|---|
| **passZ_pipeline (baseline)** | **0.094 (6/64) 0.044-0.190** | **0.000 (0/58) 0.000-0.062** | -- |
| passA (Sonnet) | 0.094 (6/64) | 0.000 (0/58) | 0 / 0 |
| passB (Sonnet) | 0.094 (6/64) | 0.000 (0/58) | 0 / 0 |
| committed (H reference) | 0.094 (6/64) | 0.000 (0/58) | -- |

**Read this before using the number.** Baseline E is **6 as measured, 0 flagged-excluded**, and the six are the six rows the build
flagged before any reader was scored, where every reader and the committed reference agree: 436 'nous' (the sibling key has 436 =
vous: align-conflict), and five `off-key-ref` rows where the gloss word is keyed to another code than the group on the leaf
(72 cent, 175 ce, 1167 ere, 1185 nul: homophones the 68/37/55 key lacks; 1195 'cette': an alignment shift, since 1032 = cette is not
in the independent key). So the measured errors are truth-side, not reading errors. **Under the brief's >= 8 rule this item misses
it both ways**: these 1781 clerk's figures read at 0/58 on the scored positions (A/B agreement 708/719 = 98.5% over the whole letter),
so the leaf adds no headroom to the pool. The lane may still want it as a digit-hand / numeric-code eval row; that is its call.

## Why p.1 only (independence)
The known text is mssDE 108(B), the Duplicata deciphered in ink by Destouches. Its gloss is in pairs_108B.tsv (R19, 24 Sept 2026),
but R19 read pp.2-6 "cross-checked line by line against key.tsv's existing values" (folder NOTES.md, R19), so only p.1 (read at
native resolution, and contradicting the key at 436 and 1188) counts as independent of the key. The key is restricted to the C rows
from the siblings' interlinear decipherments (mssDE 68/37/55): the 31 figures key.tsv took from 108(B), the R16 context fills and
the pencil rows are not used. Named next step to widen the item: a blind re-read of 108(B) pp.2-6's GLOSS ONLY (5 Sonnet calls, one
page each, the reader never shown key.tsv; about 2/3 of this job's reader cost), then `--pages` on the same build script. Given
0/58 here, that adds scored positions but probably few errors.

## Counts
115 positions (committed p.1). 64 scored (1 align-conflict, 5 off-key-ref flagged). 51 excluded: value-unkeyed 27, gloss-unread 19
('?', struck, punctuation or a '?'-marked gloss), multi-word 5. Pass agreement A/B 708/719 = 98.5% (nw, whole letter); 11
disagreements + 8 agreed rows with an alt or L conf went to one Sonnet adjudicator (19 rows; queue rule in make_queue.py).
Alignment control (truth build): share of keyed committed groups whose key value equals the aligned gloss, real 0.953 vs 20
word-shuffled glosses mean 0.245, max 0.312.
Truth sha256 cf477c2c0211e030ff7c4dc33e212b881dd45643c0df223da0ae3ec4202ac061 (`python3 benchmark-tx/build_luzerne108a.py --check`).

## Crops (pasted)
`python3 tools/iiif_lines.py --image ciphers/huntington-luzerne-destouches-1781/images/mssDE108A_p<N>.jpg --region <R> --out
benchmark-tx/txpool/luzerne108a/crops --prefix p<N> --max-width 1250 --band-extent 0.05 --mask-neighbours --mask-keep 0.5
--overlap-note --debug --distance 70`, regions p1 380,360,750,1180; p2 340,210,720,1270; p3 330,200,720,1230; p4 120,210,960,1230;
p5 340,200,790,1230; p6 240,210,860,850 -> 11/12/12/12/12/8 bands = the committed line counts. crops_note.md (manifest-generated,
pasted into the reader brief): "each line is one crop (no segments, no overlap)" for p1-p6. Readers read all six pages; only p.1
is scored.

## Caveats
- Correction to CANDIDATES.md's prior-work answer: 108(A) is not gloss-free. A few interlinear words (de, ri, e on p.1; 'les' on
  p.3) are written under some groups; the reader brief told readers to ignore words. They do not reveal figures.
- Reference = the committed H-graded reading (home advantage on segmentation, as no.87 and spinelli).
- A code with homophones scores value-level (any keyed code for the gloss word counts), as on no.87 and spinelli.
- Requests 0 (images on disk). Subagent calls: 12 Sonnet reader calls (2 passes x 6 pages) + 1 Sonnet adjudication.
