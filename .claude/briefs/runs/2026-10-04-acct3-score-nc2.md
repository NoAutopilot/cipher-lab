# SCORE-NC2 (account 3 worker) -- 4 Oct 2026 15:0x UTC (account-3 orchestrator; owner approved)
Read research/MARY-STUART-METHOD-2026-10-04.md (section 1 row 16, section 2 "Score with sum Nc^2") first. Lasry et al. 2023 App. A score
S = sum_g N_g log F_g / sum_c N_c^2 (n-gram log-likelihood over the decrypt divided by the sum of squared letter counts), which
penalises degenerate keys that pile many symbols on one letter. RUN5-C1161RA (clair1161-avis-flandre-1688, two/reanneal.py,
tx/PREREG_reanneal.md) failed its planted control 0/3 because "word-cover stage drove all free signs to i".
1. Tool (Usage 8): add a `norm` option (none | nc2) to the homophonic anneal scorer used by tools/families/homophonic.py (and by
   reanneal.py if it calls its own scorer -- if so, add the option to the shared scorer and point reanneal.py at it, no private copy);
   --help text, offline test in tools/tests/ showing nc2 ranks a degenerate all-one-letter key below the true key on a synthetic case
   where plain log-likelihood ranks it above. SYSTEM.md row if a new file.
2. PREREG addendum to clair1161 (pushed before any run): identical C1161RA design (C/S held fixed, same M signs free, same seeds, same
   planted controls a/p/d), only change norm=nc2 -- one knob, a different objective, so a new instrument (rule 3 third-attempt clause:
   say why). Gate: planted control recovers >= 2 of 3; only then run the target arm (10 seeds) and report per M sign the consensus value
   and seed agreement. Headroom check first (rule 3): report the control's blind baseline.
3. Nothing enters key.tsv in this job; proposals only, graded M, with a ROOM line. Write results in clair1161 NOTES.md + HYPOTHESES.md.
Disk only, no network, no subagents. Model Opus 5.5. Cap USD 3.5, box 60 min. ROOM claim/done via tools/room.py. Do not touch other targets.
