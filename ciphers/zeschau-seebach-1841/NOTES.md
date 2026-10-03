partial
No printed edition of these Zeschau-Seebach dispatches exists; IA full-text search (be-api fts, 4 queries incl. "Zeschau" "Seebach" chiffre and "Albin Leo von Seebach") and Google Books (3 queries, 0 hits) read by this worker 3 Oct 2026, letters absent; HStAD 10731 Nr. 12 catalogue record read ("Ministerialdepeschen", 1841-1849, digitalisatExists: false).
Status `partial` (CHECK-ZESCHAU, 3 Oct 2026): six-source check finds no decipherment anywhere; Bourdeau holds 7 grade-I syllabary values from the rubbed R5005 gloss and we hold 692 transcribed R5006 digits, so the target is partly in hand, not untouched.
Read (26 Sept 2026, bZES): Bourdeau's `zeschau1841/` folder and CATALOGUE.md #53 in full at HEAD fc0c9e8
(25 Sept 2026, `github.com/dbourdeau/cyphersolver`, shallow clone, deleted after); Aymeloglu's
`catalogue/decode-records.jsonl` at HEAD (`github.com/aaymeloglu/unsolved-ciphers`, shallow clone, deleted
after, no per-item solve, catalogue mirror only); DECODE's own RecordsList cache
(`sources/decode/records-non-decrypted-2026-09-24.tsv` rows 849-852) plus one live `RecordsView/5006` fetch
(200, "Access mode: Authentication required", thumbnail template unfilled without a session); one OpenAlex
query (`search=Zeschau Seebach cipher`, 0 results) and one Semantic Scholar query (same terms, 0 results).

## Who, what

Heinrich Anton von Zeschau (Saxon foreign minister, Dresden) to Albin Leo von Seebach (Saxon minister resident,
St Petersburg). Saxon Main State Archive Dresden, HStAD 10731 Sächsische Gesandtschaft in Russland, Nr. 12.
DECODE R5005 (18 Jan 1841, French), R5006 (6 Apr 1842, French), R5007 (13 Jun 1842, German; DECODE's own record
mistypes the year as 1846), R5008 (26 Oct 1843, German). Bourdeau CATALOGUE.md #53.

## Established (H/C-grade facts, not our cryptanalysis)

- R5005 is fully transcribed by Bourdeau: 3,969 digits, unseparated two-digit groups (96 of 100 pairs occur),
  about 70 lines across 6 images / 5 written spreads. Source: `zeschau1841/ct_R5005.txt`,
  `zeschau1841/ct_R5005.digits.txt` (Bourdeau, MIT code / CC BY 4.0 text, credited).
- The cipher is a syllabary, not a letter substitution (Bourdeau's own diagnosis from a faintly-visible pencil
  decipherment still on R5005 p.5 right, line a5_03: `11 70 82 34 29 40` glossed "la pre m i er e").
- Seven values recovered from that gloss: **11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que** (46 from the end of
  line a8_05). Grade **I** (inferred from a rubbed, partially-legible pencil trace, not a clean key source) --
  Bourdeau's own NOTES.md does not claim these as certain.
- Bourdeau tried these values on R5005 only (homophonic/syllabary annealers seeded with the glosses, all
  failed to produce French) and explicitly did **not** try them against R5006-R5008 ("R5006-R5008 are not
  transcribed yet" -- his own NOTES.md, "What would move it" item 3).
- R5006/R5007/R5008 have no ciphertext transcription anywhere found: not in Bourdeau's `zeschau1841/` folder
  (only `ct_R5005.*` exist), not in Aymeloglu's catalogue mirror (metadata only, `Available Documents: ""` for
  all four ids), not on DECODE without login (see below).
- DECODE's own status for all four records is "Partially decrypted" ("interlinear decrypted, but unfortunately
  rubbed out"), page counts R5005=9, R5006=2, R5007=3, R5008=3 (`sources/decode/records-non-decrypted-2026-09-24.tsv`).
- No printed edition of this correspondence found by Bourdeau or by this pass's OpenAlex/S2 queries (0 hits
  each); not searched further per the intake step's minimal scope.

## The test this job was assigned, and why it stopped

