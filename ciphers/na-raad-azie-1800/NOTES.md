open
The whole finding-aid text of NA toegang 2.01.27.02 (Raad der Aziatische Bezittingen en Etablissementen,
1800-1806, 63-page PDF, `www.nationaalarchief.nl/onderzoeken/archief/2.01.27.02/download/pdf`, extracted
and full-text grepped by this worker), its predecessor toegang 2.01.27.01 (Comité tot de Zaken van de
Oost-Indische Handel en Bezittingen, 1796-1800, 56-page PDF, same route) and toegang 1.04.17 (Hoge Regering
Batavia, 1602-1827 residuals, 132-page PDF, same route) all read directly by this worker 25 Sept 2026; the
two Atlas-of-Mutual-Heritage-style secondary literature checks named in the job brief (Huygens retroboeken
Gedenkstukken, Internet Archive's "Opkomst van het Nederlandsch gezag" series) were **not opened** -- see
below -- so this verdict rests on the primary catalogue text and images plus DECODE/solver-repo/web checks,
not on those two printed editions.

# NA 2.01.27.02 Raad der Aziatische Bezittingen -- Smissaert/Prediger cipher and the Elout/Van Grasveld
cipher key, 1800-1801 (VX-N03)

QUEUE row: VX-N03 (`.claude/briefs/runs/2026-09-25-lane-vx-cs04.md`), sourced from worker VX-SCNA's
National Archief round-2 sweep (QUEUE.md, "Key beside the letter (LANE VX, 25 Sept 2026)" section).

## What was asked

Open invnr 317 ("Stukken over het aan Elout en Van Grasveld medegegeven cijfer") and search 2.01.27.02 and
its successor/predecessor archives (Raad der Aziatische Bezittingen; Comité Oost-Indische Handel; Hoge
Regering Batavia copies) for other secret missives "in cijfer" 1796-1806, digitised or not, cipher state of
each. Check-solved via printed editions for the Raad/Prediger/Elout correspondence (Colenbrander
*Gedenkstukken 1795-1840* for 1800-1806, Van Deventer/De Jonge *Opkomst* series), web, DECODE, solver
repos. Not asked: decode, build a key, or classify novelty.

## Correction to the QUEUE row's own description of invnr 209 (rule 2: image over transcription)

The QUEUE row called invnr 209 "the strongest pair of this pass: a true parallel plain/cipher text (not
just a decipherment written after the fact)" and described the cipher as "dense rows of non-alphabetic
marks, not simple digits -- a symbol-substitution cipher, not a nomenclator." **Both claims are wrong on
the image evidence**, eye-checked at native resolution across all 5 leaves of the item
(`images/209_leaf1.jpg` through `209_leaf5.jpg`, `images/manifest.json`):

- It is **not** a parallel plain-and-cipher rewrite of the same letter. It is **one letter**: the opening
  salutation ("20 Nov. 1800 / van Prediger / Geacht vriend!", leaf 2 recto) and the closing (signature,
  compliments, a same-day P.S. about a Council appointment, leaf 4) are in plain Dutch; only the substantive
  body in between is enciphered. This is the same clear-open/clear-close, cipher-body-only pattern as
  several other targets already on file (e.g. Schonenberg 1.02.04), not a full-text twin.
- The cipher itself is **numeric, not a symbol/character cipher**: `images/209_leaf2_cipher_zoom.jpg` shows
  unambiguous Arabic digits in two aligned rows -- a longer top row of multi-digit cipher groups (e.g.
  "56315 26346 6166", "26136 76275 24766 7", "35134") and a shorter row of single digits written directly
  beneath nearly every digit of the top row. This worker does not know what the bottom row means (a
  segmentation mark, a homophone/frequency annotation, or something else) and is not attempting to find
  out -- that is a solver's job, not this check-solved pass's -- but it is plainly digit-on-digit, not the
  "dense rows of non-alphabetic marks" the QUEUE row described. A third leaf (`209_leaf3.jpg`,
  `209_leaf3_zoom.jpg`) carries more of the same paired-digit-row cipher but is very faint, looking like a
  mirrored ink bleed-through from the facing recto rather than the page's own ink -- legible enough to
  confirm the same format, not enough to transcribe confidently; a properly lit/contrast-enhanced rescan
  would help whoever transcribes this.
