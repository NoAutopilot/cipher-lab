LANE R6 CM -- fr2933-salviati-1525: the code+mark (cm) test at the real pooled N, control first (Opus, cap $10, box 60 minutes; disk only).
Common: 2026-09-25-lane-r6-common.md. Intake gate: pasted into your spawn prompt (must be exit 0).
Read NOTES.md "Code+mark control curve (LANE R4 P)", "Crib loop on code+mark at N=720 (solvEX2)" and leafnotes/*.md. The pooled transcription is
ciphertext_f54r, f54v, f55r, f55v, f56r, f56v, f57r, f57v .tsv (all eight leaves; grades AB / AC / BC / settled / B-split mark provenance).
Job, in order, stop at the first gate that fails:
1. Pool: extend control/codemark_curve.py (an option, e.g. --leaves all; keep f54r+f54v the default so P's rows reproduce) to read all eight
   leaves; report N sign tokens, base codes, code+mark types, share with marks, plain boxes, per leaf and pooled. Exclude f57r line 17's
   marginal note and any leaf-end plain postscript already coded `_`.
2. Control first at the real N (rule 3; match the design, not only N and K): `codemark_curve.py control cm <N> <seed>` for 3 seeds with the
   pooled leaves' own row pattern and type frequencies. Gate: the blind cm control must read >= 80 percent token accuracy on at least 2 of 3
   seeds (P's curve: 88.9-94.0 at 2,800). If it does not, report both numbers and stop: cm stays untested, not negative.
3. Target: `codemark_curve.py target cm <seed>` for 3 seeds. Report per-seed score per symbol vs the control's solve and its true plaintext,
   and cross-seed agreement (P used both for vi). A reading exists only if the three seeds agree on most symbols AND the text reads as Italian.
4. Only if the blind control reads above 45 percent AND the target does not already read: run the solvEX2 crib loop on top (its code is in
   control/solvex2), control first, and report the gain over blind with the control's headroom (CLAUDE.md rule 3's gain-gate paragraph).
5. If any decode reads as Italian: write it to reading_cm.txt with a regeneration script and --check, spec specs/fr2933-salviati-1525.json
   if missing (it16 judge, which has a real corpus), paste `tools/judge_plaintext.py specs/fr2933-salviati-1525.json --file reading_cm.txt`,
   grade tokens S (cryptanalytic with a control) or M, and ROOM "for LANE V6: reading ready" -- a fresh-instance re-derivation is the
   orchestrator's next job, not yours. If nothing reads: the negative with its control numbers, conditional on the transcription's agreement.
NOTES.md: section "## Code+mark at the pooled N (25 Sept 2026, LANE R6 CM)" (you are the only writer of NOTES.md now). Report what was found
and where it was not found; do not classify novelty. ROOM done: "for LANE R6: salviati cm target <x> vs control <c> at N=<n>".
