# LANE OX triage: 12 orphaned open copy-free-ish targets, 25 September 2026

OX-TRIAGE (Sonnet, session_01GA7gH4LMd4Hyi5yLHAyjQx). Disk-only pass: read each target's NOTES.md, its QUEUE.md
row(s), REQUEST.md/images where present, LESSONS.md sections 1-2, no fetching of any external host. Rule 10:
report only what was found and where it was not found; no novelty wording; the verifier classifies novelty, not
this worker. None of the twelve is found-solved on disk -- every NOTES.md's status line reads `open`.

---

## hellen-frederick-1752

**On disk:** 0 images. No ciphertext transcription, no key files. NOTES.md is a check-solved search log only
(LANE N4 csNA, 24 Sept 2026).

**Route: recovery**, for one of the eight ciphertexts only. NA (Nationaal Archief) 1.10.29 Fagel inv. 5206,
**185 page scans, digitised, no login**, titled "Afschriften van ontcijferde brieven..." (copies of
**deciphered** letters) for foreign envoys' despatches, dated range 1752-1753 -- confirmed by NOTES.md to be
genuine clear-French prose by an eyeballed thumbnail, not a re-copy of cipher. This window (1752-53) covers only
**R1953 (4 Jan 1752)** of the eight target ciphertexts (KHA Prins Willem V inv. 196); the 1756 letter (R1049)
and the six 1763 letters (R1045-R1048, R1060, R1061) fall outside inv. 5206's date range, and Bourdeau/De Leeuw
are cited stating "no Prussian codes broken between April 1757 and October 1763" -- structural reason not to
expect a decipherment for the later cluster anywhere.

**Expected value:** P(first cheap test moves it) high for R1953 specifically -- the decipherment series is
already located, copy-free, and the task is page-by-page date matching, not fresh cryptanalysis. Value is
partial (1 of 8 ciphertexts). Cost low (no login, IIIF/thumbnail access already proven reachable).
**Score: 7/10.**

**First step:** fetch NA Fagel inv. 5206's 185 page images/thumbnails and scan for a 4 January 1752 dateline or
"Von Hellen"/"Sieur H" heading matching R1953's content; no transcription needed until a match is found. Cap
**$4**, no prior transcription required.

---

## breda-statengeneraal-1624-25

**On disk:** 1 image (`images/statengeneraal_07_GS223_100.jpg`, the printed *Resolutiën* register page --
the summary only, never the ciphertext itself). No ciphertext, no key. `REQUEST.md` present.

