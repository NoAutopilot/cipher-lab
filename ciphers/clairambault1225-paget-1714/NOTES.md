partial

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

**Requests, 25 September 2026 (OX-PAG, folio-pinning + imaging pass):** gallica.bnf.fr approximately 40
(1 IIIF manifest fetch via `tools/gallica_folio.py`, ~32 image/region fetches saved to
`images/bracket/` for the bracket search and corner-numeral checks, ~5 `info.json` size checks not saved
as files, 2 transient `Recv failure: Connection reset by peer` -- each retried once after a pause and
succeeded, no third attempt). All requests sequential, one at a time, >=1.5s apart (most loops used 1.6s).
No 429/403/challenge seen. This is a single Gallica "slot" (OX) per COMMON; released at the end of this
session (see ROOM.md).

## What the leaves show (25 September 2026, OX-PAG)

**Located and imaged.** Folio 48 is pinned with direct confirmation, not a guess: the leaf tab reads
"Rosset-de fleury." and the item heading reads "Testament de M. le Card. de Fleury Ministre d'Estat et
cyder. Precepteur du Roy Louis XV." -- Gallica canvas `f55` (IIIF `f`-number; see
`images/manifest.json`'s `folio_pinning` note for the corner-numeral method and offset). The prior sweep's
two probes (canvas `f48`, `f54`) were simply the wrong canvases, off by the offset now established; both
kept in `images/` for the record.

The dossier reads, in canvas order: Cardinal Fleury's testament (`f55`-`f56`, vol.folio 48-49, dated "fait
a Issy le 6 janvier 1743"), a biographical notice of Fleury (`f57`-`f59`, vol.folio 50-52, seen at 1400px,
not saved -- not part of either Paget letter), then **two enciphered autograph letters from Paget**,
writing from Genoa ("Gennes") to an unnamed French "Monseigneur", each opening "Monseigneur, J'ay receu
la/les lettre(s)..." and closing "Je suis avec tres profond respect, Monseigneur, De Vostre Excelence, Le
tres humble et tres obeissant serviteur, [signed] Paget":

- **Letter 1**: `f60` (start, right page only) through `f65` (left page, signed). Dateline **"A Gennes le
  8e Avril 1714."** Content: Venetian news via "M. l'Abbe Lomelini"; the France-Empire peace (Treaty of
  Rastatt, concluded March 1714) and whether "le Roy de Sicile" (Victor Amadeus II) is covered by it;
  Genoese banking-family news (the death of the banker marquis Pallavicino, the Grimaldi and Rospigliosi
  families); a new vice-consul, "Langier de Toulon"; and Paget's own request that Monseigneur send his
  "expeditions" so he can take up **"le consulat de la nation en Sardaigne"** that has been destined for
  him, referring back to a memoire on the duties of a consul he had sent in April 1712.
- **Letter 2**: `f65` (right page, start) through `f66` (both pages, signed). Dateline **"a Genes le 28
  aoust 1714."** Content: much more heavily enciphered throughout -- dynastic/marriage politics around
  Parma, "le Prince Francois Farnese", "le Roy d'Espagne" and "Madame la Duchesse", consistent with the
  run-up to Elisabeth Farnese's marriage to Philip V of Spain (September 1714, about a month after this
  letter).

**The cipher is a nomenclator**, not a full substitution: continuous French prose with isolated
period-separated numbers (2-3 digits, values roughly 1-300 seen so far) standing in for proper names,
places and sensitive terms; the surrounding French is never enciphered. Token density varies sharply by
passage -- some paragraphs (Genoa gossip, the plague news) carry no cipher numbers at all, others (most of
Letter 2) are almost continuously coded. **No interlinear or marginal gloss/decipherment was seen on any
leaf** (checked per `.claude/briefs/transcription.md`'s pre-pass rule (a) on every fetched image) -- this
looks like a live, unbroken nomenclator, not a found-solved leaf; nor was a second copy of either letter,
or a printed edition of the passages, checked for this pass (rules (b)/(c) of the same brief, left for the
next worker; see Next).

This resolves "which Paget": the document itself names only "Paget" (no forename or title given in what
was read), writing in French from Genoa about Mediterranean/Italian affairs and his own pending consular
appointment to Sardinia. Nothing here supports or requires the earlier "Henry Paget, 7th Baron
Paget/Hanover mission" lead from the 23 September web search (an English peer's Hanover mission does not
fit a French-language letter from Genoa about a French consulship in Sardinia); that lead is now
considered unlikely rather than the best-sourced candidate, but not formally ruled out by name-search this
pass. This is a document-based finding, not a web-search lead: grade C-adjacent for "sender = someone
named Paget, at Genoa, 1714" (read directly off the signature and dateline), nothing here is a
decipherment or claimed as new/unpublished/first (rule 10).

Full canvas-by-canvas description, IIIF URLs and the folio-pinning method are in `images/manifest.json`.

## Edition risk

**Unresolved, narrower now.** No scholarship, cipher blog, DECODE record or solver-repository entry names
Clairambault 1225 or this Paget correspondence (23 Sept sweep, sources 3-6 above). Not yet checked this
pass: a phrase/name search for "Paget" together with "consul" and "Sardaigne" or "Gennes"/"Genes" 1714 in
French diplomatic-history scholarship (AE Correspondance Politique Genes inventories, any published guide
to French consuls in Sardinia/Genoa), which the old-series page stamps ("239"..."281") suggest these
letters were extracted from -- a continuously paginated volume of outgoing/incoming consular
correspondence, not this Clairambault "Melanges" binder's own numbering. That volume, if identified, may
also hold the nomenclator's key or a decipherment.

## Verdict

**Partial: located, imaged, dated, signed and described; not yet transcribed or decoded.** Two Paget
letters confirmed (matches the finding aid's plural "PAGET -- Lettres chiffrees" exactly), dated 8 April
and 28 August 1714, Genoa. Nothing here is claimed as new, unpublished or unread (rule 10) -- only that a
search by the methods logged found nothing describing this correspondence.

## Next

1. **Transcribe.** Two independent blind Sonnet passes + `tools/reconcile_passes.py` per
   `.claude/briefs/transcription.md`, into `ciphertext.tsv` (nomenclator numbers only need to be captured
   accurately; the surrounding French can be read more loosely but should still be captured for context/cribs).
   Scope: 7 canvases (`f60`-`f66`, `images/manifest.json`), roughly 12 written pages, two letters. Not
   attempted this pass -- out of proportion for one Sonnet worker under a stall-alarm cap; this is really a
   `transcription.md`-scale job (its own $30 cap, Fable reconciliation) or a lane of its own.
2. **Old-series page numbers** ("239"-"281" on these leaves, distinct from this volume's own foliation --
   see `images/manifest.json`) are a strong hint these letters were extracted from a continuously paginated
   register, almost certainly BnF or AE (Ministere des Affaires etrangeres) Correspondance Politique,
   Genes, 1714. Identifying that register (an archives.diplomatie catalogue search, or a BnF/AE
   correspondence-politique guide) before transcribing could turn up a printed calendar, an index of
   consuls, or the key itself.
3. Search "Paget" + "consul" + "Sardaigne"/"Genes" 1714 in French diplomatic-history scholarship
   (OpenAlex/Persee/HAL per the Access playbook) and in any guide to the AE's Correspondance Politique
   Genes series, before a solver session assumes any identification of this Paget.
4. The Henry Paget/Hanover-mission lead (23 Sept sweep) can likely be dropped given the document's own
   French-language, Genoa/Sardinia content, but was not formally re-searched-and-ruled-out this pass.
