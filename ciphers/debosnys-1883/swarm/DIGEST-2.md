# DIGEST-2: Debosnys swarm, round 2, merged (DEB-SWARM-MERGE-2, 29 Sept 2026)

Merge worker DEB-SWARM-MERGE-2, a session separate from every round-2 job. Written 29 Sept 2026 from 10:13 UTC
(`date -u`). Inputs: the six round-2 folders under `swarm/R2/` (PREREG.md, LOG.md, RESULT.md and the JSON each names),
their done lines (ROOM 07:23 R2-1, 07:26 R2-3, 07:40 HARNESS-2, 08:20 R2-4, 08:23 R2-2, 08:55 R2-5), DIGEST-1, the
harness README.md, and the runner's rows H51-H58 in CAMPAIGN.md and NOTES.md (DEBOSNYS-RUNNER-3b, 06:37-09:36 UTC).
All six jobs had posted a done line before this merge started. No key is copied between jobs; no job produced one.
Public copies only; nothing here comes from the museum's restricted material. Grade S throughout; **nothing is read,
no key passed any bar, and the target's status stays `open`.**

## The one-paragraph answer

Round 2 did not add a reading. It closed three questions DIGEST-1 left open. It also found that the tool meant to
gate a claim cannot yet do so. (1) **The order result on c2 survives the real error mix.** With a quarter of the
errors as insertions or deletions, with the declared folds, and with the stroke classes dropped, c2 stays at
no-language level where every language control clears (R2-1, gated at 0.94-0.96). (2) **The public pixels are the
limit for a letter-level transcription by the protocol on file.** A synthetic page cut from our own crops, with known
answers, reads at 15.6-17.7 pct error with two strong blind readers (R2-2). An independent outside witness bounds the
error hidden in our agreed boxes at the same size (H51, 16.5-17.7 pct). No larger public copy exists. (3) **c4 is not
a contiguous copy of the eight pool texts under a letter-level design** (R2-3, control-backed). The two structural jobs (R2-4
line units, R2-5 Folger split) failed their registered controls and are non-tests. The one positive number of the
round is R2-5's post-registration D2 lead (name-order split of c1+c2 above 80 iid nulls, 9.55 vs 8.9), which is weak
and unreplicated. The harness's second FROZEN line was not written: the planted French key fails its own
cross-language rule on quadgrams, because the Latin corpus rewards any Romance text. Everything that needs a
cleaner transcription now waits on better images or a different reading protocol. The public-data rows worth running
are four cheap CPU checks (section 7).

## Per job

