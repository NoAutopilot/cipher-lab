open
The whole finding-aid text of NA toegang 2.01.27.02 (Raad der Aziatische Bezittingen en Etablissementen,
1800-1806, 63-page PDF, `www.nationaalarchief.nl/onderzoeken/archief/2.01.27.02/download/pdf`, extracted
and full-text grepped by this worker), its predecessor toegang 2.01.27.01 (Comité tot de Zaken van de
Oost-Indische Handel en Bezittingen, 1796-1800, 56-page PDF, same route) and toegang 1.04.17 (Hoge Regering
Batavia, 1602-1827 residuals, 132-page PDF, same route) all read directly by this worker 25 Sept 2026; the
Atlas-of-Mutual-Heritage-style secondary literature check named in the job brief and flagged by VX-CS04 as
not yet opened, Colenbrander's *Gedenkstukken der Algemeene Geschiedenis van Nederland 1795-1840* (Deel III,
GS 3/4, 1798-1801(2); Deel IV, GS 5/6, "Staatsbewind en Raadpensionaris" 1801-1806 -- both title pages read
to confirm), has now also been read directly by this worker (VX-CS06, 25 Sept 2026) via
`resources.huygens.knaw.nl`'s own full-text OCR search across all four bands, for Smissaert, Prediger, Elout,
Grasveld, cijfer and secrete -- see "Colenbrander Gedenkstukken -- independent read (VX-CS06)" below; the
Internet Archive "Opkomst van het Nederlandsch gezag" series remains not opened, deprioritised as a probable
period mismatch (the VOC-era documentary series ends the year before this correspondence).

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
  named in the job brief for 1800-1806): **read** (VX-CS06, 25 Sept 2026) -- see "Colenbrander Gedenkstukken
  -- independent read (VX-CS06)" below for the accessor, the source-id map, and the full search log. Letter
  and cipher absent from all four bands searched.
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

## Colenbrander Gedenkstukken -- independent read (VX-CS06, 25 Sept 2026)

