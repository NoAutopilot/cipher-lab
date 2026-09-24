blocked


**Edition check (LANE N3 csED, 24 Sept 2026 15:45 UTC):** hold lifted -- verdict `open`. No printed edition of
Marie de Médicis's letters to Savary de Brèves or of his Rome embassy papers was located; Lasry's 2021 break
covers a different, sibling letter (Henri IV to Brèves, fr.3541, 5 Jan 1610), not this one, and was never shown
to read this passage (section 2 below). Brief `.claude/briefs/runs/2026-09-24-lane-n3-csED.md`.
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
2. **Standard printed edition / calendar (edition check, LANE N3 csED, 24 Sept 2026).** No dedicated printed
   edition of Marie de Médicis's regency correspondence exists (WebSearch for "lettres de Marie de Médicis"
   editions turns up only modern narrative histories of the regency -- e.g. Zeller, *La minorité de Louis
   XIII; Marie de Médicis et Sully (1610-1612)*, on archive.org -- not a letters edition); this is a genuine
   search result (no such edition to read), not an unreachable one. No printed embassy papers or *Relation* of
   Savary de Brèves's 1608-1614 Rome mission were located either (WebSearch: his Rome-embassy letters and
   dispatches are described only as unpublished BnF manuscript holdings). Lasry's 2021 work (point 3 below) is
   the closest thing to an edition and is addressed there in full, including the specific question this brief
   asks -- whether Lasry printed or deciphered this very letter (no: a different, sibling letter). No HistoCrypt
   or other formal-paper publication of the Henri IV/Brèves break was found by WebSearch either; per Tomokiyo
   and Bourdeau's notes (point 3), the reading exists only as a DECODE record (R2077) and a photographed key,
   not print.
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

## Key capture and reading (24 Sept 2026, LANE R4 M)

**fr.3642 key: not obtainable via Gallica, confirmed independently.** Gallica SRU (`gallica.bnf.fr/SRU`), four
query variants on 24 Sept 2026 (`gallica adj "Français 3642"`, lowercase `"francais 3642"`, `gallica all "ms-3642"`,
`gallica all "fr. 3642"`; the last two intentionally broad as a check) all return either the same 3 unrelated
records (a Béthune manuscripts catalogue, a national bibliography serial, an Algiers newspaper — none is BnF
Français 3642) or thousands of noise hits from the untokenised broad query, never the manuscript itself. This
independently reproduces Bourdeau's own finding (`breves1610/NOTES.md`: "not on Gallica, SRU search 0 hits").
BnF fr.3642 is simply not digitised on Gallica. The only image of its key in either project is a 833×587px photo
attached to DECODE record R2077 (Camille Desenclos's find, per Tomokiyo/Bourdeau), and DECODE image access is
permission-blocked for this brief (ASKS.md row 42; not attempted, per brief instruction). **No key.tsv, no
decode.json, no decode run this session** — per this brief and rule 3/rule 7, a key that cannot be fetched is not
a cryptanalysis attempt to report, just an access blocker, already logged by Bourdeau and now reconfirmed.

**Cipher passages fetched and transcribed (two independent blind passes).** Gallica IIIF, ark `btv1b9059628m`
(manifest cached `sources/gallica-manifests/btv1b9059628m.json`, all 126 canvases labelled 'NP'; foliation fixed
by eye-checked anchors, canvas 36 = stamped f.19r, canvas 37 = f.19v, confirmed by the printed folio numeral
visible on each leaf and by the letter's dateline). Confirms Bourdeau's foliation exactly: the 15 Sept 1610 letter
is stamped f.17r (cipher, canvas 32) – f.17v (canvas 33, plain) – f.18r (canvas 34, signature "...jour de
Septembre 1610", "Brulart") – f.18v (canvas 35, blank/offset, not fetched); the 10 Nov 1610 letter is f.19r
(cipher, canvas 36) – f.19v (canvas 37, digits are show-through per Bourdeau, not more cipher, not separately
transcribed here). Native-resolution page images and line crops (`tools/iiif_lines.py`, ink-profile line
detection, debug overlays checked by eye) are in `images/`; `images/manifest.json` records the fetch.

Pass A (this worker) and pass B (one Sonnet subagent, blind from the same line-crop images, no outside source,
no plaintext inference) were reconciled with `tools/reconcile_passes.py` (`passA.tsv`, `passB.tsv` ->
`disagreements.tsv`, `ciphertext_draft.tsv`, `agreement.tsv`). Raw agreement: 32/104 aligned columns, 30.8%.
Reading `disagreements.tsv` by eye, the great majority of this is a **segmentation artifact, not a sign-identity
disagreement**: pass A tokenised the run largely letter-by-letter (`bx m ka`), pass B kept adjacent letters as
run-together clusters (`bxmy ka`), which shifts the column alignment for the rest of each line without either
pass actually disagreeing on the ink. Genuine content disagreements are narrower and listed for a future
reconciler to settle from the image: sept_L01 col 6 ("56" vs "7̄o" — plain digits vs a barred numeral +
letter-form, at the position Bourdeau's own transcription reads as part of the alphabet run), sept_L01 cols
20-22 ("za bm go" vs "3a [round-mark]mgo"), nov_L01 col 6 ("croiste" vs "avisse", both guesses at a hard-to-read
verb before "bien"), and the tail runs of nov_L02 (cols 15-24) where both passes agree on shape but not on
whether "ylc/yl c/mty" segment one way or another. `ciphertext_draft.tsv` (pass A's line/token grid, alternate
pass-B readings in the `alt` column, confidence M on every token because there is no key to grade against) is
the working transcription; it has not been fully settled against the image sign-by-sign and should not be
treated as a finished ciphertext.tsv without that pass. No H or C grade applies anywhere in this section: there
is no key and no known plaintext, so nothing here is a decipherment or a graded reading, only a transcription
capture, per this brief's "no cryptanalysis" instruction.

**Files:** `images/` (leaves, line crops, manifest), `sources/gallica-manifests/btv1b9059628m.json`,
`passA.tsv`, `passB.tsv`, `passA_sept.txt`/`passA_nov.txt`/`passB_sept.txt`/`passB_nov.txt` (line-prose working
notes behind the TSVs), `disagreements.tsv`, `ciphertext_draft.tsv`, `agreement.tsv`.

**Follow-up (not in this brief, one line only):** a settling pass on `disagreements.tsv` against the image would
sharpen `ciphertext_draft.tsv` into a citable `ciphertext.tsv`; separately, per Bourdeau's own note, only Lasry's
R2077 plaintext/ciphertext pair or a full-resolution fr.3642 image (BnF reading room, not Gallica) would reopen
the key side of this target. Status stays `open`.

Credit: this session's transcription and Gallica-negative reconfirmation build directly on D. Bourdeau's prior
`breves1610/` attempt (cited above) and do not supersede it; Bourdeau's own ciphertext transcription
(`ciphertext.txt`, `ct_sept.txt`, `ct_nov.txt` in his repository, CC BY 4.0) was deliberately not consulted before
this worker's pass A, to keep both passes blind.

LANE R4 orchestrator, 24 Sept 2026 17:25 UTC: status set `blocked` -- the key (BnF fr.3642) is not on Gallica and its DECODE photo (R2077) is behind ASKS 42; ASKS 43 asks for the route.
