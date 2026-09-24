open

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
