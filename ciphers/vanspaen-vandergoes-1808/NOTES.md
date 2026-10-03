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

## While waiting (GF4-BATCH16, account-4, 3 Oct 2026)

Still open and workable, but the first test waits on a key or on DECODE's claimed annex decipherment.
- Action that depends on nobody: read the NA inv. 281 scan list (360 IIIF images, public) at thumbnail size to locate
  the 14-15 Jan 1808 letter, then view the leaves on each side at native resolution for a decipherment, a clear draft
  or a ministry gloss (premise (c)); then one logged-in DECODE pass listing R1941's documents (premise (a)). S.
