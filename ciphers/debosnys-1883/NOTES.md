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
