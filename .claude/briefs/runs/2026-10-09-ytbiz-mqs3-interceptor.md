# MQS-INTERCEPTOR (LANE MQS-3, account 4) -- job brief

Written 9 Oct 2026 (clock read 10:1x UTC by date -u) by the LANE MQS-3 orchestrator (account 4,
session_01An6QVEiGnTrULNnQG5xqvG). Lane brief: `2026-10-09-acct3-mqs-lane.md`; research row: `research/MARY-STUART-TALK-2026-10-09.tsv`.

- **Model, cap, box:** Opus 5.5, cap USD 2, box 70 min. Stop at the cap; at 80% of the box do not start a new unit.
- **Row:** M45 (search the intercepting power's archive for the key and the decipherers' copies; paper p.108-109 TNA SP 53/22, p.188 n.332 BL Harley 1582).
- **Goal:** `tools/data/interceptor_depots.tsv` (power, period, depot series, what it holds, source) seeded from paper, KEY-OFFICES.tsv and KEYHUNT-2026-10-07.tsv only (no network), and a `tools/prior_work.py --interceptor` check that, for a pile with a probable recipient power and date, lists the depots to log as searched families (prints; never marks searched itself).
- **Known answer and gate (pre-register in `tools/tests/PREREG-MQS-INTERCEPTOR.md`, pushed before any control runs):** known answer: the Mary Stuart case (SP 53 / Harley 1582 for England 1586) and two KEYHUNT rows whose key was found in an interceptor's depot must be listed; a mismatched power/date must not list them. Plumbing: shelf at most controlled-only.
  Say in one line why the null can fail differently from the known answer for the statistic computed (rule 3). A control
  that misses its gate ships the option `weak` with both numbers; nothing is run on a target from it; it is not re-briefed.
- **Files:** `tools/data/interceptor_depots.tsv`, `tools/prior_work.py` (the `--interceptor` option only), tests; the PREREG file; `tools/data/tool_shelf.tsv` rows and `SYSTEM.md` (append and rebase). No status,
  key, reading or AUDIT.md change anywhere; nothing from ciphers/debosnys-1883 or the private repository; no Birago 1572
  family value-bearing page for the owner while ASKS 118 is open. No host.
- **Credit (rule 8):** Lasry, Biermann and Tomokiyo 2023 (Cryptologia 47:2); CTTS (Apache-2.0) where its design is followed.
- **Common rules:** as in `2026-10-09-acct3-mqs-sheets.md` ("Common rules"), with this job's name MQS-INTERCEPTOR and "for LANE MQS-3
  (account 4)" in your ROOM lines. Do not edit CLAUDE.md or `.claude/briefs/README.md`: give your one Registration line in
  the final report and in your ROOM done line. Done line names: option, control vs null, shelf grade, commit.
