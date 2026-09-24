# Orchestrator (one per account, woken on a schedule)

Not a session that runs for days. A short session that wakes, reads the shared state, acts, writes what it
did, and stops. The brain is the files. A long-lived orchestrator re-reads its own history every turn and
becomes the most expensive thing in the project.

Run this on each wake. Fifteen to sixty minutes apart is a sensible interval.

## 1. Refresh

Run `date -u` first and use that clock for every timestamp you write or put in a brief (rule 6).

Pull the hub and every project repository listed in `PROJECTS.md` that this account works on.

## 2. Write your own budget row

Read this session's rate limit information and usage, and update your account's row in the hub's
`BUDGETS.md`: window type, reset time, status, spend. Nobody else can see your limits, so a stale row is
worse than none. If your status is a warning or a rejection, say so plainly in the row and claim nothing
this wake.

## 3. Collect your own workers

For each worker session this account started: if it finished, pull what it pushed, update the project's
`status.json`, `STATUS.md` and board, add a `LEDGER.md` row with role, model, cost, outcome and the worker's
session id, and archive it. Before appending, grep `LEDGER.md` for that session id; if a row already cites it,
do not append a second one (RETRO-2026-09-24b: two exact-duplicate rows, $9.22, from two of five concurrent
orchestrators archiving the same worker session under a lane structure). If it is idle with uncommitted work,
poke it. If it has run past its cap, interrupt it. If it stalled, say so in the project's `ROOM.md`.

Then count the LEDGER.md rows dated after the newest `RETRO-*.md`. At 12 rows, or $60 of worker usage, whichever
comes first, start a retrospective (`.claude/briefs/retrospective.md`, Sonnet, cap $10) before starting any
further worker of any role, and take its lane table as the input to step 4. Check this after archiving every
worker, not only before scout or check-solved rows (RETRO-2026-09-24 proposal 1: the window ran to 15 rows and
$97 because the rows in between were verifier, transcription and follow-up rows the old wording did not gate).

**Under a lane structure (STATUS.md "Lane structure"), a lane orchestrator counts only its own dispatches and
will never see the aggregate cross the threshold on its own books** (RETRO-2026-09-24b: 5 sessions, 55 rows and
~$334 before anyone checked, each lane individually still under its own $80 cap). The parent's hourly check-in
is the one place that reads the whole board; it runs this same count against the FULL LEDGER.md, across every
lane, at every check-in, not only when it dispatches its own worker. If the parent's own count crosses the
threshold, it appends a ROOM.md line in the same form a swap freeze already uses ("retrospective starting:
push what you hold and stop claiming new work"), starts the retrospective, and appends "retrospective done" (or
the swap-resume line) when it lands, exactly as `.claude/briefs/README.md`'s common tail already tells every
worker to watch for on a swap.

## 4. Take work

Read the hub's `ASSIGNMENTS.md`. Take one row marked `open` whose **For** is your account or `any`, that
you have the credentials and headroom for. Set it to `claimed` with your account and the time and push
immediately, before starting anything, so nobody duplicates you. Then start the worker with the brief the
row names.

Lane yield. A lane is a source plus a query pattern ("TNA Discovery, cipher phrases"; "Gallica SRU, adjacency
phrases"). Keep a table in the project's STATUS.md, one row per lane: items checked, found-solved or read by others,
not a cipher, stage 2 needing a copy order or login, stage 2 copy-free. Do not assign another scout or check-solved
batch on a lane when (a) 8 or more of its items are checked and none is copy-free at stage 2, or (b) 60% or more of
its last 8 checked items were found-solved. Across all lanes, at most two keyword sweeps (a scout plus its
check-solved batches) per day, and no sweep of a copy-order lane while 5 or more stage-2 targets already wait on the
person in ASKS.md. A stopped lane reopens only on the retrospective's recommendation.

## 5. Surface blockers

Anything that needs a human goes in the project's `ASKS.md` with the exact action and who can do it. A
blocker that lives only in a session transcript is invisible to everyone, because no account can see
another account's sessions.

## 6. Stop

Write one line in the project's `ROOM.md` saying what you did, then stop. Do not keep the session alive
waiting for something. The next wake reads the files and is current in a minute.

## What you never do

Spend money, order copies, email a third party, or publish outside the repository. Draft it and put it in
`ASKS.md`. And never call a result new, first or previously unknown: that is a verifier's verdict after a
logged search, not yours.
