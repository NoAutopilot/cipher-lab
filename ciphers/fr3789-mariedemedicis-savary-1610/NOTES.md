open

# Marie de Médicis to Savary de Brèves, Rome, 10 November 1610 — BnF fr. 3789 no. 12

QUEUE row: CS2-05 (`sources/solver-diffs/2026-09-24-cyphersolver-site.tsv`, LANE N3 scout scCS2, 24 September
2026 — catalogue item 25 at dbourdeau.github.io/cyphersolver/catalogue.html). Check-solved run 24 September 2026
by LANE N3 csCS2a (session_01JrahDoApcsEHgiQigjaJPY), brief `.claude/briefs/runs/2026-09-24-lane-n3-csCS2a.md`.

## What it is

Regent Marie de Médicis's letter of 10 November 1610 to François Savary de Brèves, then French ambassador in
Rome (undersigned "Brulart"), with a short ciphered passage (about 45 signs). A sibling letter of 15 September
1610 in the same volume (about 70 signs) is the same case. Bourdeau's repository (`breves1610/NOTES.md`, session
21 Sept 2026) gives the precise foliation: the BnF notice's "no. 12, fol. 21 et 23" is actually **stamped f.19r-v
(canvases 36-37)**; the notice runs two folios ahead of the stamped foliation here, and stamped f.21 is an
unrelated Savoy letter (a trap noted explicitly in his session).

## Six-source search log (24 September 2026)

1. **Tomokiyo (sources/cryptiana/ on disk; `louisxiii.htm` local snapshot names this exact letter).** Quoted
   verbatim: *"Marie's letters of 15 September and 10 November 1610 to Savary de Breves, then ambassador in Rome
   ..., (undersigned 'Brulart') in BnF fr.3789 ..., f.17, f.19, contain short passages in cipher, not deciphered.
   The cipher does not seem to match the known ciphers used by Savary de Breves (see [henryiv.htm])."* This
   names our exact date (10 Nov 1610) and states plainly: not deciphered. A live fetch of
   cryptiana.web.fc2.com/code/henryiv.htm (24 Sept 2026, not in the local snapshot) gives the "known cipher"
   referred to: Savary de Brèves's 1602-1603 cipher, whose key is in **BnF fr.3462** -- a different volume from
   the one below, for an earlier period, and Tomokiyo's own text says it does *not* match the 1610 passages.
   henryiv.htm also separately notes a *different* correspondent's cipher reused in fr.3789: "a letter of
   Villeroi from December 1605 in BnF fr.3789 ..., f.26" -- a different folio, not this item.
2. **Standard printed edition / calendar.** Not located this pass for Marie de Médicis's regency correspondence
   specifically to Savary de Brèves (no dedicated printed edition of her letters to this ambassador found;
   flagged for a future pass, not a blocker here since points 1, 3 and 4 below independently and directly name
   this exact letter as undeciphered).
