blocked
Check-solved verdict (updated RUS-CS, 8 Oct 2026): still `blocked`. This worker opened Krüger 1876 earlier (FAM-CS4333) but could not open Cuhn's *Mémoires* (1789) or the *Consilia* (1725) as text from the cloud: HathiTrust bibliographic API returned no record for either title (OCLC 236090673 empty; the *Mémoires* has no Open Library/OCLC entry), so HTRC Extracted Features had no HTID to query; Google Books API snippets show the *Mémoires* print Latin letters addressed 'Illustrissimo Domino AXELIO OXENSTIERN ... Regni Sueciae Cancellario' (ids o2ZeAAAAcAAJ, M4B-0ou3Tb0C, p. 23 of a volume), but no page carrying these leaves' dates was reached. Edition check unread; LOCAL-QUEUE L67 stays the named blocker.

# decode-4333-rusdorff-oxenstierna-1628

QUEUE row: DECODE R4333-R4337, "Riksarkivet_Rusdorff_Oxenstierna_1628-1..5", Johann Joachim von Rusdorf (Palatine envoy, The Hague/London) to Axel Oxenstierna, 1628. Created 8 Oct 2026 by worker FAM-CS4333 (LANE FAMILY, account 2). No transcription, no login, no cryptanalysis in this job. Sources and read/unread flags: sources.tsv.

## What the record pages say (read, 8 Oct 2026, 7 requests to de-crypt.org, login-free)
- Five Cipher records, all `Non-decrypted`, `Inline Plaintext: No`, `Available Documents` empty (no decipherment, transcription or gloss attached), `Access mode: Public`. Pages 4+3+3+2+3 = 15. Symbol sets: Numerical (R4333, R4336, R4337), Alphabet (R4334, R4335). Same description on all five: "Letter from Rusdorff ... (Often employed in the letters' signature as 760, 761, 3230, 853, 953) to Oxenstierna ... letters - 1628 January-December, the Hague, (in many cases annotated as unsolved cipher)". Record dates empty.
- Only 200x266 px thumbnails are served login-free (checked R4333 p.1); the leaves have not been looked at by this worker.
- Bourdeau (read in his clone, 8 Oct 2026) saw the images with a project cookie: "two- and three-digit numbers inside clear text", German/Latin, status `open`, "R4333-R4337 ... not worked ... surveyed only". Not an independent reading of the images by us.

## Prior work (prior-work-step.md, run by hand; `tools/prior_work.py` absent)
1. Own work: `git fetch` 8 Oct 2026; grep R4333|R4334|R4335|R4336|R4337|Rusdorf over *.md *.tsv *.json and ROOM.md: hits only in QUEUE.md (Gustav II Adolf 1632 row), POOLS.tsv:76 (0/5 read), research/FAMILY-POOLS-2026-10-08.md row 3, ciphers/riksarkivet-r4282-1628/NOTES.md:1385 (side lead) and ciphers/oxenstierna-gustav-adolf-1632/NOTES.md:65, QUEUE-github-held.tsv:72 (Bourdeau: not-attempted), ROOM.md 4 Oct (KEY1629-XMATCH) and 8 Oct (FAM-POOL). No earlier folder, no done marker, no live claim other than this one. Result: nothing done before.
2. Leaf and neighbours: UNCHECKED. Only 200 px thumbnails reachable without login; native images need the one browser login (not in this job). Result: unchecked.
3. Holder/portal/solvers: DECODE pages above (no documents); Riksarkivet Oxenstierna search service lists six text editions, none Rusdorf (sok.riksarkivet.se/en/Oxenstierna); Bourdeau clone HEAD 1fb3c46 and Aymeloglu clone HEAD d2800bb: no reading (see sources.tsv S7, S8). Tomokiyo/Cryptiana cache (sources/cryptiana, sources/ciphermysteries, sources/schmeh, sources/solver-diffs, sources/lasry, sources/papers, sources/articles): grep "Rusdorf" 0 files. Riksarkivet NAD catalogue note: not reached (unchecked).
4. Edition identity: Krüger 1876 (read) says the Kassel Landesbibliothek holds four Rusdorf folios; "Der 3. Band umfasst ausschliesslich die Korrespondenz Rusdorfs mit Oxenstiern, die ... die Jahre 1624 bis 1628 sich ausdehnt", unprinted in 1876; Cuhn 1789 printed "den grössten Theil" of vol. 1 (the reports to Frederick V), not vol. 3. The Munich Camerarius collection holds Bd.72 "Lettres et advis ... a. 1628" and Bd.73/74 copy-books of his Latin/French correspondence 1627-36. Droysen's *Gustaf Adolf* cites "Rusdorf mem. II. S.668 ff. (d.d. Haag VII Idus Jan. 1628)" (IA full-text snippet, droysen-gustav-adolf-v-2): a Latin Hague letter of Jan 1628 IS printed in Mémoires II, recipient not seen. Positive control for an in-book search of Mémoires: none possible (text unreachable) => unchecked.
5. After decode: not applicable, no decode.

