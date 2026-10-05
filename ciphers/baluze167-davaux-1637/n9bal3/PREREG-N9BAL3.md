# PREREG N9-BAL3 -- f.110r (c234) gloss anchors + anchored planted control for the N9-BAL2 test (5 Oct 2026, written 06:0x UTC, pushed before any f.110r pass is read or any score computed)

Worker N9-BAL3 (account 2, for LANE-NEAR9), brief `.claude/briefs/runs/2026-10-05-ytbiz-near9-wave3.md` job N9-BAL3. PREREG-N8BAL and
PREREG-N9BAL2 stay as registered. This file adds anchors to the N9-BAL2 procedure; nothing else in it changes.

**Step 1 -- f.110r transcription.** Baluze 168 c234 (f.110r, court hand, ~22 glossed groups). Crops by `tools/iiif_lines.py` (command pasted
in NOTES). Two blind Sonnet passes (A, B), one call each over the leaf's crops, convention identical to N9-BAL2's (numerals as digits +
mark suffix; every non-numeral sign `s:` + nearest Latin letter form, capital-like forms kept; `?` unreadable), each also writing the
interlinear words above each group verbatim. No key values and no f.247 tokens shown to either pass. One reconciliation by this worker
against the crops (not blind to the gloss, which is on the leaf anyway), logged per position.

**Step 2 -- anchors at C.** A sign token of the reconciled f.110r transcription gets a C value only where the gloss fixes it unambiguously:
(a) a glossed group whose cipher tokens are all `s:` signs and whose count equals the gloss word's letter count (1:1, read in order); or
(b) a token aligned by `tools/interlinear_align.py align` (same flags as N9-BAL2: `--code-prefix @ --code-chunk 3 --seg-bonus 0 --len-prior 0.5`)
over the f.110r (gloss, group) pairs to the same single letter at >= 2 occurrences, and to nothing else. Two-way conflicts -> no C.
Numerals and multi-letter chunks are reported but are NOT used as anchors (the f.247 hand's numerals are a separate question).
Transfer to f.247: an anchor is used only for a label string that occurs in the N9-BAL2 reconciled f.247 transcription
(`passes/reconciled_b168f247v.tsv`). This transfer assumes the two hands share letter-sign forms (by eye only, N9-BAL); the control
below does NOT test that assumption, it tests only whether k correct anchors give the procedure power. k = number of transferable anchors.

**Step 3 -- anchored procedure (the only change to N9-BAL2).** Each anchored token's value is (i) passed to the fit as
`interlinear_align.py --prior` (seeds the first EM iteration, 2 counts each), and (ii) fixed in the decode key (overrides the fit's value
for that token, and anchored tokens absent from run 2 enter the key too). Nulls: null 1 shuffles all key values (anchored included) within
class among the keyed tokens; null 2 shuffles F1's letters. Statistic, candidate passages, >= 10 compared letters, 1000/200 draws: as N9-BAL2.

**Step 4 -- anchored planted control (the gate).** `n9bal3/planted_control_anch.py`: N9-BAL2's planted control (same design, seeds 100-119,
err 0.28 measured err_2reader), plus k anchors = the TRUE values of k planted `s:` tokens drawn at random (per seed) among the `s:` tokens
occurring in the planted run 2 (all of them if fewer than k). Also reported, not gating: the same at k = 0, 5, 10, 15 to show the power curve.
**Gate (fixed now): the control passes iff >= 10 of 20 seeds PASS their own nulls at the real k and err 0.28.** If k = 0 (no transferable
anchor), the control is not run at k and the job is a non-test.
**Step 5 -- only if the control passes:** re-score c511 run 2 vs F2 and the F1 hold-out (reconciled, A, B) under the N9-BAL2 statistic and
nulls with the anchors; PASS iff T > both p99 and >= 10 letters compared, on the reconciled transcription; no other knob changes.
**If the control fails:** logged as a non-test; this is the third failed instrument on the f.247 known-answer hypothesis (N8-BAL, N9-BAL2,
N9-BAL3), so the F2-fit/F1-hold-out alignment instrument is marked [retired] for that hypothesis (rule 3 third-attempt clause), and the job stops.
