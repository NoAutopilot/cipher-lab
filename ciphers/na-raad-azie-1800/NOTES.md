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

## Web and blog check (GF-A2-8, 2 Oct 2026)

Plain web searches (WebSearch, standard):
1. `Prediger Smissaert 1800 cijfer Raad der Aziatische Bezittingen` (sender + recipient + date): parlement.com and DBNL
   biographies of the Smissaerts (J.C. Smissaert was secretary-general of the Comité / Raad 1796-1806), the NA
   2.01.27.02 finding-aid PDF (already grepped by VX-CS06), a Van Braam Wikipedia page. No decipherment of invnr 209.
2. `"2.01.27.02" 209 OR 317 cijfer Elout Grasveld` (shelfmark + cipher word): only civil-engineering, postcode and
   tender pages. No hit.
3. `"Nebawo" cijfer OR "De zaak zal geld kosten"` (the two distinctive clear-text strings on invnr 317's worked example,
   quoted): only Dutch legal-aid forum pages. Neither string is on the open web.
4. `Elout Van Grasveld commissarissen-generaal 1805 cipher key secret correspondence East Indies` (descriptive title):
   Elout Wikipedia/parlement.com, Van Grasveld parlement.com, NA 2.21.059 finding-aid PDF, a DBNL Molhuysen entry, and
   the Tartu repository item "The Codebook of Willem Six van Oterleek: Dutch Diplomatic Intelligence from Saint
   Petersburg between 1806-1810". By title and snippet that item covers a different envoy and office, and it does not
   name 2.01.27.02, Prediger or Smissaert. It was not opened further.
Blog site searches:
5. Cipherbrain (`site:scienceblogs.de`), "Prediger Smissaert Dutch cipher 1800": the only plausible hit, "The Top 50
   unsolved encrypted messages: 34. Unsolved nomenclator messages" (24 Apr 2017), was opened and its body and comment
   thread (965 text lines, 23 comment markers) grepped for prediger|smissaert|aziatisch|batavia|indies|1800|dutch. It
   carries a Dutch nomenclator from Karl de Leeuw and the Dedem van Gelder 1809 message, plus the remark that Dutch
   nomenclators from 1800 on are "quite tough". It does not touch the Raad, Prediger or invnr 209.
6. Cryptiana (`site:cryptiana.blogspot.com`, `cryptiana.web.fc2.com`), "Dutch East Indies cipher 1800 Prediger": only
   arXiv and unrelated pages. No hit.
7. Cipher Mysteries (`site:ciphermysteries.com`), "Dutch East Indies cipher 1800 Batavian": La Buse posts and an "Indus"
   ship-history post. Nothing on this correspondence.
