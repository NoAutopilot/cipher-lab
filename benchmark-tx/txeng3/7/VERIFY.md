# VERIFY TXE3-7 PROPAGATE (11 Oct 2026, 15:1x UTC by date -u)

Verifier for the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M). I did not run TXE3-7 (worker
session_01N6wTuin3FG55h6UUkN9Kpo) and I re-derived everything from committed files only: no model reading pass, no
image read, no network beyond git. I opened no owner sorter page, no L74 oracle answer and no confirm item. I changed
none of the experiment's files; this file is the only one added.

## Verdicts in one place

| # | Claim told to the owner (about 07:05 UTC) | Verdict |
|---|---|---|
| 1 | "Applied through the family atlas to a letter he never sorted, the owner's labels came out no better than without them (the machine's starting labels)." | **overstated.** The numbers and the registered null re-derive exactly. But on the one letter he never sorted (f152r) the test can only show a large effect, and the letter with enough signs to measure (no.87) is one he did sort, in a separate 4 Oct sort that was not used. Only one classifier was tested, and in the override arm his labels did measurably worse than the machine's. |
| 2 | "Reuse his sorts so he is never asked twice, not as an accuracy step." | **overstated.** Only one route was measured: a kNN built from his 438 tiles, reading 0.33-0.36. The two mechanisms TRANSCRIPTION.md actually prescribes were never tested: cluster-level `sign_sorter_apply.py`, and his tiles as the exemplar sheet for a reading pass. Used to overwrite a line read, his propagated labels did harm. "Never asked twice" was not measured; it is a process choice, not a finding. |

## 1. Re-derivation (committed scorer, `benchmark-tx/txeng3/7/score.py` -> `tools/tx_bench.py --exclude-flagged --paired`)

I re-ran `make_labels.py`, `map_f152r.py`, `tools/glyph_atlas.py classify --only-train-labels` for A1 and A2 on f152r, f178v and
f179r (at origin/main 3d5fa95e, which includes the later TXE3-5/TXE3-6 edits to glyph_atlas.py) and then `score.py`. Every label TSV, the
f152r box map, all six classify runs and results.tsv/results.json came back **byte-identical** to the committed files.
Rule 7 is met: the reading regenerates from the transcription, the labels and the tool.

| figure | reported (RESULTS.md) | re-derived |
|---|---|---|
| f152r line read (passZ_pipeline) | 0.069 (5/73); fe 0.029 (2/70) | 0.069 (5/73); fe 0.029 (2/70) |
| f152r A1 machine, atlas | 0.384 (28/73) | 0.384 (28/73); fe 0.371 (26/70) |
| f152r A2 owner, atlas | 0.356 (26/73) | 0.356 (26/73); fe 0.343 (24/70) |
| f152r A2 vs A1 paired (position) | 4 / 3, p 1.0 | 4 / 3, p 1.0 (fe 4 / 3, p 1.0); lines 2 improved / 1 worsened, line_p 1.0 |
| f152r gain A1-A2 | +0.027 | +0.0274 |
| f152r null gains p95 | -0.41 | -0.4109 (mean -0.4815, max -0.3972); null err 0.781-0.918 |
| f152r A0a cluster-name atlas | 0.192, vs A1 16 / 5 p 0.027 | 0.1918, 16 / 5 p 0.0266 |
| f152r A1 / A2 override | 0.069, 0 / 0 | 0.069, 0 / 0 (both) |
| no.87 line read (passC) | 0.051 (41/803); fe 0.038 (30/792) | same |
| no.87 A1 machine, atlas | 0.343 (275/803) | 0.343 (275/803); fe 0.336 (266/792) |
| no.87 A2 owner, atlas | 0.329 (264/803) | 0.329 (264/803); fe 0.322 (255/792) |
| no.87 A2 vs A1 paired (position) | 41 / 33, p 0.416 | 41 / 33, p 0.416 (fe 40 / 32, p 0.410); lines 13 / 7, line_p 0.263 |
| no.87 gain A1-A2 | +0.014 | +0.0137 |
| no.87 null gains p95 | -0.39 | -0.3910; null err 0.726-0.793 |
| no.87 A1 override vs line read | 0.066, 0 / 11 | 0.066 (53/803), 0 / 11, p 0.001 |
| no.87 A2 override vs line read | 0.080, 0 / 22 | 0.080 (64/803), 0 / 22, p <0.001 |
| pooled A2 vs A1 atlas | 45 / 36, p 0.37 | 45 / 36, p 0.374 |
| can-vary A1 != A2 top-1 | 19 of 90; 125 of 714 | 19 of 90; 125 of 714 (can_vary.json regenerates) |
| boxes / owner != machine | 438 / 121 (moved 175) | 438 / 121 (moved 175); dropped 43 no 1:1 box, 7 aside/bad-cut/empty |

