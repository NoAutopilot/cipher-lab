# RETIRED-REOPEN (parent worker for orchestrator (account-4); Opus 5.5; cap 6, box 75 min; 9 Oct 2026 19:1x UTC)

Owner, 9 Oct 2026: every retired step is noted somewhere we can return to. RETIRED.tsv (tools/retired.py, 208 rows) now exists,
but `python3 tools/retired.py --check` lists 88 rows whose reopen_when reads `not stated` (the owner cannot return to a step that
names no reopen condition) and some rows whose step/instrument cells are parse residue ("the instrument", "Result", "B 5/7)").

Do, without editing any file under ciphers/ (the folders are other lanes'):
1. Add to `tools/retired.py` an overrides file `tools/data/retired_overrides.tsv` (columns: source, step, instrument, reopen_when,
   note, set_by, date) merged by `source` (file:line) when the register is built; a row's override cells replace the parsed cells;
   `--check` passes when every row has a reopen_when that is not `not stated`. Offline test for the merge (tools/tests/test_retired.py).
2. For each of the 88 `not stated` rows and each row with parse residue: read the source line and the 40 lines around it in the
   folder's NOTES.md (and its HYPOTHESES.md row if the line cites one), and write the override from what the record itself
   says -- the real step, the instrument named, and the reopen condition the text gives (a different instrument, new material,
   a better image, owner tiles, a named ASKS row, a person's count). Where the record gives none, write reopen_when =
   "unknown: none recorded at retirement (<date>); reopens only on new material or a different instrument (rule 5)" so the
   register is explicit, never a guess at what the retiree meant. set_by = RETIRED-REOPEN, date by `date -u`.
3. Regenerate RETIRED.tsv, run `--check` (must pass), run the tests, system_map_check and file_shrink_guard on every file touched;
   paste all in the done line with the count of overrides written and how many carry "unknown: none recorded".
ROOM claim first ("for orchestrator (account-4)", cap, box end by date -u), halfway line, done line at the end; then
python3 tools/work_queue.py --done RETIRED-REOPEN --note "<counts>", git add by path, commit, git pull --rebase origin main,
git push origin HEAD:main. Never AskUserQuestion; never print credentials; stage by path; never force-push; never edit a target
folder's files; never the words solved, cracked, novel, first, new for anything this project did.
