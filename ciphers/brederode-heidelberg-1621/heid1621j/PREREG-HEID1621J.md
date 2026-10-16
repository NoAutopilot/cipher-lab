# PREREG-HEID1621J, 16 Oct 2026, written 00:1x UTC by date -u, before any fetch

Job HEID-1621J (brief `.claude/briefs/runs/2026-10-15-acct4-depth-steps-2.md`; account 2; for the orchestrator / LANE VIV-KEYSTONE).
Target: ciphers/brederode-heidelberg-1621. Nothing is transcribed, decoded or read as plaintext; no key edit.

## Step 1: the edition list
Resolutien SG nieuwe reeks deel 5 (1621-1622), Huygens retroboeken `statengeneraal/searchText`, source 5, terms in this order:
"in code", "in cijfer", "cijfer", "gecodeerd", "gedecifreerd", "gedechiffreerd", "code", then the "Brederode" hit list (109 hits,
batches 0-100). An entry enters `code_letters.tsv` if its resolution or its note names a Brederode letter AND the note says in code /
in cijfer / gecodeerd / gedecifreerd (or the like), read on the printed page's OCR html, not the snippet. Budget: <= 20 requests
(>= 2 s apart); if the budget runs out, the list says which terms were not run.

## Step 2: the screen
For each listed entry pointing at inv. 6021 or 6022 not yet located (13 Aug = 375/379 and 17 Sept = 423 are done): predict a start scan
from the neighbouring dated scans already called in heid1621e/f screen.tsv (6021) or from the liasse's length (6022), fetch at
IIIF `/full/700,/0/default.jpg` in date order outward from that scan with `../oldenbarnevelt-brederode-1605/screen_tools/na_fetch.py`
(>= 3.1 s, descriptive UA, scratch only), contact sheets by `screen_tools/contact_sheets.py`, SHEET_SCANS=9, the OBRED-6020 disk controls
(CTRL-CIPHER inv. 2016 scan 31, CTRL-PLAIN inv. 6016 order 261, CTRL-PS inv. 6016 scan 187 at 1200 px), seeds 16220, 16221, ...
Calls (control tile letters + hit tile letters) to `sheetcalls.txt`, pushed before each sheet key is opened; a sheet with any control
misplaced counts as unscreened. One reader, this worker's eye; no subagent.
Hit: a numeral block (any grouping), key leaf, interlinear decipherment or figure postscript. Each hit: one 1200 px re-look of that scan,
sha1 in images/manifest.json, nothing committed. A hit is the target entry only when a dateline or signature at 1200 px matches its date (M).

## Stop rule
Per entry: stop at its target hit or after 54 scans past the predicted start without it (reported "not located in scans a-b").
Whole job: 140 service.archief.nl requests (METS + scans + re-looks), or before a batch that would cross 80% of the cap (USD 3.2) or of
the box (00:12-01:12 UTC; 80% = 01:00 UTC). Entries left unscreened are named with the next scan to start from.
www.nationaalarchief.nl <= 6 (item pages for availability only, if an entry points at an inventory number not yet checked).

## Limits stated in advance
700 px tiles can miss a block of a dozen groups or fewer; datelines M; one reader; the system call (pair+letter vs number+letter) is by eye, M.