| job | hypothesis / question | registered control | control passed? | best real number | verdict |
|---|---|---|---|---|---|
| HARNESS-2 | refit null, cross-language check and fold pairs added to the bar (`score_v21.py --claim`); second FROZEN line | K1 planted FR-HOMO passes; K2 random fails; K3 B's shuffled refits fail; K4 NULL climber fails; K5 reach reported | **no**: K1 fails fr_quad on both pairs (cross-language: c2->c1 D -0.280 vs p99 0.121; c1+c2a->c2b -0.063 vs 0.216); K3 refit 15 passes en_quad and es_dict, refit 34 passes fr_dict; K2, K4 pass | nothing run on c1/c2 (by design) | **control-fail non-test** of the new bar; `score.py` unchanged (blob d80e6baa, one FROZEN line) |
| R2-1 ORDER-DOSE | is c2's no-order result the cipher or the transcription (indel noise, folds, strokes dropped); dose-response on c3+c4 | D's battery separates NULL-IID from 5 language designs at bal. acc. >= 0.80 at each text's N and decision noise, 3:1 replace:indel | **yes** on b, c, raw (0.938, 0.958, 0.955 at 20 pct); a (c3+c4) 0.85 at 15 pct | b folded 2.56 vs thr 5.5 (0-1 of 40 language pairs as low); c strokes-dropped 0.27 vs 5.1 (0-1 of 40); raw 0.96 vs 5.6 (0-1 of 40); a 2.84 vs 4.9 but 10/2/7/8/2 of 40 FR/EN/PT/LA/SYLL as low | **result** on c2 (NULL at every arm); a is ambiguous (fails the "at most 5 of 40" clause); overall kill test "not met" by the letter of PREREG because of arm a |
| R2-2 T-LOW | bring c1+c2 under 5 pct type noise from the public images | synthetic 96-box page (known truth, our own native crops) read by the same protocol under 5 pct | **no**: 15.6 pct (folds, or folds + rule), 17.7 unfolded; 13.5 pct even counting both doubtful truth labels correct; single readers 11.5 (Sonnet) and 7.3 (Opus) folded | real re-reads not run (stopped at the control, as registered) | **result**: with this protocol the public images are the limit. Side products: RULE.md (sign-or-mark rule), no larger public copy |
| R2-3 CRIB-LENGTH | c4 is a copied period poem (length-and-rhyme profile; survives running key, in-word scrambling and noise) | a pool poem enciphered at 15 pct noise (3:1) ranks 1 among 1,000 decoys (homophonic and running key) | **yes**: 10/10 rank 1 for both; post hoc same-genre pool, R alone, 10/10 rank 1; syllabic (extra) fails (ranks 9-25,954 by S, 14-41,737 by R) | best S 1.359 (Moore Anacreon ode, #8187) vs decoy p99 0.718, but the couplet-permutation null reaches it in 33.5 pct; best R 0.815, reached in 66.5 pct | **result** (letter-level, contiguous, 8 pool texts): no crib. The S pass is voided by the genre-matched null added afterwards. Syllabic: untestable (control fails) |
| R2-4 LINE-UNITS | containers close lines; width is not the cause; picture-opened verse lines start couplets | K1 Copiale capitals >= 0.80 detection; K1r reversed; K2 planted closer power >= 0.80; K2 false positive <= 0.05; K3 width false positive <= 0.05; K3 width power >= 0.80 | **no**: K1 0.310, K1r 0.297, K3 false positive 0.054 (500 draws) fail; K2 1.000 / 0.006 and K3 power 1.000 pass | (unlicensed) containers 5 of 8 line-final, p 3.4e-6; width-matched expectation 0.37; cups/jug 5 of 5, bottle/barrel/glass 0 of 3; couplet starts 1 of 4, p 0.957 | **control-fail non-test** (rule 3) |
| R2-5 FOLGER-SPLIT | composites are ligatures; splitting them restores order D's test cannot see unsplit | Folger passage and a planted French ligature text at 24 pct composites: gate >= 0.80 and >= 32 of 40 above | **no**: Folger passes (0.843, 40/40) but the planted ligature text at the real share fails (0.555, 25/40); D2 planted 26/40 (power about 65 pct) | real-T 36.8, real-N 41.7 vs NULL-SPLIT thresholds 44.3/48.8 (shuffle level); D2 real-N 9.55 vs 80 nulls max 8.9 (real-T 3.51); B gap 0.059/0.077 vs Folger 0.22-0.26 | **control-fail non-test** of the split design at this share; one post-registration lead (D2 real-N), weak |

The runner's rows in the same window agree with every line above. H51 (outside witness: agreed boxes 16.5-17.7 pct,
majority-settled 50-54 pct, three-way 70-80 pct) and H53 (verse agreed boxes 6.8-11.7 pct) bound the hidden error.
H52 finds one key across all four cryptograms, verse included. H54 priced a c2 re-read; H58 withdrew that price after
R2-2. H56 finds Sektu's inventory comparable to ours on the tilde count only. H58 reconciles R2-2, R2-4 and R2-5 with
the campaign and needs no numeric correction. This merge found no conflict between the runner's rows and the round-2
files.

## 1. The harness

**What the frozen bar can gate after round 2.** `score.py` (blob d80e6baa) is unchanged. Its frozen modes reproduce
SELFTEST.md exactly (`R2/HARNESS-2/frozen_selftest_rerun.json`). It can gate a **fixed key that no fitting step
chose**: a published or period alphabet, a key from a crib, a key from better images. For such a key the
value-shuffle and stratified nulls are the right nulls, and the two-direction conjunction holds. It **cannot gate a
key fitted on the texts**, for two measured reasons:
- The refit null is missing from `score.py` (DIGEST-1 section 3). HARNESS-2's K3 shows that the null alone would not
  save it: B's shuffled-text refits 15 and 34, each the most extreme of 40 null draws, sit above all 50 fresh refits
  in their fitted direction. A one-direction rank test at n 50 is a 1-in-51 test and cannot reject a selected key.
  What protects the bar is the two-direction conjunction (about (1/51)^2 per statistic), which the frozen bar
  already requires.
