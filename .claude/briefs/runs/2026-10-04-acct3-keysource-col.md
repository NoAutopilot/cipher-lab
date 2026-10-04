# KEYSOURCE-COL (account 3 worker) -- 4 Oct 2026 19:4x UTC (account-3 orchestrator)
Owner's question (4 Oct): "Do we denote when we make the key, vs finding it or using a plaintext already known?" We record it (CLAUDE.md
rule 10: AUDIT.md + status.json `key` = ours/period/published, `text` = known/...), but the progress block's K column only says "key in hand",
and 67 of 114 status.json results have no `key` field. Make it visible.
1. PROGRESS.tsv: add two columns after K: `ksrc` (o = ours: recovered by us -- cryptanalysis, plain-copy alignment, identifying the codebook;
   p = period: rebuilt from a decipherment/key sheet of the time; b = published: someone else's modern key; o+p mixes allowed as "p+o";
   ? = not recorded) and `txt` (k = plaintext already in print/known; n = not located in print after a logged search (N3+); ? = unrecorded).
   Fill every row FROM DISK ONLY: the target's AUDIT.md key-source/class lines first, then status.json, then NOTES; put the file in `source`.
   Never guess: unrecorded stays '?', and list those rows in your report.
2. tools/progress_block.py: render the K cell as the ksrc letter when set (o/p/b/P for p+o... pick a clear one-letter scheme and document it),
   and add a T column; update the legend line ("K key: o ours, p period, b published; T text: k known in print, n not found in print").
   Keep --check working; offline test in tools/tests/.
3. status.json: fill missing `key`/`text` fields only where AUDIT.md states them (fetch+rebase first; keep others' edits).
4. Paste the new block into your ROOM done line count summary (how many o / p / b / ?). Commit by explicit path; file_shrink_guard.
Disk only. Model Opus 5.5. Cap USD 3, box 30 min. ROOM claim/done via tools/room.py.
