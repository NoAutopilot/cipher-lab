open

check-solved (26 Sept 2026, bRIK, LANE B5): grepped a fresh shallow clone of dbourdeau/cyphersolver
(commit fc0c9e865d0fae67ca92d19750d2b09ab11972e0, 2026-09-25 -- riksarkivet1628/NOTES.md read in full:
"outcome (21 Sept 2026): read in part... R4282, R4284 and R4306 were attempted and stay open"; the
R4284 key-test leaf is explicitly logged there as "not yet used" against R4282); grepped a fresh
shallow clone of aaymeloglu/unsolved-ciphers (both catalogue/decode-records.jsonl and
decode-catalog.csv give id 4282 and id 4284 both `Non-decrypted`, no further note; clone deleted
after grep); DECODE's own login-free listing cache already on disk (sources/decode/records-non-decrypted-2026-09-24.tsv,
fetched 24 Sept 2026, read this session, not re-fetched) lists 4282 and 4284 both `Non-decrypted`,
tagged `riksarkivet1628[read in part]` `ours:oxenstierna-gustav-adolf-1632`; full-text search via
OpenAlex (`api.openalex.org/works?search=Riksarkivet Chifferklaver cipher decrypted`, one call, one
irrelevant hit -- a terminology paper) and Semantic Scholar (`graph/v1/paper/search?query=Riksarkivet
Chifferklaver cipher`, 429 once, one retry after a 3s pause, 0 results) found no scholarship. Verdict:
open, unsolved, no source found that changes Bourdeau's own "open" call. `python3 tools/intake_gate_check.py
riksarkivet-r4282-1628` output pasted below.

## What this is

Riksarkivet Stockholm, Chifferklaver låda II:113 (DECODE record 4282) and låda II:114 (DECODE record
4284), 1628 (QUEUE.md G4 / "Re-rank for LANE B5" rank 4). Both Latin letters in the same "unknown
sender/recipient, Stockholm, Latin, 1628-1646" catalogue bundle (DECODE catalogue #207) that Bourdeau's
own NOTES.md (`riksarkivet1628/`) shows is really four unrelated correspondences -- the R4282/R4284
key-sharing tested here is a hypothesis from that bundling, not an established fact (QUEUE.md's own
caveat on this row).

- R4282: a ~1,000-character Latin letter cipher using Latin letter shapes plus a handful of special
  signs (D, L=lambda, T=delta, B=boxed square, E=epsilon, F=phi, A=alpha, M=mu, G) and digits 3 4 5 7 8,
  with a few words left in clear Latin. Not read (Bourdeau: "homophonic and substitution annealing...
  gave no Latin").
- R4284: a numeric homophonic cipher (108 distinct values over ~754 numbers), also not read, but
  carries on one leaf a **key-test**: four Latin phrases ("effusorem sanguinis", "pestem patriae",
  "praeter naturalem", "disturbatorem religionis") written by a period hand directly over their
  cipher-letter equivalents -- a different, letter-shaped alphabet from R4284's own numeric body,
  which Bourdeau's notes flag as possibly R4282's own alphabet, never tried against it.

Image over transcription (rule 2): only Bourdeau's single-pass eye transcriptions of both leaves exist
here (`r4282_transcription_bourdeau.txt`, `r4284_transcription_bourdeau.txt`, copied verbatim from
dbourdeau/cyphersolver, riksarkivet1628/, commit fc0c9e8, read 26 Sept 2026, credited per CLAUDE.md
item 8 -- MIT code, CC BY 4.0 text). No page image was fetched this job (disk/git-only cap; DECODE's
full-size images are account-blocked without a working login, and Riksarkivet's own IIIF route was not
needed since Bourdeau's transcription already existed). Any negative below is conditional on that
transcription being accurate; Bourdeau's own comment on the key-test leaf notes "individual letters
uncertain, esp. g/y/p/z", and two of the four crib words come up 1-2 characters longer or shorter on
the cipher side than the Latin phrase they gloss (see `report.json`'s `crib_mismatches`), consistent
with that uncertainty.

## Test run (26 Sept 2026, bRIK): R4284 key-test leaf as a crib against R4282

Method: `scripts/crib_test.py` (reproducible, `--check` re-derives and diffs; rule 7). It parses the
four (Latin phrase, cipher word) pairs from the key-test leaf, aligns them character-by-character
(truncating the two mismatched-length pairs at the shorter side, logged in `report.json`), builds a
letter -> cipher-sign(s) key (homophonic: e.g. `s` has four signs, `e` three, `t` one), and applies the
reverse (sign -> majority letter) to every non-bracketed cipher sign in R4282.

Design (rule 3, three conditions, one gate question: does the crib's *specific* letter assignment do
anything on R4282, beyond what its symbol alphabet alone would by chance):
- **A** (the test): real crib key vs real R4282.
- **B0-B2** (control 1): three synthetic keys of the same shape -- the same sign groupings the crib
  actually found (which signs are homophones of which other signs), but with the 16 letter labels
  reshuffled across those groups -- vs real R4282. Isolates whether the crib's own letter choices, not
  just its alphabet, matter.
- **C0-C2** (control 2): the real crib key vs three random shuffles of R4282's own cipher-character
  stream (multiset preserved, order destroyed). Isolates whether any Latin-like structure the crib
  surfaces depends on R4282's actual character order.

No wired Latin corpus exists for `tools/judge_plaintext.py` (`LANG_CORPORA` has no `"la"` key; the
tool's own comment calls `tools/data/la_repo` circular -- its one file is a target's own reading, not
an independent corpus -- "not wired"). Latin-likeness is graded by eye (rule 4: M grade) using a small
fixed list of common short Latin function words/endings (`et in ad ut sit est non sed per cum qui quod
de ab ex si se nec jam tam tum hoc hic haec ille eius suis quae quibus atque que tur unt ent ibus orum
arum tio tas`) as a substring-match count over decoded tokens, applied identically to A, B and C so it
is at least a fair comparison even though it is not a language model.

### Numbers (from `report.json`; German not run -- letter is Latin, not the 1628-33 German-era R4330/31
crib, so `de16`/`de` was not the applicable judge here; H0 count 0, C0, S0, all M/I)

| condition | coverage (chars) | coverage frac | Latin-hint tokens (of 155) | fully-covered tokens >=3 |
|---|---|---|---|---|
| A: real crib key vs real R4282 | 471/1094 | 0.4305 | 4 | 2 |
| B0: synthetic key (same shape) vs real R4282 | 471/1094 | 0.4305 | 8 | 2 |
| B1: synthetic key (same shape) vs real R4282 | 471/1094 | 0.4305 | 3 | 2 |
| B2: synthetic key (same shape) vs real R4282 | 471/1094 | 0.4305 | 8 | 2 |
| C0: real crib key vs shuffled R4282 | 471/1094 | 0.4305 | 1 | 3 |
| C1: real crib key vs shuffled R4282 | 471/1094 | 0.4305 | 2 | 4 |
| C2: real crib key vs shuffled R4282 | 471/1094 | 0.4305 | 1 | 5 |

Coverage (43.05%) is identical across every row by construction (A/B share the same known-sign set;
C preserves the character multiset) -- reported per rule 3 ("report both numbers"), not because it
distinguishes anything here. The number that would distinguish a real hit is the Latin-hint count:
real crib (A=4) sits inside, and below the mean of, the same-shape synthetic-key range (B: 8, 3, 8;
mean 6.3) and does not exceed the shuffled-R4282 range either (C: 1, 1, 2). By the fixed by-eye metric
used identically across all seven runs, R4284's key-test leaf, applied as a crib, does not make R4282
read more like Latin than a same-shape key with the letters reshuffled.

Correction (bRIKFIX, 26 Sept 2026, V8-QA7 finding 2): this paragraph previously misstated B as
"3, 4, 8; mean 5.0", transposed against its own table two lines above (row values 8, 3, 8) and against
`report.json`. Re-ran `ciphers/riksarkivet-r4282-1628/scripts/crib_test.py --check`: "OK: report.json
matches a fresh re-derivation" -- the table and `specs/riksarkivet-r4282-1628.json`'s "8, 3, 8 (mean
6.3)" were the correct values; this paragraph and STATUS.md's LANE B5 row were the ones wrong. The crib
verdict (4/155) is unaffected.

### Reading the decoded sample (grade M, by eye, sighted on `report.json`'s `sample_decoded` for A)

`_t_n m__save _sp___r _es_ft fv____ n____ n_p_r__pm ___p__e ____ _f__eaf_a__ vpf__v_e_ ...` -- no
run of more than 3-4 consecutive covered signs forms a recognisable Latin word or ending under the
fixed hint list beyond scattered 2-3-letter fragments ("save", "est" inside "_es_ft", "eaf" -- none of
which are the phrases used to build the key, so not circular, but also none is a clear content word).
Same impression on the B and C samples in `report.json` (not reproduced here for length).

### Verdict

**Partial, not closed-negative** (rule 5 as amended, CLAUDE.md LANE B3 line): this is a control-backed
negative for the specific hypothesis under test (R4284's key-test leaf, read as a direct letter-cipher
key, unlocks R4282), not a exhaustive negative for "R4282 and R4284 share a key" in general --
untested: (a) the key-test leaf might use a *different* sign-to-letter direction, i.e. plaintext read
top-to-bottom rather than left-to-right through the multi-line cipher block (Bourdeau's transcription
keeps the two-line phrase/cipher pairing but this job did not re-check the leaf image itself for a
column-wise reading); (b) the two length-mismatched pairs (`natvralem`/`cpikyppatb`,
`religionis`/`gtaygygdieys`) were truncated rather than re-aligned by eye against the image, which this
job's disk-only cap did not allow; (c) R4282's own special signs (L=lambda, T=delta, B, E, F, A, M, D,
G) were never assigned a letter by the crib at all (the leaf's cipher alphabet is plain Latin letters
plus one capital L and one digit 3), so 57% of R4282's characters are outside this crib's reach
regardless of alignment. A next worker with image access could re-transcribe the key-test leaf leaf
against the actual photograph to settle (a) and (b), and check whether R4282's special signs appear
anywhere else in the R4284 leaf or body that this pass did not have time to search.

No language-judge PASS/FAIL is claimed (no wired "la" corpus; see above). Files: `r4282_transcription_bourdeau.txt`,
`r4284_transcription_bourdeau.txt` (both credited copies from Bourdeau, dbourdeau/cyphersolver,
riksarkivet1628/, commit fc0c9e8, read 26 Sept 2026), `scripts/crib_test.py`, `report.json`.

## Escalation
- [x] siblings: Bourdeau's own NOTES.md for the 14-record bundle read in full (see check-solved above)
- [x] known-keys: this job (R4284's key-test leaf as a crib key)
- [x] clear-pages: R4282's own clear-Latin cribs ("et qualis sit eius futurus status dubitatur", "sed
      tamen ut res", "tractatus magnas admodum", "Mittatur nobis responsum") -- RIK-CRIBS, 2 Oct 2026: dragged
      as pattern cribs with tools/crib_pattern.py; the 22- and 37-letter phrases place nowhere at 0 misreads
      (where a design-matched synthetic places each at rank 1, key 15/15) and only at chance at 1-2 misreads;
      the two short phrases are below the instrument's resolution; max 3/12 signs agree with bRIK's R4284 crib
      key, matched by a negative crib. No partial key. See "## RIK-CRIBS" below and HYPOTHESES.md.
- [x] known-keys, shelf neighbours R4280/R4281 (FT4, 3 Oct 2026): both numeric-only keys; no sign overlap with R4282's
      letter-shape alphabet, stopped at the overlap check (see "## FT4" below). Not a test of R4282.
- [ ] known-keys (remaining): 66 of the 70 (after R4280/R4281 above); next: grep their DECODE `Symbol Sets` field
      (login-free record pages) for an Alphabet/letter-shape key before fetching any image, ~$1 fetched Chifferklaver låda II key records (R4259-R4329) still
      untried against R4282 -- this job used only R4284's key-test leaf, per its brief, not the other 68
- [ ] print: Rikskansleren Axel Oxenstiernas skrifter och brefvexling series II, and Camerarius editions,
      not searched this job (out of scope/cap)
- [ ] image re-check: the two mismatched-length crib pairs, and whether the leaf reads column-wise

## RIK-CRIBS (2 Oct 2026, account-4): the leaf's own clear-Latin phrases as cribs on the R4282 stream

Brief `.claude/briefs/runs/2026-10-02-account4-rik-cribs.md` (Escalation item "clear-pages"). Disk only, no
image, no network; conditional on Bourdeau's single-pass transcription (rule 2; `r4282_transcription_bourdeau.txt`,
dbourdeau/cyphersolver riksarkivet1628/, commit fc0c9e8, CC BY 4.0 -- cited, not copied as code).

**Where the clear phrases sit.** All four are inside the cipher text, not marginal: P1 `xpEr4m [et qualis sit]
[eius?] [futurus status dubitatur] | Spr MrAq5bD` (p.1 line 10, three brackets, the sentence resumes in cipher);
P2 `rbbl5p8MmLu [sed tamen ut res] LkMnl7oa` (p.1 line 21, mid-sentence, the strongest shape); P3
`fDeMrbm4nLx5 . [tractatus magnas admodum] EptMSab?` (p.1 line 25, after a stop); P4 `[Mittatur nobis responsum]
S? fbm7o` opens p.2. A phrase left in clear is not by itself evidence that the same words recur in cipher; the
test is whether any of them does.

**Method.** `scripts/clear_cribs.py` (rule 7, `--check` re-derives `cribs/clear_cribs_report.json`, verified
"OK" this session) builds `cribs/r4282_codes.tsv` (one row per sign, 1,094 signs, K=34, the same stream
`scripts/crib_test.py` parses -- asserted identical -- with the page as the group so no placement crosses the
p.1/p.2 boundary; the one `^` mid-token in `bLrMpkn^ou` is kept as a sign, as bRIK kept it) and
`cribs/brik_crib_key_compare.tsv` (bRIK's R4284 key-test crib reversed to sign -> majority letter: 13 signs,
4 ties `a b d e` left uncompared), then drags each phrase with `tools/crib_pattern.py`'s own `run` under
`--homophones` (a letter may have several signs; a sign has one letter), max-err 0, 1 and 2, la18 unigram,
200 shuffled-order controls, plus a same-length NEGATIVE crib from la18 tomus I and a design-matched POSITIVE
control (synthetic la18 letter, N=1094, K=34, R4284-shaped homophony, the phrase embedded; 100 shuffles).
The brief's `--lock`-style constraint from bRIK's key: the tool has no such option and none was added; runs are
unconstrained and agreement with bRIK's key is counted after the fact (`--compare`). The canonical CLI form,
run once this session and matching the script's P2-err0 row exactly:

```
python3 tools/crib_pattern.py --codes ciphers/riksarkivet-r4282-1628/cribs/r4282_codes.tsv \
  --crib "sed tamen ut res" --homophones --group-col page --lang la18 \
  --compare ciphers/riksarkivet-r4282-1628/cribs/brik_crib_key_compare.tsv --shuffles 200
