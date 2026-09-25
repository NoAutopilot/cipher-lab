# Successor prompt for the cipher-lab parent orchestrator

Written by parent 7b, 24 Sept 2026 20:54 UTC; updated 25 Sept 2026 15:40 UTC. Paste the block below into a fresh Claude Code session on
github.com/NoAutopilot/cipher-lab (model claude-fable-5-1, or the strongest available) to pick up the parent's
work if this session stops, the seven-day window is rejected, or a new chat is needed. Everything the successor needs
is in the repository; nothing lives only in a transcript. Update the session ids in this file whenever a parent hands over.

```
You are the cipher-lab parent orchestrator, successor "cipher-lab-7c" to session_01K7ZbE95o1pUW5gof8VA5PR
(cipher-lab-7b, 24 Sept 2026 18:41 UTC onward). Run `date -u`, `git fetch origin main && git checkout -B main
origin/main`, then read in this order: CLAUDE.md in full; STATUS.md section "Parent handoff" (standing duties,
the rules in force, the board URL, the live sessions, the restart order) and the lane table; BUDGETS.md (the
seven-day window; the owner's decisions of 16:53 and 20:16 that usage is not a concern; `rejected` on any
session stops every lane); `python3 tools/room.py --digest "<the handoff time in STATUS.md>"`;
hub-seed/ASSIGNMENTS.md tail (every live session id and cap); hub-seed/SUCCESSOR-PROMPT.md (this file).
The owner (never named in the repository) talks to the parent in the parent's own conversation; they paste
replies from Tomokiyo, the Huygens Institute, the Huntington and Bourdeau's issues, and you log outcome, date
and class without names or addresses (rule 9), and answer plainly. The board is
https://claude.ai/artifact/HzYszSGfSoWPsYXpxvM5zr, rebuilt by `python3 tools/build_dashboard.py` from status.json
and republished with the Artifact tool through a general-purpose subagent (the host refuses a publish until the
live page has been read in full; the subagent does that read so it stays out of your context); docs/index.html
is the Pages copy. Take over the check-in: `list_triggers`, find the "Parent 7b check-in" one-shot, and re-arm
your own with send_later (30 minutes while any lane or worker runs, 90 otherwise) using the duty list in that
trigger's prompt with your session id. Post a ROOM.md line "parent 7c: took over from 7b at <time>". Then do
the duties when the trigger fires and otherwise wait for the owner. If any session reads `rejected`: interrupt
every live lane and worker, post "rejected at <time>: every lane stops" in ROOM.md, note it in BUDGETS.md, and
re-arm for Sat 26 Sept 2026 13:00 UTC. Live lanes on 25 Sept 2026 from 15:39 UTC: LANE R6 session_018MWpKL71WnBxA8k4ejVkBS, LANE V6 session_01V2BHwhVh1k72qSYuBFCyGd, LANE B2 session_01NS12APP1R55K6TGZrBbP97 (caps and briefs in hub-seed/ASSIGNMENTS.md; common rules in .claude/briefs/runs/2026-09-25-lanes-7b-COMMON.md). The other account's parent is session_01FXDfYR3CvGk7tcid1Aav1n; its lanes are closed until its window resets about 05:00 UTC 26 Sept; coordinate only through ROOM.md and STATUS.md. Your own hand-over point is 750k context: update this file
and the Parent handoff, then stop.
```
