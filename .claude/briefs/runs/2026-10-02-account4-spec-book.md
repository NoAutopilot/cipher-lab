# SPEC-BOOK: write the already-run first tests into three specs' `cheap_test_done` (bookkeeping, no new test)

Written 2 Oct 2026 01:5x UTC (clock read) by the account-4 parent (session_01SEzoee67SivPooFpTkxMme).
Role field for ROOM.md lines: `SPEC-BOOK (account-4)`. Model: Fable 5.1 (Opus 5.5 if Fable fails). Cap: USD 3.
Box: 25 minutes. Disk only. Touch only the three spec files named below (never a ciphers/ folder: two of the three
targets are claimed by account 2 this hour).

## Why

The breadth lane (CLAUDE.md Pipeline 3a) reads `specs/*.json` `cheap_test_done` to know which first tests are unrun.
Three specs have no such field although their first test already ran on 25-26 Sept 2026, so they read as unrun:
- `specs/antt-msliv0638-brochado-1712.json` -- test 1 "decode letter 134 against the period key and report per-token
  C/M/U grades (YX-BRO79, 25 Sept 2026)": numbers in `ciphers/antt-msliv0638-brochado-1712/NOTES.md` (YX-BRO79,
  ZX-BRO2, AX-BRO3, AX2-BRO4/5, and NEXT-BRO of 2 Oct 2026: C 54 / M 12 / U 4, percentile 5.0 under pt17 and pt18,
  judge calibration on the volume's own glosses) and its HYPOTHESES.md.
- `specs/lodewijk-5797.json` -- test 1 "apply key.tsv to the 6 located missing-subject code clusters plus one
  Groen-clear positive-control run (AX-5797, 26 Sept 2026)": numbers in `ciphers/lodewijk-van-nassau-1573-74/NOTES.md`
  (AX-5797 section) and HYPOTHESES.md (grep 5797).
- `specs/rah-morillo-1817.json` -- test 1 "interlinear key recovery from the leaf's own gloss (NX-MOR2)": the spec's own
  `value` field already states the numbers (13 of 21 groups, shuffle-consistency real 1.000 vs shuffle mean 0.621,
  p95 0.800); V9-MOR's AUDIT.md later classed item 3 N0 (plaintext in print, Portuguesa en Carabobo 2021 p.37 n.100).

## The job

For each spec, add a `cheap_test_done` entry in the shape the other specs use (read `specs/antt-linhares-chave.json`'s
entry as the model: date, by, test, target numbers, control numbers, verdict, cost if recorded), copied from the
numbers already on disk with the section or job name that produced each number cited. Do not run any test, do not
reinterpret a result, do not change any other field. If a number cannot be found on disk, write "not recorded" for that
cell rather than inferring it. Validate each file with `python3 -c "import json;json.load(open('<spec>'))"`, run
`python3 tools/next_steps.py --check` (report its line, do not regenerate NEXT-STEPS.tsv), commit the three specs by
explicit path, rebase on origin/main, push to main. ROOM.md claim and done lines (`touching specs/<slug>.json`). Stop.
Rule 10 wording only. The common tail of `.claude/briefs/README.md` applies in full.
