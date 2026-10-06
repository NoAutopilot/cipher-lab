# PREREG-R9NEVF -- L05 glyph-atlas test re-registered without class 0 (account 1, 6 Oct 2026, written 06:1x UTC before any segmentation or classification)

Brief: `.claude/briefs/runs/2026-10-06-account1-run9-jobs.md` job R9-NEVF (LANE LANE-RUN9-account-1), cap $4.5, box 06:07-07:02 UTC.
Previous registration: NOTES.md "A1B-FILS-L05 pre-registration" (3 Oct 2026), non-test at its class gate (class 0 had 0 H exemplars).
This registration is the same test with the class-0 questions removed. Nothing below has been run yet.

**Questions (L05 run `43181987394579655416`, committed digits; pos -> token):**
- pos 5 (`1` of token 19), reader's alternative: a stroke of 9 -> alternative class 9.
- pos 13 (`7` of token 79), reader's note "mark above 7" -> alternative class: the nearest non-7 digit class in the pool (strictest choice; the 57 reading would make it 5).
- pos 17 (`5` of token 54), alternative 6.
- pos 20 (`6` of token 16), alternative 8.
Dropped from this registration (stay M whatever happens): pos 4 and 7 (alternative is "01", needs class 0: tokens 18, 87), pos 15-16 (one fused box in A1B-FILS-L05: token 65).

**Instrument.** `tools/glyph_atlas.py` as A1B-FILS-L05: `segment --page f43=images/src_ark_12148_btv1b9058240c_f43_3950_3560_3150_1800.jpg --rel 0.7 --debug`,
then `cluster` (defaults), then `classify --page f43 --topk 3 --knn 5 --holdout <L05 box ids>` with a labels.json whose cluster map is all '_'
and whose `override` labels individual boxes. If the segmentation does not reproduce A1B-FILS-L05's counts (345 signs, 10 lines) that is
reported; the box mapping below is done on this run's own boxes either way.

**Rules (fixed now):**
1. Atlas: only single-digit boxes inside tokens graded H in `f35r_ciphertext.tsv`, outside L05, are labelled (by eye on the debug overlay,
   one digit per box). A box holding two digits, a partial digit, or a digit fused with script is left '_'. All L05 boxes never vote.
2. Gate (unchanged from A1B-FILS-L05 except class 0 removed): leave-one-out over all labelled digit boxes (each classified with itself
   excluded, the tool's own self-exclusion, L05 held out) -- share whose kNN code equals its label >= 0.90; and classes 1, 5, 6, 7, 8, 9
   (the digits named by the four questions and their alternatives) each >= 3 exemplars. Below either: non-test, no grade moves.
   Added, stricter only (CLAUDE.md rule 3, unbalanced held-out gate): per-class LOO accuracy is reported, and a settle to D also needs
   class D's own LOO accuracy >= 0.67 (with >= 3 exemplars). Also reported, not gating: a shuffled-label control (labels permuted among the
   labelled boxes, 200 permutations, seed 20261006) LOO share mean and p95, so the real LOO share is read against chance.
3. Settling statistic per glyph in question: settles to digit D only if (a) the kNN code k1 is D, (b) vote share s1 >= 0.60, and
   (c) margin: nearest distance of the alternative class / nearest distance of D >= 1.10 (alternative absent from the 40-box pool = met).
   A glyph fused into one box with a neighbour or with script is unsettled.
4. A token moves M -> H only if its glyph in question settles to the committed digit. A glyph that settles to a different digit is reported
   and the token stays M; no digit is changed by this run. Key coverage never chooses. A FAIL is logged, not re-tuned (brief).
5. Rule 7: `decode_f35.py --check` after any grade change; NOTES.md counts, AUDIT.md safe sentence and the SO prompt are checked for
   counts to propagate.
