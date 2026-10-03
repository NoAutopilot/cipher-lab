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

## While waiting (27 Sept 2026, WAIT-PASS-A)

Not waiting on an archive or a person -- images (f.2-4) are already on disk; the block is a dedicated
transcription pass that exceeded a breadth worker's $2.5 cap, since 26 Sept 2026 (Cheap test 1).

- Run the dedicated transcription pass named in Cheap test 1: build key.tsv from the legible glosses only (601=Dennemarck at grade C; more leads already named). M.
- Check whether the ~19 unglossed codes, especially the two-letter codes FF/XX/LL/WW/NN/WO, recur in other HStAM 4f Dänemark items already catalogued in this repo or the solver repos. S.
- Compare the bold glossing hand's style against other HStAM diplomatic-secretary annotations already on disk elsewhere in this repo, to judge whether it is period marginalia or a later HCPortal-era annotation. S.

## Siblings lookup (NEXT-HDK, 2 Oct 2026, 03:13-03:30 UTC)

The cheapest next step named by the 1 Oct finish-or-blocker Verdict: Bourdeau's HCPortal harvest, the Arcinsys
record for Nr. 125, one DECODE query. No transcription, solver or judge was run, so rule 3 has nothing to control.

1. **Bourdeau HCPortal harvest** (`research/catalogue_harvest/hcportal/` in dbourdeau/cyphersolver, sparse clone,
   HEAD 34e0fc8981112070c6b8b718519eeed6dca3a7ee, 1 Oct 2026; the path is under `research/`, not at the root as the 1 Oct
   gap line said). `index.json` (1,493 cryptograms): only one `hstam_4_f_daenemark` record, 494 (this one). The other
   `hstam_4_f` record is 495 (Schweden Nr. 116, 1630, Solved, monoalphabetic). `keys/*.json` (176 keys): there is no 4f Dänemark key.
   The 4f keys are all Schweden Nr. 116/253/271. The one HStAM key of the right decades is **HCPortal key 255**,
   `hstam_4 d Nr 1234_0013-0016` (fond 4 d Kanzlei- und Geheimeratskorrespondenz), `used_around: 1666`, category
   Nomenclator, structure `1fnd,2s,Vn,0n`, 4 images on api.hcportal.eu, no transcription. This is the same file as
   HCPortal cryptogram 522 (the c.1660 extension to code 712 cited under known-keys), but ff.13-16 are a key, not
   that letter. It has not been fetched here. The clone was deleted after reading.
2. **Arcinsys Hessen** (route: simple-search GET in headless Chromium, then the Staaten D tree and
   `ajaxlist.action` pages for node g143361; `tools/browser_fetch.js`-style Playwright). Record:
   `HStAM, 4 f Staaten D, Dänemark 125 (in)`, archivalDescriptionId 1881503 (`detailAction.action?detailid=v1881503`),
   Sachakte, title "Auswärtige Politik (Berichte von Linker). Landtagsproposition zu Rendsburg", Laufzeit 1672,
   representations Original + Mikrofiche. **Online flag: digitised, "Digitalisat von 6"**, served at
   `https://digitalisate-he.arcinsys.de/hstam/4_f_staaten_d/daenemark_125/hstam_4_f_staaten_nr_daenemark_125_000N.jpg`
   (N=1-6; also DFG-viewer METS `https://arcinsys.hessen.de/arcinsys/mets?detailid=v1881503`). Tree path: HStAM >
   Akten bis 1867 > Hessen und Hessen-Kassel > Zentralregierung und Hofverwaltung > Auswärtige Angelegenheiten > 4 f >
   4 f Staaten D (fondsId 6830) > 01 Dänemark (g201874) > 01.8 Politik, auch innere Verhältnisse und Territorialsachen
   (g143361, 10 pages).
   **The whole file is 6 images, so nothing of Nr. 125 is missing.** Arcinsys image 0002 is the same leaf as HCPortal 0002
   (compared on downscaled previews), so the numbering agrees. The three images HCPortal lacked were fetched to `images/` (manifest.json):
   - 0001: a modern archival cover, stamp "Staatsarchiv Marburg Bestand 4f Dänemark Nr. 125". The summary reads (my
     reading of a modern hand, M): "Akten des fürstl. Kanzlers Vultejus. Sekr. Lyncker schreibt von Hamburg aus über
     seine Behandlung seitens des Dänischen Hofes u. die der Brandenburgischen Gesandten, klagt über Kurbrandenburgs
     Prätensionen in Etikettefragen, schreibt über auswärtige Politik (z. Th. in Chiffern) u. Landtagsproposition zu
     Rendsburg. 1672 Mai 4". The archive's own summary therefore names the sender (the Hessian secretary Lyncker/Linker)
     and the recipient (Chancellor Vultejus). This fills the "Unknown" sender and recipient on HCPortal 494, at M
     until the letter's own signature line on 0004 is read.
   - 0005: the verso of 0004. It is blank apart from show-through and an endorsement in a 17th-century-looking hand,
     read on a 900-px preview as "L. Lincker an Cantzl. Vultejum / d. data Hamburg / d. 4 May 1672" (M). There is no
     ciphertext, address panel or key on it.
   - 0006: a printed Kassel Rentkammer circular dated 12 May 1738, signed F.B. von Adelebsen. It is unrelated, has no
     cipher and was filed at the end of the folder. It was not kept on disk; its URL is in the manifest.
   **Sibling files in node g143361, 1666-1676** (read from the same ajaxlist pages, no further requests). Only two
   carry a digitisation marker: **Dänemark 125 (this file) and Dänemark 131**. Dänemark 131 is "Korrespondenz mit dem
   brandenburgischen Residenten zu Kopenhagen, Friedrich v. Brandt ...", 1671-1674, and has not been opened. The
   same-sender files are undigitised: Preußen 345 "Sendung Linkers nach Dänemark" (1668), Dänemark 105 "Korrespondenz mit v.
   Dalwig in Kopenhagen betr. den hessischen Sekretär Lynker in Berlin ..." (1668), Hamburg 2 "Vorgänge in Dänemark"
   (1671-1672) and Preußen 363 "Verhandlungen mit Braunschweig, Kursachsen u. Dänemark" (1672). Whether any of them
   carries the same nomenclator is unknown.
3. **DECODE**: the catalogue listings already on disk were grepped, with no live request. The listings are
   `sources/decode/records-decrypted-2026-09-24.tsv`, `records-non-decrypted-2026-09-24.tsv` (cipher records) and
   `keys-all-2026-09-28-merged.tsv` (6,325 rows). No Marburg 4 f record exists, and no Dänemark/Kassel cipher from the
   1670s. The 252 Marburg rows are all keys or ciphers of fond 4 d (Nr. 1218-1238). The one dated close to 1672 is
   **DECODE record 4692, `Hstam_4_d_nr_1235_01`, Key, dated "1670 -", 1 page**, which no file in this repository cited
   before today. Nr. 1234 has four DECODE key records (4687, 4688, 4690, 4691, "1600 - 1699", 4687 in French). On this
   account DECODE images are account-gated (Access playbook table), so the next route is the Arcinsys image of HStAM
   4 d Nr. 1235 if it is digitised.

