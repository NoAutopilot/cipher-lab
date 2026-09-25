LANE R7 WORKER COMMON (parent: LANE R7 orchestrator, session_01UpWfpbLwYL1xmDG1vFyi6h). Written 25 Sept 2026 20:01 UTC.
Read, in order: CLAUDE.md; `.claude/briefs/runs/2026-09-24-lane-r4-common.md` (base rules); `.claude/briefs/runs/2026-09-25-lanes-7b-COMMON.md`
(25 Sept addendum, wins where they differ); `.claude/briefs/runs/2026-09-25-lane-r6-common.md` (its overrides still hold); this file; your job brief.
First command: `python3 tools/room.py --start`. ROOM lines through `tools/room.py` only.
Overrides and additions:
- Wall-clock box and $ cap in your brief: stop and push at whichever comes first. The box is also a minimum: do not stop early with the job undone.
  Never read your own cost (no get_session self-read); the orchestrator reads it.
- No subagents unless your brief names them (R6 lesson: a pass-B subagent cost 3x the worker's own pass).
- Hosts: only those your brief names, at the Access playbook's per-host limits; report the request count per host in the done line.
- Every cryptanalytic run goes through `tools/family_run.py` or the target's own control script with the control first; a target run without its
  control on record does not count (rule 3). Near-solve numbers go into your NOTES section; the orchestrator moves NEAR.md.
- Never call AskUserQuestion. If blocked, write a `flag:` ROOM line, push, stop.
- Rule 10 wording only; never `solved`, new, first, unpublished, previously unread. Report what was found and where it was not found.
- Done line: `done: for LANE R7: <target> <target number> vs <control number> ...`, requests per host, no cost figure.
- Python deps: `pip install -q numpy pillow scikit-learn scikit-image` if an import fails (do not commit a venv).
