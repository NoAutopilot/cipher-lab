# RETRO-2026-10-19 P1 and P2: two small tools (account 4, 19 Oct 2026, 07:2x UTC by date -u)

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself). CLAUDE.md Usage 8a applies to both tools: each states in its docstring the cases it must catch and at least one it
must NOT block, each backed by an offline test in tools/tests/, and each is named in SYSTEM.md in the same commit
(`tools/system_map_check.py` passes). Cite "RETRO-2026-10-19 P1/P2, applied 19 Oct 2026" in each tool's header (P5).

## JOB RETRO19-TOOLS (account 4; Sonnet 5; cap USD 5; box 50 minutes; hosts: none; Price: vision calls: 0 x USD 0 = 0)

Read RETRO-2026-10-19.md sections 2, 3 and 6 first.
1. P1: `tools/near_audit_columns.py` counts cells in every NEAR.md active-table row the way `tools/near_check.py` parses them and flags
   any row whose count differs from the header's; run it on NEAR.md and paste the output (report, do not fix rows owned by other lanes).
   `tools/near_touch.py <target> [--note TEXT]` appends to a row's Evidence and stamps Last-touched with the current UTC date in the same
   edit (read the clock; never type a date), refusing when the target has no row. Tests: a synthetic NEAR.md with a pipe inside a cell
   (must flag), a clean one (must not), and a touch round trip.
2. P2: `tools/dup_check.py <target> [--hours N]` greps ROOM.md (all accounts) for claim/done lines naming the target folder or its job
   section within the window, and prints them with an exit code (1 when a live claim without a done line exists). Tests: the three
   motivating shapes from RETRO-2026-10-19 section 3 as fixtures (must catch), a target whose only lines are done lines (must not block).
   Add one line to .claude/briefs/README.md's common tail: run `python3 tools/dup_check.py <target>` before opening a job and paste it.
3. Run the new tests and `tools/system_map_check.py`; update RETRO-PROPOSALS.tsv rows RETRO-2026-10-19 P1 and P2 to applied with the
   evidence (commit, test names). Commit by path, push.
Report: the two tools, the NEAR.md audit output in one line, tests passing, five lines.