## Web and blog check (FAM-CS4333, 8 Oct 2026)
Queries (WebSearch, standard): (1) "Rusdorff Oxenstierna 1628 cipher letters Riksarkivet deciphered" -> only Waldispühl/Kopal on Heusner von Wandersleben to Oxenstierna 1637 (dspace.ut.ee), no Rusdorf; (2) "Rusdorff "Oxenstierna" 1628 chiffre "Mémoires et négociations secrètes" lettre" -> no hit; (3) "Riksarkivet Rusdorff Oxenstiernska samlingen 1628 chiffer brev ej dechiffrerat" -> sok.riksarkivet.se/en/Oxenstierna (edition list, no Rusdorf), Heusner paper; (4) "Cipherbrain OR Cryptiana OR Cipher Mysteries Rusdorff Oxenstierna" -> no hit. Also IA full-text (be-api) "Rusdorf Oxenstiern chiffre 1628": Krüger, Droysen only; AOSB vols rikskanslerenax00akadgoog, 01styfgoog, 00styfgoog, 03akadgoog, 02akadgoog searched for Rusdorf/Rusdorff: 0 hits each (no positive control run on the Rusdorf spelling; 3 further AOSB identifiers errored and were not retried). Blog site searches by name (Cipherbrain, Cryptiana blog, Cipher Mysteries) were run only inside query (4) via WebSearch, not as site-restricted searches: no blog comment thread opened. Model-solve announcements ("Rusdorff solves Claude"): not searched. Google Books API (country=US): Rusdorf volumes listed in sources.tsv; no snippet route.

## Premise check (FAM-CS4333, 8 Oct 2026)
(a) Folder's own mentions: no folder existed; the DECODE description says "in many cases annotated as unsolved cipher" and attaches no document: found nothing deciphered. Not found.
(b) Other solvers' working files: Bourdeau `targets/riksarkivet1628/` (NOTES, profile.json, transcriptions of R4282/R4284/R4306/Bremen): none for Rusdorf; Aymeloglu: catalogue rows only. The Bremen-1631 key he rebuilt (two-digit homophones, six-column grid) describes a different correspondence. Not found.
(c) Physical neighbours and facing pages: UNREACHABLE without the login route (thumbnails only). Owed.
(d) Recipient/sender-side editions: LEAD, not closed. Rusdorf's own copy-books (Kassel MS vol. 3, Rusdorf-Oxenstiern 1624-28; Munich Camerarius Bd.72-74) hold his side of this very correspondence, probably in clear; Cuhn 1789 and the 1725 Consilia printed parts and are unread by this worker. AOSB: Riksarkivet lists no Rusdorf volume; AOSB full-text search 0 hits (limited, see above). Whether a copy-book text maps onto these leaves is unknown.
Verdict on the premise: nothing found that reads these letters, but (c) and the standard editions are unchecked, so this does not clear the item.

## Leaf check with one DECODE login (FAM-4333L, 8 Oct 2026, 17:23-17:4x UTC by date -u)
Route: `tools/decode_browser_login.js 4333 ... --guess-fullsize --delay 2000` with the other records as `--fetch-page`, one real-browser
login, logged in first time. de-crypt.org requests: 1 login + 7 RecordsView + 42 file requests = about 50, 2 s apart, no 429/challenge.
Full size WAS served for every page (no forbidden.png; camera photos 2448x3264). Originals (about 30 MB) not committed; 1600 px copies
and sha1 of the originals in images/manifest.json. The logged-in HTML pages were not committed (account name).

