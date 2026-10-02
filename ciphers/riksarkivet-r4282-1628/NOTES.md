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
- [ ] clear-pages: R4282's own clear-Latin cribs ("et qualis sit eius futurus status dubitatur", "sed
      tamen ut res", "tractatus magnas admodum", "Mittatur nobis responsum") not tried this job
- [ ] known-keys (remaining): 68 of the 70 fetched Chifferklaver låda II key records (R4259-R4329) still
      untried against R4282 -- this job used only R4284's key-test leaf, per its brief, not the other 68
- [ ] print: Rikskansleren Axel Oxenstiernas skrifter och brefvexling series II, and Camerarius editions,
      not searched this job (out of scope/cap)
- [ ] image re-check: the two mismatched-length crib pairs, and whether the leaf reads column-wise

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
