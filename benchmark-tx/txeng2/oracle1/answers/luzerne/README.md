# L74 box check, La Luzerne 1781 p.1 (luzerne108a-p1): the owner's answers

Read 10 Oct 2026 about 18:0x UTC (date -u) by the account-3 parent from the artifact database of the page the owner worked
on: https://claude.ai/artifact/Cq5vxXXMJ552jZW1K3kbgY (account 3; the same 445 boxes as the account-4 page
6AUbkHX1JxhYSp2QzHQ2kj, built from benchmark-tx/txeng2/oracle1/sorter/oracle_boxes_luzerne.html, with the owner's gesture
rule R05 and a step-2 "Fix the cut" button added; see LOCAL-QUEUE L74). Owner's word: "Oracle boxes (luzerne): done".
Blind: the page shows boxes only, no value, label or machine guess; nothing here was read by a model.

## What was answered
- The 83 boxes the build flagged (focus.tsv, step 2, one at a time): all 83 answered, none left.
  57 kept in "sign box" (25 of them with the box re-cut first), 25 trashed as not a sign (NOT-LETTER), 1 marked bad cut.
  No split and no added box (db collections `added` and `clusters` empty).
- The other 362 boxes (not flagged) carry no answer of their own: the apply tool counts them "kept" because they stayed in
  their pile. Whether the owner looked them over in step 1 is asked of him (10 Oct 18:0x UTC); until he says so, treat them
  as machine boxes not individually confirmed (ORACLE-LOCATION-1 wants every line checked by a person).

## Time (from the database's own save stamps)
First answer 17:10:38, last 17:56:31 UTC: 45.9 min wall. One pause of 25.1 min (17:11-17:36) is the page being fixed
(step 2 had no Fix the cut until about 17:3x; the owner reported it); two more of 6.4 and 5.7 min. Without the 25.1 min
pause: about 20.8 min for 83 flagged boxes, so about 25 min per 100 flagged boxes. These are the boxes the machine doubted
(the hardest ones), not "100 signs" of the line: it is not the L74 minutes/100 signs figure until the owner says how much of
the rest he checked.

## Files
- `db/` the database as read (ArtifactData list per collection: checked, moves, recuts, piles, newpiles; added and clusters
  empty).
- `settled.tsv`, `summary.json`, `recuts.tsv` from
  `python3 tools/sign_sorter_apply.py --labels benchmark-tx/txeng2/oracle1/sorter/luzerne/labels.tsv --db <this>/db --out
  <this>/settled.tsv --summary <this>/summary.json --recuts-out <this>/recuts.tsv --added-out <this>/added.tsv`
  (no added.tsv is written: nothing was added). Re-cut boxes are not yet applied to signs.tsv (tools/sorter_apply_recuts.py,
  the lane's step).
