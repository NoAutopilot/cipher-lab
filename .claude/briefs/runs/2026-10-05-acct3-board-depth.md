# BOARD-DEPTH (account 3 worker) -- 5 Oct 2026 (account-3 orchestrator). Owner approved 5 Oct ("I'd agree").
The board's headline "recovered-passage documents" (tools/build_dashboard.py counted()) checks N3+ and two audits but not depth; CLAUDE.md
rule 4a (4 Oct 2026) says a unique solve is N3+ AND D2+. On 5 Oct the count is 29, of which 9 are D1 (status.json depth). Fix:
1. counted(): require depth D2+ (status.json `depth`, e.g. "D2"/"D3"/"D4"); rows with no depth field are held out and listed (not counted)
   until a verifier sets it. Add a fifth, separate figure "fragments read" = the same rule at D1, shown beside the headline, never summed.
   Headline wording follows rule 4a's outward words. Update the TLDR count line in .claude/briefs/parent.md if it names the old four counts.
2. Offline test in tools/tests/ (a D1 row is not counted, a D2 row is, a missing depth is held out). Rebuild dashboard.html + docs/index.html.
   Expected on 5 Oct: 20 counted / 9 fragments (report the actual numbers and any row held out for missing depth).
3. SYSTEM.md mention if the tool's contract changed (tools/system_map_check.py); file_shrink_guard; ROOM done line with the new counts.
Model Opus 5.5. Cap USD 2, box 25 min. ROOM claim/done via tools/room.py.
