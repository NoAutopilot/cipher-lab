# LEARN worker: what the other account's sessions pushed, and what to take from it

Sonnet, cap $5 or 30 minutes, whichever first. Spawned by the parent about every three hours while lanes run (owner's
request, 25 Sept 2026, 17:10 UTC clock read: "have some sort of a check-in to see what the other staff members are
pushing to GitHub, see if there's anything you can learn from it to improve what you're doing").

Two accounts work in this repository and neither sees the other's sessions; the only shared record is git. This worker
reads that record for the window the parent names and turns it into at most five concrete, transferable practices.

1. `date -u`; `python3 tools/room.py --start`; ROOM claim "LEARN <window>: cross-account read".
2. `git log origin/main --since="<window start>" --format='%h %cI %s' --stat` and, for every commit whose subject or
   ROOM line names a lane this parent does not run (on 25 Sept: ZX, CX2, the owner-account parent
   session_01FXDfYR3CvGk7tcid1Aav1n, QA runs, any lane letter not in the parent's ASSIGNMENTS), read the diff of its
   NOTES.md, AUDIT.md, QA/*.md, RETRO-*.md, tools/ and .claude/briefs/ changes. Also read the other account's "Parent
   handoff (owner account" section and any "LANE <X> handoff" it added in the window.
3. For each thing they do that we do not, or do better than we do, write one row: what (one sentence), where (commit
   and file), evidence it worked (a number from their own log: agreement rate, cost, a gate passed, a catch), and the
   diff to one of our brief or tool files that would adopt it. Skip anything already in CLAUDE.md, LESSONS.md or
   `.claude/briefs/README.md`. Also list, separately, any place their work and ours overlap or contradict (same target,
   conflicting status words, two tools for one job) with the file and line.
4. Write `LEARN-<date>-<hhmm>.md` (at most 80 lines: the rows, the overlaps, a one-line verdict "nothing new" is fine),
   commit, push, ROOM done line "LEARN: N practices, M overlaps, file <name>".
Rule 10 throughout; touch no target; never print or commit credentials; the parent applies brief- and tool-only diffs
and puts anything else to the owner.
