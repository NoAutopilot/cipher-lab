# DIGEST-1: Debosnys swarm, round 1, merged (DEB-SWARM-MERGE-1, 29 Sept 2026)

Merge worker DEB-SWARM-MERGE-1, a session separate from every group. Written 29 Sept 2026 between 05:16 and 06:0x UTC
(`date -u`). Inputs: every group's LOG.md (A, B, C, D, F, G, H), group E's files (PAGEMAP, LIFE, PICTURES, WRITINGS,
CRIBS, pict_tests.json), D's CASE.md, H's WORDSIGNS.md, the harness README.md and SELFTEST.md, the ROOM done lines
(0 at 03:15, F 03:23, E 03:28, A 03:44, D 03:48, H 03:52, C 04:17, G 04:31, B 05:06), and the transcription files
`disagreements*_classes.tsv`, `h27_confusions_all.json`, `h6_folds.json` and the settled c1/c2 drafts. All nine
sessions had posted a done line before this merge started, so nothing is merged from a partial log. No key is copied
between groups. Public copies only; nothing here comes from the museum's restricted material. Grade S throughout;
**nothing is read, no key passed the bar, the target's status stays `open`**.

## The one-paragraph answer

No group produced a key that passes the frozen bar; the solving groups fitted well over 150 keys between them, all short.
The swarm's negatives split in two. **The solver negatives are partly about our transcription:** every letter or
syllable solver fails its own control somewhere between 3 and 10 pct transcription noise in the c1->c2 direction,
C's syllabic method fails its control even on clean text, and H's Copiale method fails at 8 pct noise or more at every
size, so none of those can say anything about c1/c2 at the drafts' measured 14-18 pct. **But the order result is about
the cipher, not the transcription:** group D's order test still sees a language at 15 pct noise (every harness language
control 8.8-86 against a threshold of 4.3) and mostly at 25 pct (only 2-8 of 40 language pairs score as low as the
real text), while c1+c2 score 0.39-0.91, level with the no-language control. And in the c2->c1 direction, groups A, B and
G read their matched 15-pct-noise controls (A 5 of 8 seeds pass, B 100/100, G 4 of 4) but no real key. So noise does not
explain why the solvers find nothing. Noise explains why nothing could be read if a language sits under one of the
routes D could not exclude: a running key, letters scrambled inside words, or random filler making up a third or more of
the signs. One condition remains, and round 2 can check it cheaply (R2-1): the harness noise model is uniform
replacement, but a quarter of the real disputes are a sign against no sign (boxes that may be strokes or marks).

## Per group (what was tried, best numbers, how it failed, at most three insights)

