# The Mayenne polyphonic cipher (1592-93): a period key read from the family's own interlinear decipherments

F61-FAMILY, parent worker (Fable, session_015PuVvzMs61hNhz5J7XgmVR), 28 Sept 2026, 00:20-01:xx UTC. Key source
`period` (CLAUDE.md rule 10 vocabulary): every pair in `key_period.tsv` is read from a contemporary decipherment written
between the lines of a letter in this cipher, aligned to the atlas-coded signs -- grade C for the pair (rule 4), no
cryptanalysis, no refit on f.61. Tomokiyo's `mayenne.png` reconstruction (`../keys/key_mayenne_1592.tsv`) is a separate,
`published` key and is not used here; his `mayenne.htm` is credited for the family list (lines 38-66 of the mirror copy).

## The family (MANIFEST.tsv; every Gallica request in requests.log)

Eleven leaves Tomokiyo lists, three volumes, no folio labels on any manifest (canvases anchored by Sonnet looks at
1200-px thumbnails, at most three per volume, and one own look per fetched leaf at quarter scale):

| leaf | canvas | hand | decipherment on the leaf | fetched |
|---|---|---|---|---|
| fr.3982 f.97r (de Diou to Jeannin, 27 Oct 1592) | 202 | de Diou's secretary | none seen (38 lines of cipher) | native, kept as 1600-px reference |
| fr.3982 f.101r (Bishop of Lisieux, 27 Oct 1592) | 210 | Lisieux's secretary | **interlined throughout, about 60 lines** | native (not cut in this job) |
| fr.3982 f.124r (de Diou to Mayenne, 12 Nov 1592) | 256 by rule | de Diou's | partly interlined; folio read "121?" and date "7 nov." by the look, unresolved | native, 1600-px reference |
| fr.3983 f.106r (Mayenne to de Diou; headed "4 de mars 1593") | 191 | Mayenne's secretary | interlined, sparse, about 22 dense lines, heavy bleed-through | 1600-px reference (not cut) |
| fr.3983 f.108r (H19's leaf) | 195 | same | interlined (the runner's H21) | the runner's |
| fr.3983 f.108v (ends "De Soissons ce dernier jour de fevrier 1593") | 196 | same | interlined, sparse, two blocks | native, 7 bands cut, 4+2 passes |
| fr.3983 f.211r | 362 by rule | ? | one short glossed run per the look; content does not match Tomokiyo's row | 1600-px reference |
| fr.3984 f.176r (Desportes to Clement VIII) | 327 | Desportes | separate sheet (not located) | 1600-px reference |
| fr.3984 f.184r | 343 | clear | IS the separate-sheet decipherment of f.188 | 1600-px reference |
| fr.3984 f.186r, f.188r, f.189r | 347, 351, 353 | Desportes | none / f.184 / none | 1600-px references |
| fr.3984 f.274r (Lisieux to Desportes, Rome, July 1593) | 513 | Lisieux's secretary | **interlined, every line, neat** | native, 6 bands cut, 2+4 passes |

Note the folio/date mismatches against Tomokiyo's list (f.106 is headed 4 March, f.108v ends 28 February; f.124 read as
121 and 7 November): recorded as read, not resolved; an outward citation of these leaves needs the BnF finding aid.

## f.274r: how the key was read

1. Native leaf fetched once (`images/3984_f274r.jpg`, sha1 in MANIFEST.tsv). Cipher block region 2050,3260,2700,1040
   (six cipher rows, each with the decipherer's clear words written above it, plus three signs at the end of the clear
   line above, glossed "le", left out). Bands cut by `cut_bands.py` (per-segment centres, because the rows rise to the
   right: the first cut lost the right half of every gloss row and the two readers put segment-2 words on the wrong band;
   those two gloss passes are kept in `passes/f274_glossA/B.tsv` and voided -- the brief's crop error, not the readers').
2. Signs: two blind Opus passes with the f.61 atlas only (`passes/f274_signsA/B.tsv`), 167 rows each, reconciled by
   `tools/reconcile_passes.py` (nw): 149/167 = 89.2% identical. 12 of the 18 disagreements are one systematic split --
   the "2 joined to a crossed 4" sign, HASH4 for A, 4STEM (alt HASH4) for B -- which the gloss reads differently from
   the plain "#/4#" sign (i/x under the "24" sign, d/q under the plain one), so the (A, B) pair defines two classes
   here: HASH4 and **H24** (a new atlas row for this hand). The rest are VBAR_A/B and PHI/DBL alternations.
