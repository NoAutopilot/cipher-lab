open
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
