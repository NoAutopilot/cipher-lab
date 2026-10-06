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

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/roell1809/NOTES.md ; https://dbourdeau.github.io/cyphersolver/roell1809.html
- Their extent, in their words: attempted, open: no key, no decipherment, no crib; closed from the evidence
- Their date: 21 Sept 2026
- Note: already cited in our NOTES.md
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## Web and blog check (LIKELY-7, 2 Oct 2026)

Run first because `tools/intake_gate_check.py roell-vandedem-1809` exited 1 on this missing check alone (check-solved.md
"Required step", 28 Sept 2026). Clock read 04:24 UTC, 2 Oct 2026. WebSearch (plain web) for every query; two hits
opened and their comment threads read (WebFetch).

(a) Plain web searches, four:
1. `Röell van Dedem 9 februari 1809 cijferschrift brief Constantinopel ontcijferd` -- nl.wikipedia F.G. van Dedem;
   Historisch Nieuwsblad "Onze man in Constantinopel" (Van Dedem wrote coded letters "met een ingesloten cijfer");
   the NA inventory PDFs 2.21.008.78 and 1.02.20; Van Galen's dissertation on dragomans. No decipherment.
2. `"Legatie Turkije" 1.02.20 cijfer sleutel OR cipher key 1809` -- the 1.02.20 inventory page (inv. 17 "Sleutels
   geheimschrift ..."); the 1.02.13 inventory (Legatie in Rusland) with "1808-1809, In cijfercode op basis van het
   cijfer van Van Hogendorp" (inv. 226, Six van Oterleek, not digitised -- see below); a Cryptologia 46/6 (2022)
   article on encryption in early-19th-c. Ottoman diplomatic correspondence (doi 10.1080/01611194.2021.1919943,
   Ottoman side, not opened); noise. No decipherment.
3. `"Roell" "Dedem" 1809 cipher letter DECODE R1469 OR "Legatie in Turkije" nomenclator` -- Bourdeau's index page
   (already cited); de-crypt.org; nomenclator articles. No decipherment.
4. `Van Dedem tot de Gelder ambassadeur Constantinopel 1809 geheimschrift code Croiset` -- NA 2.21.049 (Van Dedem
   family), 2.21.006.46 (F.G. van Dedem's own papers, 1781-1818), 1.02.20 inv. 756, NNBW entry, Tor & Schmidt
   "Per koets naar Constantinopel". No decipherment; nothing on Croiset.

(b) Blog site searches, three:
- Cipherbrain (`site:scienceblogs.de klausis-krypto-kolumne Dedem Konstantinopel 1809 verschlüsselt Niederlande`):
  **hit** -- "Top-25 der ungelösten Verschlüsselungen, Platz 10: Das Van-Gelder-Kryptogramm", Klaus Schmeh, 8 Aug
  2013 (scienceblogs.de/klausis-krypto-kolumne/2013/08/08/...). The post describes this letter (9 Feb 1809, the
  Dutch ambassador in Turkey Dedem van Gelder, about 1,500 numbers in a nomenclator with values to about 3,000,
  homophones suspected), supplied by Karl de Leeuw, who "has not found" the nomenclator in a Dutch archive and
  holds that locating it is the only realistic route. Comment thread read in full: two comments (Jayson Matix, 29
  Jul 2014, suggests Dutch/French skills and the Testa family; leah16, 21 Apr 2016, speculates only underlined
  numbers count) -- no solution, no key, no plaintext. Also opened: "Top-25-Krypto-Rätsel wahrscheinlich gelöst
  (Teil 2)", 14 Jan 2016, page 2 -- covers the Konkordientag cryptogram only, no mention of Van Gelder/Dedem.
- Cryptiana blog (`site:cryptiana.blogspot.com Dutch 1809 Dedem Constantinople cipher OR Röell`): forum root, Sept
  2025 index, unrelated Wikipedia pages. Nothing on this letter (Tomokiyo's dutch.htm already checked, 24 Sept).
- Cipher Mysteries (`site:ciphermysteries.com Dutch legation Constantinople 1809 cipher Dedem`): Golden Dawn,
  Voynich, Van Heeck, d'Agapeyeff. Nothing.

Verdict unchanged (`open`): no decipherment, key or plaintext of R1469/R1470 on the open web or in the three blogs'
posts and comment threads. New facts for the folder: the letter is Schmeh's Top-25 no. 10 (2013) and came to him
from Karl de Leeuw, so the two best-placed people have looked for the key without finding it.

## LIKELY-7 (2 Oct 2026, account-4)

Worker LIKELY-7-roell-vandedem-1809 (Fable 5.1), brief `.claude/briefs/runs/2026-10-02-account4-likely-phase2.md`,
row 7 of `ciphers/_triage/likely-solves-2026-10-02.tsv`: first cheap test = the candidate period key NA 1.02.20
inv. 164 (QUEUE.md VX-E02). Intake gate: exit 1 on the web/blog check only (section above), exit 0 after (output
at the end of this section). Box 04:24-05:14 UTC, cap USD 7; 2 vision calls (both used), no subagents.

**Availability (route: item page drupal-settings-json, CLAUDE.md hosts table).**
`www.nationaalarchief.nl/onderzoeken/archief/1.02.20/invnr/164`: `availability: DIGITALIZED`, 78 scans, each with
a `default` JPEG URL and an IIIF base on service.archief.nl (all 78 saved in `images/na_1.02.20_164_viewer.json`,
no further request needed). 11 scans fetched once at 1000 px width (`images/p*_w1000.jpg`, manifest.json).

**Date (finding aid, fetched once as EAD XML, `.../archief/1.02.20/download/xml`).** inv. 164 = "Sleutels
cijferschrift, 1747, 3 katernen en enige losse stukken", subseries ELBERT DE HOCHEPIED (1747-1763). The scout's
"undated, early-18th-c. hand" (VX-E02) is the inventory's 1747. Not the letter's decade.

**What the 78 scans hold (vision call 1, contact sheet of scans 1, 3, 9, 13, 21, 39, 41, 47, 63, 68, 76;
`images/inv164_contact_11scans.jpg`).** Scans 1-8: a large loose ruled table, red-ruled columns, numbered
word entries (Dutch and French: "aan de", "aan den", "abandon", "abord", "adroit" ...). Scans 9-21: narrow
alphabet strips (a-z over two-digit numbers; small substitution tables). Scan 39: a numbered list of place and
person names. Scan 41: a marbled-cover booklet labelled "Ciffer ... 1747". Scan 47: the booklet's alphabetical
word list (columns J, K, L, M) with numbers. Scan 63: a numeric table headed "Om te ontcijfferen". Scan 68: a
nomenclator page (places, months, with numbers). Scan 76: blank ruled leaves. So: several keys of the 1747
legation, as the inventory says.

**Range of the large table (vision call 2, header strips of scans 1 and 3 enlarged 2x,
`images/inv164_scan001_003_headers.png`).** Scan 1's columns are based 100, 200 ... 900 (entries 1-9 at the
top, then 10, 100 "ad", 200, 310, 410, ...); scan 3's columns are headed 2000, 2100, 2200 ... 2900 ("plein",
"plus", "poli-", "post", "pour" ... in the 2000s). The table is a one-part (alphabetical = numeric) word code of
about 3,000 entries, undated within a bundle the inventory dates 1747. The letter's groups (Bourdeau's parse of
the DECODE transcription, now on disk in `decode_transcription/`): 2,585 groups, 931 distinct, max 3264; 45.6%
above 900, 14.1% above 1500, 3.3% above 2500. The range is compatible, which the scout's "~900 entries" reading
would not have been. Bourdeau's argument that the code "is not one-part" rests on the frequent groups being
spread 35-2920; in a 3,000-entry alphabetical word code the French function words (de, et, la, le, pour, que,
vous ...) are spread across the alphabet too, so that spread does not exclude this table. What does count
against it: 62 years between the bundle's date and the letter, and the heavy homophony Bourdeau measured (no
group above 1%).

**Key application: NOT run.** The row's test ("transcribe the key table, apply with decode_key.py vs shuffled
keys") needs the ~3,000-entry table read from 8 native scans (2 blind passes + reconciliation, ~17 vision calls),
beyond this brief's 2. No control was run because there is no key to shuffle. Grade counts: H 0, C 0, S 0, M 0,
I 0. Status stays `open`.

**Result of the first cheap test: NON-TEST on the row's premise** (inv. 164 is 1747, not 1809, by the archive's
own inventory), with one new fact that keeps it worth a second look (range match of the large table).

**Other key items in 1.02.20 (from the EAD, 0 further requests), all digitised (dao present), none in a series
after 1785:** inv. 17 "Sleutels geheimschrift, gebruikt bij correspondentie met de Staten-Generaal en
Nederlandse diplomaten, z.d." (Colyer, 1682-1725); inv. 628 "Sleutel geheimschrift. 1764" (Dedel 1765-68); inv.
686 "Sleutel geheimschrift. z.d." (De Weiler 1768-76); inv. 785 "Sleutel geheimschrift. z.d." (Kroll 1784-85, Van
Dedem's immediate predecessor). The Van Dedem (1785-1793), Van Dedem (2) and Testa (1808-1810) series carry no
key item. So the 1809 code is not among the legation archive's own keys; it would have been issued by the
ministry in 1808-09 (Croiset), and the ministry's side is where to look: NA 2.01.08 (Buitenlandse Zaken
1795-1813) finding aid, grep "cijfer"/"Croiset" (1 request, EAD xml); Croiset's letters in Röell's papers
2.21.008.78 (not online, Bourdeau). A same-ministry same-era sibling: NA 1.02.13 (Legatie in Rusland) inv. 226,
Six van Oterleek's minutes 1808-1809 "In cijfercode op basis van het cijfer van Van Hogendorp", with inv. 228
"Cijfer, 1803 aug. 5" -- neither digitised (EAD, no dao), so a different code anyway (Van Hogendorp's 1803
cipher), noted for the design prior only.

