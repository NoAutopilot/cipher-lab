open


**Edition check (LANE N3 csED, 24 Sept 2026 15:45 UTC):** hold lifted -- verdict `open`. CSP Spain III.2 (British
History Online, full text) and Lanz's Correspondenz des Kaisers Karl V vol. 1 (archive.org) both read for the
date; neither carries the letter or a decipherment (section 2 below). Brief `.claude/briefs/runs/2026-09-24-lane-n3-csED.md`.
# Unsigned letter to Seigneur Garbino, Madrid, 11 April 1528 — BnF fr. 3022 no. 20 (ff.44r-46v)

QUEUE row: CS2-01 (`sources/solver-diffs/2026-09-24-cyphersolver-site.tsv`, LANE N3 scout scCS2, 24 September
2026 — catalogue item 7 at dbourdeau.github.io/cyphersolver/catalogue.html). Check-solved run 24 September 2026
by LANE N3 csCS2a (session_01JrahDoApcsEHgiQigjaJPY), brief `.claude/briefs/runs/2026-09-24-lane-n3-csCS2a.md`.

## What it is

An unsigned Italian memoire/letter dated Madrid, 11 April 1528, catalogued as addressed "au seigneur Garbino"
(endorsement, f.47v). D. Bourdeau's own working notes (`vasto1527/NOTES.md` in his repository, session of
18-22 Sept 2026) identify the writer as "almost certainly **Hieronimo Ranzo**, Gattinara's man" from the shared
code, matching this queue row's sender attribution "Hieronimo Ranzo(?) to 'Garbino'". Probably a report of a
Venetian agent in Madrid (Tomokiyo).

The item is bound in the same BnF fr. 3022 recueil as two Marquis del Vasto/Gasto letters to Charles V
(ff.16v-17v, 26-28, 40-43) that George Lasry and Satoshi Tomokiyo solved/largely solved in April 2026 — a
**different** cipher from no. 20's (Bourdeau's no. 6 write-up: Caesar+1 substitution with a b-/c-/d- syllable
nomenclator; no. 20's is a base-letter-plus-superscript-number code, structurally unrelated).

## Six-source search log (24 September 2026)

1. **Tomokiyo (sources/cryptiana/ on disk + one live fetch of cryptiana.web.fc2.com/code/venetian.htm and
   unsolved.htm).** `venetian.htm`, "Memoire in Italian (1528)": *"A memoire in Italian, dated Madrid, 11 April
   1528 also uses a similar cipher with superscript figures (BnF fr.3022 ... f.44). Probably, it is a report of
   a Venetian agent in Madrid."* No solved tag on this item. `unsolved.htm` lists it under the same superscript-
   digit cipher family as Ranzo's fr.2988/fr.3019 letters: *"...a memoire in Italian dated Madrid, 11 April 1528
   (BnF fr.3022, f.44), all undeciphered, are also in a similar cipher with superscript digits."* Distinct
   passage on the same page for BnF fr.3022 "Most Solved" lists only the del Vasto/Gasto letters (f.16, f.26-28,
   f.40-43) as broken by Lasry in April 2026 -- no. 20/f.44 is not among them. No sentence anywhere on Tomokiyo's
   site claims a solution for no. 20.
2. **Standard printed edition / calendar (edition check, LANE N3 csED, 24 Sept 2026).** *Calendar of State
   Papers, Spain*, vol. 3 pt. 2, 1527-1529 (ed. Pascual de Gayangos, London 1877) -- read in full for the whole
   of April 1528 via British History Online (free full text, not Gallica/Google Books):
   https://www.british-history.ac.uk/cal-state-papers/spain/vol3/no2/pp641-651 (items 392-397, 1-10 April),
   .../pp652-664 (items 398-404, 11-20 April, includes the 11 April date itself: item 398 is Juan de Miranda to
   Lope Hurtado on French agents in Lisbon, unrelated), .../pp664-673 (items 405-413, 21-30 April). No item in
   the month matches an unsigned memoire to "Seigneur Garbino" from Madrid, and neither "Garbino" nor "Ranzo"
   appears anywhere on these pages -- confirms Bourdeau's note that the calendar covers no. 19 (the del Vasto
   letter) but not no. 20. Karl Lanz, *Correspondenz des Kaisers Karl V*, vol. 1 (1513-1532; Leipzig 1844) --
   full djvu text fetched from archive.org (id `correspondenzde00chargoog`, OCR of reasonable quality: "1528"
   and "Madrid" both hit repeatedly) and grepped: no "Garbino", no genuine "Ranzo" hit (only false positives on
   "Franzosen"); the entry nearest the date, no. 107 (N. Perrenot to the Emperor, 31 March/8/10 April 1528), is
   an unrelated report from the French court, not this letter. Marino Sanudo, *I Diarii*, vol. 47 (covers March-
   May 1528; archive.org id `idiariidimarino47sanugoog`) was also fetched (full djvu text, 1.59 MB) but its OCR
   is too degraded to search reliably -- zero hits even for "1528" or "Madrid", terms certainly present in the
   volume, so this is a search result of near-zero value, not a confirmed negative; flagged for a future pass
   with page images rather than OCR text if this target is promoted. Two of the three named editions were read
   with a genuine negative; the third (Sanudo) was fetched but not usably searched.
