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

## The undeciphered leaves (F61-FAMILY-4, 2026-09-28 03:4x UTC): two of the four are glossed

On the native images fr.3982 f.124r (de Diou to Mayenne, headed "7 de Nove[mbre] 1592") is interlined THROUGHOUT -- 45 cipher rows,
each with the period decipherer's clear line above it -- and fr.3982 f.97r (de Diou to Jeannin, 27 Oct 1592) is interlined throughout
too (about 38 rows); the family table's "partly interlined" / "none seen" came from 1200-px thumbnails. That makes a FOURTH glossed
hand (de Diou's secretary) with about 5,000 signs between the two leaves. fr.3984 f.186r and f.189r (Desportes) remain the family's
undeciphered leaves; they were not cut in this job (H48).

f.124r signs: 45 bands at 2x (sheets/f124r; hand-set centres from a long-stroke profile, the ink-weight detectors lock onto the gloss
rows on this leaf as on f.101r; `cut_bands.py --track 18` drifted one row at s5 on L27-L30, those four crops are held out), two blind
Opus passes per chunk of 8 with the f.101r atlas unchanged (passes/PROMPTS_undec.md), 2387/2839 = 84.1% identical (0.70-0.94 per band),
`passes/recf124r/ciphertext_draft.tsv`. Class inventory of the draft: PHI 705, VBAR_A 419, 4TRI 245, H24 232, C43 205, LOOPS 195,
EBR_B 175, HASH4 141, OTHER 151 (this hand's word-code sign), 4STEM 84, ... and of the rare classes only LOOPBAR 3, CROSS 3, CA 1,
ZHOOK 1: de Diou's hand does not write f.61's five uncovered classes either.

f.124r gloss: HELD (`key_period_f124_held.tsv`). Two blind Opus gloss passes agree on 42% of words over 24 bands (2x cipher-centred
bands 49%/43% on chunks 1-2; a gloss-centred 3x recut, the H41 recipe, 36% on chunk 3; both readers mostly '?' at confidence l) --
under the family's 60% gate, and the alignment of the agreed words alone is flat (top-letter share 0.205). Yet band L01 (82% word
agreement) reads under key_period_v3 with no refit: "auant" C43 LOOPS C43 C43 VBAR_A, "la lettre" EBR_B C43 EBR_B PHI VBAR_A VBAR_A PHI
PHI, "escrite" PHI VBAR_B 4STEM PHI H24 VBAR_A PHI, "luy" EBR_B LOOPS EBR_B, "aye" C43 EBR_B PHI, "este" PHI VBAR_B VBAR_A PHI, "rendue"
PHI PHI C43 4STEM LOOPS PHI, and the readers' OTHER takes "que", "Mons[ieu]r", "m'" whole. So (1) the family key applies to the fourth
hand, (2) the leaf is a letter-by-letter interlinear decipherment with word codes, (3) the readers' EBR_B is l/y and LOOPS u/v here as
on f.101r, and (4) the hold is the gloss READING, not the leaf: H46 names the recipes to try. Tool note: `tools/interlinear_align.py`
in `--code-prefix` mode gives every code at most one letter, so a word-code OTHER pushed its letters onto the neighbours and flattened
the key; `align_period.py --numeral-other` (OTHER as an above-floor Thurloe numeral) and `--wild-disagree` (disagreed words as `?`
wildcards) are the fix, off by default.

Under v3, `decode_leaf_period.py f124r`: 2,782 signs, covered 0.939, firm 0.061 (C 6, C+ 163, M 2,444, unread 169) -- the skeleton of
the leaf, the same polyphonic pairs as f.61's.

## Rare classes (F61-FAMILY-4, 2026-09-28 03:42 UTC): untestable by context inference at this coverage

CA, LOOPBAR, ZHOOK, CROSS, LL occur 78 times across f.61r, f.108r, f.101r, f.188r, f.108v and f.124r (`rare_contexts.tsv`; 20 of
f.61r's 99 signs but a handful on every other leaf, 8 on f.124r's 2,782). The brief's H16-shaped inference -- a blind Opus text judge
proposing letters from the French around each occurrence, 21 sets with the contexts re-dealt among the classes at random -- was gated
on a positive control first (`rare_classes.py build control`: HASH4 d/q, BETA m, INF u hidden from the key, 20 contexts each): the
judge ranks the true set 13 of 21 and proposes the same filler letters (d, l, m) for all three labels, missing INF's u. FAIL, so the
target call was not spent and no grade-S row exists (`rare_classes.tsv`). The reason is structural: rendered under v3 the neighbours
are period pairs for nearly every class, 0-1 firm letters per context, so there is no French to read -- H33's limit met from the class
side. What would test it: firm neighbours (the polyphonic cells resolved, H24/H40) or a period source that writes these signs (none of
the five glossed hands does; H43's blind shape sort against the covered classes remains the open route, and H44's published-table
check is script-only). The scattered n = 1 gloss tokens (CA c/q/s/t/p, ZHOOK a/e/r and f.108v's held a 7 / e 4 / u 4, LOOPBAR e/u,
CROSS p, LL e) are listed in rare_classes.tsv for the record and used by nothing.


## de Diou's gloss hand (f.124r, f.97r): a letter-aligned recipe, held after its own control (F61-FAMILY-5, 28 Sept 2026)

H45 left f.124r's gloss HELD at 42% word agreement. The brief's recipe: read the gloss AS LETTERS ALIGNED TO SIGNS. Segments of
8 signs were cut from the native leaf at 3x (`cut_segments.py`: cipher centre - 82 to + 42 native px, a white strip under the crop
with a numbered red tick at every sign's x, the x recovered per draft position from pass A or B), and each blind Opus reader was
given the image plus the v3 skeleton of the segment (the period letter SET per position, `?` where none). Control design: 40% of
the covered positions were hidden as `?` (seed per segment) so that a reader cannot tell a hidden covered position from a truly
uncovered one; agreement on the hidden positions measures reading, not copying (`sheets/f124s_segments.json`, `score_letters.py`,
`place_letters.py`). Prompts in `passes/PROMPTS_f124r_gloss.md`, written before every call; the exact texts in `passes/prompts_f5/`.

| form | unit | hidden positions in the v3 set (A / B / where A = B) | shown positions | word agreement A vs B |
|---|---|---|---|---|
| letter per tick (c0, 8 segments of L01-L02, 62 rows per pass) | one letter above each tick | 12/32 = 0.375 / 10/32 = 0.312 / 9/23 = 0.391 | 0.536 / 0.536 | (34/51 positions identical) |
| word with tick span (same segments, the one knob change; letters placed by a monotone DP that scores +1 for a letter inside a shown set, 0 at a hidden or uncovered position) | word + first/last tick | 14/32 = 0.438 / 12/32 = 0.375 / 11/20 = 0.550 | 0.571 / 0.500 | 10/25 = 0.400 |

Gate 0.8 on the hidden positions: FAIL both forms; the shown positions -- where the reader holds the answer set -- pass no better
than 0.57, and the word agreement (0.40) is H45's 42% again. Why (from `sheets/f124s/f124s_L01_g8.jpg`, looked at by this session):
the decipherer writes each clear word compactly over a span of signs ("tisfaict" over four struck signs, then a dash), so a letter
does not sit above each sign, and the words themselves ("?rie"/"?ue", "estr"/"astr", "fin ss?r"/"tiu sse d?") are read differently
by two readers at 3x with the signs marked. Per the brief (one knob, then hold) no target gloss call was spent on either leaf and
no key rows come from de Diou's gloss: `key_period_f124_held.tsv` stands, no `key_period_f124.tsv`/`key_period_f97.tsv`, no v4.
The readers' word files are kept (`passes/f124s_letters*_c0.tsv`, `passes/f124s_words*_c0.tsv`, `passes/f124s_placed_c0.tsv`) and
used by nothing. What would settle it: a person's reading of six f.124r rows as a known-answer control (H46 option b), against
which a reader's word list can be scored before any further gloss call; or a 4x recut of the gloss row alone with a word-level
gate -- not a third pass at the same 3x segments (CLAUDE.md rule 3, the "same knob" lesson).

f.97r (H47, same job): signs read, gloss not. 42 cipher rows recut by `chain_rows.py` (rows chained per segment column
after the fixed-centre and --track cuts drifted on this leaf's curving rows), two blind Opus sign passes per chunk, 2,485
signs at 73.2% agreement (`passes/recf97r/`), under v3 covered 0.970 / firm 0.091. Rare classes on the leaf: 20 of 2,424
(CA 8, CROSS 7, LOOPBAR 3, ZHOOK 1, LL 1); the family census (`rare_contexts.tsv`, seven leaves) is 98: CA 31, ZHOOK 35,
CROSS 15, LOOPBAR 14, LL 3, of which f.61r alone carries 20 of its 99 signs. De Diou's two leaves therefore add no period
reading for the five classes even if their gloss were read: they hardly use them.

## v4 (F61-FAMILY-6, 28 Sept 2026, 15:06-15:3x UTC): the four tile-sort splits applied to the family passes

Parent worker F61-FAMILY-6 (Opus 5.5, session_01TPNoYGTE6dLBPfyEgZTLAc), campaign row H52 widened. The runner's blind tile
sorts (H65/H67 SBS b/o, H69 4TRI c/p vs the 4-with-hook a/n, H70 VBAR s/t, H77 LOOPS = SBS o + INF u; controls H71/H73/H75
failed as they should) showed that four of the family readers' classes each merged two glyphs. Key source stays `period`;
Tomokiyo's table stays `published` and separate (`key_published_rare.tsv`, `../keys/key_mayenne_1592.tsv`), used by nothing here.

**Re-coding (`recode_split.py`, design pre-registered in its docstring and pushed with the sheets, 58d4c7f0, before any call).**
Five blind Opus shape sorts (cap 6), one per leaf and shape family, prompts in `recode/PROMPTS.md`. The labelled anchors are
the runner's own H65/H67/H69/H70/H77 tiles of the same leaf whose blind group and period letter agree, re-cut from the native
leaves exactly as the runner cut them and shown as "form 1/2/3" (no letters); max(2, ceil(n/10)) anchors per class were
held out and mixed, unlabelled, among the query tiles as the check (gate 0.80 per class). The query is a stratified sample
(stratum = leaf, reader class, period letter, letters under 8% pooled; up to 20 sorted tokens per stratum, the runner's
earlier tiles counting toward the 20 by their own blind group); key rows are stratum-weighted estimates, `bands` = "est from
k sorted tokens". Native f.101r and f.188r fetched once each (2 Gallica requests, requests.log; f.188r's byte stream,
sha1 d6c5b0a1..., differs from MANIFEST's 00:28 sha1 at the same class of server re-encode F61-FAMILY-4 recorded; the
H65-H77 anchors re-cut from it were recognised on every held-out tile), not committed.

| call | forms | held-out check | query tiles (none) | result |
|---|---|---|---|---|
| f101r_loops | PHI / SBS / INF | 2/2, 4/4, 2/2 | 67 (10) | split applied |
| f101r_4tri | 4TRI / 4HOOK | 2/2, 2/2 | 84 (9) | split applied |
| f101r_vbar | VBAR_A / VBAR_B | 2/2, **1/2** | 21 (5) | **STOPPED**: VBAR_B below 0.80; VBAR_A keeps its v3 rows (t 138, s 93 ...) |
| f188r_loops | PHI / SBS / INF (INF anchors from f.101r's hand) | 2/2, 2/2, 2/2 | 78 (1) | split applied |
| f188r_4tri | 4TRI / 4HOOK | 2/2, 2/2 | 25 (0) | split applied |

The held-out checks are small (2-4 tiles per class, the brief's tenth of 4-30 anchors): 1.00 on four calls says the reader
reproduces the runner's groups, not that every query tile is right. f.188r's readers already code VBAR_A (t 19) and VBAR_B
(s 27) apart, so no VBAR sort there. f.274r has no x positions (its align lines do not equal its draft): its PHI, 4TRI,
VBAR_A, VBAR_B rows (14) are dropped from v4 as unsorted merged codes, its other 23 rows kept (`key_period_f274_v4.tsv`).
Per-token recoding: `passes/f101r_align_v4.tsv`, `passes/f188r_align_v4.tsv` (column `split_v4`: the sorted class, `unsorted`
for a token outside the sample, `=` for an unaffected class); the sign passes A/B themselves are unchanged. Result and
per-class estimates: `recode/heldout.txt` (`recode_split.py score --check`).

Per-leaf estimates of the split classes (letters with estimate >= 1; readers' own INF rows summed in):

| class | f.101r (sorted tokens) | f.188r (sorted tokens) |
|---|---|---|
| PHI (trefoil) | e 198, r 75, u 18, b 12, l 8, o 7 ... (50) | e 56, r 23, q 5 ... (40) |
| SBS (side by side) | o 79, b 37, e 22, u 6 ... (42) | o 19, b 12, e 9, u 4 ... (36) |
| 4TRI (4 over triangle) | c 26, p 25, d 10, n 10, a 9 ... (48) | c 11, p 10, t 3 ... (30) |
| 4HOOK (4 with hook / r-stroke / loop) | n 73, a 69, then 7 or fewer (42) | n 7, a 5 (12) |
| INF (+ LOOPS sorted as INF) | u 130, h 10 ... | u 31, e 4, h 3, r 3, v 3 ... |

SBS's e (f.101r 22, f.188r 9) is four earlier-tile misfits (H65/H67 group A under e, two per leaf) times the PHI-e stratum
weight (about 11 on f.101r); it is the sort's own error rate carried by the pre-registered estimator, not a period
attestation, and it keeps SBS three-way (o/b/e) under the n >= 0.1 x leaf-total rule. Not re-tuned.

**key_period_v4.tsv** = f274_v4 + f101_v4 + f188_v4 (`merge_period_keys.py`, 459 rows, 25 classes; header conflicts 4: C43,
CH, OTHER, RSIGN -- the 4TRI and VBAR_A conflicts of v3 are gone, VBAR_A because f.274r's rows left, not because of a split).
Under the tests' rule (n >= 2, n >= 0.1 x leaf class total): PHI e/r, SBS b/e/o, 4TRI c/p/t, 4HOOK a/n, INF u, VBAR_A s/t,
VBAR_B s; the rest as v3.

**Tests, no refit** (`test_period_key.py --key key_period_v4.tsv --collapse-ebr --min 2 --frac 0.1 --sbs --perms 200`; `--sbs`
applies H26/H51's loop relabel on f.61r and f.108r via `sbs_relabel.py`, H27's EBR relabel not applied; `--perms 200` is new):

| key | f.61 five spans (55) | 200 permuted: mean / p95 / max, >= key | f.108r overlay (84) | 200 permuted: mean / p95 / max | f.61 coverage |
|---|---|---|---|---|---|
| v3 (same 200 perms) | 43/55 = 0.782 | 0.338 / 0.509 / 0.618, 0/200 | 66/84 = 0.786 | 0.324 / 0.452 / 0.512 | 0.80 |
| **v4** | **48/55 = 0.873** | 0.319 / 0.436 / 0.527, 0/200 | 65/84 = 0.774 | 0.303 / 0.393 / 0.476 | 0.80 |

Per span v4: S1 3/4, S2 9/10, S3 11/12, S4a 4/7, S4b 11/11, S5 10/11. f.108r loses one letter (T1 31 -> 30). Coverage
unchanged: CA, CROSS, LL, LOOPBAR, ZHOOK still carry no period pair (none of the glossed hands writes them).

**f.61r under v4** (`decode_period.py --key key_period_v4.tsv --frac 0.1 --sbs` -> `f61_decode_period_v4_frac0.1_sbs.tsv/.txt`):
99 signs, **firm 20 (C 10, C+ 10) / two-way-or-wider M 59 / unread 20**, against v3's 14 / 65 / 20. Letter-set sizes among the
M tokens: v3 two 19, three 35, four 9, seven 2; v4 two 36, three 18, four 3, seven 2. Every sign that moved (42 of 99):

| moved | n | positions | why |
|---|---|---|---|
| INF u/e M -> u C+ | 6 | L01/4, L05/10, L07/8, L08/4, L08/8, L10/8 | LOOPS tokens sorted INF raise INF's total, so f.188r's e (4) falls under 0.1; u on two leaves |
| PHI e/r/o -> e/r | 17 | L01/5,9; L02/1; L03/4; L05/4,15,17; L08/1,6,12,13,14; L10/3,5; L11/2,4,7 | o leaves PHI with the SBS tokens |
| PHI e/r/o -> SBS o/b/e | 3 | L07/7, L10/6, L10/11 | H26 blind group G2 on f.61 (sbs_relabel) |
| DBL e/r/u -> SBS o/b/e | 4 | L03/14, L05/5, L08/5, L11/10 | f.61's pass-A DBL is the side-by-side glyph (H26/H51) |
| 4TRI n/a/c/p -> c/p/t | 6 | L01/6, L03/7,10, L05/6,14, L08/11 | a/n leave with the 4-with-hook tokens; t is f.188r's 3/30, at the 0.1 line |
| VBAR_A t/s/f -> t/s | 6 | L01/10, L03/6, L05/3, L10/4, L11/6,12 | f.274r's merged rows dropped (its f 4); NOT the s/t split, which stopped |

The .txt of v1-v3 is regenerated for one display fix: a C+ token was printed as `<CLASS>` like an unread sign (the .tsv and
the header counts were always right). Not a reading of the letter; the choice inside every M set is not made here.

## key v5 (F61-FAMILY-9, 29 Sept 2026, 01:1x UTC): four cells from the fr.3984 f.176r / fol. 177r decipherment

`build_key_v5.py` (with `--check`) writes `key_period_v5.tsv` from `key_period_v4.tsv` (not edited) and `key_period_f176.tsv`
(H177, runner 6), taking only the four rows VERIFY-F61-V5 endorsed (AUDIT.md, section VERIFY-F61-V5; `verify_v5/`). Each changed
class's v4 rows stay in the file as `#superseded-v4` comment lines; the new rows are `CELL` rows, which are the class's whole letter
set and are exempt from the 0.1 x leaf-total rule (that rule would cut the cell partner: g 10 of 110, x 3 of 31, b 6 of 64). Read
v5 with `build_key_v5.load_key_v5()`, not `test_period_key.load_key`. Key source of every CELL row: `period` (fr.3984 f.176r,
Desportes to Clement VIII, 22 July 1593, deciphered on fol. 177r), cross-checked on the Mayenne hands against Tomokiyo's published
letters (`published`, credited) and f.108v's sequence gain.

| class | v4 | v5 | rows (f.176r counts, fol. 177r clear folded j=i v=u y=i) | provenance |
|---|---|---|---|---|
| VBAR_A | s/t | **g/t** | t 100, g 10 (code VBAR_A) | cell 0.55 vs wrong text 0.20; blind 14/26, 18/33; f.108r t5 g2 7/7 (p 0.005); grade C on f.61 with VERIFY-F61-V4's caveat on the VBAR_A/VBAR_B boundary |
| EBR_B | l (v4 rows l, y, s...) | **l/y** | l 95, y 10 (code EBR; the y row is the folded i/y count) | f.176r brackets are form B (H180, 11/11); cell 0.67 vs 0.18; f.61's brackets are all form B (H22 4/4), so f.61's EBR takes l/y at C. EBR_A and v4's unsplit EBR rows untouched: on form-A brackets (f.108r) EBR stays a/l/s |
| SBS | b/e/o | **b/o** | o 32 + 26, b 3 + 3 (codes SBS + DBL) | the runner's reader code DBL on f.176r is the side-by-side glyph, v4's SBS; written as SBS, nothing written under DBL (v4 DBL e/r/u unchanged). f.61 SBS b/o 5/5 (p < 0.005), f.108r 2/2, f.108v rank 2/51; v4's e was a sort artefact (VERIFY-F61-V4) |
| ZHOOK | unread (v4 rows n 1 each) | **i/x** | i 28, x 3 (code ZHOOK) | graded **S** on f.61, not C: no glyph link across hands (H178b tile gate failed); rests on f.61 i 3/3, f.108r i 7/7 with ZHOOK left out of the aligning key, f.108v rank 1/51 |

Not merged (the verifier's "may not take"): 4STEM p/c (f.108r contradicts; data conflict, rule 4), HASH4 d/q (the leaf's own i
share 16%), BETA m/z (period n 16), DBL o (a reader code for the SBS glyph), 4PI p/c, CROSS s. The script checks that each of these,
and every class other than the four, loads exactly as v4 does (`test_period_key.load_key --collapse-ebr --min 2 --frac 0.1`).

**Reproduction of VERIFY-F61-V5's numbers from the v5 file** (`build_key_v5_result.txt`): **yes**, every figure. f.61 five known
spans 53/55 (2000 permuted keys, seed 20260929: mean 0.307, p95 0.455, 0/2000 at or above); f.108r overlay 74/84 with EBR at its
form-A set (mean 0.312, p95 0.429, 0/2000); f.61 meter firm 12 / two-way 50 / wider 12 / unread-or-null 25 of 99 (C6 unread/null),
tokens changed VBAR_A x6, EBR x4, SBS x7, ZHOOK x3. The firm count does not move: each new value is a two-letter period cell, so a
two-way token under v5 is a cell of the design, not an undecided merge. The known spans are Tomokiyo's published letters (text:
known); this is a test of the key, not a reading of anything outside his spans.

## key v6 (F61-FAMILY-10, 29 Sept 2026, 07:1x UTC): the hash family by shape (VERIFY-F61-V7) and the bowl rule on f.61 only (VERIFY-F61-V6)

`build_key_v6.py` (with `--check`) writes `key_period_v6.tsv` from `key_period_v5.tsv` (not edited): every v5 line verbatim, except
the two f.188r HASH4 i/x rows, kept as `#moved-to-H24-v5` comment lines. Read v6 with `build_key_v6.load_key_v6()`: CELL rows give a
class's letter set outright (as in v5); `F61READ` rows are skipped by the pooled key and apply only with `f61=True`, the f.61 reading.
Key source: `period` for every changed row (the hash cells from the decipherments of fr.3982 f.101r, fr.3984 f.188r and f.274r; the
F61READ rows from fr.3984 f.176r / fol. 177r), carried to other hands by a blind shape attribute, and cross-checked against
Tomokiyo's published letters (`published`, credited).

| row | v5 | v6 | counts written | provenance |
|---|---|---|---|---|
| HASH4 (the 4-head hash), pooled | d/i/q | **CELL d/q** | d 43 / 12 / 5, q 24 / 3 / 5 (f.101r / f.188r / f.274r) | VERIFY-F61-V7, endorse: on the three period-lettered leaves the 4-head reads d/q 37 of 45 tiles (setD), within-leaf permutation p 5e-05; each leaf clears on its own. Grade C on those leaves. f.101r's HASH4 i 4 stays as a stray row (not in the cell) |
| f.188r HASH4 i 10, x 3 | in HASH4 | **moved to H24** | H24 i +10, x +3 on f.188r (rows marked `MOVED from HASH4 by shape`) | V7: of the f.188r HASH4-coded i/x rows, 10 of 12 tiles are the 2# sign (H224 had 8 of 11) |
| H24 (the 2# sign), pooled | i/j/y | **CELL i/x** | i 170 / 43 / 6, x 5 / 4 / 1 (f.188r includes the moved rows) | V7: the 2# reads i/x 38 of 42 tiles (setD); the class reappeared, unprompted, from the reader never offered it (setN). j/y are period spellings of i (folded). H24's own d/q stray rows are left in place: V7 places 4 of the 7 H24-coded d/q tiles on the 4-head, which is not a per-row assignment |
| HASHLOOP (the looped hash) | pooled into HASH4 by pass code | **separate row, UNREAD** | none (letter `-`, n 0; never loads) | V7 caveat 3: f.106r's HASH4 is looped 5/5 (setD), as is most of f.108r's; no period value; never pooled into HASH4's counts |
| 4TRI on f.61 (F61READ) | c/p/t | **c/p** (f.61 reading only) | 5 f.61 tokens that Tomokiyo reads c or p | VERIFY-F61-V6, endorse in part: bowl yes c/p 18/3, no 10/39 on f.176r (p 4e-7); on f.61 the bowl sign is 4TRI at all 5 positions, Tomokiyo c/p 5/5. Grade **S** on f.61. The pooled 4TRI row is unchanged (c/p/t) |
| 4STEM on f.61 (F61READ) | a/c/e/n | **a/n** (f.61 reading only, L11) | f.61's single 4STEM token | V6: no bowl at L11; Tomokiyo a/n 9/9 at no-bowl positions. Grade **S**. **No pooled 4STEM a/n cell**: f.108v's 4STEM is the c/p sign by sequence, a code conflict between leaves (rule 4) |
| HASH4 on f.61 (L01) | d/q/i | **d/q** (through the pooled cell) | the one token | V7: the 4-head in both blind readers (setN "less sure"), as in H233. Grade **S** on f.61 (period value from three leaves, linked by blind shape) |

Not merged, awaiting VERIFY-F61-V8: ZHOOK = 2# (H235; ZHOOK stays the v5 CELL i/x, grade S) and the 4PI split (H233-H240; 4PI stays
a/d/n/q). The script checks that ZHOOK, 4PI, 4STEM, 4TRI and C43 load in the pooled key exactly as in v5, and that H24 and HASH4 are the
only pooled classes that change.

**Reproduction from the v6 file** (`build_key_v6_result.txt`): **yes**, every figure. f.61 five known spans **53/55** under the f.61
reading key (2000 permuted keys, seed 20260929: mean 0.286, p95 0.418, 0/2000 at or above; the pooled key also gives 53/55); f.108r
overlay **74/84** under the pooled key, EBR at its form-A set (mean 0.305, p95 0.417, 0/2000); f.61 meter **firm 12 / two-way 58 /
wider 4 / unread-or-null 25** of 99 (C6 unread/null), which is VERIFY-F61-V7's "v5 + V6 + V7". Still wider than two: 4PI x2, OTHER x2.
Tokens changed against v5 on f.61: 4TRI c/p/t -> c/p x6, 4STEM -> a/n x1, HASH4 d/q/i -> d/q x1. The firm count does not move: each
new value is a two-letter cell. The known spans are Tomokiyo's published letters (text: known); this is a test of the key, not a
reading of anything outside his spans.

## key v7 (F61-FAMILY-11, 29 Sept 2026, 10:1x UTC): ZHOOK's glyph link and the 4PI split (VERIFY-F61-V8)

`build_key_v7.py` (with `--check`) writes `key_period_v7.tsv` from `key_period_v6.tsv` (not edited): every v6 line verbatim, except
the two ZHOOK rows (kept as `#replaced-v6` comment lines) and f.188r's five 4PI r-tail rows (kept as `#moved-to-4PIR-v6`). Read v7
with `build_key_v7.load_key_v7()`: as v6, plus `HELD` rows never load and `F61TOK` rows load only with `f61=True`; run
`build_key_v7.f61_relabel()` on the f.61 lines so that f.61's two 4PI tokens carry the new class (L11 9 `4PIPI`, L01 12
`4PIPI_UNREAD`). Only the four items in VERIFY-F61-V8's "What should merge" list are merged. **H240 as proposed (both f.61 4PI a/n) is
not merged**: V8 did not endorse it, because L01 12 has no source.

| row | v6 | v7 | counts written | provenance |
|---|---|---|---|---|
| ZHOOK, pooled | CELL i/x, note "no glyph link" | **CELL i/x, value unchanged**; note "the 2# sign = H24 cell, glyph link VERIFY-F61-V8", grade **S** | i 28, x 3 (f.176r/f.177r, as v5/v6) | V8 verdict (1), endorse: setF and setG each put all 10 Mayenne-hand ZHOOK tiles (f.61 3/3, f.108r 7/7) in the 2# class, and none of 27 in-hand distractors; within-leaf p 5e-05; both readers passed the f.274r gate (20/21) and the repeat control (8/8). f.108r's overlay letters at ZHOOK are i/j (= i) under a key-free positional alignment. Key source: `period` (the H24 cell), linked by a blind shape attribute. No meter token moves |
| 4PI (the 4-head), pooled | a/d/n/q (frac rule) | **CELL d/q** | d 5 / 9, q 2 / 2 (f.101r / f.188r) | V8 verdict (2), the endorsed split: every period 4PI row lettered d/q is the 4-head in both readers (12/12), and so is every f.108r 4PI (9/9). Grade C on f.101r/f.188r (period decipherments); f.108r's 4PI reads d/q through this cell (overlay letters d 4, p 1). f.101r's other 4PI rows (n 3, a 1, c, m, p, s 1 each) were not shape-tested by V8 and stay as stray support rows outside the cell; f.188r's three unlettered `-` rows stay in 4PI |
| 4PIR (the 4-with-r-tail form), f.188r | pooled into 4PI | **separate row, HELD, never loads** | a 5, n 1, e 1, h 1, r 1 | V8 "Finding for the key" and merge item 4: the f.188r rows lettered a/n are a third form ("4r-like", "4 + r-like tail"), described like several C43 tiles; split before any further pooling. No value endorsed; whether they are C43 miscoded as 4PI deserves one test (not run here) |
| 4PIPI (f.61's 4-over-Pi), f.61 reading only (F61TOK) | 4PI a/d/n/q (pooled) | **L11 9: a/n, grade M**; **L01 12: unread** | L11 9 (Tomokiyo S5's n); L01 12 none | V8 verdict (2) P2: f.61's two 4PI are E in both readers, the only tiles either called "4 over Pi", so not the 4-head and not d/q. The registered E <-> a/n read-out failed, so a/n has no period glyph: L11 9 rests on Tomokiyo S5's single published letter (`published`, credited) at grade M; L01 12 lies outside the published spans and has no value |

**Reproduction from the v7 file** (`build_key_v7_result.txt`): **yes**, every figure. f.61 five known spans **53/55** under the f.61
reading key with f.61's 4PI relabelled (2000 permuted keys, seed 20260929: mean 0.276, p95 0.418, 0/2000 at or above; for information,
the pooled key without the relabel gives 52/55, because d/q at L11 9 misses Tomokiyo's n); f.108r overlay **74/84** under the pooled
key, EBR form A (mean 0.295, p95 0.405, 0/2000); V8's meter (verify_v8/meter_v8.py bands) with both cells as endorsed, f.61's two 4PI
held unread: **firm 12 / two-way 58 / wider 2 / unread-or-null 27** of 99; and key v7 as merged, L11 9 a/n grade M and L01 12 unread:
**12 / 59 / 2 / 26** (V8's variant added after scoring). Still wider than two: OTHER x2. The script also checks that every pooled class
except 4PI loads exactly as in v6 (ZHOOK, HASH4, H24, 4STEM, 4TRI, C43, EBR, SBS, VBAR_A), that 4PIR, HASHLOOP and 4PIPI never load
into the pooled key, and that `verify_v8/meter_v8.py --check` and `build_key_v6.py --check` still pass. The known spans are Tomokiyo's
published letters (text: known); this is a test of the key, not a reading of anything outside his spans.

## CA on f.61 (V9) (F61-FAMILY-12, 29 Sept 2026, 11:2x UTC): a published null in the scribe's letter a, f.61 reading only

Merged from AUDIT.md section VERIFY-F61-V9, "What should merge" item 1, and nothing more. **No key file changes**: `key_period_v7.tsv`
(F61-FAMILY-11, 10:17 UTC) stays as built; CA is not a cell and gets no row.

- **What CA is on f.61.** A null by Tomokiyo's published markup (H44: a dash where the sign stands, his words complete without a letter;
  `published`, credited), whose letterform is the scribe's clear letter a. The letterform finding is the campaign's (H256, H260) and
  VERIFY-F61-V9 replicated it with its own tiles cut from the native image and three fresh readers: CA 10/10 with the clear a's, the
  eleven cipher controls from the same runs 0/11, within-line permutation **p 0.0013** (setP, the one reader that passed the registered
  text-a gate; setQ and setR gave the same CA and cipher counts but are unscored by that gate). Three placement helpers, asked only for
  clear words, listed seven of the ten CA as the one-letter word "a" unasked.
- **What the null rests on.** Direct for the four CA inside Tomokiyo's spans (H259, re-run by V9: inserting a at CA breaks one of his
  words, ca|pable, and falls at a word boundary three times); the six outside his spans (L01 8, L03 1, L07 1, L10 2, L10 9, L10 12) are
  null only by the assumption that one sign has one function on the leaf. Whether this is a null drawn as an a or a clear a drawn among the
  signs is not decidable from the ink; the known spans answer the functional question (no letter) at every in-span CA.
- **Scope.** f.61 reading only, never a pooled cell. The glossed leaves' CA rows stay as they are (f.101r glosses -, c, q, s, t; f.188r
  c, p, s): either that class there is not this glyph, or the null is f.61's own usage.
- **Meter** (`verify_v9/meter_v9.py --check` OK, re-run by F61-FAMILY-12): key v7 as merged, CA counted as null, **firm 12 / two-way 59 /
  wider 2 / unread-or-null 26 [null 17 + unread 9]** of 99. No band count moves; ten tokens move from unread to null inside the last band.
- The class note in `f61_null_band.tsv` (written by `f61_null_band.py`, `--check` OK) cites V9. The f.61 decode file
  (`f61_decode_period_v4_frac0.1_sbs.tsv`) carries no per-class note column, so the null band is the one class-note file.
