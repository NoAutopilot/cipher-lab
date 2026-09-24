status: open

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
