partial
Rousset, *Histoire de Louvois et de son administration politique et militaire* (tome IV, archive.org
histoiredelouvoi04rousuoft, read in full via djvu text and grepped by this worker), control "Boufflers" 23
hits confirming readable OCR; no hit for "Avis de Flandre" and the volume's several "Noailles" hits are all
the duc de Noailles's Catalonia/Roussillon campaigns, not Flanders -- consistent with the item's sender/date
still being unidentified rather than a confirmed absence from print.

## Check-solved (LANE CX, 2026-09-25)

Six-source sweep run fresh this pass (LANE CX worker CX-CLAIR), on top of -- not only quoting -- the 24 Sept
2026 LANE G check-solved pass kept below (which already established the item has no independent sender, date
or recipient in the BnF finding aid, only a shared folio note for four different Noailles-family pieces
spanning 1570-1719, and that the volume's own "Année 1688" heading is the compiled minutes-series slot, not
necessarily this item's date).

1. **Web search.** `"Avis de Flandre" chiffre Clairambault 1161 Noailles Louvois 1688 espionnage` -- no hit
   identifying this item, no printed edition, no secondary literature (repeats and extends the 24 Sept query).
2. **Standard printed edition, opened and read.** Job brief names Rousset's *Histoire de Louvois* for 1688
   war-office correspondence. archive.org `histoiredelouvoi04rousuoft` (tome IV, covers into the 1690s, the
   Nine Years' War years) fetched in full (`_djvu.txt`, HTTP 200, 1.2MB) and grepped: control "Boufflers" 23
   hits (a Flanders-theatre marshal, confirms the OCR is readable and the volume covers 1688-era Flanders
   material at all); "1688" 30 hits; "Noailles" 14 hits, all read in context -- every one is the duc de
   Noailles's Roussillon/Catalonia command, not Flanders; "Avis de Flandre" 0 hits; "chiffre" 6 hits (none in
   a Flanders-intelligence context). No occurrence of this item. Acta Pacis Westphalicae not applicable (wrong
   war/period for this target). APW is for clair571/espagnol142, not this row.
3. **Community lists.** No Cryptiana page found via web search naming "Clairambault 1161" or "Avis de
   Flandre" (repeats 24 Sept finding; local `sources/cryptiana/` snapshot has no dedicated Louis-XIV Flanders
   page either, checked by directory listing). No Cipherbrain hit.
4. **DECODE.** `unsolved-ciphers/catalogue/decode-catalog.csv` (fresh clone, 25 Sept 2026) grepped for
   "clairambault 116", "avis de flandre", "noailles": zero hits for the shelfmark or the item title; several
   unrelated "Noailles" rows exist in the catalogue's plaintext-corpus files only (not cipher records).
5. **Bourdeau** (fresh shallow clone, 25 Sept 2026). Grepped for "clairambault 1161", "avis de flandre": no
   hit.
6. **Aymeloglu** (fresh shallow clone, 25 Sept 2026). Grepped for "clairambault 1161", "avis de flandre": no
   hit.

Requests this section: archive.org 2 (1 advancedsearch already run for target 1's edition family, reused; 1
new `_djvu.txt` fetch for Rousset tome IV). WebSearch 1. github.com 0 new (clones reused from target 1).

## Verdict (confirmed, LANE CX 2026-09-25)

Stays **open, low confidence**, gate now closed with a real edition read (Rousset tome IV, controlled). The
24 Sept pass's core blocker is unchanged: without a sender or date for "Avis de Flandre, chiffrés" beyond the
shared folio's 1570-1719 span, the correspondent-specific legs of the sweep (a dedicated edition, a calendar)
cannot be targeted precisely -- Rousset's negative here is a real but broad-brush check (Louvois's own
published administrative correspondence, not a Noailles family edition), not a close read of the right
volume. The image (folio 106 et suiv., not yet located per the 24 Sept access-route section below) remains
the fastest way to actually identify sender and date.

---

## M20 — BnF Clairambault 1161, "Avis de Flandre, chiffrés"

Check-solved pass, 24 September 2026 (LANE G check-solved worker, session per ROOM.md claim at 03:26 UTC).
Queue row: QUEUE.md M20. `date -u` read at session start: 2026-09-24 03:26 UTC.

### What is established

- Shelfmark BnF Clairambault 1161, ark:/12148/btv1b90010063 (confirmed live via Gallica SRU
  `gallica all "Clairambault 1161"`, 24 Sept 2026). The volume's own title (Gallica `dc:title`) is:
  "Volumes consacrés à l'histoire de l'Ordre du Saint-Esprit. I-CXX «Minutes du Recueil pour servir à
  l'histoire de l'Ordre et des commandeurs, chevaliers et officiers de l'Ordre du Saint-Esprit, par
  Clairambault,» classées dans l'ordre chronologique. LI Année 1688." — i.e. this is volume 51 of a
  120-volume chronological series of minutes on the Ordre du Saint-Esprit (a chivalric order), not a
  diplomatic-intelligence volume as such.
- The BnF finding aid (archivesetmanuscrits.bnf.fr, ark:/12148/cc137837/cd0e35310, "Clairambault
  1111-1239") gives the actual composite-item note for this volume. "Avis de Flandre, chiffrés" is
  **not** a standalone catalogued item with its own date/sender. It is one clause inside a single
  bundled note for "Fol. 106 et suiv.":
  > Anne-Jules, duc de Noailles ; Louis-Antoine de Noailles, cardinal archevêque de Paris ;
  > Adrien-Maurice, duc de Noailles, et François de Noailles, comte d'Ayen (« Discours sur la
  > présentation des lettres de commandement pour le Roy en la province de Languedoc pour...
  > Anne-Jules duc de Noailles..., par Me Henri de Burta, avocat au Parlement. » Impr. Toulouse,
  > L. Auridan, 1683, in-4° de 20 p. ; Arrêt du Parlement, du 4 juin 1698, concernant le même, impr.,
  > in-fol. ; son Oraison funèbre par le P. Delarue, impr. Paris, Josse, 1719, in-4° de 39 p. ; Mémoire
  > du même au Roi, avec pièces, 1704-1708 ; **Avis de Flandre, chiffrés** ; lettre orig. de François II
  > de Noailles, évêque de Dax, au marquis de Villars, 20 déc. 1570). [FRBNFEAD000013783_d0e14521]
  So the same folio range bundles printed pamphlets and manuscript letters spanning 1570-1719 for four
  different Noailles-family figures; "Avis de Flandre, chiffrés" has no sender, recipient or date of its
  own in the finding aid, and the volume's "Année 1688" heading is the chronological slot of the whole
  compiled volume in the Ordre-du-Saint-Esprit minutes series, not necessarily this item's date — the
  Jacqueton-lesson caveat QUEUE.md already flagged before this pass is confirmed, not resolved: we still
  do not know whose correspondence this is or when it was written.