Requests: arcinsys.hessen.de 16 (curl and headless Chromium, one at a time, >=2 s apart, no challenge, no 4xx);
digitalisate-he.arcinsys.de 4 images (0001, 0002 for the numbering check, 0005, 0006); github.com 1 sparse clone;
de-crypt.org 0; one web search. No login used.

## Intake gate re-run (A2-HDK, 2 Oct 2026, 20:55 UTC)

Run before the known-keys and sibling check (brief .claude/briefs/runs/2026-10-02-acct2-a2-hdk.md, step 2):
```
$ python3 tools/intake_gate_check.py hessen-daenemark-1672
hessen-daenemark-1672: partial (line 1) has an edition citation but no logged open-web and blog-comment check (no 'Web and blog check' heading, no paragraph naming [the three blogs]) -- run check-solved.md's 'Open web and blog comment threads' step first (CHECK-SOLVED-WEB, 28 Sept 2026: spinelli-beinecke-c1515 was read in a [blog] comment thread in 2017)
EXIT 1
```
In this paste the blog names are replaced by [the three blogs] and [blog]. Quoted verbatim, the gate's own message would satisfy the gate's name-all-three-blogs test.
A re-run also showed a second missing section: no '## Premise check', the adversarial pre-reading pass added 2 Oct 2026.
The 26 Sept intake passed an older gate. The open-web and blog-comment step was added on 28 Sept 2026, and this target has never run it. Both steps belong to check-solved, not to the known-keys and sibling check, so this worker stopped before fetching anything (0 requests). HCPortal key 255, HStAM 4 d Nr. 1235 / DECODE 4692 and Dänemark 131 are still unfetched.

## Known-keys and sibling check (A2-HDK, 2 Oct 2026, 21:32-21:45 UTC)

