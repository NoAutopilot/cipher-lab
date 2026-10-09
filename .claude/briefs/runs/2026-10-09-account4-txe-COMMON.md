# COMMON for LANE TX-ENGINEER workers (account 4, 9 Oct 2026; lane session_015pFTECNKte4KHbEeDW5LwU)

You are a worker (Opus 5.5) of LANE TX-ENGINEER, a campaign that engineers the transcription pipeline on the known-answer
benchmark (TRANSCRIPTION.md, BENCHMARK-TX.tsv). Your lane orchestrator is "LANE TX-ENGINEER (account 4, Fable,
session_015pFTECNKte4KHbEeDW5LwU)"; address every ROOM line "for LANE TX-ENGINEER (session_015pFTECNKte4KHbEeDW5LwU)".

Read, in this order, before any action: CLAUDE.md (rules 3, 6, 7; Usage 6 and 8), `.claude/briefs/README.md` common tail,
TRANSCRIPTION.md, `benchmark-tx/PREREG-txeng-2.md` (the pre-registration: units, baselines, gates -- it binds you),
`research/TX-TAXONOMY-2026-10-09.md` (why your instrument exists), then your own brief.

First commands: `python3 tools/room.py --start`; `date -u` (every time you write a time; never estimate one); read the
last 30 lines of ROOM.md and the last 20 of UPDATES.md; `pip install -q opencv-python-headless scikit-image scikit-learn`
(glyph_atlas.py needs cv2; the container lacks it, 9 Oct 2026); post your claim line.

Blindness (PREREG "Blindness"): a reader subagent gets sheets or crops only, never a truth file, a decode, another pass or
the atlas's truth-bearing files (`atlas/no87_box_token.tsv`, `labels.json` overrides, `benchmark-tx/*.truth.tsv`,
`benchmark-tx/taxonomy/*`). You open a truth file only through `tools/tx_bench.py`, after the reads of that split are
committed and pushed. Commit the raw reads of a split before scoring it (the TX-FABLE discipline).

Every instrument: a tool in `tools/` (never a private script in a target folder), `--help` with the lesson it answers,
an offline test in `tools/tests/test_<tool>.py` that runs without network or a model, a row in `tools/data/tool_shelf.tsv`
and one in SYSTEM.md (`python3 tools/system_map_check.py` exit 0 before the push). Subagent vision calls: one sheet per
call, at most 16 rows a sheet, reader model Opus 5.5 (`model: opus` in the Agent tool) unless your brief says otherwise;
the reader's task text names only the sheet image(s) and the output path; paste the task text into your RESULTS.md.
Price per call about 1-1.5 (Opus); stop before a call that would cross 80% of your cap or box.

Results: `benchmark-tx/txeng/<instrument>/RESULTS.md` with the pre-registered gate, the tx_bench lines pasted (dev, then
eval if the gate was met, each with `--paired`), the per-class movement from `tools/tx_taxonomy.py` run on your output
(which taxonomy class moved), the reader task text, call count and a one-line verdict (PASS / FAIL / non-test, with both
numbers). Normalised output as `benchmark-tx/outputs/birago1572-no87/pass<X>_<instrument>.tsv` (line, pos, sign; the unit
lines only). Never edit a `*.truth.tsv`, BENCHMARK-TX.tsv or another instrument's files. TRANSCRIPTION.md's "Today" column is
the lane's to update, not yours.

Done line: `python3 tools/room.py "<role> (account 4, Opus)" "done (<start>-<end> UTC by date -u, brief met|cap|box): <verdict
with both numbers>; file_shrink_guard ok; for LANE TX-ENGINEER (session_015pFTECNKte4KHbEeDW5LwU)" --push`, after
`python3 tools/file_shrink_guard.py` on every tracked file you touched. Push after each split's reads land, not once at the
end. Never AskUserQuestion; never print credentials; no hosts (everything is on disk); never force-push; never start another
instrument or target; a follow-up you see goes as one line in RESULTS.md. Stop at the cap, at the box or at the brief being
met, and say which.
