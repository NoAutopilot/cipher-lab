# BnF Français 2980, ff.29-30: two cipher letters of Cardinal Gabriel de Gramont, bishop of Tarbes

open

Check-solved sweep, 23 September 2026 (started ~23:19 UTC, this section written ~23:40 UTC; `date -u` read before
writing). QUEUE row M8. Worker: check-solved M8-M11 (Sonnet, cap $8 across all four targets).

## What the BnF finding aid and Gallica leaf show

BnF finding aid (`archivesetmanuscrits.bnf.fr/ark:/12148/cc494342`, fetched 23 Sept 2026, one retry after a
connection reset):

- Fol. 29, item 21: "Lettre, avec chiffre, du cardinal Gabriel DE GRAMONT, evesque de Tarbe... à monseigneur...
  de Villandry, conseiller du roy et secretaire de ses commandemens et finances... A Rome, le XXme jour de may."
  No year given in the finding-aid snippet.
- Fol. 30, item 22: "Lettre en chiffre du cardinal Gabriel DE GRAMONT, evesque de Tarbe... Faict à Rome, le XXme
  jour de may M.D.XXX" — dated **20 May 1530**.

Both leaves viewed via Gallica IIIF (`images/f29_item21.jpg` = canvas f31, `images/f30_item22.jpg` = canvas f32,
`images/f31_item23_context.jpg` = canvas f33). Canvas-to-folio offset for this volume found by direct probing
(f41/f53/f75 misleading, f33 gave the first firm anchor via item 23's plain Latin text matching folio 31
exactly; see `images/manifest.json`).

**Both items are genuinely and heavily ciphered, confirmed by image, no key or gloss on the leaf itself:**

- **Fol. 29 (item 21):** mixed letter — ~7 lines plain French salutation, a wax seal, then **~13 lines of dense
  cipher** (numeral and symbol tokens, roughly 15-20 tokens/line, so very roughly 150-200 cipher tokens), signed
  in clear "De Gramont E. de Tarbe". No interlinear or marginal decipherment visible.
- **Fol. 30 (item 22):** **entirely ciphered**, ~25 lines filling the whole recto densely (roughly 20-25
  tokens/line, so **very roughly 500-600 cipher tokens**), continuing onto the verso where it closes and is
  again signed "De Gramont E. de Tarbe" (canvas f33, left page). No plaintext, gloss or key anywhere on either
  leaf or its facing pages.

Total extent across both items: roughly 650-800 cipher tokens, well above the M6/M7 "short letter" scale (rule
3/size caveat in QUEUE.md no longer applies at this size).

## Editions and prior art

- **Cryptiana (Tomokiyo, `sources/cryptiana/web/francis.htm`), section "BnF fr.2980 (1530)":** explicitly names
  both items — "f.29 (no.21) is a letter dated Rome, 20 May [1530], from Cardinal Gabriel de Gramont, Bishop of
  Tarbe, to Jean Breton, seigneur de Villandry... f.30 (no.22) is a letter dated Rome, 20 May 1530 from Cardinal
  Gabriel de Gramont, Bishop of Tarbe... **These undeciphered letters can be read with Gramont's cipher (1530)
  below.**" Tomokiyo gives no plaintext or transcription for either item — only the observation that the key
  applies.
- **The key itself is already published and cross-validated**, but not on this manuscript. "Gramont's Cipher
  (1530)" was reconstructed by Tomokiyo from BnF fr.3019 f.20 (a different Gramont-to-Grand-Master letter), then
  the same key was independently rediscovered by George Lasry's codebreaking in 2023 and confirmed to also read
  BnF fr.3071 f.17 (no.7) and two letters in BnF fr.3040 (f.12 no.4, f.18 no.6, "both deciphered"). None of
  those source volumes is fr.2980.
