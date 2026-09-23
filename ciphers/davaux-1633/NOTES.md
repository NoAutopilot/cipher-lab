found-solved

# Comte d'Avaux to Cardinal Antonio Barberini, Paris, 25 November 1633 — BnF Baluze 188

QUEUE row: N4 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

BnF, Departement des Manuscrits, **Baluze 188** ("Melanges se rapportant principalement a l'histoire
d'ITALIE"), Gallica `ark:/12148/btv1b90014586`. Gallica OAI/Dublin Core record (`dc:description`, fetched
24 September 2026, 1 request) gives the volume's full contents list. Two separate items in the same
miscellany matter here, quoted verbatim:

> "**Lettre du comte d'Avaux au cardinal Antonio [Barberini] (Paris, 25 novembre 1633)** ; Lettre non
> signee ... (Bologne, 2 novembre 1637) ; Lettre de Louis de Vendome au meme (24 mai 1633) ; ... ;
> **Lettre chiffree avec dechiffrement partiel (18 mai 1632)** ; Sentence prononcee sur divers
> cardinaux ..."

The QUEUE N4 row's "What the catalogue says" cell quoted only the second item ("Lettre chiffree avec
dechiffrement partiel (18 mai 1632)") but attached its year and the cipher/partial-decipherment claim to
the *first* item, the d'Avaux-Barberini letter of 25 November 1633 — these are two different, unrelated
items bound in the same recueil. This is a scout conflation, not a fact about the d'Avaux letter.

## Check-solved sweep (24 September 2026)

1. **Image (decisive).** Fetched the Gallica IIIF manifest once (`manifest.json`, 1 request; 198 canvases,
   all labelled "NP" — no folio numbers given in the manifest) and viewed nine leaves at reduced width
   (~700 px) to locate and read the d'Avaux letter: Gallica images f2 (cover), f3 (marbled endpaper), f4/
   f5/f6 (blank flyleaves), f8/f9 (the volume's first item, a Latin inscription transcription — "Inscriptio
   Divi Aug Pontifici Maximo... Forma dell'Inscrittione che si dice essere stata ne' Trofei d'Augusto
   sull'Alpi", matching the catalogue's first list item), **f10-f11 (the d'Avaux letter itself)**. f10-f11
   are two full pages of plain, fluent Italian secretary hand — a courteous thank-you note ("Con quel
   respetto che e proprio di chi riceve inaspettati fauori io vengo con questa a rendere infinite gratie a
   Vra Eminenza dell'humanissima [lettera] che... si e compiaciuta scrivermi sotto gli 17 del passato...")
   closing "Di V.ra Em.za Devotmo et Obligmo Servre D'AVAUX", dated "di Parigi alli 25. Novembre 1633", with
   the contemporary docket "al Sig.re Card.le Antonio [Barberini]" in the corner. **There is no cipher
   anywhere on either page** — no numerals, no symbol alphabet, no interlinear decipherment. Images saved
   to `images/` (`btv1b90014586_p10_davaux.jpg`, `btv1b90014586_p11_davaux_signature.jpg`,
   `images/manifest.json`). A spot check of f22-f23 (guessed to be near the "18 mai 1632" item; it was not —
   f22-23 reads as the end of the Bologna, 2 November 1637 letter instead, confirming items in this
   miscellany are not evenly spaced in image order) was not pursued further; the identification of the
   "18 mai 1632" item rests on Tomokiyo's own citation and image (below), not a fresh image here.
2. **Print / scholarship.** The d'Avaux-Barberini correspondence of the 1630s is in print in the standard
   editions of the papal nunciature and d'Avaux's own letters (not searched page-by-page this sweep, since
   the letter is not in cipher and so carries no recovery/cryptanalysis value regardless of print status).
3. **Community lists.** Satoshi Tomokiyo's own site (mirrored in `cs-recheck/gallica_siblings/src/
   louisxiii.htm`, section "Italian Cipher (1632)") independently identifies the *other* item in this same
   volume: "BnF Baluze 188, f.22, is a letter in Italian partly in cipher (18 May 1632)" — matching the
   Gallica catalogue's date and description exactly — and gives a reconstructed nomenclature (`h14 (altr),
   h20 (algun), h40 (ben), h51 (cred), r13 (fare), r35 (grand), r48 (havere), r66 (Cardinal Richelieu), p61
   (francia), q14 (lettre), x57 (piu), x66 (quest), u16 (Re), u41 (Roma), u49 (spagli), y29 (stato), y44
   (suo), y62 (voglio), y77 (volte)`), with an image (`BnFbaluze188f22.png`, not cached locally). This is an
   anonymous letter, unconnected to d'Avaux by name in either the catalogue or Tomokiyo's page.
4. **DECODE.** The cached catalogue (`ay/catalogue/decode-catalog.csv`, grepped for "Baluze188") has one
   record for this volume: id 2768, "Baluze 188, f.22-23", 1632, "Italy Verona", Italian, status
   **Decrypted**, 5 pages. This matches Tomokiyo's "f.22" item (date, folio, language) exactly — a third,
   independent source converging on the same already-solved anonymous cipher letter. No DECODE record
   exists for the d'Avaux-Barberini letter of 25 Nov 1633 (grepped "avaux": one unrelated hit, a 1684
   letter of a different, later Comte d'Avaux, Jean-Antoine de Mesmes).
5. **Bourdeau.** `cs-recheck/CATALOGUE.md` and `SOLVED_CATALOGUE.md` grepped for "Baluze 188": no entry
   (consistent with the item already being solved/published by Tomokiyo and so outside his working list).
6. **Aymeloglu.** `ay/*.md` grepped for "Baluze 188"/"avaux"/"barberini": no hit.

Requests: gallica.bnf.fr 15 (1 OAI record, 1 IIIF manifest, 1 archivesetmanuscrits.bnf.fr notice page — JS-
rendered, no usable content extracted client-side, and 12 IIIF image fetches at reduced width; 2 connection
resets on the first two image requests, each retried once successfully per the good-citizen rule).
WebSearch: 1 query (no results connecting Baluze 188/Dupuy 63 to cryptanalysis, expected — this is
manuscript-catalogue material, not previously blogged).

## Edition risk

**Moot for the named target.** The letter QUEUE N4 named (d'Avaux to Barberini, 25 Nov 1633) is not in
cipher at all, so there is no cipher to check against an edition. The volume's actual ciphered item (18 May
1632, anonymous) is realized: already keyed by Tomokiyo and already marked Decrypted on DECODE.

## Verdict

**Found-solved / not a valid cryptanalysis target as named.** Two findings, both against rule 10 wording:
(a) the d'Avaux-Barberini letter of 25 November 1633 is a plain Italian courtesy letter, confirmed by direct
image inspection of both its pages — it was never in cipher, so QUEUE N4's premise is a conflation of two
different items in the same bound miscellany; (b) the volume's one genuinely ciphered item ("Lettre chiffree
avec dechiffrement partiel", 18 May 1632, unsigned) is already read: Tomokiyo has published a reconstructed
nomenclature for it, and DECODE independently lists it as Decrypted (record 2768). Neither item is a target
for this project. Not "new"; not "unpublished" — the ciphered item has a published key and a Decrypted
catalogue status.

## Next

Drop N4 from the board entirely; nothing here needs an access route, a copy order or further cryptanalysis.
If anyone wants to sanity-check DECODE record 2768 against Tomokiyo's nomenclature (a Bourdeau/Aymeloglu-
style verification of an already-claimed solve), that is a much smaller, separate task and not this
project's lane per README "What counts as a result".