**Correction carried from Bourdeau (21 Sept 2026) into this folder:** 1.02.20 inv. 804 (174 scans, confirmed
"Yes" copy-free by scARCH on 24 Sept) holds clear Dutch copies of the legation's letters to the States General
1785-93, not the cipher pages; the real NA location of R1469/R1470 is unknown, and DECODE's images are
account-gated (sources/decode/NOTES.md). The folder's `images` are therefore of the candidate key, not of the
letter. Language: French per DECODE and per the one clear word "Monsieur"; the row's "judge nl" is replaced by
`fr1810` in the spec (era-matched, 1805-10 official French).

**Requests this pass:** www.nationaalarchief.nl 3 (item page 164, EAD 1.02.20, EAD 1.02.13); service.archief.nl 11
(IIIF, 1.6 s apart, all HTTP 200 image/jpeg); raw.githubusercontent.com 7 (Bourdeau NOTES.md, R1469/R1470
groups, parse.py; three 404 probes for file names); scienceblogs.de 2 (WebFetch); WebSearch 7. 0 DECODE requests.

**Next step (priced; a worker with its own vision budget):** crib-position test of the large inv. 164 table,
~USD 8: region-crop the 10 column bases of each of scans 1, 3, 5, 7 at native width (4 IIIF requests, local crops),
read the numbers of ~20 French function words and the column bases (~12 vision calls on crops), then compare
those numbers' frequency in the letter with 20 shuffled group lists; a hit (the function-word numbers ranking
in the letter's top decile) licenses the full transcription (~USD 35-40, 8 scans x 2 passes + reconciliation,
Usage 6 per-pass pricing) and decode_key.py vs 20 shuffled keys; a miss closes inv. 164 with a control-backed
negative. Independent of that: the NA 2.01.08 EAD grep for the ministry's 1808-09 code (~USD 1).

