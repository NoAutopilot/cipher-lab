# AUDIT: novelty of the f.35 reading (Danzay to the Cardinal of Lorraine, "27 Jan 1557")

Verifier session, 24 Sept 2026 (03:00-03:15 UTC), orchestrator session_01EFmUvFAifLKGdBSsW9mjEG. This session
did not take part in the check-solved, transcription or solver sessions and did no decoding. Levels N0-N5 are
those of CLAUDE.md rule 10. Claim under audit: NOTES.md "Reading with Tomokiyo's key" says f.35 reads with
Tomokiyo's published 1557 Danzay key: 638 cipher tokens, H 508 (61 nulls) / M 61 / U 69 [H 509 / M 59 / U 70 after the second-reader adjudication of 24 Sept 2026, NOTES.md], continuous French on
about 23 of 37 lines; the letter continues on f.36, which has not been transcribed [superseded: f.36r has since been transcribed and partly read, see "f.36r, 24 Sept 2026"; V3b, 24 Sept 2026]. The repo makes no novelty
claim. This audit tests whether the plaintext or a decipherment of f.35 is already in print.

## 1. Verdict

| item | prior plaintext | prior decipherment | level |
|---|---|---|---|
| fr.20140 f.35r-v, Danzay to the Cardinal of Lorraine, dated 27 Jan 1557 | not located (see the log in section 3) | none: Tomokiyo, the only source that names the folio, calls it "not deciphered" and prints only the key | **N3** |

**Why N3 and not N4.** Every edition and study of Danzay that could hold this letter was reached and searched
(section 3). Two sources that mention fr.20140 or Danzay in 1557-58 were read only as search snippets:
Delavaud 1911, which describes "fos 16-56" of this volume, and Cuisiat 1998, the Cardinal's own letters. JSTOR
was not searched. Until those three gaps are closed, the class stays N3.

**Safe sentence:** "BnF fr.20140 f.35 (Danzay to the Cardinal of Lorraine, dated 27 Jan 1557) has no
contemporary decipherment. Read with the key Tomokiyo published in 2026, about 23 of its 37 lines give
continuous French (509 of 638 cipher tokens at grade H, 70 signs unkeyed). No prior decipherment or printed
plaintext was located in the Danzay editions, the Scottish and English state-paper series, or the Danish
regesta (search log in AUDIT.md). The letter continues on f.36, which has not been read." [Superseded by the N4 safe sentence in "N4 decision (Cryptiana closed)"; f.36r is now partly read. V3b, 24 Sept 2026.]

**Unsafe sentence:** "The first decipherment of a previously unread 1557 letter from Danzay." Four things are
wrong with it. It needs N4. The reading is partial. The key is Tomokiyo's, so the result is a key application
(recovery) and should be credited to his reconstruction. And the letter is incomplete without f.36.

Qualifiers for any sentence about this reading:
- It is **partial**. Of 37 lines, 14 are not continuous French (R1-R4, R7, V1, V3, V4, V29 and parts of others).
  69 tokens are unkeyed and 61 are M. The seven grade-I key suggestions in NOTES.md have not been applied or
  tested.
- It rests on **one reconciled transcription**. The two blind passes could not be merged sign by sign because
  their `unk` labels were private to each pass. The solver re-read the strips glyph by glyph, and that re-reading
  (reconciliation.md) is the only sign-level transcription. No second independent reader has checked it.
- About 150 clear-hand words carry much of the letter's sense. Those words were never enciphered. Whether a
  historian has quoted them is covered by the same search, but the cipher runs are the only part that needed
  "reading".
- The key is Tomokiyo's (cryptiana, first posted 22 Feb 2026). He reconstructed it from the contemporary
  decipherments of f.16, f.24 and f.30. Credit him in any outward note.

**Evidence quality:** good for the Danish, Swedish and English print series (full OCR text grepped, or token
counts for every page). Moderate for French scholarship (snippet-only for two titles). Weak for journal
literature (no JSTOR). **Confidence** that no printed decipherment of f.35 exists: high, because Tomokiyo
himself found none and the manuscript carries none. Confidence that its clear passages are not quoted anywhere:
moderate (Delavaud unread).

## 2. What was extracted from the repo

- Item: BnF fr.20140 (old shelfmark Gaignières 679, 10 and 11), f.35r-v. Gallica `btv1b52521512h` canvases
  f69/f70 (labels 35r/35v), with an alternative digitisation at `btv1b10782904z`. Sender Charles de Danzay,
  French resident in Denmark. Recipient the Cardinal of Lorraine. Dated 27 January 1557 in the margin. The
  place is not stated in the files (presumably Denmark). The letter is unfinished on f.35v and continues on f.36.
- Ciphertext: `ciphertext.txt`, 791 tokens. Reading: `reading.txt` (decode.py --check).
- Phrases searched. Clear hand: "le plus commodement qu'il me sera possible", "ceste depesche affin que vous
  peussiez congnoistre l'estat des affaires de ce royaulme", "la promesse qui de long temps m'a esté faicte",
  "attendant plus certain et expres commandement de ce que je doy entreprendre", "il me semble qu'il seroyt bon
  de regarder". From the key: "chancelier", "Danoys", "marchans de Lion", "Augsbourg", "de ceulx desquels", "la
  resolution des", "de leur volonte".
- What earlier sessions searched (NOTES.md "Check-solved (24 Sept 2026)"): Tomokiyo; Bricka 1901 (ruled out by
  its 1567-1573 span); the "Fryxell vol. IX" Handlingar (not reached; the IA copy `handlingarrrand06unkngoog`
  was the wrong volume); CSP Foreign (a Danzay index hit traced to the 1580s volume); IA titles; Google Books;
  both solver repositories (shallow clones on 24 Sept 2026, no hit).

## 3. Search log (24 Sept 2026)

Requests: archive.org about 30 (advancedsearch, metadata, djvu text, be-api fts), data.htrc.illinois.edu 2,
googleapis.com 14 (key and `country=US`, key never printed), books.google.com 1 (a challenge page came back,
so this session stopped using that host), books.openedition.org 1, archivesetmanuscrits.bnf.fr 1, WebSearch 4.
All requests were at least 1.6 s apart and sent one at a time.

**(a) Editions of Danzay's correspondence**
- *Correspondance de Charles Dantzai* (Stockholm, Elmén och Granberg, 1824). This is **Handlingar rörande
  Skandinaviens historia vol. XI**, not vol. IX. The series' own chronological register (IA
  `handlingarrrand03scangoog`) indexes "Dantzai ... hans brefvexling, 11: 1-345", and it indexes a further
  "Dépêches de l'année 1575" at 17: 132. Tomokiyo's "vol. ix" is a mis-citation, and so is the check-solved
  brief's "Fryxell vol. IX". The volume itself is IA `handlingarrrand02scangoog`, dated 1824. Its Swedish preface
  says the despatches are Danzay's own copies, kept at Drottningholm. The full djvu text was grepped: "1557"
  gives 0 hits, "Augsbourg" gives 1 (a 1570s diet), there is no "Lorraine" as cardinal, no "marchans/marchands
  de Lyon", and the years run 1562-1579 (mostly 1570s). **Reached. Does not contain the letter.** This closes
  the gap that check-solved left open.
- Bricka (ed.), *Indberetninger fra Charles de Dançay ... 1567-1573* (1901), HathiTrust `hvd.hnnfqp`. HTRC
  Extracted Features token counts for all 266 pages: 0 pages with 1556, 1557 or 1558, "Augsbourg", "Lyon" or
  "Lion". **Does not contain the letter** (and its span already rules it out).
- 15 other Handlingar volumes on IA (all the `handlingarrrand*` ids) were grepped for Dantzai, Danzay and
  Dançay: the only hits are vol. XI and the register.

**(b) Calendar of State Papers Foreign, Mary 1553-1558** (Turnbull 1861, IA `cu31924028043622`, full djvu
text): 0 hits for Danzay, Dansay or Dantzai. The January 1557 and January 1558 entries are unrelated.
**Does not contain the letter.**

**(c) Scottish, French and Danish documentary series**
- Teulet, *Papiers d'État ... relatifs à l'histoire de l'Écosse* (Bannatyne Club 1851) and *Relations
  politiques de la France et de l'Espagne avec l'Écosse* (1862). Vol. 1, 1515-1560 (IA
  `relationspoliti06teulgoog`), has 0 Danzay hits. Vol. 2 (`relationspoliti07teulgoog`) has a note saying he
  searched for Danzay's correspondence without success: "Quelques lettres de cet ambassadeur sont conservées à
  la Bibliothèque impériale, mais elles sont toutes postérieures à l'année 1567 et étrangères aux affaires
  d'Écosse." This matters because a 1557 letter to the Cardinal of Lorraine is squarely within Teulet's scope,
  and his note shows that he did not know of the fr.20140 letters.
- Louis Paris, *Négociations, lettres et pièces diverses relatives au règne de François II* (1841, IA
  `ngociationslet00pari`). Danzay appears only in the introduction (pp. xi, xxxiv), in a 1548 commission to
  Basse-Fontaine. No 1557 letter is printed.
- *Regesta diplomatica historiae Danicae*, 2nd series (IA `regestadiplomat04copegoog`). Grepped for Danzay and
  Dancay: the hits are 12 Mar 1555 (Noailles), 3 Oct 1558 (Gustav I) and the 1560s-70s. No 1557 or early-1558
  entry for a Danzay despatch, and no French entries in the 1557 section.
- Rørdam, *Résidents français près la cour de Danemark au XVIe siècle* (1897/98), HathiTrust
  `njp.32101074252246`. Token counts for all 68 pages: 1557 appears on pp. seq 21-22 (the Laetus dedication and
  the 1558 negotiations), and there are no tokens for "20140", "Augsbourg", "Lyon" or "chiffre". His Danish
  version, *Historiske Samlinger og Studier* II (IA `historiskesamli02rrgoog`), was read around 1557-1559: he
  knows only that "en Del af Danzay's Rapporter og Breve" are at the BN and does not use fr.20140.
- Richard, *Un diplomate poitevin du XVIe siècle: Charles de Danzay* (1910, IA `undiplomatepoite00richuoft`),
  full text: no citation of fr.20140. Its only 1557 facts are that Danzay was in Paris in 1557, received his
  commission on 20 May 1557, and was back in Denmark on 22 Apr 1558. No 1557 letter is quoted.
- Not searched: Danmark-Norges Traktater, Rørdam's Monumenta, the Christian III correspondence editions.
  These are treaty and domestic series with a low prior; the Regesta above calendars them.

**(d) Holding archive and Tomokiyo**
- The BnF Archives et manuscrits notice for Français 20140 (`cc51725m`) reads: "Correspondance, originale et en
  partie chiffrée, de Charles de Danzay, ambassadeur en Danemark, 1557-1567 (fol. 16)". It gives no
  bibliography and no edition.
- Tomokiyo, "Danzay's Ciphers" (local mirror `sources/cryptiana/web/danzay.htm`) lists f.16, f.24, f.30 and
  f.35 and says f.35 is "not deciphered". His page prints the reconstructed key table (an image) and discusses
  nulls. **It prints no reading or plaintext of f.35**, nor of the other three.
- Ryabov 2025 (*Quaestio Rossica* 13/4, pp. 1487-1508). The abstract, via the journal page and WebSearch, says
  it reconstructs the cipher from letters of 14 Oct 1574 and 28 Feb 1578. That is a different cipher and a
  different volume. [Confirmed from the full text, 24 Sept 2026: see "Ryabov 2025" at the end.]

