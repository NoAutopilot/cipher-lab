# STALE-SWEEP (account-3 worker, 3 Oct 2026 17:0x UTC; owner: "I don't want to lose that data")

Opus 5.5 (script-first; Sonnet subagents allowed for the per-claim lookups). Cap USD 6, box 50 min. No vision, no network beyond git.
Claim in ROOM.md first (tools/room.py); done line at the end.

`python3 tools/orphan_check.py --no-sessions --room` lists 92 STALE CLAIMs (a ROOM.md claim with no done line, 23 Sept - 3 Oct 2026;
the 6 from 1-3 Oct were closed by the orchestrator at 16:45). For EACH remaining claim, decide from the repository alone (git log
--author/--grep by role name and target folder, the folder's NOTES.md/HYPOTHESES.md/AUDIT.md, later ROOM lines on the same target, LEDGER.md):
- `landed`: its result is in the repo (name the commit and file);
- `superseded`: a later job on the same target did the same step (name it);
- `lost`: work started (a prereg, scratch files referenced, a halfway line) but no result landed and nothing later covers it -- name what is
  missing and the step to redo it (brief path if one exists);
- `never-started`: no commit or file trace at all.
Write `STALE-CLAIMS-2026-10-03.md` (one table row per claim: time, role, target, verdict, evidence, redo-step) and, for every `lost` row,
add one line under the target NOTES.md "## Remaining gaps" (rule 5 format, "; next: <step>, ~$<cost>") so tools/next_steps.py picks it up.
Then post ONE ROOM line per verdict class with the counts (not one line per claim) and mark the claims closed by listing them in the
table -- do not rewrite ROOM.md history. tools/system_map_check.py if you add a tool (you should not need one); file_shrink_guard on every
file touched; commit by explicit path; push (commit first, then fetch/rebase/push; no --autostash with other edits pending).
Report counts per verdict and the list of `lost` items in plain words.

## Part 2, every account (owner 17:2x: "need it for all accounts")
ROOM.md is shared, so part 1 already covers every account's claims. But a session that stalled without ever posting a claim is visible
only to its own account (list_sessions shows only your own account). So each account's live lane orchestrator / parent does this once, now:
`mcp list_sessions mine=true` (paginate), and for every session that is NOT archived (idle, blocked, failed, review_ready) and is not itself
a live lane/parent/dispatcher: get_session, read its last summary; decide landed / superseded / lost / never-started exactly as in part 1
(repo evidence); append one row per session to `STALE-CLAIMS-2026-10-03.md` under a heading "## Sessions, account <N>"; for `lost` add the
NOTES.md "## Remaining gaps" redo line; then archive the session (archive only after the row is written). Post one ROOM line with counts.
Account 3's non-archived sessions as of 17:2x UTC (for STALE-SWEEP, which is on account 3): session_0113PwRRnYY4NLTGoND6ebFm (Debosnys R6
MAGCIPHER2, private -- record only, do NOT archive or read private material into this repo), session_01Vtwc6CEJD2BSnYdzzY4f8W (F61 campaign
runner 16), session_016uAW8YgYrVGtYiXdHpR1Rq (OUT-CHECK-TM3), session_01YRxhvLZems8u4Y34NV2jdX (VERIFY-CEPPO-D2-1),
session_019cJYkajEQyd7wXeaDJjfZF (Armstrong line B, failed), session_01Noix4JTUhtvS6M6LYxDmwg (dispatcher bootstrap),
session_01FjVZSWMkiqRej2VVuV4Ru4, session_0184aEYLcRsRq1umMaZVciUW (non-cipher-lab: record as out-of-scope, do not archive).