3. **Lasry's publications (fr.3642 key).** This is the crux check for this row. Tomokiyo's `louisxiii.htm`
   records that a *similar-looking but different* cipher, used in a letter from **Henri IV** to Savary de Brèves
   of 5 January 1610 (BnF fr.3541, f.4-7, DECODE R2077), *was* solved ciphertext-only by George Lasry (with
   Norbert Biermann and Tomokiyo) in 2021, after which Camille Desenclos located its key at the BnF. Bourdeau's
   `breves1610/NOTES.md` confirms and extends this: DECODE R2077's own note gives the key's location as
   **"BNF Francais 3642"** (matching this queue row's "Lasry 2021 key fr.3642" note) and states *"The record's
   only document is a photo of that key ... R2077's note itself says R2075/R2076 'may be in the same cipher.'"*
   Bourdeau **tried this key** against Marie's 10 Nov passage: the opening groups "72 4 79" plausibly read as
   "[name?] le pape avec", but a systematic beam search over the photographed alphabet against the fr-1600 letter
   model "reaches -95 on 16 letters" -- i.e. it does not produce coherent French from the rest of the passage.
   His verdict: *"Closed as unreadable from available sources: the key photo is partial and too coarse... Only
   [Lasry's own R2077 decryption] or [a full-resolution image of BnF fr.3642, not on Gallica, 0 SRU hits] would
   reopen it."* So the Lasry/fr.3642 key exists and is the leading candidate, but **has not actually been shown
   to read this letter** with the material available -- it does not qualify as found-solved or a recovery with
   a working key per this brief's rule 3, only as an unconfirmed, partially-tested lead.
4. **DECODE (sources/decode/ on disk) + both solver-repo clones.** Local DECODE snapshot rows 2075 ("BnF
   Francais 3789, f.17-18", 1610-, French, non-decrypted) and 2076 ("BnF Francais 3789, f.19-20", 1610-, French,
   non-decrypted) match the two letters exactly (Bourdeau's notes give these the same DECODE ids, R2075/R2076,
   both "not deciphered" per Tomokiyo). dbourdeau/cyphersolver (shallow clone, 24 Sept 2026): dedicated working
   folder `breves1610/`, session 21 Sept 2026, states plainly *"Status: no write-up... Result: attempted, not
   read."* His session also checked Brèves's own reply in his Rome letter-book (BnF Cinq cents de Colbert 351,
   pp.724-730, "A la Reyne Regente, du 9 Decembre 1610"): it answers the letter point by point but "in
   paraphrase, never in her words", so it gives context (the subject is Savoy's disarmament and Spain's
   response) but no crib strong enough to recover signs. aaymeloglu/unsolved-ciphers: no hit for fr.3789.
5. **Ciphertext confirmed present on the Gallica leaf.** IIIF fetch, gallica.bnf.fr, 24 Sept 2026, 1 request:
   `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9059628m/f36/full/500,/0/native.jpg` (canvas 36 = stamped f.19r).
   Image shows an ordinary secretary-hand letter opening "Monsr de Breues..."; a run of digit/code groups is
   visible mid-page in a line beginning "74 4 79 39..." -- matching Bourdeau's transcribed opening "72 4 79" for
   this exact passage closely enough (a 2 vs 4 reading of one digit is exactly the kind of ambiguity his notes
   flag). Leaf: https://gallica.bnf.fr/ark:/12148/btv1b9059628m/f36.item

## Verdict

**Stage 2, open.** No source of the six claims this letter is deciphered. The nearest thing to a "found-solved"
risk -- Lasry's 2021 break of the sibling Henri IV letter and its located key (BnF fr.3642) -- was directly
tested against this letter by Bourdeau and did not produce readable French from the available (partial,
833x587px) photo of that key. This is therefore a genuine, still-open target with an identified but
unconfirmed/untried-at-full-resolution key lead, which is exactly the kind of candidate this lane's brief asks
for: a recovery target if a better image of BnF fr.3642 (not on Gallica) can be obtained, or Lasry's own R2077
plaintext/ciphertext pair can calibrate the photographed alphabet.

Credit: D. Bourdeau, cyphersolver, https://dbourdeau.github.io/cyphersolver/ (catalogue item 25; `breves1610/`
working folder, including the Brèves reply-letter search), CC BY 4.0 -- prior attempt (not a solution). S.
Tomokiyo, "Cipher Letters of Louis XIII's Reign" (cryptiana.web.fc2.com/code/louisxiii.htm) and "Cipher Letters
of Henri IV's Reign" (henryiv.htm), for identifying the letter and the (non-matching and partially-matching)
known ciphers. Camille Desenclos for locating R2077's key at the BnF (per Tomokiyo/Bourdeau, second-hand).

Not decoded, not transcribed here beyond the presence check above (out of scope for check-solved; Bourdeau's
`breves1610/ciphertext.txt` already has a transcription if a solver picks this up). Rule 10: no novelty claim
made; this is a search result, not a verifier's classification.
