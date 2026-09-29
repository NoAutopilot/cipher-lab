open
Schmeh's Cipherbrain FAQ (15 Aug 2016) and Top 50 post 3 (6 Jan 2020) read in full by this worker
(both call the four cryptograms unsolved), Cipher Mysteries' "Thoughts on the Debosnys Ciphers"
(7 Nov 2015, 90 comments) read in full, and a full-text search of Bauer's *Unsolved!* and
Farnsworth's *Adirondack Enigma* via Google Books and Internet Archive (be-api full-text search)
-- see "Check-solved sweep" below for the complete six/seven-source log.

## Check-solved sweep (GOLD-0D, 25 Sept 2026, session_01PjWaPzZTSmZbX6DitArcwb)

Brief: `.claude/briefs/runs/2026-09-25-lane-gold-intake-debosnys.md`. This section is check-solved
(CLAUDE.md Pipeline item 2 / the check-solved skill); LANE B2's cheap-test-1 pass (image fetch +
sign inventory, commit f7c7460) is check-solved's replacement for this line only -- its full
section is kept intact below, unchanged.

1. **Farnsworth, *The Adirondack Enigma* (2010) and Bauer, *Unsolved!* (2017/2019).** Neither is
   full-view on Google Books (`filter=full` returns 0 items for "Debosnys"); read via Google
   Books' snippet/index search instead (`&country=US&key=$GOOGLE_BOOKS_KEY`, queries "Debosnys
   cipher", "Debosnys" + solved/decipher/solution, 25 Sept 2026): Bauer's own back-of-book index
   snippet reads "Debosnys, Henry, 195-217; ciphers of, 196-199" (a chapter, consistent with the
   book's title, *Unsolved!*), no "solved"/"solution" snippet anywhere near "Debosnys". Internet
   Archive full-text search (`be-api.us.archive.org/fts/v1/search?q=Debosnys%20cipher`, 25 Sept
   2026) surfaces Bauer's book (`unsolvedhistorym0000baue`/`unsolvedhistorym0000crai`, both
   lending-only/print-disabled, not borrowed this pass) with hits only on generic cipher-teaching
   passages elsewhere in the book, not a Debosnys solution, plus a third hit, the *Norwich Morning
   Bulletin* 27 Apr 1883 (`norwichmorningbu00bull_15`), 1883 execution-week reportage ("At
   Debosnys' request his beard was taken off yesterday"), not a cipher solution. Neither book's
   own text was read page-by-page (no full-view/loan this pass) -- this is a search result on
   both, not a confirmed page-by-page negative; a museum-holdings key (row below) or a JSTOR/local
   read of either book would still be worth doing before deep work banks on "no key printed
   anywhere in print".
2. **Schmeh's post 3 (saved copy, `sources/schmeh/posts/03-debosnys.txt`) and its comment thread**
   (2 comments in the saved copy, neither a solve claim). Fresh fetches (25 Sept 2026,
   scienceblogs.de, browser UA, >=2s apart): the tag page `.../tag/henry-debosnys/` (all 8 posts
   2015-2021, none titled or dated as a solve; latest is "Henry Debosnys war ein Abschreiber", 29
   Oct 2021, about a plagiarised clear-text poem, not the cipher), the FAQ post (15 Aug 2016, "the
   cryptograms... are still unsolved to date... chances to solve them are good"), and the
   `category/solved-cryptograms/` listing (Debosnys does not appear in it). No later Cipherbrain
   post on Debosnys than 29 Oct 2021.
3. **Cipher Mysteries** (ciphermysteries.com, 25 Sept 2026, its own search, 2 pages): all Debosnys
   posts are 2015 (cipher analysis) or 2021 (an unrelated identity/DNA thread, "was Debosnys in
   fact Pierre Keff?"); the main analysis post, "Thoughts on the Debosnys Ciphers..." (7 Nov 2015),
   read in full with its 90 comments -- states "nobody has so far decrypted so much as a word of
   any of these" and links a fuller scan set at cipherfoundation.org/older-ciphers/debosnys-ciphers/
   (not fetched this pass, not a source named in this brief; flagged as a lead below). Comments
   include unverified partial guesses (one reader: the "L.M.F." page's last word "deciphers to
   ULTIME") with no stated method and no reproducing key -- a documented attempt per CLAUDE.md's
   guidance, not a solution.
4. **DECODE** (de-crypt.org): no fresh crawl this pass -- `sources/decode/records-decrypted-
   2026-09-24.tsv` and `records-non-decrypted-2026-09-24.tsv` (24 Sept 2026, 1361+1187 rows, a
   full non-decrypted+decrypted crawl one day old) grepped for Debosnys/Adirondack/Elizabethtown/
   Essex/New York/America: zero rows -- DECODE's catalogue is exclusively European chancery/
   diplomatic material and holds nothing on this US target either way.
5. **Both solver repositories' snapshots in `sources/solver-diffs/`**: grepped every file
   (`grep -ril debosnys`), zero hits. (Per this brief, the cached snapshots were checked, not a
   fresh clone of dbourdeau/cyphersolver or aaymeloglu/unsolved-ciphers.)
6. **Open indexes**: OpenAlex (`Authorization: Bearer $OPENALEX_KEY`, "Debosnys cipher") 0 results;
   Semantic Scholar (`x-api-key: $S2_KEY`, same query) returned 42012 generic "cipher" results with
   no actual "Debosnys" match (the term is too rare to filter the API's OR-ranked search) -- read
   as no relevant hit, not a true zero; CrossRef (`api.crossref.org/works?query=Debosnys+cipher`)
   7531 generic cipher-engineering results, same read. No scholarship on this specific target
   found by any of the three.
7. **Search engine, incl. the model-solve family and forums/Reddit** (WebSearch, 25 Sept 2026):
   "Debosnys cipher solved", "Debosnys cryptogram decoded", "Debosnys cipher Claude GPT solved",
   "Debosnys cipher reddit", "Debosnys cipher zodiackillersite forum" -- every result is 2015-2023
   commentary (Cipher Mysteries, Cipherbrain, Dark Histories podcast, Crime Capsule, Quora, the
   Sektu blog) stating the cryptograms remain unsolved; no AI-lab or evaluation-company solve
   announcement, no Reddit/forum solve claim, no evidence either GPT or Claude has been reported
   solving it. Wikipedia's "Henry Debosnys" article (25 Sept 2026) still carries the category
   "Undeciphered historical codes and ciphers" (consistent with the spec's 24 Sept 2026 check of
   "List of ciphertexts").
8. **New lead found this pass, not run (one line per Usage rule 7):** the Sektu blog
   (sektu.blogspot.com, author "Brian") has an 18-post "Debosnys" label series from Jun-Aug 2017 --
   real cryptanalytic groundwork on cryptogram #4 (the poem), including a French-alexandrine/
   nasalization-subglyph frequency test against Beaudelaire's *Fleurs du Mal* ("this looks like a
   promising match, but more work needs to be done") -- read in full for a solve claim (none
   found; its latest post, "Another note on N-Glyphs", 7 Aug 2017, is still hypothesis-testing) but
   not otherwise used; worth reading in full before any homophonic/MASC anneal on cryptogram #4
   (spec cheap test 3), since it may already rule out or narrow the alphabet-family hypothesis.
   Checked the blog's own 2023 and Jan 2026 posts too (its most recent activity) -- both are on
   unrelated topics (Toyfl; a Meroitic-inscription mystery), no further Debosnys content since
   Aug 2017.

**Verdict: open.** No solution, key, or documented full decipherment found for any of the four
Debosnys cryptograms in any of the eight source families above. Rule 10: this is a search result,
not a novelty claim -- a verifier session would still need to run before any "not published
anywhere" wording.

`python3 tools/intake_gate_check.py debosnys-1883`:
```
debosnys-1883: open (line 1) -- edition/page or full-text-search citation found within 6 lines
```

## What this pass did (25 Sept 2026, LANE B2 worker bDEB, session_01Uktvb4t31yu7ECakLwuugc)

Brief: `.claude/briefs/runs/2026-09-25-lane-b2-debosnys-1883.md`, re-scoped 25 Sept 2026 16:33 UTC
(no subagent, no second pass -- test 1 only, cap $3/30 min). Carried over from LANE B's unrun
24 Sept 2026 brief.

1. **Images.** Fetched from `sources/schmeh/posts/03-debosnys.html` (Cipherbrain / scienceblogs.de,
   Schmeh, 6 Jan 2020) into `images/`, manifest at `images/manifest.json`. The post's four
   cryptograms: #1 is one page, #2 is two pages (2a, 2b), #3 is one page, #4 is two pages (4a,
   4b) -- six image files for four cryptograms. The brief capped requests to this host at 4, so
   **cryptogram #4 (4a, 4b) was not fetched this pass** -- next fetch for a future worker.
   Requests: scienceblogs.de 4 (Cryptogram-1.png, 2a.png, 2b.png, 3.png), all HTTP 200, no
   429/403, spaced >=1.8s apart, browser UA (Chrome/120 string).

2. **Sign inventory.** `tools/glyph_atlas.py segment` (with `--debug`, checked each overlay
   before trusting it) on a hand-picked crop of each page's cipher-only region (excluding the
   pencil portraits/drawings and, for #1 and #3, the clear-text signature/poem below the
   cipher -- see "plain text on the page" below), then one `cluster` (k=90 signs, k-marks=20,
   the tool's deliberate over-split) and `atlas` run across all four pages together so the same
   cluster id means the same shape everywhere. `pip install numpy scikit-image scikit-learn
   pillow opencv-python-headless` was needed (installed clean, no other issues).
   Scripts: `scripts/compute_ic.py` (IC + controls), `scripts/build_ciphertext.py` (renders
   `ciphertext.txt` from the segmentation).

   | cryptogram | lines | N (signs) | K (distinct clusters used, of 90 global) |
   |---|---|---|---|
   | #1 | 6 | 136 | 70 |
   | #2 (2a+2b) | 17+9=26 | 549+229=778 | 88 |
   | #3 | 4 | 118 | 64 |
   | #4 | -- | not fetched | -- |
   | combined (1,2,3) | 36 | 1032 | 90 (all clusters used somewhere) |

   Line counts match Schmeh's text: #1 "six line text" (confirmed), #3 "the shortest of the
   four" (confirmed shortest N and fewest lines of the three fetched).

3. **IC**, `scripts/compute_ic.py` (fr16 and en16_repo corpora on disk, 20 trials each, matched
   N; uniform-random control at matched N and K, 20 trials, same script):

   | group | N | K | IC target | IC French (fr16) | IC English (en16_repo) | IC uniform-random |
   |---|---|---|---|---|---|---|
   | #1 | 136 | 70 | 0.0129 | 0.0695 | 0.0916 | 0.0144 |
   | #2 (2a+2b) | 778 | 90 | 0.0121 | 0.0695 | 0.0991 | 0.0111 |
   | #3 | 118 | 64 | 0.0135 | 0.0693 | 0.0914 | 0.0157 |
   | combined | 1032 | 90 | 0.0125 | 0.0696 | 0.0984 | 0.0111 |

   The target's IC sits far below both natural-language controls (French ~0.070, this en16
   corpus ~0.09-0.10) and close to (indistinguishable from, given the trial spread) the
   matched uniform-random control at the same N and K. Read cautiously (next paragraph), this
   is consistent with the spec's own hypothesis ("considering the large alphabet, it seems
   unlikely that the cipher used is a simple substitution [MASC]... perhaps homophonic or a
   code") rather than ruling anything in or out on its own.

   **Caveat (rule 2, single pass):** K and the IC numbers are conditional on one
   machine-segmented, machine-clustered pass with a deliberately over-split k=90 (the tool's
   documented default behaviour, not tuned per page). Over-splitting fragments true repeats of
   the same sign across multiple clusters, which mechanically pulls IC down and could by
   itself explain most of the gap to the random control -- this pass cannot distinguish "the
   cipher alphabet really is this flat" from "the clustering split real repeats apart." A
   second pass (test 2, not run here) and/or hand-merging the 90 clusters against the atlas
   contact sheets (`glyphs/sheet_signs_0{0-4}.png`) would be needed before treating the IC
   comparison as informative either way.

4. **Plain-letter/digit text on the page (yes, on three of the four fetched images):**
   - Cryptogram #1: the signature "**H.D. Debosnys**" in clear script directly below the six
     cipher lines (excluded from the sign inventory above).
   - Cryptogram #2: "**H.D.D.L.M.F.**" in clear capitals mid-page-a (line 9 area), the digits
     "**516**" in clear on page a, page number "**No. 9**" clear at the top of page a, and
     "**L.M.F.**" in clear again at the bottom of page b next to a drawing of a hand holding a
     scroll. (All excluded from the sign inventory; the "6"/"5" on a drawn cube near the top of
     page a were also left out as part of that drawing, not counted as cipher signs.)
   - Cryptogram #3: page number "**No. 10**" in clear at the top, and, more importantly, a
     complete **French poem in clear cursive script fills the lower two-thirds of the same
     page**, directly below the four cipher lines ("Oh! mes amis je vous supplie en grace / de
     bien vouloir un instant m'ecoute / ..."), ending "...(next page la suite)". This is the
     spec's own suggested crib/host-text relationship (`constraints.host_text`: "his clear
     poems from the same jail papers are the natural crib and form source") turning up
     directly on the cryptogram page itself, not just among his other papers. **Not analysed
     here** -- comparing the cryptogram's line/syllable structure to this poem, or any of his
     other clear verse, is the spec's cheap test 2, which this brief explicitly does not run.
   - Cryptogram #1 and #3 both carry a faint pencil portrait bleeding through from the other
     side of the sheet; these were cropped out of the sign-inventory region but are visible in
     the debug overlays and contributed a handful of small spurious "sign" boxes on #2b in
     particular (mustache/eye shading treated as short strokes) -- a source of noise in the
     N/K counts above, not corrected in this single pass.

5. **Design note (context, not yet used for anything).** The Schmeh post itself states no
   transcription of these cryptograms is known to exist ("People have asked me if there is a
   transcryption, but I'm not aware of one") as of Jan 2020 -- noted here only as what the
   source page says about itself, not a novelty claim (rule 10) and not checked against the
   solver repositories or any other source by this worker (that is check-solved's job, not run
   on this target -- see the intake-gate note at the top of this file). The alphabet mixes
   abstract symbols with drawn pictograms (a horse, sun, birds, a tree, an anchor, a house, a
   ship's wheel, a "W"-shaped dingbat, etc.) used inline as signs, consistent with the spec's
   description of a large, code-like alphabet.

## Files

- `images/` -- 4 PNGs + manifest.json (cryptograms 1, 2a, 2b, 3; 4a/4b not fetched)
- `ciphertext.txt` -- sign codes as segmented, single pass, **draft**, per cryptogram, in reading
  order (`=== Cryptogram N ===` sections); `+Mxx` marks noted inline
- `glyphs/` -- segmentation/clustering working files: `signs.tsv`, `marks.tsv`, `clusters.tsv`,
  `atlas.tsv`, `labels.json` (auto-generated placeholder codes S00-S89/M00-M19, not hand-described),
  `debug_c*.jpg` (segmentation overlays, checked before trusting the counts above),
  `sheet_signs_0{0-4}.png` / `sheet_marks.png` (cluster contact sheets, for a future hand-merge pass)
- `scripts/compute_ic.py`, `scripts/build_ciphertext.py`

## Suggested follow-ups (not run here, one line each per Usage rule 7)

- Fetch cryptogram #4 (4a, 4b; 2 more requests to scienceblogs.de) to complete the set. **Done
  in GOLD-4A, test 1, below.**
- Hand-merge the 90 over-split clusters against the contact sheets to get a real distinct-K
  and a trustworthy IC before treating the homophonic/code hypothesis as supported. **Done in
  GOLD-4A, test 1, below.**
- Spec's cheap test 2 (form/crib test against Debosnys's own clear poems, including the one
  on the #3 page itself) is now unusually promising given the poem sitting right on the same
  sheet as the cipher -- a natural next breadth test.

## GOLD-4A, test 1 completed (25 Sept 2026, session_01AgfLAn9zg6JxzBSoWkR4UY)

Brief: `.claude/briefs/runs/2026-09-25-lane-gold-debosnys-passes.md`. Cap $6 / 60 min. Intake
gate re-checked at brief launch (`debosnys-1883: open (line 1) -- edition/page or full-text-search
citation found within 6 lines`, exit 0, 25 Sept 2026 17:21 UTC) -- unchanged from the
check-solved section above.

**1. Fetched cryptogram #4** (`Debosnys-Cryptogram-4a.png` 1107x1493, `4b.png` 1105x563) from the
same scienceblogs.de URLs as the other three, browser UA, 2 requests >=2s apart, both HTTP 200,
no 429/403. `images/manifest.json` updated; all four cryptograms (six page images) are now on
disk. Host total this pass: scienceblogs.de 2 (6 across the target's whole history).

**2. Merged sign inventory.** Viewed all five `glyphs/sheet_signs_0{0-4}.png` contact sheets
(90 sign clusters) and `glyphs/sheet_marks.png` (20 mark clusters) directly, by eye, and wrote
`glyphs/merge.tsv`: cluster -> merged sign id, one-line shape description, confidence (H/M/L).
Real duplicates the k=90 over-split had fragmented collapse to one id each -- **X** (12 clusters:
4,14,22,25,26,28,47,52,53,56,62,84), **PCT** (percent-like double loop; 3 clusters: 9,57,66),
**BAR-SOLID** (3: 8,10,45), **BAR-THIN** (2: 12,51), **Y-CURL** (2: 19,88), **LOOP-TAIL** (2:
23,89), **WAVE** (3: 27,58,70), **PHI** (2: 34,86), **CROSS-T** (2: 48,68) -- plus 20 more
one-cluster-one-sign named shapes (SUN, ANCHOR-family pictograms folded into SUN's cluster 16,
GEAR-DOT, CIRC-O, CRESCENT, VENUS, VEE, DASH-H, NOTE, TRIPOD, AMP, RHO, EYE-DOT, DELTA-TAIL,
V-DOT, HOOK-L, BAR-SERIF, DASH-V). 90 sign clusters -> **68 merged sign ids**.

Honest limit, not glossed over: 39 of the 90 sign clusters (and most of the 20 mark clusters)
are genuinely heterogeneous "junk-drawer" buckets -- k-means grouped several *different* rare or
complex shapes together because they share aggregate features (stroke count, ink density), not
actual outline. These are left **unmerged**, one cluster = one placeholder id (`MISC-05`,
`MISC-13`, ... `MISC-87`), confidence L, flagged in merge.tsv as "not one shape, needs by-eye
split" rather than guessed into a real sign. `sign 16` (SUN) is a partial exception: the sunburst
pictogram dominates its 14 members but a handful of rare pictograms (anchor, a running figure, a
wheel-like shape) also fell into the same cluster and were not split out -- noted in merge.tsv,
confidence M.

`glyphs/labels_merged.json` is the machine-readable form of merge.tsv (for `glyph_atlas.py
atlas`/`classify`). `glyphs/atlas.tsv` + `glyphs/atlas.png` were regenerated from it as the
labelled reference sheet (68 rows, up to 6 exemplars each) used for Pass B below.

**3. Segmentation on 4a/4b, mapped into the same inventory.** Re-ran `glyph_atlas.py segment`
with the *same* page-crop parameters as the original four pages plus two new boxes picked by
eye from a row/column ink-profile scan of the new images (`c4a@0,425,1107,1493` excludes the
"monographe. verse." title and a decorative monogram, both sitting above y=420, confirmed by a
column-ink scan showing the monogram is at the *same* height as the title, not beside line 1 as
it first looked at display scale; `c4b@0,0,1105,410` excludes the "Hênêcos Debosnostys" clear
signature at the bottom). Segmentation is deterministic: re-running it on c1/c2a/c2b/c3 with
their original boxes reproduced the exact same counts as LANE B2's pass (136/549/229/118),
confirming the re-run didn't disturb the established pages. New: **c4a 214 signs, 49 marks**
(14 lines); **c4b 69 signs, 13 marks** (5 lines); combined cryptogram 4 = 283 signs, 19 lines.
`--debug` overlays (`glyphs/debug_c4a.jpg`, `debug_c4b.jpg`) checked before trusting: segmentation
looks clean except for the same kind of pencil-portrait bleed-through noise B2 flagged on c2b,
here affecting a few boxes around c4a's lines 11-13 (a smudged watermark/portrait area) -- not
corrected this pass.

Mapping the new pages into the established inventory needed `classify` (kNN against the already
merged, labelled c1-c3 boxes), since they were never part of the original k-means clustering. The
tool's own default kNN (`glyph_atlas.py classify`) compares every box, including a target page's
own still-unlabelled boxes, against each other -- for c4a/c4b that meant 33% (70/214) and 45%
(31/69) of boxes voted noise (`_`) simply because their nearest neighbours were *other unlabelled
c4a/c4b boxes*, not real matches in the trained set. A small standalone script (not a change to
`glyph_atlas.py`; reused its own `feats()` via import) excluded same-page candidates from the kNN
vote entirely, dropping the noise rate to **6.5% (14/214) c4a** and **26% (18/69) c4b** -- still
real uncertainty, not zero, and worth fixing properly in `glyph_atlas.py` itself (an
`--exclude-page` option) before the next page is added this way; flagged here rather than done,
given the cap. **Pass A** (`passA.tsv`, 1315 rows, all four cryptograms) = c1/c2a/c2b/c3 boxes
mapped by their *direct* established cluster (via merge.tsv, deterministic, confidence = merge.tsv's
own H/M/L for that sign id); c4a/c4b boxes by the same-page-excluding kNN code (confidence capped
at M even where merge.tsv would say H, since the kNN step adds its own uncertainty layer).

**4. Pass B** (one Sonnet subagent, per the LANE R4 common rule): blind transcription of
cryptogram 4's 19 lines from `glyphs/strips/c4{a,b}_L*.jpg` against the merged atlas reference
sheet only -- never opened `ciphertext.txt`, `passA.tsv`, or `glyphs/classify/`. Wrote
`passB_c4.tsv` (283 rows) to disk page-by-page as instructed. Confidence self-report: H 58 / M
207 / L 18 -- the subagent flagged the same problem merge.tsv already names: "distinguishing
between visually similar MISC-NN buckets... was often a judgment call."

**Reconciliation** (`tools/reconcile_passes.py passA_c4.tsv passB_c4.tsv --crops glyphs/strips`,
Needleman-Wunsch): **agreement 66/294 = 22.4%**, line range 7.7-41.2% (`agreement.tsv`). Far
below the brief's 80% gate for writing `ciphertext.txt` -- **per the brief, `ciphertext.txt` is
left unchanged** (still LANE B2's single-pass draft, cryptograms 1-3 only, raw un-merged S-codes);
the reconciled cryptogram-4 draft is `ciphertext_draft.tsv` (294 draft signs, all graded M) and
the full disagreement list is `disagreements.tsv` (228 columns), both already written by the tool.
Breaking down the 228 disagreement columns: 123 (54%) involve at least one `MISC-*` bucket (the
flagged-unreliable clusters disagreeing exactly where merge.tsv said they would), 32 (14%) involve
the kNN `_` noise code, and **105 (46%) are disagreements between two supposedly-distinct named
codes** (top confusions: BAR-THIN/PCT x5, PCT/Y-CURL x4, BAR-THIN/X x3, DELTA-TAIL/LOOP-TAIL x3,
HOOK-L/X x3) -- meaning even the cleanly-merged shape groups are not yet visually crisp enough
for two independent reads to agree reliably. Read together with the noisy Pass-A method for c4
(kNN, not a real second visual pass), this 22.4% is not a trustworthy measure of "how legible
cryptogram 4's alphabet really is" -- it is a control-free single data point, reported as the
brief requires (a FAIL, reported as a FAIL), not a claim that the alphabet is unreadable.
Cryptograms 1-3 were not re-run through Pass B this test (scope choice under the $6 cap, see
below); their ciphertext.txt draft keeps LANE B2's single-pass caveat.

**5. N / K / IC per cryptogram, merged codes, matched controls** (`scripts/compute_ic.py`'s own
`ic()`/control functions, called from a short script over `passA.tsv`; fr16/en16_repo/uniform-random,
20 trials each; full table in `glyphs/ic_merged.txt`):

| group | N | K (incl. kNN noise) | K (excl.) | IC target | IC French (fr16) | IC English (en16) | IC uniform-random |
|---|---|---|---|---|---|---|---|
| #1 | 136 | 52 | 52 | 0.0359 | 0.0695 | 0.0916 | 0.0192 |
| #2 (2a+2b) | 778 | 68 | 68 | 0.0363 | 0.0695 | 0.0991 | 0.0147 |
| #3 | 118 | 49 | 49 | 0.0343 | 0.0693 | 0.0914 | 0.0204 |
| #4 (4a+4b) | 283 | 49 | 48 | 0.0551 | 0.0704 | 0.0975 | 0.0203 |
| combined (all 4) | 1315 | 69 | 68 | 0.0380 | 0.0698 | 0.1012 | 0.0145 |

lines.tsv has the per-line sign counts feeding GOLD-4B's form test. Compared to B2's raw-cluster
IC (K=90, all four groups statistically indistinguishable from uniform-random), **merging moves
every cryptogram's IC clearly above its matched uniform-random control** (1.7x-2.7x) while
staying far below both natural-language controls -- consistent with the spec's own hypothesis of
a large, flat-frequency homophonic-or-code alphabet, not a plain substitution, and not yet
distinguishable from "genuinely flat code" vs "still-too-coarse a merge, some MISC buckets hiding
real repeats." Cryptogram #4 (the "monographe. verse." poem cryptogram, the one Sektu's 2017 blog
tried against Baudelaire) has a visibly higher IC (0.0551) than 1/2/3 (0.034-0.036) -- worth
carrying into GOLD-4B's form test, not interpreted further here. The kNN `_` noise code (32
occurrences, all in cryptogram 4, none in 1-3) is counted as one of the K bins above; excluding it
drops K(#4) 49->48 and K(combined) 69->68 -- a small effect, noted for completeness rather than
because it changes the picture.

**Word-divider check** (brief step 5): computed self-adjacency and gap statistics for the five
most frequent merged signs across all 1315 tokens. **X is the single most frequent sign overall**
(198/1315 = 15.1%) but is self-adjacent 28 times (14% of its own occurrences) -- ruling it out as
a word divider by the brief's own test (a divider should never sit next to itself). **Y-CURL**
(43 occurrences, 3.3%) is never self-adjacent (0/43) with a fairly even gap (mean 8.8, sd 4.1
positions) -- the one candidate among the top five that fits the divider profile, though its
raw frequency is much lower than X's. PCT (71 occurrences) is self-adjacent 4/71 times with a
noisier gap (mean 9.0, sd 6.7) -- a weaker fit. Reported as an observation for GOLD-4B, not a
claim about what the sign means.

**Scope choices made under the $6/60-min cap, stated plainly:** (a) Pass B and reconciliation
were run for cryptogram 4 only, not re-run for 1-3, since test 1's job was completing the
inventory and the new cryptogram; (b) the 39 heterogeneous MISC clusters were left unsplit
rather than hand-sorted glyph-by-glyph, which is real remaining work before K can be trusted as
a true distinct-sign count; (c) `glyph_atlas.py`'s classify kNN same-page-noise bug was
worked around in a throwaway script, not fixed in the shared tool.

**Grade:** all of this is machine segmentation + one blind Sonnet pass + arithmetic on top --
cryptanalytic result, grade **S** throughout, 0 H, 0 C. No decoding attempted, no claim about
what any cryptogram says. Rule 10: nothing here is a novelty claim.

Files: `images/{Debosnys-Cryptogram-4a,4b}.png` + updated `manifest.json`; `glyphs/merge.tsv`,
`glyphs/labels_merged.json`, updated `glyphs/{signs,marks,atlas}.tsv`/`atlas.png`/`pages.json`/
`bitmaps.npz`, `glyphs/debug_c4{a,b}.jpg`, `glyphs/classify/{c1,c2a,c2b,c3,c4a,c4b,c4a_xpage,
c4b_xpage}.tsv`, `glyphs/strips/*.jpg` (55 line crops, all four cryptograms); `passA.tsv`,
`passA_c4.tsv`, `passB_c4.tsv`, `ciphertext_draft.tsv`, `disagreements.tsv`, `agreement.tsv`;
`lines.tsv`; `glyphs/ic_merged.txt`. `ciphertext.txt` unchanged (80% gate not met for cryptogram
4; cryptograms 1-3 keep their existing single-pass draft).

Requests this pass: scienceblogs.de 2 (step 1 only; everything else was disk/CPU work, no other
host touched). Subagents: 1 (Sonnet, Pass B, blind, per the LANE R4 common-rule cap).

## GOLD-4B, form test (25 Sept 2026, session_011bxY3axv9kyCqNZAxS4M3e)

Brief: `.claude/briefs/runs/2026-09-25-lane-gold-debosnys-form.md`. Spec cheap test 2. No images
newly fetched (used `images/` already on disk); no decoding attempted; grade throughout is **S**
(cryptanalytic/descriptive, arithmetic on the existing transcription), 0 H, 0 C.

**1. Clear poems transcribed** (`clear_poems.tsv`, from the images already on disk, by eye):
- **Cryptogram 3 page**: the 14-line clear French poem filling the lower two-thirds of the page,
  below the 4 cipher lines ("Oh! mes amis je vous supplie en grâce" ... "c'est là, où je veux
  aller pour l'éternité."). Syllable counts (heuristic French-prosody counter,
  `scripts/count_syllables.py` -- vowel-group nuclei, word-final unaccented "e" mute unless it is
  a word's only vowel or the word sits mid-line before a consonant, elisions read off the
  transcription's own apostrophes) range **9-15 syllables/line, mean 11.0**; letters/line range
  24-42, mean 32.8. **Not a regular alexandrine** -- consistent with Sektu's own independent
  finding on the same poem (below), which also reports irregular meter topping out at 14-15
  syllables.
- **Cryptogram 4 page**: no clear poem (the whole page is cipher). Clear text present is only the
  title **"monographe. verse."**, a circular banner reading **"HENRY.D.DEBOSNYS"** (around a
  bird-and-key monogram drawing, appears twice), and the signature **"Hênêcos Debosnostys."** at
  the foot of 4b -- transcribed in `clear_poems.tsv` with syllable/letter columns marked `[?]`
  since these are not verse lines.

**2. Sektu blog** (sektu.blogspot.com, "Debosnys" label, 20 posts, 8 Jun - 7 Aug 2017, author
credited as "Sektu"): full summary with every hypothesis, test, number and post URL/date in
`sektu-2017.md`. Headline items: the alexandrine/one-symbol-per-syllable hypothesis for the
"cipher poem" (cryptogram 4) was **tested and rejected** against a real Baudelaire alexandrine
control (21 Jun 2017); the N-glyph/nasalization test against *Fleurs du Mal* (3182 lines, mean
2.05 nasalized syllables/line) found the cipher poem's N-glyphs (20 lines, mean 1.5/line) "a
promising match, but more work needs to be done" (7 Aug 2017, explicitly not a solve); Sektu's
own corpus-wide transcription (his own segmentation convention, not this repo's) counts 1188 glyph
instances of 425 types, most frequent glyph 89 occurrences (7.5%). **Rule 10: none of this is our
claim** -- credited to Sektu throughout, per rule 8.

**3. Form test** (`scripts/form_test.py`, reads `lines.tsv` and `clear_poems.tsv`):

| group | lines | mean signs/line | vs poem's 14 lines |
|---|---|---|---|
| cryptogram 1 | 6 | 22.67 | line count differs, no per-line pairing possible |
| cryptogram 2 (2a+2b) | 26 | 29.92 | line count differs, no per-line pairing possible |
| cryptogram 3 | 4 | 29.5 | line count differs, no per-line pairing possible |
| cryptogram 4 (4a+4b) | 19 | 14.89 | line count differs (19 vs 14), no per-line pairing possible |
| cryptogram 4a alone | **14** | 15.29 | **line count matches the c3 poem's 14 lines exactly** |

Only cryptogram 4a's line count (14) matches the clear poem's (14), so it is the only pairing a
per-line correlation can test. Pearson r between cryptogram-4a signs/line and the poem's
letters/line = **0.269** (shuffle-control percentile **80.3** of 1000 trials, null range
-0.75..+0.74); against the poem's syllables/line, r = **0.439** (percentile **93.6**, null range
-0.75..+0.79). Neither clears a conventional significance bar (e.g. >=95th/97.5th percentile), and
80th/93rd-percentile correlations of this size are unremarkable at n=14 with a two-sided null this
wide -- **read as a weak, inconclusive shape match, not a crib finding.**
Signs/letter ratio (paired, cryptogram 4a total signs / poem total letters) = 214/459 = **0.466**
signs per poem letter (about 2.1 poem-letters per cipher sign) -- consistent with the spec's
code/homophonic-alphabet hypothesis (a sign standing for more than one letter) rather than 1
sign = 1 letter, but this is arithmetic on an assumed pairing that step "b" below weakens, not
independent support for it.
Letters-per-12-syllable-line estimate, derived from the poem's own letters/syllable ratio
(459 letters / 154 syllables = 2.98 letters/syllable x 12 = **35.8 letters**, since no 19th-c.
French verse-line sample exists in tools/data to draw 500 alexandrine lines from, per the brief):
no cryptogram's mean signs/line (13-30) is close to 35.8, for any cryptogram under any of the
sign=letter or sign=syllable readings.

**Cross-check against Sektu's own numbers weakens the cryptogram-4a/poem line-count match**:
Sektu's 2017 post ("Another note on N-Glyphs") states plainly "of the **20** lines of the cipher
poem" -- his own count of the same object (the two-page cryptogram 4 cipher, not just page 4a) is
20 lines, which is far closer to this repo's combined-cryptogram-4 total (**19** lines, c4a's 14 +
c4b's 5) than to cryptogram 4a's 14 lines alone. Read together, the 14-line coincidence between
cryptogram 4a in isolation and the c3 clear poem looks like an artefact of only counting half of
"the cipher poem" (the object Sektu, working independently in 2017 from different scans, treats as
one 19-20-line unit spanning both pages), not a genuine structural match -- **downgraded from
"candidate" to "not supported once cryptogram 4 is counted as Sektu counts it."**

**Conclusion**: no cryptogram's line count and line-length profile is a convincing match for the
c3 clear poem once cryptogram 4 is counted correctly as one 19-20-line unit; the one candidate
that did line up (cryptogram 4a alone, 14 lines) is better explained as counting only one of
cryptogram 4's two pages. This is a control-backed negative for "the clear c3 poem is a full crib
for a Debosnys cryptogram" among the four cryptograms and pairing tested here, not a claim that no
crib relationship exists (a different clear poem not on these six pages, or the Greek poem Sektu
identifies on the reverse of the cryptogram-4 leaf, remain untested; neither is on disk here).

Files: `clear_poems.tsv`, `sektu-2017.md`, `sources/sektu/` (raw feed JSON + 20 per-post text
extracts, not committed as images), `scripts/count_syllables.py`, `scripts/form_test.py`,
`form_test_result.json`.

Requests this pass: sektu.blogspot.com 2 (see `sektu-2017.md`). No other host touched; no new
images fetched (rule "image over transcription" satisfied from images already on disk).

## GOLD-4C, inventory (25 Sept 2026, session_01DKinsj1fqVdAVyWw5x6Xtf, Fable)

Brief: `.claude/briefs/runs/2026-09-25-lane-gold-debosnys-inventory.md`. Cap $10 / 60 min, started 18:00 UTC.
Intake gate at brief launch: `debosnys-1883: open (line 1) -- edition/page or full-text-search citation found
within 6 lines` (exit 0). No decoding, no annealing; this is inventory design from the crops, one pass, by eye.

**1. Every box now carries a sign id with a confidence** (`glyphs/box_labels.tsv`, 1315 rows: sid, page, line,
pos, sign, family, confidence, source). What was looked at, from labelled contact sheets cut from the grey page
crops (not the binarised bitmaps): all 445 boxes of the 39 `MISC-*` clusters and the 14 of `SUN` (source
`eye-split:<old id>`); all 283 cryptogram-4 boxes, both the 118 the kNN had left as `MISC-*`/`_` and the 165 it
had given a named id (source `eye-check:knn-<old id>`, so the kNN's own uncertainty layer is gone from c4); and
180 boxes of twelve GOLD-4A "named" clusters that the first inventory sheet showed to be mixed themselves --
PHI, LOOP-TAIL, CIRC-TAIL, DELTA-TAIL, TRIPOD, WAVE, BAR-SERIF, EYE-DOT, GEAR-DOT, CRESCENT, RHO, HOOK-L (source
`eye-resplit:<old id>`). The 393 boxes of the fifteen clusters that looked pure on the sheet (X, PCT, Y-CURL,
VENUS, CROSS-T, BAR-SOLID, BAR-THIN, CIRC-O, NOTE, AMP, TRIDENT, VEE, DASH-H, DASH-V, V-DOT) keep their cluster
label (source `cluster-map:<cluster>`), with merge.tsv's confidence. `glyphs/merge.tsv` rows for every split
cluster now read `PER-BOX` with the split's contents in the desc; `glyphs/labels_box.json` is labels_merged.json
plus a per-box `override` block, so `glyph_atlas.py classify --labels glyphs/labels_box.json --exclude-page`
votes with the corrected labels. `glyphs/inventory.png` / `inventory.tsv`: one row per sign id, count, pages,
H/M/L counts, up to eight exemplars spread across pages.

**K after the split: 160 sign ids** (162 rows counting the two non-sign classes `_` noise and `MULTI`, a box the
segmenter cut across several signs), against 68 before; **158 families** after folding the two variant pairs
that the sheet shows are one shape written two ways (PCT-SLASH, a % with dots instead of loops, into PCT;
BAR-SOLID, which is the same ink blob as BLOB, into BLOB). Confidence over the 1315 boxes: **H 481 (36.6%),
M 638 (48.5%), L 196 (14.9%)**. 73 ids have fewer than three exemplars (50 seen once), and inventory.tsv says
so per row: they are the twenty pictograms (horse, eagle, leaf, bird, anchor, house, tree, runner, face, jug,
barrel, bottle, arrow, crown, fish, heart, glass, figure, "crossed", "D"; 42 boxes in all), eight plain-letter
shapes (A, D, F, H, L, M, N, T), and one-off composites. That long tail is a property of the pages, not of the
split: Debosnys draws a great many things once.

What the split found that GOLD-4A's cluster view could not: a large part of the alphabet is **composite**, a
base sign with a stack of strokes above or below it that the segmenter (rightly, they touch or overlap) kept
in one box -- tilde over o / ox / xx / oo / dots, two dashes over o, dashes over ıı, cc over dashes, arch over
dashes or over o, a bar between an arch or a cc and an x, ıı over a bar over o. 36 such composite ids cover
267 boxes (20% of all signs). Whether the stacked strokes are part of the sign, or the "marks" of the marks.tsv
layer written large, is the design question the next pass should keep open; here they are signs, named by their
parts (O-TILDE, OX-TILDE, O-DASH2, II-DASH, CC-DASH, ARCH-DASH, C-BAR-X, II-O, ...), so a later merge is a
lookup, not a re-read. Also found: GOLD-4A's PHI cluster was mostly loops with a *diagonal* stroke, which is the
same Ø shape that filled LOOP-TAIL and part of MISC-78/-37/-54 (now one id, O-SLASH, 27 boxes, plus PHI proper
19); DELTA-TAIL was mostly a cross over a loop (DAGGER-O, 18); HOOK-L was two shapes, a comma (HOOK-L, 3) and
pairs of slanted strokes / nested chevrons (DBL-SLASH 14, CHEVRON2 10); CIRC-TAIL was a junk drawer (X, comma,
o, blobs, faint marks); RHO is a loop on a stem like a magnifier (LOOP-STEM, 9).

**2. `tools/glyph_atlas.py classify --exclude-page`** (commit b08f48f): the target page's own boxes never vote;
help line and docstring updated; `tools/tests/test_glyph_atlas.py` gains a case that classifies a wholly
unlabelled second page from the first page's per-box overrides and a case that a page with nothing else to vote
with fails loudly. Test passes (`ok`). This replaces GOLD-4A's standalone workaround.

**3. Cryptogram 4's 228 disagreement columns, settled on the image with the new inventory**
(`disagreements_classes.tsv`, one row per column of GOLD-4A's reconciled draft, kept as
`glyphs/c4_draft_gold4a.tsv`; `scripts/gold4c_inventory.py` derives the classes mechanically from box_labels.tsv):

| class | columns | share | what it means |
|---|---|---|---|
| inventory confusion | 174 | 76% | 128 where one pass used a `MISC-*` bucket or the kNN `_` class (one id for several shapes); 46 where the shape read on the image had no id at all in the 68-id inventory, so both passes reached for different impure ids (e.g. PHI vs LOOP-TAIL for an Ø, TRIPOD vs PCT for a %) |
| segmentation | 34 | 15% | 22 columns where one pass has a box the other lacks; 12 where the box is several signs merged (`MULTI`) or noise |
| reading error | 20 | 9% | both ids exist and stay distinct in the new inventory; 14 where one pass had it right, 6 where neither did |

So GOLD-4A's 22.4% agreement measured the inventory, not the legibility of the page: three quarters of the
disagreement is two ids for one shape or one id for two shapes. The 9% reading-error residue (about 20 of 283
signs) is the floor a second blind pass on this inventory has to beat; the 80% gate is reachable in principle.

**4. Pass A rebuilt for all four cryptograms** from box_labels.tsv (`passA.tsv`, 1315 rows, now with a family
column) and written to `ciphertext_draft.tsv` (same rows, single pass A; `ciphertext.txt` untouched -- the
next Sonnet job is a blind pass B against `glyphs/inventory.png` and decides it). N/K/IC per cryptogram with
`scripts/compute_ic.py`'s own controls (fr16 and en16_repo text at the same N, uniform random at the same N and
K, 20 trials each; full four-way table in `glyphs/ic_inventory.txt`; sign ids, `_`/`MULTI` excluded):

| group | N | K | IC target | IC fr16 | IC en16 | IC uniform (same K) |
|---|---|---|---|---|---|---|
| #1 | 132 | 58 | 0.0397 | 0.0694 | 0.0915 | 0.0172 |
| #2 (2a+2b) | 734 | 123 | 0.0465 | 0.0696 | 0.0989 | 0.0082 |
| #3 | 116 | 59 | 0.0352 | 0.0695 | 0.0915 | 0.0169 |
| #4 (4a+4b) | 269 | 85 | 0.0282 | 0.0704 | 0.0973 | 0.0118 |
| combined | 1251 | 160 | 0.0391 | 0.0697 | 0.1022 | 0.0063 |

On families the same rows read 0.0452 / 0.0506 / 0.0390 / 0.0300 / 0.0435 (K 56 / 121 / 57 / 84 / 158). Reading
this against GOLD-4A's table: K more than doubled (69 -> 160) and the uniform control fell accordingly (0.0145
-> 0.0063), while the target IC barely moved (0.038 -> 0.039): the text is now **six times** its uniform-random
control at the same K and N, still at 56% of French and 38% of English. Cryptogram 4's IC fell from 0.055 to
0.028 with K 49 -> 85: GOLD-4A's kNN had been forcing c4's boxes into ids it already had (a collapse the
"higher IC" reflected), and by eye c4 is the most varied page (85 ids in 269 signs; c2 has 123 in 734). None of
this is a reading; grade S throughout, 0 H, 0 C. Rule 10: nothing here is a novelty claim.

**Limits, stated plainly.** (a) The eye labels are one pass by one session, graded by that session's own
confidence; the H/M/L shares above are self-assessed, and the matched check is the blind pass B the brief
names as the next job, not anything in this section. (b) 36 composite ids are a naming decision, not a finding
that they are single signs; a base+mark reading of the same boxes would give a smaller K and a higher IC, and
the names make that re-count mechanical. (c) 29 boxes are `_` (faint marks, bleed-through, dust) and 35 are
`MULTI` (several signs in one box, mostly c2's ornate lines and c4a's lines 11-13): these are segmentation
work, not inventory work, and are excluded from the IC rows above and flagged in box_labels.tsv. (d) The IC
controls are letter frequencies of running text; a matched control for a 160-symbol homophonic or code design
at N=1251 (rule 3) has not been run and is the cheap test before any solver: `tools/family_run.py` with a
synthetic homophonic cipher at this N and K would say whether 0.039 is what such a design gives.

Reproduce: `cd ciphers/debosnys-1883 && python3 scripts/gold4c_inventory.py --check` (exit 0 when passA.tsv,
ciphertext_draft.tsv, disagreements_classes.tsv and glyphs/ic_inventory.txt match box_labels.tsv).

Suggested next (one line each, not started): blind pass B (Sonnet) on `glyphs/strips/` against
`glyphs/inventory.png`, all four cryptograms, 80% gate per line; a base+mark re-count of the 36 composite ids
against marks.tsv's mark classes; a matched synthetic homophonic control at N=1251, K=160 through
`tools/family_run.py` before any IC-based claim.

Requests this job: none (disk and CPU only). Subagents: none.

## GOLD-4E, cryptogram 1 pass B (25 Sept 2026, session GOLD-4E, Sonnet)

Brief: `.claude/briefs/runs/2026-09-25-lane-gold-debosnys-c1passB.md`. Cap $3 / 25 min, started 19:05 UTC
(GOLD-4D, the same job on all four cryptograms through one subagent, was interrupted at 3.3x its cap with
nothing pushed; this job is c1 only, done directly, no subagent). Intake gate at launch: `debosnys-1883: open
(line 1) -- edition/page or full-text-search citation found within 6 lines` (exit 0).

**Blind pass B** (`passB_c1.tsv`, 136 rows): each of c1's six line strips (`glyphs/strips/c1_L01.jpg`
.. `c1_L06.jpg`, upscaled 4x with Pillow for legibility, `/tmp` scratch only) read sign-by-sign against
`glyphs/inventory.tsv` (the 160-id atlas) and `glyphs/inventory.png`; `passA.tsv`, `box_labels.tsv`,
`ciphertext_draft.tsv` and `ciphertext.txt` were not opened before this pass. Box segmentation matched pass A's
exactly (136 boxes each line-by-line) since both come from the same pre-cut strip crops -- this pass supplies
only the sign id per box, not new segmentation.

**Reconciliation** (`tools/reconcile_passes.py`, pass A = `passA_c1.tsv` extracted from GOLD-4C's `passA.tsv`):
full-id agreement **86/138 aligned columns = 62.3%**; family/base-level (both passes' sign ids folded through
`glyphs/inventory.tsv`'s own `family` column, which folds PCT-SLASH->PCT and BAR-SOLID->BLOB but not the
broader eye-merges GOLD-4C's prose describes) **91/137 = 66.4%**. Both well under the 80% gate.

**Disagreement classes, 52 columns** (`disagreements_c1_passB.tsv`, `disagreements_c1_passB_classes.tsv`):
classified **mechanically**, not settled on the image -- the 25-minute/\$3 cap did not leave time to re-open
each of 52 columns against the crop, which the brief asked for and this job did not do. The mechanical proxy
(gap or MULTI/`_` on either side -> segmentation; same `family` on both sides -> inventory confusion; otherwise
reading error) gives: **segmentation 7, inventory confusion 5, reading error 40 (of 52)**. This undercounts
inventory confusion relative to GOLD-4C's c4 finding (76%) because the family column folds only two declared
variant pairs, not the eye-level "one id for several shapes" merges that pass required looking at the page;
most of the 40 "reading error" columns are unverified and likely include further inventory confusion once
someone opens the crops. Flagged column count: of the 52, 8 were flagged low-confidence by pass A only, 30 by
pass B only, 9 by both, 5 by neither (`flagged` field in the classes file).

**Step 3 (gate):** full-id agreement 62.3% is under the 80% threshold, so per the brief `ciphertext.txt` is left
untouched; `ciphertext_c1_draft.tsv` (136 aligned rows, agreed signs at H, disputed columns at M with A's/B's
value in `alt`) is written instead.

**Honest limits.** (a) This pass was one session, one read, under a hard 25-minute wall-clock stop; 62.3% is
what a rushed second eye gets on this inventory, not a ceiling -- GOLD-4C's own reasoning (three-quarters of
c4's disagreement was inventory confusion, not legibility) was reached only after settling columns on the
image, which this job's budget did not include. (b) The `base` column pass B wrote per-row was an ad hoc
simplification (e.g. O-TILDE -> O) that does not match `inventory.tsv`'s own `family` grouping and was not used
for the reported base-level number; the family-column fold above is the one reported. (c) No decoding attempted.
Grade: S/M throughout (cryptanalytic inventory work), 0 H, 0 C. Rule 10: nothing here is a novelty claim.

Suggested next (one line, not started): a reconciler session opens `disagreements_c1_passB.tsv` against
`glyphs/strips/c1_L0*.jpg` and settles the 52 columns by eye, which is what would move this from 62% toward
GOLD-4C's c4 ceiling (91%) if the same inventory-confusion pattern holds for c1.

Requests this job: none (disk and CPU only, one `pip install pillow` for local image upscaling). Subagents: none.

## GOLD-D1 (25 Sept 2026, session_01Qcv68Pn46JNXkktRXTv6DL, Sonnet)

Controls-only job pricing the transcription before any more transcription spend: a base+mark recount of
GOLD-4C's 160-id inventory (K_base 128, 16 mark classes) and profile-/noise-matched homophonic-French controls
at K 160, at base level, and at K 160 minus X, fr19 corpus, 3 seeds each, never the target. Full numbers, the
recount table, the two new `tools/families/homophonic.py` params (`profile=target`, `noise=p`) and the branch
decision: `HYPOTHESES.md` section "GOLD-D1, noise-matched controls". Headline: clean control clears the 0.6 gate
only at base level (K_base 128, mean 0.859), not at the full 160-id level (mean 0.440) -- branch (b), BM has
headroom, H does not; no design clears the gate once 10-20 pct transcription noise is added. No decoding, no
images, no transcription; status stays `open`; grade S throughout, 0 H, 0 C.

## GOLD-D2 (25 Sept 2026, session_019a43vGLshPA8EZvcuNjGCG, Sonnet)

Controls-only job filling D1's base-level noise curve between its 0 and 0.10 points (2.5/5/7.5 pct), pricing c2
(N=734) settled alone against the whole four-cryptogram inventory, and adding a K160 0.05 pct point for the
record; same procedure as D1 (`tools/family_run.py --family homophonic`, fr19, seeds 1-3, restarts 8,
`--param profile=target`), scratch cipher copies only, target never run. Full numbers and table:
`HYPOTHESES.md` section "GOLD-D2, base-level noise curve". Headline: base-level control mean is 0.816 at 2.5 pct
noise but drops to 0.385 at 5 pct and 0.322 at 7.5 pct; against the top block's own gate (settlement licensed
only at >= 0.5 at 5 pct AND >= 0.4 at 7.5 pct), both conditions fail, so the verdict is **(c) for the letter
families**: no letter-substitution design (base level, K160, or c2 settled alone at 0.433) reads above the gate
at the noise a settled two-pass transcription is expected to carry. A c1 or c2 image-settlement pass is not
licensed by these numbers. No decoding, no images, no transcription; status stays `open` (rule 5: not
`closed-negative`); grade S throughout, 0 H, 0 C.

## Museum reply (MAIL-3, 28 Sept 2026)

The Adirondack History Museum (Essex County Historical Society) answered the 26 Sept 2026 email
(outreach/debosnys-museum.md, ASKS row 52) on 28 Sept 2026 at 18:09 UTC, read by the owner-account orchestrator:

- **No key.** They found no key sheet or cipher alphabet among Debosnys's papers. The "key survives at the
  museum" route is closed; the cryptograms stay a cryptanalysis question (status unchanged, `open`).
- **Clear-text scans, restricted.** They shared scans of his clear-text writings (about 43 images, Google Drive)
  as a restricted collection, for reference and research only, not to be shared or published without their
  permission. The terms and the handling rules are in `RESTRICTED.md`: nothing from the scans (image, crop,
  transcription, quotation) enters this repository or any public place, and findings derived from them are
  published only after the museum's written permission. The scans were not downloaded in this job.
- Next step (suggestion, not run): a research-only job reads the scans off-repo for the crib/host-text question
  the spec already names (the clear poems), under RESTRICTED.md, and records here only whether a usable crib
  exists; a thank-you reply is in Gmail for the owner.

## Campaign (28 Sept 2026, DEBOSNYS-RUNNER-3, Fable, session_018qnyJQbVSd2NyPvDVApXqS)

Brief: `.claude/briefs/runs/2026-09-28-debosnys-runner-3.md` (owner decision 20:4x UTC: lean in on this target as a
fourth campaign). Rows, budget and log: `CAMPAIGN.md`. Nothing below is a reading; rule 10 throughout.

### H1, check-solved refresh (28 Sept 2026, three Sonnet search subagents, 21:16-21:27 UTC)

`checksolved_2026-09-28.tsv` (133 rows: 71 no-claim pages, 28 system guesses, 17 partial claims, 0 N0 candidates;
saved page texts stay in the session's scratch, not committed). Covered: Cipherbrain's Debosnys tag (all 8 posts,
2015-2021, every comment thread; the solved-cryptograms category has no Debosnys entry), Cipher Mysteries (the
2015 "Thoughts" post with its 90 comments, the Cimbria and 2021 Keff/DNA/Sektu posts with comments),
cipherfoundation.org's Debosnys page (six scans, no transcription or reading), Google Books snippet search on
Farnsworth 2010 and Bauer 2017 (Bauer's index: "Debosnys 195-217, Greek poem 216"; no reading in any snippet;
Farnsworth has no preview, no IA item and no HathiTrust record under OCLC 495995946/963914459, so its reported
cipher appendix stays unchecked), IA full text (33 be-api calls, nothing beyond 1883 reportage and Bauer's
teaching passages), OpenAlex 0 / CrossRef 0 / Semantic Scholar generic only, Reddit (OAuth search: three casual
threads, r/codes r/cryptography r/ciphers r/UnresolvedMysteries 0 hits), Wikipedia article + talk + List of
ciphertexts (unsolved), podcast and news pages (Dark Histories notes, Crime Capsule, History.com, Spyscape),
zodiackillerciphers.com site search (none), voynich.ninja (one Voynich thread, member-only), Sektu's feed (no
Debosnys post after 7 Aug 2017), 38 web searches. Unreachable: schmeh.org (connection reset), Quora (403),
puzzling.stackexchange (fetch refused), darkhistories.com (bot interstitial), YouTube comments.

Both solver repositories now carry Debosnys work (both absent from the 23 Sept snapshots GOLD-0D grepped):
- **Bourdeau, cyphersolver `targets/debosnys/NOTES.md` (15 Sept 2026; clone at commit 648309e, 26 Sept; code MIT,
  text CC BY 4.0):** "nobody has published a decryption of a single word". His own transcriptions (verse 279 tokens
  / 111 types; No.10 block 99 / 72; No.9 597 / 239) and results: (i) the verse's line-final glyphs are identical
  within 9 of 10 couplets and match 0 of 9 across couplet boundaries (rimes plates, AABB), so the line-final glyph
  encodes sound at syllable scale; (ii) crib **No.10 cipher = lines 1-8 of the clear poem below it**: isomorph
  alignment 58 against random French verse median 59 / max 66, while a planted encoding of the same poem scores
  86-88 (control max 74-80) -- a control-backed negative; (iii) the verse against 7,821 twenty-line couplet windows
  of 28 French verse volumes: no outlier, planted window ranks 1st of 7,821; (iv) Delille's Aeneid V, Moore,
  Stoddart, his own English poems: chance level; (v) a mark-stack "monograph" letter reading: real order does not
  beat shuffled; (vi) a clean one-to-one syllabary positive control at 1,000 glyphs recovers 0.0 pct of tokens
  (5.4 pct at 5,000), and a unicity estimate of 800-2,000 glyphs for a 333-type syllabary key. His conclusion: a
  syllabary too short for a key-only attack; a crib (a copied source, or a key sheet at the museum) is the only route.
- **Aymeloglu, unsolved-ciphers `TARGETS.md` row 9 (17 Sept 2026; no licence, cited only):** "open, eleven rounds",
  transcription 1,139 groups / 365 labels, no cross-block repeat over three glyphs, matched controls fail at the
  target density, "needs human palaeography"; no reading.

The one concrete reading claim on record is still Rick A. Roberts's comment of 23 Nov 2015 on Cipher Mysteries ("the
last line of the 'L.M.F.' page deciphers to 'ULTIME'"), with no method, key or follow-up: a partial claim, not
checkable without a stated key. Numerology comments (dots under H.D.D.L.M.F. = missing letters; "X = 66 = W") give no
table and no plaintext. **Verdict: open, no N0.** The campaign continues. Requests: scienceblogs.de 13,
ciphermysteries.com 18, cipherfoundation.org 2, googleapis 26, be-api 33, archive.org 2, openlibrary 2, hathitrust 2,
openalex 1, semanticscholar 2, crossref 1, oauth.reddit.com 12, reddit.com 2 (403), sektu 3, wikipedia 3, others 1
each; no 429 except one Semantic Scholar 429 cleared on a single retry.

### H2, cryptogram 1 third pass and adjudication (28 Sept 2026, 21:19-21:28 UTC)

Rule written and committed before any crop was cut (`scripts/PROMPTS_c1.md`, commit 610a4675). Unit: the physical
box (both passes read the same 136 pre-cut boxes), so the disputed set is the 52 positions where `passA_c1.tsv` and
`passB_c1.tsv` differ (`scripts/h2_disputed_positions.tsv`; GOLD-4E's 52 aligned columns include 4 alignment-gap
artefacts; position-based agreement 84/136 = 61.8 pct, family 66.2 pct). Crops: `scripts/h2_crops.py` (6x Lanczos
per-sign crops from the Schmeh PNG's own pixels plus a row-context strip with the box outlined; the inventory sheet in
17 tiles; regenerable, not committed). Reader: five value-blind Fable subagent calls (lines 1-2, 3-4, 5, 6, and two
line-5 boxes the third call's list had mis-numbered), given only crop paths and the inventory tiles, never a pass file:
`passC_c1.tsv` (52 rows; self-graded H 28 / M 17 / L 7). Adjudication: `scripts/h2_adjudicate.py` (`--check` exits
non-zero if `ciphertext_c1_draft.tsv` or the cryptogram-1 section of `ciphertext.txt` is stale).

| number (rule 5 of PROMPTS_c1.md) | value |
|---|---|
| (a) pairwise blind, disputed 52, full id | A-C 22/52 = 0.423; B-C 5/52 = 0.096 |
| (a) pairwise blind, disputed 52, family | A-C 25/52; B-C 10/52 |
| (b) settled by majority | full id 27, family 3, base 3 |
| (b) agreement over 136 boxes after adjudication | full 111/136 = 81.6 pct; family 114/136 = 83.8 pct; base 117/136 = 86.0 pct |
| (c) unsettled | 19 (17 three-way splits, 2 segmentation flags: C read MULTI/`_`) |
| (d) type-noise estimate of the settled draft | floor 19/136 = 14.0 pct, ceiling 25/136 = 18.4 pct |
| gate 80 pct full id | met; cryptogram 1 written to `ciphertext.txt` in inventory ids per rule 6 |

Reading these honestly: the third reader sides with pass A on 42 pct of the disputed boxes and with pass B on 10 pct,
so the settled c1 is mostly pass A (GOLD-4C's own by-eye labels) with GOLD-4E's rushed pass B as the outlier; and a
third of the disputed boxes (17 of 52) drew three different ids from three readers, which is the inventory-confusion
shape GOLD-4C found on c4 (several ids for one shape) rather than illegibility. The 80 pct gate is met by majority
adjudication, but the type noise the draft carries (14-18 pct) sits far past the GOLD-D2 knee (0.816 at 2.5 pct,
0.385 at 5 pct), so **no letter-substitution attack on c1 is licensed by this pass either**; what it buys is a
settled c1 for the structural tests (H3, H5, H6) and a confusability list for the inventory. Settled K for c1: see
`ciphertext_c1_draft.tsv` (grade S/M, 0 H-from-key, 0 C-from-plaintext). Costs: five Fable subagent calls of about
135-145k tokens each; the orchestrator reads the session cost.

### H4, crib test against the c3-page poem (28 Sept 2026, CPU only, `scripts/h4_crib_test.py`)

Statistic S1 = share of repeated-sign pairs whose aligned plaintext units are also equal (1.0 for any one-sign-one-unit
cipher at the right offset, minus transcription noise), maximised over every offset with the shorter sequence nested
in the longer; nulls: 1000 unit-order shuffles and 1000 line-order shuffles of the poem, gate at the 97.5th percentile
of both plus a secondary statistic. Cryptograms 1-4 (pass A; c1 also as the H2 settled draft) x letter / syllable /
word x 160-id / base level: **0 of 24 clear** (`h4_result.json`; best c1-syllable at the 92nd percentile; the settled c1
crosses p975 on S1 alone for syllables, 0.0436 vs 0.0403, and fails the other two statistics). Planted positive control
(`--planted`, `h4_planted.json`): the poem's own letters / syllables / words enciphered with a homophonic key at each
cryptogram's K, then 0 / 5 / 15 pct type noise, clears at every setting (S1 0.54-0.78 at 15 pct against nulls under
0.21), so the test has power at the noise the H2 draft carries. **Control-backed negative**: the clear poem on the
cryptogram-3 page is not the contiguous plaintext of any of the four cryptograms under those units. Bourdeau's
isomorph test (15 Sept 2026) reached the same for the No.10 block with its own planted control. Untested: the Greek
Anacreon-preface ode on the c4 reverse (not on disk), non-contiguous or reordered pairings.

### H5, couplet rhyme on our transcription (28 Sept 2026, CPU only, `scripts/h5_couplets.py`)

Bourdeau's 15 Sept 2026 observation on his own read of the cipher verse (cryptogram 4): line-final glyphs identical
within 9 of 10 couplets, 0 of 9 across couplet boundaries. His transcription (`sources/bourdeau/cyphersolver-targets-
debosnys/verse_transcription.py`, MIT, credited) reproduces that under a 20,000-permutation line-order null,
p < 0.0001. **On our pass A** (19 lines: c4a's 14 are verse lines 2-15 and c4b's 5 are 16-20, see H7 below), with the
segmenter's trailing punctuation boxes dropped (BLOB, HOOK-L, DASH-H, `_`, MULTI): **within-couplet identical 4 of 9,
across 0 of 9, p = 0.0001** at full id and at family level (raw last box: 2/9 vs 0/9, p 0.09, since our last box is
usually the comma or dot he strips). The five couplets that do not match on ours are two ids for one shape (NOTE vs
PICT-ARROW for his "dark note with arrow, two dots below"; PCT-SLASH vs CIRC-O for his SL(y,o)), the OX / DAGGER-O pair
he also reads as a near-rhyme, and two lines where our last non-punctuation token is QUESTION. So an independent
transcription confirms: **the line-final sign encodes sound (rimes plates, AABB)**, which puts the unit at syllable
scale and rules out a plain letter substitution for the verse, unless the rhyme is written at the letter level and the
final letters happen to match, which 0 of 9 across boundaries argues against. Grade S, structural; no reading.

### H7 finding: cryptogram 4's first verse line is missing from our transcription (28 Sept 2026)

Checking our c4 lines against Bourdeau's: our c4a L01 opens with the heart pictogram that opens his verse line 2, our
L03 with the sun of his line 4, L12 with the leaf of his line 13, L13 with the anchor of his line 14; and the page image
carries a full cipher line directly under "monographe. verse." at page y about 385-420 (delta-ring, %, curl, slash,
tilde-o, xx, y, venus, ., slash-x, tilde-o, X, curl, comma -- his line 1), above GOLD-4A's crop box (y from 425), which
had been drawn to exclude the title and monogram. So the verse has 20 lines (as Sektu and Bourdeau count) and our N for
c4 is short by about 13 signs. CAMPAIGN.md H7 is the fix (segment that band, classify, eye pass, append as c4a_L00).

### H3, unit profile with matched French controls (28 Sept 2026, CPU only, `scripts/h3_unit_profile.py`)

Seven token statistics of the target (pooled and per cryptogram, 160-id and base level, c1 as the H2-settled draft)
against 200 samples of fr19 prose at the same N under six unit hypotheses, each a control that can differ from the
target on every statistic: letter, phonetic-shorthand alphabet (letters with silent finals and doubles dropped, the
token profile a Duployé-style writing leaves), syllable (crude onset-nucleus-coda), rime (nucleus+coda, Sektu's 2017
rhyme-group unit), word (nomenclator), and a K-matched flat homophonic. Pooled, id160, N 1251 (band = 2.5-97.5 pct):

| statistic | target | letter | shorthand | syllable | rime | word | homophonic K160 |
|---|---|---|---|---|---|---|---|
| K | 160 | 22-25 | 23-25 | 357-455 | 98-127 | 473-599 | 159-160 (by construction) |
| hapax share | 0.31 | 0-0.08 | 0-0.08 | 0.50-0.62 | **0.29-0.47** | 0.66-0.80 | 0-0.02 |
| top-1 share | 0.161 | **0.147-0.193** | **0.120-0.165** | 0.034-0.054 | 0.245-0.321 | 0.030-0.067 | 0.011-0.015 |
| top-5 share | 0.314 | 0.467-0.517 | 0.468-0.510 | 0.136-0.181 | 0.512-0.604 | 0.122-0.174 | 0.053-0.064 |
| IC | 0.039 | 0.073-0.083 | 0.069-0.077 | 0.008-0.011 | 0.091-0.130 | 0.007-0.010 | 0.006 |
| doubled-adjacent | 0.047 | **0.023-0.048** | 0.004-0.014 | 0.001-0.008 | 0.079-0.130 | 0-0.005 | 0.001-0.006 |
| bigram-repeat share | 0.434 | 0.937-0.963 | 0.934-0.958 | 0.184-0.346 | 0.676-0.752 | 0.116-0.223 | 0.066-0.112 |

No unit fits more than two of seven (per-cryptogram rows in `h3_profile.json` say the same). The target sits between
the syllable and the rime bands on K, top-5, IC and bigram repetition, with one letter-like dominant sign (X, 16 pct):
a syllable-scale inventory of about 160 types plus a dominant sign, which is also what H5's couplet rhymes and
Bourdeau's line-length arithmetic point to, and not a letter substitution (K alone excludes it, before any solver).
Shape census from the inventory names (descriptive): 23 pictogram ids, 15 Latin/Greek letters, 15 typographic or
astronomical symbols, 55 composites (base plus stacked marks), 52 abstract strokes; 33 pct of ids and 27 pct of tokens
are not strokes, so a period stenography (Duployé 1867, Prévost-Delaunay, Aimé-Paris, Pitman: closed stroke alphabets
of 25-40 signs) is excluded on shape and on K without a shorthand-sample control being needed. Caveats: prose, not
verse; no injected transcription noise (14-18 pct on c1 inflates K and hapax); crude syllabification. H9 covers those.

### H6, confusability fold (28 Sept 2026, CPU only, `scripts/h6_confusability.py`, `h6_folds.json`)

79 distinct id pairs are confused across the 52 disputed c1 boxes (A, B, C triples): PCT/PCT-SLASH 8, X/X-CURL 5,
PCT/X 3, twelve pairs at 2. Folding pairs confused five or more times (PCT+PCT-SLASH, X+X-CURL) lifts c1 agreement
from 81.6 to 86.8 pct at K_fold 158; three or more (one slash-family component) to 87.5 pct at 157; two or more chains
eleven ids into one component through pairwise links (X-PCT-Y-CURL-O-TILDE-WAVE...), 94.9 pct at 149, which is not
one shape and not a legal fold. The row's condition (90 pct at K under 100) is not met: the confusions are reader
quality (pass B) and the %-like slash family, not evidence of a smaller alphabet. No control box was bought.

### H7 done: the verse's first line added (28 Sept 2026, 21:3x-21:45 UTC)

Band `images/Debosnys-Cryptogram-4a.png` @ 280,372,740,436 segmented with `tools/glyph_atlas.py segment` alongside the
six original page boxes of `glyphs/pages.json` (deterministic: every original box reproduces exactly, so
`glyphs/signs.tsv`, `marks.tsv`, `bitmaps.npz`, `pages.json` were replaced by the seven-page run): 16 boxes, kNN read
with `classify --exclude-page` against `labels_box.json` (`scripts/h7_knn_c4a0.tsv`), then one value-blind Fable eye
pass with H2's prompt (rule in `scripts/PROMPTS_c1.md`, H7 section, written before the reader ran). Eye and kNN agree
on 10 of 16; the eye labels (H when both agree and the eye says H, else M) are appended to `glyphs/box_labels.tsv` as
page `c4a0`, line 1: DIAMOND PCT Y-CURL PCT-SLASH O-TILDE X-SLASH X VENUS `_` PCT-SLASH X O-TILDE `_` X WAVE `_` (13
signs, a dot, a comma, a stain fragment; box 11's small x is the lower part of a slash-with-x composite the segmenter
split, kept as labelled at L). Token for token that is Bourdeau's verse line 1 (DELTA_RING SL(o,o) GAM SL(t,d) N_O XS2 Y
VENUS . SL(p,x) N_O? X TCURL ,). `lines.tsv` gains `c4a0_L01`; `scripts/gold4c_inventory.py` and
`scripts/base_mark_recount.py` group `c4a0` under cryptogram 4 and were re-run (`--check` clean): c4 is 20 lines,
pooled N 1264 (was 1251). `scripts/h5_couplets.py` on ten couplets: within 5/10, across 0/9, p < 0.0001 on ours
(line 1 and 2 both end WAVE, his TCURL TCURL).

### H8 and H9 (28 Sept 2026, CPU only)

**H8, rhyme signs** (`scripts/h8_rhyme_signs.py`, `h8_rhyme.json`): on Bourdeau's read of the verse the ten couplet
rhyme signs occur inside lines at or below the rate their overall share predicts (TCURL 6 interior vs 9.3 expected,
XD 23 vs 23.2, VENUS 8 vs 9.3, SL(y,o) and EQ3_O 0 vs 1.9), and on ours likewise (WAVE 6 vs 5.1, X 33 vs 38.4): they
are ordinary units that also fall line-final, not line markers. Marked/unmarked classes of his ten rhyme signs run
S M S M S S S M S S (6 changes of 9; a strict masculine/feminine alternation would give 9; permutation p 0.16), so
the stacked mark does not alternate the way a mute-e marker would; no corpus of French rimes plates is on disk, so
this part has no control and claims nothing (rule 3). **H9, the controls H3 lacked** (`scripts/h9_controls.py`,
`h9_controls.json`, 200 samples per condition): a coarse syllabary (fr19 syllables merged to the target's K) fits
K, doubled-adjacent and bigram repetition but the target is more skewed than it (top-1 0.161, top-5 0.314, IC
0.039 above the band) and has more hapax (0.31 above it); 15 pct injected type noise moves no verdict; Baudelaire's
verse (`tools/data/fr19v`, fetched once) in place of prose changes nothing for c4 or pooled. Reading of H3+H9: a
syllable-scale inventory carrying one letter-like dominant sign and a long one-off tail (the pictograms), i.e. a
mixed design; H10 tests that shape directly. Grade S, no reading.

### H10-H14, the design question narrowed and left open (28 Sept 2026, CPU only)

`scripts/h10_mixed.py` (`h10_mixed.json`): a mixed design (a share q of words spelled letter by letter, the rest by a
coarse syllabary merged to the target's K) fits the pooled profile on at most 2 of 7 statistics at any q, and c4 on 5
of 7 at q 0.3-0.4 (misses: K higher and bigram repetition lower in the target, the direction transcription noise that
invents ids pushes). `scripts/h11_line_lengths.py` (`h11_lines.json`): the verse carries 13-14 signs per line
(ours mean 13.2, Bourdeau 13.95; both differ from a strict 12/13 alexandrine and from the clear poem's 9-15 syllables
per line, permutation p under 0.01), about 1.2-1.3 signs per syllable of a 12-syllable line, far under a letter
level. `scripts/h13_newtype_noise.py` (`h13_noise.json`, v2 K formula): with a noise model in which 5-20 pct of
tokens are replaced and half of those become fresh singleton ids, the q 0.3 mixed design sits inside the band on all
seven statistics for c4 (N 282, 5-10 pct noise) and for c1 (N 132, most settings) -- read as consistency across 72
conditions, not proof -- while the pooled text (N 1264, tight bands) fits no design on more than 3 of 7: one sign
(X) at 16 pct and a top-5 at 31 pct sit above every letters+syllables band. `--drop-x` (`h14_noise_noX.json`):
removing X flips the pooled profile from too skewed to too flat on top-1, top-5, IC and bigram repetition, so X is
not a null hiding a natural text. Where this leaves the design: syllable-scale units with couplet rhymes (H5), line
lengths 1.2-1.3x a syllable count (H11), each cryptogram's own profile compatible with letters+syllables plus about
10 pct invented-type noise (H13), but a pooled distribution -- one dominant sign over a tail flatter than any
natural-unit model -- that none of these reproduce: the signature of spread homophones or a large code, which the
GOLD-D1 `profile=target` control reproduced only by construction. Grade S throughout; no reading; status `open`.

### H21 and H21b, cryptogram 2 settled (28 Sept 2026, 22:0x-22:4x UTC)

Pass B: five value-blind Sonnet calls on the numbered line strips of c2a (17 lines) and c2b (9 lines) rendered by
`tools/glyph_atlas.py classify --strips` at 2x, against the inventory tiles (`passB_c2.tsv`, 778 rows: H 141 / M 464
/ L 173). Position-based agreement with pass A (GOLD-4C's by-eye kNN labels): 380/778 = 48.8 pct full id, 51.0 pct
family; 398 disputed. Third pass: 27 value-blind Fable calls on per-sign 6x crops of the disputed boxes only
(`scripts/h21_pipeline.py crops`; rule in `scripts/PROMPTS_c1.md`, H21 section, written before pass B landed;
`passC_c2.tsv`, H 134 / M 235 / L 29). Adjudication (`scripts/h21_pipeline.py adjudicate`, `--check` clean):

| number | value |
|---|---|
| pairwise blind on the 398 disputed, full id | A-C 100/398 = 0.251; B-C 164/398 = 0.412 |
| pairwise blind, family | A-C 116/398; B-C 172/398 |
| settled by majority | full 264, family 7, base 18 |
| agreement over 778 boxes | full 644/778 = 82.8 pct; family 83.7; base 86.0 |
| unsettled | 109 (104 three-way, 5 segmentation flags) |
| type-noise estimate | floor 14.0 pct, ceiling 17.2 pct |
| gate 80 pct | met; cryptogram 2 (pages a and b) written to `ciphertext.txt` in inventory ids, `?` on unsettled boxes |

On c2 the third reader sides with pass B (the strip read) more than with pass A (the kNN-seeded eye labels), the
reverse of c1, so neither earlier pass is the reliable one across pages; the majority of three is what the draft
rests on, and its 14-17 pct residual noise is the same band as c1's. Pooled profile on the settled c1+c2 (H3/H13
scripts now read both settled drafts; N 1197 excluding `_`/MULTI): X 13.9 pct (was 16.1), top-5 0.286, IC 0.032,
bigram repetition 0.383; the mixed letters+syllables design with 5 pct invented-type noise now sits inside the band
on 5 of 7 statistics (top-1 still above, bigram repetition still below); merging doubled X adds nothing. A settled
transcription moved the pooled skew about halfway to the design. Grade S/M; nothing read; status `open`. Costs: the
orchestrator reads the session (5 Sonnet + 27 Fable subagent calls for this row).

### H23, cryptograms 3 and 4 settled; the whole transcription three-pass (28 Sept 2026, 22:3x-22:5x UTC)

Same recipe as H21 (`scripts/PROMPTS_c1.md`, H23 section): four value-blind Sonnet calls on the numbered strips of c3
(4 lines), c4a (14) and c4b (5) gave `passB_c34.tsv` (401 rows); position agreement with pass A 240/401 = 59.9 pct
(family 61.1); 161 disputed boxes read by eleven value-blind Fable calls (`passC_c34.tsv`, H 34 / M 114 / L 13);
`scripts/h21_pipeline.py adjudicate --pages c3,c4a,c4b` (`--check` clean): A-C 61/161 = 0.379, B-C 60/161 = 0.373;
settled 121 full + 4 family + 2 base; **agreement 361/401 = 90.0 pct full id** (91.0 family, 91.5 base); 31 three-way
splits and 3 segmentation flags; type-noise floor 8.5 pct, ceiling 10.0 pct. The verse's first line (c4a0, H7) rides on
its two H7 witnesses (eye pass and kNN; H where they agree). `ciphertext.txt` now carries all four cryptograms in
inventory ids from three-pass drafts (`ciphertext_c1_draft.tsv`, `ciphertext_c2_draft.tsv`, `ciphertext_c34_draft.tsv`),
each regenerable and checked by its script. Settled per cryptogram: c1 81.6 pct (noise 14-18), c2 82.8 (14-17),
c3+c4 90.0 (8.5-10). On the settled verse the couplet-rhyme test (H5 re-run) still gives within 5/10, across 0/9,
p < 0.0001. Pooled on all settled text (N 1184 excluding `_`/MULTI): K 160, X 12.8 pct, top-5 0.270, IC 0.029,
doubled 0.030, bigram repetition 0.369; the mixed letters+syllables design with invented-type noise fits 4 of 7 (top-1
above the band, hapax and bigram repetition below) -- the residual survives a settled transcription, so it is a
property of the system, not of the reading. Grade S/M throughout; nothing read; status `open`. Costs: 4 Sonnet + 11
Fable subagent calls for this row (the orchestrator reads the session).

### H31, pictograms as units (29 Sept 2026, DEBOSNYS-RUNNER-3b, session_018dZR8GLsqcAxRTHKBiDGFu, CPU only)

`scripts/h31_pictograms.py` (`h31_pictograms.json`) and `scripts/h31b_class_control.py` (`h31_class_control.json`), on
the settled drafts with punctuation-class boxes dropped; pictograms are h3_unit_profile.py's shape class (PICT-* plus
SUN, STAR, HEART, RAM): 23 ids, 60 tokens over 56 lines. Null: 10,000 within-line shuffles (every statistic can move
under it). **Pictograms begin lines far more often than chance: 11 of 56 lines start with one against a null band of
0-6 (expectation 2.95, p 0.0002)**; verse alone 4 of 20 (band 0-3, p 0.013), prose c1-c3 alone 7 of 36 (band 0-5,
p 0.001). Line-final 5 (band 0-6), within-line fifths, pictogram-pictogram adjacency (4, band 1-7) and adjacency to X
(13, band 9-21) are all inside their bands. Power: moving every pictogram to its line's first slot gives 37 line-initial
(all lines), far outside, so the test can see an edge preference at this N. Class control (can differ, rule 3): among
1,000 random sets of non-pictogram ids of the same token count (60), none reaches the pictograms' line-initial excess
(8.05 against a random-set p97.5 of 3.47; rare-id sets, count <= 10, p97.5 4.91), while their line-final excess (2.05)
is ordinary (rank 0.175). The lines they open: verse lines 2, 4, 13, 14 (PICT-HEART, SUN, PICT-LEAF, PICT-ANCHOR); c1
L02 (SUN); c2a L02, L03, L05, L15 (PICT-LEAF, PICT-EAGLE, PICT-HOUSE, PICT-ANCHOR); c2b L07 (SUN); c3 L01
(PICT-RUNNER). Only one of the ten couplet-end signs is a pictogram (PICT-ARROW, couplet 8). Reading: the pictograms
are not decoration and not symmetric whole-word logograms (those would also crowd line ends); they are units that
prefer a line's first slot, i.e. word- or phrase-initial units (a capital-like or determinative-like role, or
word-initial syllables written as pictures). A structural result at grade S, nothing read; the named next step is H32
(what precedes an interior pictogram). Status `open`.

### H29, Bourdeau's No.9 read as a fourth witness for cryptogram 2 (29 Sept 2026, DEBOSNYS-RUNNER-3b, CPU only)

Bourdeau's `n9_transcription.py` (MIT, commit 648309e8, one raw.githubusercontent.com request; snapshot in
`sources/bourdeau/cyphersolver-targets-debosnys/`, credited, never ours): 25 lines, 637 tokens, = our c2a L01-L17 and
c2b L01-L08 (his CLEAR_* initials dropped). `scripts/h29_bourdeau_n9.py` (`h29_bourdeau_n9.json`, `h29_votes.tsv`), the
H26 recipe with everything held out: the his-code -> our-id concordance is fitted on odd (even) lines using only boxes
that are not three-way splits, and scored on the other half. Gate written into the script before the run: apply the
votes to a variant draft only if held-out concordance on known codes is >= 0.60 and the resolution count beats a
shuffled-code control's p97.5. **Held-out concordance 0.514 of known codes** (0.503 / 0.524 per fold; 0.31-0.35 of
all aligned non-split boxes) -- below the verse's 0.54-0.66 (H26) and below the gate. Of 96 three-way splits aligned,
his mapped code equals one of the three readings on 14 (A 5, C 9, B 0) against a within-line shuffled-code control
of mean 3.8, p97.5 7 -- more than chance, but the witness quality fails the gate, so **no vote is applied**;
`ciphertext_c2_draft.tsv` and `ciphertext.txt` are unchanged and the 104 splits stay M. The 14 votes are kept in
`h29_votes.tsv` for any later adjudication. Side result for H31, an independent reader: 6 of his 25 lines open with a
pictogram (his PIC_* class, 33 tokens) against a within-line expectation of 1.3 (p 0.0008), so the line-initial
preference reproduces on a transcription that is not ours; his line-final pictograms 4 (p 0.033, borderline; ours
ordinary). Grade S, nothing read; status `open`.

### H32, the sign before an interior pictogram (29 Sept 2026, DEBOSNYS-RUNNER-3b, CPU only)

`scripts/h32_boundary.py` (`h32_boundary.json`): word-final-prone ids fitted on one half of the 56 settled lines (>= 2
line-final and at least twice their within-line expectation), scored on the other half. Interior pictograms preceded by
a final-prone id: **1 of 49** against a 10,000-shuffle band of 1-8 (p_ge 0.99) -- no enrichment; followed by one 1 of
49. Planted power control (each interior pictogram's predecessor set to the fold's most final-prone id) 45 of 49, so
the scoring can see the effect. But the instrument itself does not replicate: the two folds' final-prone sets share
one id of nine (WAVE; fold 0 BUCKET, DAGGER-O, PCT-SLASH, QUESTION, WAVE, XX-TILDE; fold 1 DASH-V, O-DASH2, O-SLASH,
WAVE), i.e. line ends in the prose are not a stable word-end signal at this N (physical line wraps, and only the 20
verse ends are known sense breaks). Logged as untestable by this method at this N, not as a refutation of H31's
word-initial reading. Grade S; nothing read; status `open`.

### H33 and H35, which ids open lines, and whether H31 survives layout exclusions (29 Sept 2026, CPU only)

H33 (`scripts/h33_initial_class.py`, `h33_initial_class.json`): per id with >= 3 settled tokens (83 ids), line-initial
and line-final counts against a per-line shuffle null, Benjamini-Hochberg at q 0.10: **no single id clears** at either
edge (counts of 1-4 per id are too small). The two strongest openers are pictograms (PICT-LEAF 2 vs 0.16 expected,
p 0.008; SUN 3 vs 0.44, p 0.009), then BAR-THIN and X-O (p 0.03); no Latin-letter id (D-LETTER, T-LETTER ...) is
among them, so the "capitals of names" variant gets no support. The strongest closers are BUCKET, QUESTION, XX-TILDE
(p 0.004-0.006), none past BH. H31's excess is a property of the pictogram class, not of one sign.
H35 (`scripts/h35_layout_check.py`, `h35_layout_check.json`): the line-initial excess with lines that begin in a `_`
region dropped (portrait area of c2a L04-L06, unread starts) is 10 of 50 (expected 2.66, band to 6, p 0.0004); with
each page's first line dropped 10 of 50 (p 0.0002); both 9 of 45 (expected 2.18, band to 5, p 0.0002); verse only
4 of 20 (p 0.015). Bourdeau's verse read (verse_transcription.py) opens the same four verse lines (2, 4, 13, 14) with
the same four signs (HEART, PIC_SUN, PIC_LEAF, PIC_ANCHOR): 4 of 20 vs expected 0.88, p 0.008 -- a second reader of
the same image, not independent evidence of the statistic, but no transcription artefact on our side. H31 stands as a
layout-robust class effect. Grade S; nothing read; status `open`.