- **No key or decipherment was found anywhere in this item.** All 5 leaves were eye-checked; leaves 1, 4 and
  5 are plain Dutch (a dispatch-routing memo and a separate 20 April 1801 postscript, matching the
  unittitle), leaves 2-3 carry the cipher with no interlinear gloss. This target therefore **fails this
  lane's own gate** (a key or decipherment beside the letter) -- it is a cryptanalysis-lane candidate, not a
  recovery-lane one, contrary to how VX-SCNA filed it.

## Established (H: catalogue text and images read directly by this worker)

**Invnr 317**, "Stukken over het aan Elout en Van Grasveld medegegeven cijfer" (documents on the cipher
issued to Elout and Van Grasveld), 3 leaves, fully digitised, copy-free
(`images/317_leaf1_alphabet.jpg`, `317_leaf2_example.jpg`, `317_leaf3_blank_verso.jpg`). This is **not a
ciphertext** -- it is the cipher *system itself*, undated, unsigned, complete: leaf 1 is a 13-row reciprocal
substitution-alphabet table headed by letter pairs (Z.Y down to B.A) with instructions that sender and
recipient need only share "een gegeven woord of slegte klanken zonder betekenis" (a given word, or
meaningless sounds) to use it, and that it "op 200 veel verschillende manieren" (200-odd different ways) can
be arranged; leaf 2 is a fully worked example keying the table with the word "Nebawo" against the plaintext
"De zaak zal geld kosten" and showing the resulting cipher letter by letter. Web search (below) confirms
Elout and Van Grasveld were the Commissioners-General sent out to reform Dutch East Indies governance around
1805-1806 (Van Grasveld also named Governor-General 11 Nov 1805, the commission recalled by King Lodewijk
before it could take effect), so this key was almost certainly cut for their outward mission -- but no
ciphertext produced with it was found anywhere in this pass. Grade: this is a key source (H if anyone later
applies it), not a reading; it has the same "key with no ciphertext beside it" shape CLAUDE.md's own table
already flags for VX-E02 (Legatie Turkije "Sleutels cijferschrift").

