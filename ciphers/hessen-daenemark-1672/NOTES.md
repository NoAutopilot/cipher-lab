partial
Bourdeau CATALOGUE.md #341 (fresh shallow clone, HEAD fc0c9e865d0fae67ca92d19750d2b09ab11972e0, read 26 Sept 2026) read in full: "Hesse-Kassel and Denmark, letter with enciphered passages (partly solved on HCPortal): unknown -> unknown ... HCPortal: 'Partially solved'; three images online. What part is read and by whom is not stated on the record"; confirmed live against HCPortal's own API (`api.hcportal.eu/api/cryptograms/494`, HTTP 200 with header `Accept: application/json` -- without it the host answers a non-standard 466 "Access Forbidden" page, 26 Sept 2026 04:52 UTC), which carries `solution.name: "Partially solved"`, `cipher_key_id: null`, `note: null`, no attachment beyond the 3 plain images -- no reader, method or partial key is recoverable from the record itself; Aymeloglu's repo (fresh shallow clone, HEAD 2495c45e8b94ffbc4f09a085224aa5ebce5cdf9f) grepped for "hessen", "hessisch", "marburg", "hstam", 0 hits, not in that catalogue at all; Tomokiyo/Cryptiana pages on disk (sources/cryptiana/web/) grepped for "hessen", "hessisch", "marburg", "daenemark" -- the only hits are the unrelated Carl von Rabenhaupt 1646 letter to the regent of Hesse-Kassel (solved 2020, german.htm/habsburg.htm/unsolved.htm/unsolved-2026-09-24.htm) and a Habsburg-era Hesse mention (habsburg.htm) neither naming HStAM 4 f Dänemark Nr. 125; one OpenAlex query ("Hesse-Kassel Denmark 1672 cipher decipherment", 0 results, header auth, 26 Sept 2026) and one Semantic Scholar query ("Hesse-Kassel Denmark 1672 cipher decrypted", 0 results, header auth, 26 Sept 2026); no web search run this pass (not needed once both solver repos, the API and both scholarship indexes agreed -- see gate note below).

# Hesse-Kassel and Denmark letter with enciphered passages, 4 May 1672

Status: partial. HCPortal record 494 marks the item "Partially solved" but the record itself names no reader, no method and carries no attached key or solution text (see line 2). Treat this as "an outside partial claim, unattributed and unverified" rather than a completed reading until a source for it turns up.

## Target

- Shelfmark: Hessisches Staatsarchiv Marburg, HStAM 4 f Dänemark Nr. 125, ff. 2-4 (fond "4f - Staatenabteilung: Dänemark", folder "Nr.125").
- HCPortal record 494, name `hstam_4_f_daenemark_nr_125_0002-0004`, category "Nomenclator", language German, date 4 May 1672, sender/recipient both "Unknown" in HCPortal's structured fields, `solution: "Partially solved"` (id 3), created by Eugen Antal, no `cipher_key_id`, no `note`.
- 3 images online: ff. 2, 3, 4 (`hstam_4_f_daenemark_nr_125_0002/0003/0004`), fetched to `images/` (manifest.json).
- Bourdeau's own note (CATALOGUE.md #341, read 26 Sept 2026): "The year of the Dutch War; a completion job with a partial reading to anchor it" -- his own catalogue entry does not identify who solved the partial part either.

## Search log (intake, 26 Sept 2026)

1. Bourdeau's `dbourdeau/cyphersolver`, fresh shallow clone, HEAD `fc0c9e865d0fae67ca92d19750d2b09ab11972e0`: `CATALOGUE.md` #341 read in full (quoted in line 2); `find -iname "*494*"` over the whole clone found 3 unrelated hits (soria1523/decode/view9494.json, soria1523/read_r9494.md, decode_updates/decryptions/R9494.txt -- all DECODE record 9494, an unrelated Soria 1523 target, not HCPortal id 494). No dedicated solve folder, decode script or key file for this HCPortal id anywhere in the repo. Clone deleted after reading.
2. Aymeloglu's `aaymeloglu/unsolved-ciphers`, fresh shallow clone, HEAD `2495c45e8b94ffbc4f09a085224aa5ebce5cdf9f`: `grep -rin "hessen\|hessisch\|marburg\|hstam"` over the whole clone (markdown files): 0 hits on this target (one unrelated PARES row and one unrelated cipherkit README line, neither about Hesse-Kassel). Not in this catalogue. Clone deleted after reading.
3. Tomokiyo/Cryptiana pages on disk (`sources/cryptiana/web/`, no live fetch): grepped for "hesse", "hessisch", "marburg", "hstam" case-insensitively. Hits are all the unrelated Carl von Rabenhaupt 1646 letter (solved 2020 by finding the key in the Hessian State Archives Marburg, german.htm/unsolved.htm/unsolved-2026-09-24.htm) and one Habsburg-era Hesse succession mention (habsburg.htm, 1637-41, a different letter). Nothing naming HStAM 4 f Dänemark Nr. 125 or a 1672 Denmark correspondence.
4. HCPortal record status, live: `api.hcportal.eu/api/cryptograms/494` needs both a browser User-Agent and `Accept: application/json` (without the Accept header the host returns a non-standard HTTP 466 "Access Forbidden" page, not JSON -- new finding this session, not documented in CLAUDE.md's Access playbook table for this host yet). With it: HTTP 200, `solution.name: "Partially solved"`, `cipher_key_id: null`, `note: null`, `datagroups` carries only the 3 plain images, no attachment, no text field with a partial transcription. So "partially solved" is HCPortal's own category label with no recoverable evidence of what was read, by whom, or how -- confirms Bourdeau's own catalogue note that "what part is read and by whom is not stated on the record". 26 Sept 2026 04:52 UTC.
5. OpenAlex (`OPENALEX_KEY`, header auth): `search=Hesse-Kassel Denmark 1672 cipher decipherment`, 0 results, HTTP 200, 26 Sept 2026.
6. Semantic Scholar (`S2_KEY`, header auth): `query=Hesse-Kassel Denmark 1672 cipher decrypted`, 0 results, HTTP 200, 26 Sept 2026 (no 429, no retry needed).

No reader, method, key or independent reading found for HStAM 4 f Dänemark Nr. 125 in any of the six sources checked; HCPortal's "Partially solved" tag is on file but unattributed.

`python3 tools/intake_gate_check.py hessen-daenemark-1672`:
```
hessen-daenemark-1672: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
EXIT: 0
```
Gate passed 26 Sept 2026 04:53 UTC. Proceeding to image fetch and the brief's first cheap test.

## Images

Fetched 26 Sept 2026 to `images/` (manifest.json): ff. 2, 3, 4, via `api.hcportal.eu/api/cryptograms/494`'s `datagroups[].data[].image.original` URLs. Host: api.hcportal.eu, 4 requests this step (1 record JSON + 3 images), >=2s apart.

## Cheap test 1 (first cheap test per QUEUE.md row 7): what the existing partial reads, and what is left

No separate attachment or key exists anywhere (HCPortal record, both solver repos, Cryptiana) -- see search log above.
The "Partially solved" label refers to bold interlinear/marginal glosses written directly on the manuscript
images themselves, in a hand distinct from (and bolder than) the letter's main German Kurrent hand -- these are
not mentioned or transcribed anywhere in HCPortal's record, Bourdeau's catalogue, or Aymeloglu's catalogue (all
three treat the item as opaque). Whether the glossing hand is the period addressee's own decipherment marginalia
or a later (HCPortal-era) annotation is not established either way this pass.

