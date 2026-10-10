# TX-ENGINEER-2: results of the second transcription-engineering campaign (LANE TX-ENGINEER-2, account 4, Fable; 9 Oct 2026)

INTERIM, 9 Oct 2026 17:5x UTC by date -u (incarnation 1, session_01NmaB9fhuaMSMYexV4NaVsR; the programme is standing,
research/TX-PROGRAM.md, so this file is updated by each incarnation and never final). Brief
`.claude/briefs/runs/2026-10-09-account4-lane-tx-engineer-2.md` + Amendment 1; pre-registrations `benchmark-tx/PREREG-txeng2-0.md`
(S1-S5, the gate, Amendments 1-2), -1, -2, -3, -4, -S2 (draft); the ideas register `research/TX-IDEAS-2-2026-10-09.md` (statuses,
results log, TX-RED answers); the one memory `research/TX-REGISTER.tsv` (tools/tx_register.py); the adversarial review
`research/TX-RED-2026-10-09.md`; per-experiment results under `benchmark-tx/txeng2/<job>/RESULTS.md`.

## For the owner, in plain words

Success was defined before anything ran: the new pipeline must read a held-out pool of known-answer signs with fewer errors
than today's, by a paired count (signs fixed minus signs broken) that clears a pre-registered test on a pool big enough to show a
30% gain, plus one look at a fresh leaf (the confirm2 item) built by someone outside the lane. The first thing we checked was the
measurement itself: the first campaign's units carried 12-15 errors, which gives a genuine 30%-better instrument about a 1-5% chance
of passing, so its twenty-three "nothing works" results were mostly non-tests. We rebuilt the pool (a second Birago leaf from its
decipherment slip; the Spinelli leaf reused) to 29 unflagged errors (a verifier has now checked the Spinelli positions every reader got wrong the same way, flagging 2; the three lines of no.87's recto, which had sat outside both halves though five earlier instruments had been scored on them, were added as a held-out unit), chose the test from a power table, and ran the controls
(a planted 30% fixer passes 85% of the time; a no-op, a random change and a worse instrument pass 0%).

Fifteen experiments then ran, each pre-registered, each scored on development lines before any held-out look. None earned a
held-out look. The honest summary: the signs today's readers get wrong are look-alike pairs that every reader, in every
presentation, reads the same wrong way. A classifier trained on the family's clean tiles broke 11 signs for 1 fixed; the same
classifier trained on this hand's own ink fixed 3 and broke 0 but on too few tiles to count; a wider candidate list now holds
the right sign at 10 of 12 errors but neither a word-level language model nor a reader shown the candidates can pick it (the
reader took the wrong alternative 14 times in 19); showing the hand's own page beside a doubtful sign removed the pull that
printed exemplars caused but gained nothing. Two things did move. First, the sorter feed: a read-free rule now finds 10 of 12
development errors at 14% of positions flagged, and in an oracle-bounded simulation (the truth standing in for you; real owner decisions on file moved 0 of 3) it takes the held-out lines to 2% in about 22 decisions per tile instead of 32 (propagating a decision to a whole atlas cluster is destructive on this atlas, so each decision counts for
one tile, or one pile within a cluster at most). Second, cost: one call per page read a Dinteville leaf at about a third of the tokens of one call per line at 2x, at an accuracy
within one reader's spread of the per-line call (replicated on a second reader and a second hand); neither Opus arm beat the best
Sonnet single pass on either leaf, which became its own experiment (the reader model, X21): the full two-reader pipeline run with
Sonnet readers and again with Opus readers on the same crops came out even on the two leaves whose truth is independent of
both (12 fixed, 14 broken), and the one leaf where Sonnet looked far better turned out to be scored against its own Sonnet
reading, so that result was set aside; re-run on independent truths only, the two reader models came out even (Opus ahead 17 to 11, not significant), so the readers stay as they are.

The most useful finding of the last hour came from the verifier, not from an instrument: the sign sheet the readers are
given for the Spinelli letter shows one of the letter's own h signs as an example of the SIX cell, so three of that leaf's
twelve remaining errors are the sheet's fault, not the reader's. Because that was found by looking at the answer key, fixing
the sheet counts as a change to the baseline, never as an instrument's gain; the sheet has been corrected (three mislabelled example tiles found and removed; every other sheet in use is cut from a printed key or
is a text list, so has no such defect), and the Spinelli baseline re-read under the corrected sheet came down from 12 unflagged errors to 6 (8 signs fixed, 2 broken). That
is a correction of the measuring stick on a leaf the sheet was built from, not a gain of the pipeline on an unseen hand; the one
number that would be is the confirm2 leaf, still unopened. With the Spinelli count halved the held-out pool fell to 23, one under its
floor; a further known-answer leaf built outside this lane (a 1561 letter of Willem van Oranje's German secretary, with a printed
decipherment as its answer key) brings it back to 28, so an instrument can be scored again once its flags have been checked. The
one grown-sheet instrument that was waiting has been retired before running: at most 5 of the 6 remaining Spinelli errors are
reachable by it, and 5 fixed with none broken cannot clear the pre-registered test, so it could not pass even if perfect. What
it found is three missing cells in the Spinelli sheet, which are being added from the published key as a further baseline change. The overlap note in every reading
instruction turned out to be wrong on every folio but two (the readers measured 350 to 1,100 pixels where the text said 100 to 150),
but the readers' deletions and insertions do not cluster at the seams, so the sentence is corrected for future briefs and nothing
is re-read for it.

