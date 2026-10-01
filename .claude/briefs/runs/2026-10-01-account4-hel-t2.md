# HEL-T2: hellen-frederick-1752 -- the spec's test 2 (homophonic/nomenclator anneal on the pooled 1763 cluster, fr18 judge)

Written 1 Oct 2026 23:5x UTC (clock read) by the account-4 parent (session_01SEzoee67SivPooFpTkxMme).
Role field for ROOM.md lines: `HEL-T2 (account-4)`. Model: Fable 5.1 (Opus 5.5 if Fable fails). Cap: USD 4. Box: 40
minutes. Disk only: no network, no vision.

## The job, in one line

`specs/hellen-frederick-1752.json` `cheap_tests_in_order[1]` (test 2), which ZX2-HEL (25 Sept 2026) left gated on an
era-matched French corpus that now exists (`tools/data/fr18`, the spec's own judge block): run the matched control
FIRST, then the target only if the control clears the gate, through `tools/family_run.py`, and write both numbers into
the spec's `cheap_test_done["2"]`, HYPOTHESES.md and NOTES.md.

## Steps

1. `python3 tools/room.py --start`; last 30 ROOM.md lines; claim line.
2. `python3 tools/intake_gate_check.py hellen-frederick-1752`; paste the output in NOTES.md. Nonzero exit: stop with a
   `blocked` ROOM line (the verdict needs a check-solved worker, not you).
3. Read NOTES.md "ZX2-HEL: pool" and the spec's test-2 text for the exact pooled stream (the six 1763 records, 1234
   numeric tokens) and K. Run `python3 tools/family_run.py specs/hellen-frederick-1752.json --family homophonic
   --param profile=target --seeds 3 --corpus tools/data/fr18` (check `--help` and `--dry-run` first for how the spec's
   pooled ciphertext is addressed; `--cipher PATH` if the spec's `ciphertext` block needs one pooled file -- build it
   with a small script in the folder, never by hand). If K is far above what a homophonic control can read at this N
   (BER-HOMO, 27 Sept 2026: N=325/K=207 was a non-test), the expected result is CONTROL BELOW GATE; that is a logged
   non-test, not a negative -- say so and name `--family nomenclator` as the next instrument (run it too if the box
   allows and the control clears; `--family nomenclator --help` text first).
4. Record: a `cheap_test_done["2"]` entry in the spec (date, worker, method, control mean/range, target judge line or
   "target not run: CONTROL BELOW GATE"), the HYPOTHESES.md rows family_run writes, a dated NOTES.md section
   "## HEL-T2 (1 Oct 2026, account-4)". Status word stays as it is. If a judge PASS appears, run the ARM-C1 check
   (`--shuffle-target`) before writing anything else, and post "reading ready" ONLY if the shuffled decode FAILs.
5. Commit by explicit path, rebase on origin/main, `python3 tools/restricted_guard.py --outgoing`, push to main. Done
   line with both numbers. Stop; no test 3, no sibling sweep.

Rule 10 wording only. The common tail of `.claude/briefs/README.md` applies in full.
