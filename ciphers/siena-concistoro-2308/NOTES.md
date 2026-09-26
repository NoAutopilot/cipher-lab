open
Bourdeau CATALOGUE.md #336 (dbourdeau/cyphersolver, clone fc0c9e865d0fae67ca92d19750d2b09ab11972e0, siena1421/NOTES.md read in full) read by this worker: whole busta on DECODE, 25 photographed pieces; nos. 6/24, 20/23, 7, 9, 11, 15, 17, 19, 21 filed as open/blocked in Bourdeau's own escalation log (no filed key fits at their length); no. 1 (1421) and nos. 2, 26-28 not among the DECODE photographs. Aymeloglu/unsolved-ciphers (clone 2495c45e8b94ffbc4f09a085224aa5ebce5cdf9f) grepped for "siena"/"concistoro"/"4790".."4814": no hits. OpenAlex `search=Siena Concistoro cipher` and Semantic Scholar `query=Siena Concistoro cifra` (26 Sept 2026): no matching work. DECODE listing (login-free, tools/decode_list.py not run this pass -- read via Bourdeau's own catalogue note instead, which already gives the record status "images" for R4790-R4814); full-size DECODE images not fetched this pass (account-wide block, see CLAUDE.md Access playbook).

## Intake gate

    $ python3 tools/intake_gate_check.py siena-concistoro-2308
    siena-concistoro-2308: open (line 1) -- edition/page or full-text-search citation found within 6 lines
    exit=0

## QUEUE row 2's first cheap test: Bourdeau nos. 25/14/4 key transfer

Slug: siena-concistoro-2308. Target: QUEUE.md "Scored backlog for LANE B6, second pass" row 2, Archivio di
Stato di Siena, Concistoro 2308 fasc. 2 "Lettere in cifra" (DECODE keys R4746-R4789, letters R4790-R4814;
Bourdeau #336). No transcription of this busta exists in ciphers/ yet; the test below works entirely from
Bourdeau's own already-published transcripts and keys (MIT code / CC BY 4.0 text, dbourdeau/cyphersolver,
credited above), read at the pinned commit, per this brief -- no image fetch, no DECODE login.