Prior-work check 1 (this job, 17:23 UTC): grep 4333-4337 / 4104 / 4120 / keys_decode in this folder, riksarkivet-r4282-1628 and the
last 1,500 ROOM lines: no earlier image fetch, no keys_decode folder, no live claim -- not done before. Checks 2-4: see the
FAM-CS4333 section above; check 2 is the leaf check below.

### Premise (c): the 15 leaves (one Sonnet reader per 5 pages at 1600 px; R4333 p.1 and R4334 p.2 margin also viewed by this worker)
| page | what it is | cipher | gloss / decipherment / key | date or identifier read |
|---|---|---|---|---|
| R4333 p1 | small German note on a thin sheet (show-through) | 2 lines of dotted 2-3 digit groups (110.65.47. 83.56.103.61.77.) | none: a short German note citing the groups, not a gloss (seen by this worker) | none |
| R4333 p2, p4 | photos of the volume's spine/cover | none | none | labels "OXENSTIERNA AF SÖDERMÖRE", "Bref till Rikskansleren Axel Oxenstierna", "E 701 Ser. B." |
| R4333 p3 | letter page, rotated 90 deg., ~90% cipher | dotted 1-3 digit groups (61.33. 21.30.95.12. 147. 385) | none seen (reader ~85% sure) | none |
| R4334 p1 | address leaf, two seals | none | none | "Illustri et generoso Dno Axelio Oxenstiern ... Regni Sueciae Cancellario" |
| R4334 p2 | letter body, Latin, ~25-30% cipher in letters | letter cipher: pseudo-words such as "Kmnchnh" | **YES: a left-margin list keyed a, b, c ... z, a, b ... in a second hand gives clear meanings ("a. Sueciae Regis", "k. Regis magnae Britanniae", "q. Rex noster ...", "Britanniam ad", "Rex", "milites"), keyed to letters set beside cipher phrases in the body** | "12 Marti 1624" |
| R4334 p3 | blank backing sheet | none | none | label "1624_1625" |
| R4335 p1 | letter body, Latin, letter cipher ~25-30% | "Hkktrsghr ds fdmdgyrd Cnlhmd", "Kmnchnh 20 Zoghkhr 1624" | none seen on the page | archivist "d 10 Nov. 1624" |
| R4335 p2 | continuation | letter cipher | none seen | "... 10 April Anno 1624" |
| R4335 p3 | address leaf | none | none | "... Axelio Oxenstiern ... Regni Sue[ciae] Vice Cancellario"; "Stockholm" |
| R4336 p1 | letter opening, Latin, ~35-40% cipher | comma-separated 2-digit groups (16,36,60,25,18,49,19,40,38) + 3-digit name codes with case endings (678^bus, 744^is, 746, 745, 740, 598, 734) | none seen (~90%) | -- |
| R4336 p2 | letter end, ~10% cipher | 2-digit groups; name codes 746 301 240 517 747 740 | none seen | "Dabam 526. 15/25 februarij 1625" |
| R4337 p1 | continuation, ~25-30% cipher | 2-digit groups (range seen 15-86), lone 3-digit codes 356 306 637 738 631 388 627 635 628 458 | none seen | "ultimis meis 25/15 febr. scriptis" |
| R4337 p2 | letter end + docket in a second hand | none | none | "Dabam 526. 26 Febr. veteri stylo 1625" |
| R4337 p3 | opening of another letter, ~35% cipher | 2-digit groups; name codes 238 239 670 738 740 236 428 | none seen (~85%; heavy show-through) | none on the page |

Findings (search results and design observations; nothing read, nothing graded above I):
1. **The dates on the leaves are 1624 and 1625, not 1628** (12 Mar 1624, 10 Apr 1624, 10 Nov 1624, 15/25 Feb 1625, 26 Feb 1625 o.s.).
   DECODE's "1628 January-December" fits none of the dated pages. R4333 p3 and R4337 p3 are undated. The sender is DECODE's
   attribution; no page carries a legible "Rusdorf" signature (R4336/37 close with a flourish and the place code "526").
2. **Two different systems.** R4334/R4335 (1624, London per "Kmnchnh" in a dating line) are a letter cipher that looks like a
   one-place alphabet shift (each cipher letter one before the clear: Kmnchnh -> Londini, Hkktrs... -> Illus..., Cnlhmd -> Domine;
   four words, from reader transcriptions of reduced images: design observation, grade I, NOT a reading). R4333 and R4336/R4337
   (1625) are a numeric system: 2-digit letter groups about 15-86 plus 3-digit name codes with Latin case endings.
