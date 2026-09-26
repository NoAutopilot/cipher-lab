JOB bBLZ5 (LANE B5, Sonnet worker). One line: blitz-ciphers spec test 2 -- fetch the six untranscribed page images (Blitz-Cipher-01..06.jpg, scienceblogs.de) and transcribe them in one blind pass in the same conventions as the two pages on file, then report whether the symbol inventory and case pattern recur (internal consistency) and the new N.

Read first: `.claude/briefs/runs/2026-09-26-lane-b5-common.md` (and the 7b COMMON it names), `.claude/briefs/breadth.md`, specs/blitz-ciphers.json (test 2 and cheap_test_done), NEAR.md blitz-ciphers row, ciphers/blitz-ciphers/NOTES.md (the transcription conventions used for the two pages on file). Intake: `python3 tools/intake_gate_check.py blitz-ciphers` exit 0 at 01:05 UTC 26 Sept (re-run and paste).

Cap and box: $6 or 60 minutes from your first `date -u`, whichever first. Unit estimate: fetch about $0.5; about $0.8 per page for one pass (6 pages); margin one page. Stop before starting a page that would cross 80% of either figure, and push after every page. Host: scienceblogs.de only (images linked from the Cipherbrain post; one request at a time, >= 1.5 s apart, at most 20 requests, descriptive UA; on 403/429/challenge stop, log, one retry after a pause at most). No subagent (one pass only; RETRO-2026-09-25j).

Steps:
0. `date -u`; `python3 tools/room.py --start`; ROOM claim (tools/room.py) naming ciphers/blitz-ciphers/.
1. Fetch the six images to ciphers/blitz-ciphers/images/ with manifest.json (URL, size, sha1); folder under 30 MB.
2. One blind pass per page into ciphers/blitz-ciphers/pages_1-6.tsv (page, line, text), same case and punctuation conventions as the two pages on file; mark uncertain characters with the convention already used there.
3. Consistency test with a control: per page, the character inventory and case-pair ratios (upper/lower per letter) against the two pages on file; control: the same statistics between page halves of the two known pages (within-document spread). Report per page whether it sits inside that spread. Report total N (case-folded letters) across all eight pages.
4. Append cheap_test_done in specs/blitz-ciphers.json (date, method, both numbers); push; done line with target and control side by side. Do NOT run a family test on the new N (next job). Report in five lines.
