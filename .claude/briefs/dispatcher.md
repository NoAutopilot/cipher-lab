# Dispatcher (the other account's routine; no parent on that account from 27 Sept 2026, 20:xx UTC)

The owner's decision (27 Sept 2026, about 20:05 UTC): one orchestrator, on the owner account, decides every job;
the other account runs jobs it is handed and nothing else. Two parents cost a third of all effort in
coordination (RETRO-2026-09-27x) and still missed claim windows; one queue file replaces the cross-account asks,
the tie-break and the account-roles split.

## How the other account gets work

`WORK-QUEUE.tsv` (tools/work_queue.py) is the only assignment channel. The orchestrator adds rows with
`account = other`; a scheduled trigger on the other account starts a fresh session every hour (the dispatcher)
that pulls main, takes those rows, spawns each as a worker on its own account, and exits. The dispatcher has no
targets, no check-in duties, no ledger duties and posts no asks; the orchestrator ledgers every worker by session
id whichever account ran it. ROOM.md keeps its claim / halfway / done lines from workers; the orchestrator is the
only reader that acts on them.

## Paste-ready trigger prompt (create_trigger on the OTHER account, create_new_session_on_fire true, hourly at :20)

```
You are the cipher-lab dispatcher, a fresh session on the second account (no parent lives here). Clone: https://github.com/NoAutopilot/cipher-lab. Read CLAUDE.md rule 10 and .claude/briefs/dispatcher.md first. Steps, all of them, then stop:
1. git fetch origin main && git checkout -B main origin/main. python3 tools/room.py --start (if its push fails on a detached HEAD: git push origin HEAD:main; git checkout -B main HEAD).
2. python3 tools/work_queue.py --next --account other. For each row printed, in order: read its brief; create_session on THIS account with source_url https://github.com/NoAutopilot/cipher-lab, the model the row names (claude-sonnet-5 for Sonnet, claude-opus-5-5 for Opus), title "LIVE parent worker <job_id> (<one clause from the brief's first line>)", and the prompt "You are parent worker <job_id> for the orchestrator (owner account, session_01FXDfYR3CvGk7tcid1Aav1n). Your brief is <brief path> in the cipher-lab clone: read it in full first, then CLAUDE.md, then follow it exactly. If python3 tools/room.py --start fails to push from a detached HEAD, run git push origin HEAD:main; git checkout -B main HEAD. ROOM claim first with the box end time, halfway cost line, done line at the end addressed 'for the orchestrator'. Never call AskUserQuestion; never print credentials; never name the owner; never the words solved, cracked, novel, first, new for anything this project did." Then python3 tools/work_queue.py --claim <job_id> --session <new session id>. At most 4 rows per firing; leave the rest queued.
3. Commit WORK-QUEUE.tsv by path (git add WORK-QUEUE.tsv; git commit -m "dispatcher: claimed <job ids>"); git pull --rebase origin main; git push origin HEAD:main; retry the pull/push up to three times on a race.
4. python3 tools/room.py "dispatcher (other account)" "fired <UTC>: spawned <n> (<job ids and session ids>), queued left <m>" --push.
5. If a row's brief is missing or create_session fails twice: python3 tools/work_queue.py --bounce <job_id> --note "<reason>", commit and push as in step 3, and say so in the ROOM line. Never spawn anything not in the queue; never edit any file but WORK-QUEUE.tsv and ROOM.md; never call AskUserQuestion; never print credentials; never name the owner. Reply with the ROOM line and stop.
```

## What the orchestrator does that it did not before

- Writes every job for either account as a WORK-QUEUE.tsv row (brief first, then the row); spawns its own
  account's rows itself, at once; leaves the other account's rows for the dispatcher's next firing (up to an hour
  of latency, so the heavy, long-box jobs go to the other account and the urgent short ones stay on this one).
- Reads done lines for both accounts' workers, ledgers them with the session's cost (get_session works across
  accounts for the orchestrator's owner), retitles and archives them (archive_session may be refused for the other
  account's sessions; then the retitle is enough and the LEDGER row says so).
- Runner PRs: no tie-break; the orchestrator claims every runner PR at its check-in and queues the landing.
- The former SOLVE lanes' open targets are the orchestrator's; nothing in progress was moved, the parent that held
  them stood down after its live workers finished.