The cheapest next step named by the Verdict: HCPortal key 255, DECODE 4692 (HStAM 4 d Nr. 1235), the digitised
Dänemark 131, and a code-range comparison. Intake gate first: `python3 tools/intake_gate_check.py hessen-daenemark-1672`
-> `hessen-daenemark-1672: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.

1. **HCPortal key 255** (`api.hcportal.eu/api/cipher-keys/255`; note the route is `cipher-keys`, not `keys`, which 404s).
   Name `hstam_4 d Nr 1234_0013-0016`, Nomenclator, `used_around 1666`, no note, no transcription. 4 images fetched to
   `keys/hcportal_key255_0013..0016.jpg` (manifest.json). My reading (M, 1400-px and native crops):
   - f.13: a letter table with 5 two-digit homophones per letter, A=20 30 40 50 60, B=22 32 ..., C=24 ..., D=26 ..., E=28 ...,
     F=21 31 ..., G=23 ..., H=25 ..., I=27 ..., K=29 ..., L=70 80 90 100 110, M=72 ..., N=74 ..., O=76 ..., P=78 ..., Q=71 ...,
     R=73 ..., S=75 ..., T=77 ..., U=79 ..., W=120 130 ..., X=122 ..., Y=124 ..., Z=126 ... 166 (full table in
     `keys/key255_gloss_test.py`); a doubled-letter row shifted by two (A=CC, B=DD, C=EE, D=FF, ... I=LL, L=NN, T=WW, U=XX,
     W=YY, X=ZZ, Y=AA, Z=BB); a syllable row (au eu ei ie ii ou ch ck ct ff ll mm nn pp rr sch ss sp sl tt tz) with symbols;
     nulls ("Blinde Zahlen") 1-20 and 121 131 141 151 161 171 123-139 odd, 143-169 odd, 173 175 177 178 179.
   - ff.13-16: a nomenclator 180-407 (180 Kayser, 184 Kön. in Dennemarck, 205 Brandenburg, 212 Dänemark(?), 229 Frankreich,
     252 Mark Brandenburg, 253 Holstein, 295 Copenhagen, 298 Hamburg, 309-369 French political words, 397-407 numerals).
   - **Endorsement on f.16** (M): "Clavis mit H. Dalwig zu Cleve(?) und Frenach(?) mit Secretario Lincker 1666. Item 1676 mit
     dem Herrn ... OEr". A key of the Kassel chancery for its correspondence with Secretary Lincker, the sender of this letter.
2. **DECODE 4692** (`Hstam_4_d_nr_1235_01`, Key, "1670 -", Private Ciphertext: True). The login-free RecordsView answers;
   ImagesList redirects (302) to login. One login via `tools/decode_browser_login.js 4692 DIR --fetch-page ImagesList
   --guess-fullsize`: the full-size image **did serve** (7051x6178 px, 13.4 MB, sha1 32ec988d..., a real image, not the
   forbidden.png placeholder), so the account-wide block in the Access playbook table did not hold for this record on
   2 Oct 2026. Not committed (account-gated source; over the folder budget); URL and sha1 in manifest.json. Reading (M):
   letter table A=41-44 ... Z=133-136 (4 homophones each) plus one symbol per letter; nomenclator 153-363, which names
   174 Dennemarck, 190 Linker, 214 Churbrandenburg, 230 Canzlar Brand, 231 Resident Brand, 246 Canzlar Vultejus,
   249 Mr OEr, 281 Berlin, 284 Coppenhagen, 288 Hamburg. A later key of the same circle (Lincker, Vultejus, Brandt).
3. **Dänemark 131** (Arcinsys archivalDescriptionId 537589, METS `mets?detailid=v537589`, 106 images; the image path is
   `.../daenemark_131/hstam_4_f_staaten_d_nr_daenemark_131_NNNN.jpg`, with `_d_` that Nr. 125's path lacks). Sampled 8 of 106
   leaves (0003 0016 0029 0042 0055 0068 0081 0094) on 1000-px contact sheets: Friedrich von Brandt's reports from Copenhagen,
   27 Jan, 18 May, 14 Sept, 17 Nov 1672, to the Landgravine regent, her drafts, a Latin treaty copy. All in clear; no code
   group seen on the sampled leaves. A sample, not a full read.
4. **Code-range comparison.** The letter's nomenclator values (601 Dennemarck, 229 Berlin by the gloss, up to 834) match
   neither key: key 255 has Dennemarck 184/212 and Berlin not at 229 (229 = Frankreich); 4692 has Dennemarck 174, Berlin 281,
   and both end below 410. **The nomenclator of 1672 is a different, larger list; neither key reads a 3-digit group.**
   The letter table is another matter. Every 2-digit group in the two f.4 runs falls in key 255's 20-166 range, and the
   letter uses key 255's doubled-letter codes (FF XX LL WW NN YY); 4692's letter table starts at 41, so 20-38 are outside it.
5. **Gloss test of key 255's letter table** (rule 3; `keys/key255_gloss_test.py`). Native crops of the two f.4 runs, my
   reading (M): run 1 "Totaliter FF. 67. 85. 33. XX. 6d. LL. 143. WW. 119. 74. 26. 28. 83. 117. 20. bb. 37. 104. 634.",
   marginal gloss "disgustirt und ertanin holstein"; run 2 "... 63. 38. 22. FF. 20. 75. 20. I. / YY. 96. NN. 30. 32. 110.
   0. XX.", interlinear glosses "geb", "das", "amm", "wo", "ab laut". 26 (token, gloss-letter) pairs where the gloss letter
   sits clearly over or beside one token. Control: the same table with the 24 letter labels randomly permuted across columns
   (homophones and the doubled row move together), 20,000 draws, seed 255; the permutation changes every decoded letter, so
   the control can differ from the target on this statistic.
   ```
   $ python3 keys/key255_gloss_test.py --quiet
   pairs 26  key255 matches 26  control mean 1.09  control max 11  p(control>=real) 0.00005
   $ python3 keys/key255_gloss_test.py --alt22 --quiet      # run 2's '22' read as '21'
   pairs 26  key255 matches 25  control mean 1.09  control max 10  p(control>=real) 0.00005
   $ python3 keys/key255_gloss_test.py --notes --quiet      # tokens as the 1 Oct NOTES read them, before key 255 was seen
   pairs 26  key255 matches 21  control mean 1.05  control max 10  p(control>=real) 0.00005
   ```
   Caveat: the 26 pairs were chosen by me after I had seen key 255's table, and my token readings of 67/28/22/YY/32 agree
   with key 255 where the 1 Oct preview read 69/24/21/WO/31; the `--notes` row, on readings fixed before key 255 was seen,
   is the fair figure (21/26 against a control max of 10). Decoded with key 255: run 1 "D I S G U [6d LL 143 WW] U N D
   E R T A [bb] I N [634]" = gloss "disgu(stirt) und ertan(in)" with 634 = holstein (gloss, M); run 2 "G E B D A S A ..
   W O L A B L . U" = glosses "geb das .. wo (l)ab l.u". Unresolved inside run 1: 6d, LL (=I in key 255) and 143 (a null in
   key 255) against the gloss's "stirt"; WW = T fits the final t.
   **Result: key 255's letter table (1666, endorsed for correspondence with Secretary Lincker) reads the 2-digit letter
   cipher of this 1672 letter, cross-checked against the letter's own gloss; its nomenclator does not read the 3-digit
   groups.** The letter values are graded S (a key of the same office tested against a control), not H, until the token
   reading is a reconciled transcription: the key was endorsed for 1666 and the 1672 letter may use a revised table.

Requests: api.hcportal.eu 4 JSON (3 route guesses, 1 hit) + 4 images; arcinsys.hessen.de 1 curl + 5 headless Chromium
searches + 1 METS; digitalisate-he.arcinsys.de 2 range probes (404, wrong path guesses) + 16 image requests (8 served,
8 404 beyond the 106 images); de-crypt.org 2 login-free + 1 browser login with 3 fetches. All one at a time, >=1.6 s apart,
no 429/403/challenge. Vision calls (my own reads): 11.

## key.tsv and DECODE Nr. 1234 check (A2-HDK3, 2 Oct 2026, 22:10-22:25 UTC)

The Verdict's cheapest next step, nothing else. Intake gate first:
```
$ python3 tools/intake_gate_check.py hessen-daenemark-1672
hessen-daenemark-1672: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
EXIT 0
```
1. **key.tsv** written by `keys/make_key255_tsv.py` from the letter table already typed in `keys/key255_gloss_test.py`
   (one source): 120 letter homophones, 24 doubled-letter codes, 50 nulls as key 255 f.13 lists them, plus 128/148/158
   (see 2). 197 rows, all grade S. The key sheet says "Blinde Zahlen sind von 1 biß 20", but its own table gives
   20 = A; key.tsv keeps 20 = A (nulls 1-19), which the letter's gloss reads three times and the period scale in 2
   confirms ("20 a"). The syllable row is in symbols, not codes, and the nomenclator 180-407 does not read this letter:
   neither is in key.tsv. `--check` exits 1 if key.tsv is stale.
   So that `tools/decode_key.py --check` has something to regenerate, `ciphertext_f4runs.tsv` holds the two f.4 runs
   exactly as A2-HDK read them (single eye, native crop, every token conf M; not a reconciled transcription, and not a
   substitute for gap 1), with `decode.json`:
   ```
   $ python3 tools/decode_key.py ciphers/hessen-daenemark-1672 --check
   ciphertext_f4runs.tsv: tokens 36: M 31, U 5
   reading up to date
   $ cat reading_f4runs.txt   (body)
   f4_run1   d i s g u [6d] i t u n d e r t a [bb] i n [634]
   f4_run2a  g e b d a s a [I]
   f4_run2b  w o l a b l [0] u
   ```
   Grades: 31 M (key S, token reading M), 5 U (6d, bb, 634, I, 0); 0 H, 0 C. 143 decodes as a null and drops out.
   `--split-check` flags the same five; 634 has candidate splits (6|34 = null c, 63|4 = g null) that only the image can
   settle (the gloss gives "holstein", a nomenclator reading). Against the gloss "disgustirt", run 1 reads
   "disgu[6d]it": 6d sits where the gloss has "s", and LL = i, 143 = null leave the gloss's "r" unread. This is a
   cryptanalytic result on a provisional token reading, not a reading of the letter.
2. **DECODE 4687/4688/4690/4691 (HStAM 4 d Nr. 1234)**, one browser login (`tools/decode_browser_login.js 4687 DIR
   --listen`; `--fetch-page ImagesList/<id>` turned out to be the global image list, not the record's, so the record
   pages were fetched through the listener). All 16 full-size images were served (HTTP 200, real JPEGs; sizes and sha1
   in images/manifest.json, not committed: account-gated). My reading (M, contact sheets and 2 native crops):
   - **4691 (Nr. 1234_04) is key 255 itself**: the same four leaves as HCPortal 255 (letter table, nomenclator 180-407,
     endorsement "mit Secretario Lincker 1666 ... 1676").
   - **4690 (Nr. 1234_03)**: a nomenclator 300-409 (P1, P5), a different letter table 20-199 with symbols (P3), endorsed
     "Clavis mit dem Obrist Lieutenant Dobely(?) 1668" (P4), and on P2 **"Scala über den Clavem mit Secretarium
     Linckern"**, a decipher scale (code -> letter) for the Lincker key. `keys/check_scale4690.py` compares the 120 scale
     entries I read on the top 62% of P2 (20-37, 47-67, 78-98, 110-133, 145-166, LL-ZZ) with key.tsv:
     `scale entries 120: agree 120, disagree 0`. 128, 148 and 158, which are dashes on the scale and have no entry on
     key 255 f.13, were added to key.tsv as nulls from this witness. So the letter table now has two period witnesses
     of the Lincker key (the key sheet and the decipher scale). It stays grade S for this letter, because both are
     1666-era and the 1672 letter may use a revised table.
   - **4688 (Nr. 1234_02)**: a Latin cover-word list (Cassell = Nutrix, Hollandt = Diues, ...), no numbers.
   - **4687 (Nr. 1234_01)**: the folder cover ("Chiffren aller Art 17. Jh."), an endorsement "Chiffre mit dem Envoyé
     Martine zu Paris", a French note "Le chiffre dont on se sert pour moi va jusqu'a 712, je voudrois y adjouter 713 pour
     dire 252.258.303.291 [mi ni st ve] ... 716 pour dire ..." (a syllabic chiffre, list not present), and a symbol
     nomenclator with a letter table.
   **Result: none of the four records carries a nomenclator reaching 834 or Dennemarck at 601.** The highest list is the
   Paris chiffre's 712 (+713-716), which is not present as a list, belongs to a different correspondent, and uses
   syllable values such as 252 = mi. The 1672 nomenclator is not in HStAM 4 d Nr. 1234 as DECODE has it. Not checked: Nr.
   1236-1238 (no DECODE record in the cached listings), and HStAM 4 d outside the DECODE records.

Requests: de-crypt.org 1 browser login + 1 RecordsView + 4 ImagesList pages (global list) + 25 auto-discovered
thumbnails (other records; the tool's --max-files cap) + 3 RecordsView + 16 full-size images, one at a time, 1.6 s
apart, no 403/429/challenge. Vision calls (my own reads): 7.

## Arcinsys lookup of HStAM 4 d Nr. 1236-1238 (A2-HDK4, 2 Oct 2026, 22:28-22:40 UTC)

Intake gate (pasted before work): `hessen-daenemark-1672: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.

