# PREREG-COL26-1181 (account 4, LANE DEFAULT-A4-0437-15, 15 Oct 2026, written 05:1x UTC before any score)

Job: COL26-1181, `.claude/briefs/runs/2026-10-15-acct4-default-0437-jobs.md`. Script: `siblings/c1181_try.py` (docstring = full
run list; pushed with this file before its first run). Disk only, no host, no vision call. Prior work: `tools/prior_work.py` has no
per-code item spec (`code` not an accepted key); the per-code step's only prior is COL26-KEY (NOTES.md, PREREG-COL26-KEY.md,
siblings/c50_keyrev_out.txt), which tested the 15 candidates as a unit and named this test.

- **Instrument:** `tools/decode_key.py --try` (MQS-CROSSWORD) on key_f23.tsv (11 = n M, 81 = il M now), streams = f23, c50 and the
  key_f23-family sibling units (c32, c33, c3536, c3940, c4749, c5456, c6263, c51). Its per-code controls are built in: null 1
  (shuffled-position pseudo-code with the same current value, 200 draws) and null 2 (the code's own positions read as random
  values of the hypothesis's class); its verdict rule (accept / reject / undecided) is used unchanged.
- **Primary:** the verdict on the **held-out** streams (all but c50, the unit the candidates came from) under `tools/data/fr17`
  (era-matched, 1617-1644 French). Secondary, reported only: c50 alone, all streams, and fr16.
- **Runner-up:** the code blanked, `--words re,me,ble,il,de`, held-out, fr17; reported, not gating.
- **Value-class control (licence for S):** the 5 key_f23 C codes with 2-letter values (16 se, 28 la, 33 ux, 36 ez, 51 de), each
  set to one letter ('e', or 'a' for ez) to mimic the target's single-letter current values, all streams, fr17: true value tried
  (5) and each other control value tried (20). Control passes if true accepted >= 4/5 and false accepted <= 2/20.
- **Grades written to key_f23_c50rev.tsv `rev_grade` only:** held-out accept AND control pass -> S; held-out accept, control fail
  -> M (note "per-code --try accept, value-class control failed"); undecided -> M (note); reject -> '-' (candidate dropped).
  key_f23.tsv, decode.json and readings unchanged; no C or H from this test.
