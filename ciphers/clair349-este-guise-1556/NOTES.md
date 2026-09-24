partial

# Cardinal Hippolyte d'Este (cardinal de Ferrare) and the duc de Guise, ciphered originals, BnF Clairambault 349

QUEUE row: M17 (sources/solver-diffs — "Third pass, 24 September 2026 (M17-M21)" section of QUEUE.md).

## Source

BnF, Departement des Manuscrits, **Clairambault 349**, Gallica `ark:/12148/btv1b9000668z`. Catalogue note (per
the QUEUE row, matching BnF's own archivesetmanuscrits description): "Lettres orig. du cardinal de Ferrare
[Hippolyte d'Este], au duc de Guise et réponse (novembre-décembre 1556, janvier et février 1557), avec
chiffres." Part of the Bossuet-Béthune-Brienne copy series within Clairambault, but this item is explicitly
catalogued as **originals**, not the 18th-c. Bossuet copies.

## Check-solved sweep (24 September 2026)

**Finding that overrides the "open"/cryptanalysis framing (rule 10, M9 lesson): Tomokiyo's `guise.htm` already
identifies this exact letter and publishes the key.**

1. **Web search.** Several queries ("Clairambault 349" chiffre Guise Ferrare; Ribier Lettres et mémoires d'estat
   cardinal Ferrare duc de Guise 1556 1557 déchiffré; "cardinal de Ferrare" "duc de Guise" lettre chiffrée
   déchiffrement 1556 1557 correspondance). Results only reproduce the BnF catalogue description (Biblissima,
   archivesetmanuscrits, Gallica) and general Guise-family scholarship (Classiques Garnier's "François de
   Lorraine, duc de Guise entre Dieu et le Roi" bibliography page — 403 on WebFetch, not read). No printed
   decipherment located this way.

2. **Print/scholarship — Tomokiyo's `guise.htm` (local mirror `sources/cryptiana/web/guise.htm`), the decisive
   lead.** The page catalogues the keys in BnF fr.20974, "Clefs de la correspondance chiffrée de François, duc
   DE GUISE, avec quelques lettres de lui (1556)" (Gallica `ark:/12148/btv1b9062131g`). Entry **no.15** (fr.20974
   p.57-60, 69-72): "Cipher between Guise and Hippolyte le jeune d'Este, cardinal de Ferrare." Verbatim, directly
   under the key images: *"A letter in this cipher, dated 4 January 1556, is found in BnF Clair 349 (Gallica),
   f.3. It is annotated 'Lettres orig. du cardinal de Ferrare [Hippolyte d'Este], au duc de Guise et reponse
   (novembre-decembre 1556, janvier et fevrier 1557), avec chiffres' in catalogue information. Another is found
   in BnF Clair 348 (Gallica), f.304 ('Lettre d'Hippolyte d'Este, cardinal de Ferrare, au duc de Guise (3 janvier
   1557), avec chiffres.')"* Tomokiyo shows the substitution-alphabet-and-nulls key as an image
   (`guise/BnFfr20974f57.png`, `guise/BnFfr20974f69.png`) and, directly under the paragraph above, a cropped
   photo of the actual ciphertext leaf (`BnFClair349f3.jpg`) bordered to mark it out — i.e. he has already
   located and photographed the very folio this check-solved sweep was sent to find. **The page gives the key
   and points at the letter, but does not print a plaintext/decipherment of it** — no reading follows the image,
   and the page's own "undeciphered ciphertexts" section (`#SEC2`, covering nos. 1, 7 and 8) does not include
   no.15/Clair 349, i.e. Tomokiyo does not call it unsolved either — it is simply not addressed beyond the key
   and the pointer. Page metadata: first posted 18 March 2020, last modified 5 June 2022 — this key has been
   public for over four years without (as far as this sweep found) anyone applying it and publishing the
   reading.

3. **Community lists.** `sources/cryptiana/` grepped in full for "vergier" (M19 term, 0 hits, see below) and
   separately for "349"/"clair 349"/"clairambault 349": only the `guise.htm` passage above. No other Cryptiana
   page or blog post names this shelfmark.

4. **DECODE.** `unsolved-ciphers/catalogue/decode-catalog.csv` (10,107 rows, fresh clone) grepped for
   "Clairambault 349", "clair349", "Hippolyte", "d'Este".guise/"Ferrare".guise combinations: no row for this
   shelfmark (the only Clairambault rows near it are 325, 328, 417, 574, 577, 580 — a different sub-range).

5. **Bourdeau (dbourdeau/cyphersolver).** Fresh shallow clone, grepped for the ark (`btv1b9000668z`, 0 hits) and
   for bounded "Clairambault 349" (0 hits). The repo's own Guise-family solved item, `guise1587/` (catalogue
   172), is a different letter entirely: [Henri, duc de Guise?] to the duc de Mercœur, BnF fr.15564 ff.119/142,
   27 May/20 June 1587 — thirty years later, different correspondent, different shelfmark, read with George
   Lasry's 2022 fr.15564 key. Several "d'Este" hits in `CATALOGUE.md`/`README.md`/`SOLVED_CATALOGUE.md` are all
   Ippolito I / Ercole I / Alfonso I d'Este at the Hungarian legation (Eger/Pozsony, 1482-1521) — the earlier,
   unrelated Ferrara branch, not Hippolyte II d'Este (cardinal de Ferrare from 1550) of this target. No overlap.

