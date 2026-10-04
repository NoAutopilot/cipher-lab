# George Lasry: open-access methods, read 27 Sept 2026

Sources searched (clock read `date -u` at start, 26 Sept 2026 23:53 UTC, session ran past midnight into
27 Sept 2026): OpenAlex author search (`A5008372044`, ORCID 0000-0002-0269-4793, University of
Kassel/Uppsala affiliation confirming this is the cryptologist, not a namesake) -- 30 works, 2 excluded as
homonyms (a 1979 finance note, a 1968 Aramaic philology paper, neither this author). CORE (`v3/search/works/`,
keyed) -- 1,028,730 raw hits for `authors:"George Lasry"` (a broad OR-style match on the whole corpus, not an
exact-author filter), read by relevance rank for cipher-related titles; found 7 items not in the OpenAlex set
(a 2018 PhD thesis and 6 HistoCrypt/Cryptologia-adjacent papers). HistoCrypt (`ecp.ep.liu.se`) tables of
contents for issues 15, 16, 17, 18, 49, 77 (the years with a Lasry OpenAlex hit plus their neighbours) grepped
for "Lasry": no title found beyond what OpenAlex/CORE already gave. de-crypt.org not queried (no Lasry-specific
public project page found in the time available; not a negative). Notes on open-access papers; no text
mirrored -- 8 PDFs were fetched to $SCRATCH (core.ac.uk, dspace.ut.ee bitstreams, ecp.ep.liu.se), read with
`pdfminer.six`, and deleted at the end of this job; nothing beyond notes and citations is in this repository.

Hosts and request counts: api.openalex.org 2, api.core.ac.uk 5, doi.org 4 (redirect resolution only),
dspace.ut.ee 11 (discovery search + bundle/bitstream API calls, 3 papers), ecp.ep.liu.se 9 (6 TOC pages + 3
PDF downloads), core.ac.uk 3 (1 succeeded, 2 returned `BlobNotFound` and were re-fetched from dspace.ut.ee
instead), tandfonline.com 1 (Cloudflare "Just a moment" challenge, stopped after one attempt per the
good-citizen rule, no retry). All requests one at a time, >=1.5s apart, descriptive UA.

