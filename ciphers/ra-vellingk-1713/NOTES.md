# Mauritz Vellingk reports partly in cipher, Hamburg exile, 1713-1714

**Status: blocked**
Handlingar rörande Skandinaviens historia vol. 8 (Stockholm 1820, IA `handlingarrrand01swegoog`) read by this worker (GF4-BATCH19, 3 Oct 2026) by full-text grep of the djvu OCR: it prints Erik Sparre's drafts of letters to Vellingk father and son, Paris, 20 May 1713 - 1715, marked 'partie en chiffre', with the editor's note that Vellingk's own letters answered by them are printed in vol. 6 (1818), register 6:223 ff.; vol. 6 is full view on books.google.com (6d1AAAAAcAAJ, owgPAAAAYAAJ) and on HathiTrust (wu.89107728503, nyp.33433066618947; R8-VELL, 6 Oct 2026), neither of which serves page text to the cloud, and is on no IA item, so the sender-side print stays to be read from a desk browser. Both Riksarkivet holdings are undigitised (copy order, REQUEST.md).

## Item

Mauritz Vellingk (1651-1727, former Swedish governor-general of Bremen-Verden, general and privy councillor),
reports sent partly in cipher from Hamburg after the Danish conquest of Bremen-Verden (occupied from late
1712), plus his own collected copies referencing the 1713 neutrality treaty. Two related holdings, same
repository:
1. SE/RA/1411/E/E VI/1 (Kanslikollegium, "Inkomna handlingar / Skrivelser i utrikesärenden samt ansökningar
   till diplomat- och konsulstjänster"), catalogue note: "Från M. Vellingk, förutvarande generalguvernör i
   Bremen-Verden, som efter dessa provinsers erövring av danskarna vistades i Hamburg utan egentligt uppdrag men
   sände rapporter, delvis i chiffer." (from M. Vellingk, former governor-general of Bremen-Verden, who after
   the provinces' conquest by the Danes stayed in Hamburg without formal assignment but sent reports, partly in
   cipher).
2. SE/RA/720626/E/E 6015 (Mauritz Vellingks samling, "Avskrifter"), catalogue note: "Avskrifter. Chiffer.
   Handlingar angående neutralitetstraktaten 1713." (copies. Cipher. Documents concerning the 1713 neutrality
   treaty).
Riksarkivet i Stockholm/Täby. Found by the LANE S scout of 24 September 2026, QUEUE.md row R7, kind:
cryptanalysis (no key is catalogued alongside either holding).

No transcription or image exists in this repository; `ciphertext.txt` is not created (rule 2).

## Check-solved sweep, 24 September 2026

Run directly by this worker, per `.claude/briefs/check-solved.md`'s six sources. 6/6 checked, 0/6 found a
solution, key transcription, or documented prior attempt.