Route: Arcinsys Hessen simple search (`tools/browser_fetch.js --type "#inputSearchTerm=Chiffern"`) returned the
classification node **HStAM 4 d > Gliederung > 8 Chiffern** (`showItemsList.action?nodeId=g59523`; fonds 4 d
Kanzlei- und Geheimeratskorrespondenz, fondsId 4891). The node holds 21 items, all "Chiffernschlüssel", Nr. 1218-1238
(read in full, one rendered page with the length selector set to all). Catalogue records of the three named files:

| Nr. | archivalDescriptionId | Title (catalogue) | Laufzeit (catalogue) | Online | DECODE (cached listing) |
|---|---|---|---|---|---|
| 1236 | 2375205 | Chiffernschlüssel aus der 2. Regierungshälfte des Landgrafen Karl | ca. 1715 | Nutzungsdigitalisat JPEG (thumbs to at least _0117) | 46 key records, 4697-4740 range, "1715 -" |
| 1237 | 1923395 | Chiffernschlüssel aus der Zeit Landgraf Wilhelm VIII | Mitte 18. Jh. | Nutzungsdigitalisat JPEG | 2 key records (4741, 4742), "1700 - 1799" |
| 1238 | 93919 | Chiffernschlüssel | Anfang 19. Jh. | Nutzungsdigitalisat JPEG | 3 key records (4743-4745), "1800 - 1850" |

All three are digitised (`digitalisate-he.arcinsys.de/hstam/4_d/<nr>/...`), but **the archive dates none of them to
1670-72**: 1236 to ca. 1715 (Karl reigned 1670-1730, regency to 1675, so "second half" is after 1700), 1237 to
Wilhelm VIII (mid-18th c.), 1238 to the early 19th c. The rest of the node is dated 1600 (1219), 1635-52 (1218),
1670 (1235 = DECODE 4692, already checked: nomenclator 153-363) and 1710-1731 (1220-1233; 1220 undated in Arcinsys,
"1715 - 1750" in DECODE); 1234 is undated (key 255 of 1666 and the DECODE 4687/4688/4690/4691 sheets, already
checked). **By catalogue date, the 4 d Chiffern node holds no key of 1671-72 besides those already checked, and so no
candidate for the nomenclator reaching 834 with Dennemarck at 601.** No image was opened: the dates come from the
catalogue and DECODE, not from the sheets, so an undated 1670s sheet bound into 1236 is not excluded (M, not tested).
Aside (M): 1228 "Chiffernschlüssel für den Residenten Martine in Paris" is dated 1719, so the DECODE 4687 note "Chiffre
mit dem Envoyé Martine zu Paris ... va jusqu'a 712" belongs to c. 1719, not the 1670s.

Correction: A2-HDK3's step above says Nr. 1236-1238 have "no DECODE record in the cached listings". They do, in
`sources/decode/keys-all-2026-09-28-merged.tsv` (and `keys-na-p59-128-2026-09-28.tsv`): 52 rows for 1235-1238, dated
as in the table. The grep that missed them presumably searched the 2026-09-24 record listings only.

Requests: arcinsys.hessen.de 7 (1 curl that got a 302, 6 headless-Chromium page loads: 3 searches incl. one timeout,
node list x2, 3 detail pages; one at a time, >=2 s apart, no 403/429/challenge). digitalisate-he.arcinsys.de 0.
Vision calls 0.

## GAPS152-hessen-daenemark-1672 (3 Oct 2026, account-4): page 1 (image 0002, f.2) of the transcription and gloss pass

Crop step (pasted command): `python3 tools/iiif_lines.py --image ciphers/hessen-daenemark-1672/images/hstam_4_f_daenemark_nr_125_0002.jpg --out ciphers/hessen-daenemark-1672/images/crops_p1 --region 280,950,2240,3000 --prefix p1 --lines-per-crop 2 --overlap 1 --debug` -> "region 2240x3000, 25 lines, 13 bands x 1 segments; pitch 93 distance 65 prominence 195.3 ... wrote 13 crops". The debug overlay was checked by eye: every written line is inside a band. Pass A and pass B (two blind Opus subagents, one call each, given only the 13 crops) agreed that the crops do not overlap, so `--overlap 1` had no effect. The page has 23 written lines; pass A counted 22, but both passes put the code on the same line, 21.

Result: image 0002 carries **one** cipher group, on line 21: "...hof geführet, aber zu der zeit der **690.** zugegen-/wartig, dann selbiger über seine reception...". Both passes read `690` at M, with the alternative 630 (the middle glyph is a descending 9 or 3). `tools/reconcile_passes.py` reports signs agreeing 1/1 (100%), 0 disagreement columns, 1 agreed-uncertain sign, and gloss agreement 0/1. There is one gloss, in the bold hand directly above the group. The passes split on its letters: pass A read "Bleinenkehl" and pass B "Bleinenkohl". My own reconciliation on a 2x native zoom reads B-l-e-i-n-e-n-k-[e/o]-[f/s/h]-l. The name is not identified, so the gloss is graded M, not C. The context says 690 is a person ("zu der zeit der 690. zugegen"). 690 is outside key.tsv, whose key-255 nomenclator runs 180-407, so the gloss is the only witness. Every other numeral on the page reads as plain text, and both passes excluded the same three: "den 24 passato" (line 2), "vor 3 tagen" (line 4) and "über 8 tage" (line 16). That corrects the 1 Oct gap note: "the code in its last lines" on 0002 is this one group, not several.