- Gallica IIIF manifest (fetched 24 Sept 2026): 342 canvases, all labelled "NP" — no foliation encoded,
  the same defect LANE V hit on fr.3019 (24 Sept 2026 ROOM.md note: "manifest has no folio labels at
  all"). Canvas-to-folio calibration for this volume is **unresolved**.

### Six-source sweep (all dated 24 Sept 2026)

1. **Web search** (general + phrase-restricted): "Avis de Flandre" + Clairambault/1688/Noailles/espionnage
   — no hit identifying this item, no printed edition, no secondary literature.
2. **Sender's/recipient's printed correspondence**: not applicable — no sender is established (see above).
   Checked whether any of the four named Noailles figures have a printed *Mémoires* or correspondence
   edition that might carry this piece; not pursued further this pass because the item's date and author
   cannot yet be narrowed past "somewhere 1570-1719 in a Noailles family dossier."
3. **Calendars / comment threads**: none found via web search for this shelfmark.
4. **DECODE (de-crypt.org)**: not logged in — `DECODE_USER`/`DECODE_PASS` were still rejected as of the
   21 Sept 2026 log in CLAUDE.md and the single-attempt rule (good-citizen rule) means no further login
   attempt was made this pass. A site-restricted web search (`site:de-crypt.org Clairambault OR Montaigu
   OR "NAF 14913"`) returned no relevant record for either M20 or M21.
5. **Solver repositories**: fresh shallow clones of `dbourdeau/cyphersolver` and
   `aaymeloglu/unsolved-ciphers` (24 Sept 2026), grepped case-insensitively for "clairambault 1161",
   "avis de flandre", and "noailles". No hit on the first two; "noailles" appears only inside unrelated
   corpus/plaintext files (e.g. Napoleonic-era digitised sources used as language-model training text),
   not as a named cipher target in either repository.
6. **Tomokiyo's Cryptiana**: no page found via web search naming this shelfmark or "Avis de Flandre".

### Leaf viewed

One Gallica IIIF leaf viewed at full resolution (canvas index 105, a naive canvas+1="f106" guess,
**unverified** — see images/manifest.json). It shows an engraved printed portrait of "François de
Neufville de Villeroy, archevêque et comte de Lyon" with printed page numbers "137"/"83" in the margin,
confirming the volume interleaves unrelated printed matter with manuscript letters and that the naive
canvas-to-folio mapping does not hold for this volume. The actual "Avis de Flandre, chiffrés" leaf was
**not located** in this pass's request budget.

### Verdict

**Open, low confidence, not promoted.** Weakest of the five Clairambault survivors already flagged in
QUEUE.md (score 28, lowest). Six-source sweep found no prior solution, no prior discussion, and no
identifying sender/date — but for the same reason (no sender/date established), "unsolved" cannot yet be
verified with confidence either, since we do not know which printed edition to check. Not found in either
solver repository or (by web search only) in DECODE's catalogue.

**Before this can go on the board:** an access worker needs to (a) calibrate this volume's canvas-to-folio
mapping (the visible printed page numbers, e.g. "137" seen at canvas 105, may key off the Lauer catalogue's
own collation rather than manuscript foliation — worth checking Lauer's *Catalogue des manuscrits de la
collection Clairambault*, tome II, N° 782-1354, Gallica ark:/12148/bpt6k209158x, for volume 1161's own
description, which likely gives a fuller item list than the online finding-aid snippet) and (b) actually
view folio 106 et suiv. to determine whether "Avis de Flandre, chiffrés" is a genuine ciphertext, an
already-deciphered copy, or a fragment too short to attack.

### Access route

gallica.bnf.fr IIIF manifest + image endpoints, public domain, no login needed once the correct folio is
found. archivesetmanuscrits.bnf.fr finding aid, public, no login (browser_fetch.js needed — plain curl
gets a 500/altcha wall on this host consistently this pass; browser_fetch.js worked on both the reader
page and the finding-aid page on the first or second attempt, and on the IIIF `full/full` image endpoint
on the third attempt after two `,400`-thumbnail-size attempts returned "upstream request failed").

### Requests this pass (gallica.bnf.fr + archivesetmanuscrits.bnf.fr combined)

curl: 2 failed (500) direct page/ark fetch attempts, 1 SRU query (success), 2 failed manifest retries
(proxy `ws_closed_mid_exchange`, not a site block). browser_fetch.js: 1 reader-page fetch (success),
1 manifest fetch (success), 2 failed thumbnail-size image fetches ("upstream request failed", not
altcha/403), 1 successful full-resolution image fetch. archivesetmanuscrits.bnf.fr: 1 browser_fetch.js
page fetch (success). All one request at a time, >=1.5s apart, UA `cipher-lab research script (contact
via repository)` for curl / default Chromium UA for browser_fetch.js. No 403/altcha/Cloudflare challenge
seen from either host — the failures were a proxy-side connection reset (`ws_closed_mid_exchange`,
confirmed via `/__agentproxy/status`) and an intermittent "upstream request failed" on the IIIF image
tile service, not a bot block.

## Y3: transcription (25 Sept 2026, LANE R6)

Brief: LANE R6 Y3, disk-only transcription of the cipher leaf from `images/f106_full.png` (no Gallica
fetch). Viewed the image full-resolution (1280x1800 PNG, a two-page spread) before cutting any crops or
starting passes, per the brief's own escape clause ("if the image is too coarse to read... stop").

**Stopping this pass: the image on disk is not the cipher leaf.** It is confirmed (again, more
definitively than the 24 Sept note that first flagged it) to be a printed engraved portrait, not a page of
"Avis de Flandre, chiffrés":

- Left-hand page: blank, with only faint stains/foxing (no ink, no impression of writing visible at full
  resolution).
- Right-hand page: a printed oval-frame engraved portrait, captioned in Latin around the frame
  "FRANCISCVS DE NEVFVILLE DE VILLEROY ARCHIEP. ET COMES LVGD. GALLIAR. PRIMAS" (François de Neufville de
  Villeroy, archbishop and count of Lyon, primate of the Gauls), with an episcopal coat of arms below the
  frame, printed page numbers "137" and "83" in the top margin (two different pagination systems from the
  volume's compiled printed matter, matching the 24 Sept note), and a "Bibliothèque Royale" round library
  stamp. No manuscript text, no numerals, no cipher symbols, no interlinear gloss anywhere on either page.

This is not a resolution or coarseness problem — there is nothing cipher-shaped on this leaf to transcribe
at any resolution. It reconfirms the 24 Sept access-route finding: the naive canvas-to-folio mapping
(canvas index + 1 = folio number) used to fetch this image does not hold for this volume, and the actual
manuscript leaf "Fol. 106 et suiv." carrying "Avis de Flandre, chiffrés" (per the BnF finding aid) has
still not been located. `images/manifest.json`'s own fetch note already said as much; this pass adds a
closer visual confirmation (the full caption text and both page numbers, not just "a portrait was seen")
so a future access worker does not need to re-fetch and re-view this same leaf to rule it out again.

No crops were cut and no transcription passes were run: there is no ciphertext-bearing content on this
image to pass over, and fabricating a transcription of the printed Latin caption (or of nothing) would
misrepresent the target. Per the brief, no cryptanalysis and no new fetch were attempted either.

**Suggestion (one line, not actioned):** the next worker on this target needs a Gallica fetch (out of this
brief's scope: disk-only) to actually locate folio 106 et seq. in the true manuscript foliation — e.g. by
paging sequentially from a known-calibrated anchor canvas, or by checking Lauer's *Catalogue des
manuscrits de la collection Clairambault* (already flagged 24 Sept, ark:/12148/bpt6k209158x) for this
volume's own collation note, before any further transcription attempt.

Hosts touched this pass: none (disk-only, per brief). Requests: 0.

## Y7: leaf located (25 Sept 2026, LANE R6)

Brief: locate the true canvas for folio 106 (the start of the finding aid's "Fol. 106 et suiv." bundle
carrying "Avis de Flandre, chiffrés") by fitting canvas=a*folio+b from ink-foliation probes, then bisect
toward it. `date -u` at session start: 2026-09-25 16:57 UTC.

**Folio 106 is pinned.** The manifest's canvas labels are all "NP" (no foliation, as already logged), but
every leaf in this part of the volume carries the true archival foliation in cursive ink in the top-right
corner, distinct from a *second*, unrelated large reference number on the same corner (e.g. "137", "8925",
"9017", "9181"...) that belongs to some other old Clairambault-era numbering and does not track folio count.
Low-resolution top-right-corner probes (IIIF region crops, ~1-2 s apart, one at a time) at canvas indices
30, 60, 74, 100, 105, 118, 124, 128, 132, 142 gave **six independent exact matches** to the formula:

    true_folio (ink, cursive) = canvas_index_0based - 22

(canvas 105->folio 83, 118->96, 124->102, 128->106, 132->110, 142->120). This supersedes the naive
canvas+1=folio guess used for the 24 Sept `f106_full.png` fetch (Y-worker, "canvas_index+1"): that leaf is
actually **folio 83**, not 106 -- a Villeroy portrait, correctly identified as not-the-target back on 24
Sept, but for the wrong reason (it was read as "no relation at all" between canvas and folio; there is a
relation, just offset by 22, not 1). `images/manifest.json` is corrected accordingly and the file is kept,
relabelled, not deleted.

**True folio 106 = canvas_index_0based 128 (`f129` in the IIIF path).** Viewed at 1200px and at a
3400x3800 top-right crop: an engraved portrait in a plain oval frame, no caption text visible in the
crop -- not Villeroy (different frame style), not yet identified as one of the four Noailles figures the
finding aid names. **This is not the cipher leaf.**

**Cipher not found in an extensive sweep from folio 106 through folio 192 (canvas 128-216), 25+ points
checked, no gaps larger than 2 folios left unread in that span.** Full detail, canvas by canvas, is in
`images/canvas_sweep.tsv` (44 rows, corner + full-page reads). Summary of what *is* there, in physical
order:

| true folio (approx) | content |
|---|---|
| 106 | unidentified portrait, plain frame (start of the bundle) |
| 107-120 | "DISCOURS SUR LA PRESENTATION...ANNE JULE DUC DE NOAILLES..." (Toulouse, 1683) -- finding-aid item 1, plus biographical/genealogical continuation (Villeroy-family text bleeds in around folio 96-105, a *preceding*, unrelated bundle, not part of this one) |
| 121-143 | "ORAISON FUNEBRE DE ANNE JULE DUC DE NOAILLES PAIR ET MARESCHAL DE FRANCE" (Delarue, 1719, 39 pp.) -- item 3, with its own Approbation/Privilege du Roy end-matter (dated 1709, a reused older privilege) |
| ~144 | an unrelated verse fragment headed "1710" + a portrait-plate caption starting (Anne-Jules duc de Noailles, first of two copies in this volume) |
| 146-179 | "AU ROY / Sire / Le Marechal de Noailles..." and "Pieces Justificatives du memoire presente au Roy par M. le mareschal de Noailles..." (the M. de Bouillon arrerages/imposition dispute, Meyssac/Curenne certificates 1704-1708) -- item 4, Memoire au Roi avec pieces |
| 180-181 | two more portraits: an unidentified Spanish-costume figure, then Anne-Jules duc de Noailles again (second copy, full caption, dedicatory verse) |
| 182-187 | "DECLARATION DE MONSEIGNEUR LE DUC DE NOAILLES EN FAVEUR DES CATALANS...A Toulouse...M.DCC.X" (1710) -- a bilingual French/Spanish pamphlet, signed at Valladolid 25 Sept 1710 by the King and Don Pedro Caitano Fernandes del Campo. **Not named in the finding-aid item note at all.** |
| 188 | the Noailles-family miscellany ends mid-leaf; the volume's own titular content begins: "Promotion du 31 Decembre 1688 & jours suivans" -- a portrait/armorial gallery for the 1688 promotion of the Ordre du Saint-Esprit (Armand seigneur du Cambout, duc de Coislin, etc.), continuing at least to folio 192 (canvas 216) with no gap for a cipher letter |

No leaf in this range shows numeral-dense text (the one numeric-looking leaf, folio ~192, is an ordinary
accounts memorandum in livres/sols/deniers, not a cipher). Neither "Avis de Flandre, chiffrés" nor "lettre
orig. de François II de Noailles, évêque de Dax, au marquis de Villars, 20 déc. 1570" (finding-aid items 5
and 6) were seen, and there is no unaccounted gap of more than ~2 folios anywhere in folio 106-192 where a
short item could hide unnoticed -- the Noailles miscellany runs essentially gapless from folio 106 to its
own end at folio 188, then straight into unrelated promotion-portrait content.

**Conclusion: the finding aid's citation order (Discours, Arret, Oraison funebre, Memoire avec pieces, Avis
de Flandre chiffres, lettre orig. 1570) does not match this volume's physical binding order for the items
actually found** (Discours and Oraison funebre are in citation order; Memoire avec pieces follows correctly;
but the volume then contains an unlisted 1710 Catalans pamphlet and no trace of the last two listed items
before the bundle visibly ends). Either (a) "Avis de Flandre, chiffrés" and the 1570 letter are bound
earlier in the volume (unsampled: canvas 0-90/folio roughly -22 to 68, only spot-checked at c0, c10, c30,
c60 so far, all unrelated printed ephemera with a *different*, non-offset-22 numbering -- worth a systematic
sweep with the same corner-crop method), or (b) the BnF finding aid's composite note is simply wrong about
physical order (not uncommon for a "Recueil factice" catalogued long after assembly), and the two items are
elsewhere in the volume's 342 canvases (up to folio ~304), possibly among further Ordre-du-Saint-Esprit
promotion material past folio 192, which was not checked this pass.

**Not pinned. Suggestion for the next worker (one line, not actioned):** sweep canvas 0-90 (folio range
below the confirmed offset-22 zone, using the same corner-crop calibration method -- it may use a different
offset, since the numbering there did not match offset 22 at c10/c30/c60/c74) before assuming the item is
lost; if that also fails, a sweep past canvas 216 (folio 192+) through the rest of the promotion gallery
(up to ~canvas 342) is the remaining unchecked two-thirds of the volume.

Hosts touched: gallica.bnf.fr only, one request at a time, >=1.5-2s apart (curl, UA "cipher-lab research
script (contact via repository)"), ~63 requests (IIIF `info.json` x1, manifest.json x1, low-res/corner
probes and full-page reads at ~55 distinct canvases; 5 requests failed with a proxy-side connection reset
or 502/400, all retried at most once, consistent with the known `ws_closed_mid_exchange` proxy issue noted
24 Sept 2026, not a site block). No altcha/403/429 seen from Gallica. No native-resolution leaf was saved to
`images/` this pass (the target leaf was not identified with confidence, and none of the research-probe
images individually exceed the 30 MB folder cap, but were not committed to keep the folder clean --
`images/manifest.json` and `images/canvas_sweep.tsv` are the durable record).

## ZX2-GAL: sweep (25 Sept 2026, LANE ZX2)

Brief: sweep the two regions Y7 left unchecked -- canvas 216-342 (rest of the volume) first, then canvas
0-127 (the different, non-offset-22 numbering series) -- with 300-600px probes, pinning any leaf that shows
rows of numerals/signs or "Avis de Flandre"/a 1688 date. `date -u` at start: 2026-09-25 19:15 UTC.

**Canvas 216-342 (26 points sampled, step ~10 then bisected to ~5): all printed pamphlets, engraved
portraits, or plain-prose manuscript letters -- no cipher, no numeral-dense text, no Noailles/Flanders
content.** Content identified, in order: c217 portrait "Louis Marquis de Rochefort"; c222-232 a plain-prose
manuscript letter (2 mounted leaves, stained, no numerals); c237-267 a run of printed pamphlets for
"Oraison funebre...François Henry de Montmorency Duc de Luxembourg" (1695) with continuous internal
pagination bleeding across several unrelated-looking probe points (~110, ~139, ~210, ~365, ~377 -- multiple
distinct printed items bound together, not one continuous pagination); c272 a mounted plain-prose letter
fragment; c277 mounted wax-seal/signature clippings annotated "Rabel de Montmorency" (a genealogical-proof
dossier, not a letter); c282 a full-length portrait of the same Montmorency-Luxembourg marshal; c287 an
engraved monument/column; c292-307 more printed pamphlet pages (same Montmorency dossier, pagination series
continues ~265-577); c312-322 three plain-prose manuscript letters (one with an intact wax seal, one a
heavily corrected draft); c327-332 a printed 1576 royal declaration on "l'innocence de...Duc de Montmorency"
signed "Henry" with its seal description; c337 a manuscript fragment; c339 blank leaves near the volume's
end. One canvas (302) failed twice (connection reset by peer) and was not retried further per the one-retry
rule.

**Canvas 0-127 (27 points sampled, step ~8-10): same pattern -- entirely portraits and pamphlets for Order
of Saint-Esprit commanders, no cipher.** c15 a religious/royalist supplication pamphlet; c20 a portrait of
"Emanuel de Crussol Duc d'Uzès" explicitly captioned "Promotion du 31 Decembre 1688" -- the *same* 1688
Saint-Esprit promotion event already found starting at canvas ~212 (Y7's sweep), meaning this front block is
also part of the volume's own titular portrait gallery, not a separate dossier; c25/c35/c45/c50 further
Order-commander portraits (Gramont, an unidentified armored figure, one unread caption); c55-c78 a printed
"Factum pour Dame Hortence Mancini Duchesse Mazarin" pamphlet run (Mazarin-family testament dispute); c86-c121
a repeated portrait and "Oraison funebre" pamphlet for "François de Neufville Duc de Villeroy et de
Beaupreau" (the same Villeroy family already identified at canvas 105/128 by Y7, now confirmed to recur
here too); c126 a portrait of "Henry-François de Foix de Candale, Duc de Randan". Two canvases (40, 82)
each failed twice and were not retried further.

**Conclusion: negative for both regions.** Combined with Y7's prior canvas 128-216 sweep (Noailles-family
bundle, folio 106-188) and this pass's 53 new sample points across the remaining ~253 canvases (roughly one
every 5), the whole 342-canvas volume now has some coverage, and the picture is consistent throughout: this
recueil is a portrait-and-pamphlet gallery of Order du Saint-Esprit commanders and their family disputes/
funeral orations (Villeroy, Montmorency-Luxembourg, Mazarin/Mancini, Gramont, Crussol, Foix-Candale,
Rochefort), interrupted only by the one Noailles-family manuscript/print insert Y7 already mapped. No leaf
anywhere sampled shows rows of numerals or cipher signs, and "Avis de Flandre, chiffrés" / the 1570 Dax
letter were not seen. This does not rule out the two finding-aid items being digitised somewhere in the
~65 canvases still entirely unsampled (small gaps between this pass's probe points, plus canvas 1-14 and a
few single-digit gaps), but it makes it substantially less likely they sit anywhere outside the already-
identified Noailles bundle, and raises the same possibility already logged for the sister target
clairambault296 (Y4b): that a finding-aid citation does not track this volume's physical binding order at
all (here, two different old page-numbering series bleed across probe points in ways inconsistent with the
finding-aid's own citation sequence -- see the Montmorency pamphlet pages jumping non-monotonically, e.g.
c237~210/211 then c247~110/111).