3. **R4334 p2 carries a period decipherment apparatus**: the a-z keyed margin gives the clear sense of that page's cipher
   phrases (e.g. "a. Sueciae Regis"; under the apparent shift the body's "Rtdbhe Qdfhr" would be "Sueciae Regis"). For that
   page the cipher content is KNOWN from the leaf itself (prior-work kind "decipherment on the same leaf"): it is a key source /
   known answer, not a target. R4335's letter cipher has no gloss on its leaves.
4. **Name codes 744, 746, 747, 740 in R4336/37** are in the same 7xx range as the Swedish chancery name codes printed in AOSB
   ser. I Bd 3 footnotes for 1625-26 letters (746 = "Regi Daniae", 744, 747, 785 = "Regi Bohemiae"; IA-DESK-ALT section of
   ciphers/riksarkivet-r4282-1628/NOTES.md), and AOSB I:3 p.306 (Oxenstierna to the King, 10 Feb 1626) speaks of Rusdorf letters
   "icke öfversat aff cyphrene" and sends "cyphrerne eller nyckeln". Same-range numbers are a lead, not a match.
5. No interlinear decipherment, clear copy or key on any numeric page (R4333, R4336, R4337), by reduced-image readers only.

### Key records R4104 and R4120 (images in ciphers/riksarkivet-r4282-1628/keys_decode/)
- R4104 (Chifferklaver II:2, cover "Positiva och Resolutiva ... (a = 19, 48, 63, 96, 139, 191) (11 - 271) 1620-talet"): Swedish
  homophonic key, 4-8 scattered values per letter, letters 11-193, a Swedish military/administrative nomenclator 209-271; no 3- or
  4-digit value above 271; no correspondent named. Verso pencil "Carl X", "1670-".
- R4120 (cover "II:15 [DECODE says II:18] 1626 Camerarius och Grubbe (a = 14, 15, 16)"): Latin key, 24-letter alphabet in four bands
  of six, three CONSECUTIVE values per letter (A 14-16, B 26-28, C 38-40, D 50-52, E 62-64, F 74-76, G 17-19, T 23-25, Z 83-85),
  nulls above 85 (86, 87, 100, 120, 130 ... and letters); worked example "Deus nobiscum" = 50.62 35.80. 20.32.26.41.81.39.36.77.;
  cover-name lists "Vera nomina / Ficta" (Rex Sueciae -> Achilles/Antonius, Bethlen Gabor -> Paulus/Sigismundus, Ordines Belgici
  -> Areopagitae/Quirites, Camerarius -> Leodius/Anastasius ...) and "Vera nota / Ficta" countries (Transsylvania -> Norwegia ...).
  No numeric name codes.
- Against R4333/R4336/R4337: R4104 cannot cover them (no codes in the 700s, no 3230/853/953). R4120's letter range 14-85 with
  nulls from 86 matches the 2-digit groups seen (about 15-86) in range and is the period Camerarius key of the same years, but it
  has no 3-digit name codes, so it could at most read the letter groups. **Candidate (range only) for the letter groups of
  R4336/R4337; not a candidate for the name codes.** Not tested (no key test in this job).
- Against R4334/R4335: neither key is a letter-shift; not candidates.

## RUS-CS: cloud routes for the edition check (RUS-CS, 8 Oct 2026, 19:20-19:25 UTC by date -u)
Prior work: `tools/prior_work.py ... --item-spec ... --step-type lookup --fetch` exit 4: LEAD = this worker's own ROOM claim (not another worker's), UNCHECKED rows for tomokiyo (no folio), solver caches (no folio/R-id), editions (no prior_editions.tsv row); answered by the hand checks below. Check 1 own work: nothing done beyond FAM-CS4333/FAM-4333L in this folder (grep above). Checks 2-4: below. Check 5: no decode, n/a.

