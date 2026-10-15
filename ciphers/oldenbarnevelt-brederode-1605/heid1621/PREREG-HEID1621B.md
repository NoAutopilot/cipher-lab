# PREREG-HEID1621B (15 Oct 2026, 16:2x UTC by date -u; worker HEID-1621B, account 2, for LANE VIV-KEYSTONE account 4)

Pushed before any image is fetched. Brief: .claude/briefs/runs/2026-10-15-acct4-depth-steps-2.md, JOB HEID-1621B. No decode, no key.

## Material and route
NL-HaNA 1.01.02 inv. 6021 (METS c82b1eb5-6946-4ca9-8082-f13c2ab5f078), scans 361-397 at stride 1 (37 scans) at 700 px by
`screen_tools/na_fetch.py`, >= 3.1 s apart, descriptive UA. Request budget service.archief.nl <= 45: 1 METS + 37 scans = 38; at most
7 further requests (1200 px re-looks of a flagged tile or of the opening/close of the scan-379 letter). Take/release lines in ROOM.md.

## Screen (task 2) -- the OBRED-6020 method and sheet controls
`SHEET_SCANS=9 screen_tools/contact_sheets.py`, seed 16211, controls as OBRED-6019/6020/6021 (disk: images/na_301_14_2016_p0031.jpg
CTRL-CIPHER, images/na_101_02_6016_p0261.jpg CTRL-PLAIN, images/na_101_02_6016_p0187_1200.jpg CTRL-PS). 37 scans -> 5 sheets
(the last 1 scan + 3 controls). One reader, this worker's own eye, no subagent. For every sheet the tile calls (letter -> hit/plain,
and which tile is each control) are written to images/heid1621b_sheetcalls.txt and pushed before the sheet key is opened.
A sheet whose three controls are not all placed correctly is a non-test for its scans.
**Hit** = any of: a run of three or more numeral groups (dotted or spaced) inside prose or in a block; a table of letters/syllables
against figures or signs (key leaf); a figure postscript; an interlinear decipherment. Figures in a dated list or an account with a
quantity column are not hits (OBRED-6020 convention). Every hit tile is re-looked at the 700 px scan itself (no new request), and at
1200 px only if 700 px cannot decide (counts against the 7 spare requests).
Scan 379 is the known hit: it counts as a fourth in-sheet positive check, not as a finding.

## Opening and sender (task 1)
Scans 370-377 (and 378-380 for continuity) are read one by one at 700 px after the sheet calls are pushed, to find where the
13 Aug 1621 Heidelberg letter (close on 379, address leaf 380 "Duplicaet vanden 13 Augusti 1621") opens: the first page whose
first line is a salutation ("Hoochmogende ...") with text continuing to 378. **Sender read** = a name written on the leaves of this
letter (signature, heading, docket, endorsement naming the writer): graded H for the name as written; a name inferred from the
liasse, from a neighbouring signed letter or from the hand is graded M and reported as an inference, never a reading.

## Stop rule
Stop starting new units at 80% of either the cap (USD 2.4) or the box (16:54 UTC); stop at the first 403/429/challenge on
service.archief.nl (one retry after a pause at most).
