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
