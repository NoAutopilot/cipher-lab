# BnF Français 2996, f.53: ciphered despatch of Morvillier at Venice to the king

open

Check-solved sweep, 23 September 2026 (~23:41 UTC; `date -u` read before writing). QUEUE row M9. Worker:
check-solved M8-M11 (Sonnet, cap $8 across all four targets).

## Correction to the QUEUE description

QUEUE M9 dated this "mid-16th c." The BnF finding aid and the leaf itself both fix it precisely: **Venice, 24
January 1546**, from Jean de Morvillier (Wikipedia: French ambassador to Venice from October 1546, so this
letter is from just before or in the very first weeks of that posting -- worth the verifier double-checking the
year reading, "1546", against his appointment date).

## What the BnF finding aid and Gallica leaf show

BnF finding aid (`archivesetmanuscrits.bnf.fr/ark:/12148/cc49450h`, fetched 23 Sept 2026): "Fol. 53 - 25 Depeche
en chiffre de DE MORVILLIER... au roy... De Venize, le XXIIIIe jour de janvier 1546."

Leaf viewed via Gallica IIIF (`images/f53_item25.jpg`, canvas f101; this manuscript photographs one page per
canvas, not a spread, so the canvas-to-folio ratio is roughly 2:1, unlike fr.2980's near-1:1 spread
convention -- three probes were needed, see `images/manifest.json`). The pencil folio number visible top-left
on this canvas reads "55", not "53"; the content match (see below) is exact, so this is either a second,
independent foliation layer on the same leaf or a one-off transcription slip in the finding aid -- flagged, not
resolved.

**Content match confirmed by eye, word for word against the finding-aid heading:** the leaf is mostly plain
French -- diplomatic news of Ottoman naval preparations, "le grand seigneur" (the Sultan), a "grand galleon...
a barbe rousse", named Venetian figures, promises to keep the Signoria informed -- then, near the foot of the
page, **roughly 6 lines of dense mixed numeral/letter/symbol cipher** (on the order of 80-120 tokens by rough
count), then the closing "Un tres humble et tres obeissant subject et serviteur, De Morvillier", dated "ce
XXIIII[e] jour de Janvier 1546". No interlinear or marginal decipherment sits over the cipher lines themselves.

**A separate, unresolved pencil marginal note** sits in the left margin roughly level with the cipher block
(`images/f53_margin_note_crop.jpg`, an IIIF region crop at native resolution). It reads approximately "ce
qu[i]... dechiffre" -- legible as far as "dechiffre" (deciphered / to decipher), the word(s) before it not
confidently read at this resolution and in this hand. **Not interpreted here.** It could be: an archivist's
flag that a decipherment exists elsewhere (in which case this may not be as clean an "open" as it looks); an
instruction "to be deciphered" rather than a statement that it has been; or something else entirely. Whoever
next opens this folder should pull a full-resolution crop and, if still unclear, view the same spot on a
brighter/backlit scan setting if Gallica offers one, before doing anything with the cipher itself.

## Editions and prior art

- **Cryptiana (Tomokiyo, `sources/cryptiana/web/francis.htm`), section "De Morvillier's Cipher (1546)"**: names
  this exact item -- "The cipher used in a letter from de Morvillier, ambassador in Venice, to the king (BnF
  fr.2996 f.52, no.25), 24 January 1546, was broken by George Lasry in 2023" -- and shows a key-table image
  (`GL/BnF_fr2996_f52.png`, not fetched this pass). As with Gramont (M8), **the key is published; no plaintext
  or transcription is given** on Tomokiyo's page.
- **dbourdeau/cyphersolver** and **aaymeloglu/unsolved-ciphers** (fresh shallow clones, 23 Sept 2026): grepped
  both for "morvillier" and "2996"; no target folder or solved-catalogue entry for this item in either (the
  scattered hits in cyphersolver's search.json and elsewhere are unrelated matches on the digits "2996" in
  other contexts, checked individually).
- **Charriere, Negociations de la France dans le Levant, vol. 1 (1848, covers 1515-1547)**, the standard printed
  edition for French-Venetian/Ottoman diplomatic correspondence of this period and period, was checked by
  Gallica ContentSearch (full-text OCR search) on `ark:/12148/bpt6k1145214` for "Morvillier" and "Morvilliers":
  **0 hits for both spellings.** Not exhaustive (OCR misses, alternate spellings, or the letter simply not
  printed there are all still open); a verifier should not stop at this one edition.
- **DECODE cached catalogue** (`sources/decode/`): empty, nothing to grep.

## Verdict

**Open, verified unsolved by this sweep** (not found-solved): no plaintext or transcription of this specific
letter found in Cryptiana, either solver repository, or one pass through Charriere vol.1's full text.

**Reclassify kind: recovery, not cryptanalysis**, for the same reason as M8: "De Morvillier's Cipher (1546)"
is already broken and published (Lasry 2023 / Tomokiyo), just not yet applied to this leaf by anyone whose work
is public.

Stage: **2, verified unsolved**, with one open flag (the marginal note) that a solver should resolve before or
while transcribing, not after. No copy order needed (Gallica image in hand).

## For the next worker (not done this pass)

1. Full-resolution crop and read of the pencil marginal note before transcribing the cipher block itself --
   if it turns out to say a decipherment exists (elsewhere in this volume, or filed separately), that changes
   the target from "open" to "partial" per the Dupuy 468 pattern, and check-solved does not get to decide that.
2. Fetch Tomokiyo's key image (`GL/BnF_fr2996_f52.png`) into `img/` (cite, do not silently reuse without
   attribution) and transcribe the ~6-line cipher block against it.
3. Verifier: search Morvillier's Venice embassy correspondence more widely than Charriere vol.1 alone --
   Ribier, the BnF's own fr.2957 "Correspondance diplomatique de l'ambassadeur de France a Venise" (a
   contemporary copy series turned up by this pass's web search, unchecked), and any modern edition of
   Morvillier's early despatches -- before any "unread"/"new" wording (rule 10).

## Requests this pass

gallica.bnf.fr: 1 IIIF manifest.json, ~4 IIIF image fetches (2 wrong-folio calibration probes not kept, 1 kept
leaf image, 1 region crop), 1 ContentSearch (2 queries, one ark, 0 hits both). archivesetmanuscrits.bnf.fr: 1
finding-aid page. github.com: 2 shallow clones (shared with M8/M10/M11, not re-cloned). WebSearch: 2 queries
(Morvillier general search, Charriere edition search). All requests 1.5s+ apart, no 429/403 encountered, no
logins or credentials used.
