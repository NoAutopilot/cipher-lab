open
Status corrected closed-negative -> open by the LANE ZX orchestrator, 25 Sept 2026 16:25 UTC: ZX-BAR's permutation
test ran on bare digits with the printed marks ignored, and its 0/64 follows mechanically from key_gloss.tsv's own
conflict rows (its section says so). Its matched control has no marks and a correct gloss alignment by construction, so
the test cannot tell "no transferable key" from "code+mark design" (the marks on about half the numerals may split the
9 conflicting codes, as in Salviati) or "sequential gloss alignment wrong". Not closed until a mark-typed rerun
against a control of the same code+mark design. ZX-BAR's numbers stand as measured:
Measured 25 Sept 2026 (ZX-BAR): a permutation z-test on the letter's real gloss positions gives z=-0.46 (key-shuffle
null) / z=-0.33 (token-shuffle null), both near zero and far below a matched control's z range (14.6-25.0 /
5.7-12.4 over 10 seeds) -- the gloss's own repeated code occurrences do not even predict each other above chance,
let alone the unglossed tokens; see the "ZX-BAR" section at the end of this file.
No longer provisional (25 Sept 2026, YX-BARB): the QA/YX-FIX note below flagged that section 8's matched-control
negative rested on one unreconciled pass; pass B has now landed and been reconciled against the image
(see the "YX-BARB" section at the end of this file). The negative stands on the reconciled transcription too
(30.0% target vs. control avg 31.1%, 10 seeds) -- fixing the transcription (a missing 25-token line, three other
dropped/misread tokens) did not move the result.
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

## 8. Transcription, alignment, spec and first cheap test (TX-BARRT, session_01GdGCckTNN8ftrRQRpsM17A, 25 Sept 2026)

Intake gate checked: this target's `open` verdict (top of file, section 4) names the standard edition (Birch
1742, pp.685-722) and the specific editions/pages/full-text searches actually read by TX-BARR (BHO in full,
Aumale vol.6 appendix TOC in full, CSP Domestic 1654 full-text search) -- passes .claude/briefs/check-solved.md's
bar, not `blocked`.

**Design finding.** The target letter is a **word-per-code nomenclature**, not a letter-substitution cipher.
Two spans give an exact word-count match between a fully-printed interlinear gloss phrase and the run's token
count, decoded in sequential reading order (typesetting does not column-align a gloss word under its exact
source token -- confirmed by comparing gloss-word x-position against token x-position on several short runs,
which disagree by up to several token-widths even where the word-count matches exactly):
- R004+R005 (`o 70 12 34 66 40 26 68 [circle-dot] d 61` ... `75 88 78 44 71 89 79 31`, 19 tokens split by the
  clear French "ni ayant rien"): gloss "le parlement & le protecteur eftant fort oppofé, fi quoique je ne
  doubte point que le protecteur demeure le maiftre," is exactly 19 words excluding "&" -- 19-for-19.
- R022+R023+R024 (`90 d 92 39` ... `22 44` ... `89`, 7 tokens): gloss "lequel deffein d'eux le a pourroit tira,"
  is exactly 7 words -- 7-for-7.

Beyond these two, the gloss is **sparse and partial**: of 42 runs (368 code tokens total by this pass's count,
`passA.tsv`), only 25 have any printed gloss at all, and most of those give only the first few words of a much
longer run (e.g. R006, 26 tokens, gloss gives only the first 5 confidently; R026, 12 tokens, gloss gives the
first 6). This matches TX-BARR's inventory characterisation (section 2 above) better than TX-THUR's OCR-only
"mostly unglossed" (rule 2 vindicated again).

