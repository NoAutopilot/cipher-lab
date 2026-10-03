open

**Edition-check resolution, LANE N4 csCOL, 24 Sept 2026 20:13 UTC:** the orchestrator's 20:03 hold is lifted -- Colenbrander's Gedenkstukken V has now been independently read (full-text search, both bands, via `resources.huygens.knaw.nl`'s own OCR search engine, not Bourdeau's web search) for every proper noun in this letter; letter absent. See "Colenbrander Gedenkstukken V -- independent read" below and the Verdict.

# G.C. van Spaen tot Voorstonden to Maarten van der Goes, Düsseldorf, 14–15 January 1808

QUEUE row: CS2-21 (`sources/solver-diffs/2026-09-24-cyphersolver-site.tsv`, catalogue item 226 at
dbourdeau.github.io/cyphersolver/catalogue.html). Check-solved run 24 September 2026 by LANE N4 csNA
(session_01PKTy3iKiH3LzJpQauLb8Wu), brief `.claude/briefs/runs/2026-09-24-lane-n4-csNA.md`. Copy-free per LANE
N4 scARCH (ROOM.md, 24 Sept 2026 19:00 UTC), confirming the exact viewer: Nationaal Archief toegang **2.01.08**
(the row's cached shelfmark carried a stray leading zero, "02.01.08").

## What it is

DECODE R1941, a letter of two pages plus a one-page annex, both in figures between clear Dutch openings and
closings; Nationaal Archief, The Hague, 2.01.08 (Ministerie van Buitenlandse Zaken, 1796–1810), inv. nr. 281.
DECODE's own status for this record is **"Partially decrypted"** (`sources/decode/records-non-decrypted-
2026-09-24.tsv`, id 1941) — a hard filter per LANE N2 addition (c): a `[transc]`/`[decrypt]`/`[key]` document
attached to a DECODE record must be checked via DocumentsList before calling the record open. This worker has no
DECODE login (COMMON rule 4: only the DECODE worker logs in). Bourdeau's own write-up substitutes for that check
(below) — he explicitly examined the record's own note and images and found no attached document.

## Six-source search log (24 September 2026)

1. **Bourdeau, quoted verbatim** (`spaen1808.html`, posted 21 Sept, updated 24 Sept 2026 — same-day fresh):
   *"DECODE catalogues R1941 as a letter from G. C. van Spaen tot Voorstonden, 'ambassador at the Court of
   Westphalia', to Maarten van der Goes, as partly decrypted: its note says the small annex of 15 January was
   deciphered and the letter was not... No decipherment is written on either, and none is attached to the
   record."* This directly answers the "Partially decrypted" hard filter: DECODE's own annotation only claims
   the 15 Jan annex (75 groups) was deciphered elsewhere, not the 14 Jan letter (228 groups) targeted by this
   row, and Bourdeau found no document of either attached to the record.
2. **Standard printed edition — actually read (by Bourdeau, quoted verbatim).** *"Colenbrander's Gedenkstukken V
   does not print the letters."* Gedenkstukken vol. V covers 1806–1810, the correct window for a 14–15 Jan 1808
   despatch. This worker tried independently to reach the same volume: `resources.huygens.knaw.nl/gedenkstukken`
   and `/retroboeken/gedenkstukken/` (a Dojo-based page-image browser, 22 volumes, no plain-text/OCR search
   reachable via curl — its own search box is a client-side Google Custom Search over the whole huygens.knaw.nl
   site, not the volume text); `site:delpher.nl` web search located the correct-era volume
   (`MMSFUBA02:000012292:00048`, "Gedenkstukken... 1795 tot 1840", vol. 4 part 2, 1908) but WebFetch of the
   Delpher page returned only metadata, no OCR text (Delpher's viewer is JS-rendered); archive.org holds no copy
   of Gedenkstukken (`advancedsearch.php` for the title: 0 hits). This worker's own attempt to re-verify
   Bourdeau's Gedenkstukken V check did not succeed this pass; the verdict below rests on Bourdeau's stated
   check of that volume, not an independent re-read of its pages.
3. **DECODE**: no key record for this code (Bourdeau: "DECODE holds no key for this code"; Croiset's 1803
   codebook, R1035, "gives word salad" against it).
4. **Aymeloglu** (fresh shallow clone, 24 Sept 2026): "Spaen"/"Goes" occur only in his raw DECODE catalogue
   scrape files, not in any of his 8 write-ups — not attempted there.
5. **Cryptiana / Tomokiyo** (`sources/cryptiana/web/dutch.htm`, Shift-JIS): "Spaen" occurs once, but for a
   different person and episode — Alexander van Spaen's 1800 Anglo-Prussian mediation negotiations for the
   exiled Orange court, unrelated to G.C. van Spaen tot Voorstonden's 1808 border-commission correspondence.
   "Goes" does not occur.
6. **Web search**: nothing beyond Bourdeau's page and the DECODE/archive metadata found.

Archive context (Bourdeau, corroborated by the NA record itself): inv. 281 holds the papers of J.F.G. van Spaen
and G. van Riemsdijk, commissioners for taking over the districts ceded around Zevenaar (1806–09); Düsseldorf
was the capital of the Grand Duchy of Berg, the other party to that exchange — consistent with a genuine,
un-printed administrative dispatch rather than a document Colenbrander would have selected for a general
political history.

## Colenbrander Gedenkstukken V — independent read (LANE N4 csCOL, 24 Sept 2026)

`resources.huygens.knaw.nl`'s Dojo page-browser has no OCR search reachable by a plain page fetch, but it is
driven by a JSON/query backend that a browser never needs a session for: `pages.json?source=N` lists every page's
image and OCR-HTML URL, and the browser's own `searchText` accessor is a plain GET,
`/retroboeken/gedenkstukken/searchText/index_html?search_term:ustring:utf-8=<term>&source_id=<N>&id=searchText`,
that full-text-searches one volume's OCR and returns snippets with page numbers. The site's dropdown gives the
source-id → volume map directly (fetched once, `toc/index_html?page=1&source=7&id=toc`, 24 Sept 2026): Deel V is
two physical tomes, **source 7 = Deel V, Eerste Stuk, GS 11** (1910, `resources.huygens.knaw.nl/retroapp/
service_gedenkstukken/deel5_band1/`) and **source 8 = Deel V, Tweede Stuk, GS 12** (`.../deel5_band2/`) — this is
the correct edition and window (Bourdeau's own citation, "Colenbrander's Gedenkstukken V (1806-1810)"), confirmed
by reading each volume's own title page (RGP no. 11/12, "VIJFDE DEEL").

Full-text search, both sources, run 24 Sept 2026 (queries 2 s apart, descriptive User-Agent):

| term | source 7 (band 1) | source 8 (band 2) |
|---|---|---|
| Spaen | 0 hits | 3 hits — all "baron van Spaen la Leek", grootmeester der hofjacht (court chamberlain), pp. 575, 733, register p. 842 — a different Van Spaen, unrelated to G.C. van Spaen tot Voorstonden |
| Goes | 19 hits | 25 hits — all Maarten van der Goes in his ordinary role as Secretary/Minister (register entries, footnotes, French-language passages naming him as recipient of other people's letters); none is a 14–15 Jan 1808 Düsseldorf letter, and none co-occurs with "Spaen" in the same snippet |
| Düsseldorf | 1 hit, p. XXII (Inleiding), French troop-movement passage ("reçu l'ordre de se diriger sur Düsseldorf... faire venir... les troupes") | 0 hits |
| Voorstonden | 0 hits | 0 hits |
| Zevenaar | 0 hits | 0 hits |

The register (index of correspondents and subjects, the roman-numeral pages at the front of each tome, e.g.
"p. V", "p. VI") is OCR'd and searched along with the body text — the "Goes" and "Spaen" hits above include
register-page hits, so this is a read of the register as well as the text, per the brief. No sentence in either
tome names G.C. van Spaen tot Voorstonden, Van der Goes as a correspondent of his, Düsseldorf in a diplomatic
(non-military) context, or the Zevenaar/Voorstonden border-commission matter at all. This supersedes and confirms
item 2 of the six-source log above (Bourdeau's own check): the edition itself, not just his search of it, has now
been read for this letter.

## Verdict

**`open -- Colenbrander's Gedenkstukken V, Deel V Eerste Stuk (GS 11, source 7) and Tweede Stuk (GS 12, source
8), full-text search of the whole volume including its register (resources.huygens.knaw.nl/retroboeken/
gedenkstukken/searchText) for Spaen, Goes, Düsseldorf, Voorstonden, Zevenaar, 24 Sept 2026: letter absent.`** No
source claims a key, decipherment or clear copy of R1941's 14 January letter. DECODE's "Partially decrypted"
status is accounted for: it refers only to the 15 January annex, not this letter, per Bourdeau's direct
inspection of the record.

Grade counts: H 0, C 0, S 0, M 0, I 0 (nothing read here; check-solved does not decode). Rule 10: no novelty
claim made; this is a search result, not a verifier's classification.

Credit: D. Bourdeau, cyphersolver, https://dbourdeau.github.io/cyphersolver/spaen1808.html (catalogue item 226;
transcription, archive-inventory identification), CC BY 4.0 — prior attempt, not a solution. The Gedenkstukken V
edition read is this worker's own (huygens.knaw.nl full-text search, not a repetition of Bourdeau's web search).

Requests this pass: `nationaalarchief.nl` 0, `resources.huygens.knaw.nl` ~19 (index page, book_data.js,
book_scripts.js, pages.json probes, two title-page reads, one toc read, 9 searchText queries, all ≥2 s apart —
shared budget with CS2-22 below), `archive.org` 1 (advancedsearch, 0 hits, confirms csNA's prior check),
`catalog.hathitrust.org` 1 (oclc lookup, 0 hits), `github.com` 0 additional, WebSearch 0, WebFetch 0. No DECODE
login used.

Requests carried over from the prior (held) pass: `nationaalarchief.nl` 0 (already pinned by scARCH),
`archive.org` 1 (advancedsearch, shared with CS2-18/-22 checks), `github.com` 0 additional (same clones as
CS2-18), WebSearch 3, WebFetch 1 (delpher.nl, one page, no scraping loop).

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/spaen1808/NOTES.md ; https://dbourdeau.github.io/cyphersolver/spaen1808.html
- Their extent, in their words: still unread; no key on DECODE, nothing in print; "attempted, open"
- Their date: 21 Sept 2026
- Note: already cited in our NOTES.md
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## Web and blog check (GF4-BATCH16, account-4, 3 Oct 2026)

- Web: `"van Spaen" "van der Goes" 1808 Düsseldorf cijfer brief` -- Leiden thesis on Van der Goes van Dirxland
  (scholarlypublications.universiteitleiden.nl item 2948775), **E.J.T.A.M.A. Smit, *De oude Kleefse enklaves en hun
  overgang naar Gelderland, 1795-1817* (diss. Nijmegen 1975, repository.ubn.ru.nl hdl 2066/147708)**, NA inventories
  3.20.16/3.20.17 (Van der Goes family papers), Wikipedia. No decipherment or plaintext of R1941 in any of them; Smit read
  below.
- Web: `Nationaal Archief 2.01.08 inv. 281 Spaen Riemsdijk Zevenaar gecedeerde districten cijferschrift` -- unrelated NA
  inventory PDFs only.
- Web: `DECODE R1941 Spaen Voorstonden cipher 1808 "partially decrypted"` -- only Bourdeau's index ("attempted but not
  deciphered ... 303 groups of a plain code reaching 1339").
- Web (descriptive title): covered by the first query; nothing else.
- Cipherbrain: `site:scienceblogs.de klausis-krypto-kolumne Spaen OR "van der Goes" OR "Koninkrijk Holland" 1808` --
  "Wer löst diese Verschlüsselungen aus dem Jahr 1808?" (14 Feb 2016) is a crypto book's printed puzzles, and the
  Van-Gelder-Kryptogramm (Top-25 no. 10) is Dedem van Gelder at Constantinople, Feb 1809 -- different items; nothing on
  Van Spaen / Van der Goes.
- Cryptiana blog: `site:cryptiana.blogspot.com Dutch cipher 1808 OR "Kingdom of Holland" OR Spaen` -- forum index pages
  (Sept 2025, Henry IV 1590) only; local `sources/cryptiana/web/dutch.htm` already read 24 Sept (different Van Spaen, 1800).
- Cipher Mysteries: `site:ciphermysteries.com Spaen OR "van der Goes" OR "Kingdom of Holland" cipher` -- Willen Styn and
  Van Heeck posts, unrelated.
- Solver repositories, fresh clones 3 Oct 2026: dbourdeau/cyphersolver 841111b (2 Oct) `targets/spaen1808/NOTES.md`
  still reads "The letter is still unread: DECODE has no key for this code and nothing is in print ... 'attempted, open'";
  aaymeloglu/unsolved-ciphers d2800bb (27 Sept): no target, no write-up naming Spaen or R1941.

## Premise check (GF4-BATCH16, account-4, 3 Oct 2026)

- (a) Folder's own mentions of a decipherment: **found, not located.** DECODE's record note says the 15 Jan annex "is
  solved" and sets R1941 to "Partially decrypted"; Bourdeau (quoted above) saw no decipherment on the images and no
  document attached. Nobody has yet listed the record's DocumentsList while logged in (csNA had no login; Bourdeau's
  check is his). Open until a logged-in DECODE pass lists R1941's documents.
- (b) Other solvers' working files: Bourdeau's `targets/spaen1808/` holds `transcription.txt`, `letter_groups.txt`,
  `annex_groups.txt`, `profile.json`, `decode/` -- a transcription and a profile, no rendering, no key applied beyond
  R1035 Croiset 1803 ("word salad"). Not found: no reading. Aymeloglu: none.
- (c) Physical neighbours: **found, not yet viewed.** NA 2.01.08 inv. 281 is fully scanned and public: the inventory page
  (www.nationaalarchief.nl/onderzoeken/archief/2.01.08/invnr/281, fetched 3 Oct 2026) carries 360 scans,
  NL-HaNA_2.01.08_281_0001.jpg to _0360.jpg, each with a service.archief.nl IIIF info.json -- the whole file of the
  commissioners' letters, Jul 1806 - May 1809, not only DECODE's four photos of photocopies. The leaves around the
  14-15 Jan 1808 letter (a ministry decipherment slip, a clear draft, a later letter repeating its content) were not
  located in this pass: four sample scans at 700-900 px (IIIF `full/700,/0`) show the file is not in strict date order --
  _0130 a blank leaf and a P.S. in clear; _0160 a letter ending "Uwe Excellentie ... [signed] van Spaen" in clear (left)
  and Arnhem 8 March 1808 to the Landdrost of Gelderland (right); _0180 Utrecht 3 February 1808 to the King, in clear,
  naming "den Heer van Spaen van Voorstonde" and the commissioners at Wesel, beside a Ministerie van Financiën cover
  "Ingekomen ... 1808, No. 33". So the file runs at least Feb-Mar 1808 around scans 160-180, in clear, and confirms the
  Voorstonden identity used in this folder. Stopped at four images (per-unit cap); the Jan 1808 leaves remain to find.
- (d) Recipient side: the recipient's edition is Colenbrander Gedenkstukken V (BuZa), read 24 Sept (letter absent).
  Smit 1975 (above; pdftotext of the repository PDF, whole-volume grep for januari 1808, Spaen, Düsseldorf, cijfer,
  chiffre, ontcijfer): Hoofdstuk III-B pp. 59-62 narrates the commissioners' Dec 1807 - Jan 1808 position from
  A.R.A. B.Z. (1795-1810) 281 (notes 1-3, 8) with Arnhem and Düsseldorf files -- Van Spaen kept "aan het lijntje" by
  Agar, Murat's instruction of 7 Jan received at Düsseldorf on 13 Jan, Van Spaen joining Van Riemsdijk at Wesel on
  12 Jan, his confidential note to Agar on conscription in the enclaves the same day. No cipher, decipherment or
  quotation of the 14-15 Jan letter; "cijfer" occurs only as population figures. Not found as a decipherment; useful
  as context for a later reader. Smit names the commissioner J.F.W. van Spaen van Biljoen (1746-1827) in his 1802-03
  chapters; this folder and Bourdeau read the 1808 signature as "G. C. van Spaen", and scan _0180 names "van Spaen van
  Voorstonde" in Feb 1808 -- which Van Spaen signed R1941 is for the image reader, not settled here.

Host requests: www.nationaalarchief.nl 1, service.archief.nl 4 (IIIF, 2 s apart), repository.ubn.ru.nl 1 (PDF), github.com 2 clones (shared), WebSearch 6.

## While waiting (GF4-BATCH16, account-4, 3 Oct 2026; refreshed GAPS84, 3 Oct 2026)

Parked on no-key-material (GAPS84). The earlier action here (inv. 281 matched, siblings and clear letters read) is done.
- Action that depends on nobody: grep the public EAD of the King's cabinet archive at the NA (Kabinet des Konings, 1806-1810)
  and of the Berg/Grand Duchy holdings for cijfer/sleutel/chiffre/Spaen units, to find a ministry codebook 1806-1810 outside
  2.01.08 (new material, the only route that reopens the key-rebuild step). S.

## FT4-vanspaen-vandergoes-1808 (3 Oct 2026, account-4): locate the Jan 1808 leaves in NA 2.01.08 inv. 281

Step: premise (c) / While waiting, the action that depends on nobody. Locate the scans only; nothing was transcribed.
- Scan list recorded once: `images/na_2.01.08_281_scans.tsv`. It has 360 rows (order, label, file id, bytes, IIIF
  info.json), taken from the inventory page's `drupal-settings-json` `viewer.response` (www.nationaalarchief.nl, 1
  request, 3 Oct 2026). The archive gives no per-scan labels or dates beyond the file name, so the scan list cannot
  place the January 1808 leaves.
- Contact sheets: 25 IIIF views at 600-700 px wide (`full/600,/0` or `full/700,/0`), 1.6 s apart, all HTTP 200
  image/jpeg. Three vision calls, one sheet each:
  - 184-220, every 4th scan;
  - 120, 140, 150, 164, 168, 172, 176, 181, 182, 183;
  - 40, 80, 260, 300, 340.
  At this size the handwriting can be classed (clear prose, articles, blank, figures) but dates cannot be read.
- What the samples show:
  - No sampled scan carries a page of number groups, so the target's pages (19 lines of figures, a 7-line annex)
    are not among the 25.
  - No sampled scan carries a decipherment slip or a key sheet.
  - Scans 196-204 are numbered articles (Art. 9-11 headings), and 216 is "Articles convenus entre les Commissaires
    de Sa Majesté le Roi de Hollande et de Son Altesse Impériale et Royale le Grand-Duc de Berg ... Sevenaer,
    Huissen et Malburgen". That is the cession convention, so 1806-07 material.
  - Scans 140 and 150 are clear letters signed van Spaen; 150 reads "J.F.W. Baron van Spaen".
  - Scans 172 and 176 are clear letters with other signatures (176 appears to read "v[an] der Goes": a ministry
    minute or copy of an outgoing letter).
  - Scans 40 and 340 are French letters beginning "Monsieur"; scan 40 is signed "J.F.G. de Spaen".
  - Scans 80, 182, 212 and 260 are blank or wrapper leaves.
- File order: the GF4-BATCH16 readings (160 = Mar 1808, 180 = Feb 1808) next to 1806-07 convention material at
  196-216 confirm that the file is not in one date order. It is probably several bundles (convention, the two
  commissioners' letters, ministry minutes) bound one after another. A binary search on dates does not work here.
- Result: the Jan 1808 cipher leaves are **not located** after sampling 25 of 360 scans (7%). That is a search
  result, not an absence. No period decipherment, clear copy or key sheet was seen in the sample. Status unchanged:
  `open`, not found-solved.
- Signature note: Bourdeau's DECODE images are signed "G. C. van Spaen" and were sent from Düsseldorf. The
  commissioners in this file sign J.F.G./J.F.W. van Spaen. The target may be filed apart from the commissioners'
  bundles, or this inv. nr. may hold it only because DECODE's citation says so; the scan list cannot tell which.
- Requests: www.nationaalarchief.nl 1; service.archief.nl 25 images (the cap), 1.6 s apart, no 4xx/5xx. Vision 3.
  Grade counts H 0, C 0, S 0, M 0, I 0 (nothing read).

## FT4b-vanspaen-vandergoes-1808 (3 Oct 2026, account-4): second sampling of NA 2.01.08 inv. 281

Step: the gap "location of the target leaves in inv. 281". Locate only; nothing transcribed. Status unchanged (`open`).
- 25 IIIF views at 450 px wide (`full/450,/0`), 1.6 s apart, all HTTP 200 image/jpeg: scans 185-187, 189-191, 193-195,
  217-219 and 221-233 (the gaps either side of the articles bundle that FT4 sampled every 4th). Two vision calls, one
  contact sheet each (12 and 13 scans).
- What they show (dates read only where large on the page, so treat them as approximate):
  - 185, 187, 189: letters headed "DE COMMISSARIS GENERAAL ... van Gelderland" (printed letterhead), signed by the
    commissaris-generaal, not Van Spaen; 187 and 191 carry a filing note "No 3 / 17 Feb 1808".
  - 193: a Dutch letter with a red wax seal; 194-195 and 217-219: numbered articles (Art. 1-11), the cession articles
    already seen by FT4 at 196-216.
  - 221: a French letter, foot "Wesel le .. Mars 1808 ... de Spaen et ...". 223 and 225: letters headed with a filing
    note "N. 1 [?] Mars 1808" and "Wesel ... Maart 1808"; 224 is signed by the commissioners at Wesel. 226-231: a long
    French memoir, 231 ending "Wesel le 28 Mars 1808". 232-233: inserted smaller slips of Dutch prose on a larger leaf.
  - 186, 190, 222 blank or nearly blank versos.
- None of the 25 carries a page of figure groups, a decipherment slip or a key sheet.
- File order, revised: 180 (3 Feb 1808), 187/191 (17 Feb), 221-231 (March 1808, Wesel) run forward in date. So scans
  180-233 are one bundle in rising date order covering Feb-Mar 1808, with the March articles inside it; FT4's 160
  (8 March 1808) belongs to a different bundle. If the 14-15 Jan 1808 Düsseldorf letter is filed in date order in
  this bundle, it sits before scan 180: the unviewed scans 161-179 (15 scans) and 141-159 are the next place to look.
- Total now sampled: 50 of 360 scans (14%). Not located is a search result, not an absence.
- Requests: service.archief.nl 25 (the cap for this session), 1.6 s apart, no 4xx/5xx; www.nationaalarchief.nl 0.
  Vision 2. Grade counts H 0, C 0, S 0, M 0, I 0 (nothing read).

## FT4c-vanspaen-vandergoes-1808 (3 Oct 2026, account-4): DECODE DocumentsList, then inv. 281 scans 161-179

Step: the Verdict's two named steps (FT4b). Nothing transcribed or decoded. Status unchanged (`open`).
- **DECODE, one browser login** (`tools/decode_browser_login.js 1941 ... --fetch-page DocumentsList,ImagesList`,
  3 Oct 2026 04:45 UTC). Record view: "Documents 0", "Associated Records 0", field "Available Documents" empty,
  Images 4 (IMG_R1941_I13398-I13401, P1-P4, uploaded 13 Jul 2021). `DocumentsList?showmaster=records&fk_id=1941`
  answers "No records found". The only text behind DECODE's "Partially decrypted" is the record's Additional
  Information note, quoted as served (typos the site's): *"The letter itself is onsolved, only a small anne, dated
  15 January of the same year is. With 4 d9g9t numbers, the nomenclator seems a little unfaailiar, not tyically a
  nomenclator made by Croiset."* Other fields: Plaintext language French, Cleartext Dutch; Cipher type
  Nomenclatures; author given as "Gerard Carel baron van Spaen tot Voorstonden, ambassador of the King of Holland
  ar rhe Court of Westphalia". So: no decipherment of this item (letter or annex) is served by DECODE; the note
  asserts the annex was solved but cites no source and attaches nothing. Not found-solved. Saved pages and the four
  thumbnails stayed in the session scratchpad (account name in the page header; not committed). The note's
  "Plaintext: French" is a catalogue field, not a reading -- a hint for a later key attack, grade nothing.
- **NA inv. 281 scans 161-179**, IIIF `full/450,/0`, 19 views (15 new; 164/168/172/176 re-viewed beside their
  neighbours), 1.6 s apart, all HTTP 200 image/jpeg; two contact sheets, two vision calls.
  - 161-172: one long Dutch report in clear, running page to page with catchwords at the foot of each page; ends on
    172 with a closing formula and signature (not read at this size).
  - 173: blank. 174 and 178: small cabinet extract slips ("Uit het Register ..." heading, "No 14" / "No 1.."),
    pinned on cover sheets addressed "Sire" / "Aan den Koning". 175: a letter "Sire" with a dated report heading
    (year not legible at 450 px). 176: a short letter "Sire", signed. 177, 179: covers "Aan den Koning".
  - So 161-179 is ministry-to-King material (a report plus covering letters and cabinet extracts), not
    commissioners' or envoys' despatches; it continues into 180 (3 Feb 1808, to the King, FT4/GF4).
  - None of the 19 carries a page of figure groups, a decipherment slip or a key sheet.
- Total inv. 281 viewed now 65 of 360 scans (18%). Not located is a search result, not an absence.
- Requests: de-crypt.org 1 login + 2 pages + 4 thumbnails (auto, --max-files 6), 1.5 s apart;
  service.archief.nl 19 (of the 25 cap), no 4xx/5xx; www.nationaalarchief.nl 0. Vision 2.
  Grade counts H 0, C 0, S 0, M 0, I 0 (nothing read).

## GAPS26-vanspaen-vandergoes-1808 (3 Oct 2026, account-4): inv. 281 scans 141-159, then 100-136

Step: the Verdict's cheapest step. Locate only; nothing transcribed or decoded. Status unchanged.
- **Scans 141-159**, IIIF `full/450,/0`, 19 views (18 new; 150 re-viewed), 1.6 s apart, all HTTP 200 image/jpeg; one
  contact sheet. Then four header crops (`pct:50,3,50,14/700,`) of 141, 151, 153, 159 on one sheet to read dates.
  - All clear prose: Dutch letters "Hoog Edel Gestrenge Heer" and French letters "Monsieur", several signed van Spaen
    (142, 150, 151, 153), 146 and 156 signed by another hand ("Le Baron de ...", not read), 154-155 a French
    formal act with a calligraphic initial. 147, 157, 158 blank.
  - Headers read from the crops: 141 "Wezel, [1]8 Mars 1808"; 151 "Wezel den 15 Maart 1808 des avonds", docket
    "718 / Ontv. 17 Maart 1808"; 153 "Wezel den 15 Maart 1808", docket "717 / Ontv. 17 Maart 1808"; 159 "Wezel den
    16 Maart 1808", docket "730 / Ontv. 18 Maart 1808". So 141-159 is the Wesel commissioners' correspondence of
    mid-March 1808, with ministry receipt numbers 717-730.
- **Scans 100-136**, same size, 37 views (36 new; 120 re-viewed), all HTTP 200; one contact sheet (7 columns,
  330 px per spread, so headers are read only approximately).
  - Clear letters in Dutch and French, many signed van Spaen beside a second commissioner's signature (105-109,
    118-121, 128, 133-134); headers that look like "Wezel ... Januarij/Janvier 1808" at 100, 105, 107, 109, 127 and
    "... Feb 1808" at 114, 117 (approximate at this size, not read). Ruled tables in words and sums at 102-103 and
    123 (a statistical return), not figure cipher. Blank or near-blank: 110, 116, 122, 126, 129.
  - None of the 37 carries a page of figure groups, a decipherment slip or a key sheet.
- So 100-159 is the Wesel commissioners' bundle, January to mid-March 1808, in clear. January 1808 material is
  filed around 100-109, but it is Wesel, not Düsseldorf, and none of it is in figures. The target (G.C. van Spaen,
  Düsseldorf, 14-15 Jan 1808) was not seen in 100-136 or 141-159.
- Total inv. 281 viewed now 119 of 360 scans (33%): FT4 25, FT4b 25, FT4c 19, GAPS26 54 new. Not located is a
  search result, not an absence.
- Requests: service.archief.nl 60 (19 + 4 header crops + 37), the session cap, 1.6 s apart, no 4xx/5xx;
  www.nationaalarchief.nl 0. Vision 3 (two contact sheets, one header sheet). Grade counts H 0, C 0, S 0, M 0, I 0.

## GAPS34-vanspaen-vandergoes-1808 (3 Oct 2026, account-4): inv. 281 scans 137-139 and 75-99; figure leaves located

Step: the Verdict's cheapest step, batch 1 (137-139 + 75-99). Locate only; nothing transcribed or decoded. Status unchanged.
- 102 IIIF views at `full/450,/0` (137-139, 75-99, 50-74, 25-49, 1-24 in that order), 1.6 s apart, all HTTP 200
  image/jpeg. Only the first batch (28 scans, one contact sheet) was viewed: it held figure leaves, and the brief says
  stop there. **Scans 1-74 were fetched but not viewed** (not committed; re-fetchable from the scan list).
- **Figure leaves found: scans 81, 82 and 85.** Native size fetched once (5000 px wide), committed as
  images/NL-HaNA_2.01.08_281_0081/0082/0085.jpg with images/manifest.json. Headers read from one crop sheet of the
  tops of 81 and 85 (not a transcription):
  - 81 (right page): "No 4" / "Dusseldorf, den 12 January 1808" / ministry docket "105 Ontv. 14 January 1808" /
    "Hoog Edele Gestrenge Heer," then rows of figure groups (about 11 rows of 12, groups 2-4 digits, some with a
    stroke, e.g. "729-"); 82 (left page) continues with about 6 rows, then a clear Dutch closing signed
    "G.C. van Spaen". About 17-19 rows over two pages, as DECODE describes the letter (19 lines of figures).
  - 85 (right page): "No 6" / "Dusseldorf, den 15 January 1808" / docket "136 Ontv. 18 January 1808" /
    "Hoog Edel Gestrenge Heer," then 7 rows of groups, clear closing, signed van Spaen. Matches the one-page,
    7-line annex of 15 Jan.
  - So DECODE's "14 January" letter is most likely No 4, written 12 Jan and received 14 Jan (the docket date), and
    its "annex" of 15 Jan is a separate numbered dispatch, No 6. Identity with Bourdeau's transcription is NOT yet
    checked group by group (first groups seen: 81 row 1 "874. 729-. 821. 776. 826. 752. 1155. 956. 729-. 572. 58. 608.";
    85 row 1 "270. 887. 841. 330. 374. 1075. 996. 623. 615. 442. 1076-. 217." -- read at reduced size, grade M,
    for matching only). Shared groups between the two (602 441 373, 424, 996) are consistent with one code.
- Neighbours in 75-99, all clear (no decipherment slip, no key sheet, no interlinear figures seen): 75-80 French and
  Dutch letters of January 1808, 83 a French letter docketed "1?? Ontv. .. January 1808" signed van Spaen beside a
  second signature, 84 a long French text, 86 and 88 blank, 87 a short French note signed van Spaen, 89-91 and 93-94
  French and Dutch letters docketed January 1808 (91 Dutch, signed G.C. van Spaen), 97 Dutch "Wesel den 19 January
  1808", 98-99 long letters (99 headed "Wesel ... January 1808"). 137-139: Wesel, March 1808, clear.
- The numbering (No 4, No 6) shows a numbered Düsseldorf dispatch series: No 5 and No 1-3 (and any later numbers)
  are sibling dispatches by the same writer to the same ministry, possibly partly in the same figures, and the clear
  French/Dutch letters around them (83, 87, 89-94) are the obvious crib candidates for the same news. Not checked.
- Total inv. 281 viewed now 147 of 360 scans (FT4 25, FT4b 25, FT4c 19, GAPS26 54, GAPS34 28 new incl. 137-139).
- Requests: service.archief.nl 105 (102 at 450 px + 3 native), under the 110 cap, 1.6 s apart, no 4xx/5xx; no other
  host. Vision 2 (one contact sheet, one header-crop sheet). Grade counts H 0, C 0, S 0, M 0, I 0 (nothing read;
  the two quoted first rows are for matching only).

## GAPS36-vanspaen-vandergoes-1808 (3 Oct 2026, account-4): scans 81-82/85 matched row by row to Bourdeau's transcription

Step: the Verdict's cheapest step. Line crops cut from the committed natives with
`python3 tools/iiif_lines.py --image images/NL-HaNA_2.01.08_281_0081.jpg --region 2420,760,2480,3500 --prefix s81
--max-width 2480 --distance 190 --prominence 40 --out images/lines_gaps36 --debug` (likewise 0082 `600,380,2000,1450`
s82; 0085 `2620,1250,2380,1950` s85, and `2620,1000,2380,400` s85top for the annex's first row, which the first 0085
region missed): 28 crops, 1.1 MB. Two blind Opus passes over the crops only (A forward, B reverse order), neither shown
Bourdeau's file, then a reconciliation by this worker from the crops. Files: `gaps36/reconciled.tsv` (the image reading),
`gaps36/compare.py` (`--check` exits 0), `gaps36/compare.tsv`. Bourdeau's files snapshotted unmodified at
`sources/cyphersolver/2026-10-03/spaen1808/` (HEAD a439937; credit D. Bourdeau, cyphersolver, CC BY 4.0).

- **Identity confirmed.** The image's 26 figure rows (19 letter on scans 81-82, 7 annex on scan 85) are Bourdeau's 26
  rows in the same order and line breaks. DECODE R1941's "14 Jan letter" is NA No 4 (Dusseldorf 12 Jan, received 14 Jan),
  and its "15 Jan annex" is No 6.
- **Pass agreement:** A and B gave the same groups on all 25 rows both read (296 groups). They differed only in "?"
  alternatives and in one dash. Each pass's uncertain groups: 885?/548?/1197? (A); 387?/1138?/1339?/613?/1165?/548?/455?/
  1197?/693?/1093? (B). The reconciler kept the shared reading at every one. Two remain open: 455 (middle digit
  overwritten, 3/5) and 1197 (or 1191).
- **Against Bourdeau: 283 of 303 of his groups agree (93.4%).** The image has 304 groups: 19 of his groups are read
  differently, and one is missing from his row 13. He read them from DECODE's photographs of photocopies, so
  rule 2 (image over transcription) applies:
  - row 4 793->795; row 12 392->592; row 13 **134 missing** (image: ...373 134 1125...; his row 13 has 11 groups, the
    image 12); row 15 306->506; row 16 293->493; row 17 62->64, 324->334, 275->375; row 18 541->511 (with a dash);
    row 19 836->886, 457->455?; annex row 1 142->442; annex row 4 1075->1073, 462->464; annex row 5 1293->1093,
    291->491, 391->521, 276->376; annex row 6 823->623, 142->442; annex row 7 275->375.
  - In the confusions, his 2 is read as 4 or 3 eight times, 3 as 5 three times, and 1 as 4 twice. So the hand's 2/3/4
    under photocopy is the weak point, more than the 3/5 his note warned of.
  - Statistics that change: 442 now occurs twice in the annex (his 142 twice); 493 rises from 6 to 7; 375 occurs 3 times
    in all (his 275 twice). The trigram 602 441 373 is unchanged (three times). The group 134 occurs twice: letter row
    13 and the letter's last group.
- **His uncertain groups:** his letter_groups.txt and annex_groups.txt carry no "?" mark (transcription.txt's header
  says uncertain readings are marked "?", but none is). So there was no flagged group to settle. The image corrects
  the 20 differences above instead.
- **No decipherment, interlinear or marginal gloss** on scans 81, 82 or 85. Both passes and the reconciler saw only
  show-through of figures from the verso (s81 L02-L06, s82 L03-L04), a few blots, and a colon after 785 and after
  1165-. No key material on these leaves.
- Annex closing, read from the crop: "Ik heb de eer met de volmaakste hoogagting te verblyven, / HoogEdele Gestrenge Heer,".
- Grades: no plaintext reading, so H 0, C 0, S 0, M 0, I 0 (ciphertext only). Of the 304 image groups, 302 have
  both passes agreeing and 2 are uncertain (455, 1197).
- Vision calls: 2 blind passes + 1 reconciliation (the worker's own views of three composites). Requests: github.com 1
  sparse clone (Bourdeau's files were not on disk); no archive host contacted.

## GAPS41-vanspaen-vandergoes-1808 (3 Oct 2026, account-4): inv. 281 scans 1-74 viewed for dispatches No 1-3 and 5

Step: the Verdict's cheapest step. Locate only; nothing transcribed or decoded. Status unchanged.
- The 450 px views of scans 1-74 fetched by GAPS34 were not on disk (not committed; that container is gone), so they were
  fetched again once: 74 IIIF views at `full/450,/0`, 1.6 s apart, all HTTP 200 image/jpeg. Viewed as three labelled
  contact sheets (1-25, 26-50, 51-74).
- **No figure page, decipherment slip or key sheet in scans 1-74.** Every leaf is clear French or Dutch prose, blank, or
  a cover: 1 is the dossier cover (Van Spaen, commissaris ...), 52 is a printed German "Publicandum" of the
  Grossherzogthum Berg, 65-66 a long Dutch text, 46 and 48 short covering notes. No leaf shows the spaced rows of 2-4
  digit groups that scans 81, 82 and 85 show at the same size.
- One header-crop sheet (9 requests, IIIF `pct:48,0,52,22/1000,`, right-hand page tops of 58, 60, 64, 67, 68, 69, 71,
  73, 74). Header readings (grade M, for locating only):
  - **67: "No 2. Dusseldorf, ce 5 Janvier 1808", docket "44 Ontv. 7 January 1808", "Monsieur", French, in clear.**
    So No 2 of the numbered Dusseldorf series exists and is not in figures.
  - 73/74 (the same leaf, two captures): "104 Ontv. 14 January 1808" / "Dusseldorf ce 12 Janvier 1808" / "Le soussigné
    Commissaire du Roi de Hollande pour la mise en possession des Territoires de Huessen, Malburg et Zevenaar ..."
    -- a clear French note of the same date as No 4 and docketed one number before it (No 4 is "105 Ontv. 14 January
    1808"). The nearest crib candidate seen so far.
  - 64: "13. Ontv. 7 January 1808", "Le premier Commissaire de Sa Majesté le Roi de Hollande pour la mise en possession
    des Districts de Huessen et Zevenaar à ..."; 71: "65 Ontv. 10 January 1808", same heading; 68: "(Copie)", "44 bis
    Ontv. 7 Jan. 1808", "Sa Majesté le Roi de Hollande a donné ordre au Soussigné de se rendre à Dusseldorf ...";
    69: continuation of 68. All clear.
  - 58: "No 8 Ontv. 16(?) Dec 1807"; 60: "No 2 Ontv. 28 Dec 1807" -- clear letters received in December 1807; whether
    these numbers belong to the same Dusseldorf series (60 would then be a second "No 2") or to another writer's was
    not settled at this size.
- **Not found in scans 1-74:** No 1, No 3 and No 5 of the Dusseldorf series. Only the nine headers above were read at a
  legible size; the other leaves' headers are illegible at 450 px, so a numbered letter elsewhere in 1-74 is not
  excluded, but none of them is in figures.
- Total inv. 281 viewed now 221 of 360 scans (147 before + 74).
- Requests: service.archief.nl 83 (74 at 450 px + 9 header regions), 1.6 s apart, no 4xx/5xx; no other host. Vision 4
  (three contact sheets, one header sheet). Grade counts H 0, C 0, S 0, M 0, I 0 (nothing read as plaintext of the target).

## GAPS44-vanspaen-vandergoes-1808 (3 Oct 2026, account-4): clear siblings of No 4 read for a crib

Step: the Verdict's cheapest step (scans 73/74 and 67 at native size, read for a crib to No 4). No crib attack run. Status unchanged.
- Natives fetched once (`full/full`, 5000 px): scans 67, 73, 74; scan 73/74's note 104 turned out to be covered by an
  inserted slip, so 72 and 75 were viewed at 900 px, and 75 (No 3) and 76 (its continuation) fetched at native too. All
  in images/ with images/manifest.json (folder 17 MB).
- Crops: `python3 tools/iiif_lines.py --image images/NL-HaNA_2.01.08_281_00NN.jpg --region R --prefix P --ink 195
  --distance 100 --prominence 20 --lines-per-crop 3 --debug --out images/lines_gaps44` with (NN, R, P) = (67,
  2520,180,2340,4110, s67r), (73, 2550,180,2430,810, s73hdr104), (73, 2550,990,2220,2550, s73slip102), (74,
  2550,180,2430,1000, s74hdr104), (75, 2390,110,2580,4170, s75r), (76, 110,110,2420,4040, s76l), (76, 2530,110,2420,1400,
  s76r): 52 crops (the default ink threshold found no lines in the faint brown ink; 195 did). Two blind Opus passes over
  the crops only (gaps44/passA.tsv forward, passB.tsv reverse): word agreement 2314 of 2416 (95.8%). Reconciliation by
  this worker from two crop composites: gaps44/reconciled.md.
- **The 12 Jan 1808 cluster.** Dockets 102, 103, 104 and 105 were all received ("Exh.") on 14 January 1808 and all are
  dated Dusseldorf 12 January (No 3's own date line reads "1807", a slip):
  - 102: a clear slip, G.C. de Spaen thanks the Minister for an indemnity of 6,000 florins (letter of the 4th).
  - **103 = "No 3"** (scans 75-76), clear French, signed G.C. de Spaen: daily allowance of 30 florins (Arrêté of 29 Dec);
    the talk with Minister Agar on Saturday about the treaty on the cession of Sevenaar (ratified by the Emperor before
    he left for Italy, ratifications exchanged at Paris on 31 Dec, the treaty at Utrecht a week ago) -- Agar knew nothing
    of it, nor of the ratification of the Emperor-Grand Duke treaty; the Note and the "lettre de notification" await
    the Grand Duke's decision; rumour of the Grand Duke's arrival "dans peu ou vers le printems"; deputations of the
    County of the Mark[?] and of Munster gone to Paris; the flag ceremony of the Grand Duke's new infantry regiment
    (Epiphany, 6 Jan) by Count Nesselrode, Interior Minister acting for War and Justice; battalions to Munster, Anclam and
    Pomerania; the Grand Duchy's administration not yet organised, Mr Rappaert[?] influential; rain and an earthquake.
  - 104: a formal Note, "Le soussigné Commissaire du Roi de Hollande pour la mise en possession des Territoires de
    Huessen, Malburg et Zevenaer"; only the header is visible -- the body is covered by slip 102 on scan 73 and by
    another leaf on scan 74, in both captures.
  - **105 = No 4**, the target, in Dutch-framed figures, written the same day straight after No 3.
- **67 = "No 2"** (5 Jan 1808, docket 44, Exh. 7 Jan), clear French, first page only on scan 67: Spaen handed Agar a
  Note setting out the King's motives and "la proposition dont Sa Majesté m'a chargé" (copy enclosed); Agar could not
  receive it officially (not authorised; Spaen not yet accredited) but would pass a copy to the Grand Duke; Agar agreed
  the frontiers of the two States are defective and that "des limites naturelles, assurées, durables" are in both
  States' interest. Its continuation is not on scan 67 (68-69 are a "(Copie)" docketed 44 bis, GAPS41).
- Writers: scan 72 / 67 left (docket 43, 2 Jan 1808) is signed by another de Spaen, read "J.F.G. de Spaen de
  Biljoen[?]" from the 900 px view (M); No 3, slip 102 and No 4 are signed G.C. (van/de) Spaen.
- **Crib candidates** for No 4, ranked, with source lines: gaps44/crib_candidates.tsv (Agar; Grand Duc/Son Altesse;
  Empereur; le Roi; Sevenaar/Huessen/Malburg; traité, ratifications, 31 Décembre, Paris, Utrecht; Note, notification,
  mise en possession; frontières/limites; Nesselrode; places). The likely shape: No 4 carries the part of the Agar
  talks that No 3 left out of the clear text. The code has values 15-1339 (216 distinct of 304 groups), so a crib is a
  word or name list, not a letter string; No 4's language under the figures (Dutch, like its clear frame, or French,
  like No 2/No 3) is not known.
- Not found: No 1 and No 5; the body of note 104; any decipherment, interlinear figure or key on 67, 72-76.
- Grades: no reading of the target, H 0, C 0, S 0, M 0, I 0. The sibling clear text is diplomatic, not graded per token.
- Requests: service.archief.nl 7 (5 native, 2 at 900 px), 1.6 s apart, all 200. Vision: 2 blind passes + 1
  reconciliation (plus this worker's own small overview views of 67, 72-76).

## GAPS48-vanspaen-vandergoes-1808 (3 Oct 2026, account-4): crib placement under a one-part code hypothesis

Step: the Verdict's cheapest step. Disk only, no vision calls, no requests. Pre-registered in `gaps48/PREREG.md`
(commit d0e47f7f, pushed before the target was scored); script `gaps48/crib_place.py` (`--check` and `--kmatch --check`
exit 0); results `gaps48/results.tsv`, `gaps48/results_kmatch.tsv`; row in HYPOTHESES.md. Ciphertext: the GAPS36 image
reading, No 4 letter 229 + No 6 annex 75 = 304 groups, 216 distinct.
- **design_prior.py** first (`gaps48/design_prior.txt`): multi-sign d=1.12 nearest, not above null; mixed 1.62; letter
  2.23; code(numbers) 2.72 excluded; false-positive rate 0.05; nearest keys hellen-frederick-1752 sibling (mixed),
  huntington-luzerne-1781 (syllabary), vanbeuningen-dewitt-1657 (nomenclator). A large nomenclator table, in line
  with GAPS44. One-part vs two-part cannot be told apart by these label-free statistics.
- **Test.** For each GAPS44 crib (FR: agar grand duc empereur roi sevenaar traite ratifications paris utrecht note
  limites; NL: agar groot hertog keizer koning zevenaar tractaat ratificatie parijs utrecht nota grenzen), predicted value
  = alphabetical rank in a 1325-entry corpus vocabulary (fr1810 or nl18) scaled to 15-1339; S1 = AUC of the crib's
  distance to the nearest group in the text against 300 random content-word decoys.
- **Control (rule 3).** Synthetic one-part codes built from the other half of the corpus files, 20 seeds per language,
  304 groups each; a two-part (random order) control on the same passages, which can and does read differently.
  - One-part S1: 0.638 FR, 0.636 NL, against the pre-registered gate of 0.75. **CONTROL BELOW GATE.**
  - Two-part S1: 0.496 FR, 0.509 NL (G0 ok, the statistic does measure order).
  - The pre-registered control was not K-matched (synthetic K 89 FR / 72 NL vs the target's 216), because spelled-out
    out-of-vocabulary words repeat letter groups. A post-hoc K-matched variant (`--kmatch`, not pre-registered,
    out-of-vocabulary word -> one group at its alphabetical place, K 163 / 184) reads one-part 0.745 FR / 0.690 NL,
    two-part 0.460 / 0.433: still below the gate. Decoy distance <= 3 rate 0.57-0.62 at K-matched density; that is
    the reason. With 216 of 1325 values occupied, almost any predicted value has a group within a few units.
  - Ceiling check: the control is not at ceiling (0.64-0.75), so the gate failure is lack of power, not saturation.
- **Target:** S1 0.401 FR, 0.466 NL (S2 0.509 / 0.487). Both are at or below the two-part null mean, and both are below
  the two-part p95 (0.575 FR, 0.611 NL), so they would not have passed even if the gate had held. Logged as **non-test,
  untestable by crib placement at N 304** (rule 3), not as a negative against a one-part code.
- Per-crib predicted value / distance (FR): agar 31/13, grand 606/2, duc 423/1, empereur 446/1, roi 1136/2,
  sevenaar 1180/10, traite 1257/47, ratifications 1077/1, paris 907/6, utrecht 1282/57, note 849/2, limites 724/1.
  The values 1257-1339 are sparse in the text (traite and utrecht both d 47-57). These are not candidates: no PASS.
- Not found: any sign that the GAPS44 cribs sit at their alphabetical places. Not tested: names in a separate section
  (common in period nomenclators), or a vocabulary that is not uniform over the alphabet.
- Grades: H 0, C 0, S 0, M 0, I 0 (no reading). Vision 0; subagents 0; requests 0.
- `python3 tools/gaps_check.py vanspaen-vandergoes-1808`: "OK keep-going vanspaen-vandergoes-1808: keep going: 1 internal
  gap(s), 1 step(s) untried", exit 0.

## GAPS54-vanspaen-vandergoes-1808 (3 Oct 2026, account-4): one-part frequency-position test

Step: the Verdict's cheapest step. Disk only, no vision calls, no subagents, no requests. Pre-registered in
`gaps54/PREREG.md` (commit 4b06e0f0, pushed before any control or target score); script `gaps54/freq_pos.py`
(`--check` exits 0); results `gaps54/results.tsv`; row in HYPOTHESES.md.
- **Statistic.** S = mean distance from each group occurring >= 3 times (19 groups in the target) to the nearest
  alphabetical place of the 15 commonest corpus words (FR fr1810, NL nl18), places scaled to 15-1339 as in GAPS48.
- **Control first (rule 3).** K-matched synthetic one-part codes (out-of-vocabulary word -> neighbour entry, K 166 FR /
  177 NL against the target's 216), 40 seeds; two-part null on the same design, 200 seeds. Gate G1: >= 80% of one-part
  seeds below the two-part p05.
  - FR: one-part S mean 40.5, two-part mean 62.7, p05 43.8, **power 0.675**. NL: 30.1 vs 47.0, p05 31.3,
    **power 0.625**. **G1 FAIL in both languages** (G2 ok). The secondary top-10 variant (reported, not gated) reads
    0.825 FR / 0.675 NL; it was not promoted to the gate after the fact.
- **Target not scored** in either language: logged as **untestable at N 304 by this statistic**, not as a negative.
- Why: with 304 groups the commonest groups occur only 3-7 times, so the one-part frequency list is diluted by
  content words, and 15 function-word places spread over 1325 values sit about 40 apart, close to the null distance.
- With GAPS48, both cheap one-part tests are now non-tests at N 304. Not tested: names or syllables in a separate
  section, non-uniform spacing, two-part codes (no statistic for those exists without a crib match).
- Grades: H 0, C 0, S 0, M 0, I 0 (no reading). Vision 0; subagents 0; requests 0.

## GAPS58-vanspaen-vandergoes-1808 (3 Oct 2026, account-4): inv. 281, the last 139 unviewed scans

Step: the Verdict's cheapest step (locate No 1 / No 5 or a key sheet in the unviewed scans of inv. 281). Locate only;
nothing transcribed or decoded. Status word unchanged.
- Viewed set checked on disk first (NOTES.md, not the brief): 221 of 360 viewed; the 139 unviewed were 197-215 (the
  scans between FT4's every-4th sample), 234-259, 261-299, 301-339 and 341-360.
- 139 IIIF views at `full/450,/0`, 1.6 s apart, all HTTP 200 image/jpeg (0 errors). Not committed (re-fetchable from
  images/na_2.01.08_281_scans.tsv). Four labelled contact sheets (35/35/35/34 scans), four vision calls; no header
  crops were needed, since nothing called for a closer look.
- **No page of figure groups, no decipherment slip and no key sheet in any of the 139.** At this size a figure page
  is unmistakable (spaced rows of short number groups, as on 81/82/85); none appears. What they hold:
  - 197-205: numbered articles (the cession convention bundle FT4 sampled), 205 with a red wax seal; 206 blank.
  - 207-259 and 261-270: clear Dutch and French letters, most headed "Wesel den .. Maart/April 1808" and "Hoog Edel
    Gestrenge Heer", several signed jointly by the two commissioners (van Spaen and a second signature).
  - 271-272, 286-287, 302, 322: tables and accounts in money columns (financial statements; 283-285 carry
    "Algemeen Overzigt" headings), not cipher.
  - 273-360: further clear letters, notes ("Note") and memoirs of about April-May 1808 and later, blanks (e.g. 297,
    298, 304, 308, 319, 323-325, 330, 334, 338, 339, 344, 345, 350-351), and at 357-360 the end of the volume with
    the archive's "Inventaris 281" slip and the back board.
  Dates read only at thumbnail size: approximate, not quoted.
- **Not found in scans 197-360:** dispatches No 1 and No 5 of the Düsseldorf series, any other figure page, any
  decipherment, interlinear figures or key. With GAPS41 (1-74), GAPS34 (75-99) and the earlier passes, **all 360 scans
  of inv. 281 have now been viewed at least at 450 px**; the only figure leaves in the file are 81, 82 and 85 (No 4
  and No 6). No 1 and No 5 are either in clear and missed at thumbnail size, filed elsewhere, or lost -- the file
  cannot say which. Not located is a search result, not an absence.
- Requests: service.archief.nl 139 (cap 220), 1.6 s apart, no 4xx/5xx; no other host. Vision 4 (four contact
  sheets); subagents 0. Grade counts H 0, C 0, S 0, M 0, I 0 (nothing read).

## GAPS61-vanspaen-vandergoes-1808 (3 Oct 2026, account-4): NA catalogue pass for a Van Spaen key or ministry decipherment

Step: the Verdict's cheapest step (new material in another inventory). Catalogue only; nothing transcribed or decoded.
Clock read 08:25-08:32 UTC, 3 Oct 2026. Status word unchanged.
- **NA 2.01.08 finding aid, whole EAD** (`www.nationaalarchief.nl/onderzoeken/archief/2.01.08/download/xml`, 545
  described units, parsed to TSV, 1 request): **no unit anywhere in 2.01.08 carries "cijfer", "chiffre", "sleutel",
  "ontcijfer", "dechiffr" or "code"** in its title or note (grep of the raw XML, archdesc text included). The ministry
  archive 1796-1810 has no key or cipher-book series. Units near the target, all with availability DIGITALIZED read
  from each item page's `drupal-settings-json` `viewer.response` (6 requests):
  | inv. | what (EAD title) | scans | why it matters |
  |---|---|---|---|
  | 20 | Minuut verbaal van ingekomen stukken, 1808 1e halfjaar | 600 | the minister's daily register of incoming pieces (one header view, scan 25: printed form "Verbaal van den Minister van Buitenlandsche Zaken", columns No / Ingekomen stukken / Gerenvoyeerd aan den / Aanteekeningen; that spread blank). No 4 (exh. 14 Jan) and No 6 (exh. 18 Jan) should each have an entry; whether the entry summarises the deciphered content is not seen |
  | 88 | Gewone en geheime minuten van uitgaande missiven, jan-mrt 1808 | 714 | Van der Goes's replies; one header view, scan 25: minute "No 2 ... à Son Excellence Monsieur Brantsen ... Paris, 5 Janv. 1808", French, clear. The reply to No 4/No 6 would follow shortly after |
  | 99 | Verbalen van uitgaande stukken, 1808 | 656 | register of outgoing pieces |
  | 115 | Brievenboek gewone uitgaande brieven, 2 jan - 30 jun 1808 | 580 | letter-book copies (ordinary letters only) |
  | 273 | Westphalen: incl. D. van Hogendorp, minister-plenipotentiary to the King of Westphalia, 26 dec 1807 - 16 jan 1808 | 547 | the Van Hogendorp whose cipher underlies inv. 226 below; same weeks as No 4 |
  | 282 | Varia Duitsland: incl. "Missiven van ministers van de Groothertog Van Berg, commissarissen tot de grensregeling der gecedeerde districten, 1806-1810" | 646 | the Berg (Düsseldorf) counterpart side of the same cession |
  Also in the EAD and already known: inv. 244-248 (G.C. van Spaen, envoy at Vienna, 1802-1807) and 281 (the target).
  No secret-register series ("Geheim") continues past 1805 (inv. 47-64 stop at apr 1805).
- **Van der Goes family papers**: NA 3.20.16 (Van der Goes, ca. 1650-1811; 35 units) and 3.20.17 (Van der Goes van
  Dirxland, 1419-1928; 242 units), both EADs fetched (2 requests) and grepped: personal, family and seigneurial papers
  only (Maarten van der Goes's diplomas, a 1806 letter from Louis Napoleon, Dirksland papers); **no ministerial
  correspondence, no cipher, key or Van Spaen item**.
- **NA cross-inventory search** ("Spaen", `onderzoeken/zoeken`): the result list is rendered client-side from
  zvt.nationaalarchief.nl (page plus its main.js fetched, 2 requests; no plain endpoint found in the bundle); the headless
  browser could not be used (Chromium lacks the proxy CA in this container and the one-off certutil install hung, so it
  was stopped). **Not searched: a Van Spaen family archive or any other NA toegang by name** -- a person or a browser
  session can run that query.
- **Key-material lead found in the repository, not new to it** (`ciphers/roell-vandedem-1809/NOTES.md`, LIKELY-7, 2
  Oct 2026, from the NA 1.02.13 EAD): NA 1.02.13 (Legatie in Rusland) **inv. 226**, Six van Oterleek's minutes 1808-1809
  "In cijfercode op basis van het cijfer van Van Hogendorp", and **inv. 228** "Cijfer, 1803 aug. 5", both not digitised
  (no dao). On DECODE these are **R1033** (Decrypted, Cipher, "legatie Rusland, inv.nr. 226", 1808-1810, Dutch, 16
  pages) and **R1035** (the Croiset 1803 codebook, inv. 228, which Bourdeau ruled out: marked three-digit groups to
  999, word salad on the annex). R1033 is a *decrypted 1808-1810 ministry code derived from* the 1803 book; whether it
  is the same design as R1941 (unmarked groups 15-1339) is unknown from the listing. Bourdeau's check (sources/
  cyphersolver/2026-10-03/spaen1808/NOTES.md) names only key records ("DECODE key records dated 1780-1815 at Dutch
  holders"); R1033 is a cipher record, so it was not in that set. Also seen: the Tartu repository item "The Codebook of
  Willem Six van Oterleek: Dutch Diplomatic Intelligence from Saint Petersburg between 1806-1810" (cited by title in
  `ciphers/na-raad-azie-1800/NOTES.md`; not opened here).
- **DECODE login-free listing** (on disk, `sources/decode/keys-all-2026-09-28-merged.tsv`, 6,324 key records, and the
  24 Sept records-decrypted / non-decrypted listings; 0 new requests): Dutch-holder or Dutch-language **keys** 1780-1815
  are R1035 (NA, 1803), R1024 (KHA, 1782), R1891 (Museum voor Communicatie, 1798), R2233 (KHA, 1801), R2235/R2240
  (KHA Willem V, 1795-99) -- all Orange-court or pre-1804, none after 1803 from the Kingdom of Holland ministry.
  Dutch-holder **cipher** records 1800-1812: decrypted R1033 (above), R1926 (Schimmelpenninck 1803, 2.01.08 inv. 344),
  R1945/R1946 (Bourdeaux 1801, inv. 257); non-decrypted R1942 (D. van Hogendorp to Van der Goes, 1803, inv. 318),
  R1944 (inv. 257), R2034 (legatie Rusland 1803), R1469/R1470 (legatie Turkije 1809, the roell-vandedem target).
- **Not found:** a Van Spaen key, a key sheet for the 1806-1809 commissioners, or a ministry decipherment of No 4/No 6
  in any finding aid read (2.01.08, 3.20.16, 3.20.17); not found in the DECODE key listing. Candidates for the
  ministry's reading of the content (not a key): inv. 20 (incoming register) and inv. 88 (outgoing minutes), both
  digitised. Candidate for key material: R1033 / 1.02.13 inv. 226.
- Requests: www.nationaalarchief.nl 12 (2.01.08 page, 3 EADs, search page, zvt main.js, 6 item pages); service.archief.nl
  2 (IIIF 1000 px, inv. 20 and 88 scan 25), 1.6 s apart, no 4xx/5xx; de-crypt.org 0. Vision 2. Subagents 0. Grade
  counts H 0, C 0, S 0, M 0, I 0 (nothing read).

## GAPS63-vanspaen-vandergoes-1808 (3 Oct 2026, account-4): DECODE R1033 compared with R1941

Step: the Verdict's cheapest step (one DECODE login, view R1033). Clock 08:44-08:50 UTC, 3 Oct 2026. Status word unchanged.
Route: one real-browser login (`tools/decode_browser_login.js 1033 <scratchpad> --max-files 0 --delay 1700 --listen`,
`loggedIn: true`); Chromium's NSS store first needed the proxy CA (`apt-get install -y libnss3-tools`; then
`certutil -d sql:$HOME/.pki/nssdb -A ...` alone -- `certutil -N --empty-password` spins at 100% CPU and never returns,
which is the hang GAPS61 hit; kill it, the database files are already written, and `-A` succeeds).
- **R1033's record** (RecordsView/1033): Six van Oterleek, St Petersburg, to W.F. Roell, 1808-1810; Cipher, Decrypted,
  "Nomenclatures", symbol sets "Graphic signs, Numerical"; 37 images, **4 documents**: a 2020 transcription of the
  drafts (transcriber "XZ", 5 July 2020, 873 lines), and three files uploaded 9 Jan 2026 -- "Transcription of coded
  messages", "Decoded messages", "Annotated decoded messages" (35 messages, word[group+mark] per token). The documents
  are account-gated on DECODE and are not committed here; sha1 of each, and the script, in `gaps63/`.
- **Design comparison** (`gaps63/compare_r1033.py <dir>` -> `gaps63/compare.tsv`):
  | | R1033 (Six van Oterleek 1808-10) | R1941 (No 4 + No 6, GAPS36 image reading) |
  |---|---|---|
  | groups | 5,359 cipher groups, 5,358 annotated pairs | 304 |
  | range | 1-999, none over 999 | 15-1339, 36 groups over 999 |
  | length | 1-3 digits | 2-4 digits |
  | marks | 89.5% marked: ^ 1227, " 1122, : 906, ~ 751, + 700, = 92; unmarked 561 | none (a dash after some groups, a colon twice) |
  | code values | 872 numbers, 1,766 number+mark values (the mark selects the meaning: 885 = de, 885^ = in) | 216 distinct |
  | decryption | yes: Dutch plaintext, syllable- and word-level (nulls tagged) | none |
  R1033 is the same code+mark family as the Croiset 1803 book (R1035) Bourdeau ruled out: three-digit numbers to 999
  with a mark that selects the value. R1941 has no marks and runs past 999. **Different design.**
- **Overlap test, with a control that can differ** (coverage depends on which numbers occur, which a random draw changes;
  order shuffling would not -- rule 3): share of No 4/No 6 groups whose number is an attested R1033 code value, mark
  ignored. Full range: target 0.757 vs same-range random sets (uniform 15-1339, N 304, 1000 draws, seed 63) mean 0.648,
  p95 0.694, 0/1000 at or above target -- **but that excess is the range alone** (R1033 has nothing over 999; 12% of the
  target's groups are over 999 against 26% of a uniform draw). Restricted to groups <= 999 (N 268) against uniform
  15-999 draws: target **0.858** vs control mean **0.871**, p95 0.903, 771/1000 at or above target. **No overlap beyond
  chance.** Applying R1033's values (unmarked value where one exists, else the two commonest) to No 4 reads
  "schrijven-en aux rec onregt reeds regel-en ? ou aux sen de|ac meest|gewis ..." -- no Dutch or French run.
- Grades: no reading, H 0, C 0, S 0, M 0, I 0. Not found: any R1033 code value carried into R1941; any key, decipherment
  or Van Spaen mention in R1033's record or documents (grep of the four documents for Spaen, Dusseldorf/Düsseldorf,
  Berg, Goes: none -- the record is Six van Oterleek's St Petersburg traffic only).
- Credit: D. Bourdeau (cyphersolver) for the R1941 transcription and for ruling out R1035; R1033's transcription
  (DECODE, 2020, "XZ") and decryption documents (DECODE, uploaded 9 Jan 2026) are the DECODE contributors' work.
- One-line suggestion (Usage 7, not done here): R1033's 1,766 decoded number+mark values are a decrypted same-ministry
  1808-10 code+mark nomenclator; `ciphers/roell-vandedem-1809` (legatie Turkije 1809, R1469/R1470) cites inv. 226 as a
  sibling and could compare its own group design against them.
- Requests: de-crypt.org 7 (login page + login submit + RecordsView/1033 + 4 documents), 1.7 s apart, no 4xx/5xx;
  example.com 1 (browser TLS test). Vision 0. Subagents 0.

## GAPS66-vanspaen-vandergoes-1808 (3 Oct 2026, account-4): the ministry's verbaal (inv. 20) and outgoing minutes (inv. 88)

Step: the Verdict's cheapest step. Clock 09:01-09:15 UTC, 3 Oct 2026. Status word unchanged. Read clear register text
only; nothing in figures was decoded. Locator table: `gaps66/scans_located.tsv`; native line crops in `gaps66/crops/`
(cut with `python3 tools/iiif_lines.py "<inv. 20 scan 34/35/47/48 info.json>" --region x,y,w,h --out
ciphers/vanspaen-vandergoes-1808/gaps66/crops --prefix i20s34|i20s35|i20s47r|i20s48 --columns ... --distance 90`;
two margin views cut from the tool's cached native source with `convert -crop`).
Route: scan lists from each item page's `drupal-settings-json` (www.nationaalarchief.nl, 2 requests); date bisection on
IIIF header strips and 450-1200 px views (inv. 20: scan 40 = 16 Jan, 60 = 22 Jan; 32-35 = Thursday 14 Jan; 46-48 = Monday
18 Jan); native regions only for the found entries.
Reading of the verbaal (inv. 20; [M] = word uncertain, abbreviations kept):
- **Entry 105** (scan 35, right page, Donderdag 14 Jan 1808): "Eene miss. van den Commissaris van Spaen van Voorstonde,
  geschreven te Dusseldorp den 12 January No 4. houdende Advertentie in Cyffer". Gerenvoyeerd: "gewone respecten" [M].
  Aanteekeningen: a mark [M] and a brace against 105 with "Zie Uitgaande" [M, may be struck through]; the brace against
  106 (Gronovius, Carlsruhe 29 Dec No 26, also "in Cyffer") reads [struck word] "aan den Koning gecommuniceerd".
  **No summary of No 4's content is entered** -- the clerk logged it only as an advice in cipher.
- **Entry 136** (scan 48, left page, Maandag 18 Jan 1808): "Eene miss. van den voornoemden Commissaris van Spaen
  v[an] Voorstonde gedateerd 15 January No 6. in Cijffer houdende advertentie rakende den inhoud zyner depeche hier voor
  sub No 135 breeder geextendeerd". Gerenvoyeerd: "gew. respecten" [M]. Aanteekeningen: "Zie U.S. No 86".
  So **No 6 (the 75-group annex) is an advice "touching the content of" No 5**, whose summary the clerk wrote at entry 135.
- **Entry 135 = No 5** (scans 47-48; not in inv. 281, GAPS58): "Eene miss. van den Commissaris Van Spaen van Voorstonde
  geschreven te Dusseldorp den 15 Jan[uary] No 5. houdende de rapport van eene Communicatie die hem door den Heer Agar
  gedaan was, zoo nopens de bevelen, welke hy van Z. Keiz. en Kon. Hoogheid ontvangen had om met den Hollandschen
  Commiss[aris] in onderhandeling te treden over het aangaan van schikkingen wegens eenen afstand van terrein op de
  Frontieren, als wel opzigt tot het nog niet ratificeren van zeker Tractaat tusschen den Franschen Keizer en den
  Grootshertog, waarin de Cessie van Huissen etc. mede gestipuleerd was. En behelzende voorts Advertentie van eenige aan
  hem gesuppediteerde informatien aangaande de intentie van het Ministerie van Berg om de Domeinen in de gecedeerde
  Landen te verkoopen of te verpachten, de pachtpenningen te ontvangen, de conscriptie door te zetten en in het algemeen
  om uit gezegde Districten zoo veel geld en manschappen te trekken als maar mogelyk zyn zoude -- mitsgaders informatie
  dat hy van den Heer Agar den 16 January zoude overhandigen de brieven van Notificatie [M] van den Koning, wegens
  hoogstderzelfs komst tot den troon." Gerenvoyeerd: "gewone respecten" [M] and "brieven van notif." Aanteekeningen:
  "Zie U.S. No 86".
- Neighbours: 102 (scan 34) is No 3 (Leg. Weenen, "Notif."), matching GAPS44's clear No 3; 103 (scan 34-35) is a clear
  12 Jan letter acknowledging the minister's missive of 6 Jan about his pay; 104 (scan 35) is from "Commissaris [van]
  Spaen van Biljoen" [M] (a Wesel act, the Berg ministry pressed "without effect"; "Zie U.S. No 126" [M]); 134 (scan 47)
  is from the commissioners Van Spaen and Van Reinesdyk [M] at Wesel, 14 Jan, on the Berg orders for Huissen, Malburg and
  Sevenaar ("Zie U.S. No 86 & 121").
Outgoing minutes (inv. 88): the minutes carry the U.S. number top right. Scans 116-145 hold U.S. 74-93 in order (81 at
scan 134 = to Ambassador Verhuell, Paris, 18 Jan, No 9, the English parlementaire -- the reply to verbaal 137; 84 at 137 =
list of pensions; 85 at 139 = to Bourdeaux, 19 Jan; 87 at 140 = to Brantsen, 23 Jan; 88-91 and 93 at 141-145). **U.S.
86, the reply the verbaal cites for No 5, No 6 and entry 134, is not in sequence** (not between scans 139 and 140, nor in
138 or 141-145); nor is 92. It may be filed with the secret minutes elsewhere in inv. 88, or registered in inv. 99
(Verbalen van uitgaande stukken 1808). The reply to No 4 has no U.S. number in the verbaal and was not looked for.
- What this gives the cipher (rule 4: none of it is a decoded token): the topic of No 6 is the topic of No 5, now known
  in summary; crib terms added to the ranked list in prose here, not yet tested: Agar, Grootshertog / Groothertog, Keizer,
  Tractaat, ratificeren/ratification, Huissen, afstand van terrein, frontieren, Domeinen, verkoopen/verpachten,
  conscriptie, geld en manschappen, notificatie, troon. No 4's content is not summarised anywhere seen.
- Not found: a decipherment, a plain-text copy or a content summary of No 4; a decipherment of No 6; U.S. 86 in inv. 88's
  sequence. Grades: H 0, C 0, S 0, M 0, I 0 (no cipher token read).
- Requests: www.nationaalarchief.nl 2; service.archief.nl 58 (IIIF views and native regions, 1.6 s apart, no 4xx/5xx).
  Vision: in-session image reads only, no subagents.

## GAPS70-vanspaen-vandergoes-1808 (3 Oct 2026, account-4): U.S. 86 found in the outgoing verbaal (inv. 99)

Step: the Verdict's cheapest step. Clock 09:37-09:45 UTC, 3 Oct 2026. Status word unchanged. Clear register text only;
nothing in figures read or decoded.
Route: inv. 99 scan list from the item page's `drupal-settings-json` (656 scans); date bisection at 450 px (scan 25 =
16-17 Jan, entries ~61-62; scan 32 = 19 Jan; 34 = 21 Jan; 36 = 22 Jan, entries ~94-96); scan 33 read at 1100 px, left and
right page regions (committed: `gaps70/inv99_s033_left_1100.jpg`, `gaps70/inv99_s033_right_1100.jpg`). Legible at that
size, so no native fetch was needed. Line crops not cut: `python3 tools/iiif_lines.py -h` fails in this container
(`ModuleNotFoundError: No module named 'numpy'`), and the entry holds nothing that calls for two blind passes (below).
- **U.S. 86** (inv. 99 scan 33, Woensdag 20 January 1808; [M] = word uncertain, abbreviations kept): "Een rapport aan den
  Koning, strekkende tot communicatie 1o. van de miss. van den Baron von Hende [M] Extr. Env. & Min. Plenip. v. den Koning
  van Wurtemberg, betrekkelyk eene wedergedane ruiling [M] en distributie van Ridderorden, breeder vermeld in het Verb.
  van ingek. stukken no 144. 2o. van de missive der Commissarissen Van Spaen van Biljoen en van Riemsdyk, van de brieven
  van den Commissaris van Spaen van Voorstonde & van de depeche van den Minister Brantsen, respectivelyk te vinden in het
  Verbaal van ingekomen stukken sub no 134, 135, 136 en 147. 3o. van de miss. van den Min. Plenip. Brantsen over de
  zending van den Heere Caulincourt naar Napels, geextendeerd [M] in het Verb. van ingekomen stukken no 146. En
  behelzende voorts ingevolge de mondelinge bevelen van Z.M. [four lines struck through, illegible] eenige informatien
  met betrekking tot het geen tot hier toe is geobserveerd geworden by het aannemen van een Hofvrouw." Aanteekeningen
  (right page): "ter gelegenheid van het overlyden van de Hertoginne van Mecklenburg Schwerin" [M; may belong to the
  struck passage].
  So U.S. 86 is **a report to the King passing on Van Spaen's No 5 and No 6 (with entries 134 and 147)**, not a reply
  to Van Spaen. The verbaal records only that the pieces were communicated. **No summary, gloss or decipherment of No 6 or
  No 4 is in the entry**, so the two-blind-pass condition did not arise. The report's text, and anything it annexed (a
  deciphered copy of No 6 sent to the King, say), would be in the report itself.
- **inv. 88 (secret minutes):** U.S. 86 is not in a separate secret block. The volume is filed as monthly bundles
  (scan 1 = "January 1808" wrapper; scans 711-714 = end, March). Header strips of scans 200-248 run on in sequence (U.S.
  126 at 212, 129 at 218, 135 at 224 = 29 Jan, then 143 [M], 148, 152). Scans 170 and 190 hold ordinary minutes, 190 a
  report "Aan den Koning, Sire" in sequence. Gaps 86 and 92 are as GAPS66 found them. Inv. 88 has no secret section:
  "gewone en geheime" are interfiled. The minute of 86 is simply absent there.
- **Where the report should be (EAD, re-read this session):** NA 2.01.08 **inv. 189**: "Missiven van de Koning,
  kabinetsorders, 1806-1810 / **Rapporten aan de Koning, met de beschikking daarop aan de minister teruggezonden,
  1808-1810** / Huis des Konings / Grootkanselier", DIGITALIZED, 504 scans. A report returned with the King's disposition
  is the likeliest place for U.S. 86 and any enclosure.
- **Correction to GAPS61** ("no unit anywhere in 2.01.08 carries ... code"): **inv. 204A** reads "Kopieën van ingekomen en
  uitgaande brieven van en aan gezanten, welke door de codeur van het Departement van Buitenlandse Zaken in geheimschrift
  werden overgezet. 1795-1807", DIGITALIZED, 274 scans. That is the ministry coder's working copies of letters to and
  from envoys. They end in 1807, before No 4, but they cover Van Spaen's Vienna mission (inv. 244-248, 1802-1807) and the
  ministry's code practice just before 1808. **Possible key or crib material, not viewed.**
- Not found: a decipherment, a plain-text copy or a content summary of No 4 or No 6 in inv. 99 entry 86; the minute of
  U.S. 86 in inv. 88. Grades: H 0, C 0, S 0, M 0, I 0 (no cipher token read).
- Requests: www.nationaalarchief.nl 5 (item pages inv. 99, 88, 204A, 189; 2.01.08 EAD); service.archief.nl 38 (IIIF
  views and header strips), 1.6 s apart, no 4xx/5xx. Vision: in-session image reads only, no subagents.

## GAPS72-vanspaen-vandergoes-1808 (3 Oct 2026, account-4): inv. 204A viewed in full

Step: the parent's named step (inv. 204A, the coder's copies 1795-1807, for key or crib material), run before the Verdict's
inv. 189 step on the parent's instruction. Clock 09:56-10:07 UTC, 3 Oct 2026. Status word unchanged. Nothing in No 4 or No 6
decoded or tested.
Route: scan list from the item page's `drupal-settings-json` (`gaps72/na_2.01.08_204A_scans.tsv`, 274 scans); all 274 at
450 px on contact sheets of 20 (thumbnails in scratch, not committed); natives of scans 17, 20, 21, 65, 260 fetched once
(`gaps72/native/`, `gaps72/manifest.json`). Crop command (scan 17, as the brief requires; numpy/Pillow installed with pip
first): `python3 tools/iiif_lines.py --image ciphers/vanspaen-vandergoes-1808/gaps72/native/NL-HaNA_2.01.08_204A_0017.jpg
--out ciphers/vanspaen-vandergoes-1808/gaps72/crops17 --region 2400,700,2500,3200 --prefix s17 --ink 200 --prominence 60
--lines-per-crop 6` -> 15 lines in 6 band crops (the default settings found 0 lines on this faint ink). The list was read
from the native at about 1000 px in-session; the crops are there for a second read.
What the volume holds (by scan, from the contact sheets; years from the dated slips "1796", "1797", "1798", "1799", "1800",
"1801-1807" filed between the blocks):
- **Scan 17 (front dossier, scans 1-21): a word list for a new cipher.** Heading: "Eenige eigene namen en andere woorden die
  begrepen moeten worden in het Cyffer op te maken voor de Commissarissen Six, Goldberg en van Leyden." 68 entries, clear
  words only, **no code values** (`gaps72/word_list_scan17.tsv`, H 65 / M 3). They include Huyssen [M], Zevenaer, Malburg,
  Lobith, Agar, 's Gravenwaard, Elten, Emmerik, Rees, Wezel, Het Kleefsche, Dusseldorp, Prins Joachim, Groothertogdom, Rhyn
  Confederatie, cessie, ruiling, domeinen, schulden, heerlykheid, tol, regter oever. "Rhyn Confederatie", "Groothertogdom"
  and "Prins Joachim" date it to 1806 or later (inferred; no date on the sheet as read). This is the same frontier business
  as No 5/No 6 (GAPS66: Agar, Huissen, terrain exchange, Berg domains) and overlaps the GAPS44 crib list (Agar,
  Sevenaar/Huessen/Malburg). So a cipher was built c. 1806-07 for a Dutch commission on the Berg/Cleves frontier, with
  this vocabulary in it. Whether Van Spaen's 1808 dispatches use that cipher is **not established**. Scans 2-16 show the
  same sheet with letters of 1795-96 laid over it.
- Scans 18-21: name lists for an earlier cipher (scan 21 = French Convention members marked "c.d."/"c.g.", c. 1795), no
  values.
- Interlinear pages (cipher groups with the clear text written between the lines by the coder): scans 57-58, 63-65 (65 =
  "aan den Minister Bangeman Huygens", 10 March 1797, French), 84-85, 90 (enciphered letter on printed "Gelykheid, Vryheid,
  Broederschap" paper, 1797), 145-146 (1798-99), 259-260 (260 = to "den Secretaris Bourdeaux te Berlyn", French, with a
  worksheet grid; on the 1801-07 block). **Design on all of them: groups 1-999, nearly every group carrying a mark above it
  (dieresis, tilde, v, +, ″, =)**, i.e. code+mark, the R1033 design (GAPS63), not R1941's unmarked 15-1339. Scan 260 itself
  says Van Reede may have copied the cipher still in use and tells the secretary not to mix clear text into cipher; scan 65
  discusses a copy of the cipher.
- Scan 257: a numbered list of about 24 place names (Alger, ...) on the 1801-07 block, not read further; scan 268: a note
  about putting a piece "in Cyffer", not read further.
- Not found: any copy to or from Van Spaen or the Dusseldorf/Berg mission (the volume ends in 1807); any page in R1941's
  unmarked 15-1339 style; any key or nomenclator sheet with values. Code-value pairs were **not transcribed**: every
  interlinear page is code+mark, so pairs from it cannot be applied to No 4's unmarked groups. A test that the code+mark
  pairs do not fit would also be a non-test, since the two designs differ before any value is compared (rule 3).
  Grades: H 0, C 0, S 0, M 0, I 0 for cipher tokens (none read).
- Requests: www.nationaalarchief.nl 1 (item page inv. 204A); service.archief.nl 279 (274 thumbnails + 5 natives), 1.6 s
  apart, all 200. Vision: in-session image reads only (13 contact sheets/crops), no subagents.

## GAPS76-vanspaen-vandergoes-1808 (3 Oct 2026, account-4): the Six-Goldberg-Van Leyden commission's papers

Step: the Verdict's cheapest step (NA catalogue search for the cipher made for Commissioners Six, Goldberg and van Leyden,
GAPS72 word list). Clock 10:13-10:20 UTC, 3 Oct 2026. Status word unchanged. Nothing in No 4 or No 6 decoded or tested.
- **Catalogue (NA 2.01.08 EAD, fetched once, grepped for Goldberg/Leyden/Six/grens/Kleef/Berg/commissari):** the
  commission is **inv. 221**, "Missiven van Six, Goldberg en Van der Sleyden [sic in the EAD], commissarissen voor de afstand
  van Oostfriesland te Parijs, sep 1807" (with Smits Jan-Sep 1807 and Brantsen Sep-Dec 1807), DIGITALIZED, 531 scans
  (`gaps76/na_2.01.08_221_scans.tsv`). Other hits, not this commission: inv. 217 (De Vos van Steenwijk, Six, Jacobson,
  Blanken at Paris, 1803), inv. 261 (J. Goldberg, envoy at Berlin, 19 Feb 1808 - 17 Oct 1809), inv. 282 (Berg ministers and
  frontier commissioners 1806-1810, already listed by GAPS61), inv. 431-432 (1802 Prussian treaty and ratification ceding
  Sevenaer, Huyssen and Malburg). Still no unit with cijfer/sleutel/chiffre in 2.01.08 other than inv. 204A.
- **Inv. 221 viewed:** every 25th scan, then every 8th of 334-526, then all of 511-531 at 300 px (contact sheets, scratch);
  scans 430, 510, 515, 518, 525 at 1000 px (515, 518, 525 committed in `gaps76/`). Scans 1-~510 are Smits and Brantsen
  (copies "pour copie conforme Smits", Paris, to Dec 1807). **The commission's section is scans 515-531**: wrapper (scan
  515) "Commissarissen wegens de afstand van Oostfriesland te Parys", No 13 exh. 25 Sept 1807 signed Six, Goldberg and Van
  Leyden; scan 518 = Goldberg's No 2, exh. 23 Sept 1807, to Van der Goes, naming "de Heeren Six en Van Leyden van
  Westbarendrecht [M]" as fellow commissioners "te regelen alle de zaken betrekkelyk tot den afstand van Oostfriesland en
  alle zodanige andere zaken als ... den Koning goed zal vinden". So the GAPS72 word list (scan 17 of inv. 204A) is for this
  Paris commission of Sept 1807 (the Fontainebleau negotiation), not a Rhine frontier commission; the EAD's "Van der
  Sleyden" is Van Leyden on the documents.
- **Every page of the commission's section is in clear** (Dutch and French). Scan 525 (French, clear): the Grand Duke of
  Berg's article on the cession of "Zevenaer [M], Huyssen et Malburg", proposed by Champagny and accepted on the King's
  orders at the last conference, to go into the treaty of France with His Highness; also "Monsieur Agar". This is the same
  business as No 5/No 6 (GAPS66), a clear crib-context source for Jan 1808, not a key.
- **Not found:** the commission's cipher (a code table or values), any page in figures, any decipherment, in inv. 221 (the
  commission's whole section seen at 300 px; scans 1-510 sampled at 1 in 25 and 1 in 8 of 334-526, no figure page seen in
  the sample). Not found in the family archive NA 2.21.073 (Maarten van der Goes, 116 units, EAD grepped: no
  cijfer/sleutel/chiffre/Spaen/Goldberg/Berg unit; inv. 77, secret papers 1808, is on a nobility decree). So whether R1941
  (unmarked 15-1339) is that commission's cipher is still **not established** -- it was apparently not used in the
  commission's Sept 1807 letters at all.
- Grades: H 0, C 0, S 0, M 0, I 0 (no cipher token read). Requests: www.nationaalarchief.nl 3 (2.01.08 EAD, inv. 221 item
  page, 2.21.073 EAD); service.archief.nl 72 (65 at 300 px, 7 at 1000 px), 1.6 s apart, all 200. Vision: in-session image
  reads only (6), no subagents. numpy/Pillow pip-installed; no line crops cut (nothing to transcribe).

## GAPS81-vanspaen-vandergoes-1808 (3 Oct 2026, account-4): U.S. 86 sought in inv. 189 (reports to the King returned)

Step: the Verdict's cheapest step. Clock 10:32-10:45 UTC, 3 Oct 2026. Status word unchanged. Clear text only; nothing in No 4
or No 6 decoded or tested.
Route: scan list from the item page's `drupal-settings-json` (`gaps81/na_2.01.08_189_scans.tsv`, 504 scans); every 22nd scan at
450 px, then header strips (top 30 pct at 1100 px, or top 22 pct of the right page at 600 px) at scans 50-100 and 265-386
(scratch, not committed); scan 69 right page at 1500 px (`gaps81/inv189_s069_right_1500.jpg`, `gaps81/manifest.json`). Legible
at that size; no native fetched, no line crops cut (nothing in figures, no two-pass condition).
What inv. 189 holds (from the samples, by scan):
- **1-~265: the King's missives to the minister, 1806-1810, in date order** ("Cabinet du Roi ... Au Ministre des affaires
  étrangères"): scan 56 = La Haye 8 Jan 1807; 62-63 = Utrecht 6 Jan 1808 (exh. 50, 8 Jan); **65-69 = copy, Utrecht 20 Jan
  1808, exh. 160 on 21 Jan 1808**; 72 = Utrecht 5 Feb 1808 (exh. 4 Feb, 241 bis); 78-100 blank leaves; 111-155 1808; 177-199
  1809; 265 June 1810.
- **~270-360: reports to the King returned with the disposition, filed in exhibitum bundles** labelled "Exh. 15 van hooimaand
  1809/1810" and "... zomermaand 1810", not in date order: 279-285 = the one January 1808 report in the sampled range, Roëll's
  "Rapport aan den Koning, Utrecht 14 January 1808" (exh. 129 on 16 Jan) on the Duke of Oldenburg's toll at Elsfleth and
  East Frisia, "Renvoyé à l'examen du Ministre des affaires étrangères, Utrecht 14 Janvier 1808" (scan 285 read at 1200 px);
  287/289 = exh. 16 Sept 1808; 295-317 = 1809 (317: a merchant matter naming Dusseldorp, 1809, not Van Spaen); 329-351 =
  1810.
- 361-386: Huis des Konings, Kanselarij "Décisions" 1806 and copies of 1806-07; 397-504: Huis des Konings and Grootkanselier
  (1807-1809), sampled at 1 in 22 only.
- **The King's letter of 20 Jan 1808 (scan 69, copy; H for the clear words, [M] marked):** "Monsieur Roëll, j'attends avec
  impatience une Note que l'on a remise à M. de Brantsen sur M. de Caulincourt. Mandez à M. de Brantsen de revenir. Écrivez à
  M. Verhuell [M] de demander que l'on désigne quelqu'un pour recevoir les Domaines de l'Ost frise de même que les Commissaires
  pour recevoir les papiers et la Place de Flessingue et enfin le Commissaire qui avec celui que je nommerai fixera les limites
  du départ[ement] de Brabant et celles autour de Flessingue, aux termes du dernier traité. Expédiez à M. Apostol l'ordre de
  continuer sa route pour Naples où il sera chargé d'Affaires en attendant, et envoyez lui les deux Lettres ci-jointes. Il aura
  soin de prendre avant son départ les décorations de l'Ordre Royal qui doivent les accompagner, que M. de Caulincourt devait
  remettre. Sur ce, Monsieur Roëll, je prie Dieu qu'il vous ait en sa sainte garde. (Sig.) (Louis). Utrecht 20 Janvier 1808."
  Same day as U.S. 86 and it answers U.S. 86's item 3 (Brantsen, Caulaincourt's mission to Naples) and the Wurttemberg orders
  question (decorations), so it is very likely the King's disposition on U.S. 86 (inferred). **It says nothing of Van Spaen,
  Berg, Agar, Huissen/Zevenaar/Malburg or the Düsseldorf dispatches**, and carries no enclosure.
- **Not found:** the report U.S. 86 itself, any enclosure, any decipherment or plain copy of No 4 or No 6, any key, in inv. 189
  (missives section seen at 1 in 22 plus scans 50-72 at header level; reports section 265-386 at about 1 in 3 header strips).
  The reports section holds 1808 only as strays (one report of Jan, two of Sept in the sample); its bundles are 1809-1810 by
  exhibitum date, so the 20 Jan 1808 report is not expected there unless unsampled. Not run: inv. 261 (Goldberg at Berlin), held
  back because the cost could not be checked against the brief's 50 pct condition from inside the session and the per-host
  request count stood at 96 of 120.
  Grades: H 0, C 0, S 0, M 0, I 0 for cipher tokens (none read).
- Requests: www.nationaalarchief.nl 1 (inv. 189 item page); service.archief.nl 95 (23 at 450 px, 51 header strips at 1100 px or
  600 px, 1 page at 1200 px, 1 at 1500 px, 1 info.json, plus 18 more header strips), 1.6 s apart, all 200. Vision: in-session
  image reads only (13), no subagents.

## GAPS84-vanspaen-vandergoes-1808 (3 Oct 2026, account-4): NA 2.01.08 inv. 261 (Goldberg at Berlin) sampled for a key or cipher

Step: the Verdict's cheapest step. Clock 10:49-11:00 UTC, 3 Oct 2026. Status word unchanged. Nothing in No 4 or No 6 decoded
or tested.
Route: scan list from the item page's `drupal-settings-json` (`gaps84/na_2.01.08_261_scans.tsv`, **798 scans**, not the 531 of
inv. 221); every 14th scan from 1 (57 scans) and every 14th from 8 over scans 8-386 (28 scans), all at 450 px, read as contact
sheets in-session (scratch, not committed except scans 1 and 218, `gaps84/manifest.json`). At 450 px a page of figure groups
(numbers in lines, as R1941's scans 81-82/85 of inv. 281) is distinguishable from cursive prose and from print; no native fetched,
no line crops cut (nothing in figures to transcribe).
What inv. 261 holds (from the samples, by scan; wrapper readings [M] at 450 px):
- scan 1: wrapper "Pruisen ... 1e January - 20 February 1808" (the name under "Pruisen" reads "Bourdeaux" [M]); scans 15-43:
  Berlin dispatches of Jan-Feb 1808, the first Goldberg-signed page seen at scan 43 ("Berlin ... Février 1808" [M]); scans 50-
  200: 1808 dispatches to the minister with exhibitum dockets (e.g. scan 64 "exh. 6 May 1808"), printed enclosures (a Prussian
  "Reglement ... Portepee-Fähnriche", scans 106-134; Berlin newspapers, 176-190).
- scan 218: wrapper "Pruisen. Extraordinair Envoijé J. Goldberg, 1809, 1e January - 17 October" [M]; scans 218-560: 1809
  dispatches addressed to "Monsieur W. F. Roëll, Ministre des Affaires étrangères", most with Berlin and Vienna newspapers
  enclosed (Königlich privilegirte Berlinische Zeitung, Wiener Zeitung), "Ordre du jour" print (351).
- scans 589-785: fair copies in a clerk's hand, numbered "No ..", dated Berlin 1810 [M] (e.g. 715 "No 54 exh. ...", 771, 785
  "No 150 ... 1810" [M]), one with a tabular printed enclosure (645).
- **Not found:** any page in figures (code groups, numbered lines, interlinear decipherment over figures), any key sheet or
  code table, any decipherment slip, in the 85 sampled scans (57 across 1-785 at 1 in 14; scans 8-386, the 1808-09 section, at
  1 in 7). Every sampled leaf is clear French or German print. Nothing of R1941's design (unmarked numeric groups 15-1339) seen.
  A cipher leaf could fall between samples (1 in 14 after scan 400); the brief named a sample, not a full view.
  Grades: H 0, C 0, S 0, M 0, I 0 for cipher tokens (none read).
- Requests: www.nationaalarchief.nl 1 (inv. 261 item page); service.archief.nl 85 (all at 450 px), 1.6 s apart, all 200.
  Vision: in-session image reads only (8 contact sheets), no subagents.
- With inv. 261 the archival route inside 2.01.08 named by earlier steps is exhausted (inv. 281, 20, 88, 99, 189, 204A, 221 and
  now 261 read; catalogue grep GAPS61/GAPS76 found no other cijfer/sleutel/chiffre unit). The target parks on no-key-material.
  New material that would reopen it: a ministry codebook or key list of 1806-1810 in another archive (e.g. the King's cabinet,
  NA 2.02.xx, or a Berg/French holding), or D. Bourdeau's own key work on R1941.

## Remaining gaps (FT4-vanspaen-vandergoes-1808, 3 Oct 2026; updated FT4b, FT4c, GAPS26, GAPS34, GAPS36, GAPS41, GAPS44, GAPS48, GAPS54, GAPS58, GAPS61, GAPS63, GAPS66, GAPS70, GAPS72, GAPS76, GAPS81 and GAPS84, 3 Oct 2026)
Read so far: 0 of 304 groups (229 letter + 75 annex, image reading GAPS36; Bourdeau's has 303); nothing decoded
- letter 14 Jan 1808 (228 groups) - blocker: no-key-material; no key for this code on DECODE, Croiset 1803 (R1035) gives word salad; located 3 Oct 2026 (GAPS34) as inv. 281 scans 81-82, "No 4, Dusseldorf 12 January 1808", received 14 Jan; no key sheet in any of the 360 scans of inv. 281 (GAPS41: none in 1-74; GAPS58, 3 Oct 2026: none in the last 139)
- annex 15 Jan 1808 (75 groups) - blocker: no-key-material; located 3 Oct 2026 (GAPS34) as inv. 281 scan 85, "No 6, Dusseldorf 15 January 1808", a separate numbered dispatch; DECODE DocumentsList 0 documents (FT4c); no decipherment seen beside it in scans 75-99, nor anywhere in inv. 281 (all 360 viewed, GAPS58)
- numbered sibling series and crib - blocker: no-key-material; every internal step run (below), no key or plain copy found; identity with Bourdeau confirmed row by row 3 Oct 2026 (GAPS36); scans 1-74 viewed (GAPS41); clear siblings read 3 Oct 2026 (GAPS44): No 3 (docket 103, 12 Jan 1808, same day as No 4) and No 2 transcribed, note 104 body covered by a slip in both captures; ranked crib list in gaps44/crib_candidates.tsv (Agar, Grand Duc, Empereur, Roi, Sevenaar/Huessen/Malburg, traité/ratifications/Paris/Utrecht, limites); crib-placement test under a one-part code run 3 Oct 2026 (GAPS48): control below gate (one-part 0.64 FR/NL, K-matched 0.75/0.69 vs gate 0.75), target 0.40/0.47 at the two-part null, non-test at N 304; one-part frequency-position test run 3 Oct 2026 (GAPS54): control power 0.675 FR / 0.625 NL vs gate 0.80, target not scored, untestable at N 304 by this statistic; all 360 scans of inv. 281 viewed 3 Oct 2026 (GAPS58): No 1 and No 5 not found, no other figure page, no key; NA catalogue pass run 3 Oct 2026 (GAPS61): no key or cipher unit in 2.01.08, 3.20.16 or 3.20.17, none in the DECODE key listing; candidates found: DECODE R1033 (decrypted 1808-10 code "op basis van het cijfer van Van Hogendorp", NA 1.02.13 inv. 226, not digitised) and the ministry's own registers 2.01.08 inv. 20 (incoming verbaal 1808, 600 scans) and inv. 88 (outgoing minutes Jan-Mar 1808, 714 scans), both digitised; R1033 compared 3 Oct 2026 (GAPS63): different design (code+mark, 1-999, 89.5% marked, 1,766 decoded values; R1941 unmarked 15-1339), group overlap at chance (<=999: 0.858 vs same-range random 0.871, 771/1000 >= target), not R1941's key; ministry registers read 3 Oct 2026 (GAPS66): verbaal inv. 20 entry 105 logs No 4 only as "Advertentie in Cyffer" (no content summary), entry 136 says No 6 "in Cijffer" concerns the content of No 5 (entry 135, summary read: Agar, frontier terrain exchange, unratified Emperor-Grand Duke treaty on Huissen, Berg domains, conscription, money and men, the King's notification letters), both cross-referenced to reply U.S. 86, which is not in inv. 88's sequence (U.S. 74-93 at scans 116-145, 86 and 92 absent); U.S. 86 found 3 Oct 2026 (GAPS70) in inv. 99 scan 33 (20 Jan 1808): a report to the King communicating entries 134, 135, 136 and 147 (with Wurttemberg and Brantsen pieces), no gloss or decipherment of No 4/No 6 in the entry; its minute is not in inv. 88 (no separate secret block, U.S. 86 and 92 absent); the report itself is likely in inv. 189 (Rapporten aan de Koning, met de beschikking teruggezonden, 1808-1810, 504 scans, digitised); GAPS61 missed inv. 204A (the ministry coder's copies of envoy letters put into cipher, 1795-1807, 274 scans, digitised), a possible key or crib source; inv. 204A viewed in full 3 Oct 2026 (GAPS72): no Van Spaen copy, no unmarked-style page, no key with values; interlinear pages all code+mark 1-999 (not R1941's design); scan 17 is a word list for the cipher "op te maken voor de Commissarissen Six, Goldberg en van Leyden" (c. 1806-07, Berg/Cleves frontier: Huyssen, Zevenaer, Malburg, Agar, Lobith, Dusseldorp, Prins Joachim), crib vocabulary in gaps72/word_list_scan17.tsv, cipher itself not found; commission papers found 3 Oct 2026 (GAPS76): 2.01.08 inv. 221 scans 515-531, Six/Goldberg/Van Leyden at Paris for the cession of East Frisia, Sept 1807, all in clear, no cipher, values or figure page; not in 2.21.073 (Van der Goes papers) either; inv. 189 searched 3 Oct 2026 (GAPS81): the report U.S. 86 not found (reports section is 1809-10 exhibitum bundles with 1808 strays); the King's letter of 20 Jan 1808 (scan 69, exh. 160) answers U.S. 86's Brantsen/Caulaincourt and decorations items but says nothing of Van Spaen, Berg or the dispatches; no enclosure, decipherment or key; inv. 261 sampled 3 Oct 2026 (GAPS84): Goldberg's Berlin dispatches 1808-1810, 798 scans, 85 sampled at 450 px (1 in 7 over 1808-09), all clear, no figure page, key or decipherment; archival route in 2.01.08 exhausted; reopens only on new material (a ministry codebook 1806-10 in another archive, or Bourdeau's own key work)

## Escalation (3 Oct 2026)
- [x] siblings: GAPS34 found the target is No 4 and No 6 of a numbered Düsseldorf dispatch series; GAPS41 (3 Oct 2026) viewed scans 1-74: No 2 (scan 67, 5 Jan 1808) is in clear, No 1/3/5 not found there, no figure page in 1-74; GAPS58 (3 Oct 2026) viewed the last 139 scans: no No 1/No 5, no figure page, inv. 281 complete
- [x] clear-pages: GAPS44 (3 Oct 2026) read No 3 (docket 103, scans 75-76), slip 102 and No 2 (scan 67) from crops, 2 blind passes 95.8% word agreement; note 104 body hidden under slip 102 in both captures; crib list gaps44/crib_candidates.tsv. Clear letters 83, 87, 89-94 not read (later than No 4)
- [x] known-keys: DECODE keys 1780-1815 at Dutch holders checked by Bourdeau, R1035 ruled out; R1941's own DocumentsList empty (FT4c, 3 Oct 2026); GAPS61 (3 Oct 2026) found the decrypted cipher record R1033 outside Bourdeau's key-record set; GAPS63 (3 Oct 2026) viewed it: code+mark 1-999, a different design from R1941, overlap at chance against a same-range random control -- not this letter's key
- [x] print: Colenbrander Gedenkstukken V read 24 Sept; Smit 1975 grepped 3 Oct; letter absent from both
- [x] key-rebuild: crib candidates listed (GAPS44); crib placement (GAPS48) and frequency-position (GAPS54) under a one-part code both non-tests at N 304, controls below gate (3 Oct 2026); no further cheap statistic at this N -- inv. 281 fully viewed, no further ciphertext or key in it (GAPS58, 3 Oct 2026) -- NA catalogue pass done (GAPS61, 3 Oct 2026): no key unit in 2.01.08/3.20.16/3.20.17; R1033 compared (GAPS63, 3 Oct 2026): different design, overlap at chance; verbaal read (GAPS66, 3 Oct 2026): No 6 concerns No 5's content (summary in hand, crib terms in the GAPS66 section), No 4 unsummarised, reply U.S. 86 not in inv. 88's sequence; U.S. 86 located (GAPS70, 3 Oct 2026): a report to the King, entry has no gloss; inv. 204A viewed (GAPS72, 3 Oct 2026): code+mark interlinear copies only, plus a word list for the cipher made for Commissioners Six, Goldberg and van Leyden; that commission's papers found (GAPS76, 3 Oct 2026): inv. 221 scans 515-531, Paris Sept 1807 (East Frisia), all clear, no cipher or values; inv. 189 searched (GAPS81, 3 Oct 2026): U.S. 86 report not found, the King's 20 Jan 1808 letter is silent on Van Spaen; inv. 261 sampled (GAPS84, 3 Oct 2026): Goldberg's Berlin dispatches all clear, no key or figure page; no further internal instrument: statistics are non-tests at N 304 and every 2.01.08 unit named is read
- [x] image-check: native 5000 px images of scans 81, 82, 85 fetched and committed 3 Oct 2026 (GAPS34); transcribed from crops and matched to Bourdeau's, 20 corrections (GAPS36, 3 Oct 2026)
- [n/a] retry: no attempt has failed yet that a retry could repeat
Verdict: parked: every gap has an outside blocker (no-key-material); GAPS84 (3 Oct 2026) sampled NA 2.01.08 inv. 261 (Goldberg, Berlin 1808-10) and found no key, cipher or decipherment, closing the archival route in 2.01.08; new material that reopens it: a ministry codebook or key list 1806-1810 in another archive, or D. Bourdeau's own key work on R1941

## Next step (READ2-RELABEL, 3 Oct 2026)
The images are on disk and fully used, so this is not an image step. On disk: native 5000 px captures of NA 2.01.08 inv. 281 scans 67, 73-76, 81, 82 and 85 (the target letter No 4 at scans 81-82, the annex No 6 at scan 85; manifest.json, na_2.01.08_281_scans.tsv with all 360 scans listed), line crops in images/lines_gaps36 and lines_gaps44, and the inv. 261 and 204A samples under gaps72/gaps84. The 304 groups were transcribed from these crops and matched to Bourdeau's (GAPS36), and every scan of inv. 281 was viewed (GAPS41, GAPS58) with no key sheet in it. What reopens the target is new material, not a pass over these scans: a ministry code book or key list for 1806-1810 held in another archive, or D. Bourdeau's own key work on R1941. The one action that depends on nobody (~USD 1): grep the public finding aid of the King's cabinet archive at the Nationaal Archief (Kabinet des Konings, 1806-1810) for a key unit.

## Remaining gaps (READ2-RELABEL, 3 Oct 2026; restates the 3 Oct 2026 section, nothing re-run)
Read so far: 0 of 304 groups (229 letter + 75 annex; image reading GAPS36, Bourdeau's count 303); nothing decoded
- letter 14 Jan 1808 (228 groups, inv. 281 scans 81-82) - blocker: no-key-material; no key sheet in any of the 360 scans of inv. 281, none on DECODE for this code, Croiset 1803 (R1035) gives word salad
- annex 15 Jan 1808 (75 groups, scan 85) - blocker: no-key-material; DECODE DocumentsList 0 documents (FT4c), no decipherment beside it in inv. 281
- numbered sibling series and crib - blocker: no-key-material; crib placement (GAPS48) and frequency-position (GAPS54) are non-tests at N 304 (controls below gate), R1033 is a different design (GAPS63), inv. 261 holds no key (GAPS84)

## Escalation (READ2-RELABEL, 3 Oct 2026; restates the 3 Oct 2026 ladder)
- [x] siblings: target is No 4 and No 6 of a numbered Düsseldorf series (GAPS34); inv. 281 fully viewed, No 2 and No 3 clear (GAPS41, GAPS44, GAPS58)
- [x] clear-pages: No 3, slip 102 and No 2 read from crops, 2 blind passes 95.8% word agreement (GAPS44); crib list in gaps44/crib_candidates.tsv
- [x] known-keys: DECODE keys 1780-1815 at Dutch holders checked (Bourdeau), R1035 ruled out, R1941 DocumentsList empty (FT4c), R1033 compared (GAPS63)
- [x] print: Colenbrander Gedenkstukken V read 24 Sept 2026, Smit 1975 grepped 3 Oct 2026; letter absent from both
- [x] key-rebuild: crib placement and frequency-position both non-tests at N 304; NA catalogue pass found no key unit in 2.01.08, 3.20.16, 3.20.17 (GAPS61); ministry registers read (GAPS66, GAPS70)
- [x] image-check: native scans 81, 82, 85 fetched and committed (GAPS34); transcribed from crops and matched to Bourdeau's, 20 corrections (GAPS36)
- [n/a] retry: no attempt has failed yet that a retry could repeat
Verdict: parked: every gap has an outside blocker (no-key-material); the images are on disk and read, and new material reopens it: a ministry code book or key list 1806-1810 in another archive, or D. Bourdeau's own key work on R1941
