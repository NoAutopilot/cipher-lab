# PREREG-OBRED6019 (addendum to the OBRED-6018 screen method), 15 Oct 2026, written 05:5x UTC by date -u, before any scan is fetched

Job OBRED-6019 (LANE DEFAULT-A2-0509-15, account 2). Target: NL-HaNA 1.01.02 inv. 6019 (Liassen Agent Brederode, 1619), METS
1ebb4182-2b80-4e37-a226-8b8c7e578c8b, 649 scans (`nl_brederode_lias.tsv`). Question: is there a third numeral-code text in the
no. 92 / scan-187 table? Nothing is decoded and no key gate is computed here.

Method, unchanged from OBRED-6018: scans 1, 4, ..., 649 (= 1 mod 3; 217 scans) at IIIF `/full/700,/0/default.jpg`
(`screen_tools/na_fetch.py`, >= 2.1 s apart, descriptive UA), sheets by `screen_tools/contact_sheets.py` with SHEET_SCANS=9 (4x3:
nine scans + the three disk controls CTRL-CIPHER = inv. 2016 scan 31, CTRL-PLAIN = inv. 6016 order 261, CTRL-PS = scan 187 at 1200 px),
seed 6019, tile letters only. One reader (this worker's own eye), no subagent.

Calls: for each sheet, the reader writes the tile letters of the three controls and of any numeral-hit tile to
`images/6019_screen_sheetcalls.txt`; the calls file is pushed before `images/6019_screen_sheetkey.json` is opened or checked.
A sheet is a valid test only if all three controls are placed correctly (checked mechanically against the key); a sheet with a control
misplaced is a non-test and its scans count as unscreened. A hit = a block of numeral groups of the target's system (arabic numerals in
runs of separated groups inside or after prose, as in no. 92 / scan 187), a key table or an interlinear decipherment; a doubtful tile
may be re-looked at 1200 px (scratchpad only, at most 8 such requests).

Stop rule (Usage 6): priced from OBRED-6018's own numbers (4.43 for 22 sheets, about 0.20 per sheet all-in, Opus floor ~1.5), the 80%
line of the cap 5 (4.0) allows about 19-20 sheets; the reader stops before a sheet that would cross that line or 80% of the box
(07:01 UTC; box 05:49-07:19 UTC). Sheets are read in order 1, 2, ...; any sheet not read is reported as unscreened by scan range.
Requests: at most 230 to service.archief.nl (1 METS + 217 at 700 px + <= 8 at 1200 px). Images stay outside git (session scratchpad).