- **Reach.** K5: the harness climber passes nothing on either pair even on clean FR-HOMO (refit null 44-50 of 50
  below). Only the planted key does. At this N a fitted key that cleared the bar would be far beyond the reference
  method's own power, so the bar is a gate no fitted route on file can reach. The bar can still check a key; it
  cannot guide a search.

**The cross-language rule: a fact about the corpora, not a code bug.** The code does what it says (frozen modes
reproduce; K2 and K4 fail as they should). The failure is in what the rule compares. On the 125- and 186-letter test
texts, the planted French key gains more over its refits under the **Latin** quadgram model than under the French one
(c2->c1: la 0.652 vs fr 0.372; c1+c2a->c2b: la 0.507 vs fr 0.444; `diag_quad_gain.json`). The `la` model is built
from one small c.1709 corpus (Zaluski's letters; README flags it as not era-matched). A sharper model from a small
corpus rewards any real Romance letter sequence. So the quadgram statistics of five languages, built from corpora of
very different size and era, are not on one scale at this length. The dictionary statistics do carry the language:
the planted key passes fr_dict in all four directions. This is rule 3's era-mismatched-corpus lesson (pt17/pt18) in
another form. The fault is in the rule's premise, not in `score.py`'s arithmetic.

**Proposal for the orchestrator (not an edit; `score.py` stays frozen).** One change makes the claim mode usable:
**apply the cross-language condition to the dictionary statistics only.** The quadgram statistics keep the frozen
nulls, the refit null and both directions, with no cross-language comparison. The alternative, dropping `la` from the
quad comparison until an 1850-1900 Latin corpus exists, fixes this case only. The same size-and-era mismatch would
recur between the other four. HARNESS-2's second point goes with it as a restatement of the control, not a change to
the scorer: K3 as a **pair** test (one key fitted on shuffled c1+c2a plus one fitted on shuffled c2b must fail the
pair), with 100+ refits so p99 is not the refit maximum. A separate session reruns K1-K4 blind before a second FROZEN
line. Until then `score_v21.py --claim` is a second opinion printed beside the frozen bar, never the bar. With no
fitted route in reach (K5), this is not urgent. It matters the day a fixed key arrives from outside, when the frozen
bar is already sufficient.

## 2. The order result

DIGEST-1 said: "the no-order result is about the cipher, not the transcription". The condition it left open was the
noise model: replacement only, while about a quarter of the real disputes are a sign against no sign. R2-1 measured
that condition:
- At a 3:1 replacement:indel mix, D's frozen battery (`G-D/dcore.py`, unchanged) separates language from NULL-IID on
  the c1/c2 shape at bal. acc. 0.91-0.955 over 15-25 pct noise.
- The real c1+c2 scores 0.96 (D's reading), 2.56 (declared folds) and 0.27 (stroke classes dropped), against
  thresholds of 5.1-5.6. At most 1 of 40 language pairs per design scores as low, and 25-34 of 40 NULL-IID pairs do.
- c2 alone: at most 2 of 40 per design as low, in every arm.

**For c2 the statement now stands**, against the three transcription explanations anyone had named: the indel mix,
the confusable pairs (PCT and X families) and the stroke boxes. It stands conditional on the settled public drafts,
and it holds for **in-line, adjacent-sign order** only. It does not reach c3+c4. Arm a passes its gate (0.85), and
the real score (2.84) is under its threshold (4.9). But 10 of 40 FR-HOMO, 7 PT and 8 LA pairs score as low, and the
real score sits near the 78th percentile of NULL-IID. At N 370 the battery is too weak to call the verse null. The
verse's recurring pairs without transfer or MI (c4 doubled signs +1.93, language controls -0.7 to -0.9) fit verse
repetition as well as language. So the dose-response question (does order come back as noise drops?) is **open
because the clean pages are short**, not because they show order.

**What would still overturn it**, each with the number that decides:
1. **True c2 error above the calibrated range.** R2-1 calibrates to 25 pct. H51's outside witness disagrees with our
   agreed boxes 16.5-17.7 pct, with majority-settled boxes 50-54 pct and with three-way boxes 70-80 pct. Weighted by
   c2's row shares (49 / 34 / 17 pct), that is a crude upper bound near 39 pct, and it includes the witness's own
   misreads. R2-2's single readers err 7.3-11.5 pct on known boxes, so the true figure is well under that bound, but
   it is not measured. A calibration of D's battery at 30-40 pct mixed noise on the c1/c2 shape settles whether the
   margin survives the bound: CPU, R2-1's own scripts (row H60).
2. **Order that lives across boxes a split or a re-segmentation would reveal.** R2-5's D2 puts the name-order split
   of c1+c2 at 9.55 against 80 iid-box nulls (max 8.9), with the unsplit text at 1.70. If that replicates with 500+
   nulls, a habit null and a planted control of at least 80 pct power, "no order" becomes "no order at our
   segmentation". Row H59.
3. **Non-adjacent order**: a transposition, of which D's R34 (columnar, height 34) is the one lead. It was fragile to
   the stroke boxes, which RULE.md now settles. Row H62.
4. **The designs D listed as invisible to any order test at any noise**: running key, letters scrambled inside
   words, 35 pct+ random filler. The order result never excluded these. R2-3 now covers a running key (with a
   control) and in-word scrambling (by construction, since the profile ignores letter order inside a line; no
   scrambled control was run) for a contiguous copy of its pool on c4 (section 4).

## 3. The noise floor, second reading

**Are the public images the limit for a letter-level transcription?** Yes, for the reading protocol on file: two
value-blind model readers, one line of native crops per call, against the inventory tiles. Two independent routes
give the same size:
- R2-2's known-answer page: 15.6 pct folded, 17.7 unfolded, 13.5 pct in the reading most favourable to the protocol.
  Single readers: Sonnet 11.5, Opus 7.3 pct folded.
- H51's outside witness: 16.5-17.7 pct on our agreed boxes.

R2-2 found no larger public copy. Commons carries the same file (identical sha1 for cryptogram 1), and the Cipher
Foundation's six PNGs are the same set at the same dimensions. The printed figures (Bauer 2017, Farnsworth 2010) were
not reachable, so "no larger public copy" means none found by R2-2's search, not a proof that none exists. The
readers split on the classes DIGEST-1 section 2 named: EIGHT/VENUS/THREE, C-BAR-X/ARCH-DASH, CIRC-O/BLOB,
O-SLASH/PHI, II-DASH/CC-DASH, S-CURL/DOUBLE-LOOP. At 15-30 px per sign these are pixel-limited, and more votes on the
same pixels do not add resolution. Two limits remain untested: a different protocol (for example a per-glyph
classifier trained on `glyphs/bitmaps.npz`), and a reader of another kind.

**What that means for every solver route (public side only):**
- **Closed on public data**, because each needs under about 5-10 pct letter-level noise: every fitted
  homophonic-letter route in the c1->c2 direction (A, B, G); the Copiale method (H, fails at 8 pct+); the syllabic
  solver (C, fails even clean); every automatic key search the scorer would gate. The priced c2 re-reads (H50, H54)
  are withdrawn (H58) and are not re-proposed here.
- **Still open on public data**, because each tolerates 15-20 pct or does not depend on the confusable classes:
  - order and structure tests on c2: D's battery (already run, section 2) and the split test at the right null
    (H59);
  - the length-and-rhyme crib profile, which reads only line lengths and line-final agreement and passed its
    letter-level controls at 15 pct (R2-3);
  - position statistics on the pictograms, the most reliable class (2 of 121 three-way splits);
  - a **coarse fold** of the pixel-limited classes, declared as a design assumption and reported both ways. R2-2's
    own reader files can say, at no cost, whether its control drops under 5 pct at the folded K (row H61). A fold
    that merges two signs of different value makes a polyphonic sign, so a folded text is lower-noise but not a
    cleaner copy of the same cipher. That is why every result on it is reported both ways.
- **The private side** is the private session's business: whether sharper scans exist and what they read is not a
  question this digest can answer or ask for. The one public-side fact to pass on is that R2-2's control is portable.
  The same synthetic-page test can be built from any image set before a re-read is bought on it.

## 4. Crib-length (R2-3): dead and only untested

**Dead (control-backed, conditional on the settled public drafts):** c4 is not 20 consecutive lines of any of the
eight pool texts, enciphered as homophonic letters or with a running key at 15 pct noise or less. The texts: Moore,
*Complete Poems* #8187, *Odes of Anacreon* #38230, *Lalla Rookh* #76794; Stoddart, *The Death-Wake* #16601; Hugo,
*Contemplations* #29843, #29844, *Légende des siècles* I-II #72885, #76396; 61,663 windows. Every letter-level
control's true window has R 0.85-0.99 and ranks 1 of 54-60k same-genre windows. c4's best R is 0.815, which the
couplet-permutation null reaches in 66.5 pct. Letters scrambled inside words are covered by construction, since
the length profile does not see letter order within a line, but no scrambled control was run and the rhyme term
would change. The S "pass" (1.359 vs decoy p99 0.718) is not a crib: the genre-matched
couplet null reaches it in 33.5 pct, and the top two windows (Moore, Hugo) are 0.003 apart.

**Untested at this pool size (not dead):**
- Authors not in the pool because they are not on Gutenberg: Chivers, Colesworthy, *Peterson's Magazine* 1879,
  Lamartine's verse, Béranger, Musset's verse. His clear writing is shown to copy the first three (WRITINGS.tsv), so
  this is the gap that matters (row H63, proposed but ranked below the cut).
- Non-contiguous or re-lineated copies, and patchworks (his clear poems are Moore patchworks). A 20-line window
  statistic cannot see these.
- Moore's Greek preface ode (the c4 verso): not in the pool as Greek. H17 tested Gaffney's Greek and English
  renderings of the verso (0 of 48, planted control clears). H20 keeps the Greek ode itself.
- c2: not testable by this instrument (its line breaks are page layout).

**Untestable by this instrument:** any syllabic or sub-word-unit design (control ranks 9 to 25,954). c4's 7-17 signs
per line, about 0.5 per letter of a typical window, point that way, as H5's rhymes and H30's 12-13 non-X signs per
verse line do.

## 5. Line-units (R2-4) and Folger-split (R2-5): non-tests

Both are logged as **non-tests under rule 3**: each registered control failed, and no gate was moved.

**R2-4.** Three gates failed. K1 (Copiale capitals as a known opener, 0.310 vs 0.80), K1r (reversed, as a known
closer, 0.297) and K3's width false-positive gate (0.054 vs 0.05 at 500 draws). The planted-closer power (1.000 at 5
of 8, 0.868 at 3 of 8), its false positive (0.006) and the width power (1.000) passed.
- *What a passable control would need.* K1 as registered cannot pass at this N: Copiale's capital class averages 6.2
  per 56 lines, and only 24 pct of the capitals in windows dense enough to hold 8 are line-initial. A marker that
  diffuse is not seen at 8 tokens and alpha 0.01 by any test. A passable K1 needs a known-answer marker at least as
  strong as the effect claimed and at least 8 tokens per 56-line window, for example a period cipher with a known
  terminal or initial mark. K3 needs a gate with sampling tolerance (the nominal alpha plus 2 SE, or 2,000+ draws);
  as registered it is met or missed by chance.
- *The deeper limit.* Even with passing controls, T1 (containers line-final) rests on classes chosen after positions
  were seen: BUCKET after H33, and the cups and jug by E. The three containers named only by drawing are 0 of 3
  final. No control repairs a selection effect at this N. The only fix is a class fixed in advance and tested on text
  not used to pick it, and all four cryptograms have been used. So the vessel rule is **untestable at this N**, not
  waiting on a better control. If it is used downstream it is "BUCKET, PICT-JUG and BOX-M close lines", never
  "containers do". H31's picture-opener result is untouched: it has its own licensed controls, and R2-4's sanity rerun
  reproduces it (11 line-initial vs 2.36 expected).
- T3 (picture-opened verse lines start couplets, 1 of 4, p 0.957, minimum reachable p 0.043) was testable. It falls
  with the failed gates. The number points against the prediction, but it is not a logged negative.

**R2-5.** The Folger control passes (0.843, 40/40, at 6.5 pct composites). The planted French ligature text at
Debosnys's real 24 pct composite share fails (0.555, 25 of 40). The cause is diagnosed: D's within-line shuffle
breaks each composite's internal pair, so the split itself reads as order (NULL-SPLIT 34.6 vs language 15.6-26.5).
The main test is **untestable by this instrument at this composite share**. It is not a negative on the ligature
design.
- *What a passable control would need.* A null that carries the split: box-level shuffles, R2-5's D2. D2 needs
  planted power of at least 80 pct. At c1+c2's split N (about 970) and 20 pct noise it reaches about 65 pct (26 of
  40). The two routes are more text or less noise. Pooling c3+c4 adds about 370 boxes at 8.5-10 pct noise, so a
  pooled c1-c4 run at a noise mix weighted to the pages is the one cheap way to raise power (H59). If the pooled
  planted control still reads under 80 pct, no passable control exists at this N and the design waits on material.