The gains differ slightly between the two scales because tx_bench's err_true charges indels at 0.75 while the position
McNemar counts net positions (no.87: 11 net errors vs 8 net positions; f152r: 2 vs 1). Both are as committed.

**Not in RESULTS.md but registered outputs, computed here with the same scorer:** the paired A2 override vs A1 override on
no.87 is **0 fixed / 11 broken, p 0.001** (lines 0 improved / 7 worsened, line_p 0.016). In the one arm that sits on the line
read, the owner's labels are worse than the machine's. None of these 11 involve X_NEW; all are unanimous votes into a wrong family
(T33 x3, T60 x2, T85 x2, T63 x2, ...). On f152r both override arms are 0 / 0.

Approximate 95% intervals on the A2-A1 gain (position level, normal approximation on the discordant pairs): f152r +0.014
(-0.057 to +0.085); no.87 +0.010 (-0.011 to +0.031); pooled +0.010 (-0.010 to +0.030). f152r cannot rule out a gain or a
loss of 6-8 points. no.87 rules out a gain larger than about 3 points on a classifier that is itself at 0.33.

## 2. Pre-registration order

| commit | time (%cI) | what |
|---|---|---|
| f70bc534e | 2026-10-11T05:57:52Z | PREREG-txeng3-7.md |
| ecde11e97 | 2026-10-11T05:57:52Z | prereg header clock 06:0x -> 05:5x (one line, no design change) |
| 5552b57eb | 06:00:27Z | glyph_atlas classify --only-train-labels + offline test (test passes here) |
| d61b2b225 | 06:04:42Z | label TSVs, f152r box map, run_arms.py, score.py |
| 65a3c5742 | 06:08:07Z | every arm output + can_vary.json, before scoring |
| af6528f10 | 06:10:38Z | results.tsv/json, RESULTS.md, LEDGER row |

The prereg came before every output and every score, and it was not edited after scoring. The hash it cites as the prereg
push (`c351e72e`, in RESULTS.md and the ROOM claim line) does not exist in this repository. It looks like a pre-rebase local
hash; the prereg as pushed is f70bc534e. This is a citation slip and does not affect the order.

The two deviations are declared, in RESULTS.md and in the LEDGER row. (a) 438 boxes rather than 445: the prereg's own drop rule
removes 7 aside/bad-cut/empty tiles. (b) 121 owner-vs-machine label differences rather than 206, after the pre-registered family
stripping. The "gain per owner decision" lines still divide by 206, and RESULTS says "19 decisions reached the target" where 19
is a count of boxes whose top-1 changed, not of decisions. Both are minor.

## 3. Gate as registered, and what it yields

Registered: "**Transfers** on a target iff A2 err_true <= A1 - 0.02 AND fixed > broken with sign p < 0.05 AND the gain exceeds
the p95 of the 20 null gains. Anything else is a null result."

- f152r: gain 0.027 >= 0.02 yes; 4 > 3 yes; p 1.0 < 0.05 **no**; gain > null p95 (-0.41) yes -> **FAIL (null)**.
- no.87: gain 0.014 >= 0.02 **no**; 41 > 33 yes; p 0.416 **no**; gain > -0.39 yes -> **FAIL (null)**.
- Flagged-excluded beside: f152r 0.343 vs 0.371, 4/3 p 1.0; no.87 0.322 vs 0.336, 40/32 p 0.41. Both are still FAIL.

