# MQS-WITNESS-LABELS (LANE MQS-3, account 4) -- job brief

Written 9 Oct 2026 (clock read 10:1x UTC by date -u) by the LANE MQS-3 orchestrator (account 4,
session_01An6QVEiGnTrULNnQG5xqvG). Lane brief: `2026-10-09-acct3-mqs-lane.md`; research row: `research/MARY-STUART-TALK-2026-10-09.tsv`.

- **Model, cap, box:** Opus 5.5, cap USD 3.5, box 100 min. Stop at the cap; at 80% of the box do not start a new unit.
- **Row:** M28 (plaintext copies from printed editions diffed against the decipherment; the paper's n.70 criteria for 'sent in cipher', p.131).
- **Goal:** `tools/decode_witness.py --label-diffs`: each difference between a decode and a printed or clear witness is labelled (omission, addition, substitution, name/code, spelling-only after normalisation per rule 3's PX-BRODEC paragraph) instead of only reconciled; `tools/data/sent_in_cipher_criteria.tsv`, the n.70 criteria as a checklist (channel references, references to other cipher letters, hostile statements) with a scan option that flags a clear copy's sentences meeting them as a lead, never a verdict; shelf rows for `tools/stream_align.py`, `tools/gibbs_align.py`, `tools/hot_cold.py` (read each one's docstring and tests; grade only from evidence on disk, else `untested`).
- **Known answer and gate (pre-register in `tools/tests/PREREG-MQS-WITNESS-LABELS.md`, pushed before any control runs):** planted-difference control on an already-read decode with a printed witness on disk (Pisany kp86 or another named in LEDGER's RUN*-PIS* rows; prior_work.py step pasted): label accuracy on planted diffs vs a label-shuffled null; normalisation must not hide planted substitutions. The criteria scan is graded weak unless it has its own known answer. Give the check-solved line for pools in your Registration report (do not edit `.claude/briefs/check-solved.md`).
  Say in one line why the null can fail differently from the known answer for the statistic computed (rule 3). A control
  that misses its gate ships the option `weak` with both numbers; nothing is run on a target from it; it is not re-briefed.
- **Files:** `tools/decode_witness.py`, `tools/data/sent_in_cipher_criteria.tsv`, tests, shelf rows for the three aligners; the PREREG file; `tools/data/tool_shelf.tsv` rows and `SYSTEM.md` (append and rebase). No status,
  key, reading or AUDIT.md change anywhere; nothing from ciphers/debosnys-1883 or the private repository; no Birago 1572
  family value-bearing page for the owner while ASKS 118 is open. No host.
- **Credit (rule 8):** Lasry, Biermann and Tomokiyo 2023 (Cryptologia 47:2); CTTS (Apache-2.0) where its design is followed.
- **Common rules:** as in `2026-10-09-acct3-mqs-sheets.md` ("Common rules"), with this job's name MQS-WITNESS-LABELS and "for LANE MQS-3
  (account 4)" in your ROOM lines. Do not edit CLAUDE.md or `.claude/briefs/README.md`: give your one Registration line in
  the final report and in your ROOM done line. Done line names: option, control vs null, shelf grade, commit.
