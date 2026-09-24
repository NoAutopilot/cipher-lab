# taurello-roma-1527

Status: open

## What this is

Single Este-Rome dispatch entirely in cipher, 24 June 1527, from the mission of Petr'Antonio Taurello to
Filiberto di Chalons, Prince of Orange (imperial commander, later commander at the Sack of Rome, 6 May 1527 —
this letter is from five weeks after the sack began, sent from Vetralla near Rome). Archivio Segreto Estense,
Cancelleria, Carteggio ambasciatori — Roma, piece no. "32" as printed in the finding aid (flagged by the 24 Sept
scout as likely an early Appendice-I piece number, not a final ASMo shelfmark). Finding-aid note (verbatim):
"Questa lettera è tutta in cifra" ("this letter is entirely in cipher"). No key or sibling decipherment noted in
the finding aid. QUEUE.md row IR8 (LANE N scout IT3 of 24 Sept 2026); source PDF
`ASE_Cancelleria_ambasciatori_roma.pdf`, ASMo/Este archive.

Ciphered status is stated directly and unambiguously by the finding aid ("tutta in cifra"). No key is filed with
it, per the same entry — unlike IR1/IR2/IR4/IR5, this is a cryptanalysis candidate (single letter, unicity
distance depends on length, not yet known — LESSONS.md's "large nomenclator, one letter" failure class is the
relevant risk here until the item is seen). `ciphertext.txt` is not created.

## Check-solved sweep, 24 September 2026

1. **Web.** WebSearch `Taurello "tutta in cifra" 1527 Filiberto Chalons Orange Vetralla lettera` and
   `"Petronio Taurello" OR "Pietrantonio Taurello" Ferrara Este ambasciatore Roma 1527`. Hits: Wikipedia pages
   for Philibert of Chalon, Battle of Gavinana, Siege of Florence (all general Sack-of-Rome-era context, no
   Taurello mention); a search-index PDF and the ASMo Spagna-fondo PDF itself, noting Pietrantonio Taurello as
   Ferrara's orator to Spain with correspondence documented May 1525 – Nov 1526 (a different posting/fondo from
   the Roma dispatch under review, not necessarily inconsistent — envoys moved between courts). No hit names
   this specific 24 June 1527 letter, its cipher, or a decipherment. Not found.
2. **Print.** WebSearch for Pastor's *History of the Popes* appendix material on Este ambassadorial dispatches
   around the Sack of Rome returned only general Sack-of-Rome background, no specific citation of this letter or
   piece "32". Not confirmed absent at verifier level (Pastor's, Venturi's and Balan's appendices were not read
   page-by-page — out of one worker's budget).
3. **Lists.** `sources/cryptiana/` grepped locally for `taurello|torello`: no hits.
4. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` grepped for `taurello|torello|roma.*1527`:
   no matching envoy/shelfmark. Live de-crypt.org not queried.
5. **Bourdeau/Aymeloglu.** Fresh shallow clones, `grep -ril "Taurello"` (and "Torello") across both trees: 0
   hits for either spelling.

## Verdict

**Open.** No source located a solution, key, plaintext or documented attempt for this item. Given the historical
proximity to the Sack of Rome (Taurello was with the future Habsburg commander five weeks before it), this is
the kind of item worth checking specifically against Pastor/Sanuto/Sack-of-Rome documentary collections before
any solver attempt — the general web sweep this pass found only secondary/tertiary background, not the primary
diplomatic editions themselves.

Copy-order: no digitised image found; the piece number "32" is not a confirmed shelfmark (see above — a worker
should cross-check the Roma fondo's own key before requesting). REQUEST.md below gives what can be specified.

Requests this pass: WebSearch 4, github.com 0 (reused shared clones). No SIAS, no Google Books, no DECODE login,
no promotion, no decoding.
