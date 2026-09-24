open

# Loménie de Brienne to the Queen of Poland, BnF Clairambault 1067, 19 May 1646

QUEUE row: M18 (sources/solver-diffs — "Third pass, 24 September 2026 (M17-M21)" section of QUEUE.md).

## Source

BnF, Departement des Manuscrits, **Clairambault 1067**, part of the composite "Clairambault 1058-1110,
Mélanges généalogiques et historiques, classés par ordre alphabétique des noms de familles et de matières"
series (finding aid `archivesetmanuscrits.bnf.fr/ark:/12148/cc137820/FRBNFEAD000013782_info`, fetched this
sweep). Gallica digitisation: `ark:/12148/btv1b9000856f` (422 canvases; QUEUE also names `btv1b90008551` as a
second, unconfirmed digitisation of the same volume, not checked this pass). This individual volume is
catalogued "X BRUN (DE)-BUX (DU)" — confirmed by the finding aid: the item immediately before and after the
Brienne entry are "Bournonville" (Fol. 223) and "Bourc de Geoli" (Fol. 225)/"Bouvery" (Fol. 230), all B-names.

**Precise catalogue entry, from the finding aid's own item list (not just the OAI summary QUEUE quoted):**
"**Fol. 226** • Lettre avec chiffres adressée par de Brienne à la reine de Pologne (19 mai 1646)." A short,
single-item entry (the next item starts at Fol. 230), so probably a 1-4 folio letter.

## Check-solved sweep (24 September 2026)

1. **Web search.** "Loménie de Brienne lettre reine de Pologne Marie-Louise de Gonzague 1646 correspondance" and
   "'Marie-Louise de Gonzague' correspondance France 1646 Brienne édition lettres". Surfaced: Marie-Louise de
   Gonzague (Queen of Poland from her March 1646 proxy marriage) corresponded with Mazarin in cipher after
   arriving in Warsaw (fr.wikisource.org, "Un Mariage politique au XVIIe siècle — Marie de Gonzague à Varsovie":
   *"En quittant Paris, elle avait emporté un chiffre qui lui permettait de correspondre avec Mazarin en toute
   sécurité"* and a later "letter half in ciphers, half in clear" to Mazarin on arrival) — general context for
   why a Secretary-of-State letter to her might be ciphered, not a hit on this specific 19 May 1646 letter. That
   Wikisource article was fetched directly and checked for a 19 May 1646 date or any Brienne letter: **none
   found** (its cipher discussion is all Queen-to-Mazarin, not Brienne-to-Queen). Also surfaced *Lettres inédites
   à Marie-Louise de Gonzague... sur la cour de Louis XIV (1660-1667)* (Magne ed., 1920) — wrong decade (1646
   vs. 1660s), not the same letter. No dedicated printed edition of Brienne's own outgoing letters to the Queen
   located.

2. **Print/scholarship.** Tomokiyo's `louisxiv0.htm` (local mirror, already flagged as a same-office lead by the
   QUEUE row) gives two Brienne ciphers, both to a **different correspondent** (Comte d'Estrades, the
   Netherlands ambassador) and **later dates**: "Brienne's Cipher 1" (p.501, letter of 28 June 1647, also used
   19 Sept 1647) and "Brienne's Cipher 2" (p.45/163, letters of 28 April and 20 September 1651). Neither is
   dated 1646 and neither is addressed to the Queen of Poland. This is a plausible same-office design lead (the
   Secretary of State's bureau likely reused cipher designs across correspondents in a similar period) but **not
   a match, not tried as a key this pass** — flagged for a solver, not applied here.

3. **Community lists.** `sources/cryptiana/` grepped for "clairambault 1067", "brienne.*pologne", "pologne.*
   brienne", "gonzague": no hit beyond `louisxiv0.htm`'s unrelated D'Estrades ciphers above.

4. **DECODE.** `unsolved-ciphers/catalogue/decode-catalog.csv` grepped for "Clairambault 1067", "clair1067",
   "Brienne.*Pologne", "Pologne.*Brienne", "Gonzague": no row.

5. **Bourdeau.** Fresh shallow clone grepped for the ark (`btv1b9000856f`/`btv1b90008551`, 0 hits) and bounded
   "Clairambault 1067" (0 hits). The repo's only Brienne item is unrelated: "Bordeaux → Brienne" (Brienne as
   *recipient* at London, 30 May 1653, BL Add MS 4200, solved 18 Sept 2026 with the English Deciphering Branch's
   own key sheet) — a different direction (someone writing *to* Brienne, not Brienne writing out), a different
   archive (BL not BnF), a different year, no overlap.

6. **Aymeloglu.** Fresh shallow clone; catalogue and target folders grepped for "1067", "brienne", "pologne",
   "gonzague": no hit.

Requests: gallica.bnf.fr 5 (1 IIIF manifest, 1 Pagination service call [422/422 pages "NP", confirms this
manuscript carries no Gallica-indexed foliation, same finding as clairambault361-marini-1610's precedent], 1
ContentSearch call [0 hits for "Pologne", confirms no OCR index either], 2 native-image probe fetches at
naively-offset canvas guesses [f246, f232] — both landed on unrelated **later, printed** material bound into
the same composite volume (an 18th-c. judicial "Arrêt"/factum text mentioning dates 1701-1702, folio stamps
"117"/"45" and "110"/"32" respectively, neither matching the target period), matching the clairambault361
precedent that naive folio=canvas guesses fail on these composite Clairambault volumes), archivesetmanuscrits.
bnf.fr 1 (the finding-aid info page, HTTP 200 after a 302 redirect handled with `-L`), WebSearch 2, WebFetch 1.

## What the leaf shows

**Not located by image this sweep.** Two calibration probes, both wrong (see above); a third/fourth attempt
was not made this pass to stay within a reasonable request budget for one target, given the good-citizen
1.5s-apart /≈40-total-request ceiling shared across all three M17-M19 targets and that M19's leaf (below) still
needed fetching. The manuscript is not paginated or OCR'd in Gallica's own services, so folio 226 cannot be
reached without either a better calibration point (a labelled facing page, a known sibling item's confirmed
canvas) or a further, more patient probing pass — left as the next concrete step for whoever picks this target
up next.

## Verdict

**Open.** No published plaintext, decipherment, or key lead specific to this letter found in six sources. The
Tomokiyo same-office cipher designs (1647, 1651, different correspondent) are a real but unconfirmed lead, not
a match — a solver should try Brienne's Cipher 1/2 against this letter's ciphertext once an image is obtained,
before any cryptanalysis from scratch. **Leaf not viewed** — the single open item before this target can go to
stage 2 with confidence on the image side; the finding-aid text itself (precise folio, single short item,
correct alphabetical neighbours) is solid.

Not touched: no key application, no decoding, no novelty wording.
