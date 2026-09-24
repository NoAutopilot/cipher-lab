# zbz-ulrich-zwingli-1531

Status: found-solved (K3); open (K4)

## What this is

Two items scored together by LANE S scout, 24 Sept 2026 (QUEUE.md, "German and Austrian catalogue candidates"),
both catalogued at ZB Zürich as partial, in-line ciphers inside otherwise-plaintext letters from Duke Ulrich of
Württemberg, addressed (per the cataloguer's own hedged "?") to Ulrich Zwingli:

- **K3**: Ms F 46.186 (swisscollections `ZBCb0983abd4cda4e25b2ec4c18a151b83a`), dated 11 Apr 1531. Catalogue
  note (`500 |a`): "Der Brief ist in der Anrede sehr vage und stellenweise verschlüsselt" (vague in the
  salutation and enciphered in places).
- **K4**: Ms F 46.202 (swisscollections `ZBC63cf86b536d443f3b00b57ccd32ad325`), undated, "possibly an enclosure
  to another letter". Same fonds, same note pattern, lower confidence.

Both are `gesuchspflichtig` at ZB Zürich; no ciphertext.txt exists (no transcription in hand; the check below
was done from the printed edition's transcription, not the manuscript image — see caveat at the end).

## Check-solved sweep, 24 Sept 2026

Six sources, run directly (no subagents). The print check below overturns the "open" status the scout carried
these two rows in at.

1. **Web.** WebSearch: `Duke Ulrich Württemberg Zwingli 1531 Brief verschlüsselt Zürich`. General
   biographical results on Ulrich/Zwingli's contact from 1524 onward and their October 1529 meeting at Marburg;
   nothing naming a cipher or this shelfmark directly, but one result (`bullinger-digital.ch/persons/P9708`,
   a person-authority page for Ulrich von Württemberg on the sister Bullinger correspondence-edition site) was
   followed up (WebFetch) — it documents Ulrich's later contact with Bullinger (from 1534) and confirms the
   Zwingli contact but names no cipher and gives no April 1531 letter; not the source that resolved this (see
   Print below).
2. **Print — this is the finding.** Huldreich Zwinglis sämtliche Werke (the Corpus Reformatorum edition of
   Zwingli's collected works and correspondence, ed. Egli/Finsler/Farner), vol. 11 (1935), covering the
   Briefwechsel for early-mid 1531 (archive.org `HuldreichZwinglisSaemtlicheWerkeVol11`, public domain, full
   OCR text fetched to `/tmp/zwingli_vol11.txt`, not kept in the repo). This volume prints **two** direct
   letters headed "Herzog Ulrich von Württemberg an Zwingli":
   - **No. 1176**, "Kassel, 3. März 1531", source given as "Zürich, Zentralbibliothek: F 46, p. 475-476,
     Siegelspur", with "Abdruck: Sch. u. Sch. VIII 585" (an earlier printing, in the 19th-century Schuler &
     Schulthess edition of Zwingli's works). This is neither K3 nor K4 by date (3 March, not 11 April or
     undated), but shares the exact shelfmark family (F 46) and is worth the orchestrator's attention as an
     adjacent F 46 item the scout's catalogue sweep did not surface as its own row.
   - **No. 1193**, "(Cassel), 11. April 1531", source given as "Zürich, Zentralbibliothek: F 46, p. 473,
     Siegelspur", with "Abdruck: Sch. u. Sch. VIII 594". **This is K3**: same shelfmark family, same sender,
     same recipient, and the exact date the swisscollections catalogue gives for Ms F 46.186.
   Both letters carry the editors' square-bracket convention for words originally enciphered in the
   manuscript — e.g. letter 1193's text reads (per the edition's transcription) "...roie [ZürichJ]
   [Landgraf von Hessen] gefdjriben..." and later "...es bnb [Herzog von Württemberg] halben..." — each
   bracketed word cross-referenced by footnote to "die Chiffrentafel am Schlüsse von Bd. X und XI" (the cipher
   table printed at the end of volumes X and XI of this same edition), which is how the editors resolved them
   into clear. Letter 1176 carries the identical footnote apparatus and the identical "eingeklammerten Worten"
   convention. In other words: the enciphered code-names in K3's letter are already deciphered and printed in
   clear, with the underlying cipher key table also in print, and this printing itself is stated to reprint an
   even earlier decipherment ("Sch. u. Sch.", i.e. the Schuler & Schulthess edition, predating 1935).
   No third, undated "Herzog Ulrich von Württemberg an Zwingli" letter was found in this volume: `grep -n
   "F 46"` across the full OCR text returns only the two page references above (p. 473 and p. 475-476); no
   undated item matching K4's "possibly an enclosure" description was located here. Vol. 10 (covering 1530) and
   the original Schuler & Schulthess edition were not checked this session (budget) — the next step for K4.
3. **Lists.** No hit for "Zwingli" in `sources/cryptiana/web/` or `sources/cryptiana/blog/` (grep, both
   directories). Not a target Tomokiyo's list covers.
4. **DECODE.** Cannot log in (ASKS row 1). Cached catalogue (`aaymeloglu/unsolved-ciphers/catalogue/
   decode-catalog.csv`): zero hits for Württemberg, Zwingli or Ulrich.
5. **Bourdeau.** Fresh shallow clone, 24 Sept 2026. Zero hits for "Zwingli" anywhere in the repository.
6. **Aymeloglu.** Fresh shallow clone, 24 Sept 2026. Zero hits for "Zwingli" beyond the cached DECODE catalogue
   already covered under source 4.

## Verdicts

- **K3 (Ms F 46.186, 11 Apr 1531): found-solved.** The letter is identified in print (Egli/Finsler/Farner,
  Corpus Reformatorum ed., vol. 11, 1935, letter no. 1193, with an earlier printing already extant in Schuler &
  Schulthess vol. VIII, p. 594) and its coded words are resolved via the edition's own printed cipher table.
  Who did not know: this project's own catalogue sweep, which had this row as an unread, uncheck-solved
  cryptanalysis candidate; the swisscollections/Kalliope metadata record carries no cross-reference to either
  print edition. What this leaves to hand on: a transcription of the letter as printed (with the editors'
  bracketed resolutions) plus a citation chain (CR vol. 11 no. 1193 -> Sch. u. Sch. VIII 594) for whoever writes
  this target up; no cryptanalysis or archive visit is needed to read it. Grading and any repair proposal are a
  solver-stage task, not this sweep's.
- **K4 (Ms F 46.202, undated): open.** Not located in CR vol. 11; the two Ulrich-to-Zwingli letters printed
  there (nos. 1176 and 1193) are both fully dated and neither matches K4's "undated, possibly an enclosure"
  catalogue description. Remains stage 2 verified unsolved (conditional), pending a check of CR vol. 10 and the
  Schuler & Schulthess original.

Caveat: this check was done from the 1935 edition's own transcription of the manuscript, not from the ZB Zürich
image itself (per CLAUDE.md rule 2, "image over transcription" — no image has been seen for either item this
session; treat as conditional on the edition's transcription being accurate until the leaf itself, or at least
a facsimile, is checked). Novelty is not classified here (rule 10) — "found-solved" states only that a prior
print decipherment exists and where; an AUDIT.md N-class is a verifier's job, not this sweep's.

Requests this pass: archive.org 3 (advancedsearch metadata + djvu.txt fetch for
`HuldreichZwinglisSaemtlicheWerkeVol11`), github.com 2 (shallow clones, shared with K1/K2). No swisscollections.ch
or kalliope-verbund.info calls needed (scout already read both record pages). No TNA Discovery, no Google Books.