**Conflict finding (important).** Building `key_gloss.tsv` from every confidently/tentatively glossed span and
checking for the same bare digit assigned different values at different spots (not to be confused with two
*different* digits both meaning the same common word, e.g. 34 and 71 both "protecteur" -- that is an ordinary
homophone, not a conflict): at least 9 codes conflict -- **61** (four different values across R004/R006/R014/
R015: ne, que, premier, la), **12** (le vs si), **40** (fort, chef, mil), **44** (le, pourroit, ne), **88**
(point, un, le), **90** (e, lequel, chofes), **89** (demeure, tira), **31** (maistre, traiter), and **d** (je,
de, deffein, le -- the single most conflicted code). This held even for two of the *cleanest* short exact-match
spans (R014 "premier chef" and R015 "la vie", each an unambiguous 2-for-2 sequential match). The most likely
reading, per LESSONS.md's "genuine break" table and CLAUDE.md rule 3's Salviati lesson: this is a nomenclature
that gives its handful of highest-frequency short French words (le/la/que/ne/de/se) many interchangeable
homophone slots specifically to defeat exactly this kind of frequency/crib attack, rather than each digit having
one stable meaning. Marks were visible on roughly half of all numeral tokens (circumflex, grave, acute, macron/
overline, caron, diaeresis shapes all observed) and might in principle disambiguate some of these conflicts, but
this pass could not reliably distinguish mark *type* at the resolution available (only presence, recorded as a
trailing `*` in `passA.tsv`) -- flagged as the most promising unresolved lead for a dedicated high-resolution
mark-typing pass, not resolved here.

**Files:** `passA.tsv` (this worker's transcription, run-based: run_id, tokens with mark-presence flags, gloss
text, left/right clear context, leaf, note), `key_gloss.tsv` (every gloss-derived code/value/grade-C candidate,
with an explicit `status` column: `primary` = the 30 non-conflicting codes used below, `conflict` = recorded but
not applied), `coverage_test.py` (applies the primary key to every run in `passA.tsv` and reports coverage),
`matched_control.py` (builds a control of the identical run/gloss-reveal structure over fresh, unrelated period
French from `tools/data/fr16`, with ground truth, over N seeds).

`tools/interlinear_align.py` does not fit this target (checked, per brief): it is built for the Blake/Montagu
convention (a full decipherment line printed *above* each cipher line, one djvu-OCR pair per manuscript line),
not for this letter's sparse phrase-level gloss printed *below* only some spans of inline-embedded code. Manual
position + sequential-order alignment (above) was used instead, documented run by run in `passA.tsv`.

**First cheap test (breadth rule, one test only, per spec).** Applied the 30-code non-conflicting `primary` key
to every run of the letter (not just the glossed ones) and compared against a matched control of the identical
design (CLAUDE.md rule 3: same N, same alphabet/homophone structure, same 42-run/368-token layout, same per-run
gloss-reveal counts, same conflict pattern, but built over unrelated real period French with randomly-assigned
homophone codes, so ground truth is known):

| | tokens | key size | coverage | newly-covered (beyond the gloss itself) | sense rate on the newly-covered |
|---|---|---|---|---|---|
| **target** (this letter) | 368 | 30 | 108/368 = **29.3%** | 36 | not computable (no ground truth -- that is the open question); qualitatively dominated by le/se/de/que/a/je |
| **control**, avg of 10 seeds | 368 | 42-46 | avg **33.4%** (range 28.5-37.0%) | avg 74/run-structure | avg **74.2%** (range 62.8-84.2%) |

`python3 coverage_test.py` and `python3 matched_control.py --seeds 10` reproduce these numbers (both scripts
read only `passA.tsv`/`key_gloss.tsv` and, for the control, `tools/data/fr16`; no network).

