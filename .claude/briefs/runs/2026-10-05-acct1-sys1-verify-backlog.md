# SYS1-VBL -- verifier backlog list (job 3 of LANE-SYS1). Cap $8, box 60 min. URGENT: LANE-VER1 (account 2) waits on it.
Lane LANE-SYS1 (account 1, orchestrator session_01J31Le8NaBKQi9NAUW3YBs4), parent brief .claude/briefs/runs/2026-10-05-acct3-lane-sys1.md (read it). First command: `git fetch origin && git checkout -B main origin/main`, then `python3 tools/room.py --start`. ROOM claim with box end (date -u), halfway cost line, one done line addressed to LANE-SYS1. Model Opus 5.5. Write for agents (terse, machine-shaped). Every tool change: offline test in tools/tests/, --help, one SYSTEM.md line (tools/system_map_check.py passes), and a Usage 8a docstring stating what it catches and at least one case it must NOT block/misclassify, each with a test. Run tools/file_shrink_guard.py on every touched shared file before the final push; push via tools/room.py --push <paths> or rebase+push. Do NOT change any target NOTES.md status line. Never call AskUserQuestion; never print credentials; never name the owner. Stop when the brief is met.
1. Write tools/verify_backlog.py: read PROGRESS.tsv (columns 1=Audit 1, 2=Audit 2, C=Counted; see its own header comments and
   tools/progress_block.py for the column meanings -- confirm them there, do not guess) and status.json results; list every reading
   with Audit 1 done and Audit 2 or Counted missing, oldest first (by last audit date / updated date; state the key used), one row each:
   name, folder, leaf/row, audit1_date, missing (audit2|counted|both), next_action (the concrete next verifier action: e.g. "second
   adversarial audit per CLAUDE.md Outreach gate 2 (separate session)", "count per rule 4/4a: tools/depth_check.py <t>", naming the files),
   source. Reconcile the two registers: a row present in one and absent from the other is listed with a note, not dropped.
2. Write VERIFY-BACKLOG.tsv (header comment naming the generator and date from date -u). Add --check (exit non-zero if the committed
   file is stale). Test offline with fixtures. PUSH THE TSV AS SOON AS IT IS CORRECT, then post a ROOM line
   "flag: VERIFY-BACKLOG.tsv ready for LANE-VER1 (N rows)" before polishing anything else.
3. Done line: row count by missing-kind, commit hashes.
