# SORTER-PREFLIGHT (written by account 3, 6 Oct 2026, for account 1). Opus 5.5. Cap $5, box 60 min. Public repo (tools).
Owner, 6 Oct 2026, after the Oldenbarnevelt sorter cut its tiles from the clear line above the cipher and the Dinteville
/ MLH pages reached him unanswerable or unreadable: "how do we prevent this in the future?" Rule 8a: make it a tool.
Build tools/sorter_preflight.py SORTER.html [--cipher-lines FILE] [--expect-owner-account] that exits non-zero unless:
 1. template: the page carries Fix the cut (ctxFix) and the current template's version marker;
 2. answerable: every Check-these-first tile has >=2 named piles it can be placed in (not one UNREAD pile), and the
    focus box is non-empty;
 3. right line: every tile's page/line id is in the cipher-line list (signs.tsv page ids vs --cipher-lines, or the
    target's decode.json / line map); tiles whose box is mostly blank or solid black (ink ratio outside 3-60%) and
    tiles wider than 2.5x the median sign width (merged signs) are counted, and the run fails above 5%;
 4. contact sheet: writes SORTER.preflight.png with 24 random tiles beside their line strip, for a person or a
    separate session to eye in 30 seconds.
Wire it into tools/sign_sorter.py (run after build, print the verdict) and into .claude/briefs/parent.md gate 6 (one
line naming the tool). Offline tests in tools/tests/ with three fixtures: a good page; a wrong-line page (the
Oldenbarnevelt shape); an unanswerable page (the Dinteville one-pile shape). State in the docstring what it must NOT
block (a page whose focus tiles are legitimately all one family). Register in SYSTEM.md. Then run it on the current
Ferdinand sorter inputs (ciphers/bne20211-ferdinand-1478/sorter/: text only, report numbers) and on Oldenbarnevelt's
(expect FAIL). ROOM done line for the account-3 orchestrator.