Gloss pairs: 1 (690 -> "Bleinenk??l", M). `tools/interlinear_align.py` and a held-out check were not run, because a held-out check needs a code seen at least twice and page 1 has a single pair; they wait for pages 2-3. Files: `transcription/p1_passA.tsv`, `p1_passB.tsv`, `p1_agreement.tsv`, `p1_ciphertext.tsv` (the reconciled page-1 row), crops in `images/crops_p1/`. No reading beyond the graded pair. Vision calls: 2 subagent passes plus the reconciler's own zooms (3 units).

## GAPS155-hessen-daenemark-1672 (3 Oct 2026, account-4): page 2 (image 0003) of the transcription and gloss pass

Crop step (pasted command): `python3 tools/iiif_lines.py --image ciphers/hessen-daenemark-1672/images/hstam_4_f_daenemark_nr_125_0003.jpg --out ciphers/hessen-daenemark-1672/images/crops_p2 --region 300,580,2220,2640 --prefix p2 --lines-per-crop 2 --overlap 1 --debug` -> "region 2220x2640, 28 lines, 14 bands x 1 segments; pitch 92 distance 64 prominence 154.8 ... wrote 14 crops". The debug overlay was checked by eye. Two blind Opus subagent passes, one call each, were given only the 14 crops. Both counted 28 written lines.

Result: image 0003 carries **9 cipher groups, all 3-digit, all glossed** in the bold hand. It has no 2-digit or letter groups, and its only plain numerals are "500 Rthl" (line 6) and "70 Rthl" (line 11). `tools/reconcile_passes.py` reports signs agreeing 9/9 (100%) with 0 disagreement columns, 4 agreed-H and 5 agreed-uncertain. Its gloss agreement is 0/9 because it compares exact strings; in substance the passes' glosses agree on 7/9. Reconciled rows are in `transcription/p2_ciphertext.tsv`:

| line | code | gloss | sign | gloss grade |
|---|---|---|---|---|
| 2 | 605 | K. Dennemarck | H | C |
| 3 | 651 | Cur Brandenburg | M (alt 657) | C |
| 7 | 625 | margin gloss unread (two Kurrent words, "...stelt / ...bel") | M | U |
| 9 | 653 | Cur Brand. | H | C |
| 17 | 229 | Berlin | M | C |
| 25 | 651 | Curbrandenburg | H | C |
| 25 | 690 | Bleinenk?fl | M (reconciler override, see below) | M |
| 28 | 774 | Holland | H | C |
| 28 | 775 | Gen. Staden | H | C |

Gloss grades: C 7, M 1, U 1 (9 tokens). Points from the reconciliation:
- **625 is a code, not a section counter.** It stands inline ("und hat 625. hierbey signalirte dienste gethan", a person), and the margin repeats "625" over a gloss. This settles that half of the 1 Oct exclusion of 625/774/775 as section counters; 774 and 775 are inline glossed codes too (Holland, General-Staaten).
- **690 recurs.** Both passes read the last group on line 25 as 650 (alternatives 656/659 in A, 690/630 in B). On a 2x native zoom the middle glyph is a loop with a long descender, the same descending 9 as page 1's 690, and the gloss above is the same word as page 1's (B-l-e-i-[n]-e-n-k-[o/e]-[f/s]-l). I read it as 690 at M. The person's name is still unidentified.
- **651 and 653 are both glossed Kurbrandenburg.** That is two codes for one meaning, a homophone or a variant (M).
- **605 is "K. Dennemarck"**, beside 601 "Dennemarck" glossed on f.4. Key 255 makes the same split (184 Kön. in Dennemarck, 212 Dänemark).
- **Key-255 range check (180-407).** Only 229 falls in range, and key 255 reads 229 as Frankreich where this letter's gloss reads Berlin: a conflict, so key 255's nomenclator does not read this letter. 605, 625, 651, 653, 690, 774 and 775 are all above 407. This is the third witness, after 601 and 690, that the 1672 nomenclator is a different list.

**Gloss alignment and held-out check.** `tools/interlinear_align.py align transcription/gloss_pairs.tsv transcription/gloss_align.tsv transcription/gloss_key.tsv --floor 100` ran over the 9 pairs from pages 1-2 ("tokens 9; values 7; single-segment 6, agrees 2, conflict 1"). The 1 conflict is 690's '?' letter, not a real disagreement. Each gloss sits directly over its group, so the DP alignment is trivial here; the tool is used for its key output. Then `keys/gloss_heldout.py` ran a leave-one-out check: each occurrence of a recurring code is predicted from that code's other occurrences, against a control that shuffles glosses among occurrences (codes and counts fixed, 10000 draws). As read, it scores **4/4** against a control mean of 0.44, p95 2 and P(ctrl >= 4) = 0.007 (seed 1; seed 7 gives 0.009). That 4/4 is partly circular, because the 650 -> 690 override used the gloss match. With that row left at the passes' 650, it scores **2/2** (651 only) against a control mean of 0.22 and P = 0.11: not discriminating at this N, so the held-out check licenses nothing yet. It needs page 3's recurrences. No key.tsv rows were added: key.tsv stays the letter table, and the gloss-pinned nomenclator values live in `transcription/gloss_key.tsv` (C/M per row of p1/p2_ciphertext.tsv) until page 3 is merged into ciphertext.tsv.

Files: `transcription/p2_passA.tsv`, `p2_passB.tsv`, `p2_agreement.tsv`, `p2_ciphertext.tsv`, `gloss_pairs.tsv`, `gloss_align.tsv`, `gloss_key.tsv`, `keys/gloss_heldout.py`, crops in `images/crops_p2/`. No reading beyond the graded pairs. Vision calls: 2 subagent passes plus the reconciler's own zooms (3 units).

## GAPS159-hessen-daenemark-1672 (3 Oct 2026, account-4): page 3 (image 0004) of the transcription and gloss pass; pooled held-out

Crop step (pasted command): `python3 tools/iiif_lines.py --image ciphers/hessen-daenemark-1672/images/hstam_4_f_daenemark_nr_125_0004.jpg --out ciphers/hessen-daenemark-1672/images/crops_p3 --region 120,540,2380,2900 --prefix p3 --lines-per-crop 2 --overlap 1 --debug` -> "region 2380x2900, 28 lines, 14 bands x 1 segments; pitch 89 distance 62 prominence 105.6 ... wrote 14 crops". The region includes the left margin (the marginal gloss of run 1). Debug overlay checked by eye. Two blind Opus subagent passes, one call each, crops only; both counted 30 written lines.