**Not pinned. Status stays `open`, unchanged from the check-solved verdict above; the target remains the
weakest of the five Clairambault survivors (score 28) and still lacks a sender/date for "Avis de Flandre"
independent of the finding aid's own composite note.** Suggestion for a future worker (one line, not
actioned): the ~65 still-unsampled canvases (mostly small 3-5-canvas gaps between this pass's points, plus
c1-14) could be closed with a further bisection pass, but given the uniform negative result so far and this
target's low priority, that is better spent on a higher-scoring target unless the finding-aid access route
(Lauer's *Catalogue des manuscrits de la collection Clairambault*, already flagged 24 Sept, unread) is tried
first.

Hosts touched: gallica.bnf.fr only, one request at a time, >=2s apart, UA "cipher-lab research script
(contact via repository)". Requests: 53 (26 canvases in region 216-342: 13 step-10 + 13 bisection, with 5
connection-reset retries, one canvas (302) unresolved after its retry; 27 canvases in region 0-127: 18
probes + 5 retries, two canvases (40, 82) unresolved after their retry). No altcha/403/429 seen; all
failures were transient connection resets, one retry each, per the good-citizen rule. No native-resolution
leaf fetched (nothing pinned); probe images kept in scratchpad only, not committed, per the same practice
established on the sister target. `images/canvas_sweep.tsv` updated with all 53 new rows.