6. **Aymeloglu (aaymeloglu/unsolved-ciphers).** Fresh shallow clone. `catalogue/decode-catalog.csv` covered
   above (point 4); repo's own `CATALOGUE.md`/`TARGETS.md`/`SHORTLIST.md` and target folders
   (burgess-1912, ferdinand-1634, ferdinand-1635-1640, forster-1644, moray-1568, ottobon-1589, royalist-1646,
   starhemberg-1758) grepped for "349", "guise", "este", "ferrare": no hit relevant to this item.

Requests: gallica.bnf.fr 6 (1 manifest, recovered on the 3rd attempt after two tunnel-side `ws_closed_mid_exchange`
resets confirmed via `/root/.ccr/README.md`'s documented pattern, not a Gallica block; 1 thumbnail, same
pattern, recovered 3rd attempt), archivesetmanuscrits.bnf.fr 0 for this target (not needed — Tomokiyo's page and
the QUEUE row's own catalogue note already gave the exact folio), WebSearch 3, WebFetch 1 (403, not read),
github.com 2 (both solver repos, shallow clones shared across M17/M18/M19).

## What the leaf shows

Tomokiyo's link resolves to Gallica **canvas f9** for manuscript "f.3" (a +6 image/foliation offset, confirmed
by fetching the same canvas independently rather than trusting the link blindly). Thumbnail fetched:
`images/f9_thumb.jpg`. The spread shows two leaves: the right-hand page is dense ciphertext in short arbitrary
symbol/figure groups, consistent with the no.15 key's design (arbitrary symbols, some figures, per `guise.htm`'s
general note "these ciphers mainly employ arbitrary symbols... Some of the other ciphers (e.g., no.15) also use
figures"); the left-hand page is continuous plain cursive French, likely the reply or a covering/docket leaf.
This confirms the catalogue note: a real, substantial ciphertext letter, not a key-only or foliation false
positive.

## Verdict

**Partial**, not open and not found-solved. No published plaintext/decipherment of this specific letter was
located anywhere this sweep (web, DECODE, both solver repos, Cryptiana beyond the key pointer, and no
Ribier/Guise-scholarship confirmation reached — see below). But the **key is already public** (Tomokiyo,
fr.20974 no.15, 2020/2022) and the **exact matching ciphertext letter is already identified and photographed**
by the same source, down to the folio. Per rule 10 and the M9/Morvillier lesson, this cannot be reported as
"open" without quoting and flagging that. **Kind correction for the orchestrator:** QUEUE.md lists M17 as
`cryptanalysis`; per README's "Result label" convention ("a key that opened it is recovery, a reading without
the key is cryptanalysis"), this is a **recovery** target once solved — a solver only needs to apply Tomokiyo's
already-published key to the already-identified leaf, not break the cipher from scratch. This is now the
single cheapest, highest-confidence target of the three in this batch for a follow-on solver worker: fetch the
fr.20974 key images (`guise/BnFfr20974f57.png`, `f69.png`) and full-resolution Clair 349 f.3 (canvas f9, and
its facing/following canvas for any continuation), transcribe the key table into a `key.tsv`, and apply it.

**Edition check, not fully closed.** Ribier's *Lettres et mémoires d'estat* (1666, IA `bub_gb_bOnmNv2ZLVoC`) full-
text-searched for "cardinal de Ferrare": one hit, page 667, a generic passage ("...aussi bien Monseigneur le
Cardinal de Ferrare, lequel me fait cet honneur de m'en...") that does not read as this letter's decipherment
and whose surrounding date was not confirmed as Nov 1556-Feb 1557 this pass — flagged as **not checked to a
safe negative**, the single biggest remaining edition-risk gap before this can move past stage 2. The duc de
Guise's own *Mémoires-journaux* (Michaud-Poujoulat collection) was not reached this pass (out of budget).

Not touched: no key transcription, no decoding, no novelty wording. This target should go on the board as
**recovery**, ahead of M18/M19 for solver attention.