Intake gate after this pass (`python3 tools/intake_gate_check.py roell-vandedem-1809`, 04:33 UTC 2 Oct 2026):
`roell-vandedem-1809: open (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.

## Premise check (GF-A2-13, 3 Oct 2026)

Worker GF-A2-13 (account 2, LANE-A2PUSH), 01:36-01:4x UTC. Gate-fix only; no key application, no transcription.
(a) Decipherments the folder already mentions: **not found.** NOTES.md, HYPOTHESES.md and decode_transcription/
README.md mention no decipherment, gloss or clear copy of R1469/R1470. Bourdeau checked all 13 DECODE pages "page by
page" (his targets/roell1809/NOTES.md, "What the records hold"): "There is no interlinear, margin or separate
decipherment. The only clear words are an opening 'Monsieur' (R1469) and a docket on R1470 p.1." The R1470 docket
("? 69 Fermer? no? 9?" as DECODE read it) is the only unread clear-hand item; DECODE images are account-gated here,
so not viewed by this worker.
(b) Other solvers' working files: **not found.** Fresh shallow clone of dbourdeau/cyphersolver (3 Oct 2026),
targets/roell1809/: NOTES.md, parse.py, R1469/R1470 group lists, na804/na988 scan lists, turk_inv.txt, profile.json
-- no key file, no rendering, no apply-key script; his tests (DECODE keys, the Dedem 1788-93 code with its French
cribs, Van Spaen 1808, Fagel 1804, alphabetical ordering) all negative. aaymeloglu/unsolved-ciphers: `dedem`/`1469`
occur only in the raw DECODE catalogue files and in unrelated starhemberg-1758 numerals; no working file. Cited, not
copied. Schmeh's 2013 Cipherbrain post and its two comments (read by LIKELY-7) give no solution; one more web search
(`"Van-Gelder-Kryptogramm" OR "Van Gelder cryptogram" gelöst OR solved Dedem 1809`) returned no solved-list entry.
(c) Physical neighbours: **unreachable for the letter itself, not found in the neighbouring files.** The letter's
real NA location is unknown (DECODE's "1.02.04 ... inv. 804" is wrong on both counts, per Bourdeau and LIKELY-7),
so its own facing pages and adjacent leaves cannot be viewed outside DECODE's gated images. Bourdeau viewed the
nearest same-period files in 1.02.20 page by page: inv. 988 (Röell to Testa 1809-10, clear Dutch, no 9 Feb
despatch), inv. 990 (Van Dedem to Testa 1809-11, clear French, "Monsieur"), inv. 980 (Testa to Van Dedem copies
1808-11, copies of 10 and 26 Feb 1809, none of 9 Feb): no cipher, no decipherment.
(d) Recipient side: **lead found, not reachable online.** NA 2.21.006.46 (Van Dedem van de Gelder's own papers,
EAD fetched once, 3 Oct 2026, 94,937 bytes; grep for cijfer/chiffr/geheimschrift/ontcijfer/sleutel/Croiset/Röell:
no hit). Its introduction states that Van Dedem left Constantinople "voor goed 26 December 1808, na Gaspard Testa
tot chargé d'affaires aangesteld te hebben" -- so a 9 Feb 1809 French "Monsieur" letter fits Van Dedem (then at
Bucharest) to Testa or Testa to Van Dedem, as Bourdeau proposed, better than a letter to an ambassador in post. The
recipient-side files are inv. 73 "Brieven van Gaspar Testa aan Van Dedem van de Gelder. 1794-1811. 78 stuks", inv.
73A "Bijlagen tot brieven van Gaspar Testa aan Van Dedem van de Gelder. 1809. 2 stuks", and inv. 78 "Brieven van
Van Dedem van de Gelder aan Gaspard Testa te Konstantinopel. 1795-1815. 8 stuks". Only 2 items in the whole
inventory carry a digitisation link (both unrelated: loose notes on Constantinople; protégés' petitions); inv. 73,
73A and 78 have none (EAD, no dao), so not viewed. The two 1809 "bijlagen" (enclosures) to Testa's letters are the
nearest place a deciphered copy, key or clear duplicate could sit. Next: a reading-room or scan request for NA
2.21.006.46 inv. 73A (2 pieces) and the 1809 part of inv. 73; this is an owner-side copy order, not a cloud step.
Result: no decipherment, key or plaintext of R1469/R1470 found; status line unchanged.
Requests: www.nationaalarchief.nl 2 (EAD 2.21.006.46; item page 73A, which carried no availability field);
WebSearch 1; github.com 2 shallow clones (shared with the other targets of this job).

## Next step (READ2-RELABEL, 3 Oct 2026)
What is on disk is the candidate key's images, not the letter's: images/ holds 11 scans of NA 1.02.20 inv. 164 (the 1747 key bundle, 78 scans, availability DIGITALIZED) at 1000 px, with every scan's native URL in images/na_1.02.20_164_viewer.json, and decode_transcription/ holds the letter's own groups (R1469, R1470; 2,585 groups) from the transcription, not from page images. The next step is the LIKELY-7 priced crib-position test of the large inv. 164 table: native region crops of the column bases of scans 1, 3, 5 and 7 (5000x3904, 4 requests), about 12 vision calls on crops reading the numbers of ~20 French function words, then their frequency in the letter against 20 shuffled group lists; ~USD 8. A hit licenses the full table transcription (~USD 35-40); a miss closes inv. 164 with a control-backed negative. Independent of that, ~USD 1: grep the NA 2.01.08 finding aid for the ministry's 1808-09 code. Still outstanding for the other half: the recipient-side file NA 2.21.006.46 inv. 73A (Testa to Van Dedem, 1809, 2 items) shows no availability field online, so a scan request to the Nationaal Archief is a speculative lead (GF-A2-13 premise check (d)); nothing new is filed here, and the target stays open.

## READ2-ROELL (3 Oct 2026)

Worker READ2-ROELL (account 2, for LANE-READ2), brief `.claude/briefs/runs/2026-10-03-acct2-read2-roell.md`, 23:37-23:5x UTC.
Pre-registration committed before any image read: `inv164/PREREG.md` (commit 72939949). Status unchanged: `open`.

**Route.** Natives of scans 1, 7, 3 from their `default` URLs on service.archief.nl (one at a time, 1.6 s apart, descriptive
UA; served 5000x39xx JPEGs of ~1.9 MB; not kept, sha1 in `inv164/manifest.json`), 1000 px IIIF of scans 2, 4, 5, 6, 7, 8 to
locate the code ranges (not kept). Crops: `python3 tools/iiif_lines.py --image <native> --region 650,60,4350,3700 --centres
455,1365,2275,3185 --max-width 2400 --overlap 150 --out <scratchpad>/crops --prefix s00N --debug` (the row-profile detector
mis-reads a ruled table, so band centres by eye); 16 crops of 2400x910 committed in `inv164/crops/` (6.3 MB).

**What the table is (corrects LIKELY-7's "one-part, 1-~3000").** Scan 1 = codes 1-1000 (a-g); scan 7 is a second
photograph of scan 1; scans 2, 4, 6, 8 are blank; scan 3 = 2001-3000 (p-z); scan 5 = 3001-~3500 (w-z, names, the years
1776-1799) plus a Dutch note that names a cipher of 1776 (not read in full). Codes 1001-2000 (g-p) are on none of scans 1-8.
Layout: ten [word | number] blocks across the sheet, the number to the RIGHT of its word (the leftmost cell is a word and
the rightmost a number; blocks 1-5 hold x001-x500 and 6-10 x501-x1000 as two row-wise alphabetical streams). Each block's
last rows (x89-x00) hold a sub-block of short entries (a, de, en, et, il, ne, se, la, le, les, que ...). Common words carry
many homophones ("de" 14 cells, "en" 11 on the two sheets read), so the table is the same broad design as the letter (no group above 1%).
One Sonnet reader of band 1 took the number as left of its word; I checked every function-word cell against the crop.

**Test (PREREG statistic S1; `python3 inv164/score.py`, output in `inv164/score_out.txt`).** 80 codes for 18 of the 20 words
(`inv164/function_codes.tsv`; pas and par lie in the missing 1001-2000 sheet, and il/la/le/les/ne appear only in the
bottom sub-blocks there). Letter frequency of those 80 codes: **S1 = 76 of 2,585 groups (2.94%)**, S2 = 1. Control, 1,000
random sets of 80 codes from the read ranges (1-1000, 2001-3000): **mean 67.4, p95 98, p99 114**; 278/1000 sets score at
least the target. Control from 1-3000: mean 69.0, p99 117. Number-left sensitivity (all codes -100): S1 = 81 for 69 codes,
also at control level. If this table keyed the letter, 18 French function words would fill about a quarter of a French text
(several hundred groups); they fill 2.9%, at the random level. **Verdict: FAIL -- inv. 164 does not key this letter
(control-backed),** conditional on Bourdeau's parse of the DECODE transcription (rule 2; the letter's own images were not
viewed). Grade counts: H 0, C 0, S 0, M 0, I 0 (no reading). The full-table transcription (~USD 35-40) is not licensed.

**Requests:** service.archief.nl 9 (3 natives, 6 IIIF 1000 px), all HTTP 200; no other host. Subagent calls: 8 Sonnet
readers (one per band of 2 crops); the worker's own check of the function-word rows (vision on the crops).

**Next step (one line, for the lane):** the ministry side for the 1808-09 code: grep the NA 2.01.08 EAD for
cijfer/chiffre/Croiset (~USD 1, LIKELY-7); the scan 5 note on the 1776 cipher dates the inv. 164 table and is worth
one read for the design prior (KEY-DESIGN), not for this letter.

## D2B-ROELL (5 Oct 2026): NA 2.01.08 finding-aid grep for the 1808-09 code

Worker D2B-ROELL (account 2, for LANE DEFAULT-account-2-20261005-2217), brief
`.claude/briefs/runs/2026-10-05-account2-default-2217-jobs.md`, 23:52-23:55 UTC. Finding aid only; no scan read, no decoding.
Status unchanged: `open`. Grade counts: H 0, C 0, S 0, M 0, I 0 (no reading).

**Route.** `www.nationaalarchief.nl/onderzoeken/archief/2.01.08/download/xml` fetched once (HTTP 200, 419,081 bytes, sha1
02aa293e...; title "Inventaris van het archief van het Ministerie van Buitenlandse Zaken, 1796-1810"); grepped the full text
for cijfer, ciffer, chiffr, geheimschr, sleutel, Croiset, codeur, ontcijf, Röell/Roell, Dedem, Testa, Turkije. Availability
from each item page's `drupal-settings-json` (CLAUDE.md hosts table), not from the EAD's `dao` handle. The scans' IIIF
`info.json` URLs for the three items below are saved in `na20108/iiif_info_urls.json` (no further item-page request needed).

**Found.**
- **No key item.** 0 hits for cijfer/ciffer/chiffr/sleutel/ontcijf/Croiset anywhere in the 2.01.08 inventory, including the
  introduction. The ministry's own 1808-09 code (key or table) is not described in this finding aid.
- **inv. 204A** -- "Kopieën van ingekomen en uitgaande brieven van en aan gezanten, welke door de codeur van het Departement
  van Buitenlandse Zaken in geheimschrift werden overgezet. 1795-1807. 1 pak" (the only `geheimschrift`/`codeur` hit; filed
  after 196-204 Rekwesten). Availability **DIGITALIZED, 274 scans**. Clear copies of letters the ministry's codeur put into
  cipher -- plain/cipher pairs of the department's own system -- but the dates stop at 1807, a year before Röell took office
  (KB 8 Jan 1808, per the inventory's introduction). Useful for the design prior of the ministry's code just before 1808, and
  if the 1808-09 code continued it, as a source of cribs; not a key for 1809 on its face.
- **inv. 348** (3.2.20 Turkije) -- "Missiven van de ambassadeur F.G. van Dedem van de Gelder, 1 jan 1808 - 7 feb 1809;
  Missiven van de chargé d'affaires Gasp. Testa, 24 feb 1809 - 6 jul 1810." Availability **DIGITALIZED, 508 scans**. The
  incoming side from Constantinople; the 9 Feb 1809 letter falls in the 17-day gap between the two series as described, so it
  is not described here, but deciphered or clear despatches from the same two men in the same weeks may be.
- **inv. 92** -- "Gewone en geheime minuten van uitgaande missiven en rapporten", jan 1809 - mrt 1809 (series 65-98).
  Availability **DIGITALIZED, 523 scans**. If the letter is the minister's (Röell's) to Van Dedem or Testa, its minute --
  the clear draft before enciphering -- would sit here. Also inv. 100, "Verbalen van uitgaande stukken" 1809 (EAD `dao`
  present; item page not fetched).
- Context only: inv. 273 (Jacobson, 14 Oct 1808 - 20 Feb 1809) and the other legations' missives carry no cipher wording.

**Not found.** No key, cipher table, "cijfer" volume or Croiset item in NA 2.01.08 (EAD full text, 5 Oct 2026). Croiset's
letters in Röell's own papers (2.21.008.78, Bourdeau) were not checked by this job.

**Next step (priced, one line):** find a 9 Feb 1809 minute to Van Dedem/Testa in inv. 92 (523 scans, Jan-Mar 1809,
presumably chronological): fetch 1000 px IIIF of ~4 scans to bracket early February, then read the ~20-40 scans of 5-12 Feb
for a minute addressed to Constantinople, one scan per vision call (~USD 4-6); a clear minute of the same letter would be a
C-grade crib for R1469/R1470 (and a plaintext). Inv. 348's last Van Dedem / first Testa scans are the cheaper second look
(~USD 2). inv. 204A (274 scans, 1795-1807) is for KEY-DESIGN, not this letter.

**Requests:** www.nationaalarchief.nl 4 (EAD 2.01.08; item pages 204A, 348, 92), all HTTP 200, >= 2 s apart; no other host.

## D2B-ROELL2 (6 Oct 2026): the 9 Feb 1809 window in NA 2.01.08 inv. 92

Worker D2B-ROELL2 (account 2, for LANE DEFAULT-account-2-20261005-2217), brief
`.claude/briefs/runs/2026-10-05-account2-default-2217-jobs.md`, 00:14-00:20 UTC by `date -u`. Page images read by eye
(IIIF 700-900 px views plus three header crops), no subagent, no decoding. Status unchanged: `open`. Grade counts: H 0, C 0,
S 0, M 0, I 0 (no reading). Per-scan log: `na20108/inv92_scans.tsv` (scan, folio, date as written, addressee).

**Layout of inv. 92.** One bound volume of minutes in strict date order, ordinary and secret together (no separate secret
block was seen at the February/March boundary or at the end): January to scan ~174, a "Februarij 1809" cover at scan 175,
February to scan ~330 (scan 318 = 27 Feb, fol. 256), March from about scan 331 (334 = 2 March, fol. 269) to scan 521
(31 March, fol. 409). Months are written in Dutch as Sprokkelmaand/Lentemaand as well as Februarij/Maart (scan 350 is
"6en van Lentemaand", i.e. 6 March, not February -- a first misreading corrected by the 9 March and 15 March headers).

**The 9 Feb 1809 window, read in full.** 8 Feb ends at scan 208 (fol. 165, to Larochefoucauld); 10 Feb begins at scan 224
(fol. 171, to the King). Every scan between, 209-223, was viewed. The 9 Feb minutes are: to the King (fol. 166, consul at
Rouen); the Minister van Oorlog (fol. 167); Marshal Verhuell in Paris, No 13 and No 14 (fol. 168-169, Dutch); a French
minute to a member of the Dutch embassy in Paris (fol. 170); and the Staatssecretaris (fol. 170bis) with an 8-page
enclosure of corrections to the Koninklijke Almanak for 1809 (scans 216-223). **No minute to Van Dedem, Testa or
Constantinople is filed under 9 Feb 1809.** None of the 9 Feb minutes viewed carries a note of encipherment (no
"in cijfers"/"en chiffre" marginal seen at this resolution; the marginal notes are registration marks of the "(I.S. 9 Feb)"
kind).

**One context fact (read, not graded).** The almanac enclosure, scan 223, "Turkijen pag. 85": "De Baron van Dedem tot de
Gelder ... valt weg"; "De Heer [Testa], secretaris van legatie en charge d'affaires" -- on 9 Feb 1809 the ministry was
already listing Testa, not Van Dedem, as the post's head for the 1809 almanac. This fits inv. 348's change of series
(Van Dedem to 7 Feb 1809, Testa from 24 Feb 1809) and makes an outgoing ministry letter to Van Dedem dated 9 Feb less
likely than a letter *from* the Constantinople legation (Van Dedem's last or Testa's first), which would sit in inv. 348 or
in the legation archive 1.02.20, not here. Inference, not established.

**Not found / not searched.** No 9 Feb minute to Constantinople in inv. 92 (scans 209-223 complete). Not searched: the other
February dates (only 200, 208, 230, 245, 318 sampled), so a minute to Constantinople dated otherwise (e.g. a covering
letter that the cipher letter answers or encloses) is not excluded; January and March were bracketed, not read.

**Next step (priced, one line):** inv. 348's scans around the break (Van Dedem's last despatches to 7 Feb, Testa's first
from 24 Feb) for a clear or deciphered copy of a 9 Feb letter from Constantinople (~USD 2-3, bisect by date as here,
<= 30 requests); then a page-by-page read of February in inv. 92 for any minute to Constantinople (~scans 176-330, ~USD 4).

**Requests:** service.archief.nl 35 (32 full-opening views at 700-900 px, 3 header crops), all HTTP 200, >= 2 s apart; no
other host. Subagent calls: 0.

## D2B-ROELL3 (6 Oct 2026): NA 2.01.08 inv. 348, the Van Dedem / Testa handover

Worker D2B-ROELL3 (account 2, for LANE DEFAULT-account-2-20261005-2217), brief
`.claude/briefs/runs/2026-10-05-account2-default-2217-jobs.md`, 00:37-00:42 UTC by `date -u`. Page images read by eye (IIIF
700 px openings plus four 1400 px header/body crops), no subagent, no decoding. Status unchanged: `open`. Grade counts: H 0,
C 0, S 0, M 0, I 0 (no reading). Per-scan log: `na20108/inv348_scans.tsv` (22 scans).

**Layout of inv. 348.** Not one chronological run. The pak opens with the bundle received in 1809: Van Dedem's last despatches
(No 47, Constantinople 25 Nov 1808, rec. 7 Jan 1809, scan 2; No 48, 10 Dec 1808, scan 8) and Dutch letters of his (scans 17,
20 -- the latter dated "den 31 van Hooymaand 1809", on travel costs for his return to Holland), then Testa's numbered series
from scan ~22 (No 1, 11 Jan 1809, scan 30; No 3, 12 Jan, scan 22; No 5 and No 6, both 19 Jan, scans 34-36; No 7, 10 Feb,
scan 40; No 16/18, 10 May, scan 80; No 36, 11 Dec 1809, scan 200). The 1808 Van Dedem series follows later (scan 350 = No 3,
5 March 1808). Within the 1809 bundle the order is not strictly by number (No 3 at scan 22 before No 1 at scan 30).

**The handover, read.** The inventory's dates (Van Dedem to 7 Feb 1809, Testa from 24 Feb 1809) are not the writing dates.
Van Dedem's No 48 (10 Dec 1808, scan 13) says he will leave Constantinople by Bucharest and Vienna and present Testa to the
Porte as chargé d'affaires during his absence; Testa's No 1 (11 Jan 1809, scan 30) reports that Van Dedem left the residence
on the 2x of the previous month (December 1808). From January 1809 the legation's despatches are Testa's.

**The 9 Feb 1809 window.** Testa's No 6 is dated 19 Jan 1809 (scan 36) and No 7 is dated 10 Feb 1809 (scan 40); No 7 opens by
citing "ma respectueuse Dépêche sous No 5 en date du 19 du passé" and goes straight on to the Dardanelles peace and the frigate
Seahorse, with no mention of a despatch of the 9th. **No despatch dated 9 Feb 1809 was seen in Testa's numbered series, and
every scan viewed (22 of 508) is in clear French or Dutch; no cipher groups, no "en chiffre" note and no deciphered
interlinear copy were seen.** If R1469 is a Constantinople despatch of 9 Feb 1809, it is not one of Testa's numbered ones
(No 6 and No 7 bracket it); an unnumbered or separately sent ciphered despatch, or one from Van Dedem on the road (he was
travelling by Bucharest/Vienna in Dec 1808-Feb 1809), is not excluded. Inference, not established.

**Not found / not searched.** Scans 3-7, 9-12, 14-16, 18-19, 21, 23-24, 26, 28-29, 31-33, 38, 41-42, 44-46, 48-79 were not
viewed, so an unnumbered enclosure or a cipher piece filed inside a despatch in the 1809 bundle is not excluded; nothing from
Van Dedem dated on the road (Bucharest, Vienna) was seen in the scans viewed.

**Next step (priced, one line):** read inv. 348 scans 3-79 in full (~75 openings at 700 px, by eye, ~USD 3-4, <= 2 sessions at
the 40-request limit) for any cipher piece, unnumbered despatch or Van Dedem letter from the road dated around 9 Feb 1809;
then the legation archive 1.02.20's own 1809 letter-book (outgoing side) for a 9 Feb 1809 minute.

**Requests:** service.archief.nl 29 (24 views at 700 px, 4 crops at 1400 px, 1 info.json), all HTTP 200, >= 2 s apart; no
other host. Subagent calls: 0.

## R8-ROELL4 (6 Oct 2026): NA 2.01.08 inv. 348 scans 3-79 read in full

Worker R8-ROELL4 (account 2, for LANE LANE-RUN8-account-2), brief `.claude/briefs/runs/2026-10-06-account2-run8-jobs.md`,
03:17-03:22 UTC by `date -u`. Page images read by eye (IIIF 1000 px openings, two per view), no subagent, no decoding. Status
unchanged: `open`. Grade counts: H 0, C 0, S 0, M 0, I 0 (no reading). Per-scan log: `na20108/inv348_scans_3-79.tsv` (60 scans
not viewed by D2B-ROELL3, plus scan 8 re-viewed to confirm the scan-number-to-canvas offset; with `inv348_scans.tsv` every scan
2-80 is now logged).

**Found.**
- **No cipher.** All 60 scans are clear French (Van Dedem's Nos 47-50, Testa's Nos 1-15 and 25-29, copies of notes and
  translated Ottoman documents) or clear Dutch (Van Dedem's letters after his return). No cipher groups, no "en chiffre" note,
  no deciphered interlinear copy, no key or table anywhere in scans 3-79.
- **No 9 Feb 1809 item.** Van Dedem's numbered series ends with No 50 (Constantinople 24 Dec 1808, "Exhib. 7 Februarij 1809",
  scan 14; scan 15: audience de congé the next day, departure the day after). Testa's series runs No 7 (10 Feb 1809) -> No 8
  and No 9 (both 25 Feb 1809, scans 42-44) -> No 10 (10 Mar) -> No 11 (24 Mar) -> No 12 (26 Mar); No 8 cites "ma Dépêche du 15
  janvier" and No 10 cites "No 8 du 25 du passé", so no Testa despatch of 9 Feb 1809 is implied by the series' own
  cross-references either.
- **Where Van Dedem was on 9 Feb 1809 (read, not graded).** Testa's No 8 (25 Feb 1809, scan 46): Van Dedem arrived at Bucharest
  on 10 January and left it on 31 January [1809] for Vienna; Testa expects the minister to hear of his arrival there from Van
  Dedem himself. On 9 Feb 1809 he was therefore on the road between Bucharest and Vienna, which fits an outgoing letter
  addressed to him there (R1469's attribution "Röell to Van Dedem") better than a despatch from Constantinople. Inference
  about R1469, not established.
- **Context on the channel (read, not graded).** Testa's No 26 (6 Jul 1809, scans 56-57, 65): the ministry (secretary-general
  Bosscha) had his despatches only to 19 Jan; packets of 10 and 26 April for Vienna were held at Buda, others presumed
  "égarés et interceptés"; he sends duplicates from 11 and 25 April and will write on thin paper "d'un format différent ...
  plus en petit" via merchants (the duplicates of Nos 25 and 26 at scans 70-75 are in that small hand). He speaks of
  interception and changes paper and route, not of cipher, in every scan viewed. No 28 (scan 77) sends a despatch "dans le
  pli de Mr W. Willinck que Mr l'Ambassadeur Van Dedem aura déjà présentée".

**Not found / not searched.** No cipher piece and no 9 Feb 1809 item in inv. 348 scans 2-80 (complete). Not searched: inv. 348
scans 81-508 (later 1809-1810 Testa and the 1808 Van Dedem series from ~scan 250), the legation archive 1.02.20's own 1809
letter-book (outgoing side), and inv. 92's other February dates.

**Verdict line:** `open` -- inv. 348's 1809 bundle (scans 2-80) carries no cipher and no 9 Feb 1809 piece; R1469 was most
plausibly written to Van Dedem on the road (left Bucharest 31 Jan 1809 for Vienna). Cheapest next: the ministry's outgoing
side for letters to Van Dedem at Vienna in Jan-Feb 1809 -- inv. 92 scans 176-230 (1-12 Feb, ~USD 2-3, <= 40 requests) for any
minute addressed to Van Dedem at Vienna or "en chiffre"; then 1.02.20's 1809 letter-book.

**Requests:** service.archief.nl 62 (61 full openings at 1000 px plus 1 duplicate fetch of scan 8; all HTTP 200, >= 1.6 s
apart, one at a time); no other host. Subagent calls: 0.

## R8-ROELL5 (6 Oct 2026): NA 2.01.08 inv. 92 scans 176-230, the ministry's outgoing side 1-10 Feb 1809

Worker R8-ROELL5 (account 2, for LANE LANE-RUN8-account-2), brief `.claude/briefs/runs/2026-10-06-account2-run8-jobs.md`,
03:52-03:57 UTC by `date -u`. Page images read by eye (IIIF 1000 px openings), no subagent, no decoding. Status unchanged:
`open`. Grade counts: H 0, C 0, S 0, M 0, I 0 (no reading). Per-scan log: `na20108/inv92_scans_176-230.tsv` (34 scans not
viewed by D2B-ROELL2, plus 175 re-viewed to confirm the scan-to-canvas offset; with `inv92_scans.tsv` every scan 175-230 is
now logged).

**Found.**
- **No minute to Van Dedem, Vienna or Constantinople.** The February minutes (cover at scan 176) run fol. 138 (3 Feb) to fol.
  177 (10 Feb), with some 1-2 Feb pieces filed after the 3 Feb ones (fol. 143-146). Addressees: the King (most), the French
  ambassador Larochefoucauld, Bangeman Huygens at Cassel (No 3, 3 Feb), a consul-general (No 1, 3 Feb; post read as Trieste,
  uncertain), the Vice-President of the Staatsraad, the Minister of Finance, and internal fee/fund letters of the
  secretary-general (Bosscha). The one Vienna item (scan 194, fol. 152, 6 Feb) is a French note to the **Austrian** chargé
  d'affaires at Amsterdam about the Gazette Royale, not a letter to Van Dedem.
- **No cipher.** Every scan is clear Dutch or French; no cipher groups, no "in cijfers"/"en chiffre" note, no key. The only
  confidential marking is "confidentiellement" in the text of a clear French minute to Larochefoucauld (8 Feb, fol. 163).
- With D2B-ROELL2's 9 Feb read (scans 209-223), **inv. 92 has no outgoing minute to Van Dedem or the Constantinople legation
  between 1 and 10 Feb 1809.** If R1469 (9 Feb 1809) is a ministry letter to Van Dedem on the road, its minute is not filed
  in this volume's February run to the 10th, although the finding aid describes inv. 92 as ordinary and secret minutes
  together ("Gewone en geheime minuten", D2B-ROELL); a letter written outside the ministry (the King's cabinet, another
  minister) is not excluded. Inference about R1469, not established.

**Not found / not searched.** Scans 231-330 (11-28 Feb), January (scans ~4-174) and March were not read in full, so a
later covering letter or an earlier one sent ahead to Vienna is not excluded. Not searched: the legation archive 1.02.20's
1809 letter-book; the King's cabinet papers for a letter to Van Dedem in Feb 1809.

**Verdict line:** `open` -- inv. 92 has no 1-10 Feb 1809 minute to Van Dedem, Vienna or Constantinople and no cipher;
cheapest next: the legation archive 1.02.20's 1809 letter-book (incoming side, Van Dedem's papers on the road) or the
January run of inv. 92 (scans ~100-174, letters sent ahead to Vienna before 31 Jan; ~USD 2-3, <= 45 requests).

**Requests:** service.archief.nl 35 (35 IIIF openings at 1000 px; all HTTP 200, >= 1.8 s apart, one at a time); no other
host. Subagent calls: 0.

## R9-ROELL6 (6 Oct 2026): NA 2.01.08 inv. 92, the January 1809 run (scans 100-173)

Worker R9-ROELL6 (account 2, for LANE LANE-RUN9-account-2), brief `.claude/briefs/runs/2026-10-06-account2-run9-jobs.md`,
05:37-05:45 UTC by `date -u`. Page images read by eye (IIIF 1000 px openings, two stacked per view; one local 3x crop of
scan 128's header from the image already on disk), no subagent, no decoding. Status unchanged: `open`. Grade counts: H 0,
C 0, S 0, M 0, I 0 (no reading). Per-scan log: `na20108/inv92_scans_100-173.tsv` (45 scans).

**Coverage.** Scans 100-140 read in full (16 Jan fol. 73 to 23 Jan fol. 107, every minute); 150, 158, 166, 173 sampled
(25, 26, 28, 31 Jan, fol. 116-136). The 45-request limit was reached; scans 141-149, 151-157, 159-165, 167-172 and 174
(23-31 Jan, about 30 scans) were not viewed, nor January before the 16th (scans ~4-99).

**Found.**
- **No minute to Van Dedem, Testa or Constantinople, and no cipher, 16-23 Jan 1809.** Addressees: the King, Larochefoucauld
  (French ambassador, several), Prince Dolgorouki (Russian envoy), Marshal Verhuell at Paris (No 9, No 10), the Dutch
  ministers at the Danish court (No 5-7) and at Munich (No 2, name uncertain), the order-commanders at Berlin and St
  Petersburg, the Ministers of Finance and of the Interior, the Public Debt, Zeeland, Rotterdam, the Bayreuth Kammer, the
  legation controller at Paris. Every minute is clear Dutch or French; no cipher groups, no "in cijfers"/"en chiffre" note.
- **The Constantinople decision (read in gist, not graded).** Scan 100 (fol. 73, 16 Jan 1809, to the King): the embassy at
  Constantinople (and the mission in Spain) is not to be re-filled; affairs there go to a chargé d'affaires, and the
  minister proposes Testa, secretary of legation, as chargé d'affaires on a daily allowance. This is the ministry's side of
  the handover inv. 348 shows, and dates it before 9 Feb.
- **A Vienna series opens on 20 Jan 1809.** Scan 128 (fol. 98, 20 Jan): "No 1", to Lieutenant-General Van Hogendorp,
  envoy extraordinary and minister plenipotentiary at the court of Vienna ("Weenen" read at low resolution; the 1.02.20 EAD's
  inv. 996, "Brieven van en aan D. van Hogendorp, gezant te Wenen. 1809", agrees). A long Dutch instruction; its first
  page, read at 1000 px, does not mention Van Dedem or Constantinople, and no cipher note was seen. With Van Dedem heading
  for Vienna (left Bucharest 31 Jan, R8-ROELL4), the ministry's Vienna envoy is the route a 9 Feb letter to him would
  plausibly take; NOTES.md line ~122 already records a Van Hogendorp cipher (1803) in use at the Russian legation in
  1808-09 (1.02.13 inv. 226). Inference, not established.

**1.02.20 (the legation archive), availability looked up (EAD fetched once, one item page).** The Testa-period series
holds: inv. 978 "Brieven aan W.F. Roël ... Afschriften. 1809-1810" (the legation's copies of its outgoing letters to the
ministry) -- item page `www.nationaalarchief.nl/onderzoeken/archief/1.02.20/invnr/978`, drupal-settings `availability:
DIGITALIZED`, 362 scans; inv. 980 (to Van Dedem, copies 1808-11), 987 (to A.B.G. van Dedem, copies 1808-10), 988 (Röell,
1809-10), 990 (Van Dedem at Bucharest, Vienna ..., 1809-11) and **996 (to and from D. van Hogendorp at Vienna, 1809)**, 997
(Silliman, legation secretary at Vienna, 1809-10) all carry a METS dao in the EAD (digitised; item pages not opened).
Bourdeau has viewed 980, 988 and 990 (Premise check above); 978 and 996 are not recorded as viewed by anyone in this folder.

**Not found / not searched.** No 16-23 Jan 1809 minute to Van Dedem or Constantinople in inv. 92 (scans 100-140 complete);
23-31 Jan only sampled; 1-15 Jan not read. Not searched: 1.02.20 inv. 978 and inv. 996 page by page.

**Verdict line:** `open` -- inv. 92 has no minute to Van Dedem or Constantinople 16-23 Jan 1809 and no cipher, but opens a
Vienna series (No 1 to Van Hogendorp, 20 Jan). Cheapest next: 1.02.20 inv. 996 (Hogendorp at Vienna, 1809, digitised) for
any piece passed to or from Van Dedem around 9 Feb 1809 or any cipher (~USD 2-3, <= 45 requests); then 1.02.20 inv. 978
around Jan-Feb 1809 (Testa's copies; 362 scans, bisect by date); then inv. 92 scans 141-174.

**Requests:** service.archief.nl 45 (IIIF /full/1000,/0/ openings; all HTTP 200, >= 1.9 s apart, one at a time);
www.nationaalarchief.nl 2 (EAD xml 1.02.20, item page 1.02.20/978; both HTTP 200). Subagent calls: 0.

## R9-ROELL7 (6 Oct 2026): NA 1.02.20 inv. 996, Testa and Van Hogendorp at Vienna, 1809 (all 22 scans)

Worker R9-ROELL7 (account 2, for LANE LANE-RUN9-account-2), brief `.claude/briefs/runs/2026-10-06-account2-run9-jobs.md`,
05:57-06:01 UTC by `date -u`. Page images read by eye (IIIF 1000 px openings; scans 19-22 from a 700 px contact sheet of
the same downloads), no subagent, no decoding. Status unchanged: `open`. Grade counts: H 0, C 0, S 0, M 0, I 0 (no
reading). Per-scan log: `na10220/inv996_scans.tsv`; IIIF info URLs: `na10220/inv996_iiif_info_urls.json`.

**What inv. 996 is.** Item page `www.nationaalarchief.nl/onderzoeken/archief/1.02.20/invnr/996`, drupal-settings
`availability: DIGITALIZED`, 22 scans (title "Brieven van en aan D. van Hogendorp, gezant te Wenen."). It is Testa's file of
his own letters to Van Hogendorp at Vienna, 11 Jan to 26 Jun 1809 (wrapper "Par Monsieur Gaspard Testa, Chargé d'Affaires
... près la Sublime Porte"; most marked "(signé) Gaspd. Testa", i.e. copies, scan 5 headed "Copie"), plus one original from
Van Hogendorp (Vienna, 3 Mar 1809, docketed received 29 Mar, answered 11 Apr). Every page is clear French; **no cipher
groups, no key, no "en chiffre" note anywhere in the 22 scans.**

**Found (relevant to R1469, 9 Feb 1809).**
- **Testa's 10 Feb 1809 cover to Van Hogendorp (scans 5-6, copy) carries an enclosure for Van Dedem.** It ends: "Je prie V.E.
  de vouloir bien donner cours au pli ci-joint pour S.E. le Ministre Röell et avoir la bonté de remettre à S.E. l'Ambassadeur
  Van Dedem que je suppose déjà à Vienne, celui à son adresse également ci-joint" (read at 1000 px; spelling normalized).
  So one pli for Röell and one for Van Dedem left Constantinople with the 10 Feb post. A 9 Feb 1809 French "Monsieur" letter
  (R1469) fits either enclosure by date. Inference, not established: the cover gives no date for the enclosures, and
  Bourdeau's read of inv. 980 (Testa to Van Dedem, copies) records copies of 10 and 26 Feb 1809 to Van Dedem and none of
  9 Feb, so the Van Dedem enclosure is more likely the 10 Feb copy in inv. 980 than R1469; the Röell enclosure is unchecked.
- Testa used Van Hogendorp as a forwarding post for both Röell and Van Dedem throughout: 16 and 22 Jan (plis for Röell and
  for "Monsr. l'Ambassadeur Van Dedem", by a French courier), 10, 25 and 26 Feb, 10 and 24 Mar ("les deux incluses pour
  Mrs Van Dedem Père et fils"), 11 and 25 Apr, 10 and 25 May, 26 Jun.
- Van Hogendorp, 3 Mar 1809: received Testa's letters of 11, 15 and 16 Jan and forwarded "les incluses pour S.Exc. le
  Ministre Röell" at once; "Monsieur l'Ambassadeur de Dedem vient d'arriver ici, il y a deux jours" (Van Dedem at Vienna
  about 1 Mar 1809). Testa's 10 Mar letter acknowledges the news.

**Not found.** No cipher, key or clear copy of R1469/R1470 in inv. 996; no letter dated 9 Feb 1809 in it; no Van
Hogendorp letter to Testa between 3 Mar and the end of the file (only the one original). Not searched: inv. 978 (Testa's
copies to Röell, 1809-10, 362 scans) for the pli sent with the 10 Feb cover; inv. 997 (Silliman at Vienna).

**Verdict line:** `open` -- inv. 996 holds no cipher and no 9 Feb 1809 letter, but shows a Röell pli and a Van Dedem pli
enclosed in Testa's 10 Feb 1809 cover to Vienna. Cheapest next: 1.02.20 inv. 978, Testa's copies to Röell, at early
Feb 1809 (bisect the 362 scans by date; <= 20 requests, ~USD 2) for a 9 or 10 Feb letter and whether it was sent in cipher;
then inv. 980's 10 Feb copy to Van Dedem compared against R1469's length and form (Bourdeau's scan list).

**Requests:** www.nationaalarchief.nl 1 (item page 1.02.20/996, HTTP 200); service.archief.nl 22 (IIIF /full/1000,/0/,
all HTTP 200, >= 1.9 s apart, one at a time). Subagent calls: 0.

## R9-ROELL8 (6 Oct 2026): NA 1.02.20 inv. 978, Testa's copies to Röell, early February 1809

Worker R9-ROELL8 (account 2, for LANE LANE-RUN9-account-2), brief `.claude/briefs/runs/2026-10-06-account2-run9-jobs.md`,
06:24-06:30 UTC by `date -u`. Page images read by eye (IIIF 1000 px openings, one 1400 px header crop), no subagent, no
decoding. Status unchanged: `open`. Grade counts: H 0, C 0, S 0, M 0, I 0 (no reading). Per-scan log:
`na10220/inv978_scans.tsv`; IIIF info URLs for all 362 scans: `na10220/inv978_iiif_info_urls.json`.

**What inv. 978 is.** Item page `www.nationaalarchief.nl/onderzoeken/archief/1.02.20/invnr/978`, `availability: DIGITALIZED`,
362 scans, "Brieven aan W.F. Roël, minister van Buitenlandse Zaken. Afschriften." Wrapper (scan 1): "1809-1810. A Son
Excellence Monseigr. W.F. Roëll ... à Amsterdam, par Monsieur Gaspard Testa ... et par intervalle à S.E. Msgr Mollerus, Van
Wickevoort Crommelin et Van der Heim". It is Testa's copy book of numbered despatches, in date order, every page in clear
French and signed "(signé) Gaspd. Testa".

**The early-February 1809 run (located by bisection: scans 1, 2, 6, 9-16, 30).**
- No 5, 19 Jan 1809 (scans 9-10); No 6, 29 Jan 1809 (scans 11-12); **No 7, Constantinople 10 Février 1809 (scans 13-14,
  header read at 1400 px)**; No 8, 25 Février 1809 (scans 15-16). The numbering runs straight on from No 6 to No 8 with no
  gap and nothing between them, so the copy book holds **no despatch to Röell dated 9 Feb 1809**.
- No 7 opens from Testa's No 5 of 19 Jan (the Dardanelles peace) and reports Adair's arrival at Pera, the Smyrna consulate,
  Latour-Maubourg's courier to Napoleon of 16 Jan, American ships at Smyrna on 29 Jan and a sultana's birth on the 5th. Clear
  French throughout; no cipher groups, no blank left for a cipher passage, no "en chiffre" note on scans 13-14.
- So the "pli ci-joint pour S.E. le Ministre Röell" in Testa's 10 Feb cover to Van Hogendorp (inv. 996, R9-ROELL7) is most
  likely No 7 of 10 Feb, dated the same day as the cover. Inference, not established: a copy book records text, not the
  form in which the original went out, so it cannot show whether No 7 left in cipher. Its length (about three pages of copy)
  and its "Monseigneur" address do not match R1469 (a 7-page "Monsieur" letter dated 9 Feb).

**Not found.** No cipher, key or clear copy of R1469/R1470 in the scans read; no 9 Feb 1809 item. Not read: scans 3-5, 7-8
(Nos 1-4, early-mid January) and 17-29, 31-362 (March 1809 onwards, outside the brief's window).

**Verdict line:** `open` -- inv. 978 holds no 9 Feb 1809 despatch to Röell (No 6 of 29 Jan runs straight on to No 7 of
10 Feb and No 8 of 25 Feb, all in clear copy), so the Röell enclosure of 10 Feb is most likely No 7, not R1469. Both plis of
the 10 Feb cover are now matched to clear 10 Feb copies (inv. 978 No 7; inv. 980, per Bourdeau's read). That points R1469
away from Testa as the writer to either addressee. Cheapest next: inv. 980's 10 Feb copy to Van Dedem compared against
R1469's length and form (one or two scans, ~USD 0.5), then whether R1469 is an incoming letter *to* the legation (from Van
Dedem or the ministry) rather than an outgoing one.

**Requests:** www.nationaalarchief.nl 1 (item page 1.02.20/978, HTTP 200); service.archief.nl 13 (IIIF, 12 openings at
1000 px + 1 header crop, all HTTP 200, >= 1.9 s apart, one at a time). Subagent calls: 0.

## R10-ROELL9 (6 Oct 2026): NA 1.02.20 inv. 980, Testa's copies to Van Dedem, the 10 Feb 1809 letter

Worker R10-ROELL9 (account 2, for LANE LANE-RUN10-account-2), brief `.claude/briefs/runs/2026-10-06-account2-run10-jobs.md`,
07:22-07:27 UTC by `date -u`. Page images read by eye (IIIF 1000 px openings; header and P.S. crops at 1400-1600 px), no
subagent, no decoding. Status unchanged: `open`. Grade counts: H 0, C 0, S 0, M 0, I 0 (no reading). Per-scan log:
`na10220/inv980_scans.tsv`; IIIF info URLs for all 143 scans: `na10220/inv980_iiif_info_urls.json`.

**What inv. 980 is.** Item page `www.nationaalarchief.nl/onderzoeken/archief/1.02.20/invnr/980`, `availability: DIGITALIZED`,
143 scans, "Brieven aan F.G. van Dedem van de Gelder. Afschriften." Testa's letters to Van Dedem in date order, from
Constantinople le 30 Xbre 1808 (scan 1). The run read here is entirely in clear French, apart from Dutch passages from March
1809 on (below); each letter opens "Excellence!" (or "Exc.") and the copies are signed "(signé) Gd. Testa".

**The early-February run (located by bisection: scans 1, 72, 12, 24, 18, 23, then 10-17).**
- Scan 10 left: end of the letter of 25 Jan 1809, with a P.S.: "Ayant écrit le 19 ct au Mr Roëll par le C[ourier] fr[ançais]
  qui n'est parti que la nuit passée, et faute de matière digne de son attention je me dispense de lui adresser aujourd'hui
  une nouvelle dépêche. Le change sur Amsterdam est à 65." (day read as 19; the "1" is faint.)
- **Scans 10 right to 16 left: the 10 Feb 1809 letter**, headed "Copie" in the margin, "Constple le 10 février 1809",
  "Excellence!", signed "(signé) Gd. Testa". It opens "Depuis l'acheminement de ma précédente en date du 25 janvier, que
  j'ai adressée à Mess. Geymuller & Cie à Vienne", so **Testa wrote Van Dedem nothing between 25 Jan and 10 Feb; there is no
  9 Feb item.** Length: about 12 pages of copy (half of scan 10 and of scan 16, all of scans 11-15). Content: Van Dedem's
  letters from Bucharest of 17 and 21 Jan, the firman and the Janissaries, the inventories and sale of furniture, Adair at Pera
  since 27 Jan, Hochepied after the Dardanelles event of 5 Jan, the rupture with the Austrian legation, a request for an
  "ostensible" letter from Minister Röell, the birth of Sultan Mahmud's daughter, five enclosed letters. On scan 14 Testa
  writes "V.E. verra par la copie de la Dépêche d'aujourd'hui, que je lui transmets ci-joint": Van Dedem also got a copy of
  that day's despatch, i.e. of No 7 to Röell (inv. 978, R9-ROELL8). No cipher groups, no blank left for cipher, no "en
  chiffre" note anywhere in scans 10-16.
- Scan 16 right: the next letter, "Constple le 2[5 or 6] février 1809" (second digit overwritten; Bourdeau has 26), "Exc.",
  referring to "ma précédente du 10 ct". So inv. 980's February run is 10 Feb and 25/26 Feb only, as Bourdeau recorded.
- From 24 March (scan 23) Testa switches into Dutch, underlined, for one sensitive passage (breaking off relations with the
  Austrian legation in case of war), and scan 24 is wholly in Dutch; scan 17 notes Van Dedem had asked him to write in
  Dutch. A change of language, not a cipher; recorded because it shows how this correspondence kept passages private.

**Compared with R1469 (7 pages, "Monsieur", 9 Feb 1809).** The 10 Feb copy is a different letter: different date, about 12
pages against 7, "Excellence!" against "Monsieur", clear French throughout, and Testa addresses Van Dedem as "Excellence"
in every letter seen here (30 Dec 1808, 10 Feb, 25/26 Feb, 24 Mar 1809). **So inv. 980 shows R1469 to be neither a copy of
a Testa letter to Van Dedem nor any letter of 9 Feb in this file.** Inference, not established: the address form argues
against Testa -> Van Dedem as the pair behind R1469 at all, since a chargé d'affaires writing to his ambassador uses
"Excellence"; a "Monsieur" letter fits a writer of equal or higher rank to a lower-ranked addressee (e.g. Van Dedem to
Testa, as inv. 990 is addressed per Bourdeau, or the ministry to a chargé). Not checked: the length of a cipher page against
a page of copy (2,585 groups over R1469 and R1470 together; the split per letter is not on disk), so the page counts are a
weak comparison.

**Not found.** No cipher, key or clear copy of R1469/R1470 in the 16 scans read; no 9 Feb 1809 item in inv. 980. Not read:
scans 2-9 (30 Dec 1808 to 25 Jan 1809), 19-22, 25-71, 73-143.

**Verdict line:** `open` -- inv. 980 holds no 9 Feb 1809 letter (Testa's letters to Van Dedem run 25 Jan -> 10 Feb ->
25/26 Feb), and its 10 Feb copy is a different, clear, ~12-page "Excellence!" letter that encloses a copy of No 7 to Röell.
Both plis of the 10 Feb cover to Van Hogendorp are now matched to clear 10 Feb letters seen on the page (inv. 978 No 7,
inv. 980 10 Feb), and neither is R1469. Cheapest next: test R1469 as an *incoming* letter -- inv. 990 (Van Dedem to Testa,
1809-11, "Monsieur" per Bourdeau) at its early-February 1809 run for a 9 Feb letter, and whether any letter there says
"en chiffre" or encloses a cipher (bisection, <= 20 requests, ~USD 2).

**Requests:** www.nationaalarchief.nl 1 (item page 1.02.20/980, HTTP 200); service.archief.nl 16 (IIIF, 12 openings at
1000 px + 4 region crops, all HTTP 200, >= 1.9 s apart, one at a time). Subagent calls: 0.

## R10-ROELL10 (6 Oct 2026): NA 1.02.20 inv. 990, Van Dedem's letters to Testa, January-March 1809

Worker R10-ROELL10 (account 2, for LANE LANE-RUN10-account-2), brief `.claude/briefs/runs/2026-10-06-account2-run10-jobs.md`,
07:40-07:44 UTC by `date -u`. Page images read by eye (IIIF openings at 800-1000 px; the scan 2 header at a 1400 px crop), no
subagent, no decoding. Status unchanged: `open`. Grade counts: H 0, C 0, S 0, M 0, I 0 (no reading). Per-scan log:
`na10220/inv990_scans.tsv`; IIIF info URLs for all 83 scans: `na10220/inv990_iiif_info_urls.json`.

**What inv. 990 is.** Item page `www.nationaalarchief.nl/onderzoeken/archief/1.02.20/invnr/990`, `availability: DIGITALIZED`,
83 scans, "Brieven van F.G. van Dedem van de Gelder, te Boekarest, Wenen, Den Haag en Amsterdam." Wrapper (scan 1): "Lettres de
S.E. Mr le Baron van Dedem van de Gelder ... Ambassadeur de S.M. le Roi de Hollande près la Sublime Porte Ottomane, à Amsterdam,
à Mr Gaspard Testa Chargé d'Affaires ...". The originals as Testa received them, each docketed by Testa "Reçu le ..., rép. le ...".

**The January-March 1809 run (scans 1-15, all read).**
- Bucharest 17 Jan 1809 (scans 2-4; day read as 17, possibly 13), "Reçu le 2 févr. 1809, rép. le 10 dito".
- Bucharest 21 Jan 1809 (scan 5), "Reçu le 2 févr. 1809 par Giustiniani, rép. le 10 dito".
- "Duplicata" of 17 Jan 1809 (scans 6-8), same docket: Van Dedem sent duplicates by a second route, in clear.
- Bucharest 29 Jan 1809 with a P.S. "Bucharest den 31 January 1809" (scans 9-11), "Reçu le 16 févr. 1809, rép. le 25 dito"; a long
  passage and the P.S. are in Dutch (the same switch into Dutch for private matter that R10-ROELL9 saw in inv. 980).
- Scans 11 right to 14 left: enclosures, letters from Neuchâtel of Nov-Dec 1808 to Van Dedem ("Votre Excellence") passed on to Testa.
- **Next Van Dedem letter: Vienne 3 Mars 1809** (scans 14 right-15), "Reçu le 29 Mars, rép. le 8 Avril".
So **Van Dedem wrote Testa nothing between 31 Jan and 3 Mar 1809 in this file; there is no 9 Feb item.** The dockets close the loop
with Testa's side (inv. 980, R10-ROELL9): the 17 and 21 Jan letters came on 2 Feb and were answered 10 Feb (R10-ROELL9 read Van Dedem's
letters of 17 and 21 Jan in that answer), the 29 Jan letter came on 16 Feb and was answered 25 Feb. Inference: Van Dedem was most likely on the road from
Bucharest to Vienna in February (at Vienna about 1 Mar, inv. 996), which would explain the silence.

**Address form.** Every Van Dedem letter read here opens "Mon cher Testa!" (17, 21, 29 Jan, 3 Mar), not "Monsieur" as this folder's
Premise check recorded from Bourdeau's description; the "Monsieur" note is not confirmed by the pages. No cipher groups, no blank left
for cipher, no "en chiffre" note, no key in scans 1-15.

**Compared with R1469 (7 pages, "Monsieur", 9 Feb 1809).** Not in inv. 990: no letter of that date, and the Van Dedem -> Testa letters
use "Mon cher Testa!", not "Monsieur". With R10-ROELL9 (Testa -> Van Dedem: "Excellence!", no 9 Feb) and R9-ROELL8 (Testa -> Röell:
no 9 Feb), **neither direction of the Testa / Van Dedem correspondence, nor Testa's despatches to Röell, holds R1469 or a letter of its
date.** Inference, not established: the address form argues against the Testa-Van Dedem pair altogether, and R1469's date points to
some other correspondent of the legation or of the ministry; a cipher letter is also unlikely to appear in a file of originals that
holds only clear letters and clear duplicates.

**Not found.** No cipher, key or clear copy of R1469/R1470 in scans 1-15; no 9 Feb 1809 item in inv. 990. Not read: scans 16-83
(March 1809 onward, outside the brief's window).

**Verdict line:** `open` -- inv. 990 holds no 9 Feb 1809 letter (Van Dedem to Testa runs 17, 21, 29/31 Jan -> 3 Mar 1809, all clear,
"Mon cher Testa!"), so R1469 is neither an outgoing nor an incoming letter of the Testa / Van Dedem pair as preserved in 1.02.20
inv. 980 and 990. Cheapest next: R1469's real NA location (DECODE's "1.02.04 inv. 804" is wrong) is the open question; find which file
DECODE's images came from (the DECODE record's own image file names or source note, ~USD 1) before searching further files by date;
other same-date candidates in 1.02.20 are inv. 987 (to A.B.G. van Dedem, copies 1808-10) and 997 (Silliman at Vienna).

**Requests:** www.nationaalarchief.nl 1 (item page 1.02.20/990, HTTP 200); service.archief.nl 18 (IIIF: 12 openings at 1000 px,
4 at 800 px, 1 info.json, 1 header crop; all HTTP 200, >= 1.9 s apart, one at a time). Subagent calls: 0.

## R10-ROELL11 (6 Oct 2026): where DECODE's R1469/R1470 images come from

Worker R10-ROELL11 (account 2, for LANE LANE-RUN10-account-2), brief `.claude/briefs/runs/2026-10-06-account2-run10-jobs.md`,
07:59-08:08 UTC by `date -u`. No login (see below why), no subagent, no decoding. Status unchanged: `open`. Grade counts: H 0, C 0,
S 0, M 0, I 0 (no reading). Scan log: `na10220/inv804_806_scans.tsv`; IIIF info URLs: `na10220/inv804_iiif_info_urls.json`
(174), `na10220/inv806_iiif_info_urls.json` (217).

**What DECODE itself records (RecordsView/1469 and /1470, public without login).** Holder "Nationaal Archief, legatie Turkije,
inv.nr. 804"; no folio, no other provenance field. Dates: "1809 -" with start 1809-2-9 on R1469, taken from the record name
(`..._1809_02-09-1`; R1470 is `..._1809_02-09-2`, so both carry the same day and month). Author/receiver Röell -> Van Dedem are
the contributor's guess ("probably written by the Minister of Foreign Affairs ... not addressed nor signed ... Van Dedem was already
on his way home, when the letter was sent"). Record created 18 Feb 2020 by DECODE user 34; access mode "Authentication required".
The record links to 1947-1952, 2053, 2120-2122, 2131, 2134, 2141: Kroll, Van Dedem, Van Haeften and Van Schenck letters of
1776-1793 in NA 1.01.02 (States General) and 3.01.26 (Van de Spiegel) -- grouped by their 4-digit code, not by provenance (R2131's
own note: "the same codebook ... as in many other letters by Van Dedem, and also by Kroll, Wasmuht, Schenk and Van Haeften").
DECODE's transcription (SofPe, 2 Feb 2020, copy in Bourdeau's `targets/roell1809/decode/`) names the images 6681-6687 and
6688-6693 and marks the opening word **"Monsieur?"**, with a question mark: the "Monsieur" address is DECODE's tentative reading,
not established. The two public 200 px thumbnails of the first pages (6681, 6688) are **camera photographs** with a "2019 08 22"
date stamp, the leaves on a pink backing, not NA scans: someone photographed the originals in the reading room on 22 Aug 2019.
No archive stamp or folio number is legible at thumbnail size.

**Not reachable here:** image metadata (ImagesList) redirects to login, and that page is gated account-wide even when logged in
(sources/decode/NOTES.md, 24 Sept 2026); the transcription file and full images return DECODE's forbidden placeholder
(sha1 035489a0...). So no login was spent: it could not reach any field the public record view does not already show.

**What "inv. 804" is.** The 1.02.20 inventory (Bourdeau's `turk_inv.txt`, version 1 May 2021) numbers 804 in the **first Van
Dedem mission (1785-1793)**: "Uitgaande brieven aan de Staten-Generaal. Afschriften. 1785-1793. 8 katernen". Its concordance of
old numbers (Hardenberg 1932, 1-443; Fasel 1952, 495-939) has no older 804 that could point to the 1808-10 Testa series: Fasel 804
is today's inv. 1294 (a 1793 lawsuit, "Gerry en P. Apik Oglou"). So DECODE's number is a current 1.02.20 number, and it sits in the
1785-1793 series, not among the 1808-10 files that R8-R10 workers read (inv. 92, 348, 978, 980, 990, 996).

**inv. 804 holds a despatch of 9 February 1793.** Item page `www.nationaalarchief.nl/onderzoeken/archief/1.02.20/invnr/804`,
availability DIGITALIZED, 174 scans. Scan 152, right page: "Pera van Constant[inopel] den 9 February 1793 ... get. F.G. Van Dedem
van de Gelder", a clear Dutch copy of a despatch to the States General ("Hoog Mogende Heeren!") that runs from scan 150 right to
152 right; the next despatch opens "Van dat ik op den 9 dezer ...". The last signed copy is 24 Aug 1793 (scan 170), when Van Dedem
was about to leave Constantinople. The companion copy-book to the griffier, inv. 806 (DIGITALIZED, 217 scans, clear Dutch,
"Hoog Edele Gestrenge Heer"), ends with 27 Dec 1792 (scans 213-214): no 1793 letter there. Separately, DECODE R2131 is Van Dedem to
Van de Spiegel, **9 Feb 1793** (NA 3.01.26 inv. 212), with one paragraph in the 4-digit code, listed as unsolved.

**Inference, not established.** The inventory number DECODE gives, the day and month in both record names, and the code family
DECODE links them to all point to Van Dedem's first mission and to 9 Feb 1793, not to Röell in 1809; the "1809" may be the
contributor's year, written into the name from the guess that the letters were Röell's. Against it: (a) the 804 copy is Dutch to
the States General, while DECODE calls R1469 French on one uncertain word ("Monsieur?"); (b) Bourdeau found R1469/R1470's groups
overlap the decrypted Van Dedem 1788-89 letters (R1947, R2053, R2121) only at chance level (30-33% of distinct groups against a 28%
baseline), so if they are Van Dedem's of 1793 they use a different code or table than those letters -- which R2131, also unsolved
and also 9 Feb 1793, would fit; (c) NA's 174 scans of 804 show no cipher leaves (Bourdeau, page by page, 21 Sept 2026; this pass saw
scans 150-153, 160, 170, 174 only), so the photographed sheets are not in the scanned file as it is now, or are filed elsewhere.

**Is the original reachable?** Not online. DECODE's photographs are account-gated; NA's scans of inv. 804 show only the clear
copies. The physical sheets are cited by DECODE as in 1.02.20 inv. 804 (unverified; a reading-room or scan request would settle it).

**Not found.** No cipher leaves, key or decipherment in the 804/806 scans read; no 9 Feb 1793 item in inv. 806.

**Verdict line:** `open` -- DECODE's only provenance is "legatie Turkije inv. 804" (camera photos of 22 Aug 2019); inv. 804 is
Van Dedem's 1785-1793 series and holds a clear Dutch copy of his despatch of 9 Feb 1793 (scans 150R-152R). Cheapest next, in order:
(1) ~USD 1, disk only: compare R1469/R1470's groups with R2131's (9 Feb 1793, Van Dedem to Van de Spiegel), if DECODE's R2131
transcription is reachable (Bourdeau's `targets/dedem1788/` may hold it) -- a shared code would back the 1793 dating, with a shuffle
control; (2) ~USD 2-3: the States General's received copy of the 9 Feb 1793 despatch (NA 1.01.02, Levantse/Turkse lias 1793,
where Kroll's cipher letters of 1784-85 sit decrypted in inv. 7009) for a cipher original with an interlinear decipherment;
(3) ~USD 3: transcribe the 804 copy (scans 150R-152R) and compare its length with R1469's 1,297 groups, a weak check on its own.

**Requests:** de-crypt.org 7 (RecordsView 1469, 1470, 2131; ImagesList 1469 -> 302 to login; 1 transcription file -> forbidden
placeholder; 2 thumbnails; no login); www.nationaalarchief.nl 2 (item pages 804, 806); service.archief.nl 13 (IIIF at 900 px:
804 scans 150-153, 160, 170, 174; 806 scans 190, 205, 211-214; all HTTP 200, >= 2 s apart, one at a time); raw.githubusercontent.com
2, github.com 1 sparse clone, api.github.com 1 (Bourdeau's targets/roell1809). Subagent calls: 0.

## R10-ROELL12 (6 Oct 2026): R1469/R1470 groups vs R2131 (Van Dedem, 9 Feb 1793)

Worker R10-ROELL12 (account 2, for LANE LANE-RUN10-account-2), brief `.claude/briefs/runs/2026-10-06-account2-run10-jobs.md`,
08:19-08:25 UTC by `date -u`. Disk only, no subagent, no decoding. Status unchanged: `open`. Grade counts: H 0, C 0, S 0, M 0, I 0
(no reading). Pre-registration `r2131/PREREG.md` (pushed 7ed61121f before the run); script `r2131/overlap_test.py` (`--check` exit 0);
output `r2131/overlap_result.tsv`. Inputs are transcriptions only (rule 2): Bourdeau's parse of DECODE's R1469/R1470, and his
transcriptions of R2131 and of the 1788-89 Van Dedem family R1947, R2053, R2121, R2122 (dbourdeau/cyphersolver targets/dedem1788/tx,
MIT / CC BY 4.0, copied unchanged into `r2131/`).

**Test.** Q = R2131's 45 distinct groups after dropping the frame/indicator groups (701 ... 301, 2504). S = how many of Q occur in a
pool. Null N1 (the gate): each q jittered by a non-zero offset in +-50 (keeps R2131's magnitude profile, so S can vary), 10,000 draws.

| pool | tokens / distinct | S of 45 | N1 mean | N1 p95 / p99 | P(N1 >= S) | uniform-null mean / p99 |
|---|---|---|---|---|---|---|
| FAM (R1947+R2053+R2121+R2122), positive control | 1,600 / 833 | **23** (51%) | 11.5 | 16 / 18 | 0.0001 | 9.7 / 16 |
| R1469+R1470, target | 2,585 / 931 | **15** (33%) | 14.5 | 19 / 21 | 0.50 | 10.9 / 18 |

**Result (pre-registered branch).** The control passes: R2131 shares its code with the 1788-89 Van Dedem letters detectably at N=45
(23 vs a null p99 of 18), so the test has power at this length. R1469/R1470 sit at their jittered null's mean (15 vs 14.5, p95 19):
**R2131's code is not detectably shared by R1469/R1470 at this N, control-backed.** This agrees with Bourdeau's 1788-89 crib overlap
(30-33% vs a 28% baseline) and extends it to the 1793 text itself. Side result, for the dedem1788 family: DECODE's grouping of R2131 with
the 1788-89 letters as one codebook is supported by overlap (S, not a reading).

**What this does and does not say about the date.** It removes the one cheap positive the 1793 inference could have had (a shared code
with Van Dedem's own 9 Feb 1793 cipher); it does not establish 1809 either. If R1469 is a 1793 Van Dedem despatch, it is in a different
code from his 1788-93 code with Van de Spiegel -- possible (a States General despatch could use another table), but now unsupported by
any code evidence. Descriptive, not gated: R1469 opens with 501 (also at groups 187, 416) and has 401 at 205; R1470 has 601 at 34 and
1178; in the family these are frame/indicator groups, but 501/401/601 are also ordinary-looking values, so this is no evidence either way.
The date stays as DECODE gives it; no rename proposed.

**Not run.** A crib decode of R1469 against the inv. 804 clear copy (scans 150R-152R): no key for the 1788-93 family exists in this
folder, a sibling, or Bourdeau's targets/dedem1788 (his aligners found no consistent values), as stated in the PREREG.

**Verdict line:** `open` -- R1469/R1470 do not share R2131's (Van Dedem 1793) code at a detectable level (S 15/45 vs null mean 14.5,
p95 19; positive control 23/45 vs p99 18), so the 9 Feb 1793 dating has no code support. Cheapest next: (1) ~USD 2-3, the States General's
received copy of the 9 Feb 1793 despatch (NA 1.01.02, Levantse lias 1793) for a cipher original -- the only remaining test of the 1793
dating; (2) the DECODE photographs' own archive stamp/folio at full size (account-gated; an ASKS-side image request), which would settle
the provenance directly.

**Requests:** github.com 1 sparse clone (dbourdeau/cyphersolver, targets/dedem1788 + roell1809); api.github.com 1 (refused, scope).
No archive or DECODE request. Subagent calls: 0.