**System.** f.2 (0002) is a plain, un-coded German cover leaf (salutation + opening, dated "1672 Mai 4/14" o.s./n.s.).
ff.3-4 (0003-0004) carry the enciphered passages: a nomenclator mixing (a) numeric code groups up to at least 834
(625, 651, 653, 774, 775, 601, 626, 69, 85, 33, 6d, 143, 119, 74, 26, 24, 83, 117, 20, 37, 104, 634, 427, 641, 303,
447, 834, 63, 38, 21, 20, 75, 96, 30, 31, 110) and (b) two-letter code groups (FF, XX, LL, WW, NN, WO), embedded
inline in otherwise plaintext German/Latin diplomatic prose -- at least ~40 code-token occurrences across the two
leaves (rough count from the legible crops; not a verified sign-by-sign transcription, see next step below).
Marginal numbers in a third, plainer hand (625, 774, 775 on f.3; 748/749-style numbers) look like paragraph/section
counters rather than code values and are excluded from that count.

**What the partial reads.** The one code I can read with confidence, glossed three times in the same bold hand
(f.4, crops `f4_top.jpg`/`f4_mid.jpg`): **601 = "Dennemarck"** (Denmark) -- unambiguous, plain German, no
paleographic doubt. Grade C (read directly from the image, not our cryptanalysis, but not from an attributed
key source either since no source for the gloss is named anywhere). A cluster of further bold glosses sits near
other code groups (f.3: "Cur Brandenburg", "Berlin", "B. Reichstag", "Ga. Stadt"; f.4: "der König in Dennemarck"
as a sentence-level paraphrase rather than a single-code label, "herzog von Ploen" near 427/641, "Kayser" and
"Bey Dennemarck" near 303/447/834, and four short abbreviation-like glosses -- "seco", "g:et", "d:af", "amm" --
over the dense 63/38/21/FF/20/75/20/WO/96/NN/30/31/110/XX cluster) but I could not pin an exact one-to-one
code-to-value correspondence for any of these at this image resolution and in this hand with confidence enough
to grade above M; reporting them here as leads, not readings.

**What is left.** Of roughly 20 distinct code values used across ff.3-4, only 601 is read with confidence (C);
the other ~19 (including every two-letter code FF/XX/LL/WW/NN/WO, which recur across the cluster and are
structurally the most promising to pin down first) are unglossed or glossed too unclearly for me to commit to a
value. No key.tsv is written this pass -- committing a guessed number-to-value table under time/paleography
pressure risks exactly the kind of silent repair rule 2 forbids. Next step (not run here, out of a breadth
worker's $2.5 cap): a dedicated transcription pass reading every gloss and every code occurrence at full native
resolution (crops under `images/`, already fetched), building key.tsv from only the glosses that are legible,
then testing whether the ~19 unglossed codes recur across other HStAM 4f Dänemark records (this is a single
short letter, not a pool -- QUEUE.md row 7 already flags it "no" for pool status).

No S (cryptanalytic) claim is made this pass, so no matched control is required (rule 3's condition for a control
is a solver's cryptanalytic attempt or a negative claim; this is a read-what-exists-and-report step only).

Hosts this target: api.hcportal.eu, 5 requests (2 record JSON + 3 images), >=1.6s apart, one Accept-header retry
(the first attempt without `Accept: application/json` got a non-standard HTTP 466 "Access Forbidden" page --
logged in the Access playbook note above, not a 429/403/challenge, so not a good-citizen-rule stop).
