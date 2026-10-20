# Research director, wave 31 (20 Oct 2026, 03:1x UTC by date -u): Sherwood grid heading-gap scan

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, `tools/experiment_log.py --check`, `python3 tools/dup_check.py sherwood-cossit-1781` pasted). Solver job: report
what was found and where it was not found; no novelty class (rule 10). AUDIT.md is the verifier's; do not edit it. Done line addressed
for the account-4 parent.

## JOB SHERWOOD-GRID (account 2; Opus 5.5; cap USD 5; box 45 minutes; hosts: archive.org (11280377bsb page images only for the pages step 2 names, at most 12, one at a time, 1.5 s apart); Price: vision calls: 3 x USD 1.2 + 0 reconciliation = 3.6)

ciphers/sherwood-cossit-1781 (partial, N3/D2, H/C/S 159/216 = 73.6% after SHERWOOD-CELLS). SHERWOOD-CELLS (NOTES.md "## Cell check")
found a grid fault: on p.165 col 1 book/entick_lines.tsv counts the blank space above a centred section heading ("H.") as a line, so the
cited cell 165-13 was off by one. The same fault can sit under any other cited cell in a column with a centred heading, including cells
graded S today. Price note: the last two Opus image jobs here ran about USD 1.2 per page-level vision call; stop before a call that
would cross 80% of the cap.
1. Script first (no vision): list every column of entick_lines.tsv that (a) holds a centred section heading (a single capital letter
   with a period, or the grid's own heading flag) and (b) has blank grid rows directly above it; cross it with every cell the reading
   cites (reading.tsv). Paste the count: columns flagged, cited cells below a flagged heading in the same column.
2. For the flagged cited cells only, cut line-band crops of that column around the heading and the cited line (`tools/iiif_lines.py
   --image ... --centres ...`, paste the command; never a whole page to a reader) and read blind which printed line the cell falls on,
   batching all crops of one page into one call. Decide the counting rule once from the image evidence (heading counts as a line or not)
   and state it with the anchors it rests on (the 153 c2 case and p.165 c1).
3. Fix the grid rule in decode_entick.py/book tools (not hand edits to the TSV), regenerate reading.tsv/reading.txt and the controls
   (`decode_entick.py --controls`), `--check` passing, judge output pasted (rule 7). Grade counts before/after; every S row whose word
   changed is named and drops to M unless it re-earns S by the existing rules (rule 4a: depth is lowered on any revision).
4. NOTES.md "## Heading-gap scan (SHERWOOD-GRID, 20 Oct 2026)" with the six research-director questions; gaps_check passes; ROOM flag
   for a verifier if any counted word changed.
Report: columns flagged, cells changed, grade counts before/after, judge, five lines.
