# AUDIT: novelty of the f.35 reading (Danzay to the Cardinal of Lorraine, "27 Jan 1557")

Verifier session, 24 Sept 2026 (03:00-03:15 UTC), orchestrator session_01EFmUvFAifLKGdBSsW9mjEG. This session
did not take part in the check-solved, transcription or solver sessions and did no decoding. Levels N0-N5 are
those of CLAUDE.md rule 10. Claim under audit: NOTES.md "Reading with Tomokiyo's key" says f.35 reads with
Tomokiyo's published 1557 Danzay key: 638 cipher tokens, H 508 (61 nulls) / M 61 / U 69, continuous French on
about 23 of 37 lines; the letter continues on f.36, which has not been transcribed. The repo makes no novelty
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
continuous French (508 of 638 cipher tokens at grade H, 69 signs unkeyed). No prior decipherment or printed
plaintext was located in the Danzay editions, the Scottish and English state-paper series, or the Danish
regesta (search log in AUDIT.md). The letter continues on f.36, which has not been read."

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
  different volume.

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
its 37 lines give continuous French (508 of 638 cipher tokens at grade H). Two independent audits found no prior
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
