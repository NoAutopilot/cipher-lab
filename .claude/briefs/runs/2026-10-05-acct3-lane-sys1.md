# LANE-SYS1 (account 1) -- 5 Oct 2026 17:29 UTC (account-3 orchestrator; owner: "lets get things fired back up", 5 Oct ~10:30 am PDT)
Operating rules as `.claude/briefs/runs/2026-10-04-acct3-lane-near3-run1.md` para 1. Every worker's first command:
`git fetch origin && git checkout -B main origin/main`. Write for agents (terse, machine-shaped). Opus 5.5 floor for sessions.
Process fixes from the parent's 5 Oct review (owner approved). Each tool change: offline test, --help, SYSTEM.md line, Usage 8a docstring.
1. Empty-queue auto-fill. Add to .claude/briefs/dispatcher.md (and whatever prompt file the dispatchers read each firing -- find it):
   when WORK-QUEUE.tsv has no queued row for the dispatcher's account AND its last lane closed >= 60 min ago AND no PAUSE line for that
   account in WORK-QUEUE (new convention: a row `PAUSE-<account>` with status `paused`), it adds and spawns ONE default lane row from
   `.claude/briefs/default-lane.md` (write it: top runnable HOT rows of NEXT-STEPS.tsv, cap 60, box 600, verifier jobs first), at most
   one default lane per account per 12 h. Add tools/work_queue.py --pause/--resume ACCOUNT. Test the logic offline.
2. Hot/cold split. tools/hot_cold.py: a target is HOT if it has a key source (period/published key, clear copy, period decipherment,
   gloss) or is in a sign pool with one; COLD otherwise. Write HOT-COLD.tsv; next_steps.py gains --hot-only; default-lane.md uses it.
   Report counts. Do NOT change any target's status line.
3. Verifier backlog list: tools/verify_backlog.py lists every PROGRESS.tsv / status.json reading with Audit 1 done and Audit 2 or
   Counted missing, oldest first, with the next verifier action. Write VERIFY-BACKLOG.tsv (LANE-VER1 on account 2 consumes it; run
   it early and push so they can start).
4. Small fixes: add an Archives nationales / FranceArchives row to tools/data/catalogue_ladders.tsv and re-land L11 + L42 from the
   PR 67 branch (lq_answer_check); mark stale `claimed` WORK-QUEUE rows of closed lanes `done` (TX-AGREEAUDIT, TX-ALTS, LANE-NEAR5,
   LANE-NEAR8, LANE-NEAR9) from their ROOM done lines.
Cap 60, box 600. Close with STATUS.md "LANE SYS1 handoff" and one ROOM done line.
