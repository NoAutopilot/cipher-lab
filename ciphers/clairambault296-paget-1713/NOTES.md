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

## Digitisation check (24 Sept 2026, LANE G2 worker O)

**Digitised: yes**, ark `btv1b9000759b`, item at canvas not yet pinned (label checked: none -- see below).
The archivesetmanuscrits finding aid (`https://archivesetmanuscrits.bnf.fr/ark:/12148/cc138146`) marks its
"Clairambault 296 (cote) • I Années 1572-1713" sub-unit `avecDaoGal` ("Consultable sur gallica"); the other
three sub-units (297, 298, 299) are not marked. Our item, "Lettre en partie chiffrée de Paget," is at **p. 249**
of the finding aid's own item list, inside the 1572-1713 span, so it is in the digitised volume (297-299 are
not). The `avecDaoGal` link itself is loaded by an AJAX click (`refreshCompInfo`), not a static href on the
page, so the ark was found instead via Gallica SRU (`gallica all "Clairambault 296"`, 1697 total hits, one
with `dc:source` exactly "Bibliothèque nationale de France. Département des Manuscrits. Clairambault 296"),
whose
`dc:relation` cites `archivesetmanuscrits.bnf.fr/ark:/12148/cc138146/cd0e505` -- the exact same finding-aid
component id as the marked sub-unit, confirming the match. `tools/gallica_folio.py btv1b9000759b --folio 249`
found 316 canvases but 0 carry any folio/page label at all (this recueil's leaves are unlabelled, like fr.16092
per CLAUDE.md) -- canvas for p.249 cannot be pinned without an eye-checked `--anchor` pair, out of this brief's
scope ("no crops, no passes"). Status stays open (a capture worker can now proceed; not blocked).

Requests this section: gallica.bnf.fr 2 (1 SRU query "gallica all Clairambault 296", 1
`gallica_folio.py` manifest fetch).

## Canvas pin attempted, not found (24 Sept 2026)

LANE G2 worker P (Sonnet, cap $4). Confirmed manifest independently (`https://gallica.bnf.fr/iiif/ark:/12148/
btv1b9000759b/manifest.json`, shelfmark "Clairambault 296", title matches the sub-unit above, 316 canvases, all
labelled `NP` -- no page/folio metadata, as worker O already found). ContentSearch (`?ark=btv1b9000759b&query=...`)
returns 0 hits for "Paget" **and** for a control word known to be on a printed page in this volume ("THERESE",
see below) -- this ark carries **no OCR layer at all**, so Gallica full-text search cannot locate the item; only
eye-checking images works.

**Physical page stamps found, but they mislead.** Most openings in this recueil carry an ink page number in the
top outer corner (distinct from the mount's own item numbering and from any printed pamphlet's own internal
page numbers). Three probes calibrate it as continuous and linear: canvas f130 -> corner "235"; f137 -> corner
"249" (predicted by interpolating the other two, then confirmed by fetching and reading it); f144 -> "263";
f250 -> "503". Rate ~2.24 pages/canvas, matching the finding aid's own max cited page (P. 709) divided by the
316 digitised canvases (709/316 = 2.244) almost exactly -- so this stamp is very likely the same running
pagination the finding aid's "P. xxx" citations refer to, and the calibration itself is reliable.

**But the content at the predicted canvas does not match.** Canvas f137 (stamped "249", exactly where the
finding aid places "P. 249 - Lettre en partie chiffrée de Paget") shows the opening leaf of a wholly unrelated
**printed** pamphlet, "Panégyrique de Ste Thérèse" (devotional oratory, not diplomatic correspondence, no cipher,
no handwriting). Canvas f250 (stamped "503") is likewise a different printed pamphlet, an "Oraison funèbre de
Monseigneur le Dauphin" / "de M. de Harlay Archevêque de Paris". Canvas f130 (stamped "235", next to the finding
aid's "P.235 Proposition au sujet du port des armes") shows yet another mismatch: two mounted printed leaves
about a poisoning affair ("Saint Laurens", "Officier de Cour Souveraine"). Every stamped-number prediction tried
lands on print, never on the political 1712-13 manuscript correspondence the finding aid describes at those
same numbers. Most likely explanation: this recueil is "Pièces historiques diverses, dont plusieurs imprimées
(1572-1742)" (manifest title) -- printed items were pasted in among manuscripts in whatever order the volume was
bound, not the finding aid's item order, and the finding aid's "P. xxx" is probably a page reference into a
separate printed catalogue description of this volume (an Omont-type inventory), not the physical page stamped
on these images. **This means the canvas-from-page-number method does not work for this ark and should not be
retried without new evidence for what "P. xxx" actually indexes.**

**Not pinned.** Two thumbnail probes near the finding aid's predicted position (f130, f137, f144) and one
further out (f250) plus a check at f300 (also print, "Oraison Funèbre de Monseigneur le Dauphin") found no
handwritten political letter of any kind in the ~120-canvas span sampled; the actual "Lettre en partie chiffrée
de Paget" was not seen this pass. A full sweep of all 316 canvases (or of whatever block turns out to hold the
Pontchartrain 1713 diplomatic correspondence specifically, which the manifest title calls out as if a distinct
component of the volume) is outside this brief's scope ("no passes"; this was a location check only) and is
the next step. Status stays `open`; not blocked, just unpinned -- a worker with more budget should browse in
wider strides (every 20-30 canvases) looking for handwriting rather than print, since prose type alone
(handwritten vs. printed) distinguishes the diplomatic letters from the pamphlets at a glance.

**Hand/cipher comparison with clairambault1225-paget-1714 (M4): not possible this pass.** The brief asked
whether the two Paget items' hands and ciphers look alike; without a located image of this item's actual letter,
no comparison can be made. Deferred to whoever pins the canvas.

Requests this section: gallica.bnf.fr 8 (1 manifest re-fetch, 2 ContentSearch, 5 image previews at 1000px:
f130, f137, f144, f250, f300, all 200 on first try, >=1.5s apart). No other host.