- **dbourdeau/cyphersolver** (fresh shallow clone, 23 Sept 2026) has a `gramont1529/` folder (catalogue item 6:
  Gramont, Mâcon and Langeac to Montmorency, 1529-1537) that read **fr.3071 no.7 with this exact "Gramont's
  cipher (1530)"** to ~85%, plus fr.3091 no.23 ("Gramont's cipher (1529)", a different key, read in full) and
  two other letters. His NOTES.md is explicit that "Neither site gives any plaintext... the task here was
  reading the letters, not breaking the ciphers" — i.e. he applied Tomokiyo/Lasry's published keys by hand.
  **fr.2980 does not appear anywhere in his repository** (grepped the full clone for "2980" and "gramont",
  checked every hit; none is this manuscript).
- **aaymeloglu/unsolved-ciphers** (fresh shallow clone, 23 Sept 2026): no hit for "2980" or "gramont" anywhere
  in the repository.
- **DECODE cached catalogue** (`sources/decode/`): empty, nothing to grep (no cached catalogue file present
  this session).
- No web search run this pass beyond the Cryptiana/solver-repo checks above (in-budget triage; a full
  Gramont-correspondence edition search, e.g. Wirtz-Daviau on the 1529-30 Rome embassy noted as unchecked prior
  art in Bourdeau's own NOTES.md, is left to the solver/verifier stage).

## Verdict

**Open, verified unsolved by this sweep** (not found-solved): no source checked gives a plaintext or a
transcription of fr.2980 ff.29-30 specifically, and the only two projects that read letters in this key
(Bourdeau, and Tomokiyo/Lasry themselves) explicitly did not include this manuscript.

**Reclassify kind: recovery, not cryptanalysis.** The QUEUE row scored this as "cryptanalysis" on the
assumption no key existed. A key does exist, is published, and is independently cross-validated on three other
manuscripts (fr.3019, fr.3071, fr.3040) by two different methods (Tomokiyo's reconstruction and Lasry's
codebreaking) — applying it to fr.2980 is transcription-and-substitution, not fresh cryptanalysis. Per
README's metric this is close to the cheapest kind of unique solve: a known key, an unread ciphertext, in
different boxes. Rule 10 still applies in full: nothing here may be called new, unpublished, first or unread
until a verifier searches for the plaintext in print (Gramont's own printed correspondence/embassy papers,
etc.) and classifies N0-N5.

Stage: **2, verified unsolved.** No copy order needed (Gallica image in hand).

## For the next worker (not done this pass — check-solved does not decode)

1. Fetch the full-resolution IIIF crops of fr.2980 f.29r (cipher portion only), f.30r-v, transcribe against the
   published "Gramont's Cipher (1530)" table (image at `cryptiana.web.fc2.com/code/francisGramont.png`, copy
   should be pulled into `img/` before transcribing, cited not copied).
2. Check Bourdeau's `gramont1529/decode.py` and alias table for the 1530 key's exact symbol-to-letter mapping
   before re-deriving it from the picture by eye.
3. Verifier must search Gramont's own printed embassy correspondence circa Rome, May 1530 (Wirtz-Daviau on
   Chabot's 1529 embassy, flagged unchecked in Bourdeau's own notes; Le Glay; Ribier; Négociations diplomatiques
   de la France series) before any "unread"/"new" wording, per rule 10 and the Dupuy 468 lesson (verifier's own
   re-dating/re-attribution widens the search, never narrows it).

## Requests this pass

gallica.bnf.fr: 1 IIIF manifest.json, 1 Pagination service call (all-"NP", unused), 1 ContentSearch (0 results,
manuscript not OCR'd), ~9 IIIF image fetches at 900px/1400px width for canvas-to-folio calibration and the two
item leaves (2 connection resets, each retried once after a pause, per the good-citizen single-retry rule).
archivesetmanuscrits.bnf.fr: 1 finding-aid page fetch (1 connection reset, retried once). github.com: 2 shallow
clones (dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers). No logins, no credentials used.
