# PREREG-OBRED6020 (addendum to the OBRED-6018/6019 screen method), 15 Oct 2026, written 12:0x UTC by date -u, before any scan is fetched

Job OBRED-6020 (LANE DEFAULT-A2-1109-15, account 2, wave 3). Target: NL-HaNA 1.01.02 inv. 6020 (Liassen Agent Brederode, 1620), METS
6b71330d-279e-4fe8-904b-01493a2c93d1, 604 scans (`nl_brederode_lias.tsv`). Question: is there a third numeral-code text in the
no. 92 / scan-187 / 6019-556 table, a key leaf, or a Brederode cipher postscript? Nothing is decoded and no key gate is computed here.

Method, unchanged from OBRED-6019 except the stride: scans 1, 7, ..., 601 (= 1 mod 6; 101 scans) at IIIF `/full/700,/0/default.jpg`
(`screen_tools/na_fetch.py`, >= 3.1 s apart, descriptive UA), sheets by `screen_tools/contact_sheets.py` with SHEET_SCANS=9 (4x3:
nine scans + the three disk controls CTRL-CIPHER = inv. 2016 scan 31, CTRL-PLAIN = inv. 6016 order 261, CTRL-PS = scan 187 at 1200 px),
seed 6020, tile letters only; 12 sheets (11 x 9 scans, the last with 2). One reader (this worker's own eye), no subagent.

Calls: for each sheet, the reader writes the tile letters of the three controls and of any numeral-hit tile to
`images/6020_screen_sheetcalls.txt`; the calls file is pushed before `images/6020_screen_sheetkey.json` is opened or checked.
A sheet is a valid test only if all three controls are placed correctly (checked mechanically against the key); a sheet with a control
misplaced is a non-test and its scans count as unscreened. A hit = a block of numeral groups of the target's system (arabic numerals in
runs of separated groups inside or after prose, as in no. 92 / scan 187), a key table, an interlinear decipherment, or a Brederode letter
with a figure postscript; a doubtful tile may be re-looked at 1200 px (scratchpad only, at most 8 such requests). A confirmed hit gets
one Opus read at native/1200 px (brief: one read per flagged page), described M; nothing decoded.

Stop rule (Usage 6): priced from OBRED-6018/6019 (about 0.20 per sheet all-in, start-up ~1), 12 sheets ~2.4 + start-up ~1 = ~3.4 against
the cap 4: the reader stops before a sheet that would cross 3.2 (80% of cap; about sheet 11) or 80% of the box (13:01 UTC; box
12:01-13:16 UTC). Sheets are read in order 1, 2, ...; any sheet not read is reported as unscreened by scan range.
Requests: at most 120 to service.archief.nl (1 METS + 101 at 700 px + <= 8 at 1200 px + <= 2 native reads). Images stay outside git.
Limit: stride 6 samples one scan in six; a one-leaf postscript is a sixth as likely to be sampled as a page run of six. A negative is
for the scans read at this resolution, not for inv. 6020 as a whole.
