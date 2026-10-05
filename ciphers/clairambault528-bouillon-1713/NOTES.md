blocked

# Ciphered letter concerning the affaire du cardinal de Bouillon, and English/Netherlands/Spanish affairs -- BnF Clairambault 528

QUEUE row: M28 (`sources/solver-diffs/2026-09-24-lane-g2-gallica4.tsv`, LANE G2 worker F's archivesetmanuscrits
item-level sweep).

## Source

BnF, Clairambault 528 ("Pièces diverses, dont plusieurs imprimées, des XVIIe et XVIIIe siècles"),
`ark:/12148/cc13874f`. One ciphered letter inside a mixed printed-and-manuscript miscellany, catalogued as
concerning "l'affaire du cardinal de Bouillon" and English/Netherlands/Spanish affairs, dated **1713** (the
volume's own scope is broad, "XVIIe et XVIIIe siècles", and the item is not otherwise distinguished -- lower
confidence than the QUEUE row's own M26/M27 siblings). Cardinal de Bouillon is **Emmanuel-Théodose de La Tour
d'Auvergne** (1643-1715), exiled to Rome after refusing the king's recall order c.1710-12 -- the "affaire" this
item concerns is almost certainly that exile dispute, consistent with the 1713 date. Not fetched at
gallica.bnf.fr or archivesetmanuscrits.bnf.fr this pass per the brief; catalogue text only, no image viewed.

## Check-solved sweep (24 September 2026)

1. **Search engine.** `Clairambault 528 cardinal de Bouillon 1713 lettre chiffrée` -- surfaced the BnF
   Archives et manuscrits notice itself (`cc13874f`), the Wikipedia biography of Cardinal de Bouillon, and an
   unrelated Gallica item (Baluze's own correspondence with the cardinal, 1681-1698 -- a different collection,
   different correspondent pairing, different dates, not this item). `cardinal de Bouillon mémoires
   correspondance 1713 chiffre déchiffré archive.org` -- same result: no dedicated cipher discussion, only
   generic biographical and archival-inventory pages (a Persée article on his portrait, a diplomatic-archives
   PDF index, an antiquarian bookseller's listing of an unrelated signed 1713 Bouillon letter).
2. **Printed correspondence / calendars.** No dedicated edition of Cardinal de Bouillon's own correspondence
   for this exile period located and opened this pass; his published *Mémoires* (19th-c. edition) were not
   full-text searched -- budget-limited, flagged as the next step.
3. **Cryptiana.** Local snapshot grepped for "Bouillon", "Clairambault 528": no hit.
4. **Cipherbrain.** No dedicated query for "Bouillon" run; the M22 query (1708/1713/1745, Arsenal-focused)
   does not cover this shelfmark and returned no relevant hit regardless.
5. **DECODE.** Aymeloglu's cached `catalogue/decode-catalog.csv` (10,107 rows) grepped for "bouillon": zero
   hits. This repo's own local harvest also has no matching row.
6. **Solver repositories.** Fresh shallow clones of both repos grepped for "Bouillon" and "Clairambault 528"/
   "cc13874f" exactly. "Bouillon" returns many hits in both repos (e.g. `hesse1603/`, `breves1603/`,
   `nevers1593/`, `vieuville1587/`) but these are all 16th-17th century items from the Duchy of Bouillon or the
   place-name Bouillon (Ardennes), not Cardinal de Bouillon or this shelfmark -- checked by context, none names
   Clairambault 528 or the cardinal's 1710s exile affair. No hit for the shelfmark or ark in either repo.

## Verdict

**Open, stage 2 verified unsolved (conditional).** Not found in a search engine, Cryptiana, DECODE's cached
catalogue, or either solver repository, searched by shelfmark, ark and the named affair on 24 Sept 2026.
Conditional because: (a) this is the QUEUE row's own lowest-confidence item of the three Clairambault
diplomatic-miscellany rows (M26/M27/M28) -- the volume's broad "pièces diverses" scope and the item's lack of
independent distinction in the catalogue means it has not been confirmed as a genuine, substantial cipher
rather than a short annotation; (b) Cardinal de Bouillon's own published Mémoires and a targeted Persée/
scholarship search for the 1710s exile affair were not run this pass.

Requests: WebSearch 2 queries. github.com 0 new (reused clones). No gallica.bnf.fr, no
archivesetmanuscrits.bnf.fr fetch. No subagents.

## Digitisation check (24 Sept 2026, LANE G2 worker O)

**Digitised: no** (finding aid without DAO; SRU `gallica all "Clairambault 528"` 1118 records, none a
`dc:source` match -- the same query did surface Clairambault 1108, an unrelated volume, confirming the query
works but 528 itself is absent; 24 Sept 2026). Fetched the archivesetmanuscrits finding aid
(`https://archivesetmanuscrits.bnf.fr/ark:/12148/cc13874f`) in full: `avecDaoGal` applied to no element, no
`gallica.bnf.fr` href on the page. Reservation link `Cote=Clairambault 528&typecote=orig` only, no microfilm
substitute. Wrote `REQUEST.md`. Status set to blocked.

Requests this section: archivesetmanuscrits.bnf.fr 1, gallica.bnf.fr 1 SRU query (200 first try).

## NX-UNBLOCK (26 Sept 2026)

Re-checked Gallica SRU for Clairambault 528 by shelfmark: still `numberOfRecords=0`, consistent with the
24 Sept finding. No new free route found this pass. REQUEST.md (BnF reading-room visit or reproduction
enquiry) stands unchanged; still blocked, waiting on the owner.

## While waiting (27 Sept 2026, WAIT-PASS-A)

Waits on a BnF reading-room visit or reproduction enquiry for Clairambault 528, "blocked, waiting on you"
since 24 Sept 2026, unchanged through the 26 Sept 2026 NX-UNBLOCK check.

- [x] Full-text search on archive.org (5 Oct 2026, D2-CL528): no memoir by the cardinal exists on IA; "Clairambault 528" 0 hits in all IA full text and Boislisle's Saint-Simon; see section above. Remaining: Boislisle p. reading, 1923 Clairambault catalogue (not on IA).
- Run the open-index scholarship pass (Persée, OpenAlex, HAL) for "cardinal de Bouillon" 1713 exile correspondence chiffre, beyond the generic web search already tried. S.
- Re-read the finding-aid description to judge whether this item (lowest-confidence of the M26/M27/M28 siblings) is a substantial cipher or a short annotation, before the reproduction request is escalated. S.

## Edition search: Bouillon / Clairambault 528 on IA full text (D2-CL528, 5 Oct 2026, 23:55-00:00 UTC by date -u)

Search results only (rule 10). Premise correction: the WAIT-PASS-A line says "Cardinal de Bouillon's own Mémoires (19th-c. ed.)";
IA advancedsearch (title Bouillon + mémoires/cardinal) lists no memoir by the cardinal himself. The "Mémoires" hits are other Bouillons
(Saumières 1708 *Mémoires du duc de Bouillon et du vicomte de Turenne*, `mmoiresdemonsi00saum`; Henri de La Tour d'Auvergne 1901,
`mmoiresduvicom00boui`), plus 1706 *Apologie du cardinal de Bouillon* (`bub_gb_LYRzh_02ot0C`, `bub_gb_gKCVR89k_EkC`) and a 1710 English
*Collection of some letters ... concerning ... the Cardinal de Bouillon* (`bim_eighteenth-century_a-collection-of-some-let_1710`) -- all
pre-1713 or other persons, not opened. The 19th-c. edition that discusses his 1710s affair is Boislisle's Saint-Simon *Mémoires*.

be-api fts (all items), exact phrases, 0 hits each: "Clairambault 528", "Clairambault, 528", "Clairambault, t. 528", "Clairambault, vol. 528",
"ms. Clairambault 528", "Clairambault 528" cardinal; "Clairambault 528" Bouillon restricted to `memoiresdesaints14sain` (Saint-Simon/Boislisle vol. 14, which
carries the cardinal's letters p.525ff and "Le cardinal de Bouillon et Baluze"): 0. Loose (non-phrase) queries return Boislisle's
Saint-Simon volumes (`memoiresdesaints04sain`, `07sain`, `14sain`, `mmoires07sainuoft`, `mmoires14sainuoft`) citing *other* Clairambault volumes
(290, 303, 664, 733) for the cardinal, never 528; no hit for "lettre chiffrée"/"en chiffre" tied to a Bouillon 1713 letter in any edition surfaced.
Google Books API (country=US, key): `"Clairambault 528" Bouillon`, 12 items, snippets are index noise (Colbert *Lettres* vol. 430 fol. 208, Almanach de la Cour,
Lorraine 1909, etc.); none names Clairambault 528 with the cardinal. The 1923 *Catalogue des manuscrits de la collection Clairambault* appears
in Google Books (no snippet); not found on IA (advancedsearch, 0 rows), so the volume's own item list was not read.
Not done (not in this job): Persée/OpenAlex/HAL pass, reading the Boislisle pages themselves, scanning the 1710 letters collection.
Result: no print of this item or a decipherment of it located by these methods on 5 Oct 2026; conditional on OCR (all text-layer, no page images).
Requests: archive.org advancedsearch 2, be-api 14, googleapis.com 1. No subagents.
