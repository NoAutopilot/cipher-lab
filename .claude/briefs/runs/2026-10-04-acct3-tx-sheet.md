# TX-SHEET (account 3 worker) -- 4 Oct 2026 14:2x UTC (account-3 orchestrator; owner approved 4 Oct, 7:2x am PDT)
Research #4 of research/TRANSCRIPTION-PRACTICE-2026-10-04.md: a per-hand exemplar sheet (the palaeographer's alphabet) for line-read
passes. The other machine additions are spent (TRANSCRIPTION.md: TX-VIEWS FAIL, TX-AGREEAUDIT NON-TEST, TX-ALTS not adopted); this is
the last untried one aimed at the readers' shared blind spots. Read TRANSCRIPTION.md and research note #4 first.
1. Add an option to tools/glyph_atlas.py (Usage 8: option + --help + offline test, SYSTEM.md row): `atlas --from-truth TOKENS.tsv --per 6
   --spread --exclude-leaf LEAF ...` -- 4-6 tiles per sign from securely read positions, chosen for the widest shape spread (allographs,
   cramped and line-end forms), one sheet image per sign group sized for one subagent call.
2. Source positions: Birago 1572 key family, EXCLUDING every no.87 leaf (f.178r, f.178v, f.179r -- the eval item; building from the no.87
   clerk sheet voids the test). Prefer C/H grades; else S positions where two independent instruments agree; state the rule and the
   per-sign counts in the PREREG before any pass. Signs with fewer than 2 secure exemplars keep the current single canonical shape.
3. PREREG (pushed before any pass): one blind Sonnet line-read pass of no.87 with the sheet replacing the canonical sign sheet, same crops,
   prompt and model as pass A otherwise. Gate: err_true below pass A's 0.069 on the eval item AND paired fixed > broken vs pass A
   (`tools/tx_bench.py --paired`), with d<-T98 and s<-T50 down in the top-confusions list. Tune (sheet size, spread) only on the dev item
   dint-f128-print, never on no.87. Report cost per 100 signs (TRANSCRIPTION.md target 8).
4. Write the result into TRANSCRIPTION.md's job table (new row TX-SHEET, "Today" column) and benchmark-tx/outputs; LESSONS.md line only
   if adopted. Price per pass, not per page (Usage 6): state the unit count and per-call estimate before the first subagent call; line
   crops only (tools/iiif_lines.py outputs already on disk), never a full page to a subagent.
Model Opus 5.5 (worker), Sonnet 5 for the read pass. Cap USD 8, box 75 min (stop before a step that would cross 80% of either). ROOM
claim/done via tools/room.py. Do not change key files or readings of any target; do not touch other targets.