**Verdict: negative with a matched control, on `passA.tsv` alone** (confirmed no longer provisional as of 25 Sept
2026, YX-BARB: pass B reconciled against the image, missing/misread tokens fixed, and the negative re-run on the
reconciled `ciphertext.tsv` -- same result, see the "YX-BARB" section at the end of this file). The target's raw coverage (29.3%) is not distinguishable from --
and is in fact slightly *below* -- what an unrelated control of the identical design achieves purely by chance
(avg 33.4%, and the control's own sense rate on its "newly covered" tokens is a respectable 74% purely because
the reused homophone codes decode to ultra-common short words that are correct at a high prior rate anywhere in
French prose). This is exactly the failure mode CLAUDE.md rule 3's Salviati lesson warns against: a coverage
number, on its own, from a design with this much homophone/null reuse for common short words, demonstrates
nothing. Per the breadth rule (CLAUDE.md 3a), this first test did not move the spec; no campaign is proposed
from this worker, and no further test was run (one test per spec per breadth worker). The spec's
`cheap_test_done` records both numbers.

**What would be worth trying next (not this job's scope, listed for the next worker):**
1. A token-shuffle or key-shuffle permutation z-test on this *same* letter's real gloss positions (LESSONS.md
   "Controls, always"), which reuses the actual glossed spans rather than resampling a fresh control -- sharper
   than rebuilding another synthetic control.
2. A dedicated high-resolution re-crop specifically to type the marks (circumflex vs grave vs acute vs macron vs
   caron vs diaeresis) rather than just flagging presence, to test whether marks resolve the 9 digit conflicts
   found above -- this is the single most promising unresolved lead from this pass.
3. TX-BARR's section 5 leads (the solver-repositories' note of a distinct "1655 cipher" for this same
   correspondence, and DECODE's Add MS 4200 records 8395/8398, both still unopened) remain the more likely route
   to an actual key than further cryptanalysis of this one letter alone, per LESSONS.md's "almost nothing fell
   to pure cryptanalysis" table (this letter's ~320-token nomenclature-with-heavy-homophones sits squarely in
   the "large nomenclator, one letter" blocked category, not the "genuine ciphertext-only break" one).