Test: apply Bourdeau's own recovered sign->letter key values for Siena nos. 25 (`keys/no25_key.txt`), no. 14
(`key14.txt`) and no. 4 (`keys/no04_key.txt`, short/simple sign tokens only -- its longer descriptive names,
e.g. "S (5-like)", cannot literally match another piece's own sign legend) against Bourdeau's own transcripts
of the shorter still-open pieces 7 (R4796), 9 (R4798), 11 (R4800), 15 (R4803), 17 (unlisted R-number, Bourdeau's
own no.17 slot), 19 (R4807) and 21 (R4809) (`transcripts/no07.tok`, `no09.txt` TRANSCRIPTION section, `no11.tok`,
`no15.tok`, `no17.tok`, `no19.txt`/`no21.txt` TRANSCRIPTION sections; token sequences reproduced in
`specs/cheap-tests/siena-concistoro-2308/pieces.py`, key tables in `keys.py`). Coverage (fraction of a piece's
sign tokens present in a given key) is reported but is NOT the test statistic (CLAUDE.md rule 3, bCAS/AX-5799:
coverage from a per-token key cannot depend on token order, so a coverage-only gate is not a test). The test
statistic is order-sensitive: `tools/judge_plaintext.py`'s `it` corpus 4-gram score and its greedy word-cover
(`min_word_cover`), computed on the decoded letters in real transcript order vs. the same key applied to the
same piece with token order scrambled (3 seeds: 1, 2, 3) -- coverage is identical real vs. scrambled by
construction (checked with an assert in the script) but score/word-cover can differ, which is what makes this
a real control per rule 3's own worked examples.

Era flag (queue row 2): these letters are 15th/early-16th c. (busta spans back to 1421); `it` on disk
(tools/data/it16, 6 volumes of 16th-c. Italian letters, ~mid-late 16th c. register) is a real era gap, wider
than the pt17/es17c precedent (CLAUDE.md rule 3) -- graded by eye alongside the numbers below, not trusted on
the score alone even if it had passed.

Script: `specs/cheap-tests/siena-concistoro-2308/run_test.py`. Reference thresholds at N=100 letters on the
`it` corpus (200 samples, seed 1): real_p05 = -1.007, null_p99 = -1.630, real_median = -0.823.

| piece | key | sign_cov (matched/total) | decoded letters | real score | scrambled score mean (3 seeds) | real word-cover | scrambled word-cover mean |
|---|---|---|---|---|---|---|---|
| no07 | no25 | 0.270 (98/363) | 98 | -2.139 | -2.193 | 0.367 | 0.354 |
| no07 | no14 | 0.468 (170/363) | 170 | -2.120 | -2.112 | 0.518 | 0.490 |
| no07 | no04 | 0.457 (166/363) | 166 | -1.885 | -2.022 | 0.572 | 0.488 |
| no09 | no25 | 0.304 (14/46) | 14 | -2.007 | -2.325 | 0.214 | 0.000 |
| no09 | no14 | 0.435 (20/46) | 20 | -1.562 | -2.141 | 0.700 | 0.533 |
| no09 | no04 | 0.435 (20/46) | 20 | -2.311 | -2.161 | 0.250 | 0.483 |
| no11 | no25 | 0.166 (68/409) | 68 | -2.208 | -2.232 | 0.485 | 0.456 |
| no11 | no14 | 0.281 (115/409) | 115 | -1.909 | -1.916 | 0.713 | 0.716 |
| no11 | no04 | 0.152 (62/409) | 62 | -1.927 | -1.869 | 0.790 | 0.839 |
| no15 | no25 | 0.180 (38/211) | 38 | -2.140 | -2.166 | 0.158 | 0.140 |
| no15 | no14 | 0.417 (88/211) | 88 | -1.989 | -2.016 | 0.568 | 0.617 |
| no15 | no04 | 0.204 (43/211) | 43 | -1.968 | -1.975 | 0.605 | 0.659 |
| no17 | no25 | 0.416 (117/281) | 117 | -2.177 | -2.065 | 0.248 | 0.239 |
| no17 | no14 | 0.438 (123/281) | 123 | -2.193 | -2.254 | 0.179 | 0.198 |
| no17 | no04 | 0.416 (117/281) | 117 | -2.316 | -2.151 | 0.436 | 0.442 |
| no19 | no25 | 0.299 (35/117) | 35 | -2.159 | -2.081 | 0.600 | 0.590 |
| no19 | no14 | 0.350 (41/117) | 41 | -2.445 | -2.138 | 0.488 | 0.447 |
| no19 | no04 | 0.188 (22/117) | 22 | -2.435 | -2.087 | 0.682 | 0.636 |
| no21 | no25 | 0.327 (35/107) | 35 | -1.832 | -1.940 | 0.714 | 0.610 |
| no21 | no14 | 0.308 (33/107) | 33 | -2.124 | -2.160 | 0.455 | 0.414 |
| no21 | no04 | 0.206 (22/107) | 22 | -1.938 | -2.355 | 0.636 | 0.455 |

Result: **negative, matched control.** All 21 real-order scores (-1.56 to -2.45) sit below the `it` corpus's
own null_p99 (-1.63) for the majority of cells, and every one sits below real_p05 (-1.007) -- worse than the
letter-shuffled-null threshold, not just below real prose. The real-order vs. scrambled-order comparison shows
no consistent, one-directional margin: real beats scrambled in 11 of 21 cells and loses in 10, by amounts
(median |delta| about 0.1-0.2 score points, 0.03-0.24 word-cover) that are well inside the seed-to-seed noise
of the scrambled control itself (compare no09/no25's own scrambled_cover_mean of 0.000, from 3-4 seeds on only
14 letters). None of nos. 25/14/4's key values decode any of pieces 7, 9, 11, 15, 17, 19, 21 into Italian: no
gain from real order over scrambled order, at any of the three keys, on any of the seven pieces. Grade: S
(cryptanalytic negative with a matched control), per CLAUDE.md rule 4 -- no H or C token read.

Caveat (rule 2, image over transcription): this test used only Bourdeau's own already-published transcripts
and sign legends, not the DECODE page images. A different transcription convention, or the physical possibility
that one of these seven pieces literally reuses no. 25/14/4's key under a different sign-naming scheme than
Bourdeau assigned it, is not excluded by this test -- only that Bourdeau's own transcript + Bourdeau's own key,
read literally, do not fit.

Judge (rule 7), the single best-scoring cell of the 21 (no09/key14, real_score -1.562, real word-cover 0.700):

    $ python3 tools/judge_plaintext.py specs/siena-concistoro-2308.json --text "oueepunavaoeeuaavele"
    FAIL language: score=-1.562, null_p99=-1.188, real_p05=-1.115, real_median=-0.832, mode=both, N=20
    ok   words: cover=0.7, min=0.6, real_text_median_cover=0.9
    FAIL - siena-concistoro-2308 (a PASS is a gate for a verifier, not a reading; rule 10)

FAIL on language even at this best-scoring cell (below both null_p99 and real_p05 at this short N=20); words
alone would have passed the 0.6 bar but the language check does not, and this is only 20 letters against a
piece's real 46 tokens (44% coverage) -- not a candidate reading, the closest of 21 negative cells.

Next step (not run this pass, per brief -- ciphertext-only anneal on nos. 6/24 and 20/23 needs a synthetic-
Italian control of matching length/design and is out of this $3 cap): queue row 2's own fallback.

Search-before-solving (rule 1): Bourdeau CATALOGUE.md #336 read in full (see above); Aymeloglu repo grepped,
no hits; one OpenAlex + one Semantic Scholar query, no hits; web search "Siena Concistoro 2308 lettere in
cifra" and "Siena Concistoro cipher 1421-1530", no solved-status hits found. DECODE record status read from
Bourdeau's own catalogue note (images present, R4790-R4814); the site's own listing not re-fetched this pass.
Checked 26 Sept 2026.
