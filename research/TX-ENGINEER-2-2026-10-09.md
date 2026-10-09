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

## Headline numbers (S1-S5)
| what | figure | source |
|---|---|---|
| S1 held-out gain | no instrument earned an eval look; eval looks spent 0; the pool is 28 unflagged errors (tuned-letter lines: eval_heldout 10 + f178r 6; held-out leaves: Spinelli 6 under the corrected sheet + f152r 1 + gunther 5), gate p < 0.05 at >= 24 (Amendment 7); nothing is past dev to spend a look on | PREREG-txeng2-0 |
| S2 confirm2 | FROZEN 21:3x (the orchestrator's decision: the product baseline on an unseen hand); reads running, verifier running, the lane scores once after both; not yet looked at | PREREG-txeng2-S2 FROZEN |
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
41 workers ledgered 211.02 (round 8: TXE2-SHEET3 1.49, TXE2-SHEETS-ALL 3.42, TXE2-REGFIX 1.99) + round 9 (caps 33); lane orchestrator incarnation 1 about 23 by get_session, incarnation 2 19.1 at 21:24. Eval looks 0, S2 looks 0; read-free eval openings: 0d 1, X9 1, X1b 3, V2 1, f178r baseline 1.
