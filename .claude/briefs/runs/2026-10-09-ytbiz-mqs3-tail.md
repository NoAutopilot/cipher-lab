# MQS-TAIL (LANE MQS-3, account 4) -- job brief

Written 9 Oct 2026 (clock read 10:1x UTC by date -u) by the LANE MQS-3 orchestrator (account 4,
session_01An6QVEiGnTrULNnQG5xqvG). Lane brief: `2026-10-09-acct3-mqs-lane.md`; research row: `research/MARY-STUART-TALK-2026-10-09.tsv`.

- **Model, cap, box:** Opus 5.5, cap USD 3, box 90 min. Stop at the cap; at 80% of the box do not start a new unit.
- **Row:** M23 (month, date, place and enclosure-mark symbols as one positional class; paper p.124-125 Fig. 12, p.137 n.99).
- **Goal:** `tools/freq.py --tail N`: per sign, its rate in the last N tokens of each letter of a pool against a shuffled-letter-end null (the end of letter i swapped for a random window of the same length elsewhere in the pool), ranking signs that concentrate in closing lines (date, place, sign-off).
- **Known answer and gate (pre-register in `tools/tests/PREREG-MQS-TAIL.md`, pushed before any control runs):** Janssens pool, `ciphers/na-janssens-java-1811/key.tsv` (1089 Juillet C n=4, 845 Juin C, 43 mars C, 547 aoust M; datelines 'neuf Juillet', 'trente Juin'): pre-register that the month codes rank in the top K (state K) against the null's p95; no planting needed. Second, mismatched cell: a pool without datelines in cipher (pick one from disk, state it) must not rank month codes. Report both numbers.
  Say in one line why the null can fail differently from the known answer for the statistic computed (rule 3). A control
  that misses its gate ships the option `weak` with both numbers; nothing is run on a target from it; it is not re-briefed.
- **Files:** `tools/freq.py` (the `--tail` option only; TOOLS-TOMO's options unchanged), its tests; the PREREG file; `tools/data/tool_shelf.tsv` rows and `SYSTEM.md` (append and rebase). No status,
  key, reading or AUDIT.md change anywhere; nothing from ciphers/debosnys-1883 or the private repository; no Birago 1572
  family value-bearing page for the owner while ASKS 118 is open. No host.
- **Credit (rule 8):** Lasry, Biermann and Tomokiyo 2023 (Cryptologia 47:2); CTTS (Apache-2.0) where its design is followed.
- **Common rules:** as in `2026-10-09-acct3-mqs-sheets.md` ("Common rules"), with this job's name MQS-TAIL and "for LANE MQS-3
  (account 4)" in your ROOM lines. Do not edit CLAUDE.md or `.claude/briefs/README.md`: give your one Registration line in
  the final report and in your ROOM done line. Done line names: option, control vs null, shelf grade, commit.