**Route: blocked**, on two fronts. (1) NA 1.01.02 invnr 4945 ("S.G. 4945 I") is `availability:PHYSICAL,
scans:[]` -- not digitised, a copy order is the only route to the manuscript. (2) A specific unread print lead:
the same resolution's footnote apparatus cites "Van der Kemp IV p.391" as printing a *different* part of the
same resolution (Maurits' letter) -- Deel IV of C.M. van der Kemp's *Maurits van Nassau, Prins van Oranje* was
never located or opened this pass (not on DBNL; Google Books/archive.org were out of scope for the worker that
found this). CLAUDE.md's own Torpadie/Thurloe lesson says exactly this kind of adjacent-footnote print lead must
be checked before outreach.

**Expected value:** the Van der Kemp IV check is a genuine cheap test that could close the row (if it prints the
cipher passage, this becomes found-solved or at least edition-risk-resolved) or clear it for a copy order (if
it doesn't). Value is moderate (a full near-total cipher letter, "including the day in the date" per the
register), cost low if HathiTrust/library catalogue access works. **Score: 5/10.**

**First step:** locate and read C.M. van der Kemp, *Maurits van Nassau, Prins van Oranje*, Deel IV, p.391 and
surrounding pages, via HathiTrust or a library catalogue, to confirm it does not also print or discuss the
Breda magistrate's cipher letter. Cap **$3**, no transcription needed.

---

## clairambault1225-paget-1714

**On disk:** images folder has 2 files, both wrong guesses (canvas 48 = an unrelated 18th-c. religious-
community letter; canvas 54 = a mounted engraved portrait, not saved). Folio 48 (BnF finding-aid citation,
"Fol. 48 -- ... lettres autogr. de Paget, avec chiffre, 1714") has **not been located** in this 268-leaf,
non-sequential "Melanges" volume. No ciphertext.

**Route: cryptanalysis**, blocked purely on locating the folio, not on copy status -- Gallica
`ark:/12148/btv1b9001034d` is copy-free, public domain, no login. Gallica's own ContentSearch OCR index
returned zero hits for "Paget" (the volume is not machine-OCR'd), so a systematic canvas-index bracket search
is needed instead of text search. A named tool exists for exactly this in CLAUDE.md's Access playbook,
`tools/gallica_folio.py ARK --folio N`, which reads the manifest's canvas labels once and reports offset
changes -- not yet run against this ark. A sibling lead also exists: QUEUE row M26, Clairambault 296-299
("Lettre en partie chiffrée de Paget," 14 Jan 1713, a different shelfmark, check-solved open) -- a second,
distinct Paget cipher letter about a year earlier, useful as a design comparison once both are imaged, not a
duplicate.

**Expected value:** cheap, copy-free, tool already exists for this exact problem. Value depends on what the
folio turns out to hold (plural "lettres chiffrées" per the BnF name-index -- could be more than one letter).
**Score: 6/10.**

**First step:** run `tools/gallica_folio.py ark:/12148/btv1b9001034d --folio 48` to map the finding-aid's
citation to the correct canvas index, then fetch that canvas. Cap **$3**, transcription is a follow-on step
once located.

---

## vaudemont-willemiii-1699

**On disk:** images 2 files (`willemiii_ks24_0812.jpg`, the printed edition's own alphabetical letter-index
page -- not the target letter, which is held at Nottingham). No ciphertext.

**Route: recovery.** The edition's own index states the 25 March 1699 letter is "grootendeels in onopgelost
cijferschrift" (mostly unsolved cipher) but adds "ook een ontcijferde brief is aanwezig" (a deciphered letter
is ALSO present) in the same correspondent run -- and the same index page carries **at least 20 further
asterisked (cipher-marked) entries across 1695-1701** for the same Vaudemont/Bentinck circle, none individually
read yet. Identifying which entry is "the deciphered letter" is a known-plaintext-pairing lead (LESSONS.md's
strongest class) once found.

**Expected value:** the identification step itself needs no archive visit -- the printed edition
(`resources.huygens.knaw.nl/retroboeken/willemiii`) is copy-free, no login, already the source in hand. Only
if a specific enciphered *original* is then wanted does the Nottingham copy-order block apply (the target
25 March letter itself is copy-order, per CLAUDE.md's standing note that Portland/Bentinck papers are not
digitised). **Score: 7/10.**

**First step:** read the ~20 further asterisked entries in the same Vaudemont/Bentinck alphabetical index
(1695-1701) in the printed edition to find and date the "ontcijferde brief," then compare its noted subject
against 25 March 1699's own content. Cap **$3**, no transcription, no archive access needed for this step.

---

## willem-van-hessen-1567

**On disk:** images 3 files (`01127_p1-1.png` etc., the draft/minuut's address leaf, confirmed by eye). Draft
is copy-free (free PDF, `resources.huygens.knaw.nl/media/wvo/images/01000-01999/01127.pdf`) and WVO's own
curators state it "geeft de complete tekst" (gives the complete text) -- a crib, if the draft and the enciphered
original passage cover the same wording (not yet confirmed; a "minuut" can be an earlier compositional stage).
The **original**, where the cipher sits (Koninklijk Huisarchief Den Haag, A 11/XIV B/15-43), has no PDF in WVO
-- `REQUEST.md` written.

**Route: recovery/cryptanalysis (crib).** A csWV3 pass across all 73 un-nominated WVO cipher letters (24 Sept
2026) found **two further Willem van Hessen letters in the same correspondent circle, neither fetched or
imaged**: briefnr **174** (9 Apr 1567, WVO remark "solved on leaf" -- a contemporary decipherment accompanies
the manuscript) and briefnr **1069** (23 Mar 1563, WVO remark "bij het origineel een exemplaar in cijferschrift
en met ontcijfering" -- a cipher copy WITH a decipherment beside the original). Both are flagged only as leads
for "LANE R3" as possible key sources for the same office/correspondent's cipher design; their own copy status
(PDF availability) was never checked.

**Expected value:** two already-solved same-correspondent instances in the identical circle as the target,
never even fetched -- if either is copy-free, this is the single cheapest recovery lever in this batch: a
same-office key candidate with zero cryptanalysis required, only alignment. **Score: 8/10.**

**First step:** fetch WVO briefnr 174 and 1069 detail pages, check PDF availability, and if free, download and
image both, since 174's "solved on leaf" language suggests the decipherment is on the manuscript itself. Cap
**$3**.

---

## vanbeuningen-dewitt-1657

**On disk:** images 2 files (`dewitt_01_405.jpg`, the printed *Brieven aan Johan de Witt* page -- gives the
**plain text of the letter itself**, a copy in an unidentified hand). No ciphertext image.

**Route: recovery -- the strongest single lead in this batch.** The edition's own footnote states plainly:
"Dezelfde brief ook in onopgelost cijfer, van een andere hand" (the same letter also survives in unsolved
cipher, in another hand) -- i.e. **known plaintext already in hand** (not merely a sibling letter, the exact
same letter), the strongest lead class named in LESSONS.md. NA 3.01.17 ("Inventaris... Johan de Witt") is
confirmed as the correct archive two independent ways (the edition's own front matter; EMLO's project page),
but the **specific inv.nr for the cipher copy was not resolved** -- EMLO's advanced-search React form did not
actually filter on guessed parameter names, and NA's own `zvt`/`hub3` search API endpoints returned 503/404 on
guessed paths.

**Expected value:** highest in this batch. Value is very high (a genuine known-plaintext pairing, likely a
quick key recovery once the cipher copy is located and imaged, versus a from-scratch cryptanalysis for
everything else here); cost is a search/lookup task, not an archive visit, assuming the item turns out
digitised via EMLO once found (unconfirmed -- EMLO's own caveat is that its manuscript images are "provisional,
lower-quality" where available at all). **Score: 9/10.**

**First step:** drive EMLO's advanced-search form interactively (`tools/browser_fetch.js --type/--selector`,
not guessed query parameters) for sender "Van Beuningen" / date September 1657 / or find NA's real search API,
to pin the specific inv.nr of the cipher copy "van een andere hand." Cap **$4**, no transcription until located.

---

## Heinsius circle: borssele-heinsius-1714, heinsius-dopff-1702, heinsius-hermitage-1704, heinsius-vanhaersolte-1703, rumpf-vandebie-heinsius-1716-19

All five are letters within the Anthonie Heinsius correspondence archive, **NA 3.01.19**. A dedicated check for
a shared office key (per this brief's instruction):

**The archive holds a three-item "2.4.10 Cijferschrift" subsection at the very end of the Heinsius series**
(found by heinsius-hermitage-1704's csHU2 pass): invnrs **2315** ("Stukken betreffende cijfers en sleutels van
cijferschrift" -- general miscellany, could hold more than one system, never individually examined), **2316**
("Cijfer voor de het cijferschrift met P. Battier" -- a named correspondent not in this batch, ruled out), and
**2317** ("Sleutel van een cijferschrift, waarschijnlijk voor correspondentie met Engeland," c.1705 -- candidate
for the London-based correspondent). **All three, like every H.A. number checked in this circle, are
`availability:PHYSICAL, scans:[]` -- not digitised. No key for any of these five letters is published,
decrypted, or on disk anywhere in this repository; 2317 is an unconfirmed candidate, not a recovered key.**

Per-target fit for 2317 and for each other:
- **heinsius-hermitage-1704** (HU2: letters 166/177/477, H.A. 946, 1704; HU10: letter 1231, H.A. 1034, 1705,
  same correspondent Sauniere de l'Hermitage, London) -- **best fit for 2317** (London correspondent, 1705
  date closer to 1034 than to 946) but still the editor's own "waarschijnlijk" (probably), unconfirmed. HU2's
  three letters and HU10's one letter are the **same correspondent circle and plausibly the same cipher
  system** (the editor cross-references 166/177 to each other directly) -- the strongest "one key serves
  several" candidate in this group, contingent entirely on an archive visit to compare H.A. 946 and H.A. 1034
  side by side (never done) and to photograph 2317.
- **heinsius-dopff-1702** (letter 357, H.A. 756, 1702) -- 2317 does not fit (dated ~1705, England-specific,
  Dopff's letter concerns Prussia/William III's inheritance, not England). 2315 (general miscellany) not
  examined. Only ten repeating name-codes, likely below unicity distance alone.
- **heinsius-vanhaersolte-1703** (letter 341, H.A. 841, 1703, Warsaw) -- 2317 explicitly does not fit
  ("waarschijnlijk voor correspondentie met Engeland," not Poland); 2315 flagged as the more plausible lead but
  not examined. Only two ciphertext tokens (178, 198), each appearing once -- the weakest single instance in
  this whole batch, well below unicity distance without a sibling.
- **borssele-heinsius-1714** (letter 959, H.A. 1836, London) -- a *different*, dossier-local lead: the editor's
  own footnote states a decipherment ("mogelijk dezelfde," possibly the same) is physically present **on the
  same leaf** as the unsolved cipher letter -- not linked to 2317 (dated c.1705, nine years earlier) by any
  worker so far. One photograph of H.A. 1836 either resolves this to found-solved or turns it into a genuine
  sibling-recovery case; this is not a "cheap test" in the web sense (physical-only archive), but it is the
  single highest-value archive visit in the whole Heinsius circle since it could close the item outright.
- **rumpf-vandebie-heinsius-1716-19** (letters 142/309/446/455, H.A. 1975/2030/2044, 1716-19, Rotterdam then
  Stockholm) -- a different region (Sweden) and different decade from 2317's England/~1705 fit; not linked. This
  is also the one target in this circle with a genuine cryptanalysis attempt already run: letter 142's
  ciphertext is fully printed (`ciphertext_142.tsv`, 208 tokens, 64 distinct values), and LANE R2 worker H1
  (Opus) ran a matched-control homophonic-substitution test -- **negative but weak** (control read 29-71%
  depending on seed, mean ~54%, itself only partial at this length/K; target read 0% recognisable, best score
  matching the control's noise floor). A loose namesake lead, NA 1.10.29 Fagel inv. 5345 ("cipher van Rumpf
  1743," DECODE id 2818), is a different archive series and 24-27 years later -- unconfirmed same person,
  flagged only as worth one look.

**Expected value, per target:**
- heinsius-hermitage-1704: value high (candidate key + likely-shared system across two letter batches), but
  cost is an archive visit (not digitised) -- **score 5/10**, flagged as the Heinsius circle's top REQUEST.md
  priority for the person, not a worker's cheap web test.
- borssele-heinsius-1714: value very high if resolved (either closes the item or confirms a sibling), cost is
  one archive photograph -- **score 5/10**, same reasoning, arguably the single most decisive individual leaf
  in this circle.
- heinsius-dopff-1702: **score 3/10** (below unicity distance alone, no key fit found).
- heinsius-vanhaersolte-1703: **score 2/10**, the weakest item in this entire triage (two tokens, no key fit).
- rumpf-vandebie-heinsius-1716-19: **score 3/10** (one instance already cryptanalysed to a weak negative; further
  progress needs archive copies of 309/446/455, not a cheap test).

**First step for the circle as a whole:** none of the five has an available cheap web test left to run --
every candidate key and every uncompared leaf sits behind NA 3.01.19's undigitised "2.4.10 Cijferschrift"
subsection and the individual H.A. numbers. The actionable next step is consolidating the REQUEST.md asks
already written per-target (946+1034+2317 together for Hermitage; 1836 alone for Borssele; 2315 examined
alongside Dopff's and Van Haersolte's own H.A. numbers) into one archive-visit ask to the person, prioritising
H.A. 1836 (Borssele) first since one photograph there resolves the item outright, then 946/1034/2317 together
(Hermitage). No dollar cap applies to a REQUEST.md consolidation; if run as a worker task, cap **$2**
(read-and-merge only, no new search).

---

## la-garde-1577

**On disk:** the most heavily worked target in this batch by far -- 13 image files, plus four completed
transcription/cryptanalysis passes (L1-L4) already on disk with scripts (`solve_l2.py`, `build_v2.py`,
`freq.py`, `reindex_l1.py`), `images/manifest.json`, `images/inventory.tsv`.

**Route: cryptanalysis, already run twice with matched controls -- negative both times.** L2 (Opus) and L4
(Sonnet, reconciled v2 transcription with overlines as distinct signs) both tested homophonic/simple
substitution and periodic Vigenère/Beaufort (periods 1-14) against a matched control of the same N and sign
count (contemporary 1580 French letter prose, not this letter's own clear text, which is not on disk). Every
control reads cleanly (73-100%); the target never beats its own noisy (8%-misreading) control in any test, in
either overline-folded or overline-as-distinct-sign mode. A crib test (6467's own marginal note against its
adjacent 27-sign cipher run) found no consistent sign-to-letter map. This is a genuine control-backed negative
per rule 3, not merely "no reading" -- the status line still reads `open`, not `closed-negative`; relabelling is
the orchestrator's call, not this worker's.

**Expected value:** low for repeating the same design tests. Two cheap, not-yet-tried levers remain, both
flagged by L2/L4 themselves: (1) the 9 still-unresolved transcription cells (single-digit disputes, image-only,
need a crop tool) -- flagged as not expected to change the negative's shape; (2) the printed editions GSME/LMSAC
already cited in WVO's own record for briefnr 6467 (Marnix, same date/region, whose margin carries "a solution")
were never located or read -- if either is a nomenclator table rather than a narrative edition, it could supply
an actual key for this cipher family, not just another crib. **Score: 3/10** (four worker-passes deep already;
this is a genuine control-backed negative on the two most obvious designs, not an unexplored target).

**First step:** locate and read the GSME/LMSAC printed editions cited in WVO briefnr 6467's own Brongegevens
field, checking specifically for a cipher/nomenclator table rather than narrative text. Cap **$3**.

---

## Ranked table

| rank | target | route | EV score | first step | cap |
|---|---|---|---|---|---|
| 1 | vanbeuningen-dewitt-1657 | recovery (known plaintext in hand) | 9 | drive EMLO's search form interactively / find NA's search API to pin the cipher copy's inv.nr | $4 |
| 2 | willem-van-hessen-1567 | recovery/cryptanalysis (crib) | 8 | fetch WVO briefnr 174 and 1069, check PDF availability | $3 |
| 3 | vaudemont-willemiii-1699 | recovery | 7 | read the ~20 further asterisked Vaudemont index entries (copy-free edition) for the dated sibling | $3 |
| 3 | hellen-frederick-1752 | recovery (1 of 8 ciphertexts) | 7 | page through NA Fagel inv. 5206's 185 scans for the 4 Jan 1752 match | $4 |
| 5 | clairambault1225-paget-1714 | cryptanalysis (folio unlocated) | 6 | `tools/gallica_folio.py` bracket search to pin folio 48 | $3 |
| 6 | breda-statengeneraal-1624-25 | blocked (copy-order + unread print lead) | 5 | read Van der Kemp IV p.391 (HathiTrust) | $3 |
| 6 | heinsius-hermitage-1704 | recovery (candidate key, archive-only) | 5 | consolidate REQUEST.md: 946+1034+2317 together | archive visit |
| 6 | borssele-heinsius-1714 | recovery (ambiguous, archive-only) | 5 | photograph H.A. 1836 | archive visit |
| 9 | la-garde-1577 | cryptanalysis (control-backed negative x2) | 3 | locate GSME/LMSAC printed editions for briefnr 6467 | $3 |
| 9 | heinsius-dopff-1702 | cryptanalysis (below unicity distance) | 3 | none cheap; archive-only | archive visit |
| 9 | rumpf-vandebie-heinsius-1716-19 | cryptanalysis (one instance already negative) | 3 | none cheap; archive copies of 309/446/455 | archive visit |
| 12 | heinsius-vanhaersolte-1703 | cryptanalysis (2 tokens, no key fit) | 2 | none cheap; archive-only | archive visit |

**TOP THREE: vanbeuningen-dewitt-1657, willem-van-hessen-1567, vaudemont-willemiii-1699** -- all three share the
same shape: a same-correspondent or same-letter sibling with a stated decipherment already exists, the
identifying step is copy-free (a printed edition already in hand or a form-search, not a physical archive
visit), and none needs fresh cryptanalysis to make progress.

Inferred/uncertain calls in this file, flagged per target above rather than restated here: the Henry Paget
identification (clairambault1225), 2317's fit to Hermitage vs. the rest of the Heinsius circle, and every "not
yet examined" 2315/174/1069 lead are inferences from adjacent evidence, not confirmed matches.
