# decode-9970-simancas-1527

Status: open

## What this is

DECODE R9970: Simancas, Archivo General de Simancas, sec. Estado, leg. 1563, fol. 572, 1527, Spanish
(Non-decrypted, 4 images, no attached document found on the record page). QUEUE.md row DC5. Sender/recipient
per aaymeloglu's scrape: Andrea del Burgo (Ferrara) to Chancellor [Mercurino] Gattinara, dated 26 October 1527.
Checked as part of LANE N check-solved batch DC1 (`.claude/briefs/runs/2026-09-24-lane-n-csDC1.md`).

## Check-solved sweep, 24 September 2026

1. **Bourdeau.** dbourdeau/cyphersolver's `CATALOGUE.md` entry 2.5 is this exact item: "AGS, sec. Estado, leg.
   1563, fol. 572 (DECODE R9970) ... DECODE R9970: Non-decrypted, 4 pp., unknown; alphabet, graphic signs,
   numerical; images login. Not viewed here. DECODE note: Letter dated October 26, 1527, from Andrea del Burgo
   to Chancellor Gattinara from Ferrara." Catalogued but explicitly "not viewed", confirming it has not been
   solved or attempted there.
2. **Editions.** CSP Spanish (Bergenroth/Gayangos), the brief's named edition for Simancas Estado 1509-1527:
   found `calendarorleters0003vari` (Gayangos, 1877, internetarchivebooks) on archive.org. An archive.org
   be-api full-text search for `"Andrea del Burgo" "Gattinara"` returns this volume as a hit, with highlighted
   snippets about "Giovan Bartholomeo da Gattinara" (Mercurino's nephew) — the query is a document-level AND,
   not a phrase match, so this does not show both names co-occurring on the same page, only that the volume
   discusses Gattinara's circle at length. Per the Access playbook's 23-24 Sept 2026 finding, be-api's
   `page_num` field is not a real page locator (it equals the item's total page count), so this hit cannot be
   cited to a page; the volume was not opened and read page by page this pass.
3. **Aymeloglu.** id 9970 is present in `decode-catalog.csv`/`decode-records.jsonl` as a routine catalogue
   entry; absent from `decode-ranked.md`'s printed rows and from `exclude.txt`.
4. **Tomokiyo.** No hit in `sources/cryptiana/` for "Andrea del Burgo", "leg. 1563", or "fol. 572".
5. **Web.** WebSearch `"Andrea del Burgo" Gattinara 1527 cifra Simancas carta` returned only general
   biographical pages (Gattinara's Wikipedia entry, del Burgo as Maximilian's ambassador alongside Gattinara in
   1509) — no specific mention of this 1527 cipher letter or a decipherment.
6. **Community lists.** None found this pass.

## Verdict

**Open.** CSP Spanish (Gayangos, vol. 3, 1877) is the named edition for this period and discusses Gattinara's
circle, but was not opened to a specific page this pass — the archive.org full-text search cannot cite a page
number for this item, per the Access playbook. A worker with more budget should read the relevant supplement
volume covering late 1527 directly (or the volume's own index for "Burgo") rather than rely on full-text
search alone before this is called blocked. Not found by any of the six sources checked.

Requests this pass: WebSearch 1, archive.org 2 (advancedsearch 1 + be-api fts 1, >=3s apart), github.com 0. No
DECODE login. No promotion, no decoding.

## LANE N audit, 24 September 2026

**DocumentsList check** (`DocumentsList?showmaster=records&fk_id=9970`): **"No records found"** — no
attached document. RecordsView: `Available Documents:` (empty), `Inline Cleartext: Yes`, `Inline Plaintext:
No`. No change to the verdict: still **open**, cryptanalysis. Status word unchanged.

**Edition gap (job 3): CSP Spanish vol. 3.** Identified the correct HathiTrust volume for the letter's date
(26 Oct 1527, per Bourdeau's `CATALOGUE.md` entry 2.5): *Calendar of letters, despatches, and state papers ...
preserved in the archives at Simancas, Vienna, Brussels, and elsewhere*, v.3 pt.2, 1527-1529 (Gayangos, 1877),
HathiTrust id `msu.31293027025760`, 1214 pages (bibliographic search only, catalog.hathitrust.org not queried
directly — found via WebSearch). Ran `tools/htrc_ef_headwords.py msu.31293027025760 --words
burgo,gattinara,ferrara,cipher` (HTRC Extracted Features API, no HathiTrust page view, no login) to place the
correspondence without reading the Cloudflare-gated site. Del Burgo (69 pages), Gattinara (81 pages) and
Ferrara (191 pages) all recur throughout the volume, as expected for its two chief correspondents-adjacent
figures over two years — not by itself a page citation. Narrowed by requiring all three tokens within one page
of each other: **seq 508, 643, 851, 980, 1065, 1105, 1129** (scan sequence numbers, front matter included, so
not printed page numbers). Of these, **seq 508 and seq 980** also fall within one page of a "cipher" token hit,
the two strongest candidates for the entry itself or an adjoining editorial note. **Not read**: HathiTrust's
page images are Cloudflare-gated and out of this brief's host list (data.htrc.illinois.edu and
catalog.hathitrust.org's bibliographic API only); nobody has yet opened seq 508 or seq 980 to confirm this is
the 26 Oct 1527 del Burgo-to-Gattinara letter or check for an "in cipher"/deciphered editorial note. This
narrows "read a 1214-page volume" to "read two candidate pages" for whichever worker has HathiTrust access
next (or the person, via `REQUEST.md` if a login proves necessary) — genuine progress, not a block, and not a
confirmed page citation. Status word unchanged (open); no REQUEST.md written (nothing here needs the person's
direct action yet, only HathiTrust page access which the tool list may open to a future worker).

Requests this pass (job 3 only): WebSearch 2 (PPKE, HathiTrust catalog record), data.htrc.illinois.edu 2
(metadata + pages, one volume, cached to disk), curl direct 0.
