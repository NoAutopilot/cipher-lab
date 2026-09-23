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
`status.json`, `STATUS.md` and board, add a `LEDGER.md` row with role, model, cost and outcome, and archive
it. If it is idle with uncommitted work, poke it. If it has run past its cap, interrupt it. If it stalled,
say so in the project's `ROOM.md`.

## 4. Take work

Read the hub's `ASSIGNMENTS.md`. Take one row marked `open` whose **For** is your account or `any`, that
you have the credentials and headroom for. Set it to `claimed` with your account and the time and push
immediately, before starting anything, so nobody duplicates you. Then start the worker with the brief the
row names.

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
