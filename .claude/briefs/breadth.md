# Breadth worker (LANE B)

Spec: `specs/<slug>.json`. Run `cheap_tests_in_order[0]` and its matched control, nothing else. Write both
numbers into the spec's `cheap_test_done` (with date, method, cost). Judge any candidate plaintext with
`tools/judge_plaintext.py` and paste its output. Cap $3. Report in five lines; do not run test 2.

Intake step (added 25 Sept 2026 18:14 UTC by LANE B2 after QA/2026-09-25-1740.md failure 3: bMOU, bKAL, bDEB and bPOL ran transcription/IC work with no check-solved verdict on file). Before the cheap test: if `ciphers/<slug>/NOTES.md` exists, run `python3 tools/intake_gate_check.py <slug>` and paste its output into your NOTES.md; exit 0 lets you proceed. Otherwise (no folder, or a nonzero exit) do a minimal check-solved first and write its verdict as NOTES.md lines 1-2 in the gate's format (status word on line 1; line 2 names what was read, with dates): the Cipherbrain post and its comment thread already on disk under sources/schmeh/, a grep of both solver repositories for the item (clone shallow, grep, delete), and one OpenAlex plus one Semantic Scholar query for the item's name with 'solved' or 'decrypted'. Re-run the gate; proceed only on exit 0, else stop with a `blocked` line and the reason. This step counts inside the cap.

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
> A negative's done line carries target and control numbers side by side, or it is not a negative.
