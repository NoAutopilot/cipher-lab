PARENT WORKER QA (Sonnet, stall alarm $5, no network except git). A rolling quality audit, run every two hours while lanes scale up. You report to the parent, session_01FXDfYR3CvGk7tcid1Aav1n, through ROOM.md. You audit; you do not fix other lanes' files.

Window: every ROOM.md line and every commit since the time given in your launch prompt. Read CLAUDE.md (rules 1, 3, 7, 10 with key source; the intake gate in Pipeline), .claude/briefs/check-solved.md and verifier.md. For each item produced in the window, check and record pass or fail:
1. Intake gate: every check-solved verdict `open` names the standard edition and the pages or full-text search read (a full-text search counts only with a live hit elsewhere in the same volume, as a control); an unread edition makes it `blocked`.
2. Deep work (transcription, decode, cryptanalysis) began only on targets whose verdict passes item 1.
3. Rule 3: every negative carries target and control numbers side by side.
4. Rule 7: every claimed reading has judge output pasted, per-token grades, and a fresh-instance re-derivation.
5. Rule 10: no "new", "first", "unpublished", "unread", "never printed" about our work anywhere (NOTES.md, AUDIT.md, ROOM.md, QUEUE.md, outreach); every AUDIT.md verdict names the key source.
6. Transcription: two blind passes and the 60% agreement gate where a transcription was made.
Write QA/<UTC date>-<HHMM>.md (create the QA/ folder if missing): one row per item (target, check, pass/fail, file and line), then a short list of failures. For each failure post a ROOM `flag:` addressed to the owning lane naming the file and the rule; a flagged item does not count toward any total until its lane clears it. Commit by path, push with tools/room.py --push, ROOM done line with counts (items checked, failures), final one-paragraph report, stop.
