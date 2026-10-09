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

**Verifier note (VERIFY-HDK, 3 Oct 2026; AUDIT.md):** the 8/8 above counts each agreeing pair twice. It is 4/4 agreeing pairs on 4 recurring codes (690, 651, 229, 601), 3/3 without the circular 690 override; chance per pair 0.047, so the consistency result stands, but quote it as "3 recurring codes consistent", not as 8 tests.

## GAPS163-hessen-daenemark-1672 (3 Oct 2026, account-4): merged ciphertext.tsv, gloss-derived key, decode_key --check

Script only, no vision, no subagents. `keys/merge_pages.py` merges `transcription/p1-p3_ciphertext.tsv` into
`ciphertext.tsv`: 65 groups, line id `pN_L`, with the sign, its confidence and the gloss. It also writes
`key_gloss.tsv`, 18 nomenclator rows pinned by the letter's own bold-hand glosses: C 11, M 6, I 1. `--check` exits 1
when either file is stale. `decode.json` now has one job, ciphertext.tsv with keys [key.tsv, key_gloss.tsv] (no code
sits in both). `ciphertext_f4runs.tsv`, `reading_f4runs.txt` and `reading_f4runs_tokens.tsv` are superseded and
removed; their corrections are listed under GAPS159. `python3 tools/decode_key.py ciphers/hessen-daenemark-1672 --check`
gives "tokens 65: C 9, I 1, M 21, S 30, U 4 / reading up to date", exit 0. `--split-check` (written to
`split_check.tsv`) flags 3 tokens, 4 occurrences: 625 x2 (unkeyed; its margin gloss on p2 is unread), 7480 (margin,
probably not a code) and I (p3:20.12, unkeyed). None of these is a glued pair of the table's codes that the context
supports.

Coverage: 61 of 65 tokens are keyed (93.8%).
- **Nomenclator** (3- and 4-digit codes above the letter table, 26 tokens): 23 keyed by the gloss key and 3 unkeyed
  (625 x2, 7480).
- **Letter cipher** (2-digit groups, doubled letters, and 3-digit codes up to 179; 39 tokens): 38 keyed by key.tsv
  (1666 table, S) and 1 unkeyed (I).

Unglossed groups and the gloss-derived key:
- **602 at p3:26.3** reads [Konig_in_Dennemarck] (M) from p3:1's gloss.
- **634 at p3:17.2** is filled at I. The run-1 margin gloss "disgustirt / unvertanin / Holstein" puts its third word
  where 634 stands, the run's only nomenclator group before 601. This is inferred, not read.
- **68 at p3:2.2** reads e by the letter table (M; context "mit ey68.").
- **625 x2** and the margin **7480** stay unread.

Conflicts with key 255 at 229 (letter: Berlin, C, 2/2; key 255: Frankreich) and 303 (letter: allian?e, M; key 255:
Munster, M) are logged with their witnesses in `HYPOTHESES.md` (rule 4) and are not merged.

What the decoded stretches say (grades in reading_tokens.tsv):
- **Nomenclator.** The 23 keyed nomenclator tokens read the glosses back: Dennemarck / K. Dennemarck / Konig in
  Dennemarck / Rex Daniae, Cur Brandenburg (three codes), Berlin x2, Holland, Gen. Staaten, Franckreich, Kayser,
  Hertzog von Ploen (a pair), alliance, ?ueco, and Bleinenk?l x2. This is the period gloss restated (C where the
  gloss is legible and both passes read it), not an independent decipherment.
- **Run 1** (p3:15-17) reads by the 1666 table "d i s g u a i r t u n d e r t a d i n [Holstein] [Dennemarck]"
  (S, with 60 = a and 113 = r and 66 = d at M), beside the margin's "disgustirt / unvertanin / Holstein". It matches
  the margin closely, except at 60 (table a, margin "st") and 66 (table d, margin "n"); both signs are M on the image.
- **Run 2** (p3:20-21) reads "[?ueco] h o k g e b d a s a [I] / w o l a b l u" under the group-by-group gloss
  "gott geb das amm.. / w o .. a b l au t".

Letter-table check against the letter's own per-group letter glosses (p3 runs, 7 groups with a gloss of their own):
5 agree (YY w, 96 o, 30 a, 32 b, 110 l) and 2 disagree. These are 55 (table h, gloss g) and 6 (table NULL, gloss t);
69 (table k) also sits under the gloss "ott". So at most three 2-digit groups differ from the 1666 table. That fits
either a 1672 revision of a few cells or misread signs (55/53, 6/7?); it is not settled here. This is not a control-
backed test (no shuffled-gloss control at N=7); the A2-HDK 26/26 result with its relabelled-table control remains the
letter table's support.

Reading ready (for a separate verifier): yes. The target now has a graded reading with 9 tokens at C from the letter's
own glosses, and a letter-cipher run at S that agrees with its marginal gloss. Two caveats. No judge spec exists for
this target (`specs/` has none), and the decoded text is names plus three short runs, not prose. Whether the glossing
hand is period or later is still unsettled (While waiting); that changes the source label, not the C grade (known
plaintext). No status change by this worker. Rule 10: report only; nothing here says new or first.

**Verifier note (VERIFY-HDK, 3 Oct 2026; AUDIT.md):** class N0, key `period`, text known -- the leaf carries its own period decipherment (the bold glosses); this reading transcribes it and identifies the 1666 letter table, it is not an independent decipherment. Re-derivation reproduced. A selection-free LCS test (keys/verify_hdk_controls.py) confirms key 255's letter table on both runs (17/20 and 14/21 vs control max 12 and 11). Two cells the letter's own gloss contradicts were regraded S -> M in exceptions.tsv (p3_20 pos 2 = 55, p3_21 pos 7 = 6); tokens now C 9, I 1, M 25, S 28, U 2.

## GAPS168-hessen-daenemark-1672 (3 Oct 2026, account-4): native-zoom re-read of the 625 margin gloss and of run 2

Two vision calls by the worker itself (no subagents), on crops cut from the native images on disk with PIL:
image 0003 x 0-1300, y 1150-1450 (the margin beside p2:7) and image 0004 x 100-1500, y 2390-2750 (p3:20-21).

- **625 margin gloss.** The margin repeats "625" and carries two words in the bold hand. Word 2 reads
  **Ahlefeldt**; that agrees with pass B's "Ahl?feldt?" (two eyes, M). Word 1 is a Kurrent word of 9-10 letters
  ending -halt?/-stelt. "Stathalter" is possible but rests on one eye, so it stays unread. The context ("und hat
  625. hierbey signalirte dienste gethan") is a person. Frederik von Ahlefeldt was the royal Danish Statthalter in
  the duchies at this date, but that identification is inference (I) and is not in the key. key_gloss.tsv now has
  `625 = [?_Ahlefeldt]` at M (19 rows: C 11, M 7, I 1). Both 625 tokens now decode at M; p3:4 has no gloss of its
  own. `decode_key.py --check` gives tokens 65: C 9, I 1, M 23, S 30, U 2, "reading up to date", exit 0.
  `merge_pages.py --check` exits 0. `--split-check` now flags 2 tokens (7480, I), down from 3.
- **Run 2, 55 / 69 / 6.** On the zoom, **55** is clearly two flat-topped 5s, not 53. The 1666 table gives 53 = g and
  55 = h. The gloss above it is clearly "g", with "ott" over the following 76 (table o). So the 55-vs-g difference
  is not a misread sign. It is either the encipherer's slip (55 for 53) or a changed cell. **69** (table k, under
  "ott") lies at the crop's right edge and was not re-read. **6** (table NULL) on p3:21 reads as "6." with "t"
  above it (sign M, right edge of the crop). Read by the gloss, the run says "gott geb das a... / wol abl[au]t". In
  context this is "Gott geb, dass a[lles] wol ablauft". That sentence is a context reading (I), not a decode.
  Under the table, 55, 69 and 6 still give h, k and NULL. No table revision is made from one occurrence per cell,
  and key.tsv is unchanged.

Rule 10: nothing here is called new. The Ahlefeldt identification is not looked up in any edition.

## GAPS176-hessen-daenemark-1672 (3 Oct 2026, account-4): is the 1672 nomenclator any key list on disk or in DECODE?

No vision calls and no subagents. Script: `keys/nomen_list_match.py` (output `keys/nomen_list_match.tsv`, `--check` exits 0).

- **Test.** The 18 gloss-pinned nomenclator rows of key_gloss.tsv (C 11, M 7; the I row 634 is left out) are
  scored against every key table tools/key_crossmatch.py discovers. That is 224 tables: all ciphers/**/key*.tsv,
  tools/keys/key60.tsv, the Cryptiana tables and the uscodes legation key, and this folder's own two keys are
  excluded. A hit means the key maps the code to a value matching the gloss's name stem (German, Latin or French
  spelling: e.g. denne/dän/dania, brandenb, holl, staat/etats, franck/galli). **Control:** the same key is scored
  against the glosses after a random reassignment among the same codes, 1000 shuffles. A shuffle changes which value
  each code is checked against, so the control count can differ from the real one. Gate: real >= 3 and real > the
  shuffle p99.
- **Positive control** (`--selftest`). A 300-row decoy key is planted with k of the letter's own gloss values at
  their codes. Real/p99 for k = 3, 4, 6 and 9 is 3/2, 4/2, 5/2 and 8/3. All four are flagged CANDIDATE, so the gate
  catches a list sharing as few as 3 of the 18 values.
- **Result.** 224 keys, 0 candidates, **0 real hits in total**. Only 14 keys contain any of the 18 codes at all (at
  most 6, na-janssens-java-1811). None of them gives a matching value at any code, and every shuffle p99 is 0. **No
  key list held as a table on disk is this nomenclator.**
- **DECODE metadata, login-free** (sources/decode/keys-all-2026-09-28-merged.tsv, 6,324 key records, grepped for
  Marburg/Kassel/Hessen/Denmark/Danish holders). There are 256 such rows. The ones dated within 1650-1690 or undated
  are exactly 4687, 4688, 4690, 4691 (HStAM 4 d Nr. 1234) and 4692 (Nr. 1235). All five were opened on 2 Oct 2026
  (A2-HDK, A2-HDK3), and none reaches 834 or has Dennemarck at 601. The 4 d Nr. 1218 run stops at 1652, and Nr.
  1236-1238 date from ca. 1715 or later. No Danish-held key in the listing falls inside 1650-1690. **DECODE has no
  unopened candidate.** Key 255 and 4692 are not tables on disk, only images. They were compared by eye on 2-3 Oct
  (229 = Frankreich vs Berlin; Dennemarck at 184/212 and 174 vs 601), and they stay "different list", logged in
  HYPOTHESES.md.
- **Limit.** The test only sees lists that exist as code-to-value tables, plus the DECODE catalogue's dates and
  holders. A Danish-side key (Rigsarkivet, Tyske Kancelli) or one of the undigitised Lyncker files (Preussen 345, 1668;
  Daenemark 105, 1668; Hamburg 2, 1671-72; gap 4 below) is outside it. These need the archive, which is an outside
  blocker (needs-physical-access).

Rule 10: nothing here is called new. Requests: none to any host (all on-disk).

## GAPS188-hessen-daenemark-1672 (3 Oct 2026, account-4): print check

No vision calls and no subagents. Ran `tools/print_check.py` with `phrases.txt` and `sources.tsv` (4 target phrases and 2 positive controls). Full table: AUDIT.md
"Addendum: print check".
- Positive controls read on IA (listed item and all items) and on Google Books. They **missed on OpenAlex**, so OpenAlex's phrase
  negatives are non-tests (rule 3). Semantic Scholar returned 429 after 3 requests and was not retried.
- Target phrases: 0 phrase hits on IA and IA-global. Google Books has 0 for "disgustirt und vertanin holstein". Its other three phrases
  return only scattered-word volumes (a 1722 lexicon, hymnals, Pufendorf), which are not the phrase.