The known-answer material for hands that read at 10-25% is the real bottleneck. Three glossed Dinteville leaves and one Birago
1591 leaf were fetched from DECODE and built, but a key rebuilt from a gloss cannot score the reads it was built from, and the
printed-key truth over-charged homophones; after the fix the readers also saw the gloss on three of the four leaves, so those
items serve read-free instruments only until a masked re-cut from Gallica's native image (blocked all day) exists.

What you should do at the sorter: the feed (TXE2-FEED, being written) lists the tiles; one decision per tile; never propagate.


**S2, the one unseen-hand number (added 22:2x UTC 9 Oct by incarnation 3).** The look has now been taken, once, after the adjudication step was re-run properly. On the confirm2 leaf (a Saint-Gouard clerk hand of 1573 that nobody in this lane had read, with only a shape list of its signs as support and no examples from the hand, on a leaf the project's own folder had read a week earlier) today's pipeline reads at 15.0% of unflagged signs wrong (75 of 500; 29.6% on all 1,068 counting the positions whose answer rests only on two blind readings of the period decipherment), and the two-pass-plus-adjudication pipeline did no better than either of its single passes. Beside it, the builder's own two passes of 4 Oct, from which the reference reading and its flags were made, score 4.8% and 7.4% on the same set -- a floor-adjacent figure by construction, not a second reader: a label-inventory check with no answer key shows the fresh readers used a different sign list (half the colon marks dropped, capital S written as s, other names for two signs), so we checked whether some of the 15% was naming rather than reading (the fresh readers' sign list differed from the reference's): it was not -- a normalisation built before looking at any error moved the figure to 15.4%, and of the 75 errors none is a naming difference, 42 are signs dropped or added and 33 are misread signs. The two figures are two scores under two masks, not a range the truth lies in (an outside review of 10 Oct corrected our earlier 'bracket' wording): the lower one counts only the 500 signs where the item's earlier reading already agreed with the period decipherment, the higher one counts 236 doubtful answers against the readers as well; the earlier reading itself scores 3.2% and 22.1% on the same two sets. The same review found three faults in the scoring tool itself (a line the readers skipped is not charged, the paired test counts a different set of signs than the headline rate, and an inserted sign that a change removes is invisible to the adoption test), so both figures will be re-scored once with a corrected scorer on the same frozen readings, as a corrected audit, never a new look. Both scores sit well above 5% and a scorer fix cannot bring them under it, so the honest answer to 'does an unseen hand read at 5%' stays no: not this one, not under today's pipeline. On the sibling leaf f.102r, read the same way as a development check, the pipeline reads 19.9% of unflagged signs wrong (80 of 403), mostly by inserting signs the reference does not have; that leaf's answer key turned out to be anchored in the wrong place in the clerk's decipherment (about 750 letters too late); re-anchored where the scan put it, the same readings score 12.4% of unflagged signs wrong (6.3% misread or dropped plus 2.2 inserted signs per 100 read), and a single reading pass alone does better than the two-pass pipeline there (9.6%). All of these figures are value-level: a sign misread as another sign with the same meaning scores as right, so the true visual error is not lower than them. Three of the failure classes are specific, not diffuse: one two-dot mark dropped at 24 scored places, a 3-for-z confusion, and 33 descriptive tokens for signs the readers could not name under the sheet's own rule -- repairable by sheet and brief for a later leaf of this hand, never for this number. The next step named for the item is a check of its flags against the clerk's own pages once Gallica answers after midnight UTC, never a re-read.

**Corrected audit of that number (added 01:1x UTC 10 Oct by incarnation 4).** The scorer was corrected as the outside review asked and the same frozen readings were re-scored once: the two figures come out the same (15.0% of the 500 unflagged signs, 29.6% of all 1,068), and beside them the standard edit-distance count reads 13.4% and 28.8% (the standard count pairs some inserted signs with misread ones; a convention, not a different reading). No line was skipped by the readers, so the review's missing-line fault did not touch this number. The paired comparison against the leaf's earlier reading now counts whole lines on the same signs the rate uses: 0 lines better, 23 worse, 13 the same -- which says only that the earlier reading is the one the answer key was aligned to, as we already knew, not anything about the pipeline. A separate read-free scan found the answer key's alignment on this leaf 155 letters short of its best position (a near miss of our own gate, unlike the sibling leaf's 750-letter miss); a second answer key is being built at the better position and the same readings will be scored once against it, with the result put beside these figures. Nothing in this changes the answer: this hand reads at 15% and 30% under the two masks, not 5%.

