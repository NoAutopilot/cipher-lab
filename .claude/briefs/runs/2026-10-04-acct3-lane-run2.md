# LANE-RUN2 (account 1) -- 4 Oct 2026 02:2x UTC (account-3 orchestrator)

Follows LANE-RUN1 (STATUS.md "LANE RUN1 handoff"). Operating rules exactly as `.claude/briefs/runs/2026-10-04-acct3-lane-near3-run1.md`
paragraph 1 (off-limits list included; account 4 is out of usage). DECODE-derived images and sorter pages are NEVER committed (build.sh +
manifest only); a sorter page for the owner goes to account 3 to publish (ROOM line), and is added to his desk board.

Jobs, in order:
1. fr16142-noailles-constantinople-1571, the known-plaintext pair: c510-516 (7 July 1574 cipher, ~9,750 signs) vs Dupuy 521 ff.221R-226R
   (clear). Two blind passes of c510-516 under TRANSCRIPTION.md (crops with tools/iiif_lines.py --follow-slope, pasted), then key recovery
   by alignment (tools/interlinear_align.py, and tools/gibbs_align.py as the second instrument) against the Dupuy text; pre-register a
   held-out gate (key from c510-513 reads c514-516 vs shuffled-text and shuffled-key nulls) before scoring. If the reader split is >10%,
   the next pass is a sorter sheet (account 3 publishes). Size it per pass (Usage 6); split across workers by leaf.
2. es132-vargas-mexia-1578: f.89r-91r, f.119v upper, f.120r under Cp.30 (letters outside cabinet-noir's list), same pre-registered gates
   as RUN1-ES132 (Teulet where printed; key-shuffle and wrong-paragraph nulls).
3. fr16144-savary-lancosme-1588: look for the 1587 original in BnF fr.17020 ff.372-382 (one survey worker).
4. Backlog: NEXT-STEPS.tsv `runnable` rows not claimed by LANE-NEAR3 (cost band S then M), one worker each at the row's named step.
