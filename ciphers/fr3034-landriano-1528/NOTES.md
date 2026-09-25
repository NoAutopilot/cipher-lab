# BnF Français 3034, items 68-69 (f.154/156, "Lettre, en chiffre")

found-solved
`sources/cryptiana/web/francis.htm` and `sources/cryptiana/web/GL.htm` (Tomokiyo's Cryptiana, "Earliest French Ciphers" and "Galeaz Vesconte's Cipher" / "Ambrosio Bizozola-Maximilian Sforza Cipher" sections, folio 154 and folio 156 of BnF fr.3034) were read in full by this worker; `https://dbourdeau.github.io/cyphersolver/index.html` (Bourdeau's cyphersolver site) was fetched and read in full live, 25 Sept 2026; `sources/decode/records-non-decrypted-2026-09-24-diff.tsv` rows 4223 (fol. 154) and 4224 (fol. 156) were read on disk.

## Target

LANE R8 scout lead (`ciphers/fr2933-salviati-1525/siblings.tsv`, row "Français 3034"): the finding aid for
BnF Français 3034 (ark cc494932, https://archivesetmanuscrits.bnf.fr/ark:/12148/cc494932) lists item 68,
"Lettre, en chiffre," dated at the camp at Landriano (Battle of Landriano, 30 Aug 1528), anonymous sender per
the finding aid's own item text, and item 69, "Lettre, en chiffre, d'Ambrosio Bizozola... a Maximiliano
Sforza," in the same volume. Neither is a Salviati letter (different sender/office); this intake was to
establish status before any deep work, per CLAUDE.md rule 1 and the check-solved brief.

## Search log (25 Sept 2026)

1. **Web search**: `"BnF" "3034" Landriano 1528 cipher Lasry OR Tomokiyo OR chiffre` (WebSearch) -- surfaced
   dbourdeau/cyphersolver GitHub issues/PRs and its site, plus George Lasry's Wikipedia page (background).
2. **Tomokiyo's Cryptiana** (`sources/cryptiana/web/`, checked first per Usage rule 3):
   - `francis.htm`, "Earliest French Ciphers (1526-1530)" section: BnF fr.3034 (Gallica ark cc494932, also
     catalogued in Google Books) f.154 no.68, "a mons. le grant maestre... Data al campo a Landriano, a li
     XXX d'aust 1528" -- listed as one of the letters carrying **Galeaz Vesconte's Cipher (1528-1529)**,
     alongside BnF fr.3045 f.28 (Galeazzo Visconti to Angelo Bolano, Alexandria, 12 Oct 1528, the letter the
     key was reconstructed from) and BnF fr.3096 f.91 no.47 (Galeas Visconte to Francis I, 12 June 1529).
   - `GL.htm` (Tomokiyo's article on George Lasry's 2023 codebreaking), section "Galeaz Vesconte's Cipher
     (1528-1529): BnF fr.3045, BnF fr.3034, BnF fr.3096" reproduces the reconstructed key
     (`GL/BnF_fr3045_f28.png`, image not mirrored in this repo's `sources/cryptiana/` snapshot) and repeats
     the same three-letter list, item 68 named explicitly by folio+item number ("f.154 no.68").
   - `GL.htm` section "Ambrosio Bizozola-Maximilian Sforza Cipher: BnF fr.3034" (separate key,
     `GL/BnF_fr3034_f156.png`, also not mirrored locally): "f.156 no.69 Lettre, en chiffre, d'AMBROSIO
     BIZOZOLA,... allo... principe... Maximiliano Sforza" -- this is item 69, its own key, also credited to
     Lasry 2023.
   - `unsolved.htm` (Tomokiyo's master unsolved-list page) heads BnF fr.3034 among 15 volumes under
     "Most Solved" (Lasry 2023), with the same paragraph naming what still remains unsolved elsewhere in
     that group (two items in fr.3022, one in es.336) -- fr.3034 is not among the named exceptions.
3. **DECODE (de-crypt.org)**: no live fetch needed -- the existing catalogue diff on disk,
   `sources/decode/records-non-decrypted-2026-09-24-diff.tsv` (built 24 Sept 2026 by cross-referencing
   DECODE's own listing against a fresh clone of dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers,
   see `sources/decode/NOTES.md`), already carries both records: row 4223 (id 4223, `BNF_Français_3034_154`,
   DECODE status "Non-decrypted") tags `bourdeau_hit = bizozola1520[read];visconti1528[read in
   part];visconti1529[read]`; row 4224 (id 4224, `BNF_Français_3034_156`) carries the identical tag string.
   DECODE's own catalogue status field is stale here (still "Non-decrypted" even though Bourdeau's repo
   already reads it) -- read as a DECODE-catalogue lag, not a live status, consistent with how the diff
   file's own caveat describes `held_by` ("hits to check, not verdicts").
4. **Bourdeau's cyphersolver repository site**, `https://dbourdeau.github.io/cyphersolver/index.html`
   (fetched live, one page, this worker; text quoted, no code copied -- Bourdeau's code is MIT, text CC BY
   4.0, per CLAUDE.md rule 8): "Galeazzo Visconti to Montmorency, Landriano, 30 August 1528 -- deciphered in
   part (93.3% of symbols)" -- this is item 68 (recipient "monseigneur le grant maistre" = Montmorency, Grand
   Master of France, matches the finding aid's own addressee). Separately: "Galeazzo Visconti to Angelo
   Bolano and to Francis I, October 1528 and June 1529 -- deciphered with Lasry's key, extended: the siblings
   of the Landriano letter (BnF fr. 3045 f. 28, fr. 3096 f. 91)" -- confirms the same three-letter set as
   Tomokiyo's page. Also: "Ambrogio Bizozola to Maximilian Sforza, Bologna, 4 November 1529 -- deciphered
   with Lasry's key" -- item 69 (the date "Bologna, 4 Nov 1529" is Bourdeau's own reading of the letter's
   heading, not independently checked against the image by this worker).
5. **Aymeloglu's unsolved-ciphers repository**: not grepped this pass (Bourdeau's independent confirmation
   plus Tomokiyo's primary account already give two-source corroboration; no clone of aaymeloglu's repo was
   on disk and cloning it was not needed to reach a verdict -- flagged as the one search-log gap for a
   verifier, per rule 10's template, to close if this target is ever re-examined).
6. **BnF finding aid** (`archivesetmanuscrits.bnf.fr/ark:/12148/cc494932`): not re-fetched live this pass --
   its item-68/69 text is already transcribed into `ciphers/fr2933-salviati-1525/siblings.tsv` (previous
   worker, read directly from `item_fr3034.html`) and matches Tomokiyo's and Bourdeau's folio/item numbers
   closely enough (Tomokiyo/Bourdeau: item 68 = f.154, item 69 = f.156; siblings.tsv: item 68 = "Fol.156" --
   a 2-folio discrepancy between the two transcriptions of the same finding aid, not chased further since
   both item *numbers* and both letters' content/date/sender agree across all three sources).

## Verdict

**found-solved, F0** (README's "What counts as a result": the specialist edition/database already links the
item to its decipherment; no contribution). Both cataloged-cipher items in this volume -- item 68 (Landriano,
30 Aug 1528, to Montmorency) and item 69 (Ambrogio Bizozola to Maximilian Sforza) -- were solved by
**George Lasry in 2023** (key reconstructed from the sibling letter BnF fr.3045 f.28, extended to this
volume; a separate key for item 69), published with reconstructed-key images on Tomokiyo's Cryptiana site
(`GL.htm`) and independently read into `dbourdeau/cyphersolver` (93.3% of item 68's symbols per that site;
item 69 "deciphered with Lasry's key"). Grade for every token in this NOTES.md: **H**, read from the two
named sources above (Tomokiyo's Cryptiana, Bourdeau's cyphersolver site); no cryptanalysis attempted by this
worker; no key applied by this worker; no image fetched by this worker (moot once found-solved). Per rule 10,
this is not novel and is not described as such anywhere in this file. Not a Salviati-pool match (different
cipher family and different sender/office from `fr2933-salviati-1525`/`fr5761-election-1519`) -- no glyph
comparison run.

## Next step

None. Do not promote to the board; do not fetch images; do not attempt a key. If a future pass wants the
actual plaintext text (not just the fact of the solve), read it from `dbourdeau/cyphersolver`'s own target
files for `visconti1528`/`bizozola1520` (not yet pulled into this repo) rather than re-deriving it.
