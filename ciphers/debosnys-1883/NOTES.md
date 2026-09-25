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

- Fetch cryptogram #4 (4a, 4b; 2 more requests to scienceblogs.de) to complete the set.
- Hand-merge the 90 over-split clusters against the contact sheets to get a real distinct-K
  and a trustworthy IC before treating the homophonic/code hypothesis as supported.
- Spec's cheap test 2 (form/crib test against Debosnys's own clear poems, including the one
  on the #3 page itself) is now unusually promising given the poem sitting right on the same
  sheet as the cipher -- a natural next breadth test.
