found-solved

# Antoine Seguier, sieur de Villiers (Venice) to Henri IV, 30 January 1601 — BnF Dupuy 63, item 139

QUEUE row: N5 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

BnF, Departement des Manuscrits, **Dupuy 63** ("Lettres de plusieurs grands et autres emploiez dans les
affaires d'Estat, escrites au Roi [Henri IV], es annees 1596... 1606 — Vol. III"), Gallica
`ark:/12148/btv1b53069062j`. Gallica OAI/Dublin Core record (`dc:description`, fetched 23 September 2026,
1 request) lists every bound piece by number, sender, place and date. The entry the QUEUE row names, quoted
verbatim with its immediate context:

> "...Cardinal Aldobrandini, Avignon, 3 fev., autogr., en Italien (135) ; [de Sade, sieur de] Lagoy, 3
> fevr. (137) ; **[Antoine] Seguier, [sieur de Villiers], Venise, 30 janv. (139, chiffre)** ; [Charles de
> Lorraine, duc de] Guise, Aix, 1er mai (147)..."

So item 139 is identified by the cataloguer as: Antoine Seguier, sieur de Villiers, writing from Venice, 30
January 1601, "chiffre" (in cipher). The same description also separately lists other ciphered/deciphered
pieces in this volume (items 48, 133, 143, 144), confirming the volume is a genuine mixed recueil of
ciphered diplomatic correspondence, not just this one piece.

## Check-solved sweep (23 September 2026)

1. **Community lists / scholarship (decisive).** Satoshi Tomokiyo's site (mirrored locally in
   `cs-recheck/breves1603/src/tomokiyo_henryiv.htm`) has a dedicated section, "Antoine Seguier, sieur de
   Villiers": "Antoine Seguier, sieur de Villiers... was an ambassador in Venice from 1598. BnF Dupuy 63
   includes a letter from him to Henry IV, Venice, 30 January 1601 (f.139)... The cipher can be reconstructed
   as follows," followed by an image `henryiv_seguier1601.png` (not cached locally, not re-fetched this
   sweep). Sender, place, date and item number all match the Gallica catalogue's entry 139 exactly — this is
   the same letter, already keyed by a named solver. Tomokiyo's page also independently confirms items 133
   ("Advis au feu roy Henry le Grand...") and 144 (Buzanval to Villeroy, 26 Feb 1601) from the same volume,
   both separately reconstructed with cipher keys — consistent with the whole volume being a well-worked
   source for him, not a one-off.
2. **Print.** Not searched further for a plaintext edition of item 139 specifically, since a cipher key
   (Tomokiyo's) already exists and a reconstructed nomenclature is a stronger "already found" signal than an
   edition search would add; the wider question of whether Berger de Xivrey's *Recueil des lettres missives
   de Henri IV* prints letters from Dupuy 63 by number is left open for whoever next needs the plaintext
   itself (Xivrey's index by correspondent would resolve it quickly, not checked this pass).
3. **DECODE.** Cached catalogue (`ay/catalogue/decode-catalog.csv`) grepped for "Dupuy63"/"Dupuy_63"/"Dupuy
   63": no record. `ay/catalogue/` does not cover this manuscript.
4. **Bourdeau.** `cs-recheck/CATALOGUE.md`, `SOLVED_CATALOGUE.md`, `TARGETS.md` grepped for "Dupuy 63"/
   "Seguier"/"Villiers": no hit (item 191/192 nearby in his catalogue concern different Baluze volumes, not
   Dupuy 63). Consistent with the item being outside his working list because it is already solved and
   published by Tomokiyo.
5. **Aymeloglu.** `ay/*.md` grepped for the same terms: no hit.
6. **Web.** WebSearch for `"Baluze 188" OR "Dupuy 63" chiffre dechiffrement cryptanalysis`: no results
   connecting either shelfmark to cryptanalysis discussion outside the sources above (expected — Tomokiyo's
   own site, already checked directly, is the primary record).

**Image not captured.** Tried to locate and view Gallica image f.139 as the brief asked. The manuscript has
518 IIIF canvases (all labelled "NP", no folio numbers in the manifest) for pieces numbered up to at least
245 in the catalogue description, so piece numbers and Gallica image indices are not on a fixed offset.
Calibrated one point directly: piece "65" (Daffis, Bordeaux, 20 July 1598 — confirmed by reading the image's
own date and signature) sits at Gallica image f142; extrapolating the volume's average ~2.1 images-per-piece
to piece 139 predicted image f298-300, but the image actually at f298 is a faded, largely illegible secretary
hand with no name or date matching Seguier/Venice/30 Jan 1601 legible in it, so the guess did not land.
Stopped there rather than keep guessing blind (4 more IIIF requests beyond the calibration point would have
been needed for another attempt) — the found-solved verdict does not depend on it, since it rests on the
catalogue description plus Tomokiyo's independent match, not on a fresh transcription.

Requests: gallica.bnf.fr 5 (1 OAI record, 1 IIIF manifest, 3 IIIF image fetches for the failed calibration
attempt). WebSearch: 1 query.

## Edition risk

**Realized.** Item 139 is not merely "possibly printed somewhere" — it already has a published, named
reconstruction of its cipher (Tomokiyo, `henryiv.htm`, section "Antoine Seguier, sieur de Villiers"), keyed
specifically to this letter (sender, place, date and Gallica/BnF item number all match). The Berger de Xivrey
edition route named in the brief was not needed to reach this verdict and was not pursued.

## Verdict

**Found-solved — not a cryptanalysis target.** Not "new"; not "unpublished" (rule 10): a named solver has
already reconstructed the cipher used in this exact letter and published it. Whether Tomokiyo's key reads
the letter to completion (a token-level grade) is not established here — his page gives the reconstructed
alphabet/nomenclature image, not a stated plaintext — but that is a narrower verification question for
whoever wants Dupuy 63/139's plaintext specifically, not grounds to run fresh cryptanalysis on an
already-keyed cipher.

## Next

Drop N5 from the board. If the plaintext itself (not just the key) is wanted, the shortest route is
fetching Tomokiyo's `henryiv_seguier1601.png` and applying it to a transcription of Gallica image ~f296-300
(recalibrate from piece 137, which per the catalogue is only 2 items earlier and about 4 images before
piece 139 on this volume's average spacing) — a transcription task, not a cryptanalytic one.
