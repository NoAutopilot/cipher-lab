# SFZ-NEXT (account-3 orchestrator, 7 Oct 2026 23:3x UTC). default-lane common tail; Opus 5.5 orchestrating, Sonnet passes.
Source: LANE ST-REBUILD handoff in STATUS.md ("Left, runnable"). Folders: ciphers/sforza-italien1584-1447 (pool),
ciphers/sforza-pusterla-1447-f13 (partial, NEAR row), ciphers/sforza-duke-1447-f15 (open). Gallica btv1b100373864.
Read the three NOTES.md and the NEAR row first; run tools/intake_gate_check.py on each target and paste the output.

## SFZ-NEXT (account 2), cap $14, box 120 min. Units and per-unit estimates (Usage 6):
1. Pusterla f.71 (text printed in Osio III no. CCCXCI): line crops (tools/iiif_lines.py, paste the command), two blind
   Sonnet passes + 1 reconciliation, align to Osio's print (tools/interlinear_align.py), add C-grade codes to the Pusterla
   key; held-out G1 re-run. ~$4.
2. Pusterla f.67, same steps if a clear text exists; if not, decode it with the grown key + 200-shuffle control. ~$4.
3. it15 Lombard/Italian 15th-c judge corpus in tools/data/ (era/register-matched per rule 3; report per-fold spread),
   then re-judge the f.13 decode with the grown key. ~$2.
4. Duke (f.15): settle the sign inventory (lookalike_pass + second reader on f.5/f.8 against f.6/f.9 translations),
   try pusterla/g1p.py's anchored learner, G1 gate 0.60 unchanged. ~$4.
Stop before starting a unit that would cross 80% of cap or box. Gates are pre-registered as in the handoff; do not lower them.
Rule 5: Pusterla stays partial unless the judge PASSes with a matched control; update NEAR.md either way; gaps_check.py
before the done line. A PASS on f.13 goes to a separate verifier session (rule 10), not this one.
Report what was found and where it was not found; do not classify novelty.
