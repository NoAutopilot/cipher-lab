# TX-HUMAN-ASKS (written by account 3, 5 Oct 2026, for account 1). Opus 5.5. Cap $5, box 45 min. Public repo only.

Owner, 5 Oct 2026: "For things with bad transcripts happy to pull down better images, review symbols manually, etc."
Goal: a ranked list of owner tasks where a person's eye or a better image is the cheapest way to move a target.

1. Script first: from ciphers/*/NOTES.md, status.json, PROGRESS.tsv, ZOOM-ASKS.tsv and every focus.tsv / sorter page
   under ciphers/*/ (tools/sign_sorter.py outputs), list open/partial targets whose blocker is the transcription:
   measured reader disagreement or error > 5% (TRANSCRIPTION.md), unsettled sign inventory, look-alike splits left by
   tools/lookalike_pass.py, "illegible", "two-way", "image too small". Skip Armstrong, Debosnys and Birago sorter
   work already on the owner's board, and targets whose text is already printed (PROGRESS T=k) unless a counted row
   depends on it.
2. For each kept target pick ONE owner task type: (a) zoom screenshots (viewer link at the page, first/last words,
   est. shots), (b) sign-sorter session (the sorter page link, number of tiles, est. minutes), (c) a short "check
   these first" list (n signs with crop links, what to decide for each), (d) a single symbol question (two crops, A
   or B). Estimate minutes; keep tasks <= 20 min each.
3. Rank by: closeness to a counted result (PROGRESS columns), tokens unlocked per owner minute, and whether the
   decision can be checked afterwards by a control.
4. Write HUMAN-TX-ASKS.tsv (repo root): rank, target, task_type, link, steps (numbered, plain words, one line each,
   ending in where to put the result: the sorter's own save, a private-repo folder link with Add file -> Upload
   files, or a reply in the board card), minutes, tokens_unlocked, why. Register it in SYSTEM.md
   (tools/system_map_check.py passes). Push by explicit path; ROOM done line with the top 5. Do not create board
   cards (the account-3 orchestrator does), do not email.