The reported verdict, null on both targets, follows from the gate as registered, and score.py implements the gate as written.

## 4. Control (rule 3)

- **A1 machine labels** is the control that matters. It shares the same 438 tiles and the same classifier, and differs only at the
  owner's decisions. It can vary on the statistic: top-1 differs from A2 on 19/90 f152r boxes and 125/714 no.87 boxes, counted
  before scoring. A1 and A2 then differed by noise (above). This is a real test, not a non-test.
- **A3 permuted null** also varies, but only trivially. Permuting the codes destroys every association between shape and label,
  so any non-random label set beats it by about 0.4. The gate's third clause therefore cannot separate the owner's decisions
  from the machine's labels and is close to vacuous. It did not decide either verdict.
- Third-attempt clause: MQS-CLASSIFY-ROUNDS (9 Oct) was the first atlas-kNN transfer test, with gain 0.000. This run changes one
  knob (`--only-train-labels`) and is again null. The next step RESULTS proposes is decision-level relabel rules "for tiles
  whose kNN neighbours are owner-moved tiles, applied to the line read". It still uses atlas-kNN neighbourhoods as the trigger,
  and it is close to the override arm already measured here (0 fixed / 22 broken vs the line read). Before it is briefed, it
  should be argued as a genuinely different instrument; otherwise it is a third pass with the same instrument, and the
  third-attempt clause would retire it.

## 5. Split

Both targets are BENCHMARK-TX **eval** items (birago1572-f152r, birago1572-no87). No dev item of this hand exists. Nothing was
tuned: kNN 5, the unanimous override rule and the f152r x-bounds were all fixed in the prereg before any score. I found no
eval look used for tuning. A0a on no.87 uses cluster names partly drawn from no.87's tune lines, and the worker correctly
reported it without gating it.

## 6. The claims

**Claim 1, overstated.** Evidence for it: both registered gates FAIL, the control can vary, and every number re-derives. Why
the sentence is still stronger than the evidence:
- "A letter he never sorted" is strictly f152r only: 73 scored signs and 7 discordant positions. The prereg itself says f152r
  "can show only a large transfer", and its interval runs from -0.057 to +0.085. The powered result, no.87, is a letter the owner
  did sort (`sorter/no87/owner-sort-2026-10-04/settled_no87.tsv`: 21 moved, 217 kept). That sort was excluded from training, so no.87 is
  "not among the sorted tiles", not "never sorted".
- Only one route was measured: a kNN on the atlas's HOG+PCA features, built from his 438 tiles. It reads 0.33-0.36, five to seven
  times worse than the line reads. The scoring is value-level, so the 54 mapped within-family splits are invisible, and his
  unvalued X_NEW-* piles can only score as wrong.
- In atlas mode the point estimate favours his labels on both letters (26 vs 28 errors; 264 vs 275), within noise. In
  override mode they are worse than the machine's (no.87 0 / 11, p 0.001). "No better than" hides both directions.
- Robustness, post hoc and labelled as such: in 10 of the 33 no.87 positions his labels broke, the owner arm voted X_NEW.
  Nine of those are o-valued tiles (truth T19|T52|T55) that A1 read as T19 or T52; the tenth is a T51. This fits his moves of
  3 T19, 2 T92 and 1 T96 tiles into the new pile X_NEW-l, but I infer that link and did not trace it per vote. The prereg's
  stripping rule cites BIR87-ALIGN's "every testable owner pile carries its family's printed value", which cannot cover an
  X_NEW-* pile, since X_NEW has no printed value. Excluding only those positions gives 40 / 23, p 0.04, but that adjustment is
  one-sided and invalid. Under a symmetric rule, where an X_NEW/UNREAD
  top-1 keeps the line read in both arms (as `_` already does), the result is still null: no.87 239 vs 251, 41 / 32, p 0.35;
  f152r 24 vs 27, 4 / 3, p 1.0. The null is robust to that scoring choice.

