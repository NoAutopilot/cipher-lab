# Reconciliation of the transcription passes, Dupuy 468 f.28r-v (23 September 2026)

Material: 84 native-resolution line crops (images/crops/, cut by images/crop.py from the IIIF full/full images
of canvases 63 and 64) and the symbol legend images/crops/legend.jpg. Lines r02-r30 (recto) and v01-v11 (verso)
carry cipher. r00, r01 and v12-v18 are plain Latin and were transcribed by the reconciler only.

## Passes

| pass | who | rows | cipher tokens | gloss rows | file |
|---|---|---|---|---|---|
| A | Sonnet session, from the crops only | 815 | 677 | 122 | passA.tsv |
| B | Sonnet session, from the crops only | 782 | 642 | 163 | passB.tsv |
| R | reconciler (Opus), row by row from the crops, taller band views and zooms | 929 | 687 | 659 tokens under a gloss | ciphertext.txt |

A against B (reconcile.py, difflib alignment per line): token agreement 529 of 883 aligned rows (59.9%);
gloss agreement 10 of 153 glossed rows. Disagreement exceeded a tenth of rows on every line, so the third
reading covers all lines. It was made by the reconciler rather than a third Sonnet session, because the
disagreements were systematic legend errors (below), not random misreadings. R against A: 71.2% of R's
tokens matched; R against B: 70.8% (cmp3 alignment, scratch).

## Systematic causes (why A and B disagree with R)

1. **q and 9 are two signs.** The legend had one code, q. The page has an angular q with a flat top (e) and a
   rounder 9 whose descender curls left (l: multi, alij, filius, ligam, velle, nullus). A note to the running
   passes could not be delivered (the sessions could not be messaged). R codes 9 separately at 17 tokens.
2. **Po read as P.** Po (pi with a dot or small circle at the upper right, t) and P (pi with a foot bar, s)
   were merged by both passes at many places. The zooms at v02:8, v11:1, r21:2 and r19:10 show the dot or circle. R keeps them apart (Po 59, P 47).
3. **D read as T.** D (a loop with a small cross on top, m) was read as T (a T with a tick, d) at r06
   (x5), r12:18, r17:1 and r23:13. The zoom of r06 (commissionem, meam) shows the loop-and-cross shape.
4. **R read as T or P.** r10:2 and r17:5 are R (the looped fork shape).
5. **P standing alone.** The P-shape standing alone between clear words (r04:3, r04:25, r07:6, r09:1) was
   called II by both passes. It has the P shape; II (a box with separate verticals, x in auxilio r08:10) is
   different. R codes the standalone P as PW (a word sign, glossed mekleburg).
6. **Gloss offsets.** Both passes shifted gloss words by one to four tokens and often attached them to the
   wrong line. R places each gloss by eye over its tokens. key_from_gloss.py then checks every span
   letter for letter against the key, and a misplaced span shows up as an unaligned or minority vote.
7. **Crop geometry.** Lines slope down to the right by up to 90 px. The first cut (one centre per line,
   git f1fe9b1, which the passes used) clipped the right half of several recto lines. crop.py now uses
   separate right-half centres (RIGHT), and the committed crops are the recut. R was read from the recut and
   from taller bands (y-165..y+150).

All 35 positions where A and B agreed with each other against R were rechecked on the image: 17 on native
zooms (r04:3, r07:6, r14:5, r10:2, r17:1, r17:5, r27:2, v02:1, v02:8, r21:2, v11:1, r19:10, r06:11-22) and 18 on
the taller band views. All were kept as R. One of R's own readings was corrected on the zoom: r13:16 q to Y
(possunt).

## Symbol legend (codes in ciphertext.txt)

Letter signs: q, 9, V, Po, P, cc (the 'oe'-like joined cc), R and R2 (a curled variant, r06:2 and v08:8),
6, U, Y, D, L (lambda), 4, T, 3, +, 7, Z, Π (pi with no foot and no tick), II. Word signs: K (star, stroke
and small box), F, O (theta), PW (P-shape standing alone), SX (a looped sign, r03:24). Unexplained: g
(dumbbell, circle-stem-circle), o (small plain circle), HHH (a bar with three verticals, r03:23), Y~ (Y with a
tilde, r04:15), ß (a B-shaped mark, r19:18, also seen in clear text at r11 'ß ppß'). ?BLOT: an ink blot hides
the symbol (r08:16, r14:6, r29:3).

## Counts

929 tokens on 49 rows: 687 cipher tokens and 242 clear words. 31 distinct cipher symbols, plus the ?BLOT
placeholder. 659 cipher tokens stand under a gloss word; 643 of them align letter for letter with their
gloss word (key_from_gloss.tsv).

## Still uncertain on the image

r03:23-25 (HHH, SX, and a gloss read 'ma?ch??'); r04:15 (Y~) and r04:25 (PW, glossed 'dux'); r18:4 (a P-shape
where t is expected); r14:21 (Po where s is expected); r19:17-18 (the clear 'quoniam' and the ß mark); the
clear word r30:19 ('vri'?); v06:15 and v07:9 (a small Z after g). The gloss hand's reading of r03:23 was not
settled.