No claim of a reading is made here (rule 7: no candidate plaintext is reported, so `judge_plaintext.py` was not
run against a candidate -- only the spec file records the cheap test's judge block for a future worker).
Grades: every `key_gloss.tsv` row is grade **C** (from the gloss, i.e. known plaintext for that span); nothing
here is graded H or S. Rule 10: nothing in this section is new, unpublished, unread, first or never printed --
a verifier classifies novelty, and none is claimed.

## YX-BARB (25 Sept 2026)

QA (25 Sept 2026, `.claude/briefs/runs/2026-09-25-lane-yx-barb.md`) flagged that TX-BARRT's negative (s.8 above)
rested on one unreconciled pass -- pass B was interrupted before landing (LEDGER.md: "Interrupted at ~2x the $6
alarm while running pass B after the deliverable was pushed"). This job ran pass B, reconciled, and re-ran the
cheap test on the reconciled transcription. Intake gate checked first: `tools/intake_gate_check.py
thurloe-barriere-1654` exits 0 (the `open` verdict at the top of this file names the standard edition and the
pages/full-text searches actually read).

**1. Pass B.** A second Sonnet subagent transcribed `images/collectionofstat02thur_leaf0729.jpg` (p.721) and
`leaf0730.jpg` (p.722) blind -- it was given only the two page images and the run/column conventions (not
passA.tsv or any other file in this folder) -- and wrote `passB.tsv`: 33 runs, 400 tokens (vs. passA.tsv's 42
runs, 368 tokens).

**2. Reconciliation.** `tools/reconcile_passes.py passA.tsv passB.tsv` run as named in the brief first, naively
(no options): **agree 33/608 = 5.4%**. Investigated before accepting that number, since the whole point of this
job is to know whether the two passes actually agree: the low figure is almost entirely a tooling-convention
mismatch, not real transcription disagreement --
  1. `reconcile_passes.py`'s own "uncertain" marker is a trailing `?`; this target's convention for "a diacritic
     mark was visible above this token" is a trailing `*` (passA.tsv) or, inconsistently in passA.tsv, `^` (see
     e.g. `42^`, `36^`) -- `coverage_test.py`'s own `strip_mark()` already strips the full set
     (`* ^ \` ' ´ ˇ ¨ =`) for exactly this reason, but a naive `reconcile_passes.py passA.tsv passB.tsv` call
     does not, so `70` and `70*` compare as different signs.
  2. The two symbol glyphs are labelled differently by convention (`[circle-dot]`/`[phi-symbol]` in passA.tsv vs.
     `Th`/`Ph` in passB.tsv) for the *same* referents, which also reads as disagreement to a literal string compare.
  3. Pass B's run boundaries are not numbered 1:1 against pass A's from partway through the letter: pass B (correctly, see below) merged several of pass A's runs that pass A had incorrectly split at a page-line wrap with no intervening French word -- so `reconcile_passes.py`'s row-key alignment (which assumes the same run_id means the same content in both files) compares unrelated text once the row numbering diverges.
  Re-ran with marks stripped (the same regex `coverage_test.py` uses) and symbol labels normalized, aligning the
  **whole letter as one token stream** (both pages, reading order) rather than by row_id, since row segmentation
  itself was in question: **agree 362/400 = 90.5%** (`tools/reconcile_passes.py` on the two derived single-row
  files; scratch script + derived files not committed, reproducible from passA.tsv/passB.tsv). This is the
  meaningful agreement figure for this pass pair -- well above the 60% gate (`transcription.md` /
  `PROCESS-2026-09-24` proposal 4) -- and it is the number this job used to decide to proceed to settling rather
  than stop.

**3. Settling from the image (not by vote), all 38 real disagreement columns (`reconcile_disagreements.tsv` in
this folder is the mark/symbol-normalized, whole-letter-stream disagreement list):**
  - Most of the 38 columns are the `[circle-dot]`/`Th` and `[phi-symbol]`/`Ph` labelling difference (not a real
    disagreement -- both passes saw the same glyph, just wrote its name differently; normalized to
    `[circle-dot]`/`[phi-symbol]` throughout `ciphertext.tsv`).
  - **A real digit disagreement**, the run opening "puis que je feur qu'illes": passA.tsv read the first token as
    `83`; passB.tsv (itself flagging uncertainty: "first token ... read closely as '88', not '83'") read `88`.
    Zoomed crop of `leaf0729.jpg` at native resolution (this worker, this pass) against a confirmed `83` elsewhere
    on the same page ("`10 83 77 le bruit`") for shape comparison: the two glyphs are visibly different (the
    confirmed `83`'s second digit is open-sided; the disputed token's second digit is a closed loop matching
    the page's `8`s). **Settled: `88`, not `83`** -- pass A misread this one.
  - **A whole printed line of ciphertext (25 tokens) is missing from passA.tsv entirely.** The line "`7 c 76 81
    88 u 70 p 44 92 22 13 75 6 47 53 34 80 72 22 39 9 89 61 7 75`" (gloss below it: "prize may z car on la pr j
    lon ge du") sits between "`...ne fachant pas encor 89`" and "`58 51 32 ce qui ne ce fera...`" on leaf 729 --
    confirmed directly on the page image, an entirely cipher line with no intervening French word at either
    line-wrap, so by the stated run rule it is one continuous run with the tokens either side of it. None of
    these 25 tokens appear anywhere in passA.tsv's R017-R026 (checked against every row); passB.tsv's R020 has
    them in full. **Settled: pass B correct, pass A skipped the whole line** (the single largest reconciliation
    finding this job made -- a plausible whole-line skip in a single unreconciled pass, exactly the kind of error
    the transcription brief's two-pass rule exists to catch).
  - **A symbol identification.** At "`...74 99 [symbol] 42 o 40 ce qu'il va à craindre`" (end of the Espagne
    line), passA.tsv read the symbol as `[phi-symbol]`; passB.tsv read it `Th` (circle-dot). Zoomed crops of
    all three of this letter's circular-symbol occurrences on leaf 729, compared side by side: the "affaires ...
    68 [X] d 61" occurrence and this one both show a circle with an internal horizontal squiggle/mark; the "qui
    eft al lé e à la" occurrence (both passes agree: phi) shows a circle with a clean vertical bar, visibly
    different in kind. **Settled: circle-dot type (matches passB.tsv), not phi** -- pass A mislabelled this one.
  - **An isolated single-token run pass A dropped as plain text.** "`Je vis hier 17 pour lui`": passA.tsv's R035
    row folds "17" into its `ctx_left` field (i.e. did not treat it as cipher at all); passB.tsv's R026 reads it
    as a one-token run. The printed "17" is set in the same type as the surrounding cipher numerals, and the
    letter's own dateline ("Londres, 20 Novemb. 1654") makes "hier" (yesterday) the 19th, not the 17th, so a
    plain date reading of "17" does not fit the sentence chronologically. **Settled: cipher token, pass A missed
    it.**
  - **A symbol plus a digit dropped at the very end of leaf 729.** The last cipher line on the page reads
    "`[phi-symbol] 84 91 7 23 7 ll 47 5 77 12 9 94 x 18 7 80 38 40 73 65 71 89 16 21 39 de`" (confirmed on the
    image, immediately above the "Vol. II. / 8 X / vos" footer and catchword) -- passA.tsv's R040 is missing both
    the leading phi-symbol and the "47" that sits between "`ll`" and "`5`"; passB.tsv's R031 has both, and
    (unlike this worker's initial suspicion) had already correctly attributed the run to leaf 729, not 730 --
    passA.tsv's R040 wrongly put it on leaf 730. **Settled: pass B correct on both the symbol, the extra digit,
    and the leaf.**
  In every one of the 8 real (non-labelling) disagreement points checked against the image, pass B's reading was
  the one confirmed -- pass A's flaws were all omissions or misreadings, not overreadings; no point was found
  where pass A had something correct that pass B lacked.

**4. `ciphertext.tsv` written**: pass B's run structure (which correctly did not split a run at a page-line wrap
lacking an intervening French word, unlike pass A -- this is *why* pass B did not lose the 25-token line), marks
kept, symbol labels normalized to `[circle-dot]`/`[phi-symbol]`, plus a `confidence` column (H = this run's
tokens all agree with passA.tsv after normalizing marks/labels; M = at least one token disagreed with or was
absent from passA.tsv, settled here from the image) and a note on every M row citing this section.
24 of 33 runs are fully H; the 9 M rows are exactly the ones covering the digit fix, the missing line, the symbol
fix, the dropped "17", and the dropped end-of-page symbol+digit, all as settled above. Token-level: 366/400
(91.5%) agree with pass A once marks/labels are normalized (this worker's own NW alignment, `reconcile_agreement.tsv`
reports the equivalent 362/400 = 90.5% from `tools/reconcile_passes.py` itself on the derived whole-letter-stream
files -- the 4-token gap between the two figures is tie-breaking differences between the two NW implementations
on a few ambiguous alignment columns, not a disagreement about content).

**5. Cheap test re-run on the reconciled ciphertext**, same `key_gloss.tsv` "primary" (30-code, non-conflicting)
key, unchanged -- this tests whether the transcription fixes alone move the earlier negative, holding the key
fixed:

| | tokens | key size | coverage (before -> after) |
|---|---|---|---|
| **target**, passA.tsv (TX-BARRT, 25 Sept) | 368 | 30 | 108/368 = 29.3% |
| **target**, ciphertext.tsv (this pass, reconciled) | 400 | 30 | **120/400 = 30.0%** |
| **control**, avg of 10 seeds, matched to passA.tsv's profile | 368 | avg ~43 | 33.4% (range 28.5-37.0%) -- unchanged, re-verified this pass as a regression check |
| **control**, avg of 10 seeds, matched to ciphertext.tsv's profile | 400 | avg ~42 | **31.1% (range 26.5-34.0%)** |

`coverage_test.py key_gloss.tsv ciphertext.tsv` and `matched_control.py --seeds 10 --ctpath ciphertext.tsv`
reproduce these numbers. `matched_control.py` was extended (not rewritten -- same file, same corpus, same
control-construction logic) with a `--ctpath` option; the default (`passA.tsv`) still reproduces TX-BARRT's exact
original 33.4%/74.2% (checked, this pass), so the original result is unaffected and still reproducible.
For `--ctpath ciphertext.tsv`, the control's per-run gloss-reveal count (`k_gloss`) is **not** read from
`ciphertext.tsv`'s own `gloss_as_printed` word count -- an earlier attempt at this did that and it roughly
doubled the control's average key size (30 -> ~81-87 codes), because that field, unlike `key_gloss.tsv`, includes
gloss text passA.tsv's own notes explicitly flagged as *not* confidently mapped per token (e.g. R011: "9 gloss
words for 6 tokens -- sparse/mismatched, no confident per-token mapping attempted"); counting all of it as
"revealed" handed the control a bigger, better-informed key than the real pass ever built from the same gloss --
exactly the unmatched-design failure CLAUDE.md rule 3's Salviati/PX-BRODEC lessons warn against. Instead,
`matched_control.py` now projects the *original* passA.tsv glossed-token-position set onto `ciphertext.tsv` by
the same Needleman-Wunsch alignment used to build `ciphertext.tsv`, and every token that is new relative to
passA.tsv (the recovered 25-token line, "17", the end-of-page symbol+digit) counts as **unglossed** for the
control -- deliberately conservative, since it credits the control with none of the gloss the reconciliation
itself uncovered. See the module docstring in `matched_control.py` for the full method.

**Verdict: negative holds, unchanged by the transcription fix.** The reconciled target's coverage (30.0%) is
still statistically indistinguishable from -- and still slightly below -- the matched control's average (31.1%,
target squarely inside the control's 26.5-34.0% range). Recovering the missing line, the dropped "17", the
dropped symbol+digit, and fixing the one digit misread did not move the result: this was not a transcription
artifact. The spec's `cheap_test_done` is updated below with both the original and reconciled numbers side by
side (rule 3: report both, before and after).

**Next test (not this job, one line per the brief):** the token-shuffle/key-shuffle permutation z-test on this
letter's real (now reconciled) gloss positions that TX-BARRT and the spec both already named as the sharper next
cheap test -- still not run.

**Files:** `passB.tsv` (blind pass B), `ciphertext.tsv` (reconciled transcription, H/M graded), `reconcile_disagreements.tsv`
/ `reconcile_agreement.tsv` (from `tools/reconcile_passes.py` on the mark/symbol-normalized whole-letter-stream
derived files -- the derived files themselves are scratch, not committed, and reproducible from passA.tsv/passB.tsv
by the method described in s.2 above), `matched_control.py` (extended with `--ctpath`, see s.5).
Grades: `ciphertext.tsv`'s H/M column is a transcription-confidence grade (tools/reconcile_passes.py's own H/M
convention: agreed-blind vs. reconciler-settled), distinct from rule 4's H/C/S/M/I reading grades in `key_gloss.tsv`
(unchanged by this pass, still all grade C). Rule 10: nothing in this section is new, unpublished, unread, first
or never printed -- a verifier classifies novelty, and none is claimed here.