Brief: apply the 7 recovered syllabary values to R5006-R5008 as a crib wherever their ciphertext is on disk,
with a random-digit-string coverage control and an order-scrambled German-bigram control (CLAUDE.md rule 3,
order-sensitive statistic since a coverage figure alone cannot distinguish a real crib from noise -- see
CLAUDE.md's "bCAS"/"AX-5799" lesson on non-tests, 26 Sept 2026).

**Blocked before the test could run: no ciphertext for R5006, R5007 or R5008 exists on any disk this account can
read.** Checked, in the Access playbook's order:
1. Bourdeau's own folder -- absent (confirmed above).
2. A DECODE attachment readable without login -- absent. `RecordsView/5006` (live fetch, 26 Sept 2026, 200 OK,
   one request) shows the record's own "Access mode: Authentication required" field, and the page's image
   slots are an unfilled `{{>thumbnailUrl}}` template with only a 1x1 placeholder GIF as the actual `src` --
   no image URL is exposed to an unauthenticated fetch, consistent with the Access playbook's account-wide
   DECODE image block (confirmed on 25 other records across 6 institutions, ASKS.md row 42) and with
   Aymeloglu's mirrored `"Paper Access Mode": "Authentication required"` for all four ids.
3. The holding archive itself -- QUEUE.md's own CS2-09 entry (LANE N4 scARCH2, 24 Sept 2026) already resolved
   this exact shelfmark (`archiv.sachsen.de`, guid `fb8ee3d8-3829-4665-8b8f-45c2574196d7`) to
   `digitalisatExists: false`: the whole Nr. 12 dispatch file is not digitised at all, so no route through the
   archive's own site gets an image either. Not re-fetched this pass (already on file, dated).

No browser login was spent (the Access playbook already establishes the DECODE image block holds even when
logged in, so a login would not clear it); no image or archive host was newly hit beyond the one `RecordsView`
GET above.

Per CLAUDE.md's rule 9a/ASKS.md convention, the only route left is a physical copy order from HStAD Dresden for
10731 Sächsische Gesandtschaft in Russland, Nr. 12 (a mixed ministerial-dispatch file, not letter-specific --
the exact leaves for R5006/R5007/R5008 within it are not known from any metadata read this pass). Not written
as a fresh REQUEST.md this job (out of the brief's scope and cap); ASKS.md row 42 already covers the general
DECODE account-wide image block this finding rests on.

## Credit

Bourdeau, `dbourdeau/cyphersolver`, `zeschau1841/` folder and CATALOGUE.md #53, read 26 Sept 2026 at commit
fc0c9e8 (25 Sept 2026 18:14 CDT). MIT code, CC BY 4.0 text. The 7 syllabary values above are his recovery, not
ours.

## GAPS173-zeschau-seebach-1841 (3 Oct 2026, account-4)

Step run: Next step 1 (the HStAD Dresden copy order) needs a person, but its purpose -- images of R5006-R5008 --
has a cloud route since 28 Sept 2026: DECODE serves full-size scans after a browser login (sources/decode/NOTES.md
"Full-size images: access after the PI's extension", DECODE-OPEN, which fetched only the first image of each of
these records). This pass ran that route for all six images.

- One login (`tools/decode_browser_login.js 5006 <scratch> --fetch-page RecordsView/5007,5008 --guess-fullsize`,
  `loggedIn: true`, 3 Oct 2026 16:59-17:00 UTC). Six full-size JPEGs, all 7214x5412, none the `forbidden.png`
  placeholder. Images stay in the session scratchpad only, never in this repository (the PI's reminder: the holding
  archive's permission may be needed before any image is published); a later worker refetches them the same way.

| file | sha1 (12) |
|---|---|
| IMG_R5006_I28865_P1.jpg | 483bbb1d719f (matches DECODE-OPEN) |
| IMG_R5006_I28865_P2.jpg | 27186d7b5d48 |
| IMG_R5007_I28868_P1.jpg | b5ec8e9e93cd (matches DECODE-OPEN) |
| IMG_R5007_I28868_P2.jpg | c081766ef775 |
| IMG_R5008_I28871_P1.jpg | 86e6105b60fe (matches DECODE-OPEN) |
| IMG_R5008_I28871_P2.jpg | 17a51f08bf33 |

- Vision call 1 (downscaled overview of R5006 p.1): heading "No. 13", "Dresde, ce 6 Avril 1842", clear French
  opening "J'accuse la réception de Vos rapports inclus le n° 17 du 22 Mars", then 9 lines of unseparated digits
  on the leaf, which takes about a third of the image width (the rest is the copy-stand background). A red archival
  foliation note sits at the foot (not read).
- Vision call 2 (one native-resolution line crop, `tools/iiif_lines.py --image` on a local crop of the page body, 8
  lines found): the first cipher line is fully legible, about 68 digits, written in the same unseparated style as
  R5005. Faint pencil traces show above the digits, which fits DECODE's own note "interlinear decrypted, but
  unfortunately rubbed out". No digit string is committed here: one unchecked read is not a transcription (rule 2/4).
- Estimate, from 9 lines x ~68 digits on R5006 p.1: about 600 digits a page, roughly 3,000-3,600 digits over the
  six pages, nearly doubling the 3,969 digits of R5005 now on disk (Bourdeau).
- Not done: no transcription, no crib test, no reading. Status word left `blocked` for the parent to change: the
  outside blocker it named (no images anywhere reachable) no longer holds.

Requests: de-crypt.org 1 login + 3 RecordsView + 12 filesrv (6 thumbnails, 6 full-size) = about 17, 2 s apart, one
at a time. No other host.

## Next step (refreshed 3 Oct 2026, GAPS173)

1. Transcribe R5006-R5008 (6 pages) from the DECODE scans: refetch them with one login as above, crop with
   `tools/iiif_lines.py --image`, two blind passes a page on line crops (one page per subagent call), then
   `tools/reconcile_passes.py`. That is 12 pass-calls + 1 reconciliation at the 3 Oct ledger's Opus native-vision
   rate (USD 3.5-10 a pass), about USD 45-65 in total.
   Mark the rubbed pencil traces above the digits as they are found: they may give more gloss values (grade I).
2. Then apply Bourdeau's 7 values as a crib with the coverage + order-scrambled controls the bZES brief specified.
3. The HStAD copy order (ASKS 64, SEND-QUEUE S5, still `queued` on 3 Oct) is no longer needed to get images; the
   parent decides whether to hold S5 or reword it as a permission/quality request. Multispectral/UV imaging of
   R5005 (Bourdeau's suggestion) stays a person/archive step.

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/zeschau1841/NOTES.md
- Their extent, in their words: attempted, open: system identified, a few code values from the erased decipherment, letters not read
- Their date: by 25 Sept 2026 (undated in NOTES)
- Note: already cited in our NOTES.md (bZES, 26 Sept)
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## GAPS175-zeschau-seebach-1841 (3 Oct 2026, account-4)

Step run: transcribe R5006 p.1 only (the first page of Next step 1).

- Image: one DECODE browser login (a second one, after the first run's `--max-files 1` spent its single fetch on the
  thumbnail; the run before that failed at `page.goto` on the container's TLS proxy before any credential was sent,
  fixed with the playbook's `certutil` line). `IMG_R5006_I28865_P1.jpg`, 7214x5412, sha1 483bbb1d719f -- matches the
  GAPS173 table. The full scan stays in the session scratchpad, out of git.
- Crops: `python3 tools/iiif_lines.py --image <scratch>/IMG_R5006_I28865_P1.jpg --region 2420,1960,2360,1900
  --out ciphers/zeschau-seebach-1841/images --prefix r5006p1 --debug` -> 9 bands of 2360 px, overlay checked
  (`images/r5006p1_lines_debug.jpg`). L01 is the clear French line ("J'accuse la réception de Vos rapports inclus le
  n° 17 du 22 Mars"); **L02-L09 are the cipher: 8 lines, not the 9 GAPS173 estimated.** Folder 0.9 MB.
- Two blind Opus passes per half-page (L02-L05, L06-L09): 4 vision subagent calls. The two passes used different
  prompts and methods (A: whole line; B: thirds, joined). A grep of each subagent's tool inputs found no read of the
  other pass's folder.
  `tools/reconcile_passes.py passA passB --split-chars`: **agreement 500/501 = 99.8%** (err_2reader 0.2%), 1
  disagreement (L02 col 35: A dropped a 7; the crop reads "...5587159...", B is right). Agreed signs both passes read
  as H: 465. Agreed signs where at least one pass read M: 35. The reconciler spot-checked L06, the line with the most
  uncertain signs (10), on two native crops and confirmed it. err_true is not measurable: BENCHMARK-TX.tsv has no item
  for this hand or for a digit cipher. High two-reader agreement on one model family is not accuracy (TRANSCRIPTION.md
  "Why").
- Result: **501 digits** (lines 69/66/61/59/59/62/58/67) in `transcription/r5006p1_ciphertext.txt` (one line per row)
  and `transcription/r5006p1_ciphertext.tsv` (line, pos, digit, conf H 466 / M 35, alt, why, pencil_above,
  pencil_grade). Raw passes, agreement and disagreements are in `transcription/passes/`. The total is odd and four
  lines have odd length. If the cipher is in pairs (R5005: 96 of 100 pairs occur), either a pair runs onto p.2 or one
  digit is missing or extra. This is not checked, and no pairing is committed.
- Pencil column: neither pass read a single letter. Pass A has 9 trace rows and pass B 14, all "strokes": rows of
  faint short vertical ticks above the digits, densest on L05 (M in both passes) and L06. 365 of 501 digits sit under
  at least one pass's trace span. Graded M at most, spans approximate. Two explanations are open and not settled
  here: show-through from the back of the leaf (whose mirrored cursive is visible on every crop), or pencil
  tick-marks dividing the digit stream into groups. The reconciler's own look at L06 favours regular ticks a digit or
  two apart, but that is one eye on one line. No gloss pairs were recovered from p.1, so DECODE's "interlinear
  decrypted, but rubbed out" is not borne out here as legible text.
- No reading, no crib test (Bourdeau's 7 values are not applied).

Requests: de-crypt.org 2 logins (plus 1 failed navigation before login), 2 RecordsView, 1 thumbnail, 1 full-size =
about 6, 1.5 s apart. No other host.

## GAPS179-zeschau-seebach-1841 (3 Oct 2026, account-4)

Step run: transcribe R5006 p.2 (the Verdict line's cheapest step).

- Image: one DECODE browser login (`tools/decode_browser_login.js 5006 <scratch> --guess-fullsize --delay 2000`),
  4 files: 2 thumbnails, 2 full-size. `IMG_R5006_I28865_P2.jpg`, 7214x5412, sha1 27186d7b5d48, matching the GAPS173
  table. The full scan stays in the session scratchpad, out of git.
- Layout (downscaled overview, 1 vision call): p.2 is an open spread. **Only 3 cipher lines**, at the top of the left
  page. The rest of the left page is clear French (a passage on the estate of a deceased councillor at Moscow,
  then "Eu égard à la demande de Madame ..."). The right page is clear French, the closing formula, the signature and the
  address to Seebach at St Petersburg. The clear text is not transcribed here; it is the letter's own clear text,
  not a gloss of the cipher. GAPS175's "about 600 digits a page" estimate therefore does not hold for p.2.
- Crops: `python3 tools/iiif_lines.py --image <scratch>/IMG_R5006_I28865_P2.jpg --region 1330,1380,2340,660 --out
  ciphers/zeschau-seebach-1841/images --prefix r5006p2 --debug` -> "region 2340x660, 3 lines, 3 bands x 1 segments;
  pitch 214", 3 crops of 2340 px. Overlay checked (`images/r5006p2_lines_debug.jpg`, 1 vision call).
- Two blind Opus passes, one call each, since all 3 lines fit in one call: A read whole lines; B read overlapping thirds at 2x
  and joined them itself (overlaps reported, 5-6 digits each). Neither prompt named the other pass's folder.
  `tools/reconcile_passes.py passA passB --split-chars`: **agreement 191/192 = 99.5%** (err_2reader 0.5%), 1
  disagreement. L03 col 55: A read `...411216...` and B `...41216...`. On a 6x crop the reconciler sees one downstroke
  after the 4, with a wide head and an ink blot beside it. Settled to B's single `1`, graded M, alt `11`.
  Agreed signs read H by both passes: 176 (the reconciler's 177, less the settled sign). Agreed signs where at least one pass read M: 14.
  The M signs are mostly retouched digits (heavier ink over a first digit: L01 48/54/55/57, L02 30/54), so the
  writer corrected the cipher on the page. L03 18 (`9`, or `0`+tail) is the main doubtful sign. err_true is not measurable:
  BENCHMARK-TX.tsv has no item for this hand.
- Result: **191 digits** (lines 64/63/64) in `transcription/r5006p2_ciphertext.txt` and `transcription/r5006p2_ciphertext.tsv`
  (H 176 / M 15; same columns as p.1). Raw passes, agreement and disagreements are in `transcription/passes/`. R5006 now has 692 digits
  (501 + 191), an even total. If p.1's odd count is real, the pairs run across the page break. This is not
  checked, and no pairing is committed.
- Pencil: no letters again. Both passes saw only faint grey ticks. Pass B places them *below* the digits (between
  the digits and the underline flourishes), not above. It saw no show-through on p.2. Pass A logged each whole line as `strokes` (L).
  The column is still named `pencil_above` for format parity with p.1. Graded M at most.
- A marginal mark right of L02 ("Sy"/"Sp" with a flourish, both passes) is not a digit and not counted. It sits beside
  the red marginal note between the two pages (not read).
- No reading and no crib test.

Requests: de-crypt.org 1 login + 1 RecordsView + 2 thumbnails + 2 full-size = about 6, 2 s apart. No other host.
Vision calls: 3 by this session (overview, overlay, the reconcile crops), 2 subagent passes.

## Status word (GAPS179, 3 Oct 2026)
Line 1 stays `blocked`, although the outside blocker it named (no images reachable) is gone since GAPS173.
`tools/intake_gate_check.py` treats `blocked` as terminal (exit 0, "nothing to gate"). A scratch copy with line 1 set to
`partial` exits 1. In turn it lacks: (1) a standard-edition citation or full-text phrase on the status line (none exists:
no printed edition found, bZES); (2) a `## Web and blog check` section; (3) a `## Premise check` section. A check-solved
worker writing those three is what moves the word to `partial` (~$4.5). Deep transcription has gone ahead under the
parent's GAPS briefs.

## GAPS185-zeschau-seebach-1841 (3 Oct 2026, account-4)

Step run: the crib test of Bourdeau's 7 published values on R5006's 692 digits (the Verdict line's cheapest step).
Pre-registered in `PREREG-GAPS185.md` (commit b75a39a8, 18:08 UTC, before any statistic). Script `crib_test.py`
(seeded; `--check` exits 0), output `crib_test.json`. R5005 reference text: Bourdeau's `ct_R5005.txt` and
`offsets.json`, snapshot in `sources/cyphersolver/2026-10-03/zeschau1841/` (HEAD a439937, CC BY 4.0, credited; no
code copied). Script only: no vision, no subagents.

**Overlap with Bourdeau (rule 8).** Transcribing R5006-R5008 and testing his seed values on them is Bourdeau's own
stated next step ("What would move it" item 3 in `targets/zeschau1841/NOTES.md`, dbourdeau/cyphersolver), and his
target table shows he has viewed those images. The 7 values are his recovery; GAPS175/179's R5006 transcription and
this test are ours, done in parallel with his plan, not ahead of it. The parent weighs offering him the 692 digits.

| statistic | R5006 target | shuffled-digit control (2,000 draws) | p | verdict (prereg) |
|---|---|---|---|---|
| T1 cosine of the pair profile to R5005 | **0.886** | mean 0.760, p95 0.805 | **0.0005** (the floor at 2,000 draws) | PASS |
| T2 share of pairs that are one of the 7 pins | 0.099 (34 of 345) | mean 0.080, p95 0.104 | 0.106 | not significant (support only) |
| T3 Spearman, pin counts R5006 vs R5005 (7 points) | 0.273 | -- | -- | reported, no gate |

- Parsing: the 692-digit stream concatenated in page/line order; the fixed rule (higher pair IC) picked phase 1, 345
  pairs, pair IC 0.0141 (R5005 0.0142 on 1,846 pairs under Bourdeau's per-line phases).
- Power at the target's N (positive control): 200 random 692-digit windows of R5005 against the rest of R5005, each
  with its own 200-draw shuffled null: **200/200 reach p < 0.01** (window cosine mean 0.880, their null mean 0.773).
  R5006's 0.886 sits right on R5005's own self-similarity at this length.
- The control can differ from the target: shuffling digits changes the pair counts, which both statistics are
  computed on (a pair-level shuffle would have tied by construction and was not used).
- Pin counts in R5006: 11 (la) 7, 70 (pre) 2, 82 (m) 5, 34 (i) 6, 29 (er) 5, 40 (e) 3, 46 (que) 6. Pin coverage 9.9%
  against 11.1% in R5005.
- Not pre-registered, descriptive only: two of Bourdeau's four long R5005 repeats occur verbatim in R5006,
  `7778948206` (5x in R5005) once (p.1 L04) and `06777818711001` (3x in R5005) once (p.1 L06); `2437784` and `00866`
  do not occur.

What this licenses: R5006 shares R5005's pair profile beyond its digit frequencies, so it is consistent with the same
two-digit syllabary. The 7 values may be applied to R5006 as pins. Rule 4 grades: the pins stay **I** (Bourdeau's
values from a rubbed gloss, his own grade). Applied in R5006 they are at most **M**: 34 tokens (7+2+5+6+5+3+6), 0 H,
0 C, 0 S. No token is read, no plaintext is claimed, and nothing is shown about whether the values themselves are
right. T2's non-result means the pins do not stand out in R5006 beyond digit frequencies at N=345 pairs. A
single global phase is wrong wherever an odd-length line shifts the pairing, so the test is conservative there.
Rule 10: no novelty claim.

## GAPS190-zeschau-seebach-1841 (3 Oct 2026, account-4)

Step run: the Verdict line's "transcribe R5007 p.1". **R5007 p.1 carries no cipher**, so the job transcribed R5007's
first cipher page instead, the left page of the p.2 spread.

- Image: one DECODE browser login (`tools/decode_browser_login.js 5007 <scratch> --guess-fullsize --delay 2000`;
  the container first needed the playbook's `certutil` line, since the first attempt failed at `page.goto` with
  ERR_CERT_AUTHORITY_INVALID before any credential was sent). It returned 2 thumbnails and 2 full-size images.
  `IMG_R5007_I28868_P1.jpg` sha1 b5ec8e9e93cd and `IMG_R5007_I28868_P2.jpg` sha1 c081766ef775, both 7214x5412, both
  matching the GAPS173 table. The full scans stay in the session scratchpad, out of git.
- Layout (downscaled overviews, 2 vision calls). **p.1 is clear German only**: "No. 18", "Dresden, am 13. Juni 1842",
  the salutation, then about 20 lines of clear text down to the foot (not transcribed). DECODE's 1846 year is confirmed
  as a typo. **The cipher is all on the p.2 spread.** The left page has 7 clear lines (continuing p.1), then **9 cipher
  lines** and a catchword "53386" at the foot. The right page has **5 cipher lines** at the top (starting "53386..."),
  then clear German, the closing, the signature and the address to Seebach at St Petersburg.
- Crops: `python3 tools/iiif_lines.py --image <scratch>/IMG_R5007_I28868_P2.jpg --region 1580,2340,2040,1800 --out
  ciphers/zeschau-seebach-1841/images --prefix r5007p2l --debug` gave "region 2040x1800, 9 lines, 9 bands x 1
  segments; pitch 184". The overlay was checked (`images/r5007p2l_lines_debug.jpg`, 1 vision call). The catchword was
  cut with `--region 3330,3960,330,160 --prefix r5007p2lcatch`. The crops were committed before any pass ran (067851fa).
- Two blind Opus passes per half-page (L01-L05, and L06-L09 with the catchword): 4 subagent calls. Pass A read whole
  lines by eye. Pass B cut each line into overlapping thirds at 2x and joined them itself. Neither prompt named the
  other pass's output folder. `tools/reconcile_passes.py passA passB --split-chars`: **agreement 604/610 = 99.0%**
  (err_2reader 1.0%), with 6 disagreements, settled on 2x and 4x zooms (2 vision calls). The settled readings:
  - L01 col 2: `5` (flat top), M, alt 3.
  - L03 col 13: A's `2` (three signs between 77 and 1 at 4x), M.
  - L05 col 22: A's extra `1` dropped; it is the tick after the 8, not a digit. M.
  - L06 col 58: A's `3` dropped (`7778566283` is clear).
  - L08 col 28: `4` (an r-shaped 4), M, alt 7.
  - L08 col 54: B's extra `4`, M.

  err_true is not measurable: BENCHMARK-TX.tsv has no item for this hand.
- Result: **603 digits** in the body (lines 64/69/68/68/64/63/67/69/71), H 572 / M 31, in
  `transcription/r5007p2l_ciphertext.txt` and `.tsv` (same columns as R5006). The catchword is the `r5007p2l_catch`
  row in the tsv and is not counted. Raw passes, agreement and disagreements are in `transcription/passes/r5007p2l_*`.
  The total is odd. If the cipher runs in pairs, a pair crosses to the right page, which the catchword supports: the
  page break falls inside the stream. This is not checked, and no pairing is committed.
- Pencil: no letters. Pass A logged nothing. Pass B logged faint ticks and strokes on L02-L05 and L07-L08 (130 digits
  under a span), including "letter-like R/B shapes" below L04 pos 44-52 at M. Graded M at most, and unread.
- No reading and no crib test.

Requests: de-crypt.org 1 login + 1 RecordsView + 2 thumbnails + 2 full-size = about 6, 2 s apart (plus 1 failed
navigation before the cert fix). No other host. Vision: 5 by this session (2 overviews, overlay, 2 reconcile zooms),
4 subagent passes.

## GAPS196-zeschau-seebach-1841 (3 Oct 2026, account-4)

Step run: the Verdict line's "transcribe R5007's right cipher page (5 lines) as GAPS190, then rerun `crib_test.py` on
the whole of R5007". Both done. No reading.

- Image: the GAPS190 scan was not in this container, so one DECODE browser login (`tools/decode_browser_login.js 5007
  <scratch> --guess-fullsize --delay 2000`, after the playbook's `certutil` line). `IMG_R5007_I28868_P2.jpg` sha1
  c081766ef775 matches GAPS190. The scan stays in the scratchpad, out of git.
- Crops: `python3 tools/iiif_lines.py --image <scratch>/IMG_R5007_I28868_P2.jpg --region 3800,1320,2120,940 --out
  ciphers/zeschau-seebach-1841/images --prefix r5007p2r --debug` gave "region 2120x940, 5 lines, 5 bands x 1 segments;
  pitch 186". Placed from a 25% overview (1 vision call) and checked on the overlay `images/r5007p2r_lines_debug.jpg`
  (1 vision call). The crops were committed before any pass (856ff5a2).
- Two blind Opus subagent passes over the 5 crops (2 calls). Pass A read whole lines by eye. Pass B cut thirds at 2x
  and joined them. `tools/reconcile_passes.py passA passB --split-chars`: **agreement 344/348 = 98.9%**, with 4
  disagreements settled on one 2.5x zoom montage (1 vision call):
  - L03 col 14: A's `3` (8-3-5), M.
  - L03 col 38: `0`, M, alt 6 (a short-ticked oval, not this hand's tall-stemmed 6).
  - L04 col 46: `3`, M, alt 8 (a small squeezed sign).
  - L04 col 61: B's `4`, M, alt 2 (9-4-2-4-8).
- Result: **348 digits** (lines 70/68/72/73/65), H 337 / M 11, in `transcription/r5007p2r_ciphertext.txt` and `.tsv`.
  Raw passes, agreement and disagreements are in `transcription/passes/r5007p2r_*`. L01 opens `53386`, matching the
  left page's catchword. The trailing comma on L05 and the blots are not digits. No pencil marks were seen by either
  pass. err_true is not measurable (no BENCHMARK-TX item for this hand).
- **R5007 cipher body complete: 951 digits** (603 left + 348 right), odd. It is not checked whether a pair crosses the
  page break.

**Crib test on R5007** (pre-registered in `PREREG-GAPS196.md`, commit af121715, before the right page was transcribed
and before any statistic). Same statistics as GAPS185. `crib_test.py --target r5007` (seed 196) writes
`crib_test_r5007.json`; `--check` exits 0 for both targets, and the R5006 default output is unchanged.

| statistic | R5007 target (951 digits) | shuffled-digit control (2,000 draws) | p | verdict (prereg) |
|---|---|---|---|---|
| T1 cosine of the pair profile to R5005 | **0.838** | mean 0.752, p95 0.789 | **0.0005** (the floor) | PASS |
| T2 share of pairs that are one of the 7 pins | 0.082 (39 of 475) | mean 0.075, p95 0.097 | 0.311 | not significant |
| T3 Spearman, pin counts R5007 vs R5005 | 0.667 | -- | -- | reported, no gate |

- Phase 0 (higher pair IC), 475 pairs, pair IC 0.0142 (R5005 0.0142).
- Power at N=951: 200 R5005 windows, **200/200 reach p < 0.01** (window cosine mean 0.900, their null mean 0.794).
- Descriptive only: T1 against R5006 is 0.775 (shuffled mean 0.700). None of Bourdeau's four long R5005 repeats occurs
  in R5007.
- Pin counts in R5007: 11 (la) 7, 70 (pre) 2, 82 (m) 10, 34 (i) 5, 29 (er) 7, 40 (e) 1, 46 (que) 7. That is 39
  tokens at most M (pins are grade I, Bourdeau's values), 0 H / 0 C / 0 S.

What this licenses: R5007, like R5006, shares R5005's pair profile beyond its digit frequencies, so it is consistent
with the same two-digit syllabary, and the pools R5005+R5006+R5007 can be merged for a key rebuild. It does not show
that the 7 values are right, and no token is read. A single global phase is wrong wherever an odd-length line shifts
the pairing, so the test is conservative. The 7 values are Bourdeau's recovery (dbourdeau/cyphersolver, CC BY 4.0);
transcribing R5006-R5008 is his own stated next step too. Rule 10: no novelty claim.

Requests: de-crypt.org 1 login + 1 RecordsView + 2 thumbnails + 2 full-size = about 6, 2 s apart (plus 1 failed
navigation before the cert fix). No other host. Vision: 3 by this session (overview, overlay, reconcile montage),
plus 2 Opus subagent passes.

## Remaining gaps (GAPS179, refreshed GAPS185, GAPS190, GAPS196, 3 Oct 2026)
Read so far: 1,643 digits transcribed (R5006 whole, 692; R5007 whole cipher body, 951 = 603 left + 348 right, GAPS190/196) of about 2,500-3,000 on R5006-R5008; R5007 p.1 holds no cipher (GAPS190); 0 tokens read
- R5008 p.1-2 transcription - blocker: not-attempted; scans reachable through DECODE (GAPS173/175/179/190/196); next: check each R5008 page for cipher on an overview first (R5007 p.1 had none), then one cipher page per worker as GAPS190/196 (1 login, iiif_lines crops, 2 blind Opus passes per half-page + 1 reconcile), ~$4-6 a page, about $10 for R5008
- Key rebuild on the pooled pairs - blocker: not-attempted; crib test done on R5006 (GAPS185, T1 0.886 vs control mean 0.760, p 0.0005) and on R5007 (GAPS196, T1 0.838 vs control mean 0.752, p95 0.789, p 0.0005, power 200/200 at N=951; pin coverage n.s. both times); next: a syllabary annealer seeded with Bourdeau's 7 pins on R5005+R5006+R5007 (5,612 digits: 3,969 + 692 + 951) with its matched synthetic-syllabary control at the same N and design, ~$3; rerun `crib_test.py` on R5008 once transcribed
- Erased pencil decipherment on R5006 - blocker: illegible; p.1 and p.2 passes saw only ticks, no letters, at native resolution; multispectral/UV imaging is an archive step (SEND-QUEUE S5 / ASKS 64)

## Escalation (3 Oct 2026, refreshed GAPS179)
- [ ] siblings: R5005 is on disk (Bourdeau), R5006 done (GAPS175/179), R5007 whole cipher body done (GAPS190 left, GAPS196 right, 951 digits); R5008 still to transcribe, one page per worker
- [n/a] clear-pages: only the letters' own clear passages are in clear text; no clear copy of the cipher body is known
- [x] known-keys: Bourdeau's 7 gloss values from R5005 are the only key material found (bZES, 26 Sept 2026)
- [x] print: no printed edition of this correspondence found (bZES OpenAlex/S2, 0 hits)
- [ ] key-rebuild: R5006 and R5007 both share R5005's pair profile (GAPS185, GAPS196, p 0.0005 each), so the pools can be merged; next a seeded syllabary annealer on R5005+R5006+R5007 with a matched control, then R5008
- [x] image-check: R5006 p.1 and p.2 pencil traces checked at native resolution by two passes plus the reconciler, ticks only (GAPS175, GAPS179)
- [ ] retry: none yet
Verdict: keep going: 2 internal gaps (R5007 fully transcribed by GAPS190/196, 951 digits, two-pass agreement 99.0%/98.9%; crib test on R5007 by GAPS196, same pair profile as R5005, p 0.0005, power 200/200); duplicate-effort risk with Bourdeau's stated next step (see Check-solved verdict and GAPS185); cheapest next: seeded syllabary annealer on R5005+R5006+R5007 with its matched synthetic control, ~$3, or transcribe R5008 (overview first), ~$10

## Check-solved verdict (CHECK-ZESCHAU, account-4, 3 Oct 2026)

Verdict: **not found solved; `partial`** (no decipherment, key or plaintext of R5005-R5008 located in any of the six
source families; Bourdeau's 7 grade-I values and our R5006 transcription are the only progress). Sources, all checked
17:47-18:05 UTC 3 Oct 2026 by this worker:

1. **Web** (search engine, 9 queries, see Web and blog check below): only hit about the cipher is Bourdeau's own site
   (dbourdeau.github.io/cyphersolver), which calls it undeciphered.
2. **Print** (sender's/recipient's papers): no edition of Zeschau's or Seebach's diplomatic correspondence exists that
   any search reached. IA be-api fts, 4 queries (`"Zeschau" "Seebach" chiffre` 226 hits, `"Zeschau" "Seebach"
   Petersburg 1842` 530, `"Albin Leo von Seebach"` 33, `"Seebach" "Zeschau" Depesche` 181; top 8 of each read): hits are
   Hof- und Staatshandbücher, Almanach de Gotha, newspapers, Vehse's *Geschichte der Höfe des Hauses Sachsen*
   (geschichtederde60/63vehsgoog -- its "Chiffre" hits concern 18th-century Prussian ciphers, not these letters) and
   Wagner literature (Seebach in Paris 1859). None prints the 1841-43 dispatches. Google Books API (`country=US`, keyed),
   3 queries (`"Zeschau" "Seebach" chiffre`; `"Zeschau" "Seebach" 1842 Petersburg Gesandtschaft`; `"Seebach" "Zeschau"
   dépêche 1841`): 0 results each. OpenAlex/S2: 0 each (bZES, 26 Sept, not repeated).
3. **Holding archive catalogue**: archiv.sachsen.de record guid fb8ee3d8-3829-4665-8b8f-45c2574196d7, read this pass
   (HTTP 200): "Sächsisches Staatsarchiv, 10731 Sächsische Gesandtschaft für Russland, St. Petersburg, Nr. 12",
   "Ministerialdepeschen", Datierung 1841 - 1849, Benutzung im Hauptstaatsarchiv Dresden; "Enthält u. a." lists subjects
   (Zollangelegenheiten ... Auslieferung von Michael Bakunin) with no mention of Chiffre, Schlüssel or decipherment;
   availability flag in the page data: `digitalisatExists: false`. Not digitised by the archive; DECODE's scans are
   the only images.
4. **DECODE** record notes (cached RecordsList, `sources/decode/records-non-decrypted-2026-09-24.tsv`, and Aymeloglu's
   mirror): all four "Partially decrypted", note "interlinear decrypted, but unfortunately rubbed out"; R5007's title
   mistypes 13.06.1846 (letter dated 1842). No key or decipherment document attached.
5. **Bourdeau** (`github.com/dbourdeau/cyphersolver`, fresh shallow clone, HEAD a439937, 3 Oct 2026 01:07 -05:00):
   `targets/zeschau1841/NOTES.md` line 3 verbatim: "Status: attempted, open. The system is identified and a few code
   values are recovered from the erased decipherment, but the letters are not read." CATALOGUE.md #53: "No key on
   DECODE; ciphertext-only solvers failed." Only `ct_R5005.*` ciphertext files; no R5006-R5008 transcription.
   **Duplicate-effort risk** (brief's "stated next step" rule): his "What would move it" item 3 reads "Transcribe
   R5006–R5008. The German letters use the same code; the cipher in R5008 sits inside a known sentence frame, and
   R5006's cipher follows a clear acknowledgement of Seebach's reports." His target table already describes the
   R5006-R5008 layouts (8 + 3 cipher lines on R5006, about 10 on R5007, 5 on R5008), so he has viewed the images.
   This target is his own stated next step with the material in his hands; the parent weighs that before further spend.
6. **Aymeloglu** (`github.com/aaymeloglu/unsolved-ciphers`, fresh shallow clone, HEAD d2800bb, 27 Sept 2026): only
   `catalogue/decode-records.jsonl` and `decode-catalog.csv` rows 5005-5008 (DECODE metadata, "Partially decrypted").
   No working files.

Who did not know: nobody is shown to have read it; DECODE's own "interlinear decrypted" note means the 1840s recipient
did, and that pencil is now largely rubbed out. Nothing to hand on. Not a novelty statement (rule 10).

## Web and blog check (CHECK-ZESCHAU, 3 Oct 2026)

Search engine, 9 queries, every hit title read:
- `Zeschau Seebach 1841 cipher` -> Bourdeau index (undeciphered, posted 21 Sept 2026), Wikipedia/Zeno biography pages. No solution.
- `"Sächsische Gesandtschaft in Russland" Chiffre Zeschau Seebach` -> de.wikipedia "Liste der sächsischen Gesandten in Russland" (Seebach 1839-1852), archiv.sachsen.de Beständeübersicht, Deutsche Biographie (Zeschau). No cipher content.
- `"10731" "Gesandtschaft in Russland" Nr. 12 chiffre` (shelfmark + cipher) -> archiv.sachsen.de Beständeübersicht pages only.
- `Zeschau Seebach Chiffre Dresden St. Petersburg 1842 entziffert` -> Zeschau family Wikipedia pages, Bourdeau index. None.
- `"J'accuse la réception de Vos rapports" Zeschau 1842` (the most distinctive clear-text phrase, R5006 l.1) -> only Zola's *J'Accuse* pages and one 1842 Preußische Staats-Zeitung OCR page without the phrase. No hit.
- `Zeschau Seebach cipher solved Claude OR GPT` (model-solve announcements) -> Bourdeau index; Vals AI / Cyphral Distich (Urquhart 1653) coverage; LiveScience "AI decodes 217-year-old secret letter ordered by Napoleon" (a different item, a Napoleonic general's letter). None concerns this cipher.
- Cipherbrain: `site:scienceblogs.de/klausis-krypto-kolumne Zeschau OR Seebach OR "sächsische Gesandtschaft"` -> 10 posts, none about this item (the one Saxon mention is a 1786 Munich legation secretary in the Bernotat PDF).
- Cryptiana blog: `site:cryptiana.blogspot.com Saxony OR Saxon OR Zeschau OR Seebach cipher` -> Richelieu 1641, Henry IV 1590, Catherine of Aragon posts; none about this item.
- Cipher Mysteries: `site:ciphermysteries.com Zeschau OR Seebach OR Saxon 1841` -> two unrelated posts (Middle Ages codes, Schmeh interview).
No post about this item was found on any of the three blogs, so there was no comment thread to open. Searches are a log, not a novelty finding.

## Premise check (CHECK-ZESCHAU, 3 Oct 2026)

(a) Folder's own mentions -- **found, partial only**: DECODE's "interlinear decrypted, but unfortunately rubbed out"
for all four records. R5005: Bourdeau's 7 values from the rubbed pencil (grade I, already in Established). R5006 p.1-2:
looked at native resolution by two passes plus the reconciler (GAPS175, GAPS179): ticks only, no letters. R5007 and
R5008: pencil **not yet looked at** -- their transcription workers must mark it (the "Next step" already says so). No
clear copy or "Dechiffrement" sheet is mentioned anywhere in the folder.
(b) Other solvers' working files -- **not found**: Bourdeau's `syll*.py`, `hsolve.py`, `gl.py`, `enh*.py` run on
`ct_R5005` only (no R5006-R5008 ciphertext in his repo, HEAD a439937); Aymeloglu has metadata only. No borrowed key has
been run on R5006-R5008 by anyone.
(c) Physical neighbours -- **partly viewed, rest unreachable**: R5006 p.2 (the cipher's own spread, facing page
included) viewed by GAPS179: clear French, signature and address, no decipherment. Nr. 12 runs 1841-1849
(Ministerialdepeschen); the leaves around each cipher letter are not on DECODE and the file is not digitised
(`digitalisatExists: false`). Unreachable without HStAD (SEND-QUEUE S5 / ASKS 64).
(d) Recipient's side -- **not found / unreachable**: 10731 is itself the recipient's (St Petersburg legation's) file,
so the rubbed interlinear is the recipient-side decipherment. The other direction (Seebach's reports and their Dresden
decipherments, in the foreign ministry's holdings) is not digitised as far as this pass found and was not searched by
shelfmark. No printed Saxon or Russian documentary series for 1841-43 prints these dispatches (print search above).
No find in (a)-(d) makes the item calibration or found-solved.
