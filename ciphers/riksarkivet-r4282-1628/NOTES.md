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

## GAPS3-riksarkivet-r4282-1628 (3 Oct 2026, account-4)

Verdict step run: "one DECODE login fetching key 4307's fourth page (IMG_R4307_I25838_P) full size and one vision
call on its letter table for sign overlap with R4282, ~$1". Intake gate:
`riksarkivet-r4282-1628: open (line 1) -- edition/page or full-text-search citation found within 6 lines` (exit 0).

**Fetch.** One `tools/decode_browser_login.js 4307 --fetch .../filesrv/?file=IMG_R4307_I25838_P.pdf --max-files 1`
run (first attempt died at page load on ERR_CERT_AUTHORITY_INVALID before any login; certutil fix applied, then the
one login). Served a real one-page PDF (1,905,112 bytes, sha1 f5ed54b9..., not the forbidden.png placeholder):
the full-size page is available to this account with an explicit --fetch. 80 dpi render in `keys_r4327_r4307/`.

**What p.4 is (vision call 1, 200 dpi, all reading M).** Left strip: name codes 20-24 continuing p.3 (Statt ...,
Reichstag(?), ... "Rottenburg an der Tauber"), then the heading "Dis verkehrte Alphabet kann auch nach aller
notdurfft gebraucht werden", a three-row table (plain letter above, one cipher letter-shape below, ten columns per
row), a docket "Cathalogg so Hartman Drach den 13. ... uberschickt" and "Correspondentz mit Drach". Right leaf: a
second name list 18-32 (Reichstag, Catholische Union, Eps Herbipolensis, Bambergensis, Nuncius Apostolicus
Caesareus, Nuncius Coloniensis, Summus Pontifex, Rex Hispaniae, Orator Hispanicus, Rex Franciae, R. Angliae,
Poloniae, Daniae, Sueciae, Magdeburgisch Administrator). So record 4307's letter key is a monoalphabetic
"reversed alphabet" whose cipher signs are ordinary Latin letter shapes (read: a q, b e, d x, f c and A, g f,
i g, m h, n i, o r, p k, q t, r u, s 3/Z, x n, z D; first-row and third-row alignment uncertain, conflicting
cells s and d dropped). No digits and no Greek signs.

**Overlap: real, larger than 4327's.** 16 cipher shapes with a single value in that read occur in R4282, covering
456 of 1,110 tokens (4327: 7 signs, 214 tokens). Of R4282's commonest eight (b 80, M 66, 7 63, k 61, q 53, 5 53,
4 51, L 47) only k and q are covered; R4282's digits 4 5 7 8 and its Greek signs (L M F E T) have no cell in this
table, so a 23-cell simple alphabet cannot be R4282's whole key (38 sign classes).

**Test (rule 3).** `scripts/key4307p4_overlap.py` (--check exits 0; `key4307p4_overlap.json`), same statistic and
controls as the 4327 test: mean la18 Latin unigram log-probability of the letters the key gives the covered tokens;
(a) the same 16 values permuted among the 16 signs, (b) 16 distinct random Latin letters, 2000 draws each.

| | mean logp | control mean | control p95 | share of control >= real |
|---|---|---|---|---|
| real key 4307 p.4 | -3.617 | | | |
| (a) permuted values | | -3.553 | -3.298 | 0.65 |
| (b) random letters | | -3.747 | -3.287 | 0.33 |

The real assignment is below the permutation mean: k (61) -> p, t (44) -> q and n (39) -> x give rare Latin letters
to frequent R4282 signs. Read: key 4307's reversed alphabet does not decode R4282's shared letter shapes; the
overlap is the shared stock of Latin letter shapes, not a shared key. Grades: none claimed (rule 4; no reading).
Conditional on Bourdeau's single-pass transcription and on an M-grade eye read of a German-hand table whose row
alignment is itself uncertain (rule 2). Not a negative on the other 14 letter/graphic-sign key records.

Requests: de-crypt.org 3 (login page, submit + RecordsView/4307, one filesrv PDF; 1.7 s apart), one login; no other
host. Vision calls: 1.

## GAPS4-riksarkivet-r4282-1628 (3 Oct 2026, account-4)

Verdict step run: "fetch the 1630s-dated letter/graphic-sign key records 4298 and 4299 (Chifferklaver II:125-126) full
size in one DECODE login and one vision call for sign overlap with R4282, ~$1". Intake gate:
`riksarkivet-r4282-1628: open (line 1) -- edition/page or full-text-search citation found within 6 lines` (exit 0).

**Fetch.** One `tools/decode_browser_login.js 4298 --fetch-page .../RecordsView/4299 --listen` run (one login; both
RecordsView pages read for file names, then four explicit filesrv gets). DECODE metadata for both: Key, 1630-1639,
"Simple substitution, Nomenclatures", Symbol Sets "Graphic signs, Numerical". All four PDFs served full size (real
one-page PDFs, sha1s in `keys_r4298_r4299/manifest.json`; 80 dpi renders beside it, PDFs not committed).

