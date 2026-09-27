partial

INTAKE-SPINELLI, 27 Sept 2026: solver-ready intake (Layout, no cryptanalysis, no new reading, no class).
Built from KEY-ADJACENT.tsv row 5 (rank 6) and `sources/cryptiana/web/henryvii.htm`, read in full this job
(cp932-decoded per the file's own declared charset, not re-fetched -- already on disk).

# Beinecke Library (Yale), Spinelli Family Papers, GEN MSS 109, Filza 163

Beinecke record/OID 10844890 (the legacy vufind URL Tomokiyo links, `Record/3811294`, 302-redirects here);
fetched this job with `tools/browser_fetch.js` after a plain curl returned an empty 202. Sender and recipient
come from the record's own title (Italian, quoted in full in `images/manifest.json`): "Il Sig. Tommaso scrive
di Barcellona al Sig. Canonico Leonardo..." -- **Thomas ("Tommaso") Spinelli writing to his brother Leonardo
Spinelli, a canon**, dated **7 September 1519**, from Barcelona ("Barchenonia"), where Thomas was resident
ambassador to the Spanish court at the time (per `henryvii.htm`'s own biographical section above the
Spinelli-brothers note). Language Italian; call number GEN MSS 109; provenance "Purchase, 1988"; 3 digitised
canvases (p.[1], p.[2], p.[3: address leaf]) though the record's own title cites "4pp." -- not resolved this
job, see `images/manifest.json`'s note.

## Tomokiyo, verbatim

`henryvii.htm`, "Notes added in August 2018" (the passage this row's own KEY-ADJACENT.tsv sentence is drawn
from):

> "Ekaterina Domnina, "Ciphers in Early Tudor Diplomacy" in *Geheime Post* (2015) (updated pdf) focuses on
> Thomas Spinelly (Thommaso Spinelli in Italian), in particular his private correspondence with his younger
> brother Leonardo Spinelli in Florence or Rome. It was about 1515 that he introduced cipher in his private
> correspondence. In a letter of 3 January 1515, he asked his brother to use cipher to keep some information
> from their other brother, after which they used cipher frequently. (p.184) ..."
>
> "Spinelli brothers' cipher was a homophonic substitution cipher with some nulls (p.185, Fig.1), in which he
> frankly wrote, apart from private matters, critical comments on diplomatic proceedings and political
> figures (p.188-190)."
>
> "Spinelli's private correspondence is in Spinelli Family Papers, among which one letter in cipher is
> available online (Beinecke Digital Collections). (**Note in January 2024**: This particular letter can be
> deciphered with Spinelli brothers' cipher reconstructed by Domnina. Words "la gubernation d'ispagnia" can
> be read.)"

`henryvii.htm`, "Notes added in August 2023" (a separate, later addendum, presenting Tomokiyo's own
reconstruction of the same cipher, not a reproduction of Domnina's Fig.1):

> "Spinelly's cipher can be reconstructed as follows." [image: `spinelly1515.png`, the key of record below]

Tomokiyo does **not** print any reading of this letter beyond the one quoted phrase, "la gubernation
d'ispagnia" -- no transcription, no fuller decode, no image of the leaf with markup (contrast
`ciphers/fr4715-f61-mayenne-1592`, where Tomokiyo's own published image carries five short interlinear
spans). This matches Bourdeau's catalogue entry (already quoted in this row's own `in_repo` cell from
SCOUT-OWN-8, 27 Sept 2026): "Spinelli family private cipher letters (Beinecke Library, GEN MSS 109): Read in
part... Tomokiyo read part of the Beinecke letter online with it. The rest of Gen. MSS 109 has no published
reading."

## Gate verdict (Job 0, this job)

**Not found-solved. Continues to intake** (the same "partially read, most of the letter unread" bucket
`ciphers/fr4715-f61-mayenne-1592` used for the Mayenne cipher on BnF fr.4715 f.61, 27 Sept 2026 -- an existing
published crib is valuable material for a future worker, not grounds to retire the row when it falls short of
a full reading).

- **(a) `henryvii.htm`'s Spinelli passage, read in full this job**: prints only the one phrase, "la
  gubernation d'ispagnia", as evidence the letter "can be deciphered" -- no transcription, no fuller reading.
  Quoted above in full.
