key-only

# "Double du chiffre de Claudio Marini" (1610) and a second cipher, BnF Clairambault 361

QUEUE row: M5 (sources/solver-diffs/2026-09-23-digitised-hits.tsv, "Digitised candidates, no copy needed").

## Source

BnF, Departement des Manuscrits, **Clairambault 361**, Gallica `ark:/12148/btv1b9001048f` (535 leaves),
"LI Regne de Henri IV. -- Annees 1606-1610" (part of the Clairambault "Ordre du Saint-Esprit"/Bossuet
research series). BnF Archives et manuscrits notice `https://archivesetmanuscrits.bnf.fr/ark:/12148/
cc13826w/cd0e15574`. The notice's item-level index (not just the OAI summary) gives precise folios:
**"Fol. 211 -- Double du chiffre de Claudio Marini (avril 1610)"** and **"Fol. 237 -- Double d'un
chiffre."** Both fall strictly within the volume's own "Clairambault 361" section of the finding aid
(confirmed by locating the section boundary against the following volume, Clairambault 362, in the same
notice file).

## Check-solved sweep (23 September 2026)

1. **Web search.** No dedicated query run for "Clairambault 361 Marini" alone this sweep (folded into the
   cryptiana/print check below, which surfaced the relevant lead directly).
2. **Print/scholarship -- the key lead.** `sources/cryptiana/web/louisxiii.htm` has a dedicated "Marini"
   section: "Claudio Marini, Marquis of Borgofranco, was ambassador in Turin in 1617-1629 (Gellard). A
   letter to him partially in cipher, dated 13 July 1624... is presented in Fig.3 of Anna Cantaluppi
   (2010-2011), 'Le carte del genovese Claudio Marini, ambasciatore del Re di Francia in Piemonte, nell'
   archivio della Compagnia di San Paolo', Bollettino della Societa Piemontese di Archeologia e Belle Arti
   (Academia.edu), which allows reconstruction of the cipher." Tomokiyo also separately notes "BnF fr.3662,
   f.24bis, is a cipher in Italian with Claudio Marini (I have not seen it)." **Neither of these is this
   shelfmark or this date**: Cantaluppi's 1624 letter is in the Turin Compagnia di San Paolo archive, not
   BnF, and both of Tomokiyo's Marini references postdate 1610 by 7-14 years, sitting inside what he gives
   as Marini's ambassadorship (1617-1629). This volume's key is dated **April 1610**, seven years before
   Tomokiyo's stated start of Marini's Turin embassy -- either Marini held an earlier, unrecorded
   diplomatic role (plausible; ambassadors often had prior missions), or the 1610 date marks when the
   French court acquired/copied a cipher for future use with him, or this is a namesake. **Flagged as an
   unresolved discrepancy, not resolved this sweep** -- worth a historian's note, not applied as if it
   settles the identification.
3. **Community lists.** `sources/cryptiana/` grepped for "clairambault 361"/"clairambault361": no hit
   (only the general "Marini" section above, tied to a different shelfmark/date).
4. **DECODE.** Cached catalogue grepped for "marini", "clairambault 361": no hit for either.
5. **Bourdeau.** `cs-recheck/CATALOGUE.md`, `SOLVED_CATALOGUE.md`, `TARGETS.md` grepped for "marini": no
   hit (the one incidental match, "Rationes contra exactionem marini... in Prussia (1617)" elsewhere in the
   same composite finding aid, is an unrelated Latin common noun "marini" [of the sea], not the person).
6. **Aymeloglu.** `ay/CATALOGUE.md`, `TARGETS.md`, `SHORTLIST.md` grepped for "marini": no hit.

Requests: gallica.bnf.fr 7 (1 OAI GetRecord retried once on connection reset, 1 IIIF manifest, 1
Pagination service call [0 folio numbers returned], 1 ContentSearch call [0 OCR hits, manuscript not
full-text indexed], 4 IIIF image fetches: 2 canvas probes, 2 more attempted then abandoned per budget),
archivesetmanuscrits.bnf.fr 2 (both HTTP 200, plain curl; one for the OAI-linked notice fragment, one for
the full composite finding aid with item-level folios). WebSearch 0 dedicated queries this target
(cryptiana grep answered the print/scholarship question directly).

## What the leaves show

**Neither key was located by image this sweep.** Two probe fetches, at canvas index 211 and 237 (naive
guesses equal to the cited "Fol." numbers), both landed on unrelated plain administrative items (a 1609
Bordeaux election dispute; a 1610-era barony/jurisdiction dispute) under **different, overlapping period
foliation stamps** ("131"/"295" at canvas 211; "144"/"143"/"261" at canvas 237) -- proof this 535-leaf
composite volume carries multiple historical numbering layers that do not track Gallica's own IIIF canvas
order the way Dupuy 452 and Dupuy 468 did. Gallica's Pagination service (which sometimes exposes an OCR'd
folio-to-canvas map) returned zero numbered pages for this ark, and its ContentSearch full-text index
returned zero hits for "Marini" -- this manuscript is not OCR'd. **No ciphertext letter is named anywhere
in this volume's finding-aid item list** (grepped in full for "chiffre": only the two "Double..." key
entries appear, out of roughly 80 distinct items spanning 1606-1610) -- this determination rests on the
finding aid's text, not on a confirmed image of the keys themselves.

## Edition risk

**Unresolved, flagged rather than settled.** Cantaluppi (2010-2011) has already reconstructed a cipher
used by/with Claudio Marini, but from a different archive, a different (later) date, and possibly a
different specific key -- this is a real but imperfect edition-risk signal, not a clean match. No
scholarship or solver-repository entry names Clairambault 361 itself.

## Verdict

**Closed-negative / key-only**, matching QUEUE M5's own framing and its precedent M2
(clairambault351-paliano, also closed-negative/key-only this sweep). The finding aid text is unambiguous:
two keys ("Double du chiffre de Claudio Marini", "Double d'un chiffre"), zero ciphertext letters, among
roughly 80 named items covering 1606-1610. This is a recovery target only if a Marini letter (or a letter
using "un chiffre" unattributed) turns up **elsewhere** in the wider Clairambault series and needs this
volume's key to read it -- not a target in its own right as catalogued. Nothing here is claimed as new,
unpublished or unread (rule 10).

## Next

1. **Drop M5 from the "digitised, view leaves" board** as a stand-alone target; it is a key-only volume,
   like M2. If anyone wants the key photographed for a future recovery elsewhere in the series, canvas
   indices in this volume need a proper folio-by-folio crawl (bracket search, or the Gallica reader's own
   "aller a la page" box, not reachable by curl) since naive canvas=folio guessing fails here.
2. **Resolve the 1610-vs-1617 Marini discrepancy**: check Gellard's source for "ambassador in Turin
   1617-1629" against any earlier Marini posting, or confirm/rule out a namesake, before treating
   Cantaluppi's 1624 reconstruction as a lead for this key.
3. If a future sibling search finds an actual Marini ciphertext (in another Clairambault or Français
   volume), this key's folio (211, per the finding aid) would be the one to fetch first, once properly
   pinned.