**What 4298 and 4299 are (vision call 1: 4298 p.1 + 4299 at 200 dpi; vision call 2: 4298 pp.2-3; all reading M).**
The same key in two copies. 4298 p.2 is a modern archive cover: "1630-talet, 2 ex, Polsk klav med Sigismund
Gyllenstierna (Nyckelord: Wilman)", shelf "II:98"(?); 4298 p.3 is the endorsed outer leaf ("Von ... [Gyllen]stierna(?)
Ziffer"). The key (4298 p.1, 4299) is Polish: a reciprocal keyword alphabet, top row "W i l m a n b c d e f g" over
bottom row "h k o p q r s t u x y z" (each letter swaps with the one in the other row: w-h, i-k, l-o, m-p, a-q, n-r,
b-s, c-t, d-u, e-x, f-y, g-z); Roman numerals II-XXIIII for names and offices (Xiaze II, Krol III, Cesarz IIII,
Krolewiec V, Papiez VI ... Polska XII, Imperium XIII ... Katolicy XXII, Ewangelicy XXIII); Arabic 15-44 for persons,
places and months (Tylli XXIV, Gustaw 15, Bawarczyk 16, Saski 17, Brandeburczyk 18, Oxenstern 19, Warszawa 20,
Krakow 21 ... Wilman 27, Januarius 29 ... December 40, Kazanowski 41 ... K. Wladislaw 44); marginal additions 45-49
(Der Herr Feldherr(?), Gorny(?), Woiewod Derpt, Riga, Stockholm(?)).

**Overlap with R4282: letter shapes only, not the commonest signs.** The key's cipher alphabet is the Latin alphabet
itself, so all 19 lowercase Latin signs of R4282 (660 of 1,110 tokens) have a cell -- a trivial overlap, shared with
any Latin-letter key. Of R4282's commonest eight (b 80, M 66, 7 63, k 61, q 53, 5 53, 4 51, L 47) only b, k and q are
covered; R4282's single digits 4 5 7 8 (199 tokens) have no single-digit cell (the key's Arabic codes are two-digit
name codes 15-49) and its Greek signs (M L F E T, 157 tokens) have none. The brief's condition for the known-key test
(overlap covering the commonest signs) is not met, so the la18 test was not run: an inapplicable test, not a
negative on this key. Language also argues against: the key's names are Polish and its nomenclator is for Polish
affairs of the 1630s (Wladyslaw IV), while R4282's clear phrases are Latin (RIK-CRIBS).
Beside GAPS3: key 4307 p.4 shared 16 signs / 456 tokens and scored real -3.617 vs permuted mean -3.553 (p95 -3.298),
no read; 4298/4299 share 19 letter shapes / 660 tokens but none of R4282's digits or Greek signs, so no test.

Grades: none claimed (rule 4; no reading). Requests: de-crypt.org about 9 (login page, submit, RecordsView/4298,
RecordsView/4299, one auto-fetched thumbnail, four filesrv PDFs; 1.5-1.8 s apart), one login; no other host. Vision calls: 2.

## GAPS27-riksarkivet-r4282-1628 (3 Oct 2026, account-4)

Verdict step run: "fetch the 1630s-dated letter/graphic-sign key records 4275 and 4305 full size in one DECODE login
and one vision call for sign overlap with R4282, ~$1". Intake gate:
`riksarkivet-r4282-1628: open (line 1) -- edition/page or full-text-search citation found within 6 lines` (exit 0).

**Fetch.** One `tools/decode_browser_login.js 4275 --fetch-page .../RecordsView/4305 --guess-fullsize --max-files 24`
run (first attempt died at page load on ERR_CERT_AUTHORITY_INVALID before any login; NSS database rebuilt and the
proxy CA added, then the one login). Served full size: all 7 pages of 4275 and page 1 of 4305's 4 (real PDFs, sha1s
in `keys_r4275_r4305/manifest.json`, 80 dpi renders beside it, PDFs not committed). 4305 pp. 2-4 (I25827-I25829)
were not fetched: the file cap was spent on 4275's thumbnails and --guess-fullsize .png guesses (each a 100x100
placeholder, one sha1) before them. No second login. Metadata: 4275 "Simple substitution, Homophonic substitution,
Nomenclatures", Graphic signs + Numerical, 7 pp.; 4305 "Simple substitution, Nomenclatures", Alphabet + Numerical, 4 pp.

**What they are (contact sheet of all 8 pages at 80 dpi, then one 200 dpi crop of 4275's letter table; all reading
M).** 4305 p.1 is a modern cover, "Brandenstein 1630-"; its key pages are among the three not fetched. 4275 is a
German key: heading "Zu Meynz gefundene feindl. Ziffern Ao 1634 in Julio durch Herr Nicodemi(?)", cover "Mainz
1634 ... Chiffer ... med ... Hofmeister ... Aschaffenburg", nomenclator 200-331 of German offices and persons
(Kaiser, Könige, Kurfürsten, ...), with the letter table repeated on two later pages. The letter table gives each
letter one sign and one 2-digit number: a W 12, b theta 14, c inverted V 21, d 0/o 30, e U/upsilon 22, f square
bracket 26, g y 35, h boxed square 27, i # 38, k up-arrow 29, l pi-like 25, m Omega 13, n omega 24, o 1 31, p I 23,
q barred inverted triangle 32, r reversed epsilon 20, s + 33, t d-like 28, v Delta 15, w barred Z 37, x 9/rho 36,
y 8 34, z infinity 18.

