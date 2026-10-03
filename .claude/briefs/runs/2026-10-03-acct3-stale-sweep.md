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