**Editions first:** the relevant documentary-edition candidates named in the row (Sveriges traktater med
främmande magter, and Karl XII's letters, ed. Ernst Carlson) were checked for digitisation:
`archive.org/advancedsearch.php?q=title%3A(Sveriges+traktater)` returns 0 hits, and a plain-text search for
`Vellingk` across all of Internet Archive full text (`archive.org/advancedsearch.php?q=Vellingk`) also returns
0 hits — neither series, nor any other IA-held volume, is reachable there. Not checked on HathiTrust this pass
(no HTRC Extracted Features run for "Vellingk" — should be the next step given both editions are far more
likely to be a HathiTrust-only German/Swedish scholarly series than an Internet Archive Google-scan). The
German Wikipedia article on Vellingk (`de.wikipedia.org/wiki/Mauritz_Vellingk`, fetched directly) covers his
1712-1714 Hamburg period and the 1713 burning of Altona in detail but cites no edition of his Hamburg reports
or any cipher, and mentions no decipherment.

**Web:** WebSearch "Mauritz Vellingk Hamburg 1713 chiffer rapport Bremen Verden" — results (Wikipedia,
Bremen-Verden campaign pages, a Niedersachsen Arcinsys archival finding-aid entry, a Rigsarkivet Bremen-Verden
register) confirm the historical context (Vellingk in Hamburg from Sept 1712, the Altona affair) but no mention
of a cipher report or any decipherment.

**Community lists:** `sources/cryptiana/` grepped for "vellingk" — no hits.

**DECODE:** not logged separately — same session, same negative result as R1-R3 (no login attempted per this
brief; de-crypt.org not indexed by the web search engine for this name).

**Bourdeau:** same shallow clone. `grep -rli "vellingk"` across the whole tree — no matches at all.

**Aymeloglu:** same shallow clone, same grep — no matches.

**Riksarkivet digitisation check:** queried `text=chiffer Vellingk&type=Record` (1 retried transient
`SSL_ERROR_SYSCALL`, 200 on the retry after a ~5s pause). 2 hits, matching both of this row's shelfmarks.
SE/RA/720626/E/E 6015: `onlyDigitisedMaterials: false`. SE/RA/1411/E/E VI/1: `onlyDigitisedMaterials: false`.
**Neither is digitised.** No IIIF manifest or image link for either.

**Verdict:** open. No prior solution, key transcription, or attempt found anywhere searched. This is the one
cryptanalysis-kind row of the four in this batch — no key is catalogued with either holding, so even after a
copy is obtained, this would need either the key found elsewhere (a Kanslikollegium chiffernyckel volume from
the same 1712-1714 window) or a genuine ciphertext-only attack with a matched control (rule 3), not a
straightforward key application.

**Not digitised — copy order needed.** See REQUEST.md.

## Request log

24 Sept 2026: no personal data logged here.

queued JSTOR rows, 26 Sept 2026, QUEUE-FILL.

## JSTOR runner, 26 Sept 2026

- `"Mauritz Vellingk" AND Hamburg AND 1713 AND chiffer`: no relevant hit (0 results, none about the letter).
- `"Bremen-Verden" AND "neutralitetstraktaten 1713"`: no relevant hit (0 results, none about the letter).

## While waiting (27 Sept 2026, WAIT-PASS-B)

Waits on: Riksarkivet copies of `SE/RA/1411/E/E VI/1` and `SE/RA/720626/E/E 6015` (REQUEST.md, since 24 Sept
2026).

- M: run tools/htrc_ef_headwords.py for 'Vellingk' against Sveriges traktater/Carlson's Karl XII letters -- this file's own named next step, not run (HathiTrust's own site is Cloudflare-blocked, but the separate HTRC Extracted Features API works from the cloud).
- S: search Riksarkivet's Sök-API for a surviving Kanslikollegium cipher-key volume, 1712-1714, by date/type rather than by correspondent name.
- S: check Litteraturbanken.se or a Swedish national library digitised edition of Carlson's Karl XII brev, not tried on this host this pass.

## Edition citation (GF4-BATCH19, 3 Oct 2026)

IA full-text search (`be-api.us.archive.org/fts/v1/search?q=Vellingk chiffre`, 87 items) led to *Handlingar rörande
Skandinaviens historia* (HRSH), the Swedish documentary series of Karl XII's reign. **Vol. 8 (1820)**, IA
`handlingarrrand01swegoog`, `_djvu.txt` fetched once and grepped: section "Utkast till bref af ... Grefve Erik Sparre
(hvaraf de flesta äro till Herrar Wellingk, Far och Son), med tillhörande handlingar", printed from Sparre's minutes
(Stierneld collection), from 20 May 1713 into 1715. The letters to "M:r le C:te Welling" from Paris (12 Jun, 16 Jun,
26 Jun 1713 ...) carry headings "Chiffre" / "partie en chiffre", and the editor notes: "De i originalet understrukne
ord äro förmodligen sedermera skrifne i Chiffer" (the words underlined in the original were probably afterwards
written in cipher). The editor adds: "H. E. Grefve Wellingks Bref, hvarpå en del af dessa Minuter äro svar, finnas i
Sjette delen af Handlingar rörande Skandinaviens Historia" -- Vellingk's own letters to Sparre, printed in **vol. 6
(1818)**; the 1865 register (Google Books FZ0EAAAAQAAJ, snippet) gives "Wellingk, 6: 223 f". Vol. 6 is full view on
Google Books (6d1AAAAAcAAJ, BSB copy), but books.google.com page and text view is captcha-blocked from the cloud
(access playbook table) and no IA item carries vol. 6 (IA title search: 15 HRSH items, vol. 6 not among them; the
1817 and both 1819 items checked by grep, not vol. 6). Not opened this pass, hence **blocked**. The series vol. 9
(1821) register entries for Vellingk (IA `handlingarrrand00swegoog`/`00scangoog`, grepped) point to the same vol. 6
letters and to 1720s Pomeranian material, out of range.
What vol. 8 shows about this item: Vellingk in Hamburg was corresponding in cipher in 1713 with the Swedish envoy in
Paris; the clear minutes of Sparre's side are printed. Whether any of these are among the "Avskrifter. Chiffer." of
E 6015 (Vellingk's own collection) is unknown until the copy arrives; E VI/1 holds his reports to the Kanslikollegium,
a different series from the letters to Sparre.

Desk-browser task (draft, not filed -- NOTES.md only per brief): open
https://books.google.com/books?id=6d1AAAAAcAAJ (HRSH vol. 6, 1818), go to p. 223 ff. ("Wellingk" in the register),
and record for each Vellingk letter: date, place, recipient, and whether the print marks cipher passages or prints
them in clear (screenshots of the first page and of any 'chiffre' note).

## Web and blog check (GF4-BATCH19, 3 Oct 2026)

Web searches (4): (1) `Mauritz Vellingk 1713 1714 Hamburg reports cipher chiffer Kanslikollegium` -- Adelsvapen,
SBL (Feif), de.wikipedia, Arcinsys NLA ST Rep. 5a Nr. 617, Riksarkivet SE/RA/6592 (his samling); nothing on a cipher
or decipherment. (2) `"Vellingk" "E VI/1" OR "E 6015" Riksarkivet chiffer` -- only Riksarkivet portal pages; nothing.
(3) `Vellingk Sparre letters 1713 1715 deciphered neutrality treaty Hamburg Görtz "Welling"` (also the descriptive
title) -- the 1717 London print *Letters which passed between Count Gyllenborg, the Barons Görtz, Sparre, and others*
(idref 239639073): the British government's printed decipherments of the 1716-17 Gyllenborg plot, a later affair
not involving these 1713-14 reports; nothing on Vellingk's cipher. (4) The model-solve query `Vellingk cipher solves
Claude GPT` folded into (1)/(3): no announcement.
Blogs, site search by name for both spellings, 3 Oct 2026: **Cipherbrain** (scienceblogs.de/klausis-krypto-kolumne
`?s=Vellingk`, `?s=Wellingk`): no results. **Cryptiana blog** (cryptiana.blogspot.com `search?q=`): "No posts
matching the query" for both; on-disk `sources/cryptiana/`: no hit. **Cipher Mysteries** (`?s=`): "Nothing Found"
for both. No hit, no comment thread to read.
Other projects' new publications: **Cabinet Noir** (github.com/el-descifrador/cabinet-noir, HEAD 47b6db9, 3 Oct
2026): no Vellingk/Welling folder or file (its Swedish item is karlgustav-1657, out of range). **Apeiron** (apeiron.re):
only known publication Koehler. Solver repos re-grepped 3 Oct 2026 (Bourdeau HEAD a439937, Aymeloglu HEAD d2800bb):
no vellingk/wellingk hit. DECODE: no record under either spelling in `sources/decode/` listings.
No decipherment or plaintext of this item located by these queries on 3 Oct 2026.

## Premise check (GF4-BATCH19, 3 Oct 2026)

(a) Folder's own mentions: no decipherment, key, gloss or clear copy named in NOTES.md or REQUEST.md. Not found.
(b) Other solvers' working files: Bourdeau and Aymeloglu grepped (above): nothing. Not found.
(c) Neighbouring material: HRSH vol. 8 prints the clear minutes of the Paris side of a 1713-15 cipher correspondence
with Vellingk (above) -- a possible crib source if E 6015's "Chiffer" copies prove to be that correspondence; HRSH
vol. 6 prints Vellingk's own letters to Sparre (not yet read). The RA holdings themselves are undigitised, so their
physical neighbours cannot be viewed. **Found: a candidate plain-text source for part of the correspondence, not a
decipherment of this item.**
(d) Recipient-side edition: the Kanslikollegium reports (E VI/1) have no known printed edition; for the Sparre letters,
HRSH vol. 8 (Sparre's side) read, vol. 6 (Vellingk's side) blocked from the cloud. Not found.

## HTRC EF headword run (R8-VELL, 6 Oct 2026)

Brief: run `tools/htrc_ef_headwords.py` for 'Vellingk' against Sveriges traktater / Carlson's Karl XII letters.
Volume ids found (HathiTrust Bibliographic API, `api/volumes/brief/recordnumber/N.json`; record numbers from the Online
Books Page title search, extended shelves):
- **HRSH** (record 008697824, OCLC 1605152, all 40 vols + register full view): **vol. 6 (1818) = `wu.89107728503`,
  `nyp.33433066618947`, `hvd.hnt6vv` (v.5-6)**; vol. 8 (1820) = `wu.89107728545`, `nyp.33433066618962`; register
  1-40 = `wu.89107728388`, `inu.30000123989836`, `nyp.33433082301353`. This corrects the 3 Oct line "vol. 6 is full view
  only on books.google.com": it is full view on HathiTrust in three copies too (HathiTrust's own reader is still
  Cloudflare-blocked from the cloud, so this changes the desk route, not the cloud one).
- **Carlson, *Konung Karl XII:s egenhändiga bref*** (1893, record 006031530): `hvd.hnndj7`, `hvd.hnnczt`,
  `inu.30000053834564`, all full view. German ed. 1894: `hvd.32044084710946` (rec. 100375180), `uc1.$b761736`
  (rec. 009959877).
- **Sveriges traktater med främmande magter**: no title hit on the Online Books Page (standard or extended shelves);
  not located on HathiTrust this pass (Open Library, the usual OCLC route, reset the connection twice: stopped).
The run itself: **not done -- the HTRC EF API answered HTTP 500** (`PrimaryUnavailableException: No primary node is
available`) for all four htids tried (vol. 6 x2, Carlson 1893, Carlson 1894) at 03:55 UTC and on the one permitted
retry at 03:56 UTC; R8-WHIT (account 4) logged the same outage ("HTRC EF down x3") at 03:49 UTC. Untested-by-this-
tool today, not a negative.
Google Books API (keyed, `country=US`), query `Wellingk chiffre Sparre`: a second full-view copy of vol. 6,
**`owgPAAAAYAAJ`** (416 pp., `ALL_PAGES`, PDF listed available), snippet: "... Wellingk, till Friherren,
Ambassadören och Generalen, sist Riks-Rådet och Fält-marskalken Gref Erik Sparre ... Chiffre. **) Detta skämt lärer
syftat på Friherre Spa[rre] ..." -- so vol. 6 prints Vellingk-to-Sparre letters with "Chiffre" headings (search
result, page not located). Three further Wellingk/Hamburg/1713-1714 queries: no items. The listed PDF download
(books.google.com) answered HTTP 429 (sorry page) on one attempt: stopped.
Requests: data.htrc.illinois.edu 6, catalog.hathitrust.org 5, onlinebooks.library.upenn.edu 4, openlibrary.org 2
(reset), www.googleapis.com 5, books.google.com 1 (429).
Next (desk or a later cloud session): rerun `python3 tools/htrc_ef_headwords.py wu.89107728503 hvd.hnndj7
--words vellingk,wellingk,welling,chiffre,chiffer --target x=1` once the EF API is back (~$0.5), which gives the
seq numbers of the Wellingk/Chiffre pages in vol. 6 for the desk read; or the desk browser opens vol. 6 directly
(HathiTrust `wu.89107728503` full text search "Wellingk", or Google Books owgPAAAAYAAJ / 6d1AAAAAcAAJ) at p. 223 ff.

## Remaining gaps (R8-VELL, 6 Oct 2026)
Read so far: unmeasured -- no ciphertext on disk; both holdings undigitised, only the clear side of the correspondence printed.
- HRSH vol. 6 (1818) pp. 223 ff., Vellingk's letters to Sparre (snippet confirms "Chiffre" headings) - blocker: not-attempted; books.google.com (6d1AAAAAcAAJ, owgPAAAAYAAJ; PDF 429) and HathiTrust (wu.89107728503) both blocked from the cloud, R8-VELL section; next: a LOCAL-QUEUE desk-browser row for the draft task above, ~$0.5
- HTRC EF page location of Wellingk/Chiffre in vol. 6 and Carlson 1893 - blocker: not-attempted; the HTRC EF API answered HTTP 500 (outage logged 6 Oct 2026 03:49 and 03:55 UTC); next: rerun the command in the R8-VELL section once the API answers, ~$0.5
- Riksarkivet copies of SE/RA/1411/E/E VI/1 and SE/RA/720626/E/E 6015 - blocker: needs-physical-access; undigitised, copy order in REQUEST.md since 24 Sept 2026

## Escalation (R8-VELL, 6 Oct 2026)
- [n/a] siblings: no ciphertext of any sibling letter is on disk or online
- [ ] clear-pages: HRSH vol. 6 Vellingk letters (clear print, possible crib) to be read from a desk browser
- [n/a] known-keys: no Swedish 1713 key located; nothing to apply without ciphertext
- [x] print: HRSH vols. 8 and 9 grepped (GF4-BATCH19); vol. 6 located in full view on HathiTrust and Google Books (R8-VELL)
- [n/a] key-rebuild: no ciphertext on disk to rebuild a key from
- [n/a] image-check: no image of either holding is available online
- [n/a] retry: no attempt has been made that could be retried
Verdict: keep going: 2 internal gaps; cheapest next: desk-browser read of HRSH vol. 6 pp. 223 ff., ~$0.5 (queued for the owner's local runner as LOCAL-QUEUE row L59, 6 Oct 2026, R9-LQROWS)

Gate re-run (GF4-BATCH19, 3 Oct 2026): `ra-vellingk-1713: blocked (line 3) -- already terminal, nothing to gate`, exit 0 (was exit 1 as an uncited open); status moved open -> blocked by this pass.

## While waiting (R9-LQROWS, 6 Oct 2026)
LOCAL-QUEUE row L59 (page read of HRSH vol. 6 pp. 223 ff., HathiTrust wu.89107728503 / Google Books owgPAAAAYAAJ) queued 6 Oct 2026.

## Next step (LANE-RUN15-account-2 orchestrator, 6 Oct 2026, 17:2x UTC; NEXT-STEPS.tsv read this folder as `runnable` from an older line)

next: the desk-browser read of HRSH vol. 6 pp. 223 ff. is queued as LOCAL-QUEUE row L59 (R9-LQROWS, 6 Oct 2026); the HathiTrust page view does not open from the cloud. Who acts: the owner's local runner. Blocker class: needs-person.