**Overlap with R4282: small.** Four key signs match R4282 classes without doubt: T=Delta -> v, B=boxed square -> h,
8 -> y, o -> d (81 of 1,110 tokens). Three more are only ambiguous shape pairs: L=lambda vs the key's inverted V (c),
E=epsilon vs its reversed epsilon (r), u vs its U-shape (e) (76 more tokens). None of R4282's commonest eight
(b 80, M 66, 7 63, k 61, q 53, 5 53, 4 51, L 47) is covered except L in the ambiguous set; R4282's digits 4 5 7 and
signs M, F, A, D have no cell.

**Test (rule 3).** `scripts/key4275_overlap.py` (--check exits 0; `key4275_overlap.json`), same statistic and controls
as GAPS/GAPS3: mean la18 Latin unigram log-probability of the letters the key gives the covered tokens; (a) the same
values permuted among the signs, (b) distinct random Latin letters, 2000 draws each. Both controls can differ from
the real key on this statistic.

| | covered tokens | real mean logp | (a) perm mean / p95 / share >= real | (b) random mean / p95 / share >= real |
|---|---|---|---|---|
| strict, 4 signs | 81 | -4.792 | -4.467 / -3.371 / 0.66 | -3.765 / -2.660 / 0.87 |
| wide, 7 signs | 157 | -3.880 | -3.707 / -3.080 / 0.67 | -3.751 / -2.907 / 0.62 |

The real assignment is below both control means on both sets: o (36) -> d and 8 (32) -> y give rare Latin letters to
frequent R4282 signs. Read: key 4275 does not decode R4282's shared signs; beside 4327 (7 signs / 214 tokens, real
-4.357 vs permuted mean -4.399) and 4307 p.4 (16 / 456, -3.617 vs -3.553), the overlap is again the period's stock
of Greek-letter and symbol cipher signs, not a shared key. Grades: none claimed (rule 4; no reading). Conditional on
Bourdeau's single-pass transcription and an M-grade eye read of the table (rule 2). 4305 untested (key pages not
fetched).

Requests: de-crypt.org 27 (login page, submit, RecordsView/4275, RecordsView/4305, 24 files; 1.7 s apart), one
login; no other host. Vision calls: 2 (contact sheet, one table crop).

## GAPS30-riksarkivet-r4282-1628 (3 Oct 2026, account-4)

