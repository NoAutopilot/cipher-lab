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

> Wall-clock box (every worker brief): "stop and push at $<cap> or at <minutes> minutes, whichever first." The box is also a minimum: a worker does not stop early with the job undone while budget and minutes remain; it stops at the cap, at the minutes, or at the brief being met, and says which (LEARN-2026-09-25-1718 item 2, from the R6 common brief).

> Before the first action, also read the last 20 lines of UPDATES.md (changes instituted across both accounts since your brief was written; they override an older brief where they conflict).

**Spawning a session (parent or lane orchestrator, 25 Sept 2026, RETRO-2026-09-25l).** Every `create_session`
call passes `source_url` and `source_revision` explicitly, and the prompt opens with the brief file's path and
the one-line reason the job exists, before any cap or rule text -- see `.claude/briefs/parent.md`'s "Opening a
lane" section for the wording and the incident (three sessions this window stopped at their first turn on a
missing repository source and an injection-suspicion trip). A lane orchestrator spawning its own Sonnet workers
follows the same convention.

**Sizing a unit-loop brief's box (25 Sept 2026, RETRO-2026-09-25l).** When a job loops over discrete same-shaped
units (a native-resolution crop fetch, an eye-bisected token comparison, a full control+target `family_run.py`
pair), a round-number wall-clock box can be crossed from well under to well over in the single step of starting
one more unit: R7-AT55V (13 Gallica native crops) ran 1.23x its $6 cap, R7-MEYE (122 eye-bisected tokens) ran
1.86x its $2.50 cap, GOLD-K2 (a family-variant sweep) jumped from about 56% to 89% of its 75-minute box starting
one more ~25-minute control+target variant. Size the cap and the box from (planned unit count x a per-unit
cost/time estimate drawn from the nearest comparable ledger row) plus one unit of margin, state the unit count
and the per-unit estimate in the brief itself, and have the worker stop before starting a unit that would cross
80% of either figure -- not only after aggregate elapsed time crosses 80%, which one large unit can jump past in
a single step. See CLAUDE.md Usage item 6 for the full incident and the subagent-level precedent (GOLD-4D) this
extends.

**Copying a COMMON file forward (26 Sept 2026, LEARN-2026-09-26-0022/-0058).** A new lane's `-COMMON.md` is
drafted by copying the previous lane's forward; the "Cost and time" paragraph got pasted in twice, back to
back, in six files (cx, cx2, yx, zx, zx2, ax) before anyone caught it by eye. Run
`python3 tools/tests/test_common_briefs.py` after copying a COMMON file forward and before committing it; it
exits non-zero and names the file if any paragraph appears twice.

## The consolidator pattern, for standing campaigns

A target that has run more than two `tools/family_run.py` families is a standing campaign, not a one-shot job, and
gets a periodic strongest-model "consolidator" check-in: it reads the last cycle's workers' control and target
numbers side by side, rewrites the target's HYPOTHESES.md summary block, and decides continue / pivot / park per
family against a pre-written decision rule (written the cycle before, not moved after seeing the new numbers), then
writes the next cycle's job briefs. Worked example: `.claude/briefs/runs/2026-09-25-lane-gold-consolidator-c2.md`
(LANE GOLD cycle 2, Fable) -- three Sonnet workers' family_run.py rows read together, the cycle-1 decision rule
applied unchanged, and three named cycle-3 briefs written from it.
- A credential you need and the container lacks: `python3 tools/key_request.py NAME --purpose "..." --tool tools/x.py --by "<you>"`
  files it (KEYS.md, ASKS.md, ROOM.md); the owner adds it on both accounts; a later fresh session announces it in ROOM.md. Do the
  part of the job that does not need it and stop; never ask for a value in chat, never print one.