Paper count: **35 rows** in `sources/lasry/PAPERS.tsv` (title, year, venue, doi, oa_url, oa_status, found_via).
**21 rows carry a free full-text URL** (OpenAlex `is_oa`/`best_oa_location`, or a CORE/dspace bitstream this
job resolved by hand). **8 papers read** (method + results sections, capped ~250 lines each after grep):
the 2018 PhD thesis, "Deciphering Historical Syllabic Ciphers" (2024), "An early French digit cipher... Duke of
Nevers (1592)" (2024), "Deciphering a Letter from the French Wars of Religion" (2022), "Deciphering a Short
Papal Cipher from 1721" (2022), "Armand de Bourbon's Poly-Homophonic Cipher – 1649" (2023), "What Encryption
Errors Can Reveal: Cross-Cipher Errors in Mary Queen of Scots' Letters" (2024), "Cryptanalytic and historical
challenges with unidentified encrypted documents from the early modern era" (2025). **2 papers abstract-only**
by choice ("Deciphering papal ciphers from the 16th to 18th Century" 2020, Cryptologia -- Cloudflare-blocked
PDF, OpenAlex abstract_inverted_index read instead; "Deciphering a Letter to Louis XIV... le Comte d'Avaux,
1684" 2021 -- ranked lower once the syllabic-ciphers paper's own citation of it, footnote 10, gave the same
fact: the d'Avaux key was recovered from a similar key, Lasry 2019). **24 papers not read at all**, marked
`abstract-only` or `unread-not-fetched` in PAPERS.tsv (machine ciphers -- Enigma, ADFGVX, Hagelin M-209,
Chaocipher, SIGABA, Playfair, Schlüsselgerät 41, Tunny; transposition; the ICDAR/CTTS/Location-Matters
transcription-tooling papers; a popular-press mirror of the Biafra article).

## Section 1: Papers

| Title | Year | Venue | URL | Cipher class | Method (one sentence) | Reported success | Our tool | Read |
|---|---|---|---|---|---|---|---|---|
| A Methodology for the Cryptanalysis of Classical Ciphers with Search Metaheuristics (PhD thesis) | 2018 | Kassel University Press | doi.org/10.19211/kup9783737604598 | general (transposition, homophonic, machine) | Simulated annealing / hill-climbing over key space, n-gram fitness scores, restarts; the source recipe cited by every later paper below | thesis-length synthesis of his machine and classical-cipher breaks (SIGABA, M-209, double transposition, Enigma, homophonic) | `homophonic_anneal.py`, `subst_hillclimb.py` (SA/hill-climb core) | method |
| Deciphering papal ciphers from the 16th to the 18th Century | 2020 | Cryptologia | doi.org/10.1080/01611194.2020.1755915 | homophonic, digit code groups, papal/Vatican nomenclature | Large corpus of Vatican ciphertexts transcribed; keys recovered with "novel cryptanalysis methods" + CrypTool; era split at 16th (sophisticated) vs 17th-18th (simpler) | "recovered most of the keys" across a large corpus (dozens of keys, hundreds of letters); no single N reported | `homophonic_anneal.py`, `family_run.py --family homophonic/nomenclator` | abstract |
| Deciphering a Short Papal Cipher from 1721 | 2022 | HistoCrypt (ecp.ep.liu.se) | ecp.ep.liu.se/.../401 | homophonic digit codes (1/2/4-digit groups, comma-separated, ASV Nunz. Colonia/5) | Standard trigram-SA failed on 198 groups/47 types; fixed by (a) era-matched Old Italian corpus, (b) 5-gram instead of 3-gram scoring, + manual completion of short words/prepositions | Most of key + plaintext recovered; nomenclature codes (9336/9485/9356) still unidentified; one Vatican challenge (part 5) remains unsolved | `family_run.py --family homophonic`, `italian16_corpus.py` | full |
| Deciphering a Letter from the French Wars of Religion | 2022 | HistoCrypt | ecp.ep.liu.se/.../402 | homophonic, 2-6 homophones/letter, BnF Colbert 500/33 f555 | Trigram-SA failed on 858 symbols/86 types (short + many types); 5-gram scoring gave partial confirmation; switching a generic French corpus for a **historical** French (Gutenberg) corpus + manual work gave a mostly-readable decode | Majority of ciphertext deciphered; some homophones/meanings still unresolved; encryption errors noted (T used for F in places) | `family_run.py --family homophonic`, `french16_ngram.py` | full |
| Armand de Bourbon's Poly-Homophonic Cipher – 1649 | 2023 | HistoCrypt | ecp.ep.liu.se/.../699 | novel "poly-homophonic" (mixes true homophony -- 2 symbols for one letter -- with **polyphony**, one symbol standing for >1 letter) | Standard homophonic SA output had >150 uncorrectable discrepancies; author diagnosed genuine polyphony (not a repaired key) from repeated, non-random errors and crib comparisons | Key + most of one letter deciphered; author states this is the only known example of a poly-homophonic design | none (design not modelled by any family_run.py family) | full |
| An early French digit cipher: deciphering a letter from the King of France to the Duke of Nevers (1592) | 2024 | HistoCrypt 2024 (Tartu DSpace) | dspace.ut.ee (bitstream db2fc9d2) | homophonic + nomenclature, continuous (unseparated) digit stream, BnF | Segmentation-first approach: tested fixed group length (failed), then a single null digit (failed), then variable-length groups distinguished by a leading marker digit (nomenclature groups start with `1`, are 3 digits; homophones are 2 digits, don't start with `1`) -- *then* ran Kopal 2019's ciphertext-only homophonic SA | Letter deciphered; original cipher table later located in a second BnF manuscript; names a sibling pool of >=23 digit-cipher letters to Nevers 1589-91 (BnF fr.3422/3614/3616/3623/3633/3634/3646) | none (no digit-stream segmentation-hypothesis-ladder tool of ours) | full |
| Deciphering Historical Syllabic Ciphers | 2024 | HistoCrypt 2024 (Tartu DSpace) | dspace.ut.ee (bitstream 75a7d17c) | syllabic (extends homophonic with CV/VC/CCV/CVC syllable symbols, regular or irregular diacritics, random or systematic word decomposition) | Extension of Kopal 2019 SA: **swap-only** moves (fixed homophone count per element, found more stable than variable-count schemes), 4-gram fitness over *decomposed vocabulary elements* (not raw letters) built from an assumed decomposition scheme, plus a semi-automated loop: the tool highlights plausible plaintext segments, cryptanalyst locks confirmed assignments as a "tentative key assignments" parameter, re-runs | 9 ciphers, 900-4,300 symbols / 101-219 types: decrypted-text accuracy 73-96% (35-86% at 1,000-symbol cap); author states "an initial accuracy of 40% or above is most often enough" to finish by hand; needed a 64-core/256GB machine for practical run times | `family_run.py --family syllabary`/`wordcode` (neither implements swap-only fixed-count moves, vocabulary-element n-grams, or the iterative human-lock loop) | full |
| What Encryption Errors Can Reveal: Cross-Cipher Errors in Mary Queen of Scots' Letters | 2024 | HistoCrypt 2024 (Tartu DSpace) | core.ac.uk/download/651258327.pdf | homophonic, multiple related keys used by the same scribe | Names and systematically surveys "cross-cipher errors" (CCEs): a scribe fluent in >1 cipher occasionally enciphers with the *wrong* key's symbol-to-letter mapping; CCEs are diagnosed by checking whether an "error" symbol matches a value in a *different, related* key the same office used, not by treating it as noise | Confirms 2+ additional ciphers implicated in Mary-to-Castelnau letters via this method; several CCEs were caught and corrected by the period scribe himself | none | full |
| Cryptanalytic and historical challenges with unidentified encrypted documents from the early modern era | 2025 | (Tartu DSpace, venue not fully confirmed -- likely HistoCrypt 2025) | dspace.ut.ee (item ac338631) | mixed, 3 16th-century case studies | Names 3 routes to an unidentified document: (1) find the original key already associated with the letters, (2) recover a key from an available decrypted text elsewhere, (3) reconstruct cryptanalytically; and 4 archival scenarios for where the key ends up relative to the letter (same box; with other keys; alone/unlabelled; lost). Route 1 is "a few minutes" once a candidate key/letter pair is in hand | 3 case studies identified/decrypted (dates given, not detailed further here); cites BnF fr.3349 as an example of an **unidentified** cipher key (probably 1580s) sitting beside uncoded Henri III/Catherine de Medici letters | `key_crossmatch.py` (already implements route 1 as "try every key on every ciphertext") | full |
| Antonio Elio "Cipher" and his Polyphonic-Syllabic Cipher | 2025 | venue not confirmed | core.ac.uk/download/663819864.pdf | polyphonic-syllabic (papal) | not read (ranked below the 8 above at this cap) | -- | -- | abstract-only-not-fetched (URL recorded, text not pulled) |
| Solving the Double Transposition Challenge with a Divide-and-Conquer Approach | 2014 | Cryptologia | doi.org/10.1080/01611194.2014.915269 | transposition (machine-era method paper) | not read | -- | -- | abstract-only (not fetched, paywalled, no OA link) |
| Deciphering ADFGVX messages from the Eastern Front of World War I | 2016 | Cryptologia | doi.org/10.1080/01611194.2016.1169461 | ADFGVX | not read | -- | -- | abstract-only |
| Deciphering Mary Stuart's lost letters from 1578-1584 | 2023 | Cryptologia | doi.org/10.1080/01611194.2022.2160677 | homophonic (period predecessor to the 2024 CCE paper) | read in full 4 Oct 2026: research/MARY-STUART-METHOD-2026-10-04.md (owner-supplied PDF, sources/papers/) | recovers several of Mary's letters to Castelnau, precursor to the CCE finding | -- | abstract-only |
| Cryptanalysis of columnar transposition cipher with long keys | 2016 | Cryptologia | doi.org/10.1080/01611194.2015.1087074 | transposition | not read | -- | -- | abstract-only |
| Automated Known-Plaintext Cryptanalysis of Short Hagelin M-209 Messages | 2015 | Cryptologia | doi.org/10.1080/01611194.2014.988370 | machine (M-209) | not read | -- | -- | abstract-only |
| Modern Cryptanalysis of Schlüsselgerät 41 | 2021 | HistoCrypt | ecp.ep.liu.se/.../163 | machine | not read | -- | -- | abstract-only |
| ICDAR 2024 Competition on Handwriting Recognition of Historical Ciphers | 2024 | LNCS | ddd.uab.cat/record/325042 | transcription tooling, not cryptanalysis | not read | -- | -- | abstract-only |
| Deciphering German diplomatic and naval attaché messages from 1900-1915 | 2020 | Cryptologia | doi.org/10.1080/01611194.2020.1755914 | machine-era diplomatic code | not read | -- | -- | abstract-only |
| Ciphertext-only cryptanalysis of Hagelin M-209 pins and lugs | 2015 | Cryptologia | doi.org/10.1080/01611194.2015.1028683 | machine (M-209) | not read | -- | -- | abstract-only |
| Cryptanalysis of Chaocipher and solution of Exhibit 6 | 2016 | Cryptologia | doi.org/10.1080/01611194.2015.1091797 | Chaocipher | not read | -- | -- | abstract-only |
| Ciphertext-only cryptanalysis of short Hagelin M-209 ciphertexts | 2018 | Cryptologia | doi.org/10.1080/01611194.2018.1428836 | machine (M-209) | not read | -- | -- | abstract-only |
| Solving a 40-Letter Playfair Challenge with CrypTool 2 | 2019 | (talk/writeup, no DOI) | -- | Playfair | not read | -- | -- | abstract-only-not-fetched |
| Analysis of a late 19th century french cipher created by Major Josse | 2022 | Cryptologia | doi.org/10.1080/01611194.2021.1996484 | homophonic/nomenclature, 19th c. French military | not read (ranked below the 16-17th c. set) | -- | -- | abstract-only |
| Cracking SIGABA in less than 24 hours on a consumer PC | 2021 | Cryptologia | doi.org/10.1080/01611194.2021.1989522 | machine (SIGABA) | not read | -- | -- | abstract-only |
| Cryptanalysis of Enigma double indicators with hill climbing | 2019 | Cryptologia | doi.org/10.1080/01611194.2018.1551253 | machine (Enigma) | not read | -- | -- | abstract-only |
| Solving a Tunny Challenge with Computerized "Testery" Methods | 2020 | HistoCrypt | ep.liu.se/ecp/171/014/ecp2020_171_014.pdf | machine (Lorenz/Tunny) | not read | -- | -- | abstract-only |
| Eavesdropping on the Biafra-Lisbon link – breaking historical ciphers from the Biafran war | 2020 | Cryptologia | doi.org/10.1080/01611194.2020.1762261 | machine-era (20th c.) code | not read | -- | -- | abstract-only |
| How we set new world records in breaking Playfair ciphertexts | 2021 | Cryptologia | doi.org/10.1080/01611194.2021.1905734 | Playfair | not read | -- | -- | abstract-only |
| Invited Talk - Special Session on Arne Beurling: Modern Codebreaking of T52 | 2018 | (talk, no DOI) | -- | machine (T52) | not read | -- | -- | abstract-only-not-fetched |
| Deciphering a Letter to Louis XIV from his Ambassador to the Dutch Republic, le Comte d'Avaux, 1684 | 2021 | HistoCrypt | ecp.ep.liu.se/.../162 | syllabic | not read in full; cited inside the 2024 syllabic-ciphers paper (its own footnote 10): key recovered from a similar known key, not cryptanalysis | recovery (key transplant), grade would be C/period not S | -- | abstract (via citation) |
| German World War I diplomatic and attaché codes – a revised study and the Dutch contribution | 2026 | Cryptologia | doi.org/10.1080/01611194.2026.2638191 | machine-era code | not read | -- | -- | abstract-only |
| CTTS – CrypTool Transcriber and Solver | 2026 | Tartu DSpace | dspace.ut.ee (bitstream 627d8d1f) | transcription tooling | not read | -- | -- | abstract-only-not-fetched |
| Location Matters: Accelerating Historical Cipher Transcription with Detection-Based Models | 2026 | Tartu DSpace | dspace.ut.ee (bitstream 0421bad3) | transcription tooling | not read | -- | -- | abstract-only-not-fetched |
| We decrypted messages from the Biafran war that have remained secret for 50 years | 2020 | popular-press mirror | (not resolved) | machine-era code | duplicate of the Cryptologia Biafra article above, popular framing | -- | -- | unread-not-fetched |

## Section 2: His approach (numbered practices, paper + page/section cited)

1. **Escalate n-gram order before concluding a cipher is unbreakable at this length.** Trigram scoring is his
   default; on two short, high-distinct-symbol-count homophonic ciphers (Papal 1721, sec. 3; French Wars of
   Religion, sec. 2) trigram-SA found nothing, 5-gram scoring on the same corpus found a partial confirmation.
   He treats "5-grams empirically most effective, 3 or 5 sometimes useful" as a per-target parameter to sweep,
   not a fixed setting (Syllabic Ciphers, sec. 4, "n-gram size").
2. **Era-matched corpus is not optional, it is the second lever after n-gram order.** Both the Papal 1721 paper
   (sec. 3, "Old Italian books instead of a generic Italian corpus") and the Wars of Religion paper (sec. 2,
   "French texts from a corpus of historical French books... instead of a generic French corpus") name the
   corpus swap, not a smarter algorithm, as what actually broke a short ciphertext after the vanilla SA failed.
3. **Fixed homophone-count swap-only moves, not variable reassignment.** For syllabic ciphers he restricts SA
   transformations to *swapping* two symbols' assignments (constant homophone count per vocabulary element)
   rather than allowing a symbol to be freely reassigned; found this "more stable and more effective" (Syllabic
   Ciphers, sec. 4). His homophonic-cipher papers (Papal 1721, Wars of Religion) instead allow both a swap *and*
   a single-homophone reassignment, with an explicit "maximum homophones per element" cap to keep the key
   balanced.
4. **Scoring is over decomposed vocabulary elements, not raw letters, for syllabic/nomenclature ciphers.**
   4-grams are computed over the assumed decomposition (letters + syllables + words), built ad hoc per target
   from reference texts parsed under the same decomposition scheme -- not pre-computed generic n-gram tables
   (Syllabic Ciphers, sec. 4).
5. **Semi-automated, human-in-the-loop iteration is the default workflow, not a fallback.** Every homophonic/
   syllabic paper here ends the automated stage well short of 100%: the tool highlights plausible decrypted
   segments and counts repeated correct-looking symbol occurrences, the cryptanalyst manually confirms/locks
   assignments, and the next SA run takes those as a "tentative key assignments" parameter (Syllabic Ciphers,
   sec. 4; also implicit in Papal 1721 sec. 2 and Wars of Religion sec. 2's "some manual processing").
6. **An explicit "good enough to finish by hand" accuracy threshold: ~40% initial decrypted-text accuracy**
   (Syllabic Ciphers, sec. 6). Below that, more compute or a design rethink; at or above it, manual completion
   is the stated next step, not further automated search.
7. **Segment continuous digit streams by hypothesis ladder, cheapest first.** For unseparated digit ciphers:
   try fixed group length -> try a single null digit -> try variable-length groups distinguished by a leading
   marker digit (a specific digit always starts the longer, nomenclature-length groups) -- each hypothesis
   tested by whether it makes segment lengths between cleartext anchors consistent, *before* any SA run
   (Nevers 1592, sec. 3).
8. **Transcription/encryption errors are graded, not just tolerated.** Where automated output has systematic,
   repeated "errors" that a single re-keying cannot fix (Armand de Bourbon, >150 discrepancies), he tests two
   specific alternative explanations before writing the passage off: (a) the design is not purely homophonic
   but **polyphonic** (one symbol standing for several plaintext letters) -- diagnosed from crib comparisons and
   the pattern of the errors; (b) the "error" symbol is a valid value in a **different key from the same
   office/scribe** used elsewhere ("cross-cipher error", CCE) -- diagnosed by checking the symbol against every
   other key the same correspondent/scribe is known to have used (Mary Stuart CCE paper, throughout).
9. **A result is "real" when cribs/context corroborate the SA output independently of the score:** period place
   names, common short words (il, ne, per), and a subsequent archival find of the actual key table are all used
   as confirmation, not the fitness score alone (Papal 1721 sec. 2; Nevers 1592 sec. 3, "later located the
   original cipher table in another BnF manuscript").
10. **Route order for an unidentified document, cheapest first**: find the key already paired with the letter
    (minutes, if archival scenario 1 holds) > recover a key from an available decrypted text elsewhere > full
    cryptanalytic reconstruction; and catalogue an archive's actual pairing scenario (same box / with other
    keys / alone and unlabelled / lost) before choosing which route to spend effort on (Unidentified Docs,
    sec. 3, "3.1 Finding the original cipher key in the archives").

## Section 3: What we do not do yet

1. **Escalating n-gram order per target (practice 1).**
   (c) tool option -- `homophonic_anneal.py` / `family_run.py --family homophonic` and `wordcode`/`syllabary`
   take a single scorer; add an `--param ngram=3|4|5` (or a small automatic sweep 3->5, stopping at the first
   order that breaks the control's own gate) rather than a fixed order per family. Name the option only, do not
   build it.
2. **Era-matched corpus before any run (practice 2).**
   (a) already in CLAUDE.md and in practice: rule 3's V6-PTCORP/MJ lessons and `tools/data`'s per-era corpora
   (fr16, fr18, it16, es17, es17c, pt17, pt18, ...) are exactly this discipline, cited already.
3. **Fixed-count swap-only moves for syllabic/nomenclature designs (practice 3).**
   (c) tool option -- `tools/families/syllabary.py` and `wordcode.py`: add a `--param moves=swap_only` that
   restricts the anneal to symbol-pair swaps (current behaviour, if it allows single-symbol reassignment,
   should be checked against this and offered as an alternative, not replaced outright without a control
   comparison on a held target). Name the option, do not build it.
4. **Vocabulary-element n-grams for decomposed syllabic ciphers (practice 4).**
   (b) brief addendum -- for `wordcode`/`syllabary` family runs, add a step to the family brief: "build the
   n-gram table over the assumed decomposition (letter/syllable/word units), from the spec's own corpus, not
   over raw letters" as a pre-flight step before the anneal, the way `key_design.py`/`design_prior.py` already
   build a structural signature before a family is chosen. Diff text (for `.claude/briefs/breadth.md` or a
   family-specific addendum): *"Before running `family_run.py --family wordcode` or `syllabary` on a target
   with CV/VC/CCV syllable symbols, confirm the family's n-gram table is built over the decomposed vocabulary
   (letters+syllables+words) implied by `--param codes=`, not over raw letters; if it is not, this is a known
   gap (LESSONS-LASRY.md, Section 3 item 4), not a silent design mismatch."*
5. **Semi-automated human-in-the-loop locking of tentative key assignments (practice 5).**
   (c)/(d) tool option and a named target -- `family_run.py` runs one shot per seed/restart and reports a
   control-gated verdict; it has no `--param lock=<tsv of confirmed symbol->element pairs>` to feed forward
   into a second run. This is the single largest gap relative to Lasry's own recipe, since every one of his
   syllabic/homophonic breaks in Section 1 above used this loop, not a single blind run. Untried step:
   **fr2933-salviati-1525** (code+mark/syllabic-like design, `partial`, NEAR.md row, LANE R8's own curve reads
   22-67% blind depending on error rate) -- an iterative lock-and-rerun pass, seeded from the highest-confidence
   symbol assignments of the existing blind run, is a genuinely different instrument from the single-shot
   `wordcode`/`syllabary` runs already tried and control-gated on this target; see the NEXT-STEPS line below.
6. **The ~40% initial-accuracy threshold as a stopping/continuing rule (practice 6).**
   (b) brief addendum -- name this figure explicitly as a checkpoint in any syllabic/nomenclature family brief:
   *"If a `wordcode`/`syllabary` run's token accuracy on the target reaches ~40% or higher, the named next step
   is a manual completion pass (crib-anchored, symbol-by-symbol), not a further automated restart; below 40%,
   a further automated attempt (different corpus, different n-gram order) is still the right next step."* Not
   a gate in the rule-3 sense (it does not license or void a control), a workflow checkpoint.
7. **Continuous-digit-stream segmentation ladder (practice 7).**
   (d) named target -- none of our currently open digit-cipher targets are pure continuous (unseparated) digit
   streams needing this ladder (the Nevers no.60 pool, fr3985/86/87/90, already has a known period key per
   Bourdeau/Tomokiyo; its blocker is glyph identification, not segmentation -- see fr3990's own NOTES.md,
   "Diagnosis: the blocker is identifying the signs, not the key"). Logged for the next continuous-digit target
   that has no known key.
8. **Cross-cipher errors as a diagnostic for "garbled" decode tokens (practice 8b).**
   (d) named target -- **matignon-mayenne-1586** (`partial`, NEAR.md row): its key.tsv carries 23 unkeyed ("+")
   codes per its own NOTES.md. Untried step: before treating these as unrecoverable, check each against every
   *other* key attested for the same office/correspondent cluster (Mayenne/Forget/Matignon-adjacent ciphers
   already in `KEY-OFFICES.tsv`) the way `key_crossmatch.py` already does target-to-key, but done code-by-code
   for the unkeyed residue rather than whole-cipher; cost band: cheap (a script pass over existing KEY-OFFICES
   rows, no new transcription). Cite: What Encryption Errors Can Reveal (Mary Stuart CCE paper), Section 3.
9. **Polyphony as an alternative design hypothesis when a homophonic decode has many uncorrectable errors
   (practice 8a).**
   (c) tool option -- no family in `tools/families/` models a symbol standing for more than one plaintext
   letter (polyphony proper, as opposed to homophony, more than one symbol per letter). Name as a future family
   (`polyphonic`) rather than build it; no target currently named as needing it (the one worked example,
   Armand de Bourbon's cipher, is not ours).
10. **Route order for unidentified/unkeyed documents (practice 10).**
    (a) already in CLAUDE.md and in a tool: `key_crossmatch.py` already implements "try every key on every
    ciphertext" (route 1); CLAUDE.md's Pipeline section 4 (access workers) and the Verifier brief already
    prioritise archival key-pairing search before cryptanalysis. Cited, not new.

NEXT-STEPS.tsv-shaped lines (folder, step, cost band, paper cited):
```
fr2933-salviati-1525	iterative lock-and-rerun pass on wordcode/syllabary family, seeded from the existing blind run's highest-confidence symbol assignments, matching Lasry's semi-automated loop (Section 3 item 5)	medium (needs family_run.py --param lock= support first, Section 3 item 5's tool option)	Deciphering Historical Syllabic Ciphers (2024)
matignon-mayenne-1586	check the 23 unkeyed ("+") codes in key.tsv against every other key in the same office cluster in KEY-OFFICES.tsv, code by code, before treating them as unrecoverable (cross-cipher-error diagnostic)	cheap (script pass, no new transcription)	What Encryption Errors Can Reveal: Cross-Cipher Errors in Mary Queen of Scots' Letters (2024)
```

Never claimed: no reading in this repository is called new, unpublished, unread, first, or never printed as a
result of this digest; this file only reports what Lasry's own papers say about his own methods and results.
