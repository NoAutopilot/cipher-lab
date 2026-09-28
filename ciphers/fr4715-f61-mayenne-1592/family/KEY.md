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
