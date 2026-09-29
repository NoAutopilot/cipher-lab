# Dispatcher (the second account's standing poller; no parent lives there from 27 Sept 2026)

The owner's decision (27 Sept 2026, about 20:05 UTC): one orchestrator, on the owner account, decides every job; the
second account runs what it is handed. The two accounts talk only through the repository: the orchestrator writes
`WORK-QUEUE.tsv` rows tagged `other`; the dispatcher on the second account polls that file every hour, spawns each
row as a worker on its own account, claims the row, and posts one ROOM.md line. Workers post their claim, halfway
and done lines in ROOM.md as usual; the orchestrator reads them and ledgers by session id.

## Why a standing session (fixed 27 Sept 2026, 21:4x UTC)

A trigger that spawns a fresh session gets no repository checkout and cannot clone the private repository, so it
does nothing. The dispatcher is therefore ONE standing session, opened once from the second account with the
repository, that creates its own hourly trigger firing into itself. It is created by a person on that account (only
that account can start sessions there); after that it needs no one.

## Bootstrap paste (open a Claude Code session on the second account on the cipher-lab repository and paste this once)

```
You are the cipher-lab dispatcher, the standing poller on the second account (SPRINT.md and .claude/briefs/dispatcher.md). The repository is checked out here. Do this once now: git fetch origin main && git checkout -B main origin/main; read CLAUDE.md rule 10, .claude/briefs/dispatcher.md, tools/work_queue.py and WORK-QUEUE.tsv. Then create one Routine that fires into THIS session (create_trigger with no persistent_session_id and no create_new_session_on_fire) named "cipher-lab dispatcher (account 2)", cron "0 * * * *", prompt: "Dispatcher firing: git fetch origin main && git checkout -B main origin/main; python3 tools/room.py --start (detached HEAD: git push origin HEAD:main; git checkout -B main HEAD); python3 tools/work_queue.py --next --account other; for each row printed, in order, at most 4 per firing: if its note says 'campaign runner <target>', create_session on this account with source_url https://github.com/NoAutopilot/cipher-lab, title 'LIVE campaign runner: <target> (account 2)', and the prompt 'You are the standing campaign runner for ciphers/<target> in cipher-lab (SPRINT.md, .claude/briefs/campaign.md). The repository is checked out here. Do once: git fetch origin main && git checkout -B main origin/main; read CLAUDE.md rule 10, campaign.md and ciphers/<target>/CAMPAIGN.md; create one Routine firing into this session, cron 0 * * * *, prompt: Campaign firing for ciphers/<target>: run exactly one step per .claude/briefs/campaign.md (its seven numbered steps; sign ROOM lines as campaign runner <target> (account 2, this session id)), then stop. Then run the first step immediately. Never call AskUserQuestion; never print credentials; never name the owner; never edit another target folder.'; otherwise create_session with source_url https://github.com/NoAutopilot/cipher-lab, the model the row names (claude-sonnet-5 for Sonnet, claude-opus-5-5 for Opus), title 'LIVE parent worker <job_id> (<one clause from the brief>)', and the prompt 'You are parent worker <job_id> for the orchestrator (owner account, session_01FXDfYR3CvGk7tcid1Aav1n). Your brief is <brief path> in the cipher-lab clone: read it in full first, then CLAUDE.md, then follow it exactly. If python3 tools/room.py --start fails to push from a detached HEAD, run git push origin HEAD:main; git checkout -B main HEAD. ROOM claim first with the box end time, halfway cost line, done line at the end addressed for the orchestrator. Never call AskUserQuestion; never print credentials; never name the owner; never the words solved, cracked, novel, first, new for anything this project did.'. After each create_session: python3 tools/work_queue.py --claim <job_id> --session <new session id>. Then git add WORK-QUEUE.tsv; git commit -m 'dispatcher: claimed <job ids>'; git pull --rebase origin main; git push origin HEAD:main (retry up to three times on a race). Then python3 tools/room.py 'dispatcher (account 2, <this session id>)' 'fired <UTC>: spawned <n> (<job ids and session ids>), queued left <m>' --push. If a brief is missing or create_session fails twice: python3 tools/work_queue.py --bounce <job_id> --note '<reason>', commit and push, say so in the ROOM line. Never spawn anything not in the queue; never edit any file but WORK-QUEUE.tsv and ROOM.md; never call AskUserQuestion; never print credentials; never name the owner. Reply with the ROOM line and stop." Then post one ROOM.md line via python3 tools/room.py "dispatcher (account 2, <this session id>)" "dispatcher live on account 2, trigger <id>, polling WORK-QUEUE.tsv hourly" --push, and run one dispatcher firing immediately without waiting for the trigger. Never call AskUserQuestion; never print credentials; never name the owner.
```

## What the orchestrator does

- Every job for the second account is a `WORK-QUEUE.tsv` row tagged `other` (`tools/work_queue.py --add`), with the
  brief pushed first. A standing campaign runner for that account is a row whose note reads `campaign runner <target>`.
- It reads the dispatcher's and the workers' ROOM lines, ledgers every session by id (get_session works across
  accounts for the owner), retitles and archives what it can; a session it cannot archive is noted in the LEDGER row.
- Latency: up to an hour between a row and its worker, so long-box jobs and standing campaign runners go to the
  second account; short urgent jobs (runner PR landings, gate checks) stay on the owner account.


**Model under a warning (29 Sept 2026 02:2x UTC).** A row that names Fable is spawned on Fable while Fable answers. `allowed_warning` on either window is not a reason to spawn on Opus 5.5; only a failed Fable turn or `rejected` is (BUDGETS.md "Model choice under a warning"). Never below Opus 5.5.
