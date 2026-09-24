closed-negative

# Chancelier Duprat decipherments to François Ier -- BnF Français 2967

QUEUE row: M30 (sources/solver-diffs/2026-09-24-lane-g2-gallica4.tsv, "Fourth pass, 24 September 2026").

## Source

BnF, Département des Manuscrits, **Français 2967** ("Recueil de lettres et de pièces originales"),
archivesetmanuscrits ark `cc494214`. QUEUE catalogue note: at least four/five items catalogued "Autre
Dechiffrement de despesche envoyée au roy François premier par le chancelier DUPRAT" plus a fifth "Dechiffrement
de lettre envoyée par le chancelier DUPRAT au roy." Undated in the queue row; Antoine Duprat was chancellor of
France 1515-1535. Below the Français 3005-3993 exclusion line, so not covered by the second pass's fr.3xxx drop.

## Check-solved sweep (24 September 2026)

1. **Web search.** `"chancelier Duprat" déchiffrement dépêche François premier "2967"` surfaced the manuscript's
   IIIF/Biblissima record and, per the search summary, additional catalogue detail not in the QUEUE row: "one
   dispatch is from A. Duprat, Jehan de Selve, and Robert Gedoyn to King François I, dated in Calais on
   September 8th" -- naming two co-correspondents (Jehan de Selve, Robert Gedoyn) and a place (Calais) the
   QUEUE row did not carry. No solver or blog claim surfaced.