Corrected sentence: *"Measured one way (a shape classifier built only from your 438 sorted Birago 1572 tiles), your labels
did not measurably beat the machine's starting labels on the same tiles. On no.87, which has enough signs to tell, the gain was
+0.014 (41 fixed, 33 broken, p 0.42), and the pre-registered test fails. On f.152r, the letter you never sorted, the test was
too small to show anything but a large effect (4 fixed, 3 broken). Used to overwrite the line read, your labels did worse than
the machine's (0 fixed, 11 broken on no.87). Both classifiers read five to seven times worse than the line reads."*

**Claim 2, overstated.** TRANSCRIPTION.md's rule ("apply every owner decision already made in its key family
(`tools/sign_sorter_apply.py`, cluster-level) and use the owner-labelled tiles as the exemplar sheet for that hand") names two
mechanisms, and this experiment measured neither. It measured a third: his tiles as the only kNN voters, which no pipeline
uses as a product. Saying "not as an accuracy step" in general goes beyond one null on one route. The registered override arm
also shows that propagating his labels onto another letter's line read does harm, worse than the machine's labels, so
"reuse" must not mean auto-overwriting readings. "Never asked twice" is a sensible process rule, but it is not a result of this
experiment.

Corrected sentence: *"Keep your decisions on file so you are never asked about the same tile twice. Carried to other letters by a
shape classifier, they gave no measurable accuracy gain, and used to overwrite a line read they did harm, so do not expect an
accuracy gain from reuse by that route. Whether they help in the two ways the transcription rule actually uses them (cluster-level
application, and as the exemplar sheet for a reading pass) has not been measured."*

## 7. Rule issues and objections

1. No flagged-excluded figure is quoted alone. RESULTS.md and the LEDGER row give "as measured" with fe beside it or not at all.
2. Cost: the LEDGER row gives USD 11.45, under the USD 15 cap. Time: about 05:45-06:10 UTC, under 2 h. 0 requests, 0 subagents.
3. Novelty words: none found.
4. The prereg hash `c351e72e` cited in RESULTS.md and the ROOM claim does not exist on origin/main; the real one is f70bc534e.
5. RESULTS.md "What it means for the owner" calls reuse "therefore safe". The registered override arm contradicts that for
   any reuse that overwrites readings: no.87 A2 override 0 / 22 vs the line read and 0 / 11 vs A1 override. "Safe" holds only
   for keeping the labels on file.
6. RESULTS.md never states the A2-override vs A1-override paired figure (0 / 11, p 0.001), the one place his labels differ
   measurably from the machine's, and it is against him. The "0 fixed / 33 broken pooled" line pools two arms (A1 11 + A2 22),
   not two targets.
7. The "gain per owner decision" lines divide by 206, but only 121 labels differ after the declared stripping. "19 decisions
   reached the target" counts boxes, not decisions.
8. The gate's null clause (A3) is near-vacuous by construction (section 4). A future prereg on label transfer should use a
   null that keeps shape information, for example the machine labels with the owner's 121 changes moved to random other boxes.
9. The proposed next step reuses atlas-kNN neighbourhoods and resembles the override arm already measured (section 4,
   third-attempt clause).
