# TXV-SPIN: verifier pass on spinelli-c1519-confirm's six all-same-wrong positions (PREREG-txeng2-5 V2)

TXV-SPIN, a verifier session (account 4, Opus 5.5; never a solver or reader on this item), 9 Oct 2026 18:37-18:4x UTC by
date -u, for LANE TX-ENGINEER-2 incarnation 2. Sources: the line crops every pass saw (`benchmark-tx/txeng/confirm/crops/`,
cut from the Beinecke native page images `ciphers/spinelli-beinecke-c1515/images/beinecke3811294_p1_canvas10867298.jpg` and
`_p2_canvas10867299.jpg`), the readers' sheet `glyphs/atlas.png`, the 2017 plaintext (`verify2/cipherbrain_2017-03-24_tommaso.txt`
via `verify2/align_2017_signs.tsv`), `key.tsv` (Domnina 2016, H rows) and NOTES.md. No cipher sign was read beyond the six
positions; no instrument was run; tx_bench was run only on the baseline passZ_pipeline for the recount below.

Verdicts live in `benchmark-tx/spinelli-c1519-confirm.flags.tsv` and reach the truth through the flag column added to
`benchmark-tx/build_spinelli_confirm.py` (as `build_birago152.py`): the script regenerates the truth and its sha256;
`--check` exits 0. Truth columns 1-6 are byte-identical to the previous build; only the `flag` column was added.

## Verdicts (2 FLAG, 0 CORRECT, 4 KEEP)

| position | truth | committed | passes Z/A/B | verdict | region (crop pixels x0,y0,x1,y1) | reason |
|---|---|---|---|---|---|---|
| p1c_L01 5 | i | OMEGADOT | EIGHT x3 | **FLAG** reading-doubtful | p1c_L01_s1.jpg 1257,177,1335,292 | a figure-8 shape with its right stroke rising above the line: not OMEGADOT's omega-with-dots (g, 3/3 elsewhere), not any i-sign of the key (PHI_I, SEVEN_I, SEVENB); i comes only from the 2017 modern reading "li" (align class conflict), against image and committed code; an 8-family sign is o or r in the key, so not correctable from the image |
| p1c_L01 14 | h | ESS | SIX x3 (ERRORMAP: deleted) | KEEP | p1c_L01_s2.jpg 520,105,610,295 | h-shaped sign; ESS = h (H), 2017 "che", the earlier Opus pair's ESS (NOTES: "L1.25 ... ESS (reconciled SIX)"); the passes read it as SIX, they did not delete it |
| p1c_L01 15 | e | SEVEN_E | none (ERRORMAP: SIX) | KEEP | p1c_L01_s2.jpg 610,205,665,250 | the small 7 after the h; SEVEN_E = e (H), 2017 "che"; the passes dropped it. ERRORMAP's aligner put their SIX here and the deletion on pos 14 |
| p1c_L03 16 | p | TWO_P | THREE x3 | **FLAG** label-doubtful | p1c_L03_s1.jpg 1480,170,1600,250 (= s2 0,170,80,250) | Z-shaped zigzag; "di spagnia" forces p, and p is not in doubt. But the scored code set {TEE_P1, TWO_P} rests on TWO_P, a code used for this token only (the H38 shape sort). Both blind key-matching passes filed Domnina's P sign 2 under THREE (key.tsv THREE note). The sheet has no Z, so the image cannot settle whether this sign is TWO or THREE in the reader vocabulary |
| p1c_L03 25 | h | ESS | SIX x3 (ERRORMAP: deleted) | KEEP | p1c_L03_s2.jpg 1005,115,1080,275 | h-shaped sign; ESS = h (H), 2017 "che", earlier Opus pair's ESS (NOTES: "L3.24 ESS (reconciled SIX)"); the passes read it as SIX and read the barred d before it as PHI. ERRORMAP matched their SIX to the committed SIX at pos 24 (excluded) |
| p2c_L02 7 | n | DIAMOND | PHI x3 | KEEP | p2c_L02_s1.jpg 545,185,630,262 | rotated square with corner spurs, the atlas DIAMOND shape; DIAMOND = n (H), 2017 "andarai"; image, key and plaintext agree |