- **(b) Domnina's PDF (istina.msu.ru)**: **not fetchable this job**. The URL `henryvii.htm` links
  ("updated pdf", `istina.msu.ru/media/publications/article/a81/378/11992054/Domnina_Spinelli_cipher_
  EnglishRussian_-_kopiya.pdf`) returns a plain nginx 404 (this job's one allowed request to that host, per
  the good-citizen rule a 404 is not retried). Her Fig.1 (p.185), the cipher table this row's `key_location`
  cell names, and any fuller reading she may print, could **not** be checked this job -- an access gap, not
  a "no" answer. Flagged as the first thing a future worker with a working route to this PDF (a mirror, a
  different URL, a library route) should check before relying on this folder's key beyond calibration.
- **(c) the Beinecke record (OID 10844890) and its IIIF manifest**, read in full this job: no transcription
  or decipherment named anywhere in the record's own metadata (title, date, language, provenance, collection
  note, finding-aid link) or in the manifest's `metadata`/`seeAlso`/`rendering` fields. The Archives at Yale
  item-level finding-aid page the record links (`archives.yale.edu/repositories/11/archival_objects/2787659`)
  was **not** fetched this job -- a different host, out of this job's allowed network scope (brbl-dl.library.
  yale.edu / collections.library.yale.edu only); a future worker could check it.

No vision subagent call was needed for the gate itself -- the record's own text and metadata settled it, the
same way INTAKE-MC108 and INTAKE-4715-F61 settled their own gates from text plus a direct look.

## The key (key of record) -- with an important substitution flagged

`keys/key_spinelli_c1515.tsv`, transcribed from `spinelly1515.png`, embedded in `henryvii.htm`'s "Notes added
in August 2023" section (quoted above). **This is Tomokiyo's own independent reconstruction of the cipher,
not Domnina's Fig.1 itself** -- her PDF being unreachable this job (gate item (b) above) meant her actual
table image could not be fetched or cross-checked. Tomokiyo's own page treats the two as the same cipher
(the January 2024 note explicitly credits "Spinelli brothers' cipher reconstructed by Domnina" as what makes
the online letter readable, and the August 2023 table is presented on the same page as his own reconstruction
of "Spinelly's cipher" -- singular, no indication of a second, different cipher), but this has not been
independently verified against Domnina's own Fig.1 this job. The same substitution was already precedented
this same day: `ciphers/fr4715-f61-mayenne-1592` used Tomokiyo's own `mayenne.png` table rather than any
period original, for the same reason (it was what was actually published and fetchable).

Design, from this worker's own careful transcription (not stated in prose anywhere on `henryvii.htm` --
see the key file's own header comment for the full method): 23 plaintext-letter columns (a b c d e f g h i k
l m n o p q r s t u x y z, the period Italian/Latin set omitting j, v, w). **Three columns (q, x, z) are
blank** -- no symbol drawn in this reconstruction, confirmed by this worker's own 4x zoomed crop of each
(not a transcription gap; genuinely no ink in the source image). **Five columns (d, i, l, n, t) carry two
stacked symbols each** -- homophones for that one letter (not a letter-PAIR the way the Mayenne table in
`ciphers/fr4715-f61-mayenne-1592` stacks two different letters per column; flagged so the two are not
confused). The other 15 non-blank columns carry one symbol each. A block of **12 null symbols** (this
worker's own crop-based count; both blind Sonnet subagent reads independently reported 10 and 11 and both
explicitly flagged their own count as uncertain -- the 12 is this worker's careful recount from a 6x zoomed
crop, not an average of the two guesses) and **5 word-code entries** ("I", "of", "Emperor King of Arragon",
"Prince of Castile", "new amity") round out the table. Total hand-drawn symbols: 15 + 10 + 12 + 5 = 42.

