# Campaign runner (SPRINT.md; fired by a per-target trigger every hour; overlap guard 55 minutes)

A campaign is one target worked continuously. Its state is `ciphers/<target>/CAMPAIGN.md` (format in
tools/campaign.py's docstring): a ranked hypothesis table and a step log. The runner is a fresh session that does
ONE step and exits; the trigger brings the next runner. Nothing here parks: a runner that finds no runnable
hypothesis writes three new ones (from the folder's evidence) before it stops, and says so.

## Paste-ready trigger prompt (create_trigger, create_new_session_on_fire true, cron hourly, staggered minutes; one per target)

```
You are the campaign runner for ciphers/<TARGET> in cipher-lab (https://github.com/NoAutopilot/cipher-lab), a fresh session that does one step and exits. Read CLAUDE.md rule 10, .claude/briefs/campaign.md, SPRINT.md, then ciphers/<TARGET>/CAMPAIGN.md, NOTES.md (the last 300 lines at least), HYPOTHESES.md if present, and the last 40 ROOM.md lines mentioning <TARGET>. Steps:
1. git fetch origin main && git checkout -B main origin/main; python3 tools/room.py --start (detached HEAD: git push origin HEAD:main; git checkout -B main HEAD). If another runner's ROOM claim on <TARGET> is under 90 minutes old with no done line, stop and say so.
2. python3 tools/campaign.py --next <TARGET>. If it prints "budget spent for today" or "closed", post one ROOM line saying so and stop. If it prints "none": write three new hypotheses into the table (each grounded in a named file or finding in the folder, with needs, est_usd, rank), commit, push, post a ROOM line naming them, and stop.
3. Otherwise take that row: set its status to `running <your session id>`, commit CAMPAIGN.md by path, push; post the ROOM claim "campaign <TARGET> step <id>: <hypothesis>, cap <est> USD, box 60 min".
4. Run the step with the repository's own tools and briefs (transcription.md, solver.md, verifier.md, check-solved.md as the hypothesis needs), at most the row's est_usd, at most 4 vision subagent calls, halfway cost line in ROOM. Every result goes into NOTES.md under "## Campaign step <id> (<UTC>)" with the numbers, controls and files; never a reading claim without a control, never a class change (status.json is the verifier's), never the words solved / cracked / novel / first / new for anything this project did.
5. Record: the row's status to done (or dropped, with why) and its result cell to one clause; re-rank the remaining open rows if the result changes their order and say why in the log; add any new hypothesis the step suggested (a failed transcription pass suggests a re-crop; a passed calibration suggests the blind passes; a document need becomes `needs: doc <what>` with the ASKS row); append the log line; python3 tools/campaign.py --spend <TARGET> <cost estimate from your own turn, or the est if unknown>; commit CAMPAIGN.md and NOTES.md by path; python3 tools/campaign.py --check; push (git pull --rebase origin main first; keep both sides).
6. If the step produced a reading-ready line (two blind passes reconciled, key applied with a shuffled-key control passing the gate), post "reading ready: for LANE VO3 -- <TARGET> ..." in ROOM so the verifier lane picks it up.
7. Done line in ROOM: "campaign <TARGET> step <id> done: <result one clause>; next <id> <hypothesis>; spent today <n>/<budget>". Stop.
Never call AskUserQuestion; never print credentials; never name the owner; never edit another target's folder; the owner's Codex session may also work <TARGET> (Armstrong): read its ROOM lines and folders first and never redo a step it has recorded.
```

## Orchestrator duties per campaign, at every check-in

Read CAMPAIGN.md; update the SPRINT.md scoreboard row; argue with the ranking (re-rank with a logged reason if the
runner's order is wrong); raise the daily budget only with a logged reason; ledger each runner session by id (the
LEDGER row's role is "campaign runner <target> step <id>"); close a campaign only with `closed: <reason>` and a
SPRINT.md note. A campaign with three consecutive dropped steps and no new hypothesis is a red line for the owner,
not a close.