3. **Lasry's publications.** Lasry's April 2026 work on fr.3022 (via Tomokiyo, GL.htm) covers only the del
   Vasto/Gasto cipher (nos. 6, 10, 19) -- a different system from no. 20's. No Lasry solution of no. 20 is
   referenced anywhere.
4. **DECODE (sources/decode/ on disk) + both solver-repo clones (grepped by shelfmark).** Local DECODE snapshot
   row id 2292: "Paris, BnF, Francais 3022, f.44-47" (BnF_fr3022_f44), 1528-, Italian/probably Italian, non-
   decrypted, 6 of 12 fields filled -- matches this item exactly, status non-decrypted. dbourdeau/cyphersolver
   (shallow clone, 24 Sept 2026): `vasto1527/NOTES.md` gives the fullest account -- full transcription of no. 20
   made (1,315 groups, 546 types, `n20/f44r.txt` etc., combined with ~2,600 groups from Ranzo's signed fr.2988
   letters for ~3,900 groups total, 316 shared types), the code's numbering tested and found non-alphabetical
   (z=-0.5 against a shuffled null, vs +6.5 for a genuinely alphabetical control), and a word-substitution
   annealer validated at only ~46% token / ~9% type accuracy on a matched Castiglione control -- so on the real
   text it recovers only a function-word skeleton (che, il, per, la, non, si, etc.), no content words. Verdict:
   **"not solved... A reading needs the base key or real cribs."** No known nomenclator for Ranzo's code was
   found by Cipherbrain commenters (Norbert Biermann, Thomas, 2016-2017) either. aaymeloglu/unsolved-ciphers:
   no hit for fr.3022 in this shallow clone. WebSearch ("BnF fr.3022 f.44 Ranzo Garbino chiffre"): no result
   beyond Tomokiyo/Bourdeau's own pages.
5. **Ciphertext confirmed present on the Gallica leaf.** IIIF fetch, gallica.bnf.fr, 24 Sept 2026, 1 request:
   `https://gallica.bnf.fr/iiif/ark:/12148/btv1b90601558/f87/full/500,/0/native.jpg` (view 87, within the ff.44-46
   range). Image shows a full page of clear Italian prose with several lines of numeral cipher groups (two- and
   three-digit numbers, e.g. "26 133... 66... 100... 213...") at the foot of the page -- matches Bourdeau's
   description of no. 20's mixed clear/cipher layout. Leaf: https://gallica.bnf.fr/ark:/12148/btv1b90601558/f87.item

## Verdict

**Stage 2, open.** No source of the six claims a decipherment of BnF fr.3022 no. 20 (ff.44r-46v). Bourdeau's own
repository, working the item most recently (18-22 Sept 2026), closes it as "not solved" for lack of a key or
crib, having built a full transcription and a validated (matched-control) annealer that only reaches the
function-word skeleton. This is therefore a genuine cryptanalysis target, not a fresh one: the obvious annealer
route has already been tried and shown insufficient by a matched control (rule 3). What would move it, per
Bourdeau: Garbino's own side of the correspondence, Ranzo's letters elsewhere with a contemporary decipherment,
or Gattinara's papers -- none located this pass.

Credit: D. Bourdeau, cyphersolver, https://dbourdeau.github.io/cyphersolver/ (catalogue item 7; `vasto1527/`
working folder), CC BY 4.0 -- prior attempt (not a solution). S. Tomokiyo, "Reading Old Venetian Ciphers"
(cryptiana.web.fc2.com/code/venetian.htm) and "Undeciphered Historical Ciphers" (unsolved.htm).

Not decoded, not transcribed here (out of scope for check-solved; Bourdeau's `vasto1527/n20/` already has a full
transcription if a solver picks this up). Rule 10: no novelty claim made; this is a search result, not a
verifier's classification.
