# LANE-NEAR9 wave 3 (5 Oct 2026, written 06:0x UTC by LANE-NEAR9, account 2 / ytbiz, session_011SW24uoRbdvoyBAWiy9m98)

Common rules, do-not-touch list, model and pricing rules: exactly as `.claude/briefs/runs/2026-10-05-ytbiz-near9-wave2.md` header (which points
to wave 1's). Read only the NOTES sections named. This is the lane's last wave: stop at the cap, no follow-ups.

## N9-COSVW -- VERIFIER: costabili-modena-1491, W = t at C (cap USD 3.5; box 40 min)
You are a verifier, not the solver (N9-COS2, 0c150c16, did it). Claim under audit: "W (dash + open loop, own label in align/labels.tsv) = t at C
(A 3/5, B 3/4, 3 groups each); A 0.614 / B 0.521 vs p95 0.260/0.233" (NOTES section N9-COS2, PREREG addendum d2fd89bd). Steps: (1) re-run the
committed scoring and confirm the numbers; (2) check the 12 mechanical z/o -> W relabels against the crops (one DECODE browser login only if the
crops are not on disk; images never committed): is each truly W? (3) list every W group with its gloss chunk; C needs the gloss to fix t
unambiguously on >= 2 independent groups; (4) check the p1_u03/p1_u18 re-cut did not move any other sign's value. Write "## Verification of W = t
at C (N9-COSVW, 5 Oct 2026)" in AUDIT.md: CONFIRMED or LOWERED with reasons; carry a lowering into align/key_n9cos2.tsv and NOTES gaps.

## N9-MANT2 -- sachsstaatsarchiv-manteuffel-1712: eye-screen frames 0504-0578 for a copy of the f.410 P.S. and other cipher (cap USD 4.5; box 50 min)
NOTES Verdict line (N9-MANT): frames 0504-0508 (enclosures of no. 96) first, then the other uninventoried frames of 0509-0578. Low-resolution
contact sheets from the image source in the folder's manifest (good-citizen rule, one request at a time, <= 80 requests), one Sonnet call per sheet
of ~12 frames asking only: blank / clear text / cipher (numeric groups) / glossed cipher; then native fetch only of frames classed cipher or glossed
cipher, and your own eye on whether any carries f.410's P.S. (compare against the folder's f.410 transcription by group n-grams after a quick
group read of the candidate lines, not a full transcription). Output: inventory TSV (frame, class, note), update the image-check gap counts; price
any transcription found. Do not touch leaf 0501's decision.

## N9-BAL3 -- baluze167-davaux-1637: f.110r (c234) gloss calibration + anchored planted control (cap USD 5; box 60 min)
NOTES Verdict line (N9-BAL2: NON-TEST, planted control 0/20; next f.110r gloss anchors). PREREG first (pushed before reading): use the f.110r glossed
letter (court hand, ~22 groups, n9bal/glossed_candidates.tsv) to fix letter-sign values at C where the gloss is unambiguous; then the anchored planted
control: does the f.247v c511 procedure, seeded with those anchors, recover a planted synthetic at the measured err_2reader 0.28 (gate fixed in the
prereg)? Only if the control passes, re-score c511 run 2 vs F2 and the F1 hold-out under the N9-BAL2 statistic and nulls (no knob change besides the
anchors; say so). Crops via `tools/iiif_lines.py` (pasted), 2 blind Sonnet passes + 1 reconcile on f.110r (3 units). If the control fails, log it as
a non-test and stop (rule 3 third-attempt clause: name the instrument [retired] for this hypothesis if it is the third failure). Gaps refresh.

```
costabili-modena-1491: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
sachsstaatsarchiv-manteuffel-1712: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
baluze167-davaux-1637: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
```
