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

## NEAR3-C1RD rule-7 re-derivation (4 Oct 2026)
Fresh session, read only the brief, CLAUDE.md rules 4 and 7, spec, ciphertext.tsv, key.tsv, decode_key.py --help (no decode.json exists; NOTES.md, HYPOTHESES.md, reading*, glossctl/ not opened before step 2 was written).
Convention used (from spec/key/decode_key help alone): clear words ([PLAIN:..]) and '/' are not cipher tokens; value and grade from key.tsv; conf != H downgrades to M; unkeyed = '?'/U.
Script: `rederive/rederive_c1rd.py` -> `rederive/rederive_c1rd.txt` (924 cipher tokens: C 97, S 675, M 152, U 0).

`python3 tools/decode_key.py ciphers/clair1161-avis-flandre-1688 --check`:
```
ciphertext.tsv: tokens 939: C 97, M 152, S 675, U 15
reading up to date
exit=0
```
(939 = 924 cipher tokens + 15 non-cipher rows graded U by the tool: the clear words and '/'.)

Diff against `reading_tokens.tsv` (opened after step 2), token by token on line, pos, sign, value and grade: 924 agree, 0 differ. Grades C 97 / S 675 / M 152 match the committed header.
Verdict: PASS (rule 7). This checks that the committed reading regenerates from ciphertext.tsv + key.tsv; it says nothing about whether the key is right (rule 10). key.tsv and the reading were not edited. Subagent calls: 0; requests: 0 (disk only).

## NEAR3-C1LOOSE (4 Oct 2026)

Account 2 worker for LANE-NEAR3, brief `.claude/briefs/runs/2026-10-04-ytbiz-near3-wave1.md`. Box 01:15-02:15 UTC; done 01:3x.
Disk only, no network, no subagent calls. Pre-registration `tx/PREREG_loose.md` (commit 32dd3ba0, pushed before any run).
Script `glossctl/loose.py` (imports `repair.align` and `glossctl` unchanged); rows `glossctl/loose.tsv`, log `glossctl/loose_run.log`,
keys `glossctl/loose_real_key.tsv`, `glossctl/loose_shufN_key.tsv` (column `unrepaired` = the value before any repair).
Tool shelf ("gloss-seeded key repair with a shuffled-gloss control"): nothing fits -- `key_repair.py` is retired (rule 3, Nassau)
and is a code-by-code repair without a gloss alignment; the other hits are running-key / seeded-code / key-order tools.
The procedure reuses READ2-C1161B's own `repair.py`.

