# RETIRED-REGISTER (parent worker for orchestrator (account-4); Opus 5.5; cap 3, box 45 min; 9 Oct 2026 18:5x UTC)

Owner, 9 Oct 2026 (11:4x am PT): "for those that are retired, just make sure that we're noting it somewhere, so if we want to
return to it later, we can." Today retired steps live only inside each target folder (NOTES.md "## Remaining gaps" lines marked
`[retired]`, HYPOTHESES.md rows marked untested-by-this-tool) and, for transcription families, in research/TX-REGISTER.tsv
(verdict `retired`). There is no one place to see them all. Build it.

1. `tools/retired.py` (--help; offline test in tools/tests/test_retired.py; SYSTEM.md row via tools/system_map_check.py;
   tool_shelf.tsv row): scans every ciphers/*/NOTES.md for lines carrying `[retired]` (any case) and every ciphers/*/HYPOTHESES.md
   row whose verdict or note says `untested-by-this-tool` or `retired`, plus research/TX-REGISTER.tsv rows with verdict
   `retired`, and writes `RETIRED.tsv` at the repository root with columns: folder (or `transcription`), step (the step or family,
   one line), instrument (the tool or method retired, as named), date (from the line; `unknown` if none), attempts (the three
   results if the line gives them), why (one line: the rule-3 clause -- control failed three times, numbers not moving together,
   non-test at this N), reopen_when (what the line says would reopen it: a different instrument, new material, a better image,
   owner tiles; `not stated` if none), source (file:line). Best-effort parsing: a line it cannot parse is written with step =
   the raw line and the other cells `?`, never dropped. `--check` exits non-zero if any row has reopen_when `not stated` (prints
   them) -- the rule in CLAUDE.md rule 5: a [retired] step names the instrument and what reopens it.
2. Run it once; commit RETIRED.tsv; paste the row count and the `--check` list in your done line. Do NOT edit any NOTES.md or
   HYPOTHESES.md: a row with `not stated` is reported, not repaired (the orchestrator queues the repairs).
3. Note in the docstring the must-catch (a [retired] line with no reopen condition) and must-not-block (a [retired] line that
   names "a different instrument or new material") cases, each with a test row.
ROOM claim first ("for orchestrator (account-4)", cap, box end by date -u), done line at the end with the counts, system_map_check
and file_shrink_guard output; then python3 tools/work_queue.py --done RETIRED-REGISTER --note "<rows>", git add by path, commit,
git pull --rebase origin main, git push origin HEAD:main. Never AskUserQuestion; never print credentials; stage by path; never
force-push; never edit a target folder's files.