Transcription method: two independent blind Sonnet subagent reads (2 of this job's 4 allowed vision calls),
each shown only the image and the table's own printed column headers, asked for a literal ink-shape
description per cell with no letter-guessing beyond what the image's own printed labels already give. Both
passes read the first several columns (a-p) reasonably consistently but had low confidence or missed marks
entirely from column q onward, disagreed on the null count, and did not reliably catch the five stacked
homophone columns. This worker settled every cell with its own zoomed/cropped re-examination (column x-ranges
located mechanically from the header row's own white-pixel runs, not eyeballed), which is what actually
resolved the blank columns, the homophone stacking, and the null count -- recorded per-row in the key file
with grade AB (blind passes agreed, crop confirms) / M (blind passes disagreed or missed it, crop settled
it) / ? (one null symbol, an irregularly-placed 12th mark neither blind pass reported at all, whose exact
place in the table's intended grid stays unresolved even after the crop). Grade counts: **23 AB / 21 M / 1
?** (45 rows total).

## The target leaf

`images/manifest.json`: IIIF Presentation API 3.0 manifest, `collections.library.yale.edu/manifests/
10844890`, 3 canvases at 3577x4997 native resolution. Page 1 (canvas 10867298) fetched this job at 1500px
width (`images/beinecke3811294_p1_canvas10867298.jpg`). A direct look at this image (no vision subagent call
needed) shows the catalogue's "4pp. part in cipher" is literally true of this one page: roughly the top 9
written lines are continuous hand-drawn cipher symbols (several shapes visibly resemble this folder's own key
table on sight -- a pi-like mark, a w/omega-like double-hump mark, an H-like ladder mark, numeral-like marks
-- promising for calibration), with a few plain words at the very top ("Scrissi un'altra..."), then the text
switches to plain Italian prose from "L'amorte del Car[dinale]..." onward. Pages 2 and 3 (address leaf) were
not fetched this job (out of this job's cost/time budget; next worker's first step per "What remains" below).
No transcription or decoding attempted this job -- out of scope for an intake job, per the fr61/3251/mc108
pattern.

## Check-solved header (not a formal `.claude/briefs/check-solved.md` pass -- see "What remains")

- `henryvii.htm`'s Spinelli passage read and quoted in full above; prints only the one phrase, no fuller
  reading.
- `KEY-ADJACENT.tsv` row 5's own `in_repo` cell already records a solver-repository grep (SCOUT-OWN-8, 27
  Sept 2026, quoting Bourdeau's catalogue entry 306 in full) -- not re-run this job (GitHub was not in this
  job's allowed network scope).
- `CATALOG.md` and `LESSONS-LASRY.md` grepped this job (offline, already on disk) for "Spinelli"/"spinelly":
  no row for this item in either.
- No full-text/phrase search run this job (out of scope for an intake job; a phrase search on "la gubernation
  d'ispagnia" is the kind of check rule 10 and `tools/print_check.py` are for, once/if a fuller reading
  exists -- Tomokiyo's own one phrase would not be novel to us either way, and this job made no reading
  claim of its own to search for).
- The Beinecke record and its IIIF manifest metadata read in full this job (gate item (c) above): no
  transcription or decipherment named.

What remains before any class (rule 10) or any deep-work brief:
- Domnina's PDF itself, unreachable this job (gate item (b)) -- a future worker with a working route (a
  mirror, a different URL at istina.msu.ru, a library database) should fetch it, read her p.185 Fig.1 and
  p.188-190, and cross-check this folder's Tomokiyo-sourced key against her original before trusting it
  beyond calibration.
- The Archives at Yale item-level finding-aid page (`archives.yale.edu/repositories/11/archival_objects/
  2787659`) -- a different host, not checked this job (out of allowed network scope).
- Pages 2 and 3 (address leaf) of the Beinecke letter, not fetched this job.
- A formal `.claude/briefs/check-solved.md` pass proper; `tools/intake_gate_check.py spinelli-beinecke-c1515`
  run once below.
- Once any reading exists: `tools/print_check.py` on the decoded phrases (rule 10).

**Next step:** locate "la gubernation d'ispagnia" on the image (Tomokiyo's own known-answer span, the "known
answer first" discipline in `.claude/briefs/README.md`'s common tail) and calibrate `keys/
key_spinelli_c1515.tsv` against it -- likely on page 2 or 3, since the phrase was not obviously visible in
this job's direct look at page 1's cipher lines, though it was not searched for systematically. Then two
blind passes on the whole letter (all 3 canvases) and a 20-shuffled-key control (rule 3); reading to a
verifier. Given the three blank letter columns (q, x, z) and five homophone columns already known from this
transcription, a calibration pass should also try to resolve q/x/z (do they appear in the plaintext at all
within this one short business/family letter, making their absence unsurprising, or does the source material
Tomokiyo drew on for the reconstruction simply not attest them yet).

**Requests this job:** cryptiana.web.fc2.com 1 (`spinelly1515.png`; `henryvii.htm` itself already on disk,
no re-fetch needed). istina.msu.ru 1 (Domnina's PDF, 404 -- see gate item (b); not retried, per the
good-citizen rule). brbl-dl.library.yale.edu 1 (initial vufind Record URL, 302 redirect to
collections.library.yale.edu, empty body); collections.library.yale.edu 3 (1 browser-rendered catalog page,
1 IIIF manifest JSON, 1 page-1 image at 1500px) -- 4 of the allowed 6 combined for that host pair, 2s apart,
descriptive/browser user agent per the brief. No other hosts. No credentials. No AskUserQuestion. No
novelty/first/unpublished wording (rule 10) -- Tomokiyo's own one phrase is credited to him throughout, not
claimed as ours; Domnina's cipher reconstruction is credited to her by name even though her own PDF could not
itself be read this job.