**Setup as pre-registered.** Alignment = repair.py's edit-distance DP of the 220-sign c186R block to the 170 gloss letters, cost key
= the unrepaired READ2-C1161 key (rebuilt from key.tsv's "was 'x'" sources; checked: block vs gloss 0.594). Rule: >= 3 aligned
occurrences and majority letter >= 60%. Re-anneal homophonic_anneal seed 1, restarts 32, fr16 order 3, 924-sign stream. Control: same
procedure with the gloss shuffled within itself, seeds 1-10. Gate: real c185R judge > max of 10 shuffles AND > -1.128.

| run | signs held | held != unrepaired key | anneal score | block vs real gloss | c185R judge language (fr16, N 704) |
|---|---|---|---|---|---|
| **real gloss, loose** | 13 | 0 | -2277.4 | 0.588 | **-1.146** (FAIL; cover 0.908) |
| shuffled 1 | 5 | 0 | -2278.4 | 0.594 | **-1.130** (best control) |
| shuffled 2 | 8 | 3 | -2492.2 | 0.565 | -1.309 |
| shuffled 3 | 3 | 0 | -2277.9 | 0.588 | -1.143 |
| shuffled 4 | 5 | 0 | -2277.8 | 0.588 | -1.150 |
| shuffled 5 | 2 | 0 | -2350.4 | 0.288 | -1.179 |
| shuffled 6 | 4 | 0 | -2280.0 | 0.565 | -1.144 |
| shuffled 7 | 5 | 0 | -2278.7 | 0.588 | -1.145 |
| shuffled 8 | 4 | 0 | -2284.1 | 0.594 | -1.133 |
| shuffled 9 | 2 | 0 | -2278.7 | 0.600 | -1.133 |
| shuffled 10 | 3 | 0 | -2281.6 | 0.582 | -1.145 |
| strict real repair (READ2-C1161B, reference) | 6 | 0 | -2278.5 | 0.612 | -1.128 |

Thresholds: null_p99 -1.70, real_p05 -0.949. Shuffled controls: max -1.130, median -1.145, mean -1.161.

**Pre-registered outcome: FAIL.** Target -1.146 vs best control -1.130 (and vs strict -1.128): the real-gloss loose repair is below
both, and sits at the control median. Block vs gloss is also not higher than the controls (0.588 vs 0.565-0.600, excluding shuf5).

**Signs held (real gloss):** + = e (15/18), 4 = o (8/9), 9 = s (2/3), d = n (5/5), e = p (7/7), iii = e (5/6), p = c (3/3), qb = a (9/12),
th = s (5/7), w = i (5/6), wb = l (6/8), y = r (6/7), z = t (3/4). All 13 already had these values in the unrepaired key: as in the
strict run, the repair confirms, it corrects nothing. The strict rule's a = u, ee = y and sd = g fall below the >= 3 floor here.
**Signs that moved in the re-anneal (real gloss), from -> to:** 6r i->l, 8 l->d, K u->f, L b->i, c f->d, dia i->l, iib d->l, l r->n,
tz l->a, vdash d->t, x a->u (11). Per run in `loose.tsv` column `moved_vs_unrepaired`.

**What the controls show beyond the gate (read these before the pooled job).**
1. *The alignment cannot propose a correction.* Its cost is 0 only where the key already gives the gloss letter, so the majority
   letter of a sign's aligned occurrences is, in practice, the key's own letter: 9 of 10 shuffled glosses also held only signs whose
   value equals the key (column 4). A held set is a subset of the key's values chosen by a gloss-driven filter; it can raise or lower
   the anneal's free-sign choices, not fix a wrong sign. A third pass with a different threshold on this alignment would be the same
   instrument (rule 3, third-attempt clause): the next instrument is an alignment whose cost does not read the key (e.g.
   `tools/interlinear_align.py`'s hard-EM over the block/gloss pair, grade C from the gloss alone), or more glossed material.
2. *The same moves recur whatever the gloss.* 8 l->d, vdash d->t, iib d->l, K u->f, L b->*, l r->*, x a->*, tz l->* appear in the real
   run and in most shuffled runs. They are the anneal's own second basin once any few signs are held, not gloss evidence. That covers
   the 10 signs READ2-C1161B's strict repair moved (8 l->d, K u->f, L b->n, c f->s, iib d->l, l r->s, phi s->l, tz l->e, vdash d->t,
   x a->s), now in key.tsv at grade S: they carry no support from the gloss.
3. *The strict-rule margin is inside this 10-shuffle band.* The strict repair's -1.128 beat its own 3 shuffles (-1.177..-1.243), but
   three of these ten loose-rule shuffles reach -1.130, -1.133, -1.133. These are different-rule controls, so this does not formally
   re-test the strict rule, but with 10 seeds a +0.002 to +0.005 margin is not distinguishable from holding an arbitrary few key-agreeing
   signs. Suggestion for the lane (not done here, no brief): re-run the strict rule with 10 shuffles before the pooled job relies on
   the strict repair's 10 moved signs.

key.tsv and the reading were not touched. Recommendation for the pooled re-anneal: do not adopt the loose-rule key; treat the 10
strict-repair moves as unsupported by the gloss (S, same as any anneal value).

Report what was found and where it was not found: no outside source searched; novelty not classified. Requests: none (disk only).
Subagent calls: 0. Cost: see the lane ledger.

## NEAR3-C1SPLIT (4 Oct 2026)

Account 2 worker for LANE-NEAR3. Brief `.claude/briefs/runs/2026-10-04-ytbiz-near3-wave1.md`. Claim 01:15 UTC; runs 01:20-01:31 UTC
(container clock). Disk only, no network, no subagent calls. Two crop looks by this worker: the c186R block's 16 line crops
stacked, and a 53-snippet grid of the c185R `S`. Pre-registration `split/PREREG_split.md`, commit e6b33c38, pushed
before any run. Script `split/split.py`; occurrence assignment `split/assign.tsv`; rows `split/results.tsv`;
keys `split/<run>_key.tsv`. ciphertext.tsv, key.tsv and the reading are untouched.

**How each occurrence was assigned.**
- q/ls: pass B separates them. The 9 c185R occurrences reconciled as `q` where pass B read `ls` (7 q|ls, 1 S|ls, 1 p|ls in
  tx/c185R_rec/disagreements.tsv; L21's two columns are offset by one) became `qL`. The other 20 `q` are unchanged.
- S: neither pass separates them in the block (both write `S`). Assigned by eye from the stacked block crops: 7 open
  5-like -> `S5` (L03, L04 x2, L05, L06 3rd, L07 3rd, L08 2nd). 7 looped g-like stay `S`; the L07 2nd is graded M.
  The c185R snippet grid shows both shapes on c185R too, e.g. "+ S 4 S a" on L02, one of each. But the snippets were
  cut at x-positions estimated from token index. They were not reliable enough to label all 53 occurrences. So the S
  split was tested on the block only, and the 53 c185R `S` stay merged.

**Recipe.** Each run used homophonic_anneal.solve on the 924-sign stream: fr16 order 3, restarts 32, iters 40000,
seed 1, blind. The merged rerun reproduces key.tsv's anneal exactly: score -2281.4, gloss 0.5941, the
same as READ2-C1161 and READ2-C1161B. So the baseline is the current key's own recipe.

| run | K | anneal score | gloss match (c186R block) | c185R judge | new symbol's letter |
|---|---|---|---|---|---|
| merged (baseline) | 49 | -2281.4 | **0.5941** | **-1.155** | - |
| **qls split** (9 q -> qL) | 50 | -2360.7 | 0.3059 | -1.217 | qL = i, same as q (ls = e) |
| placebo-qls 1-5 (w, o, e, 9, p; 9 c185R occurrences each) | 50 | -2396.8, -2380.7, -2329.9, -2272.2, -2330.4 | 0.247, 0.165, 0.435, 0.582, 0.259; **p80 0.4353** | -1.222, -1.215, -1.157, -1.157, -1.169; **p80 -1.157** | - |
| **S split** (7 block S -> S5) | 50 | -2278.6 | 0.5824 | -1.143 | S5 = u, same as S |
| placebo-S 1-5 (+, 7, 4, th, qb; 7 block occurrences each) | 50 | -2343.8, -2314.9, -2368.1, -2322.6, -2324.3 | 0.112, 0.318, 0.200, 0.177, 0.271; **p80 0.2706** | -1.186, -1.200, -1.186, -1.228, -1.183; **p80 -1.186** | - |

(p80 = the 4th smallest of 5, as pre-registered.) judge thresholds on c185R: null_p99 -1.70, real_p05 -0.949 (N=704); every row FAILs the judge.

**Against the pre-registration.**
- q/ls: **FAIL**. The gloss match is 0.306, against 0.594 merged and 0.435 placebo p80. The c185R judge is -1.217,
  against -1.155 merged and -1.157 placebo p80. The split loses on both statistics, against both the baseline and the
  placebo.
- S: **FAIL**. The gloss match is 0.582, against 0.594 merged: it loses to merged by 0.012, though it beats placebo p80
  0.271. The c185R judge is -1.143, which beats merged -1.155 and placebo p80 -1.186. The gate needs both statistics,
  so the split fails.

**What else the runs show (not the gate).**
- In both real splits the anneal gave the new symbol the same letter as its parent: qL = q = i, and S5 = S = u. With
  one free letter more, the decipherment did not want to separate either pair.
- The S split stays close to the merged optimum: anneal score -2278.6 vs -2281.4, gloss 0.582 vs 0.594. Every S
  placebo falls far from it: scores -2315 to -2368, gloss 0.11-0.32. So treating the two S shapes as one sign is
  consistent with the key; a split of the same size elsewhere breaks it.
- The seed-1 anneal is sensitive to any change in the stream. 9 of 10 placebos and the qls split ended in a worse
  local optimum. That makes a single-seed comparison a coarse instrument. The pre-registration fixed seed 1, and no
  other seeds were run.

**Recommendation for the pooled re-anneal job: keep both pairs merged.** For q/ls this follows reconciliation's
choice, which was q. For the S shapes, keep one sign `S`. When c186L, c187L/R and c188L are transcribed, still record
the 5-like vs looped shape per occurrence (for example `S` plus a shape note). Then a pooled split test can be rerun at
higher N without another crop look. On c185R the shape is not recorded per occurrence. Recording it would need a
per-sign crop look, which this job did not do.

Report what was found and where it was not found: no outside source was searched; novelty is not classified here.

## NEAR3-C1TX-c186L (4 Oct 2026)

Account 2 worker for LANE-NEAR3, brief `.claude/briefs/runs/2026-10-04-ytbiz-near3-wave1.md`; clock 01:16 UTC at claim.
Written here, not in NOTES.md, per the brief (five clair1161 jobs in parallel); the lane folds it in.

**Leaf.** c186L = IIIF f187, left mounted leaf, native region 100,50,3400,2000 (ark btv1b90010063; NOTES.md "IMG-GALLICA1").
It is a whole short block, not only "the lower part" as IMG-GALLICA1 guessed from the thumbnail: **9 lines** of cipher
(2 lines, a gap, then 7 lines), no clear words, no heading or gloss visible in the region.

**Route and crop command** (pasted before any subagent call):
`python3 tools/iiif_lines.py --ark btv1b90010063 --canvas 187 --region 100,50,3400,2000 --out ciphers/clair1161-avis-flandre-1688/images --prefix c186L --bottom-margin 75 --debug`
found 10 bands, two of them wrong (a spurious band on the leaf's top edge, and the close-set first two lines -- pitch ~85 px
against ~140 px below -- merged into one centred on line 2's descenders). Re-cut from the cached source with centres read by
eye from the overlay: `... --centres 548,633,984,1126,1271,1394,1528,1668,1808 --top-margin 15 --bottom-margin 75
--max-width 1300 --overlap 100 --debug` -> 9 lines x 3 segments = 27 crops `images/c186L_L01..L09_s1..s3.jpg` + overlay
`images/c186L_lines_debug.jpg`, re-encoded JPEG q75 at the same dimensions (1.8 MB). The `src_*` native region was deleted
after cropping; its URL stays in `images/manifest.json` (each c186L entry carries a `source_file_note`). Stale manifest rows
from the first cut (L10) removed.

**Requests:** gallica.bnf.fr 1 (one native region, descriptive UA, no challenge). **Subagent calls (Sonnet): 2** (pass A,
pass B; each saw only the 27 crop paths and `tx/labels_v2.md`; B worked bottom-up). Reconciliation by this worker from 9
crop views (the third priced unit). Glyph atlas (TRANSCRIPTION.md step 2) not run: the brief names the line-read fallback
for this job; the family atlas belongs with the pooled job once all four leaves are cut.

**Signs and error.**

| | lines | signs | vs reconciled |
|---|---|---|---|
| pass A | 9 | 247 (raw) | 13/246 = 0.053 |
| pass B | 9 | 246 | 0/246 (see note) |
| reconciled `tx/c186L_rec.tsv` | 9 | **246** | -- |

**err_2reader = 13/248 aligned columns = 0.052** (`tools/reconcile_passes.py`, nw; 235 agree, 13 split; per line 0.889-1.000).
Below 0.10, so no look-alike pass was run. err_true not measurable: no benchmark item of this hand. Note: every one of the 13
splits was settled from the crop in B's favour (L05 col 8: B's extra `iii` kept), so "B vs reconciled = 0" is not an
independent accuracy figure; it says A's errors were mostly segmentation of compound signs (`z e` for one `K`, an extra `e`
after a `z`) and `z` for the blob-centred cross `dia` (3 of 13).

Settlements (line/col of `tx/c186L_rec/disagreements.tsv`): L01 9-10 `z e`->`K` (one sign); L01 26 A's extra `e` dropped;
L04 8 `e`; L04 24 `4`; L05 4 and 14 `dia`; L05 8 `iii` (the "um" after `to` = `w iii`, M); L06 4 `dia`; L06 20 `eloop` (same
shape as the agreed `eloop` later in the line, not `L`); L07 14 and L08 23 `iii` (three strokes with a bar; labels_v2 puts
barred and unbarred three-strokes under `iii` -- they may be two signs, see below); L07 21 `4` (M).

**Shapes outside labels_v2.**
- `s` (both passes wrote it as NEW: a small flat-topped s, mostly paired `s s` at line ends, and before `z` as `s z`):
  normalised to `s`, the symbol already in `tx/stream_all.txt` (21 occurrences) and `tx/c185R_rec.tsv`, which labels_v2's
  table omits. 7 occurrences (L01 x2, L04 x3, L05, L08).
- **`NEW1`** (provisional): a small v / rotunda hook followed by a long horizontal bar, `v—`. 3 occurrences: L03 col 1
  (line start), L05 col 5 (before `to`), L06 col 25 (before `eloop`); crops `c186L_L03_s1`, `c186L_L05_s1`/`s2`,
  `c186L_L06_s3`. It may be the `vdash` of c185R pass B (2 occurrences in stream_all, keyed `t` after READ2-C1161B) --
  not merged here; the pooled job or the sorter decides.
- For the split test / sorter: the three-stroke sign appears both bare (`iii`, L05, L07 col 13) and with a long bar through
  it (L07 col 14, L08 col 23); labels_v2 lumps them.

**Decode for information only** (`tx/c186L_decode_info.txt`, key.tsv as committed, ungraded, not a reading; NEW1 = `?`):
letter runs such as `aultres` (L01), `peuple` (L02), `princ` (L03), `port` (L04), `leurs` (L07), `encore`, `aussi` (L09)
appear unprompted; the rest is not word-segmentable. No judge run (not a reading).

**Not done:** no edit to `ciphertext.tsv`, `key.tsv`, `tx/stream_all.txt`, NOTES.md or NEAR.md (the pooled job merges);
no look-alike pass (err_2reader under 0.10).

## NEAR3-C1TX-c187L (4 Oct 2026)

Account 2 worker for LANE-NEAR3. Brief `.claude/briefs/runs/2026-10-04-ytbiz-near3-wave1.md`, job NEAR3-C1TX-<LEAF> with
LEAF = c187L. Clock: claim 01:15 UTC; reconciliation done by 01:25 UTC (box 60 min). Leaf: IIIF f188 (canvas c187) left leaf,
headed "Autres advis".

**Route.** `python3 tools/iiif_lines.py --ark btv1b90010063 --canvas 188 --region 100,1200,3250,4450 --out
ciphers/clair1161-avis-flandre-1688/images --prefix c187L --bottom-margin 75 --debug` (one native fetch). I checked the overlay
and a stack of every band by eye. L01 is the clear heading "Autres advis". L02-L17 are paragraph 1 (16 lines) and L18-L27 are
paragraph 2 (10 lines). Each band holds one whole line. The next line's tops show at the bottom edge, and the passes were told
to ignore them. The default segments overlapped by 1550 px (s1 x 0-2400, s2 x 850-3250), which invites double reading. So I re-cut
from the cached native file, with no second request, with `--max-width 1700 --overlap 150`. That gives s1 x 0-1700 and s2 x 1550-3250,
27 bands x 2 = 54 crops. The crops were re-encoded as grayscale JPEG q75 at the same dimensions (4.2 MB). The `src_*` native file was
removed from the folder and is not committed (sha1 kept in the worker's scratchpad). Its URL is in `images/manifest.json` under
`iiif_lines`. Requests: gallica.bnf.fr 1 (a native region, descriptive UA, no challenge).

**Tool shelf** (`tools/tool_shelf.py "transcribe a 16th-century French pen-sign symbol cipher from line crops"`). It offers
`glyph_atlas.py` (proven) first. Not used: the brief names line reads, as for c185R/c186R, and no atlas exists for this hand. On
the one benchmark where both were measured (Birago no.87), atlas top-1 read 0.162 against 0.040 for line reads (TRANSCRIPTION.md row 3).
TRANSCRIPTION.md asks for a family atlas before line reads when a key family has siblings. Building one for the six clair1161 leaves is
for the pooled job, not this one.

**Subagent calls (Sonnet): 3.** Pass A was 1 call. Pass B took 2 calls: the first call failed on an API safeguard error before
writing anything, and the second ran with the same prompt plus a one-line context sentence. Each pass saw only the crop paths
and `tx/labels_v2.md`, and the prompt is in this report's commit as `tx/c187L_pass_prompt.md`. I did the reconciliation from
the crops myself (5 composite views), with no subagent.

**Numbers.**

| item | value |
|---|---|
| lines | 26 cipher lines (L02-L27) |
| tokens reconciled | 725, of which 713 are cipher signs and 12 are clear words (PLAIN:) |
| err_2reader (pass A vs B, `tools/reconcile_passes.py`, nw) | 69/733 = **0.094** (under 0.10, so no look-alike pass was run) |
| single pass vs reconciled | A 38/728 = 0.052, B 39/731 = 0.053. Upper bounds: they count A's provisional NEW labels as differences. |
| confidence in tx/c187L_rec_long.tsv | H 685, M 40 |
| err_true | not measurable: no benchmark item of this hand |

Files: `tx/c187L_passA.tsv`, `tx/c187L_passB.tsv`, `tx/c187L_rec/` (reconcile_passes output), `tx/c187L_rec.tsv` (wide, same
columns as `tx/c185R_rec.tsv`), `tx/c187L_rec_long.tsv` (line/pos/sign/conf/note, with ids `c187L_Lnn` ready for the pooled
merge), and `tx/c187L_reconcile.py`, which holds every settlement with its reason and regenerates both rec files.

**Settlements and conventions** (each one is listed in `tx/c187L_reconcile.py`):
- Pass A's `NEW:5hook` (6x, always followed by z) is the small s of the `s z` pair that c185R already reads. It is settled as `s`.
- Pass A's `NEW:v-bar` (4x) is c185R's `vdash`. The L10 line-initial `NEW:triangle`, which both passes read, is c185R's `tri`.
  Both labels are already in key.tsv.
- `0` is written as `o`, following ciphertext.tsv, which has no `0`.
- `6r` is one sign, the "6z" shape: pass B's `6 z` was settled to pass A's `6r` 3x. The "6y" shape at L23 is kept as `6 7` (M).
- Pass A's `sqc` was pass B's `2` 6x. Each of these is the arc-hooked 2 of labels_v2, so it is settled as `2`. The true open
  square `sqc` (L06, L15, L26, where both passes agree) is kept.
- In this hand `p` is drawn with a crossbar through the stem. Pass B read two of these as `+ p` (L16), and pass A's single `p`
  was kept.
- Count shift: `2` occurs 9 times in 713 signs here against 1 in the 924 signs of c185R+c186R. Either this leaf uses the
  sign more, or the earlier leaves read it as something else. The pooled job should check this.

**New shapes:** `NEW1`, one occurrence. It is an open arc "(" at L24 pos 9, before `o th e`, on crop `images/c187L_L24_s1.jpg`
about x 830-900. Pass B read it as `2?`. It is not forced into an existing label.

**Clear words inside the cipher** (all grade M): L03 "pour" at the line end; L04 "Disant(z) cete ?ugte"; L08 "Cet Dandre?
fermeu?" at the line start; L18 a large initial plus "m", and "tout"; L27 "amou[r?]" at the line end.

**Decode for information** (`tx/c187L_decode_info.txt`). This is ungraded and not a reading. The leaf is decoded under the current
key.tsv, which was annealed on c185R+c186R only. This leaf took no part in fitting that key, but I did not run a control.
By eye, the output has runs of French: "aultres ...", "per secret", "espai[g]nol", "pretext", "plus",
"encore ... apres", "princip(a)ulx", "anllois", "trois". A held-out judge score of this decode with a shuffled-key control
would be a cheap check of the key. It was not in this brief, so I did not run it.

Not done (brief): ciphertext.tsv, key.tsv and tx/stream_all.txt were not edited. No lookalike pass was needed (err_2reader < 0.10).
No sorter focus list. The `S` shape merge and q/ls stay as in labels_v2 (NEAR3-C1SPLIT's question).

## NEAR3-C1TX-c187R (4 Oct 2026)

Account 2 worker for LANE-NEAR3. Briefs: `.claude/briefs/runs/2026-10-04-ytbiz-near3-wave2.md` (wave-2 change: crops plus overlay
must total <= 1.5 MB) and the wave-1 job NEAR3-C1TX-<LEAF> with LEAF = c187R. This section is written here, not in NOTES.md, per the
brief; the lane folds it in. Clock: claim at 01:34 UTC, reconciliation done at 01:42 UTC, box 60 min.

**Leaf.** c187R = IIIF f188, the right mounted leaf, native region 3950,50,3150,4650 (ark btv1b90010063; NOTES.md "IMG-GALLICA1").
It has **26 cipher lines**: paragraph 1 is L01-L08, and paragraph 2 is L09-L26. Paragraph 2 opens with a large initial and the clear
date "Juil 23". The leaf ends "... 6r q monsr", with "monsr" in clear script. Old foliation "164" and "187" are top right, and a BIBLIOTHEQUE ROYALE
stamp is below the text.

**Route and crop command**, pasted before any subagent call:
`python3 tools/iiif_lines.py --ark btv1b90010063 --canvas 188 --region 3950,50,3150,4650 --out ciphers/clair1161-avis-flandre-1688/images --prefix c187R --bottom-margin 75 --debug`
- The run found 29 bands. Three of them were not text: the folio number at y 69 and the stamp at y 4303 and 4578.
- The default segments overlapped by 1650 px.
- **Side effect, reverted.** With the native file on disk, the folder was over 30 MB, so the tool's size guard downscaled the
  *committed* `src_*` files of f186 and f187 (another leaf's sources) and rewrote their manifest entries. I restored both files and
  `manifest.json` from git and removed the `_ref1600` copies, so no other leaf's file changed. A lane should know that running
  `iiif_lines.py --out` into this folder while it sits near 30 MB touches other leaves' committed sources. Writing to a scratchpad
  `--out` avoids that.
- **Re-cut.** Row-ink profiles over the left, middle and right thirds show the lines slope up to the right by 60-90 px across the
  region. The tool's single centre at y 2831 fell between two lines. I re-cut into the scratchpad from a second native fetch (the
  first native file had been downscaled by the guard), using the middle-third centres:
  `... --out <scratchpad>/cut --prefix c187R --centres 358,469,598,721,843,976,1102,1230,1551,1677,1813,1937,2069,2187,2335,2457,2603,2727,2878,3028,3166,3309,3437,3583,3709,3851 --bottom-margin 75 --max-width 1700 --overlap 150 --follow-slope 400 --debug`
  This gave 26 lines x 2 segments = 52 sheared strips (s1 x 0-1700, s2 x 1550-3150), with drift fitted per line (-17 to -93 px).
  Every line was checked by eye on the reconciliation views. The two passes both read L07 and L08 as distinct lines.
- **Size.** Crops are committed as grayscale JPEG **q35 at the same dimensions**: q60 gave 2.41 MB and q40 gave 1.75 MB including
  the overlay. The overlay is resized to 1000 px, q50. The total is 1.43 MB. The `src_*` native file is not committed; each manifest
  entry carries its `source_url` and a `source_file_note`. q35 is legible at reading size (checked on L03_s2).
- **Folder.** Tracked files total 29.15 MB after c188L's crops (ad631ae3) and these. This is under the 29.5 MB line, but there is
  little room left for the pooled job.

**Requests:** gallica.bnf.fr 2 (native region twice, 2 s apart, descriptive UA, no challenge). **Subagent calls (Sonnet): 2.**
Pass A read top-down and pass B bottom-up. Each saw only the 52 crop paths and `tx/labels_v2.md`, through the prompt in
`tx/c187R_pass_prompt.md`. I did the reconciliation from 12 two-line composite views plus one single crop, with no subagent.

**Numbers.**

| item | value |
|---|---|
| lines | 26 |
| tokens reconciled (`tx/c187R_rec.tsv`) | 745: 740 cipher signs + 5 clear tokens (Juil, 23, toute x2, monsr) |
| err_2reader (A vs B, `tools/reconcile_passes.py --keep-plain`, nw) | **57/751 = 0.076**; 53/751 = 0.071 without the 4 notational `0`/`o` columns. Under 0.10, so no look-alike pass was run. |
| single pass vs reconciled | A 38/749 = 0.051, B 29/747 = 0.039. These are upper bounds: they count provisional NEW labels and `0`/`o` as differences. |
| confidence (`tx/c187R_rec_long.tsv`) | H 697, M 48 |
| err_true | not measurable: there is no benchmark item for this hand |

Files: `tx/c187R_passA.tsv` and `tx/c187R_passB.tsv`; `tx/c187R_rec/` (reconcile_passes output); `tx/c187R_rec.tsv` (wide, same columns as
`tx/c185R_rec.tsv`); `tx/c187R_rec_long.tsv` (ids `c187R_Lnn` for the pooled merge). `tx/c187R_reconcile.py` holds every settlement with
its reason and regenerates both rec files.

**Settlements and conventions** (all 57 are in `tx/c187R_reconcile.py`):
- **sqc, 7 occurrences.** A read `iib` and B read `sqc` 7 times (L05, L06, L14, L15, L20, L23). On the crop the sign is the small
  open square that follows `wb` almost every time ("wb ⊏"), so it was settled as `sqc`.
- **K, 6 occurrences.** A read `rot` and B read `K` for the ornate crossed "Rs" sign 6 times (L04, L12, L13 line-initial, L14,
  L18). It was settled as `K` (M). The "p⁸"-shaped crossed 8 at L06 and L11 (A `8`, B `rot`) was settled as `rot` (M), the same
  shape the passes agreed as `rot` at L25.
- **vdash, 2 occurrences.** The v-with-long-bar (L03 end, L12 start) is `vdash`, as in c186L NEW1 and c187L.
- **Crossed p.** A crossed `p` is one sign, `p` (L01, L02), following c187L.
- **Small looped l, 4 occurrences.** The small looped ℓ (L03, L12 x2, L16 initial) is `l` (M). The passes split it as `l`/`c`/`f`.
- **Smaller settlements.** L04's line-initial `th` was missed by A. The barred three-stroke at L04 is `iii`; c186L flagged barred and
  bare `iii` as perhaps two signs, and it is barred here too. L07's `tz` is a bar over a 3-body. L10's `th` carries a dot above (M).
  L18 col 22 is `eloop`, the same crossed loop the passes agreed as `eloop` at L12. L19 has no `+` between `4` and `d` on the crop.
  L26 col 23 is a barred `z`.
- **Notation.** `0` is written as `o`.

**New shapes** (provisional labels, not forced into labels_v2):
- **`NEW_c187R_2`, 3 occurrences:** an "xe"/fish ligature, an x-like crossing run straight into an e. It is at L22 col 24 (crop
  `c187R_L22_s2`, after `p`), L25 col 8 (`c187R_L25_s1`, after `p`) and L26 col 6 (`c187R_L26_s1`, after `th`). Pass A read `x e`
  each time, and pass B read `K`, `rot` and `K`. I set it as one sign because the stroke is continuous. It may be a K variant; the
  pooled job or the sorter should decide.
- **`NEW_c187R_1`, 1 occurrence:** a flat bar with an ink blob, at L04 col 25 (`c187R_L04_s2`, before `4 4 qb`). It may be a heavily
  inked sign or a blot.
- **`NEW_c187R_blot`, 1 occurrence:** a large ink blot covering one sign, at L20 col 5 (`c187R_L20_s1`, between `a` and `sqc`). It is
  illegible on this image.
- **Not new.** Neither c186L's NEW1 (it is `vdash` here) nor c187L's NEW1 (the open arc at L24) was seen as such on this leaf.
- **Recorded for the pooled job, not settled here:**
  - `s` (the 5-hook) occurs 4 times, 3 of them in `s z` (L08, L18, L20), as in c186L and c187L; `ss` occurs 6 times.
  - The arc-hooked `2` does **not** occur at all on c187R (0 in 740 signs). c187L had 9 in 713, while c185R+c186R had 1 in 924. So
    c187L's count stands alone.
  - `S` occurrences are not split by shape (NEAR3-C1SPLIT recommends keeping them merged).

**Clear words inside the cipher** (all grade M): L09 "Juil" with a large decorative initial, then "23", as a date heading for paragraph 2;
L17 and L24 "toute" (both passes partly read it as "tour"); L26 "monsr" at the line end. These were kept as `PLAIN:` tokens.

**Decode for information** (`tx/c187R_decode_info.txt`). It is ungraded and not a reading. The leaf is decoded under the current
key.tsv, which was annealed on c185R+c186R only. This leaf took no part in fitting the key, and no control was run. `ss` is split to
`s s`, and the NEW labels and `/` are left unkeyed.
- Runs of French show up unprompted: "ceulx" (L05, L06, L15, L23), "aultres" (L10, L17), "plus" (L11), "trois" (L09),
  "leur conseil et tout" (L20), "accroire" (L19), "conseil" (L20), "lesd ... ostel" (L26).
- The rest is not segmentable by eye.
- A held-out judge run of this decode against a shuffled-key control would be a cheap check. It was not in this brief, so I did not
  run it.

**Not done (brief):** no edit to ciphertext.tsv, key.tsv, tx/stream_all.txt, NOTES.md or NEAR.md. No look-alike pass (err_2reader
< 0.10). No sorter focus list. No glyph atlas: the brief names line reads, and the family atlas belongs with the pooled job.

## NEAR3-C1TX-c188L (4 Oct 2026)

Account 2 worker for LANE-NEAR3. Brief `.claude/briefs/runs/2026-10-04-ytbiz-near3-wave2.md` (job NEAR3-C1TX-<LEAF>,
LEAF = c188L), pointing to the wave-1 job of the same name. Clock: claim 01:35 UTC, reconciliation finished 01:52 UTC
(box 60 min). Written here, not in NOTES.md, per the brief; the lane folds it in.

**Leaf.** c188L = IIIF f189, left leaf, native region 100,50,3150,4600 (ark btv1b90010063; NOTES.md "IMG-GALLICA1").
It holds **27 lines** of cipher, continuous from top to bottom. There is no heading. The only clear writing is one small
word at the end of L14 ("curou?", read M). Below L27 the leaf is blank apart from the library stamp.

**Route and crops.**
- The crop command, pasted before any subagent call:
  `python3 tools/iiif_lines.py --ark btv1b90010063 --canvas 189 --region 100,50,3150,4600 --out
  ciphers/clair1161-avis-flandre-1688/images --prefix c188L --bottom-margin 75 --debug`.
  - It found 28 bands, with spurious centres at y 81 and 4568, so the bands straddled two lines.
  - **Side effect on other leaves' files.** Because the folder was over 30 MB on disk, the tool shrank two committed
    reference images from other leaves (`src_..._f186_...`, `src_..._f187_...`) to 1600 px "_ref1600" copies, and
    rewrote their manifest rows. It also downscaled this job's own native file. I restored both files and their manifest
    rows from git before committing. **The lane should know the tool does this whenever several leaves crop into one
    folder.**
- I fetched the region a second time into the scratchpad (not committed; sha1 dd16bb37cd08eaf2c35b4d955dcc62de31fa9a80).
  I re-cut it with centres set by eye: `python3 tools/iiif_lines.py --image <native> --out <scratchpad>/crops --prefix
  c188L --centres 280,420,600,720,850,990,1140,1260,1390,1530,1660,1800,1920,2050,2190,2330,2460,2580,2710,2850,2980,3130,
  3270,3400,3540,3670,3800 --top-margin 15 --bottom-margin 75 --max-width 1700 --overlap 150 --debug`.
  That gives 27 lines x 2 segments. The two blind passes read these crops (q95, in the scratchpad).
- **Those level crops were still wrong.** The lines on this leaf rise about 0.05-0.08 px per px to the right, some
  110-170 px across the leaf. A level band therefore holds its own line on the left, and on the right the end of the
  line cut at the top plus the next line in full. Both passes reported this.
- For the reconciliation I cut **slope-following crops** with `tx/c188L_slopecrop.py`. It tracks each line strip by
  strip on the ink profile and cuts 3 segments per line (x 450-1500, 1350-2400, 2250-3150), 81 crops.
- These are the committed crops: `images/c188L_L01..L27_s1..s3.jpg` plus an overlay of the boxes,
  `images/c188L_lines_debug.jpg`. They are grayscale JPEG q30 at native size, **1.34 MB** in all, under the brief's
  1.5 MB.
- The first-cut crops pushed in ad631ae3 are removed in this commit, along with their manifest rows. They can be
  regenerated with the commands above.
- The script reproduces the committed boxes exactly from the native region. The committed folder is about 27.8 MiB.

**Requests.** gallica.bnf.fr: 2. The first was the iiif_lines fetch; the second was a refetch after the tool had
downscaled its own copy. Both used a descriptive UA, with no challenge.

**Subagent calls (Sonnet): 2.** Pass A and pass B, run in parallel. Each saw only `tx/labels_v2.md` and the 54
level crop paths, with the prompt in `tx/c188L_pass_prompt.md`. Pass B worked bottom-up. I did the reconciliation from
27 three-segment line composites plus 4 detail views. That is the third priced unit; no third pass was run.

**Numbers.**

| item | value |
|---|---|
| lines | 27 |
| pass A / pass B signs | 730 / 750 |
| reconciled `tx/c188L_rec.tsv` | **752 cipher signs** + 1 clear word (PLAIN:curou?), conf H 634, M 119 |
| err_2reader, raw (`reconcile_passes.py`, nw) | 156/758 = 0.206 |
| err_2reader after `tx/c188L_signmap.tsv` (ε->e, 0->o, NEW:v-bar->vdash, NEW:triangle->tri: spelling, not reading) | **137/758 = 0.181** |
| of which one uniform convention split (A tz / B z on the same shape, every time) | 35; the rest 102/758 = 0.135 |
| pass vs reconciled (same sign map) | A 119/760 = 0.157 (35 of them the tz/z convention), B 63/762 = 0.083 |
| err_true | not measurable: no benchmark item of this hand |

Most of the split comes from the level crops, not from look-alike signs:
- L04 and L18 are 10 signs short in pass A, because the line's right half was cut off in its crop.
- Several splits are one sign that a pass read twice in the overlap.
- **One error was shared by both passes and so did not show up as a split.** Both gave L16's line end
  (`e wb S th w + a y th`) to L15 and left out L15's real end (`iii 7 7 th K w + S 9`). I fixed this from the slope crops
  (grade M, one reader).
- I checked every line end against the slope crops; the other 25 match the passes.

**Look-alike pass not run.** The brief asks for `tools/lookalike_pass.py` when err_2reader is over 0.10, but the tool
does not fit this leaf: it needs a blind sheet of sign tiles (glyph atlas) and a confusion table, and no atlas exists for
this hand. It also re-reads only tiles that look alike, while this split comes mostly from the line framing. I wrote the
residual questions as a sorter focus list instead (`tx/c188L_focus.tsv`, sid<TAB>question, 8 rows). No third full pass
was run.

**Settlements** (each is in `tx/c188L_reconcile.py` with its reason; 86 positional decisions, a tz/z rule and two
line-end corrections):
- **tz/z.** The shape is a barred z with a small raised loop on top. I settled all 35 as `z`, grade M, the label the
  earlier leaves use for this shape (c185R: z 48, tz 6; c187L: z 48, tz 1). Whether it differs from the plain barred z is
  focus row 1.
- **iii/iib.** Settled by stroke count where I looked. Barred three-stroke groups (iii) are the usual form
  (L02, L15, L16, L17, L22, L23), and a two-stroke `#` (iib) occurs too (L12 three times, L19). The two unviewed cases
  keep A (M). This is the same two-form question c186L raised.
- **The raised hook before q.** Pass A read f, pass B e or 7. I settled e (M where unclear), which is c187L's c/e
  convention.
- **`s z` pair** read as `s` (5-hook), as c186L and c187L did.
- **phi vs q** on the bowl with the stem through it: phi (M).
- **The e-looped K** at L07 and L17 is one sign, K (M).
- **A merged with B.** Pass B's `NEW:v-bar` (L25) = `vdash` and `NEW:triangle` (L25) = `tri`, the c187L conventions.
- **Signs dropped.** A's extra `a` before y at L02 and L05: the y glyph is drawn as a+y. Also overlap doubles at L05,
  L06, L08, L16, L20 and L23. The "ls" in L20 is L19's long-s descender.

**Shapes outside labels_v2** (provisional names; the c186L/c187L `NEW1` labels do not fit them):
- `NEW_c188L_1`: a closed D-loop under a long arched over-bar. 3 occurrences: L01 x2 (slope crop c188L_L01_s1/s2) and
  L19 (c188L_L19_s2).
- `NEW_c188L_2`: a small caret ^. 2 occurrences: L01 before `a` (c188L_L01_s3) and L17 before `S` (c188L_L17_s2).
  Pass B named it NEW:caret; pass A read `a`.
- `NEW_c188L_3`: a large open C enclosing a barred z. 4 occurrences: L05 (s2), L09 (s3), L11 (s3) and L24 (s1).
  - The passes read it as eloop, tz, or `eloop z`.
  - **L09 and L11 share the run `7 7 a sqc 3 7 NEW_c188L_3 y 4 q th`.**
  - In the information decode below it falls where a t would fit ("...rois" twice). In the current key, z = t. It may
    therefore be a form of z, but that is not settled.
- c186L's `NEW1` (v with long bar) is the `vdash` at L25 here. c187L's open-arc `NEW1` does not occur.

**Decode for information only** (`tx/c188L_decode_info.txt`). It is ungraded and not a reading: the leaf is decoded
under the current key.tsv, which was annealed on c185R+c186R only, and no control was run. decode_key's own count:
C 78, S 561, M 111, U 9 (the U are the NEW_c188L_* signs).
- Runs of French appear unprompted: "entreulx", "tous le", "conseil", "assisti", "pareile des", "plusieurs aultres",
  "persoune", "couuert", "eulx et", "croire".
- Much of the rest does not segment into words.
- A held-out judge score with a shuffled-key control would be the cheap check of the key on this leaf. It was not in
  this brief.

**Files:** `tx/c188L_passA.tsv`, `tx/c188L_passB.tsv`, `tx/c188L_signmap.tsv`, `tx/c188L_rec/` (reconcile_passes
output), `tx/c188L_rec.tsv` (wide), `tx/c188L_rec_long.tsv` (ids `c188L_Lnn`, line/pos/sign/conf/note),
`tx/c188L_reconcile.py` (regenerates both rec files), `tx/c188L_slopecrop.py`, `tx/c188L_focus.tsv`,
`tx/c188L_decode_info.txt`, `tx/c188L_pass_prompt.md`.

**Not done** (per the brief): no edit to ciphertext.tsv, key.tsv, tx/stream_all.txt, NOTES.md or NEAR.md; no judge
run; no third pass.

**Next step for the pooled job.** Before merging, re-read L15/L16 and the 119 M-graded signs against the slope crops,
or run two fresh blind passes on the slope crops (2 Sonnet calls at about the per-pass rate of this job), so that
err_2reader measures reading rather than framing.

## NEAR3-C1POOL (4 Oct 2026)

Account 2 worker for LANE-NEAR3, brief `.claude/briefs/runs/2026-10-04-ytbiz-near3-wave3.md`. Box 02:07-03:17 UTC (container
clock). Disk only for the statistics; 2 Gallica requests for the regen check of step 5. No subagent calls. Pre-registration
`tx/PREREG_pool.md`, commit 5329826a, pushed before any statistic. Script `pool/pool.py`; rows `pool/heldout.tsv`,
`pool/anneal.tsv`; keys `pool/key_*.tsv`.

**Material.** `pool/new_leaves.tsv` = the four TX reports' reconciled files, as transcribed: c186L 246, c187L 718, c187R 744,
c188L 759 = 2467 cipher signs. Notation only: `ss` written as two `s` rows (the c185R/c186R convention), `PLAIN:x` as
`[PLAIN:x]`, and the two leaf-local `NEW1` labels renamed `NEW_c186L_1` (v with long bar) and `NEW_c187L_1` (open arc), since
the reports describe different shapes. Every NEW* stays its own sign. No marginal gloss on any of the four leaves, so
`tools/interlinear_align.py` stays [retired] for this block.

**(a) Held-out test of the current key.tsv** (built on c185R + c186R only). Statistic: the fr16 judge model's language score
and word cover. Controls: (i) key.tsv on each leaf's order-shuffled signs, 20 seeds (p95 = 19th of 20); (ii) the 20
shuffled-ciphertext anneal keys `glossctl/key_shuf1..20.tsv` on the unshuffled leaves. Unkeyed NEW* -> '?' in every arm.

| set | signs (unkeyed) | real score | (i) p95 | (ii) max | real cover | (i) p95 | (ii) max | gate | judge |
|---|---|---|---|---|---|---|---|---|---|
| **pooled, 4 leaves** | 2467 (18) | **-1.268** | -1.581 | -1.425 | **0.897** | 0.816 | 0.863 | **PASS** | FAIL, real_p05 -0.910 |
| pooled, no c188L | 1708 (9) | -1.274 | -1.585 | -1.425 | 0.892 | 0.816 | 0.875 | PASS | FAIL, real_p05 -0.927 |
| c186L | 246 (3) | -1.310 | -1.562 | -1.350 | 0.918 | 0.819 | 0.926 | FAIL (cover) | FAIL |
| c187L | 718 (1) | -1.304 | -1.599 | -1.409 | 0.873 | 0.802 | 0.887 | FAIL (cover) | FAIL |
| c187R | 744 (5) | -1.233 | -1.547 | -1.404 | 0.903 | 0.836 | 0.884 | PASS | FAIL |
| c188L | 759 (9) | -1.254 | -1.550 | -1.358 | 0.908 | 0.840 | 0.884 | PASS | FAIL |

**Pre-registered outcome (a): PASS** on the all-four figure, and also without c188L. A key fitted on c185R + c186R reads the
four leaves it never saw better than the same key on shuffled order and better than any of 20 keys annealed on shuffled
ciphertext. The judge itself still FAILs every set (no real_p05 is met). c188L's figure carries its err_2reader 0.181; c187R
may carry the same slope framing (flagged in the c188L report, not re-transcribed here).

**Merge.** `ciphertext.tsv` gained the 2489 new rows (same columns): 3436 rows, 3391 cipher signs, 57 types. `tx/stream_all.txt`
regenerated (3391 tokens). `specs/clair1161-avis-flandre-1688.json` NOT edited: its stream stays the 924 signs, because
glossctl.py and split/split.py assert or shuffle that stream; the lane updates it before the next rule-7 re-derivation.

**(b) Pooled re-anneal** (homophonic_anneal restarts 32, iters 40000, fr16 order 3, 6 C signs held, q/ls and S merged; one
timing anneal 113 s, so restarts stayed 32).

| arm | seed / shuffle | anneal score | gloss match (c186R block) | c185R judge | c185R+c186R judge |
|---|---|---|---|---|---|
| real | 1 | -8760.8 | 0.565 | -1.219 | -1.199 |
| **real (best)** | **2** | **-8711.2** | **0.612** | **-1.225** | **-1.213** |
| real | 3 | -8735.9 | 0.582 | -1.217 | -1.204 |
| real | 4 | -8720.7 | 0.624 | -1.222 | -1.206 |
| real | 5 | -8711.2 | 0.612 | -1.225 | -1.213 |
| shuffled 1 (best of seeds 1-2) | s2 | -10167.4 | 0.212 | - | - |
| shuffled 2 | s1 | -10176.6 | 0.171 | - | - |
| shuffled 3 | s2 | -10157.0 | **0.265** (max) | - | - |
| shuffled 4 | s2 | -10149.1 | 0.188 | - | - |
| shuffled 5 | s1 | -10155.5 | 0.229 | - | - |

Current key.tsv (reference, NOTES.md READ2-C1161B): gloss 0.612, c185R -1.128, c185R+c186R -1.136. All 15 anneals ran
(02:12-02:43 UTC), each about 111 s.

**Pre-registered outcome (b): FAIL.** Condition (2) fails in every real seed: the best-score key (seeds 2 and 5 reach the
same optimum, -8711.2) gives c185R -1.225 (needed >= -1.128) and c185R+c186R -1.213 (needed >= -1.136). Condition (1) holds: real gloss 0.612 against a shuffle max of 0.265 (5 shuffles, 2 seeds each). Pooling
the new leaves pulls the anneal to a key that reads the original two leaves worse than the key fitted on them alone, while the
gloss match stays where it was (0.612, against 0.612 for the strict-repair key).

**key.tsv not changed.** The reading is regenerated for the merged ciphertext under the old key (new leaves' tokens S where
keyed, M where the token conf is M, U for NEW*): `python3 tools/decode_key.py ciphers/clair1161-avis-flandre-1688` ->
`ciphertext.tsv: tokens 3410: C 360, M 343, S 2670, U 37`; `--check` -> "reading up to date", exit 0. Judge on the full
3391-sign decode under the old key (`pool/full_decode_oldkey.txt`):
```
FAIL language: score=-1.232, null_p99=-1.753, real_p05=-0.934, real_median=-0.823, mode=both, N=3373
ok   words: cover=0.899, min=0.5, real_text_median_cover=0.959
FAIL - clair1161-avis-flandre-1688 (a PASS is a gate for a verifier, not a reading; rule 10)
```
The reading changed (ciphertext merged), so the lane briefs a rule-7 re-derivation; not done here.

**Reports folded.** `reports/NEAR3-C1RD.md`, `-C1LOOSE`, `-C1SPLIT`, `-C1TX-c186L/c187L/c187R/c188L` appended above verbatim
(checked by substring match against NOTES.md before deletion), then `reports/` deleted in the final commit.

**Folder size.** Tracked files were 29.3 MB, over the 29 MB line. `images_manifest_full.tsv` (378 files, sha1, source URL,
cited_by, status) written; the 72 c186R crop entries in `images/manifest.json` that had an empty `source_url` now carry the f186
region URL; `images/src_..._f186_4450_100_3150_4650.jpg` (regen byte-identical, sha1 checked) and
`images/src_..._f187_3800_1300_3400_4650.jpg` (same URL regenerates with different JPEG entropy coding, 2512638 vs 2512838 bytes;
the original stays in git history) deleted. Tracked size now about 24.6 MB.

Requests: gallica.bnf.fr 2 (regen check, descriptive UA, 2 s apart). Subagent calls: 0. Report what was found and where it was
not found: no outside source searched; novelty not classified. Cost: see the lane ledger.

## Remaining gaps (NEAR3-C1POOL, 4 Oct 2026)
Read so far: 3391 cipher signs transcribed, every cipher leaf and block IMG-GALLICA1 names (c185R 704, c186R block 220, c186L 246, c187L 718, c187R 744, c188L 759; the earlier ~2,500 estimate was low), decoded under the unchanged key.tsv: C 360, S 2670, M 343, U 37 tokens; 0 H.
- the key beyond the 6 C signs - blocker: not-attempted; the pooled re-anneal (seeds 1-5, 6 C held) FAILed its c185R judge gate (-1.225 vs -1.128); no glossed material on the four new leaves, so gloss-alignment instruments stay retired; next: tools/key_crossmatch.py against KEY-OFFICES.tsv for c.1570 French chancery keys, ~$2
- c188L framing errors (err_2reader 0.181) - blocker: not-attempted; slope framing, tx/c188L_focus.tsv 8 rows; next: two fresh blind passes on the committed slope crops, then reconcile, ~$4
- c187R slope check - blocker: not-attempted; c188L's report flags the same line slope on c187R; next: compare c187R level vs slope-following crops on 3 lines, ~$1
- new shapes NEW_c186L_1, NEW_c187L_1, NEW_c187R_1/_2, NEW_c188L_1/2/3 and iii barred vs bare - blocker: not-attempted; 18 unkeyed occurrences; next: owner sign sorter pass or a per-shape split test at pooled N, ~$3
- left edge of the gloss under the mount - blocker: illegible; letters cut by the mount on every line (c186Rmarg crops)
- spec stream - blocker: not-attempted; specs/clair1161-avis-flandre-1688.json still carries the 924-sign stream; next: lane updates the spec before the rule-7 re-derivation, ~$0.5

## Escalation (NEAR3-C1POOL, 4 Oct 2026)
- [x] siblings: c186L, c187L, c187R, c188L transcribed (2467 signs) and merged; held-out test of the old key PASSes on them (pooled -1.268 vs controls max -1.425 / p95 -1.581; cover 0.897 vs 0.863 / 0.816)
- [x] clear-pages: the c186R marginal gloss matches the blind key at 0.594, above shuffled-order anneals (max 0.312, 20 seeds) and fr16 windows (p95 0.335)
- [ ] known-keys: no key on file matched yet; next: run tools/key_crossmatch.py against KEY-OFFICES.tsv for 1570 French chancery keys
- [n/a] print: no printed edition of these Avis located by check-solved and Premise check
- [retired] key-rebuild: gloss-alignment instruments retired for this block by rule 3 third-attempt clause: strict repair (READ2-C1161B), loose repair (NEAR3-C1LOOSE), interlinear_align.py (READ2-C1161 tool_shelf, control at chance); pooled re-anneal FAILed its own gate (NEAR3-C1POOL)
- [ ] image-check: c188L framing and c187R slope unsettled, seven provisional new shapes; next: two fresh blind passes on c188L slope crops
- [n/a] retry: pooled re-anneal ran five seeds; a sixth seed of the same recipe is not a different instrument
Verdict: keep going: 5 internal gaps; cheapest next: spec stream update, ~$0.5
## N4-C1 (4 Oct 2026)

Account 2 worker for LANE-NEAR4, brief `.claude/briefs/runs/2026-10-04-ytbiz-near4-wave1.md` (job N4-C1). Claim 04:16 UTC, box
to 06:06 UTC (container clock). Pre-registration `tx/PREREG_two_instr.md` (commit ed52489f, pushed before either statistic).
Scripts `two/two_instr.py` (instrument 2, agreement, grading, the Noailles shape-key test), `tx/c188L_rerec.py` (c188L re-pass merge).

**Dating and the slug.** The "1688" in the slug is the volume's chronological slot ("Année 1688", the 31 Dec 1688 Saint-Esprit
promotion that follows the bundle; Check-solved and Y7 above), not the item's date. The cipher leaves sit in the Noailles bundle
beside c188R, a clear letter signed "Noailles e. d'Acqs", Paris, [20?] Dec 1570 (IMG-GALLICA1; seen again on the committed 1200 px
grid this pass). The spec's own date ("c. 1570, by the neighbouring clear letter; the item itself is undated") stands. The slug is a
catalogue artefact; it is not renamed here (folder renames touch every register).

**1(a) Leaves.** On `images/contact_sheets/c185-188_1200px_grid.jpg`: c185L is a clear "Copie du Certificat" of 27 Aug 1707 (no
cipher); c188R is the clear 1570 letter (a short clear note in its left margin, no cipher run). Two new 1200 px views (gallica.bnf.fr
2 requests, descriptive UA, 2.5 s apart, both 200): **c184 (IIIF f185)** is two clear pages of 1707 certificates (Meyssac,
"Gaffard", foliated 161 and "2733"), no cipher; **c189 (IIIF f190)** is a faded verso, foliated 166, carrying only show-through of a
clear letter, a stamp and a few pen strokes; no cipher. No continuation of the cipher run on either side: the group is c185R-c188L.

**1(b) c187R slope check.** NEAR3-C1TX-c187R already cut c187R with `--follow-slope 400` (drift fitted per line, -17 to -93 px), so the
committed crops are the slope crops. Checked by eye on three lines' right halves (L03_s2, L14_s2, L22_s2) and one left half (L22_s1),
stacked in one view: each crop holds one whole line, centred, ascenders and descenders inside, neighbours cut at the edges only;
L03_s2 ends "... 4 o +", the overlay's line end. Framing does not differ from what a slope cut gives, so no re-pass (c187R
err_2reader 0.076 stands). No subagent call, no request.

**1(c) c188L re-pass.** The NEAR3 crop step was already run and committed (`tx/c188L_slopecrop.py`, 81 slope crops), so the passes
read those committed crops; the prompt is `tx/c188L_slope_pass_prompt.md` (3 segments per line; tz written only when the raised
loop is seen). Subagent calls (Sonnet): 2, pass C top-down and pass D bottom-up, run in parallel. Neither saw the earlier passes or
the reconciled file.

| item | value |
|---|---|
| pass C / pass D signs | 748 / 759 |
| **err_2reader C vs D** (`tools/reconcile_passes.py`, nw, sign map `tx/c188L_signmap2.tsv`: ε->e, 0->o, caret->NEW_c188L_2, triangle->tri) | **64/760 = 0.084** (was 0.181 with the level-crop passes A/B); target <= 0.10 met |
| three-way, C + D + NEAR3 reconciled (`tx/c188L_rec3/`) | 683 of 766 columns agree in all three; 83 differ, 10 of them three ways |
| merged `tx/c188L_rec2_long.tsv` (`tx/c188L_rerec.py`) | 750 cipher signs + 1 clear word, H 573 / M 178; differs from NEAR3's reconciled file at 16 positions |
| each pass vs merged | C 713/751 = 0.949, D 721/761 = 0.947 |

- The merge rule was fixed in the script's docstring before it ran: a 2-of-3 majority over C, D and NEAR3's file. Where all three
  differ, NEAR3's eye-settled sign is kept. A sign is H only where all three agree at H.
- Seven of the 10 three-way columns are the raised hook (f/c/e, settled e as before) or NEW_c188L_3 (ee/z/C-z). The other three
  are th/phi/dia and +/dia/th at L05 and L08, and tz/d/D-loop at L01.
- **tz vs z (focus row 1).** Both fresh passes were told to write tz only where they saw the raised loop. They wrote z 40 and 53
  times, tz only 2 and 4. That supports NEAR3's settlement as z. The question matters for reading, since key.tsv has z=t and tz=e.
- **L02 start.** The committed crop `c188L_L02_s1` frames L01 and cuts L02 at its bottom edge, as pass D reported. I checked this on
  a stacked L01-L03 view. Both fresh passes lost L02's first signs. NEAR3's `6r y +` is kept at M: the cut tops are consistent with it.
- **Merged into ciphertext.tsv.** The c188L rows were 760 and are now 758: `ss` is written as `s s`, the pool.py convention, and
  each row carries the note `N4-C1 re-pass: ...`. ciphertext.tsv now holds 3434 rows and **3389 cipher signs, 57 types**.
  tx/stream_all.txt is regenerated. The spec stream is updated to these 3389 signs (gap "spec stream"). The old 924-sign stream is
  kept verbatim as `ciphertext_v1_924`, because glossctl.py reads `ciphertext` and its rows were run on the 924. Folder: see the
  done line.

**2. Two instruments (PREREG `tx/PREREG_two_instr.md`, pushed ed52489f before any statistic).**
- Instrument 1 = key.tsv: the strict-repair key, fitted on c185R and the c186R block.
- Instrument 2 = a blind homophonic anneal on the four non-training leaves only (c186L, c187L, c187R, c188L; N 2465, K 54).
  Recipe: fr16 order 3, restarts 32, iters 40000, seed 1, nothing held. It never saw c185R, the block or key.tsv.
- Control = the same recipe on the four-leaf stream order-shuffled, shuffles 1-5.
- Statistic A = token-weighted agreement of the two keys over the six-leaf stream. It excludes the 6 C signs and any sign either
  key lacks: 2989 tokens, 40 types.
- The anneals ran 04:26-04:28 UTC, four at a time, about 73 s each. Rows are in `two/anneal.tsv` and `two/agree.tsv`.

| key compared with key.tsv | anneal score | A (tokens) | A (types) | A on c185R+c186R only (823 tokens) |
|---|---|---|---|---|
| **instrument 2, real seed 1 (pre-registered)** | -6397.9 | **0.624** | 0.375 (15/40) | 0.603 |
| real seed 2 (stability only) | -6626.0 | 0.288 | 0.175 | 0.267 |
| real seed 3 (stability only) | **-6300.9** | 0.565 | 0.275 | 0.566 |
| shuffled 1 / 2 / 3 / 4 / 5 | -7160.6 / -7158.5 / -7214.8 / -7180.2 / -7176.4 | 0.351 / 0.148 / 0.034 / 0.280 / 0.033 | 0.15 / 0.10 / 0.05 / 0.15 / 0.05 | 0.322 / 0.129 / 0.034 / 0.256 / 0.035 |

**Gate: PASS**, 0.624 vs shuffled max 0.351.
- A key annealed only on the four leaves that key.tsv never saw gives the same letter as key.tsv for the 15 most-shared signs. They
  cover 62% of the tokens, well above what sign frequency alone gives (shuffled order: 0.03-0.35).
- **Caveats, read with the gate.**
  - Seed sensitivity is large. Seed 2 fell into a worse basin, at score -6626 and A 0.288, inside the control range.
  - Seed 3 reached a better anneal score than seed 1 (-6300.9). It agrees with key.tsv on some signs that seed 1 does not: 7=i,
    th=s, z=t. It disagrees on others where seed 1 agrees: S, 4, q.
  - The pre-registered single seed decides the grades. A 3-seed consensus instrument would be a different, stricter rule. It was
    not pre-registered, so it is not applied.
- Of the 6 C signs, instrument 2 agrees on 3 (a=u, d=n, e=p) and differs on 3 (ee y/i, p c/t, sd g/i). Their C grade comes from
  the gloss and is unchanged.

**Grades applied** (`python3 two/two_instr.py grade`; each source cell carries the N4-C1 note and instrument 2's letter):
- key.tsv now has **S 15, M 28, C 6**.
- The S signs are + e, 3 e, 4 o, 9 s, S u, box a, f n, iii e, q i, qb a, s e, tri q, w i, wb l, y r. Instrument 2 gives a different
  letter for each of the 28 M signs, or has none for it. The M signs include 7, th, z, p, o, phi, ls, iib, eloop, 6r, 8 and K.
- `python3 tools/decode_key.py ciphers/clair1161-avis-flandre-1688` gives `tokens 3408: C 353, M 1325, S 1697, U 33`.
- `--check` gives "reading up to date", exit 0.
- Per leaf (C/S/M/U):

| leaf | C | S | M | U |
|---|---|---|---|---|
| c185R | 74 | 304 | 326 | 2 |
| c186R | 23 | 104 | 93 | 13 |
| c186L | 34 | 140 | 69 | 3 |
| c187L | 70 | 404 | 243 | 3 |
| c187R | 81 | 386 | 272 | 7 |
| c188L | 71 | 359 | 322 | 5 |

  U counts the clear words and `/` as well as the unkeyed NEW_* shapes.
- Before this pass, every non-C keyed sign was S on one anneal alone. 1325 tokens now drop to M. **No letter value changed.**

**3. Judge (fr16).**
- Why fr16 and not fr17: the 1570 dating holds. The leaves are mounted in the same bundle as the dated 1570
  Dax letter. Nothing on the leaves points to the 1688 slot. fr16 = Catherine de Medicis and Marguerite letters, the same decade
  and the same court-letter register (rule 3 era note).
- `python3 tools/judge_plaintext.py specs/clair1161-avis-flandre-1688.json --file ciphers/clair1161-avis-flandre-1688/reading.txt`:
```
FAIL language: score=-1.3, null_p99=-1.751, real_p05=-0.913, real_median=-0.823, mode=both, N=3913
ok   words: cover=0.878, min=0.5, real_text_median_cover=0.957
FAIL - clair1161-avis-flandre-1688 (a PASS is a gate for a verifier, not a reading; rule 10)
```
  The judge folds reading.txt's line ids ("c185R_L01" ...) into the letters, hence N 3913. The clean letters-only decode of the
  3389 signs (`two/full_decode.txt`) gives:
```
FAIL language: score=-1.233, null_p99=-1.758, real_p05=-0.905, real_median=-0.82, mode=both, N=3375
ok   words: cover=0.901, min=0.5, real_text_median_cover=0.957
FAIL - clair1161-avis-flandre-1688 (a PASS is a gate for a verifier, not a reading; rule 10)
```
- **Period gloss through the same judge** (rule 3 period-gloss paragraph). The c186R marginal gloss is 170 letters, from
  `align/pairs_c186R_v0.tsv`. It scored against the c186R block decode under key.tsv and three letter-shuffles of the gloss:

| text | N | language score | judge |
|---|---|---|---|
| c186R gloss (period clear text) | 170 | **-0.808** (real_p05 -0.975, null_p99 -1.60) | **PASS** |
| c186R block decoded under key.tsv | 220 | -1.154 (real_p05 -1.002, null_p99 -1.629) | FAIL |
| gloss letter-shuffled, seeds 1/2/3 | 170 | -1.993 / -1.864 / -1.981 | FAIL |

  Unlike ZX-DEC349, the leaf's own period text scores at the judge's real-prose median. So the judge is calibrated for this
  register at this length, and the decode's FAIL is not a corpus artefact. It reads as what the grades say: a key right on its
  frequent signs (S), wrong or unsettled on many others (M). The decode sits about midway between the gloss and the shuffled nulls.

**4. Known keys.**
- `tools/key_crossmatch.py --help` was read. The tool matches code labels, and neither folder's labels are shared with ours: ours
  are private pen-sign names (tx/labels_v2.md). fr16142's key.tsv is Tomokiyo's table worded as glyph descriptions, and
  fr16142's `run2/nxaln/key_learned.tsv` uses atlas cluster ids (k000...), with its own gate FAIL. A label-level sweep could only
  report "coverage < 0.5". KEY-OFFICES.tsv has no Noailles/Dax row (grep 0). fr3151-noailles-1558 and fr3151-seure-1558 have no key
  file. So the pre-registered shape-level test was run instead.
- **The test.** 16 glyphs were matched by description between Tomokiyo's fr16142 table (Noailles, bishop of Dax, Constantinople
  Dec 1571-1574) and labels_v2. The statistic counts how many of them carry Tomokiyo's letter in key.tsv (`two/tomokiyo.tsv`).
- **Result: 2/16** (e = p, ls = e). The permutation null over key.tsv's values (10,000, seed 1) has mean 0.76 and p99 3, with
  P(null >= 2) = 0.18. Instrument 2: 1/16. **Gate: NO FIT.**
- On the worded descriptions, the Constantinople key's letters are not this key's letters. Tomokiyo's table image, which is not on
  disk, is the authority; this FAIL is conditional on the worded glyph descriptions.
- The two alphabets share shape stock: caret, fish, triangle, D-loop, a crossed iii, 7, 4. Sign values, though, are what a key
  is, and those do not match.
- Before writing the mapping, I had seen several key.tsv values in this file's earlier sections. The mapping was fixed from shape
  words only, and it gives our key 2 matches.

**Gist (interpretation, not a reading).** This reads the S and C letters of the decode by eye, with M letters filling gaps. It is
not graded and not checked against any source.
- c185R: news of "les aultres prisonniers", an enterprise ("entreprinse ... seraient par ... executee"), "beaucoup", things
  "descouvertes" and "reportees a la cour", "ce qui sera execute", "a croire", "au roy", "le peuple", "justice", "dissimulation".
- c186R block, consistent with its own gloss: letters written several times to the queen, the matter of "la religion en ce
  royaulme", Spain, the people, "en plus grand repos".
- c187R (headed by the clear date "Juil 23"): "avoir", "ceulx", "aultres", "leur conseil et tout", "pensions", "au roy" and
  "a croire" again, "soldats"(?).
- In English: intelligence reports, in cipher, on prisoners, a planned enterprise and its discovery, reports carried to the court,
  religion in the kingdom and relations with Spain, and the state of the people. The c186R clear heading, "Advis de flandres", names
  them as news from Flanders.

Report what was found and where it was not found:
- No outside source was searched beyond the two Gallica thumbnails. Novelty is not classified.
- Requests: gallica.bnf.fr 2.
- Subagent calls: 2 (c188L passes C and D). The reconciliation was this worker's own unit.
- Cost: see the lane ledger.

## Remaining gaps (N4-C1, 4 Oct 2026)
Read so far: 3389 cipher signs on all six cipher leaves/blocks (c185R 704, c186R 220, c186L 246, c187L 718, c187R 744, c188L 757), decoded under key.tsv with two-instrument grades: C 353, S 1697, M 1325, U 33 tokens; 0 H.
- 28 M-graded key signs (7, th, z, p, o, phi, ls, iib, eloop, 6r, 8, K ...) - blocker: not-attempted; the two instruments disagree on them and seed 3 agrees with key.tsv on 7, th, z where seed 1 does not; next: a pre-registered multi-seed consensus instrument 2 (seeds 1-10 on the four leaves, majority letter per sign) with the same shuffled-order control, ~$3
- rule 7 re-derivation of the merged reading - blocker: not-attempted; reading grades and c188L changed this pass; next: a fresh session re-derives from the spec and key.tsv with tools/decode_key.py --check (LANE-NEAR4 briefs it), ~$3
- new shapes NEW_c186L_1, NEW_c187L_1, NEW_c187R_1/_2, NEW_c188L_1/2/3 and iii barred vs bare - blocker: not-attempted; 33 U tokens incl. clear words; next: owner sign sorter pass or a per-shape split test at pooled N, ~$3
- left edge of the gloss under the mount - blocker: illegible; letters cut by the mount on every line (c186Rmarg crops)

## Escalation (N4-C1, 4 Oct 2026)
- [x] siblings: all six cipher leaves/blocks transcribed and merged; c184 and c189 checked, no continuation (N4-C1 1a); c188L re-passed to err_2reader 0.084
- [x] clear-pages: the c186R marginal gloss matches the blind key at 0.594 (shuffled max 0.312); the gloss itself PASSes the fr16 judge (-0.808), the decode FAILs (-1.233)
- [x] known-keys: fr16142 Noailles (Dax) Constantinople key, shape-level test 2/16 vs permutation p99 3, NO FIT (N4-C1 4); no other Noailles/Dax key on disk or in KEY-OFFICES.tsv
- [n/a] print: no printed edition of these Avis located by check-solved and Premise check
- [ ] key-rebuild: two-instrument agreement PASS (0.624 vs shuffled max 0.351) graded 15 signs S; next: multi-seed consensus instrument for the 28 M signs
- [ ] image-check: seven provisional new shapes; next: sorter or split test as in Remaining gaps
- [n/a] retry: a further single-seed pooled anneal is not a different instrument
Verdict: keep going: 3 internal gaps; cheapest next: rule 7 re-derivation, ~$3

## RUN3-C1161R7 (4 Oct 2026)
Fresh rule-7 re-derivation (account 1, LANE-RUN3) from the spec, key.tsv and ciphertext.tsv only: spec stream is the
merged 3389-sign stream (token-identical to ciphertext.tsv minus clear words); `tools/decode_key.py` regenerates
reading.txt and reading_tokens.tsv byte-identically (C 353, S 1697, M 1325, U 33; 0 H); `--check` exit 0. SAME, not
sent back. Details: RD7-2026-10-04-run3.md; regenerated copies in rederive/run3_reading*.

## Remaining gaps (RUN3-C1161R7, 4 Oct 2026)
Read so far: 3389 cipher signs on all six cipher leaves/blocks (c185R 704, c186R 220, c186L 246, c187L 718, c187R 744, c188L 757), decoded under key.tsv with two-instrument grades: C 353, S 1697, M 1325, U 33 tokens; 0 H. Rule-7 re-derivation done (SAME, RD7-2026-10-04-run3.md).
- 28 M-graded key signs (7, th, z, p, o, phi, ls, iib, eloop, 6r, 8, K ...) - blocker: not-attempted; the two instruments disagree on them and seed 3 agrees with key.tsv on 7, th, z where seed 1 does not; next: a pre-registered multi-seed consensus instrument 2 (seeds 1-10 on the four leaves, majority letter per sign) with the same shuffled-order control, ~$3
- new shapes NEW_c186L_1, NEW_c187L_1, NEW_c187R_1/_2, NEW_c188L_1/2/3 and iii barred vs bare - blocker: not-attempted; 33 U tokens incl. clear words; next: owner sign sorter pass or a per-shape split test at pooled N, ~$3
- left edge of the gloss under the mount - blocker: illegible; letters cut by the mount on every line (c186Rmarg crops)

## Escalation (RUN3-C1161R7, 4 Oct 2026)
- [x] siblings: all six cipher leaves/blocks transcribed and merged; c184 and c189 checked, no continuation (N4-C1 1a); c188L re-passed to err_2reader 0.084
- [x] clear-pages: the c186R marginal gloss matches the blind key at 0.594 (shuffled max 0.312); the gloss itself PASSes the fr16 judge (-0.808), the decode FAILs (-1.233)
- [x] known-keys: fr16142 Noailles (Dax) Constantinople key, shape-level test 2/16 vs permutation p99 3, NO FIT (N4-C1 4); no other Noailles/Dax key on disk or in KEY-OFFICES.tsv
- [n/a] print: no printed edition of these Avis located by check-solved and Premise check
- [ ] key-rebuild: two-instrument agreement PASS (0.624 vs shuffled max 0.351) graded 15 signs S; next: multi-seed consensus instrument for the 28 M signs
- [ ] image-check: seven provisional new shapes; next: sorter or split test as in Remaining gaps
- [n/a] retry: a further single-seed pooled anneal is not a different instrument
Verdict: keep going: 2 internal gaps; cheapest next: multi-seed consensus instrument for the 28 M signs, ~$3

## RUN3-C1161MS (4 Oct 2026)
Account 1 worker for LANE-RUN3, brief `.claude/briefs/runs/2026-10-04-acct1-run3-wave2.md`. Claim 09:06 UTC. Pre-registration
`tx/PREREG_consensus.md` (pushed 00c7cec4 before any anneal); script `two/consensus.py` (pushed e1427a95 before scoring); outputs
`two/cons/` (60 keys, `anneal.tsv`, `consensus.tsv`, `signs.tsv`). Disk only, no network, no subagent calls.

**Instrument.** N4-C1's instrument 2 recipe (four non-training leaves, N 2465, K 54, fr16 order 3, restarts 32, iters 40000), seeds
1-10; per sign the majority letter, kept as the consensus letter only at n >= 6 of 10. Control: the same 10-seed consensus on each of
the five order-shuffled four-leaf streams (50 anneals). Statistic A_cons = token share (six-leaf stream, C signs out) whose consensus
letter equals key.tsv; no consensus counts as disagreement. Why the control can differ: shuffling keeps every sign's frequency but
destroys the order the anneal's n-gram model reads, so control letters agree only as far as frequency rank explains and its seeds
need not agree with each other (it did move: 0.000-0.122). Anneals 09:08-09:26 UTC, four at a time, about 70 s each.
Determinism: fresh seed 1 reproduces `two/key_real_s1.tsv` exactly; seeds 2 and 3 reproduce N4-C1's scores (-6626.0, -6300.9).

| consensus (10 seeds, n >= 6) | A_cons tokens | A_cons types |
|---|---|---|
| **real** | **0.334** | 0.140 (6/43) |
| shuffled 1 / 2 / 3 / 4 / 5 | 0.000 / 0.000 / 0.024 / 0.122 / 0.000 | 0.000 / 0.000 / 0.023 / 0.047 / 0.000 |

**Gate: PASS**, 0.334 vs shuffled max 0.122 -- but a much weaker instrument than its single-seed form (0.624): the ten real seeds
spread over anneal scores -6300.9 to -6626.0 and reach a strict majority on only 13 of 43 keyed non-C signs.

**Per-sign result for the 28 M signs** (full table `two/cons/signs.tsv`):
- **M -> S: 1 sign, `7` = i** (219 tokens; real consensus i 7/10; 0/5 shuffled controls give i at n >= 6). This is the sign N4-C1
  noted seed 3 agreed on.
- Consensus contradicts key.tsv: `2` (key r, consensus t 6/10, 10 tokens), `tz` (key e, consensus l 6/10, 20 tokens). Stay M; values
  not changed (pre-registered).
- No consensus (top letter below 6/10): the other 23 present signs, incl. `th` (top s 5/10 = key), `z` (top t 5/10 = key), `rot`,
  `eloop`, `ls`, `o`, `phi`, `iib`, `6r`, `8`, `K`. `th` and `z` miss the threshold by one seed. Absent from the four leaves:
  `Sorn`, `blot`, `spiralG`.

**Information only, not acted on (pre-registered): the consensus contradicts three current S signs.**
- `qb` (key a, 187 tokens): consensus e, 8/10.
- `4` (key o, 224 tokens): consensus e, 6/10.
- `S` (key u, 275 tokens): consensus n, 6/10.
- These three S grades rest on seed 1 alone (N4-C1's pre-registered rule), and seed 1 sits in a minority basin on them. Of the 15 S
  signs the consensus agrees on 5 (+, 9, w, wb, y), contradicts 3, and has no majority on 7 (3, box, f, iii, q, s, tri). Treat those
  S grades as single-seed S: a reviewer should not read them as stronger than that.

**Grades applied** (`python3 two/consensus.py score --apply`): key.tsv S 16, M 27, C 6. `tools/decode_key.py`: tokens 3408: C 353,
S 1908, M 1114, U 33 (was S 1697, M 1325). **No letter value changed**; reading.txt differs only in its grade-count header line, and
reading_tokens.tsv only in the grade column of the `7` tokens. `--check`: "reading up to date", exit 0. Because the grades changed,
a rule-7 re-derivation of the regraded reading is owed (letters are unchanged, so it is a grade check, ~$1).

Report what was found and where it was not found: no outside source searched; novelty not classified. Requests: none. Subagent calls:
0. Cost: see the lane ledger.

## Remaining gaps (RUN3-C1161MS, 4 Oct 2026)
Read so far: 3389 cipher signs on all six cipher leaves/blocks (c185R 704, c186R 220, c186L 246, c187L 718, c187R 744, c188L 757), decoded under key.tsv: C 353, S 1908, M 1114, U 33 tokens; 0 H. Multi-seed consensus run (PASS 0.334 vs 0.122; 1 sign M->S).
- 27 M-graded key signs (th, z, rot, eloop, ls, o, phi, iib, 6r, 8, K ...; 2 and tz with a contrary consensus) - blocker: not-attempted; the 10-seed consensus reaches a majority on too few signs; next: a gloss-and-judge value test of the contrary/near-majority letters (2=t, tz=l, and qb=e, 4=e, S=n for the contested S signs) scored by c186R gloss match and the fr16 judge against shuffled-key nulls, ~$3
- rule 7 re-derivation of the regraded reading - blocker: not-attempted; grades changed this pass (letters unchanged); next: a fresh session re-derives with tools/decode_key.py --check from spec and key.tsv, ~$1
- new shapes NEW_c186L_1, NEW_c187L_1, NEW_c187R_1/_2, NEW_c188L_1/2/3 and iii barred vs bare - blocker: not-attempted; 33 U tokens incl. clear words; next: owner sign sorter pass or a per-shape split test at pooled N, ~$3
- left edge of the gloss under the mount - blocker: illegible; letters cut by the mount on every line (c186Rmarg crops)

## Escalation (RUN3-C1161MS, 4 Oct 2026)
- [x] siblings: all six cipher leaves/blocks transcribed and merged; c184 and c189 checked, no continuation (N4-C1 1a); c188L re-passed to err_2reader 0.084
- [x] clear-pages: the c186R marginal gloss matches the blind key at 0.594 (shuffled max 0.312); the gloss itself PASSes the fr16 judge (-0.808), the decode FAILs (-1.233)
- [x] known-keys: fr16142 Noailles (Dax) Constantinople key, shape-level test 2/16 vs permutation p99 3, NO FIT (N4-C1 4); no other Noailles/Dax key on disk or in KEY-OFFICES.tsv
- [n/a] print: no printed edition of these Avis located by check-solved and Premise check
- [ ] key-rebuild: two-instrument PASS (0.624) and 10-seed consensus PASS (0.334 vs 0.122) grade 16 signs S; next: gloss-and-judge value test of the contrary consensus letters
- [ ] image-check: seven provisional new shapes; next: sorter or split test as in Remaining gaps
- [n/a] retry: a further seed sweep of the same anneal is not a different instrument
Verdict: keep going: 3 internal gaps; cheapest next: rule 7 re-derivation of the regraded reading, ~$1

## RUN3-C1161R7B (4 Oct 2026)
Fresh rule-7 grade re-derivation after RUN3-C1161MS: `tools/decode_key.py` regenerates reading.txt and reading_tokens.tsv
byte-identically (C 353, S 1908, M 1114, U 33; 0 H); `--check` exit 0. SAME, not sent back. Against run 3 the only change
is sign 7's 211 tokens M -> S (value 'i' unchanged). Details: RD7-2026-10-04-run3b.md; copies in rederive/run3b_reading*.

## Remaining gaps (RUN3-C1161R7B, 4 Oct 2026)
Read so far: 3389 cipher signs on all six cipher leaves/blocks (c185R 704, c186R 220, c186L 246, c187L 718, c187R 744, c188L 757), decoded under key.tsv: C 353, S 1908, M 1114, U 33 tokens; 0 H. Rule-7 re-derivation of the regraded reading done (SAME, RD7-2026-10-04-run3b.md).
- 27 M-graded key signs (th, z, rot, eloop, ls, o, phi, iib, 6r, 8, K ...; 2 and tz with a contrary consensus) - blocker: not-attempted; the 10-seed consensus reaches a majority on too few signs; next: a gloss-and-judge value test of the contrary/near-majority letters (2=t, tz=l, and qb=e, 4=e, S=n for the contested S signs) scored by c186R gloss match and the fr16 judge against shuffled-key nulls, ~$3
- new shapes NEW_c186L_1, NEW_c187L_1, NEW_c187R_1/_2, NEW_c188L_1/2/3 and iii barred vs bare - blocker: not-attempted; 33 U tokens incl. clear words; next: owner sign sorter pass or a per-shape split test at pooled N, ~$3
- left edge of the gloss under the mount - blocker: illegible; letters cut by the mount on every line (c186Rmarg crops)

## Escalation (RUN3-C1161R7B, 4 Oct 2026)
- [x] siblings: all six cipher leaves/blocks transcribed and merged; c184 and c189 checked, no continuation (N4-C1 1a); c188L re-passed to err_2reader 0.084
- [x] clear-pages: the c186R marginal gloss matches the blind key at 0.594 (shuffled max 0.312); the gloss itself PASSes the fr16 judge (-0.808), the decode FAILs (-1.233)
- [x] known-keys: fr16142 Noailles (Dax) Constantinople key, shape-level test 2/16 vs permutation p99 3, NO FIT (N4-C1 4); no other Noailles/Dax key on disk or in KEY-OFFICES.tsv
- [n/a] print: no printed edition of these Avis located by check-solved and Premise check
- [ ] key-rebuild: two-instrument PASS (0.624) and 10-seed consensus PASS (0.334 vs 0.122) grade 16 signs S; next: gloss-and-judge value test of the contrary consensus letters
- [ ] image-check: seven provisional new shapes; next: sorter or split test as in Remaining gaps
- [n/a] retry: a further seed sweep of the same anneal is not a different instrument
Verdict: keep going: 2 internal gaps; cheapest next: gloss-and-judge value test of the contrary consensus letters, ~$3

## RUN4-C1161AU (4 Oct 2026, verifier hat)
AUDIT.md propagation of the sign-7 regrade (rule 10): sections 4 and 5 carry dated addenda (C/S 67.0%, key 22/49 at C/S, longest
C/S run 16 and non-French; rule 7 SAME per RD7-2026-10-04-run3b.md); the section 3 safe sentence now reads "about 67%". Depth stays
D1. status.json `depth_pct` 60.7 -> 67.0 handed to the status.json owner. No SECOND-OPINIONS-QUEUE.tsv row exists for this target.
The remaining gaps and escalation are unchanged from RUN3-C1161R7B above.

## RUN4-C1161GJ (4 Oct 2026)
Account 1 worker for LANE-RUN4, brief `.claude/briefs/runs/2026-10-04-acct1-run4-wave2.md`. Disk only, no network, no subagent
calls. Pre-registration `tx/PREREG_glossjudge.md` (pushed 743c1b02 before any score); script `two/glossjudge.py` (pushed
69d7f2e3 before scoring); outputs `two/glossjudge.tsv` (26-letter and 50-key null rows) and `two/glossjudge_gate.tsv`.

**Test.** Per sign, value A (key.tsv) vs B (10-seed consensus letter), each sign alone with the rest of key.tsv fixed. G = the
glossctl gloss match on the c186R block (key.tsv now reads **0.612**, 104/170; READ2-C1161B's 0.594 was an earlier key). J = the
fr16 judge's 4-gram language score on the 3375-letter decode (reproduces `two/full_decode.txt`; key.tsv -1.233), read only as a
relative score because the gloss itself PASSes the judge and the decode FAILs (rule 3, ZX-DEC349). Nulls: the 50 shuffled-order
anneal keys of RUN3-C1161MS (same A->B swap; can differ because the neighbouring letters change, so a gain that is only unigram
frequency shows in the null too) and the sign set to each of a-z. Gate: V beats W on both G and J, beats the shuffled-key p95 on
both, and ranks top 2 of 26 on both; a sign with fewer than 3 c186R tokens cannot pass the G half.

| sign | A (key) | B (consensus) | c186R tokens | dG (B-A) / null p95 | dJ (B-A) / null p95 | best of 26 (G / J) | verdict |
|---|---|---|---|---|---|---|---|
| 2  | r (M) | t | 1  | 0.000 / 0.000 | +0.0007 / 0.0025 | z / l | neither; G untestable at 1 token |
| tz | e (M) | l | 3  | 0.000 / 0.029 | +0.0048 / 0.0146 | c / **l** | neither |
| qb | a (S) | e | 14 | **-0.071** / (A-B: 0.094) | **-0.009** / (A-B: -0.001) | **a** / **a** | A fails only clause ii on G (0.071 < 0.094) |
| 4  | o (S) | e | 12 | -0.059 / (A-B: 0.129) | +0.0077 / 0.0713 | **o** / **e** | split: gloss favours o, judge e |
| S  | u (S) | n | 14 | 0.000 / 0.082 | **+0.033** / 0.057 | n (tie, dG 0) / **n** | neither; J favours n, below null |

**Gate: no sign passes either way.** Per the pre-registration nothing changes in key.tsv: no value, no grade. `tools/decode_key.py
--check` exit 0 ("reading up to date", C 353, S 1908, M 1114, U 33). The reading is unchanged, so no rule-7 re-derivation or AUDIT
propagation is owed by this pass.
- Contested S signs, named here as pre-registered: **`4` (o) and `S` (u) are "contested (single-seed S, gloss/judge undecided)"**:
  for `4` the gloss's best letter is the key's o and the judge's best is the consensus e; for `S` the judge's best letter of 26 is
  the consensus n (+0.033, the largest gain of the five) and the gloss is indifferent, but the gain sits under the shuffled-key p95.
  **`qb` = a** is the best letter of 26 on both statistics and beats the consensus e on both, missing only the shuffled-key p95 on
  G (0.071 vs 0.094): evidence for the key value, not enough to clear the gate.
- Information only (not gated): all five B at once: G 0.612 -> 0.412, J -1.233 -> -1.197 -- the judge prefers the consensus set,
  the period gloss strongly prefers key.tsv. The two instruments pull opposite ways on qb and 4, which is why the gloss (a period
  plaintext) and not the corpus n-gram score should decide where they disagree.
- The shuffled-key null on G is wide (p95 0.03-0.13 on a 170-letter gloss): a 12-14-token sign moves difflib's block alignment by
  several letters even in a garbage context, so the gloss half needs a sign with more c186R tokens, or more glossed text, to pass.

Report what was found and where it was not found: no outside source searched; novelty not classified. Requests: none. Subagent
calls: 0. Cost: see the lane ledger.

## Remaining gaps (RUN4-C1161GJ, 4 Oct 2026)
Read so far: 3389 cipher signs on all six cipher leaves/blocks (c185R 704, c186R 220, c186L 246, c187L 718, c187R 744, c188L 757), decoded under key.tsv: C 353, S 1908, M 1114, U 33 tokens; 0 H. Gloss-and-judge value test of 2, tz, qb, 4, S run (no sign passes; key unchanged).
- 27 M-graded key signs (th, z, rot, eloop, ls, o, phi, iib, 6r, 8, K, 2, tz ...) and the contested S signs 4 and S - blocker: not-attempted; gloss-and-judge test (RUN4-C1161GJ) undecided for 2/tz/4/S, the gloss is too short to move a sign with under ~15 block tokens past its shuffled-key null; next: a word-level instrument (French word cover of the full decode per candidate letter, same 50-key and 26-letter nulls, pre-registered), ~$2
- new shapes NEW_c186L_1, NEW_c187L_1, NEW_c187R_1/_2, NEW_c188L_1/2/3 and iii barred vs bare - blocker: not-attempted; 33 U tokens incl. clear words; next: owner sign sorter pass or a per-shape split test at pooled N, ~$3
- left edge of the gloss under the mount - blocker: illegible; letters cut by the mount on every line (c186Rmarg crops)

## Escalation (RUN4-C1161GJ, 4 Oct 2026)
- [x] siblings: all six cipher leaves/blocks transcribed and merged; c184 and c189 checked, no continuation (N4-C1 1a); c188L re-passed to err_2reader 0.084
- [x] clear-pages: the c186R marginal gloss matches the blind key at 0.612 under the current key.tsv (shuffled max 0.312 at 0.594); the gloss itself PASSes the fr16 judge (-0.808), the decode FAILs (-1.233)
- [x] known-keys: fr16142 Noailles (Dax) Constantinople key, shape-level test 2/16 vs permutation p99 3, NO FIT (N4-C1 4); no other Noailles/Dax key on disk or in KEY-OFFICES.tsv
- [n/a] print: no printed edition of these Avis located by check-solved and Premise check
- [ ] key-rebuild: two-instrument PASS (0.624), 10-seed consensus PASS (0.334 vs 0.122), gloss-and-judge value test of the contrary letters undecided (RUN4-C1161GJ); next: word-cover instrument for the M and contested S signs
- [ ] image-check: seven provisional new shapes; next: sorter or split test as in Remaining gaps
- [n/a] retry: a further seed sweep of the same anneal is not a different instrument
Verdict: keep going: 2 internal gaps; cheapest next: word-cover value test of the M and contested S signs, ~$2

## RUN5-C1161WC (4 Oct 2026)
Account 1 worker for LANE-RUN5, brief `.claude/briefs/runs/2026-10-04-acct1-run5-wave1.md`. Disk only, no network, no subagent
calls. Pre-registration `tx/PREREG_wordcover.md` (pushed 974a85d3 before any score, headroom included); script
`two/wordcover.py` (pushed 09363dce before scoring); outputs `two/wordcover_headroom.tsv`, `two/wordcover.tsv`,
`two/wordcover_gate.tsv`. Statistic: fraction of the 3375 decoded letters covered by non-overlapping words (len >= 3,
freq >= 3) of the fr17 + fr16 vocabulary (24,173 words), dynamic programme over the unsegmented decode.

**Rule 3 headroom check: passed (not at ceiling).** key.tsv decode C0 **0.918**; its 200 order shuffles mean **0.787**
(p99 0.804); held-out genuine fr17 text (Mazarin, letters 300000-303375, vocabulary built without that file) 0.972 vs its
letter shuffles 0.643. The statistic separates real French from noise at this N, and the decode sits between the two.

**Planted-value control: FAILED on one of two -> NON-TEST (pre-registered: both must recover).**

| planted | true value | argmax of 26 | true value's rank | gain D (argmax - planted) | order-shuffle p99 | 50-key p95 | result |
|---|---|---|---|---|---|---|---|
| `a` = e | u (C, 98 tokens) | **u** | 1 | 0.0382 | 0.0273 | 0.0174 | recovered (all four clauses) |
| `p` = e | c (C, 112 tokens) | i | 5 (tied with r; i 0.9289, u 0.9256, l 0.9230, t 0.9185, c 0.9179) | 0.0207 | 0.0290 | 0.0251 | **NOT recovered** |

Word cover prefers i, u, l and t over the gloss-confirmed `p` = c (a C-graded value, every aligned gloss occurrence
agrees): with about a third of the decode's tokens on M signs, short common words (les, ont, qui ...) made from vowel and
liquid letters out-score the right consonant. Per the pre-registration **the 30 target signs (27 M + 4, S, qb) were not
scored**, nothing changes in key.tsv (no value, no grade), and the reading is unchanged (`tools/decode_key.py --check`
below). This is a non-test of the instrument at this decode quality, not evidence about any sign's value.

Report what was found and where it was not found: no outside source searched; novelty not classified. Requests: none.
Subagent calls: 0. Cost: see the lane ledger.

## Remaining gaps (RUN5-C1161WC, 4 Oct 2026)
Read so far: 3389 cipher signs on all six cipher leaves/blocks (c185R 704, c186R 220, c186L 246, c187L 718, c187R 744, c188L 757), decoded under key.tsv: C 353, S 1908, M 1114, U 33 tokens; 0 H. Gloss-and-judge value test (RUN4-C1161GJ) no sign passes; word-cover value test (RUN5-C1161WC) NON-TEST, planted control p=c not recovered.
- 27 M-graded key signs (th, z, rot, eloop, ls, o, phi, iib, 6r, 8, K, 2, tz ...) and the contested S signs 4, S, qb - blocker: not-attempted; per-sign word cover failed its planted control (RUN5-C1161WC), per-sign gloss/judge undecided (RUN4-C1161GJ); next: a joint instrument -- re-anneal only the M signs with the C and agreed S signs held, objective fr17 4-gram + word cover, pre-registered with the same planted controls (p=e, a=e) required to recover first, ~$3
- new shapes NEW_c186L_1, NEW_c187L_1, NEW_c187R_1/_2, NEW_c188L_1/2/3 and iii barred vs bare - blocker: not-attempted; 33 U tokens incl. clear words; next: owner sign sorter pass or a per-shape split test at pooled N, ~$3
- left edge of the gloss under the mount - blocker: illegible; letters cut by the mount on every line (c186Rmarg crops)

## Escalation (RUN5-C1161WC, 4 Oct 2026)
- [x] siblings: all six cipher leaves/blocks transcribed and merged; c184 and c189 checked, no continuation (N4-C1 1a); c188L re-passed to err_2reader 0.084
- [x] clear-pages: the c186R marginal gloss matches the blind key at 0.612 under the current key.tsv (shuffled max 0.312 at 0.594); the gloss itself PASSes the fr16 judge (-0.808), the decode FAILs (-1.233)
- [x] known-keys: fr16142 Noailles (Dax) Constantinople key, shape-level test 2/16 vs permutation p99 3, NO FIT (N4-C1 4); no other Noailles/Dax key on disk or in KEY-OFFICES.tsv
- [n/a] print: no printed edition of these Avis located by check-solved and Premise check
- [ ] key-rebuild: two-instrument PASS (0.624), 10-seed consensus PASS (0.334 vs 0.122); per-sign gloss/judge undecided (RUN4-C1161GJ); per-sign word cover NON-TEST, planted control p=c not recovered (RUN5-C1161WC); next: joint M-sign re-anneal with C/S held and planted controls first, as in Remaining gaps
- [ ] image-check: seven provisional new shapes; next: sorter or split test as in Remaining gaps
- [n/a] retry: a further seed sweep of the same anneal is not a different instrument
Verdict: keep going: 2 internal gaps; cheapest next: joint M-sign re-anneal with C/S held and planted controls, ~$3

## RUN5-C1161RA (4 Oct 2026)
Account 1 worker for LANE-RUN5, brief `.claude/briefs/runs/2026-10-04-acct1-run5-wave2.md`. Disk only, no network, no subagent
calls. Pre-registration `tx/PREREG_reanneal.md` + script `two/reanneal.py` (pushed 9d85bc83 before any run); W calibration
`two/ra/calib.tsv` (e0f2d0ac, before any control number); outputs `two/ra/` (10 control keys, `runs.tsv`, `ctl_signs.tsv`,
`ctl_gate.txt`). One code fix after the anneals and before any scoring: `score` raised KeyError on the non-planted free signs of the
control arm (A must fall back to key.tsv for them); a one-line fix, recipe/W/seeds untouched.

**Instrument.** Six-leaf stream (3375 keyed tokens), 6 C + 13 agreed S signs held, 29 signs free (27 M + 4, S). Stage 1
`homophonic_anneal.solve` (fr17, order 4, restarts 32, iters 40000, held signs fixed); stage 2 coordinate ascent on
J = 4-gram log-prob per letter + W x word cover (RUN5-C1161WC's fr17+fr16 vocabulary), W = 5.509 by the pre-registered
held-out formula (Mazarin fr17: L real -1.820 vs shuffled -3.624, cover 0.972 vs 0.644). Consensus >= 7/10 seeds plus a
50-context shuffled-value null per sign.

**Planted control (a=u, p=c, d=n freed, planted at e): 0/3 recovered -> NON-TEST; the target arm was not run** (pre-registered:
>= 2/3 needed). key.tsv unchanged (no value, no grade); `tools/decode_key.py --check`: "reading up to date" (C 353, S 1908,
M 1114, U 33).

| planted | true | consensus (10 seeds) | votes | result |
|---|---|---|---|---|
| a | u | none | u5 i5 | NOT recovered |
| p | c | i (10/10) | i10 | NOT recovered (wrong letter) |
| d | n | none | n5 i5 | NOT recovered |

**Why it failed (diagnosed after the gate, not acted on).** Stage 1 converged to the same key on all 10 seeds (score -9268.7,
J 2.3045): with 19 signs held the 4-gram anneal has one basin, so seed diversity came only from stage 2's sign order. Stage 2 then
hit its 4-pass limit on every seed, and on 5 seeds (2, 3, 5, 7, 10; J 2.822-2.824 vs 2.686-2.701 on the others) it pushed
**every** free sign, planted ones included, to 'i'. The fr17+fr16 vocabulary contains 'iii', 'iiii', 'iiiii', 'iiiiii', 'iiiiiii'
(roman numerals / OCR debris, freq >= 3), so runs of i are "words" and the cover term at W = 5.5 outweighs the 4-gram loss. The
5 non-degenerate seeds read a=u, d=n (right) and p=i (wrong; RUN5-C1161WC's control also put p at i). Full per-sign rows for the
29 free signs (control arm only) are in `two/ra/ctl_signs.tsv`; they are a degenerate instrument's output and say nothing
about any sign's value.

This is the second NON-TEST of a word-cover-weighted instrument on this key (RUN5-C1161WC per-sign, RUN5-C1161RA joint), both
failing their planted controls toward i: logged in Escalation (key-rebuild line) as retired for word cover with this vocabulary (rule 3,
third-attempt clause applied early because the cause is identified: the vocabulary, not the setting). A different
instrument, not a reweighting, is what the remaining gap names.

Report what was found and where it was not found: no outside source searched; novelty not classified. Requests: none. Subagent
calls: 0. Cost: see the lane ledger.

## Remaining gaps (RUN5-C1161RA, 4 Oct 2026)
Read so far: 3389 cipher signs on all six cipher leaves/blocks (c185R 704, c186R 220, c186L 246, c187L 718, c187R 744, c188L 757), decoded under key.tsv: C 353, S 1908, M 1114, U 33 tokens; 0 H. Gloss-and-judge value test (RUN4-C1161GJ) no sign passes; word-cover value test (RUN5-C1161WC) NON-TEST; joint M-sign re-anneal with word cover (RUN5-C1161RA) NON-TEST, planted control 0/3 (vocabulary admits i-runs).
- 27 M-graded key signs (th, z, rot, eloop, ls, o, phi, iib, 6r, 8, K, 2, tz ...) and the contested S signs 4, S, qb - blocker: not-attempted; word-cover instruments retired (two NON-TESTs, i-run vocabulary); the held 4-gram anneal has a single basin (all 10 seeds identical), so seed consensus carries no information; next: a held 4-gram anneal under leave-one-leaf-out streams (6 streams, consensus across leaves instead of seeds) with the same planted a/p/d control first, ~$3
- new shapes NEW_c186L_1, NEW_c187L_1, NEW_c187R_1/_2, NEW_c188L_1/2/3 and iii barred vs bare - blocker: not-attempted; 33 U tokens incl. clear words; next: owner sign sorter pass or a per-shape split test at pooled N, ~$3
- left edge of the gloss under the mount - blocker: illegible; letters cut by the mount on every line (c186Rmarg crops)

## Escalation (RUN5-C1161RA, 4 Oct 2026)
- [x] siblings: all six cipher leaves/blocks transcribed and merged; c184 and c189 checked, no continuation (N4-C1 1a); c188L re-passed to err_2reader 0.084
- [x] clear-pages: the c186R marginal gloss matches the blind key at 0.612 under the current key.tsv (shuffled max 0.312 at 0.594); the gloss itself PASSes the fr16 judge (-0.808), the decode FAILs (-1.233)
- [x] known-keys: fr16142 Noailles (Dax) Constantinople key, shape-level test 2/16 vs permutation p99 3, NO FIT (N4-C1 4); no other Noailles/Dax key on disk or in KEY-OFFICES.tsv
- [n/a] print: no printed edition of these Avis located by check-solved and Premise check
- [ ] key-rebuild: two-instrument PASS (0.624), 10-seed consensus PASS (0.334 vs 0.122); per-sign gloss/judge undecided (RUN4-C1161GJ); word-cover instrument retired (fr17+fr16 vocabulary, per-sign RUN5-C1161WC and joint re-anneal RUN5-C1161RA both NON-TEST on planted controls); next: leave-one-leaf-out held 4-gram anneal with planted controls first, as in Remaining gaps
- [ ] image-check: seven provisional new shapes; next: sorter or split test as in Remaining gaps
- [n/a] retry: a further seed sweep of the same anneal is not a different instrument
Verdict: keep going: 2 internal gaps; cheapest next: leave-one-leaf-out held 4-gram anneal with planted controls, ~$3

## SCORE-NC2 (account-3 worker, 4 Oct 2026, 14:42-15:0x UTC by date -u)
Brief `.claude/briefs/runs/2026-10-04-acct3-score-nc2.md`; PREREG addendum `tx/PREREG_reanneal_nc2.md` and the script change
pushed before any run (3a2e2efa). One change from RUN5-C1161RA: `--norm nc2`, the Lasry, Biermann and Tomokiyo 2023 App. A score
(n-gram log-likelihood divided by sum N_c^2), now a shared option of `tools/homophonic_anneal.py` (`ngram_term`, test
`tools/tests/test_homophonic_nc2.py`), used by both stages of `two/reanneal.py --norm nc2`. W re-derived by the same held-out
formula: 5.47771 (`two/ra_nc2/calib.tsv`; norm=none had 5.50926). Outputs `two/ra_nc2/`; `two/ra/` untouched.

**Headroom:** the same planted control at norm=none read 0/3 (two/ra/ctl_gate.txt) -- no ceiling problem.
**Planted control under nc2: 0/3 recovered -> NON-TEST, target arm not run** (`two/ra_nc2/ctl_gate.txt`, `ctl_signs.tsv`).

| planted | true | votes (10 seeds) | consensus >= 7 | planted e vs best alternative: dJ / null p95 |
|---|---|---|---|---|
| a | u | u4 c1 t1 s1 n1 d1 b1 | none | -0.854 / -0.324 (e rejected) |
| p | c | c4 m3 d2 s1 | none | -0.962 / -0.484 (e rejected) |
| d | n | t3 n2 u2 s2 x1 | none | -0.593 / -0.095 (e rejected) |

What changed and what did not: nc2 removed the degenerate basin (at norm=none every free sign went to i in 9-10/10 seeds and all
10 seeds' stage-1 keys were identical; under nc2 no free sign piles on i, stage-1 scores differ by seed, 27187.8-28144.9).
The wrong planted value e is now rejected beyond the null for all three, and the true letter is the modal vote for a (u 4/10)
and p (c 4/10), but no planted sign reaches the pre-registered 7/10 consensus, so none is "recovered". Of the 29 free signs only
`4` reaches consensus (o 9/10 = its key.tsv value, clears its null) and `L` (g 8/10) and `l` (f 7/10) reach it at a value
different from key.tsv; with the control failed these are not proposals (rule 3: a control below its gate licenses no target
reading), so **nothing is proposed for key.tsv** and no grade moves. Per the PREREG no W, seed or recipe tuning follows.

Rule 3 bookkeeping: this was one attempt of a different objective (not a re-weighting); it failed differently from C1161RA
(dispersion instead of collapse), which is the shape that says the joint free-sign problem at this N (3375 signs, 32 free
signs incl. the 3 planted C) is under-determined by a 4-gram objective however it is normalised, not that the
normalisation was wrong. Logged as [retired] for the joint re-anneal (instrument: 4-gram + word cover, none or nc2).

Report what was found and where it was not found: no outside source searched; novelty not classified. Requests: none. Subagent
calls: 0.

## Remaining gaps (SCORE-NC2, 4 Oct 2026)
Read so far: 3389 cipher signs on all six cipher leaves/blocks (c185R 704, c186R 220, c186L 246, c187L 718, c187R 744, c188L 757), decoded under key.tsv: C 353, S 1908, M 1114, U 33 tokens; 0 H. Gloss-and-judge value test (RUN4-C1161GJ) no sign passes; word-cover value test (RUN5-C1161WC) NON-TEST; joint M-sign re-anneal with word cover (RUN5-C1161RA) NON-TEST 0/3; the same with nc2 normalisation (SCORE-NC2) NON-TEST 0/3 (no collapse, no consensus).
- 27 M-graded key signs (th, z, rot, eloop, ls, o, phi, iib, 6r, 8, K, 2, tz ...) and the contested S signs 4, S, qb - blocker: not-attempted; joint re-anneal retired under both norms (29-32 free signs too many for a 4-gram objective at N=3375); next: a held 4-gram anneal under leave-one-leaf-out streams (6 streams, consensus across leaves instead of seeds) with the same planted a/p/d control first, ~$3
- new shapes NEW_c186L_1, NEW_c187L_1, NEW_c187R_1/_2, NEW_c188L_1/2/3 and iii barred vs bare - blocker: not-attempted; 33 U tokens incl. clear words; next: owner sign sorter pass or a per-shape split test at pooled N, ~$3
- left edge of the gloss under the mount - blocker: illegible; letters cut by the mount on every line (c186Rmarg crops)

## Escalation (SCORE-NC2, 4 Oct 2026)
- [x] siblings: all six cipher leaves/blocks transcribed and merged; c184 and c189 checked, no continuation (N4-C1 1a); c188L re-passed to err_2reader 0.084
- [x] clear-pages: the c186R marginal gloss matches the blind key at 0.612 under the current key.tsv (shuffled max 0.312 at 0.594); the gloss itself PASSes the fr16 judge (-0.808), the decode FAILs (-1.233)
- [x] known-keys: fr16142 Noailles (Dax) Constantinople key, shape-level test 2/16 vs permutation p99 3, NO FIT (N4-C1 4); no other Noailles/Dax key on disk or in KEY-OFFICES.tsv
- [n/a] print: no printed edition of these Avis located by check-solved and Premise check
- [ ] key-rebuild: two-instrument PASS (0.624), 10-seed consensus PASS (0.334 vs 0.122); per-sign gloss/judge undecided (RUN4-C1161GJ); word-cover instrument retired; joint re-anneal retired under norm none and nc2 (RUN5-C1161RA, SCORE-NC2: planted controls 0/3 both); next: leave-one-leaf-out held 4-gram anneal with planted controls first, as in Remaining gaps
- [ ] image-check: seven provisional new shapes; next: sorter or split test as in Remaining gaps
- [n/a] retry: a further seed sweep or W/threshold change of the same anneal is not a different instrument
Verdict: keep going: 2 internal gaps; cheapest next: leave-one-leaf-out held 4-gram anneal with planted controls, ~$3

## C1161-LOLO step 1: diagnosis of the 0/3 planted control (account-3 Fable worker, 4 Oct 2026, 15:22-15:4x UTC by date -u)
Brief `.claude/briefs/runs/2026-10-04-acct3-c1161-lolo.md`. Disk only, no network, no subagents. Script `two/lolo_diag.py`
(reuses `two/reanneal.py`'s stream, model, W and vocabulary unchanged); outputs `two/lolo/`. Question: why did the joint
re-anneal's planted a/p/d control read 0/3 under both norm none (RUN5-C1161RA) and nc2 (SCORE-NC2) -- too many free signs,
a flat objective, the search, or the planted design?

**Answer: none of the four. The anneal and the design are fine; the two additions to the anneal (the word-cover stage and
the nc2 normalisation) each destroyed the signal in a different way, and the real stream's optimum is not key.tsv.**

| # | test (two/lolo/) | result |
|---|---|---|
| D1 rank.tsv | 4-gram-only score per letter (L4) of key.tsv (a/p/d at truth) vs the 20 final control keys | every control key outscores key.tsv: norm none -2.63..-2.71 vs -2.796; nc2 8.06-8.36 vs 6.71. The objective does not rank key.tsv first; the final keys differ from key.tsv on 23-31 of 32 free signs |
| D2 cond.tsv | each free sign's key.tsv letter ranked among 26 with every other sign at key.tsv | plain 4-gram: a, p, d rank 1 of 26 (identifiable in the true context), 9 of 27 M signs rank 1, 8 rank 2, K (f) 18, to (m) 12, eloop (c) 11. Adding the cover term (J): p drops to rank 4 behind i even in the true context -- word cover breaks p by itself. nc2: 6/ls/rc/tz (all e) rank 26, a (u) 18: the sum N_c^2 term scores letter balance (the decode has e 17.9%, i 15.3%, u 11.0%, m 0.2%, b 0%), not context |
| D3 ascent.tsv | coordinate ascent from key.tsv (truth start) | key.tsv is a local optimum of none of the four objectives: 21-27 of 32 free signs drift in <= 4 passes. Plain 4-gram keeps a=u p=c d=n while 21 others drift; J moves p to i; nc2 drifts signs onto k, z, w, v, j, x (rare letters lower sum N_c^2) |
| D4 synth.tsv | **same-design synthetic control**: held-out fr17 text (the W-calibration passage), N=3375, one synthetic sign per key.tsv sign, the same homophone sets and per-sign token shares, letters the design lacks (b k w z after fold) one extra held sign each, the same 19 held / 32 free (a/p/d planted at e), stage 1 only (fr17 4-gram, 32 restarts, 40000 iters), 3 seeds | **32/32 free signs right, 100% of letters, planted 3/3, on all three seeds** (identical score -5834.0: one basin = the truth). 50% of tokens free is not too many for a 4-gram anneal at this N on French of this design |
| D5 stage1.tsv | the PREREG's stage 1 alone on the **real** control arm, seed 1 (reanneal.py never saved this key; score -9268.7 reproduces runs.tsv) | **planted 3/3 recovered: a=u p=c d=n.** 20 of the 29 free M/S signs move away from key.tsv (ls e>m, o n>m, L n>d, iib l>d, vdash t>d, S u>n ...); L4 -2.666 |
| D6 noise.tsv | error bracket (rule 3, SALV-DIAG shape): L4 of genuine French at N=3375 with a share q of signs misread | q=0 -1.72, 5% -2.12, 8.4% -2.36, 10% -2.44, 14.6% -2.67, 20% -2.97, shuffled -3.58. The anneal's optimum on the real stream (-2.63/-2.67) scores like French with about 14% of signs misread; key.tsv (-2.80) like 17%; the measured two-reader error is 0.084-0.10 (c188L, c185R) |
| D7 blind.tsv | nothing held: the order-4 anneal on the real stream with all 49 signs free, seed 1 | L4 -2.797 -- no better than key.tsv (-2.796) and worse than the held anneal (-2.67); agrees with key.tsv on 3 of the 17 control-arm held signs and 6 of 32 free. A different, equally poor basin: the held C/S values *help* the objective, and no homophonic key found brings the stream near French |

Reading. (1) The 0/3 at norm none was stage 2: the cover term prefers i for p even in the true context (D2) and the
i-run vocabulary then collapsed 5 of 10 seeds (C1161RA's own finding); stage 1 had already recovered 3/3 (D5). (2) The 0/3
under nc2 was the normalisation: at this free share the 1/sum N_c^2 factor rewards moving tokens onto rare letters (D2, D3),
so the planted e's were rejected (SCORE-NC2's "e rejected" rows) but no letter won. (3) The "single basin / seed consensus
carries no information" worry that named the leave-one-leaf-out step is the signature of a working solver, not a defect:
the synthetic's three seeds also share one basin, and it is the truth. (4) What remains is not a search problem: the plain
4-gram optimum on the real stream moves 20 of 29 free signs off key.tsv (D5) and still scores like French at ~14% misread
(D6), with the C/S signs held (D7: held beats blind by 0.13 per letter). key.tsv's M values came from a noise-0.10 fr16 order-3/4 blind anneal of one seed
(key.tsv source column), which the two-instrument and 10-seed consensus tests graded as a family, not per sign; D1-D3 say the
order-4 fr17 objective does not endorse them, and the truth-start drift (D3) says they are not a stable reading under it.
Which of key.tsv and the anneal optimum is nearer the text cannot be told from the stream alone: neither reaches French at
the measured error, so a share of the gap is the transcription (two-reader agreement is not accuracy, LESSONS "Look-alike
pass"), the held values, or the design (the decode has no b, 0.9% d, 0.2% m against French b~1%, d~3.7%, m~3%: six letters
nearly absent, and the free signs the anneal moves go to m, d, b).

Decision for step 2. The named next step (a held 4-gram anneal under leave-one-leaf-out streams) is not ruled out by the
diagnosis -- it is stage 1 alone, which D4 and D5 show is a working instrument on this design and recovers the planted signs
on the real stream -- but its stated purpose (restoring variance for a consensus) is: the 6 leaf streams share 78-93% of
their tokens with the full stream and will sit in the same basin. What the leaf streams can add is per-sign stability (a
sign whose value flips when one leaf is dropped is leaf-driven), so it runs **as a stage-1-only instrument** (norm none, no
cover: the two components diagnosed as the failure are removed, not re-tuned), pre-registered in
`tx/PREREG_reanneal_lolo.md`, planted control first. A fewer-free-signs design is not the right instrument: D4 says the
free count is not the limit, and holding more M values at key.tsv would hold values D3 says the objective does not keep.

## C1161-LOLO step 2: stage-1-only held 4-gram anneal under leave-one-leaf-out streams (4 Oct 2026, 15:36-16:0x UTC by date -u)
Pre-registration `tx/PREREG_reanneal_lolo.md` (97351e1b, pushed before any run). Instrument: `two/reanneal.py`'s stage 1
alone (fr17 4-gram, norm none, 32 restarts, 40000 iters, seed 1), no word-cover stage, no nc2; the 6 C + 14 agreed S signs
held (the earlier PREREG's prose says 13 S, its list has 14; the list is what the code holds), the 29 M/4/S signs free;
six streams, each the full stream minus one leaf/block (N 2623-3155); consensus = the same letter in >= 5 of 6 streams;
dL4 over the full stream against a 50-context shuffled-value null; outputs `two/lolo/lolo_*`, `key_lolo_*`. A one-token
sign that lives only on the dropped leaf has no entry in that stream's key: it keeps its key.tsv value for full-stream
scoring and casts no vote (the first launch crashed on this at 15:38, fixed before any scoring; two saved keys reused).

**Planted control a/p/d (freed with the 29, started at e): 3/3 recovered -> GATE PASS** (`two/lolo/lolo_ctl_gate.txt`).

| planted | true | consensus | leaves | dL4 (true vs e over K*) | null p95 |
|---|---|---|---|---|---|
| a | u | u | 6/6 | 0.1318 | 0.0744 |
| p | c | c | 6/6 | 0.0711 | 0.0332 |
| d | n | n | 6/6 | 0.0775 | 0.0426 |

Headroom (rule 3, as pre-registered): this is a licence gate, and its blind baseline for this instrument was already 3/3 on
the full stream (step 1, D5); the pass says the held 4-gram anneal recovers known C values in this context with 50% of
tokens free, which the same-design synthetic (D4, 32/32) predicted. It does not say the free signs' values are right.
Control-arm free signs (`two/lolo/lolo_ctl_signs.tsv`, 32 free): 22-24 of them differ from key.tsv in every stream.

**Target arm (6 streams, `two/lolo/lolo_tgt_signs.tsv`).** Every stream's key coincides with its control-arm key (the control
recovered a/p/d exactly, so the two arms sit in the same optimum): 22-24 of the 29 free signs differ from key.tsv in every
stream, L4 -2.666 to -2.712 over the full stream. Per sign (A = key.tsv, B = consensus at >= 5/6, dL4 = B vs A over K*,
null = 50-context shuffled-value p95):

| decision | signs (tokens) | consensus / leaves / dL4 / null p95 |
|---|---|---|
| **proposal M** (B != A, consensus, dL4 > 0 and > null) | K f->s (28); iib l->d (36); l s->f (12); ls e->m (40); o n->m (77); rot r->h (16); spiralG h->n (1); to m->s (6); x s->f (11) | K s 5/6 0.0422/0.0296; iib d 5/6 0.0098/0.0062; l f 6/6 0.0083/0.0042; ls m 5/6 0.0118/0.0110; o m 6/6 0.0076/0.0053; rot h 5/6 0.0079/0.0030; spiralG n 5/6 0.00275/0.00266; to s 5/6 0.0062/0.0041; x f 6/6 0.0112/0.0020 |
| key.tsv value is the leaf-stable optimum (B == A, A beats its best alternative beyond the null) | th s (208), z t (189), 4 o (224) | th 6/6 0.0978/0.0842; z 6/6 0.0923/0.0650; 4 6/6 0.0463/0.0262 |
| consensus but dL4 below its null (no proposal) | 2 u, 8 u, eloop e (6/6), sqc e (6/6), tz l (6/6), vdash d (6/6), S n (5/6: 0.0446 vs 0.0527, the nearest miss) | -- |
| no consensus (<= 4/6) | 6, 6r, L, Sorn, blot, c, dia, phi, psi, rc | leaf-driven: these flip when one leaf is dropped |

**Grades and what the proposals are.** All nine are **proposals graded M**; nothing enters key.tsv (decode_key --check
below: reading unchanged). They are the leaf-stable 4-gram optimum given the held C/S signs, not a reading: step 1's D6
puts that optimum at the 4-gram score of genuine French with about 14% of signs misread, against a measured two-reader
error of 8-10%, so a share of the stream is still not French under any key found. Two things make them worth a next test
rather than a shrug: (i) they move 227 tokens off e/n/s/l onto m, d, f, h, which key.tsv almost lacks -- under the nine,
m goes 0.2% -> 3.5% of tokens (French about 3%), d 0.9% -> 2.0%, e 18.0% -> 16.8%, f unchanged (K loses f, l and x gain it) --
but n falls 4.5% -> 2.2%, further below French (about 7%), so the letter balance is only partly repaired; (ii) six of them
(K, iib, l, ls, o, x) are the same letters stage 1 reached on the full stream in step 1 (D5) and that the nc2 run's
dispersed votes leaned to (SCORE-NC2: o m4, ls m3, iib x3/d2) -- three instruments with different pathologies agree on
where the mass should go, which is still not a control-backed reading of any one sign.

Rule 3 bookkeeping: the retired joint re-anneal (cover; nc2) stays retired; this run is its stage 1 alone under leaf
streams, a different instrument by the component the diagnosis removed, licensed by a same-design synthetic (D4) and a
3/3 planted control; one attempt, no tuning. HYPOTHESES.md row appended.

Report what was found and where it was not found: no outside source searched; novelty not classified. Requests: none.
Subagent calls: 0. Cost: see the orchestrator's get_session. Suggested follow-up (not run, outside this brief): decode
under key.tsv + the nine proposals and re-run the c186R gloss match (`two/glossjudge.py`, key.tsv reads 0.594-0.612 vs
shuffled max 0.312) and the fr16 judge -- the one independent text on the leaf decides between key.tsv and the
proposals where the 4-gram objective cannot.

## Remaining gaps (C1161-LOLO, 4 Oct 2026)
Read so far: 3389 cipher signs on all six cipher leaves/blocks (c185R 704, c186R 220, c186L 246, c187L 718, c187R 744, c188L 757), decoded under key.tsv: C 353, S 1908, M 1114, U 33 tokens; 0 H. Gloss/judge per sign undecided (RUN4-C1161GJ); word-cover and nc2 joint re-anneals NON-TEST (RUN5-C1161RA, SCORE-NC2); stage-1-only leave-one-leaf-out anneal (C1161-LOLO) GATE PASS 3/3, nine M-sign value proposals (grade M, not in key.tsv), three key.tsv values confirmed leaf-stable.
- 27 M-graded key signs (th, z, rot, eloop, ls, o, phi, iib, 6r, 8, K, 2, tz ...) and the contested S signs 4, S - blocker: not-attempted; nine proposals (K s, iib d, l f, ls m, o m, rot h, spiralG n, to s, x f) and three confirmations (th, z, 4) from C1161-LOLO, graded M because the optimum still scores like French at ~14% misread (two/lolo/noise.tsv); 10 signs leaf-driven (no 5/6 consensus); next: decode under key.tsv + the nine proposals and re-run the c186R gloss match and fr16 judge against key.tsv's own (two/glossjudge.py), ~$2
- new shapes NEW_c186L_1, NEW_c187L_1, NEW_c187R_1/_2, NEW_c188L_1/2/3 and iii barred vs bare - blocker: not-attempted; 33 U tokens incl. clear words; next: owner sign sorter pass or a per-shape split test at pooled N, ~$3
- the gap between the anneal optimum (-2.67 per letter) and genuine French at the measured error (-2.36 to -2.44 at 8-10%) - blocker: not-attempted; either transcription error above the two-reader figure (agreement is not accuracy), a wrong held value, or a design element (code groups, nulls: the decode has no b and few d/m); next: a key-constrained lookalike pass on the highest-token free signs (th 208, z 189, S 275, 4 224) against the native crops, ~$3
- left edge of the gloss under the mount - blocker: illegible; letters cut by the mount on every line (c186Rmarg crops)

## Escalation (C1161-LOLO, 4 Oct 2026)
- [x] siblings: all six cipher leaves/blocks transcribed and merged; c184 and c189 checked, no continuation (N4-C1 1a); c188L re-passed to err_2reader 0.084
- [x] clear-pages: the c186R marginal gloss matches the blind key at 0.612 under the current key.tsv (shuffled max 0.312 at 0.594); the gloss itself PASSes the fr16 judge (-0.808), the decode FAILs (-1.233)
- [x] known-keys: fr16142 Noailles (Dax) Constantinople key, shape-level test 2/16 vs permutation p99 3, NO FIT (N4-C1 4); no other Noailles/Dax key on disk or in KEY-OFFICES.tsv
- [n/a] print: no printed edition of these Avis located by check-solved and Premise check
- [ ] key-rebuild: two-instrument PASS (0.624), 10-seed consensus PASS (0.334 vs 0.122); per-sign gloss/judge undecided (RUN4-C1161GJ); word-cover and nc2 joint re-anneals retired (NON-TEST 0/3 both); stage-1-only leave-one-leaf-out anneal GATE PASS 3/3 with nine M proposals (C1161-LOLO); next: gloss match + judge of the nine proposals vs key.tsv, as in Remaining gaps
- [ ] image-check: seven provisional new shapes; next: sorter or split test as in Remaining gaps; and a lookalike pass on th/z/S/4 for the error gap, as in Remaining gaps
- [n/a] retry: a further seed sweep or W/threshold change of the same anneal is not a different instrument
Verdict: keep going: 3 internal gaps; cheapest next: gloss match + fr16 judge of the nine C1161-LOLO proposals against key.tsv, ~$2

## C1161-GLOSS9 (account-3 worker, 4 Oct 2026, 17:07-17:1x UTC by date -u)
Brief `.claude/briefs/runs/2026-10-04-acct3-c1161-gloss9.md`. Pre-registration `tx/PREREG_gloss9.md` and script `two/gloss9.py`
pushed before any score (769ff65a). Disk only, no subagents. Instrument: RUN4-C1161GJ's G (c186R block vs its period gloss,
key.tsv 0.612) and J (fr16 judge, relative only; key.tsv -1.233), 50 shuffled-order anneal keys as the null. Outputs
`two/gloss9_gate.tsv`, `two/gloss9.tsv`.

| sign | A -> B | c186R tokens | dG / null p95 | dOcc | gloss half | dJ alone | verdict |
|---|---|---|---|---|---|---|---|
| K | f -> s | 2 | 0.000 / 0.029 | +1 | fail | +0.0214 | fail |
| iib | l -> d | 1 | 0.000 / 0.035 | 0 | fail | -0.0031 | fail |
| l | s -> f | 1 | +0.006 / 0.000 | +1 | holds | -0.0092 | fail (judge worse) |
| ls | e -> m | 2 | 0.000 / 0.000 | 0 | fail | -0.0052 | fail |
| o | n -> m | 5 | +0.012 / 0.012 | 0 | fail (= null) | -0.0151 | fail |
| rot | r -> h | 1 | +0.006 / 0.000 | +1 | holds | -0.0024 | fail (judge worse) |
| spiralG | h -> n | 0 | -- | -- | no evidence | -0.0005 | no evidence |
| to | m -> s | 2 | -0.018 / 0.018 | 0 | fail | +0.0018 | fail |
| x | s -> f | 1 | 0.000 / 0.000 | 0 | fail | -0.0058 | fail |

**0 of 9 pass; key.tsv unchanged** (`tools/decode_key.py --check`: reading up to date, C 353, S 1908, M 1114, U 33). No grade
moves, so no AUDIT propagation, re-derivation or depth change is owed. Rule 3: eight of the nine have 0-2 tokens in the glossed
block, where one letter is ~0.006 of G; the gloss half holds for l and rot on a single token each, which is no evidence either
way at this gloss length, and spiralG never occurs in glossed text. The nine stay M proposals.

Information only (not gated, not pre-registered as a gate): all nine together raise G 0.612 -> 0.647 (+6 letters of 170) and
the judge +0.0053, while the same nine swaps in the 50 shuffled-order keys lower it (mean -0.055, p95 -0.038). So as a set the
nine fit the real context better than a shuffled one on both instruments, even though no single value clears its own gate; six
of the nine single swaps lower the judge, so the joint gain lives in the interactions. A pre-registered joint gate (the nine as
one hypothesis, joint G against the shuffled-key joint G null) is the honest next test of that, not a per-sign re-run.

Report what was found and where it was not found: no outside source searched; novelty not classified. Requests: none.
Subagent calls: 0.

## C1161-JOINT9 (account-3 worker, 4 Oct 2026, 17:55-17:59 UTC by date -u)
Brief `.claude/briefs/runs/2026-10-04-acct3-c1161-joint9.md`. Pre-registration `tx/PREREG_joint9.md` and script `two/joint9.py`
pushed before any score (06c01d13). Disk only, no subagents, no network. Output `two/joint9.tsv`.

The nine C1161-LOLO proposals as one hypothesis (key.tsv + K s, iib d, l f, ls m, o m, rot h, spiralG n, to s, x f), against 50
random joint keys (the same nine signs, each value drawn from key.tsv's value frequencies, seeds 1-50):

| statistic | real | null mean | null p95 | null max | real > p95 |
|---|---|---|---|---|---|
| dG (c186R gloss letter agreement) | +0.0353 (0.612 -> 0.647) | -0.0128 | +0.0059 | +0.0118 | yes (0/50 null >= real) |
| dJ (fr16 judge, 3375-letter decode) | +0.00530 | -0.03355 | +0.00318 | +0.01067 | yes (2/50 null >= real) |

**PASS as registered.** The nine enter key.tsv at grade S (witnesses in each row's source: LOLO anneal + this joint test).
`tools/decode_key.py --check`: reading up to date, tokens 3408: C 353, S 2070, M 952, U 33 (was S 1908, M 1114). C/S
2423/3375 = 71.8% (was 67.0%); longest C/S run 19 tokens (was 16). Judge on reading.txt, pasted:
```
FAIL language: score=-1.303, null_p99=-1.751, real_p05=-0.913, real_median=-0.823, mode=both, N=3913
ok   words: cover=0.869, min=0.5, real_text_median_cover=0.957
FAIL - clair1161-avis-flandre-1688 (a PASS is a gate for a verifier, not a reading; rule 10)
```
(the pre-JOINT9 reading scores -1.300, cover 0.878 through the same command: the whole-reading judge with separators moved
slightly the other way from the letters-only dJ the test used; reported, not re-tested.)

What the PASS means and does not: the null is random letters on those nine signs, which any anneal-chosen value set is expected
to beat on the judge, and the real numbers were already known from C1161-GLOSS9 (info only); the gloss half carries 15 block
tokens for eight signs and none for spiralG. So the nine fit the gloss and the judge better than random values, jointly; no
single value is shown right (GLOSS9 0/9 per sign stays true). Grade S is per the brief; a verifier may hold any of them at M.
The prereg's "14 tokens" was a miscount; the script counts 15. Pre-change key kept as `two/key_pre_joint9.tsv`;
two/gloss9.py, glossjudge.py, wordcover.py and joint9.py now read it, so each still regenerates its committed output
(they assert the pre-change full_decode.txt). Rule 7: the reading changed, so a fresh re-derivation is owed before stage 9.

Report what was found and where it was not found: no outside source searched; novelty not classified. Requests: none.
Subagent calls: 0.

## Remaining gaps (C1161-JOINT9, 4 Oct 2026)
Read so far: 3389 cipher signs on all six cipher leaves/blocks (c185R 704, c186R 220, c186L 246, c187L 718, c187R 744, c188L 757), decoded under key.tsv: C 353, S 2070, M 952, U 33 tokens; 0 H. Nine C1161-LOLO values entered at S after the joint test PASS (C1161-JOINT9); per sign 0/9 (C1161-GLOSS9) still stands.
- 18 M-graded key signs (th, z, eloop, phi, 6r, 8, 2, tz ...) and the contested S signs 4, S - blocker: not-attempted; no further proposal on file for them (C1161-LOLO gave confirmations only for th, z, 4); next: a key-constrained lookalike pass on th/z/S/4 (below) before any new anneal, ~$3
- rule-7 re-derivation of the JOINT9 reading - blocker: not-attempted; key.tsv changed 9 values; next: fresh-session re-derivation from spec + key.tsv + ciphertext.tsv with tools/decode_key.py --check, ~$1
- new shapes NEW_c186L_1, NEW_c187L_1, NEW_c187R_1/_2, NEW_c188L_1/2/3 and iii barred vs bare - blocker: not-attempted; 33 U tokens incl. clear words; next: owner sign sorter pass or a per-shape split test at pooled N, ~$3
- the gap between the anneal optimum (-2.67 per letter) and genuine French at the measured error (-2.36 to -2.44 at 8-10%) - blocker: not-attempted; transcription error above the two-reader figure, a wrong held value, or a design element; next: a key-constrained lookalike pass on the highest-token free signs (th 208, z 189, S 275, 4 224) against the native crops, ~$3
- left edge of the gloss under the mount - blocker: illegible; letters cut by the mount on every line (c186Rmarg crops)

## Escalation (C1161-JOINT9, 4 Oct 2026)
- [x] siblings: all six cipher leaves/blocks transcribed and merged; c184 and c189 checked, no continuation (N4-C1 1a); c188L re-passed to err_2reader 0.084
- [x] clear-pages: the c186R marginal gloss matches at 0.647 under the current key.tsv (0.612 before JOINT9); the gloss itself PASSes the fr16 judge (-0.808), the decode FAILs (-1.303)
- [x] known-keys: fr16142 Noailles (Dax) Constantinople key, shape-level test 2/16 vs permutation p99 3, NO FIT (N4-C1 4); no other Noailles/Dax key on disk or in KEY-OFFICES.tsv
- [n/a] print: no printed edition of these Avis located by check-solved and Premise check
- [x] key-rebuild: nine C1161-LOLO proposals entered at S after the pre-registered joint test PASS (C1161-JOINT9); remaining M signs have no proposal, next instrument is the lookalike pass under image-check
- [ ] image-check: seven provisional new shapes; next: sorter or split test, and a lookalike pass on th/z/S/4, as in Remaining gaps
- [ ] retry: rule-7 re-derivation of the changed reading, as in Remaining gaps
Verdict: keep going: internal gaps open; cheapest next: fresh-session rule-7 re-derivation of the JOINT9 reading, ~$1

## Remaining gaps (C1161-GLOSS9, 4 Oct 2026)
Read so far: 3389 cipher signs on all six cipher leaves/blocks (c185R 704, c186R 220, c186L 246, c187L 718, c187R 744, c188L 757), decoded under key.tsv: C 353, S 1908, M 1114, U 33 tokens; 0 H. Per-sign gloss/judge of the nine C1161-LOLO proposals: 0/9 pass (C1161-GLOSS9); joint nine beat the shuffled-key null on the judge (info only).
- 27 M-graded key signs (th, z, rot, eloop, ls, o, phi, iib, 6r, 8, K, 2, tz ...) and the contested S signs 4, S - blocker: not-attempted; the per-sign gloss test cannot move a sign with 0-5 glossed tokens (C1161-GLOSS9, RUN4-C1161GJ); next: a pre-registered joint test of the nine C1161-LOLO proposals as one hypothesis (joint dG and dJ vs the 50-key shuffled joint null), ~$1
- new shapes NEW_c186L_1, NEW_c187L_1, NEW_c187R_1/_2, NEW_c188L_1/2/3 and iii barred vs bare - blocker: not-attempted; 33 U tokens incl. clear words; next: owner sign sorter pass or a per-shape split test at pooled N, ~$3
- the gap between the anneal optimum (-2.67 per letter) and genuine French at the measured error (-2.36 to -2.44 at 8-10%) - blocker: not-attempted; transcription error above the two-reader figure, a wrong held value, or a design element; next: a key-constrained lookalike pass on the highest-token free signs (th 208, z 189, S 275, 4 224) against the native crops, ~$3
- left edge of the gloss under the mount - blocker: illegible; letters cut by the mount on every line (c186Rmarg crops)

## Escalation (C1161-GLOSS9, 4 Oct 2026)
- [x] siblings: all six cipher leaves/blocks transcribed and merged; c184 and c189 checked, no continuation (N4-C1 1a); c188L re-passed to err_2reader 0.084
- [x] clear-pages: the c186R marginal gloss matches the blind key at 0.612 under the current key.tsv (shuffled max 0.312 at 0.594); the gloss itself PASSes the fr16 judge (-0.808), the decode FAILs (-1.233)
- [x] known-keys: fr16142 Noailles (Dax) Constantinople key, shape-level test 2/16 vs permutation p99 3, NO FIT (N4-C1 4); no other Noailles/Dax key on disk or in KEY-OFFICES.tsv
- [n/a] print: no printed edition of these Avis located by check-solved and Premise check
- [ ] key-rebuild: stage-1 leave-one-leaf-out anneal GATE PASS 3/3 with nine M proposals (C1161-LOLO); per-sign gloss+judge 0/9 (C1161-GLOSS9); next: pre-registered joint test of the nine, as in Remaining gaps
- [ ] image-check: seven provisional new shapes; next: sorter or split test, and a lookalike pass on th/z/S/4, as in Remaining gaps
- [n/a] retry: a further per-sign gloss run of the same nine is not a different instrument
Verdict: keep going: 3 internal gaps; cheapest next: pre-registered joint gloss+judge test of the nine C1161-LOLO proposals, ~$1

## VER-C1161J (account-3 verifier, 4 Oct 2026, 18:17-18:3x UTC by date -u)
Audit of C1161-JOINT9 (AUDIT.md section 7). Pre-registration `tx/PREREG_verc1161j.md` before any score; `two/verc1161j.py`.
The gloss was never an input of the LOLO anneal, and the c186R-held-out stream gives the same nine values, so G is
out-of-sample for the choice; but dJ is circular (the anneal maximises French 4-gram fit, the judge measures it) and the G gain
is not content-specific: the nine raise agreement with 200 random fr16 windows of the gloss's length by up to +0.17 (p95 +0.0824)
against +0.0353 on the gloss (T2 FAIL); a best-of-2000 L4-selected null is beaten (p95 +0.0059, pass). As registered, the nine go
back to **M** (values kept as working reading). Rule 7 of the JOINT9 reading: SAME. Counts now C 353, S 1908, M 1114, U 33; C/S
67.0%; depth D1 kept. Report what was found and where not found: no outside source searched; novelty not classified.

## Remaining gaps (VER-C1161J, 4 Oct 2026)
Read so far: 3389 cipher signs on all six cipher leaves/blocks (c185R 704, c186R 220, c186L 246, c187L 718, c187R 744, c188L 757), decoded under key.tsv: C 353, S 1908, M 1114, U 33 tokens; 0 H. The nine C1161-LOLO values are the working reading at M (VER-C1161J: joint gloss gain not above a fr16-window null).
- 27 M-graded key signs (th, z, eloop, phi, 6r, 8, 2, tz, and the nine LOLO values K, iib, l, ls, o, rot, spiralG, to, x) and the contested S signs 4, S - blocker: not-attempted; the c186R gloss (170 letters) cannot license a per-sign or nine-sign change (window null p95 +0.08); next: a key-constrained lookalike pass on th/z/S/4 against the native crops before any new anneal, ~$3
- new shapes NEW_c186L_1, NEW_c187L_1, NEW_c187R_1/_2, NEW_c188L_1/2/3 and iii barred vs bare - blocker: not-attempted; 33 U tokens incl. clear words; next: owner sign sorter pass or a per-shape split test at pooled N, ~$3
- the gap between the anneal optimum (-2.67 per letter) and genuine French at the measured error (-2.36 to -2.44 at 8-10%) - blocker: not-attempted; transcription error above the two-reader figure, a wrong held value, or a design element; next: the same lookalike pass on the highest-token free signs (th 208, z 189, S 275, 4 224), ~$3
- left edge of the gloss under the mount - blocker: illegible; letters cut by the mount on every line (c186Rmarg crops)

## Escalation (VER-C1161J, 4 Oct 2026)
- [x] siblings: all six cipher leaves/blocks transcribed and merged; c184 and c189 checked, no continuation (N4-C1 1a); c188L re-passed to err_2reader 0.084
- [x] clear-pages: the c186R marginal gloss matches at 0.647 under key.tsv; the nine's gain over the pre-JOINT9 key (+0.035) is inside a fr16-window null (p95 +0.082, VER-C1161J); the gloss PASSes the fr16 judge (-0.808), the decode FAILs
- [x] known-keys: fr16142 Noailles (Dax) Constantinople key, shape-level test 2/16 vs permutation p99 3, NO FIT (N4-C1 4); no other Noailles/Dax key on disk or in KEY-OFFICES.tsv
- [n/a] print: no printed edition of these Avis located by check-solved and Premise check
- [retired] key-rebuild: instrument c186R gloss match (G) for per-sign and joint value changes -- per-sign 0/9 (GLOSS9), joint gain inside the window null (VER-C1161J); reopens only with a longer clear text or new material
- [ ] image-check: seven provisional new shapes; next: sorter or split test, and a lookalike pass on th/z/S/4, as in Remaining gaps
- [x] retry: rule-7 re-derivation of the JOINT9 reading SAME (VER-C1161J); regraded reading --check exit 0
Verdict: keep going: 3 internal gaps; cheapest next: key-constrained lookalike pass on th/z/S/4 against the native crops, ~$3

## Desk runner 4 Oct 2026 (DESK-LAND, account-3 worker; JSTOR rows J22-J25)

Source: the owner's browser runner, outreach/local-runner/DESK-2026-10-04.md. The four JSTOR rows queued on 4 Oct 2026 are
answered in JSTOR-QUEUE.tsv:

| row | query | hits | relevant |
|---|---|---|---|
| J22 | Noailles Dax Villars 1570 chiffre Flandre | 9 | no -- indexes and bibliographies (top: Pannier, Table alphabétique 1852-1902, Bulletin SHPF 1902) |
| J23 | "Clairambault 1161" chiffre OR chiffrés | 0 | -- |
| J24 | "quant au fet de la religion en ce royaulme" | 0 | -- |
| J25 | "Advis de Flandres" 1570 | 0 | -- |

Search results, not a novelty verdict (rule 10); for the verifier to carry into AUDIT.md. No gap or escalation line changes.

## AUDIT 2 (VER1-C1161, verifier, 5 Oct 2026)
Second adversarial audit in AUDIT.md "## AUDIT 2 (VER1-C1161, 5 Oct 2026)": N3 confirmed, two audits, key ours, text not known
in print; depth D1 (C/S 67.0%, longest C/S run 16), not counted. Lauer t. II p. 332 read from Gallica page images: the entry
repeats the finding-aid words, no date, sender or decipherment. CSP Foreign 1569-71, CSP Spanish II, Teulet II: no hit.
status.json results row added; SO-C1161 queued. Suggestion for a solver (not actioned): shape test against the "Chiffre envoyé
en Flandres à monseigneur Des Pruneaux" (BnF fr. 3281, per Tomokiyo), ~$1. Novelty is classified only in AUDIT.md.

## D2-C1161LA (account-1 worker for LANE-D2PUSH, 5 Oct 2026, 18:47-18:5x UTC by date -u)
Brief `.claude/briefs/runs/2026-10-05-acct1-d2-c1161la.md`. Intake gate pasted: `ciphers/clair1161-avis-flandre-1688: partial (line 1)
-- edition/page or full-text-search citation found within 6 lines` (exit 0). PREREG `la/PREREG_c1161la.md` pushed before any
re-read or score (4baba1228). Scripts `la/build_align.py`, `la/make_tiles.py`, `la/la_test.py`.

- Packet: C (ciphertext.tsv) vs readers A/B aligned per line: 3434 signs, agree 2971, split 299, split_gap 81. Tiles = every split
  with th/z/S/4 on any side: **109** (merged z 45, s 17, th 11, S 6, 4 only 2). The other ~790 th/z/S/4 tokens have both readers
  agreeing and cannot be moved by a 2-of-3 rule (LESSONS.md "Look-alike pass").
- Instrument: `tools/lookalike_pass.py windows` (label hidden, candidates alphabetical, shapes from tx/labels_v2.md), 11 montages
  of per-tile windows cut from the existing native line crops (la/win/, gitignored; regenerate with the PREREG command). 3 Sonnet
  calls (40/40/29 tiles): conf H 31, M 63, L 15.
- Reconcile (2-of-3): 80 settled (70 confirm passC, **10 relabel**), 29 UNSETTLED -> `la/focus.tsv` for the owner's sign sorter.
  Residual 0.008 is agreement, not reader error.
- Test (50 random same-label relabel seeds): dG real +0.0000 vs null p95 +0.0000 -- none of the 10 lies in the c186R block, so G
  cannot discriminate (the PREREG's named case); dJ real +0.00128 vs null p95 -0.00048 (beats); longest C/S run 16 -> 16.
  **GATE FAIL as registered; the 10 relabels are NOT applied.** ciphertext.tsv, key.tsv and grades unchanged (C 353, S 1908,
  M 1114, U 33; C/S 67.0%); no decode, depth or AUDIT propagation owed. The judge gain alone is information only.
- The 10 relabels for a future sorter/verifier (passD.tsv): c185R_L07.9 q->ls, c186L_L07.21 4->qb, c187L_L04.5 y->S,
  c187L_L06.24/L11.21/L13.15 sd->S, c187L_L07.15 and L23.5 2->z, c187L_L23.12 th->dia, c187R_L15.28 w->z.
Report what was found and where it was not found: no outside source searched; novelty not classified. Subagent calls: 3 (Sonnet).

## Remaining gaps (D2-C1161LA, 5 Oct 2026)
Read so far: 3389 cipher signs on all six cipher leaves/blocks (c185R 704, c186R 220, c186L 246, c187L 718, c187R 744, c188L 757), decoded under key.tsv: C 353, S 1908, M 1114, U 33 tokens; 0 H. th/z/S/4 look-alike pass: 10 relabels found, gate FAIL (G non-discriminating outside c186R), not applied.
- 27 M-graded key signs (th, z, eloop, phi, 6r, 8, 2, tz, and the nine LOLO values K, iib, l, ls, o, rot, spiralG, to, x) and the contested S signs 4, S - blocker: not-attempted; the c186R gloss (170 letters) cannot license value changes and the 2-of-3 look-alike pass cannot touch agreed tokens; next: the 29 unsettled tiles (la/focus.tsv) plus the 10 relabels through the owner's sign sorter, then a held-out-leaf judge test of the sorted transcription, ~$2
- new shapes NEW_c186L_1, NEW_c187L_1, NEW_c187R_1/_2, NEW_c188L_1/2/3 and iii barred vs bare - blocker: not-attempted; 33 U tokens incl. clear words; next: owner sign sorter pass or a per-shape split test at pooled N, ~$3
- the gap between the anneal optimum (-2.67 per letter) and genuine French at the measured error (-2.36 to -2.44 at 8-10%) - blocker: not-attempted; agreed-but-wrong signs are invisible to the look-alike pass (D2-C1161LA); next: a TX-AGREEAUDIT planted audit (`lookalike_pass.py audit` + `windows --items`) on agreed th/z/S/4 tokens, ~$3
- left edge of the gloss under the mount - blocker: illegible; letters cut by the mount on every line (c186Rmarg crops)

## Escalation (D2-C1161LA, 5 Oct 2026)
- [x] siblings: all six cipher leaves/blocks transcribed and merged; c184 and c189 checked, no continuation (N4-C1 1a); c188L re-passed to err_2reader 0.084
- [x] clear-pages: the c186R marginal gloss matches at 0.647 under key.tsv; the gloss PASSes the fr16 judge (-0.808), the decode FAILs
- [x] known-keys: fr16142 Noailles (Dax) Constantinople key, shape-level test 2/16 vs permutation p99 3, NO FIT (N4-C1 4); fr.3281 Des Pruneaux key shape test with D2-C1161PRU (same lane)
- [n/a] print: no printed edition of these Avis located by check-solved and Premise check
- [retired] key-rebuild: instrument c186R gloss match (G) for per-sign and joint value changes -- per-sign 0/9 (GLOSS9), joint gain inside the window null (VER-C1161J); reopens only with a longer clear text or new material
- [ ] image-check: th/z/S/4 split-tile look-alike done (10 relabels, gate FAIL, D2-C1161LA); next: planted agreed-token audit on th/z/S/4, and the sorter for the 29 unsettled tiles and seven new shapes, as in Remaining gaps
- [x] retry: rule-7 re-derivation of the JOINT9 reading SAME (VER-C1161J); regraded reading --check exit 0
Verdict: keep going: 3 internal gaps; cheapest next: planted agreed-token audit (lookalike_pass.py audit + windows --items) on th/z/S/4, ~$3
## D2-C1161PRU: fr.3281 f.4 Des Pruneaux key, shape test (account-1 worker for LANE-D2PUSH, 5 Oct 2026, 18:48-19:0x UTC by date -u)
Brief `.claude/briefs/runs/2026-10-05-acct1-d2-c1161pru.md`. Intake gate, pasted before work:
`clair1161-avis-flandre-1688: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
- **Located.** Tomokiyo (cyphersolver mirror `research/gallica_sweep/src/henryiii.txt`, shallow clone 5 Oct 2026): "Chiffre envoye en
  Flandres a monseigneur Des Pruneaux" (f.4); Des Pruneaux represented Alençon before the States General from 1578; two homophones
  per letter, double-letter signs, code words. Gallica SRU `dc.source all "Français 3281"` -> ark:/12148/btv1b9060310c; catalogue
  record http://archivesetmanuscrits.bnf.fr/ark:/12148/cc49738j; SRU dc: "domaine public", "Numérisation effectuée à partir d'un
  document de substitution" (microfilm, two-page openings, 173 canvases, no folio labels). Contents note item 3 = « Chiffre envoyé
  en Flandres à monseigneur Des Pruneaux ». Key sheet = canvas 5, right page; folio "4" read on the leaf (pru/images/fr3281c5_L01_s2.jpg).
- **Crops** (pasted): `python3 tools/iiif_lines.py --ark btv1b9060310c --canvas 5 --region 4400,250,3950,5300 --out
  ciphers/clair1161-avis-flandre-1688/pru/images --prefix fr3281c5 --debug` (19 lines, 38 crops) and, for the alphabet block,
  `python3 tools/iiif_lines.py --image .../src_ark_12148_btv1b9060310c_f5_4400_250_3950_5300.jpg --region 0,330,3950,800
  --lines-per-crop 9 --out ciphers/clair1161-avis-flandre-1688/pru/images --prefix fr3281c5alpha --max-width 1400 --overlap 100` (3 crops).
- **Transcription.** 24 columns (a b c d e f g h i k l m n o p q r s t u x y z &), two cipher symbols each. Pass A (this worker) and
  pass B (Sonnet subagent, blind, the 3 alphabet crops only) in `pru/sheet_f4.tsv`; reconciliation kept a shape only where both
  passes describe it the same way (17 cells, `pru/cells.tsv`); dropped on disagreement: f/r/t "6"/"θ" shapes, q row 2 (p vs f),
  p row 2 (8 vs e), o row 2, n/z row 2 "d" (no bar across the ascender, labels_v2 d needs one). The code-word list below "Nulles"
  was not transcribed (a word code has no counterpart in the 1161 sign inventory's shape test).
- **Test** (pru/PREREG_pruneaux.md, pushed 7e07995e9 before scoring; `python3 pru/shape_test.py`, output `pru/shape_test.out`):
  **2/17** labels carry the sheet's letter in key.tsv (7 = i, S = u). Permutation null over key.tsv's values on the same 17 labels
  (10,000, seed 1): mean 0.88, p99 4, P(null >= 2) = 0.217. **Gate: NO FIT.** Instrument 2 not scored (not gated).
- Caveats: the worker had seen several key.tsv values (two/tomokiyo.tsv) before the PREREG, flagged per cell in cells.tsv; both hits
  are on cells whose shape is unambiguous in both passes. The sheet is c. 1578-79; the 1161 item's date is unsettled. The shared
  shape stock is real (6r is a sign both alphabets carry, as are 7, 4, 3, x, a, z, L, iii-with-bar), but the values do not match:
  6r = b on the sheet, i in key.tsv. A shared office stock with re-assigned values, not the same key.
- Not tested: the different "Pruneaux-Aranger" cipher in the same volume (ff.120-140, Oct-Dec 1579, per Tomokiyo, rebuilt from
  decipherments on separate sheets); Gallica requests this job 14 (SRU 1, manifest 1, info.json 1, thumbnails 9 incl. 1 reset, 2 region fetches).
- Images kept: the folio-number crop and the 3 alphabet crops only (pru/images, 0.6 MB); the region source and other line crops are re-made by the first iiif_lines command above (folder stays under 30 MB).

## Remaining gaps (D2-C1161PRU, 5 Oct 2026)
Read so far: 3389 cipher signs on all six cipher leaves/blocks (c185R 704, c186R 220, c186L 246, c187L 718, c187R 744, c188L 757), decoded under key.tsv: C 353, S 1908, M 1114, U 33 tokens; 0 H (unchanged by this job; no grade moved).
- 27 M-graded key signs (th, z, eloop, phi, 6r, 8, 2, tz, and the nine LOLO values K, iib, l, ls, o, rot, spiralG, to, x) and the contested S signs 4, S - blocker: not-attempted; neither known key on file fits (fr16142 2/16, fr.3281 f.4 2/17, both NO FIT); the th/z/S/4 split-tile look-alike pass found 10 relabels but FAILed its gate (D2-C1161LA); next: planted agreed-token audit (lookalike_pass.py audit + windows --items) on th/z/S/4, ~$3
- new shapes NEW_c186L_1, NEW_c187L_1, NEW_c187R_1/_2, NEW_c188L_1/2/3 and iii barred vs bare - blocker: not-attempted; 33 U tokens incl. clear words; next: owner sign sorter pass or a per-shape split test at pooled N, ~$3
- the gap between the anneal optimum (-2.67 per letter) and genuine French at the measured error (-2.36 to -2.44 at 8-10%) - blocker: not-attempted; transcription error above the two-reader figure, a wrong held value, or a design element; agreed-but-wrong signs are invisible to the look-alike pass (D2-C1161LA); next: the same planted agreed-token audit, ~$3
- left edge of the gloss under the mount - blocker: illegible; letters cut by the mount on every line (c186Rmarg crops)

## Escalation (D2-C1161PRU, 5 Oct 2026)
- [x] siblings: all six cipher leaves/blocks transcribed and merged; c184 and c189 checked, no continuation (N4-C1 1a); c188L re-passed to err_2reader 0.084
- [x] clear-pages: the c186R marginal gloss matches at 0.647 under key.tsv; the nine's gain over the pre-JOINT9 key (+0.035) is inside a fr16-window null (p95 +0.082, VER-C1161J); the gloss PASSes the fr16 judge (-0.808), the decode FAILs
- [x] known-keys: fr16142 Noailles (Dax) Constantinople key 2/16 vs p99 3 (N4-C1 4) and BnF fr.3281 f.4 Des Pruneaux Flanders key 2/17 vs p99 4 (D2-C1161PRU), both NO FIT; the fr.3281 Pruneaux-Aranger cipher (1579) not tested, a later key of a different design
- [n/a] print: no printed edition of these Avis located by check-solved and Premise check
- [retired] key-rebuild: instrument c186R gloss match (G) for per-sign and joint value changes -- per-sign 0/9 (GLOSS9), joint gain inside the window null (VER-C1161J); reopens only with a longer clear text or new material
- [ ] image-check: th/z/S/4 split-tile look-alike done (10 relabels, gate FAIL, D2-C1161LA); next: planted agreed-token audit on th/z/S/4, and the sorter for the 29 unsettled tiles and seven new shapes
- [x] retry: rule-7 re-derivation of the JOINT9 reading SAME (VER-C1161J); regraded reading --check exit 0
Verdict: keep going: 3 internal gaps; cheapest next: planted agreed-token audit (lookalike_pass.py audit + windows --items) on th/z/S/4, ~$3

## D2-C1161AUD: planted agreed-token audit on th/z/S/4 (account-1 worker for LANE-D2PUSH, 5 Oct 2026, 19:07-19:1x UTC by date -u)
Brief `.claude/briefs/runs/2026-10-05-acct1-d2-c1161aud.md`. Intake gate, pasted before work:
`ciphers/clair1161-avis-flandre-1688: partial (line 1) -- edition/page or full-text-search citation found within 6 lines` (exit 0).
PREREG `aud/PREREG_c1161aud.md` pushed before any re-read or score (0c5f581f3).
- Items: `python3 aud/run_audit.py` (`lookalike_pass.audit`, pool narrowed to D2-C1161LA's agreed th/z/S/4 positions, 829 tokens:
  4 222, S 266, th 197, z 144), seed 51, 120 items, 20 plants to the top confusion partner (th->dia 7, z->tz 6, 4->qb 4, S->s 3),
  `--hide-passc`. Hidden answers `aud/c1161aud_audit_items.tsv`. Tool fix on the way (85a0caff3): a transcription's own
  `[PLAIN:..]` token was parsed as an audit bracket and crashed the prompt; offline test 2d added, all three lookalike tests pass.
- Instrument (pasted): `python3 tools/lookalike_pass.py windows --items aud/c1161aud_audit_items.tsv --passc la/passC.tsv
  --manifest la/crops/manifest.json --crop-pattern '{line}_s*' --out aud --run c1161aud_win --per 10 --scale 1 --desc la/desc.tsv`
  -- 120 per-item windows cut from the existing native line crops (made by the iiif_lines.py commands recorded above), 12 montages
  (aud/win/, gitignored; regenerate with the command). 3 Sonnet calls of 40 items (aud/part{1,2,3}_prompt.md -> aud/reread.tsv).
- Score (`lookalike_pass.py audit-score`, aud/score.json): **planted catch 13/20 = 0.65 < gate 0.80 (and < the brief's 0.70):
  NON-TEST, exit 3.** No unplanted figure is interpreted and nothing is applied; ciphertext.tsv, key.tsv and grades unchanged
  (C 353, S 1908, M 1114, U 33); no decode, depth or AUDIT propagation owed.
- Diagnosis (information only, not a re-score): per plant class th->dia 7/7, z->tz 4/6, S->s 1/3, 4->qb 1/4. Of the 7 misses, 6
  picked the original label but at conf L (the tool's rule counts only H/M), 1 picked the planted label at L. The reader marked
  99 of 120 answers M and only 2 H: on this hand, at --scale 1 with the evenly-spaced x estimate, it does not commit on the
  4/qb and S/s pairs, so the instrument cannot license a negative on agreed tokens there. Unplanted firm flags 5/100 (th->S 3,
  4->qb 1, 4->+ 1; no class near the registered >= 10), so the conditional relabel test was not run; the 5 go to `aud/focus.tsv`
  for the owner's sign sorter beside la/focus.tsv.
Report what was found and where it was not found: no outside source searched; novelty not classified. Subagent calls: 3 (Sonnet).

## Remaining gaps (D2-C1161AUD, 5 Oct 2026)
Read so far: 3389 cipher signs on all six cipher leaves/blocks (c185R 704, c186R 220, c186L 246, c187L 718, c187R 744, c188L 757), decoded under key.tsv: C 353, S 1908, M 1114, U 33 tokens; 0 H (unchanged by this job; no grade moved).
- 27 M-graded key signs (th, z, eloop, phi, 6r, 8, 2, tz, and the nine LOLO values K, iib, l, ls, o, rot, spiralG, to, x) and the contested S signs 4, S - blocker: not-attempted; neither known key on file fits (fr16142 2/16, fr.3281 f.4 2/17, both NO FIT); split-tile look-alike gate FAIL (D2-C1161LA); planted agreed-token audit NON-TEST (catch 0.65, D2-C1161AUD); next: the owner's sign sorter on la/focus.tsv (29 tiles) + aud/focus.tsv (5), then a held-out-leaf judge test of the sorted transcription, ~$2
- new shapes NEW_c186L_1, NEW_c187L_1, NEW_c187R_1/_2, NEW_c188L_1/2/3 and iii barred vs bare - blocker: not-attempted; 33 U tokens incl. clear words; next: owner sign sorter pass or a per-shape split test at pooled N, ~$3
- the gap between the anneal optimum (-2.67 per letter) and genuine French at the measured error (-2.36 to -2.44 at 8-10%) - blocker: not-attempted; agreed-but-wrong signs unmeasured: the Sonnet window reader missed the planted control on 4/qb and S/s (D2-C1161AUD); next: the same planted audit with a different instrument (per-line slope-followed re-cuts, iiif_lines.py --follow-slope, --scale 2, Opus reader), PREREG unchanged in gate, ~$4
- left edge of the gloss under the mount - blocker: illegible; letters cut by the mount on every line (c186Rmarg crops)

## Escalation (D2-C1161AUD, 5 Oct 2026)
- [x] siblings: all six cipher leaves/blocks transcribed and merged; c184 and c189 checked, no continuation (N4-C1 1a); c188L re-passed to err_2reader 0.084
- [x] clear-pages: the c186R marginal gloss matches at 0.647 under key.tsv; the nine's gain over the pre-JOINT9 key (+0.035) is inside a fr16-window null (p95 +0.082, VER-C1161J); the gloss PASSes the fr16 judge (-0.808), the decode FAILs
- [x] known-keys: fr16142 Noailles (Dax) Constantinople key 2/16 vs p99 3 (N4-C1 4) and BnF fr.3281 f.4 Des Pruneaux Flanders key 2/17 vs p99 4 (D2-C1161PRU), both NO FIT; the fr.3281 Pruneaux-Aranger cipher (1579) not tested, a later key of a different design
- [n/a] print: no printed edition of these Avis located by check-solved and Premise check
- [retired] key-rebuild: instrument c186R gloss match (G) for per-sign and joint value changes -- per-sign 0/9 (GLOSS9), joint gain inside the window null (VER-C1161J); reopens only with a longer clear text or new material
- [ ] image-check: split-tile look-alike done (10 relabels, gate FAIL, D2-C1161LA); planted agreed-token audit with the Sonnet window reader NON-TEST (catch 0.65 < 0.80, D2-C1161AUD); next: the owner's sign sorter on la/focus.tsv + aud/focus.tsv, or the audit with re-cut slope-followed windows and a stronger reader
- [x] retry: rule-7 re-derivation of the JOINT9 reading SAME (VER-C1161J); regraded reading --check exit 0
Verdict: keep going: 3 internal gaps; cheapest next: owner's sign sorter on la/focus.tsv + aud/focus.tsv, then a held-out-leaf judge test, ~$2