- Ribbeck, *FBPG* 12 (the AUDIT's open lead) covers Lincker at Berlin in **1666-1669** (IA full-text title hits), not
  Hamburg in 1672.
- Class stays N0 (AUDIT.md). Rule 10: "not found by print_check.py on IA, Google Books, OpenAlex and CrossRef on 3 Oct 2026". This is a search result.

## GAPS193-hessen-daenemark-1672 (3 Oct 2026, account-4): bracketing the unglossed groups against the gloss-pinned values

Script only: no vision calls, no subagents, no network. The prereg `PREREG-GAPS193.md` (statistic, control, gate,
licences) was pushed as commit 4ea2abe1 before anything was computed. Its disclosure: the topical statistic was chosen
after the codes had been seen. Script `keys/bracket_gaps193.py`, output `keys/bracket_gaps193.tsv` (seed 193;
`--check` re-runs the full control, about 9 minutes of CPU). Rule 3 third-attempt clause: this is attempt 1, since no
bracketing had been run before.

Testable codes: the 16 gloss-pinned codes at C or M, leaving out 690 (referent unidentified), 634 (I) and 625 (both
under test). The matched code+mark control is 1,000 synthetic letters of K = 16 codes in 200-849 with the same headword
and topic multiplicities, run under a structured design (power) and a two-part random design (size), at gloss noise
0, 0.2 and 0.4. The M share among the 16 codes is 0.375.

| statistic | target | target p | control power (noise 0 / 0.2 / 0.4) | control size (noise 0 / 0.2 / 0.4) | gate |
|---|---|---|---|---|---|
| S1: Kendall tau, code vs headword alphabetical rank (one-part order) | tau 0.194 | 0.172 | 1.000 / 0.989 / 0.807 | 0.051 / 0.047 / 0.040 | control passes; target fails: **control-backed negative** |
| S2: same-topic adjacent pairs (topical blocks) | 5 of 15 pairs | 0.014 | 1.000 / 0.769 / 0.318 | 0.017 / 0.026 / 0.016 | control power 0.318 < 0.8 at noise 0.4: **non-test at this N** |
| S2 sensitivity, DK and HOLST merged (not gated) | 6 | 0.022 | - | - | - |

- **S1.** The nomenclator is not a one-part alphabetical list at K = 16. A matched one-part list would have been seen at
  power 0.81 even at 0.4 gloss noise. So no alphabetical window can bracket 625 or 634.
- **S2.** Same-topic codes do sit together (DK 601/602/605, Kurbrandenburg 651/653/681, Holland/Gen. Staaten
  774/775), with p 0.014 against a shuffle. But at 16 codes and this letter's M share, the control cannot reach
  power 0.8, so under the prereg's gate S2 licenses nothing. 625 and 634 do lie between 605 (DK) and 641 (von Ploen).
  That is recorded as an observation and is not used as support.
- **No key change.** 625 stays [?_Ahlefeldt] at M and 634 stays [Holstein] at I. `tools/decode_key.py
  ciphers/hessen-daenemark-1672 --check` gives tokens 65: C 9, I 1, M 25, S 28, U 2, "reading up to date", exit 0.
- **Out of scope by the prereg.** 68 is a 2-digit letter-table group (reads e, M, unchanged), not a nomenclator code.
  7480 is a 4-digit margin number with no bracket either side.
- **Gap 2's next step cannot be run in this letter.** 55, 69 and 6 each occur once in ciphertext.tsv, and 53 does not
  occur at all. So "another occurrence reads g/t/t" has no second occurrence to test.

Rule 10: report only, and nothing here is called new.

## GAPS199-hessen-daenemark-1672 (3 Oct 2026, account-4): second blind native-zoom read of the 625 margin word 1

Prereg `PREREG-GAPS199.md` (commit a2d13f3e, pushed before the read). Six equal-size crops (420 x 100 px, native, cut with
`tools/iiif_lines.py --image ... --region R --centres C --lines-per-crop 1`, commands in the prereg) went to one blind Opus
subagent call: the target and 5 decoys (settled C-grade glosses of the same hand), shuffled with seed 199. The map is
{"X1": "t", "X2": "a", "X3": "d", "X4": "e", "X5": "c", "X6": "b"}, and its sha256 prefix matches the prereg.

| crop | what it is | blind best reading (confidence) | gate |
|---|---|---|---|
| X2 | decoy p2:3 Cur Brandenburg | Cur Brandenburg (medium) | correct |
| X3 | decoy p2:28 Gen. Staden | Gen. Staden (medium) | correct |
| X4 | decoy p2:2 K. Dennemarck | K. Dennemark (medium) | correct |
| X5 | decoy p2:28 Holland | holland (medium) | correct |
| X6 | decoy p2:17 Berlin | Berlin (medium) | correct |
| X1 | **target, 625 margin word 1** | **geschehet?** (low), letters g e s ? ? e ? e t; alternatives gestellet, geschehen, gesichert | disagrees |

The decoy gate passes at 5/5, so the read is a real test. The target does not normalise to stathalter: edit distance
well above 2, a different word. Under the prereg, 625 stays `[?_Ahlefeldt]` at M, word 1 stays unread, and no key
change is made. `decode_key.py --check` still exits 0 (unchanged files).

The five reads of word 1 so far:
- GAPS155 pass A: gesandschaffter? (blind)
- GAPS155 pass B: y?rkestelr? (blind)
- the reconciler: ?-?-?-?-stelt
- GAPS168: -halt?/-stelt, Stathalter possible (one eye, context known)
- GAPS199: geschehet?/gestellet (blind)

Two blind reads begin "ge-s" and two give a -stel- ending. "Stathalter" is the only one of the five that came from a
reader who knew the context. That pattern is a description of the reads, not a reading (I at most): a past participle
such as "gestellt" is one possibility. The targeted native-zoom method is [retired] for this word (rule 3,
third-attempt clause, as preregistered). Only a different instrument reopens it, such as a sign-by-sign atlas of this
hand or a palaeographer. Vision calls: 1 subagent call, plus the worker's own low-resolution previews to place the crops.

## D4-HDK (7 Oct 2026, account-4): Escalation key-rebuild step, context fill with a held-out control

Script only, disk only: no network, no vision calls, no subagents. Prereg `PREREG-D4HDK.md` (commit 9a91d4a1d) was pushed
before any score. Script `keys/context_fill_d4hdk.py` (`--check` regenerates `keys/context_fill_d4hdk.tsv` and fails if stale).
- **What was left untried.** The stale Escalation line said no transcription exists. In fact the gloss alignment (GAPS152-163)
  and the bracketing (GAPS193) were done, and the 625 margin re-read was retired (GAPS199). Only an LM context fill was untried.
  Targets: 625 (p2_7, p3_4), 634 (p3_17), 602 (p3_26.3). Out of scope: 68 (a letter-table group) and 7480 (a margin number, no
  context).
- **Instrument.** A word-bigram model on `tools/data/de17` (1631-1660s German diplomatic print, spelling folded), scoring 28
  fixed candidate referents from the nearest prose word on each side.
- **Control first.** 14 occurrences of C-grade gloss-pinned codes, each ranked among the 28 by its own context:

| statistic | control (14 held-out C tokens) | shuffled-context null (1,000, seed 4) | prior-only | gate | verdict |
|---|---|---|---|---|---|
| top-1 | 0.071 (1/14: 651 at p2_3) | - | 0.000 | >= 0.50 | FAIL |
| MRR | 0.208 | p95 0.314 | - | > null p95 | FAIL |

- **No target value scored for the key.** The target ranks are in the TSV for the record only and are graded nothing (all
  four put "Konig" first, the same as most control tokens: the model ranks by a frequent referent, not by context).
- **Retry.** `tools/decode_key.py ciphers/hessen-daenemark-1672 --check`: tokens 65: C 9, I 1, M 25, S 28, U 2, reading up to
  date, exit 0. No regrade; key.tsv and key_gloss.tsv unchanged.
- **Why it fails.** The contexts are one function word each side ("zwischen _ und", "nach _ gehet"). Those do not separate
  proper names in a 354k-word corpus where 6 of the 28 referents (Ahlefeldt, Bleinenkehl, Griffenfeld, Gottorf, Ploen, Gabel)
  barely occur. Escalation key-rebuild is now [retired] with the instruments named. It reopens only with new material (more
  gloss-pinned codes of the same list, gap 4) or a different instrument.

Rule 10: report only, and nothing here is called new. Requests: none (disk only).

## HDK-131 (9 Oct 2026, 00:17-00:3x UTC by date -u; LANE FAMILY-A2d, account 2): full sweep of Dänemark 131

Prior work: `python3 tools/prior_work.py hessen-daenemark-1672 --item-spec 'shelfmark=HStAM 4 f Staaten D Daenemark 131;sender=Brandt'
--step-type read --fetch` exit 2: plaintext KNOWN from AUDIT.md:225 (that line is Nr. 125's own class, not this volume), step LEAD
= my own claim line; LOOK 2-leaf (no gloss check recorded for this unit), UNCHECKED 3-tomokiyo/3-solver/4-editions (no folio or
R-id on the unit). Checks by hand: (1) own work: only A2-HDK's 8-leaf sample (Known-keys and sibling check item 3), all clear;
the remaining 98 leaves were never looked at, so the step was not already done. (2) leaf/neighbours: this sweep is that check.
(3) solver repos and Tomokiyo: the Premise check (GF-A2-1) grepped both for this target; nothing names Dänemark 131. (4) editions:
none known for Brandt's reports to Kassel; unchecked beyond that.

Method: the 98 unsampled leaves (0001-0106 less 0003 0016 0029 0042 0055 0068 0081 0094) fetched once from
digitalisate-he.arcinsys.de (3500 px long side, kept in the scratchpad, not committed; URL pattern and leaf list in
images/manifest.json), shrunk to 1000 px and shuffled (seed 131) into 12 contact sheets of 9 with Nr. 125's images 0003 and 0004
placed blind among them; one look per sheet ("numeral code groups or glosses over them; none/light/heavy"); the leaf map read
only after all 12 calls were written down. **Positive control: 2/2** (both Nr. 125 images called heavy + glossed, on sheets 1 and
2), so 9 per sheet was small enough and no halving was needed. Three native-resolution crop looks (0020 head, 0020 code block,
0049 slip). Per-leaf result: `dk131_inventory.tsv`.

Result (M throughout; no transcription, no decoding):
- The cover (0001) reads "Acta der Landgräfin Hedwig Sophie ... 1671-72-73-74, Correspondenz mit dem Chur-Brandenburgischen
  Residenten zu Coppenhagen Friedrich von Brandt": Brandt was the Elector of Brandenburg's resident at Copenhagen, writing to the
  Kassel regent; the volume also holds her drafts to him, a Latin treaty copy and a Christian V letter of 4 Feb 1671.
- **Seven leaves carry numeral cipher: 0020, 0021, 0049, 0050, 0062, 0063, 0064 (heavy 4, light 3; 0050 doubtful).** The
  8-leaf sample of 2 Oct missed all of them (it fell between them). 91 of 98 swept leaves: none.
- 0020 (spread with 0021, Brandt, Copenhagen, signed 27 Feb 1672, pr. 9 March; M): about 30 lines of dotted groups on the right
  page, mostly 2-3 digit values from about 32 to 170 with a few higher groups (198, 259, 262, 272), mixed with clear words
  ("sonderlich", "auch", "undt", "da die"). **A running German decipherment stands in the left margin** line by line (from
  the crop: "... Herzog de Jorck ... Prinzessin ...", "daher kommen sonderlich vor gestern die tragedie vom König in England
  Carl Stuard agirt ... mit Gülden ... auf englische manier ... und andere Cavallieren ... die masquen ab, da die tragedie"),
  plus interlinear glosses over some groups.
- 0049 (Brandt, Copenhagen, 22 June 1672; M): an inserted slip opens with four lines of groups, **each group glossed with one
  letter above it** in a lighter ink ("[s]chwanger wirt", "...z meist", ...) -- a letter-for-group decipherment, i.e. known
  plaintext pairs. Groups 42 73 144 35 94 67 56 120 are glossed c h w a n g e r; key.tsv (key 255) gives b r y h n i d w for
  them: 1/8 agree (94 = n), so Brandt's letter table is **not** key 255's table. The left page foot of 0049 has about four more
  lines of groups.
- 0021, 0062, 0063, 0064 (sheet level only): blocks of 4-9 lines of numeral groups at the head of a page; whether they are
  glossed was not settled at sheet scale (0064 shows small marks over some groups).
- Code range against Nr. 125: Nr. 125's nomenclator runs to 601/605/651/690/774/834 and its letter table is key 255 (20-166);
  Brandt's groups are mostly 32-170 with a few 198-272, and the one testable letter pair set disagrees with key 255. So this is
  a different correspondent's cipher (the Brandenburg resident's, M), not Lyncker's: it does not read Nr. 125's 3-digit
  nomenclator and gives no value for 625/634/602. Whether the Kassel decipherer's glossing hand is the same on both is not
  checked.
- What it is: a separate, glossed cipher correspondence of 1672 in the same chancery -- at least two leaves (0020, 0049) with a
  period decipherment on the leaf. Not called new or unread anywhere (rule 10); no check-solved has been run on it.

Requests: digitalisate-he.arcinsys.de 1 HEAD + 98 GET, 2 s apart, all 200, no challenge. Vision: 12 sheet looks + 3 crop looks.
Suggestion (not run, rule 7 of Usage): a check-solved and a breadth spec for "Brandt to Hedwig Sophie 1672 (HStAM 4 f Dänemark
131 ff. 0020-0064)" as its own target, with the 0049 slip and 0020 margin as known-plaintext pairs for interlinear_align.py.

## HDK-BRANDT check-solved (9 Oct 2026, 00:41-00:5x UTC by date -u; LANE FAMILY-A2d, account 2)

Item: Friedrich von Brandt (Brandenburg resident at Copenhagen) to the Kassel regent Hedwig Sophie, 1672, numeral cipher on HStAM 4 f Staaten D
Dänemark Nr. 131 leaves 0020 0021 0049 0050 0062 0063 0064 (HDK-131, dk131_inventory.tsv). Considered as one candidate, not a new folder.
**Verdict word: open** (conditional, see the two gaps below). Nothing found that reads, keys or prints any of these leaves' cipher.

Prior work: `python3 tools/prior_work.py hessen-daenemark-1672 --item-spec 'shelfmark=HStAM 4 f Staaten D Daenemark 131;folio=0020;date=1672-02-27;
sender=Friedrich von Brandt;recipient=Hedwig Sophie' --step-type lookup --fetch` exit 4: plaintext KNOWN is AUDIT.md:225 (Nr. 125's own class, not this
volume); LEAD rows = HDK-131's and this claim (neither covers a lookup); 3-tomokiyo CONTEXT hits are other letters' "f.20"; UNCHECKED-NET rows 3-solver /
4-editions are answered below by hand (`--record` not run: the item-spec is ad hoc, no items.tsv row).

Checks, one line each (route, query, result):
1. Own work: grep of the folder, HDK-131 section and dk131_inventory.tsv: seven leaves flagged, nothing keyed, nothing decoded, no earlier check-solved on
   Dänemark 131 (the Premise check GF-A2-1 (c) listed it as unopened). Not already done.
2. HCPortal: `api.hcportal.eu/api/cryptograms` (3 GETs, Accept: application/json; the paging parameter is ignored, the list returned is the same 1,875 names
   each time): names matching Dänemark/Denmark/Brandt/Copenhagen/Hessen/Marburg/1672 = `hstam_4_f_daenemark_nr_125_0002-0004` (id 494, Nr. 125, the other
   item) and `The Copenhagen cryptogram` (id 4, a different item); no Dänemark 131 record. The cached solver-repo copy of the HCPortal keys index
   (cyphersolver research/catalogue_harvest/hcportal/keys_index.txt) lists only the HStAM 4 d Nr. 1218 keys and nothing from 4 f.
3. DECODE: no login; cached listings sources/decode/records-*-2026-09-24.tsv grepped for Marburg/HStAM/Hessen/Dänemark/Brandt/Copenhagen: only
   Hstam_4_d_nr_1218 records (1635-52); key listings only 4 d Nr. 1234-1238 (A2-HDK3, already logged). No record for Dänemark 131 or Brandt (listing date
   24 Sept 2026, 28 Sept for keys; not re-crawled today).
4. Solver repositories, fresh shallow clones 9 Oct 2026 (grep only): dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers for daenemark/dänemark/
   brandt/hedwig/hessen/hesse-kassel/marburg/hstam: cyphersolver hits are CATALOGUE.md #341 (Nr. 125, 4 May 1672), hard_targets.md item 4 (HStAM 4 h
   Nr. 1411, Malsburg 1636) and the HCPortal/DECODE index files above; unsolved-ciphers hits are DECODE catalogue rows for Hstam_4_d_nr_1218/1236-1238 only.
   Neither names Dänemark 131, Brandt or Hedwig Sophie; no "next step" line on this item.
