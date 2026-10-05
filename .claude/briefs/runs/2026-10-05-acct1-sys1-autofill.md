# SYS1-AF -- empty-queue auto-fill (job 1 of LANE-SYS1). Cap $14, box 120 min.
Lane LANE-SYS1 (account 1, orchestrator session_01J31Le8NaBKQi9NAUW3YBs4), parent brief .claude/briefs/runs/2026-10-05-acct3-lane-sys1.md (read it). First command: `git fetch origin && git checkout -B main origin/main`, then `python3 tools/room.py --start`. ROOM claim with box end (date -u), halfway cost line, one done line addressed to LANE-SYS1. Model Opus 5.5. Write for agents (terse, machine-shaped). Every tool change: offline test in tools/tests/, --help, one SYSTEM.md line (tools/system_map_check.py passes), and a Usage 8a docstring stating what it catches and at least one case it must NOT block/misclassify, each with a test. Run tools/file_shrink_guard.py on every touched shared file before the final push; push via tools/room.py --push <paths> or rebase+push. Do NOT change any target NOTES.md status line. Never call AskUserQuestion; never print credentials; never name the owner. Stop when the brief is met.
Context: dispatchers (account 1 session_01FXDfYR3CvGk7tcid1Aav1n; account 2 session_017E8NVaLGF23Wd9DtaiA91T) fire from Routine
prompts stored in their triggers (text in .claude/briefs/dispatcher.md "Bootstrap paste" sections); each firing runs
`python3 tools/work_queue.py --next --account <acct>` then commits WORK-QUEUE.tsv. You cannot edit their stored trigger prompts, so put the
logic where every existing firing already reaches it: inside `work_queue.py --next` (opt-out flag --no-autofill), and also document it
in dispatcher.md (both sections, and the bootstrap pastes for future re-bootstraps).
1. Rule: when WORK-QUEUE.tsv has no queued row for that account AND that account's last lane row (LANE-*) closed (done) >= 60 min ago
   (none open) AND no row `PAUSE-<account>` with status `paused` AND no default lane for that account was added in the last 12 h, --next
   appends ONE row DEFAULT-<account>-<YYYYMMDD-HHMM> (brief .claude/briefs/default-lane.md, Opus 5.5, cap 60, box 600, queued, note
   "auto-fill: empty queue") and prints it like any queued row. Account aliases (owner == account-1, other == account-2, third ==
   account-3) must be treated as the same account -- check how work_queue.py already maps them.
2. tools/work_queue.py --pause ACCOUNT / --resume ACCOUNT (adds/updates the PAUSE-<account> row; resume sets it `done <ts>`). --check
   must accept PAUSE rows.
3. Write .claude/briefs/default-lane.md: a lane-orchestrator brief (own account, operating rules as
   .claude/briefs/runs/2026-10-03-acct3-lane-pools-images.md para 1) whose backlog is the top runnable rows of
   `python3 tools/next_steps.py --hot-only` (a sibling worker SYS1-HC is adding --hot-only and HOT-COLD.tsv now; if it has not landed
   when you finish, reference it anyway and fall back to plain next_steps.py), verifier jobs first (VERIFY-BACKLOG.tsv from sibling
   SYS1-VBL), cap 60, box 600, never a folder with a ROOM claim < 6 h, LANE <X> handoff + done line at close.
4. Offline tests covering: fills on empty queue; does NOT fill when a queued row exists, when a lane closed < 60 min ago, when a lane is
   still claimed, when PAUSE is set, when a default lane was added < 12 h ago, for the other account's empty queue only.
5. Do not touch the live trigger prompts. Done line: test count, commits, one sentence on how a dispatcher picks it up.
