# GAPS-<target>: run the one cheapest step named in a partial target's "## Remaining gaps" Verdict line (one target per worker)

Written 2 Oct 2026 01:5x UTC (clock read) by the account-4 parent (session_01SEzoee67SivPooFpTkxMme), on account-3's
nomination (ROOM.md 00:52 and 01:26 UTC 2 Oct): the finish-or-blocker pass of 1 Oct 2026 appended a "## Remaining gaps
(finish-or-blocker pass, 1 Oct 2026)" section to each partial target's NOTES.md whose Verdict line names the cheapest
next step and its cost; account-4 runs that step on the twelve partial targets not queued to account 2 (NEXT-* rows in
WORK-QUEUE.tsv). The session's prompt names the target, the Verdict step verbatim, the cap and the vision-call count.
Role field for ROOM.md lines: `GAPS-<target> (account-4)`. Model: Opus 5.5 (owner, 2 Oct 2026: nothing below Opus 5.5 -- this includes every subagent the worker spawns; FT4-rousseau used a Sonnet subagent on 3 Oct, do not). Box: 60 minutes. Cost: a native Opus vision pass has cost USD 3.5-10 (3 Oct 2026 ledger); the prompt states the vision-call count and per-pass rate.
Stop before any unit that would cross 80 pct of the cap or the box, push what you hold.

## Order of work

1. `python3 tools/room.py --start`; read the last 30 ROOM.md lines; if another account's line claims this target in
   the last six hours, stop with a `blocked` line. Claim line.
2. `python3 tools/intake_gate_check.py <target>`. If it exits 1 ONLY because no open-web and blog comment-thread check
   is logged (the 28 Sept 2026 CHECK-SOLVED-WEB step), do that step first, exactly as `.claude/briefs/check-solved.md`
   "Required step" and `.claude/briefs/runs/2026-10-01-account4-webcheck.md` describe (four plain web searches, the
   three blogs by name, every plausible hit's comment thread read, a section headed exactly
   `## Web and blog check (GAPS-<target>, 2 Oct 2026)` at the end of NOTES.md, rule 10 wording), re-run the gate and
   paste its output. A hit carrying a decipherment or plaintext of the item: status word -> `found-solved`, line 2
   names the source, stop there (no deep step), done line says any later reading is N0. If the gate exits 1 for any
   other reason, stop with a `blocked` line naming it. Budget for this stage: about USD 4.5 of the cap.
3. Read the target's "## Remaining gaps" section in full (its gap list, "## Escalation" if present, and the Verdict
   line). Run the Verdict line's cheapest step and nothing else -- not the second step it names, not a sibling, not a
   sweep. The rules that bind every step: rule 3 (a negative carries its matched control beside it; a control that
   cannot vary on the statistic's own axis is a non-test), rule 4 (every token graded H/C/S/M/I, counts given;
   S needs two words), rule 7 (any reading change re-runs the folder's `--check` script and it exits 0), rule 10
   (never new/first/unpublished; report what was found and where it was not found). Vision work: cut line crops with
   `tools/iiif_lines.py --image <file> --out <dir>` first, one page or crop set per subagent call, never a whole leaf
   to one call, at most the number of vision calls the prompt names.
4. Update the "## Remaining gaps" section IN PLACE (the gap you addressed gets its result and date; the Verdict line
   is rewritten to name the next cheapest step and cost, or "blocked on <ASKS row>" if nothing cheap remains), add a
   dated step section above it ("## GAPS-<target> (2 Oct 2026, account-4)") with the numbers, then run
   `python3 tools/gaps_check.py <target>` and paste its output.
   If the rewritten Verdict line is "blocked on <ASKS/LOCAL-QUEUE row>" or names a person, also write or refresh
   "## While waiting" with the one action that depends on nobody (WAIT-CHECK, 27 Sept 2026), then run
   `python3 tools/next_steps.py --wait-only | grep <target>` and paste the (empty) result; a non-empty result is
   a brief failure, not a done line (RETRO-2026-10-02-account4 proposal 4, applied 2 Oct 2026).
   Status word: stays `partial` (rule 5: never
   `closed-negative`; `found-solved` only per step 2; a reading that clears its judge AND the shuffled-target check
   gets a "reading ready" ROOM line for a separate verifier, never a status change by you). If the target has a NEAR.md
   row, add one sentence with the numbers and refresh its "Last touched"; `python3 tools/near_check.py`.
5. Commit by explicit path, `git fetch origin main && git rebase FETCH_HEAD`, `python3 tools/restricted_guard.py
   --outgoing`, `python3 tools/file_shrink_guard.py <every file touched>`, push to main. Done line: the step's result in
   numbers, the gate's exit code, vision calls used, request count per host. Stop.

The common tail of `.claude/briefs/README.md` applies in full. Never a cost figure of your own in a ROOM line.