## Web and blog check (GF4-BATCH11, account-4, 3 Oct 2026)

Plain web searches (WebSearch, 3 Oct 2026). The item has no established sender, recipient or date, and no clear text, so the sender+date
and phrase queries use the finding aid's own words:
1. `"Avis de Flandre" chiffrés Clairambault 1161 Noailles` (descriptive title + family): BnF finding aids (Clairambault 1058-1110,
   1111-1239, 312-452), Wikipedia Noailles pages, unrelated pages. No discussion of the item.
2. `"Clairambault 1161" chiffre` (shelfmark + chiffre): company-register noise, Wikipedia/FranceArchives on Pierre Clairambault, Gallica
   records for Lauer's *Catalogue* tomes I and III and Clairambault's own 1727 *Inventaire*. Nothing on this item.
3. `Noailles 1688 avis de Flandre chiffre espion lettre` (sender family + volume date): FranceArchives Noailles items, an SHD Vincennes
   manuscripts list (galleys/bailli de Noailles 1677-89), Wikipedia. No decipherment or discussion.
4. Phrase query: the finding-aid string "Avis de Flandre, chiffrés" is query 1's quoted phrase; it has no other distinctive text.
Blog site searches: scienceblogs.de (`Paget 1713 Chiffre OR Clairambault OR Noailles Flandre`, run jointly with clairambault296) -- Catinat,
Soglia, Dorabella and other posts, none on Noailles, Flanders or Clairambault 1161; cryptiana.blogspot.com + cryptiana.web.fc2.com
(`"Avis de Flandre" OR Noailles cipher`) -- no indexed hit. Local snapshot sources/cryptiana/ grepped: "Avis de Flandre" 0,
"Clairambault 1161" 0. "Noailles" hits (elizabeth.htm, mary.htm, henryii/iii.htm, frencheastern.htm) are the 16th-century ambassadors Antoine, Gilles
and François de Noailles (1553-1570). One of them, François, is the bishop of Dax whose 20 Dec 1570 letter shares this folio note,
but those hits are Tomokiyo's ambassador ciphers, not this item. ciphermysteries.com (`Noailles Flanders cipher 1688`): no relevant hit.
Also grepped github.com/el-descifrador/cabinet-noir (Descifrado, *Cabinet Noir* v1.0, 29 Sept 2026, CC BY 4.0; shallow clone HEAD 47b6db9)
for "clairambault 1161", "avis de flandre", "btv1b90010063": 0. Its "noailles" hits are 1743 clear passages in loss-debrose-1742-1746
(a different item). Result: nothing found.

