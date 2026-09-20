# Brief templates

One file per recurring role. A worker brief is a copy of the template with the target filled in. When the
retrospective proposes a change, it edits the template here, so improvements are diffs, not folklore. Every
brief ends with the same four lines: cap, push, report, stop.

Common tail (paste into every brief):

> Read the last 30 lines of ROOM.md first; append a line before editing a shared file and a `done` line when you stop; use `flag` for anything the orchestrator must see. Cap: about $N of usage; at most K subagents, on Sonnet unless the brief says otherwise. Commit, `git fetch
> origin main && git rebase FETCH_HEAD && git push -u origin main`, report in a short paragraph (first line:
> the answer), stop. Per rule 10, report what was found and where it was not found; never new, unpublished,
> first. Do not start other targets. Never print or commit credentials.