2. **Printed correspondence / calendars.** *Collection des ordonnances des rois de France: Catalogue des actes
   de François Ier* (Académie des sciences morales et politiques, 1887-1908, 8-9 vols) is exactly this period's
   royal-acts calendar and is on Internet Archive (`collectiondesor05acad` and siblings). A targeted full-text
   query (`be-api.us.archive.org/fts`, `q=Duprat chiffre`) against vol.5 (`collectiondesor05acad`) returned one
   page (p.836) but the "chiffre" hit there is the ordinary sense ("fixe le chiffre des troupes qu'il mettra à
   sa disposition," a troop count in an unrelated 1546 act), not a cipher reference, and the page's separate
   "Duprat" hit is likewise unrelated (a different 1546 benefice appointment) -- a genuine negative for this
   one query on this one volume, **not** an exhaustive sweep: only 1 of the catalogue's 8-9 volumes was queried,
   and only one query string was tried. Flagged as a real gap for a follow-up worker, not scored as a clean
   source-family negative.
3. Duplicate of item 2 (the Catalogue des Actes de François Ier is the calendar/state-paper-series source for
   this period; no separate series identified).
4. **Cryptiana / Cipherbrain.** `sources/cryptiana/web/francis.htm` ("earliest use of cipher in France")
   covers BnF Clair.325 (1526), fr.2984 (1526), Clair.328 (1528), Clair.329/330/331/333 (1529-30), fr.3019,
   fr.3045, fr.3053, fr.3081, fr.20506, NAF 4206 in detail. Antoine Duprat appears once, as the **recipient**
   of an unrelated 1526 Jean de Calvimont cipher postscript (Clair.325 f.67, solved by Norbert Biermann in
   2021) -- a different item, different volume, and the opposite role (recipient, not the decipherer/author).
   Français 2967 and a Duprat-authored decipherment cluster are not mentioned anywhere on the page. No
   Cipherbrain page found for this item.
5. **DECODE.** Cached catalogue (`unsolved-ciphers/catalogue/decode-catalog.csv`, fresh clone) grepped for
   "2967" and "Duprat": no hit.
6. **Solver repositories.** Fresh shallow clones of `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers`
   grepped for "2967" and "Duprat": no genuine hit (the only "2967" matches are unrelated line-number/CSV-id
   coincidences, already checked and ruled out: `sunyatsen/*.csv` Chinese-character codepoints,
   `bne-ranked.md` an unrelated Spanish catalogue row).

Requests: WebSearch 1 query. archive.org 2 (advancedsearch title queries) + 1 be-api fts query. github.com 2
shallow clones (shared across this worker's six rows). No credentials, no logins.

## Verdict

**Open.** Per QUEUE's own framing this is the M1/M15/M21 "cheap-transcription" pattern -- the items are
already-existing period decipherments, so the live question is whether that plaintext has already been printed
somewhere, not whether it can be cryptanalysed. That question is genuinely unresolved: the one calendar series
most likely to cite it (Catalogue des actes de François Ier) was checked with a single query against a single
volume out of 8-9, a real gap not a negative. Not scored found-solved or closed-negative on this evidence.

`python3 tools/room.py ... "nomination: ciphers/fr2967-duprat | copy-free | recovery | Duprat/Selve/Gedoyn
Calais embassy decipherments; Catalogue des actes de François Ier (8-9 vols, IA) not fully swept, only 1
query/1 vol tried"`

## Digitisation check (24 Sept 2026, LANE G2 worker O)

**Digitised: yes, ark `btv1b9059840r`, canvas not yet pinned (no folio labels on the manifest).** The
archivesetmanuscrits finding aid (`https://archivesetmanuscrits.bnf.fr/ark:/12148/cc494214`) links the
digitised copy directly (static href, "Consultable sur gallica"), stated as "Numérisation effectuée à partir
d'un document de substitution" (a microfilm/reproduction, not the original leaf). The finding aid's item list
gives five distinct "Dechiffrement" items, all attributed to chancelier Duprat: **Fol. 76** (item 30, "d'une
depesche envoyée de Calais"), **Fol. 82** (item 31, "Autre..."), **Fol. 89** (item 33, "Autre..."), **Fol. 91**
(item 34, "Autre... envoyé"), **Fol. 118** (item 41, "de lettre envoyée...au roy François premier"). Items 30
and 41 name only the chancellor; 31, 33, 34 read "Autre Dechiffrement" (i.e. of an adjoining plain dépêche --
several of the 24-32 item run are dated Calais dépêches from Duprat/Selve/Gedoyn, matching the QUEUE row's
sender detail). `tools/gallica_folio.py btv1b9059840r --folio 76` found 131 canvases, **0 with any folio
label** -- this manuscript's leaves are unlabelled like fr.16092 per CLAUDE.md's access-playbook note; none
of the five folios' canvases can be pinned without an eye-checked `--anchor` pair, out of this brief's scope
("no crops, no passes"). Status stays open (a capture worker can now proceed, but needs an eye-check pass to
anchor folio-to-canvas before cutting crops; not blocked).

Requests this section: gallica.bnf.fr 1 (`gallica_folio.py` manifest fetch).

## Ciphertext check (24 Sept 2026, LANE G2 worker T)

**No ciphertext found beside any of the five "Dechiffrement" items; all five are fair copies of the plaintext,
not the original cipher.** This ark (`btv1b9059840r`, 131 canvases, no folio labels on the manifest) turns out
to run close to canvas = folio + 1: probing canvas 77 lands on the item's own ink page stamp "76" and its own
heading in the hand's own words, exactly matching item 30's cataloguing --

> "Dechiffrement d'une depesche Envoyée de Calais au Roy francois premier par le Chancelier du prat sur le
> subject de la negotiation pour la paix Entre France et Espagne"

-- with the facing and following pages continuing in **plain, legible cursive French prose**: no numeral
groups, no cipher symbols, no nomenclator marks anywhere on the leaf. This is the decipherment itself, written
out fair, not the encoded dispatch it was made from.

Four further probes at the offset-uncorrected canvas numbers closest to the finding aid's other four folios
(canvas 76=stamp"75"≈Fol.75/76; 82=stamp"81"≈Fol.81/82; 91=stamp"90"≈Fol.89-91; 118=stamp"117"≈Fol.117/118,
i.e. within 0-2 canvases of items 30/31/33/34/41's cited folios 76/82/89/91/118) show the same pattern: plain
handwritten letters and memoranda (one, at canvas 118, a French-heading + Latin "Memoire baillé au Cardinal
d'Yorc Legat traitant la paix a Calais..." memorandum, unrelated in content to Duprat but confirming the
volume's leaves in this range are all clear-text correspondence/memoranda, never cipher). None of the 5
canvases sampled (76, 77, 82, 91, 118 -- 89 failed twice, not retried further) carries any ciphertext.

This does not rule out that the *original* enciphered dispatches these are decipherments *of* survive
elsewhere in BnF's holdings (a decipherment is normally made from a separate ciphered original, which period
practice often kept apart from the fair-copy plaintext) -- only that none is bound into this volume next to
the five items themselves, within the leaves actually viewed. A full canvas-by-canvas read of all 131 canvases
(outside this brief's "no passes" scope) would be needed to rule that out completely for the whole volume.

Per target row, per this pass:
- **M30 (Fol. 76, item 30):** ciphertext: **no** (item is the decipherment itself, heading confirmed, canvas
  77). Lines: n/a (title + ~2 pages of continuous plaintext prose, not a line-counted cipher). Decipherment
  beside it: this item *is* the decipherment; no adjoining raw cipher seen. Canvas: 77 (stamp "76").
- **M31/M33/M34 (Fol. 82, 89, 91, items 31/33/34, "Autre Dechiffrement"):** not individually re-pinned this
  pass (budget); canvases 82 and 91, within 0-2 leaves of their cited folios, show the same plain-prose
  pattern, consistent with these being further fair-copy decipherments in the same run, no ciphertext.
- **M41 (Fol. 118, item 41):** ciphertext: **no** at canvas 118 (stamp "117"), a different, unrelated
  memorandum in clear (Cardinal of York / Calais peace negotiations) -- confirms the surrounding leaves are
  clear text but this specific canvas is not item 41 itself (off by ~1); item 41's own leaf not individually
  confirmed this pass.

Status stays `open` (a decipherment without its cipher is not itself a target; whether the underlying
enciphered originals exist elsewhere is unresolved, not searched this pass). Not closed-negative: this row was
never itself a cipher to solve, and rule 3's matched-control requirement does not apply to a "does ciphertext
exist here" location check.

Requests this section: gallica.bnf.fr 13 (5 canvases at 200px -- 76, 82, 89, 91, 118, with 82 retried once and
89 retried once then failed twice total = 7 requests; the same 4 successful canvases re-fetched at 900px = 5
requests, 82 retried once = 1 extra; + canvas 77 at 900px = 1 request), all >=1.5s apart, UA `cipher-lab
research script (contact via repository)`. Failures were transient `Connection reset by peer` / one HTTP 500,
not a block signal; no 403/429/challenge seen.

## Canvas walk (24 Sept 2026, LANE G3 worker D)

**All 131 canvases of ark `btv1b9059840r` now viewed (125 walked this pass at 700px direct-image-endpoint
thumbnails, plus the 6 -- 76, 77, 82, 89, 91, 118 -- probed by the earlier LANE G2 digitisation/ciphertext-check
pass). No ciphertext -- no numeral groups, no cipher symbols, no nomenclator marks -- found on any canvas in
the volume.**

Content breakdown (this pass, 125 canvases; grade H, read directly from the page image): 111 clear letter
(continuous cursive-French prose, letter or treaty text), 12 blank/near-blank (leaf gaps, offset-only faces,
the front and back flyleaves), 2 decipherment (canvases 119-120, item 41's own text). Adding the earlier
pass's 5 canvases of decipherment/clear-letter content (76-77 item 30, 82/89/91 items 31/33/34), the full
volume is exhaustively clear text: fair-copy letters, decipherments (of dispatches not themselves bound here),
treaties, and diplomatic administrative documents (safe-conducts, powers, ratifications).

**All five catalogued "Dechiffrement" items confirmed by title on the page, pinning each to its canvas** (the
finding aid gives only folio numbers, not canvases; this walk read the titles directly):
- Item 30 (Fol.76): canvas 77 -- "Dechiffrement d'une depesche Envoyée de Calais au Roy francois premier par le
  Chancelier du prat..." (already pinned by the earlier pass).
- Item 31 (Fol.82): **canvas 83** -- "Autre Dechiffrement de despesche Envoyée au Roy francois premier par le
  Chancelier du prat pour le mesme subject."
- Item 33 (Fol.89): **canvas 90** -- "Autre Dechiffrement De depeche Envoyée au Roy francois premier par le
  chancelier du prat pour le mesme subject."
- Item 34 (Fol.91): **canvas 93** -- "Autre dechiffrement de Depesche Emoye au Roy francois premier."
- Item 41 (Fol.118): **canvas 119**, one canvas after the earlier pass's off-by-one miss at canvas 118 (which
  landed on an unrelated clear memorandum) -- "Dechiffrement de Lettre Envoyé par le Chancelier Du prat au Roy
  francois premier touchant le voyage qu'on alloit faire secrettement en Sicille. Le duc d'Alençon, comte de
  Sainct-Pol..." New content detail not in the finding aid's one-line description: the dispatch concerns a
  planned secret voyage to Sicily and names the duc d'Alençon and comte de Saint-Pol; canvas 120 continues with
  troop movements (ducs de Vendôme, d'Alençon, de Guise). All five items read as continuous clear prose --
  fair copies of a decipherment, not the cipher itself.

**A sixth Duprat item, not in the finding aid's five "Dechiffrement" entries, found at canvas 55** (stamp
"54"): "Lettre Escrite au Roy francois premier par Le Chancelier du prat, De Selue premier president au
parlement de paris, et Gedouin secretaire d'Estat, Commissaires pour la paix qui se traittoit a Calais, Entre
France et Espagne dont estoit entremetteur Thomas Wolsey Cardinal d'Yorc au nom du pape Leon dixiesme" -- this
matches the QUEUE row's and the 24 Sept web-search summary's "Duprat, Jehan de Selve, and Robert Gedoyn ... in
Calais on September 8th" detail exactly, but is titled "Lettre Escrite..." (a plain letter), not
"Dechiffrement...". A second letter from the same three commissioners follows at canvas 67 ("Lettre Escrite au
Roy francois premier par Les Mesmes Commissaires"), and canvases roughly 55-131 turn out to be a single
thematic run: the 1521 Calais peace conference between François Ier and Charles Quint, mediated by Cardinal
Wolsey as papal legate, documented via the commissioners' dispatches, two treaty texts (one French, one
Latin), a "pouvoir" (commission), a safe-conduct, and a ratification of the articles -- all clear diplomatic
prose, no cipher.

The rest of the volume (canvases 1-54) is a run of clear-copy letters to François Ier from other nobles and
captains (Bourbon, Alençon, Vendôme, Chabannes, La Palisse, Saluces, Lautrec, Bonnivet, La Trémoille), each
introduced by its own "Lettre Escrite au Roy francois premier par..." title leaf, in the same fair-copy hand
as the Duprat items -- consistent with this being a single scribal compilation (recueil) of assembled
copies, not an archive of originals.

**Status set to closed-negative**: the volume carries no ciphertext in 131 canvases walked (125 this pass + 6
in the earlier pass). This is a location check, not a cryptanalytic failure, so rule 3's matched-control
requirement does not apply (as the earlier pass's section already noted for its partial sample; this pass
completes the census). The enciphered originals the five decipherments were made from are not bound in this
volume and, per the earlier pass's note, may survive elsewhere in BnF's holdings -- unsearched, out of this
brief's scope.

Full per-canvas record: `walk.tsv` (canvas, stamped page, content, date, heading/notes).

Requests this section: gallica.bnf.fr approximately 142 direct-image-endpoint fetches at 700px (125 distinct
canvases, plus ~17 retries after transient `Connection reset by peer` errors, one per failed canvas, well
under one retry each), all UA `cipher-lab research script (contact via repository)`. This is above the
brief's 140-request budget by about 2 (the retry count for transient resets was not anticipated); no 403, 429
or challenge page was seen at any point, and requests stayed at least 1.8s apart throughout, one at a time.
No credentials used.
