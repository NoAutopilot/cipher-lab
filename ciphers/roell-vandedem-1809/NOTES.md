open

**Edition-check resolution, LANE N4 csCOL, 24 Sept 2026 20:13 UTC:** the orchestrator's 20:03 hold is lifted --
Colenbrander's Gedenkstukken V has now been independently read (full-text search, both bands, via
`resources.huygens.knaw.nl`'s own OCR search engine, not Bourdeau's web search) for every proper noun in this
letter; letter absent. See "Colenbrander Gedenkstukken V -- independent read" below and the Verdict.

# Röell (attributed) to Van Dedem tot de Gelder, 9 February 1809

QUEUE row: CS2-22 (`sources/solver-diffs/2026-09-24-cyphersolver-site.tsv`, catalogue item 233 at
dbourdeau.github.io/cyphersolver/catalogue.html). Check-solved run 24 September 2026 by LANE N4 csNA
(session_01PKTy3iKiH3LzJpQauLb8Wu), brief `.claude/briefs/runs/2026-09-24-lane-n4-csNA.md`. Copy-free per LANE
N4 scARCH (ROOM.md, 24 Sept 2026 19:00 UTC), confirming the exact viewer: Nationaal Archief toegang **1.02.20**
(Inventaris van het archief van de Legatie in Turkije, 1668–1810), inv. nr. 804 — the row's cached shelfmark
"legatie Turkije inv.804" is the correct legation but the DECODE catalogue's own toegang code (1.02.04) is
wrong; scARCH's NA viewer test confirms 1.02.20.

## What it is

DECODE R1469 (7 pages, dated 9 Feb 1809) and R1470 (6 pages, undated), both status Non-decrypted (`sources/
decode/records-non-decrypted-2026-09-24.tsv`, ids 1469/1470 — no "Partially decrypted"/hard-filter case here).
2,585 groups total, 931 distinct, heavily homophonic (no group reaches 1% of the text). Neither letter is
addressed or signed; the attribution to W.F. Röell is DECODE's own guess, which Bourdeau's write-up argues
against (Röell's own despatches in this legation archive are in clear Dutch, none dated 9 February).

## Six-source search log (24 September 2026)

1. **Bourdeau, quoted verbatim** (`roell1809.html`, posted 21 Sept, updated 24 Sept 2026 — same-day fresh):
   *"No key, decipherment or clear copy was found online or in print, and nothing was decoded."* And, on print:
   *"Colenbrander's Gedenkstukken V (1806-1810) gave nothing by web search."* Same volume as CS2-21 above,
   correct window for a Feb 1809 despatch.
2. **Standard printed edition — attempted independently, not reached.** Same access attempt as CS2-21: the
   huygens.knaw.nl retroboeken Dojo viewer has no plain-text/OCR search reachable via curl; a `site:delpher.nl`
   web search surfaced a Gedenkstukken page mentioning "M. Röell's response to inquiries... to the Dutch
   government" (`MMSFUBA02:000012293:00211`) but WebFetch returned only page metadata, no OCR text, and — more
   importantly — that snippet's context (parliamentary/ministerial inquiries) does not obviously match a
   9 February 1809 cipher despatch to Constantinople; it was not independently confirmed to be the same person
   or event. This worker's own attempt to verify Bourdeau's "gave nothing by web search" line, or to read the
   volume's own pages, did not succeed this pass. The verdict below rests on Bourdeau's search, not an
   independent re-read.
3. **DECODE**: no key for this code (Bourdeau: "DECODE has no key for it"); Röell's own papers (NA 2.21.008.78)
   list letters from Van Dedem and the codemaker S.F. Croiset for 1808–09, but no codebook.
4. **Aymeloglu** (fresh shallow clone, 24 Sept 2026): "Roell"/"Dedem" occur only in his raw DECODE catalogue
   scrape files, not in any of his 8 write-ups — not attempted there.
5. **Cryptiana / Tomokiyo** (`sources/cryptiana/web/dutch.htm`, Shift-JIS): neither "Roell"/"Röell" nor "Dedem"
   occurs anywhere in this page (which does cover Dutch cipher-bureau and Fagel-family codebook history in
   general, including the 1751 Hellen episode for CS2-18 above) — no coverage of this target.
6. **Web search**: nothing beyond Bourdeau's page found; "Röell" "van Dedem" 1809 cipher/code/ontcijferd queries
   return only unrelated biographical pages (Willem Jan van Dedem's canal-digging permit, a different Van Dedem;
   Gerrit van Spaan).

Bourdeau also checked frequency structure against the code being one of the ministry's other known systems (Van
Spaen 1808, Fagel 1804, the 1788–93 legation code) and against alphabetical ordering — none fits, and no group
reaches even 1% of the text, so ciphertext-only attack has no crib to start from without the key.