| group | hypothesis | control (bar 70 pct recovery) | best real held-out (pct / pct_strat) | attempts | verdict |
|---|---|---|---|---|---|
| 0 harness | frozen scorer, controls, bar | self-test: planted passes, random and NULL-climber fail | -- | -- | FROZEN ed4a3743 (blob d80e6baa) 03:14 UTC; no refit null (Q3) |
| A | French, homophonic letters | FR-HOMO 94.9; -N15 28.5-67.7; held-out c2->c1 on N15 passes 5 of 8 seeds | c2->c1 fr_quad 99.2 / 96.4; c1->c2 86.7 / 32.6 | 21 real fits (+ 8+8 matched-seed NULL and N15 fits) | disfavoured, control-backed at uniform 15 pct noise: real 0 of 8 vs N15 5 of 8, (3/8)^8 = 0.0004; real median strat 89.5 sits with NULL (85.8), not French-N15 (100) |
| B | English, homophonic letters | EN-HOMO 95.2; -N15 73.8; held-out c2->c1 on N15 100/100 | c2->c1 en_quad 93.3 / 32.7 (8th pct of 50 refits); c1->c2 79.1 / 78.1 (untestable: control fails) | 30 rows, ~180 fits + 90 refits | control-backed negative at uniform 15 pct noise; the real text fits no better than its own sign-order shuffle, below a French text read with the English model |
| C | syllabic / mixed (French) | FR-SYLL **64.7 / 67.0 (fail)**; -N15 37.0 | not scored (Phase 1 not met) | 2 Phase 1 attempts + 22 exploratory | non-test: control fails even clean at N 790; the held-out bar cannot see a key that reads 53.8 pct of the unseen control text |
| D | disproof (no language) | own blind 100 pairs bal. acc 0.90; harness blind **5 of 5** | frozen order score c1+c2 0.39-0.91 vs threshold 4.3 (NULL -0.5; language controls 8.8-86) | 12 | c2 has no in-line order at 15 pct noise; excluded: homophonic letters/syllables in line order, WORDMIX word code, periodic polyalphabetics (separate or shared alphabets), autokey, X as a word space; not excluded: running key, word-internal anagram, 35 pct+ random nulls; one fragile lead (R34) |
| E | context and pictures (scores no keys) | within-line shuffles, class control, power check | -- | 6 tests E1-E6 | pictures open lines (12 of 56, p < 0.0001); drawn cups and a jug close them (5 of 5, p < 0.0001); X avoids the slot before a picture (3 vs 8.7, p 0.016); no recurring phrase round repeated pictures (p 0.51, power shown); his clear poems and portraits are mostly copies (Brown 2021) |
| F | Masonic comparison | Copiale known answer for the design tests (space signature 16/16 windows, 9/14 at X's density); pigpen/Copiale keys are fixed, not fitted | KEY_copiale_HML c1->c2 98.4 / 76.2, c2->c1 99.8 / 89.1 on 118 / 29 letters, coverage 0.31 / 0.36 | 6 | Masonic alphabets are not his sign set (pigpen shapes 3.8-5.2 pct of tokens); Copiale overlap is the shared planet/Greek stock; pictograms are not Copiale word symbols (23 types in 60 tokens vs Copiale max 8); Folger untested (text unreachable then) |
| G | Portuguese / Spanish / Latin, homophonic letters | PT-HOMO 81-90; -N15 held-out c2->c1 4 of 4; hand-planted at 15 pct: pt 1/4, es 1/4, la 2/4 | c2->c1 pt 99.7 / 91.4, es 99.8 / 82.7, la 99.8 / 89.3; c1->c2 best 87.2 / 59.4 | 56 keys | pt control-backed negative (0 of 24 vs 4 of 4); es/la disfavoured on partial-power controls (8 misses each, all below the controls' misses); fit gap real 0.01-0.04 per char vs control 0.13 |
| H | the Copiale method, replicated | Copiale clean 79-94 at 770-1,200 tokens (German ranked 1 of 12 in 10 of 10); 135 tokens 4-18; 658 tokens clean 1 of 3; **8 pct noise or more fails at every size** (1,200 at 3 pct: 84-90; at 8 pct: 1-7); FR-HOMO 6.4 | none scored (Phase 1 not met at the target's noise) | 10 | non-test at 14-18 pct noise; Copiale-type word symbols between space signs excluded for the pictograms (neighbour test p 0.68 vs control 5 of 5 at Debosnys's size) |

Insights per group, as the groups wrote them (trimmed; every number is in the group's LOG.md):

- **A.** (1) The noise wall: a true French homophonic key at c2 size is identifiable only below about 10 pct uniform
  type noise with a 5-gram model; at 15 pct the true key's decode scores *below* spurious keys (-1763 vs -1474), so no
  search recovers it. (2) Word spaces lift a planted French text to 0.70-0.74 letters at 15 pct noise (edge: 2 of 4
  seeds at N 658), but the spaced fit on the real text matched NULL too. (3) Tool: `hsolve.c` + `fitkey.py` (C annealer,
  5-gram, frequency term, window floor, optional space symbol, base-family fold with a random-fold null); it passes
  c1->c2 on the clean FR-HOMO control, which the harness README had judged out of reach.
- **B.** (1) Under English 5-grams the real text fits no better than its own shuffle and worse than a French text read
  with the English model; keys fitted on the real order carry to held-out text slightly better than shuffled-order
  refits by the *same* margin in every language (fold: 36-38 of 40 refits beaten in en/fr/es/pt): some order is shared
  between the texts (cf. H41's recurring pairs) that no letter model prefers. (2) The value-permuted null does not
  identify a language: one of 40 shuffled-text refits cleared beats_all under BOTH nulls on en_quad; the refit null
  and a cross-language check are needed. (3) Tool: Witten-Bell 5-grams (`build5.c`) instead of quadgrams took the
  planted control from 0.43-0.78 to 0.93-0.95 clean; `fit_key.py --shuffle-seed` + `refit_null.sh` supply the refit null.
- **C.** (1) A homophonic solver scoring P(plaintext) alone piles signs on frequent units and beats the true key by
  500+ nats; the channel term (-sum C_u log C_u) fixes it. (2) Under any one-sign-per-unit syllabary or mixed system X
  (14.4 pct) cannot be one ordinary unit (largest French unit 3.6 pct syllables, 6.8 pct mixed). (3) The held-out bar
  is out of reach for a syllabic key at this length even when the answer is known.
- **D.** (1) Inside its lines c2 has no more order than its own shuffles (0.4-1.0 vs 8.8+ for language controls at
  15 pct, 5 of 5 blind). (2) No frequent sign is a word space (X zero-gap p 0.25, dispersion p 0.36; control p 0.000).
  (3) Tool: `dcore.py`, the frozen order score, usable on any intermediate text; the real sequence is closest to
  signs drawn independently from a table, unlike both human "meaningless writing" models tried (habitual successors,
  avoided repeats).
- **E.** (1) Line edges are structured: pictures open, vessels close. (2) X avoids the slot before a picture as it
  avoids line edges, so X is not a divider in front of picture-initial words. (3) Context: 516 on c2a = 16 May, his
  claimed birthday (grade M); execution 27 Apr 1883; his clear poems, the Greek verso (Moore) and the women's portraits
  are copies; CRIBS.tsv 346 rows feed DEB-VOCAB.
- **F.** (1) Pictograms are not Copiale word symbols; their line-initial ratio (3.7) sits between Copiale's word
  symbols (1.8) and its decorative capitals (17). (2) Plain X is not a Copiale-type space (test power about 64 pct at
  X's density). (3) Masonic alphabets are not the source of the sign set; the Folger composite design is the one
  Masonic design left untested.
- **G.** (1) Fit gap: a Portuguese homophonic control fits 0.13 per char better than its order-shuffled copy; real c2
  0.01-0.04 in pt, es and la. (2) Taking pictograms and punctuation-like signs out lowers the stratified percentile,
  it does not raise it. (3) Not tried: 5-gram verse-heavy Portuguese, heavier homophony than the curve implies,
  syllable or word units in these languages.
- **H.** (1) A homophonic solve of Copiale shape needs about 700+ clean tokens and under about 5 pct noise. (2) Word
  symbols between space signs are excluded for the pictograms. (3) Tools: `hsolve_h.c` (a sign may take "space"),
  `pipeline.py copiale --noise` (a real known-answer text at any length and noise), `neighbour_test.py`, the gold-labelled
  Copiale token file (73,391 tokens).

## 1. The noise floor, settled with the logs' numbers

What each method needs (recovery on its own control, uniform replacement noise; "held-out" = score.py's c2->c1 test):

| method | clean | 5 pct | 10 pct | 15 pct | crossover | source |
|---|---|---|---|---|---|---|
| A French 5-gram annealer, c2 size (planted) | 0.93 | 0.83 | 0.69 | 0.40 | ~10 pct | A LOG, noise sweep |
| A same, with word spaces kept (planted) | 0.96 | -- | -- | 0.68 / 0.68 / 0.42 / 0.45 | ~15 pct, 2 of 4 seeds | A LOG |
| A on the harness control | FR-HOMO 94.9 | -- | -- | -N15 28.5-67.7; held-out c2->c1 5 of 8 pass; c1->c2 fails | -- | A LOG |
| B English Witten-Bell 5-gram (planted) | 0.93 | -- | 0.41 / 0.71 | 0.47-0.65 | 10-15 pct | B LOG |
| B on the harness control | EN-HOMO 95.2 | -- | -- | -N15 73.8; held-out c2->c1 100/100; c1->c2 fails (c1 too short even clean) | -- | B LOG |
| G Portuguese quadgram + floor + ILS | PT-HOMO 81-90 | -- | -- | -N15 pooled 29.5-63; held-out c2->c1 4 of 4; hand-planted pt/es/la 1/4, 1/4, 2/4 | ~15 pct, partial | G LOG |
| C syllabic (FR-SYLL) | **64.7-67.0** | -- | -- | 37.0 | below the bar even clean | C LOG |
| H Copiale method, 1,200 tokens | 87-94 | 84-90 (at 3 pct) | 1-7 (at 8 pct) | 4-8 | 3-8 pct | H LOG row 8 |
| H Copiale method, 658 tokens (c2's size) | 92 in 1 of 3 windows, 3-5 in 2 of 3 | 2-8 | 2-8 | 2-8 | fails at c2's size even clean in 2 of 3 | H LOG row 8 |
| earlier GOLD-D2 base-level control (NOTES.md) | -- | 0.385 (0.816 at 2.5) | 0.322 at 7.5 | -- | ~3-5 pct | NOTES.md GOLD-D2 |
| D order battery (language vs no language) | 17.5-86.2 | -- | -- | 8.8-56.9 (threshold 4.3); 0 of 40 FR/EN/FR-SYLL and 1 of 40 PT pairs as low as real | 25 pct: 2-8 of 40 as low as real | D CASE.md |

The drafts: c1 81.6 pct three-reader agreement (noise floor 14.0, ceiling 18.4 pct), c2 82.8 (14.0-17.2), c3+c4 90.0
(8.5-10.0) (NOTES.md H2, H21b, H23).

Plainly, per negative:

- **About our transcription (non-tests):** C (control fails even clean), H (fails at 8 pct+), every c1->c2 row in A,
  B, G (the method fails that direction on its own control at 15 pct, and B's and the harness's even clean), A's spaced
  design (no harness control), G's Spanish and Latin (per-seed control power 1/4 and 2/4). These say nothing about
  the cipher.
- **About the cipher as transcribed, at uniform 15 pct noise:** A's French, B's English and G's Portuguese homophonic
  letter designs in the c2->c1 direction. Their matched controls pass at the same noise (5/8, 100/100, 4/4) and the real
  keys never do (0/8, 0/1 + 8th pct of 50 refits, 0/24).
- **About the cipher, with most noise headroom:** D's order result. At 15 pct noise the language controls clear the
  threshold by 2-13 times; at 25 pct most still do. Nothing in the solver groups contradicts it: B's and G's real
  fit-vs-shuffle gaps (0.00-0.04 per char) sit at the NULL level too.

**The condition that remains:** the harness and D model noise as uniform *replacement*. The real disputes are a
different mix (section 2): about a quarter are "a sign or no sign" (a stroke or blob boxed as a sign, or missed), which
acts as insertion and deletion. An insertion or deletion breaks adjacent pairs much as a replacement does, so D's
margin probably survives it, but that is not measured. Round-2 prompt R2-1 measures it, together with the one
dose-response test the swarm did not run: D's order battery on c3+c4, whose three-pass noise is already down to 8.5-10
pct. If c3+c4 also shows no order where a 10-pct control does, the structural negative holds whatever a cleaner c1/c2
would give.

## 2. A transcription track for round 2 (public images only)

Where the disagreement sits (all four cryptograms, 611 disputed boxes, 1,009 pairwise confusion events,
`h27_confusions_all.json`; tallies by this merge):

| confusion class | events | share | largest pairs |
|---|---|---|---|
| a sign vs no sign (`_`/MULTI): segmentation, strokes and blobs | 245 | 24.3 pct | BAR-SOLID/_ 42, BLOB/_ 38, BAR-THIN/_ 29, CIRC-O/_ 13, DASH-V/_ 13, X/_ 10, DASH-H/_ 8 |
| inside the X family | 103 | 10.2 pct | X/X-DOT 35, X/X-CURL 12, X/X-BAR 12, X/X-O 10, X/X-SLASH 5 |
| X family vs other ids | 64+25+22 | ~11 pct | PCT-SLASH/X 8, PCT/X 7, O-SLASH/X-LOOP 9 |
| inside the % family | 40 | 4.0 pct | PCT/PCT-SLASH 32, PCT-SLASH/SLASH 6 |
| circle family (CIRC-O, O-*, OO-*) with anything | ~135 | ~13 pct | CIRC-O/O-TILDE 8, BLOB/CIRC-O 9 |
| chevrons | 25 | 2.5 pct | CHEVRON/CHEVRON2 11, CHEVRON2/DBL-SLASH 8 |
| stroke family among itself | 27 | 2.7 pct | BAR-SOLID/BLOB 10 |

On c4 the classifier (`disagreements_classes.tsv`, 228 rows) calls 174 "inventory" (one id for several shapes), 34
segmentation, 20 reading; on c1 pass B (`disagreements_c1_passB_classes.tsv`, 52 rows) 40 reading, 7 segmentation, 5
inventory. On c1+c2 (914 boxes): 464 agree A and B, 291 settled 2-of-3, 28 settled only at family or base, **121
three-way splits and 7 segmentation flags**. The three-way splits touch the circle family 41 times, X 32, `_` 32,
strokes 29, % 19, chevrons 12, and the pictograms only 2: the pictures are the reliable class, the small curved and
stroked signs are not. Folding (h6, c1): PCT+PCT-SLASH and X+X-CURL lift agreement 81.6 -> 86.8 pct at K 158; three
or more confusions, one slash-family component, 87.5 at K 157; chaining at two or more merges eleven ids (94.9 pct at
K 149), which is not one shape and is not a legal fold.

What under 5 pct noise would take on c1+c2 (914 boxes; 5 pct = at most about 45 wrong boxes, against an estimated
130-160 now):

1. **A written sign-or-mark rule, before any re-read.** Decide once, from the images, whether BAR-SOLID, BAR-THIN, BLOB,
   DASH-V, DASH-H and HOOK-L are signs, punctuation or stray strokes (a quarter of all confusion events, and the boxes
   group D's R34 lead turns on). A rule applied by one reader is a segmentation fix, not a reading, and it removes most
   of the sign-vs-no-sign class at a stroke.
2. **Declared folds, reported both ways.** Fold only pairs confused five or more times and read as one shape by eye:
   PCT+PCT-SLASH, X+X-DOT, X+X-CURL (and test X+X-BAR, X+X-O, CHEVRON+CHEVRON2 against H45/H47's base-mark results
   before folding). Every solver then runs on the folded and the unfolded text; a fold is a design assumption, not a
   transcription fact.
3. **Value-blind re-reads of the disputed positions only.** The 121 three-way and 7 segmentation boxes plus the 28
   family/base-settled ones (156 boxes), each read by two fresh readers who never see a pass file, on per-box crops with
   two neighbours each side, at the highest public resolution. Plus an **audit sample**: 60 boxes drawn at random from
   the 291 majority-settled and 30 from the 464 A-B agreed, read the same way, to measure the residual error the majority
   rule leaves (the floor-to-ceiling range 14-18 pct counts only unsettled boxes, not wrong majorities). Price it per
   pass (CLAUDE.md Usage 6): about 246 boxes x 2 readers in crop batches of one line, plus one reconciliation unit.
4. **A known-answer control for the protocol.** Render a synthetic page from `glyphs/bitmaps.npz` (his own sign
   images) with a known sequence at the public scans' resolution, read it by the same protocol, and report its measured
   error beside the real estimate; the real estimate counts only if the protocol reads the synthetic page under 5 pct.
5. **Resolution.** The public images are the Schmeh / Cipherbrain PNGs (c2a 1053 x 1527). A search for any larger
   public copy (Wikimedia Commons, Bauer 2017's figures, Farnsworth 2010's reproductions, the holding museum's own
   public web images) comes before the re-read, since a sharper image does more for the circle and stroke classes than
   a third reader does.

c3+c4 reached 8.5-10 pct with the same three-pass recipe, so the recipe works where the page is cleaner; the step from
there to under 5 pct is the rule in item 1 and the targeted re-reads in item 3. The museum's own scans may be sharper;
the private session can run the same protocol on them privately. The public side needs only items 1-5 above.

## 3. What the frozen scorer lacks

`score.py` froze at 03:14 UTC (blob d80e6baa) with the plain value-shuffle null and the frequency-stratified null. The
refit null (fit the same method on the fit text with its token order shuffled, 50+ refits, pass above the refit p99)
was added to the bar by the orchestrator's 03:15 amendment, one minute after the freeze; `score.py` has no
`--refit-cmd` and no refit code (checked by grep). Groups carried it themselves or not at all:

| group | refit null on the real text? | what it carries instead |
|---|---|---|
| A | **no** (50-refit form); an order-shuffled-fit null of 6 fits was built and validated on controls only (`pipeline.py`) | matched-seed comparisons: 8 fits each on real c2, NULL and FR-HOMO-N15, c2->c1 |
| B | **yes**: 50 refits c2->c1 (real at 8th pct, 4 of 50 below it); 40 refits on the c1+c2a -> c2b fold (real under p99; one refit beats_all under both nulls) | -- |
| C | n/a (no real key scored) | -- |
| D | n/a (no key); its whole test is against the text's own within-line shuffles (200-scan own-shuffle null for R34) | -- |
| E | n/a (scores no keys) | within-line shuffles, class control |
| F | n/a in form: fixed published keys, no fitting step to refit | plain and stratified nulls only |
| G | **no** (50-refit form) | fit-gap diagnostic (4 real-order fits vs 2 order-shuffled fits per language) and hand-planted matched controls |
| H | n/a (no real key scored) | a token-shuffled null per Copiale window on its control |

No verdict in round 1 depends on the missing null, because no key reached even the frozen bar. It matters for round 2:
B's fold run shows a shuffled-text refit can clear beats_all under both frozen nulls, so the frozen bar alone can pass
noise. Before round 2 scores anything, the harness should add the refit null to `score.py`, add B's cross-language check
(a claim in language L beats the same key's standing in the other languages), and adopt the c1+c2a <-> c2b fold bar
the README offered (c1->c2 is out of reach for every fitted method on its own control), then re-freeze with a second
FROZEN line.

## 4. Leads worth a round-2 group, each with the test that would kill it

- **E's line structure.** Pictures open lines (12 of 56, p < 0.0001, H31 reproduced with E's corrections) and drawn
  cups and a jug close them (5 of 5, p < 0.0001; the part H33 could not have selected, PICT-JUG and BOX-M, 2 of 2, p
  0.0009). Every token in these tests is an in-line sign inside a cipher line on the cipher leaves (c1, c2a, c2b, c3,
  c4); none of the page drawings (the portraits, the c2a still life, the c3 couple and owl) enters them, so the report that
  some album drawings are earlier prisoners' work does not touch these counts. It does touch any argument from the page
  drawings (the bonnet portrait is already traced to a *Peterson's* plate). A check by this merge (positions only, from
  the settled drafts): three other container-like singletons sit **mid-line**: PICT-BOTTLE c2a L02 at 9 of 26,
  PICT-BARREL c2a L10 at 17 of 29, PICT-GLASS c4b L05 at 11 of 14. With them the "container" class is 5 of 8
  line-final. **Kill test:** a pre-registered class definition (by what is drawn, fixed before counting) and a
  width-matched control (in-line signs of the vessels' drawn width): if the broadened class is not line-final beyond
  chance, or wide signs of any kind sit at line ends as often, the vessel rule is layout, not system.
- **E's copied-text finding.** His clear English poems are copied or patched from Moore, Stoddart, Chivers and
  Colesworthy, the Greek verso is Moore's, the Latin is Virgil and the Vulgate, the portraits are *Peterson's* 1879
  plates (Brown 2021, WRITINGS.tsv). So the plaintext may be a copied text. Bourdeau's Moore and Delille tests were at
  chance on his transcription. The useful form is a crib search that survives what D found: line lengths in signs and
  the couplet line-end matches of c4 (H5: within 5 of 10, across 0 of 9) are unchanged by a running key, by scrambling
  letters inside words, and by sign-replacement noise. **Kill test:** a known-answer control before any real search (a period poem from
  the candidate pool enciphered under homophonic letters with 15 pct noise, and again with a running key, must rank
  top among 1,000+ same-period decoys on the length-and-rhyme profile); then a real candidate dies if its profile
  match is not above the decoys' 99th percentile.
- **D's columnar transposition at height 34.** Scan maximum 8.18, p 0.010 against 200 own-shuffle scans; fresh-seed
  replication p 0.03; both halves above 0; **gone (p 0.80) when the 15 punctuation-class boxes are kept**. One family
  of about ten, so a p near 0.01 is weak. **Kill test:** settle BLOB, HOOK-L and DASH-H as signs or marks on the images
  (transcription item 1), rerun `reread.py` on the settled reading with its 200-scan own-shuffle null; p > 0.05 kills
  it. Only if it survives, a matched-control solver on the R34 reading with the c2a/c2b fold held out.
- **F's Folger design test.** `sources/folger/` now holds Bennett's NSA paper (English, monoalphabetic, clusters
  between spaces are words, about 12 strokes per cluster, the recovered alphabet); Morris's 1999 lecture and figures
  load by curl with a browser user agent (not copied, copyright). The design lead: Folger figures are composites of
  several characters in one figure; Debosnys has 36 composite ids (about 20 pct of signs), many built from stacked
  dashes. If his composites are ligatures of several units, splitting them in reading order could restore order that D's
  test does not see in the unsplit text. **Kill test:** a Folger known-answer text (a passage transcribed from Bennett's
  or Morris's figures, value by the recovered alphabet) on which the split-and-score test sees the design; then the
  split Debosnys text scoring at shuffle level on D's frozen order score kills it.

## 5. Dead, and only untestable

"Dead" below means a control-backed negative at the current transcription, for one design; the target stays `open`
(rule 5), and every item is conditional on the settled drafts and on uniform replacement noise at 15 pct.

Dead at the current noise:
- **French homophonic letters** (one letter per sign, line order): A 0 of 8 vs FR-HOMO-N15 5 of 8 (c2->c1), plus D's
  order battery (FR-HOMO pairs: 0 of 40 as low as real at 15 pct).
- **English homophonic letters:** B, EN-HOMO-N15 passes and the real key sits at the 8th pct of 50 refits; D 0 of 40.
- **Portuguese homophonic letters:** G 0 of 24 vs PT-HOMO-N15 4 of 4; D 1 of 40.
- **Masonic alphabets (Royal Arch pigpen, Copiale values):** F; this one is not a noise question at all, since the
  pigpen-shaped signs are 3.8-5.2 pct of tokens whatever their values, and the Copiale overlap is the planet/Greek
  stock both makers drew on.
- **Copiale-type word symbols for the pictograms:** H's neighbour test p 0.68 against a control that reads the design
  5 of 5 at Debosnys's size, and F's type count (23 in 60 vs Copiale's 8 at most). The pictograms are the most reliably
  transcribed class (2 of 121 three-way splits), so noise does not rescue this.
- **X as a word space** (Copiale-style or any): D (p 0.25 / 0.36 vs control 0.000), F (null at 64 pct power), E3 (X
  avoids the slot before a picture). H's word-length KL leans slightly word-like and is logged as weak, not a lead.
- **Periodic polyalphabetics (separate or shared alphabets), autokey, a word code of the 60 commonest words:** D, each
  with a control that reads it.

Disfavoured, not dead: **Spanish and Latin homophonic letters** (G: 8 misses each, below even the missing control
seeds, but per-seed control power only 1/4 and 2/4; D's calibration includes LA-HOMO, 4 of 40 as low as real with an
X-like null).

Untestable until the noise drops (or until a different instrument exists):
- the syllabic / mixed design (C's control fails even clean at N 790; needs the pooled c1-c4 and a cleaner text);
- the Copiale method's automatic solve (under about 5 pct noise, 700+ tokens: pooled c2+c3+c4 is about 1,200);
- every c1->c2 held-out test (fails on its own control);
- a letter design with a word-space sign (no harness control; A's own planted controls reach the bar only at the edge);
- the R34 transposition (turns on the stroke boxes);
- pictograms as rebus syllables (needs a reading of the following signs);
- running key, word-internal scrambling and 35 pct+ random filler: not a noise question; order tests cannot see them
  at any noise, so they need a different instrument (the length-and-rhyme crib search in R2-3 is one).

## Round-2 prompts (ranked by expected value; each names its known-answer control)

Prerequisite for any group that scores a key, not a group itself: **HARNESS-2** adds the refit null (`--refit-cmd`,
50+ refits, p99), B's cross-language check and the c1+c2a <-> c2b fold bar to `score.py`, reruns the self-test (planted
passes; B's shuffled refit that cleared beats_all must now fail), and writes a second FROZEN line before any round-2
key is scored.

**R2-1 ORDER-DOSE (cheap, CPU only; from D, with G's fit-gap as a second instrument).** Decide whether the no-order
result is the cipher or the transcription, without any fresh reading. Run D's frozen order battery (`dcore.py`, no
retuning) on (a) c3+c4 alone, whose three-pass noise is 8.5-10 pct; (b) c2 with the declared folds (PCT+PCT-SLASH,
X+X-DOT, X+X-CURL); (c) c2 with the stroke classes (BAR-SOLID, BAR-THIN, BLOB, DASH-V, DASH-H, HOOK-L) dropped. Known-answer
control: D's calibration regenerated at each text's own N, K, line lengths and measured noise, with a noise model that
mixes replacement and insertion/deletion in the real 3:1 proportion (section 2), FR/EN/PT/LA-HOMO and FR-SYLL against
NULL-IID; the test counts only where it separates them at balanced accuracy >= 0.80. Kill: if (a)-(c) all stay at the
NULL level where their controls clear the threshold, the structural negative stands whatever a cleaner c1/c2 would give,
and letter and syllable solving waits on nothing. Suggested for group D or G. Cap about USD 5.

**R2-2 T-LOW (the transcription track; public images only).** Bring c1+c2 under 5 pct type noise. Steps in order: the
public-resolution search; the written sign-or-mark rule for the stroke classes; declared folds; two fresh value-blind
readers on the 156 disputed boxes and the 90-box audit sample, one line of crops per call, crop commands pasted before
the opening call (CLAUDE.md Usage 6); adjudication with `scripts/h21_pipeline.py`; a noise estimate that adds the audit's
measured majority-error rate to the unsettled floor. Known-answer control: a synthetic page rendered from
`glyphs/bitmaps.npz` with a known sign sequence at the public scans' resolution, read by the same protocol; the real
estimate counts only if the protocol reads the synthetic page under 5 pct. Stop and report if the synthetic page reads
above 5 pct: then the public images are the limit, and that is the result. Suggested for a transcription worker
separate from every solver group (not A-H). Price per pass.

**R2-3 CRIB-LENGTH (copied-text crib search; from E, for A and B).** Test whether c4's verse (and then c2) is a copied
period poem, with a statistic that a running key, letters scrambled inside words, and sign-replacement noise all leave
intact: the line-length profile in signs and the couplet line-end match pattern (H5). Candidate pool: the sources he is
shown to copy (Moore, Stoddart, Chivers, Colesworthy, *Peterson's Magazine* 1879) and period French verse (Lamartine,
Hugo, Béranger, Musset), public-domain texts only. Known-answer control: a poem from the pool enciphered as homophonic
letters with 15 pct noise, and again with a running key, must rank top among 1,000+ same-period decoys; report the
rank for both. Kill: the best real candidate is not above the decoys' 99th percentile. A hit is a crib to hand to the
scorer and two audits, not a reading. Suggested for group A or B (their hypotheses are dead at this noise).

**R2-4 LINE-UNITS (E's picture structure, pre-registered; for E with F's decorative-capital measure).** Fix the
classes by what is drawn before counting (openers: drawn pictures; closers: every container, cups, jug, bottle, barrel,
glass), then test on in-line signs inside cipher lines only, never page drawings. Kill tests: the broadened container
class (5 of 8 line-final by this merge's count) against within-line shuffles; a width-matched control (in-line signs as
wide as the vessels) for layout; and whether picture-opened lines start couplets in c4's verse (H5's couplets).
Known-answer control: Copiale's decorative capitals (F: open 95 of 196 lines, never close one) as a known line-opening
mark, and a planted closer class of the same count as the power check. Kill: containers at chance, or wide signs at
line ends as often.

**R2-5 FOLGER-SPLIT (F's Folger design test, now reachable).** Build the Folger known-answer text from
`sources/folger/` (Bennett's recovered alphabet; a passage transcribed from his or Morris's figures, public, cited),
show that a split-composites test sees the Folger's cluster design there, then split Debosnys's 36 composite ids into
components in reading order (stacked dashes, O-DASH2, II-DASH, CC-DASH, ARCH-DASH, X-DASH, U-DASH) and run D's frozen
order score and B's fit-vs-shuffle gap on the split text. Known-answer control: the Folger passage, plus a planted
ligature text (French split into letters, letters joined in pairs as composites) at Debosnys's N. Kill: the test fails
the Folger control, or the split Debosnys text stays at shuffle level. Suggested for group F.

**R2-6 R34-RECHECK (conditional on R2-2's sign-or-mark rule; from D).** Rerun `reread.py` on the c2 reading the rule
produces, 200-scan own-shuffle null, with the halves check as pre-registered in D's LOG. Known-answer control: D's
TRANS-7/19/33 planted transpositions (they pick their own height 10-12 of 12) rebuilt with the settled box set. Kill:
p > 0.05, or either half at or below 0. Only a survivor goes to a matched-control solver with the c2a/c2b fold held out.
Lowest value of the six: one test family of about ten, and it already failed once on a box-set change.

Where the round-1 groups go: A and B to R2-3 (their designs are dead at this noise; the length-profile search is the
one route D's escape list leaves readable); C waits for R2-2 (its design is untestable, not dead); D or G to R2-1; E to
R2-4; F to R2-5; H waits for R2-2 and then reruns its pipeline on pooled c2+c3+c4 under 5 pct noise; D to R2-6 after
R2-2. Nothing in this digest is a key, and none is to be carried between groups.