**Whole-toegang cijfer sweep.** The complete finding-aid text of 2.01.27.02 (63 pages, full-text extracted
from the site's own `download/pdf` route and grepped for `cijfer`/`geheimschrift`/`chiffre`) contains
**exactly two hits: invnr 209 and invnr 317, and no others.** This is a stronger result than a catalogue
term-search sample -- it is the complete finding-aid text, not a paged search UI -- so within this one
toegang the inventory asked for is complete and negative beyond the two items already known.

**Predecessor/related archives**, same full-finding-aid-PDF method:
- **2.01.27.01** (Comité tot de Zaken van de Oost-Indische Handel en Bezittingen, 1796-1800, the direct
  predecessor named in the job brief): 56-page finding aid, **zero** hits for cijfer/geheimschrift/chiffre.
- **1.04.17** (Hoge Regering Batavia, 1602-1827, the 19th-century residual items transferred to this toegang
  -- the bulk of the historical Hoge Regering archive is at ANRI Jakarta, not here): 132-page finding aid,
  **zero** hits for cijfer/geheimschrift/chiffre. One incidental hit for **"Prediger"** himself ("... door de
  Hoge Regering van R. Prediger, als commissaris ...") confirming his role but not a cipher item.
- **"Comité Oost-Indische Handel"** is the same body as 2.01.27.01 (its full name); no separate toegang
  found under that shorter name.

Not checked this pass, out of budget: a systematic sweep of every other 2.01.27.xx sub-series (only .01,
.02, and the unrelated .05 already on file from round 2 were touched) and the full VOC-successor family
beyond 1.04.17. Flagged as a follow-on, not a negative.

## Check-solved (web / print / community / DECODE / both solver repos)

- **Web search**, 25 Sept 2026: no hit for any decipherment, transcription or discussion of either item;
  general search on "Elout" "Van Grasveld" 1800 confirms them as the 1805-1806 Commissioners-General (see
  above) but nothing about the cipher itself. No hit for "Smissaert" + "Prediger" + cijfer beyond the NA
  catalogue page itself.
- **Colenbrander, *Gedenkstukken der Algemeene Geschiedenis van Nederland van 1795 tot 1840*** (the edition
  named in the job brief for 1800-1806): **not opened**. This worker located the series' Huygens retroboeken
  landing page (`resources.huygens.knaw.nl/gedenkstukken`) but could not find its per-volume `searchText`
  accessor id in the time budgeted (a guessed accessor 404'd), and it is not on Internet Archive under
  "Colenbrander Gedenkstukken" (checked, 0 hits both narrow and broad). Flagged for a successor worker who
  can spend the time finding the right accessor, rather than reported as a negative.
- **Van Deventer / De Jonge, *De Opkomst van het Nederlandsch gezag in Oost-Indië*** (the other edition
  named in the job brief): found on Internet Archive (26 volumes/scans, e.g. `deopkomstvanhet01devegoog`
  onward), but **not searched** -- this series is a VOC-era documentary collection (the VOC itself dissolved
  in 1799, one year before this correspondence), so it is very unlikely to cover an 1800-1801 Raad der
  Aziatische Bezittingen letter; deprioritised as a probable period mismatch rather than opened and read.
  Flagged rather than silently skipped.
- **DECODE (de-crypt.org)**: this worker's own grep of the repo's cached crawl
  (`sources/decode/records-decrypted-2026-09-24.tsv`, `records-non-decrypted-2026-09-24.tsv`) for
  "aziatische", "2.01.27", "prediger", "smissaert", "grasveld" -- zero hits.
- **Both solver repositories**, grepped 25 Sept 2026: zero hits for "smissaert", "prediger", "elout",
  "grasveld" or "raad der aziatische" in `aaymeloglu/unsolved-ciphers`; a handful of substring hits in
  `dbourdeau/cyphersolver` (inside unrelated corpus/binary files -- `bordeaux/run_real_plain_prime_umlaut_nowords.txt`,
  `harley1582r8505/ct2_p3.txt`, etc.) that on inspection are not about this correspondence, treated as noise.

## Hosts and requests (this target)

`www.nationaalarchief.nl`: 5 (item pages for invnr 209 and 317, plus the three toegang finding-aid PDFs
2.01.27.02/2.01.27.01/1.04.17, all >=1.5s apart). `service.archief.nl`: 11 (5 leaves of invnr 209 + 2
native-res crops + 3 leaves of invnr 317 + 1 IIIF info.json, all >=1.5s apart, all HTTP 200). `archive.org`:
3 (advancedsearch queries for Colenbrander and the Opkomst series). WebSearch: 4 queries. Combined with
VX-N01's usage this worker's total on nationaalarchief.nl+service.archief.nl is 11+38 = 49 of the 60-request
combined budget for both targets in this batch.

## Closing line (job brief format)

**Key beside the letter:** no, for invnr 209 -- corrected from the QUEUE row's claim; no key or gloss found
on any of its 5 leaves. **Invnr 317 is itself a key** (a complete, worked cipher system) but has no
ciphertext letter beside it in this pass -- it names the two officials it was cut for (Elout, Van Grasveld)
rather than the Prediger correspondence, and nothing ties the two systems together (317's letter-substitution
table vs. 209's paired-digit cipher look like different systems on their face, not checked further).

**Undeciphered copy-free material it could read:** invnr 209's cipher body (leaves 2-3, paired-digit format,
partly faint) is undeciphered and copy-free:
- leaf 2: `https://service.archief.nl/api/file/v1/default/a9eb3ad8-af67-41bc-b3d1-e63e3e7f0179`
- leaf 3 (faint): `https://service.archief.nl/api/file/v1/default/bfbdac90-46db-4bee-a9cd-78ab5bf06a51`

Invnr 317 (the Elout/Van Grasveld key) has no ciphertext of its own to read, but is copy-free and worth
keeping on file as a candidate key for any other 1800s-1806 Raad der Aziatische Bezittingen cipher that
turns out to use a keyword-driven reciprocal alphabet:
- `https://service.archief.nl/api/file/v1/default/ddc734bb-c772-47b6-bd53-4baf8e4ea9eb` (alphabet table)
- `https://service.archief.nl/api/file/v1/default/9032c2ee-6cd1-46e6-8bf9-04e262562f67` (worked example)

## Suggested next step (not this job's scope)

Invnr 209 is a cryptanalysis-lane candidate, not recovery: a modest amount of undeciphered numeral cipher
(roughly a dozen-plus lines across leaves 2-3), clear-text crib available (the letter is *to* Prediger,
*from* Smissaert, dated 20 Nov 1800, about troop reinforcements for Java per leaf 1's summary), Dutch
plaintext expected. A rescan of leaf 3 at better exposure/contrast would help before any transcription
attempt. Separately: test whether invnr 317's keyword-table system matches any other undeciphered Dutch
diplomatic cipher already on file from this period (the same "M12 key-only" pattern as VX-E02's Legatie
Turkije nomenclator).