10. Side note, outside the two claims: the prereg states that the "reconciled plus the owner's sorted labels 0.042" figure on
    no.87 is output L, the NO87-LABELS relabels. That is a value-blind subagent re-read plus a verifier's ruling (NOTES.md
    "NO87-LABELS", LEDGER 3 Oct 2026), not an owner decision. If the owner-facing premise "your sorting gave the biggest gain"
    (experiment 1's "builds on") rests on that figure, it is misattributed. I did not trace it further; the parent should
    check before repeating it.

## Safe sentence for the owner

Your 4 Oct Birago sort, carried to other letters by a shape classifier, gave no measurable accuracy gain over the machine's own
starting labels. The never-sorted letter was too small to show more than a large effect, and used to overwrite a line read
the labels did harm. Keep the decisions on file so you are never asked twice. The two ways the transcription rule actually uses them
(cluster-level application, exemplar sheet) are still unmeasured.

## Second check (11 Oct 2026, written 16:28 UTC by date -u, by the account-3 parent from the second verifier's report; workflow wf_35ed2244-0e6)

A second, independent agent ruled on each objection and non-holds verdict above, re-running the commands itself. Where it disagrees with this file, this section governs.

### Rulings on the first verifier's objections

- **partly**: 1. RESULTS.md calls family-wide reuse 'therefore safe', but the override arm contradicts that for any reuse that overwrites readings (A2 override 0/22 vs the line read, 0/11 vs A1 override, p 0.001). It is safe only as keeping labels on file.
  - Evidence: I re-ran score.py at d1fdd0ba8 and results.tsv/json came back byte-identical. Override vs the line read: A1 0/11 (p 0.001) and A2 0/22. So 'safe' does need a qualifier: overwriting a line read with this classifier's votes does harm. Attributing that harm to the owner through the 0/11 against A1 override does not hold up. I re-ran `tx_bench.py A2_override --paired A1_override` and got 0/11, p 0.001, lines 0/7, line_p 0.016. Then I went token by token. At all 14 tokens where the A1 and A2 override outputs differ, the A1 and A2 kNN top-1 is the *same* code: f178v_11_013 T33, f178v_13_027 T33, f179r_02_008 T80, f179r_03_022 T60, f178v_20_017 T60 and the rest. Only the vote share differs: A1 0.58-0.81, A2 1.00. His labels made the same wrong votes unanimous; A2 is unanimous on 135 no.87 boxes against A1's 93 (can_vary.json). That is the override rule's unanimity threshold reacting to more consistent piles. It is not his labels reading differently. RESULTS 'Reading 2' already says the override 'only breaks'.
- **partly**: 2. RESULTS.md never states the A2-override vs A1-override paired result (0/11, p 0.001), 'the one place the owner's labels differ measurably from the machine's, and it is against him'. Its '0 fixed / 33 broken pooled' adds two arms, not two targets.
  - Evidence: The paired figure is indeed absent. 33 is A1's 11 plus A2's 22. A2 override also broke every position A1 override broke (fixed 0 in the paired run), so 33 counts 11 positions twice; the distinct broken positions number 22. Still, the RESULTS table gives 53 vs 64 errors, so the direction was not hidden. 'The one place his labels differ measurably, and it is against him' is wrong. The difference is unanimity on identical top-1 codes (see ruling 1). Post hoc, the owner arm also differs measurably *in his favour* in atlas mode once his own X_NEW-l ruling is applied (see ruling 5).
- **agree**: 3. The claim says 'a letter he never sorted', but the powered target no.87 was sorted by the owner on 4 Oct (settled_no87.tsv: 21 moved, 217 kept). The never-sorted f152r has 7 differing positions, too few to show anything but a large effect.
  - Evidence: `git show origin/main:.../sorter/no87/owner-sort-2026-10-04/settled_no87.tsv` has 248 rows: 21 moved, 217 kept, 9 bad-cut, 1 not-letter. Of these, 191 are on f178v and 28 on f179r, the pages scored. PREREG-txeng3-7 line 22 says the same. No file under sorter/ mentions f152r. On f152r the paired result is 4/3, p 1.0, and the normal-approximation interval on the gain is -0.057 to +0.085 (I re-checked the arithmetic). Excluding the no.87 sort from training was correct, so the transfer test itself is not contaminated. Only the wording 'never sorted' is wrong for the powered half.
- **agree**: 4. The test is narrower than the rule: TRANSCRIPTION.md line 150 prescribes cluster-level application with sign_sorter_apply.py and an owner exemplar sheet, and the experiment tested neither, only a kNN from 438 tiles (reading 0.33-0.36).
  - Evidence: TRANSCRIPTION.md lines 150-152: 'apply every owner decision already made in its key family (tools/sign_sorter_apply.py, cluster-level) and use the owner-labelled tiles as the exemplar sheet for that hand.' Row 6 (line 23) and step 7 (line 99) say `sign_sorter_apply.py --atlas-labels` writes cluster-level decisions into labels.json for every letter. TXE3-7 used `--only-train-labels`, so labels.json contributes nothing. The cluster-name route it left out (A0a) reads 0.138 on no.87 and 0.192 on f152r, against 0.33-0.38 for the kNN-only route, so the untested mechanism starts from a very different baseline. The exemplar-sheet route needs a vision reader, which this run excluded.
- **partly**: 5. The prereg justifies stripping family suffixes with BIR87-ALIGN's 'every testable owner pile carries its family's printed value', which cannot cover X_NEW-* piles. 10 of the 33 no.87 breaks are X_NEW votes (9 on o-valued tiles). A symmetric post-hoc rescoring (41/32, p 0.35) shows the verdict is robust.
  - Evidence: Agree the premise is misapplied; the verifier actually understated it. Disagree that the verdict is robust. I reproduced the 10/33 X_NEW breaks (9 with truth T19|T52|T55, one with T51). The very source the prereg cites, BIR87-ALIGN RESULTS.md, values X_NEW-l at **o** (6/7, grade C) and recommends merging it into T19. The owner's own committed answer, harvest/ownersort/adj/owner_review_2026-10-04.tsv q2, says 'merge X_NEW-l into T19 (owner said so twice)'. It was committed at 07:40 UTC on 4 Oct, after the 06:51 sort export, and nothing since overrides it; BIR-KEYFIT applied it. TXE3-7 mapped X_NEW-l to X_NEW, a pile with no value, so those tiles can only score as wrong.

I re-ran the arm with only that ruling applied: 7 of 438 boxes moved from X_NEW-l to T19. q3 is already in settled_corrected, and q4's tiles sit on shared boxes, so neither changes anything. Method: glyph_atlas classify --only-train-labels, after first checking that A2 f179r reproduces byte-identical, then tx_bench.
- no.87 atlas: 0.310 (249/803) vs A1 0.343 (275/803), gain +0.032, 45 fixed / 23 broken, p 0.010.
- no.87 flagged-excluded: 0.303 vs 0.336, 44/22, p 0.009.
- Against the registered gate (gain >= 0.02, p < 0.05, gain > null p95 -0.39), no.87 PASSES.
- Line level: 15/6, line_p 0.078.
- f152r: 25/73, 4/2, p 0.69, FAIL.
- Pooled: 49/25, p 0.007.
- Against A2: 14 fixed / 0 broken.

The verifier's symmetric rule reproduces (239 vs 251, 41/32, p 0.35). But it also gives the machine's own 31-tile X_NEW bag the 5%-error line read, which cancels about 17 owner moves *out of* that bag, so it is not a neutral robustness check. My variant is post hoc on an eval item and cannot be reported as a PASS. What it does show is that the registered null turns on one mis-specified 7-tile pile, and the error ran against the owner.
- **agree**: 6. The gate's A3 permuted-null clause is near-vacuous by construction; a future prereg should use a null that keeps shape information (machine labels with 121 changes on random boxes).
  - Evidence: In the score.py re-run, null err_true is 0.726-0.793 (no.87) and 0.781-0.918 (f152r); null gains have p95 -0.391 and -0.411, max -0.384 and -0.397. Permuting the codes cuts every link between shape and label, so any non-random label set clears this clause by about 0.4, and it decided nothing. The suggested null keeps shape information: the owner's number of changes, placed on random boxes. It is the same shape as the BIR-OWNER random-change control already used on these leaves.
- **partly**: 7. Third-attempt clause: the proposed next step (relabel rules for tiles whose kNN neighbours are owner-moved tiles, applied to the line read) reuses atlas-kNN neighbourhoods and resembles the override arm already measured; it should be argued as a different instrument before being briefed.
  - Evidence: Agree on substance. The next step overwrites a 5% line read using the neighbourhoods of a classifier that reads 0.33. The override arm already broke with both label sets (A1 0/11, A2 0/22), so the step needs an argument that it is a different instrument. Disagree that this run counts as a clean second failure toward retiring owner-label transfer. TXE3-7's FAIL rests partly on the X_NEW-l mis-specification (ruling 5). MQS-CLASSIFY-ROUNDS was, on TXE3-7's own prereg reading, a design in which the owner's tiles could not vote. A pre-registered re-run with his committed q2 merge and a null that keeps shape information corrects an error rather than turning a knob, so rule 3's third-attempt clause should not be applied yet.
- **agree**: 8. The prereg hash c351e72e cited in RESULTS.md and the ROOM claim line does not exist; the prereg as pushed is f70bc534e.
  - Evidence: `git cat-file -t c351e72e`: 'Not a valid object name'. No commit in any ref starts with c351e72. The hash is cited at RESULTS.md line 3 and in the ROOM.md claim line, 05:57, 11 Oct. f70bc534e (05:57:52Z) comes before the outputs (65a3c5742, 06:08:07Z) and the results (af6528f10, 06:10:38Z). This is a citation slip; the order is not affected.
- **agree**: 9. (Outside the claims) The 'reconciled plus the owner's sorted labels 0.042' figure is the NO87-LABELS relabels (a value-blind subagent re-read), not an owner decision; if experiment 1's premise 'your sorting gave the biggest gain' rests on it, it is misattributed.
  - Evidence: TRANSCRIPTION.md line 40 labels 0.042 (34/803) 'reconciled + NO87-LABELS (L)'. PREREG-txeng3-7 line 20 identifies it as a value-blind Sonnet relabel of 42 no.87 tiles and records that the brief misnamed it as the owner's. It goes further: PREREG-txeng3-1 builds on TXE2-SORT X6, in which 'the benchmark truth plays the owner' inside tools/tx_sorter_curve.py. That is a simulated sorter. So the owner-table premise 'your sorting gave the biggest gain' does not rest on any measurement of his real sorting.
- **partly**: Verifier verdict on claim 1: 'overstated' (f152r underpowered; no.87 owner-sorted; one classifier; override shows his labels measurably worse).
  - Evidence: The verdict stands, and the first two reasons hold. The override reason is a unanimity-threshold artifact: identical top-1 at all 14 differing tokens (ruling 1). The verifier missed the main reason: the registered owner arm left out his own q2 ruling, and with it applied no.87 passes the registered gate post hoc (45/23, p 0.010). The verifier's corrected sentence ('your labels did not measurably beat the machine's ... used to overwrite the line read, your labels did worse than the machine's') is therefore itself unsafe to send.
- **agree**: Verifier verdict on claim 2: 'overstated' (only one route measured; the rule's two mechanisms untested; overwriting did harm; 'never asked twice' is a process choice).
  - Evidence: Confirmed against TRANSCRIPTION.md lines 150-152 (ruling 4). Two additions. 'Not as an accuracy step' is not supported even for the measured route, since that route's null flips with one of his own committed rulings (ruling 5). And the harm from overwriting belongs to the override route under either label set (A1 0/11, A2 0/22 vs the line read), not to his labels specifically.

### Final verdict on each claim told to the owner (11 Oct ~07:05 UTC)

- **overstated**: Applied through the family atlas to a letter he never sorted, the owner's labels came out no better than without them (the machine's starting labels).
  - Evidence: The registered numbers re-derive (score.py byte-identical): no.87 0.329 vs 0.343, 41/33, p 0.42; f152r 0.356 vs 0.384, 4/3, p 1.0; gate FAIL on both. Three problems with the claim:
(a) f152r, the only letter never sorted, can show only a large effect (CI -0.057 to +0.085).
(b) no.87 is a letter he sorted on 4 Oct (21 moved, 217 kept; excluded from training).
(c) The registered owner arm scored his X_NEW-l pile as valueless, although his committed 4 Oct answer (q2) and BIR87-ALIGN (o, 6/7, grade C) both make it T19. With only that ruling applied (7 boxes, post hoc), no.87 reads 0.310 vs 0.343, 45 fixed / 23 broken, p 0.010 (line_p 0.078), which passes the registered gate. That is not reportable as a PASS on an eval item, but the null is fragile.
  - Corrected: Carried to other letters by a shape classifier built only from your 438 sorted Birago 1572 tiles, your 4 Oct corrections showed no measurable gain over the machine's starting labels in the pre-registered test (no.87: 41 fixed, 33 broken, p 0.42). That test scored your X_NEW-l pile as always wrong, although on 4 Oct you ruled it the same sign as T19. With only that ruling applied, in a check made after the fact, your labels came out ahead on no.87 (45 fixed, 23 broken). The question stays open until a corrected, pre-registered re-run. f.152r, the one letter you never sorted, is too small to show anything but a large effect.
- **overstated**: Reuse his sorts so he is never asked twice, not as an accuracy step.
  - Evidence: Three gaps:
- 'Never asked twice' is a process choice, not a result of this run.
- 'Not as an accuracy step' rests on one route, owner tiles as the only kNN voters. The two mechanisms TRANSCRIPTION.md lines 150-152 name were not tested: cluster-level sign_sorter_apply.py into labels.json, and the exemplar sheet.
- Even for the measured route, the null flips on no.87 once his own q2 merge is applied (post hoc).
The override arm does show that overwriting a line read with this classifier's votes is harmful under either label set (A1 0/11, A2 0/22).
  - Corrected: Keep your decisions on file so you are never asked about the same tile twice. Whether reusing them improves accuracy is not settled: the one route measured gave a null that turns on one of your own pile rulings, and the two routes the transcription rule names (cluster-level application, exemplar sheet) are untested. Overwriting a line read with this classifier's votes did harm whichever labels it used, so reuse must not mean auto-overwriting readings.
- **overstated**: (First verifier's new claim) In the override arm the owner's labels are measurably worse than the machine's: no.87 A2 override vs A1 override 0 fixed / 11 broken, p 0.001.
  - Evidence: The figure reproduces: 0/11, p 0.001, lines 0/7. But at every one of the 14 tokens where the two override outputs differ, A1 and A2 have the same kNN top-1 code. Only the vote share differs (A1 0.58-0.81, A2 1.00), and A2 is unanimous on 135 boxes against A1's 93. His labels made the same wrong votes unanimous, which the fixed unanimity rule then let through.
  - Corrected: In the override arm, his labels made the classifier unanimous more often on the same wrong codes the machine labels already voted for (11 more overwrites, all wrong). The harm comes from overwriting a 5%-error line read with a classifier that reads 0.33, and it occurs under both label sets.
- **wrong**: (First verifier's new claim) The null is robust to the X_NEW scoring choice (symmetric rescoring 41/32, p 0.35).
  - Evidence: The symmetric figure reproduces (239 vs 251, 41/32, p 0.35). But that rule gives the machine's own 31-tile X_NEW bag the line read, which cancels the owner's moves out of that bag. The scoring choice supported by the prereg's own cited source and by the owner's committed q2 is X_NEW-l = T19, and under it no.87 is 45/23, p 0.010, gain +0.032, which passes the registered gate (post hoc).
  - Corrected: The null is not robust: applying the owner's own committed X_NEW-l = T19 ruling (7 boxes) turns no.87 into 45 fixed / 23 broken (p 0.01 by sign, 0.08 by line), above the registered gate. This is post hoc on an eval item, so it voids confidence in the null without establishing a gain.

### Sentence the parent may give the owner

The pre-registered test found no measurable gain when a shape classifier carried your 4 Oct Birago corrections to other letters, but it is not conclusive: it scored your X_NEW-l pile as always wrong although on 4 Oct you ruled it the same sign as T19, and with only that ruling applied (a check made afterwards, not a pre-registered result) your labels came out ahead of the machine's on no.87 (45 signs fixed, 23 broken), while f.152r, the one letter you never sorted, is too small to show anything but a large effect; so keep your decisions on file so you are never asked twice, do not let this classifier overwrite a line read (it did harm with either set of labels), and treat the accuracy question as open until a corrected re-run.