## Colenbrander Gedenkstukken V — independent read (LANE N4 csCOL, 24 Sept 2026)

Same route as CS2-21 (`ciphers/vanspaen-vandergoes-1808/NOTES.md`): `resources.huygens.knaw.nl`'s Dojo viewer has
no OCR search reachable by a plain page fetch, but its `searchText` accessor is a plain GET,
`/retroboeken/gedenkstukken/searchText/index_html?search_term:ustring:utf-8=<term>&source_id=<N>&id=searchText`,
that full-text-searches one volume's OCR (register included) and returns snippets with page numbers. Deel V is
two tomes: **source 7 = Deel V, Eerste Stuk, GS 11** (1910) and **source 8 = Deel V, Tweede Stuk, GS 12** — both
title pages read to confirm.

Full-text search, both sources, run 24 Sept 2026 (queries 2 s apart, descriptive User-Agent):

| term | source 7 (band 1) | source 8 (band 2) |
|---|---|---|
| Röell | 80 hits | 73 hits — W.F. Röell throughout appears as Minister of Foreign Affairs/a domestic minister of the Kingdom of Holland, corresponding with King Louis Napoleon, Gogel, Mollerus, van der Heim, Verhuell etc., 1808–1810 (e.g. register: "RÖELL aan Champagny, 50", "288. RÖELL AAN DEN KONING, 5 Aug." p. 428); not one hit addresses or is addressed to Dedem, and none is dated 9 Feb 1809 |
| Dedem | 5 hits | 1 hit — all biographical/footnote mentions of (Van) Dedem van de Gelder as ambassador at Constantinople or as an Overijssel aristocrat (register p. 836); none is a letter title, none co-occurs with Röell in the same snippet |

No sentence in either tome pairs Röell and Dedem as correspondents, and no document is dated to 9 February 1809
in a Constantinople/Ottoman context. This is consistent with Bourdeau's own attribution critique (DECODE's
"Röell" sender is a guess he doubts) and independently confirms his "gave nothing by web search" line against the
edition itself, not just a web search of it.

## Verdict

**`open -- Colenbrander's Gedenkstukken V, Deel V Eerste Stuk (GS 11, source 7) and Tweede Stuk (GS 12, source
8), full-text search of the whole volume including its register (resources.huygens.knaw.nl/retroboeken/
gedenkstukken/searchText) for Röell and Dedem, 24 Sept 2026: letter absent, no pairing of the two names as
correspondents anywhere in the volume.`** No source claims a key, decipherment or clear copy of either R1469 or
R1470.

Grade counts: H 0, C 0, S 0, M 0, I 0 (nothing read here; check-solved does not decode). Rule 10: no novelty
claim made; this is a search result, not a verifier's classification.

Credit: D. Bourdeau, cyphersolver, https://dbourdeau.github.io/cyphersolver/roell1809.html (catalogue item 233;
transcription, frequency analysis, attribution critique), CC BY 4.0 — prior attempt, not a solution. The
Gedenkstukken V edition read is this worker's own (huygens.knaw.nl full-text search, not a repetition of
Bourdeau's web search).

Requests this pass: `nationaalarchief.nl` 0, `resources.huygens.knaw.nl` shared with CS2-21 (~19 total for both
rows this session, ≥2 s apart), `archive.org` 0 additional, `catalog.hathitrust.org` 0 additional, `github.com` 0
additional, WebSearch 0, WebFetch 0. No DECODE login used.

Requests carried over from the prior (held) pass: `nationaalarchief.nl` 0 (already pinned by scARCH),
`resources.huygens.knaw.nl` 0 additional (shared check with CS2-21), `archive.org` 0 additional, `github.com` 0
additional, WebSearch 2, WebFetch 0 additional.