**Update (added 02:5x UTC 10 Oct by incarnation 5).** The second answer key announced above was not built: its build stopped at its own check, because the supposedly better position turned out to be the same alignment to within 26 letters, so no second figure is coming and the numbers above stand as checked. Separately, a printed copy of the letter's closing passage (Groen van Prinsterer's edition, printed from a different manuscript) was used by a verifier to check the clerk's text where our two blind readings of the clerk's hand had disagreed: it confirms the clerk at 84 of the 182 doubtful letters it covers, against a chance level of at most 9. It could only confirm, never contradict, so the other 98 stay doubtful. Counting those 84 positions as sound widens the stricter count from 500 to 576 signs and moves the lower figure from 15.0% to 14.1%; the higher figure stays 29.6%. The answer key of record is unchanged; whether to adopt the widened count for later comparisons is the orchestrator's call. (The orchestrator decided at 03:0x: the widened count is the one later comparisons on this leaf will use; the figure of record stays 15.0% on 500, always quoted beside 14.1% on 576.)

**The first reader experiment with headroom (added 03:3x UTC 10 Oct by incarnation 5).** On the development leaf of the same hand (f.102r, 679 signs with a sound answer), today's readers were given a picture sheet cut from the printed key instead of the text list they had before; everything else was kept. Errors fell from 84 to 60 of 679 (the edit count by 27%), and 16 lines improved against 8 that got worse. That did not reach the pre-registered line-level test (which needs more lines than this leaf has to be sure), so it licenses nothing yet; the two single readings behind it both beat the old reading on their own. Two things could still explain it besides the sheet: ordinary run-to-run spread, since the old reading is a single run, and one sentence about plain words that changed at the same time. A control run with the old text list under the new sentence is running to separate them; if the picture sheet still wins by the declared margin, the next step is the same test on a second hand, and only then a rule for the product.
## Headline numbers (S1-S5)
| what | figure | source |
|---|---|---|
| S1 held-out gain | no instrument earned an eval look; eval looks spent 0; the pool is 29 unflagged errors (tuned-letter lines: eval_heldout 10 + f178r 6; held-out leaves: Spinelli 6 under atlas_v5 and the declared notation fold + f152r 1 + gunther 6 under the corrected sheet), gate p < 0.05 at >= 24 (Amendment 9); nothing is past dev to spend a look on | PREREG-txeng2-0 Amendments 7-9 |
| S2 confirm2 | **look taken 22:22:57 UTC 9 Oct (1 of 1): the frozen pipeline (two blind Opus passes + reconcile + packet-shape Sonnet adjudication, S2-ADJ) reads the unseen Saint-Gouard clerk hand at 0.296 as measured (316/1068) and 0.150 flagged-excluded (75/500; flags from the two blind clerk reads, not the clerk image, 568 of 1,068 flagged); single S2 passes 0.148 / 0.154; the builder's own earlier passes 0.048 / 0.074 beside (committed 0.032, a floor by construction). A product baseline on an unseen hand, never a gain. Two scores under two masks (the 'bracket' wording withdrawn 10 Oct on the outside review): 0.150 on the 500 positions with verifier flags dropped (54 + 21 insertions) and 0.296 on all 1,068 (295 + 21), committed's own 0.032 / 0.221 beside; a corrected-audit rescore with the fixed scorer (TOOL-SCORER-FIX) owed; error mass by class (F38): ':' mark dropped x24, 3/z, invented sign names, look-alike residue; the notation audit (S2-NOTE) found notation 0 / segmentation 42 / read 33 of the 75, companion 0.154 / 0.301 beside the look -- not a notation artefact; the look stands** | PREREG-txeng2-S2 "S2 look taken"; benchmark-tx/txeng2/s2score/ |
| S3 live letter | TXE-R (first campaign, same pipeline): f.117r err_2reader 0.134, S 207 vs 190 committed, judge 0.010 worse, no licensed change | ciphers/birago-fr3252-1571-72/harvest/f117/RESULTS-TXE-R.md |
| S4 sorter | feed: dev 10/12 at 14.0% flagged; eval read-free 9/15 at 2.9% (substitute rule); decisions-to-2% per tile: eval 22 (was 32); whole-cluster propagation destructive (77% purity) | benchmark-tx/txeng2/doubt/, sorter/ |
| S5 cost | one per-page Opus call at 0.29-0.30x the input tokens of per-line 2x calls, accuracy within reader spread (dint 0.235/0.318 vs 0.318/0.388; Ceppo 0.122 vs 0.166; N=2 readers x 2 hands); both Opus arms worse than the best Sonnet single pass (dint B 0.188, Ceppo A 0.043) | benchmark-tx/txeng2/cost/, cost2/ |

