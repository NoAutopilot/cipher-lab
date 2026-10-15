# PREREG-HEID1621F, 15 Oct 2026, written 20:1x UTC by date -u, before any scan is fetched

Job HEID-1621F (brief `.claude/briefs/runs/2026-10-15-acct4-depth-steps-2.md`; account 2; for LANE VIV-KEYSTONE / the orchestrator).
Target: ciphers/brederode-heidelberg-1621. Question: where in NL-HaNA 1.01.02 inv. 6021 is Brederode's letter dd. Heidelberg 17 Sept 1621,
which Resolutien SG NR 5 p. 295 res. 1879b (28 Sept 1621) calendars as "S.G. 6021 (orig.). Gedeeltelijk in code"?
Nothing is decoded, no key is edited, nothing is read as plaintext.

## Screen
Scans 398, 399, 400, ... in order, at IIIF `/full/700,/0/default.jpg` from METS c82b1eb5-6946-4ca9-8082-f13c2ab5f078
(`../oldenbarnevelt-brederode-1605/screen_tools/na_fetch.py`, >= 3.1 s apart, descriptive UA), scratch only. Scans already screened at
stride 3 (400, 403, 406, ...; HEID-1621E / OBRED-6021) are fetched and screened again: the stride-1 sweep is the test here.
Fetched in batches of 27 (three sheets); sheets by `screen_tools/contact_sheets.py`, SHEET_SCANS=9 (4x3: nine scans + the three disk
controls CTRL-CIPHER = inv. 2016 scan 31, CTRL-PLAIN = inv. 6016 order 261, CTRL-PS = inv. 6016 scan 187 at 1200 px), seed 16216 for
batch 1, 16217 for batch 2, ...; tile letters only. One reader (this worker's own eye), no subagent.
Calls: per sheet, the tile letters of the three controls and of any hit tile go to `heid1621f/sheetcalls.txt`, pushed before that batch's
sheet key is opened or checked. A sheet is a valid test only if all three controls are placed correctly (checked mechanically);
otherwise its scans count as unscreened.
Orientation (not a hit test): the worker may open single 700 px scans already on disk (no request) to read datelines and address-leaf
dates, recorded M in `heid1621f/screen.tsv`, so the report can say where 27 Aug / 17 Sept / Oct 1621 fall.

## What counts as a hit
A numeral block (arabic numerals in runs of separated groups inside or after prose: pair+letter as scans 375/379, or any other grouping),
a key leaf, an interlinear or marginal decipherment, or a figure postscript. Quantities, dates or money in columns are not a hit.
Each hit gets one 1200 px re-look of that scan only (sha1 in images/manifest.json, no image committed), described M: date line and
signature as read, whether the numerals are the pair+letter design of 375/379 (consecutive two-digit pairs plus a trailing letter), by eye.
The **target hit** is a letter dated 17 Sept 1621 carrying numeral groups; its duplicate (as 379 duplicates 375) is looked for in the
following scans of the same batch and of at most one further batch.

## Stop rule
Stop at the first target hit (plus its duplicate check above), or at 136 service.archief.nl requests (1 METS + scans + 1200 px re-looks),
or before a batch that would cross 80% of the cap (USD 3.2; priced ~0.20 per sheet all-in, OBRED-6020/6021) or of the box (box 20:12-21:12
UTC; 80% = 21:00 UTC), whichever comes first. The last scan screened is reported so the next row can continue from it.
A non-target numeral hit (another date, another system) is recorded and the screen continues.

## Limits stated in advance
700 px tiles on sheets read at ~2,000 px can miss a block of a dozen groups or fewer inside prose; datelines at 700 px are M; one reader.
A negative covers the scans read at this resolution only.
