# Jobs queued by the account-4 parent (LANE VIV-KEYSTONE, session_01D7XWmthshMVqxumdDvitPh) for account 1's dispatcher, 15 Oct 2026 01:5x UTC

Both jobs report to the account-4 parent (ROOM.md done line "for LANE VIV-KEYSTONE (account 4)"); the account that runs them ledgers them
(CLAUDE.md Improvement loop). Each worker: CLAUDE.md first, `python3 tools/room.py --start`, last 30 ROOM.md lines, claim before any edit, done
line when stopping, commit by explicit path, pull --rebase, push to main, five-line report. Neither touches key.tsv, any reading, status.json, or
the owner's published pages; neither starts another job.

## JOB SORTER-FIX-R12-R16 (tool job; Opus 5.5; cap USD 10; box 120 minutes; Price: vision calls: 0 x USD 0 = 0)

Why: the owner's two Vivonne packets (14-15 Oct 2026) hit the same page defects twice; his words are rows R12-R16 of
`tools/data/sorter_owner_requirements.tsv` (read every row, and the file's header rule that each row becomes an automatic check). Result of the
second packet: 18 of 34 answers "new sign" because the piles mixed shapes (NOTES.md of ciphers/fr16104-vivonne-spain-1572, "VIV-PACKET3 result").
No owner page is published again until this job's checks pass.

Do, in `tools/sign_sorter.py` (and `tools/sign_sorter_apply.py` where the export changes), with offline tests in `tools/tests/`:
1. R12/R16: on the question page (step 2), "Fix the cut" is removed from the question card. A person judges from the line strip; the only
   box answer is "Bad cut". Keep the fix-the-cut machinery on the pile cards (step 1/tray) but make it correct there: after "Save cut" the tile
   is re-rendered from the saved box and stays in its pile and placeable (reproduce the vanishing first with Playwright against the committed
   f.191r page `ciphers/fr16104-vivonne-spain-1572/tx/sorter_f191/sorter_viv_f191.html` -- Chromium is pre-installed, PLAYWRIGHT_BROWSERS_PATH
   set; a headless test that opens the page, saves a cut on one tile and asserts the tile is still rendered and movable).
2. R13/R15: a new build option `--piles-from SETTLED.tsv [--piles-from ...]` that builds the piles ONLY from a person's settled piles
   (sign_sorter_apply.py output: sid, new_sign, status moved|kept) plus optional certain-answer tiles, one shape per pile, and a build-time
   check that fails the build when (a) any tile appears in two piles, (b) a waiting (question) tile is shown inside any pile preview, (c) two
   piles carry the same meaning without a visible "same letter, two shapes" note. The unsorted/waiting box is rendered as a queue, not a pile
   (no "keep in unsorted" answer; R15).
3. R14: the build refuses a question page whose box check file (`box_check.tsv` or `boxes_handcut.tsv` with a check column) has under 90% pass,
   printing the failing sids; a page built without a box-check file prints a warning naming the rule.
4. `tools/sorter_preflight.py` gains these checks (R12-R16 by name); `python3 -m pytest tools/tests -k sorter -q` passes; a one-paragraph
   entry in SYSTEM.md (tools/system_map_check.py passes).
5. Re-render, do NOT publish, the f.191r packet with the new build from the owner's own settled piles
   (`ciphers/fr16104-vivonne-spain-1572/tx/vivhuman/answers_2026-10-14_attempt2/settled.tsv` and `answers_2026-10-14/settled.tsv`) and the
   three truth leaves' certain-answer tiles, into `ciphers/fr16104-vivonne-spain-1572/tx/sorter_f191b/`; paste the preflight and build-check
   output in NOTES.md "## SORTER-FIX-R12-R16 (<date -u>)" and in the done line. The account-4 parent publishes it, or not.
Stop at the cap or box; a defect you cannot fix in the box is written as a failing test with a skip marker naming R-number, never silently.

## JOB VIV-F191C (measurement; Opus 5.5 worker, Sonnet readers; cap USD 8; box 90 minutes; Price: vision calls: 8 x USD 0.6 = 4.8)

Why: VIV-F191B (ciphers/fr16104-vivonne-spain-1572/NOTES.md, 14 Oct 2026) found pass D drifted on f.191r L22-L36 (its line mapping failed
there), so those 15 lines carry three usable votes, not four. A third fresh blind pass on exactly those lines, with a per-pass line-drift check,
is the named next step in STATUS.md's LANE VIV-KEYSTONE handoff.

Do: 1. PREREG-VIVF191C.md pushed first: the lines (L22-L36), the reader protocol (blind: no key values, no other pass shown), the drift check
(per line, NW agreement of the new pass with pass A at the same line id must beat both neighbours' ids, as f191.py's `mapping()` does), and
the gate for using the pass (drift check passes on >= 13 of 15 lines; else the pass is logged and not used). 2. Line crops: the VIV-F191
crops; if gone, regenerate with the committed command in NOTES.md "VIV-F191" (openapi.bnf.fr: take/release lines, one request at a time
>= 3 s, at most 2 requests), then `tools/iiif_lines.py --image <leaf> --out <dir>` crops under 2500 px, pasted. 3. Readers: Sonnet subagent
calls, ONE line crop (or its two halves) per call, 15 lines -> at most 8 calls with two lines per call where the crops are short; readers
return text only, the worker writes `tx/viv63_f191/f191r_passE.tsv` (row, codes; the pass A/B/C/D format). 4. Drift check per line, pasted.
5. Report only: agreement of E with A, B, C per line on L22-L36 (`err_2reader` style), and what the fourth vote would settle (count of
flagged positions on those lines where E agrees with the plurality vs with the minority) -- do NOT change f191.py's reconciliation (3-of-4)
or rec.tsv; the parent decides a 5-pass rule in a separate PREREG. 6. NOTES.md "## VIV-F191C (<date -u>)", requests per host, cost not
visible; done line: drift check x/15 first, then the agreement numbers.
