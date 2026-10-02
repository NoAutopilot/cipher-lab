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

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
Read so far: unmeasured. No ciphertext.txt, ciphertext.tsv or key.tsv exists. The only committed value is 601 = "Dennemarck" (grade C, glossed 3x on f.4; Cheap test 1). Cheap test 1's "~40 code tokens, ~20 distinct values" was a rough count, and it is an undercount. It excluded 625/774/775 as "section counters", but on a 1000-px preview of image 0003 (this pass, adversarial check, M) 774 and 775 stand inline in the prose with bold glosses above or beside them. It also called f.2 "plain", yet image 0002 carries at least one inline glossed code in its last lines. So any "~3 of ~40 (~7%)" figure is not a measurement. Note that images 0002-0004 are HCPortal image numbers, not checked foliation: 0003 has its binding on the right and faces 0004, so it is a verso.
- ff.2-4 (images 0002-0004), every inline code group that carries a bold interlinear or marginal gloss. On the preview these include 651 (by "Cur Brandenburg"), 653, 229 ("Berlin"), 774, 775 ("Ga. Stadt") and the marginal 625 gloss on 0003; on 0004, 756/768, 229, 427 641 ("herzog von Ploen"), 303, 447 and 834; on 0002, the code in its last lines. None of these is pinned code by code - blocker: not-attempted; images at 2600x3944 px are on disk and legible enough that most 3-digit codes visibly carry a gloss, so the gloss coverage is much wider than "1 of 20". Cheap test 1 stopped at a breadth cap, and the iiif_lines.py crop step in its brief (.claude/briefs/runs/2026-09-26-lane-b7-hcp.md, item A) was never pasted. The f4_top/f4_mid crops cited in NOTES are not on disk; next: run `tools/iiif_lines.py --image` on all three images and paste the output. Then do 2 blind Sonnet passes per page on line crops only (6 calls), 1 reconciliation (Usage 6: N reads + 1), `tools/reconcile_passes.py`, ciphertext.tsv and key.tsv from legible glosses only (C/M per value), and `tools/decode_key.py --check`. That is about 7 calls at the AX-COMP2 rate of ~$1.46/call, ~$11
- f.4 (image 0004), the two dense runs "FF. 69. 85. 33. XX. 6d(?). LL. 143. WW. 119. 74. 26. 24. 83. 117. 20. bb(?). 37. 104. 634." and "63. 38. 21. FF. 20. 75. 20. WO. 96(?). NN. 30. 31. 110. XX." (preview reading, M; "6d" and "bb" are doubtful tokens). The first run has a marginal gloss in the left margin (on the preview roughly "disgustirt und ertanin holstein", M). The second has letter- or syllable-sized interlinear glosses ("seco", "g:ott", "g&6", "d af", "amm"). That pattern suggests the 2-digit codes are letters or syllables, so this is a crib. Neither Cheap test 1 nor the classifier used the marginal gloss - blocker: not-attempted; the material is on disk and needs no outside help; next: after the transcription pass, align each run against its own marginal and interlinear gloss with `tools/interlinear_align.py` (grade C per value). Test whether FF/XX/LL/WW/NN/WO are nulls or separators. Run key_519 (ciphers/malsburg-hessen-1636/keys/key_519.tsv, 2-digit homophonic, HStAM 1607) as a known-answer test against the gloss, which is a real known-answer control, not the degenerate coverage control bMALK warned about. ~$3
- Every code group still unglossed after the two steps above (count unknown until the transcription exists) - blocker: not-attempted; no key-rebuild, bracketing or context fill has ever been run, so these cannot yet be called open-codes; next: bracket the 3-digit nomenclator against the gloss-pinned values (is 229 "Berlin" < 601 "Dennemarck" < 651/653 "Brandenburg" < 774 "Holland"(?) an alphabetical order?). Fill slots from the clear German/Latin context, grade S only with a matched code+mark control at the letter's own N, then rerun decode_key.py --check. ~$4
- Same-office sibling files (Nr. 125 itself is complete at 6 Arcinsys images, NEXT-HDK 2 Oct 2026: 0001 a modern cover, 0002-0004 the letter, 0005 the endorsed verso, 0006 an unrelated 1738 print. Nothing of this letter is missing.) The digitised Dänemark 131 (1671-74, Brandenburg resident Brandt at Copenhagen) and the undigitised Lyncker files (Preußen 345, 1668; Dänemark 105, 1668; Hamburg 2, 1671-72) may carry the same nomenclator - blocker: not-attempted; the siblings lookup above listed them but opened none; next: open Dänemark 131's Arcinsys images and look for code groups in the 3-digit range used here. Only if it shares the system, write REQUEST.md for the undigitised Lyncker files to marburg@hla.hessen.de. ~$1

