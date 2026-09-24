open

# "Lettre en partie chiffrée de Paget" -- BnF Clairambault 296-299

QUEUE row: M26 (`sources/solver-diffs/2026-09-24-lane-g2-gallica4.tsv`, LANE G2 worker F's archivesetmanuscrits
item-level sweep).

## Source

BnF, Clairambault 296-299 ("Pièces historiques diverses...et correspondance diplomatique de Pontchartrain"),
`ark:/12148/cc138146`. One named item, "Lettre en partie chiffrée de Paget", dated **14 January 1713**. A
second, distinct Paget cipher letter from M4 (Clairambault 1225, "lettres autogr. de Paget, avec chiffre,
1714", check-solved 23 Sept 2026, open/unlocated -- see `ciphers/clairambault1225-paget-1714/NOTES.md`):
different volume, one day short of a year earlier; not a duplicate (different shelfmark, no key stated in
either). Not fetched at gallica.bnf.fr or archivesetmanuscrits.bnf.fr this pass per the brief; catalogue text
only, no image viewed.

## Check-solved sweep (24 September 2026)

1. **Search engine.** `Clairambault 296 Paget 1713 chiffre Pontchartrain` -- surfaced only the BnF Archives et
   manuscrits notice itself (`cc138146`) and unrelated Clairambault-volume listing pages. No cipher-specific
   discussion found. `William Paget baron 1713 lettre chiffre Pontchartrain Utrecht négociation` -- confirms
   **William Paget, 6th Baron Paget** (English ambassador/diplomat) **died 26 February 1713**, six weeks after
   this letter's 14 January date, during the final months of the Treaty of Utrecht negotiations (signed 11
   April 1713) -- a plausible but unconfirmed identification, not a document-inspection match. M4's own NOTES
   flags a separate, unrelated "Paget's Cipher" (Charles Paget, correspondent of Mary Queen of Scots, SP53,
   1580s) as a known false-friend for this surname; that confusion is not repeated here.
2. **Printed correspondence / calendars.** Not run beyond the web search above; no dedicated Paget-1713 edition
   or Utrecht-negotiation calendar checked this pass (French Foreign Ministry `archivesdiplomatiques.diplomatie.
   gouv.fr` inventory pages for "Négociations de la France à Utrecht" surfaced in the search but were not opened
   or full-text searched -- flagged as the next step, budget-limited).
3. **Cryptiana.** Local snapshot grepped for "Paget", "Clairambault 296": no hit (M4's own NOTES already
   surveys the "Paget's Cipher" confusion in `sources/cryptiana/web/mary.htm`; that entry is the unrelated
   16th-century Charles Paget cipher, not this item).
4. **Cipherbrain.** `cipherbrain OR klausis "Arsenal" chiffre 1708 OR 1713 OR 1745 unsolved` (run for M22,
   covering this row's 1713 date) returned no hit naming Paget or Clairambault 296.
5. **DECODE.** Aymeloglu's cached `catalogue/decode-catalog.csv` (10,107 rows) grepped for "paget",
   "clairambault 296": zero hits for both (M4's own NOTES already recorded the same zero for "paget" against
   this catalogue on 23 Sept). This repo's own local harvest also has no matching row.
6. **Solver repositories.** Fresh shallow clones of both repos grepped for "Paget" and "Clairambault 296"/
   "cc138146" exactly. "Paget" returns many hits in both repos, but every one checked (`docs/search.json`,
   `charlesi/*.htm`, `top50/*.htm`, `sp53/NOTES.md`, `stafford1586/*`) is the unrelated 16th-century Charles
   Paget material already flagged by M4 -- confirmed by grepping the actual hit context (`docs/search.json`:
   "that vile traitor Charles Paget", from an Elizabethan-era manuscript, not 1713). No hit for the shelfmark
   or ark in either repo.

## Verdict

**Open, stage 2 verified unsolved (conditional).** Not found in a search engine, Cryptiana, Cipherbrain,
DECODE's cached catalogue, or either solver repository (beyond the already-known unrelated Charles Paget
material), searched by shelfmark, ark and correspondent name on 24 Sept 2026. Conditional because the Utrecht-
negotiation French diplomatic archive inventory and any dedicated Paget correspondence edition were not opened
or full-text searched this pass -- flagged for a future worker, and worth checking together with M4
(Clairambault 1225) as the same correspondent's two known cipher letters, one day short of a year apart.

Requests: WebSearch 2 queries (this row) + 1 shared with M22. github.com 0 new (reused clones). No
gallica.bnf.fr, no archivesetmanuscrits.bnf.fr fetch. No subagents.