## Premise check (GF4-BATCH11, account-4, 3 Oct 2026)

- (a) Folder's own mentions -- not found. No decipherment, gloss or clear copy is mentioned anywhere in the folder. The only leaf image
  on disk (images/f106_full.png) is a Villeroy portrait at true folio 83 (Y3, Y7).
- (b) Other solvers' working files -- not found. Fresh shallow clones on 3 Oct 2026, cyphersolver (HEAD 4aedb40) and unsolved-ciphers
  (HEAD d2800bb), grepped for "clairambault 1161", "avis de flandre", "btv1b90010063": 0 in both. Cabinet Noir: 0.
- (c) Physical neighbours -- not found. Y7, ZX2-GAL and canvas_sweep.tsv sampled the whole 342-canvas ark (about 1 in 5 outside
  the Noailles bundle; folio 106-192 gapless). They found no cipher leaf and no clear copy, and neither the "Avis" nor the 1570 Dax letter. The item may be
  bound elsewhere or missing from the digitised volume. Lauer's *Catalogue des manuscrits de la collection Clairambault* tome II
  (Gallica bpt6k209158x) would give the volume's own item list; its texteBrut answered Gallica's altcha challenge to curl on
  3 Oct 2026 (1 request, not retried), and archive.org has no copy (advancedsearch `title:(collection Clairambault)`: 4 unrelated
  inventories). Unreachable from the cloud.
- (d) Recipient side -- not applicable / not found. No recipient is established. The war-office side for 1688 was read: Rousset, *Louvois*
  IV (LANE CX). There, the Noailles hits are Roussillon/Catalonia, not Flanders.
Result: no prior decipherment or print located; open, low confidence. This is a search result, not a novelty verdict (rule 10).

## Verdict (GF4-BATCH11, 3 Oct 2026)

**open** (unchanged, low priority). Edition read: Rousset, *Histoire de Louvois* IV (archive.org histoiredelouvoi04rousuoft, full text,
control "Boufflers" 23 hits): no "Avis de Flandre". Open web, the three blogs, both solver repositories and Cabinet Noir: nothing. Still
unlocated on the Gallica ark. Next step: Lauer tome II's entry for Clairambault 1161 (owner's browser, Gallica texteBrut), then the
~65 unsampled canvases.

## While waiting (GF4-BATCH11, 3 Oct 2026)

