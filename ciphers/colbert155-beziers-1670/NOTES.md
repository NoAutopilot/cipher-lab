open

INTAKE-SAVOY unit B, 27 Sept 2026: solver-ready intake only (Layout, no reading, no decoding, no class), on
the `ciphers/fr4715-montholon-1589` / `ciphers/nevers-birago-fr3251-1572` pattern. Built from KEY-ADJACENT.tsv
row 7 and `sources/cryptiana/web/louisxiv0.htm` (local mirror, the Colbert-Croissy Cipher (1668-1674) section,
read in full this session; not re-fetched).

# BnF Melanges de Colbert 155, undeciphered letter of Mr l'Evesque de Beziers, Madrid, 13 August 1670

Bishop of Beziers (addressee unspecified in the extract -- likely Colbert or Louis XIV). Digits/syllables,
per louisxiv0.htm.

Tomokiyo, verbatim (louisxiv0.htm, the paragraph immediately after the Colbert-Croissy Cipher (1668-1674)
key table and its usage list across Melanges de Colbert 149-176bis):

> "An undeciphered letter of Mr l'Evesque de Beziers, dated Madrid, 13 August 1670, in Melanges de Colbert 155
> (Gallica) can be read with this key ("afin que silent reprise ...")."

Check-solved header: Tomokiyo's own page is the only source read this pass; his prose explicitly calls this
letter undeciphered and names it as readable with the printed Colbert-Croissy key, giving only the three-word
opening as a worked example. No solver-repository grep run this pass (KEY-ADJACENT.tsv's ranking already
records neither Bourdeau nor Aymeloglu as covering Melanges de Colbert 155 specifically); a fresh grep of both
shallow clones for "Beziers"/"Colbert 155"/"1670" is the outstanding check-solved step before any campaign.

## The gate (this unit's first step)

The page's own text gives only the letter's opening three words ("afin que silent reprise") followed by
Tomokiyo's own trailing ellipsis -- no further decipherment, no per-group alignment. **Gate verdict: only the
opening is given, the expected case** -- this is a genuine open target with a three-word known-plaintext crib,
not a found-solved retirement.

## The folio search (this unit's second step)

The row gives no folio number ("-- (single letter, folio not given in extract)", KEY-ADJACENT.tsv). Checked
`tools/gallica_folio.py btv1b100340323 --list`: the manifest carries 828 canvases, every one labelled "NP"
(non paginé) -- no folio labels exist for this volume at all, so there is no way to map "13 August 1670" to a
canvas from the manifest alone. A targeted `archivesetmanuscrits.bnf.fr` finding-aid search for an item-level
notice (the CS-FR3976/BNF-BATCH precedent) returned HTTP 404 on the query path tried; not pursued further
within this unit's 10-minute search cap (about 4 minutes spent: 1 Gallica manifest fetch, 1 archivesetmanuscrits
query). **Folio not located.** No images fetched; `images/manifest.json` not written. A future worker with more
time could try the volume's own item-level finding-aid record (if one exists, distinct from the Gallica ark) or
a phrase/date search once the DECODE and BnF catalogue routes are checked.

## What's on disk

- `known_plaintext.txt`: Tomokiyo's own printed three-word opening (grade H per CLAUDE.md rule 4 -- his
  reading, not ours), transcribed verbatim. No group-by-group "DUMP" alignment exists for this letter
  anywhere on the page (checked in full) -- unlike the fr4715-montholon-1589 precedent, a reader has only
  these three words and the key table to calibrate against, no aligned cipher-group anchors.
- `keys/key_colbert_croissy_1668.tsv`: the Colbert-Croissy Cipher (1668-1674) table from `louisxiv0.htm`
  (image `louisxiv_0croissy1668.png`, a clean printed/digital table, not a hand-drawn one) -- 133 rows across
  three diacritic-marked numeral code-spaces (bare/none, macron/overbar, circumflex/caret) sharing the same
  digit range, transcribed by direct inspection of three overlapping upscaled crops plus one independent
  blind Sonnet subagent read of the same crops as a cross-check. The two reads agreed on every row (all
  grade AB); three macron-marked cells (signs 40, 54, 55) print no meaning at all in the source itself,
  recorded as "(blank in source)" at grade H (read correctly as blank). `tools/key_design.py` should read
  this `usable=yes`; design family is a mixed letter/syllable/word nomenclator (homophonic letters plus a
  syllabary plus a small proper-name/common-word code), not a plain substitution -- flag this for
  `design_prior.py` before any attack family is chosen (CRYPT B1/README "Keys as an attack corpus").
- No `images/` content this pass (folio not located, see above).

## An important caveat for any future decode

Every other letter Tomokiyo cites as using this key (Melanges de Colbert 149, 158-167, 176bis, October
1668-December 1673) is Colbert de Croissy's own London-Paris despatch correspondence (to Lionne, later
Seignelay) or the one Duchess-of-Orleans passage in the same volume family. The Beziers letter is the single
outlier: a different sender (the Bishop of Beziers, not Croissy), a different place (Madrid, not London), and
two years earlier than the key's earliest dated London use (1670 vs October 1668 is actually within range, so
not a date problem -- but sender and place both diverge from every other cited use). Tomokiyo's own page does
not explain why this key would also serve a Madrid-Beziers letter; a reader should treat this as an open
question, not confirmed by this transcription, and watch for signs the actual cipher differs (an unusually
high residue of unmatched groups, in the AX-5799/CLAUDE.md rule 3 control-tests-the-manipulation sense) before
trusting a low match rate as evidence of transcription error rather than a wrong-key hypothesis.

## Next step

One careful reader with the key in view, calibrated on the three-word printed opening (`known_plaintext.txt`);
given the very short crib and the sender/place outlier above, the calibration is weak on its own -- a
20-shuffled-key control is still required (CLAUDE.md rule 3) but should be read cautiously at this sample
size, and the reader should flag early whether the letter's own code groups look like this key's mixed
letter/syllable/word design at all before committing to a full decode. Folio location is still needed before
any transcription of the actual cipher text can happen (see "The folio search" above) -- try the volume's own
item-level finding aid, or a LOCAL-QUEUE/JSTOR-style row if no free route is found. Reading to a verifier.
