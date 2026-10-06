# WVO-APPLY (account 1, for account 3) -- wvo-hessen-1564: rebuild key per the owner's settled f.23 signs

Model Opus 5.5. Cap $3 (2 units at ~$1.2 + margin), box 40 min; stop before a unit that would cross 80% of either.
Lane brief: .claude/briefs/default-lane.md (common tail applies). Claim in ROOM.md first (`tools/room.py`).

Input (done by the account-3 orchestrator, 6 Oct 2026 23:4x UTC, committed):
- The owner finished the "Orange 1564 Sign Sorter" (f.23). Applied with `tools/sign_sorter_apply.py`:
  `ciphers/wvo-hessen-1564/sorter/settled_labels.tsv` (258 tiles: 165 kept, 83 moved, 6 aside, 4 bad-cut; 28 piles -> 48
  signs incl. 23 owner-made piles, many of 1-3 tiles), `sorter_summary.json`, `recuts.tsv` (44 recuts) and
  `signs_recut.tsv` (`tools/sorter_apply_recuts.py`, boxes only). Raw db export in `sorter/db/`.
- Strips were rebuilt 6 Oct with 130 px bottom pad (tops unchanged, so tile coordinates are unchanged).

Unit 1 -- key: NOTES.md's next step ("rebuild key.tsv per settled sign and settle the uncertain gloss letters
against it"). Map each settled sign to the existing gloss/key values (the 57/53 M reductions already in NOTES.md); a
settled sign that unites tiles carrying different gloss letters, or a gloss letter split over two settled signs, is a
finding to list, not to smooth. Singleton owner piles (1 tile) are held M unless a gloss reads them. Write key.tsv
and run `tools/decode_key.py ciphers/wvo-hessen-1564 --check`; paste output.
Unit 2 -- grade counts per rule 4 (H/C/S/M/I) before vs after, depth per rule 4a via `tools/depth_check.py`, update
NOTES.md (gaps/escalation, `tools/gaps_check.py` passes), PROGRESS.tsv row for August 1561-64 / WVO if it exists.
Do not run the crib-placement test or any new family; name it as next step with a cost.
Report counts, what changed, and where nothing changed. Do not classify novelty.