Waits on locating the leaf (Lauer tome II needs a real browser for Gallica's altcha; the unsampled canvases are a further Gallica pass).

- Close the ~65 unsampled canvases of ark btv1b90010063 (c1-14 and the 3-5-canvas gaps listed in images/canvas_sweep.tsv) at 300 px, one at a time, >=2 s apart. S, plain IIIF fetch.

Requests this pass: gallica.bnf.fr 2 (texteBrut, 1 redirect + 1 altcha page, stood down); archive.org 1 advancedsearch; WebSearch 3 (+2
blog searches shared with clairambault296); github.com clones shared with clair571.

Gate re-run (GF4-BATCH11, 3 Oct 2026): `clair1161-avis-flandre-1688: open (line 1) -- edition/page or full-text-search citation found within 6 lines` (exit 0).

## IMG-GALLICA1: leaf located (3 Oct 2026, account 2 worker for LANE-IMAGES)

Brief `.claude/briefs/runs/2026-10-03-acct2-img-gallica1.md`. Clock read 21:20 UTC at start.

**Availability flag quoted.** Gallica ark:/12148/btv1b90010063, IIIF manifest
`https://gallica.bnf.fr/iiif/ark:/12148/btv1b90010063/manifest.json` (342 canvases, every label "NP";
`tools/gallica_folio.py btv1b90010063 --list`, cached in sources/gallica-manifests/). Finding aid unchanged
(ark:/12148/cc137837/cd0e35310, "Fol. 106 et suiv.").

**Count correction.** The "~65 unsampled canvases" in the While-waiting line was an undercount: canvas_sweep.tsv
held 87 rows, which left 255 of 342 canvases with no row. Y7's "gapless" claim for c128-216 rested on folio
continuity, not on looking at every canvas. With a 5-call vision cap I took 80 in priority order: every
unsampled canvas in c129-216 (the finding aid's own bundle), then c1-14, then c218-229.

**Found: the cipher group is at canvases c185-c188 (IIIF f186-f189), inside the Noailles bundle.** Y7 and
ZX2-GAL had not sampled these canvases. Mounted 16th-century leaves, each with a BnF royal-library stamp:
- c185 right leaf: three paragraphs almost wholly in a pen-sign cipher, mixed with two-digit numerals and a few
  clear words. Ink "162" large, small number uncertain.
- **c186 right leaf, headed "Advis de flandres"**, ink "163" large and "185" small. Clear French paragraphs
  (l'Empereur ..., Arras et Boullongne ..., Angleterre ...), then a 9-line cipher block that opens "Les
  seigneurs ...". In the left margin beside the block is **a contemporary note in a smaller hand, about 12 short
  lines**. It may be a gloss of the block: not read and not tested. A clear closing paragraph follows.
- c186 left: the lower part of another mounted cipher leaf, about 10 lines.
- c187 left leaf, headed "Autres advis": about 30 lines, almost all cipher. c187 right leaf (ink "164" and "187"):
  two cipher paragraphs, about 32 lines.
- c188 left leaf: about 30 lines of cipher, a continuation.
- c188 right leaf: a clear letter, "Monsieur ...", dated Paris, [20?] décembre 1570, signed "Noailles e. d'Acqs".
  This is the finding aid's item 6 (François II de Noailles, évêque de Dax, au marquis de Villars,
  20 déc. 1570), so the "Avis" and the 1570 letter sit together, as the finding aid lists them.

The ink numbers on these leaves ("163", "185") do not follow the offset-22 formula (c186 - 22 = 164). That formula
is not re-checked here.

**Native fetch + line crops, c186 right leaf only** (the leaf with the heading):
`python3 tools/iiif_lines.py --ark btv1b90010063 --canvas 187 --region 3800,1300,3400,4650 --out
ciphers/clair1161-avis-flandre-1688/images --prefix c186R --debug`. Result: 23 bands x 2 segments = 46 crops
(`images/c186R_L*_s*.jpg`), source `images/src_ark_12148_btv1b90010063_f187_3800_1300_3400_4650.jpg`, and the
overlay `images/c186R_lines_debug.jpg`. I checked the overlay by eye: band edges fall between lines through the
cipher block. Some bands span a paragraph gap, and the marginal note's short lines share bands with the block. A
transcription pass should re-cut the margin with its own `--columns`. Manifest entries were written under
"iiif_lines".

**Native regions noted but not fetched** (folder size: the c186R leaf alone added about 7 MB). These are IIIF
`f` numbers, native px:
- f186 (c185) right: 4450,100,3150,4650
- f187 (c186) left: 100,50,3400,2000
- f188 (c187) left: 100,1200,3250,4450
- f188 (c187) right: 3950,50,3150,4650
- f189 (c188) left: 100,50,3150,4600
- f189 (c188) right, the clear 1570 letter: 3850,1200,3330,4750

**What was not done.**
- Contact sheets 4-5 were built but not viewed, because the vision cap was spent. They hold c193-215 gaps, c1-14
  and c218-229, and their rows in canvas_sweep.tsv read "not-viewed".
- 175 canvases outside c129-229 and c1-14 still have no row. They are less relevant now that the leaf is found.
- No transcription, no decoding, no reading of the marginal note.

**Leaf-locator blocker flipped.** ASKS 54 and the BnF quote-batch item 6 (ASKS 78) ask the BnF where the leaf is.
That question is answered from the digitised volume, so it is flagged to the parent in ROOM.md to drop it; I did
not edit the outreach draft.

Contact sheets (committed, each under 1 MB): `images/contact_sheets/sheet_c1161_{1..5}.jpg` (16 canvases each, at
300 px) and `c185-188_1200px_grid.jpg` (the four cipher canvases at 1200 px, with a 1000-px native grid).
Thumbnails were kept in scratch, not committed.

Requests: gallica.bnf.fr 86: 1 manifest, 80 thumbnails, 4 at 1200 px, and 1 native region. One at a time, at
least 2 s apart, with a descriptive UA. No 403, 429, altcha or reset. Vision calls: 5 (sheets 1-3, the c185-188
grid, the overlay).

## Next step (IMG-GALLICA1, 3 Oct 2026)

Fetch the remaining cipher leaves (regions above) with `tools/iiif_lines.py`, keeping the folder under 30 MB: about
7 MB per leaf, and the tool shrinks its src copies past 30 MB. Then two blind transcription passes per
TRANSCRIPTION.md. Run the intake gate first: the target is `open` and has had a check-solved pass and a Premise
check, and the marginal note on c186R should be read as a possible key source before any cryptanalysis.

## READ2-C1161 (3 Oct 2026, account 2 worker for LANE-READ2)

Brief `.claude/briefs/runs/2026-10-03-acct2-read2-c1161.md`. Clock 23:16 UTC at claim. Status moved `open` -> `partial`:
a cryptanalytic reading (grade S, no H) of c185R and the c186R block, checked against the leaf's own contemporary gloss.

**Route.** c186R: the native region already on disk (IMG-GALLICA1) re-cut locally with `tools/iiif_lines.py --image`:
margin note `--region 60,2580,640,1020 --prefix c186Rmarg` (13 crops), cipher block `--region 540,2540,2860,1180
--max-width 1500 --overlap 100 --prefix c186Rblk` (16 crops). c185R: `tools/iiif_lines.py --ark btv1b90010063 --canvas 186
--region 4450,100,3150,4650` (one native fetch), lines cut with `--centres` read by eye from the overlay (autocorrelation
found 7 of 24 lines) and `--top-margin 15 --bottom-margin 75 --max-width 1300 --overlap 100 --prefix c185R` (72 crops).
Requests: gallica.bnf.fr 1 (one native region, descriptive UA, no challenge). Folder 20 MB.

**Subagent calls (Sonnet): 5.** Gloss read 1; c186R block passes A, B; c185R passes A, B. Reconciliation of both leaves
by this worker from native half-leaf views (not a subagent call). Labels: `tx/labels_provisional.md` (c186R passes),
`tx/labels_v2.md` (settled from the c186R reconciliation, used for c185R).

**Per-leaf signs and error.**

| leaf | lines | cipher signs | err_2reader (pass A vs B) | single pass vs reconciled |
|---|---|---|---|---|
| c185R | 24 | 704 | 72/716 = 0.101 | not computed |
| c186R block | 8 | 220 | 22/239 = 0.092 | A 0.277, B 0.268 (67/242, 64/239) |

err_true not measurable: no benchmark item of this hand. The c186R pass-vs-pass figure is misleading: both passes shared a
crop-height bias (descenders cut, so crossed q read as '9' and line-initial signs dropped), which is why the c185R crops
were re-cut with a bottom margin. Look-alike pairs still unsettled: the hooked-top long-descender q vs `ls`
(passes split them, reconciled as q where they split); `S` in the c186R block merges two shapes (looped g-like and
open 5-like), split in neither leaf yet; `ss` in the c186R passes = two small s. A sorter focus list was not written
(the reading below now constrains these pairs better than a person's shape sort would; see Remaining gaps).

**The marginal gloss on c186R is the block's decipherment.** Read as clear text (one Sonnet pass + this worker's check):
`[le]s seigneurs a par[ticulier?] / ?x foys escript et mander / [a l]a royne quelle / n'est pas[se]... / ...beaucoup /
[de] chose quant au fet / [de l]a Religion en ce Royaulme / [ro]m de Espaigne sa / ...e ce peuple et gens / filz et
celle ... / ...nt commandee luy / [e]n grand Repoz.` Left letters are lost under the mount; lines 2, 4, 5, 9-11 are M.
Alignment with `tools/interlinear_align.py align --code-prefix @ --wildcard ?` (flat start): target 34 tokens agree,
shuffled-order controls 32-44 (8 seeds); its positive control, a synthetic 45-sign homophonic encipherment of the same
gloss at N=218, also reads at chance (32-39 at 0 error; 35-45 at 0.10/0.27), while a monoalphabetic control at 0 error
reads 167/196 -- so the tool has no power on this design at this N: a non-test, not a negative.

**design_prior** (`python3 tools/design_prior.py tx/stream_all.txt --no-write`, 909 tokens, 44 types): multi-sign
(homophonic/nomenclator/syllabary) d=0.13 plausible (envelope 0.39, null p05 0.19); letter-for-letter d=0.30 plausible;
mixed plausible; code d=1.64 excluded; shuffled-input false-positive rate 0.045; nearest keys willem-van-hessen-1567
key_1069 (homophonic), colbert26 f23 (nomenclator).

**First cheap test: homophonic family, fr16, N=924, K=49 (`tools/family_run.py ... --family homophonic --tokens space
--corpus tools/data/fr16 --param noise=0.10 --param profile=target`).** Rows in HYPOTHESES.md.

| run | control (3 seeds, mean) | target | judge |
|---|---|---|---|
| restarts 8 | 0.387 (0.141-0.787), below gate 0.6 | not run | - |
| restarts 32 | 0.749 (0.594-0.864), control scores -2140 to -2347 | best score -2281.4 | FAIL language -1.151 (null_p99 -1.72, real_p05 -0.924, median -0.816); words ok, cover 0.912 |
| restarts 32, target shuffled (seed 1) | same control | -2539.2 | FAIL -1.31 |
| restarts 32, target shuffled (seed 2) | same control | -2546.6 | FAIL -1.328 |

Judge output, pasted (`python3 tools/judge_plaintext.py specs/clair1161-avis-flandre-1688.json --file <decode>`):
```
FAIL language: score=-1.151, null_p99=-1.72, real_p05=-0.924, real_median=-0.816, mode=both, N=924
ok   words: cover=0.912, min=0.5, real_text_median_cover=0.958
FAIL - clair1161-avis-flandre-1688 (a PASS is a gate for a verifier, not a reading; rule 10)
```
The target's anneal score sits inside its matched control's range and ~260 points above the shuffled target; the shuffled
decodes do not pass the judge either, so the judge is not voided for this family at this N. The language FAIL is at a
blind anneal over a 0.10-0.27 error transcription, not a key-read text.

**Gloss check of the key (order-sensitive, can differ from its control).** The anneal key applied to the c186R block
reads `...a par?icul?? / fois / escript / ...royn? quelle laiss... passer en ... dissimulation ... beaucoup ... choses
... religion en ce royaul[me] ... [d]e Espaigne sauoi... ce peuple ... en plus grand repo...`. Letters of the gloss
matched in order by the decode (difflib matching blocks / 172 gloss letters): **0.593**; the same with 200 shuffled
keys: mean 0.187, p95 0.279, max 0.314. So the gloss is a period decipherment of this block, and the blind key agrees
with it far above chance.

**Reading (grade S, cryptanalytic; no H, no C tokens).** `key.tsv` (anneal seed 1, every value S) + `ciphertext.tsv` ->
`reading.txt`, `reading_tokens.tsv` by `python3 tools/decode_key.py ciphers/clair1161-avis-flandre-1688` (`--check` exit 0;
tokens 939: S 772, M 152, U 15 = the '/' marks). Gist of c185R, uncorrected anneal output read by eye (interpretation,
not a reading): news of "aultres prisonniers", "nouvelles", "laisse par ... tous", "beaucoup", "ennemis ... asseure",
"encore ... leurs", "entreprinse seraient par ... executee", "descouvertes", "confusion", "arreste par les",
"reportees a la cour", "ce qui sera execute", "a croire", "au roy", "le peuple", "justice", "dissimulation". Clear words
inside the cipher: "faire" (L05, L11, L15, L22) and "Et faut pre(n)sa puis" (L22). Per CLAUDE.md rule 7, a fresh
session must re-derive this from the spec and key before the orchestrator moves the target on.

Report what was found and where it was not found: no decipherment of these leaves was found in the sources checked
earlier in this file (check-solved, Premise check); this pass searched nothing new. Novelty is not classified here.

## Remaining gaps (READ2-C1161, 3 Oct 2026)
Read so far: 924 of an estimated ~2,500 cipher signs transcribed (c185R 704, c186R block 220; IMG-GALLICA1's line counts for the other four leaves), all decoded at grade S under an annealed key; 0 H, 0 C.
- c186L, c187L, c187R, c188L (about 100 lines) - blocker: not-attempted; regions in "IMG-GALLICA1" above, cut with --bottom-margin 75; next: fetch + 2 blind passes + reconciliation per leaf, then re-run the anneal on the pooled text, ~$6 per leaf
- the key itself (S only) - blocker: not-attempted; the c186R gloss now gives a period plaintext for 220 signs; next: a gloss-seeded key repair (fix the block's signs to the gloss letters, grade C, then re-anneal the rest with those fixed) with a shuffled-gloss control, ~$4
- look-alike pairs q/ls and the two S shapes - blocker: not-attempted; passes split them, reconciled by eye only; next: split them in the ciphertext and test which split raises the anneal score and the gloss match, ~$3
- left edge of the gloss under the mount - blocker: illegible; letters cut by the mount on every line (c186Rmarg crops)

## Escalation (READ2-C1161, 3 Oct 2026)
- [ ] siblings: the four other cipher leaves of the same "Avis" (c186L, c187L/R, c188L) untranscribed; next: transcribe and pool
- [x] clear-pages: the c186R marginal gloss is the block's decipherment (gloss match 0.593 vs shuffled-key p95 0.279)
- [ ] known-keys: no key on file matched yet; next: run tools/key_crossmatch.py against KEY-OFFICES.tsv for 1570 French chancery keys once the alphabet is settled
- [n/a] print: no printed edition of these Avis located by check-solved and Premise check
- [ ] key-rebuild: anneal key only; next: gloss-seeded repair as in Remaining gaps
- [ ] image-check: q/ls and S splits unsettled; next: split test as in Remaining gaps
- [n/a] retry: first anneal already read above its matched control
Verdict: keep going: 3 internal gaps; cheapest next: split test of q/ls and S, ~$3

## READ2-C1161B (3-4 Oct 2026, account 2 worker for LANE-READ2)

Brief `.claude/briefs/runs/2026-10-03-acct2-read2-c1161b.md`. Claim 23:57 UTC 3 Oct; disk only, no network, no subagent
calls. Pre-registration `tx/PREREG_glossctl.md` (commit 252c32a8, pushed before any control ran). Scripts:
`glossctl/glossctl.py` (statistic and controls; rows in `glossctl/results.tsv`), `glossctl/repair.py` (step 2; rows in
`glossctl/repair.tsv`). Both anneal steps ran serially, one at a time.

**Statistic re-implemented.** READ2-C1161's gloss-match script was not committed. Re-implemented as stated (difflib
matching blocks, autojunk off, block decode vs gloss letters of `align/pairs_c186R_v0.tsv`): the real key reads
**0.594** (101 of 170 gloss letters; READ2-C1161 reported 0.593 over "172"; the 2-letter denominator difference was not
traced). 0.594 was fixed as the target value before the controls.

**Step 1: harder controls. PASS (both required).**

| | value |
|---|---|
| target: real key.tsv, c186R block vs gloss | **0.594** |
| (a) same recipe (homophonic, anneal seed 1, restarts 32, fr16 3 files, N=924 K=49) on token-ORDER-shuffled ciphertext, shuffle seeds 1-20; each key applied to the UNshuffled block | max **0.312** (seed 13), mean 0.215, range 0.135-0.312 |
| (b) real key's block decode vs 200 random 170-letter windows of the same fr16 corpus (seed 1) | p95 **0.335**, mean 0.235, max 0.382 |

Shuffle seeds 1 and 2 reproduce READ2-C1161's two shuffled-target anneal scores exactly (-2539.2, -2546.6), so the recipe
is the same. A French-fluent key with no information about sign order matches the gloss at most at 0.312. A
correct-order decode matches unrelated French text at most at 0.382. The real key's 0.594 is above both. On this
evidence the block-gloss agreement is not explained by LM fluency or by generic French overlap. 
The anneal key carries sign-order information that the period gloss confirms.

**Step 2: gloss-seeded key repair (rule fixed in the pre-registration).** A global edit-distance alignment of the 220
block signs to the 170 gloss letters. A sign is fixed (grade C) when all its aligned occurrences carry one letter and it
has >= 2 of them, or 1 if the sign occurs only in the block. Then the full 924-sign stream is re-annealed with those
signs held (homophonic_anneal seed 1, restarts 32, fr16 order 3). Control: the same procedure with the gloss letters
shuffled within the gloss (3 shuffles).

| run | signs fixed | anneal score | block vs real gloss | c185R judge (fr16) |
|---|---|---|---|---|
| unrepaired key.tsv (READ2-C1161) | 0 | -2281.4 | 0.594 | FAIL language -1.155, cover 0.913 |
| **real gloss** | 6 (a=u, d=n, e=p, ee=y, p=c, sd=g; all six already had these values in key.tsv) | -2278.5 | 0.612 | FAIL language **-1.128**, cover 0.912 |
| shuffled gloss 1 | 3 | -2388.9 | 0.277 | FAIL -1.243, cover 0.936 |
| shuffled gloss 2 | 3 | -2345.8 | 0.182 | FAIL -1.177, cover 0.916 |
| shuffled gloss 3 | 2 | -2310.3 | 0.506 | FAIL -1.210, cover 0.891 |

c185R judge thresholds: null_p99 -1.70, real_p05 -0.949 (N=704). The real-gloss repair beats every shuffled-gloss repair
and the unrepaired key on the c185R judge. That meets the pre-registered "better" criterion, but the margin is small
(+0.027 over the unrepaired key) and the judge still FAILs. The strict fixing rule kept only 6 signs. All six agreed with
the blind key already, so the repair confirms them at grade C rather than correcting them. Holding them moved 10 free
signs: 8 l->d, K u->f, L b->n, c f->s, iib d->l, l r->s, phi s->l, tz l->e, vdash d->t, x a->s. A looser rule (majority
letter, >= 3 occurrences) was not run: it was not pre-registered. It is the next step below.

**Key and reading regenerated.** `key.tsv` = the real-gloss repair key (6 signs C with source the c186R gloss, 10 signs S
re-annealed with the old value in the source cell, the rest unchanged S). `python3 tools/decode_key.py
ciphers/clair1161-avis-flandre-1688` -> `reading.txt`, `reading_tokens.tsv`; `--check` exit 0 ("reading up to date").
Tokens 939: **C 97, S 675, M 152, U 15** (C = occurrences of the 6 gloss-confirmed signs on both leaves; U = the '/'
marks). Judge on the full 924-sign decode (`glossctl/repaired_full_decode.txt`):
```
FAIL language: score=-1.136, null_p99=-1.72, real_p05=-0.924, real_median=-0.816, mode=both, N=924
ok   words: cover=0.905, min=0.5, real_text_median_cover=0.958
FAIL - clair1161-avis-flandre-1688 (a PASS is a gate for a verifier, not a reading; rule 10)
```
(READ2-C1161's unrepaired key: -1.151 on the same 924.) The C grade covers 6 signs' values only. The gloss is read with
M lines and a cut left edge, so its own reading limits these.

NEAR.md row and status.json `near` entry added (rule 5). `python3 tools/near_check.py` exits 2 on one WARNING only, for
another target (blitz-ciphers, 48h window), and reports nothing for this row.

Report what was found and where it was not found: this pass searched no outside source; novelty is not classified here.

## Remaining gaps (READ2-C1161B, 4 Oct 2026)
Read so far: 924 of an estimated ~2,500 cipher signs transcribed (c185R 704, c186R block 220), decoded under the gloss-repaired anneal key: C 97, S 675, M 152, U 15 tokens; 0 H.
- c186L, c187L, c187R, c188L (about 100 lines) - blocker: not-attempted; regions in "IMG-GALLICA1" above, cut with --bottom-margin 75; next: fetch + 2 blind passes + reconciliation per leaf, then re-anneal the pooled text with the 6 C signs held, ~$6 per leaf
- the key beyond 6 C signs - blocker: not-attempted; the strict all-agree rule fixed only 6 signs (READ2-C1161B step 2); next: a pre-registered looser rule (majority gloss letter, >= 3 aligned occurrences) with the same shuffled-gloss control, ~$5
- look-alike pairs q/ls and the two S shapes - blocker: not-attempted; passes split them, reconciled by eye only; next: split them in the ciphertext and test which split raises the anneal score and the gloss match, ~$3
- left edge of the gloss under the mount - blocker: illegible; letters cut by the mount on every line (c186Rmarg crops)
- rule 7 re-derivation - blocker: not-attempted; reading changed this pass; next: a fresh session re-derives from the spec and key.tsv with tools/decode_key.py --check, ~$3

## Escalation (READ2-C1161B, 4 Oct 2026)
- [ ] siblings: the four other cipher leaves of the same "Avis" (c186L, c187L/R, c188L) untranscribed; next: transcribe and pool
- [x] clear-pages: the c186R marginal gloss matches the blind key at 0.594, above shuffled-order anneals (max 0.312, 20 seeds) and fr16 windows (p95 0.335)
- [ ] known-keys: no key on file matched yet; next: run tools/key_crossmatch.py against KEY-OFFICES.tsv for 1570 French chancery keys
- [n/a] print: no printed edition of these Avis located by check-solved and Premise check
- [ ] key-rebuild: gloss-seeded repair ran with the strict rule (6 C signs, c185R judge -1.128 vs shuffled-gloss -1.177 to -1.243); next: looser pre-registered rule
- [ ] image-check: q/ls and S splits unsettled; next: split test as in Remaining gaps
- [n/a] retry: anneal already reads above its matched control and both gloss controls
Verdict: keep going: 4 internal gaps; cheapest next: rule 7 re-derivation, ~$3
