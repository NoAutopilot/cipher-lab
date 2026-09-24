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
> origin/main`. Read the last 30 lines of ROOM.md first; append a line before editing a shared file and a `done` line when you stop; use `flag` for anything the orchestrator must see. Cap: about $N of usage; at most K subagents, on Sonnet unless the brief says otherwise. Commit, `git fetch
> origin main && git rebase FETCH_HEAD && git push -u origin main`, report in a short paragraph (first line:
> the answer), stop. Per rule 10, report what was found and where it was not found; never new, unpublished,
> first. Do not start other targets. Never print or commit credentials, and never echo a credential into your own transcript: no unfiltered `env`, no `curl -v` or `set -x` on a call that carries one (Access playbook item 3).