5. Web (4 searches, standard mode): "Friedrich von Brandt Resident Kopenhagen 1672 Hedwig Sophie ... Chiffre"; ""Dänemark 131" OR "Daenemark 131" Staatsarchiv
   Marburg 4 f Brandt Coppenhagen Chiffre"; ""Friedrich von Brandt" brandenburgischer Resident Kopenhagen 1672 Urkunden und Actenstücke"; "Carl Stuart tragedie
   König Kopenhagen 1672 Brandt cipher decipherment ... Cipherbrain OR Cryptiana OR ciphermysteries". Hits: Deutsche Biographie entries of Christoph and
   Eusebius von Brandt (Brandenburg diplomats, Paris and Warsaw, other persons), the 1772 Struensee/Enevold Brandt affair, Riedel/Paderborn PDFs. Nothing on
   Friedrich von Brandt's 1672 letters or any decipherment of them. Blog site searches were not run separately this pass (the GF-A2-1 "Web and blog check"
   above covers Cipherbrain, Cryptiana blog and Cipher Mysteries for the folder, 2 Oct 2026, and found nothing on Brandt; Tomokiyo's pages on disk
   were grepped by prior_work: no Brandt/Dänemark hit): the blog threads are therefore **checked for the folder, not re-read for Brandt**.
6. Editions, read by this worker from the Internet Archive djvu text (downloaded, grepped; not page-read): *Urkunden und Actenstücke zur Geschichte des Kurfürsten
   Friedrich Wilhelm von Brandenburg*, vols 7 (urkundenundacten07berluoft), 8 (…08…), 13 (…13…), 19 (…19…), 21 (urkundenundact21berl), 23 pt 2
   (urkundenundacten2302berluoft). Vol. 13 p. 425 footnote reads "Friedrich v. Brandt, brandenburg. Resident in Kopenhagen" (identity of the sender
   confirmed, M); vol. 19 prints his reports from Copenhagen of March 1680 and later. Test: lines naming Brandt with Kopenhagen/Coppenhagen/Copenhagen
   within two lines of a 1671-73 year: **0 hits in all six volumes**; none of them prints a 1672 Brandt letter or a cipher passage of it. Volumes not opened:
   the remaining ones (1-6, 9-12, 14-18, 20, 22, 24+); the 1672 Danish business may sit in one of those. No edition of the Hessian regent's 1672 chancery
   or of the Hedwig Sophie correspondence was located (Rommel's Geschichte von Hessen and the Landgraf-Carl-era literature were not opened; an IA
   full-text query "Hedwig Sophie" Landgräfin Regentschaft 1672 Brandt returned ten keyword-soup hits, none read: not evidence either way).
7. Scholarship: OpenAlex (key) "Friedrich von Brandt Brandenburg Resident Kopenhagen": the call returned 0 (the first of two queries mis-fired in my shell
   and is not counted), a second query ("Hedwig Sophie Hessen-Kassel Brandt Copenhagen 1672 cipher", 4 results, all unrelated); Semantic Scholar
   (key) "Hedwig Sophie Hesse-Kassel regent 1672 Denmark Brandt cipher": total 0. Persée/HAL/CrossRef not queried; JSTOR not queryable from the cloud.
   Unchecked, not clear.

Premise check (a)-(d):
(a) Decipherments the folder already mentions: the period decipherment **on the leaves** (below); no separate key sheet found. Also Nr. 125's letter
    table (key 255) was tested against 0049's glossed groups in HDK-131 and disagrees (1/8).
(b) Other solvers' working files: none (check 4).
(c) Physical neighbours: Dänemark 131 is the neighbour of Nr. 125 and was swept in full (HDK-131); the 7 leaves above are the cipher. Its cover (0001) names
    the whole file "Correspondenz mit dem Chur-Brandenburgischen Residenten zu Coppenhagen Friedrich von Brandt" 1671-74. No bound-in key sheet found in
    the sweep (91 of 98 leaves none; sheet scale only).
(d) Recipient side: Hedwig Sophie / the Kassel chancery edition not located (check 6); Brandt's own Brandenburg-side letters are the sender side and
    are not printed for 1672 in the six volumes read.

What the glossed leaves cover (3 requests to digitalisate-he.arcinsys.de, 2.5 s apart, 200 each; 0020, 0049, 0021 at 3500 px kept in the scratchpad, not
committed; 1750-px views read, three vision looks; counts are eye estimates, M, +-15%):
- 0020 (letter of 27 Feb 1672, pr. 9 March): right page carries two cipher blocks, 3 lines at the head (about 44 groups) and 22 lines below (about 300
  groups), about 340 groups in all, values mostly 32-170 with 198 259 262 272 and 3-digit exceptions. **Every line of the lower block has a marginal
  gloss written beside it** (running German: "... Herzog de Jorck ... Prinzessin", "der König ist ... ma[sque] ... tragedie vom König in England Carl Stuard
  agirt ...", ending "der englische Resident hat diese tragedie übel genommen, Ihre Churfl. Durchl. mein gnädigster Herr sehen diese tragedie niemahls zu agiren
  permittirt" (reading by eye, M); the clear text above it is "Es ist hier eine troupe deutscher Commedianten"). The marginal gloss therefore covers
  the full run (about 340 of 340 groups at line level), a sense-for-sense decipherment, not a group-for-group one.
- 0049 (22 June 1672): the slip's 4 lines (about 42 groups) and the foot of the left page (2 lines, about 22 groups), about 64 groups; one letter above each
  group on line 1 (12 letters, "schwanger wirt") and part of lines 2-3 and the foot ("nochts"?), about 35 of 64 groups glossed (M). Letter-for-letter pairs.
- 0021 (end of the 27 Feb letter): 3 short inline groups (244; 209 53 74 94 54 259; 196) with interlinear words above them (about 9 groups, glossed y, partly).
  Correction to the inventory: 0021 was "?" at sheet scale.
- 0050, 0062, 0063, 0064 not re-opened (budget of <= 10 requests; this job needed 3). Together the seven leaves hold an estimated 600-700 groups; the
  two clearly glossed leaves and 0021 hold about 410-420 of them (60-70%), all on leaves with a period gloss on the page.

Cheapest first test (not run, no decoding or key building here): the 0049 letter-for-letter pairs (about 35) are too few for a table alone, so
(1) align 0020's lower block against its marginal gloss with `tools/interlinear_align.py` (hard-EM, sense-for-sense, about 300 groups against about 120
words; value -> letter/syllable candidates), (2) hold the 0049 pairs out as the independent test (letters for about 35 groups), against a shuffled-gloss
control and a code+mark synthetic control at the same N and K (rule 3: the control is the design, not only N and K), (3) only if (2) clears, key.tsv for
Brandt's table and a decode of 0050/0062-0064 with `decode_key.py`. Prerequisite: a two-pass transcription of 0020 (about 340 groups) and 0049 at
crop scale (crops via `tools/iiif_lines.py --image`), about USD 6-9; the alignment itself about USD 1. Duplicate-effort risk: none found (checks 2-5).
Class bookkeeping: not a verifier verdict; no novelty claim (rule 10). Requests: arcinsys 3 GET; api.hcportal.eu 3 GET; archive.org 6 GET + 3 fts + 1
advancedsearch (2 s apart); api.openalex.org 2; api.semanticscholar.org 1; github.com 2 shallow clones; search engine 4.

## BRANDT-TX (9 Oct 2026, 01:09-01:2x UTC by date -u; LANE FAMILY-A2d, account 2): Dänemark 131 image 0020 lower block, its gloss, and an alignment

