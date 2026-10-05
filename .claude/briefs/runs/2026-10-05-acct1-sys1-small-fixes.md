# SYS1-SF -- small fixes (job 4 of LANE-SYS1). Cap $8, box 60 min.
Lane LANE-SYS1 (account 1, orchestrator session_01J31Le8NaBKQi9NAUW3YBs4), parent brief .claude/briefs/runs/2026-10-05-acct3-lane-sys1.md (read it). First command: `git fetch origin && git checkout -B main origin/main`, then `python3 tools/room.py --start`. ROOM claim with box end (date -u), halfway cost line, one done line addressed to LANE-SYS1. Model Opus 5.5. Write for agents (terse, machine-shaped). Every tool change: offline test in tools/tests/, --help, one SYSTEM.md line (tools/system_map_check.py passes), and a Usage 8a docstring stating what it catches and at least one case it must NOT block/misclassify, each with a test. Run tools/file_shrink_guard.py on every touched shared file before the final push; push via tools/room.py --push <paths> or rebase+push. Do NOT change any target NOTES.md status line. Never call AskUserQuestion; never print credentials; never name the owner. Stop when the brief is met.
1. Add an Archives nationales / FranceArchives row to tools/data/catalogue_ladders.tsv (same columns as the others; the hosts do not
   load from the cloud -- see CLAUDE.md host table "archivesnationales.culture.gouv.fr/francearchives.gouv.fr"; rungs a runner can quote:
   the Salle des inventaires virtuelle record / FranceArchives finding-aid URL, cote, availability flag). Update tools/lq_answer_check.py
   tests if the ladder table has a test.
2. Re-land LOCAL-QUEUE.tsv rows L11 and L42 answers from the PR 67 branch (find it with the GitHub MCP tools: pull_request_read on
   NoAutopilot/cipher-lab PR 67, its head branch; git fetch origin <branch>). Apply only those two rows' answers onto main's current
   LOCAL-QUEUE.tsv (keep every other row as on main), run tools/lq_answer_check.py on them, and land if it passes; if it fails, say what
   rung is missing and leave the row unlanded. Do not merge or close the PR; tell LANE-SYS1 in the done line what remains on it.
3. WORK-QUEUE.tsv: mark rows TX-AGREEAUDIT, TX-ALTS, LANE-NEAR5, LANE-NEAR8, LANE-NEAR9 `done <ts>` (tools/work_queue.py --done) using
   the timestamp from each one's own ROOM.md done line (grep ROOM.md; if no done line exists, leave the row and say so).
4. tools/work_queue.py --check and tools/file_shrink_guard.py pass. Done line: what landed, commits.
