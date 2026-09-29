# R2-3 CRIB-LENGTH: result (DEB-SWARM2-R2-3, 29 Sept 2026, 07:15-07:3x UTC)

Grade S. Nothing is read; no key; no crib passes; status of debosnys-1883 stays `open`. Public copies only (Project
Gutenberg texts; the settled public-image drafts). Pre-registration: PLAN.md, pushed at 07:18 UTC before any real score.

**Answer.** A copied 20-line window of the pool texts is not visible in c4 under a letter-level design (homophonic letters
or a running key, up to 15 pct noise): the length term that finds every such control is not above its genre null on c4.
Under a syllabic design the instrument cannot tell: its control fails. The pre-registered combined score S did pass its
bar on c4, but a genre-matched null added afterwards voids that pass (details below).

## Data
- Target: c4 verse, 20 lines (c4a0_L01, c4a_L01-L14, c4b_L01-L05), punctuation set {BLOB, HOOK-L, DASH-H, _, MULTI}
  and clear spans dropped. Signs per line 13 13 12 10 15 16 14 12 16 13 10 7 17 17 10 11 15 13 15 14 (N 263). Line-final
  signs, H5 rule: WAVE WAVE X X SLASH CIRC-O QUESTION O-DASH2 QUESTION VENUS DELTA DELTA OX DAGGER-O NOTE PICT-ARROW WAVE
  WAVE S-CURL S-CURL.
- Candidate pool (Project Gutenberg, fetched once 29 Sept 2026 to the session scratchpad, not committed): Moore, Complete
  Poems #8187, Odes of Anacreon #38230, Lalla Rookh #76794; Stoddart, The Death-Wake #16601; Hugo, Contemplations #29843,
  #29844, Légende des siècles I-II #72885, #76396. 61,663 windows. **Not in the pool (not on Gutenberg): Chivers,
  Colesworthy, Peterson's 1879, Lamartine's verse, Béranger, Musset's verse** (Musset tomes 3-5 fetched, are plays and
  prose, dropped).
- Decoys (same period, disjoint authors): Longfellow #1365, Whittier #9600, Poe #10031, Lowell #13310, Hemans #66785,
  Campbell #59788, Tennyson #8601, C. Rossetti #19188, Byron #8861, Shelley #4800; Gautier #37733 #44180 #45886 #10442,
  Heredia #14805, Verlaine #15112 #61039, Sully Prudhomme #17916, Rimbaud #56708, Desbordes-Valmore #14258, Baudelaire
  #26710. 253,907 windows. (Holmes #7400, Bryant #29700, Burns #1279, Coppée #15324: connection reset, not retried.)
- Requests: gutenberg.org 37 (1 catalogue, 36 texts), 2 s apart.

## Known-answer control (run first; control.tsv, control_poolnull.tsv)
10 source windows (5 EN, 5 FR, seeded), each enciphered three ways with 15 pct noise (replacement : indel 3:1).
The 15 pct brackets c4's own measured error (three-pass disagreement 8.5-10 pct; H53 hidden error bound 6.8-11.7 pct).

| design | rank among 1,000 decoys, S (pre-registered) | rank among 54-60k same-genre pool windows, S | same, R only | R of true window |
|---|---|---|---|---|
| homophonic letters | 1 in 10/10 | 1 in 5/10 (max 49) | **1 in 10/10** | 0.88-0.99 |
| running key | 1 in 10/10 | 1 in 5/10 (max 121) | **1 in 10/10** | 0.85-0.99 |
| syllabic (extra) | 1 in 5/10 (max 57) | 9 to 25,954 | 14 to 41,737 | -0.07-0.72 |

Pre-registered control rule (median rank 1 among 1,000 for homophonic and running key): **pass**. The post hoc same-genre
run shows that R (line length only) is the part that finds letter-level designs; S's rhyme term adds genre noise.

## Real search (result.json, couplet_null.json)
- Best S: 1.359, Moore, Complete Poems #8187, verse-line index 1647 (an Anacreon ode, "Oh, when I drink, true joy is
  mine" .. "I've time for naught but pleasure now"); R 0.751, P 0.608. Second: 1.356, Hugo, Légende II #76396 index 1011
  ("Sire Roland, ma pente naturelle"), R 0.607, P 0.749. Decoy p99 of S 0.718; max-corrected p against the decoys < 0.001.
  **The pre-registered kill test is therefore formally not met.**
- **But the decoys were not genre-matched.** Post hoc null (not pre-registered): permute c4's 10 couplets as units
  (lengths and finals together) and take the pool maximum each time, 200 permutations: the pool maximum reaches 1.359 in
  **33.5 pct** of them (null median 1.325, p95 1.465). The real best S is what the pool's couplet verse reaches against
  any couplet-ordered profile. It is not a property of any one poem, and the top two windows (Moore, Hugo) are 0.003
  apart. **Not a hit**. No crib is handed to the scorer.
- Best R on c4: 0.815 (Hugo #72885 index 1917); the couplet-shuffle null reaches it in **66.5 pct**. Every letter-level
  control's true window had R 0.85-0.99 and ranked 1 against the same-genre pool. **Kill test on the instrument that
  works (R, letter-level designs): met.**

## What this licenses
- Control-backed negative, conditional on the settled public drafts: c4 is not 20 consecutive lines of the 8 pool texts
  enciphered as homophonic letters or with a running key at 15 pct noise or less.
- Not tested: the texts missing from the pool (above); non-contiguous or re-lineated copies; patchworks (his clear poems
  are Moore patchworks, WRITINGS.tsv), which this window statistic cannot see.
- Untestable by this instrument: a syllabic (or other sub-word-unit) design. Its control fails, and c4's
  signs-per-line (7-17, about 0.5 per letter of a typical window) fit sub-letter-rate units better than letters. That is
  the design H5's rhymes already point to.
- A note for a later crib instrument, not a claim: the top-S window is a Moore Anacreon ode, and the back of c4 carries
  Moore's Greek preface ode (WRITINGS.tsv). The statistic does not single it out.
- c2: not tested. Its line breaks are page layout, not verse lines, so the length profile has no meaning there.

Files: PLAN.md (pre-registration), crib_length.py (statistic, control, real search), couplet_null.py and
control_poolnull.py (post hoc, labelled), control.tsv, control_poolnull.tsv, result.json, couplet_null.json, LOG.md.
Reproduce: fetch the Gutenberg ids above to DIR/pool and DIR/decoy, then `python3 crib_length.py --texts DIR` (about 35 s).