Prior work: `python3 tools/prior_work.py hessen-daenemark-1672 --item-spec 'shelfmark=HStAM 4 f Staaten D Daenemark 131;folio=0020;date=1672-02-27;
sender=Friedrich von Brandt;recipient=Hedwig Sophie' --step-type transcribe --fetch` exit 2 (KNOWN = AUDIT.md:225, Nr. 125's class, not this leaf;
LEAD = HDK-131, HDK-BRANDT (lookups, not a transcription) and this claim; LOOK 2-leaf = this job). Checks by hand: (1) own work: no transcription of 0020
existed (HDK-131 and HDK-BRANDT read crops by eye only), so the step was not done; (2) neighbours: 0021/0049 left for later jobs (0049 is held out);
(3) solver repos/Tomokiyo and (4) editions: HDK-BRANDT's checks 2-7 of the same day, not repeated. Check 5 (after decode): no decode was made.

Files (all in `dk131_brandt/`): crops `crops3/` (sheared strips, `shear_crops.py`; see the crop note), `ciphertext_0020.tsv`, `gloss_0020.txt`,
`pairs_0020.tsv` (`make_pairs.py --check`), `align_0020.tsv` + `key_0020.tsv` + `shuffle_0020.json` (primary run), `PREREG-BRANDT-TX.md` (pushed
50e2da823 before any score), `explore_agrees.py` (exploratory only).

1. Fetch: 1 GET to digitalisate-he.arcinsys.de (0020 at 3500x2633, the largest served; kept in the scratchpad, not committed). Crop command, pasted:
   `python3 tools/iiif_lines.py --image <scratch>/0020.jpg --out ciphers/hessen-daenemark-1672/dk131_brandt/crops --region 1740,1130,1700,1230 --prefix b20 --debug`
   (23 bands, pitch 52). **Crop defect:** the lines climb about 40 px over the 1700 px block, so the fixed-y bands lost every line's right-hand tail; two
   blind Sonnet passes on those crops (passA/passB.tsv) agree 88.8% but both stop 2-6 groups short on most lines. `--deskew 300` fitted the slope with the
   wrong sign here (peaks tracked on neighbouring lines) and clipped the tails worse (deleted). `shear_crops.py` cuts the same 23 centres as strips sheared
   at a fixed +0.026 slope (measured by eye on the debug overlay), 86 px high; every line then reads end to end. Suggestion for tools/iiif_lines.py: a
   `--slope B` option taking a given slope (Usage 8: an option, not a private copy; this script is kept only because its output is cited).
2. Transcription: two blind Sonnet passes on `crops3/` (passC top-down, passD bottom-up; both flagged strips L06 and L14/L15 as duplicates of a
   neighbour, dropped), `tools/reconcile_passes.py passC_u.tsv passD_u.tsv --out-dir rec2 --crops crops3 --keep-plain`: 19 lines, agree 275/283 = 97.2%,
   8 disagreement columns, all settled from the image by the worker (auch not auss; clear "Der" opening L17; a stain, not a separator, in L14; a stray
   margin "1" dropped). **Result: 258 groups (H 246, M 12), 66 distinct values, mostly 32-145 with 156 157 167 170 178 188 191 262 above; clear words
   written among them: sonderlich, auch, undt (3x), nahmen, da die, bis, der, hat, haben, niemalen.** HDK-BRANDT's eye estimate (about 300 groups in 22
   lines) was high: the block is 19 cipher lines.
3. Gloss: one Sonnet pass (`gloss_pass.tsv`) plus a worker check at 2x native on margin lines 9-15; `gloss_0020.txt` (period spelling kept, rule 3
   convention clause). The worker corrected "wie aus dahin" to "sie auch daher" and "güldenen" to "Güldenlew" (Gyldenløve, M); one word before "wollen"
   is unread. Read (M): "der König ist oft masquirt dahin kommen, sonderlich vorgestern, da die tragedie vom König in Engelandt Carl Stuard agirt wurde;
   kamen sie auch daher mit Güldenlew, der selbst auf englische manier [?] wollen, und andere cavalliern, und nahmen die masquen ab, da die tragedie halb
   aus war, und blieben bis zum ende. Der englische Resident hat dieses übel genommen." The clear sentence after the block: "Ihr Churfürstl. Durchl.
   mein gnädigster Herr haben diese tragedie niemahls zu agiren permittirt." **The gloss ends beside L18: cipher lines L19-L21 (about 40 groups, with the
   clear words haben and niemalen) have no gloss beside them** (M; whether the gloss compresses them into "dieses übel genommen" is not settled).
   By eye the gloss is literal and letter-level where it can be checked, not sense-for-sense as HDK-BRANDT supposed: "die masquen ab" stands over
   46 74 53 / 90 35 124 116 139 55 95 / 34 39 and "halb aus war" over exactly 10 groups (73 34 85 37 35 138 124 144 34 117), with 35/34 a, 46 d, 53 e, 74 i, 117 r recurring.
   So this is a homophonic letter cipher with a few higher codes for words (167 König, 170 Engelandt?, 262 Gülden-, M).
4. Alignment (pre-registered). `make_pairs.py` cut the stream at the clear-word anchors into 10 (cipher run, gloss span) pairs, 220 groups.
   `python3 tools/interlinear_align.py align pairs_0020.tsv align_0020.tsv key_0020.tsv --floor 150 --clear-consumes --max-chunk 8 --shuffle 200
   --seed 1672 --min-share 0.6 --shuffle-out shuffle_0020.json` -> tokens 220, values 61, agrees 95 / single 36 / conflict 89;
   **shuffle control: real 9; control mean 6.13, p95 10, max 12, n 200; p = 0.1493. Gate (real > max AND >= 2 x mean): FAIL.**
   Why, from the alignment: the short pairs read cleanly (masquen, tragedie halb aus war, zum ende, dahin kommen), but the long pairs drift where the
   gloss's wording departs from the cipher ("oft masquirt" over 13 groups, gloss "andere" over cipher "andern", g02 with 79 gloss letters against 56
   groups), and CONSISTENT needs a value on >= 2 of only 10 segments, so the statistic has little power at 10 pairs.
   **EXPLORATORY, not pre-registered, does not change the FAIL** (`explore_agrees.py`): the tool's token-level agrees count, same parameters and
   derangements: real 95; control mean 33.2, p95 44, max 49; p = 0.005. The control can differ from the target on this statistic (a gloss over the
   wrong run gives disagreeing chunks).
   Grades: all 220 aligned tokens M (the PREREG licensed C only on a PASS); the 38 L19-L21 groups unglossed (U). No H, no C: no reading is claimed.
   `key_0020.tsv` is the tool's value -> top chunk table with counts, M throughout, not a key.