3. Gloss: two Sonnet passes on the recut sheets (`f274_glossA2.tsv`, `f274_glossB2.tsv`); segment-2 assignment still
   drifted in A2, so the reconciled word list (`passes/f274_gloss_rec.tsv`, 38 words, per-word sources) was settled by
   this session from the leaf itself: "[le] duc de feria a escript a quelques | cardinaux que ces affaires se |
   seschauffoyent par dela a leur aduantaige | plus quelles nauoyent encores | fait je croy que cest pour amuser le |
   monde comme ilz ont fait tousjours si vous ..." (the decipherer's words, not our reading; two words -- the second
   "a" of L01 and "le" at the end of L05 -- read only by the reconciler, grade M for the pairs they give).
4. Alignment: `tools/interlinear_align.py align --code-prefix @ --null-cost -1 --clear-consumes`, one pair per band
   (`passes/f274_pairs.tsv` -> `_align.tsv`, `_key.tsv`), 166 signs against 172 gloss letters: 102 tokens agree with
   their class's top meaning, 52 carry the class's second meaning (the polyphony), 11 null/unaligned. An independent
   placement by x position (`passes/f274_xcheck.tsv`) puts each gloss word over 0.7-1.3 signs per letter, i.e. the
   cipher is letter-by-letter with a few nulls and abbreviations (no word codes needed for these lines).

`key_period.tsv` (fr.3984 f.274r rows; `../keys/key_mayenne_1592.tsv` cell in brackets for comparison only):

| class | period letters (n) | table cell | note |
|---|---|---|---|
| PHI | e 24, r 11, o 7 | e/r | o: probably DBL (b/o) merged into PHI by the readers (B flags one alt DBL) |
| C43 | a 16, n 8 | a/n | |
| INF | u 16, h 1 | h/u | |
| VBAR_A | s 11, t 7, f 4 | g/t and f/s | the readers' VBAR_A takes f/s and g/t alike on this hand; VBAR_B f 1, s 1 |
| 4TRI | c 7, p 3 | c/p | |
| EBR | l 7, y 1, c 1 | l/y | |
| HASH4 | d 5, q 5 | d/q | plain "#/4#" sign |
| H24 | i 6, j 2, y 2, x 1 | i/x | "2 joined to a crossed 4" (new atlas row) |
| BETA | m 2, l 1, z 1 | m/z | |
| ELOOP o 1, OTHER t 2 | | | single counts, not used |

## Test on the two leaves the key was not read from (`test_period_key.py`, no refit)

| key | f.61 five known spans (55 letters) | 20 permuted keys mean / max | f.108r overlay (84) | mean / max |
|---|---|---|---|---|
| all pairs (n >= 1) | **43/55 = 0.782** | 0.214 / 0.382 | 52/84 = 0.619 | 0.215 / 0.369 |
| pairs with n >= 2 | 40/55 = 0.727 | 0.165 / 0.273 | 51/84 = 0.607 | 0.205 / 0.274 |

The brief's step-5 gate (0.75 on the 55 known letters) PASSES on the full key and MISSES by three letters on the
n >= 2 key; both sit at 2-3x the best permuted key. Coverage is the limit, not the pairs: the period key covers
0.56-0.62 of f.61's signs and 0.77 of f.108r's, because f.274's Lisieux hand does not use the classes CA, C6, LOOPBAR,
DBL, ZHOOK, VBAR_B, 4PI, CROSS that f.61's hand does.

## f.61r under the period key (`decode_period.py` -> `f61_decode_period.tsv/.txt`)

99 signs (the six span lines of `../scripts/passA_classes.tsv` and L02/L04/L10 of `passU2_classes.tsv`): 14 tokens
grade C (one period letter: u, t, l, m), 42 grade M (a period pair or triple, the choice by context NOT made here),
43 unread (no period pair for the class). Not a reading of the letter and not reading-ready: it is the C/M skeleton
a further gloss leaf (f.101r, 60 interlined lines in the same hand as f.274, or f.106r/f.108v in Mayenne's hand,
which carry the classes f.274 lacks) would fill.