| route | query | result |
|---|---|---|
| (1a) Open Library search | rusdorf memoires negociations; title=memoires negociations secretes; author=rusdorf | *Consilia* 1725 has OCLC 236090673; no entry for the 1789 *Mémoires* |
| (1b) HathiTrust Bibliographic API (Chrome UA) | brief/oclc/236090673; brief/oclc/79767843 (Nachrichten 1762) | empty records for both; positive control brief/oclc/29081812 (Krüger 1876) returns record 100567861, htid hvd.32044014784144 => API works, the two Rusdorf titles are not found by these OCLC numbers |
| (1c) HTRC Extracted Features | not run: no HTID for either title | unchecked (not a negative) |
| (2) Google Books API, key + country=US, filter=full | volume metadata for 4LxfAAAAcAAJ HaRJAAAAcAAJ kmZeAAAAcAAJ 35xJAAAAcAAJ o2ZeAAAAcAAJ sC5XAAAAcAAJ | all ALL_PAGES, 725-838 pp.; M4B-0ou3Tb0C is a further *Mémoires* copy (816 pp.) |
| (2) same, `"Oxenstiern" "Rusdorf"` | snippet in o2ZeAAAAcAAJ and M4B-0ou3Tb0C | "Illustrissimo Domino AXELIO OXENSTIERN ... Regni Sueciae Cancellario SALUTEM OFFICIOSAM" at printed p. 23 of a volume: the *Mémoires* DO print Rusdorf's Latin letters to Oxenstierna, dates not seen |
| (2) same, date queries (Idus Martii; Aprilis 1624; Novembris 1624; Februarii 1625 + Rusdorf; Hagae 1625; Londini 1624; Martii 1624) | none of 7 returns a snippet from the Rusdorf volumes | no hit; the snippet route does not search inside a volume, so this is not a negative. Positive control (a known letter by date) not available => unchecked |
| (2) leads seen, not read | `"Oxenstiern" "Novembris 1624"` -> dJ4AAAAAYAAJ (Bidrag till kännedom av Finlands natur och folk): a list "Epistolae Ludovici Camerarii ad Axelium Oxenstierna ... Novembris 1624 ... Dec. 1626", Camerarius not Rusdorf; `"Oxenstiern" "Februarii 1625" Rusdorf` -> HBEPCaK4NZEC (Deputy Keeper of the Public Records, annual report): calendar line with "Rusdorff ... 11 August 1625"; also 'Rusdorff an Oxenstierna, 15. März 1625' in Droysen's Geschichte der preussischen Politik III (ScU5AQAAMAAJ), citing Mém. I p.450ff | each a lead for the print check (the Droysen cite is a different date from the leaves' 15/25 Feb 1625) |
| (3) Riksarkivet NAD (sok.riksarkivet.se) | two search URLs, 2 requests | both 302 to /captcha: unreachable from the cloud; note for "E 701 Ser. B." not reached |
| (4) AOSB ser. I Bd 3 (IA rikskanslerenax00akadgoog, djvu text, one fetch after one 500 error and one retry, saved only in scratchpad) | all 3-digit numbers 7xx near a cipher footnote; "Rusdorf" occurrences | table below; "Rusdorf" appears twice in the OCR (p.306 the 10 Feb 1626 letter, and the index entry: Rusdorf pp. 32, 44, 75, 76, 214, 215, 306, 307, 313, 314, 319) |

AOSB I:3 printed name codes (OCR, ±1 page, verify on the page image) against the 7xx codes seen on R4336/R4337 (reduced-image reader transcription, grade I): 746 = "Regi Daniae" (R4336 p1, p2); 785 = "Regi Bohemiae" (not seen on R4333-37); 744 and 747 appear as footnote codes without a gloss in the OCR (R4336: 744, 747 present); 745, 740, 734, 678, 598, 301, 240, 517, 356, 306, 637, 738, 631, 388, 627, 635, 628, 458, 238, 239, 670, 236, 428 have no printed counterpart found in I:3. Overlap is on 746, 744, 747 only. A table, no decoding and no mapping claimed: in-range numbers are a lead, not a match, and 1625 Swedish chancery codes need not be Rusdorf's. Note also that the index lists Rusdorf as 'Kur-Pfalzisk resident och svensk korrespondent i England' and the Oxenstierna letter of 10 Feb 1626 says his letters were not deciphered at the chancery ("icke öfversat aff cyphrene").

