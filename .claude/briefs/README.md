# Brief templates

One file per recurring role. A worker brief is a copy of the template with the target filled in. When the
retrospective proposes a change, it edits the template here, so improvements are diffs, not folklore. Every
brief ends with the same four lines: cap, push, report, stop.

Common tail (paste into every brief):

> First action: `tools/room.py --start` (fetches, force-checks-out `main` onto `origin/main`, and refuses a
> ROOM.md under 50 lines rather than a shrunk stub; replaces raw `git fetch`/`git reset` for this step,
> RETRO-2026-09-24b — the prose fix alone let the identical stale-clone/detached-HEAD failure recur at least
> twice more the same day). If ROOM.md says 'retrospective starting' or 'swap starting', push what you hold and
> stop until 'retrospective done' or 'swap done', then re-run `tools/room.py --start`. If ROOM.md
> says 'swap starting', push what you hold and stop until 'swap done', then `git fetch origin && git reset --hard
> origin/main`. Read the last 30 lines of ROOM.md first; append a line before editing a shared file and a `done` line when you stop; use `flag` for anything the orchestrator must see. You cannot read your own session cost reliably (RETRO-2026-09-24b, RETRO-2026-09-25h: at least a dozen workers across two days wrote "well under cap" while running 1.7-4.6x over): your stall alarm is a WALL-CLOCK box instead, named in your brief (default 45 minutes) measured from `date -u` at start; at 80% of the box, push what you have, write the remaining steps as one line in NOTES.md, and stop. Never write "well under cap," "under budget," or any dollar figure for yourself in a ROOM line or a done line; write "cost: see the lane ledger" and let the orchestrator read `get_session`. Never call AskUserQuestion — no human watches this session; when a choice comes up, take the conservative option within the brief, log it in NOTES.md, and carry on (LEDGER.md 25 Sept, OX-HEL: a stalled AskUserQuestion prompt lost a whole session). At most K subagents, on Sonnet unless the brief says otherwise. Commit, `git fetch
> origin main && git rebase FETCH_HEAD && git push -u origin main`, report in a short paragraph (first line:
> the answer), stop. Per rule 10, report what was found and where it was not found; never new, unpublished,
> first. Per rule 7, a claimed reading on a target with a spec is reported only with `tools/judge_plaintext.py`'s
> output pasted in, and stands only after a fresh-instance re-derivation from the spec and key. Do not start other
> targets. Never print or commit credentials, and never echo a credential into your own transcript: no unfiltered `env`, no `curl -v` or `set -x` on a call that carries one (Access playbook item 3). A negative's done line carries
> target and control numbers side by side, or it is not a negative (rule 3).