**Hosts:** none (all work this pass was against images and files already on disk from TX-BARR/TX-BARRT; no
network requests made).

## ZX-BAR (25 Sept 2026)

Intake gate checked first (per the lane orchestrator's run at 15:44 UTC, brief-cited): `open` verdict (top of
file, section 4) names the standard edition and the pages/full-text searches actually read -- passes
`.claude/briefs/check-solved.md`'s bar, exit 0. The named next test from s.8/the spec: "a permutation z-test on
the letter's real gloss positions" -- does the gloss-derived key carry information about the UNglossed tokens
beyond what any assignment of the same code frequencies would? Answered through a sharper proxy first: is a
held-out gloss occurrence of a code predictable from that code's OTHER gloss occurrences, more than chance?

**Statistic (stated before running, per the brief):** leave-one-out over every row of `key_gloss.tsv` (64 rows,
every row grade C, one row per glossed code occurrence -- see s.2/s.3 above and `key_gloss.tsv`'s own header
comment). Hold out row *i*; rebuild a key from every OTHER row (group remaining rows by code; a code gets a
key value only if every remaining observation of that code agrees on one value after `normalize()` -- lowercase,
then fold long-s/f, u/v, i/j, since two gloss occurrences of the same word can be OCR'd/printed with different
old-spelling variants -- otherwise the code has no key entry; this is `key_gloss.tsv`'s own primary/conflict
rule, recomputed fresh each time since removing one observation can change which codes conflict). Predict row
*i*'s value from that key; correct if the code is in the key and the predicted value normalizes equal to row
*i*'s true value. The statistic is the count of held-out rows predicted correctly, out of 64.