## Escalation (1 Oct 2026)
- [x] siblings: done 2 Oct 2026 (NEXT-HDK, "Siblings lookup" above). HCPortal has only record 494 for 4f Dänemark, and its keys include no 4f Dänemark key. Arcinsys has Nr. 125 complete at 6 images, so nothing is missing; the cover and endorsement name the sender Lyncker and the recipient Chancellor Vultejus (M). The cached DECODE listings hold no 4 f record. Leads handed on: Dänemark 131 (digitised, same series, gap 4); two near-date chancery keys for known-keys below.
- [ ] clear-pages: not done. The letter's own decipherment is the bold glossing on ff.2-4. It includes a marginal gloss beside the first dense f.4 run, which neither Cheap test 1 nor the classifier used. Only 601 is pinned. Whether the glossing hand is period or modern is unsettled (While waiting bullet 3), and that decides whether gloss values stay C or are a key-source H. The rest of Nr. 125 was never checked for a clear copy or minute. Planned: the gloss read in the transcription pass plus interlinear_align.py on each run.
- [ ] known-keys: not done. KEY-OFFICES.tsv and KEY-DESIGN.tsv hold no Hesse-Kassel key of the 1670s. The classifier missed two same-archive items already on disk. One is ciphers/malsburg-hessen-1636/keys/key_519.tsv (HStAM 4 d Nr. 1219, 1607, 2-digit homophonic letter table; testable on the f.4 2-digit runs). The other is keys/hcportal_522.jpg (HStAM 4 d Nr. 1234, c.1660, a Kassel chancery French nomenclator running to code 712, with 713-716 added; HCPortal "Solved"), the nearest-decade 3-digit nomenclator of this office on file. There is also Bourdeau's marburg1635 (HStAM 4 d Nr. 1218, per malsburg NOTES step 1). design_prior.py has never been run. The siblings lookup (2 Oct 2026) adds two nearer-date candidates from the same chancery: DECODE key record 4692 (HStAM 4 d Nr. 1235, "1670", 1 page; never cited in this repository before) and HCPortal key 255 (HStAM 4 d Nr. 1234 ff.13-16, c.1666, nomenclator, 4 images on api.hcportal.eu). Planned: fetch HCPortal key 255 and the Arcinsys image of 4 d Nr. 1235 if digitised, compare their code ranges with this letter's (up to 834); key_519 known-answer test on the glossed run, a range/design comparison with 522, and design_prior.py once the code inventory exists, ~$2.
- [ ] print: not done. Only one OpenAlex and one Semantic Scholar query were run (intake 5-6, 0 hits). No edition, calendar or documentary series was searched. Candidates come from the letter's own content (an envoy writing from Hamburg 4/14 May 1672 to a Hessian chancellor about the Danish king, Brandenburg, the Dano-Brunswick foedus and the Plön duke): Urkunden und Actenstücke zur Geschichte des Kurfürsten Friedrich Wilhelm von Brandenburg, and Danish state-paper calendars. Sender and recipient are now named (Lyncker to Chancellor Vultejus, M, siblings lookup 2 Oct 2026), which gives searchable names. Planned: tools/print_check.py with phrases from the transcribed clear prose, ~$2-3.
- [ ] key-rebuild: never tried. No transcription and no key.tsv exist. Planned: gloss alignment, then nomenclator bracketing and LM context fill with a matched control on any S claim, ~$4.
- [ ] image-check: not done. No sign-by-sign transcription exists. The crops f4_top.jpg/f4_mid.jpg cited in Cheap test 1 are not on disk, and no iiif_lines.py output was pasted. The doubtful tokens "6d", "bb" and "96" in the f.4 runs, and the 625/774/775 "section counter" exclusion, need re-reading against the native image. Planned: as gap 1, ~$11.
- [ ] retry: nothing to retry yet, because no key extension exists. Planned: after the gloss read and the key-rebuild, rerun every code group and every M lead through decode_key.py and regrade per token.
Verdict: keep going: 4 internal gaps; cheapest next: first the check-solved open-web and blog-comment step that the intake gate requires (check-solved.md steps (a)-(c), not yet run; A2-HDK 2 Oct 2026 found it missing, ~$0.5) and its adversarial Premise check (~$0.5), then the known-keys and sibling check (fetch HCPortal key 255 and the Arcinsys image of HStAM 4 d Nr. 1235 / DECODE 4692, open the digitised Dänemark 131, compare code ranges), ~$2; the step that moves the reading is the 3-page transcription and gloss pass, ~$11

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
