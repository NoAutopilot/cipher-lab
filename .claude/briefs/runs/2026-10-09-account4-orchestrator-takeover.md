# Orchestrator takeover on account 4 (9 Oct 2026, 04:5x UTC)

Written by session_01SnKHiQk7k7VPDGhfcPeiVV (account-4 parent 2) after the owner said "Orchestrator is down on acct 3 ...
I pick you". That session posted the TAKEOVER line (ROOM.md, 04:56 UTC 9 Oct) but is at 662k context, so the role runs in a
fresh session. You are that session: the single orchestrator for all accounts (parent.md "Single orchestrator", "Orchestrator
fallback chain"), on account 4, until the owner or a handback line says otherwise. The owner talks to you.

## Why the takeover
- Last signed `| orchestrator (account 3) |` ROOM line: 02:03 UTC 9 Oct (sorter re-render flag). The account-3 holder,
  session_0198Cv8ypBfBVfRToKVWx33M, last committed 03:47 UTC. The owner reports it down. You cannot see or change account-3
  sessions or triggers; never try. Debosnys and NoAutopilot/cipher-lab-private stay account 3's (never taken over).

## On start (in this order)
1. `cd /home/user/cipher-lab && git fetch -q origin main && git rebase -q FETCH_HEAD` (never git stash); `date -u`;
   `export CIPHERLAB_ACCOUNT=account-4` on every command.
2. Read `.claude/briefs/parent.md` in full (start with "On start" and "Duties at every check-in"; also "Keep slots full",
   "Orchestrator fallback chain", "Standby dispatch", "Model floor", "Owner desk asks"), then `hub-seed/CHECKIN-PROMPT.md`
   (the account-3 orchestrator's mirror: its OWNER REPORT FORMAT and NO CRACKS paragraphs, added 5-9 Oct, are current;
   the 29 Sept track paragraphs -- Armstrong, f.61, Mercy, Debosnys budgets -- are history, check them against ROOM/STATUS
   before acting), the UPDATES.md tail (8-9 Oct entries), CLAUDE.md, BUDGETS.md, ASKS.md `desk` rows, NEAR.md, the
   newest STATUS.md handoff sections (grep `^## ` and read the 8-9 Oct ones), and ROOM.md from 8 Oct 18:00 UTC.
3. Post `| orchestrator (account-4) | first check-in ...` via `python3 tools/room.py 'orchestrator (account-4)' '...' --push`
   naming this session id, then run the full check-in.

## State at takeover (from ROOM.md, 04:56 UTC)
- Live lanes (all were reporting "for acct3-orchestrator"; they now report to you):
  - account 1: LANE SIG-5 (lane orchestrator; box to 14:40 UTC, cap 60; seven_day allowed_warning), worker SIG5-4612E
    session_01YQUEWkZZRErsEENMrhSjsV and SIG5-58-270; Gallica answered 403 at 04:43.
  - account 2: LANE FAMILY-A2f (lane orchestrator; five_hour allowed), workers MANT-INV08, BRANDT-MARGIN (done).
  - account 4: LANE MQS (Mary Stuart method tools; DEFAULT-account-4-20261009-0235, session_01M1fN8Gk2cnaYWXybwXW1xD),
    worker MQS-LOCK session_01AbGrrJD74ohkcZQfaN6LzW.
- Dispatchers / standing sessions: account 1 dispatcher session_01FXDfYR3CvGk7tcid1Aav1n (fires hourly ~:40); account 4
  dispatcher session_01PpZtGZsbseHrXViC8rzExA (fires ~:35); account 2's dispatcher; the owner-account standby posts
  `standby (owner account) | alive ...` lines. A session can create sessions only on its own account: work for accounts
  1-3 goes through WORK-QUEUE.tsv rows tagged for that account (`tools/work_queue.py --add`), which their dispatchers spawn.
- Open items addressed to the orchestrator:
  - BERGH sorter "ready for publication" (BERGH-SORT, 04:22): ciphers/wvo-11106-bergh-1572/sorter/bergh_sorter.html.
    Run `python3 tools/sorter_preflight.py <page> --expect-owner-account`, eye the contact sheet, build it on the current
    sorter template (account 3 was adding template 2026-10-09.1, "Check these first tiles start in the Taken-out tray";
    check whether it landed), publish with the Artifact tool and `capabilities: {"db": {}}`, put one desk card/ASKS row.
  - The 02:03 flag: the owner hit the iPhone strip bug on the Harley 287 sorter (old template 2026-10-06.1). Account 3
    was re-rendering every live sorter on the current template; check in ROOM/commits what it finished and finish the rest
    (a sorter artifact owned by account 3 can only be republished from account 3 -- if so, queue a WORK-QUEUE row tagged
    for account 3 and say so to the owner).
  - Huntington reply SENT by the owner 9 Oct 01:3x UTC; OUT-CHECK-HUNT-SHORT continues as a post-send check.
  - Run `python3 tools/orphan_check.py` and parent.md duty 3a's dropped-request check (h) for every line addressed to
    "acct3-orchestrator" / "the account-3 orchestrator" since 8 Oct 18:00 that has no answer.

## Rules
- Model: the orchestrator on Fable if account 4 has Fable usage, else Opus 5.5; never anything below Opus 5.5 for you,
  lanes or workers. `rate_limit_info` from get_session: `rejected` -> post `| orchestrator (account-4) | HANDOFF` and stop
  spawning; seven-day `allowed_warning` alone does not stop spawning (BUDGETS.md).
- Heartbeat: a `| orchestrator (account-4) | check-in ...` line at least every 90 minutes while you hold the role; arm your
  own check-in (send_later, self-bound) at every firing -- re-arm first. Keep slots full per parent.md (target live counts per
  account; 10-15 min re-arm while S-band workers are live).
- Mirror: rewrite `hub-seed/CHECKIN-PROMPT.md` as your own check-in prompt (role account 4; keep the owner report format and
  no-cracks paragraphs) once you have read the state, and refresh it whenever state changes, so a standby can continue.
- Handback: if a `| orchestrator (account 3) |` line appears after the 04:56 TAKEOVER line, the owner decides who holds the
  role; until he does, keep running and say so to him once. Two orchestrators posting check-ins for two hours with no
  decision: ask him.
- Owner reports: CHECKIN-PROMPT.md "OWNER REPORT FORMAT" (header with `date`, SOLVES/CLOSEST/NEW, full progress block via
  `python3 tools/progress_block.py --no-notes --on-it`, then --unassigned handed out as WORK-QUEUE rows, What moved,
  Accounts, Archives, Waiting on you, Fixes today). Plain language, Pacific time first.
- CLAUDE.md throughout (rules 3, 4, 7, 9, 10; outreach drafted only, never sent by you; never print credentials; never
  force-push; stage by explicit path).
- Context: at about 750k used_tokens, write `hub-seed/SUCCESSOR-PROMPT.md` for the orchestrator role and hand over to a fresh
  session the same way.
