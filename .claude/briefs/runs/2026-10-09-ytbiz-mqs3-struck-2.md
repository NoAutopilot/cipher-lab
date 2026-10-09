# MQS-STRUCK-2 (LANE MQS-3, account 4) -- job brief

Written 9 Oct 2026 (clock read 10:1x UTC by date -u) by the LANE MQS-3 orchestrator (account 4,
session_01An6QVEiGnTrULNnQG5xqvG). Lane brief: `2026-10-09-acct3-mqs-lane.md`; research row: `research/MARY-STUART-TALK-2026-10-09.tsv`.

- **Model, cap, box:** Opus 5.5, cap USD 3, box 80 min. Stop at the cap; at 80% of the box do not start a new unit.
- **Row:** M44 (second half; MQS-STRUCK e01966990 built decode_key.py X{struck} / {over=OLD>NEW} / --corrections and left these two parts).
- **Goal:** `tools/sign_sorter_apply.py`: a sorted pile or a per-box mark can carry the token state `struck` or `over=OLD>NEW`, written into the labels/pass TSV in the same state column decode_key.py now reads (read decode_key.py's MQS-STRUCK docstring first; do not change its format). `tools/decipher_sheet.py`: the reading sheet shows a struck sign as a callout (shown, bracketed, not decoded) and an overwrite as OLD>NEW, in dark ink with a text label, never by colour alone (`tools/cvd_check.py` passes on the render).
- **Known answer and gate (pre-register in `tools/tests/PREREG-MQS-STRUCK-2.md`, pushed before any control runs):** a fixture sorter export with planted struck and overwritten boxes round-trips through sign_sorter_apply -> decode_key --corrections final|original -> decipher_sheet: every planted state reaches the sheet (gate 10/10 planted) against a null where the state column is dropped or row-shuffled (the callout count or position must differ); existing sorter/sheet tests unchanged. Known answer is synthetic plus at most one already-read control folder that decipher_sheet already renders (Gramont or Danzay; never Birago 1572, ASKS 118).
  Say in one line why the null can fail differently from the known answer for the statistic computed (rule 3). A control
  that misses its gate ships the option `weak` with both numbers; nothing is run on a target from it; it is not re-briefed.
- **Files:** `tools/sign_sorter_apply.py`, `tools/decipher_sheet.py`, their tests; the PREREG file; `tools/data/tool_shelf.tsv` rows and `SYSTEM.md` (append and rebase). No status,
  key, reading or AUDIT.md change anywhere; nothing from ciphers/debosnys-1883 or the private repository; no Birago 1572
  family value-bearing page for the owner while ASKS 118 is open. No host.
- **Credit (rule 8):** Lasry, Biermann and Tomokiyo 2023 (Cryptologia 47:2); CTTS (Apache-2.0) where its design is followed.
- **Common rules:** as in `2026-10-09-acct3-mqs-sheets.md` ("Common rules"), with this job's name MQS-STRUCK-2 and "for LANE MQS-3
  (account 4)" in your ROOM lines. Do not edit CLAUDE.md or `.claude/briefs/README.md`: give your one Registration line in
  the final report and in your ROOM done line. Done line names: option, control vs null, shelf grade, commit.