Verdict step run: "one DECODE login fetching key 4305 pp.2-4 (IMG_R4305_I25827-I25829_P.pdf, explicit --fetch) and 4263
full size, one vision call for sign overlap with R4282, ~$1". Intake gate: `riksarkivet-r4282-1628: open (line 1) --
edition/page or full-text-search citation found within 6 lines` (exit 0).

**Fetch.** First run died at page load on ERR_CERT_AUTHORITY_INVALID before any login (same as GAPS27); proxy CA added
to the NSS database, then one `tools/decode_browser_login.js 4263 ... --fetch <4305 pp.2-4> --max-files 3 --listen`
login. The record page gave 4263's four image ids (I25581-I25584); their `_P.pdf` names were then fetched through the
listener in the same login. All 7 real PDFs (sha1s in `keys_r4305_r4263/manifest.json`, 80 dpi renders beside it).

**What they are (one contact sheet of all 7 pages at 80 dpi, one 200 dpi crop of 4263's letter table; all reading M).**
4305 pp.2-4: "CLAVIS ..." a name nomenclator only, each name coded by a capital letter, doubled or tripled letters, or
a letter + x / + z (A Land Pommern, C Dux Pomeraniae, Y Rex Sueciae, TZ Rex Polon., HX Rex Galliae, ...); no cipher
alphabet, no digit or graphic sign: no cell for R4282's digits or Greek signs, test inapplicable (as 4298/4299).
4263 (cover "1650- Sternberg ...", heading "... und ...s Ziffern"; I25582 cover, I25583 blank outer leaf, I25584 a
smaller copy of the same table): each letter has one 2-digit number and one sign -- a v, b angle, c x, d Pi-like,
e L-like, f T, g theta, h inverted V, i inverted Delta, k open bracket, l U, m square, n barred circle, o epsilon-like
E, p barred U, q //, r crossed I, s circled cross, t Z, u D, w barred 8, x looped delta, y x-like, z III -- and a
reverse number list whose single digits are 4 g, 6 o, 8 d (2 and 3 struck).

**Overlap with R4282.** Strict (shape without doubt): B=square -> m, E -> o, x -> c, plus R4282's digits 4 -> g and
8 -> d from the key's own number list (5 signs, 121 of 1,110 tokens). Wide adds four ambiguous pairs: L=lambda vs
the key's inverted V (h), T=Delta vs its inverted Delta (i), D (looped d) vs its looped delta (x), u vs its U (l)
(9 signs, 221 tokens). R4282's 7, 5, M, k, q (commonest after b) have no cell.

**Test (rule 3).** `scripts/key4263_overlap.py` (--check exits 0; `key4263_overlap.json`), same statistic and controls
as GAPS/GAPS3/GAPS27: mean la18 Latin unigram log-probability of the letters the key gives the covered tokens; (a) the
same values permuted among the signs, (b) distinct random Latin letters, 2000 draws each; both controls vary on this
statistic.

| | covered tokens | real mean logp | (a) perm mean / p95 / share >= real | (b) random mean / p95 / share >= real |
|---|---|---|---|---|
| strict, 5 signs | 121 | -3.746 | -3.358 / -3.059 / 0.992 | -3.753 / -2.758 / 0.557 |
| wide, 9 signs | 221 | -4.017 | -3.550 / -3.195 / 0.990 | -3.759 / -3.035 / 0.698 |

The real assignment sits below 99% of its own permutations on both sets (4 -> g with 51 tokens and 8 -> d with 32
give middling-to-rare letters to frequent R4282 signs; wide adds L -> h, 47 tokens): key 4263 does not decode R4282's
shared signs. Read: like 4327, 4307 p.4 and 4275, the overlap is the period's stock of square/Greek/Latin-letter signs,
not a shared key. Grades: none claimed (rule 4; no reading). Conditional on Bourdeau's single-pass transcription and an
M-grade eye read of the table (rule 2).

Requests: de-crypt.org 9 (login page, submit, RecordsView/4263, 3 + 4 PDFs; 1.7 s apart), one login; no other host.
Vision calls: 2 image reads (contact sheet, one table crop).

## GAPS32-riksarkivet-r4282-1628 (3 Oct 2026, account-4)

Verdict step run: "one DECODE login fetching the 9 remaining sign keys (4293 4295 4297 4308 4309 4312 4322 4323 4329) +
same test". Intake gate: `riksarkivet-r4282-1628: open (line 1) -- edition/page or full-text-search citation found within
6 lines` (exit 0).

**Fetch.** Proxy CA added to a fresh NSS database (libnss3-tools installed first), then one
`tools/decode_browser_login.js 4293 ... --fetch-page RecordsView/<other 8> --listen` login; the 31 `_P.pdf` names were
read from the nine record pages' thumbnails and fetched through the listener in the same login. All 31 are real PDFs
(sha1s in `keys_r4293_r4329/manifest.json`; 80 dpi renders of the 8 letter-table pages beside it; PDFs and record pages
not committed). Symbol Sets on the record pages: 4293 Graphic+Numerical, 4295 Graphic, 4297 Graphic+Alphabet, 4308
Graphic+Alphabet, 4309 Alphabet+Numerical, 4312 Alphabet, 4322 Graphic+Numerical, 4323 Alphabet+Numerical, 4329 Graphic.

**What they are (two contact sheets of all 31 pages at 80 dpi, three stacks of 170 dpi table crops; all reading M).**
- 4293 (1 p.): one graphic-sign alphabet written three times (runic/bar shapes); v = lambda, z = 3, y = E-shape; the
  o/p/q column has an 8.
- 4295 (1 p.): numeric homophones a 3/4/5, b 6, c 7, d 8, e 9/10/11 ... z 40; graphic signs for names only
  (Schweden, Venedig, Italie ...); below, a keyword alphabet "erlach..." with digits, and a struck reciprocal
  alphabet "erlacbdfgik / mnopqstuwxyz".
- 4297 (1 slip, "4.3"): a graphic alphabet; g = lambda, n = x, o = open square, c = a 7-like hook, x = S.
- 4308 (3 pp.: cover "Bröms..."; modern wrapper; table): a = lambda, b = crossed 4, c 9-like, d gamma, ... k looped
  delta, l x, m x with ring, n i-shape, o H, ... u B, w 6, y L.
- 4309 (2 pp.): "Alphabet" leaf whose cipher row is the 4275 Mainz alphabet (W, 8/theta, inverted V, 0, ... boxed
  square h, # i, ... Delta, barred Z, 9, 8, infinity): same key, already tested (GAPS27), not re-tested.
- 4312 (3 pp.): numeric homophonic table (1-1000) with 13 name letters (Z Oxenstierna, N Fürst Ludwig von Anhalt, Y
  Magdeburg, ...); single-digit values D 9, K 7, L 8, O 1, P 5, Q 4, S 3, V 6, W 2.
- 4322 (3 pp.): a German/Latin word list (Schweden, Kaiser, ... with Latin glosses) with no alphabet or sign column
  seen at 80 dpi: skipped and logged, test inapplicable.
- 4323 (12 pp.): a numbered name nomenclator 1-383 (Dutch: "Namen van ... steden", "Poolen", ...) and a letter table
  384-407 of astrological/planet signs; its only sign shared with R4282 is a lambda-like z: one shared sign, where a
  permutation control cannot vary (rule 3 non-test); not tested.
- 4329 (5 pp.): letters A-Z = two-digit numbers 20-43 plus name lists: no single digit or graphic cell, test
  inapplicable.

**Test (rule 3).** `scripts/keys9_overlap.py` (--check exits 0; `keys9_overlap.json`), same statistic and controls as
GAPS/GAPS3/GAPS27/GAPS30: mean la18 Latin unigram log-probability of the letters the key gives the covered tokens; (a)
the same values permuted among the signs, (b) distinct random Latin letters, 2000 draws each; both controls vary on
this statistic. 4295's struck reciprocal alphabet is applied to R4282's Latin-letter shapes as letters.

| key / set | signs | covered tokens | real mean logp | (a) perm mean / p95 / share >= real | (b) random mean / p95 / share >= real |
|---|---|---|---|---|---|
| 4293 strict | 3 | 74 | -4.079 | -5.394 / -4.079 / 0.166 | -3.737 / -2.593 / 0.723 |
| 4293 wide | 5 | 113 | -3.831 | -4.464 / -3.477 / 0.248 | -3.742 / -2.767 / 0.605 |
| 4295 numeric digits | 5 | 213 | -2.834 | -2.814 / -2.654 / 0.651 | -3.756 / -2.801 / 0.058 |
| 4295 reciprocal Latin (struck) | 22 | 660 | -3.542 | -3.576 / -3.248 / 0.442 | -3.753 / -3.393 / 0.178 |
| 4297 strict | 3 | 72 | -3.855 | -3.303 / -2.775 / 0.854 | -3.780 / -2.555 / 0.615 |
| 4297 wide | 5 | 147 | -3.651 | -3.602 / -3.062 / 0.524 | -3.764 / -2.748 / 0.518 |
| 4308 strict | 5 | 136 | -3.195 | -2.895 / -2.528 / 0.886 | -3.752 / -2.745 / 0.262 |
| 4308 wide | 8 | 252 | -3.486 | -3.409 / -2.928 / 0.560 | -3.752 / -3.012 / 0.329 |
| 4312 numeric digits | 5 | 213 | -4.672 | -4.274 / -3.756 / 0.970 | -3.753 / -2.815 / 0.909 |

No set reaches its own permutation p95 (closest: 4293 strict at 0.166 of permutations >= real, but 3 signs give only
6 distinct permutations). 4295's digits beat most random draws (0.058) only because three of the five digits carry
the frequent letter a; their own permutation, which keeps those values, does as well (0.651). Read: none of the nine
decodes R4282's shared signs; with 4327, 4307, 4298/4299, 4275, 4305 and 4263, all 16 letter/graphic-sign key records
of the Chifferklaver II set are now checked, and the overlaps are the period's stock of lambda/square/digit signs,
not a shared key. Grades: none claimed (rule 4; no reading). Conditional on Bourdeau's single-pass transcription and
M-grade eye reads of the tables (rule 2).

Requests: de-crypt.org 42 (login page, submit, 9 RecordsView pages, 31 PDFs; 1.7 s apart), one login; no other host.
Vision calls: 5 image reads (two contact sheets, three crop stacks).

## GAPS38-riksarkivet-r4282-1628 (3 Oct 2026, account-4)

Verdict step run: "second blind transcription pass on R4282's two pages". Intake gate: `riksarkivet-r4282-1628: open
(line 1) -- edition/page or full-text-search citation found within 6 lines` (exit 0).

**Images.** One DECODE login (`tools/decode_browser_login.js 4282 OUT --guess-fullsize --max-files 8`) served the
full-size page PDFs (real scans, not the forbidden placeholder): I25746 (2465x3609, letter p.1) and I25747 (4917x3895,
spread; cipher letter = left page). sha1s and URLs in `tx2/source_manifest.json`; PDFs not committed.

**Crops (pasted).** `python3 tools/iiif_lines.py --image p25746-000.jpg --region 800,40,1665,2800 --out tx2/crops
--prefix p1 --debug` -> 25 lines (pitch 109); `python3 tools/iiif_lines.py --image p25747-000.jpg --region
560,40,1900,950 --out tx2/crops --prefix p2 --debug` -> 7 lines (pitch 115). Same line counts as Bourdeau's pass;
debug overlay checked by eye.

**Pass B.** Two Opus subagent calls (one per page, line crops only, the sign inventory of Bourdeau's header given,
his transcription withheld): `tx2/passB_p1.tsv` 859 signs, `tx2/passB_p2.tsv` 230 signs, 31 graded M/L.
`tools/reconcile_passes.py tx2/passA_bourdeau.tsv tx2/passB_opus.tsv` (A = Bourdeau's single pass, as committed):
**agreement 1065/1102 = 96.6%, i.e. 3.4% two-reader disagreement** (37 columns), under the one-tenth line, so no
look-alike pass and no sorter rows were needed (TRANSCRIPTION.md). Worst line p1_L24 (0.60): see below.

**Reconciliation.** One Opus call settled the 37 columns from the crops (`tx2/rec/settled.tsv`): 14 to A, 23 to B,
0 other, 4 at L confidence (p1_L25 col 36 g/blot, p2_L01 col 2 struck f, p2_L04 col 16 blotted p under interlined m,
p2_L07 col 13 8/3). `tx2/apply_settled.py` (`--check` exits 0) writes **`tx2/ciphertext_reconciled.tsv`: 1,090 signs,
34 distinct, H 1049 / M 36 / L 5**. Against it Bourdeau's pass differs by 2.1% (1078/1101) and the blind pass by 1.3%
(1077/1091). These are err_2reader figures (two readers plus an image-settled reconciliation), not err_true: no
BENCHMARK-TX item exists for this hand.

**Findings that change the transcription.**
- p1_L24: the eight signs Bourdeau gave after the clear phrase ("E p t M S a b ?") are the clear Latin word
  *expensas*: the phrase reads "factum magnas admodum expensas" (reconciler, H), not "[tractatus magnas admodum]" plus
  cipher. Eight non-cipher signs leave the stream; this is the single largest correction.
- 13 single-sign omissions/additions and 16 sign identities settled (e.g. p1_L13 one 4 too many in Bourdeau's
  "45454t5"; p1_L01, L05 x2, L25 and p2_L07 signs he dropped).
- Open, not settled here: two scribal corrections (a blotted sign with a letter interlined above, p1_L05 col 33 and
  p2_L04 col 16) are recorded differently (corrected letter at p1_L05, struck sign + interlined m at p2_L04) and need
  one convention; p1_L25 cols 25-27 may be "M n n u" where both passes read "M n u" (reconciler's note, not changed).
  These three positions are the owner-sorter candidates if a later step needs them; they do not block annealing.

Grades: none claimed (rule 4; transcription only, no reading). Vision calls: 2 blind page passes + 1 reconciliation
(plus 3 preview/debug image views by the worker). Requests: de-crypt.org 9 (login page, submit, RecordsView/4282,
3 thumbnails, 3 full-size PDFs; 1.5 s apart), one login; no other host.

## GAPS42-riksarkivet-r4282-1628 (3 Oct 2026, account-4)

Verdict step run: "homophonic annealing on tx2/ciphertext_reconciled.tsv via family_run.py, matched control first".
Stream: `tx2/ciphertext_reconciled.tsv` as committed by GAPS38 (1,090 signs, K 34, clear phrases incl. "expensas"
already out), read by `tools/family_run.py --cipher` (32 line-messages). Spec copy with a `judge` block
(`"language": "la"`): `gaps42/spec_gaps42.json` (the shared `specs/` file is untouched).

**Design prior** (`python3 tools/design_prior.py gaps42/stream_space.txt --no-write`): 1090 tokens, 34 distinct;
multi-sign (homophonic/nomenclator/syllabary) d=0.06 (envelope 0.36) plausible; letter-for-letter d=0.31 plausible;
mixed d=1.04 plausible; code d=1.78 excluded; shuffled-input false-positive rate 0.060; advisory ranking
homophonic 0.06 < nomenclator 0.18 < alphabet substitution 0.31 < syllabary 0.56; nearest keys the fr4715 Mayenne
homophonic reconstructions (d=0.05-0.08). So the homophonic family is the design prior's first pick.

**Corpus (rule 3).** `tools/data/la18` (LANG_CORPORA "la"): Zaluski, *Epistolae historico-familiares*, Brunsberg
1709-1711, Polish crown-chancery Latin letters. Right language and genre (chancery letter Latin), about 80 years
later than the target (1628); no earlier Latin corpus is on disk. The control's numbers below show the corpus is
not what limits the solver on a control cut from the same corpus; it cannot show whether 1628 Swedish/German
chancery Latin differs enough to matter.

**Matched control** (homophonic, N 1,090, K 34, `--param profile=target` = the target's own sign-count profile,
`--measured-error 0.034`, gate 0.6; all rows in HYPOTHESES.md):

| injected error | seeds x restarts | control recovery mean (range) | best control scores |
|---|---|---|---|
| 0 (blind baseline) | 5 x 16 | 0.992 (0.981-0.998) | -2436 to -2476 |
| 0.034 (= measured two-reader rate) | 3 x 8 | 0.725 (0.261-0.960) | -2535 to -2908 |
| 0.034 | 5 x 16 (target run) | 0.948 (0.935-0.960) | -2535 to -2580 |
| 0.06 | 5 x 16 | 0.834 (0.518-0.924) | -2616 to -2836 |
| 0.10 | 5 x 16 | 0.620 (0.502-0.866) | -2768 to -2946 |

The control clears the gate at every level up to 10% injected error, three times the measured 3.4% (rule 3's
error-bracketing clause met). The 8-restart run's one stuck seed (0.261) recovers at 16 restarts.

**Target** (5 control seeds, then 16 restarts on the target): best score **-2950.3** (restarts -2950 to -3069);
decode `families/homophonic-1-profile=target,noise=0.034-gaps42targetla18.txt` reads no Latin (e.g.
"tstgnimideiuidarafiiuditstidacenpafi"); judge `FAIL language: score=-1.262, null_p99=-1.674, real_p05=-0.978,
real_median=-0.894, N=1090`. **Shuffled target** (same solver, sign order destroyed, `--shuffle-target 1/2`): best
scores -3156.5 and -3143.2, judge FAIL -1.338 both.

**Reading of the numbers.** The real stream scores about 200 points better than its own shuffles (it carries
sequential structure), but about 400 points worse than the control at the measured error and worse than every
control seed even at 10% injected error. A homophonic letter substitution of Latin at this N and this
transcription error would have been read (control 0.948 at 3.4%); the target was not. Control-backed negative for
**plain homophonic letter substitution into Latin (la18 corpus)** at N 1,090, K 34, conditional on the GAPS38
transcription and on the 1709-11 corpus standing in for 1628 Latin. Not a negative for the letter as a whole: a
homophonic design with nulls, letter+syllable signs, or a nomenclator layer (design prior's second pick, d=0.18),
or a non-Latin plaintext, is untested. Observation for the next step: line-initial "b" (12 of 32 lines) and the
repeated groups "5t4", "7t4", "t5" are the kind of signals a nulls or syllable design would explain.

Grades: none (no sign read; rule 4). Vision calls: 0. Requests: none (disk only). CPU runs serialized.

## GAPS50-riksarkivet-r4282-1628 (3 Oct 2026, account-4)

Verdict step run: "homophonic-with-nulls annealing on tx2/ciphertext_reconciled.tsv via tools/family_run.py --family
homophonic --param nulls=0.1 (matched control at N 1,090, K 34, la18, noise 0.034, first)". Same spec
(`gaps42/spec_gaps42.json`), stream, corpus (la18, Zaluski 1709-11, about 80 years later than the 1628 target), N
and K as GAPS42.

**Tool fix first (Usage 8).** `tools/families/homophonic.py` silently ignored `--param noise` whenever `merge` or
`nulls` was set, so a nulls control "at the measured error" would have been clean. Fixed (noise now applied on the
merge/nulls branch with the same redraw rule), offline test added (`tools/tests/test_homophonic_merge.py` case 4;
merge=0 nulls=0 still byte-for-byte the old control). `profile=target` is still not applied on that branch, so these
controls use the ordinary largest-remainder allotment over 28 letter signs plus 6 null signs, not the target's own
sign-count profile.

**Matched control, built WITH nulls** (109 of 1,090 tokens nulls over 6 null signs, 981 letter tokens, 28 letter
signs; recovery scored on letter positions only; rows in HYPOTHESES.md):

| injected error | seeds x restarts | control recovery mean (range) | control scores |
|---|---|---|---|
| 0 | 5 x 16 | 0.984 (0.969-0.994) | -2611 to -2706 |
| 0.034 (= measured two-reader rate) | 5 x 16 | 0.860 (0.720-0.949) | -2667 to -2869 |

Gate 0.6 met at both levels.

**Target:** best score **-2950.256**, judge `FAIL language: score=-1.262, null_p99=-1.674, real_p05=-0.978,
real_median=-0.894, N=1090`. **Shuffled target** (`--shuffle-target 1`): -3156.528, judge FAIL -1.338.

**Reading of the numbers.** The target's score and decode are byte-identical to GAPS42's plain homophonic run, and
the shuffled target matches GAPS42's shuffle 1 exactly: the solver has no null model (it maps every sign to a
letter), so `nulls` changes only the control. What this run adds is the control side: a null-unaware homophonic
solver does read a 10%-nulls homophonic Latin cipher at this N and the measured error (0.860, every seed's score
-2667 to -2869), and the target scores worse than every one of those control seeds (-2950) while still beating its
own shuffle by about 200 points. Control-backed negative for **homophonic letter substitution with about 10% nulls
into Latin (la18)** at N 1,090, K 34, conditional on the GAPS38 transcription and on the 1709-11 corpus standing in
for 1628 Latin. Second attempt on the homophonic family; a third variant of it (other null rates, `units=syl`) falls
under rule 3's third-attempt clause and is not proposed. Not a negative for a nomenclator layer (design prior's second
pick, d=0.18), a letter-or-word design, or a non-Latin plaintext.

Grades: none (no sign read; rule 4). Vision calls: 0. Requests: none (disk only). CPU runs serialized (3 runs).

## Remaining gaps (FT4, 3 Oct 2026; updated GAPS, GAPS2, GAPS3, GAPS4, GAPS27, GAPS30, GAPS32, GAPS38, GAPS42, GAPS50, 3 Oct 2026)
Read so far: 0 of 1,094 signs (no key or crib has read any sign; bRIK, RIK-CRIBS, FT4, GAPS)
- R4282 whole letter - blocker: not-attempted; Symbol Sets filter done (GAPS, 3 Oct 2026): 16 of 54 key records carry letter/graphic signs; 4327 tested on its 7 shared signs, no fit vs control (median of 2000 permutations); 4307 pp. 1-3 (GAPS2) a German name nomenclator, one shared sign; 4307 p.4 (GAPS3, 3 Oct 2026) a monoalphabetic reversed alphabet of Latin letter shapes, 16 shared signs / 456 tokens, no fit vs control (real -3.617 vs permuted mean -3.553, p95 -3.298, 0.65 of permutations >= real); 4298/4299 (GAPS4, 3 Oct 2026) one Polish reciprocal-keyword key ("Wilman", Gyllenstierna, 1630s) in two copies, Latin-letter cipher alphabet plus two-digit name codes: no cell for R4282's single digits or Greek signs, commonest signs not covered, test inapplicable; 4275 (GAPS27, 3 Oct 2026) a German Mainz 1634 graphic-sign key, 4 sure shared signs / 81 tokens (7 with ambiguous pairs / 157), no fit vs control (strict real -4.792 vs permuted mean -4.467, 0.66 of permutations >= real; wide -3.880 vs -3.707, 0.67); 4305 (GAPS30, 3 Oct 2026) pp.2-4 a capital-letter name nomenclator (CLAVIS), no alphabet, test inapplicable; 4263 (GAPS30, 3 Oct 2026) a 1650 Sternberg graphic-sign + numeric key, 5 sure shared signs / 121 tokens (9 with ambiguous pairs / 221), no fit vs control (strict real -3.746 vs permuted mean -3.358, 0.99 of permutations >= real; wide -4.017 vs -3.550, 0.99); the last 9 (GAPS32, 3 Oct 2026): 4293, 4295 (digits and struck reciprocal alphabet), 4297, 4308, 4312 tested, no set reaches its permutation p95 (shares of permutations >= real 0.17-0.97); 4309 = the 4275 alphabet; 4322 word list, 4329 two-digit table: inapplicable; 4323 one shared sign (non-test); all 16 sign key records now checked, none fits; second blind pass done (GAPS38, 3 Oct 2026: tx2/ciphertext_reconciled.tsv, 1,090 signs, err_2reader 3.4%); homophonic annealing done (GAPS42, 3 Oct 2026): control 0.948 at the measured 3.4% error (0.992 clean, 0.620 at 10%), target best score -2950 vs control -2535 to -2580 and shuffled target -3143/-3157, judge FAIL -1.262 (real_p05 -0.978): control-backed negative for plain homophonic letter substitution into Latin (la18); homophonic with 10% nulls done (GAPS50, 3 Oct 2026): control built with nulls 0.984 clean, 0.860 at 3.4% error, target -2950 (identical to GAPS42, solver has no null model) vs control -2667/-2869 and shuffled -3157, judge FAIL: control-backed negative for that design too; homophonic family not re-varied (rule 3 third-attempt); next: wordcode family (letter-or-word nomenclator, design prior second pick d=0.18), control first, la18, ~$3
- transcription reliability - blocker: open-codes; second blind pass on R4282 done (GAPS38, 3 Oct 2026): 96.6% two-reader agreement (37 of 1,102 columns), reconciled from the crops to 1,090 signs (H 1049 / M 36 / L 5), Bourdeau differs from it by 2.1% (8 of those signs are the clear word "expensas"); err_2reader only, no benchmark item for this hand; 3 positions (two interlined corrections, one possible extra n) left for the owner sorter if a decode ever turns on them; the R4284 key-test leaf still has only Bourdeau's single pass

## Escalation (FT4, 3 Oct 2026; updated GAPS, GAPS27, GAPS30, GAPS32, GAPS38, GAPS42, 3 Oct 2026)
- [x] siblings: Bourdeau's 14-record bundle read in full (check-solved, 26 Sept 2026)
- [x] clear-pages: R4282's four clear-Latin phrases dragged as cribs (RIK-CRIBS, 2 Oct 2026), negative at resolution
- [x] known-keys: all 16 letter/graphic-sign key records of the Chifferklaver II set checked (GAPS, GAPS2, GAPS3, GAPS4, GAPS27, GAPS30, GAPS32, 3 Oct 2026), plus R4284 crib leaf (bRIK) and R4280/R4281 (FT4): partial sign overlaps only, no fit vs permutation control on any
- [ ] print: AOSB series II and Camerarius letters only phrase-searched (IA full text), not read page by page
- [ ] key-rebuild: no partial key exists to rebuild from; plain homophonic annealing into Latin done (GAPS42, 3 Oct 2026): control 0.948 at 3.4% error, target not read (score -2950 vs control -2535/-2580, judge FAIL); homophonic with 10% nulls done (GAPS50, 3 Oct 2026): control 0.860 at 3.4% error, target not read (same -2950, judge FAIL); next instrument: wordcode family (letter-or-word nomenclator), control first, ~$3
- [ ] image-check: R4282 two pages done (GAPS38, 3 Oct 2026, 3.4% two-reader disagreement, reconciled); the R4284 key-test leaf still single-pass
- [n/a] retry: no earlier attempt failed on a fixable setting
Verdict: keep going: 2 internal gaps; cheapest next: wordcode family (letter-or-word nomenclator, design prior second pick d=0.18) on tx2/ciphertext_reconciled.tsv via tools/family_run.py --family wordcode (matched control at N 1,090, K 34, la18, err 0.034, first), ~$3
