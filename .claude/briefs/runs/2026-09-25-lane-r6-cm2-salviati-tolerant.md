LANE R6 CM2 -- fr2933-salviati-1525: an error-tolerant code+mark model, noise controls first (Fable, cap $15, box 75 minutes; disk only).
Common: 2026-09-25-lane-r6-common.md. NEAR.md row "fr2933-salviati-1525", next step (1). Use tools/family_run.py's control-first discipline
(parent 7c 18:18): a family runs on the target only after its matched control has read above the gate; write both numbers to HYPOTHESES.md.
Intake gate (live, 25 Sept 18:52 UTC): "fr2933-salviati-1525: open (line 1) -- edition/page or full-text-search citation found within 6 lines" (exit 0).
State (NOTES.md "Code+mark at the pooled N (LANE R6 CM)"): N=2,820 signs, 223 code+mark types; the cm control reads 94% clean but 27-43% at 10%
type noise and 24-27% at 20%; the target scores between those two noise levels. Pass agreement per leaf was 77-86% before settling.
Job: (1) design a noise-tolerant variant -- e.g. merge code+mark types into base code + a small mark class set, or a solver whose symbol model
allows a confusion matrix estimated from the leaves' own pass A/B disagreement tables (recon_box_*/disagreements.tsv are your measured
confusions); (2) build it as an option of control/codemark_curve.py or a new tools/ solver with --help and an offline test; (3) run it on the
10% and 20% noise controls (3 seeds each). Gate: above 60% token accuracy on the 10% control on at least 2 of 3 seeds. Fails -> report both
numbers and stop (the model is still untested, not negative). Passes -> (4) run the target, 3 seeds; report score vs control, cross-seed
agreement, and any Italian. A decode that reads goes to reading_cm2.txt with a regeneration script and --check, it16 judge output pasted, tokens
graded S/M, and ROOM "for LANE R6: salviati reading candidate" (the orchestrator orders the re-derivation). NOTES.md section
"## CM2: error-tolerant code+mark (25 Sept 2026, LANE R6)". ROOM done: "for LANE R6: salviati cm2 control10 <x>% control20 <y>% target <t>".
Report what was found and where it was not found; do not classify novelty.
