# MQS-PILE-REGISTER (LANE MQS-3, account 4) -- job brief

Written 9 Oct 2026 (clock read 10:1x UTC by date -u) by the LANE MQS-3 orchestrator (account 4,
session_01An6QVEiGnTrULNnQG5xqvG). Lane brief: `2026-10-09-acct3-mqs-lane.md`; research row: `research/MARY-STUART-TALK-2026-10-09.tsv`.

- **Model, cap, box:** Opus 5.5, cap USD 3.5, box 100 min. Stop at the cap; at 80% of the box do not start a new unit.
- **Row:** M05 + M32 (letters held, known and referenced-but-missing; a per-pile register and timeline; paper App. C pp.200-202, Figs 17, C25-C26; Bossy 2001).
- **Goal:** `tools/pile_register.py`: one register per pool built on `tools/holder_export.py`'s row builder (import it; no second parser): held letters from status.json / folder files, plus a `referenced` class from a references TSV (letter A mentions a letter of date D not held), and a text timeline. A `--refs-scan EDITION.txt --dates` step greps a recipient's edition text on disk near each held letter's date for 'your letter of', 'ma lettre du' etc. as leads.
- **Known answer and gate (pre-register in `tools/tests/PREREG-MQS-PILE-REGISTER.md`, pushed before any control runs):** known answer: a pool on disk whose edition text already lists letters by date (choose one, name it, prior_work.py step pasted); hold out K referenced letters and score recall of the refs-scan against a date-shuffled null. A register with no scan control is plumbing (controlled-only at best).
  Say in one line why the null can fail differently from the known answer for the statistic computed (rule 3). A control
  that misses its gate ships the option `weak` with both numbers; nothing is run on a target from it; it is not re-briefed.
- **Files:** `tools/pile_register.py` (new), its test, SYSTEM.md row; the PREREG file; `tools/data/tool_shelf.tsv` rows and `SYSTEM.md` (append and rebase). No status,
  key, reading or AUDIT.md change anywhere; nothing from ciphers/debosnys-1883 or the private repository; no Birago 1572
  family value-bearing page for the owner while ASKS 118 is open. No host.
- **Credit (rule 8):** Lasry, Biermann and Tomokiyo 2023 (Cryptologia 47:2); CTTS (Apache-2.0) where its design is followed.
- **Common rules:** as in `2026-10-09-acct3-mqs-sheets.md` ("Common rules"), with this job's name MQS-PILE-REGISTER and "for LANE MQS-3
  (account 4)" in your ROOM lines. Do not edit CLAUDE.md or `.claude/briefs/README.md`: give your one Registration line in
  the final report and in your ROOM done line. Done line names: option, control vs null, shelf grade, commit.