## The experiment table (gate per PREREG-txeng2-0 + Amendment 2; dev = dev_tune unless stated)
| id | instrument | dev (paired, p) | eval (looks) | verdict | cost |
|---|---|---|---|---|---|
| 0a | power audit (tools/tx_power.py) | first-campaign units 0.8-5% power | n/a | gate set | lane |
| 0b | f152r item (slip truth), DECODE gloss items f.89/f.98v/f.113/f.23r, kp/kp2 truth variants | f89-kp2 passZ 0.124 | f152r 5 errors (2 unflagged) | pool 26; gloss items gated out pending C1 | 6.2 + 55.6 + 5.7 |
| 0d | error map with reader agreement | dev 6/37 all-same-wrong | eval 8/29 | on file | 2.4 |
| X2 | pair classifier, secure tiles of other leaves | 1/11 p 0.006 | none | dev-FAIL | 2.2 |
| X2b | pair classifier, the hand's own ink, LOO | 3/0 p 0.25 | none | dev non-test (right way) | 2.3 |
| X3 | widened lattice + word LM at doubt positions | truth-in-lattice 10/12; 4/5 p 1.0 | none | dev non-test | 2.6 |
| X4 | calibrated top-3 confidence | top-3 holds truth 3/12; weights 2/9 | none | dev-FAIL | 6.0 |
| X5 | learned reader weighting | 3/7 p 0.34 | none | dev non-test | 3.2 (with X19) |
| X6 | sorter value curve (measurement) | cluster propagation destructive; per tile 3-6 of 7-27 in 20 | read-free | measured | 3.5 (with X20) |
| X7 | same-page strips at doubt positions | 5/4 p 1.0; swapped control 3/28 | none | dev non-test | 7.3 |
| X8 | cost per 100 signs (measurement) | page call 0.235 @332k vs line 0.318 @1,096k | n/a | measured | 6.5 |
| X9+X17 | doubt detector re-tuned | 10/12 at 14.0% PASS | read-free 9/15 at 2.9% | sorter feed | 3.3 |
| X12 | count-then-read | count gate 5/9 | n/a | FAIL read-free | 5.1 |
| X13 | lattice cells image-checked at 4x | 2/14 p 0.004 | none | dev-FAIL | 6.7 |
| X19 | ink-count deletion detector | flags 83-100% of lines | n/a | FAIL read-free | -- |
| X20 | owner's 4 Oct decisions | 0/3 p 0.25 | none | dev non-test | -- |
| X1 | off-sheet detector + grown sheet | 0/21 at 15% | none | dev-FAIL read-free (Dinteville); X1b on the unseen hands running | 3.0 |
Round 4 running (17:45): C1 kp2 known-answer control, V1 f152r flags verifier, X1b, S4 feed product, X8b.

## What goes into the pipeline, and what does not
Adopted: the doubt feed (latt + vote4 + selfcons where inputs exist) as the sorter's focus list, per tile, never cluster-propagated;
one call per page as the default call shape pending X8b. Not adopted: every instrument above. Retired for this hand (rule 3, with
the first campaign's runs): the compare/exemplar layouts (now including same-page strips and named-cell checks), feature-first,
plain re-passes under rendering, the lattice as a fixer with or without a word-level model, confusion weighting of existing passes.
Open: X2b with more labelled tiles of the same hand (new material); the colour master when Gallica answers (N1); a masked re-cut of the
gloss leaves from a native image; the grown-sheet read on Spinelli only if X1b's recall table licenses it (then the first eval look).

## Costs and looks
55 workers ledgered 282.26 (round 16 so far: TXE2-2RATE 1.96; live: TXE2-GALLICA 6, TXE2-VIV102-REANCHOR 8, TXE2-VIVWIT 3) + round 17 (TOOL-SCORER-FIX cap 8); lane orchestrator incarnation 1 27.38, incarnation 2 29.41, incarnation 3 live. Eval looks 0, S2 looks 1 (22:22:57 UTC); read-free eval openings: 0d 1, X9 1, X1b 3, V2 1, f178r baseline 1.
