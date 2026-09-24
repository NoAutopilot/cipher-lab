open

# "Du Vergier", several original ciphered letters, BnF Clairambault 1108

QUEUE row: M19 (sources/solver-diffs — "Third pass, 24 September 2026 (M17-M21)" section of QUEUE.md).

## Source

BnF, Departement des Manuscrits, **Clairambault 1108**, part of the same composite "Clairambault 1058-1110,
Mélanges généalogiques et historiques" series as M18 (finding aid `archivesetmanuscrits.bnf.fr/ark:/12148/
cc137820/FRBNFEAD000013782_info`, same fetch reused for both targets, no extra request). This individual
volume is catalogued "L UZES-VENDOME". Gallica digitisation: `ark:/12148/btv1b90009665` (537 canvases).

**Precise catalogue entry, from the finding aid's own item list:** "**Fol. 245** • Du Vergier (Lettres orig.,
dont plusieurs avec chiffres)." The next item starts at **Fol. 265** ("Vendôme..."), so the Du Vergier item runs
roughly 20 folios -- a genuinely multi-letter item, matching the QUEUE row's "plural ciphered originals in one
place" framing. No first name or further identification given in the finding aid text itself.

## Check-solved sweep (24 September 2026)

1. **Web search.** "'Du Vergier' lettres originales chiffre BnF Clairambault XVIe XVIIe siècle" surfaced only
   the general Clairambault collection guides and the correct series page (`archivesetmanuscrits.bnf.fr/ark:/
   12148/cc137820`, used above), plus, as an unconfirmed identity hypothesis worth flagging and nothing more:
   Jean du Vergier de Hauranne, abbé de Saint-Cyran (1581-1643), the Jansenist theologian -- his dates (d. 1643)
   would fit an undated item filed in a volume otherwise ranging across the 16th-17th c., but nothing in the
   catalogue snippet or the leaf itself (below) supports or rules this out; **do not repeat as an identification
   without checking his own printed correspondence** (Lancelot's or Barbier's editions of Saint-Cyran's letters)
   first.

2. **Print/scholarship.** No Tomokiyo Cryptiana page mentions "Vergier" in any form (`sources/cryptiana/`
   grepped in full, 0 hits, both the web/ mirror and blog/). No dedicated search of a Du Vergier printed
   correspondence was completed this pass (budget) -- flagged as the concrete next edition-check step once a
   sender identity is confirmed from the leaf.

3. **Community lists.** Covered by the Cryptiana grep above (0 hits).

4. **DECODE.** `unsolved-ciphers/catalogue/decode-catalog.csv` grepped for "Clairambault 1108", "clair1108",
   "vergier": no row.

5. **Bourdeau.** Fresh shallow clone grepped for the ark (`btv1b90009665`, 0 hits) and "vergier" (0 hits
   anywhere in the repository, including its large `gallica_siblings/` HTML mirror).

6. **Aymeloglu.** Fresh shallow clone; catalogue and target folders grepped for "1108", "vergier": no hit.

Requests: gallica.bnf.fr 8 (1 IIIF manifest, recovered on the 4th attempt after three tunnel-side
`ws_closed_mid_exchange` resets -- confirmed via `/root/.ccr/README.md`'s documented pattern, not a Gallica
block, checked in `/__agentproxy/status`'s `recentRelayFailures`; 1 successful thumbnail probe at canvas f251;
3 failed attempts at canvas f248, all the same tunnel reset, not retried further this pass; 2 failed attempts
at a high-resolution crop of f251, same cause, abandoned), archivesetmanuscrits.bnf.fr 0 for this target (the
M18 fetch already covered this composite finding aid), WebSearch 1.

## What the leaf shows

**Located and confirmed this sweep, at canvas f251** (`images/probe_f251.jpg`), reached by the same +6
manuscript-folio-to-canvas offset that worked for M17 (folio 245 + 6 ≈ canvas 251; the leaf's own printed folio
stamp, visible top-right in the image, reads **"248"** -- three folios into the ~20-folio item, consistent).
This is a genuine, on-target hit, not a repeat of M18's miscalibration:

- **Left page**: numeral-group ciphertext (groups like "10 34", "587", "33 131", "708 285", "24 39 26" --
  a figure/nomenclator-style cipher, not an arbitrary-symbol one like M17's), written in lines with what
  appears to be a **partial interlinear gloss in a second, lighter hand** between several of the cipher lines --
  worth a close look by whoever transcribes this, since it may be a contemporary or later part-decipherment
  attempt rather than a clean ciphertext-only leaf. Not confirmed as a reading (too small at thumbnail
  resolution; the two follow-up crop fetches to check this closely both failed on tunnel resets, see above,
  and were not retried further this pass to stay within budget).
- **Right page**: continuous clear French, ending "...Votre très humble et très obéissant serviteur" and
  signed, legibly, **"Vergier"** -- confirms the finding aid's sender attribution directly from the leaf itself,
  independent of the catalogue.

This is a real, substantial, multi-letter ciphered item with the sender's own signature confirmed on the very
first probed leaf, and a possible existing partial gloss worth checking before any cryptanalysis is attempted
from scratch.

## Verdict

**Open.** No published plaintext, decipherment, or key found in six sources for "Du Vergier"/Clairambault 1108.
Unlike M17, no external published key was located either -- this is a genuine, unaddressed cryptanalysis (or,
if the apparent interlinear marks on f251 turn out to be a real gloss, partial-recovery) candidate. Concrete
next steps for a follow-on worker, not attempted here: (1) fetch a clean high-resolution crop of f251's left
page and determine whether the faint interlinear marks are a real gloss or a scanning/bleed-through artefact;
(2) fetch canvas f248 (folio 245, the item's actual start) and the following few canvases to establish the
letter count and total cipher extent across the ~20-folio item; (3) confirm "Vergier"'s identity (Saint-Cyran
is an unconfirmed hypothesis only) before any edition search of his printed correspondence.

Not touched: no key work, no decoding, no novelty wording.
