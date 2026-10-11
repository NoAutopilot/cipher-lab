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
