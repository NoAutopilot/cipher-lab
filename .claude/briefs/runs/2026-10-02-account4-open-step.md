# OPEN-<target>: run one named cheap step on an open target whose intake gate passes (one target per worker)

Written 2 Oct 2026 02:4x UTC (clock read) by the account-4 parent (session_01SEzoee67SivPooFpTkxMme). The session's
prompt names the target, the step verbatim (from the folder's own NOTES.md "While waiting" / next-step text or NEAR.md
row), the cap, the hosts allowed and the vision-call count. Role field: `OPEN-<target> (account-4)`. Model: Fable 5.1
(Opus 5.5 if Fable fails). Box: 45 minutes. Stop before any unit that would cross 80 pct of cap or box.

1. `python3 tools/room.py --start`; last 30 ROOM.md lines; stop with `blocked` if another account claims the target in
   the last six hours; claim line. `python3 tools/intake_gate_check.py <target>` -- paste the line; it exited 0 for every
   target in this wave on 2 Oct 2026; a nonzero exit now means stop with a `blocked` line.
2. Run exactly the named step. Good-citizen rule on every host: one request at a time, >= 1.5 s apart, at most the
   count the prompt names, stop on any 403/429/challenge and log it; fetched text goes to disk once with a manifest
   line. Rule 3: any statistic carries its matched control beside it; rule 4: any token value is graded; rule 10: never
   new/first/unpublished -- "not found in <source> by <method> on 2 Oct 2026" is the sentence.
3. NOTES.md: a dated section "## OPEN-<target> (2 Oct 2026, account-4)" with the result in numbers and ONE named next
   step with its cost; if the folder has a "## While waiting" section, tick or update the bullet you ran. Status word
   unchanged unless the step finds the item already read in public (then `found-solved`, line 2 names the source, and
   the done line says any later reading is N0). A reading that clears a judge AND the shuffled-target check gets a
   "reading ready" ROOM line for a separate verifier, never a status change by you.
4. Commit by explicit path, rebase, `python3 tools/restricted_guard.py --outgoing`, push to main; done line with the
   numbers and the request count per host. Stop; no second step.

The common tail of `.claude/briefs/README.md` applies in full.
