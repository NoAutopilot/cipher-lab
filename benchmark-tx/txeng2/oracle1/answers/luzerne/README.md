# L74 box check, La Luzerne 1781 p.1 (luzerne108a-p1): the owner's answers

Read 10 Oct 2026 about 18:0x UTC (date -u) by the account-3 parent from the artifact database of the page the owner worked
on: https://claude.ai/artifact/Cq5vxXXMJ552jZW1K3kbgY (account 3; the same 445 boxes as the account-4 page
6AUbkHX1JxhYSp2QzHQ2kj, built from benchmark-tx/txeng2/oracle1/sorter/oracle_boxes_luzerne.html, with the owner's gesture
rule R05 and a step-2 "Fix the cut" button added; see LOCAL-QUEUE L74). Owner's word: "Oracle boxes (luzerne): done".
Blind: the page shows boxes only, no value, label or machine guess; nothing here was read by a model.

## What was answered
- (First read.) The 83 boxes the build flagged (focus.tsv, step 2, one at a time): all 83 answered, none left.
  57 kept in "sign box" (25 of them with the box re-cut first), 25 trashed as not a sign (NOT-LETTER), 1 marked bad cut.
  No split and no added box (db collections `added` and `clusters` empty).
- The other 362 boxes (not flagged) carry no answer of their own: the apply tool counts them "kept" because they stayed in
  their pile. Whether the owner looked them over in step 1 is asked of him (10 Oct 18:0x UTC); until he says so, treat them
  as machine boxes not individually confirmed (ORACLE-LOCATION-1 wants every line checked by a person).

## Second pass: the 6 possible shadows (read 11 Oct 2026 00:0x UTC)
After the first read, 6 more boxes were added to step 2 as "Possible shadow ... A sign, or Trash?" (p1_L03_b042-b043,
p1_L04_b041-b044; see ../shadow/README.md). Owner's word: "Oracle boxes (luzerne): verify the cuts - done". Re-read the same
database: all 6 trashed (NOT-LETTER, saved 10 Oct 2026 23:56:20-23:56:25 UTC); nothing else changed (checked 57, recuts 25,
moves 26 -> 32). `db/`, `settled.tsv` and `summary.json` are regenerated from this read with the same command below.
Totals now: 89 boxes answered, 57 kept (25 re-cut), 31 trashed, 1 bad cut; 356 not individually asked.

## Time: not a measurement
The owner, 10 Oct 2026 about 18:1x UTC: "the timing isnt trustable cause i was multitasking". The save stamps (first answer
17:10:38, last 17:56:31 UTC, one 25.1 min pause while the page was being fixed) are kept in db/ but give NO minutes/100 figure
for this hand. ORACLE-LOCATION-1's annotation-minutes figure has to come from a hand timed single-task (Vivonne or Birago).

## Files
- `db/` the database as read (ArtifactData list per collection: checked, moves, recuts, piles, newpiles; added and clusters
  empty).
- `settled.tsv`, `summary.json`, `recuts.tsv` from
  `python3 tools/sign_sorter_apply.py --labels benchmark-tx/txeng2/oracle1/sorter/luzerne/labels.tsv --db <this>/db --out
  <this>/settled.tsv --summary <this>/summary.json --recuts-out <this>/recuts.tsv --added-out <this>/added.tsv`
  (no added.tsv is written: nothing was added). Re-cut boxes are not yet applied to signs.tsv (tools/sorter_apply_recuts.py,
  the lane's step).