**Null A (key shuffle):** permute the VALUE column among all 64 observations, codes and their run/position
fixed -- keeps every word's total occurrence count fixed across the letter ("each word's code count" read as
how many times each word's code appears) while destroying any real code<->word correspondence.

**Null B (token shuffle):** within each `source_run`, permute the CODE column among that run's own rows only,
gloss words fixed in their printed order -- tests whether the target's sequential code-to-gloss-word alignment
(NOTES.md s.2's method, since typesetting does not column-align a gloss word under its source token) is itself
informative, independent of which codes exist where.

`permutation_test.py` implements both (`--help`, fixed seeds 0/1, 1000 permutations each, reproducible from
`key_gloss.tsv` alone, no network):

```
N observations (key_gloss.tsv): 64
real leave-one-out statistic: 0/64 (0.0%)
Null A (key shuffle, n=1000): mean=0.409 sd=0.891 z=-0.459 p=1.0000
Null B (token shuffle, n=1000): mean=0.256 sd=0.768 z=-0.333 p=1.0000
```

The real statistic is 0/64: not one held-out gloss occurrence of any code is correctly predicted from that
code's other occurrences. This follows mechanically from the conflict structure already documented in s.8/s.3 --
every code in `key_gloss.tsv` that has more than one observation has ALL DIFFERENT values (that is exactly why
those rows are marked `conflict`), and every code with exactly one observation loses its only observation when
held out, leaving no key entry to predict from. Both null z-scores are *negative* (real is at or slightly below
the null means of ~0.3-0.4), i.e. the real data is not even as internally consistent as a random relabelling of
the same 64 (code, value, run) triples.

**Same test on a matched control (breadth rule step 2), 10 seeds:** `matched_control.py` gained
`build_control_observations(seed, ctpath)` (ZX-BAR addition, same rng call sequence as the existing
`build_control()` for a given seed -- checked: seed 0's derived primary-key size, 43, matches
`build_control(0)`'s own reported `key_size` exactly), which returns the control's per-token (code, value,
source_run) observations instead of aggregate coverage counts, matched to `ciphertext.tsv`'s 33-run/400-token
profile (same construction TX-BARRT/YX-BARB used: fr16 period French, ~9 heavily-reused function words each
given 2-4 homophone codes, same per-run gloss-reveal counts). `permutation_control.py` (new script, imports
`permutation_test.py` and `matched_control.py` directly -- identical statistic/null code, not a reimplementation)
runs the same leave-one-out statistic and both nulls, same seeds (0/1), same n=1000, on each of 10 control draws:

```
control seed 0: N=50 real=6 (12.0%) zA=14.577 pA=0.0000 zB=6.381 pB=0.0000
control seed 1: N=50 real=7 (14.0%) zA=23.711 pA=0.0000 zB=10.249 pB=0.0000
control seed 2: N=50 real=8 (16.0%) zA=19.289 pA=0.0000 zB=8.021 pB=0.0000
control seed 3: N=50 real=7 (14.0%) zA=17.878 pA=0.0000 zB=10.874 pB=0.0000
control seed 4: N=50 real=8 (16.0%) zA=24.972 pA=0.0000 zB=12.371 pB=0.0000
control seed 5: N=50 real=8 (16.0%) zA=24.512 pA=0.0000 zB=8.021 pB=0.0000
control seed 6: N=50 real=6 (12.0%) zA=17.705 pA=0.0000 zB=5.727 pB=0.0000
control seed 7: N=50 real=7 (14.0%) zA=22.258 pA=0.0000 zB=7.792 pB=0.0000
control seed 8: N=50 real=6 (12.0%) zA=18.342 pA=0.0000 zB=9.104 pB=0.0000
control seed 9: N=50 real=8 (16.0%) zA=20.722 pA=0.0000 zB=6.706 pB=0.0000

zA range over 10 seeds: 14.577 to 24.972, mean 20.397
zB range over 10 seeds: 5.727 to 12.371, mean 8.525
```

A real word-per-code nomenclature of this design -- fewer glossed positions per run than the control (50 vs. the
target's 64, since the control's `k_gloss` is deliberately the conservative NW-projected passA glossed-position
count, see `matched_control.py`'s docstring), same homophone/conflict-generating structure -- gives this test a
strongly positive z every time: 12-16% of held-out control occurrences are predicted correctly (vs. 0% for the
target), because a genuine nomenclature's repeated code occurrences DO agree with each other far more than a
random relabelling would, even with 2-4 homophone codes competing for the same top words.

**Verdict, both numbers (CLAUDE.md rule 3):** target zA=-0.459, zB=-0.333 vs. control range zA 14.577-24.972,
zB 5.727-12.371 (10 seeds). The target's z sits nowhere near the control range and is near zero (in fact
slightly negative) rather than merely lower -- this is the brief's "clean negative" case, not the "behaves like
a real nomenclature" case: **the gloss positions in this letter carry no transferable key.** The permutation
test cannot extract more from the gloss than the earlier coverage test did (s.8: 30.0% vs. control avg 31.1%,
already indistinguishable from chance) -- if anything it sharpens that result, since a genuine nomenclature of
this exact design (same homophone/conflict structure) is trivially internally consistent under leave-one-out
(control z well over 10), while this letter's gloss-derived code assignments are not consistent with themselves
at all. This closes the cryptanalytic route on this letter alone (status set to `closed-negative` above),
pending a key (the solver-repositories' noted "1655 cipher" for this same correspondence, or DECODE's Add MS
4200 records 8395/8398, both still unopened -- s.5 above, not this job's scope) or a sibling in the same key.

**Files:** `permutation_test.py` (statistic + both nulls, operates on `key_gloss.tsv` or any same-shaped TSV),
`permutation_control.py` (runs the same test on `matched_control.py`'s control draws), `matched_control.py`
(gained `build_control_observations()`, existing `build_control()`/coverage numbers unchanged and re-verified
reproducible). Spec's `cheap_tests_in_order` and a second `cheap_test_done` entry updated below this section's
numbers (kept the first entry, per the brief).

Grades: unchanged from s.8 -- every `key_gloss.tsv` row is grade C (from the gloss, known plaintext for that
span); nothing here is graded H or S; no candidate plaintext is reported, so `judge_plaintext.py` was not run
(rule 7 n/a, no reading claimed). Rule 10: nothing in this section is new, unpublished, unread, first or never
printed -- a verifier classifies novelty, and none is claimed here.

**Hosts:** none (disk-only, per the brief -- `ciphertext.tsv`, `key_gloss.tsv`, `coverage_test.py`,
`matched_control.py`, `tools/data/fr16`; no network requests made).