**The 2 deleted h: is the h inside the line band of the crop every pass saw?**
- p1c_L01 14: **yes**. The whole sign (ascender top to foot) sits at p1c_L01_s2.jpg x 520-610, y 105-295, inside the mask band (rows 82-336 of 418; manifest box 1400,-158,3000,335 of src_2_10867298_450_440_3000_1740.jpg).
- p1c_L03 25: **yes**. p1c_L03_s2.jpg x 1005-1080, y 115-275, inside the mask band (rows 82-326 of 408; box 1400,218,3000,694).
Both are not crop errors and not deletions. All three passes read each h as SIX; the deletion is where ERRORMAP's aligner put
the gap. In L01 the pass dropped the small 7 (pos 15) after the h. In L03 it placed the passes' SIX on the committed SIX at
pos 24, where the passes had read PHI. ERRORMAP's `crop` class for these two rows is wrong. They are sign substitutions h <- SIX.

**Finding for the lane (sheet, not truth).** The SIX row of the readers' sheet (`glyphs/atlas.png`, atlas v3) has an h-shaped
3rd exemplar, "-h>", from box p1_01_025, and that box is this item's own token p1c_L01 14. Its last exemplar ".h." is also
h-shaped. So the sheet taught the readers that the h-shape is SIX, and the sheet's ESS row shows only the "5"/S form. Two
more things, outside the six and not scored by this pass: (a) the same barred-d shape over 2017 'c' is committed PHI_T at
p1c_L01 13 and SIX at p1c_L03 24, both excluded rows; (b) by these verdicts, ERRORMAP's `e <- SIX` row is really a deletion of
SEVEN_E.

## Recount (baseline passZ_pipeline only; `tools/tx_bench.py benchmark-tx/outputs/spinelli-c1519-confirm/passZ_pipeline.tsv --bench BENCHMARK-TX.tsv --item spinelli-c1519-confirm --label-map benchmark-tx/txeng/confirm/collapse_map.tsv --exclude-flagged`)

| figure | err_true | errors | wrong | deleted | inserted | position errors (wrong + deleted) |
|---|---|---|---|---|---|---|
| as measured | 0.088 (17/193), 95% 0.056-0.137 | 17 | 12 | 2 | 3 | 14 |
| flagged excluded | 0.079 (15/191), 95% 0.048-0.126 [2 flagged] | 15 | 10 | 2 | 3 | **12** |

Both flagged rows were baseline errors (i <- EIGHT, p <- THREE). Eval pool, flagged excluded, counted as in Amendment 3:
eval_heldout 10 + spinelli **12** + f152r 1 = **23** (was 25). That is under 24, so Amendment 3's under-24 rule applies: no
eval look is spent until an eval item built under 0b's rules brings the pool back to 24 or more, and the branch does not
move. The lane writes Amendment 4.

## Files committed before any score (commit 727267c49301ed4ab6749b4cf95d8cda80aeb5fe, pushed to origin/main before the tx_bench run)

| file | sha256 |
|---|---|
| benchmark-tx/spinelli-c1519-confirm.flags.tsv | 1c56960bcdd042e62b2b6d9b1da71af6259e5eaac4ffedf8e625670c11d81bce |
| benchmark-tx/build_spinelli_confirm.py | a757400baa4a1cbb7bc0a11abaf53292d35a7f7620178adbe54d1ff7f4d8cf60 |
| benchmark-tx/spinelli-c1519-confirm.truth.tsv | a0901176cf86089a98180fd8d34550321917850c3ec7fd9d31fd24b6dca97659 |
| benchmark-tx/spinelli-c1519-confirm.truth.tsv.sha256 | fcb34d9b652887b573af9826884ed532eaceae93be3284f6190d6af288e6a666 |
| BENCHMARK-TX.tsv (spinelli row: truth sha256 updated) | 50552b1195692b017caaf0e5f0e8f470de5421adfde87cbf74b6e8505372f667 |

`python3 benchmark-tx/build_spinelli_confirm.py --check`: `spinelli-c1519-confirm: ok (sha256 a0901176...97659)`, exit 0.
Requests: 0 network. Subagents: 0.

Openings of eval truth: this job is a verifier pass on the eval item's truth (1)
