LANE R7 CM3 -- fr2933-salviati-1525: a control with the transcription's MEASURED error classes, and a word-aware model (Fable, cap $10, box 75 minutes; disk only, no hosts, no subagents).
Common: 2026-09-25-lane-r7-common.md. NEAR.md row "fr2933-salviati-1525". Control first, always (rule 3; tools/family_run.py discipline); both numbers to HYPOTHESES.md.
Intake gate (live, 25 Sept 21:22 UTC): "fr2933-salviati-1525: open (line 1) -- edition/page or full-text-search citation found within 6 lines" (exit 0).
State: NOTES.md sections "Code+mark at the pooled N (LANE R6 CM)", "CM2" and "Atlas re-pass on f.55v and f.57v (LANE R7)"; leafnotes/siblings.md (no pool).
N=2,820 signs, 223 code+mark types (atlas re-pass: 204/198 at most). CM's CM_NOISE substitutes types at the target's frequencies, but CM2 measured
that the passes' real disagreements are 70.9% sign<->plain (a sign dropped to plain or a plain box read as a sign: insertions/deletions in the
sign stream), 20.4% base-code confusions (#/+, g/y, bh/g, #/Z, f/y, bh/phi) and 0% marks-only. CM2 also showed the trigram objective's optimum
is no longer the true key at 10% substitution noise: the per-letter discrimination of the language model, not the search, is the limit.
Job:
(1) Error rate: estimate the post-settlement residual rate per class from what is on disk (e.g. pass C vs the A/B-settled value on f55v and f57v;
    recon_box_*/settled.tsv), and state it with its basis. If it cannot be measured, bracket it at 3% and 7% total.
(2) Control generator: extend control/codemark_curve.py (an env or flag, with --help text and an offline test) so CM_NOISE can apply the measured
    mix -- deletions of signs, insertions of spurious signs, and the named base-code confusions -- instead of type substitution.
(3) Model: add a word-aware or 4-gram scoring option to tools/homophonic_anneal.py (its it16 corpus; keep the default unchanged, test offline), and/or the
    CM2 bounded-loss option on top of it. Keep it to one design you can justify in two sentences.
(4) Control: 3 seeds at the measured rate (or both bracket rates), 24 restarts. Gate: >= 60% token accuracy on 2 of 3 seeds. Fails -> report both numbers
    and stop (still untested, not negative). Passes -> (5) run the target, 3 seeds; report score vs the control's, cross-seed agreement, any Italian.
    A decode that reads goes to reading_cm3.txt with a regeneration script, it16 judge output pasted, tokens graded S/M, and ROOM "for LANE R7:
    salviati reading candidate" (the orchestrator orders the re-derivation).
Write "## CM3: measured-error control (25 Sept 2026, LANE R7)" to NOTES.md; rows to HYPOTHESES.md and control_curve.tsv.
ROOM done: "done: for LANE R7: salviati cm3 measured error <e>% -> control <x>/<y>/<z>% (gate 60 on 2/3) target <t or not run>".
Report what was found and where it was not found; do not classify novelty.