Result: `tools/reconcile_passes.py` (after normalising pass A's margin rows: its 7480 moved to line 1 pos 0 as in B, its margin repeat of 625 and its line-11 "12" (a plain "12 Rthl." count, which B excluded) dropped) reports signs agreeing 47/56 (83.9%), 26 agreed-H, 21 agreed-uncertain, 9 disagreement columns, of which 2 are a sort artifact of the margin 7480 and 7 are real. The reconciler settled them on native zooms (`transcription/p3_ciphertext.tsv`, one row per group with the call and why): 2.2 68 (A 968, B 68; left M, alt 768/968), 6.1 681 (A 601, B 681; the middle glyph is a closed double loop, 8), 20.1 768 (A 768, B 568), 21.2 96 (A 66, B 96), 25.1 437 (A 447, B 437; middle glyph unlike line 26's 4s), 26.1 303 (A 383, B 303), 26.2 447 (A 441, B 447). Two overrides beyond the disagreements: 1.1 read 602, not 601 (the z-shaped 2 of this hand, as at 26.3), with a gloss "Der Konig in Dennemarck" above it that both passes missed at the crop's top edge (reconciler only, so M); 21.1 read YY, not the passes' 44 (two y-forms on the zoom, the f4runs reading, gloss "w", and key 255 reads YY = w).

Page 3 nomenclator groups (3- and 4-digit) with their glosses: 602 Der Konig in Dennemarck (M), 5756 Franckreich (C), 601 Dennemarck x2 (C), 229 Berlin (C), 681 Cur Brandenb (C), 768 ?ueco (M; Sueco?), 437 641 Hertzog von Ploen (C, one gloss over the pair), 303 allian?e (M), 447 Kayser (C, after a struck word), 834 Rex Daniae (C); unglossed: 68 (M), 625 (margin repeats the number), 634, 602 (line 26), and the margin 7480 (maybe a note). Gloss grades on page 3's 11 pairs: C 8, M 3. The two dense runs (lines 15-17 and 20-21) are the letter cipher: 113, 104 and 110 fall in key 255's letter table (r, n, l), the run-2 letter glosses read "gott geb das amm.." and "w o .. a b l au t" over the groups, and the marginal "disgustirt / unvertanin / Holstein" beside run 1 is a gloss of the run, not of single groups. Corrections to the provisional f4runs: run 1's "143" is 113 in both passes, "6d" is 60 (M), "bb" is 66 (M), "96" in run 2b is confirmed (M), "44"/YY settled as YY.

Key-255 range check (180-407): 229 (gloss Berlin, key 255 Frankreich) and 303 (gloss alliance, key 255 Munster on a preview read of keys/hcportal_key255_0014.jpg, M) fall in range and both conflict; every other nomenclator group (437, 447, 601, 602, 634, 641, 681, 768, 834, 5756) is above 407. Key 255's nomenclator does not read this letter (fourth and fifth witnesses, after 601, 690 and page 2's 229).

