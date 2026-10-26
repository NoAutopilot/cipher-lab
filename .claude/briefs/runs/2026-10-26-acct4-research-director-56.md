# Research director, wave 56 (26 Oct 2026, 06:4x UTC by date -u): apply RETRO-2026-10-26 P1, P2, P3 (tools and the common tail)

Common tail .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself). Done line addressed for the account-4 parent. Offline: no network.

## JOB RETRO-APPLY-1026 (account 4; Sonnet 5; cap USD 4; box 40 minutes; hosts: none (disk only); Price: vision calls: 0 x USD 0 = 0)

Read RETRO-2026-10-26.md sections 2, 3 and 6, RETRO-PROPOSALS.tsv's five 2026-10-26 rows, CLAUDE.md Usage 8a (a gate states in its
docstring what it must catch and what it must NOT block, each with an offline test), tools/brief_price_check.py and its test
tools/tests/test_brief_price_check.py, tools/ledger_check.py and tools/tests/test_ledger_check*.py, and .claude/briefs/README.md.
1. **P1, tools/brief_price_check.py.** Per '## JOB' section: if the section text names a dense source (`\btable\b|\bregister\b|
   \bdense (?:leaf|page)\b|\btabula\b`, case-insensitive) it must also state an estimated row or entry count (`(\d+)\s*rows?\b` or
   `entries`); the gate then requires the section's vision-call N >= ceil(rows/50); a dense word with no count fails ("TABLE <job>:
   no row estimate"), too few calls fails with the expected count printed. Must NOT block: a section whose 'table' is a markdown
   output table the worker writes ("Output: ... with a table (id, item, ...)" -- restrict the dense-source rule to sections that
   also carry an image step per the existing IMAGE_RE, and skip the match when 'table' is followed within 40 chars by '(id' or
   'columns'), a brief with no image step, the HEATHCOTE-PAGES brief as the failing case (brief -52: "transcribe the table" with 8
   calls and no row count must now FAIL), and briefs -55 and -53 as passing cases. Docstring updated with both lists; tests added.
2. **P2, tools/ledger_check.py.** `--over-cap-severity FROM_ROW`: for D- rows at or after FROM_ROW whose lesson cell carries an
   `(\d+(?:\.\d+)?)x` ratio, print counts and the rows for ratio < 1.3 ("near-cap") and >= 1.3 ("real miss"); exit 0 always; a row
   with no ratio is listed under "unparsed". Offline test with three synthetic rows (1.05x, 1.71x, no ratio).
3. **P3, .claude/briefs/README.md common tail.** Two sentences, verbatim from RETRO-2026-10-26 P3's diff block, placed beside the
   existing vision-call pricing sentence, each citing RETRO-2026-10-26 P3 and the motivating rows (SORTER-KING, HEATHCOTE-HOLDER).
4. Run the whole offline suite you touched (`python3 -m pytest tools/tests/test_brief_price_check.py tools/tests/test_ledger_check*.py
   -q` or the repo's own runner), run `python3 tools/brief_price_check.py` over every brief under .claude/briefs/runs/ dated 2026-10-2*
   and list which now fail and why (expected: -52 fails on P1; any other failure is reported, not fixed), run `python3
   tools/system_map_check.py`, then set the three RETRO-PROPOSALS.tsv rows to `applied` with the evidence cell naming the files and
   tests. file_shrink_guard on every touched file before the push. Report: the three diffs in one line each, test results, the
   brief sweep result, five lines.