Same accessor family as `ciphers/roell-vandedem-1809/NOTES.md` and `ciphers/vanspaen-vandergoes-1808/NOTES.md`:
`resources.huygens.knaw.nl/retroboeken/gedenkstukken/searchText/index_html?search_term:ustring:utf-8=<term>&
source_id=<N>&id=searchText` full-text-searches one volume's OCR (register included). The site's own
`toc/index_html?page=1&source=7&id=toc` dropdown gives the complete source-id -> volume map (22 sources
total, fetched once): **source 3 = Deel III, band 1, GS 3**, **source 4 = Deel III, band 2, GS 4** (title
page read: "DERDE DEEL. UITVOEREND BEWIND. -- ENGELSCH RUSSISCHE INVAL. -- 1798-1801(2)", 1907 -- the correct
window for a 20 Nov 1800 letter); **source 5 = Deel IV, band 1, GS 5**, **source 6 = Deel IV, band 2, GS 6**
(title page read: "VIERDE DEEL. STAATSBEWIND EN RAADPENSIONARIS. 1801-1806", 1908 -- the window for invnr
317's Elout/Van Grasveld 1805-1806 appointment).

Full-text search, all four sources, run 25 Sept 2026 (queries >=2s apart, descriptive User-Agent):

| term | src 3 (Deel III b1) | src 4 (Deel III b2) | src 5 (Deel IV b1) | src 6 (Deel IV b2) |
|---|---|---|---|---|
| Smissaert | 0 | 2 | -- | -- |
| Prediger | 0 | 4 | -- | -- |
| Elout | 0 | 0 | 0 | 4 |
| Grasveld | 7 | 5 | 0 | 3 |
| cijfer | 0 | 5 | 0 | 5 |
| secrete | 6 | 10 | -- | -- |

(Elout/Grasveld/cijfer only re-run on sources 5-6 once Deel III's 0-Elout result and the Elout/Van Grasveld
1805-1806 date made Deel IV the more relevant volume for those three terms; Smissaert/Prediger/secrete were
not re-run on Deel IV since band 2 of Deel III already gave the on-topic hits below and a 20 Nov 1800 letter
falls inside Deel III's own window.)

Every hit was opened and read in context (pages fetched via the volume's own `pages.json?source=N` ->
`html_url`, not just the snippet):
- **Smissaert** (Deel III b2, pp. 857, 1207): both are a *different* Smissaert (the gezantschapsattaché who
  carried the March 1802 Amiens peace dispatches) -- but the footnote to p. 857 confirms **"J. G. Smissaert,
  den secretaris van den Aziatischen Raad en vroeger van het O. I. Comité"** is his father, i.e. this
  confirms our sender's institutional role (secretary of the Raad der Aziatische Bezittingen) independently
  of the NA catalogue, without printing anything about the 20 Nov 1800 letter or its cipher.
- **Prediger** (Deel III b2, pp. 518, 522, 528, 1205): a *different* 1799 episode -- the Comité's dispute
  with the Uitvoerend Bewind over whether to send Prediger back to Batavia, and a Committee member's near-mass
  resignation over it. Same person, same institution, but not this letter, not cipher, not dated 20 Nov 1800.
- **Grasveld** (Deel III b1+b2, Deel IV b2): all about C. H. van Grasveld's diplomatic postings (Cisalpine
  Republic, etc.) and, at Deel IV b2 p. 599, his and Elout's joint appointment ("zijne keuze op van Grasveld
  en Elout") -- confirms the pairing named on invnr 317, prints nothing about a cipher.
- **cijfer** (Deel III b2, Deel IV b2): every hit is either a footnote marker ("Het volgende uit het cijfer",
  meaning the editor is about to quote *other* people's ciphered dispatches, none involving Smissaert,
  Prediger, Elout or Van Grasveld) or an unrelated anecdote (Deel IV b2 p. 406, a different pair of prisoners
  "in cijfer naar Petersburg").
- **secrete** ("secret", both Deel III bands): register/footnote entries for secret resolutions, secret
  treaties and secret despatches of other correspondents; none names this letter.

No hit in any of the four bands pairs Smissaert and Prediger as correspondents, none is dated 20 Nov 1800, and
none prints or references a cipher passage from either invnr 209 or invnr 317. This independently confirms
and closes the gap VX-CS04 flagged (accessor not located) -- the standard edition named in the job brief has
now actually been read, not merely searched for.

## Cheap test (VX-CS06, 25 Sept 2026): does invnr 317's system read invnr 209?

Per CLAUDE.md 3a / this job's brief: transcribed invnr 209's cipher body (leaf 2 only -- leaf 3 stays too
faint to transcribe, confirmed again this pass) and invnr 317's alphabet table, then tested whether 317's
keyword-driven reciprocal alphabet reads 209.

**Transcription.** Two independent blind passes (this worker, then one Sonnet subagent with no access to this
worker's read) of leaf 2's cipher-body image (`images/209_leaf2_cipher_zoom.jpg`) **agree exactly on the top
row: 35/35 digit positions**, in the same five groups (14+10+3+3+5 digits: `56315263466166 2613676275 247
667 35134`). The accompanying second row of single digits (function unknown -- still not resolved, per
VX-CS04) is uncertain in 2 of 5 groups (flagged position-by-position in `ciphertext_209_leaf2.tsv`), but the
digit-vs-letter question this test turns on has **zero disagreement between the two passes**: every token
either worker read, certain or uncertain, is a decimal digit. No Latin letter appears anywhere in the cipher
body.

**317's system**, transcribed from `images/317_leaf1_alphabet.jpg` (the table) and `images/317_leaf2_example.jpg`
(the worked example, keyword "Nebawo", plaintext "De zaak zal geld kosten"), implemented in
`key_317.py`: 13 rows, each headed by a pair of key letters (Z.Y down to B.A, the alphabet split into 13
consecutive pairs), each row a fixed top line `a-m` reciprocally paired against a rotation of `n-z`; the
in-play keyword letter selects the row. Verified exactly (grade H) against the one worked-example instance
this worker could read with confidence -- "d in N is x" -- row 7 (N.M)'s table predicts exactly `x` for `d`.
Not independently re-verified for the other 11 rows (grade M): three other cursive instances in the worked
example ("e in E is p", "z in B is m", "a in A is n") don't match this worker's table-derived formula, most
likely a reading error in the cursive prose or the table's more compressed lower rows, not resolved in this
pass -- it doesn't affect the result below, since the control test only needs the implementation to be
internally self-consistent (round-trips whatever it encodes), not historically perfect.

**Result** (`scripts/test_317_vs_209.py`, numbers also in `specs/na-raad-azie-1800.json` `cheap_test_done`):

| | N tokens | in 317's domain (a-z) |
|---|---|---|
| **Target** (209 leaf 2) | 67 | **0 (0%)** |
| **Control** (matched-length period-Dutch sample, same table+keyword mechanism) | 35 letters | 35 (100%), round-trip decode 35/35 = 100% |

**Verdict: negative by design mismatch, not by cryptanalytic failure.** 0% of 209's tokens are even in the
alphabet 317's mechanism operates on -- a fact independent of key, keyword, or the row-transcription
uncertainty noted above. The control shows the apparatus (transcription + implementation) works perfectly
(100% round-trip) whenever its input actually is Latin letters, ruling out "the implementation is broken" as
an explanation for the target's 0%. This closes the question VX-CS04 flagged but did not check ("317's
letter-substitution table vs. 209's paired-digit cipher look like different systems on their face, not
checked further") -- now checked: they are provably different systems (one letter-domain, one digit-domain),
with no defined bridge between them in either document. No small key variation changes this, because the
mismatch is in the domain (digits vs. letters), not the specific key. Per this job's brief, this is the one
cheap test for this spec; no second test was run.

## Hosts and requests (this target)

`www.nationaalarchief.nl`: 5 (item pages for invnr 209 and 317, plus the three toegang finding-aid PDFs
2.01.27.02/2.01.27.01/1.04.17, all >=1.5s apart). `service.archief.nl`: 11 (5 leaves of invnr 209 + 2
native-res crops + 3 leaves of invnr 317 + 1 IIIF info.json, all >=1.5s apart, all HTTP 200). `archive.org`:
3 (advancedsearch queries for Colenbrander and the Opkomst series). WebSearch: 4 queries. Combined with
VX-N01's usage this worker's total on nationaalarchief.nl+service.archief.nl is 11+38 = 49 of the 60-request
combined budget for both targets in this batch (VX-CS04's figures, carried forward unchanged).

**VX-CS06 (this pass) additional hosts:** `resources.huygens.knaw.nl`: 33 requests total (1 toc dropdown
fetch, 1 reachability check, 2 pages.json listings, 3 title-page fetches, 4 result-page dereferences for
context, 22 term-search queries across 4 sources), all >=2s apart, well under the 40-request budget for this
host. No other network hosts touched this pass (the 317/209 comparison used images already on disk from
VX-CS04's fetch). No DECODE login, no credentials, no subagent network access (the transcription subagent
read a local image file only, no tools beyond Read).

## Closing line (job brief format)

**Key beside the letter:** no, for invnr 209 -- corrected from the QUEUE row's claim; no key or gloss found
on any of its 5 leaves. **Invnr 317 is itself a key** (a complete, worked cipher system) but has no
ciphertext letter beside it in this pass -- it names the two officials it was cut for (Elout, Van Grasveld)
rather than the Prediger correspondence, and the VX-CS06 cheap test above confirms nothing ties the two
systems together: 317's letter-substitution table and 209's numeral cipher are provably different designs
(0/67 of 209's tokens fall in 317's operable alphabet), not just dissimilar-looking.

**Grade counts (this pass):** H 0, C 0, S 0, M 2 (the transcription of 209's second digit row in 2 of 5
groups, and 11 of 317's 13 table rows not cross-verified against the worked example), I 0. No reading is
claimed; rule 10 -- no novelty wording used, this is a search result and a control-backed negative, not a
verifier's classification.

**Status stays `open`.** Colenbrander read (intake gate now passed); cheap test run and negative
(design mismatch, not weakness of the method). Next test, not run here per "never a second test": treat
invnr 209 as an independent numeral-cipher cryptanalysis target (see "Suggested next step" below, unchanged
from VX-CS04's pass).

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
