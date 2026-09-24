# BnF fr.5160 — Loménie de Brienne (père et fils) to Abel Servien, 1653-1661

Status: open

Check-solved pass, 24 September 2026 (Sonnet, orchestrator brief for M13-M16). Editions-first + one-leaf pass;
a formal six-source check-solved run is still owed before board promotion.

## Correction to the queue row — the ciphered letters are not Le Tellier's

QUEUE.md M16 names this "Michel Le Tellier correspondence... 'en partie chiffrées, et souvent accompagnées du
déchiffrement' — about 47 letters, 10 Jan 1653 - 21 Dec 1661." Gallica's own catalogue description (via
`services/OAIRecord`) attributes the 47 partly-ciphered letters to a **different** correspondent:

> 1 Lettres originales adressées à Abel Servien par HENRI-AUGUSTE « DE LOMENIE », comte de « BRIENNE », et par
> son fils HENRI-LOUIS DE LOMENIE DE « BRIENNE », du 10 janvier 1653 au 21 décembre 1661. Ces lettres, dont
> plusieurs sont en partie chiffrées, et souvent accompagnées du déchiffrement, sont au nombre de 47 ;
> 2 Lettres originales de MICHEL « LE TELLIER », adressées au même, entre le 22 mars 1652 et le 27 août 1658...

Item 1 (the 47 ciphered letters, with contemporary decipherment) is Brienne père-et-fils to Servien. Item 2
(Le Tellier's own letters to Servien, a smaller, separately-dated set) carries **no** cipher note in the
catalogue description at all. The QUEUE row's title and the scout's "kind" (recovery, decipherment often
present) both describe item 1 correctly in substance, but mis-name the sender. Renamed correctly in this note;
QUEUE.md M16 row updated. The folder slug (`fr5160-letellier-1653`) is kept as filed by the scout to avoid a
second rename mid-pipeline, but should be corrected to something like `fr5160-brienne-servien-1653` if this is
promoted.

## Checked (24 Sept 2026)

- Fresh shallow clone of `dbourdeau/cyphersolver`: `letellier/NOTES.md` covers a **different, unrelated** item —
  "Le Tellier → Marquis de Castelnau, 12 May 1657", cryptiana transcription `LeTellier_Castelnau1657.txt`, a
  distinct cipher family ("Le Tellier-Colbert Cipher 2", tried and set aside as unsolved/skipped, too short).
  No shelfmark given in that note beyond the cryptiana transcription filename; not established whether it is
  from fr.5160 or elsewhere in the Le Tellier papers (BnF fr.4187 or SHD A1, per Bourdeau's own suggestion in
  that note). Worth checking as a possible same-key sibling once fr.5160's actual cipher is transcribed, not
  pursued this pass. No other hit on "5160", "Brienne" or "Servien" tied to this volume.
- Fresh shallow clone of `aaymeloglu/unsolved-ciphers`: no hit.
- `sources/cryptiana/web/louisxiv0.htm` (43 "Le Tellier" hits, local mirror, no fetch) is about the Louvois/Le
  Tellier war-ministry cipher family in general; not checked line-by-line against fr.5160's 47 letters this
  pass — flagged as the next step, since it is already on disk.
- Editions: "Caron 1898" (as named in the orchestrator brief) could not be identified as a specific, real
  edition of this correspondence — WebSearch surfaced only N.-L. Caron's 1881 *Michel Le Tellier, son
  administration comme intendant d'armée en Piémont, 1640-1643* (a different, earlier period of Le Tellier's
  career, and by a different given-name initial) and Pierre Caron (1875-1952), an unrelated archivist. *
  Correspondance administrative sous le règne de Louis XIV*, ed. G.B. Depping (Imprimerie nationale, 1850-1855,
  4 vols, digitised on Gallica) is real and covers Louis XIV's administrative correspondence, organised by
  subject (provincial estates; justice/police/galleys; public works/religious affairs/sciences) rather than by
  correspondent pair; whether it includes any Brienne-Servien 1653-61 letters was **not established** this
  pass — a volume-by-volume index check is the next step, not a network fetch.
- Gallica IIIF, one leaf plus two extra probes (367-canvas volume): canvas 20 = folio 7, a clear French letter
  about the 1653 siege of Bordeaux, no cipher (`images/f20.jpg`). Canvas 100 = faint, largely illegible verso
  show-through, no cipher visible (`images/f100.jpg`). Canvas 150 = blank verso (`images/f150.jpg`). **No
  ciphertext passage was located in this three-leaf sample** of 367 canvases for 47 letters — expected, since
  the ciphered passages are a minority within each letter and scattered through the volume; not a negative
  finding on the catalogue's own claim.

## Verdict

Open at stage 2. The catalogue's own claim (47 letters, several partly ciphered, often with contemporary
decipherment already in the volume) was not contradicted, but also not directly confirmed on an image this
pass — a genuine gap, flagged rather than assumed. Kind: recovery (decipherment often present), as scored,
**for Brienne père-et-fils, not Le Tellier**. No reading attempted, nothing to grade.

Cheapest next step: use archivesetmanuscrits.bnf.fr's item-level listing (if it enumerates the 47 letters
individually, as it did for fr.4687) to get folio numbers for the ciphered ones directly, instead of paging the
367-canvas manifest blind; then view two or three of those specific leaves to confirm the "often accompanied by
decipherment" claim and separate the letters that already carry one from the ones that do not.

## Sources

- Gallica: `https://gallica.bnf.fr/ark:/12148/btv1b9060495t`, OAI record via
  `https://gallica.bnf.fr/services/OAIRecord?ark=btv1b9060495t`.
- `sources/cryptiana/web/louisxiv0.htm` (S. Tomokiyo), local mirror, not yet read against this target.
- github.com/dbourdeau/cyphersolver `letellier/NOTES.md` (a different item, cite only, code MIT / text CC BY
  4.0, nothing copied); github.com/aaymeloglu/unsolved-ciphers (checked, no relevant content).

## Requests this pass

gallica.bnf.fr: 1 OAI record + 1 manifest + 3 IIIF image fetches. github.com: 2 shallow clones (shared with
M13-M15, deleted after grep). WebSearch: 2 queries.