Request counts (this worker): openlibrary.org 5, catalog.hathitrust.org 3, www.googleapis.com 20, sok.riksarkivet.se 2 (captcha, stopped), archive.org 2 (one 500, one retry 200). Cost not read by this worker (orchestrator's get_session).

What this changes: the *Mémoires* print at least some Rusdorf Latin letters to Oxenstierna, so the printed-edition check (L67) is a live, specific need and prior-work check 4 stays UNCHECKED, not clear. The cloud routes tried cannot read the pages. No reading, no novelty class.

## While waiting
The one action that depends on nobody: open the Mémoires (Cuhn 1789, vols 1-2) and the 1725 Consilia in Google Books full view in a page-viewing environment (any browser; or HathiTrust full text via the owner's desk runner) and search "Oxenstiern", "Oxenstierna", "1628" and the signature numbers 760/761/3230/853/953; then one browser login (`tools/decode_browser_login.js`, `--guess-fullsize`, ~$1) to view the 15 native leaves for premise (c). Neither is a purchase or a person's reply.

## Remaining gaps (FAM-4333L, 8 Oct 2026)
Read so far: 0 of 15 pages read by us (unmeasured token count: no transcription yet); R4334 p2's cipher phrases are glossed on the leaf itself
- Mémoires 1789 / Consilia 1725 letters to Oxenstierna of 1624, 1625, 1628 - blocker: waiting-on LOCAL-QUEUE L67 (owner's runner, Google Books page view); no cloud text route (FAM-CS4333)
- R4336 + R4337 numeric letters (5 pages) - blocker: not-attempted; no transcription; next: two blind Sonnet passes on line crops + reconcile, ~$6
- R4120 key on R4336/R4337 letter groups - blocker: not-attempted; range match only (14-85, nulls 86+); next: after transcription, PREREG then decode vs 200 within-class permuted keys and a matched synthetic control, ~$2
- 7xx name codes in R4336/R4337 - blocker: not-attempted; tabulated against I:3 by RUS-CS (8 Oct 2026, overlap 746, 744, 747 only), further use needs the R4336/R4337 transcription; next: two blind passes on line crops + reconcile, ~$6
- R4334/R4335 letter cipher (1624) - blocker: not-attempted; apparent one-place shift, period gloss on R4334 p2; next: prior-work check 4 on Mémoires vol. I (L67) then a shift decode with --check, ~$1.5
- R4333 p1+p3 numeric pages - blocker: not-attempted; undated; next: transcribe with R4336/37, ~$2
- Riksarkivet NAD note for volume "E 701 Ser. B." - blocker: waiting-on LOCAL-QUEUE L67 (owner's runner); sok.riksarkivet.se 302s to a captcha from the cloud (RUS-CS 8 Oct 2026); next: add the NAD lookup to the L67 runner request, ~$0.3
- Kassel MS vol. 3 / Munich Camerarius Bd.72-74 copy-books - blocker: not-attempted; digitisation status unknown; next: Kassel/BSB catalogue lookup, ~$0.5

## Escalation (FAM-4333L, 8 Oct 2026)
- [ ] siblings: the Oxenstiernska samlingen volume's other leaves (DECODE shows only 15 pages); NAD lookup first
- [x] clear-pages: all 15 leaves viewed at full size served, address leaves and dating lines read (FAM-4333L)
- [ ] known-keys: R4120 (Camerarius-Grubbe 1626) range-matches the numeric letter groups; test after transcription
- [ ] print: Mémoires/Consilia unread, waiting on L67 (HathiTrust API no record, EF no HTID, Google Books snippets do not search in-volume; RUS-CS 8 Oct 2026); AOSB I:3 footnote codes tabulated
- [ ] key-rebuild: R4334 p2 margin gloss (a-z keyed) is a period key source for the 1624 letter cipher
- [x] image-check: full-size images served and viewed by reduced-copy readers (premise c), FAM-4333L
- [n/a] retry: nothing has been attempted yet to retry
Update FAM-4333L (8 Oct 2026): the leaves date 1624-1625, carry two cipher systems, and one page (R4334 p2) carries its own period gloss; the numeric letters R4336/R4337 have a range-matched period key candidate (R4120). The DECODE "1628" label is not supported by any dated page; the folder name is kept so links stay valid. Status stays blocked until L67 settles the edition check (intake gate).
Update RUS-CS (8 Oct 2026): edition check still unread; cloud routes exhausted (HathiTrust no record, NAD captcha, snippets only). Leads to read on L67: Mémoires p. 23 ff. Latin letters to Oxenstierna, Droysen's cite of Mém. I p.450ff.
Verdict: keep going: 6 internal gaps; cheapest next: L67 owner-runner page view of the Mémoires, ~$0 cloud
