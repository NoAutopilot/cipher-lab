# Breadth worker (LANE B)

Spec: `specs/<slug>.json`. Run `cheap_tests_in_order[0]` and its matched control, nothing else. If test 1 is a bare
IC/frequency statistic rather than a `family_run.py` family, read `specs/README.md`'s "Ordering
cheap_tests_in_order" paragraph first (25 Sept 2026, RETRO-2026-09-25l) -- at N>=150-200 that statistic usually
lands inside more than one candidate family's control band and settles nothing (bBLZ, 25 Sept), where the
cheapest applicable `family_run.py` family returns a categorical PASS/FAIL instead; below that length, say so
in the spec rather than re-running IC. Write both
numbers into the spec's `cheap_test_done` (with date, method, cost). Judge any candidate plaintext with
`tools/judge_plaintext.py` and paste its output. Cap $3, or $6 if the first test needs an image fetch plus a
two-pass transcription (never both a subagent pass B and a fetch in the same $3 job -- RETRO-2026-09-25j: bMOU ran
$7.61 on the flat $3 cap this way, 2.5x over, while every disk-only first test that window landed at $1-2.31). Report
in five lines; do not run test 2.

**Before re-scouting, score what is already scouted (25-26 Sept 2026, RETRO-2026-09-26a).** UNSOLVED-SURVEY ranks
31-41 gave no spec (bSPEC3, 25 Sept 2026: all eleven are famous items with no untried cheap test, correctly parked
to the gold lane per Pipeline 3). Before opening a new scout pass, run the scout's scoring step over QUEUE.md's
own unscored rows from later passes (as of 25-26 Sept: SCOUT-RERANK, QUEUE.md "Re-rank for LANE B5", 26 Sept 00:03,
has already ranked the github-held and scPOOL rows -- the VX-*/KX-*/KT-*/PX-* families are still unscored) into
QUEUE-scores.json and rank alongside 1-41 -- several are recovery-kind with a key or sibling decipherment already
beside the ciphertext, which Pipeline 3's selection rule ranks above a fresh cryptanalysis candidate of equal
novelty. A B5 brief opens from that combined ranking, not from a bare re-run of the scout pass that produced
ranks 1-41.

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