- B's English fit gap (real 0.059/0.077 vs Folger 0.22-0.26, NULL-SPLIT 0.039-0.086) is coarse (2 null instances) and
  does not decide anything. It says only that neither split looks like the Folger's English.
- **For any later composite test:** the null must carry the split. Shuffling a split text reads the split as order.

## 6. Dead vs untestable after two rounds

"Dead" means a control-backed negative on the settled public drafts, for one design. No row closes the target, which
stays `open` (rule 5).

| hypothesis | status | the number that decides it |
|---|---|---|
| French homophonic letters, line order | dead at current noise | A 0 of 8 real vs FR-HOMO-N15 5 of 8 (c2->c1); D/R2-1: FR pairs 0-1 of 40 as low as real under 3:1 indel noise |
| English homophonic letters | dead at current noise | B real at 8th pct of 50 refits vs EN-HOMO-N15 100/100; R2-1 EN 0 of 40 |
| Portuguese homophonic letters | dead at current noise | G 0 of 24 vs PT-HOMO-N15 4 of 4; R2-1 PT 0-1 of 40 |
| Spanish / Latin homophonic letters | disfavoured (control power 1/4, 2/4) | G 8 misses each; R2-1 LA 0 of 40 on c2 (a single order test; ES not in the battery) |
| any homophonic letter or syllable design with in-line order on c2 | dead at current noise, up to 25 pct mixed noise | R2-1 real 0.27-2.56 vs thresholds 5.1-5.6, bal. acc. 0.94-0.96; overturned only if c2's true error > 25 pct (H60) |
| same on c3+c4 (the cleaner verse pages) | untestable at N 370 | R2-1 arm a: 2.84 vs 4.9, but 7-10 of 40 FR/PT/LA as low |
| periodic polyalphabetics, autokey, WORDMIX word code | dead (order, noise-robust) | D round 1, each with a control that reads it |
| Masonic alphabets (pigpen, Copiale values) | dead (shape, not noise) | F: pigpen shapes 3.8-5.2 pct of tokens |
| Copiale-type word symbols for the pictograms | dead | H neighbour test p 0.68 vs control 5 of 5; F type count 23 in 60 vs Copiale <= 8 |
| X as a word space | dead | D p 0.25 / 0.36 vs control 0.000; F null at 64 pct power; E3 |
| c4 = contiguous copy of the 8 pool texts, letter-level or running key, <= 15 pct noise | dead | R2-3: real R 0.815, couplet null reaches it 66.5 pct; controls R 0.85-0.99, rank 1 10/10 |
| c4 = copy of an author not in the pool (Chivers, Colesworthy, Peterson's, Lamartine, Béranger, Musset) | open (untested) | same R statistic against an extended pool; the control already passes (H63) |
| c4 copied non-contiguously / patchwork | untestable by the window statistic | needs a different instrument |
| syllabic / mixed design (solver) | untestable until noise drops | C FR-SYLL 64.7-67.0 clean; R2-3 syllabic control ranks 9-25,954 |
| Copiale method, automatic solve | untestable until noise drops | H: fails at 8 pct+; public pixels read 15.6-17.7 pct (R2-2) |
| any c1->c2 held-out fitted key | untestable (reach) | README reach; HARNESS-2 K5 passes nothing even clean |
| composites as ligatures (split restores order) | untestable at 24 pct composite share (main test); D2 lead open | R2-5 planted 0.555 / 25 of 40; D2 real-N 9.55 vs null max 8.9, planted power 65 pct (H59) |
| vessels close lines | untestable at this N (selection) | R2-4: 5 of 8 but 0 of 3 for the containers not position-selected; controls K1, K3 fail |
| pictures open lines | holds (licensed, round 1) | H31/H35: 9/45 layout-excluded, p 0.0002; R2-4 sanity 11 vs 2.36 |
| picture-opened verse lines start couplets | non-test (R2-4 gates) | 1 of 4, p 0.957 |
| R34 columnar transposition, height 34 | open, fragile | D: fresh p 0.03, gone p 0.80 with punctuation boxes kept; RULE.md now fixes the box set (H62) |
| running key, 35 pct+ random filler (beyond the R2-3 copy test) | untestable by order tests at any noise | needs a crib instrument (R2-3's covers running key only for a copy of the pool) |
| tilde marks as nasal vowels (Sektu) | open, gated | H56: 0.8-1.5 per verse line by convention; H57 re-labelling needs vision calls |

## 7. Next rows

Every row below runs on public data, is CPU-only, carries a known-answer control that must pass first, and costs
under USD 5. Ranked by expected value, cheapest first where two tie. Appended to CAMPAIGN.md as open rows (needs
nobody); not run here.

1. **H59, D2 split lead, replicated with power** (rank 2, est_usd 4). R2-5's one positive, at the null that carries
   the split. Pre-register both split orders with a two-order correction, fresh seeds, and 500+ NULL-SPLIT draws plus
   a box-level NULL-HABIT. Pool c1-c4 (c3+c4 add about 370 boxes at 8.5-10 pct noise). Apply RULE.md's stroke folds
   before splitting. Control first: the planted French ligature text at the pooled N, 24 pct composites and a
   page-weighted noise mix must reach D2 power >= 80 pct. If it does not, log "no passable control at this N" and
   stop. Kill: real-N at or below the 99th percentile of 500 nulls, or failing the habit null.
2. **H60, D's battery at the H51 upper bound** (rank 2, est_usd 1). Rerun R2-1's calibration (`r21.py`,
   `run_calib.sh`, `dcore.py` unchanged) on the c1/c2 shape at 30, 35 and 40 pct noise, 3:1 replace:indel. This is a
   control-only run. The real scores are already on file and are not recomputed. Report the bal. acc. and the number
   of language pairs at or below the real 0.96 / 2.56 / 0.27. Kill (for the "noise could hide order" objection): the
   battery still separates at >= 0.80 at 40 pct, so c2's no-order result holds across the whole H51 bound. If
   separation fails below 40 pct, the order result is conditional on c2's true error being under that level, and
   the digest's section 2 is amended to say so.
3. **H61, coarse folds on R2-2's control, re-scored** (rank 3, est_usd 0.5). No new reader calls: `control/reads_*.tsv`
   against `truth.tsv`. First declare the six pixel-limited folds (EIGHT+VENUS+THREE, C-BAR-X+ARCH-DASH,
   CIRC-O+BLOB, O-SLASH+PHI, II-DASH+CC-DASH, S-CURL+DOUBLE-LOOP) in a PREREG committed before scoring. Then report
   the two-reader error and each single-reader error under them, and the resulting K on c1+c2. Known answer: the
   synthetic page itself. Kill: folded two-reader error >= 5 pct, in which case even the coarse fold does not lift
   the public floor. If it reads under 5 pct, the folded c1+c2 is a candidate lower-noise text, with the polyphony
   caveat of section 3, and any use of it reports both ways.
4. **H62, R34 recheck under RULE.md** (rank 4, est_usd 2). DIGEST-1's R2-6, now runnable because R2-2 wrote the
   sign-or-mark rule. Rerun `G-D/reread.py` on the c2 reading with RULE.md applied, 200-scan own-shuffle null, and
   the halves check as D pre-registered. Known answer: D's TRANS-7/19/33 planted transpositions rebuilt on the same
   box set must pick their own height in 10 of 12 or better. Kill: p > 0.05, or either half at or below 0. Lowest of
   the four: one test family of about ten, already fragile once.

Ranked below the cut and not appended: **H63**, extending R2-3's pool to Chivers, Colesworthy and *Peterson's* 1879
(Internet Archive full text) and Lamartine, Béranger and Musset's verse (Wikisource). The control already passes, but
it tests only letter-level contiguous copies, which D's and R2-1's order results already make unlikely for c4's
design. Worth running only if a syllabic crib instrument exists to run beside it.

**What would reopen the solver track** (none of it public-data work this digest can start): images sharper than the
Schmeh/Cipherbrain PNGs, with R2-2's control rebuilt on them first; a reading protocol, human or machine, that reads
R2-2's synthetic page under 5 pct; a fixed key from outside (a period alphabet, or a crib from his papers), which the
frozen bar can gate as it stands; or a syllabic crib instrument whose own control passes.
