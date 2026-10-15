# PREREG-OBRED945X (addendum to the OBRED-6019/6020 screen method), 15 Oct 2026, written 12:3x UTC by date -u, before any scan is fetched

Job OBRED-945X (LANE DEFAULT-A2-1109-15, account 2, wave 4). Target: NL-HaNA 1.01.02 inv. 9450 (Intendit tegen Oldenbarnevelt, 72 scans),
9451 (letters of Oldenbarnevelt to Caron 1610-1619, 58), 9453 (to Langerak 1614-1619, 46), unit sizes from OBRED-NA2. Question: is the
no. 92 key (Brederode's cipher, "in des Advocaets Barnevelt handen"), a key table, another numeral-code text of the no. 92 / scan-187 /
6019-556 design, or a Brederode figure postscript on these files? Nothing is decoded and no key gate is computed here.

Scans: orders = 1 mod 3 from 4 up (scan 1 of each was seen by OBRED-NA2): 9450 4..70 (23), 9451 4..58 (19), 9453 4..46 (15) = 57 scans.
Route: one www.nationaalarchief.nl item page per inventory (scan list from `drupal-settings-json`, as OBRED-NA2), then service.archief.nl
IIIF `/full/700,/0/default.jpg`, >= 3.1 s apart, descriptive UA, with NA take/release lines in ROOM.md, after OBRED-6021 releases the host.
Files are named s<inv><order:03d>_700.jpg so one sheet run covers the three files. Sheets by `screen_tools/contact_sheets.py` with
SHEET_SCANS=9 (4x3: nine scans + the three disk controls CTRL-CIPHER = inv. 2016 scan 31, CTRL-PLAIN = inv. 6016 order 261, CTRL-PS =
scan 187 at 1200 px), seed 9450, tile letters only; 7 sheets (6 x 9 + 3). One reader (this worker's own eye), no subagent.

Calls: per sheet, the letters of the three controls and of any hit tile go to `images/945x_screen_sheetcalls.txt`, pushed before
`images/945x_screen_sheetkey.json` is opened. A sheet is a valid test only if all three controls are placed correctly (checked
mechanically against the key); a sheet with a control misplaced is a non-test and its scans count as unscreened. A hit = a block of
numeral groups of the target's system (arabic numerals in runs of separated groups inside or after prose, as no. 92 / scan 187), a key
table, an interlinear decipherment, or a Brederode letter with a figure postscript; small-number name codes in prose (the 9453 s24 kind)
are logged as a hit of that kind and described, not counted as the no. 92 design. A doubtful tile may be re-looked at 1200 px (at most
3 requests). A confirmed hit gets one Opus read at 1200 px or native, described M; nothing decoded.

Stop rule (Usage 6): about 0.20 per sheet all-in, start-up ~1; 7 sheets ~1.4 + ~1 = ~2.4 against cap 3: stop before a sheet that would
cross 2.4 (80% of cap) or 80% of the box (13:16 UTC; box 12:28-13:28 UTC). Sheets read in order; any unread sheet reported unscreened.
Requests: service.archief.nl <= 60 (57 at 700 px + <= 3 re-looks); www.nationaalarchief.nl 3. Images stay outside git.
Limit: stride 3 samples one scan in three; a one-leaf key slip is a third as likely to be sampled as a run of three. A negative is for the
scans read at this resolution, not for the three files as a whole.
