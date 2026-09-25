open
Standard edition read by this worker: Birch, *A Collection of the State Papers of John Thurloe* (1742), vol. 2,
pp.685-686, 690-691, 704, 721-722, read from page images (archive.org `collectionofstat02thur`, leaves 693-694,
698-699, 712, 729-730; `images/manifest.json`); British History Online's edition of the same volume,
`thurloe-papers/vol2/pp718-733`, read in full (pp.718-733); Aumale, *Histoire des princes de Conde pendant les
16e et 17e siecles*, vol. 6 (`histoiredesprince06aumauoft`), "Mission de Barriere a Londres, 1652-1656" appendix
table of contents (djvu lines 29807-29819, corresponding to the book's own pp.684-698) read in full, plus a
full-text search of the whole volume for "Barriere", "novembre 1654" and "20 novembre"; *Calendar of State
Papers, Domestic: Interregnum, 1654* (`sim_great-britain-public-record-papers-domestic-commonwealth_1654`),
full-text search for "Barriere"; DECODE's cached catalogue crawl (`sources/decode/records-{non-,}decrypted-
2026-09-24.tsv`) plus two direct `RecordsView` fetches (R8395, R8398); github.com/dbourdeau/cyphersolver and
github.com/aaymeloglu/unsolved-ciphers, shallow-cloned 25 Sept 2026 and grepped for "barriere"/"conde". Web
search run for the letter's date, correspondents and phrases. cryptiana.web.fc2.com not reached directly (one
guessed URL 302-redirected, not retried per the one-attempt rule); Bourdeau's cached `unsolved.htm`, which
check-solved.md's "community lists" source family covers and which mirrors Tomokiyo's Cryptiana list, was read
in full instead and stands in for it. CLAUDE.md rule 10: nothing here is called new, unpublished, unread, first
or never printed -- a verifier classifies novelty.

## Target and brief

TX-BARR (Sonnet, session_01BwhnMpSZfURGUcS7KyemZz), parent LANE TX orchestrator (session_01UDxtM9Xv2dnPfoo5z9T6wA).
Brief: sibling inventory (no decoding) plus check-solved for **Barriere to the prince of Conde, Londres, 20
Novembre 1654 [N.S.]**, Birch vol. 2 pp.721-722 (`Vol. xx. p.107` in Birch's own margin citation to the
manuscript source), found by LANE TX worker TX-THUR (25 Sept 2026, NOTES.md `ciphers/thurloe-printed` s.22, the
"Wright" cluster) as a heading `scan_headings.py` had misattributed to Sir Benjamin Wright's letter. Henri de
Taillefer, sieur de Barriere, was the prince of Conde's agent in London, ca. 1652-1656 (confirmed below by CSP
Domestic 1654 and Aumale vol. 6's "Mission de Barriere a Londres" appendix title); not independently verified
against a biographical source beyond that.

## 1. Sibling inventory -- the five djvu-flagged headings

All five headings TX-THUR flagged (djvu 57111, 57493, 58692, 58702, 60082 of `collectionofstat02thur`) are
letters between Barriere, the prince of Conde and president Viole, printed together in this stretch of vol. 2.
Page images fetched for all five (see `images/manifest.json`). **Only one of the five carries cipher content.**

| Heading (djvu line) | Direction | Date | Printed page | Cipher? | Gloss/decipherment |
|---|---|---|---|---|---|
| 57111 | Barriere -> Conde | London, 30 Oct 1654 N.S. | p.685 | **No.** Plain English translation throughout, confirmed against the image (leaf 693). | n/a |
| 57493 | Conde -> Barriere | Camp at Hanmont, 1 Nov 1654 N.S. | p.690 | **No.** Plain English translation, confirmed against the image (leaf 698). Mentions in clear: "I have sent you another cypher according to your desire" -- confirms a key exchange around this date, not itself ciphertext. | n/a |
| 58692 | Conde -> Barriere | Camp at St. Gery, 12 Nov 1654 N.S. | p.704 | **No.** Plain English translation, confirmed against the image (leaf 712). | n/a |
| 58702 | President Viole -> Barriere | (undated, follows 58692) | p.704 | **No.** Plain English translation, confirmed against the image (leaf 712). | n/a |
| **60082 (TARGET)** | **Barriere -> Conde** | **London, 20 Nov 1654 N.S.** | **pp.721-722** | **Yes.** ~320 raw numeral tokens (regex count over the djvu range, confirmed unchanged from TX-THUR's count), embedded inline in continuous French prose (not on a separate interlinear line) -- a nomenclature-style code for names/terms within an otherwise plain-French letter, not a full substitution of the whole text. | **Partial**, and denser than the OCR-only pass (s.22) could tell (rule 2, image over transcription; see s.2 below). |

Four of the five siblings are English *translations* printed by Birch with no cipher at all -- they are not
"glossed siblings" in the sense CLAUDE.md's Lessons file means (a contemporary decipherment printed beside its
own ciphertext); they simply never carried a cipher to begin with, most likely because Condé's own outgoing
letters (57493, 58692, "resolved" replies) and Barriere's short covering letters needed no cipher for their
routine content, while the 20 Nov letter's discussion of the parlement/protector rift and Spain's negotiating
posture did. **Key-source count: 0 cipher-group/plaintext pairs available from these four** (there is nothing to
pair -- no ciphertext).

## 2. The target letter (60082): a genuine partial interlinear gloss, missed by the OCR-only pass

TX-THUR's OCR-only pass (s.22) found only "a handful of short annotation fragments" that did not "cleanly
1:1-align word-for-number" and concluded "mostly unglossed". Reading the actual page images (`leaf0729.jpg`,
`leaf0730.jpg`) shows this understated it: Birch's print carries a real, if sparse, layer of small-italic
interlinear gloss words printed *below* selected numeral runs throughout both pages -- not one gloss word per
number (unlike the Blake/Montagu/Lockhart convention documented in `ciphers/thurloe-printed` s.9/s.11/s.18/s.22
Lockhart), but short phrase-level glosses under some runs and nothing at all under most of them. Examples visible
on the image (eye-read, not a script -- see caveat below): under `30 47 20 52 68 72 75 22 28 93 86 56 52 ll 10 68
36 88`, "si toutes chofes fe changent fort / d'eftably pour le gouvernement:"; under `9 59 63 12 90 41 73 c 14 x
93 a 31`, "fu c fe fi e"; under `61 8 88 18 75 89 59 22 27 14 a`, "parlements"; under `86 69 36 m`, "feurement la
partie de l'armee / feparee de"; under `80 29 58 70 21`, "changer de fe nt. le"; under the line ending `...prize
may z car on la pr j lon ge du`. The end of the letter (top of p.722) has two more: "Il le le" and "a V.S. qu'il
le". None of this is a rule-7 reading -- it is eye-read from the image for inventory purposes only, per the
brief's "no decoding" scope, and is not aligned number-by-number; a real transcription-and-alignment pass (the
method `ciphers/thurloe-printed` s.18 used for P9/P10/P14, `tools/interlinear_align.py`) would be needed before
any of it could be graded or counted precisely. **Rough estimate only:** on the order of 20-25 short gloss
fragments (1-6 words each) are visible across the two pages against ~320 raw numeral tokens -- well under a
tenth of the letter's numerals have any visible gloss. This is **partial**, not "mostly unglossed" and not "full"
either; it sits between the two.

## 3. Further Barriere/Conde headings, 1652-1658 (grep across all seven volumes)

Grepped "Barriere" across all seven Birch/Thurloe volumes for further headings with numerals. Vols 2, 3, 5, 7
were already cached (`sources/ia-fulltext/thurloe-gz/`, no fetch needed); vols 1 and 4 were fetched fresh from
archive.org this pass (one IA fetch each, per the brief); **vol. 6 could not be fetched** -- `archive.org/
download/collectionofstat06thur/collectionofstat06thur_djvu.txt` returned HTTP 500 twice (one retry after a
pause, per the good-citizen rule, then stopped); flagged in ROOM.md, not retried further. Vol. 7 has zero
"Barriere" hits (consistent with the correspondence ending by early 1657, see below).

The correspondence is far larger than the five-letter cluster named in the brief: **45+ headings** across vols.
1 (1652-53), 2 (1654), 3 (1655), 4 (1655-56) and 5 (1656-57) involve Barriere, Conde, president Viole, or
Conde's secretary Caillet. A numeral-density heuristic (numerals per 50-60 lines after each heading, then a
finer 2-line-window >=3-numeral check to catch small fragments) was run over every heading found, rather than
reading each by hand (rule 2's image-over-transcription caveat therefore does not apply to the ones reported as
"no cipher" below -- that finding is OCR-only and conditional). Confirmed genuine embedded-cipher fragments,
beyond the target:

| Letter | Date | Vol./line | Fragment (as OCR'd) | Tokens | Gloss? |
|---|---|---|---|---|---|
| The prince of Conde to Barriere | 3 June 1655 | vol.3 L39346 | "what you have faid to 70. 29. 16. 9. 34." | 5 | none |
| President Viole to Barriere | 11 July 1655 | vol.3 L50474 | "4.y de g6 a confeille 4.S de fe retirer, 6f luy a bailie...que 48 luy vouloit faire un infult...Ce que vous me mandez de [9]8...41 part dimanche" | ~9 (French, embedded like the target but far shorter) | none |
| The prince of Conde to Barriere | 23 July 1655 | vol.3 L53551 | "upon the fubject of 64. 88. 55. 70. 42. 69. 92. p. 32." | ~7 | none |
| Barriere to Stouppe | 27 Jan 1657 | vol.5 L65668 | "33 57 66 30 13 82 and 93 98 34 85 17 11 43 70 t% 7 35 45 31 65 33 23." | ~23 | none |

All four are small isolated fragments (5-23 tokens) of names/terms coded within otherwise-plain prose, the same
design as the target letter but far shorter -- none carries a gloss, none was read against an image (OCR text
only, unflagged as a fetch target by the brief). Vol. 1 and vol. 4 headings were scanned the same way (numeral
density only) and **none cleared the threshold that vol.3's four fragments did** -- their windows show only
ordinary background numerals (dates, "Vol. xx. p. NNN" margin citations, occasional troop/money counts, all
individually checked where the count was 4+ in a single line and found to be false positives, e.g. "100 foote
companys, and 30 horfe" at vol.3 L44275). This is a screening result, not a certified negative for those ~40
headings; a target that wants full coverage should still eye-check each one against its image (rule 2). No key
file in this project's `ciphers/thurloe-printed` folder covers the Barriere/Conde/Viole/Caillet nomenclature
(distinct correspondence from Blake/Montagu/Stamford/Fauconberg/Butler, confirmed by TX-THUR s.22).

**Barriere's mission ends by early 1657**: the last dated Barriere item found in any volume is the 27 Jan 1657
Stouppe letter (vol.5); vol.7 (1658-1660) has no "Barriere" hits at all. This matches CSP Domestic 1654's own
framing of Barriere as "agent for the Prince of Conde" through the Cromwellian Protectorate's dealings with
Spain, which ended when England and France allied against Spain (1657 treaty); not independently verified beyond
what the volumes themselves show.

## 4. Check-solved verdict for the target letter (20 Nov 1654)

**open.** No prior decipherment, transcription-with-key, or identification of this specific letter (by date,
correspondents and shelfmark) was found in any of the sources read.

- **British History Online**, the standard modern online edition of this exact printed text
  (`thurloe-papers/vol2/pp718-733`, read in full): reproduces Birch's cipher numerals as best its own OCR/
  transcription could (with a few runs it could not resolve replaced by an editorial note, `[Paragraph contains
  cyphered content - see page images 721 and 722]`) -- **no decipherment**, same undeciphered state as the
  original print.
- **Aumale, *Histoire des princes de Conde*, vol. 6**: has a dedicated documentary appendix, "Mission de
  Barriere a Londres, 1652-1656" (book pp.684-698), printing several Barriere<->Conde letters in full --
  "Barriere au prince de Conde (15 avril 1652, 14 mars, 28 mai 1653)", "Trancars au prince de Conde (23 mai
  1653)", "Le prince de Conde a Cromwell (11 juin 1653)", "Barriere au prince de Conde (s.d., 1653)", "Barriere a
  Lenet (16 janvier 1654)", "Barriere au prince de Conde (17 avril, 1 et 26 juin 1654)", "Barriere au president
  Viole (4 septembre 1654)", then the appendix moves on to Conde-Fiesque correspondence dated Nov 1655 onward.
  **The 20 November 1654 letter is not among them** -- the appendix's own table of contents was read in full and
  its last Barriere item (4 Sept 1654) predates the target by over two months, with nothing from Nov 1654 at
  all. A full-text search of the whole volume for "novembre 1654" and "20 novembre" found neither phrase
  attached to Barriere. This is a real, edition-specific negative, not a blind absence.
- ***Calendar of State Papers, Domestic: Interregnum, 1654*** (the calendar of English Council/Domestic papers,
  a different series and archive from the Thurloe/Rawlinson collection Birch printed from): full-text search for
  "Barriere" finds exactly one entry, indexed "Barriere, M. de, petition of, 71" -- a 7 April 1654 petition to
  Council, unrelated to the Conde correspondence or any cipher. The target letter, an intercepted private
  dispatch kept among Thurloe's own papers, was never calendared here; expected, since CSP Domestic calendars a
  different physical archive (TNA) than the Thurloe/Rawlinson papers Birch printed from.
- **DECODE (de-crypt.org)**: no record for Birch's printed text (DECODE catalogues manuscript originals/images,
  not printed editions, so this is expected). A related but **distinct** manuscript source exists in DECODE's
  catalogue: British Library **Add MS 4200** ("1645-1661", English/French), a run of Cipher records (IDs 8394,
  8396-8397, 8399-8404 Partially decrypted; 8387 Decrypted; **8395 and 8398 both Status: N/A, Cipher Type:
  Unknown**, checked by direct `RecordsView` fetch since the cached catalogue crawl's non-decrypted/decrypted
  filter does not cover the N/A status). This is almost certainly the *manuscript* run of Barriere<->Conde
  ciphers (see next bullet), separate from the TNA/Rawlinson original Birch's edition was set from -- the two
  should not be conflated as the same physical letter without checking a shelfmark concordance, which this pass
  did not do.
- **Solver repositories**: `github.com/dbourdeau/cyphersolver`'s `unsolved.htm` (Tomokiyo's list, mirrored)
  names a **different** Conde-Barriere letter as undeciphered: *"A letter from the Prince of Conde to Barriere,
  his agent in London, (15 September 1654 NS; Add MS 4200, f.98; DECODE R8395) seems to be undeciphered. A
  cipher used in 1655 is known but a different cipher may have been used in 1654. See another article. (Also, it
  is not clear whether the short ciphertext in f.101 (DECODE R8398) can be read with the known cipher. There is
  some chance it is in yet another cipher.)"* -- quoted verbatim per check-solved.md's rule. This is the same
  correspondence family (Conde-Barriere, same year) but **a different letter, direction and date** (15 Sept vs.
  our 20 Nov; Conde->Barriere vs. our Barriere->Conde; BL manuscript vs. Birch's printed text) -- not our target,
  but directly relevant context: it establishes that a 1655 Conde-Barriere cipher key is known to Bourdeau/
  Tomokiyo, that a *different* cipher may be in use in 1654 letters specifically, and that the correspondence's
  manuscript originals (not just Birch's print) are independently catalogued and partly unresolved. No mention
  of the 20 Nov 1654 letter, Birch's edition, or any of the small vol.3/vol.5 fragments found in s.3 above, in
  either solver repository. `aaymeloglu/unsolved-ciphers` has no Barriere hits at all.
- **Web search**: no announcement, blog post, or model-solve claim found for this letter.
- **Cryptiana**: not reached directly this pass (see header caveat); Bourdeau's cached mirror of Tomokiyo's list
  covers the same ground as the solver-repository bullet above.

## 5. What this means for a future campaign (not this job's scope)

The target letter is a genuine open cryptanalytic/recovery candidate: ~320 numeral tokens, small partial gloss
(section 2) giving some crib material, embedded-nomenclature design (code words within otherwise-plain French,
not a full substitution -- rule 3 will need a matched control of the *same design*, not a simple-substitution
control at the same raw length, per CLAUDE.md's Salviati lesson). Two live leads worth a future worker's first
look, neither pursued here (brief: no decoding):
1. The solver-repo note that "a cipher used in 1655 is known" for this same correspondence -- if that 1655 key
   (likely built from one of the small vol.3 fragments in s.3, or from DECODE's Add MS 4200 series) can be
   found and it is a nomenclature (code-number -> word) table rather than a letter-substitution cipher, it is
   the first thing to cross-match against the target's ~320 tokens, per the project's `tools/key_crossmatch.py`.
2. DECODE's Add MS 4200 records 8395/8398 (both N/A/Unknown) and the surrounding 8394-8404 run are the
   manuscript side of this same correspondence and have not been opened by this pass (would need
   DECODE_USER/DECODE_PASS per the access playbook, one login per session) -- they may hold the period's own
   cipher table or a further partial decipherment not visible from Birch's print alone.

## 6. Access notes

Route used for all seven page images: `archive.org/metadata/<id>` (no `access-restricted-item` flag) ->
`<id>_page_numbers.json` (exact leaf<->printed-page map) -> `iiif.archive.org/iiif/<id>$<leaf>/full/full/0/
default.jpg` (302-redirect to the jp2-backed host, `curl -L` follows it) -- confirmed working from the cloud, no
login, same method as `ciphers/thurloe-printed` NOTES.md s.18. Folder size 12 MB, under the 30 MB cap.

Requests this session: archive.org (metadata + page_numbers.json + djvu.txt fetches for vols 1/4/6 + advancedsearch
queries) ~10; iiif.archive.org (7 leaf images) 7; be-api.us.archive.org (full-text search: Aumale vol.6 x3, CSP
Domestic 1654 x1) 4; www.british-history.ac.uk (toc + one content page) 2, plus one 302-redirected search attempt
(not retried, host's search endpoint is bot-challenged -- direct page fetches work fine); de-crypt.org
(RecordsView x2) 2; github.com (2 shallow clones). All >=1.5s apart, one at a time, descriptive User-Agent, no
403/429 anywhere except the BHO search redirect (not a rate limit, a bot-challenge on that one endpoint).

## 7. Files

`images/` (7 jpg + manifest.json, 12 MB), this NOTES.md. No `ciphertext.txt`, no key, no decode script -- this
job did not decode (brief scope). A future solver should start `ciphertext.txt` from the image transcription in
section 2 (not yet done as a formal line-by-line pass) rather than from the djvu OCR, per rule 2.