**(e) Full-text engines**
- IA be-api fts: "la promesse qui de long temps" 0; "attendant plus certain et expres commandement" 0.
  "marchans de Lion" Augsbourg gave 4 loose matches: Wicquefort-type and *Revue historique* 1876, not Danzay.
  "Danzay" 1557 gave 545 loose hits; the relevant ones were followed up above. "français 20140" gave 2
  (Delisle's *Mélanges*, not Danzay).
- Google Books API: all five phrase queries on the clear text returned 0. "20140" Danzay returned the
  BnF catalogue and **Delavaud, *Les Français dans le Nord* (1911)**, snippet: "[lettres de] Danzay, datant des
  années 1557 à 1568, se trouvent à la Bibliothèque nationale, dans les ms. 15967 (fo 624) et 20140 (fos
  16-56) ... [elles] sont d'une lecture très attachante". The book is snippet-only (NO_PAGES) and not on IA
  under the author's name. **Unreached in full.** He may paraphrase or quote the clear passages. He is unlikely
  to have deciphered f.35, since its cipher carries no decipherment.
- HathiTrust HTRC token counts: done for Rørdam and Bricka (above).

**(f) Solver repositories and DECODE.** On 24 Sept 2026 the check-solved worker made fresh shallow clones of
dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers and found no hit on "20140" or "Danzay". That result is
cited here, not re-cloned. The repo has no DECODE cache (`sources/` holds none), and the DECODE login is still
blocked (ASKS row 1). **DECODE unreachable.**

**(g) Scholarship**
- Daussy 2004 (OpenEdition, full text): no 1557 letter; 1557 appears only in the Laetus dedication.
- Cuisiat (ed.), *Lettres du cardinal Charles de Lorraine* (1998). Google Books, snippet only: Danzay appears
  in a note as "agent diplomatique résidant à Copenhague", near letter no. 487 of 20 June 1558. This edition
  holds the Cardinal's outgoing letters, so it would not print a letter addressed to him, but its notes could
  quote one. **Snippet-level only.**
- JSTOR: **not searched** (no session budget spent on the login). Google Scholar via WebSearch: nothing beyond
  Ryabov 2025 and the biographies above.

## 4. Postmortem and corrections

No over-claim was found. NOTES.md, reading.txt, reconciliation.md, status.json and STATUS.md do not use
"new", "unpublished", "first" or "previously unread" about f.35, and the solver's section ends "Novelty is not
classified". The failure worth naming is a **wrong citation passed down the chain**: Tomokiyo's "vol. ix" for
the 1824 Correspondance went into the check-solved brief as "Fryxell vol. IX". The worker then searched a
volume IX that was not the edition, and recorded the edition as unreached. The series register shows it is
vol. XI (IA `handlingarrrand02scangoog`). Its text contains no 1557 material.

Corrections made:
- NOTES.md: a dated note under check-solved item 3, saying the 1824 edition is Handlingar XI, has now been
  reached and holds no 1557 letter.
- status.json, this card's `note`: the "Fryxell vol. IX unreached" clause is replaced by the verifier's
  class. Stage and board placement are left to the orchestrator.

One open question for whoever next works on the reading. **The date may be old style.** Before 1567 the
French year began at Easter, so "27 janvier 1557" may be 27 January 1558 (new style). Richard places Danzay
in Paris during 1557 and back in Denmark on 22 April 1558. Any later print search should try both 1557 and
1558. This audit already did so for CSP Foreign, the Regesta, Teulet and Rørdam.

**Steps from N3 to N4:**
1. Read Delavaud 1911, the pages around the fr.20140 note (the snippet reports pp. 52/74 in its two printings).
   Try HathiTrust or Gallica; the latter may hold the *Bulletin de la Société de géographie de Rochefort*.
2. Read Cuisiat 1998 around nos. 480-490 (1557-58).
3. Run a JSTOR search for "Danzay" OR "Dançay" and 1557/1558.
4. Optionally, ask a Danzay specialist (Daussy) whether the fr.20140 letters have been edited. That would be
   the route to N5.

## Open-index scholarship pass (24 Sept 2026)

Worker session (Sonnet, cap $8, orchestrator session_01EFmUvFAifLKGdBSsW9mjEG), replacing JSTOR as the
scholarship-coverage gate (CLAUDE.md, JSTOR-QUEUE.tsv rows 16-19; this is step 3 above, run through the open
indexes rather than JSTOR itself, per the owner's 24 Sept note). Not a verifier session: does not move the N3
class, does not decode. Full per-host results in `OPEN-INDEX-RESULTS.tsv` rows 16-19.

**OpenAlex and Semantic Scholar unreachable** for this whole pass (shared-IP daily anonymous budget exhausted /
429 on repeated attempts; identical failure across all five targets this pass covered, exact error text in
fr2980-gramont/AUDIT.md's equivalent section of this date). Logged as unreachable, not as a negative.

**CrossRef and HAL both independently re-surface Daussy 2004** ("Un diplomate protestant au service d'un roi
catholique: Charles de Danzay, ambassadeur de France au Danemark (1515-1589)", in *Élites et notables de l'Ouest
XVIe-XXe s.*, PUR, pp.277-294) — cross-confirming it is the same article already reached via OpenEdition in
section 3(g), not a second one. **CrossRef also independently re-surfaces Ryabov 2025** (*Quaestio Rossica*
13/4, "The Diplomatic Cipher of Charles de Danzay") — already known per section 3(d): reconstructs a different
cipher, from letters of 14 Oct 1574 and 28 Feb 1578, not fr.20140 f.35 or the 1557 letter. Neither is new.
Persée returns no relevant hit for any of the four queries (results dominated by an unrelated pair of articles
on the Norman navigator Jean Sauvage's 1586 Russia voyage, matched on "voyage"/16th-c-diplomacy keywords, and
three OECD "Danemark" economic-survey entries matched on the country name alone).

**Row 17, one minor new biographical fact:** WebSearch surfaces that Danzay was made "panetier" (a bread-officer
post at court) on 20 May 1557 — not previously in NOTES.md or this file. It bears on his career, not on a letter
to the Cardinal of Lorraine or its cipher; no correspondence between Danzay and the Cardinal was located by any
host.

**Row 18, Delavaud 1911 located on Gallica, still not read — this is new.** Google Books' snippet (section
3(e)) placed the fr.20140 mention on pp.52/74 of Delavaud's *Les Français dans le Nord* (Rouen, 1911) but the
scan there is `NO_PAGES` (no preview at all). This pass located a full page-image copy on **Gallica**, ark
`bpt6k6571713p` (`https://gallica.bnf.fr/ark:/12148/bpt6k6571713p.texteImage`) — a route step 1 above did not
yet have. One `.texteBrut` OCR-download request was made: it 302-redirected to
`/services/engine/search/altcha?altchaNotVerified=false`, the **same Gallica bot-verification wall** documented
in `ciphers/fr2980-gramont/AUDIT.md` for the Camusat and Champollion-Figeac gaps. Not retried (single-attempt
rule). This confirms, for the first time, that the altcha wall is not specific to manuscript-image arks — it
also blocks a public-domain **printed book's** OCR download on Gallica. The book is now precisely located but
its text remains unread; a cold, uncontended Gallica session (no concurrent worker on the host, as
fr2980-gramont/AUDIT.md already recommends for its own two gaps) is the one remaining route, and could close
this target's step 1 in the same pass as fr2980-gramont's Camusat/Champollion-Figeac gaps, since all three are
now the same kind of block on the same host.

**Verdict for this pass:** no hit on any of the six hosts locates a new print or decipherment of fr.20140 f.35.
Step 3 above (JSTOR) is substituted, not closed, by this pass, per the owner's directive; step 1 (Delavaud) is
now a precisely-located, still-unread Gallica scan rather than an unreached Google Books snippet; step 2
(Cuisiat) and step 4 (asking Daussy) are untouched. **N3 unchanged; the verifier does not move the class from a
scholarship-pass worker's report.**

Requests: api.openalex.org 8 (all 429, shared budget). api.semanticscholar.org 6 (all 429). api.crossref.org 4
(200 each). api.archives-ouvertes.fr 8 (4 combined-query 0-hit attempts, 4 narrower follow-ups, one of which —
"Danzay Danemark" — returns the Daussy 2004 hit). www.persee.fr 4 (200 each). gallica.bnf.fr 1 (`.texteBrut`,
302 to altcha, not retried). WebSearch 4 queries. No logins, no credentials, no decoding.

## Second audit (adversarial), 24 Sept 2026

LANE V worker, 03:34-03:55 UTC, orchestrator session_01B5x2Dshzz71xBzbJqFnXYQ. This session took no part in the
solver, transcription, check-solved or first-verifier sessions and did no decoding. Brief: find this letter, its
plaintext or a decipherment of it in print, and so prove N3 wrong. The audit covers only f.35; f.36 was out of scope.

### Verdict

| item | first audit | this audit | reason |
|---|---|---|---|
| fr.20140 f.35r-v, Danzay to the Cardinal of Lorraine, dated 27 Jan 1557 (possibly 1558 n.s.) | N3 | **N3 confirmed** (two audits) | No printed decipherment, plaintext or quotation of the letter was found in any source family below. Not raised to N4 for three reasons. Delavaud 1911, the only study known to describe fr.20140 fos 16-56, is full-view only on Gallica, which is another lane's host, so it has been searched only through Google Books' full-text index (snippets). OpenAlex, CrossRef and Semantic Scholar rate-limited this session. The JSTOR rows are still queued. |

**Safe sentence** (unchanged in substance from the first audit): "BnF fr.20140 f.35 (Danzay to the Cardinal of
Lorraine, dated 27 Jan 1557) has no contemporary decipherment. Read with the key Tomokiyo published in 2026, about 23 of
its 37 lines give continuous French (509 of 638 cipher tokens at grade H). Two independent audits found no prior
decipherment or printed plaintext in the Danzay editions and studies, the French, Scottish, English, Danish and Swedish
documentary series, Ribier's *Lettres et mémoires d'estat*, the Cardinal's edited letters, or the solver repositories
(search log in AUDIT.md). The reading is partial, and the letter continues on f.36."

**Unsafe sentence:** "No one has ever read or published this letter." That needs N4 at least, and the Delavaud and
journal gaps below are still open. "First decipherment" is also still barred.

### Source-family log (this audit)

Requests: archive.org 50 (advancedsearch 13, djvu text 38, including 2 errors, and metadata 3, be-api fts 8; the
counts overlap by kind), googleapis.com 33 (key and `country=US`, key never printed, at least 3.2 s apart),
api.openalex.org 1 (answered "daily budget used up for this IP"; stopped), api.crossref.org 4 (1 answered; 3 returned
429 or empty; stopped after one retry), api.archives-ouvertes.fr 2, api.semanticscholar.org 3 (429 twice, one
retry, stopped), persee.fr 3, cryptiana.web.fc2.com 1, github.com 2 anonymous bare clones (deleted), WebSearch 4.
Gallica was not touched.

1. **Delavaud, "Les Français dans le Nord"**, *Bulletin de la Société normande de géographie* XXXIII (1911), pp. 27-99.
   There is also an offprint (Rouen, 1911) with its own pagination: the fr.20140 note is at p. 52 in the Bulletin and
   p. 74 in the offprint. It is not on IA (the series there holds only vols 5, 7 and 12), and no HathiTrust record was
   located through two WebSearch queries restricted to catalog.hathitrust.org. It is on Gallica, series ark
   `cb328704148` (year 1911): **pending, handed to LANE G** (ROOM.md line of this date).
   The Google Books full-text index was searched, since it covers NO_PAGES volumes: 12 queries against both
   printings, `g7MGAAAAMAAJ` (offprint) and `ltSfAAAAMAAJ` (Bulletin 1911). What the snippets show:
   - The fr.20140 reference is a finding-aid sentence: Danzay's letters "datant des années 1557 à 1568, se trouvent à
     la Bibliothèque nationale, dans les ms. 15967 (fo 624) et 20140 (fos 16-56) ...; une adressée au cardinal du
     Bellay dans le ms. 3921 (f° 62) ...". Then comes the Drottningholm copy-book, and the remark that the letters
     "sont d'une lecture très attachante".
   - Every Danzay quotation that surfaces is about commerce, from 1571, 1582, 1583 and 1584.
   - One passage has Danzay reporting words of Henri II to Christian III ("Si je savais que mon ..."). That is not
     this letter, which is addressed to the Cardinal.
   - Zero hits for "janvier 1557", "cardinal de Lorraine" or "Lyon" with Danzay, or for the clear-hand phrases of f.35.
   The Bulletin de la Société des antiquaires de l'Ouest (1919), *Annales de géographie* (1912) and Brunot, *Histoire
   de la langue française* all cite Delavaud for the 1570s-80s commercial material. Delavaud could not have printed a
   reading of the cipher runs, since the manuscript carries no decipherment and Tomokiyo's key dates from 2026. The
   residual risk is that he paraphrases the clear-hand part. The snippet index gives no sign of it.
2. **Cuisiat (ed.), *Lettres du cardinal Charles de Lorraine (1525-1574)*** (Geneva 1998), Google Books
   `o3lbuj7PnuoC` (PARTIAL), 10 queries. The edition is of the Cardinal's **outgoing** letters and calendars no letter
   written to him. The Danzay hit is the summary of **no. 486** (just before no. 487 of 20 June 1558), a letter of the
   Cardinal's that says he "a reçu les lettres du sr. de Danzay et de Sturmius auquel il écrit une réponse ...".
   Note 2 identifies Danzay as "agent diplomatique résidant à Copenhague. Gentilhomme servant du roi sous François
   II". The index entry "Danzay: v. Quissarme" follows Danzay's family name, Quissarme. The "roi de Danemark" entries
   are at letters 631 and 774, and there are 0 hits for "20140". Cuisiat thus attests that Danzay letters reached the
   Cardinal in the first half of 1558, but prints and quotes none. **Searched (snippet level); no print of f.35.**
3. **Ribier, *Lettres et mémoires d'estat*** (Paris 1666), **tome II** (1547-1559): IA `bub_gb_qWTswSr32NYC`,
   identified by its title page ("TOME SECOND"), full djvu text (3.3 MB) grepped. Hits: Danzay, Dançay, Dantzai and
   OCR variants 0; "Dannemarc*" in any spelling 1 (the Magdeburg affair, not 1557); "Augsbourg" 0; "marchans de
   Lyon" 0. Tome I (`bub_gb_Tbs9UbObcPUC` and `bub_gb_bOnmNv2ZLVoC`) was also grepped: Danzay 0. **Does not contain
   the letter.**
4. **Guise papers.** The *Mémoires-journaux* of François de Lorraine, duc de Guise, in the Michaud-Poujoulat
   *Nouvelle collection*, IA `nouvellecollecti06michuoft` (vol. 6), full text: Danzay in any spelling 0.
   "Dannemarc*" appears 15 times, all in news of the Empire, Holstein and Lübeck; none is a despatch from Danzay.
   **Does not contain the letter.**
5. **Danish series**, full djvu text of 30 IA volumes grepped for Danzay, Dancay, Dantzeus, Dantzai and OCR variants.
   `danskemagazin02unkngoog` returned a server error and one Aarsberetninger item a 404.
   - *Kancelliets Brevbøger 1556-1560* (`kancellietsbrevb02denm`): the index's single entry "Dancay, Charles, fransk
     Gesandt" leads to **3 Apr 1559** (Aarhus). There "Carolus Dantzeus, Kongen af Franckeriiges Legat" asks for an
     inheritance grant to a lackey. Nothing for 1557-58. The 1551-55 volume, the other Brevbøger volumes, and Danske
     Magazin 1st-3rd series with Nye danske Magazin (16 vols) give only index or modern references (Bricka,
     Rørdam). The Aarsberetninger fra Geheimearchivet (6 vols) give 0.
   - **Nothing prints a 1557 or 1558 Danzay despatch.**
6. **Swedish, Russian and German print.**
   - Handlingar XI was reached by the first audit and holds no 1557 material.
   - New here: Forsten, *Akty i pis'ma k istorii baltiiskago voprosa* (1889, IA `aktyipismakisto00forsgoog`). It
     prints original French Danzay material from **22 Oct 1563** on (Charles IX to the Elector August) and Danzay
     despatches of the 1560s-70s, none of 1557-58.
   - Forsten, *Baltiiskii vopros* (1893, Google Books full view) quotes Danzay from 24 Nov 1567 on.
   - Sugenheim, *Frankreichs Einfluss* (1845, IA `frankreichseinfl01suge`) cites Danzay for the 1570s-80s from
     Handlingar.
   - None prints f.35.
7. **Tomokiyo**, live page (cryptiana.web.fc2.com/code/danzay.htm, "Last modified on 22 February 2026"), fetched
   today. It still lists f.35 as "27 January 1557 (to Cardinal of Lorraine, not deciphered)" and gives no reading. The
   local mirror agrees.
8. **Solver repositories.** Fresh bare clones of dbourdeau/cyphersolver took all 16 refs, including every PR head
   (`refs/pull/*`), which covers the arya1515 and aryasn2026 forks' PR branches. aaymeloglu/unsolved-ciphers took all
   30 refs. Every ref was grepped for Danzay, Dançay, Dantzai and 20140. Hits: only the 1574 fr.4736 letter (marked
   "Solved" after Ryabov), the fr.2812 1575-1588 calendar, and numeric noise for "20140". **No f.35, no fr.20140
   folio, no 1557.** Clones deleted.
9. **Scholarship, open indexes.**
   - HAL: 2 hits, both by Daussy (2004): "Un diplomate protestant ..." (= Pitou ed., *Élites et notables de l'Ouest*,
     pp. 277-294, OpenEdition 10.4000/154oe, read by the first audit) and "En débattant la religion ... Duplessis-
     Mornay, Languet et Danzay" (1570s-80s).
   - CrossRef: one answered query, which returned Daussy 2004 and Ryabov 2025 (the 1574/1578 cipher); nothing else
     relevant.
   - Persée: 29 results for "Danzay"; the first 10 were read (Mervaud 1986, Vianey 2012/2013 on Jean Sauvage 1586,
     Lesure 1971 review, *Revue d'histoire moderne* 1911 review of Richard, *MEFR* 2006, and others). None concerns 1557
     or the Cardinal. The paging parameter did not work, so 19 were not read.
   - **Unreachable:** OpenAlex (IP daily budget spent), Semantic Scholar (429), and CrossRef after its first answer (429).
   - Google Books adds Daussy in *L'épistolaire au XVIe siècle* (Cahiers V.L. Saulnier 18, 2001, pp. 211-226; Danzay
     at pp. 217, 220), a study of Danzay's letter-writing. It is snippet-only, and the IA copy
     `lpistolaireauxvi0000unse` is lending-only (401). Snippet queries show no 1557 or Cardinal of Lorraine context.
     **Unread in full**: a toward-N4 item.
   - JSTOR: 4 more rows appended to `JSTOR-QUEUE.tsv` (below); no probe was run.
10. **Phrase search on the decoded and clear-hand French.**
    - Google Books, 14 queries: "veulx tenyr", "je ne vous puys encores asseurer", "il me semble qu'il seroyt bon de
      regarder", "comme vous verrez par les lettres du roy" + Danemark, "ce que je doy entreprendre", "l'estat des
      affaires de ce royaulme" + Dannemarch, "marchans de Lion" + Dannemarch, "le Roy de Dannemarch" 1557 Danzay,
      "expres commandement" Danzay, "marchands de Lyon" Danzay, Danzay Augsbourg 1557, Danzay chancelier 1557
      Danemark, and two Delavaud-scoped queries. The only exact hits are Coligny to Gordes (Delaborde 1881) and a 1896
      review, both unrelated. The "exprès commandement" hits are Danzay letters of 1567 and the 1570s-80s.
    - IA be-api fts, 6 queries: "veulx tenyr" gave 3 hits, all the same Coligny-period sentence and unrelated. "ce que
      je doy entreprendre" and "le plus commodement qu il me sera possible" gave 0. "Dannemarch" "marchans de Lion"
      gave 0. "cardinal de Lorraine" Danzay 1557 gave 184 loose hits; the 20 read were followed up. The one Danzay
      lot in the 1835 Techener sale catalogue (`manuscritsetdocu00meco`, lot 279) is a **1575** dossier. Dançay 1557
      "cardinal de Lorraine" gave 15 loose hits, all Richard or Rørdam biography.
11. WebSearch: "Danzay" "20140" 1557 chiffre and one Tomokiyo query. Nothing beyond Wikipedia, Commons, fr.2812, and
    the solver sites already covered.

### What this audit found that the first did not

- **Delavaud is located.** It appeared in the *Bulletin de la Société normande de géographie* XXXIII (1911), with
  two paginations. A copy is on Gallica (`cb328704148`) and on neither IA nor, as far as could be found, HathiTrust.
  Its fr.20140 reference is a finding-aid sentence, and its quotations are 1570s-80s commerce.
- **Cuisiat no. 486** (June 1558) shows the Cardinal acknowledging "les lettres du sr. de Danzay". That is contextual
  support that letters like f.35 reached him. The edition prints no Danzay letter, and its index gives Danzay under
  his family name Quissarme.
- **Ribier tome II was read in full text.** It has no Danzay and no 1557 Danish despatch.
- The Danish chancery registers for 1556-60 hold one Danzay entry, of 1559, and it is unrelated.
- Two Forsten editions print original French Danzay documents, but only from 1563.
- The fork PR branches of the solver repository were grepped too.
- No finding moves the class down.

### Postmortem and corrections

The first audit holds up. Its class, its gaps and its safe sentence were accurate. Its one weak point was describing
Delavaud's "fos 16-56" note in a way that implied he might have studied the 1557 letters. The snippets show a
finding-aid sentence inside a commerce-focused survey. That lowers, but does not remove, the chance that he paraphrased
the clear passages. No over-claiming sentence was found in NOTES.md, reading.txt, reconciliation.md or status.json.
status.json's results row changes from "N3, single audit; second audit pending" to "N3, two audits; N4 pending", and
the card's `next` line is updated to match.

**Still open for N4:**
1. LANE G reads Delavaud 1911 on Gallica, Bulletin pp. 27-99, around pp. 49-55, for any quotation of a 1557 or 1558
   letter to the Cardinal.
2. Daussy 2001 (*L'épistolaire au XVIe siècle*, pp. 211-226), through an IA loan or a library copy.
3. The JSTOR rows.
4. OpenAlex, Semantic Scholar and CrossRef re-queried on another day.
5. Optionally, ask Daussy (the route to N5).

## Toward N4: Daussy 2001, 24 Sept 2026

LANE V worker, 03:58-04:03 UTC, orchestrator session_01B5x2Dshzz71xBzbJqFnXYQ. Brief: close gap 2 above (Daussy,
*L'épistolaire au XVIe siècle*, Cahiers V.-L. Saulnier 18, 2001, pp. 211-226) via IA full-text search, then a
borrow if a term is present or the chapter can't be excluded. No decoding; this section does not assign a class.

**1. Identifier confirmed.** `lpistolaireauxvi0000unse` (`archive.org/metadata/...`): title "L'épistolaire au XVIe
siècle", 262 leaves, `access-restricted-item: true`. An `advancedsearch` query for the title turned up no other IA
copy, so this is the only one.

**2. be-api full-text search (no login), whole item** (chapter-level page boundaries aren't exposed by this
endpoint, so hits below can fall on any of the book's chapters, not just Daussy's pp. 211-226):
- "Danzay": 1 hit, two snippets, both from what reads as the book's index/name list, not a chapter body: "Charles
  de Danzay (deux lettres), ambassadeur de France au Dane[mark]" and "Danzay (Charles de) 217, 220" — the same
  page numbers the first audit's Google Books pass already found (§9). A third snippet, "À un degré moindre, La
  Fontaine, Charles de Danzay et Arnaud du Ferrier, par qui il a été protégé", is a one-clause aside about literary
  patronage, with no date and no addressee named.
- "chancelier": 1 hit, all snippets naming chancelier Guillaume de Rochefort (Louis XI's chancellor, 15th century)
  or chancelier de Cheverny — different people, wrong century, unrelated to this letter's "DAULTRE PART le
  chancelier".
- "cardinal de Lorraine": 1 hit, snippets about Cuisiat's and Dufour's *editions* of the Cardinal's correspondence
  (bibliographic citations), not a quotation of a letter to him.
- "1557": 1 hit, snippets are all publication/composition dates of unrelated works and letters (Budé's *Opera
  omnia* Basel 1557, a Cicero lexicon, a Limoges letter of 5 or 15 Jan./Feb. 1557) — none involves Danzay,
  Denmark or a cardinal.
- "Danois", "Augsbourg", "marchans de Lion": 0 hits each.
- None of the five present-term snippets sits in a context of Denmark, the Cardinal of Lorraine, or a 1557/58
  despatch together; each is independently explainable by a different chapter or the index. This does not by
  itself exclude the Daussy chapter (be-api indexes the whole book, and a short quotation could still fall
  outside these exact strings), but it gives no positive signal either.

**3. Borrow step: found closed before the loan step, not merely obfuscated at the image step.** The no-login
availability check (`archive.org/services/loans/loan/?action=availability&identifier=...`) returns
`is_lendable: false`, `is_printdisabled: true`, `max_borrowable_copies: 0`, `max_browsable_copies: 0`,
`available_to_borrow: false`, `available_to_waitlist: false`. This item is in Internet Archive's print-disabled-only
access tier, not the ordinary controlled-digital-lending tier that `tools/ia_borrow.py` was built and verified
against on 23 Sept 2026 (ASKS.md row 18: a normal loan can be held and returned, but the page images come back
obfuscated for archive.org's own reader and the script correctly refuses to decode them). For this item,
`browse_book` would not even open a loan — the account IA_USER/IA_PASS reaches is not registered as print-disabled,
so this is a harder stop than the obfuscation wall, reached without needing to spend a login or hold a loan. No
change was needed in `tools/ia_borrow.py`: it does not claim to handle the print-disabled tier, and nothing here
shows it should.

**4. HathiTrust and other copies.** A WebSearch restricted to `catalog.hathitrust.org` for the title and series
found no record. `archive.org/advancedsearch` for the title found no second IA copy. No further electronic route
to pp. 211-226 was found this pass.

**Conclusion: gap 2 stays open, and is now stated more precisely.** The chapter is not excluded, and its five
present search terms are all explained by other parts of the book, none in a Denmark/1557/Cardinal-of-Lorraine
context. The only copy on Internet Archive cannot be borrowed by an ordinary account (print-disabled tier only),
so this gap cannot be closed by any of this repository's automated or credentialed routes; it needs a physical or
institutionally-mediated copy (library ILL, or the person's own print-disability access if applicable) — a
REQUEST.md/ASKS.md matter for the person, not a further worker pass with these tools. **N3 unchanged.**

Requests: archive.org 9 (1 metadata, 6 be-api fts, 1 availability, 1 advancedsearch), all ≥2 s apart. WebSearch 1.
No logins attempted (the availability check made login unnecessary), no credentials touched, no loan opened.

## Print check through Gallica page images, 24 Sept 2026

Worker session (Sonnet, cap $10, orchestrator session_014zWyan51u9qMn9gnHpm1Aq), 04:20-04:22 UTC (`date -u`
read at the start of the whole session, 03:59 UTC). Not a verifier session: does not move the N3 class, does
not decode. Brief: item 1 of "Still open for N4" above — read Delavaud, "Les Français dans le Nord", *Bulletin
de la Société normande de géographie* XXXIII (1911), Gallica ark `bpt6k6571713p`, pp. 27-99 (sampled, not
exhaustively), especially the pages around the fr.20140 note, for any quotation of a January 1557/58 Danzay
letter to the Cardinal of Lorraine, against reading.txt. Page images only (`.texteBrut` is altcha-blocked per
CLAUDE.md, not attempted). Full file list and per-page notes in `images/print_check/manifest.json`.

**The fr.20140 note is on p. 74 of this Gallica copy, not p. 52 as the second audit's Google Books snippet
metadata suggested** (that snippet gave "pp. 52/74" for the Bulletin and the offprint; on this copy it is 74,
confirmed by directly reading the page). `tools/gallica_folio.py` shows this is a plainly paginated volume
(canvas = page + 10), so p. 27, pp. 48-56, p. 70, pp. 74-80 and p. 85 were fetched directly. Page 52 itself
(checked first, on the earlier snippet's steer) is mid-way through an unrelated passage on Christophe Richer's
1541-1547 embassy; Danzay is not named there at all — he is first named on **p. 53** ("Son successeur fut
Charles de Danzay, qui devait rester accrédité à Copenhague... pendant plus de quarante ans, de 1548 à 1589").

**Page 74, footnote 3, read directly from the image, transcribes the exact sentence the second audit could
only see as a Google Books snippet:** "Des dépêches inédites de Danzay, datant des années 1557 à 1568, se
trouvent à la Bibliothèque nationale, dans les ms. 15967 (fo 624) et **20140 (fos 16-56)** du fonds français;
une adressée au cardinal du Bellay dans le ms. 3921 (fo 62); deux, de 1570 dans le vol. 397 de la collection
des Cinq-Cents Colbert (fos 135 et 139); six, de 1575 à 1583, dans le vol. 398 de la même collection; une à la
reine-mère (23 novembre 1575) et une au roi (28 février 1578), dans le ms. 2812 du fonds français (fos 26 et
37)." Two things this full sentence adds beyond the snippet: it is a bare finding-aid list of manuscript
locations for a whole run of Danzay dispatches spanning three different registers (15967, 20140, and the
letters named individually), not a description of any one letter's contents; and **Delavaud's own word for
these dispatches is "inédites" — unpublished** — which directly corroborates NOTES.md's and this file's
existing N3 finding, now from the primary page image rather than an API snippet.

**Pages 75-79 read in sequence to check whether the discussion returns to quote the letters after this
citation. It does not, for our target.** P. 75 opens "Les lettres de Danzay sont d'une lecture très
attachante. Elles méritent d'être retenues parmi les plus intéressants documents diplomatiques de l'époque" —
the sentence the second audit already had via snippet — then pivots immediately to a biographical notice
(citing Rördam 1898 and A. Richard's 1910 monograph), not to reading the letters themselves. Pp. 76-77 give
Danzay's biography: entry into royal service c. 1542, first Copenhagen posting from 28 Nov 1548, a second
Copenhagen posting from 1554, and **"En 1557, il recevait de nouvelles lettres de créance; cette fois, qualifié
d'ambassadeur et chargé de résider à titre permanent auprès du roi de Danemark"** — this places our target
letter (27 Jan 1557, addressed as it is mid-transition) exactly at this biographical hinge, but Delavaud gives
no letter content for 1557 itself; the one letter he does quote is a different one, to Christian III, dated
23 May 1553. P. 78 then states plainly: **"Il serait hors de mon sujet de raconter les négociations poursuivies
par Danzay au milieu des complications de la politique de ce temps... Je voudrais insister seulement sur...
le développement du commerce français"** — Delavaud explicitly excludes political/diplomatic letter content
from his own scope, in favour of the commercial history that occupies the rest of the article (confirmed by
p. 79, which opens a new section on Baltic/Russian commerce 1569-1584 and leaves Danzay's letters behind).
**No quotation, paraphrase or content of the 27 January 1557 letter to the Cardinal of Lorraine, or of any of
reading.txt's clear-hand or decoded phrases, was found on any of the seventeen pages read.**

**Net for step 1 of "Still open for N4": closed, as a clean negative rather than an unread snippet.** Delavaud
1911 cites fr.20140 (including our f.35's folio range) only as an unpublished archival holding, explicitly
declines to narrate Danzay's diplomatic correspondence, and quotes no phrase matching our reading anywhere in
the pages checked (27, 48-56, 70, 74-80, 85). This does not by itself raise the class — Cuisiat 1998, JSTOR,
and the open-index re-query (items 2-4 of "Still open for N4") are still outstanding — but it removes the one
concrete, located, previously-unread source this file flagged as a residual risk for the clear-hand passages.

**Requests this session.** gallica.bnf.fr: 19 (17 image fetches, 2 connection resets — pp. 27 and 54 — each
retried once per the single-retry rule and succeeded on retry; 1 manifest fetch, clean). No other host. No
logins, no credentials, no decoding, no subagents, no edits to reading.txt/key.tsv/ciphertext.txt. Images saved
under `images/print_check/` (3.0 MB, well under the 30 MB cap).

**Recommendation (not a class change — this worker does not move the class).** Item 1 of "Still open for N4"
can be marked done. N3 should stay N3; items 2-4 remain for a future worker.

## f.36r, 24 Sept 2026

LANE V verifier, 04:21-04:35 UTC, orchestrator session_01B5x2Dshzz71xBzbJqFnXYQ. This session took no part in the
image, pass, reconciler or solver sessions for f.35 or f.36 and did no decoding. It reuses the two f.35 audits'
source-family logs above and does not repeat them. It searched only what f.36r adds. Claim under audit (NOTES.md "f.36
reading" and "f.36r lines 2-4 reading"): f.36r lines 1-4 read with Tomokiyo's key: 67 cipher tokens, H 37 / M 26 /
U 4. Line 1 reads "avecques le peu de perte pour", line 2 "le change", line 4 "par deça". f.36r is the continuation
of the f.35 letter.

### 1. Same letter or separate item? Same letter (evidence below, read by this session from native_f71/f72 and preview_f69)

| test | f.35 | f.36 | supports |
|---|---|---|---|
| leaf order | f.35r-v | f.36r-v, next leaf in the volume (canvases f69-f72) | one despatch |
| opening / closing | f.35r opens "Monseigneur, le Roy de Dannemarch continue..." with no closing; f.35v is cipher to the last line and has no closing | f.36r has no opening or salutation; it starts in cipher and ends with the closing formula "Monseigneur je me recommande treshumblement a vostre bonne grace...", the dateline and the signature | one letter over two leaves |
| dateline | margin of f.35r, a later docket hand: "27. Jan. 1557" | body of f.36r, the letter's own dateline: "De Coppenhagen ce vingt sept jo[ur] de Janvier 155[7]" (the last digit is a looped form; not checked against other digits in the hand) | same date |
| address and docket | none | f.36v: "Monseigneur / Monseigneur le Cardinal de Lorraine", with a wax seal; docket "[M]r de Danzay du xxvij de Janvier 1557" | f.36v is the outer panel of the folded despatch; addressee agrees with f.35 |
| signature | none | "Dantzay", with "Vostre treshumble et tresobeissant serviteur" | sender agrees |
| hand and cipher | secretary hand; the cipher of Tomokiyo's 1557 table | the same hand, and the same signs (x, T, dia, al, eps, pd, b6, xb, xinf, LRD, iii, xA, x88). The f.35 codes fit every f.36 glyph but `I`, `x8`, `ww`, `ringT`, and `I`, `x8`, `ringT` are f.35 codes too | same cipher |
| content bridge | V29 ends "... car du [xk]" | 36R1 begins "avecques le peu de perte pour le change" | **not read**: `xk` is unkeyed, so the textual join stays M, as the reconciler graded it |

The physical, diplomatic and cipher evidence is H. Only the sense across the f.35v/f.36r join is unread. That the
"change" run continues f.35v's passage on the Augsburg and Lyon merchants is an inference (grade I). It does not
bear on whether this is one letter. **f.36r is classified as part of the f.35 letter, not as a separate item.**

Correction this adds to section 2 above: the place is not "not stated": the letter is dated at Copenhagen
("Coppenhagen") in its own hand on f.36r. The dateline is in the body, not only in a margin.

### 2. What f.36r adds, and the search of it

New to this audit: one place name (Coppenhagen). No new person: "le Roy de Dannemarch" was already searched. No sum.
Cipher-derived phrases: "avecques le peu de perte pour le change" and "par deça". Clear-hand phrases this session read
from the image (lines 2-15): "en telle sorte vous serez asseuré de faire", "toutes les foys qu'il vous plairoyt, ou
je feray tout le debvoyr et diligence qui sera possible, et seray tres marry si je ne puys satisfaire au commandement
qui me sera faict", "Je vous supplye tres humblement Monseigneur qu'il vous plaise de vostre grace m'excuser si j'ay
faict ou obmis chose en cest endroyt qui vous desplaise, car jusques a present je n'ay eu le moyen ne pouvoir de
mieulx faire", "vous me trouverez tousjours tresfidelle et tresobeissant serviteur", and the closing and dateline.
These are courtesy formulas. The substantive new content is the exchange-loss clause, and it is partly unread.

| family | searched | result |
|---|---|---|
| Danzay editions and studies, French series, Scottish series, Danish/Swedish/Finnish regesta (the IA copies the f.35 audits used: Richard `undiplomatepoite00richuoft`, `ngociationslet00pari`, Michaud-Poujoulat `nouvellecollecti06michuoft`, Teulet `relationspoliti06/07teulgoog`, `frankreichseinfl01suge`, Forsten `aktyipismakisto00forsgoog`, `kancellietsbrevb02denm`, `danskemagazin02unkngoog`, `regestadiplomat04copegoog`, `manuscritsetdocu00meco`) | the 11 phrases in `phrases_f36.txt`, exact and proximity match on the djvu text (tools/print_check.py) | no hits |
| IA full text, all items (be-api) | same 11 phrases | no hits |
| Google Books (key, country=US) | same 11 phrases | no hits, except the stock formula "tresfidelle et tresobeissant serviteur" (Marlborough dispatches, La Bruyère, Notes and Queries), which is irrelevant |
| CrossRef | "Danzay Danemark 1557"; "Danzay Copenhague cardinal de Lorraine" | Daussy 2004 (already read by the first audit); Cardinal of Lorraine reference entries; nothing on this letter |
| HAL | "Danzay" | 2 hits, both Daussy 2004, already logged in the second audit |
| OpenAlex | the phrases | **unreachable**: HTTP 429 on the first call; host stopped, not retried |
| Semantic Scholar | "Danzay Denmark ambassador" | **unreachable**: HTTP 429; not retried |
| Web search | Danzay "Coppenhagen" 1557 cardinal de Lorraine; "Danzay" "27 janvier 1557" / "vingt sept jour de janvier 1557" | nothing on this letter (Cuisiat reviews and general pages only) |
| Solver repositories (shallow clones, grep for danzay, dantzay, copenhag, coppenhag, fr. 20140; deleted after) | cyphersolver, unsolved-ciphers | only Tomokiyo's other Danzay letter (fr.4736 f.87, Copenhagen 14 Oct 1574, marked solved), a different item. Nothing for 1557 |
| Ribier, Guise/Lorraine papers (Cuisiat), CSP Foreign and Scotland 1557 | no new searchable name; the f.35 audits' negatives cover the letter as a whole; the new phrases went through the IA/Google Books full text above | not repeated |
| JSTOR | no row added: the f.35 rows (JSTOR-QUEUE.tsv) already query the letter by sender, recipient and date, which covers f.36r | queued, not blocking |

Files: `phrases_f36.txt`, `sources_f36.tsv`, `print-check-f36.tsv`, `print-check-f36-hosts.tsv`. For this run,
tools/print_check.py gained a `--delay` option (default 1.5 s) so that the brief's 3 s spacing could be kept; its
offline test passes.

### 3. Grade check (rule 4)

- Every H and M token on f.36r is keyed through a key.tsv row that cites a cell of Tomokiyo's 1557 table
  (`sources/cryptiana/web/danzay_1557.png`). Four U tokens: `I`, `x8`, `ww`, `ringT`. No C, no S. No reading comes
  from a contemporary decipherment, and there is no control. Per rule 4 the f.36r reading is a key application of
  Tomokiyo's reconstruction, not a cryptanalytic result of ours.
- **`h9` checked against his drawing.** In column h, row 1, the image has a 9/g-shape with a tail that curls back
  to the left. The key.tsv entry describes it correctly and cites the cell. The f.36r glyph (36R2 pos 4, checked by
  this session at 3x) is a 9-shape whose stem flicks left at the foot. It is nearer to h row 1 than to d row 1 (a 9
  with a straight stem). The context "c[h]ange" fits. Grade M is right.
- `decode.py --check` exits 0 (run this session).
- **Count corrected.** Lines 2-4 are H 22 / M 18 / U 2, and 9 of the 40 H+M tokens are nulls: 5 at H (iii x2, xA
  x2, x88) and 4 at M (loop x2, xN, xA at R4 pos 14). The reconciler's "H 22 (9 null)" and "H 37 (10 nulls)" put
  the M nulls under H. Correct: all of f.36r H 37 (6 nulls) / M 26 (4 nulls) / U 4. Fixed in NOTES.md.
- **Caveat on the clear words, not an error.** Tomokiyo's table lists candidate null *words* ("bien du est il? ou
  / par quand?"), and his page says plaintext words can serve as nulls in these letters. So "quand" (36R3), "de" and
  the two "fust" set among cipher runs may be nulls. The reconciler's joined sentence ("... pour le change fust. Et
  en telle sorte ...") treats them as text. That sentence is already marked as inference, and it stays that way.

### 4. Classification

| item | prior plaintext | prior decipherment | level |
|---|---|---|---|
| fr.20140 f.36r, lines 1-4 (cipher) and the clear close, as the end of the f.35 letter (Danzay to the Cardinal of Lorraine, Copenhagen, 27 Jan 1557) | not located | none: the leaf carries none, and Tomokiyo lists f.35 as "not deciphered" | **N3**, one audit of f.36r, resting on the two f.35 audits for the letter as a whole |

Not N4, for the gaps still open on f.35: Daussy 2001, JSTOR, and OpenAlex and Semantic Scholar, which rate-limited
again today. Delavaud 1911 is now read on Gallica page images and gives a clean negative (the section "Print check
through Gallica page images" above). His note cites fr.20140 fos 16-56, which covers f.36, as "dépêches inédites", and
he quotes no 1557 letter. Evidence quality: good for IA and Google Books phrase search, weak for
scholarship indexes. Confidence that no printed decipherment of f.36r exists: high, because none exists for f.35 and
the cipher on f.36r is the same letter's.

**Safe sentence:** "The letter continues on f.36r (dated Copenhagen, 27 Jan 1557, signed Dantzay, addressed on f.36v
to the Cardinal of Lorraine). Its four cipher lines, read with Tomokiyo's key, give 37 of 67 tokens at grade H (6 of
them nulls). 'avecques le peu de perte pour le change' and 'par deça' are readable, and three stretches and the
join with f.35v are not. No printed decipherment or plaintext of the leaf was located (search log in AUDIT.md)."

**Unsafe sentence:** "f.36 completes the decipherment of the letter." Three stretches of f.36r and the f.35v/f.36r
bridge (`xk`) are unread, and about 14 f.35 lines are not continuous French. "First" or "previously unread"
wording is still barred (N3).

### 5. Postmortem

No novelty over-claim found in NOTES.md, reading_f36.txt, ciphertext_f36.tsv or status.json. Three factual slips
were corrected in NOTES.md. (a) The "f.36 images" section called the date "marginal". It is the body dateline, and
it names Copenhagen. (b) The null counts put 4 M nulls under H. (c) A clear-word null caveat was added to the
joined sentence. status.json's Danzay results row now names f.36 at the same class.

Requests: archive.org 11 (djvu), be-api.us.archive.org 11, www.googleapis.com 11 (key and country=US, key never
printed), api.crossref.org 2, api.openalex.org 1 (429, stopped), api.archives-ouvertes.fr 1,
api.semanticscholar.org 1 (429, stopped), WebSearch 2, github.com 4 anonymous shallow clones (2 repositories,
cloned twice because the first grep was too broad). All archive.org and googleapis calls were at least 3 s apart.
No Gallica, no logins, no subagents.

## N4 decision, 24 Sept 2026

LANE V verifier, 04:45-04:56 UTC, orchestrator session_01B5x2Dshzz71xBzbJqFnXYQ. This session did none of the
solving, auditing or gap work above and did no decoding. Question: does the logged coverage of the f.35r-36r letter
(Danzay to the Cardinal of Lorraine, Copenhagen, 27 Jan 1557) now meet rule 10's N4?

**Answer: no. The class stays N3.** Two principal families are still uncovered: Daussy 2015, a specialist study of
Danzay that no earlier section logs, and DECODE. Each takes one short session. Daussy 2001 (ASKS row 26) does
**not** block N4. It is a chapter on Duplessis-Mornay's correspondence, not on Danzay's.

### 1. Principal families: covered or not

| family | covered? | where logged |
|---|---|---|
| Danzay's printed dispatches: *Correspondance de Charles Dantzai* (Handlingar XI, 1824); Bricka 1901 | covered | first audit 3(a) |
| Danzay studies: Richard 1910; Rørdam 1897/98 and *Hist. Saml.* II | covered | first audit 3(c) |
| Delavaud 1911 | covered, from page images. His p. 74 n. 3 calls fr.20140 fos 16-56 "dépêches inédites", p. 78 declines to narrate the negotiations, and he quotes no 1557 letter | "Print check through Gallica page images" |
| Daussy 2004 (PUR) | covered, full text | first audit 3(g) |
| Daussy 2001 (*L'épistolaire au XVIe siècle*, pp. 211-226) | ruled out by its subject (this section, 3). Not a principal source for this letter | this section; "Toward N4: Daussy 2001" |
| **Daussy 2015**, "Un diplomate huguenot au service de la couronne de France: Charles de Danzay, ambassadeur au Danemark (1548-1589)", *Religiya. Tserkov'. Obshchestvo* 4 (St Petersburg), pp. 264-281, doi 10.24411/2308-0698-2015-00013, in French, open access (CC BY 4.0) | **not covered**. Only the abstract was read, from the Wayback capture of the article page (20250316). The PDF's Wayback lookup returned 504 and connection resets, so that host was stopped. rcs-almanac.ru is not on this session's host list | this section, 2 |
| Ryabov 2020 (the 1568 *Discours*), 2024 (Frederick II to Charles IX), 2025 *QR* (the 1574/1578 cipher), 2025 *VID* (a letter to Henry III) | covered at abstract level, and ruled out by date: none can concern January 1557. Frederick II reigned from 1559 and Henry III from 1574 | this section, 2; first audit 3(d) |
| Cardinal of Lorraine's letters, Cuisiat 1998 | covered at snippet level, 10 + 11 queries. The only Danzay hit is the summary of no. 486 (received 25 June 1558), "a reçu les lettres du sr. de Danzay". The edition calendars outgoing letters only | second audit 2; this section, 2 |
| Ribier II (1547-1559), I | covered, full text | second audit 3 |
| Guise *Mémoires-journaux*; L. Paris 1841; Teulet 1851/1862 | covered | second audit 4; first audit 3(c) |
| Danish regesta and state papers: *Regesta diplomatica* 2nd ser.; *Kancelliets Brevbøger* 1551-60; Danske Magazin; Aarsberetninger | covered | first audit 3(c); second audit 5 |
| Swedish series: Handlingar (all 16 IA vols) | covered. Svenska riksregistraturet and Gustav I's registratur were not searched. An outgoing French despatch to Paris reaches Swedish print only through the Drottningholm copy-book, and that copy-book is Handlingar XI | first audit 3(a) |
| CSP Foreign, Mary 1553-58 | covered, full text | first audit 3(b) |
| CSP Scotland vol. 1 (Bain 1898, 1547-63) | **covered in this section**: IA `calendarstatepa00baingoog`, full djvu text, 50 lines with 1557, 0 hits for Danzay/Dansay/Dançay/Dantz* (the only "Dantz" hits are "Dantzic" ships) | this section, 2 |
| BnF catalogue of fr.20140 (`cc51725m`) | covered: no bibliography, no edition | first audit 3(d) |
| Tomokiyo, "Danzay's Ciphers" | covered, live and mirror. f.35 is "not deciphered", and no reading is printed | first audit 3(d); second audit 7 |
| Solver repositories, incl. PR heads | covered | second audit 8; f.36r section |
| **DECODE (de-crypt.org)** | **not covered**. It was unreachable in both audits (login blocked). The login has worked since 04:40 UTC today, but de-crypt.org is not on this session's host list | first audit 3(f) |
| Open indexes | covered: CrossRef and HAL (several passes), Persée (29 hits, 10 read), Semantic Scholar (answered once this session, 9 hits, all listed in 2), Google Scholar via WebSearch. OpenAlex has been 429 at every attempt today, this session's included | open-index pass; second audit 9; this section |
| JSTOR | 8 rows queued (16-19, 23-26). Under the verifier template, a queued row does not block N4 on its own | JSTOR-QUEUE.tsv |
| Phrase search on decoded and clear-hand French (f.35 and f.36r) | covered: IA, Google Books, print_check | second audit 10; f.36r section |

### 2. What this session searched (one pass)

- **Semantic Scholar** answered one query ("Danzay"): 9 papers. They are Ryabov 2025 *QR* (the cipher of 1574/1578),
  Ryabov 2025 *Vspomogatel'nye ist. distsipliny* (a letter to Henry III, so 1574 or later), Ryabov 2020 (the 1568
  *Discours*), **Daussy 2015** (above), Daussy 2004, Daussy 2003 (*Siècles*, Duplessis-Mornay, Languet and Danzay
  against the theologians, 1570s-80s), Ryabov 2024 ×2 (the Franco-Swedish alliance 1572-75, and Frederick II's
  letters to Charles IX), and Ryabov 2022 (Sigismund II Augustus to Charles IX). Two follow-up calls for abstracts
  got 429, one of them after a 40 s pause, so the host was stopped. CrossRef then gave the abstracts of Ryabov 2020,
  2024 and 2025 *QR*. All are dated by their subject to 1559 or later.
- **Daussy 2015.** The article page (via the Wayback Machine) gives the abstract. The article is based on "la
  correspondance de Danzay conservée dans les archives danoises" and covers his Huguenot turn, negotiations with
  Protestant princes, Henry of Navarre, Duplessis-Mornay, a French protectorate in Livonia, and trade with Moscow.
  Nothing in the abstract points to the BnF volume or to 1557. Its title, subject and length (18 pp.) mirror
  Daussy 2004 (18 pp.). Daussy 2004 was read in full and mentions 1557 only in the Laetus dedication. That the 2015
  article is a version of the 2004 chapter is an inference (grade I), not a finding. Because the article is the
  newest specialist study and is open access, it should be read before N4.
- **Cuisiat 1998**, Google Books API, 11 queries. Six were volume-restricted (`intitle:`, for Dansay, Danzay, Dantzay,
  Danemark 1557, Dannemarc and Copenhague) and all returned 0 matches. Five were free queries: only "Danzay
  Sturmius cardinal" hit the volume (`o3lbuj7PnuoC`), again no. 486, "Reçue le 25 juin", n. 2 "Charles Quissarme,
  sr. de Danzay". The other hits were *Lettres de Henri III* (Danzay at Cracow, 1574), Eneroth 1924 and Richard
  1910, none of them the letter. **Nothing new. Cuisiat prints no Danzay letter.**
- **Daussy 2001**, IA be-api fts on `lpistolaireauxvi0000unse`, 10 more terms: Coppenhagen 0, Copenhague 0,
  Dannemarch 0, **Danemark 0**, Quissarme 0, 20140 0. "Christian" gave only humanist grammarians (Hegendorff,
  Vladeracken). "Lorraine" gave the index and bibliographic mentions of Cuisiat's edition. "chiffre" gave
  Duplessis-Mornay's cipher and a Maledent letter. "deux lettres" gave Maledent's two partly enciphered Latin letters
  (another chapter). Google Books gives the chapter's title: **"La correspondance de Philippe Duplessis-Mornay:
  inventaire et typologie"** (cited so in *Montaigne Studies* 2006 and *Servir Dieu, le Roi et l'État* 2006).
- **CSP Scotland vol. 1**: see the table.
- WebSearch, 2 queries: they located Daussy 2015 and found nothing else.

### 3. Does Daussy 2001 block N4? No.

The chapter is an inventory of **Duplessis-Mornay's** correspondence. Danzay appears in it on two pages (index
"Danzay (Charles de) 217, 220") and in a list of correspondents, "Charles de Danzay (deux lettres)". These are
letters exchanged with Duplessis-Mornay, who was born in 1549, and they belong to the 1570s-80s, like Daussy 2003. A
chapter on Duplessis-Mornay cannot print or quote a 1557 despatch to the Cardinal of Lorraine. Full-text search of
the book finds no "Danemark", "Dannemarch", "Copenhague" or "Coppenhagen" anywhere in it. **It is not a principal
source for this letter.** Recommendation for ASKS row 26: close it as not needed for N4, with no ILL request. The
owner decides.

### 4. Decision

**N3 stays.** For N4, rule 10 requires the principal editions, catalogues and project pages to be covered. Every
edition, calendar, catalogue and regesta series in the table is covered. Two families are not:
1. **Daussy 2015** (open access). It is the most recent specialist study of Danzay, based on his correspondence, and
   has not been read. One fetch of the PDF (`rcs-almanac.ru/wp-content/uploads/2017/09/2015_досси.pdf`), then a grep
   for 1557/1558, Lorraine, 20140, "Bibliothèque nationale" and the clear-hand phrases, closes it. rcs-almanac.ru is
   not on this session's host list, so the orchestrator should assign it to a worker whose brief names that host.
2. **DECODE**. It is a named status source (CLAUDE.md convention 1) and was never reached. The login works as of
   04:40 UTC today. One search of DECODE for Danzay / fr.20140 / BnF français 20140 closes it.

If both come back negative, the next verifier can assign N4 without repeating anything else. OpenAlex (never
reached today) and the 8 JSTOR rows should be logged as unreachable or queued; neither blocks N4 on its own. Nothing
found here lowers the class.

**Safe sentence (N3, current):** "BnF fr.20140 f.35r-36r (Charles de Danzay to the Cardinal of Lorraine, Copenhagen,
27 Jan 1557) carries no contemporary decipherment. Read with the key Tomokiyo reconstructed and published in 2026,
509 of 638 cipher tokens on f.35 and 37 of 67 on f.36r are at grade H, and the reading is partial. Three audits found
no prior decipherment or printed plaintext in the Danzay editions and studies, the Cardinal's edited letters,
Ribier, the French, Scottish, English, Danish and Swedish documentary series, Tomokiyo's pages or the solver
repositories (search log in AUDIT.md)."

**Sentence for N4 only, not to be used until the two gaps close:** "No prior decipherment located of Danzay's
letter to the Cardinal of Lorraine of 27 Jan 1557 (BnF fr.20140 f.35-36), read here with Tomokiyo's published key;
the reading is partial."

**Unsafe sentence:** "The first decipherment of a previously unread Danzay letter." The class is N3. The key is
Tomokiyo's, so this is a key application of his reconstruction. The reading is partial: about 14 f.35 lines are not
continuous French, and the f.35v/f.36r join is unread.

### 5. Outreach gates (CLAUDE.md Outreach 1-6)

| gate | state |
|---|---|
| 1. verifier class in AUDIT.md | **met** (N3) |
| 2. above N1: second adversarial audit, open-index pass, Google Books, JSTOR rows answered or waived by the owner | second audit **met**; open-index pass **met** apart from OpenAlex (unreachable, logged); Google Books **met**; JSTOR rows 16-19 and 23-26 **not met** (queued, neither answered nor waived) |
| 3. message is the safe sentence, states its prior print (Tomokiyo's key page), links AUDIT.md | **not met**: no draft exists |
| 4. rule 10 wording | only the N3 safe sentence above may be used; no "first", no "no prior decipherment located" |
| 5. logged in CONTRIBUTIONS.md before sending | **not met** |
| 6. verifiable links (repo folder; Gallica `btv1b52521512h` canvases f69-f72; Tomokiyo's key page, the only print the reading rests on) | links available; **not met** until a draft carries them |

**Postmortem.** No over-claim was found. The one error in the chain was a mislabel: every earlier section and ASKS
row 26 called Daussy 2001 "a study of Danzay's letter-writing". Its title shows it is Duplessis-Mornay's
correspondence. That cost a borrow attempt and an owner ask. Before an unread item gets an ASKS row, look up the
chapter's own title. The real specialist gap, Daussy 2015, was missed because OpenAlex and Semantic Scholar were 429
in every earlier pass, and CrossRef does not index that journal under the query used.

Requests: be-api.us.archive.org 10, archive.org 2 (advancedsearch 1, djvu 1), web.archive.org 6 (CDX 1 reset + 1 ok;
page 1 TLS failure + 1 ok; PDF CDX 1 reset + 1 504, then stopped), www.googleapis.com 17 (key and country=US, never
printed, ≥3.3 s apart), api.openalex.org 1 (429), api.semanticscholar.org 3 (1 ok, 2× 429, stopped),
api.crossref.org 5, WebSearch 2. No Gallica, no logins, no decoding, no subagents.

## Toward N4: Daussy 2015, 24 Sept 2026

Closing the first of the two gaps the N4 decision above named: Hugues Daussy, "Un diplomate huguenot au service de
la couronne de France: Charles de Danzay, ambassadeur au Danemark (1548-1589)", *Religiya. Tserkov'. Obshchestvo*
4 (St Petersburg, 2015), pp. 264-281, doi 10.24411/2308-0698-2015-00013, CC BY 4.0.

**DOI note.** `doi.org/10.24411/2308-0698-2015-00013` 302-redirects to
`cyberleninka.ru/article/n/sud-o-darovanii-prav-i-problema-svetskoy-i-tserkovnoy-yurisdiktsii-angliyskogo-monarha-v-period-reformatsii/pdf`
-- an unrelated article ("The Court of Delegates and the problem of secular and ecclesiastical jurisdiction of the
English monarch during the Reformation"), not Daussy's. The DOI as printed in the brief and in this repo does not
resolve to the article it names; whoever cites it next should use the direct URL below, not the DOI. Found the
correct article instead by WebSearch (`rcs-almanac.ru/en/daussy-2015-en/`, confirmed by title, author, journal,
volume and page range against the DOAJ record and the CyberLeninka mirror at
`cyberleninka.ru/article/n/un-diplomate-huguenot-au-service-de-la-couronne-de-france-charles-de-danzay-ambassadeur-au-danemark-1548-1589`).

**Fetch.** The article page's own `?format=pdf` link gives only a 3-page cover sheet (title, abstract, keywords --
no body text). The full 30-page PDF (18 printed pages, pp. 264-281, plus front matter and endnotes) is linked from
the same page as `rcs-almanac.ru/wp-content/uploads/2017/09/2015_досси.pdf`; fetched once, 391127 bytes, saved to
`sources/articles/daussy2015_full.pdf` with `sources/articles/daussy2015_full.txt` (pdftotext -layout). Licence CC
BY 4.0 per the article page. Manifest: url `https://rcs-almanac.ru/wp-content/uploads/2017/09/2015_%D0%B4%D0%BE%D1%81%D1%81%D0%B8.pdf`,
fetched 24 Sept 2026, 391127 bytes, CC BY 4.0.

**Read.** Full body text and all footnotes/bibliography read (not just grepped). Grepped for `1557|1558|Lorraine|
20140|cardinal|chiffr|déchiffr|bibliotheque nationale`, then read every hit in context, plus a second grep for
`augsbourg|augusta|marchan|lyon|chancelier` (terms from `reading.txt`/`reading_f36.txt`).

- **"Lorraine" appears zero times in the article.** The only cardinal named anywhere in the text is Jean Du Bellay,
  in a footnote citing a *different* 1547 letter (BnF Fds. fr. 3921, fol. 62) -- a different manuscript, a different
  addressee, ten years before our letter.
- **"20140" and "fr.20140"/"Français 20140" appear zero times.** The article's only BnF archival citations are
  Pièces originales 974 "Danzay" fol. 1, Fds. fr. 6619 fol. 142-151v° (a 1575 *Discours* to Pinart), and Fds. fr.
  3921 fol. 62 (the 1547 letter above). None is fr.20140.
- **No "chiffre"/"déchiffr-" anywhere; no decipherment, cipher or code is mentioned in the article at all.**
- The two other 1557 hits are unrelated to the letter: (1) Danzay was granted the office of *panetier de l'Hôtel
  du roi* on 20 May 1557 (a court-appointment record, sourced to Rördam, not to any letter); (2) the Danish
  historian-poet Erasmus Laetus dedicated a Latin religious poem to Danzay in 1557 (manuscript, sourced to Rördam
  pp. 11-12) -- this is the same Laetus dedication already found in Daussy 2004 (NOTES.md "Check-solved"), which
  confirms this session's earlier inference that the 2015 article is a version of the 2004 chapter: same content,
  same citations, same absence of the 1557 letter to the Cardinal of Lorraine.
- The article states plainly that its own sources are patchy for Danzay's first twenty years: "compte tenu du
  caractère très lacunaire des sources rassemblées pour les vingt premières années [de] son ambassade, ce n'est
  que pour la période qui s'ouvre en 1567 que le déroulement de la mission de Danzay est bien connu" (p. [267] of
  the printed text) -- 1557 falls inside the span the author says is thin.
- **Bibliography and footnote citations (25 numbered works + 3 BnF archival items), checked against NOTES.md/
  AUDIT.md for what earlier sessions already covered:** Wicquefort 1690, Catherine de Médicis' *Lettres*, Daussy's
  own *Le parti huguenot* (2014) and *Les huguenots et le roi* (2002), Bricka 1901, the *Correspondance de Charles
  Dantzai* (1824, Handlingar XI), Richard 1910, Rördam 1897/98, Vindry 1903, Champion 1943, the two CSP Elizabeth
  Foreign volumes (1583-85), Théodore de Bèze's *Correspondance*, Duplessis-Mornay's *Mémoires* -- **all already
  read or ruled out by the first and second audits** (table above, "Danzay's printed dispatches" / "Danzay
  studies" rows). Four titles are new to this repo's search log and were not chased further, since none is a
  principal source under rule 10 (general secondary histories with no sign of citing fr.20140 or a 1557
  decipherment): Dollinger, *La Hanse XIIe-XVIIe siècles* (1988); Kirby, *Northern Europe in the Early Modern
  Period* (1990); Kirchner, *Commercial relations between Russia and Europe 1400-1800* (1966); Nicollier, *Hubert
  Languet* (1995). Listed here for the record, not pursued.

**Verdict: gap closed negative.** Daussy 2015 is a version of Daussy 2004 (already read in full by an earlier
audit): same citations, same content, same silence on BnF fr.20140 and on any 1557 letter to the Cardinal of
Lorraine. Read in full, it names no prior plaintext or decipherment of this letter. This does not by itself
raise the class; it closes the one of the two named N4 gaps that this brief covers. The other named gap (a DECODE
search for Danzay/fr.20140, assigned to LANE N) is untouched here.

Requests: doi.org 1, rcs-almanac.ru 3 (page HTML, cover-sheet PDF, full-text PDF; all ≥1.5 s apart), cyberleninka.ru
0 (found via WebSearch snippet, not fetched), WebSearch 1. No Gallica, no logins, no decoding, no class change.

## DECODE search, 24 Sept 2026

LANE N DECODE worker B (Sonnet), 06:51-07:20 UTC (`date -u` read) [N4-final verifier, 24 Sept 2026: the end time cannot be right; this
section was committed at 06:52:29 UTC (5c8b113) and the clock read 06:54 when it was audited]. Closes the "DECODE" row of the N4 decision
table above (04:45 UTC). This session did no decoding, no class change, no promotion. Same session as the
Gramont DECODE search (`ciphers/fr2980-gramont/AUDIT.md`, "DECODE search, 24 Sept 2026" — see there for the
method note on the RecordsSearch → RecordsList GET pattern and the "No records found" boilerplate-text bug
found and fixed in this session's own search script).

### Queries and results

All `LIKE` (substring) searches on `RecordsList`, no login, no `x_status`/`x_record_type` restriction (all
statuses and record types included by default).

| field | term | hits (ids) |
|---|---|---|
| sender | Danzay | 0 |
| sender | Dantzay | 0 |
| receiver | Danzay | 0 |
| receiver | Dantzay | 0 |
| c_holder | Danzay | 0 |
| c_holder | 20140 | 0 |
| additional_information | Danzay | 0 |
| additional_information | Dantzay | 0 |
| additional_information | 20140 | 0 |
| origin_city | Copenha(gen) | 2: 8858, 8869 |
| receiver | Lorraine | 2: 7952, 9444 |
| sender | Lorraine | 4: 3733, 4194, 4218, 9449 |
| origin_city | Denmark | 0 |
| origin_region | Denmark | 2: 5139, 7854 |

`20140` also covers "fr. 20140" and "Français 20140" as LIKE substrings, so those spellings were not queried
separately. "Copenhagen" was queried as the substring "Copenha" to also catch "Coppenhagen" (the letter's own
spelling, "De Coppenhagen ce vingt sept jo de Janvier 1557") and "Copenhague"; the grid returned 2 rows either
way. [N4-final verifier, 24 Sept 2026: "Copenha" is not a substring of "Coppenhagen" (double p), so that spelling
was not covered; nor were Dançay, Dancay or Dansay, or a 1556-1558 date range. Not decisive: the c_holder "20140"
and receiver "Lorraine" queries would catch a record of this letter under any spelling of the sender.]

### What the hits are

- **ids 8858, 8869** (origin_city contains "Copenha"): both London, British Library, Add MS 32284 (f.89-92 and
  f.113-116), a 19th-century Key/Cipher record — id 8869's own date field reads "1837 -", plaintext language
  "Danish?", region "Paris, Copenhagen". Three centuries too late and the wrong archive (BL Add MS 32284, not
  BnF fr.20140); not Danzay.
- **ids 7952, 9444, 9449** (Lorraine as sender or receiver): BnF Lorraine 377 f.95 (shelfmark literally named
  "Lorraine", unrelated house), and BnF Français 3621 nos.22/97 (1591-92, "François II, Count of Vaudémont" /
  "France Nancy") — the Lorraine ducal house at the end of the century, not the Cardinal of Lorraine (Charles
  de Guise, d. 1574) that Danzay wrote to in 1557. Wrong Lorraine, wrong decade.
- **ids 3733, 4194, 4218** (sender contains "Lorraine"): BnF Français 3995 f.32 (1587) and Français 3980
  f.10/f.61 (1591, "Soissons") — again the later Lorraine-Guise-Soissons correspondence of the Wars of
  Religion, not 1557.
- **ids 5139, 7854** (origin_region "Denmark"): both Dresden, Saxon State Archive, Jakob Heinrich von Flemming's
  keys with the Danish court (1700-1728, 1715-1716) — 150+ years too late, different archive, different
  diplomat.

**No record for BnF Français 20140, and no record for Charles de Danzay (any spelling) as sender or receiver,
in any field searched.** This matches the search log already on file: Tomokiyo's "Danzay's Ciphers" page (first
audit 3(d)) calls f.35 "not deciphered" with no DECODE record cited, and neither the Aymeloglu cache (grepped
this session, zero rows for danzay/dantzay/20140) nor Bourdeau's repository (fresh shallow clone this session,
zero file or catalogue hits for the same terms; one unrelated 1574 "Danzay to Henry III (1574) Solved" line in
`napoleon/unsolved.txt`, a different, later Danzay letter, not fr.20140) carries this shelfmark either.

### Requests this session (de-crypt.org)

~14 `RecordsList` GET queries for this target (table above), sharing the session's RecordsSearch page fetch and
browser-submission check already logged under the Gramont search. All ≥1.6 s apart, one request at a time, UA
`cipher-lab research script (contact via repository)`. No login, no credentials touched, no images or documents
fetched.

**DECODE family in the N4 table above: now covered, no hit.** Daussy 2015 was already closed negative (05:11
UTC, "Toward N4: Daussy 2015" below). Both principal families the 04:45 N4 decision named are now closed; a
fresh N4-decision verifier can act on this without further search. This worker does not assign N4 (not its
brief).

## N4 decision (final families), 24 Sept 2026

LANE V verifier (N4 decision), 06:53-06:58 UTC, orchestrator session_01B5x2Dshzz71xBzbJqFnXYQ. This session did none of
the solving, auditing, gap or DECODE work above and did no decoding. Question: now that Daussy 2015 and DECODE are
logged, does the f.35r-36r letter (Danzay to the Cardinal of Lorraine, Copenhagen, 27 Jan 1557) reach N4?

**Answer: no, it stays N3. One principal family named in CLAUDE.md convention 1 has never been searched: the comment
threads on Tomokiyo's own posts. The Cryptiana Discussion Forum (cryptiana.blogspot.com) carries a post announcing
"Danzay's Ciphers: Ciphers of a French Diplomat with a Long Tenure", which reports the 1557 ciphers, and no section
of this file or NOTES.md reads that post or its comments.** The 04:45 table missed the family. Both gaps it named
are now closed negative.

### 1. The 04:45 principal-families table, re-checked

| family | 04:45 state | now | where |
|---|---|---|---|
| Daussy 2015 | not covered | **covered, negative**. Read in full: no Lorraine, no 20140, no cipher; a version of Daussy 2004 | "Toward N4: Daussy 2015" |
| DECODE | not covered | **covered, negative** (method checked in section 2 below) | "DECODE search" |
| All other rows (editions, Danzay studies, Delavaud, Cuisiat, Ribier, Guise, Teulet, L. Paris, Danish regesta and Brevbøger 1551-60, Handlingar, CSP Foreign and Scotland, BnF `cc51725m`, Tomokiyo's page, solver repos, open indexes, JSTOR queued, phrase search) | covered | unchanged; re-read against their sections and they hold | sections above |

**Families checked for omission (the brief's list and this session's own):**

| family | state | note |
|---|---|---|
| Cuisiat 1998, *Lettres du cardinal Charles de Lorraine* | covered at snippet level (21 queries, two passes) | edition of outgoing letters. The only Danzay hit is no. 486 (June 1558), "a reçu les lettres du sr. de Danzay". Snippet-level is enough for an edition that by its design cannot print an incoming letter; its notes were searched through the same index |
| Ribier, *Lettres et mémoires d'estat* I-II | covered, full text | second audit 3 |
| Danish *Kancelliets Brevbøger* | covered, 1551-55 and 1556-60 | second audit 5 |
| CSP Foreign, Mary 1553-58 | covered, full text | first audit 3(b) |
| Tomokiyo, "Danzay's Ciphers" (web page) | covered, live (last modified 22 Feb 2026) and mirror: f.35 "not deciphered" | second audit 7 |
| **Cryptiana Discussion Forum: the "Danzay's Ciphers" announcement post and its comments** | **not covered: blocks N4** | See below. The local mirror (`sources/cryptiana/blog/`, 15 posts and the front page as of 19 Sept 2026) holds no Danzay post; the byte hits for "20140"/"danz" in `index.html` are base64 noise in image URLs. WebSearch (3 queries this session) confirms that the post exists and summarises it. The results also list a "September 2025" archive page, which was not opened. The comments could not be read: cryptiana.blogspot.com is not on this session's host list |
| Cipherbrain (Schmeh) and other list-post threads | searched by WebSearch restricted to scienceblogs.de and cipherbrain.net ("Danzay"): no Danzay post. The hits were a 2018 post on a Henri II cipher device (not Danzay; a checking query confirmed it) and unrelated posts. No post, so no thread to read | this section |
| BnF catalogue record for fr.20140 | covered (`cc51725m`: no bibliography, no edition) | first audit 3(d) |
| Guise-affinity scholarship (Durot 2012, Carroll 1998) and other quotations of fr.20140 | Google Books, 6 queries this session: `"fr. 20140" 1557` (1 hit, a 1918 Army List, noise), `"20140" Danzay "cardinal de Lorraine"` 0, `"Dançay" 1557 "cardinal de Lorraine"` 0, `Durot Guise "20140"` 0, `"Danzay" "janvier 1557"` 2 (Richard 1910 and its *Mém. Soc. antiquaires de l'Ouest* printing: his father's estate, already covered), `"Dancay" 1557 Copenhague cardinal` 0 | not a principal family. Logged for completeness; negative |
| CSP Venetian 1556-57; Krag and Stephanius, *Christian III* | not searched | not principal. A Venetian calendar or a Danish royal history would not print a French resident's despatch to the Cardinal. Listed so the next session need not rediscover them |

### 2. The DECODE method: is its "none" from the corrected counter? Yes.

- The bug: every `RecordsList` page contains "No records found" as empty-state boilerplate, so counting that string
  reported every query as 0. The fix counts `RecordsView/<id>` links.
- The Danzay table itself shows the corrected counter in use. It reports non-zero hits with record ids for four of its
  14 queries (Copenha 2: 8858, 8869; receiver Lorraine 2; sender Lorraine 4; origin_region Denmark 2), and the ids are
  identified in "What the hits are". The broken counter could not have produced any of these, so the zeros in the same
  table (sender, receiver, c_holder and additional_information for Danzay/Dantzay/20140) come from the corrected method.
- Independent offline check this session: `sources/decode/records-non-decrypted-2026-09-24.tsv` (1,186 Non-decrypted
  and Partially decrypted records, LANE N census) has no row for 20140, Danzay in any spelling, Copenhagen or
  Coppenhagen. Its only 1557-58 rows are BL, Venice and TNA items.
- Weaknesses, recorded as bracketed corrections in the DECODE section: (a) "Copenha" does not match "Coppenhagen";
  (b) Dançay, Dancay and Dansay were not queried, nor was a 1556-58 date range; (c) the section's time span "06:51-07:20
  UTC" ends after its own commit (06:52:29), so its end time is wrong (rule 6); (d) no query script and no raw
  responses were committed, so the zeros can be re-run but not re-checked from disk. None of these is decisive. A DECODE
  record of this letter would carry "20140" in c_holder, and "Lorraine" in receiver, whatever the sender's spelling.
  Both queries were run with the corrected counter. **DECODE family: covered, negative.**

### 3. Decision

**N3 stays. Exactly one thing blocks N4:** read the Cryptiana Discussion Forum post that announces "Danzay's Ciphers"
(and the "September 2025" archive page WebSearch lists), together with every comment on it, and look for any reading,
partial decipherment or key application of the 27 Jan 1557 letter (fr.20140 f.35-36) by Tomokiyo or a commenter. The
host is cryptiana.blogspot.com, plus its Blogger comment feed if the post page does not render comments. Allow a few
requests in a brief that names the host. The prior for a hit is low: Tomokiyo's page, last modified 22 Feb 2026 and
fetched live today, still says "not deciphered", and a commenter's reading would normally have reached that page. But
convention 1 names this family, the post is the one place a reader of the 1557 key would report trying it, and it
costs one short session. If the thread is negative, the next verifier can assign N4 without repeating anything else.

Not blocking, optional: a DECODE top-up (Dançay, Dancay, Coppenh, start year 1556-1558) in any later LANE N session
that is already on that host; OpenAlex (429 every time today); the 8 JSTOR rows.

Nothing found here lowers the class, and no over-claim was found in NOTES.md, reading.txt, reading_f36.txt or
status.json. The N3 safe sentence of "N4 decision, 24 Sept 2026" (section 4) stands. So does the sentence reserved
for N4, which is not to be used until the forum thread is read. For the next verifier, the N4 wording to use then,
with the recovery credit made explicit:

> "No prior decipherment located of Charles de Danzay's letter to the Cardinal of Lorraine, Copenhagen, 27 Jan 1557
> (BnF fr.20140 f.35-36), which carries no contemporary decipherment. It was read here by applying the key
> S. Tomokiyo reconstructed and published in 2026 (cryptiana, "Danzay's Ciphers") from the sibling decipherments of
> f.16, f.24 and f.30: on f.35, 509 of 638 cipher tokens are at grade H, and on f.36r, 37 of 67. The reading is
> partial. Search log in AUDIT.md."

Unsafe, then and now: "The first decipherment of a previously unread Danzay letter." Such a sentence claims novelty
without the qualifier, credits the result to us rather than to Tomokiyo's key (this is a recovery by key
application), and hides that the reading is partial: about 14 f.35 lines are not continuous French, and the
f.35v/f.36r join is unread.

### 4. Outreach gates (CLAUDE.md Outreach 1-6), as of 06:58 UTC

| gate | state |
|---|---|
| 1. verifier class in AUDIT.md | **met** (N3) |
| 2. second adversarial audit; open-index pass; Google Books; JSTOR rows answered or waived | second audit **met**; open-index pass **met** except OpenAlex (unreachable, logged); Google Books **met**; JSTOR **not met**: all **8** Danzay rows (JSTOR-QUEUE.tsv 16-19, 23-26) are `queued`, none answered or waived by the owner |
| 3. safe sentence, prior print stated (Tomokiyo's key page), AUDIT.md linked | **not met**: no draft (outside this brief) |
| 4. rule 10 wording | **met for the N3 sentence only**. "No prior decipherment located" may not be used until N4 |
| 5. logged in CONTRIBUTIONS.md before sending | **not met** |
| 6. verifiable links (repo folder; Gallica `btv1b52521512h` canvases f69-f72; Tomokiyo's danzay.htm) | links exist; **not met** until a draft carries them |

**Postmortem.** Each N4 decision so far has been built from the families that earlier audits happened to search,
rather than from convention 1's fixed list. The 04:45 table covered editions, calendars and scholarship thoroughly,
but it skipped convention 1's fourth source (the list-post comment threads) because no earlier section had named it.
Lesson for the verifier template: start the principal-families table from convention 1's six sources in order, and
then add the target-specific editions.

Requests this session: www.googleapis.com 6 (key and country=US, key never printed, 3.5 s apart); WebSearch 5. No
other host. No Gallica, no de-crypt.org, no logins, no decoding, no subagents.

## Toward N4: Cryptiana forum thread, 24 Sept 2026

LANE V gap worker (Sonnet), ~07:22-07:30 UTC, orchestrator session_01B5x2Dshzz71xBzbJqFnXYQ. Closes the one gap
the "N4 decision (final families)" section above named: the Cryptiana Discussion Forum post and its comments. Did
not decode, did not touch any other target, does not assign a class (that is a fresh verifier's task).

**Finding the post.** Blogger's own JSON search feed (`https://cryptiana.blogspot.com/feeds/posts/default?alt=json&q=Danzay`)
returns exactly one entry, `openSearch$totalResults` = 1: "Reconstruction of a Cipher used by Charles de Danzay,
French Ambassador to Denmark", posted 22/02/2026, at
`https://cryptiana.blogspot.com/2026/02/reconstruction-of-cipher-used-by.html` (post id 2892705715433739646, blog
id 5107039156280592857). A second feed query for `q=20140` returns zero results. An independent WebSearch
`site:cryptiana.blogspot.com Danzay` agreed on the same post and additionally listed
`https://cryptiana.blogspot.com/2025/09/` (a monthly archive index page); fetched and grepped case-insensitively
for `danz`, it has no hits at all -- a search-snippet false positive (most likely matched on an unrelated word
elsewhere on that month's archive), not a second Danzay post. No other candidate post exists on this blog.

**Reading the post.** Fetched once (`sources/cryptiana/blog/2026_02_reconstruction-of-cipher-used-by.html`, 85129
bytes). Full text of the post, quoted in full since it is short:

> "A letter from Danzay, French ambassador to Denmark, to Henry III (1574) includes a undeciphered paragraph,
> which has been on my list of unsolved ciphers here. It may have been too short to solve analytically, but Sergey
> Ryabov succeeded in reconstructing the cipher by finding another letter (1578) with decipherment in the margin.
> Now I updated the record.
>
> To me, Danzay is interesting because of his unparallelled long tenure from 1548 to 1589. Comparison of ciphers
> used during his career may shed light on practices of French cryptography at the time. For the time, I found one
> from 1557.
>
> I uploaded a new article "Danzay's Ciphers: Ciphers of a French Diplomat with a Long Tenure" to report Danzay's
> ciphers from 1574-1578 and 1557."
> -- posted by cryptiana, 2/22/2026

Nothing in the post itself names f.35, f.36, 27 January 1557, Copenhagen, or the Cardinal of Lorraine, and nothing
in it states or implies that the 1557 letter (as opposed to the 1557 cipher table) was read. The post's only
function is to announce the danzay.htm article -- the very page the 24 Sept 2026 "N4 decision" table already
logged as "covered, live... f.35 'not deciphered'" (section 1 of that decision, row "Tomokiyo, 'Danzay's Ciphers'
(web page)"). The "letter... 1574... Sergey Ryabov... 1578" passage concerns the separate, already-solved 1574/1578
Danzay cipher (Cryptiana's unsolved-ciphers list entry, closed by Ryabov's find), not the 1557 correspondence at
all -- it is not a second unresolved claim about f.35.

**Comments.** The post's own rendered page reads "No comments:" beneath the post body. The Blogger comment feed
(`https://cryptiana.blogspot.com/feeds/2892705715433739646/comments/default?alt=json`, saved as
`sources/cryptiana/blog/2026_02_reconstruction-of-cipher-used-by.comments.json`) confirms this independently:
`openSearch$totalResults` = 0, zero `entry` elements. There is no comment thread to read.

**Verdict: gap closed negative.** The post exists, was read in full, and has zero comments. It contains nothing
beyond a pointer to the key page already logged (which itself still says f.35 is "not deciphered") and an
unrelated note about the separate 1574/1578 letter pair. No reading, partial decipherment, or key application of
the 27 Jan 1557 letter (fr.20140 f.35-36) by Tomokiyo or any commenter was found. This does not raise the class by
itself; it closes the one family the 24 Sept 2026 "N4 decision" table left open. A fresh verifier session should
now be able to re-run the section-4 outreach-gate table (JSTOR rows still outstanding) and, if satisfied, move the
target to N4 using the sentence already drafted in that section.

Requests this session: cryptiana.blogspot.com 5 (Blogger JSON feed x2 -- `q=Danzay`, `q=20140` -- the post page,
the comments feed, and the archive page, all >=1.5 s apart), WebSearch 1. No other host, no login, no decoding,
no subagents.

## N4 decision (Cryptiana closed), 24 Sept 2026

LANE V N4-decision verifier (Opus), 07:50-07:55 UTC, for the LANE V orchestrator. This session did none of the solving,
auditing, gap, DECODE or forum work above and did no decoding. Question: now that the Cryptiana forum thread has been
read ("Toward N4: Cryptiana forum thread"), does the f.35r-36r letter (Danzay to the Cardinal of Lorraine, Copenhagen,
27 Jan 1557) reach N4?

**Answer: yes. N4 (no prior decipherment located).**

### 1. Was the Cryptiana search sound? Yes.

Checked offline against the files the gap worker saved (`sources/cryptiana/blog/2026_02_reconstruction-of-cipher-used-by.html`
and `.comments.json`), not re-fetched:
- **Feed query.** Blogger's `feeds/posts/default?q=` is the blog's own full-text post search. `q=Danzay` gave 1 post and
  `q=20140` gave 0. WebSearch `site:` found the same single post. The extra `2025/09/` archive hit was opened and grepped:
  0 `danz`. Any later post on the 1557 letter would contain "Danzay", so the feed query covers it. It would not catch a
  post that spells the name only "Dançay" or "Dantzay". The prior for that is negligible, because Tomokiyo spells it
  "Danzay" throughout his page and post.
- **Post read in full.** The saved page's `post-body entry-content` text matches the quotation in that section word for
  word. The saved page has no `20140`, `Lorraine`, `Copenh` or `janvier`. Its two `1557` hits are both in the quoted
  body ("I found one from 1557"; "Danzay's ciphers from 1574-1578 and 1557").
- **Comments, two ways.** The rendered page shows the literal `No comments:` and has no `comment-thread` or
  `comment-block` element. The comment feed JSON has `openSearch$totalResults` = "0" and no `entry` key. Both agree.

The section's one interpretive claim also holds: the post announces the key page already covered, which still says
f.35 is "not deciphered".

### 2. Final-families table re-read adversarially, from convention 1's six sources in order

| convention 1 source | state |
|---|---|
| 1. name in a search engine | covered (WebSearch in every audit; 3 more queries this session, Russian) |
| 2. sender's printed Lettres/Correspondance on IA | covered (Handlingar XI *Correspondance de Charles Dantzai*; Bricka 1901) |
| 3. calendars and state-paper series | covered (CSP Foreign Mary, CSP Scotland I, Ribier, Danish regesta, Kancelliets Brevbøger 1551-60, Handlingar). CSP Venetian was not searched; it is not principal, as logged |
| 4. list-post comment threads (Cryptiana, Cipherbrain) | covered, negative (the Cryptiana section above; Cipherbrain has no Danzay post) |
| 5. DECODE | covered, negative ("DECODE search"; method re-checked in "final families" section 2) |
| 6. solver repositories | covered, including PR heads |
| + recipient's edition (Cuisiat 1998) | covered; it prints outgoing letters only |
| + Danzay specialists (Richard, Rørdam, Delavaud, Daussy 2001/2004/2015, Ryabov) | covered; Ryabov topped up this session (below) |
| + open indexes, Google Books, phrase search | covered; OpenAlex unreachable today (logged); JSTOR queued |

**The one principal family the table under-covered: Ryabov's newest work.** He is the one active specialist on Danzay's
ciphers. Semantic Scholar was last asked at 04:45, and nobody checked for anything newer or for his dissertation. This
session ran one logged pass:
- **CrossRef, 5 queries** (author Ryabov with Danzay; "Данзе"; "Danzay cipher 1557"; author Ryabov from 2025-06; author
  Ryabov with France/Denmark/Valois/cipher/Lorraine from 2025). The Danzay or Valois items it found were: Ryabov 2025
  *Quaestio Rossica* (the 1574/1578 cipher, already logged), Ryabov 2025 *VID* (a letter to Henry III, already logged),
  Ryabov 2020 (the 1568 *Discours*, already logged), and one item not in this file, **Ryabov 2026** (20 Aug 2026),
  "The Image of the Valois Monarchy in Protestant Writings during the First Interregnum in the Polish-Lithuanian
  Commonwealth", doi 10.15826/b978-5-7996-4204-4.17. That paper is about 1573-74, so its date rules it out. Every other
  Ryabov hit is a different person (mathematics, medicine, forestry).
- **WebSearch, 3 queries** (Russian). They found the UrFU and press reports of his 2025 decipherment, which name only
  the letters of 14 Oct 1574 and 28 Feb 1577 to Henry III. They also found **his dissertation** at the UrFU
  dissertation council (`dissovet2.urfu.ru`, "Рябов_Диссертация.pdf") and the related monograph proposal
  (naukapublishers.ru 2025, "Russian-French contacts of the second half of the 16th century"). Two independent search
  summaries give its declared scope as **Russian-French contacts in northern Europe, 1558-1581**, meaning diplomatic,
  dynastic and economic contacts.
- **Ruling:** the dissertation is excluded by scope and date, like Daussy 2001 above. A January 1557 Franco-Danish
  despatch to the Cardinal falls outside 1558-1581 and outside Russian affairs. Independently, the enciphered text of
  f.35 has no contemporary decipherment. No 1557 key was published before Tomokiyo's of 22 Feb 2026, and Ryabov's own
  reconstruction is the 1574/1578 cipher. So nobody could have printed a reading of the cipher runs before February
  2026, except by re-solving the cipher, which none of his work reports. **Limitation:** the PDF itself was not opened,
  because its host is not on this session's list. The scope comes from search summaries and is graded I, not read.
  Suggestion, not a gate: before any outreach, the drafting worker fetches the PDF once and greps for `20140`, `1557`,
  `Лотаринг`, `Lorraine`. A hit reopens the class. [Closed 24 Sept 2026 by V3b: the PDF (239 pp.) was fetched and grepped; 0 hits for `20140`, no quotation of the letter; see "Second opinion SO-DANZAY-F35".]

Nothing found lowers the class.

### 3. Decision: N4

Every source in convention 1 and every principal edition, calendar, catalogue, specialist study and project page is
covered and negative. Rule 10's N4 is met: N3, with the principal editions, catalogues and project pages covered.
Internal or unpublished work is not excluded. Unread items that remain: Ryabov's dissertation PDF (excluded by scope,
see above), OpenAlex (unreachable) and the 8 JSTOR rows (queued). None of them blocks N4 under the verifier template.

**Safe sentence (N4):**

> "No prior decipherment located of Charles de Danzay's letter to the Cardinal of Lorraine, Copenhagen, 27 Jan 1557
> (BnF fr.20140 f.35-36), which carries no contemporary decipherment. It was read here by applying the key
> S. Tomokiyo reconstructed and published in 2026 (Cryptiana, "Danzay's Ciphers") from the sibling decipherments of
> f.16, f.24 and f.30, so the result is a key application (a recovery), credited to his reconstruction: on f.35, 509
> of 638 cipher tokens are at grade H [61 of them nulls, so 448 H signs carry text; V3b, 24 Sept 2026], and on f.36r, 37 of 67. The reading is partial. Search log in AUDIT.md."

**Unsafe sentence:** "We have produced the first decipherment of a previously unread Danzay letter." It uses
"first" and "previously unread" without the qualifier. It credits the result to us, not to Tomokiyo's key. It hides
that the reading is partial: about 14 f.35 lines are not continuous French, 70 signs are unkeyed, and the f.35v/f.36r
join is unread. It also implies a check of unpublished work that N4 does not include.

### 4. Outreach gates (CLAUDE.md Outreach 1-6), as of 07:55 UTC

| gate | state |
|---|---|
| 1. verifier class in AUDIT.md | **met** (N4) |
| 2. second adversarial audit; open-index pass; Google Books; JSTOR rows answered or waived | second audit **met**; open-index pass **met** except OpenAlex (unreachable, logged); Google Books **met**; JSTOR **not met**: **8** Danzay rows open (JSTOR-QUEUE.tsv lines 16-19, 23-26, all `queued`) |
| 3. safe sentence, prior print stated (Tomokiyo's danzay.htm), AUDIT.md linked | not met: no draft yet (drafting step, outside this brief) |
| 4. rule 10 wording | **met**: the N4 sentence above, with the qualifier |
| 5. logged in CONTRIBUTIONS.md before sending | not met: drafting step |
| 6. verifiable links (repo folder; Gallica `btv1b52521512h` canvases f69-f72; Tomokiyo's danzay.htm) | links exist; not met until a draft carries them |

Gates 3, 5 and 6 are met when the note is drafted, as they were for Gramont. The only gate that is not a drafting step
is gate 2's JSTOR rows, so ASKS row 33 goes to the owner in the same shape as row 32.

**Postmortem.** No over-claim was found. status.json's grade now reads "N4 (no prior decipherment located)". Its
"line" field already uses only search-result wording. The final-families section was right to add convention 1's list
to the table, but it still skipped a check that every specialist named in the table has no newer work. Ryabov publishes
on Danzay every year, and he had a 2026 item and a dissertation that no section logged. Neither mattered this time,
but a verifier should re-query each named specialist's newest output (CrossRef by author, from the year of the last
check) before assigning N4.

Requests this session: api.crossref.org 6 (≥1.5 s apart), WebSearch 3. No other host: no Gallica, no de-crypt.org, no
cryptiana (its files were read from disk), no logins, no decoding, no subagents.

## Second opinion SO-DANZAY-F35 (ChatGPT, pull request 3), checked 24 Sept 2026 16:28 UTC

LANE V4 verifier V3b (Opus, session_01J653u9mXgcT3gwBenQP5kh). The outside answer (GPT-6 via Codex, branch
`second-opinion/SO-DANZAY-F35`, copied to `second-opinions/chatgpt-2026-09-24.md`) reports **no prior print and no prior
decipherment of f.35**. It offers no citation that prints, quotes or calendars the letter. Its main challenge is to the
logic of the exclusions: a dissertation's stated scope does not prove it leaves out 1557. This session tested that
challenge on the one specialist text it applies to, Ryabov's dissertation. The text was fetched and read, and it has
no hit. **Class stays N4 (no prior decipherment located).**

| # | claim | verdict | what was done / correction |
|---|---|---|---|
| 1 | No same-letter printing established; own search limited | right (a search result, weaker than this file's log) | none needed |
| 2 | Cuisiat 1998 prints mainly outgoing letters; Margolin's review in *RBPH* 78/3-4 (2000), pp.1076-1077, Persée | right | Persée page fetched once: Margolin, *RBPH* t.78 fasc.3-4, pp.1076-1077, reviewing Cuisiat (Droz 1998, 711 pp., 1279 letters, the Cardinal's letters). This agrees with the "final families" row ("prints outgoing letters only"). WorldCat OCLC 645897230 was not fetched |
| 3 | A title's date range cannot exclude a retrospective quotation; the scope-based exclusion of the 1558-1581 dissertation needs qualifying | right in principle; **now tested, negative** | Ryabov's dissertation (`dissovet2.urfu.ru`, "Рябов_Диссертация.pdf", 239 pp., 3.5 MB) was fetched once and its text extracted. There are 0 hits for `20140`. The 1557 hits are context only: the Danish-Swedish tension of 1557 "quickly reached the French court" (p.48, n.180 cites a 1561 Catherine de Médicis letter), Noailles in England 1557, Nepeya 1557, and bibliography dates. It quotes no Danzay letter of 1557 and names no letter to the Cardinal of Lorraine. The phrases `depesche`, `royaulme`, `marchans`, `commodement` and `Augsbourg` all give 0 hits (one hit for the 1555 Augsburg peace). The Danzay manuscripts it cites are fr.15966, 17832, 3324, 3224, 3304 and 2812, none of them fr.20140. The AUDIT limitation "PDF not opened" is closed in place |
| 4 | The Handlingar volume correction (IX to XI) should be kept | right | already in section 3 (`handlingarrrand02scangoog`, vol. XI) |
| 5 | Ryabov 2025, *Quaestio Rossica* 13/4, pp.1487-1508, doi 10.15826/qr.2025.4.1034, treats letters of 14 Oct 1574 and 28 Feb 1578, not 1557 | right | CrossRef record fetched: title, volume, issue and pages match. The abstract names the letters "dated 14 October 1574, and 28 February 1578". This agrees with section 3(d) and the N4 table. Page images not inspected (not needed for the class) |
| 6 | Tomokiyo's danzay.htm could not be reached live | unverifiable here | not re-fetched. The repo's snapshot and earlier sections stand |
| 7 | The royal word sign sits inside ordinary words (V5, V11-12, V28 "Augsbourg") | right, **already recorded** | NOTES.md "Reading with Tomokiyo's key", item 3 (LRD reads r/R in V5, V11, V26, V28). The reading is unchanged. A one-line suggestion was added to NOTES.md |
| 8 | T and hk are ambiguous in the key; the header resolves them to a/u | right, already recorded | reading.txt header line 2; NOTES.md items on `hk` (u in "Augsbourg", a in "Danoys a") |
| 9 | Tomokiyo's candidate null words (bien, du, ou, par, quand) mean clear words inside runs may be nulls | right, already recorded | NOTES.md verifier bracket and suggestion (Tomokiyo's list "bien du est il? ou / par quand?") |
| 10 | f.36r has been partly read, so the prompt and the opening audit statements are stale | right for AUDIT.md's opening, **wrong for the prompt** | The prompt says only that the letter "continues on f.36", which is true. AUDIT.md lines 7 and 25 (the original N3 claim line and safe sentence) are annotated in place as superseded. The NOTES.md header still read N3 and now reads N4, following "N4 decision (Cryptiana closed)" |
| 11 | "No marginal decipherment and a late public key" do not prove nobody re-solved the cipher independently | right in logic; the class already allows for it | N4 excludes printed and project work only, and says so: "internal or unpublished work not excluded". The N4 text itself frames this as a condition ("except by re-solving the cipher, which none of his work reports"). Nothing in print found such a re-solution |
| 12 | Keep 27 Jan 1557 as written; the year style (1557/1558 n.s.) is unresolved | right | already handled: the body dateline and the docket both read 1557 (NOTES.md f.36 section). The second audit notes "possibly 1558 n.s.". Unchanged |
| 13 | The 509 H include 61 nulls, so 448 H tokens carry text | right (arithmetic) | the qualifier is added in brackets to the N4 safe sentence. status.json's line was not edited (no class change; the brief limits status.json edits to a class change) |
| 14 | Leads: Delavaud and Richard for fr.20140 references; Ryabov's full text; Cuisiat's notes; collate f.35 with the sibling decipherments; the Danish and Swedish editions' appendices | covered, or now closed | Delavaud: "Print check through Gallica page images" (negative, pp.27, 48-56, 70, 74-80, 85). Richard: the second audit and N4 tables. Ryabov: closed this session. Cuisiat: 21 snippet queries, notes included. Collation: a reading task for a solver, not novelty. Danish and Swedish editions: section 3 (full OCR grepped) |

**Did the second opinion find a prior print or decipherment?** No. **Class:** f.35-36r stays **N4** (no prior
decipherment located). The safe sentence is the one in "N4 decision (Cryptiana closed)", with the nulls qualifier.

**Postmortem.** The one real gap the outside reader named was a limitation this file already logged: Ryabov's
dissertation, excluded only by its stated scope. It is now closed by reading the text. The lesson repeats the Ryabov
postmortem above: when a limitation says "not opened, because the host is not on this session's list", the next
verifier with that host free should open it, not carry the limitation forward.

Requests this session for this label: api.crossref.org 1, www.persee.fr 1, dissovet2.urfu.ru 1, WebSearch 1.


## JSTOR (owner's machine, 24 Sept 2026)

Recorded by the JSTOR runner on the owner's machine (logged-in JSTOR account, built-in browser, one search per queue row, 6 s apart, no block page). First-page hits for every row are in `JSTOR-QUEUE.tsv`; only the hits that could print, calendar or discuss the letter were opened. No class is changed here; the verifier moves it.

Rows 16-19, 23-26 answered (9 queries). Two hits opened:

- Petit-Dutaillis and Hauser, "Histoire de France" (bulletin historique), *Revue Historique* 105/2 (1910), pp. 353-397, https://www.jstor.org/stable/40943205 (read online). The Danzay passage (pp. 375-376) is Hauser's notice of Alfred Richard, *Un diplomate poitevin au XVIe siècle: Charles de Danzay* (Poitiers 1910), which he says prints one letter in appendix (Danzay to Catherine de Médicis, 25 Dec 1566); a footnote reads the initials on the Concorde treaty as "Carolus Quissarme Danzaeus Aquitanus" and refers to Bricka's *Indberetninger*. Nothing on 1557, the Cardinal of Lorraine or a cipher. Richard 1910 and Bricka 1901 are already covered in section 3.
- "Inventaire des pièces manuscrites de la collection Godefroy", *Annuaire-Bulletin de la Société de l'histoire de France* 3/2 (1865), pp. 4-239, https://www.jstor.org/stable/23401625 (open access). The only Danzay entry found is item 34 of a Sillery bundle (p. 110): Isaac Maillet to the king, undated (1593?), on the affairs of Danzay "mort ambassadeur en Danemark". The viewer's own search returned nothing for "Danzay" or "Dansay", so this rests on the pages the viewer loaded, not on a full read of the 236 pages. No 1557 piece seen.

The other first-page hits (Baudouin-Matuszek 1989 on d'Oisel, Jensen 1974, Jeannin 1956, Zeller 1956, Gaffarel 1879, Pelus-Kaplan 2013) are context, not prints of the letter.
- READ row 69, 24 Sept 2026: Henri Hauser, "Histoire de France" (Bulletin historique, époque moderne jusqu'à 1660), *Revue Historique* 142/2 (1923), pp. 233-256, https://www.jstor.org/stable/40944190 (read online). In-viewer search: "Danzay" 1 hit, "Lorraine" 0, "chiffre" only as numerals, "1557" only the Spanish bankruptcy of 1557 in the same notice. The one Danzay passage is footnote 3 on p. 238, in the notice of Lucien Romier, *Le Royaume de Catherine de Médicis* (Paris 1922): Hauser repeats the remark he had made in *Revue historique* 80, p. 333, that the Danzay correspondence edited by Bricka should have been cited beside Richard's monograph. Nothing on 1557, the Cardinal of Lorraine, fr. 20140 or a cipher; the bulletin neither prints, calendars nor discusses the letter.

## Outreach gate 2: JSTOR family and open indexes (verifier V5, 24 Sept 2026)

Verifier V5 (Opus, for LANE V4, session_01UBQ2tN51FBuKTx41RqnGAK), 24 Sept 2026 17:24 UTC. Triage of the JSTOR runner's first-page hits (JSTOR-QUEUE.tsv) by title, snippet and what the runner read; no decoding, no class change unless stated.

9 rows (file lines 16-19, 23-26), 2 candidates read by the runner (Hauser 1910 bulletin, stable/40943205; Godefroy inventory 1865, stable/23401625), both negative for the 1557 letter. One candidate not opened: **Hauser, 'Histoire de France (bulletin)', Revue Historique 1923, stable/40944190**, returned by 'Danzay AND 1557 AND (chiffre OR cipher)': a 1923 bulletin matching all three terms may notice a publication on Danzay's early dispatches. Listed `to read (owner's machine)` and queued as a READ row. Context only: Baudouin-Matuszek 1989 (d'Oisel), Jensen 1974, Gaffarel 1879, Jeannin 1956, Zeller 1956, Pelus-Kaplan 2013, Annales de Géographie 1912 bibliography.

**The Richard 1910 lead (checked).** Alfred Richard, *Un diplomate poitevin du XVIe siècle: Charles de Danzay, ambassadeur de France en Danemark* (Poitiers 1910), Internet Archive `undiplomatepoite00richuoft` (University of Toronto copy), full-text OCR fetched once (532 kB, 9,642 lines) and grepped for 1557, Lorraine, cardinal, chiffre, 20140, appendice and every 'Bibl. Nat.' citation. Result: the **Appendice (p.238) prints one letter only, Danzay to Catherine de Médicis, Copenhagen 25 Dec 1566** (bought by Richard from the Clouzot catalogue), as Hauser said. The **Sommaire** has no item on 1557; the narrative of 'les premières années de sa mission' (pp.42-44) passes from the 1553 mission to 1559 without the Cardinal of Lorraine or a 1557 dispatch; p.39 says only that Danzay is found in Paris in 1557 (after Rørdam, *Résidents* pp.11-12). The Cardinal of Lorraine appears once, in a later chapter (as the uncle of a bride in the 1570s narrative), no letter to him is cited, and the BnF manuscripts cited are Clairambault 333, fr. 2812, 3304, 3931 and 17832, **not fr. 20140**. 'Chiffre' occurs once for a cipher (a Danish courtier designated 'n° 167' in a letter to Bourdin of 27 June 1566). Richard neither prints, calendars nor discusses the 27 Jan 1557 letter. **No reclass: N4 stands.** OCR caveat: the OCR is fair, so a mangled '20140' cannot be excluded by grep alone, but the table, the appendix and the 1553-1559 pages were read directly. Host: archive.org 2 requests.

JSTOR family: searched on the owner's machine 24 Sept 2026, 9 rows, 2 candidates read, result negative; 1 candidate (Hauser 1923, stable/40944190) still to read. Gate 2's JSTOR condition is **not yet met** (one READ row). Richard 1910 read: negative.

Open indexes: OpenAlex (`api.openalex.org/works?search=...`) and Semantic Scholar (`/graph/v1/paper/search`) retried once each from the cloud at about 17:21 UTC: both HTTP 429 (shared free daily budget used up). The owner's run of 24 Sept 2026 (ASKS 34) covered Thurloe, Eckert and Blathwayt only; this target's queries are owed (ASKS row 44, `outreach/openalex-s2-owner-queries-2.md`).

Outward drafts written this session (status drafted, nothing sent): see `outreach/` and CONTRIBUTIONS.md.

## Ryabov 2025, read in full (verifier V6, 24 Sept 2026)

Verifier V6 (Opus, for LANE V4, session_0135A8C45WsmXm6gYxJQz5cP), 24 Sept 2026 17:57 UTC. The parent put the Tomokiyo
draft on hold at 17:54 after OpenAlex returned this article. Sections 3(d) and 3(e) had judged it from its abstract only.
No decoding was done.

**Item.** Sergey M. Ryabov, "Secrets of the Foreign Policy of the Last Valois in Northern Europe: The Diplomatic Cipher of
Charles de Danzay", *Quaestio Rossica* 13/4 (2025), pp. 1487-1508, doi 10.15826/qr.2025.4.1034, open access. The article
page at qr.urfu.ru/ojs/index.php/qr/article/view/qr.1034 and the PDF galley (22 pp., 530 kB) were fetched once to scratch,
not to the repository. The text was extracted and grepped for 20140, 1557, Lorraine, cardinal, Tomokiyo and every "BnF",
"fol." and 155x/156x date, and the body (pp. 1487-1496), the table (Appendix 1, pp. 1496-1498) and the headers of Appendices
2-3 were read. The article is in English, not Russian as the brief expected; only the reference list is transliterated.
Host: qr.urfu.ru, 3 requests (article page, galley, PDF; doi.org 1 redirect). elar.urfu.ru was not needed.

| Question | Answer (page) |
|---|---|
| Which Danzay letters | Two only, to Henri III: Copenhagen **14 Oct 1574**, BnF fr.4736 ff.86-88, and Copenhagen **28 Feb 1578**, BnF fr.2812 ff.44-46 (pp. 1489-1490, 1492). It also mentions a plaintext dispatch of 26 Jan 1576 (Cinq cents de Colbert 398 f.123; n.5). |
| Key or table printed | Yes. Appendix 1 is a reconstructed homophonic table: 5 signs for a, 3 for e, 3 for l, 4 for m, 4 for q; cc, ée, nn, rr; la, il, qui, que, pour; two nomenclators (Roy de Dannemarch, Roy de Suède); three signs for "space or null" (pp. 1493, 1496-1498). It is built from the contemporary marginal decipherment on the 1578 letter and checked against the 1574 letter (p. 1492). |
| Decipherment printed | Yes, for those two letters: an English translation of the 1574 cipher passage (p. 1494) and the full Middle French texts of both letters (Appendices 2-3). |
| fr.20140, f.35-36, 27 Jan 1557, the Cardinal of Lorraine | **None.** No hit for 20140, 1557 or Lorraine/cardinal anywhere in the text. The only 1550s dates are Danzay's career span (1548-1589) and the fall of Narva in 1558. |
| Cites Tomokiyo | Yes, for the 1574 letter only: Cryptiana's "French Ciphers during the Reigns of Charles IX and Henry III", where that letter's cipher is noted as unsolved (p. 1492). It does not cite "Danzay's Ciphers" or the 1557 key, which Tomokiyo posted in Feb 2026, after this issue. |
| Own sources | BnF fr.4736, fr.2812, Cinq cents de Colbert 398; Rigsarkivet TKUA; the printed *Correspondance de Charles Dantzai* (1824) and Bricka (1901), which the article says cover 1567-1575 with gaps (n.5); Richard 1910; Hauser 1931; Lublinskaya 1963 (DIVPF); Desenclos 2018. |

**Same key?** No. The table is a different cipher. The glyph values differ at first sight: Ryabov's first a-sign is a
"9" shape, and in Tomokiyo's 1557 table (`sources/cryptiana/web/danzay_1557.png`) the 9-like sign stands in the d column.
Ryabov's h is an "a"-shaped sign, and his 1578 nomenclator set (Roy de Dannemarch, Roy de Suède) has no Suède counterpart in
the 1557 table. This check was by eye on two images and was not a sign-by-sign comparison; it is enough to say the two
tables are not the same. **Same letter?** No. **Overlapping plaintext?** No: the 1574 and 1578 letters concern Poland after
Henri's flight, Reval and the Stettin indemnity, and an English Protestant league. The 1557 letter is not among them.

**Credit question (for outreach, not the class).** Ryabov's key is his own reconstruction of the 1574/1578 cipher.
Tomokiyo's key is his reconstruction of the 1557 cipher, from fr.20140 ff.16, 24 and 30. The two reconstructions are
independent and do not compete. Our f.35-36 reading uses Tomokiyo's 1557 key only. Tomokiyo's own Danzay page already
cites Ryabov for the later cipher (NOTES.md, "Check-solved").

**Class: N4 unchanged** (no prior decipherment located). The article is the specific study of Danzay's cipher, and it does
not print, calendar or decipher the 27 Jan 1557 letter. Nothing in it lowers the class. The family is now "searched" at the
full-text level, where before it rested on the abstract.

- Safe sentence (unchanged): "No prior decipherment located of Charles de Danzay's letter to the Cardinal of Lorraine,
  Copenhagen, 27 Jan 1557 (BnF fr.20140 f.35-36), read with the key S. Tomokiyo published in 2026; Ryabov's 2025 study of
  Danzay's cipher treats the later letters of 1574 and 1578."
- Unsafe sentence: "The first decipherment of any Danzay cipher" or "Danzay's cipher was unknown until now". Ryabov 2025
  reconstructed and published the 1574/1578 table, and Tomokiyo published the 1557 table in 2026.

**Open-index family.** The parent ran six OpenAlex queries with the owner's key, 24 Sept 2026 about 17:50 UTC. There was one
relevant hit, this article, now read. ASKS row 44(a) is marked done. The remaining gate-2 item for this target is the JSTOR
READ row (Hauser 1923, stable/40944190).

**Changes made.** The outreach draft's status line was updated and one sentence citing Ryabov 2025 was added to its Danzay
bullet; the paragraph otherwise stands. The CONTRIBUTIONS.md row, ASKS.md row 44(a) and the NOTES.md sources were updated.
status.json is untouched because the class did not change. No over-claiming sentence was found in the folder about Ryabov:
sections 3(d)/3(e) and NOTES.md already said "different cipher, different volume", and this read confirms it.


JSTOR family closed, 24 Sept 2026 18:03 UTC: the remaining READ row (Hauser 1923 (stable/40944190)) was read on the owner's machine (JSTOR-QUEUE.tsv, hits column) and does not print, calendar or discuss the letter. Open-index pass done the same day with the OpenAlex key (six queries, ASKS row 44). Outreach gate 2 is met; the parent set the outward draft to ready.