## f.108v (Mayenne's secretary): held, not merged

Seven cipher rows cut (`sheets/f108vg_*`, per-segment centres after a first horizontal cut that both Opus readers
had to deskew themselves), two Opus sign passes 191/293 = 65.2% identical (systematic VBAR_A/VBAR_B, EBR/VBAR_B and
DBL/PHI splits), two Sonnet gloss passes mostly at confidence l (the gloss is tiny and cramped at 2x). The alignment is
run for the record (`passes/f108vg_*`) and its rows are written to `key_period_held.tsv`, not into `key_period.tsv`:
a unit whose own passes agree this poorly is held pending a 3x recut (CLAUDE.md rule 3, the Szembek per-unit lesson).

## What this changes for the campaign

The recovery route (period gloss -> key -> f.61 as key application) works on this family: one glossed leaf of 166
signs, read blind and aligned by the shared tool, reads f.61's known letters at 0.73-0.78 with no fitting. The next
cheap steps are new CAMPAIGN.md rows: f.101r bands (the same hand, ten times the material), f.106r/f.108v at 3x for
the missing classes, and the f.188/f.184 pair (separate-sheet decipherment, Desportes' hand). Nothing here is called
solved, new or first; the counts are what a verifier would check.

## f.101r (F61-FAMILY-2, 2026-09-28 01:56 UTC): the same hand, ten times the material

fr.3982 f.101r, Lisieux's secretary again, 46 cipher rows each with the decipherer's clear line above it. Cut by hand-set
centres (both automatic detectors locked onto the gloss rows here), 230 crops at 2x (sheets/f101r/, sample and boxes
committed, regen recipe in MANIFEST.tsv). Two blind Opus sign passes per chunk of 8 bands, 80.2% identical over 3,081
aligned columns after the atlas gained three rows this hand needed (LOOPS = a stemless loop chain, ZBAR = a z with a bar,
RSIGN = a small r-like hook; passes/PROMPTS_f101r.md); two blind Opus gloss passes, 72.4% identical by word (the brief's
Sonnet passes read this hand at 25% and were replaced before chunk 2). Alignment as for f.274 (align_period.py), 3,077
tokens, 288 rows -> `key_period_f101.tsv`; merged with f.274's rows into `key_period_v2.tsv` (merge_period_keys.py, both
leaves' rows kept, nothing summed, conflicts in the header).

| class | f.101r period letters (n, of class total) | f.274r | table cell | note |
|---|---|---|---|---|
| PHI | e 350, r 127, o 101 (742) | e 24, r 11, o 7 | e/r | o = DBL (b/o) merged by the readers, both leaves |
| 4TRI | n 140, a 121, c 45, p 34 (438) | c 7, p 3 | c/p | this hand's readers put the "43" sign into 4TRI: a/n + c/p |
| VBAR_A | t 138, s 93 (368) | s 11, t 7, f 4 | g/t and f/s | |
| LOOPS | u 158, o 31 (263) | -- | h/u | new atlas row; the h/u sign of this hand (f.274's INF, u 31 here too) |
| H24 | i 170 (235) | i 6, j 2, y 2 | i/x | |
| EBR_B | l 104 (146) | EBR l 7 | l/y | |
| HASH4 | d 43, q 24 (108) | d 5, q 5 | d/q | |
| C43 | a 35, n 33 (76) | a 16, n 8 | a/n | |
| 4STEM | n 13, a 12, c 10, e 9 (77) | -- | -- | a third 4-shape merge; see H40 |
| EBR_A | s 18, l 13, a 8 (62) | -- | f/s | |
| BETA | m 31 (52) | m 2 | m/z | |
| ZBAR | s 26 (49) | -- | f/s | new atlas row |
| VBAR_B | s 27 (35) | f 1, s 1 | f/s | |
| INF | u 31 (35) | u 16 | h/u | |
| DBL | e 10, r 6, u 6 (29) | -- | b/o | too mixed to use at n >= 10% |
| 4PI | d 5, n 3, q 2 (15) | -- | d/q | |
| RSIGN | m 11, t 5 (30) | -- | m/z | new atlas row |
| C6 | e 2 (2) | -- | | too few |

Every class the two leaves share gives the same top letters, read blind on each leaf by different sessions with no key in
the prompt: the same secretary's decipherment is consistent across the two letters, and the pairs are the polyphonic cells
of Tomokiyo's table (compared only after the fact). The reader merges (4TRI taking a/n, 4STEM taking a/n/c) are the readers'
class boundaries on this hand, not the key's: a blind shape sort of the 4-shaped signs (H40) is the next step before the
family key is refined further.

Tests, no refit (`test_period_key.py --key key_period_v2.tsv --collapse-ebr --min 2 --frac 0.1`, 20 permuted keys): f.61
known spans 43/55 = 0.782 (permuted mean 0.344, max 0.618), f.108r 65/84 = 0.774 (0.317 / 0.488); f.61 signs covered 0.80
(was 0.56). Without the 10%-of-class rule the letter sets are wide enough that a permuted key reads 0.818-0.836 of the known
letters, so the plain n >= 1 / n >= 2 figures (0.855 / 0.800) are not tests at this N. Still uncovered on f.61: CA, LOOPBAR,
ZHOOK (plus CROSS, LL); C6, DBL, VBAR_B, 4PI now covered. `f61_decode_period_v2_frac0.1.txt`: 99 signs, C 15, C+ 8, M 56,
unread 20 -- a skeleton, not a reading.

## f.188/f.184 (F61-FAMILY-3, 2026-09-28 02:2x UTC): the separate-sheet pair, Desportes' hand

fr.3984 f.188r (Desportes to the Bishop of Lisieux, Paris, 22 July 1593) is not a "cipher block": its 48 lines mix clear French
and cipher runs from row 10 to row 47, and fr.3984 f.184r is the whole letter in clear (40 lines, the deciphered stretches
loosely underlined -- the underlines cover whole passages, not the cipher runs exactly, so they are a check, not the
alignment). Both leaves refetched native (2 Gallica requests, requests.log), sha1 unchanged from the 00:28 fetch. Rows 13-35
of f.188r cut as 23 bands (sheets/f188r, `cut_bands.py`, hand-set centres from the ink-row profile, 5 segments of 1520 x 216
px at 2x); f.184r cut as 12 strips x 2 halves at native scale (sheets/f184r_strips.json). Prompts in
passes/PROMPTS_f188_f184_f106.md, written before any call.

Passes: two blind Opus sign passes per chunk of 8 bands (6 calls; A 1194 rows, B 1159; 936/1206 aligned columns identical =
77.6%, bands under 70%: L01, L10, L15, L23), two blind Opus clear passes of f.184r (2 calls; 40 lines each; 803 words
identical of 839/842 = 95.5%, underline flag agreement 787/803). Alignment by `align_separate.py`, the separate-sheet mode
the brief asked for, recorded here as the rule: (1) the PLAIN words the sign passes read inside the cipher lines are
anchored monotonically onto the clear copy's words (length-weighted similarity, words under 3 letters never anchor; one
off-trend anchor dropped, a junk word matched 276 words away); (2) between two anchors the clear words are split among the
bands' runs in proportion to their token count (about one letter per sign, the cipher is letter by letter), the open-ended
spans before the first and after the last anchor capped at 1.0 letters per token; (3) one pair per band to
`tools/interlinear_align.py --code-prefix @ --null-cost -1 --clear-consumes`, as for the interlinear leaves. 56 of 131 clear
words anchored; letters per unit of cipher weight 0.76-1.49 per band, no band outside the drop window; L23 dropped by hand
(its crop was cut at the bottom edge: the region ended 4 px below the row centre, the brief's error, both readers reported
it). `key_period_f188.tsv`: 186 rows, 23 classes, from bands L01-L22 (1,006 signs).

| class | f.188 period letters (n) | f.274r | f.101r | table cell |
|---|---|---|---|---|
| PHI | e 133, r 51, o 37 | e/r/o | e/r/o | e/r |
| VBAR_A | t 41, e 4, g 3 | s/t/f | t/s | g/t |
| EBR_B | l 41, s 3 | l | l | l/y |
| H24 | i 33, j 3 | i/j | i | i/x |
| VBAR_B | s 30 | f/s | s | f/s |
| LOOPS | u 29, v 3 | -- | u/o | h/u |
| ZBAR | s 28, f 5 | -- | s | f/s |
| C43 | n 27, a 24 | a/n | a/n | a/n |
| 4TRI | c 23, p 19, n 9 | c/p | n/a/c/p | c/p |
| INF | u 21, e 4, h 3 | u/h | u | h/u |
| 4STEM | n 15, a 12 | -- | n/a/c/e | -- |
| HASH4 | d 12, i 10, q 3 | d/q | d/q | d/q |
| 4PI | d 9, a 5, q 2 | -- | d/n/q | d/q |
| BETA | m 9 | m | m | m/z |
| OTHER | q 14, p 4 | | | (the readers' uncoded 'q'-sign of this hand) |
| CA 3, LOOPBAR 1, ZHOOK 0, CROSS 0, LL 1 | | | | not attested: Desportes' hand does not use them either |

Read blind by a third session on a third hand with a different kind of decipherment (a separate clear copy, not an
interlinear gloss), every class shared with f.274r/f.101r gives the same top letters, and the H30 gate (top-2 agreement on
the classes shared with key_period.tsv's f.274 rows: PHI, C43, INF, VBAR_A, 4TRI, EBR, HASH4, H24, BETA) is met on all nine
(INF's second letter e 4 vs h 3 is the one near-miss). Conflicts recorded by merge_period_keys.py (v3 header): 4TRI (f.101r's
readers merged a/n into it), C43 n-vs-a (a coin toss on every leaf: the a/n cell), VBAR_A s-vs-t (f.274 only), CH, RSIGN, OTHER.

## f.106r (F61-FAMILY-3, 2026-09-28 02:2x UTC): held

fr.3983 f.106r (Mayenne's secretary, headed 4 March 1593), first six cipher rows cut at 3x (sheets/f106r, region
1540,600,3060,900, hand-set centres, 7 segments of 1560 x 360 px). Two blind Opus sign passes: 204/240 = 85.0% identical
(L01 0.92 .. L05 0.76) -- this hand IS readable at 3x, the H29/H35 question. Two blind Opus gloss passes: 20 words identical
of 58/60 = 33.9% (per band 0/8 to 5/11), both passes mostly '?'-marked at confidence l: the gloss is tiny, cramped between
rows and half hidden by the verso's bleed-through. Under the brief's gate (60% on words) the leaf is HELD: no rows merged;
the alignment is run for the record only (`key_period_f106_held.tsv`, 109 rows, 15 classes, not used by v3). Its sign
inventory (PHI 71, VBAR_A 33, HASH4 26, C43 21, H24 20, 4STEM 20, 4TRI 13, EBR_A 6, ISH 5, BETA 5) carries none of CA,
LOOPBAR, ZHOOK either. What would settle it: a gloss pass on crops cut around the gloss row itself (up 40 / down 25 around
the gloss, not the cipher row) at 4x, or a person's reading of the six glosses; the sign passes need not be repeated.

## v3 (F61-FAMILY-3): three leaves, three hands, two kinds of decipherment

`key_period_v3.tsv` = f.274r + f.101r + f.188r/f.184r rows (merge_period_keys.py, 511 rows, 24 classes, 6 top-letter
conflicts in the header, none resolved by preference). Tests, no refit (`test_period_key.py --key key_period_v3.tsv
--collapse-ebr --min 2 --frac 0.1`, 20 permuted keys): f.61 known spans 43/55 = 0.782 (permuted mean 0.372, max 0.618),
f.108r 66/84 = 0.786 (0.344 / 0.512; was 0.774 under v2); f.61 signs covered 0.80, uncovered CA, CROSS, LL, LOOPBAR, ZHOOK --
unchanged from v2, because none of the three glossed hands writes those signs (f.106r's first rows do not either). The
every-class condition for a reading-ready line therefore still FAILS. `f61_decode_period_v3_frac0.1.txt`: 99 signs, C 10,
C+ 4, M 65, unread 20 -- fewer C than v2 (15) because f.188 attests a second letter at over 10% in INF (e) and 4STEM, so
those tokens are now honestly M. The remaining route to the five uncovered classes is not another glossed leaf of this family
(all five glossed leaves are now read or held and none carries them): it is f.61's own context (H33, run on this skeleton),
or a period key sheet, or the classes being this hand's variants of covered signs (H40-style blind sort of CA/LOOPBAR/ZHOOK
crops against the covered classes -- not attempted here, not in the brief).
