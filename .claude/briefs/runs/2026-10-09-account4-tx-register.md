# TX-REGISTER (parent worker for orchestrator (account-4); Opus 5.5; cap 5, box 60 min; 9 Oct 2026 17:2x UTC)

Build `tools/tx_register.py` (--help, offline test in tools/tests/test_tx_register.py, SYSTEM.md row, tool_shelf.tsv row):
it compiles research/TX-REGISTER.tsv -- one row per experiment of both transcription campaigns -- from benchmark-tx/PREREG-*.md,
benchmark-tx/txeng/*/RESULTS.md, benchmark-tx/txeng2/*/RESULTS.md, research/TX-IDEAS-2026-10-09.md and
research/TX-IDEAS-2-2026-10-09.md (their tables and results logs), and TRANSCRIPTION.md's build-plan "Today" rows (TX-VIEWS,
TX-AGREEAUDIT, TX-ALTS, TX-SHEET, TX-FABLE). Columns: id, campaign, family, mechanism_attacked, unit_or_pool, dev_result,
eval_result, eval_looks, verdict (dev-FAIL / dev-PASS / moved-eval / did-not-move / non-test / retired / measured / running /
queued), reason (one line), source_file, date. Parsing is best-effort over the files' own tables (a row the parser cannot read
is written with verdict `unparsed` and the source line, never dropped). Add `--check PREREG.md`: exits non-zero unless the
PREREG names at least one register id under a "Nearest prior" / "differs from" heading with one sentence of difference, and
unless no named id has verdict `retired` without the word "different instrument" or "new material" in that sentence (the
rule in research/TX-PROGRAM.md "Memory"). Docstring states the must-catch (a re-run of a retired family with no stated
difference) and the must-not-block (a PREREG citing a retired id with a stated different instrument) cases, each with a test.
Run it once, commit research/TX-REGISTER.tsv, and paste the row count per verdict in your done line. Do not edit any PREREG,
RESULTS or truth file; do not score anything. ROOM claim first, done line "for orchestrator (account-4)" with the counts and
system_map_check output. Never AskUserQuestion; never print credentials; stage by path; never force-push.
