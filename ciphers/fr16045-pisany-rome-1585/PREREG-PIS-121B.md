# PREREG-PIS-121B (15 Oct 2026, 14:3x UTC by date -u; addendum to PREREG-PIS-121.md, pushed before any gloss pass is read and before any score)
Job: PIS-121B, LANE DEFAULT-A2-1410-15 (account 2), brief .claude/briefs/runs/2026-10-15-ytbiz-default-1410-jobs.md "PIS-121B".
Question (unchanged from PREREG-PIS-121.md): does Tomokiyo's 1585 table (key.tsv, 67 labels) decode the cipher of fr.16045 f.121 (canvas 252)
into text that agrees with the clerk's left-margin gloss better than a permuted table does?

## What changes, and only this
- The gloss input. PIS-121's gloss was one blind pass reading all 23 line crops in one call (every row with illegible letters). Here:
  two independent blind Sonnet passes (P1, P2) on the same 23 gloss line crops, each pass reading **one crop per Read call and writing that
  line's text before opening the next**; then one blind Sonnet reconciliation call (RG) that sees P1, P2 and the crops, settles each
  disagreement from the crop, and keeps '.' where neither reading is supported. No pass or reconciler sees the cipher, the key, the
  decode, the PIS-121 gloss, or any repository file. The worker does not edit any gloss text before scoring (V-BRANDT rule).
- Crops: the same three margin regions as PIS-121 (`--region 400,360,900,960` glA, `400,2420,900,880` glB, `400,3760,900,1060` glC,
  `--distance 70`) from the same image (openapi.bnf.fr IIIF v3 btv1b9060906j f252 full/max); if the regenerated line count differs from
  7 + 7 + 9 the crops are used as cut and the count is reported.

## What does not change
- `pis121b/score.py` is a byte-identical copy of `pis121/score.py` (checked with `cmp`, pasted in NOTES), run in a folder holding
  byte-identical copies of `pis121/passA.tsv`, `passB.tsv`, `rec/ciphertext_draft.tsv`, `rec/choices.tsv`; only `gloss_pass.tsv` differs
  (= RG). Same decode, same Smith-Waterman (+2/-1/-2), same fold, same permuted-table null (seeds 0-999), same power check, same gate.
- **PASS** if S_R (reconciled cipher draft vs RG) > the null's p99 (1,000 draws). **FAIL** otherwise. Power check as registered; a power
  FAIL makes a target FAIL a NON-TEST.

## Reported, not gated (fixed now)
- Gloss read error: letter-level two-reader disagreement of P1 vs P2 (difflib, letters only, folded as score.py), per block and overall;
  and RG vs the PIS-121 gloss, the same measure. This is the axis PIS-121's power control could not vary on.
- S_R with P1 alone and with P2 alone as the gloss (same scorer copied into two more folders, gloss file swapped only).

## What each result licenses (said in advance)
- PASS: "the 1585 table agrees with the f.121 gloss beyond a permuted table (p < 0.01)" in NOTES/HYPOTHESES; no table value changes, every
  decoded token stays M (no per-sign gate registered).
- FAIL with power PASS and P1/P2 disagreement <= 0.20: a control-backed miss at this cipher transcription (the gloss read is no longer the
  open cause; the cipher draft, 22/27 lines rule-reconciled, or the gloss paraphrasing the cipher remain).
- FAIL with P1/P2 disagreement > 0.20: still a miss of unknown cause; the gloss read is not fixed by machine passes. This is the second
  attempt at the same margin-block approach on the same page; by rule 3's third-attempt clause the next step is a person's read of the
  gloss or a different instrument (the interlinear name-gloss pairs), not a third machine pass.
- Under no outcome does this job change key.tsv, write a reading file, or grade any token above M.
