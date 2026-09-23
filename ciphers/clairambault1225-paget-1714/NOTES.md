open

# "Lettres autogr. de Paget, avec chiffre, 1714" -- BnF Clairambault 1225

QUEUE row: M4 (sources/solver-diffs/2026-09-23-digitised-hits.tsv, "Digitised candidates, no copy needed").

## Source

BnF, Departement des Manuscrits, **Clairambault 1225**, Gallica `ark:/12148/btv1b9001034d` (268 leaves),
"CXV Melanges" (the last, catch-all volume of Clairambault's 120-volume "Minutes du Recueil pour servir a
l'histoire de l'Ordre... du Saint-Esprit" research series). BnF Archives et manuscrits notice (item-level
index) `http://archivesetmanuscrits.bnf.fr/ark:/12148/cc137837/cd0e29423`, precise entry: **"Fol. 48 --
Rosset de Fleury (testament du cardinal ; lettres autogr. de Paget, avec chiffre, 1714)."** The same
notice's name-index confirms this independently: **"PAGET -- Lettres chiffrees"** (plural), i.e. more than
one enciphered Paget letter. The item sits inside a single physical dossier grouped under the "Rosset de
Fleury" family name, alongside an unrelated cardinal's testament -- almost certainly a bundling of unrelated
autographs from one acquisition lot, not evidence the two items are historically connected.

## Check-solved sweep (23 September 2026)

1. **Web search.** `Paget 1714 lettre chiffre ambassadeur Constantinople OR "Lord Paget"` -- confirmed
   William Paget, 6th Baron Paget (ambassador at Constantinople 1692-1702) **died in 1713**, ruling him out
   for a 1714-dated letter. `"Henry Paget" OR "William Paget" 1714 letter cipher diplomat` -- surfaced the
   strongest lead: **Henry Paget (1663-1743), 7th Baron Paget**, who succeeded his father 26 Feb 1713 and
   was appointed Envoy Extraordinary to the Elector of Hanover on 1 May 1714 (refusing to go unless made an
   Earl; secured the earldom of Uxbridge from George I in October 1714) -- exactly the Hanoverian-
   succession window (Queen Anne died 1 Aug 1714, George I acceded) a cipher letter of this date would most
   plausibly concern. **Not confirmed by document inspection** (see below) -- reported as the best-sourced
   candidate, not an identification.
2. **Print/scholarship.** No dedicated edition search run beyond the web search above; History of
   Parliament Online's entry for Henry Paget was the source for his 1714 Hanover mission, not a
   cipher-specific source.
3. **Community lists.** `sources/cryptiana/web/mary.htm` names an entirely **different, unrelated** "Paget's
   Cipher": Charles Paget's correspondence with Mary Queen of Scots (SP53/15-16, 1585-86), keyed at SP53/22
   f.47 -- over a century earlier, a different Paget, a different cipher, a different archive. Flagging
   this explicitly so a future search for "Paget's Cipher" does not conflate the two. No other cryptiana
   page, and no cipher blog or list, mentions Clairambault 1225 or a 1714 Paget cipher.
4. **DECODE.** Cached catalogue grepped for "paget", "clairambault 1225": no hit.
5. **Bourdeau.** `cs-recheck/CATALOGUE.md`, `SOLVED_CATALOGUE.md`, `TARGETS.md` grepped for "paget": no
   hit.
6. **Aymeloglu.** `ay/CATALOGUE.md`, `TARGETS.md`, `SHORTLIST.md` grepped for "paget": no hit.

Requests: gallica.bnf.fr 6 (1 OAI GetRecord, 1 IIIF manifest, 1 Pagination service call [0 folio numbers],
1 ContentSearch call [0 OCR hits], 2 IIIF image probes), archivesetmanuscrits.bnf.fr 1 (HTTP 200, the
composite 120-volume finding aid, containing all of Clairambault 1111-1230; the specific "Clairambault
1225" section was located within it by heading search). WebSearch 2 queries.

## What the leaves show

**Not located by image this sweep.** Two canvas probes (index 48 and 54, naive guesses against the cited
"Fol. 48") landed on unrelated items: an 18th-century religious-community letter (canvas 48, stamped
"209"/"42") and a mounted engraved portrait (canvas 54, not kept as a saved image). This 268-leaf
"Melanges" volume is a genuine grab-bag -- printed factums, portraits, testaments, genealogies and
autograph letters bound with no chronological or thematic order matching either the finding aid's item
sequence or its cited folio numbers in any simple way. Gallica's Pagination service returned zero
OCR-recovered folio numbers for this ark; its ContentSearch full-text index returned zero hits for "Paget"
(this manuscript, like Clairambault 361, is not OCR'd, though some individual printed items bound into it
elsewhere might be).

## Edition risk

**Unresolved.** No scholarship, cipher blog, DECODE record or solver-repository entry names this letter or
this shelfmark. The strongest signal is negative-by-omission: a 1714 cipher letter from a peer active in a
documented, historically significant mission (the Hanover succession) would be a plausible candidate for
existing scholarship on the succession or on the Paget family, but none was found by web search alone.

## Verdict

**Open, stage 2 verified unsolved (conditional: the item itself was not viewed by image this sweep, so
"what is enciphered, how much" and "which Paget" remain unconfirmed by direct inspection -- the "Henry
Paget, 7th Baron Paget/1st Earl of Uxbridge, 1714 Hanover mission" identification is a well-dated
historical lead from web search, not a document-based finding).** Nothing here is claimed as new,
unpublished or unread (rule 10).

## Next

1. **Pin folio 48 precisely** before any transcription attempt -- naive canvas-index guessing failed twice
   in this volume (unlike Dupuy 452/468); a systematic bracket search (every ~10-20 canvases) or the
   Gallica reader's own folio-search box (not reachable by curl) is needed. Budget for this was not spent
   this sweep given the cap and M6's priority.
2. Once viewed: confirm cipher type, approximate token count, and whether "lettres" (plural, per the
   PAGET index entry) means more than one enciphered letter in this one dossier.
3. Check the History of Parliament Online entry and any published Paget-family correspondence/biography
   (e.g. an Uxbridge-family archive catalogue) for a 1714 cipher letter matching this description, to test
   the Henry Paget identification before a solver session assumes it.