**Pooled held-out (pages 1-3).** `tools/interlinear_align.py align transcription/gloss_pairs.tsv transcription/gloss_align.tsv transcription/gloss_key.tsv --floor 100` over 20 pairs ("tokens 21; values 16; single-segment 13, agrees 6, conflict 1, doubtful 1"; the conflict is still 690's '?' letter, the doubtful is the 4-digit 5756; the tool splits "Der Konig in Dennemarck" into its last words for 602, which is cosmetic). Then `keys/gloss_heldout.py` (shuffled-gloss control, 10000 draws; new `--set` option to score a row with a different code):

| run | held-out | control mean | p95 | P(ctrl >= real) |
|---|---|---|---|---|
| as read (690 override), seed 1 | 8/8 | 0.362 | 2 | 0.0000 |
| as read, seed 7 | 8/8 | 0.373 | 2 | 0.0000 |
| without the 690 override (`--set p2:25.2=650`) | 6/6 | 0.265 | 2 | 0.0000 |
| without 690, and 6.1 read 601 instead of 681 | 6/7 | 0.434 | 2 | 0.0000 |

The pooled check is now discriminating, with or without the 690 override: 651 (p2 x2), 229 (p2, p3) and 601 (p3 x2) each predict their own other occurrence, and the shuffled control can vary on the statistic (codes and counts fixed, glosses permuted). Per-code, it rests on only three recurring codes (four with 690), so it says the gloss hand is consistent code-for-code, not that every single value is right; 651/653/681 all glossed Kurbrandenburg and 601/602/605 all Dennemarck-family remain variants (M), not merged. No key.tsv rows added (key.tsv stays the letter table); the gloss-pinned values are in `transcription/gloss_key.tsv`.

Files: `transcription/p3_passA.tsv`, `p3_passB.tsv` (raw, unnormalised), `p3_ciphertext.tsv`, `gloss_pairs.tsv` (+11 rows), `gloss_align.tsv`, `gloss_key.tsv`, crops in `images/crops_p3/`. No reading beyond the graded pairs. Vision calls: 2 subagent passes plus the reconciler's own zooms (6 small native crops and one preview of key 255 f.14) -- 3 units.

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
Read so far: unmeasured. No reconciled ciphertext.tsv exists; key.tsv (key 255 letter table, S) and a provisional ciphertext_f4runs.tsv (the two f.4 runs, single-eye, M) exist since 2 Oct 2026 (A2-HDK3), 36 tokens: 31 M, 5 U. The only committed value is 601 = "Dennemarck" (grade C, glossed 3x on f.4; Cheap test 1). Cheap test 1's "~40 code tokens, ~20 distinct values" was a rough count, and it is an undercount. It excluded 625/774/775 as "section counters", but on a 1000-px preview of image 0003 (this pass, adversarial check, M) 774 and 775 stand inline in the prose with bold glosses above or beside them. It also called f.2 "plain", yet image 0002 carries at least one inline glossed code in its last lines. So any "~3 of ~40 (~7%)" figure is not a measurement. Note that images 0002-0004 are HCPortal image numbers, not checked foliation: 0003 has its binding on the right and faces 0004, so it is a verso.
- ff.2-4 (images 0002-0004), every inline code group that carries a bold interlinear or marginal gloss. On the preview these include 651 (by "Cur Brandenburg"), 653, 229 ("Berlin"), 774, 775 ("Ga. Stadt") and the marginal 625 gloss on 0003; on 0004, 756/768, 229, 427 641 ("herzog von Ploen"), 303, 447 and 834; on 0002 the one group, done 3 Oct 2026 (GAPS152, page 1: 690 with gloss "Bleinenk??l", M, both passes agree on the sign). Image 0003 done 3 Oct 2026 (GAPS155, page 2): 9 groups, all glossed, 9/9 sign agreement: 605 K. Dennemarck, 651 x2 and 653 Kurbrandenburg, 625 (margin gloss unread), 229 Berlin, 690 (recurs from page 1, M), 774 Holland, 775 General-Staaten; held-out check 2/2 vs shuffled-gloss control P=0.11 without the 690 override (4/4, P=0.007, with it): not yet discriminating. Image 0004 done 3 Oct 2026 (GAPS159, page 3): 11 glossed nomenclator pairs (C 8, M 3: 602 Der Konig in Dennemarck, 5756 Franckreich, 601 x2 Dennemarck, 229 Berlin, 681 Cur Brandenb, 768 ?ueco, 437 641 Hertzog von Ploen, 303 alliance, 447 Kayser, 834 Rex Daniae), 47/56 sign agreement before reconciliation; 303 and 229 conflict with key 255; pooled pages 1-3 held-out 8/8 (6/6 without the 690 override) vs shuffled-gloss control mean 0.27-0.37, P<0.0001: discriminating. All three pages are now transcribed and their glosses paired. None of the 0003/0004 codes is pinned code by code - blocker: not-attempted; images at 2600x3944 px are on disk and legible enough that most 3-digit codes visibly carry a gloss, so the gloss coverage is much wider than "1 of 20". Cheap test 1 stopped at a breadth cap, and the iiif_lines.py crop step in its brief (.claude/briefs/runs/2026-09-26-lane-b7-hcp.md, item A) was never pasted. The f4_top/f4_mid crops cited in NOTES are not on disk; next (page 3 done 3 Oct 2026, GAPS159): merge into ciphertext.tsv, build key.tsv rows from legible glosses only (C/M per value), run interlinear_align.py with a held-out check once codes recur, and run `tools/decode_key.py --check`
- f.4 (image 0004), the two dense 2-digit runs and every other 2-digit/doubled-letter group on ff.2-4 (A2-HDK 2 Oct 2026: HCPortal key 255's letter table, 1666, "mit Secretario Lincker", reads both runs in agreement with the letter's own gloss, 21/26 gloss pairs on the 1 Oct readings vs relabelled-table control max 10, 26/26 on native-crop readings; S, see "Known-keys and sibling check" step 5). Still open inside run 1: 6d, LL, 143 against the gloss "stirt", and bb. A2-HDK3 (2 Oct 2026) wrote key.tsv (197 rows, S; 20 = A, nulls 1-19 etc.) and checked it against the period "Scala über den Clavem mit Secretarium Linckern" in DECODE 4690 (120/120 entries agree); decode_key.py --check passes on the provisional f.4 runs (36 tokens: 31 M, 5 U) - blocker: not-attempted; key.tsv and decode.json are in place; next: in the transcription pass, replace ciphertext_f4runs.tsv with the reconciled ciphertext.tsv for ff.2-4, run `tools/decode_key.py --check` and `--split-check`, and list the 2-digit groups the 1666 table does not read (a 1672 revision would show there). ~$0.5 on top of the transcription pass
- Every code group still unglossed after the two steps above (count unknown until the transcription exists) - blocker: not-attempted; no key-rebuild, bracketing or context fill has ever been run, so these cannot yet be called open-codes; next: bracket the 3-digit nomenclator against the gloss-pinned values (is 229 "Berlin" < 601 "Dennemarck" < 651/653 "Brandenburg" < 774 "Holland"(?) an alphabetical order?). Fill slots from the clear German/Latin context, grade S only with a matched code+mark control at the letter's own N, then rerun decode_key.py --check. ~$4
- The 3-digit nomenclator of 1672 (601 Dennemarck, 229 Berlin, groups up to 834). Neither near-date key reads it (A2-HDK 2 Oct 2026: key 255, 1666, runs 180-407 with Dennemarck 184/212 and 229 = Frankreich; DECODE 4692, 1670s, runs 153-363 with Dennemarck 174, Berlin 281). Dänemark 131 sampled 8 of 106 leaves, all clear (Brandt's 1672 reports and the regent's drafts); the undigitised Lyncker files (Preußen 345, 1668; Dänemark 105, 1668; Hamburg 2, 1671-72) are the only same-sender material left - blocker: not-attempted; the gloss-pinned values plus key-rebuild (gap 3) are the in-session route, DECODE 4687/4688/4690/4691 (HStAM 4 d Nr. 1234) opened 2 Oct 2026 (A2-HDK3): 4691 is key 255 itself, 4690 a 1668 key (nomenclator 300-409) plus the Lincker decipher scale, 4688 a Latin cover-word list, 4687 a Paris chiffre note "va jusqu'a 712"; none reaches 834 or has Dennemarck at 601. Arcinsys lookup done 2 Oct 2026 (A2-HDK4): HStAM 4 d Nr. 1236-1238 are digitised but catalogued ca. 1715, mid-18th c. and early 19th c.; the whole 4 d Chiffern node (Nr. 1218-1238, 21 items) holds nothing dated 1671-72 beyond the already-checked 1234/1235, so no archive key for this nomenclator is catalogued there; next: the gloss-pinned values plus key-rebuild (gap 3), after the transcription pass

## Escalation (1 Oct 2026)
- [x] siblings: done 2 Oct 2026 (NEXT-HDK, "Siblings lookup" above). HCPortal has only record 494 for 4f Dänemark, and its keys include no 4f Dänemark key. Arcinsys has Nr. 125 complete at 6 images, so nothing is missing; the cover and endorsement name the sender Lyncker and the recipient Chancellor Vultejus (M). The cached DECODE listings hold no 4 f record. Leads handed on: Dänemark 131 (digitised, same series, gap 4); two near-date chancery keys for known-keys below.
- [ ] clear-pages: not done. The letter's own decipherment is the bold glossing on ff.2-4. It includes a marginal gloss beside the first dense f.4 run, which neither Cheap test 1 nor the classifier used. Only 601 is pinned. Whether the glossing hand is period or modern is unsettled (While waiting bullet 3), and that decides whether gloss values stay C or are a key-source H. The rest of Nr. 125 was never checked for a clear copy or minute. Planned: the gloss read in the transcription pass plus interlinear_align.py on each run.
- [x] known-keys: done 2 Oct 2026 (A2-HDK, "Known-keys and sibling check"). HCPortal key 255 (HStAM 4 d Nr. 1234 ff.13-16, endorsed "Clavis ... mit Secretario Lincker 1666") reads the letter's 2-digit letter cipher against its own gloss (21/26 vs control max 10 on pre-key readings; S); its nomenclator (180-407) does not read the 3-digit groups, nor does DECODE 4692 (Nr. 1235, 1670s, 153-363, names Linker 190, Vultejus 246, Resident Brand 231). DECODE 4687/4688/4690/4691 (Nr. 1234) opened 2 Oct 2026 (A2-HDK3): no nomenclator reaching 834; 4691 = key 255; 4690 holds a period decipher scale of the Lincker letter table that agrees with key.tsv on all 120 entries read. key.tsv written (197 rows, S). Not opened: key_519 and hcportal_522 (superseded for the letter table by key 255). HStAM 4 d Nr. 1236-1238 looked up in Arcinsys 2 Oct 2026 (A2-HDK4): digitised, but dated ca. 1715 / mid-18th c. / early 19th c.; the 4 d Chiffern node has no other 1670s key.
- [ ] print: not done. Only one OpenAlex and one Semantic Scholar query were run (intake 5-6, 0 hits). No edition, calendar or documentary series was searched. Candidates come from the letter's own content (an envoy writing from Hamburg 4/14 May 1672 to a Hessian chancellor about the Danish king, Brandenburg, the Dano-Brunswick foedus and the Plön duke): Urkunden und Actenstücke zur Geschichte des Kurfürsten Friedrich Wilhelm von Brandenburg, and Danish state-paper calendars. Sender and recipient are now named (Lyncker to Chancellor Vultejus, M, siblings lookup 2 Oct 2026), which gives searchable names. Planned: tools/print_check.py with phrases from the transcribed clear prose, ~$2-3.
- [ ] key-rebuild: never tried. No transcription exists; key.tsv holds only the letter table (2 Oct 2026). Planned: gloss alignment, then nomenclator bracketing and LM context fill with a matched control on any S claim, ~$4.
- [ ] image-check: not done. No sign-by-sign transcription exists. The crops f4_top.jpg/f4_mid.jpg cited in Cheap test 1 are not on disk, and no iiif_lines.py output was pasted. The doubtful tokens "6d", "bb" and "96" in the f.4 runs, and the 625/774/775 "section counter" exclusion, need re-reading against the native image. Planned: as gap 1, ~$11.
- [ ] retry: nothing to retry yet, because no key extension exists. Planned: after the gloss read and the key-rebuild, rerun every code group and every M lead through decode_key.py and regrade per token.
Verdict: keep going: 4 internal gaps; cheapest next: merge p1/p2/p3_ciphertext.tsv into one ciphertext.tsv (replacing ciphertext_f4runs.tsv), apply key.tsv to every 2-digit and doubled-letter group, run `tools/decode_key.py --check` and `--split-check`, and list the 2-digit groups the 1666 table does not read, ~$0.5, script only (pages 1-3 transcribed and glossed 3 Oct 2026, GAPS152/155/159; pooled held-out 8/8, 6/6 without the 690 override, P<0.0001)

## Web and blog check (GF-A2-1, 2 Oct 2026)

Run 2 Oct 2026, 21:21-21:23 UTC (date -u; committed 1e2c3b77), by worker GF-A2-1 (account 2, LANE-A2PUSH). Plain web searches (one search engine):
1. `Lyncker Vultejus Hamburg 1672 Chiffre Dänemark Hessen-Kassel Brief` (sender + recipient + date) -- hits: Rijksmuseum
   portraits of Hermann Vultejus, books2ebooks records for N. C. Lyncker's later treatises (1686, 1692), museum-digital and
   Halle opendata portrait records. Nothing on the 1672 letter.
2. `"Dänemark Nr. 125" OR "4 f Dänemark" Marburg Chiffre OR verschlüsselt 1672` (shelfmark + cipher) -- hits: TNA blog
   "secret diplomatic message deciphered after 350 years" (an English item, not this one), HistoCrypt papers 392/152/704,
   Heidelberg EIP documents, Tartu dspace, sale listings; no hit names this shelfmark.
3. `hcportal 494 hstam Daenemark 1672 nomenclator partially solved` (record + title) -- no relevant hit (philatelic and EU
   document pages); the HCPortal record itself was read live on 26 Sept 2026 (Search log item 4: no reader, key or note).
4. `"Hesse-Kassel" Denmark 1672 letter enciphered passages decipherment` (folder's descriptive title) -- hits: Cipherbrain
   "Solved: The encrypted letter from Carl von Rabenhaupt" (1646, a different Marburg item, already logged at intake item 3),
   HistoCrypt 152 (Rabenhaupt; abstract read: no 1672/Dänemark/Lyncker/HCPortal 494 mention), Waldispühl's Heusner von
   Wandersleben 1637 paper (dspace.ut.ee 253c0934, PDF fetched, grepped for 1672/Dänemark/Lyncker/Vultejus/494: 0 hits),
   HistoCrypt 402, a Cristin record.
No decoded phrase searched in quotes: only one value (601 = "Dennemarck") is read, no running text exists.
Blog site searches: **Cipherbrain** (`site:scienceblogs.de klausis-krypto-kolumne Hessen Kassel Dänemark 1672 OR Marburg
Staatsarchiv verschlüsselt`) -- monthly archives, author/category pages and "Unsolved cryptograms from the Thirty Years War
(2)" (2018; 1618-48, outside 1672); the one Marburg post found is the Rabenhaupt solution (1646); **Cryptiana blog**
(`site:cryptiana.blogspot.com Hesse OR Hessen OR Denmark 1672 cipher`) -- no blogspot hit (HistoCrypt 705 "On the
Combination of Cryptography and Steganography in 17th Century Germany", Tartu items, TNA catalogue entries); Tomokiyo's pages
on disk were grepped at intake (item 3: only Rabenhaupt 1646 and a 1637-41 Habsburg mention); **Cipher Mysteries**
(`site:ciphermysteries.com Hesse-Kassel OR Marburg OR Denmark 1672 cipher letter`) -- no ciphermysteries.com hit at all.
No comment thread found carries a decipherment or plaintext of HStAM 4 f Dänemark Nr. 125; the Rabenhaupt post's thread is
about the 1646 letter.
Requests: ecp.ep.liu.se 1, dspace.ut.ee 1, search engine 8.

## Premise check (GF-A2-1, 2 Oct 2026)

(a) Decipherments the folder already mentions -- **found (known): the letter's own glossing, partial.** The bold interlinear
and marginal glosses on ff.2-4 (images 0002-0004) are a decipherment of part of this letter (601 = "Dennemarck" 3x; 229
"Berlin", 651 by "Cur Brandenburg", 427 641 "herzog von Ploen", a marginal gloss beside the first dense f.4 run; Cheap test 1
and Remaining gaps). They are not complete: many groups, incl. most of the two dense f.4 runs, carry none on the previews, and
whether the glossing hand is period or modern is unsettled. HCPortal 494's "Partially solved" is unattributed (no reader,
note or key). So: a partial period-or-later decipherment sits on the leaves themselves; the item is not shown found-solved,
but every glossed group is a C-grade value once the gloss hand is settled (the Verdict's clear-pages step).
(b) Other solvers' working files -- **found, nothing beyond a catalogue line.** Shallow clone of dbourdeau/cyphersolver
(2 Oct 2026, 21:16 UTC): CATALOGUE.md row 341 and `research/oldest/scan_2026-09-23/hard_targets.md` item 12 ("HCPortal partial
solution only (details on the record); no publication found ... Not in repo"); `targets/` holds hesse1603 and hesse1824
(other items), no folder, rendering or key for Nr. 125. aaymeloglu/unsolved-ciphers: grep for Hessen/Hesse/Dänemark/Marburg
pairings, 0 hits on this item (cited only).
(c) Physical neighbours -- **checked, not found.** Nr. 125 is complete at 6 Arcinsys images (NEXT-HDK): 0001 modern cover,
0002-0004 the letter, 0005 the endorsed verso (no cipher, no clear copy, no slip), 0006 an unrelated 1738 print. No clear
copy or separate decipherment is bound in the file. The digitised neighbour Dänemark 131 (1671-74) is unopened.
(d) Recipient side -- **not found.** The recipient is the Hessian chancellor Vultejus at Kassel; no edition of his incoming
correspondence or of the Hessian chancery's 1672 Danish files was located (search 1; OpenAlex/S2 at intake, 0 hits).
Danish-side editions were not searched: the letter went from a Hessian envoy at Hamburg to Kassel, so a Danish edition would
not hold the recipient's copy.
