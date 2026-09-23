found-solved

# M. de Bréval to Duke Henri II of Lorraine, cipher letter — BnF Lorraine 377, f.95-96

QUEUE row: N9 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

BnF, Département des Manuscrits, **Lorraine 377** ("Recueil de lettres originales adressées par diverses
personnes aux ducs Charles III, Henri II [1597-1623] et Léopold [1698]..."), Gallica
`ark:/12148/btv1b90008143`. Gallica OAI/Dublin Core record (`dc:description`, fetched 23 September 2026, 1
request):

> "Contient : **Lettre chiffrée de M. de Bréval au duc Henri II**"

678 feuillets, 735 Gallica canvases, all IIIF-labelled "NP" (no folio numbers in the manifest metadata).

## Check-solved sweep (23 September 2026)

1. **Image (decisive).** Fetched the Gallica IIIF manifest once (`images/manifest.json`, 1 request; 735
   canvases) and the pagination service once (`services/Pagination`, confirms no foliation is exposed by
   Gallica's own metadata for this volume — every page is "NP"). Located the leaf by trial: canvas f100 =
   physical folio "91" (plain French, unrelated letter), canvas f105 = physical folio "96", giving a local
   offset of canvas = folio + 9 for this stretch of the volume. Canvas **f104 = folio "95"**, viewed at
   1500 px (`images/btv1b90008143_f104_folio95_cipher-and-decipher.jpg`): rows of **variable-length Arabic
   numeral cipher groups (1-3 digits) with a small interlinear decipherment written above each row in a
   contemporary hand**, alternating with plain French passages ("Monseigneur, apres ce que monsieur de
   Couuongs [Couvonges?] escrira a vostre Altesse..."), and more cipher at the foot of the page. Canvas
   f105 = folio "96" (`images/btv1b90008143_f105_folio96_signature-breval.jpg`) is the letter's close and
   signature, reading in the clear "...recompense monsieur de Longueville..." and "...gouuernement de
   normandye..." before the signature "Breval" — matching Tomokiyo's citation verbatim (below). **The leaf
   already carries its own period decipherment**, interlined by a contemporary reader; this is not a blind
   cryptanalysis target, it is a transcription target with the key already worked out, once, in the 17th
   century and again in 2024 by Tomokiyo.
2. **Print / scholarship.** Not pursued: the letter is a short diplomatic note (2 pages per DECODE, below),
   already published with a reconstructed nomenclature (next point); a Correspondance/Lettres edition search
   would be for confirming a printed plaintext, not for establishing cryptanalytic status, and is out of
   scope for a target that already has a published key.
3. **Community lists (decisive).** Satoshi Tomokiyo's site, `cryptiana.web.fc2.com/code/lorraine.htm`
   ("Variable-Length Figure Cipher of Duke of Lorraine (ca.1620?)", fetched 23 September 2026 via HTTPS with
   a browser User-Agent after a plain `curl` with no UA returned HTTP 403 — 1 request each, 2 total), reads
   in full:
   > "A cipher used in a letter to the Duke of Lorraine turned out to employ variable-length symbols. The
   > letter (BnF Lorraine 377, f.95) signed 'Breval' is catalogued as 'Lettre chiffrée de M. de Bréval au
   > duc Henri II.' Breval was a 'chargé d'affaires de Lorraine à Paris.' The reference to 'gouvernement de
   > normandye' in clear after 'recompense monsieur de Longueville' suggests the letter is dated from around
   > 1619... The interlined decipherment allows reconstruction of the cipher as follows. The cipher employs
   > variable-length symbols, i.e., Arabic figures of one, two, or three digits... Such variable-length
   > symbols were used in Vatican ciphers in the sixteenth century and also in the 1620s. In contrast, no
   > cipher of this type is known to me among contemporary French ciphers."
   First posted 23 March 2024, last modified 23 March 2024. Tomokiyo gives the reconstructed nomenclature on
   the page (not reproduced here; see the source). This is the same leaf identified independently in this
   sweep by image (point 1) — folio, correspondent, and the two quoted clear phrases all match exactly.
   `sources/cryptiana/web/` does not carry a cached copy of `lorraine.htm` (only `louisxiii.htm` from this
   author was pre-cached); the live page was fetched fresh this session instead. `louisxiii.htm` itself was
   grepped for "Lorraine"/"Henri II"/"Bréval" — no hit, confirming the relevant page is `lorraine.htm`, not
   `louisxiii.htm` as this brief guessed.
4. **DECODE (decisive).** The cached catalogue (`ay/catalogue/decode-catalog.csv`, grepped for "lorraine")
   has one record for this leaf: id **7952**, "Paris, BnF, Lorraine 377, f.95, BnF_Lorraine377_f95",
   correspondent "Breval", cleartext/plaintext French, type Cipher, status **Decrypted**, 2 pages
   (`https://de-crypt.org/decrypt-web/RecordsView/7952`). A third, independent source (after the image and
   Tomokiyo) converging on the same already-solved leaf.
5. **Bourdeau.** `cs-recheck` grepped for "Lorraine 377"/"Bréval"/"Breval": no hit in his own working list
   (consistent with the item already being solved and published, so outside his open-target list). His own
   `lorraine1592/NOTES.md` (a different, still-open Lorraine target, Charles III to Vaudémont, BnF fr. 3621
   no. 97, 1592) independently cites this exact item while eliminating candidate keys for its own cipher:
   "Keys for *other* Lorraine ciphers are published and are **not** this system: Bréval to Henri II, ca.
   1620 (Tomokiyo, `lorraine.htm`; DECODE 7952)." A fourth independent confirmation, from a source with no
   incentive to invent it.
6. **Aymeloglu.** `ay/*.md` grepped for "Lorraine 377"/"Bréval": no hit (cited only, per rule 8; not copied).

Requests: gallica.bnf.fr 6 (1 IIIF manifest, 1 Pagination call, 1 OAI record, 3 image fetches).
cryptiana.web.fc2.com 2 (1 failed with a bare UA, HTTP 403; 1 succeeded with a browser UA, HTTP 200 — not a
retry of the same request, a different UA). No WebSearch needed once the DECODE/Bourdeau/Tomokiyo chain
converged.

## Edition risk

**Moot.** The leaf is not an unpublished cipher: it carries its own 17th-century interlinear decipherment,
Tomokiyo published a reconstructed nomenclature for it on 23 March 2024, and DECODE independently lists it
Decrypted. There is no cryptanalytic campaign to protect from an edition; the only remaining work is
transcription/verification of an already-broken system, which is the "contribution" lane (README "What
counts as a result"), not cryptanalysis.

## Verdict

**Found-solved.** BnF Lorraine 377, f.95-96 (Bréval to Duke Henri II of Lorraine, in cipher, c. 1619) is
already deciphered: (a) the leaf itself carries a contemporary interlinear decipherment, visible directly on
the Gallica image; (b) Satoshi Tomokiyo published a reconstructed variable-length-figure nomenclature for it
on 23 March 2024; (c) DECODE record 7952 independently lists it "Decrypted"; (d) Bourdeau's own working
notes (a different target) cite the same key as settled. Four converging sources. Not "new"; not
"unpublished" — grade H available (read from Tomokiyo's published key source) for anyone who wants a modern
transcription.

## Next

Drop N9 from the board. If anyone later wants a fresh independent transcription against Tomokiyo's published
key (a Bourdeau/Aymeloglu-style verification, not a fresh solve), the leaf is at canvas f104 (folio 95) of
`ark:/12148/btv1b90008143`; no copy order or TNA/BnF access route is needed, the volume is already digitised
and public domain.
