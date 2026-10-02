# PAGET-KEY (2 Oct 2026, written by account 3; runs on account 2). Owner: keep everything moving.

Model: Fable if it answers, else Opus 5.5. Cap USD 5, box 50 min.
Target: ciphers/clairambault1225-paget-1714. NEXT-PAG found the period decipherment written above 501/505 cipher tokens;
NEXT2-PAG built decode.json: C 71, M 47, I 7, U 380 of 505 (firm 71).
1. `python3 tools/room.py --start`; claim. Run the Premise check of .claude/briefs/check-solved.md first (Sonnet-level
   effort, ~USD 2): especially (b) both solver repos' working files and (d) English and French documentary editions of
   Paget's 1714 correspondence. Write "## Premise check (PAGET-KEY, 2 Oct 2026)". If it finds a prior decipherment or
   print of these letters, stop there and say so (calibration/found-solved). Gate must exit 0 before step 2.
2. Turn the period glosses into key entries: `tools/interlinear_align.py` on the gloss-under-run pairs (NEXT-PAG's
   options), per-letter held-out control first (rule 3; the Szembek per-unit lesson: a letter whose own control ties is
   held, not merged). Add entries to key.tsv at grade H where the gloss is the period's own decipherment of that very
   group, C where inferred across letters; regenerate with `tools/decode_key.py ... --check`.
3. Update the finish-or-blocker sections and the Paget row of PROGRESS.tsv from the files; gaps_check; commit; done line
   with the new firm count and the control numbers. Rule 10 wording; do not classify novelty.
