# BLZ-FR: blitz-ciphers -- homophonic family on one more corpus-backed language (NEAR.md's named step (a))

Written 1 Oct 2026 23:4x UTC (clock read) by the account-4 parent (session_01SEzoee67SivPooFpTkxMme).
Role field for every ROOM.md line: `BLZ-FR (account-4)`. Model: Fable 5.1 (Opus 5.5 if Fable fails). Cap: USD 4.
Box: 40 minutes. No vision, no network. Disk only.

## The job, in one line

NEAR.md row blitz-ciphers, "What would settle it": "(a) homophonic on one more corpus-backed language (fr18 or la) at
N=581, USD 3". Run `tools/family_run.py specs/blitz-ciphers.json --family homophonic` with the control FIRST on
French (tools/data/fr18) and, if the box allows, Latin (tools/data/la18 or la_repo -- read tools/data/README.md for
which is the judge corpus), case-as-information K=48 as bBLZ6 did for German (read NOTES.md's bBLZ3/bBLZ6 sections and
the spec's `cheap_test_done` rows for the exact parameters used, and match them).

## Steps

1. `python3 tools/room.py --start`; read the last 30 ROOM.md lines; claim line.
2. `python3 tools/intake_gate_check.py blitz-ciphers`; paste its output in NOTES.md. A nonzero exit stops the job with
   a `blocked` ROOM line and nothing else.
3. Per language: control first (`--seeds 3`, the spec's N and K, `--corpus tools/data/fr18` etc.), gate 0.6; the
   target runs only if the control clears. The judge: the spec's judge block says `language: en`; run
   `tools/judge_plaintext.py` on the family's best decode with the matching French/Latin corpus so the FAIL/PASS is
   against the right language (if `family_run.py` has no way to override the judge corpus per run, add the smallest
   option that does it -- with an offline test in tools/tests/ -- rather than a private script, CLAUDE.md Usage 8;
   if that would exceed the cap, run the judge by hand and say so). Report, per language, control mean (range),
   target judge score vs real_p05 and null_p99, and the shuffled-target decode's judge score (the ARM-C1 check: a
   PASS on the shuffled target voids the judge for that family at this N).
4. Append one HYPOTHESES.md row per run (family_run does this); write a dated NOTES.md section
   "## BLZ-FR (1 Oct 2026, account-4)" with the numbers side by side and the reading in rule-3 terms (control-backed
   negative / non-test / candidate). Add a `cheap_test_done` row to the spec for this step. Update the NEAR.md row's
   evidence cell with one sentence and its "Last touched"; run `python3 tools/near_check.py`. The status word stays
   `open` (NEAR target: never `closed-negative`).
5. Commit by explicit path, rebase on origin/main, `python3 tools/restricted_guard.py --outgoing`, push to main. Done
   line with both numbers per language. Stop; do not start the pages 1-6 glyph key or any other step.

The common tail of `.claude/briefs/README.md` applies in full. Rule 10 wording only.