REAL: 76 consistent placements at 76 distinct start positions; best score -2.611 (coverage 462 of 1094)
CONTROL (200 shuffled-order sequences): placements mean 43.8 p95 67 max 88; best score mean -2.624 p95 -2.592 max -2.550
RANK: real placements 76 vs shuffles -- 1/200 shuffles at or above; real best score -2.611 -- 57/200 shuffles at or above
```

`python3 tools/tests/test_crib_pattern.py`: "all ok" this session (the tool's own synthetic positive control).

**Numbers** (full table, one row per phrase and error setting, in HYPOTHESES.md; `cribs/clear_cribs_report.json`
has every placement's key). Per phrase, target vs the three controls:

| phrase (folded length) | max-err 0: real placements / shuffle p95 / negative crib / positive control | max-err 1: real / p95 / neg / pos | max-err 2: real / p95 / neg | best score rank (of 200 shuffles), err 0/1/2 | max agree with bRIK key, any placement (target / neg) |
|---|---|---|---|---|---|
| P1 et qualis sit eius futurus status dubitatur (37) | 0 / 0 / 0 / found rank 1, key 15/15 | 0 / 0 / 0 / found rank 1 | 0 / 0 / 0 | -- (nothing places, target or control) | -- |
| P1a et qualis sit (11) | 201 / 143 / 239 / rank 8 of 159, key 1/11 | 639 / 493 / 691 / rank 46 | 948 / 856 / 970 | 81 / 170 / 135 | 2 / 2 |
| P1b futurus status dubitatur (22) | 0 / 1 / 0 / found rank 1, key 11/11 | 3 / 6 / 1 / rank 3 of 5 | 28 / 26 / 12 | -- / 71 / 125 | 2 / 1 |
| P2 sed tamen ut res (13) | 76 / 67 / 84 / rank 15 of 95, key 1/13 | 418 / 287 / 402 / rank 74 | 788 / 637 / 774 | 57 / 52 / 165 | 3 / 3 |
| P3 tractatus magnas admodum (22) | 0 / 0 / 0 / found rank 1, key 15/15 | 1 / 4 / 2 / found rank 1 | 16 / 18 / 13 | -- / 77 / 112 | 2 / 0 |
| P4 Mittatur nobis responsum (22) | 0 / 0 / 0 / found rank 1, key 15/15 | 0 / 4 / 1 / found rank 1 | 8 / 14 / 9 | -- / -- / 148 | 1 / 1 |

**Result: negative with matched controls, at the instrument's resolution.** (a) The three 22-letter phrases and
the 37-letter whole place nowhere in the real stream at 0 misreads, where the design-matched synthetic places each
at its true start, rank 1, implied key right on all 15 signs (and shuffles of the synthetic place nothing): the
instrument can find a clean 22-letter crib at this N and K, and does not find these. At 1-2 misreads the real
stream admits 1-28 placements, inside what its own shuffles (p95 4-26) and the negative crib (1-13) admit, with
no best score above the shuffled p95 (rank 52-165 of 200). (b) The two short phrases (11, 13 letters) place
above the shuffled p95 in the target (201 vs 143; 76 vs 67) -- but the negative crib does the same (239 vs 172;
84 vs 63), so the excess is the real stream's own sign-order structure, not the Latin, and the positive control
cannot rank a true 11- or 13-letter placement either (rank 8-74, top key right 1/13): below resolution. (c) bRIK's
R4284 crib key: the best agreement any placement reaches is 3 of ~12 compared signs (P2 at err 1, one placement
of 418), matched exactly by the negative crib's 3 of 402; the top placements conflict with bRIK on the signs that
carry its own best support (`k=u`, `g=r`, `p=a`, `t=e`, `i=t`). Two independent cribs agreeing on 3-4 letters was
the brief's signal; it is not there. No partial key is implied; every letter value in `cribs/clear_cribs_report.json`
is M at most (rule 4) and none is a reading. Status stays `open`; not a NEAR.md row (nothing beat its control).

**What the negative is conditional on (rule 2/3).** The positive control is error-free; the transcription is a
single pass with no measured error rate ("u/n/M, q/g, k/K, b/h confusions are the main risk"). Max-err 2 covers
at most 2 misreads in a 22-sign window (about 9%); if the pass's real error rate is above that, the 22-letter
rows are a non-test rather than a negative (CLAUDE.md rule 3, SALV-DIAG). What would settle it is a second blind
pass on the two page images (Escalation item "image re-check"), which also fixes the two length-mismatched R4284
crib pairs -- an image-gated step, not this job. A second shape not tested here: the clear words may recur in
cipher inflected (`responsi`, `tractatuum`), which a whole-phrase drag cannot see; a stem-level drag (`respons`,
`tractat`, 7-8 letters) is below this instrument's resolution at N=1094 (the P1a/P2 rows show 11-13 letters
already are), so it needs a different instrument (a bigram-scored key search seeded by the stem) rather than a
re-run of this one.

**Files:** `scripts/clear_cribs.py`, `cribs/r4282_codes.tsv`, `cribs/brik_crib_key_compare.tsv`,
`cribs/clear_cribs_report.json`, `HYPOTHESES.md` (new). **Cost:** CPU only (about 90 s per derivation), no vision
calls, no network requests; USD figure is the orchestrator's to read.

## Web and blog check (WEBCHECK-riksarkivet-r4282-1628, 2 Oct 2026)

Required step of `.claude/briefs/check-solved.md` ("Open web and blog comment threads", CHECK-SOLVED-WEB, 28 Sept
2026), run 2 Oct 2026 00:14-00:20 UTC (clock read) by a Fable worker, brief
`.claude/briefs/runs/2026-10-01-account4-webcheck.md`. The item has no known sender or recipient (DECODE 4282/4284,
catalogue #207 "unknown sender/recipient, Stockholm, Latin, 1628-1646"), so the sender+recipient+date query is
replaced by shelfmark+date and by the bundle's only named people (Oxenstierna, Camerarius). Every hit about THIS
item is listed; a page is listed as "not about this item" only after it was opened.

### (a) Plain web searches (search engine, 12 queries)

| # | query | hits about this item |
|---|---|---|
| 1 | Riksarkivet "Chifferklaver" 1628 cipher Latin letter | dbourdeau.github.io/cyphersolver index (opened, below); sok.riksarkivet.se Chifferklaver collection page (catalogue description only, 16 boxes 1500s-1894, no item text); forum.skalman.nu t=38650 (opened, below); uio.no AI-decoding article (opened, below); rest unrelated (Borg, Bellaso, Cryptologia papal/Maximilian papers) |
| 2 | "effusorem sanguinis" "pestem patriae" cipher (R4284 key-test leaf phrases) | 0 -- classical Latin texts (Livy, Seneca, Digest), Caruso 2020 book title, Wikipedia cipher pages; none quotes the pair together or any 1628 letter |
| 3 | "et qualis sit eius futurus status dubitatur" (R4282's own clear-Latin phrase, exact quotes) | 0 -- only Digest of Justinian and other classical pages carrying the legal commonplace; no cipher page, no 1628 letter |
| 4 | DECODE record 4282 Riksarkivet cipher 1628 Stockholm Latin unknown sender | dbourdeau.github.io index + github.com/setsunaatto/cyphersolver (both opened, below); DECODE 2019 paper (ep.liu.se, database description, no item); rest unrelated |
| 5 | Riksarkivet 1628 cipher Chifferklaver solved Claude OR GPT "solves" (model-solve check) | 0 about this item: the Claude/AI hits are the Cyphral Distich 1653 (36kr, vals.ai, boingboing, dev.to) and the Kryptos-4 gist; setsunaatto fork and Bourdeau index again (opened) |
| 6 | "disturbatorem religionis" OR "praeter naturalem" cipher key 1628 Latin Riksarkivet | 0 -- Cryptologia papal-cipher paper (1625-28 Vatican, a different collection), Cipher Mysteries van Heeck 2016 (unrelated), Wikipedia/Amazon noise |
| 7 | Riksarkivet chiffer 1628 "låda II" latinsk brev olöst dechiffrerad (Swedish) | 0 -- sok.riksarkivet.se finding-aid pages (Salvius-Oxenstierna letters, Manuskriptsamlingen), no cipher item |
| 8 | "riksarkivet1628" cipher (Bourdeau's folder slug) | 0 -- Riksarkivet institutional pages only |
| 9 | "Chifferklaver" "II:113" OR "II:114" cipher key 1628 (shelfmark + cipher) | setsunaatto fork + Bourdeau index only (opened); the engine's own summary wrongly folds the Bremen 1631 R4330/31 result into the II:113/114 rows -- checked against the pages themselves, below: II:113/114 stay open there |
| 10 | Riksarkivet Stockholm 1628 Latin cipher letter unsolved homophonic "DECODE" Chifferklaver blog comment | Bourdeau index, Skalman thread, uio.no/sciencenorway article (same text, English mirror), SU Copiale page; none about this item |
| 11 | site:scienceblogs.de klausis-krypto-kolumne Riksarkivet Stockholm Chiffre 1628 (engine ignores site:) | 0 Cipherbrain posts about this item; results were the blog's static pages (Open Research Topics, 111 encrypted books, Catinat 2016) |
| 12 | site:cryptiana.blogspot.com / site:ciphermysteries.com Riksarkivet Swedish cipher 1628 (two queries) | 0 posts about this item on either (Cryptiana front page, 2025-09 and 2018 archive pages, Charles I 2021; CM Zodiac Z32 2014, van Heeck 2016, d'Agapeyeff) |

### (b) Blog site searches (each blog's own search box, both names where the first gave nothing)

| blog | query | result |
|---|---|---|
| Cipherbrain (scienceblogs.de/klausis-krypto-kolumne/?s=) | Riksarkivet | "Wir konnten leider keine Beiträge finden" -- 0 posts |
| Cipherbrain | Stockholm | 2 posts: "Schwedische Literatur-Wissenschaftlerin sucht Unterstützung..." (3 Apr 2015, Clas Livijn's 1781-1844 almanacs, 19th c., not this item) and the 2015 Goldene-Alice year review (no Swedish archive content); not plausible for a 1628 Latin letter, threads not read |
| Cipherbrain | Oxenstierna | 0 posts |
| Cryptiana blog (cryptiana.blogspot.com/search?q=) | Riksarkivet | "No posts matching the query" -- 0 |
| Cryptiana blog | Sweden | 2 posts (British codebreakers' French keys, 2 Jan 2024, 0 comments; Update on Korean ciphers, 23 Jul 2026, 0 comments -- "Torbjörn Andersson from Sweden" credited), neither about this item |
| Cryptiana blog | Oxenstierna | 0 |
| Tomokiyo's pages (sources/cryptiana/ on-disk snapshot, grep -ril riksarkivet, chifferklav, 4282, 4284, 1628; 0 requests) | -- | the only matches are digit-run coincidences inside long numbers (hardnuts.htm, jtelegraph.htm, polygram.htm, the 2019 Vatican-challenge post's number groups); `unsolved-2026-09-24.htm` does not name Riksarkivet or Chifferklaver; CRYPTO-INDEX.tsv's only 1628 row is the Vatican challenge (vatican.htm), a different collection |
| Cipher Mysteries (ciphermysteries.com/?s=) | Riksarkivet | "Nothing Found" -- 0 |
| Cipher Mysteries | Sweden cipher | 5 posts (Somerton Man/Handel 2020, Voynich art exhibition 2014, De Aqua 2009, German zodiac woodcuts 2009, Voynich news-bites 2008), none about this item |
| Cipher Mysteries | Oxenstierna | 0 |

### (c) Hits opened, comment threads read

1. https://dbourdeau.github.io/cyphersolver/riksarkivet1628.html (Bourdeau's live write-up, read 2 Oct 2026): R4282
   "attempted, unsolved", two keys from the same boxes "fit neither of the numerical letters", no plaintext; R4284
   "A homophonic Latin search produced Latin-sounding nonsense"; no update after 21 Sept 2026; GitHub Pages, no
   comment thread. Same state as the clone read by bRIK on 26 Sept 2026 (above).
2. https://github.com/dbourdeau/cyphersolver/issues?q=riksarkivet+OR+4282+OR+4284+OR+Chifferklaver -- 0 issues;
   the same query on /pulls -- 0 pull requests (2 Oct 2026). Nothing like the Lauriere issue 13 / PR 15 exists for
   this item.
3. https://github.com/setsunaatto/cyphersolver (the fork whose author read fr3625-lauriere-1593, 29-30 Sept 2026):
   README row "The Bremen letters read in full; three ciphers attempted, open." `targets/riksarkivet1628/` holds the
   same eleven files as Bourdeau's folder (NOTES.md, bremen_*, profile.json, qg.py, r4282_codes.txt,
   r4282_transcription.txt, r4284_transcription.txt, r4306_*, solve_num.py); its NOTES.md reads R4282 "homophonic
   and substitution annealing over the written word divisions and without them gave no Latin (best -2.77/char
   with breaks)", status open, and R4284 "not broken", status open, latest date in the file 21 September 2026
   (adds one archival note worth keeping: R4284 is labelled "Legat ... till L. Camerarius bref för 1628" -- the
   Camerarius lead already in the Escalation list above). `SOLVED_CATALOGUE.md` (compiled 17 Sept 2026) carries
   only row 65, Bremen R4330/R4331 (Nov-Dec 1631, read 21 Sept 2026); `TARGETS.md` does not mention R4282, R4284
   or Chifferklaver. No reading of this item in the fork.
4. https://forum.skalman.nu/viewtopic.php?t=38650 ("Chiffer", Swedish history forum, 13-14 Jan 2011, read in full):
   a novelist asking about 18th-century Swedish military ciphers; one poster ("Ben") describes the Riksarkivet
   Chifferklaver collection in general (16 boxes, 1500s-1894); no mention of 1628, a Latin letter, DECODE, or any
   decipherment.
5. https://www.uio.no/forskning/forskningsnytt/artikler/2025/med-ki-kan-forskere-dekode-hemmelige-brev.html
   (University of Oslo news, 2025, DECODE/Waldispühl; the hf.uio.no URL redirects here; sciencenorway.no carries
   the English mirror): general AI-decipherment piece, Mary Queen of Scots letters; the only Riksarkivet reference
   is a photo caption "Det svenske riksarkivet, Chifferklaver, II:121" -- a different box item, no text; no
   comment section.
6. sok.riksarkivet.se Chifferklaver collection page (from query 1): the archive's own description of the key
   collection; no item-level text, no decipherment.

Not reachable or not covered: none blocked (no 403/429/challenge on any host this run); Reddit not crawlable by
the search tool (same gap the hellen-frederick WEBCHECK logged).

Hits carrying a decipherment or plaintext of this item: 0. No decipherment or plaintext of this item located by
these queries on 2 Oct 2026 (a search result, never a novelty verdict, CLAUDE.md rule 10). Status word unchanged
(`open`).

Requests per host: search engine 14 queries; scienceblogs.de 3; cryptiana.blogspot.com 3; ciphermysteries.com 3;
github.com 7 (public pages, no API); dbourdeau.github.io 1; forum.skalman.nu 1; hf.uio.no 1 (301) + uio.no 1;
cryptiana.web.fc2.com 0 (on-disk snapshot grep).

### intake_gate_check re-run

```
$ python3 tools/intake_gate_check.py riksarkivet-r4282-1628
riksarkivet-r4282-1628: open (line 1) -- edition/page or full-text-search citation found within 6 lines
(exit 0)
```
## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/riksarkivet1628/NOTES.md
- Their extent, in their words: R4282, R4284, R4306 attempted and stay open; the two Bremen 1631 letters read in full
- Their date: 21 Sept 2026
- Note: already cited in our NOTES.md
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## Premise check (GF4-BATCH4, 3 Oct 2026)

Adversarial pass (.claude/briefs/check-solved.md, "Premise check"), run 3 Oct 2026 (clock read, `date -u`) by a Sonnet subagent of GF4-BATCH4; asked to prove R4282 is already done. No test, decode or reading run. Verdict: no decipherment, clear copy or key run on R4282 located.

- (a) Folder mentions: **not found**. Opened NOTES.md (323 lines), HYPOTHESES.md, report.json, cribs/*, scripts/*, both transcription files. Every "key"/"decipherment" mention is (i) Bourdeau's R4284 key-test leaf (four Latin phrases written over letter-cipher equivalents; a partial crib for a *letter* cipher, 13 signs, applied by bRIK 26 Sept 2026 to R4282 with controls: 4/155 Latin-hint tokens vs same-shape synthetic 8, 3, 8 -- not a decipherment of R4282); (ii) R4282's four clear-Latin phrases inside the cipher (dragged as cribs, RIK-CRIBS 2 Oct 2026, negative at the instrument's resolution); (iii) Bremen R4330/31 and E 708 interlinears, which belong to other letters. None decrypts R4282.
- (b) Other solvers' working files: **not found**. Shallow clone dbourdeau/cyphersolver HEAD 23416821 (opened targets/riksarkivet1628/ in full: NOTES.md, profile.json, qg.py, solve_num.py, r4282_codes.txt, r4282/r4284/r4306 transcriptions, bremen_*). R4282 only blind annealing ("gave no Latin", best -2.77/char); the R4284 key-test leaf "not yet used"; R4310 and R4296 keys tested only on R4306/R4284 (neither fits); no Oxenstierna/Gustav Adolf key or R4306 key run on R4282; no rendering of R4282 anywhere in the repo (grep 4282/riksarkiv: only that folder, README, goertz1717 mention). Clone aaymeloglu/unsolved-ciphers HEAD d2800bb2: 4282/4284/4306 appear only in catalogue/decode-records.jsonl and decode-catalog.csv (all `Non-decrypted`, no cleartext/plaintext cell; 4284 "Cleartext: Latin"), CATALOGUE.md and decode-ranked.md ("nothing: DECODE holds no image for either" -- no key run). Clones deleted after reading.
- (c) Neighbours: **not found** (one unreachable). DECODE login-free cache sources/decode/ (grep only, no login): 4282 and 4284 `Non-decrypted`; 4283 is a BnF item (Francais 3138 f.66, Decrypted, French, not Riksarkivet); **4280 and 4281 are Key records (Chifferklaver lada II:111, II:112, 3 and 8 pages, 1600-1699), the shelf neighbours of II:113** -- they sit among the 70 key records Bourdeau fetched (R4259-R4329, images git-ignored, not on our disk) and are untried against R4282; 4303 (II:130) and 4118/4119 (II:16/17, 1610, plaintext Latin) are `Decrypted` Riksarkivet Chifferklaver records, a different letter each, not R4282. No fetched record page for 4282 on disk (aaymeloglu: DECODE has no image). Riksarkivet catalogue sok.riksarkivet.se/?Sokord=Chifferklaver: **unreachable** (redirect to /captcha, 1 request, no retry); no clear copy bound with the volume could be checked.
- (d) Recipient-side editions: **not found**. The item has no named sender/recipient (catalogue #207), only the R4284 note "Legat ... till L. Camerarius bref for 1628". Searches 3 Oct 2026: archive.org advancedsearch full text, exact phrases "futurus status dubitatur", "tractatus magnas admodum", "Mittatur nobis responsum": 0 / 0 / 0 items. Web search of the same phrases with Oxenstierna 1628: no hit (classical Latin and Languet pages only). AOSB (Rikskansleren Axel Oxenstiernas skrifter och brefvexling, archive.org rikskanslerenax01akadgoog, rikskanslerenax01styfgoog; Riksarkivet's AOSB pages sok.riksarkivet.se/oxenstierna and /dokument/oxenstierna/03559/3559t.xml) located as the edition to search; its volumes were not read page by page (full-text OCR phrase search only), and the Camerarius letters (412 extant to Oxenstierna 1623-48) are not fully printed there, so absence is a search result only.

Result: not found-solved -- stays open (status word unchanged). Rule 10: a search result, not a novelty verdict.

Next cheap test: from the Escalation list, run the neighbouring key records R4280/R4281 (II:111, II:112) -- and then the other untried Chifferklaver key records -- against R4282 as a crib key (known-keys, remaining); needs their images from DECODE/Bourdeau's decode/keys (~$2-3 once images are on disk).

Requests per host (this subagent): github.com 2 (clones); sok.riksarkivet.se 3 (redirect, captcha page, /oxenstierna 200); archive.org 6 (advancedsearch, 3 phrases twice); web search 2 queries.

## FT4: shelf-neighbour key records R4280/R4281 vs R4282 (3 Oct 2026, account-4)

Brief: parent dispatch FT4-riksarkivet-r4282-1628 (first cheap test named by GF4-BATCH4's Premise check: "key
records R4280/R4281 as crib keys vs R4282"). Intake gate run first: `riksarkivet-r4282-1628: open (line 1) --
edition/page or full-text-search citation found within 6 lines` (exit 0).

**Metadata (login-free, already on disk):** `sources/decode/keys-all-2026-09-28.tsv` -- 4280 Key, N/A,
Chifferklaver_låda_II_111, 1600-1699, 3 pages; 4281 Key, N/A, Chifferklaver_låda_II_112, 1600-1699, 8 pages. The
record pages, read after login, give 4280 "Cipher Type: Simple substitution, Homophonic substitution, Nomenclatures;
Symbol Sets: Numerical" and 4281 "Cipher Type: Simple substitution, Nomenclatures; Symbol Sets: Numerical"; no
language, date or comment filled in either.

**Images:** one DECODE browser login (`tools/decode_browser_login.js 4280 ... --fetch-page RecordsView/4281
--listen`). DECODE served the **full-size page PDFs** for both records (11 files, 0.9-2.5 MB each, real scans, not
the `forbidden.png` placeholder). Rendered at 110 dpi to `keys_r4280_r4281/*.jpg`; URLs, sizes and sha1 of the
source PDFs in `keys_r4280_r4281/manifest.json` (PDFs not committed; re-fetch needs a login). The record HTML pages
stayed in the scratchpad (they carry the account name).

**What the keys are (by eye, from the images; not transcribed -- not needed, see below):**
- R4280 (II:111), p.1: a homophonic letter table, each letter A-Z (with the Swedish vowels) given 2-3 two-digit
  numbers (A 20 41 71, B 8 14 48, C 18 39 47, D 19 49 29, E 9 12 74, ... to Z 34 59 64); "Quiescentes 1 2 3 4 5 6
  7 item a 77 ad 308 inclusive" (nulls); a nomenclator 308-331 in Swedish (S. K. Maj:t, Sverige, Soldatesqua,
  Rijksdrotset, Rijksmarsk, Fältmarskalk Wrangel, Lifland, ...). Foot note "Från Skyttes arkiv" (reading M). Pp.2-3:
  a docket ("... under Miscellanea ... Chiffer"), a numeric column table, a cover.
- R4281 (II:112), 8 pp.: an alphabetical word nomenclator (A, B, C ... S headings, word -> 4-digit code, roughly
  1100-1440 where legible at this resolution) -- numbers only on the cipher side.

**Overlap check (the brief's stop condition): none.** R4282's ciphertext is Latin letter shapes plus special signs
(lambda, delta, boxed square, epsilon, phi, alpha, mu) with single digits 3 4 5 7 8 used as letter-like signs
inside words (`k448EkM5b`), 1,094 signs, K=34. Both keys encipher into multi-digit numbers (2-digit letter codes,
3-digit nulls/names, 4-digit words); no sign of R4282's alphabet appears on their cipher side, and R4282 has no
multi-digit number groups. Applying either key with `tools/decode_key.py` would decode nothing, so per the brief no
key file, no decode, no shuffled-key control and no judge were run -- this is "no overlap, not tested", not a
negative on R4282 (rule 3: a control on a key that covers 0 signs could not differ from the target). Grades: none
claimed (rule 4). No HYPOTHESES.md family row (nothing was run against the target).

**Suggestion (not this brief, rule 7):** R4284 (DECODE 4284, the numeric homophonic letter on II:114, 108 distinct
values, range 2-1493 in Bourdeau's transcription) is numeric, and its range spans both R4280's 2-digit letter codes
and R4281's 4-digit word codes. Neither key is recorded as tried against R4284 (Bourdeau tried R4310 and R4296
only). Next: transcribe R4280 p.1 (one page, 2 passes + 1 reconciliation) and apply it to R4284 against a
shuffled-key control, ~$3. That is a different target folder's test; the parent decides.

Status word unchanged (`open`). Requests: de-crypt.org 14 (login page + submit, RecordsView/4280, RecordsView/4281,
11 PDFs), 1.6 s apart, one login; no other host.

## GAPS-riksarkivet-r4282-1628 (3 Oct 2026, account-4)

Verdict step run: "filter the 66 key records by Symbol Sets, ~$1". Intake gate first:
`riksarkivet-r4282-1628: open (line 1) -- edition/page or full-text-search citation found within 6 lines` (exit 0).

**Filter (login-free).** DECODE's RecordsView page carries Symbol Sets and Cipher Type without a login (the FT4
section read them after login; not needed). The Riksarkivet Chifferklaver key records in the R4259-R4329 range on
disk (`sources/decode/keys-all-2026-09-28-merged.tsv`) are 56, not 66 (the "70" of the Premise check counted
Bourdeau's fetched range, which includes cipher records); 54 after R4280/R4281. Fetched all 54 RecordsView pages
(scratchpad, not committed). Symbol Sets: 38 Numerical only; 16 carry Alphabet and/or Graphic signs --
4263 (II:100, 1650-), 4275 (II:108, 1634-), 4293 (II:120), 4295 (II:122), 4297 (II:124), 4298 (II:125, 1630-39),
4299 (II:126, 1630-39), 4305 (II:132, 1630-), 4307 (II:134), 4308 (II:135), 4309 (II:136), 4312 (II:139, 1630-99),
4322 (II:149), 4323 (II:150), 4327 (II:154, **1620-1629**), 4329 (II:156). Only 4307 and 4327 carry all three sets
(Graphic signs + Alphabet + Numerical), R4282's own profile (letter shapes, special signs, single digits); 4327 is
the only one dated to R4282's decade. The "notes" fields are empty on all 54.

**Candidate check (one login, two vision calls).** One `tools/decode_browser_login.js` run (after the container's
certutil fix; the first try failed at page load with ERR_CERT_AUTHORITY_INVALID, before any login) served
full-size PDFs for 4327 (3 pp.) and 4307 (3 of 4 pp., --max-files cap). 80 dpi renders and a 300 dpi crop of the
4327 sign column in `keys_r4327_r4307/` (manifest.json). Vision call 1: the 4327 sheet -- p.1 is a name nomenclator
1-40 / 101-140 (Polen, Commissarier, Wrangel, ...) and a letter table a-z, each letter two 2-digit numbers and one
sign; p.4 a modern docket "Kriget med Polen under senare hälften av 1620-talet. Axel Oxenstierna - Filip Sadler"
(reading M). Vision call 2: the sign column at 300 dpi, read (all M): a ε, b barred ω, c δ, d λ, e "6.5", f V,
g β, h x, i ς, k α, l μ, m T, n 1, o Q-like, p X, q γ/r, r Z, s ό, t stacked curl, u H, w crossed loop, x θ, y o,
z ω. 4307 was not examined by eye (vision budget spent on 4327's column).

**Overlap: real, partial.** Seven of the key's signs match R4282 sign classes in Bourdeau's notation: E=ε->a,
L=λ->d, x->h, A=α->k, M=μ->l, T->m (Bourdeau's T is Δ; the key's m-sign is T-shaped and its c-sign δ-shaped, so
this pairing is itself M), o->y. They cover 214 of R4282's 1,110 transcribed signs. Ambiguous pairs (5, r/Z, 1, 8)
left out.

**Test (rule 3).** `scripts/key4327_overlap.py` (--check exits 0; `key4327_overlap.json`). Statistic: mean la18
Latin unigram log-probability of the letters the real key gives those 214 tokens. Controls that can differ from the
target on this statistic: (a) the same seven letters permuted among the seven signs, 2000 draws; (b) seven distinct
random Latin letters, 2000 draws.

| | mean logp | control mean | control p95 | share of control >= real |
|---|---|---|---|---|
| real key 4327 | -4.357 | | | |
| (a) permuted values | | -4.399 | -3.716 | 0.50 |
| (b) random letters | | -3.744 | -2.904 | 0.84 |

The real assignment sits at the permutation median and below most random keys: μ (66 tokens) -> l and λ (47) -> d
are plausible, but α (20) -> k and o (36) -> y give Latin's two rarest letters to frequent R4282 signs. Read: the
4327 sign column does not decode R4282's shared signs; any common sign shapes are the period's stock of
Greek-letter cipher signs, not a shared key. Grades: none claimed (rule 4; no reading). Conditional on Bourdeau's
single-pass transcription and on an M-grade eye read of the key column (rule 2). Not a negative on the other 15
candidates.

Requests: de-crypt.org 54 RecordsView (login-free, 1.6 s apart) + 2 ImagesList (login-free, empty answer) + 1 login
run (login page, submit, RecordsView/4327, RecordsView/4307, 12 attachments; 1.7 s apart) = about 72; no other host.

## GAPS2-riksarkivet-r4282-1628 (3 Oct 2026, account-4)

Verdict step run: "one vision call on key 4307's fetched pages for sign overlap with R4282, ~$1". Intake gate:
`riksarkivet-r4282-1628: open (line 1) -- edition/page or full-text-search citation found within 6 lines` (exit 0).

**What key record 4307 (Chifferklaver II:134) is (vision call 1, pp. 1-3 on disk at 80 dpi, all reading M).** p.1
(I25835): modern dockets, "Hartmann Drach(e) 160-? (a-g)", shelf note "II:105"(?), and "1680". p.2 (I25836):
"Catalogus für Hart. Drach", plain capitals A-Q as name codes for German imperial offices and persons (A Kaiser,
B Kayserin, C Geheimer Rath Collegium, D Reichs Vice Cantzler, K Barvitius, L Hegenmüller, N Reichshofrath Collegium,
P Catholischer Theil der Reichsstände, Q Dr Wackher ...). p.3 (I25837): a second name list, left column of signs
(R, B, T, V, W, K, Y, a Σ/C-like sign, a θ-like sign, Γ, Δ, an Ω-like sign, a hand/crown sign, a monogram, a cross,
P) for the Catholic league, the electors (Mainz, Trier, Cöln, Bayern, Pfalz, Brandenburg, Sachsen), and right column
numbers 1-19 for the house of Austria (Maximilian, Albrecht, Ferdinand, Leopold), the Reichshoffiscal, the Bohemian
and Hungarian estates. No letter alphabet on pp. 1-3: the record is a name nomenclator for Hartmann Drach's
imperial correspondence (German), not a letter key.

**Overlap with R4282: one sign class, not the commonest.** Of R4282's special signs (L=λ, T=Δ, B, E=ε, F=φ, A=α,
M=μ, D, G), only T=Δ appears on 4307 pp. 1-3, and there as a name code (10 of R4282's 1,110 tokens, 0.9%). R4282's
commonest signs (b 80, M 66, 7 63, k 61, q 53, 5 53, 4 51, L 47) are not covered; 4307's capitals A-Q are name
codes, not R4282's lowercase letter shapes. Overlap is below 4327's seven signs and does not cover the commonest,
so the brief's condition for the known-key test (la18 unigram, real vs permuted-value control) is not met and the
test was not run -- not a negative on 4307, an inapplicable test on pp. 1-3.

**The fourth page.** Record 4307 carries a fourth image, I25838, never fetched: this job's one browser login
(`tools/decode_browser_login.js 4307 --max-files 6`) spent its file cap on pp. 1-3 and their thumbnails; a
login-free full-size request returned DECODE's `forbidden.png` placeholder (sha1 035489a0...). Its login-free
thumbnail (141x200 px, vision call 2) shows a strip with a short name list, then three rows that look like a
letter table (letters with a sign or number under each), and a second leaf with a numbered name list. Too small to
read; this may be 4307's letter alphabet. No second login was made (one login per session).

Grades: none claimed (rule 4; no reading). Requests: de-crypt.org about 11 (one login run: login page, submit,
RecordsView/4307, 6 files, 1.7 s apart; then 2 login-free filesrv requests, 2 s apart); no other host.

## Remaining gaps (FT4, 3 Oct 2026; updated GAPS, 3 Oct 2026; GAPS2, 3 Oct 2026)
Read so far: 0 of 1,094 signs (no key or crib has read any sign; bRIK, RIK-CRIBS, FT4, GAPS)
- R4282 whole letter - blocker: not-attempted; Symbol Sets filter done (GAPS, 3 Oct 2026): 16 of 54 key records carry letter/graphic signs; 4327 tested on its 7 shared signs, no fit vs control (median of 2000 permutations); 4307 pp. 1-3 (GAPS2, 3 Oct 2026) are a German name nomenclator sharing one sign class (Δ, 10 tokens) with R4282, test not applicable; 4307 p.4 (I25838) shows a possible letter table in its thumbnail, full size not fetched; next: one DECODE login fetching IMG_R4307_I25838_P full size and one vision call on its letter table for sign overlap with R4282, ~$1
- transcription reliability - blocker: not-attempted; single-pass Bourdeau transcription, no measured error; next: second blind pass on R4282's two pages via tools/iiif_lines.py --image (DECODE full-size served to this account, FT4), ~$5

## Escalation (FT4, 3 Oct 2026; updated GAPS, 3 Oct 2026)
- [x] siblings: Bourdeau's 14-record bundle read in full (check-solved, 26 Sept 2026)
- [x] clear-pages: R4282's four clear-Latin phrases dragged as cribs (RIK-CRIBS, 2 Oct 2026), negative at resolution
- [ ] known-keys: R4284 crib leaf (bRIK), R4280/R4281 (FT4, no overlap), 4327 (GAPS, partial overlap, no fit vs control), 4307 pp. 1-3 (GAPS2, name nomenclator, one shared sign) done; 4307 p.4 (possible letter table) and 14 other letter/graphic-sign key records left
- [ ] print: AOSB series II and Camerarius letters only phrase-searched (IA full text), not read page by page
- [ ] key-rebuild: no partial key exists to rebuild from; homophonic annealing after a second transcription pass
- [ ] image-check: second blind pass on the two R4282 pages and the R4284 key-test leaf
- [n/a] retry: no earlier attempt failed on a fixable setting
Verdict: keep going: 2 internal gaps; cheapest next: one DECODE login fetching key 4307's fourth page (IMG_R4307_I25838_P) full size and one vision call on its letter table for sign overlap with R4282, ~$1