No decipherment or plaintext of invnr 209 (or of anything enciphered with invnr 317's table) was found on the open web
or in a blog comment thread.

## Premise check (GF-A2-8, 2 Oct 2026)

(a) Decipherments the folder mentions: **none for invnr 209.** NOTES.md records all five leaves of 209 eye-checked by
VX-CS04: leaves 1, 4 and 5 plain Dutch, leaves 2-3 cipher with no interlinear gloss, and leaf 3 a faint bleed-through.
The second row of single digits under the cipher groups is unexplained; it is not a gloss in letters. Invnr 317 is a
key (a reciprocal 13-row table plus a worked example) with no ciphertext of its own. VX-CS06's cheap test showed it
cannot be 209's key: 0 of 67 tokens in its letter domain, against a 100% round-trip control. No clear copy, "attached"
decipherment or later-hand note is mentioned anywhere in the folder or spec.
(b) Other solvers' working files: **no rendering of this item; one key-family lead.** Fresh shallow clones (2 Oct 2026)
of dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers, grepped for prediger|smissaert|grasveld|aziatische|2.01.27.
Aymeloglu: no hit. Bourdeau:
- `targets/toulon1803/NOTES.md` quotes NA 2.21.227 item 335, a *Correspondentiecijffer* annotated "eerst voor den
  minister van Grasveld in anno 1799, nu in anno 1801 voor den Minister van Dedem ...". That is Van Grasveld as Batavian
  minister in 1799, an ordered dictionary code with six mark series, values 1-992, its booklet surviving as NA 2.21.045
  inv. 34313.
- `targets/r2242/NOTES.md` line 98 has a partial reading "sitteren [van] grasveld" in a 1795 Orangist letter, a
  different system.
- The other substring hits are corpus files.
Neither applies a key to invnr 209 or invnr 317. The 1799 Grasveld code is a plausible family lead for Batavian-era
government cipher, but 209 is a Raad correspondence (Prediger to Smissaert, 20 Nov 1800) in 5-14-digit groups with a
digit row beneath, which looks unlike a 1-992 marked code. **Not tested**: the next step would be to compare 209's
groups with that code's structure, which is a solver's job and not this pass's. Cited, not copied.
(c) Physical neighbours: invnr 209's own five leaves were all viewed by VX-CS04, so there is no unviewed facing page
inside the item. The neighbouring inventory numbers of 2.01.27.02 (208, 210) were not opened. The whole-toegang
finding-aid grep (VX-CS06) found only 209 and 317 for cijfer/geheimschrift/chiffre, so no catalogued decipherment
sits nearby. **Not found.**
(d) Recipient's side: Smissaert, as secretary of the Raad in The Hague, is the recipient, and the folder already searched
the Hague side (Colenbrander *Gedenkstukken* III-IV, full-text, VX-CS06). The sender's side is Prediger at the Cape
or Batavia; the folder records his commissarial role in 1.04.17. That means the Hoge Regering / commissarial copy
registers, whose bulk is at ANRI Jakarta. Those were **not searched** (no online route tried this pass), and
nothing in the folder says a copy register holds a clear draft of this letter. **Not found / unreachable.**
Requests: scienceblogs.de 1, github.com clones shared with the other three GF-A2-8 targets, WebSearch 7.

## 2 Oct 2026 -- A2-RAA: invnr 209's groups against the 1799 Grasveld code's structure (matched control)

Intake gate, run before this step (`python3 tools/intake_gate_check.py na-raad-azie-1800`, exit 0):

    na-raad-azie-1800: open (line 1) -- edition/page or full-text-search citation found within 6 lines

**Question** (GF-A2-8's Premise check (b), "Not tested"): could invnr 209 be written in the Batavian government's 1799
Grasveld *Correspondentiecijffer* (NA 2.21.045 inv. 34313; per dbourdeau/cyphersolver `targets/toulon1803/NOTES.md`,
MIT, cited not copied: an ordered dictionary code, values 1-992, each group carrying one of six marks -- none, wave,
caret, double stroke, overbar, plus -- groups separated by full stops)? The key booklet itself is not digitised, so
this tests structure only, against the four same-key letters Bourdeau transcribed (R2034, R1944, R1945, R1946).

**Method** (`scripts/test_grasveld1799_vs_209.py`, output `data/test_grasveld1799_vs_209.out`; control tokens extracted
to `data/grasveld1799_traffic_groups.tsv`, 617 groups, 1,775 digits). Three statistics, computed identically on the
target and on every control window: T1 = digits in {0,8,9} among 35 consecutive cipher digits; T2 = longest digit run
without a group separator; T3 = share of cipher digits carrying an annotation that is itself a digit. Controls:
C1 every 35-digit window of the real same-key traffic (matched design, matched length); C2 2,000 synthetic messages of
uniform 1-992 groups; C3 positive control, 2,000 x 35 letters of period Dutch (Breda 1624-25 print corpus) in a 7x4
row/column grid, to show T1 *can* read 0 (the control can differ from the target on this statistic, rule 3).

| | T1 (0/8/9 in 35 digits) | T2 (longest unseparated run) | T3 (digit-annotated share) |
|---|---|---|---|
| **Target**, 209 leaf 2 line 1 (35 top digits) | **0** | **14** | **0.914** (32/35) |
| C1 real Grasveld-code traffic, 1,639 windows | mean 8.74, min 2; **0 of 1,639** windows read 0 | 4 (one doubtful `9130`), otherwise 3 | 0.000 (marks are non-digit signs, one per group) |
| C2 synthetic uniform 1-992 code, 2,000 | mean 9.37; 0 of 2,000 read 0 | 3 | 0.000 |
| C3 positive control, 7x4 grid, 2,000 | **2,000 of 2,000** read 0 | 35 | 1.000 |

Reading: digits 0, 8 and 9 make up 25.0% of the Grasveld traffic's digits, so a 35-digit stretch with none of them
has probability about 0.75^35 = 4e-5, and no real window comes closer than 2. Even if the one doubtful top digit
(position 9, "4, possible 9") is a 9, T1 = 1 is still below every one of 1,639 real windows. The code separates
1-3-digit groups with stops and marks each group once with a non-digit sign; 209 writes unseparated runs of up to 14
digits with a second digit (1-4) under nearly every digit. **Verdict: control-backed negative by structure -- invnr
209 is not in the 1799 Grasveld code's design** (conditional on the four transcriptions Bourdeau made and on 209
line 1 as transcribed; the key booklet itself was not seen). C3 shows the test is not rigged to fail: a design built
of stacked coordinate pairs passes all three statistics.

**Image check (rule 2) -- correction to this folder's own extent statement.** Re-reading `images/209_leaf2.jpg` at full
page (not the zoom crop) shows that leaf 2's right-hand page carries **about 14 lines of stacked digit pairs**,
interleaved with clear Dutch phrases ("maar evenwel, zo wy hopen, eerlang", "is de Asiatische Raad", "en reeds bezig
met", "waardoor, indien deselve", "Ik ben gelast u daar van deze onderhandsche en voorlopige kennis te geven, met
verzoek, dat Gy den", "tot deszelfs ..."; grade M, eye-read at page resolution) with some cancelled groups. The
earlier passes transcribed only the first line (35 pairs) and called it the whole leaf-2 body. At this resolution the
top digits across the page look like 1-7 and the bottom digits like 1-4 throughout (grade M, not counted). The
structure -- each plaintext unit as a top digit 1-7 over a bottom digit 1-4, at most 28 cells, mixed with clear text --
fits a table- or grid-coordinate letter cipher better than any word code; that is a structural observation, not a
reading, and no key or alphabet was fitted.

Grade counts this step: H 0, C 0, S 0, M 0 readings (no plaintext claimed); the clear-text phrases quoted above are
M-grade eye reads of the open text, not decipherment. Requests: none (github.com shallow clone of dbourdeau/cyphersolver
1; all images already on disk). Vision: two reads of on-disk images by this worker, no subagent.

**Next step** (~$4-6, Usage 6 per-pass pricing) [x] done 2 Oct 2026 by A2-RAA2, see the step below -- 370 columns
transcribed in 14 lines; next is the cell-substitution test named there. Original text: cut line crops of leaf 2's right page with
`tools/iiif_lines.py --image images/209_leaf2.jpg --out images/crops209` and run two blind passes plus one
reconciliation to transcribe all ~14 cipher lines as (top, bottom) pairs; then test the stacked pairs as a 7x4 (or
smaller) cell substitution with the C3 control at the transcribed length.

## 2 Oct 2026 -- A2-RAA2: leaf 2 right page, all cipher lines transcribed from line crops (rule 2)

Intake gate, run before this step (`python3 tools/intake_gate_check.py na-raad-azie-1800`, exit 0):

    na-raad-azie-1800: open (line 1) -- edition/page or full-text-search citation found within 6 lines

**Crops.** `python3 tools/iiif_lines.py --image ciphers/na-raad-azie-1800/images/209_leaf2.jpg --out
ciphers/na-raad-azie-1800/images/crops209 --region 2360,480,2180,2060 --prefix l2r --centres
39,152,295,429,542,664,776,900,1030,1157,1279,1383,1500,1605,1686,1775,1886,1986 --debug` (centres by eye from the
row-ink profile: the autocorrelation split each stacked top/bottom pair into two lines). 18 bands, one segment each
(2180 px wide); overlay `images/crops209/l2r_lines_debug.jpg` checked. Cipher lines are L02-L13, L16 and L17 (14 crops);
L01, L14, L15 and L18 are clear Dutch only ("Behalven de u bekende en voor uw vertrek reeds", "Ik ben gelast u daar
van deze onderhandsche en", "voorlopige kennis te geven, met verzoek, dat Gy", "deszelfs ...").

**Passes.** Two blind Sonnet subagent passes (A, B), one call each over the 14 line crops only, neither shown the other's
file or any earlier transcription (their tool logs show reads of the 14 crops and nothing else). Compared with
`scripts/compare_l2_passes.py` (output `data/l2passes/compare.tsv`):

| | pass A | pass B | aligned | top digit agree | pair agree |
|---|---|---|---|---|---|
| cipher columns, 14 lines | 370 | 366 | 366 | 366 (100.0%) | 355 (97.0%) |

Disagreements fall in L09, L12, L13, L16 and L17 only, under the 10% Usage 6 threshold, so no third pass was run.
This worker settled all 15 from the crops (one reconciliation unit): pass A right 12 times (B had dropped a column
in L09, L12 and L13 and shifted the pairing in L16), pass B right twice (L17 columns 7 and 9). Two columns stay M:
L13 column 18 (top blotted, bottom 2) and L17 column 13 (1/4, a possible strike-through across this stretch).

**Result** -- `ciphertext_209_leaf2_full.tsv` (line, pos, col, top, bottom, kind, tr, note): **370 cipher columns**
in 14 lines (tr: A both passes agree 355, R settled from crop 13, M 2), plus 13 struck-through columns (kind x,
transcribed but low confidence), commas, one closing stop and 7 clear-text runs (kind w: "maar evenwel, zoo wy
hopen, eerlang"; "is de Asiatische"; "Raad"; "en reeds bezig met"; "waardoor, indien dezelve"; "den"; "tot"; eye-read,
M). Per line: L02 35, L03 30, L04 34, L05 7, L06 18, L07 15, L08 33, L09 29, L10 35, L11 20, L12 35, L13 19,
L16 29, L17 31.

Inventory (descriptive only, no key fitted): top digits 1-7 only, bottom digits 1-4 only, no 0, 8 or 9 anywhere;
24 of the 28 possible (top, bottom) cells occur (absent: 7/2, 7/3, 7/4, 1/3). Top counts 1:49 2:46 3:19 4:71 5:47
6:103 7:34 (?:1); bottom counts 1:166 2:86 3:62 4:56. Most frequent cells 6/1 85 (23.0%), 1/2 35, 7/1 34, 4/4 28,
5/3 26, 4/1 25, 2/3 20. A one-cell-per-letter design over a 24-letter period alphabet would show about this shape;
that is a structural observation, not a reading.

**Rule 2 corrections, logged.**
1. *Extent*: the cipher body of leaf 2 is 370 columns in 14 lines, not the single 35-column line on file since
   VX-CS06 (25 Sept 2026). `ciphertext_209_leaf2.tsv` (35 rows) is kept unchanged as that pass's record and is
   superseded by `ciphertext_209_leaf2_full.tsv`; the spec's `ciphertext` and `alphabet` fields are corrected in this
   commit to say so.
2. *Line 1 bottoms*: against the earlier file, L02 (its line 1) agrees on all 35 tops but both new passes, and this
   worker's crop check, differ in 8 bottom digits (positions 11, 13, 14, 25-29: the old file shifted the bottoms of
   the first group by one and left 14, 28, 29 blank, where the crop shows 1/1/1). The old T3 figure in the A2-RAA
   step (32/35 digit-annotated) becomes 35/35; T1 = 0 is unchanged, so that step's verdict stands.

Grade counts this step: no plaintext claimed (H 0, C 0, S 0, M 0, I 0); the transcription status counts above are
the per-column record. Vision: 2 Sonnet subagent passes (14 line crops each) + 1 reconciliation by this worker (5
crops) + 3 own reads (page overview, debug overlay, one crop). Requests: none (all images on disk).

**Next step** (~$3, breadth cap): run `tools/family_run.py` with the `masc` family on the 370 columns treated as
24-symbol cells (top*10+bottom), matched control first at N=370, K=24, Dutch -- but the repo's Dutch corpora are
`nl20` (Gutenberg, 1880s-1900s novels) and `nl_repo` (1624-25 Breda print), neither of the letter's 1800 date and
government-letter register (rule 3, era lesson): build or pick an era-matched c.1780-1820 Dutch corpus first (~$2,
V6-PTCORP took ~12 min), then run control and target. Leaf 3 (faint bleed-through, same cipher) stays untranscribed.

## 3 Oct 2026 -- A2-RAA3: masc family_run on the 370 leaf-2 cells (matched control first, rule 3)

Intake gate, run before this step (`python3 tools/intake_gate_check.py na-raad-azie-1800`, exit 0):

    na-raad-azie-1800: open (line 1) -- edition/page or full-text-search citation found within 6 lines

**Input.** `data/masc/cells_370.txt`, built from `ciphertext_209_leaf2_full.tsv` kind `c` rows only (struck `x`
columns, commas, clear words dropped), one manuscript line per text line, each cell written top*10+bottom ("61").
370 signs; K=25 because the one blotted-top M column (L13 col 18) stays its own sign `?2` rather than being guessed.

**Corpus.** No era-matched c.1780-1820 Dutch corpus exists in `tools/data` (nl20 = Gutenberg 1880s-1900s novels;
nl_dev = Statenvertaling 1637; nl_repo = 17th-century prints totalling about 8 KB, too small to train on). Per this
job's brief none was built; `nl20` used as is. Rule 3 era lesson: a FAIL or PASS here is conditional on that.

**Command** (`data/masc/run.log`):
`python3 tools/family_run.py specs/na-raad-azie-1800.json --family masc --cipher ciphers/na-raad-azie-1800/data/masc/cells_370.txt --tokens space --corpus tools/data/nl20 --seeds 3 --gate 0.6`

| run | N | K | recovery | best score |
|---|---|---|---|---|
| control seed 1 (nl20 window, held out) | 370 | 21 | 0.892 | -877.8 |
| control seed 2 | 370 | 21 | 0.922 | -811.7 |
| control seed 3 | 370 | 21 | 1.000 | -832.0 |
| **target** (seed 1, 8 restarts; top 3 restarts converge -866.0/-866.0/-866.8) | 370 | 25 | n/a | **-866.0** |
| target shuffled, seed 11 (`--shuffle-target`, same N/K/line lengths) | 370 | 25 | n/a | -1046.3 |
| target shuffled, seed 12 | 370 | 25 | n/a | -1053.7 |
| target shuffled, seed 13 | 370 | 25 | n/a | -1059.3 |

Control mean 0.938 (0.892-1.000) meets the 0.6 gate, so the target ran. Can the control differ from the target on
the statistic? Yes: the score is an n-gram log-likelihood of the best decode, which depends on sign order, and the
shuffled-target runs (order destroyed, counts kept) land about 180-190 points lower, so the statistic separates.
Caveat: the control window drew only K=21 distinct letters against the target's 25 signs.

**What it shows.** The cell sequence carries order structure that a letter-substitution model with an 1880s Dutch
n-gram scores like real Dutch prose: the target's -866.0 sits inside the control's true-key band (-811.7 to -877.8)
and well clear of its own shuffle floor (3 of 3). **The decode itself does not read** (`families/masc-1-nl20.txt`,
e.g. line L02 "deuroiekteerdeuermendindueneenkorus"); the solver's key sends three cells to e (61, 24, 44) and two
each to n, u, d, l, i.e. it used many-to-one freedom. So: a reproducible structural signal consistent with a
substitution of Dutch (homophones or a near-letter syllabary not excluded), not a reading. Grade counts: H 0, C 0,
S 0, M 0, I 0 -- no token is claimed. Not a negative either.

Not checked by this step: whether 6/1 (23.0% of cells) is a letter, a word divider or a null; homophonic family
with `--param profile=target`; any crib from the clear words interleaved in the lines ("is de Asiatische", "Raad").

Vision: 0. Requests: none (all local).

**Next step** (~$3, breadth cap): `tools/family_run.py --family homophonic --param profile=target` on the same
`data/masc/cells_370.txt` with nl20, control first, plus the same 3-seed `--shuffle-target` floor, and a 6/1-as-
divider variant (6/1 tokens rewritten as `.`). If either reads, a c.1800 Dutch corpus (~$2, V6-PTCORP's method) is
the next gate before any judge. Leaf 3 (faint, same cipher) stays untranscribed.