Where not found: no gloss beside L19-L21; 0049 not read (held out); 0021 and 0050/0062-0064 not opened; the upper 3-line block of 0020 (about 20
groups, "46.53.117.167.47.124.139" continues from the clear text at L01) is in this transcription only from L01; the head block on 0020's right page
above "Es ist hier eine troupe" (3 lines, HDK-BRANDT's "about 44 groups") was not in this job's region. Novelty not classified (rule 10).
Requests: digitalisate-he.arcinsys.de 1 GET, 200. Vision: 5 Sonnet passes (A, B on the defective crops; C, D; gloss) + 5 worker looks.

## BRANDT-GATE (9 Oct 2026, 02:16-02:3x UTC by date -u; LANE FAMILY-A2e, account 2): pre-registered agrees gate on 0020 and the 0049 held-out letter test

Prior work: `python3 tools/prior_work.py hessen-daenemark-1672 --item-spec 'shelfmark=HStAM 4 f Staaten D Daenemark 131;folio=0049;date=1672-06-22;
sender=Friedrich von Brandt;recipient=Hedwig Sophie' --step-type transcribe --fetch` exit 2 (KNOWN = AUDIT.md:225, Nr. 125's class, not this leaf; LEAD = the
HDK-131/HDK-BRANDT claims and this job's own; LOOK 2-leaf = this job). Checks by hand: (1) own work: 0049 was never transcribed (HDK-131 noted 8 slip groups by eye;
BRANDT-TX held 0049 out), so the step was not done; (2) neighbours: 0050 doubtful, not opened; (3) solver repos/Tomokiyo and (4) editions: HDK-BRANDT's checks of the
same day, not repeated. Check 5 (after decode): no decode of unglossed text was made, so no phrase search.

Files (`dk131_brandt/`): `PREREG-BRANDT-GATE.md` (pushed 13865ab70 before any score and before 0049 was fetched), `gate_agrees.py` + `.out`, `crops49/`,
`passA49.tsv`/`passB49.tsv` (+ `_u` normalised), `rec49/`, `ciphertext_0049.tsv`, `gate_0049.py` + `.out`, `values_gate.tsv`.

1. Test 1 (0020, token agrees, the statistic of explore_agrees.py, n 2000 derangements, fresh seed 20261009): real 95; control mean 33.53, p95 43, p99 48,
   max 54; p = 0.0005. **Gate (real > max AND p < 0.01): PASS.** CONSISTENT (BRANDT-TX's FAIL) was not re-run.
2. 0049: 1 GET (3500x2633, scratchpad only). Crop commands, pasted:
   `python3 tools/iiif_lines.py --image <scratch>/0049.jpg --out ciphers/hessen-daenemark-1672/dk131_brandt/crops49 --region 1780,540,1160,330 --prefix s49 --centres 79,140,197,256 --top-margin 8 --debug`
   `python3 tools/iiif_lines.py --image <scratch>/0049.jpg --out ciphers/hessen-daenemark-1672/dk131_brandt/crops49 --region 600,1780,1180,240 --prefix f49 --centres 88,143 --top-margin 8 --debug`
   (auto-detection put each gloss row and each group row in separate bands, so the centres were given by eye from the overlay to keep gloss + groups together;
   the lines are flat here, no shear needed. **Crop defect:** the bands clip the bottoms of the digits; the passes read through it, and every split was settled on
   unclipped native views.) Two blind Sonnet passes (A top-down, B bottom-up), `tools/reconcile_passes.py passA49_u.tsv passB49_u.tsv --out-dir rec49 --crops crops49
   --keep-plain`: 66 signs each, agree 56/66 = 84.8%, 10 columns settled by the worker (35 not 75, 94 not 44, 67 not 62, 120 not 130; 101 carries "on138." above it
   and no letter; 45 = c and 73 = h at the end of slip line 3; foot line 2 group 71 glossed h (M, h/r split); **foot line 1 group 46: both passes read gloss "a", the
   native view shows "d"; worker override** -- without it test 2 reads 33, still above p99). Result: 62 cipher groups + 2 clear words ("inß", "Hauß"), 61 glossed.
   The glosses read, period spelling: slip "chwanger wirt / schatzmeist / ers [Hauß] ihrec[..]h / eshalten" (the slip starts mid-word: "[s]chwanger wirt");
   foot "doctern ohts / tochter ists" (M; continuous sense not settled, rule 4 grade M for the plaintext).
3. Test 2 (0049 held out; key = key_0020's 58 single-letter values, as committed by BRANDT-TX with no prior): 48 scorable groups, **34 agree**; value-permutation
   control mean 3.76, p99 12, max 20, n 2000; p = 0.0005. **Gate (real > p99): PASS.** Sensitivity without the 8 slip groups HDK-131 had already written into
   NOTES.md: 28/42 vs control p99 11, PASS. Scorer fix before the gate was read: the first run counted the no-letter mark "-" over 101 as a scorable letter (49
   scorable); the registered wording is "one letter", so it was excluded (48). Both controls can differ from their targets (re-dealt spans / re-assigned letters).
4. Grades (prereg: C only if both pass): **16 values grade C** (period gloss, two leaves: 34 a, 35 a, 42 c, 46 d, 52 e, 53 e, 56 e, 73 h, 75 i, 94 n, 117 r,
   118 r, 124 s, 125 s, 131 t, 144 w); **8 values M**, where 0049's gloss disagrees with key_0020's top chunk (45 c x3 not t, 123 r x2 not i, 129 s x2 not e,
   130 t x3 not e, 76 i, 86 l, 91 m, 100 o): the 0020 alignment drifted on these, and 0049's gloss is the better witness but has one leaf only. 15 glossed 0049
   groups have values outside key_0020 (e.g. 72 h, 126 s, 156 z, 104 o x2, 136 t x2): M, one leaf. `values_gate.tsv` holds the table. This is the cipher's
   letter table as the period decipherer read it, not a reading of any unglossed text; tokens of 0020 and 0049 are C where their value is C and their gloss agrees.
Where not found: 0049's slip continues the letter on another leaf (it starts "[s]chwanger"); 0020's upper block, 0021, 0050, 0062-0064 not opened in this job.
Requests: digitalisate-he.arcinsys.de 1 GET, 200. Vision: 2 Sonnet passes + worker settling on 3 native views. Novelty not classified (rule 10).
**V-BRANDT correction (verifier, 9 Oct 2026, AUDIT.md "V-BRANDT"):** test 1 re-scores the statistic BRANDT-TX had already seen (95) on the same pairs, so it
confirms a known number and is not independent evidence; test 2 holds and is the independent evidence (also on each blind pass alone: 33/48 and 30/49 vs p99 12).
Value 46 = d rests out of sample only on the worker's override of both blind passes' gloss "a": regraded M. After audit 15 values C, 9 M (values_gate.tsv not edited).
Suggestion (not run): 0020 upper block + 0021 transcribed and read with values_gate.tsv's 16 C values as a prior, then 0062-0064 (unglossed?) decoded under a
matched control, ~4.

## BRANDT-UP (9 Oct 2026, 02:45-02:54 UTC by date -u; LANE FAMILY-A2e, account 2): Dänemark 131 0020 head block and 0021 under the gate-passed values

Prior work: `python3 tools/prior_work.py hessen-daenemark-1672 --item-spec 'shelfmark=HStAM 4 f Staaten D Daenemark 131;folio=0021;date=1672-02-27;
sender=Friedrich von Brandt;recipient=Hedwig Sophie' --step-type transcribe --fetch` exit 2 (KNOWN = AUDIT.md:225, Nr. 125's class, not this leaf; LEAD = the
HDK-131/HDK-BRANDT target-level claims; LOOK 2-leaf rows written to look.tsv). Checks by hand: (1) own work: the 0020 head block and 0021 were never transcribed
(BRANDT-TX's region began at "Es ist hier eine troupe"; HDK-BRANDT only counted 0021's groups by eye), so the step was not done; (2) neighbours: 0020/0021 are
the two halves of the 27 Feb 1672 letter, both read here; 0049 done by BRANDT-GATE; (3) solver repos/Tomokiyo and (4) editions: HDK-BRANDT's checks of the same
day, not repeated. Check 5 (after decode): no unglossed text was decoded (both blocks carry a period gloss), so no phrase search.

Scope note: the brief named "the 0020 upper block (3 lines continuing from L01's clear text, ~20 groups)" and "the right-page head block above 'Es ist hier
eine troupe' (~44 groups)". On the image these are one block: the only cipher above "Es ist hier eine troupe" is the 3-line head block (44 groups); L01's own
continuation ("46.53.117.167...") is already in ciphertext_0020.tsv (BRANDT-TX). 0021 carries cipher only in its top 4 lines (8 groups); the faint numerals
lower on 0021's left page are show-through from 0020's right page, not writing on 0021.

Files (`dk131_brandt/`): `PREREG-BRANDT-UP.md` + `score_up.py` (committed and pushed before any score), `cropsU/`, `passA20u/passB20u.tsv`, `glossA20u/glossB20u.txt`,
`passA21/passB21.tsv` (+ `_u`), `clearA21/clearB21.txt`, `recU/`, `rec21/`, `ciphertext_0020u.tsv`, `gloss_0020u.txt`, `ciphertext_0021.tsv`, `grade_up.py` +
`reading_up.tsv` (`python3 grade_up.py --check`).

1. Fetch: 2 GETs to digitalisate-he.arcinsys.de (0020 and 0021, 3500 px, scratchpad only). Crop commands, pasted:
   `python3 tools/iiif_lines.py --image <scratch>/0020.jpg --out ciphers/hessen-daenemark-1672/dk131_brandt/cropsU --region 1760,360,1660,300 --prefix b20u --centres 150 --top-margin 150 --bottom-margin 150`
   `python3 tools/iiif_lines.py --image <scratch>/0021.jpg --out ciphers/hessen-daenemark-1672/dk131_brandt/cropsU --region 400,270,1400,290 --prefix b21 --centres 145 --top-margin 145 --bottom-margin 145 --debug`
   (one 3-line strip per block, margin gloss included; per-line bands `u20_L01-03` were cut first with --centres 45,110,190 and kept, but each carried
   parts of its neighbour lines, since line 3 descends about 35 px over the block, so the passes read the whole-block strip, 1660 px wide.)
2. Transcription: two blind Sonnet passes per block (A top-down, B bottom-up). `tools/reconcile_passes.py`: 0020 head block 46/46 tokens agree (the only
   column is vndt/Vndt case); 0021 8/8 groups agree. **Result: 0020 head block 44 groups + clear "vndt" + one ":" separator; 0021 8 groups (244; 209 53 74 94 54 259;
   196) among clear text.** Values seen here and not in BRANDT-TX's lower block include 198, 244, 272, 209, 196 (word-level codes) and 259 on both leaves.
3. Glosses (worker settling on 2x-3x native views, M throughout): 0020 margin, 6 short lines: "eine heuraht / zwischen dem hertzog / de Jorck undt /
   Hertzogi[?] königl / princessin zu [?]o / golyzt[?]" -- both passes misread line 1 ("Mr Hurault", "Der Hertzogh"); line 4 word 1 and lines 5-6 are not
   settled. 0021 interlinear: 244 "Gesanter", 209 "Schwedes", 53 74 94 54 "eine" (written over the four groups together), 259 "Heüraht", 196 "der verwittibten
   Königin" (passes: "nur/nuer" and "vorgeblich/vorgeschlich" for these two; worker reading). 0021 in clear: "Man hat zwar vorgeben wollen, alß were der [Gesandter]
   auß [Schweden] [eine Heurath] tractiren würde, weilen er aber nicht ein einzig mahl bei [der verwittibten Königin] gewesen, ist solches nicht zu vermuhten."
4. Known-answer test (PREREG-BRANDT-UP.md, values_gate.tsv's 16 C values frozen, no value added): C-value tokens 25 of the 52 groups (48% coverage);
   **LCS 23 of 25 against the gloss letters; control (2000 permutations of the C letters) mean 15.58, p99 19, max 20; p = 0.0005: PASS.** The control can
   differ from the target (re-assigned letters change the sequence matched against the fixed gloss). Note the control's high mean: an LCS against a long gloss
   matches common letters by chance, so the margin (23 vs p99 19) is real but modest. The 0020 head line 1 reads under C values alone
   "e[74]ne [259] [156]wische[92] : de[95]" against the gloss "eine heuraht zwischen dem" -- the two unmatched C tokens (75 i, 42 c) both sit in lines 2-3, beside
   the unsettled gloss lines 4-6.
5. Grades (`reading_up.tsv`): 52 cipher tokens, **C 23** (C value, LCS-matched to the period gloss), **M 29** (non-C values and the 2 unmatched C tokens); no S
   (no unglossed tokens), no H. Recorded as M observations only, not added to values_gate.tsv: 259 = "heuraht" on two leaves (0020 margin, 0021 interlinear);
   156 = z (zwischen; 0049 also z); 74 = i under "eine" on 0021 and in "e[i]ne" on 0020; 244 Gesandter, 209 Schweden, 196 verwittibte Königin, 198 Herzog (0020 line 2
   beside "hertzog de Jorck", M). values_gate.tsv is unchanged.
**V-BRANDT correction (verifier, 9 Oct 2026, AUDIT.md "V-BRANDT"):** the LCS gate PASSes only on the worker's settled margin gloss ("eine heuraht / zwischen"),
read with values_gate.tsv in view; on either blind gloss pass it FAILs (glossA20u 15 vs p99 16; glossB20u 16 vs p99 17; `v_brandt.py`). So the gate is not
independent evidence and the 23 C tokens revert to M (52 tokens: M 52) until a reader blind to the values re-reads margin lines 1-2 (one Sonnet call, ~1.5).
Where not found: no gloss read for 0020 margin lines 4-6 beyond the M reading above, so the 0020 head line 3 (272 156 138 94 53 64 101 42 74 76 52 118 53 94) is not
read; 0050 and 0062-0064 not opened. Novelty not classified (rule 10).
Requests: digitalisate-he.arcinsys.de 2 GETs, 200. Vision: 4 Sonnet passes + worker settling on 3 native views.
Suggestion (not run): the unglossed 0062-0064 decoded with values_gate.tsv's C values under a matched control (prereg first), ~4; and a second blind eye on
0020's margin gloss lines 4-6 (one Sonnet call, ~1.5) to settle the head line 3.

## BRANDT-062 (9 Oct 2026, 03:14-03:2x UTC by date -u; LANE FAMILY-A2e, account 2): Dänemark 131 leaves 0062-0064 and 0050's head under the gate-passed values

Prior work: `python3 tools/prior_work.py hessen-daenemark-1672 --item-spec 'shelfmark=HStAM 4 f Staaten D Daenemark 131;folio=0062;date=1672-08-09;
sender=Friedrich von Brandt;recipient=Hedwig Sophie' --step-type decode --fetch` exit 2 (KNOWN = AUDIT.md:225, Nr. 125's class, not this leaf; LEAD = the
HDK-131/HDK-BRANDT/V-BRANDT target-level claims and this job's own; LOOK 2-leaf = this job). Checks by hand: (1) own work: 0062-0064 and 0050 never
transcribed (HDK-131 sheet pass only), so the step was not done; (2) leaf and neighbours (gloss check): see 1 below -- 0062 carries a full interlinear
gloss; (3) solver repos/Tomokiyo and (4) editions: HDK-BRANDT's checks of the same day, not repeated. Check 5 after decode: item 5 below.

1. Fetch: 4 GETs to digitalisate-he.arcinsys.de (0062, 0064, 0063, 0050 at 3500 px, scratchpad only, 2.5 s apart, 200 each). **Eye check at 1/4 and
   native: only 0062 carries cipher writing.** 0062's right page holds the cipher block of the letter dated "Koppenhagen den 3. Aug. 1672" (signed
   Friedrich von Brandt; dk131_inventory.tsv's "9 Aug(?)" is 3 Aug): 6 numeral lines, not ~9, with a second-hand interlinear gloss above them. The numerals
   on the left page of 0063 and 0064 (the same page, 0063 has a slip laid over the right page) and at the head of 0050's slip are **mirror-image
   show-through**, reading reversed: 0063/0064 of 0062's block (46.100.43.131... reversed), 0050 of 0049's slip (the "on138" mark and 0049's slip groups
   reversed). The "small marks above some groups" on 0064 are 0062's gloss showing through. dk131_inventory.tsv updated. So there are no unglossed cipher
   tokens on these leaves, and the brief's unglossed statistic has no data (PREREG-BRANDT-062.md says so).
2. PREREG: `dk131_brandt/PREREG-BRANDT-062.md` + `score_062.py`, pushed 81c598738 before any score (time fix 45905fb24). Same design as BRANDT-UP: per-line
   LCS of the C-value letters against that line's gloss letters, value-permutation control n 2000, gate real > p99 and p < 0.01.
3. Crop command, pasted: `python3 tools/iiif_lines.py --image <scratch>/0062.jpg --out ciphers/hessen-daenemark-1672/dk131_brandt/crops62 --region
   1900,290,1350,480 --prefix b62 --centres 80,142,205,267,333,400 --top-margin 55 --bottom-margin 30 --debug` (lines flat enough, no shear; each crop
   carries its line, its gloss and parts of the neighbours). Two blind Sonnet passes (passA62 top-down, passB62 bottom-up; `_u` normalised),
   `tools/reconcile_passes.py passA62_u.tsv passB62_u.tsv --out-dir rec62 --crops crops62 --keep-plain`: **66/66 signs agree** (62 groups + clear
   "hat einen", "Der", "hat"). The passes agreed on the gloss words and split only on their placement; the worker settled placement on 1x/2x native views.
   Gloss, period spelling (M): L01 "d o c tor" over 46 100 43 131 102 117, "mots" over 90 102 132 129 (139 unglossed); L02 "to c h t er" over 103 43 73 136 56,
   [hat einen] "iungen" over 78 143, "gulden[?]" (word partly unread, worker reading; passes put it over 143 or 94); L03 "geboren" over 63 52 36 100 103 117
   52 94 (pos 5-12; pos 1-4, 63 52 99 262, unglossed); L04 [Der] "König" over 167 (worker reading; passes "stang?"/"Dany?"), [hat] "ihr" over 74 69 117,
   "zehen" over 156 52 73 52 94; L05 "tausente" over 130 32 138 124 53 96 134, "thaler" over 135 69 31 69; L06 "verehrt" over 138 56 123 54 73 122 52 134
   (L06 52 122, unglossed, may end "thal-er"). Files: `ciphertext_0062.tsv`.
4. Score (`python3 dk131_brandt/score_062.py`): 62 groups, C-value tokens 22, gloss letters 71; **real LCS 20; control mean 8.90, p99 14, max 17, n 2000;
   p = 0.0005: PASS.** Sensitivity without the two worker-settled glosses (König, gulden[?]): real 20 vs p99 14, max 16 (`grade_062.py --sens`).
   Secondary (not a gate): only 2 C tokens sit under a single-letter gloss, both agree. Note: 2 of the 20 LCS matches fall on unglossed positions of a
   glossed line (L03 52, L06 52); the statistic counted them as registered, the grades below do not.
   Grades (`grade_062.py`, `reading_062.tsv`, `--check` passes): 62 cipher tokens, **C 18** (C value, LCS-matched, under a gloss word), **M 44** (36 glossed
   non-C or unmatched, 8 unglossed: L01 139, L02 122, L03 63 52 99 262, L06 52 122); no S (no unglossed gate), no H. Not added to values_gate.tsv; recorded as
   M observations from the letter-over-group gloss: 100 o and 102 o (doctor, mots), 90 m, 132 t, 129 s (mots; 129 s agrees with 0049), 103 t, 156 z (zehen;
   0049 and 0020 head also z), 69 h (ihr, thaler), 32 a, 138 u/v (tausent, verehrt), 96 n, 134 t, 135 t, 122 r, 123 r (agrees with 0049), 63 g?, 167 König
   (as BRANDT-TX). The gloss reads, M: "doctor Mots tochter [hat einen] iungen gulden[?] geboren; [Der] König [hat] ihr zehen tausent thaler verehrt".
5. Check 5 (phrase search on the decoded/glossed text): be-api.us.archive.org full text, "Doctor Mots" (14 hits, all modern/unrelated: newspapers,
   phrasebooks) and "zehen tausent Thaler" (18 hits, not read; generic phrase); Google Books API answered 429 (daily quota exhausted) on the first call --
   **unreachable this session, not retried**. No hit about this letter found; print_check.py not run (Google Books down).
Where not found: no unglossed Brandt cipher on 0050/0063/0064; L02 "gulden[?]" and L03 pos 1-4 (63 52 99 262, with 262 = "Gülden-" M per BRANDT-TX) not settled;
"thaler" placement not settled. Novelty not classified (rule 10).
Requests: digitalisate-he.arcinsys.de 4 GETs (200); be-api.us.archive.org 3; www.googleapis.com 4 (429 after the first). Vision: 2 Sonnet passes + 3 worker looks.

## BRANDT-REGRADE (9 Oct 2026, 04:18-04:4x UTC by date -u; LANE FAMILY-A2f, account 2): V-BRANDT's regrades applied, 0062 re-scored on two blind gloss passes

Prior work: `python3 tools/prior_work.py hessen-daenemark-1672 --item-spec 'shelfmark=HStAM 4 f Staaten D Daenemark 131;folio=0062;date=1672-08-03;
sender=Friedrich von Brandt;recipient=Hedwig Sophie' --step-type decode --fetch` exit 2 (KNOWN = AUDIT.md:225, Nr. 125's class, not this leaf; LEAD = the
HDK-131/HDK-BRANDT/BRANDT-062 target-level claims and this job's own; LOOK 2-leaf = the 0062 gloss, which is this job's input). Checks by hand: (1) own work:
no blind re-score of 0062 and no applied regrade existed (V-BRANDT left values_gate.tsv unchanged, ROOM flag), so the step was not done; (2) leaf: 0062's
interlinear gloss is the known answer used here; (3)-(4) solver repos/editions: HDK-BRANDT's checks of the same day, not repeated. Check 5: no new decode
of unglossed text (0062 is fully glossed), so no phrase search.

1. Regrades (V-BRANDT items 4-5). `values_gate.tsv`: 46 = d C -> M (no other value named); now 15 C, 9 M. The pre-regrade file is kept as
   `values_gate_v0.tsv`, and the three records scored on it read that copy (score_up.py, score_062.py, v_brandt.py; v_brandt --check OK).
   `grade_up.py` (BRANDT-UP): INDEPENDENT = False (blind gloss FAIL), so every LCS-matched C token is M; reading_up.tsv **52 tokens: C 0, M 52**
   (--check OK); the 22 tokens matched to the worker-settled gloss are noted as such.
2. `PREREG-BRANDT-062B.md` + `score_062b.py` pushed 50ad16493 (04:28 UTC) before either blind pass ran. Same statistic, control, seed and gate as
   PREREG-BRANDT-062; only the key (15 C) and the gloss input (each blind pass separately) change.
3. Two blind Sonnet passes over `crops62/b62_L01..L06.jpg` (crop paths only; the readers saw no gloss file, ciphertext, key or prior pass; A top-down,
   B bottom-up), gloss text copied verbatim to `gloss62_blindA.tsv` / `gloss62_blindB.tsv`. Both read "doctor", "mots", "tochter", "iungen gülden[?]",
   "geboren", "ihr zehen", "tausente thaler", "uerehrt"/"uerekrt"; neither read "König" over 167 (A "Stain[?]", B "[?]ainy").
4. Score (`score_062b.out`): **pass A LCS 19 of 21 C-value tokens vs control mean 9.49, p99 14, max 16, p 0.0005: PASS; pass B 18 vs mean 8.73, p99 14,
   max 15, p 0.0005: PASS.** Reference (not a gate): worker gloss with 15 C values 19 vs p99 14. PASS on both blind passes, so BRANDT-062's C grades
   stand minus value 46: reading_062.tsv **62 tokens: C 17, M 45** (only L01 46 changed; grade_062.py --check OK). The gloss PLACEMENT over groups (which
   C tokens count as "glossed") is still BRANDT-062's worker column; the blind passes confirm the per-line letters, not the placement.
Where not found: neither blind pass reads a word over L04 167 that matches "König", so 167 = König stays an M reading; "gulden[?]" and L03 pos 1-4 are not
settled. Novelty not classified (rule 10). Requests: none (disk only). Vision: 2 Sonnet passes.
Suggestion (not run): the Brandt pool (0020/0021/0049/0062, ~380 groups, own letter table, own gloss) is a different cipher and correspondent from Nr. 125's
nomenclator; a folder of its own (e.g. hessen-brandt-daenemark-1672) would keep its gates, grades and gaps apart from this target's Remaining gaps.

## BRANDT-MARGIN (9 Oct 2026, 04:41-04:44 UTC by date -u; LANE FAMILY-A2f, account 2): 0020 margin lines 1-2 blind re-read + 0062 gloss phrase search

Prior work: `python3 tools/prior_work.py hessen-daenemark-1672 --item-spec 'shelfmark=HStAM 4 f Staaten D Daenemark 131;folio=0020;date=1672-02-27;
sender=Friedrich von Brandt;recipient=Hedwig Sophie' --step-type transcribe --fetch` exit 2 (KNOWN = AUDIT.md:225, Nr. 125's class, not this leaf; LEAD = the
target-level claims incl. this job's own; LOOK 2-leaf = the 0020 margin gloss, this job's input). Checks by hand: (1) own work: no read of margin lines 1-2
by a reader blind to the values existed (V-BRANDT item 3 open), so the step was not done; (2) leaf: the margin gloss is the item; (3)-(4) solver repos/editions:
HDK-BRANDT's checks of the same day, not repeated. Check 5 (0062 gloss): item 3 below.

1. Crops (disk only, no fetch), pasted: `python3 tools/iiif_lines.py --image ciphers/hessen-daenemark-1672/dk131_brandt/cropsU/b20u_L01.jpg --out
   ciphers/hessen-daenemark-1672/dk131_brandt/cropsM --region 0,0,245,300 --prefix m20 --centres 45,78 --top-margin 22 --bottom-margin 20 --debug`,
   then 4x LANCZOS views `m20_L01_x4.jpg`, `m20_L02_x4.jpg`, `m20_L01-02_x4.jpg` (all committed, `cropsM/`). Limit: the source strip cropsU/b20u_L01 starts at
   x=1760 of image 0020, so line 2's last word ("hertzog") is cut at the strip's edge; a wider margin crop needs a new fetch of 0020 (not in this brief).
2. Two blind Sonnet passes (A top-down, B bottom-up), shown only the cropsM paths, never values_gate*.tsv, the ciphertext, gloss_0020u.txt or any prior pass
   (`margin20_blindA.txt`, `margin20_blindB.txt`, verbatim). **A: "Lues[?] Hauszelt[?] / Wenss[?] dem hertz[?]o[?]"; B: "Lues Hauszeit[?] / Zuerst dem herz[?]".**
   Both differ from the worker-settled "eine heuraht / zwischen dem hertzog" in line 1 (both blind readers agree with each other on "Lues Haus-"; both rate
   line 1 low confidence) and in line 2 word 1; they agree with it on "dem hert(z)". So the blind readers do not confirm the worker's line 1.
3. `PREREG-BRANDT-MARGIN.md` pushed e6f727ca5 (04:42 UTC) before scoring; `score_up.py` run unchanged in a scratch copy with gloss_0020u.txt replaced by
   G_A (blind A lines 1-2 + glossA20u lines 3-6) and G_B (blind B lines 1-2 + glossB20u lines 3-6) (`score_margin.out`):
   **G_A real LCS 17 vs control mean 14.33, p99 17, max 18, p 0.0370: FAIL; G_B 18 vs mean 14.64, p99 18, max 20, p 0.0135: FAIL.** Reference (worker gloss,
   unchanged): 23 vs p99 19, p 0.0005, PASS. Blind inputs move the score up from V-BRANDT's 15/16 but still not past p99. BRANDT-UP's 52 tokens stay **M 52**
   (no grade change; values_gate.tsv unchanged).
4. 0062 gloss print check (prior-work check 5): `python3 tools/print_check.py ciphers/hessen-daenemark-1672 --phrases .../dk131_brandt/phrases_0062.txt --only gbooks
   --out .../dk131_brandt/print-check-0062.tsv --delay 1.6`: 4 gloss phrases ("hat ihr zehen tausend thaler verehrt", "zehen tausent thaler verehrt",
   "tochter hat einen iungen", "doctor mots tochter") + 1 positive control (Ribbeck's title). **Result: www.googleapis.com HTTP 429 on the first request; per the
   brief (one try, no loop) nothing was searched, positive control included: a non-test, not a miss.** Files `print-check-0062.tsv`, `print-check-0062-hosts.tsv`.
Where not found: no blind reader reads "eine heuraht" in margin line 1; no phrase search ran on the 0062 gloss. Novelty not classified (rule 10).
Requests: www.googleapis.com 1 (429). Vision: 2 Sonnet passes.
Suggestion (not run): the 0062 phrase search after the Google Books daily quota resets (phrases_0062.txt ready, ~$0.3); a wider 0020 margin fetch so line 2 is
whole, then one more blind read only if a different instrument (a gloss-hand letter atlas) is available -- a third Sonnet pass on the same crops would be rule 3's
same-knob retry.

## GB-PHRASE (9 Oct 2026, 07:23-07:3x UTC by date -u; LANE FAMILY-A2g, account 2): the owed Google Books phrase search on the 0062 gloss

Brief: .claude/briefs/runs/2026-10-09-ytbiz-family-0709-jobs.md "GB-PHRASE" item (1). Prior work: `python3 tools/prior_work.py hessen-daenemark-1672
--item-spec 'shelfmark=HStAM 4 f Staaten D Daenemark 131;folio=0062;date=1672-08-03;sender=Friedrich von Brandt;recipient=Hedwig Sophie' --step-type lookup
--fetch` exit 4 (KNOWN = AUDIT.md:225, Nr. 125's class, not this leaf; 3 LEAD = BRANDT-062, BRANDT-MARGIN and this job's own claims), recorded CLEAR
(BRANDT-062 and BRANDT-MARGIN both hit Google Books HTTP 429 on the first call, so the search was never run; this job is that search). Check 1 by hand: no
completed Google Books row for phrases_0062.txt in the folder (print-check-0062.tsv is all "not searched"). Checks 3-4: HDK-BRANDT's of the same day, not
repeated.

1. `python3 tools/print_check.py ciphers/hessen-daenemark-1672 --phrases ciphers/hessen-daenemark-1672/dk131_brandt/phrases_0062.txt --only gbooks --out
   ciphers/hessen-daenemark-1672/dk131_brandt/print-check-0062-gb.tsv --delay 1.6` (07:23 UTC): www.googleapis.com answered. **Positive control** (Ribbeck's
   title, "aus berichten des hessischen sekretars lincker"): 2 volumes (Iron Kingdom 2006, which cites it, and Verhandlungen des Kurhessischen Landtages):
   the route answers. Phrase rows: "zehen tausent thaler verehrt" 20 volumes, "tochter hat einen iungen" 23, "doctor mots tochter" 268 -- the API's quoted
   search is loose, so each was re-read with snippets (step 2); "hat ihr zehen tausend thaler verehrt" HTTP 503 in the tool run.
2. Snippet read (`dk131_brandt/gbphrase_queries.txt`, one request per query, >= 2 s apart): the 503 phrase retried once, HTTP 200, 20 volumes; all four
   phrases plus three targeted queries ('"Doctor Mots" Koppenhagen', '"Doctor Mots" 1672', 'Brandt Koppenhagen 1672 Tochter zehen tausend Thaler verehrt').
   **No volume carries any of the four gloss phrases verbatim, and no snippet concerns Copenhagen in 1672, a Doctor Mots, his daughter's child or a royal
   gift of 10,000 thaler.** Nearest matches are generic: "zehen tausent Thaler zu Verehrung" in the 1608 Braunschweig "Illustre Examen" (oJ2x0uqWsWQC,
   CilBAAAAcAAJ, rDZPAAAAcAAJ; a 1600s soldiers' deposition), Sleidan continuations of 1625 (gifts "vmb zehen tausend Thaler"), "Tochter hat einen jungen
   Maler/Mann/Erzherzog" in 1885-1963 prose, and "Doctor ... Tochter ... mot(s)" scattered across 19th-c. newspapers. "Doctor Mots" with Koppenhagen or 1672:
   nothing relevant (Dutch letter-bode registers, Jesuit bibliographies); the 7-word AND query: 0 volumes.
Where not found: Google Books (API, country=US, keyed), the four 0062 gloss phrases and the three targeted queries, 9 Oct 2026: no hit about this letter.
A search result, not a novelty verdict (rule 10). Not searched here: IA full text (BRANDT-062 ran "Doctor Mots" and "zehen tausent Thaler" on be-api: no hit
about the letter), HathiTrust full text and Danish-side print (Rigsarkivet calendars), not reachable or not in this brief.
Requests: www.googleapis.com 12 (5 tool + 7 snippet; one 503, no 429). Files: `dk131_brandt/print-check-0062-gb.tsv`, `print-check-0062-gb-hosts.tsv`,
`gbphrase_queries.txt`. No decode, no grade change, no class.

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
Read so far: unmeasured. No reconciled ciphertext.tsv exists; key.tsv (key 255 letter table, S) and a provisional ciphertext_f4runs.tsv (the two f.4 runs, single-eye, M) exist since 2 Oct 2026 (A2-HDK3), 36 tokens: 31 M, 5 U. The only committed value is 601 = "Dennemarck" (grade C, glossed 3x on f.4; Cheap test 1). Cheap test 1's "~40 code tokens, ~20 distinct values" was a rough count, and it is an undercount. It excluded 625/774/775 as "section counters", but on a 1000-px preview of image 0003 (this pass, adversarial check, M) 774 and 775 stand inline in the prose with bold glosses above or beside them. It also called f.2 "plain", yet image 0002 carries at least one inline glossed code in its last lines. So any "~3 of ~40 (~7%)" figure is not a measurement. Note that images 0002-0004 are HCPortal image numbers, not checked foliation: 0003 has its binding on the right and faces 0004, so it is a verso.
- ff.2-4 (images 0002-0004), every inline code group that carries a bold interlinear or marginal gloss. On the preview these include 651 (by "Cur Brandenburg"), 653, 229 ("Berlin"), 774, 775 ("Ga. Stadt") and the marginal 625 gloss on 0003; on 0004, 756/768, 229, 427 641 ("herzog von Ploen"), 303, 447 and 834; on 0002 the one group, done 3 Oct 2026 (GAPS152, page 1: 690 with gloss "Bleinenk??l", M, both passes agree on the sign). Image 0003 done 3 Oct 2026 (GAPS155, page 2): 9 groups, all glossed, 9/9 sign agreement: 605 K. Dennemarck, 651 x2 and 653 Kurbrandenburg, 625 (margin gloss unread), 229 Berlin, 690 (recurs from page 1, M), 774 Holland, 775 General-Staaten; held-out check 2/2 vs shuffled-gloss control P=0.11 without the 690 override (4/4, P=0.007, with it): not yet discriminating. Image 0004 done 3 Oct 2026 (GAPS159, page 3): 11 glossed nomenclator pairs (C 8, M 3: 602 Der Konig in Dennemarck, 5756 Franckreich, 601 x2 Dennemarck, 229 Berlin, 681 Cur Brandenb, 768 ?ueco, 437 641 Hertzog von Ploen, 303 alliance, 447 Kayser, 834 Rex Daniae), 47/56 sign agreement before reconciliation; 303 and 229 conflict with key 255; pooled pages 1-3 held-out 8/8 (6/6 without the 690 override) vs shuffled-gloss control mean 0.27-0.37, P<0.0001: discriminating. All three pages are now transcribed and their glosses paired. None of the 0003/0004 codes is pinned code by code - blocker: not-attempted; images at 2600x3944 px are on disk and legible enough that most 3-digit codes visibly carry a gloss, so the gloss coverage is much wider than "1 of 20". Cheap test 1 stopped at a breadth cap, and the iiif_lines.py crop step in its brief (.claude/briefs/runs/2026-09-26-lane-b7-hcp.md, item A) was never pasted. The f4_top/f4_mid crops cited in NOTES are not on disk; done 3 Oct 2026 (GAPS163): merged into ciphertext.tsv (65 groups); key_gloss.tsv holds 18 gloss-pinned nomenclator rows (C 11, M 6, I 1); decode_key --check exit 0, tokens 65: C 9, I 1, M 21, S 30, U 4; nomenclator coverage 23/26, only 625 x2 (p2 margin gloss unread) and the margin 7480 left; done 3 Oct 2026 (GAPS168): the 625 margin gloss reads "[?] Ahlefeldt" (word 2 two eyes M, word 1 unread), key_gloss 625 = [?_Ahlefeldt] M, nomenclator coverage 25/26, only the margin 7480 (probably not a code) left; next: none needed beyond gap 3
- f.4 (image 0004), the two dense 2-digit runs and every other 2-digit/doubled-letter group on ff.2-4 (A2-HDK 2 Oct 2026: HCPortal key 255's letter table, 1666, "mit Secretario Lincker", reads both runs in agreement with the letter's own gloss, 21/26 gloss pairs on the 1 Oct readings vs relabelled-table control max 10, 26/26 on native-crop readings; S, see "Known-keys and sibling check" step 5). Still open inside run 1: 6d, LL, 143 against the gloss "stirt", and bb. A2-HDK3 (2 Oct 2026) wrote key.tsv (197 rows, S; 20 = A, nulls 1-19 etc.) and checked it against the period "Scala über den Clavem mit Secretarium Linckern" in DECODE 4690 (120/120 entries agree); decode_key.py --check passes on the provisional f.4 runs (36 tokens: 31 M, 5 U) - blocker: not-attempted; key.tsv and decode.json are in place; done 3 Oct 2026 (GAPS163): ciphertext.tsv replaces ciphertext_f4runs.tsv; --check exit 0, --split-check flags only I among letter groups; 38/39 letter-cipher tokens keyed; against the letter's own per-group letter glosses 5/7 agree, 2 disagree (55 h vs g, 6 NULL vs t; 69 k under 'ott'): a 1672 revision of up to three cells or misreads, unsettled; done 3 Oct 2026 (GAPS168): native zoom shows 55 is clearly 55, not 53, under a clear gloss g; 6 reads 6 (M) under t; 69 was not re-read (crop edge); so these are encipherer slips or changed cells, not misreads of 55. key.tsv is unchanged, since one occurrence per cell cannot settle a revision; next: a separate verifier on the reading, then gap 3 (key-rebuild), which may test whether any other 55/69/6 occurrence on ff.2-4 reads g/t/t
- Every code group still unglossed after the two steps above (GAPS163, 3 Oct 2026: 5 tokens -- 602 at p3:26.3 now read M from p3:1's gloss, 634 filled I as [Holstein] from the run-1 margin gloss, 68 read e by the letter table M, 625 x2 and the margin 7480 unread) - blocker: open-codes; done 3 Oct 2026 (GAPS193, prereg 4ea2abe1): bracketing at K=16 with a matched code+mark control: one-part alphabetical order is a control-backed negative (tau 0.194, p 0.172; control power 0.807 at 0.4 noise, size 0.051), and the topical-block grouping is a non-test at this N (target p 0.014, but control power 0.318 < 0.8 at 0.4 noise). No bracket narrows 625 or 634; 68 (letter table) and 7480 (margin) are out of the bracketing's scope; no key change, decode_key --check exit 0. What would move them: more gloss-pinned codes from the same list (the Lyncker files, needs-physical-access, gap 4), or a second blind eye on the 625 margin word 1; done 3 Oct 2026 (GAPS199, prereg a2d13f3e): second blind native-zoom read of 625 word 1 with 5 decoys: decoys 5/5 correct, target read "geschehet?/gestellet" (low), which disagrees with "Stathalter"; 625 stays [?_Ahlefeldt] M; [retired] targeted native-zoom read (instrument: blind Opus reader on native crops), reopened only by a sign-by-sign atlas of the gloss hand or a palaeographer; done 7 Oct 2026 (D4-HDK, PREREG-D4HDK.md): de17 word-bigram context fill, held-out control on 14 C-grade gloss tokens FAIL (top-1 0.071, MRR 0.208 vs shuffled null p95 0.314; prior-only 0.000), no value scored; next: none in session for 625/634/602 beyond gap 4 (needs-physical-access)
- The 3-digit nomenclator of 1672 (601 Dennemarck, 229 Berlin, groups up to 834). Neither near-date key reads it (A2-HDK 2 Oct 2026: key 255, 1666, runs 180-407 with Dennemarck 184/212 and 229 = Frankreich; DECODE 4692, 1670s, runs 153-363 with Dennemarck 174, Berlin 281). Dänemark 131 sampled 8 of 106 leaves, all clear (Brandt's 1672 reports and the regent's drafts); done 9 Oct 2026 (HDK-131): all 106 leaves swept with a 2/2 blind positive control, 7 leaves carry Brandt's own numeral cipher (0020 0021 0049 0050 0062 0063 0064; 0020 and 0049 with a period decipherment on the leaf), but its letter table disagrees with key 255 (1/8) and its groups run about 32-272, not to 601-834, so Dänemark 131 holds no value of this nomenclator (dk131_inventory.tsv); the undigitised Lyncker files (Preußen 345, 1668; Dänemark 105, 1668; Hamburg 2, 1671-72) are the only same-sender material left - blocker: needs-physical-access; the gloss-pinned values plus key-rebuild (gap 3) are the in-session route, DECODE 4687/4688/4690/4691 (HStAM 4 d Nr. 1234) opened 2 Oct 2026 (A2-HDK3): 4691 is key 255 itself, 4690 a 1668 key (nomenclator 300-409) plus the Lincker decipher scale, 4688 a Latin cover-word list, 4687 a Paris chiffre note "va jusqu'a 712"; none reaches 834 or has Dennemarck at 601. Arcinsys lookup done 2 Oct 2026 (A2-HDK4): HStAM 4 d Nr. 1236-1238 are digitised but catalogued ca. 1715, mid-18th c. and early 19th c.; the whole 4 d Chiffern node (Nr. 1218-1238, 21 items) holds nothing dated 1671-72 beyond the already-checked 1234/1235, so no archive key for this nomenclator is catalogued there; done 3 Oct 2026 (GAPS176): the 18 gloss-pinned values scored against all 224 key tables on disk with a shuffled-assignment control (positive control flags 3-of-18 planted values): 0 candidates, 0 hits; DECODE's 1650-1690 Marburg/Danish key records are exactly 4687-4692, all opened; so no list on disk or in DECODE is this nomenclator. The list itself is now blocked: needs-physical-access (the undigitised Lyncker files Preussen 345 / Daenemark 105 / Hamburg 2 in HStAM, or a Danish-side key in Rigsarkivet), waiting-on an archive request not yet filed; the in-session part (bracketing the unglossed groups) is the gap above

## Escalation (1 Oct 2026)
- [x] siblings: done 2 Oct 2026 (NEXT-HDK, "Siblings lookup" above). HCPortal has only record 494 for 4f Dänemark, and its keys include no 4f Dänemark key. Arcinsys has Nr. 125 complete at 6 images, so nothing is missing; the cover and endorsement name the sender Lyncker and the recipient Chancellor Vultejus (M). The cached DECODE listings hold no 4 f record. Leads handed on: Dänemark 131 (digitised, same series, gap 4); two near-date chancery keys for known-keys below. Dänemark 131 fully swept 9 Oct 2026 (HDK-131): 7 cipher leaves of Brandt's own (Brandenburg resident) correspondence, glossed on 0020/0049, a different table from Nr. 125's; no sibling of Lyncker's nomenclator in it.
- [x] clear-pages: done 6 Oct 2026 (R12D-HDKV verifier, AUDIT.md "R12D-HDKV" section 2): the glossing hand is period (17th c.), M -- 17th-c. spelling throughout (Dennemarck, Kayser, Hertzog, Franckreich, as key 255 of 1666 writes them), Kurrent for names and Latin script for the loanword disgustirt (the clear text's own convention), iron-gall-type ink, letter-by-letter decipherer's note; not the letter writer's hand, not shown to be the key-255 scribe. Gloss values stay C (known plaintext). Earlier text of this item: The letter's own decipherment is the bold glossing on ff.2-4. It includes a marginal gloss beside the first dense f.4 run, which neither Cheap test 1 nor the classifier used. Only 601 is pinned. Whether the glossing hand is period or modern is unsettled (While waiting bullet 3), and that decides whether gloss values stay C or are a key-source H. The rest of Nr. 125 was never checked for a clear copy or minute. Planned: the gloss read in the transcription pass plus interlinear_align.py on each run.
- [x] known-keys: done 2 Oct 2026 (A2-HDK, "Known-keys and sibling check"). HCPortal key 255 (HStAM 4 d Nr. 1234 ff.13-16, endorsed "Clavis ... mit Secretario Lincker 1666") reads the letter's 2-digit letter cipher against its own gloss (21/26 vs control max 10 on pre-key readings; S); its nomenclator (180-407) does not read the 3-digit groups, nor does DECODE 4692 (Nr. 1235, 1670s, 153-363, names Linker 190, Vultejus 246, Resident Brand 231). DECODE 4687/4688/4690/4691 (Nr. 1234) opened 2 Oct 2026 (A2-HDK3): no nomenclator reaching 834; 4691 = key 255; 4690 holds a period decipher scale of the Lincker letter table that agrees with key.tsv on all 120 entries read. key.tsv written (197 rows, S). Not opened: key_519 and hcportal_522 (superseded for the letter table by key 255). HStAM 4 d Nr. 1236-1238 looked up in Arcinsys 2 Oct 2026 (A2-HDK4): digitised, but dated ca. 1715 / mid-18th c. / early 19th c.; the 4 d Chiffern node has no other 1670s key.
- [x] print: done 3 Oct 2026 (GAPS188). tools/print_check.py ran on 4 phrases from the clear prose and glosses, plus 2 positive controls. Controls read on IA and Google Books; they missed on OpenAlex, which is a non-test; S2 returned 429. Result: 0 phrase hits. Ribbeck FBPG 12 covers 1666-69 Berlin only. Class stays N0 (AUDIT.md addendum). Not reachable from the cloud: HathiTrust full text, and JSTOR (2 rows already queued). Danish state-paper calendars (Laursen, Wegener) were not read page by page.
- [retired] key-rebuild: instruments run and closed: gloss alignment (GAPS152-163, key_gloss.tsv, done), nomenclator bracketing (GAPS193: alphabetical order a control-backed negative, topical blocks a non-test at K=16), and context fill by a word-bigram model on tools/data/de17 (D4-HDK, 7 Oct 2026, PREREG-D4HDK.md 9a91d4a1d: held-out control on 14 C-grade gloss tokens top-1 0.071, MRR 0.208 below its shuffled-context null p95 0.314, prior-only top-1 0.000: gate FAIL, no target value scored). Earlier text of this item: never tried; planned gloss alignment, bracketing and LM context fill, ~$4. Reopened only by new material (more gloss-pinned codes of the same list, gap 4) or a different instrument (a larger era-matched corpus with the 1672 Danish-court names, or a palaeographer on the 625 margin)
- [x] image-check: done 3 Oct 2026 (GAPS155 page 2, GAPS159 page 3; confirmed by A4-RFHDK, 5 Oct 2026, from the files, no new fetch). f.4 (image 0004) was re-cut with a pasted `tools/iiif_lines.py --image ... --out images/crops_p3 ... --debug` command (14 crops, overlay `images/crops_p3/p3_lines_debug.jpg`), read in two blind passes and reconciled on native zooms: "6d" = 60 (M), "bb" = 66 (M), "96" confirmed (M, gloss o), run 1 "143" = 113 (M); all four as such in ciphertext.tsv (p3_15.6, p3_16.10, p3_21.2, p3_16.1). The 625/774/775 "section counter" exclusion is withdrawn: all three stand inline as glossed codes (774 Holland C, 775 Gen. Staden C, 625 [?] Ahlefeldt M; GAPS155/GAPS168). The old f4_top/f4_mid crops stay lost and are superseded by crops_p3. No further re-read needed; the full two-pass transcription named as ~$11 is the one GAPS152/155/159 already ran.
- [x] retry: done 7 Oct 2026 (D4-HDK): no key extension survived its control, so the retry reruns the unchanged key; `tools/decode_key.py ciphers/hessen-daenemark-1672 --check` exit 0, tokens 65: C 9, I 1, M 25, S 28, U 2, reading up to date; no regrade. Earlier text: nothing to retry yet; planned after the gloss read and key-rebuild
BRANDT-TX, 9 Oct 2026: 0020 lower block transcribed (258 groups, two blind passes 97.2%) and its gloss read; the pre-registered alignment gate FAILed (CONSISTENT 9 vs shuffle max 12) while an exploratory token-agreement count separates widely (95 vs max 49); next: a pre-registered agrees-count gate on these pairs plus the held-out 0049 letter test, CPU and one 0049 transcription, ~$3.
HDK-BRANDT, 9 Oct 2026: Brandt's glossed cipher on Dänemark 131 was checked as a separate candidate (section above): verdict open (conditional on 12 unopened Urkunden und Actenstücke volumes and no Hessian-side edition located), about 60-70% of its estimated 600-700 groups sit on leaves with a period gloss; next in-session step is the 0020 two-pass transcription plus interlinear_align against its marginal gloss with the 0049 pairs held out, about USD 6-9, for the orchestrator to brief as its own target.
BRANDT-GATE, 9 Oct 2026: both pre-registered gates PASS (0020 agrees 95 vs control max 54, p 0.0005; 0049 held-out letters 34/48 vs control p99 12): 16 Brandt letter-table values grade C from the period gloss on two leaves, 8 M (values_gate.tsv); next: 0020 upper block + 0021 with the C values as a prior, then the unglossed 0062-0064 under a matched control, ~4.
V-BRANDT, 9 Oct 2026 (verifier): BRANDT-GATE test 2 holds on blind passes (independent evidence); test 1 is a re-score of an already-seen number; BRANDT-UP's LCS gate FAILs on both blind gloss passes, so its 23 C tokens are M; value 46 regraded M (15 C, 9 M); next: a blind re-read of 0020 margin lines 1-2 not shown the values, ~1.5, then score_up.py unchanged.
BRANDT-UP, 9 Oct 2026: 0020 head block (44 groups) and 0021 (8 groups) transcribed (two blind passes, 46/46 and 8/8 agree); the 16 C values cover 25 of 52 groups and match the period gloss on 23 (LCS 23 vs permutation control p99 19, p 0.0005, PREREG-BRANDT-UP PASS): 23 tokens C, 29 M; next: the unglossed 0062-0064 under the C values with a matched control, ~4.
BRANDT-062, 9 Oct 2026: of 0062-0064 and 0050 only 0062 carries cipher (6 lines, 62 groups, two blind passes 66/66 agree); 0063/0064/0050 hold mirror show-through of 0062 and 0049, so no unglossed Brandt cipher was found on them. 0062 is fully glossed: the 16 C values cover 22 groups and match the gloss on 20 (LCS 20 vs control p99 14, p 0.0005, PREREG-BRANDT-062 PASS): 18 tokens C, 44 M; next: a Google Books phrase search on the 0062 gloss when the quota resets (~$0.3), and the 0062 L03 pos 1-4 / "gulden[?]" settling with a second eye, ~1.5.
BRANDT-REGRADE, 9 Oct 2026: V-BRANDT regrades applied (46 C->M: 15 C, 9 M; BRANDT-UP 52 tokens all M); 0062 re-scored on two blind gloss passes under PREREG-BRANDT-062B (A 19 vs p99 14, B 18 vs p99 14, p 0.0005 each: PASS both), so 0062 keeps its C grades minus value 46 (C 18 -> 17, M 45); next: the 0020 margin lines 1-2 blind re-read (V-BRANDT item 3, ~1.5) and a Google Books phrase search on the 0062 gloss (~$0.3).
BRANDT-MARGIN, 9 Oct 2026: two blind reads of the 0020 margin lines 1-2 ("Lues Hauszelt/Hauszeit", not "eine heuraht") and score_up.py unchanged on them under PREREG-BRANDT-MARGIN: FAIL both (17 vs p99 17; 18 vs p99 18), so BRANDT-UP stays M 52; the 0062 gloss Google Books search hit HTTP 429 on its first call (non-test); next: the 0062 phrase search after the quota reset, ~$0.3 (phrases_0062.txt ready).
GB-PHRASE, 9 Oct 2026: the 0062 gloss Google Books phrase search ran (positive control answered; 4 phrases + 3 targeted queries, snippets read): no hit about this letter; that BRANDT-062/BRANDT-MARGIN step is done.
Verdict: keep going: 3 internal gaps. HDK-131, 9 Oct 2026: the full Dänemark 131 sweep found Brandt's own glossed cipher (7 leaves), not this nomenclator, so the siblings rung adds nothing to gap 4. GAPS188, 3 Oct 2026: the print check is done, with 0 phrase hits and N0 held. The nomenclator list itself is blocked: needs-physical-access (the Lyncker files in HStAM, or a Danish-side key in Rigsarkivet). GAPS193, 3 Oct 2026: the bracketing is done. Alphabetical order is a control-backed negative and topical blocks are a non-test at K=16, so the unglossed groups are now open-codes. GAPS199, 3 Oct 2026: the second blind read of the 625 margin word 1 is done. Its decoys read 5/5 and the target disagrees with "Stathalter" (geschehet?/gestellet), so 625 stays M and that instrument is [retired] for this word. R12D-HDKV, 6 Oct 2026: the separate verifier re-derivation is done (decode_key --check exit 0; an independent script keys/r12d_rederive.py agrees on all 65 tokens, 0 diffs; 33/33 letter-table cells used agree with the key 255 f.13 image by eye), and the clear-pages question is answered (glossing hand period, M; AUDIT.md). D4-HDK, 7 Oct 2026: the key-rebuild context fill ran (de17 word-bigram, held-out control FAIL: top-1 0.071, MRR 0.208 vs null p95 0.314), so key-rebuild is [retired] and the retry reran the unchanged key (--check exit 0); no in-session step is left untried; cheapest next: open-codes 625 x2 / 634 / 602 wait on more gloss-pinned codes of the same list, ~$0 in session; the nomenclator list itself stays blocked: needs-physical-access (gap 4: the Lyncker files in HStAM or a Danish-side key)

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
