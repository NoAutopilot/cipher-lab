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
