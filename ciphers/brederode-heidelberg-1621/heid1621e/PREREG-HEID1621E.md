# PREREG-HEID1621E, 15 Oct 2026, written 19:1x UTC by date -u, before design_prior is run and before any scan is fetched

Job HEID-1621E (brief `.claude/briefs/runs/2026-10-15-acct4-depth-steps-2.md`; account 2; for LANE VIV-KEYSTONE / the orchestrator).
Target: ciphers/brederode-heidelberg-1621 (NL-HaNA 1.01.02 inv. 6021 scans 375/379, 13 Aug 1621, 96 numerals / 45 units, open).
Nothing is decoded, no key is edited, nothing is read as plaintext.

## Step 1: design prior and key files on disk
`python3 tools/design_prior.py --no-write <units file>` on the 45 units as numeral-pair+letter tokens (from ciphertext.tsv, M), output
pasted. KEY-OFFICES.tsv and KEY-DESIGN.tsv grepped for States General / Staten-Generaal / Palatinate / Pfalz / Heidelberg / Brederode /
agent rows with years overlapping 1618-1625, and for any pair-plus-letter design. A candidate is any row in those years and offices;
reported with its key_path. A design-prior output is a lead for which family to test first, never a key or a reading.

## Step 2: pool screen (the other scans of inv. 6021)
Scans 4, 10, ..., 358 (= 4 mod 6, 60 scans) and 400, 406, ..., 802 (= 4 mod 6, 68 scans): 128 scans at IIIF `/full/700,/0/default.jpg`
from METS c82b1eb5-6946-4ca9-8082-f13c2ab5f078 (`../oldenbarnevelt-brederode-1605/screen_tools/na_fetch.py`, >= 3.1 s apart, descriptive
UA), scratch only. With OBRED-6021's 1 mod 6 grid this covers stride 3 of 1-805 (361-397 also read at stride 1 by HEID-1621B).
Sheets by `screen_tools/contact_sheets.py`, SHEET_SCANS=9 (4x3: nine scans + the three disk controls CTRL-CIPHER = inv. 2016 scan 31,
CTRL-PLAIN = inv. 6016 order 261, CTRL-PS = inv. 6016 scan 187 at 1200 px), seed 16215, tile letters only; 15 sheets (14 x 9 + 2).
One reader (this worker's own eye), no subagent.
Calls: per sheet, the tile letters of the three controls and of any hit tile go to `heid1621e/sheetcalls.txt`; that file is pushed before
`sheetkey.json` is opened or checked. A sheet is a valid test only if all three controls are placed correctly (checked mechanically);
otherwise its scans count as unscreened.
**A hit** = (a) a numeral block: arabic numerals in runs of separated groups inside or after prose (pair+letter as scan 379, or any other
grouping); (b) a key leaf: a table of numbers against letters, syllables, words or names; (c) an interlinear or marginal decipherment
(clear text written over or beside groups); (d) a figure postscript (a separate paragraph or slip of groups). A list of quantities,
dates or money in columns is not a hit. Each hit gets one 1200 px re-look of that scan only (<= 8 such requests), described M.
Stop rule (Usage 6): priced at about 0.20 per sheet all-in (OBRED-6020/6021), 15 sheets ~3.0 + start-up and step 1/3 ~1.2 = ~4.2 of
cap 5. The reader stops before a sheet that would cross 4.0 (80% of cap) or 80% of the box (20:11 UTC; box 19:11-20:26 UTC). Sheets are
read in order 1, 2, ...; any sheet not read is reported unscreened by scan range.
Requests: service.archief.nl <= 140 (1 METS + 128 + <= 8 re-looks), ROOM take/release lines, one at a time with any other NA worker.

## Step 3: key candidates (no scans)
www.nationaalarchief.nl <= 10: the 1.01.02 finding-aid entries for inv. 6021 onward (Brederode liassen 6022+, titles only) and any
'sleutel' / 'cijfer' / 'chiffre' entry 1618-1625. resources.huygens.knaw.nl <= 15: Resolutien SG NR 5 full-text search for 'cijfer',
'sleutel', 'gedecifreerd'/'dechiffr' and Brederode entries naming a decipherment in 1621-1622. Every candidate listed with inventory
number and whether digitised. A candidate is a pointer, never a key.

Limits stated in advance: stride 6 per sweep (stride 3 combined) samples one scan in three; 700 px tiles on sheets read at ~2,000 px can
miss a block of a dozen groups or fewer; one reader. A negative covers the scans read at this resolution only.
