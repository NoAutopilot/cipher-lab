# BnF fr.4687 — Marguerite Paléologue, duchesse de Mantoue, to Louis de Gonzague, duc de Nevers, 1562-1564

Status: open

Check-solved pass, 24 September 2026 (Sonnet, orchestrator brief for M13-M16). Editions-first + one-leaf pass;
a formal six-source check-solved run is still owed before board promotion.

## Correction to the queue row

QUEUE.md M14 dated the item "(undated, volume covers 1585-91 Nevers-Gonzaga affairs)". Gallica's own catalogue
description (via `services/OAIRecord`) dates items 1-3 precisely:

> Recueil de pièces originales et de copies concernant l'histoire de la maison de Nevers. De 1562 à 1625...
> 1-3 Lettres, en italien, avec chiffres, de MARGUERITE PALEOLOGUE, duchesse DE MANTOUE, au duc de Nevers, Louis
> de Gonzague, son fils. De 1562 à 1564.

Margherita Paleologa (1510-1566) was regent-mother of Mantua during this period; her son Louis/Ludovico de
Gonzague later became Duke of Nevers in France. **1562-1564, not 1585-91.** QUEUE.md M14 row updated accordingly.

The same volume's item 41 is listed separately as "Chiffre. Quelques lignes non chiffrées sont en italien" —
an undated ciphered item elsewhere in the recueil, possibly unrelated to items 1-3 (different sender/date), not
investigated this pass.

## Checked (24 Sept 2026)

- Fresh shallow clone of `dbourdeau/cyphersolver`: no hit on "4687", "Paleologue/Paléologue" or "Marguerite" tied
  to this volume.
- Fresh shallow clone of `aaymeloglu/unsolved-ciphers`: no hit.
- `sources/cryptiana/web/nevers.htm` (Tomokiyo's own catalogue of ciphers in BnF fr.3995, "the Nevers
  collection") read locally, no fetch needed: covers a *different* volume — the Duke of Nevers' own cipher
  keys and correspondence as ambassador/courtier (fr.3995, fr.3251, fr.3413, etc.) — not his mother's 1562-64
  letters to him. No hit on "4687", "Paleologue" or "Marguerite" in the full 1420-line mirror.
- WebSearch for Italian scholarship on Margherita Paleologa's correspondence with her son in this period found
  only general biographical material (Wikipedia, Treccani); no edition or article naming this specific
  correspondence or its cipher was located. Tomokiyo's own background bibliography for the Nevers material
  (Daniela Ferrari 1999, "Mantoue et les Gonzague de Nevers"; Ariane Boltanski 2006, *Les ducs de Nevers et
  l'État royal*) was not checked against this specific volume this pass — flagged as the next step, not chased
  further under the check-solved brief's scope.
- Gallica IIIF, canvas 5 (f.1, faint, mostly illegible clear Italian), canvas 7 (f.5, clear Italian salutation
  "Al Ill.mo... figlio caris[si]mo"), canvas 8 (f.6, **ciphertext confirmed**: dense two-digit numeral groups,
  roughly 15-25 groups per line across at least six lines on this one leaf alone — a high-resolution crop is at
  `images/f8_crop.jpg`). Short Italian phrases appear in the left margin beside each ciphered line (e.g.
  "questa una quan[to] a quello che...", "et como...", "vi sera che... seguira..."); these read as the clerk's
  catch-phrase cues for filing/reference, not a complete parallel plaintext — no full interlinear decipherment
  was seen on this leaf. Images: `images/f5.jpg`, `images/f7.jpg`, `images/f8.jpg`, `images/f8_crop.jpg`.

## Verdict

Open at stage 2. Genuine cryptanalysis candidate: ciphertext confirmed on the primary image, no published key
found anywhere searched, no sibling decipherment located, not touched by either solver repository. Matches
QUEUE's original "cryptanalysis" kind; date corrected to 1562-1564. No reading attempted, nothing to grade.

Cheapest next step: chase the Ferrari 1999 and Boltanski 2006 literature (both already in Tomokiyo's own
Nevers-background bibliography, so likely accessible) for any prior discussion of this correspondence's content
or cipher before committing a solver run; and view the rest of items 1-3 (canvases roughly 5-15) to get a full
sign-type inventory and token count across all three letters, not just the one sampled leaf.

## Sources

- Gallica: `https://gallica.bnf.fr/ark:/12148/btv1b90075058`, OAI record via
  `https://gallica.bnf.fr/services/OAIRecord?ark=btv1b90075058`.
- `sources/cryptiana/web/nevers.htm` (S. Tomokiyo, "Ciphers in BnF fr.3995 (the Nevers collection)"), local
  mirror, no fetch.
- github.com/dbourdeau/cyphersolver, github.com/aaymeloglu/unsolved-ciphers (both checked, no relevant content;
  Aymeloglu has no licence, cite only, nothing copied).

## Requests this pass

gallica.bnf.fr: 1 OAI record + 4 IIIF image fetches (1 crop). github.com: 2 shallow clones (shared with M13,
deleted after grep). WebSearch: 1 query.
