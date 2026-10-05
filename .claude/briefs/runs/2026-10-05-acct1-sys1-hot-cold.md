# SYS1-HC -- hot/cold split (job 2 of LANE-SYS1). Cap $12, box 90 min.
Lane LANE-SYS1 (account 1, orchestrator session_01J31Le8NaBKQi9NAUW3YBs4), parent brief .claude/briefs/runs/2026-10-05-acct3-lane-sys1.md (read it). First command: `git fetch origin && git checkout -B main origin/main`, then `python3 tools/room.py --start`. ROOM claim with box end (date -u), halfway cost line, one done line addressed to LANE-SYS1. Model Opus 5.5. Write for agents (terse, machine-shaped). Every tool change: offline test in tools/tests/, --help, one SYSTEM.md line (tools/system_map_check.py passes), and a Usage 8a docstring stating what it catches and at least one case it must NOT block/misclassify, each with a test. Run tools/file_shrink_guard.py on every touched shared file before the final push; push via tools/room.py --push <paths> or rebase+push. Do NOT change any target NOTES.md status line. Never call AskUserQuestion; never print credentials; never name the owner. Stop when the brief is met.
1. tools/hot_cold.py: a target folder (ciphers/*) is HOT if it has a key source -- a period or published key, a clear copy/plain-text
   twin, a period decipherment, or an interlinear/marginal gloss -- or belongs to a sign pool (same sender/office/key family; see
   KEY-OFFICES.tsv, KEY-DESIGN.tsv, pool notes in NOTES.md/STATUS.md) with a member that has one; COLD otherwise. Evidence from files on
   disk only (status.json key field, AUDIT.md key line, key.tsv/keys present, NOTES.md phrases, PROGRESS.tsv ksrc column, KEY-OFFICES.tsv);
   every HOT row names the evidence (file + phrase) and kind (key|clear|decipherment|gloss|pool:<member>). Conservative: a mere mention
   of "key" in prose is not evidence -- design the matcher and say in the docstring what it must NOT count, with tests.
2. Write HOT-COLD.tsv (folder, hot_cold, kind, evidence, pool) with header comment; --check for staleness.
3. tools/next_steps.py gains --hot-only (filter NEXT-STEPS output to HOT folders, reading HOT-COLD.tsv); test it; keep default output
   unchanged.
4. Spot-check 10 HOT and 10 COLD rows by eye against their folders; fix the matcher where wrong; report the spot-check tally.
5. Done line: HOT n / COLD n / total, spot-check tally, commits. Do NOT change any target's status line.
