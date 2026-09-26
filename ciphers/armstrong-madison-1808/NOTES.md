open

Founders Online, Papers of James Madison, Secretary of State Series, documents 99-01-02-2728 (20 Feb 1808,
via its Wayback Machine copy, since founders.archives.gov itself answers scripted fetches with an empty
HTTP 202 CloudFront challenge) and 99-01-02-2703 (15 Feb 1808, same route) read directly by this worker;
Bourdeau's `cyphersolver/armstrong/` folder (fresh clone, commit 763a3b98ab1c) and Tomokiyo's
`madison_armstrong.htm` (already on disk, re-read) grepped/read in full; AFIO's contest announcement page
fetched directly; DECODE's cached records (`sources/decode/*.tsv`) grepped for "armstrong"/"madison", no
hit; fresh shallow clones of both solver repositories grepped, no hit in aymeloglu/unsolved-ciphers; two
WebSearch queries for a prior or model-assisted solve, none found beyond the AFIO claim already on file.

# John Armstrong to James Madison, Paris, 20 February 1808 -- unique/private code + shorthand

QUEUE row: 27 (rank 30). CATALOG.md line 160 ("Open (a claimed solution is disputed)"). LANDSCAPE.md line 53
("The AFIO claimed solution adjudicated and rejected. Still unsolved."). POOLS.tsv line 599 (pool of 1).
Assigned by the parent 26 Sept 2026 (ROOM.md 06:34) after S. Tomokiyo (Cryptiana) named this his preferred
target for us, in reply to the owner's 24 Sept email (`outreach/tomokiyo-gramont-danzay.md`), recommending it
"via sibling-code vocabulary".

## Sources fetched this pass (26 Sept 2026)

Saved unmodified in `sources/cryptiana/blog/`:
- `2026-06-undecoded-armstrongs-letter-1808-sent.html` -- Tomokiyo's blog post of 4 June 2026 pointing at his
  updated article (below).
- `dbourdeau-cyphersolver-armstrong.html` -- Bourdeau's write-up page (a *different* letter, see below).
- `2026-09-a-cipher-between-louise-of-savoy-and.html` -- the Raince/Carpi post (digest in
  `ciphers/dupuy452-carpi-1520/NOTES.md`, not this target).

Already on disk from an earlier sweep, re-read in full: `sources/cryptiana/web/madison_armstrong.htm`
("An Outlier Code in Armstrong-Madison Correspondence (1808)", first posted 22 Oct 2025, last modified
9 June 2026) -- this is Tomokiyo's own article about *this* letter, linked from the June blog post.

Fetched and read, not saved to the repo (small reference files, not this project's own working data):
`WE028.txt` (Tomokiyo's transcription of Monroe's code, see "Sibling codes" below), the AFIO contest page,
and Founders Online documents 99-01-02-2728/99-01-02-2703 via Wayback.

## What the cipher is

**Not the Armstrong-Madison office code.** Armstrong's routine correspondence with Madison (1804-1810) used
a single ~1600-element word/syllable code conventionally labelled by its group for "the", **THE=972**
(Weber, *United States Diplomatic Codes and Ciphers, 1775-1938*, pp.154, 188, cites ~40 letters in it among
DUSMF, NARA RG 59 microcopy M34 rolls 13-14). The 20 Feb 1808 letter is not in that code: Madison himself
wrote to Jefferson on 15 May 1808 (Founders 99-01-02-3082) that "The undecyphered letter from A. was
probably misaddressed to the Secretary of State. No such Cypher is in the office, and must be one concerted
with another correspondent" -- Angela Kreider (editor, Papers of James Madison, U.Va.) reads this as
referring to the 20 Feb letter, and her team confirms no other State Department code (Weber's own printed
codes included) matches it either. Bourdeau's `armstrong/NOTES.md` gives the quantitative version: his
merged THE=972 table (see below) decodes the *15 Feb 1808* Armstrong-to-Madison letter (Founders
99-01-02-2703, five days earlier, same code) at 72% (176 of 243 groups H/C-known, producing continuous
sense), but the *20 Feb* letter at only 25% (92 of 369 groups), and those hits render as noise, not sense --
"the 20 Feb code is a different code". It also carries "graphical symbols" resembling a shorthand mixed
with the numeral groups (35 short passages plus two full lines, `*`/`**`/`***` in `ciphertext.txt`); Tomokiyo
compared them to Taylor's 1786 shorthand (no match) and, per Norbert Biermann's bibliography lead (a German
1895 book with an 18th-century English-shorthand bibliography, pp.38-40), lists Weston, Mitchell, Gurney,
Byrom, Mavor and Macaulay as further candidates, none checked against the symbols as of the June 2026
update.

**Correction to QUEUE row 27's own cheap-test description.** The row reads "Place Krajcovic's crib from
Armstrong's 15 Feb 1808 letter to Jefferson against the opening groups in ... feb20_ciphertext.txt". Two
things in that sentence do not check out:
1. **"to Jefferson" is wrong.** Founders Online 99-01-02-2703 is headed "**To James Madison** from John
   Armstrong, Jr., 15 February 1808" (confirmed by direct fetch this pass, via Wayback). Every source this
   sweep read (Tomokiyo, Bourdeau, Founders itself) treats the 15 Feb letter as Armstrong-to-Madison, in the
   ordinary THE=972 code -- the same letter Bourdeau's own paired check (above) uses as the positive half of
   his negative result on the 20 Feb letter. There is no "Armstrong to Jefferson, 15 Feb 1808" letter found
   anywhere in this sweep.
2. **No "Krajcovic" connects to Armstrong anywhere reached.** Grepped fresh clones of both solver
   repositories, `sources/cryptiana/`, this repository's own QUEUE.md/STATUS.md/LANDSCAPE.md/CATALOG.md, and
   two WebSearch queries: the only "Krajcovic" this repository has on file is a solver credited on a wholly
   unrelated target, `UNSOLVED-SURVEY.md` line 113 ("Catokwacopa ads, Evening Standard", 1875, "Bosbach,
   Estes, Ernst, Krajcovic readings since 2018"). This reads as a scout-row mixup (a name from a different
   target's cheap-test note attached to this one), not a real, findable crib -- flagged, not corrected in
   QUEUE.md by this worker (out of this brief's file list; the parent should decide whether to fix the row).

Given both problems, the spec below (`specs/armstrong-madison-1808.json`) does not name "Krajcovic's crib"
as test 1; it describes what a crib-placement test against the 15 Feb 1808 letter can actually mean here
(the two letters share no code, so a crib test is about shared vocabulary/structure across Armstrong's own
letters generally, not a key transplant) and marks the named source unverifiable.

## Ciphertext (Bourdeau's transcription, CLAUDE.md rule 8)

Copied unmodified into `ciphertext.txt` from `cyphersolver/armstrong/feb20_ciphertext.txt` (commit
763a3b98ab1c, MIT code / CC BY 4.0 text), itself transcribed from the Founders Online Wayback copy of
99-01-02-2728 (Founders' own site is now CloudFront-challenged for scripts, confirmed this pass: a direct
curl fetch returns HTTP 202 with 0 bytes). **369 groups, 216 distinct, values 1 to 1900.** 35 short passages
plus 2 full lines are graphic symbols, not numeral groups (marked `*`/`**`/`***`); one group is illegible
(`<..>`). The opening word "The" is in clear. No independent second transcription against the NARA M34
roll 14 images (29-32) has been made by anyone found this sweep -- Bourdeau's own notes flag this as
unverified against the manuscript.

## Sibling codes named by Bourdeau or Tomokiyo

| Code | Correspondents | Size | Published how, by whom | Fits the 20 Feb letter? |
|---|---|---|---|---|
| **THE=972** (unlabelled WE number) | Armstrong <-> Madison, 1804-1810, all *other* known letters | ~1600 elements, blockwise alphabetical (many short A-Z runs, syllables restart the alphabet every few dozen groups) | **In part.** Tomokiyo's own partial table (227 entries, from the one known-plaintext letter of 4 May 1806, `code972_partial.json`) merged by Bourdeau with ~580 pencil decodes harvested from NARA M34 roll 13's marginal annotations (`pairs.txt`, `armstrong/NOTES.md`) into a 580-of-~1600-group table (H/C/M/I graded), published as `key972.js` in the repo (MIT) and rendered on `docs/armstrong.html` (CC BY 4.0 text) | **No** (Bourdeau's own paired-check negative, above: 72% on 15 Feb, 25%/noise on 20 Feb) |
| **WE027** | Robert R. Livingston (Armstrong's predecessor) <-> Madison | ~1700 elements, blockwise alphabetical | **Not published anywhere found.** Named only descriptively by Tomokiyo, cited to Weber 1979 pp.154, 188 (a print survey, not a transcription); no `.txt`/`.json` table for WE027 exists in Bourdeau's repo or Tomokiyo's site | Not tested (no table exists to test with) |
| **WE028 (THE=1385)** | James Monroe (sent to Paris to assist Livingston) <-> Madison | 1600 elements, blockwise alphabetical | **Published in full by Tomokiyo himself.** Fetched `WE028.txt` this pass (cryptiana.web.fc2.com/code/WE028.txt, one request): 1600 semicolon-separated `code;word` lines, 1 to 1600, no gaps found on a line-count check. Same office, same period, same code-construction convention (word/syllable groups, blockwise-alphabetical runs) as THE=972, but a different correspondent's own table -- not applied here | Not tested this pass |

No sibling code's own vocabulary has been checked, digit-for-digit, against the 20 Feb letter's 216 distinct
groups by this worker (per the brief: intake only, no cryptanalysis). Tomokiyo's suggestion ("a model might
read it if it learns the vocabulary of a sibling code") reads, after this sweep, as more plausibly about the
*construction convention* the three codes share (word-and-syllable groups, blockwise-alphabetical runs,
common-word homophones) than about any single sibling's *values* transferring directly -- THE=972's own
values are already shown not to fit.

## The AFIO claimed solution and its adjudication

**Claim.** The Association of Former Intelligence Officers announced, 27 May 2025 ("We Have a Winner in the
Armstrong-Madison Encrypted Letter Contest!", afio.com/member-news, fetched directly this pass), that
member Yaacov Apelbaum had decrypted the letter: a 56-entry code-to-word table and a 60-word "Decrypted
Text" ("The petitions of your seamen concerning their treatment have been examined ... we shall receive
satisfaction."), with a stated four-part "verification methodology" (internal consistency, cross-reference
with Armstrong's 1804/1806 letters, frequency analysis, stylistic reconstruction).

**Rejected, independently, twice:**
- Tomokiyo's article judged it unconvincing on inspection (Oct 2025, restated June 2026): partial coverage,
  forced fit.
- Bourdeau's adjudication (`armstrong/NOTES.md`, 16 Sept 2026, `adjudicate_feb20.py`) is the quantitative
  version: the key covers 133 of 369 groups (36%; 51 of 216 distinct), 5 of its 56 numbers never occur in the
  letter, 6 of the 60 published plaintext words have no code group backing them at all, and -- the decisive
  test -- **a key built by the same procedure (walk the plaintext, assign each word the next free group) on
  a *shuffled* copy of the ciphertext fits the claimed sentence and the letter as a whole *better* than the
  AFIO key does**: 500 such random keys average 70% in-span occurrence-consistency and 41% over the whole
  letter, against the AFIO key's own 59% and 30%. A key that fits random noise better than it fits the real
  text carries no information about the code. This is a matched-control negative already run and on file,
  not something this intake worker re-ran.

## The "prestigious publication project"

The June 2026 blog post's own wording: "the editorial team is still very interested in the content of the
letter. If it can be solved in the next year or two, they could probably include it in their next volume of
Madison Papers." This is the **Papers of James Madison** (University of Virginia, Founders Online's own
publisher; editor Angela Kreider, per `madison_armstrong.htm`'s "Historical Context" section) -- not named
more specifically than that in either Cryptiana post read this pass.

## What is still open, for a future solver (not run here, per this brief)

1. A crib/vocabulary test using Armstrong's *other* letters (15 Feb, 22 Feb, 4 May 1806, all in THE=972 and
   already transcribed by Bourdeau) for period/register/idiolect match against the 20 Feb letter's word
   lengths and repeats -- not a key transplant (THE=972 does not fit), a language-model-style vocabulary
   prior, matched against a shuffled control per CLAUDE.md rule 3.
2. WE028's full 1600-entry table, and a from-scratch structural comparison of its blockwise-alphabetical
   layout against the 20 Feb letter's own group-value distribution (whether the same block boundaries
   recur, even if the values differ) -- untested.
3. The shorthand passages (35 short + 2 full lines): Tomokiyo's shorthand-bibliography lead (Weston,
   Mitchell, Gurney, Byrom, Mavor, Macaulay, Taylor) is unchecked against the actual symbols.
4. A second, independent transcription against the NARA M34 roll 14 manuscript images (29-32) -- the
   Founders Online group list has never been checked against the original by anyone found this sweep.
5. Kreider's own list of candidate "other correspondents" for a private cipher: William Pinkney (Britain),
   James Monroe (Pinkney's predecessor), George W. Erving (Spain), Robert R. Livingston (Armstrong's
   brother-in-law and predecessor in Paris), or Armstrong's New York political circle -- none of their
   1808 correspondence has been located or checked against this code by anyone found this sweep.

## Intake gate

`python3 tools/intake_gate_check.py ciphers/armstrong-madison-1808` output:

    ciphers/armstrong-madison-1808: open (line 1) -- edition/page or full-text-search citation found within 6 lines
    EXIT:0

## ARM-CODES corpus (26 Sept 2026)

Built `tools/data/uscodes-1800/` for the sibling-code vocabulary family (per Tomokiyo's suggestion): four
value->word TSVs (WE028 1600 entries; THE=972 in three renderings, 580/227/95 entries with Bourdeau's H/C/M/I
grades kept where published), Bourdeau's own decodes of Armstrong's other 1808 letters (his idiolect, same
months as the target), and a stats script comparing last-digit distribution, value-gap pattern, alphabetical
block structure and homophone counts across the tables, THE=972's real usage, and the target. Full detail and
sourcing in that directory's own README.md and HYPOTHESES.md's new "ARM-CODES corpus" section; no decoding of
the target and no family run this pass, per this job's brief -- both are queued next (ARM-A2, then family C).
Headline: no sibling table or usage instance reproduces the target's last-digit skew (digit-0/digit-1 at
25%/18% of tokens) or its 900-1099 value gap, so neither is inherited from a codebook already on file; all
four tables are built in short alphabetical blocks (~5-16 entries each), the same construction convention
across Livingston's, Monroe's and Armstrong's own codes. WE027 (Livingston<->Madison) and every other
WE-numbered code Tomokiyo names have no downloadable table anywhere found, only inline worked specimens; Weber
1979 itself is on Internet Archive but print-disabled-tier and unborrowable by this account, and has no
HathiTrust volume for its OCLC number either -- not chased further.

## Requests this session (intake, 26 Sept 2026)

gallica.bnf.fr: 0. github.com: 2 shallow clones (`dbourdeau/cyphersolver`, `aaymeloglu/unsolved-ciphers`, both
deleted after grepping). cryptiana.blogspot.com: 2 (the Raince/Carpi post, the June Armstrong post).
dbourdeau.github.io: 1 (his armstrong.html page). cryptiana.web.fc2.com: 1 (`WE028.txt`; `madison_armstrong.htm`
was already on disk from an earlier sweep, not re-fetched). web.archive.org: 2 (Founders 99-01-02-2728 and
99-01-02-2703 via Wayback, after a direct founders.archives.gov fetch returned an empty HTTP 202). afio.com: 1.
founders.archives.gov: 1 (the empty-202 attempt, not retried, per the good-citizen rule -- Wayback used
instead). WebSearch: 3 queries (a prior/model-solve check, a Krajcovic check). No DECODE login, no logins of
any kind, no credentials touched. All fetches one at a time, >=1.5s apart, descriptive User-Agent.

## ARM-EN18 (26 Sept 2026): era/register-matched judge corpus built and fold-checked

The spec's `judge` block used `LANG_CORPORA["en"]` (Sherlock Holmes 1892 + Moby-Dick 1851, both 19th-c.
fiction), already flagged by TOMO-REPLY's `corpus_caveat` as an era/register mismatch for this 1808 Paris
despatch (CLAUDE.md rule 3's pt18/es17c/EN-FOLDS lessons). Built `tools/data/en18/` -- six Internet Archive
full-text sources of 1794-1819 American diplomatic/official correspondence (Monroe Vols II/V, Gallatin Vol I,
Madison Vols VII/VIII, Jefferson Vol IX; two more Monroe volumes 503'd on IA and were dropped after one retry
each, per the good-citizen rule), 4,806,387 letters after `fold()`. Registered as `LANG_CORPORA["en18"]` in
`tools/judge_plaintext.py` (a shared-tool option, not a private copy, per Usage item 8), with an offline test
(`tools/tests/test_judge_plaintext_lang_en18.py`, a held-out Madison passage not in the corpus, passes; shuffled
and random-letter controls both fail).

Leave-one-file-out fold check at N=1000/1500 (about this target's own 369-code decode length, not the 200/500
`tools/data/en`'s own check used): blended false-negative rate **14.2%/15.1%**, per-fold spread **0.270/0.260**
-- roughly 4x lower and 2.5x tighter than the identical check run against `en` at the same N this pass
(58.6%/64.8% blended, 0.675/0.710 spread). Register-matching helped substantially here, the same direction as
pt18 vs pt17, but **the spread is still above the EN-FOLDS amendment's 0.05 gate** (Gallatin Vol I and Jefferson
Vol IX read as outliers against the more despatch-heavy Monroe/Madison volumes when held out) -- a FAIL/PASS
against `en18` is better-calibrated than against `en` but not a settled result. Full numbers in
`tools/data/en18/README.md`. `specs/armstrong-madison-1808.json`'s judge block updated: `language` -> `en18`,
`letters_min`/`letters_max` widened to 600/3000 (the previous 200/500 range cannot fit a 369-group decode),
`corpora_note` records the numbers above. No long-s OCR misreads found in any of the six sources (checked, not
corrected -- none needed). Requests: archive.org about 16 (six successful `_djvu.txt` fetches, two
advancedsearch.php calls, two 503s on `writingsjamesmo0{4,5}unkngoog` retried once each per the good-citizen
rule then dropped, one held-out test snippet via byte-range on a seventh, uncommitted volume). No other hosts.

## Requests this session (ARM-CODES, 26 Sept 2026)

See `tools/data/uscodes-1800/README.md`'s own "Requests this session" section for the full breakdown:
cryptiana.web.fc2.com 41, github.com 1 shallow clone (deleted after copying), archive.org 2, openlibrary.org 1,
catalog.hathitrust.org 2 (one 403 with a descriptive UA, one 200 with a Chrome UA per the Access playbook's own
note for that host). No logins, no credentials touched, all >=1.5s apart.

## ARM-REC pass, 26 Sept 2026 (LANE ARM worker ARM-REC) -- is a key/decode/summary of the letter extant?

Full detail in `crib_sources.md`. Short version: **no decode and no later summary of the 20 Feb letter's
content found anywhere reached this pass.** The strongest evidence on file is still Kreider's own statement
(already quoted above, re-read this pass from `madison_armstrong.htm`): "we've found no evidence that it ever
was decoded, nor that Madison acknowledged receiving it." New this pass, consistent with that: the Library of
Congress's own hand-written finding-aid abstract of Armstrong's letters to Madison, 1804-1814
(`loc.gov/item/mss31021a016/`, 2 of 17 images read directly) jumps straight from 4 May 1805 to 30 Aug 1808 --
no Feb 1808 entry of any kind, suggesting nobody who compiled that finding aid had a readable text of it
either. web.archive.org was unreachable this pass (repeated connection resets, confirmed via the agent
proxy's own relay-failure log as a genuine host outage, not a proxy fault) -- Founders Online's own editorial
notes and its 21 Feb-31 Aug 1808 Armstrong letter index (this brief's step 1) could not be checked and are
still open for a successor. DECODE's cached listing (re-read, not re-fetched) and NARA's catalog API (blocked
without the missing key, matching the existing playbook note) add nothing new.

**Correction filed against this file's own "What is still open" wording above:** a genuine "John Armstrong to
Thomas Jefferson, 15 February 1808" letter *does* exist (Thomas Jefferson Papers, Library of Congress,
`loc.gov/item/mtjbib018243/`, not in the Madison Papers collection this file's earlier search covered) --
contra this file's own "There is no 'Armstrong to Jefferson, 15 Feb 1808' letter found anywhere in this
sweep." It is, however, entirely in clear (a short personal letter of recommendation for a messenger, plus a
note on Lafayette's Louisiana land grant and an enclosure on M. Skipwith), addressed to a different recipient
in a different register from the diplomatic 20 Feb letter to Madison, so it still does not supply "Krajcovic's
crib" (that name remains unconnected to anything found) or a usable key transplant -- at most one more
period/idiolect data point alongside the already-known 15 Feb and 22 Feb 1808 letters to Madison.

Kreider's four named candidate "other correspondents" (Pinkney, Monroe, Erving, Livingston): the James Monroe
Papers collection at LOC returned 0 hits for "Armstrong"; no direct Armstrong-Erving item found by name-pair
search; Livingston search timed out twice (loc.gov intermittently unresponsive this pass) and was not
completed; Pinkney not searched by name-pair (only the already-known wrong-direction Pinkney-to-Madison
letters are on file). None of the four produced a coded sibling letter to test as a pool.

Requests this pass: web.archive.org 1 success (CDX reachability ping) + 3 failed (connection reset, host
outage, stopped per good-citizen rule) -- Founders-dependent steps of this brief's job not completed. loc.gov
about 14 (2 timed out on complex queries after one retry each, per the good-citizen rule; rest succeeded).
catalog.archives.gov 2 (confirms existing "needs x-api-key" finding). DECODE 0 new fetches (cache re-read).
No logins, no credentials touched.

## ARM-A2 (26 Sept 2026): sibling-table direct-transfer sweep -- negative, both controls on file

`ciphers/armstrong-madison-1808/a2/transfer.py` (offline, seeded, no network) decoded the target's 369 numeral
groups under each of the four tables in `tools/data/uscodes-1800/` and scored the result with a word-bigram
model built from the en18 corpus, against two matched controls per CLAUDE.md rule 3: 200 tables made by
permuting each table's own plaintext column within alphabetical blocks of 20 consecutive values (destroys the
value->word pairing, keeps the value range and blockwise-alphabetical structure), and 200 shuffles of the
target's own token order decoded with the real table. No table transfers: all four FAIL
`tools/judge_plaintext.py`'s language check outright (WE028 -1.082, THE972_bourdeau -0.939,
THE972_tomokiyo_clean -0.883, THE972_tomokiyo_partial -1.108, all against real_p05 thresholds of roughly -0.80
to -0.90), and no table's percentile against either control is an extreme tail value once read alongside its
own coverage (WE028 highest coverage, 328/369 tokens, sits at the 70th/96th percentile of its two controls but
still FAILs the absolute language gate; the three THE=972 tables cover only 14-108 of 369 tokens, too few
adjacent-covered-pair bigrams (7-33) for a percentile to mean much). A round-trip positive control (re-encoding
Bourdeau's own known-plaintext decode of the 15 Feb 1808 letter under `THE972_bourdeau.tsv` and decoding it
back) recovers 87.3% of its words/syllable-fragments exactly, proving the pipeline is mechanically correct, but
still FAILs the same language judge at that length -- THE=972 publishes bare syllable fragments as entries
("ac", "ce", "mp", "t"), and dropping uncovered in-between words breaks the character-level 4-gram fluency the
judge scores, an artifact of the code family and the judge, not a pipeline defect (full explanation in
HYPOTHESES.md's ARM-A2 section, which also has the per-table table and the salad). No transfer is reported as a
reading (rule 10); the ladder's family B (vocabulary prior, not direct value transfer) and family E (recovery)
remain open. `specs/armstrong-madison-1808.json`'s `cheap_test_done.A2` records the same summary. No network
access this pass (offline job per brief); 0 requests to any host.
Orchestrator caveat (LANE ARM, 26 Sept 2026 10:17, answering V9-QA8 and V9-QA9): the en18 judge FAILs above carry ARM-EN18's
reliability limits -- leave-one-file-out false-negative 14-15 percent, per-fold spread 0.26-0.27, above the 0.05 gate -- and
ARM-C1 later found the same judge PASSes a shuffled-target salad at this length, so a judge line here is not decisive either
way; the A2 negative rests on the permuted-table and shuffled-order percentiles, not on the judge.

## ARM-REC2 pass, 26 Sept 2026 -- retried ARM-REC's step 1; web.archive.org still down

Full detail in `crib_sources.md`. **web.archive.org did not recover**: retested at 07:29-07:32 UTC (three
fetches, root page and a CDX query), all `Connection reset by peer`, confirmed via the agent proxy's own
relay-failure log as the same host-side outage ARM-REC found at 07:11, not a proxy fault -- `archive.org`
itself (non-Wayback) answers fine in the same window, so the outage is specific to the Wayback subdomain.
Founders Online direct (the metadata JSON dump) retested once, still the CloudFront empty-202 challenge, not
retried further. Founders' own editorial notes to 99-01-02-2728, and the full text of the 21 Feb-31 Aug 1808
Armstrong/Madison/Jefferson letters this brief's step 1 asks for, remain unfetched; this is now the second
consecutive worker to find the host down, so a parent check-in should confirm real recovery before a third
worker spends requests on it.

**Fallback that did produce results, using no Wayback/Founders fetch at all:**
1. **30 Aug 1808 postscript code and first groups** -- answered in full from Bourdeau's page already on disk
   (no host needed): **THE=972**, Armstrong's ordinary office code with Madison (not the 20 Feb letter's
   unknown code). First groups quoted exactly: "1394. 1116. 1273. 250. 1165. 1405." Full 49-group postscript
   decodes (48 of 49 determined): "Russel ought to be the consul: he is an American by birth, and is much
   better qualified than any other candidate. In a word, he is above men in general. Next to him in fitness is
   O'Mealy, but he is, like Warden, an Irishman[-re]." Founders prints the groups as Early Access document
   99-01-02-3466, undeciphered.
2. **Armstrong-to-Jefferson 15 Feb 1808 (`mtjbib018243`): does Founders print it, any part in cipher?** Founders
   Online does print it, as Jefferson Papers document **99-01-02-7420** (identified this pass, not previously on
   file) -- title and indexed paraphrase match ARM-REC's own direct manuscript read closely (the Talleyrand
   messenger, Admiral La Touche Tréville, Lafayette's Louisiana grant). **No part is in cipher** -- confirmed
   independently by ARM-REC's own primary-source read (entirely in clear), not by the Founders title match
   alone, which was not fetched and cannot itself be trusted for content (WebSearch's own synthesized summaries
   proved unreliable this pass -- one query restated the already-discredited AFIO "Decrypted Text" as if it were
   a real decode, which crib_sources.md flags explicitly).
3. A table of 13 further Founders document IDs (titles/dates only, located via WebSearch, none fetched) for
   Armstrong-Madison and Madison-Jefferson correspondence Feb-Sept 1808, as a fetch list for whichever
   successor next has a working Wayback route -- full table in crib_sources.md. New cross-reference found: the
   "undecyphered letter" note (99-01-02-3082, Madison collection) is cross-listed as **99-01-02-8003** in the
   Jefferson collection. Jefferson's own reply to that note is still not located; the nearest dated candidate
   (99-01-02-8006, Madison to Jefferson again the next day) is unconfirmed and not itself a reply from Jefferson.

Requests this pass: web.archive.org 3 failed (stopped, host outage persists). founders.archives.gov 1 (metadata
JSON, empty 202, not retried). archive.org 2. www.archives.gov 1 (confirmed the Founders metadata dataset is
titles/ids only, would not have answered this brief even if fetchable). WebSearch 7 queries. No DECODE, no
logins, no credentials touched.

## ARM-DESIGN (26 Sept 2026, LANE ARM worker ARM-DESIGN, Fable): family B design verdict

Plaintext-free statistics computed on the sibling tables' known layout, the four real THE=972 letters and 60
simulated 369-token en18 letters per design (contiguous one-part / two-part / WE028 blockwise / THE972 partial /
sequential-with-particle-block; decade designs H-DEC, H-HOM lazy and flat, gapped-insertion numbering), then on the
target; all numbers side by side in HYPOTHESES.md "ARM-DESIGN", scripts and tables in `design/`. Verdict: the letter
is a two-level numeric code -- a ~99-entry particle list at 1-99 (K~100 by a Zipf fit, top five values carry 14%
of tokens, flat digits) and above 100 a family book whose units digit is a fixed-meaning member slot (0 >> 1 >
4,6,7 >> 2,3,5,9, the same digits in every hundred-block): the digit concentration puts the target at percentile
100 against every contiguously numbered design and every real THE=972 letter, the digit order refutes lazy
homophone choice and fill-in-order insertions, and the decade/units dependence (z=2.76 against its own permutation
null) refutes homophones chosen independently of the word. One-part vs two-part vs blockwise is not decidable from
the ciphertext at this length (the statistics overlap by more than their shift), and the siblings are block-local
at best, so family C gets no alphabetical constraint. Above 100 the block reads as content words with near-full
coverage (168 distinct in 237 tokens; en18 content streams give 196, p05 170), so the book holds ~900-1800 forms,
not 180 roots with inflections (which would leave ~300 words per letter for the 37 shorthand passages). Family C's
unknown, score and matched control are written in `design/family_C_spec.md`. The single most valuable next access
step is the NARA M34 roll 14 image check of the units digits (open item 4 above): the whole verdict rests on
Bourdeau's transcription of the Founders group list, and a systematic misreading of 2/3/5/9 would collapse it to a
contiguous code. Requests this session: none (offline). Not done, per the brief: no decode to words, no family C
tool.

## ARM-IMG pass, 26 Sept 2026 (LANE ARM worker ARM-IMG) -- manuscript images of the 20 Feb 1808 letter fetched

**Images found and fetched, `images/` + `images/manifest.json`.** Route 1 (Internet Archive advancedsearch for
NARA microfilm M34, four query variants: bag-of-words and exact-phrase on "United States Ministers to France",
"M34 microfilm state department", "Armstrong Madison despatches") returned 0 hits every time -- IA does not carry
this NARA microfilm series; confirmed negative, not tried further. Route 2 (catalog.archives.gov): plain curl to
`/search` and to the site's own `/proxy/records/search` and `/proxy/announcements` paths (read from the React
bundle's `main.*.chunk.js`) returns only the client-rendered app shell at HTTP 200, never JSON -- the real search
runs client-side against an internal API gateway not exposed as a plain public endpoint (`/api/v2/api-docs/` is
a stock, unconfigured Swagger-UI install pointing at the petstore demo spec, not this API); this matches the
Access playbook's existing note that `catalog.archives.gov`'s API v2 needs an `x-api-key` this environment does
not have. **Route around it, not in the playbook table yet:** the same search works through a real headless
browser (`tools/browser_fetch.js`), and the item page it renders embeds a genuine public **IIIF Image API v3**
service with no key at all (`catalog.archives.gov/iiif/3/<url-encoded-object-path>/info.json` and
`.../full/<w>,<h>/0/default.jpg`, plain curl, HTTP 200). Search `"Despatches from United States Ministers to
France" 1808` (browser-rendered) surfaced the exact file unit: **NAID 188671566, "Jan. 22, 1808-Sept. 14, 1810",
Record Group 59, Reel 14** (M34 roll 14), 664 images/1 file, under "File Unit: Despatches from U.S. Ministers to
France, 1789-1906". Its rendered HTML lists every frame's IIIF object path directly
(`lz/dc-metro/rg-059/603720/M34/M34-014/M34-014-NNNN.jpg`), confirming frames 0029-0032 exist (and 0033).

Fetched all four frames named in the brief at each frame's own native resolution (read per-frame from its own
`info.json`, not a fixed guess -- **gotcha found and worked around**: requesting a size wider than a given
frame's native width does not 4xx, it silently returns the site's own HTML error shell at HTTP 200, same bytes
as the "requested image could not be found" the item-page viewer itself shows for a bad thumbnail; caught by
`file`-checking every download, not by the curl exit code or `-w` status alone): 0029 3728x3280 (354 KB), 0030
2096x2624 (473 KB, header dated "Paris 20 feby 1808", matching the target letter directly), 0031 3968x2576
(2.68 MB, "a cleaner copy of 30" per Founders/crib_sources.md), 0032 3968x2608 (1.18 MB). Total 4.5 MB, well
under the 30 MB folder rule. Read 0030 directly (Read tool, not a subagent, per the brief's "do NOT transcribe"):
digits and shorthand strokes are clearly legible at this resolution -- this is a real, checkable image, not a
placeholder or a misfiled frame. No transcription or digit comparison against Bourdeau's table performed (out of
scope for this job; the next job in the lane's queue).

Requests this pass: archive.org 4 (advancedsearch, all negative). catalog.archives.gov: 2 plain-curl probes (app
shell only) + `tools/browser_fetch.js` used 4 times (home/search x3, item page) + IIIF `info.json`/image fetches
about 14 (well under the 40-request budget the brief set for this host; under archive.org's 20 and loc.gov's 20
too -- loc.gov not used this pass, route 1/2 sufficed). No FamilySearch/Fold3/Ancestry attempt (route 4, paywalled
by the brief's own instruction, not tried). No logins, no credentials touched. New host-route finding for the
Access playbook table (not added to CLAUDE.md by this worker, which may not edit it -- flagged in ROOM.md for
the lane orchestrator/parent): `catalog.archives.gov` serves plain, unauthenticated IIIF Image API v3 image
downloads for digitized items, discoverable by rendering the item page with `tools/browser_fetch.js` even though
its own JSON search/records API needs the (absent) `x-api-key`.

## ARM-TR pass, 26 Sept 2026 (LANE ARM worker ARM-TR) -- independent manuscript transcription, PARTIAL

Full detail in `HYPOTHESES.md`'s "ARM-TR manuscript check" section and `images/layout.md`. Two blind
transcription passes per manuscript page (crops from `tools/iiif_lines.py`, reconciled with
`tools/reconcile_passes.py`), settling disagreements by this worker looking at the crop directly, per
this job's brief.

**Correction to the job brief's own framing**: frames 0030 and 0031 are NOT the "same page in two
copies" as the brief assumed -- 0031's opening line continues directly from 0030's last line
(verified against `ciphertext.txt`'s own group sequence at that point). Frames **0031 and 0032** are
the genuine duplicate pair: two independent photographic scans of the same two-page spread (pages
2-3), confirmed by matching content down to identical ink-stroke shapes. Frame 0029 is a different,
unrelated 1808 document (a later cover memo referencing a *17 Feb* letter) and was not transcribed.

**Coverage gap, the most actionable finding of this pass**: this worker's manuscript reading (312
numeric tokens, marks excluded) aligns cleanly against only the first 332 of `ciphertext.txt`'s 369
numeric groups, then simply runs out -- the alignment does not degrade, it ends. Frames 29-32 do not
contain the whole 20 Feb 1808 letter; ARM-IMG's own `images/manifest.json` already flagged frame 0033
as "not fetched". **A successor should fetch frame 0033 (and check whether the letter needs even
more) before this manuscript-verification thread can cover the last ~10% of the letter.**

**Digit-level result**: one clean, doubly-confirmed units-digit disagreement -- manuscript page 1,
line 4, group 10 reads **1843** (both blind passes agree, H-graded), against Bourdeau's
`ciphertext.txt` value **1841** at the same position. Six further disagreements were settled from the
crop in Bourdeau's favor or corrected pass-B's favor (98+8 marks on page 1 line 6; 1640, 19, 760,
1461+740, and a final 1900 pass A had cut off -- see HYPOTHESES.md for the full list); none of these
touches the units digit specifically. A separate, larger block of disagreement in the page-1 lines
this worker's own passes independently flagged as their hardest (dense shorthand-and-digit mixtures,
manuscript lines 6-13) does not resolve cleanly at all and is flagged, not adjudicated, as the next
most valuable look on this thread.

Units-digit distribution over the shared covered range (ciphertext.txt's first 332 groups) matches
closely in shape between this worker's reading and Bourdeau's transcription (0/1 dominant, 2/3/5/9
rare in both) -- this does not show the systematic 2/3/5/9 misreading ARM-DESIGN's own caveat worried
about, but the still-uncovered final 37 groups and the unresolved shorthand-heavy span mean that
caveat is not closed, only not actively contradicted by what this pass could check.

Shorthand: 29 shorthand-bearing manuscript lines (of ~34 marked passages Bourdeau records across the
whole letter; this pass only covers pages 1-3) cropped to `images/shorthand/` with an index
(`images/shorthand/index.tsv`), not read, for a later family S job per the brief.

Requests this pass: none (all work offline against already-fetched images and 6 Sonnet subagents,
each transcribing one page's line crops from a single set of images already on disk; 2 concurrent at
a time as required).

## ARM-C1 (26 Sept 2026, LANE ARM worker ARM-C1, Fable): family C built and controlled -- control below gate, target not run

Family C (`design/family_C_spec.md`) now exists as `tools/families/nomenclator.py` (registered in
`tools/family_run.py`, offline test `tools/tests/test_nomenclator.py`, 18 s): a two-level numeric word code solver
(particle block 1-99, family book >= 100 with decade = family and units digit = member slot) that anneals a
value -> word key under a word-trigram en18 LM with the sibling-vocabulary prior; `*`/`**`/`<..>` are OOV wildcards.
Its matched control (rule 3), a 369-coded-token letter cut from the HELD-OUT Jefferson Vol IX with a cold random
particle block and an 1800-form book built from that volume's register, read 0.135 (0.027-0.201; 0.141 on a pre-fix run) blended over 3 seeds
against the 0.6 gate -- particles 0.363 / 0.350 / 0.048, book 0.006 / 0.011 / 0.005 -- so `family_run.py` wrote CONTROL BELOW GATE and never
ran the target; no decode and no judge line exist for the 20 Feb 1808 letter from this family. Diagnostics on the
control letter show why: even from the true key the objective drifts (particles 0.856, book 0.274 after greedy
sweeps), with every anchor given the singletons come back at 0.113, and the blind sampler's best state scores
above the truth-anchored one -- at 369 tokens with 135-168 singleton book values the information is not there, so
the spec's own conclusion holds: family C is a non-test at this N and the next step is MORE CIPHERTEXT in the same
code (ARM-REC's route), not more restarts. Control 2 (design-mismatched, Armstrong's 15 Feb 1808 letter in THE=972
run blind without its key, 243 groups) read 12/173 known groups (0.069; 12/87 whole-word entries). Control 3
(`--shuffle-target 1`, gate disabled for the floor run only) scored -1467.8 (-3.633/token) and its salad PASSes the
en18 judge: a judge PASS on any family-C decode of this target is a false positive at the floor, so the judge is
not a gate for this family here (this is the kind of case rule 3's shuffled-null floor exists to catch). Rule 5:
the target stays `open`; this is a control-backed non-test, not a negative. Per-seed, per-class and floor numbers,
the control's shape beside the target's, and the seven logged deviations from the spec are in HYPOTHESES.md "ARM-C1
nomenclator"; logs in `families/control1_battery.log` (rerun after a determinism fix; the pre-fix run is
`control1_battery_prefix.log`), `families/control2_feb15-1.txt`, `families/control3_floor.log`. Not done here:
the spec's precondition, the NARA M34 roll 14 units-digit check against Bourdeau's transcription -- outside this
brief; ARM-TR (section above, merged in the same window) has since covered the first 332 groups with one confirmed
units-digit disagreement and a matching digit shape, so the design premise stands with the last 37 groups unchecked. No network
this job; no host requests.

## ARM-POOL pass, 26 Sept 2026 (LANE ARM worker ARM-POOL) -- frame 0033 fetched; roll-14 survey finds no matching sibling

**Frame 0033 fetched** at native resolution (3888x3264, `images/M34-014-0033.jpg`, `images/manifest.json` updated) via
the same keyless NARA IIIF route ARM-IMG documented. This is the frame ARM-TR flagged as covering the target
letter's last ~37 numeral groups (ciphertext.txt tokens 333-369); this job did not transcribe or diff it against
ciphertext.txt (a successor job, per this brief's own scope).

**Roll-14 survey (NAID 188671566, "Jan. 22, 1808-Sept. 14, 1810"), every 6th frame at 600px wide, 111 requests (frame
0001 does not exist as an object -- info.json itself 404-shells; frames 0002-0664 confirmed real, 0665 is a small
928x640 target/calibration card, not content).** Full table: `pool/SURVEY.tsv` (frame, class, date if legible, note,
and a `signature_screen` column for the two numeral hits). Classified by 6 Sonnet subagents (2 concurrent, per the
brief), each given <=19 low-res thumbnails, classification only (clear_text / numeral_code / code_with_shorthand /
other), no transcription. Breakdown: 80 clear_text, 27 other (printed pamphlets, customs-manifest tables,
citizenship/seaman-protection certificates, passports, one blank/foxed page), 2 numeral_code, 1 code_with_shorthand.

**The one code_with_shorthand hit, frame 0031, is not a new find** -- it is one of the target's own already-fetched
frames (the 29-33 range, ARM-IMG/ARM-TR), correctly re-flagged by the classifier since this survey did not exclude
the target's own frames from the 6-frame stride.

**Two numeral_code hits, both screened and both ruled out as office-code (THE=972) usage, not pool candidates:**
- **Frame 0025** (continuing from frame 0024, which carries the legible header "Paris 15 february 1808" -- read
  directly off the native-resolution image, not a low-res guess): a plain-English opening paragraph ("Sir, I have
  thought the enclosed documents sufficiently important...") running into a dense numeral block, closing in plain
  English ("With every sentiment of respect and consideration, Your most obedient and very humble Servant...") plus
  a French P.S. This date and structure match Bourdeau's already-known 15 Feb 1808 Armstrong-to-Madison letter
  (Founders 99-01-02-2703, NOTES.md's own "What the cipher is" section, Bourdeau's paired check reading it 72%
  coherent in THE=972) -- this pass is most likely the first direct manuscript look at that letter in this
  repository, not a new letter. One-line screen (12 groups from the first numeral line, `pool/signature_test.py`):
  THE=972_bourdeau.tsv coverage 7/12 (58%), digit-0/1 share 33%, digit-2/3/5/9 share 50%, top digit 1 -- looks like
  THE=972 usage (high coverage, not 0/1-skewed), consistent with the known identification. Not fetched to `pool/`
  (not a candidate; native crops kept only in scratch, not committed).
- **Frame 0643-0644** (near the end of the roll, between an unrelated "Dan Parker" letter at 0641 and a plain
  Armstrong letter re Spain at 0644's second leaf; a nearby docket at 0645 lists several 1807-1808 dates for a
  *different*, unidentified batch of "confidentially sent" Armstrong letters -- not confirmed to be this one):
  28+ lines of dense numeral groups, no shorthand marks, breaking briefly into plain text ("Friday. I called
  yesterday morning to talk upon what I could gather respecting our affairs...") before more numerals resume. Date
  not legible on this or the neighbouring frames (0638-0648 fetched at 600px, none carry this letter's own header).
  One-line screen (14 groups from the first numeral line): THE=972_bourdeau.tsv coverage 9/14 (64%), digit-0/1
  share 14%, digit-2/3/5/9 share 43%, top digit 2 -- and the line's own second value, 972, is THE=972's own
  namesake code (commonly "the"). Looks like THE=972 usage, not the target's signature (target: digit-0/1 share
  ~43%, digit-2/3/5/9 share ~13%, top digit 0). Not fetched to `pool/` (not a candidate).

**Verdict: this survey finds no sibling in the target's own private code on roll 14.** Both numeral hits found by
a 1-in-6 frame sample screen as ordinary THE=972 office correspondence, the same code ARM-A2's direct-transfer
sweep and ARM-C1's control already showed does not fit the target. This is a screen at N=12-14 groups per
candidate, not a control-backed result (rule 3 -- a one-line sample is too small for a shuffle test to mean
anything), and a 1-in-6 stride survey is not exhaustive: a short coded passage entirely between two sampled frames
would be missed. The next step, if this lane pursues the sibling-pool route further, is either (a) a full (every
frame) pass of roll 14 rather than a 1-in-6 stride, or (b) the same survey run over the *other* M34 rolls for
Armstrong's Paris legation (this target's letter is filed on roll 14 only because it falls in that roll's date
range; a private cipher used with a different, non-State-Department correspondent per Kreider's own suggestion
(NOTES.md "What is still open", item 5) would not necessarily be filed anywhere near it) -- neither attempted here,
per this job's scope.

Requests this pass: catalog.archives.gov (NARA IIIF) -- 4 info.json probes (frame range boundaries) + 1 native
frame-0033 fetch + 111 survey thumbnails (every 6th frame, 600px) + 21 neighbour-frame thumbnails (0020-0030,
0638-0648, 600px, to find extent around the two numeral hits) + 4 native-resolution fetches (0024, 0643, 0644, plus
one IIIF-region crop of 0643) = 141 total, all >=1.5s apart, descriptive User-Agent, no 429/403/challenge seen. No
other hosts. No logins, no credentials touched.

## ARM-S1 (26 Sept 2026, LANE ARM worker ARM-S1) -- shorthand mark inventory + period-system comparison, not a decode

Full detail in `HYPOTHESES.md`'s "ARM-S1 marks" section; data in `images/shorthand/INVENTORY.tsv` and
`images/shorthand/specimens/{manifest.tsv,comparison.tsv}`. Two independent Sonnet passes over ARM-TR's 29 line
crops found roughly 35-47 distinct graphic-mark shapes (merging is approximate, not pixel-reconciled) in a sharply
Zipfian frequency profile -- both passes independently described it as looking more like a syllable/word shorthand
than a flat symbol-for-letter substitution, without being shown each other's conclusion. Marks sit overwhelmingly
in unbroken runs of several to ~19 glued together at a line's start or end (not as single marks flanked by
numerals, which the bare `*`/`**` notation in `ciphertext.txt` would suggest), with a few pure-shorthand lines and,
newly found, superscript ticks sitting directly above (not beside) a numeral on two lines. Flag: two of ARM-TR's
crops (`page2_L02`, `page2_L06`) show almost none of the marks their own filenames claim -- a likely crop-region or
bookkeeping issue in that earlier pass, not fixed here.

Fetched an alphabet/consonant specimen plate for all 6 period systems Tomokiyo names (Taylor 1786 -- his own
already-known-negative crop, reused; Byrom 1796; Gurney 1752 -- a running specimen, not a clean plate, since the
book's 11 plates are all unpaginated front matter that a keyword search cannot isolate; Mavor 1792; Weston 1727;
Macaulay 1747) plus Pitman's 1837/1890 Phonography as a matched control (Victorian, geometric-line family, not
18th-c. cursive-loop). A ten-category qualitative shape comparison (`comparison.tsv`) scores the four richest,
loopiest 18th-c. systems (Taylor 7.5, Weston 7.0, Gurney 6.0, Mavor 6.0) above the two more minimal ones (Macaulay
5.0, Byrom 4.0), and all six above the geometric Pitman control (2.5) -- a real gradient, since the control
genuinely can and does score lower (rule 3). But Taylor, the already-published negative, scores at the TOP of this
table, not below the four untested candidates: a coarse "does a similar stroke-shape appear in this alphabet"
check cannot reproduce Tomokiyo's actual symbol-by-symbol negative, because generic loops/hooks/waves recur across
nearly every longhand-derived 18th-c. shorthand almost by construction. Conclusion carried to HYPOTHESES.md: this
comparison places the target's marks in the right general family (loopy cursive personal shorthand, not a
geometric or flat-substitution system) but is too coarse to pick out which of Byrom/Gurney/Mavor/Weston/Macaulay
(if any) is the actual source -- that needs a symbol-by-symbol frequency/positional match against each, the way
Tomokiyo ran it against Taylor, which is the next step for a successor and was not this job's brief.

Requests: archive.org ~35 (advancedsearch, metadata, `fulltext/inside.php` search-inside -- a route not previously
documented in CLAUDE.md's Access playbook table, used to jump straight to each book's alphabet-plate leaf by
keyword rather than paging through by trial and error -- and page-image fetches), cryptiana.web.fc2.com 1. All
>=1.5s apart, descriptive User-Agent, no logins.

## ARM-TR2 pass, 26 Sept 2026 (LANE ARM worker ARM-TR2) -- manuscript completion, page1 L6-13 root-caused

Finished ARM-TR's manuscript-verification thread. Full numbers in HYPOTHESES.md's "ARM-TR2 manuscript
completion" section; this is the narrative.

**Frame 0033 transcribed, exact match.** The native image is a two-document spread: its LEFT page is
this letter's own last leaf (the final 4 numeral lines, closing, signature "Wm Armstrong", and address
"M. Madison Secretary of State of the United States Washington"); its RIGHT page is a different, later
letter dated "Paris 27 february 1808" (mixed plain-and-cipher, not this target, not transcribed). Two
fresh blind Sonnet passes over the left page's 4 lines, two edge-of-crop digits settled by this worker
from the crop directly: the full 37-group tail reads **79 14 1160 1376 1740 18 38 764 364 1240 | 1160
1401 176 671 604 4 560 38 1207 160 | 380 87 768 14 870 462 47 648 140 1207 981 | 5 760 47 38 580 170**
-- an exact match against `ciphertext.txt`'s own final 37 groups, zero substitutions.

**Page-1 lines 6-13: the "54 unmatched groups" was mostly a crop bug, not a transcription-vs-manuscript
divergence.** Two fresh independent blind Sonnet passes over ARM-TR's own `crops_0030` L06-L13 images
disagreed with each other about as much as ARM-TR's original two passes did -- but comparing all four
passes together against a **re-crop with ~90px of extra top margin** (done directly by this worker with
PIL, not a subagent, after noticing the reconciled passes kept finding line-initial tokens ambiguous)
showed why: ARM-TR's own crop bands for lines 6-11 were cut too close to the top, silently shearing off
each line's first 1-2 tokens and the *tops* of some digits. That crop defect, not shorthand-vs-digit
ambiguity, is why FOUR independent blind passes (ARM-TR's original two plus this job's two fresh ones)
all read "43" at the start of line 9 -- with the extra top margin the same ink plainly reads **"61. 45."**,
matching `ciphertext.txt` exactly. The same fix recovers "76 1340" (line 6 head), "341 1476" (line 7
head), "88 1340" (line 8 head), and "143" (line 11 head) -- all confirmed by direct pixel-level crop
inspection (screenshots taken and checked, not left to a subagent), all now matching `ciphertext.txt`
exactly. **Before/after** (`tr/diff_ms_vs_ciphertext.py`, first-332-of-369 range ARM-TR covered):
substitutions 14->9, in_ciphertext_not_ms 54->12 (across the WHOLE now-369-covered letter; within just
the L6-13 span specifically, the residual is 2: ciphertext.txt's own "2" and "44" at the L11/L12
boundary, most plausibly folded into L12/L13's own dense mark runs rather than genuinely absent).
match_ratio 0.884 -> 0.957.

One genuine digit substitution survives in this span, now confirmed by 4 independent passes plus this
worker's own direct crop check: line 7's manuscript reads **"200"** where `ciphertext.txt` has **"203"**
-- a real transcription difference, not a crop artifact, in the same units-digit family (0<->3) as
ARM-DESIGN's own caveat, though (like the earlier 1841/1843 case) this is one more isolated instance,
not a systematic pattern (the full-letter units-digit table below still shows no systematic skew).

**What genuinely remains unresolved, honestly:** lines 12 and 13 (16 and 19 marks in ARM-TR's original
count) were re-cropped with the same extra top margin and show **no hidden digits** -- unlike lines
6-11, these really are dense, near-solid runs of shorthand marks with no numeral shapes visible at any
crop margin tried. Against this, `ciphertext.txt`'s own notation at the same sequence position is
minimal: just "2, **, 44" (one digit, one "several-marks" passage code, one digit) where the manuscript
shows two entire lines of marks. This is a real, unexplained density mismatch between Bourdeau's
transcription and what the manuscript actually shows here -- flagged for a successor (a symbol-by-
symbol shorthand-system match, per ARM-S1's own next step, is the only way this is likely to resolve
further), not something this job could adjudicate from the image alone. Similarly, this pass's own new
finding of a clear "13" inside line 10's mark run, and the original "31" at the end of line 9's mark
run, have no corresponding digit in `ciphertext.txt` at that position (folded into a mark passage there
too) -- graded M, reported as found, not force-matched.

**Page2 L02/L06 shorthand-crop bug (ARM-S1's flag): diagnosed and the two named files fixed.** Both
were pulled from `images/crops_0031L`'s raw `f0031L_L0N.jpg` filenames directly, without the +1 line-
index correction that `tr/page2_passA_shift.tsv` already applies when reconciling the actual
transcription passes -- `crops_0031L` (unlike `crops_0032L`) has one extra faint/blank line at the very
top of its own crop set before its real content starts (confirmed by direct comparison: `crops_0031L`'s
own `L01.jpg` is a near-blank margin with a faint archival number, not line 1 of the letter), so its
"L02" file is actually manuscript content-line 1, and its "L06" file is actually content-line 5. Fixed
by replacing both named files (`images/shorthand/page2_L02_seq198-212_15marks.jpg`,
`.../page2_L06_seq250-264_12marks.jpg`) with the correctly-indexed crops from `crops_0032L` (verified:
L02 now shows the true all-marks line, L06 now shows `* 45 147 1158` plus its own trailing marks,
matching the mark counts already recorded in `INVENTORY.tsv`/`index.tsv`, which were computed from
`ciphertext_ms.txt`'s own content and were never wrong -- only the image files pulled for them were).
**Not fixed here, flagged for a successor:** spot-checked `page2_L04` and confirmed the identical
one-line shift; every other page2 shorthand crop (L01, L03, L04, L07, L10, L11, L13) almost certainly
has the same bug and should be re-derived from `crops_0032L` before a family-S job trusts that folder.

**Units-digit distribution, full letter now (349-355 ms tokens vs ciphertext.txt's 369, values as
digits, `?`/`^`-suffixed digits counted at face value):**

| digit | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| ms (>=100 only) | 89 | 44 | 9 | 4 | 25 | 2 | 22 | 21 | 12 | 2 |
| ciphertext.txt (>=100 only) | 92 | 47 | 9 | 3 | 26 | 2 | 22 | 22 | 12 | 2 |

Shapes match closely (0 and 1 dominant, 2/3/5/9 rare) across the whole letter, not just the previously-
covered range -- no systematic 2/3/5/9 misreading anywhere, consistent with ARM-TR's own original
finding and now checked against the complete letter including frame 0033.

`ciphertext_ms.txt` now has a `# --- page 4 ---` section (frame 0033) and covers the whole letter by
position. `tr/diff_ms_vs_ciphertext.py` fixed to also recognise a trailing `^` (superscript-tick
marker) on a digit group, not just `?` -- it was silently dropping those tokens from the ms count
before this fix (own bug, caught and corrected this pass, not left in).

No network this job (all four subagent calls and all direct crop work against images already on disk;
`pip install numpy pillow` run locally to use `tools/iiif_lines.py`, no host requests). 4 Sonnet
subagent calls total (2 concurrent x 2 rounds): frame 0033's 2 blind passes, page-1 L6-13's 2 blind
passes. All further settlement (frame-0033 edge digits, the L06-L11 crop-top-margin fix and re-read,
the page2 shorthand-crop diagnosis and fix) done directly by this worker against the source images.

## ARM-REC3 pass, 26 Sept 2026 (LANE ARM worker ARM-REC3) -- Founders apparatus recovered, loc.gov Armstrong pool screened, Livingston/Pinkney resolved

Full detail in `crib_sources.md`'s "ARM-REC3 pass" section; `pool/LOC-ARMSTRONG.tsv` has the 20-item pool table.
Short version: **web.archive.org is reachable again this pass** (unlike the two consecutive outages ARM-REC/
ARM-REC2 found), though individual document fetches still need 1-3 retries about half the time (host-side
instability, not a proxy fault). Fetched the target letter (99-01-02-2728) via Wayback: **its own Early Access
page carries no editorial note or footnote at all, only the bare source citation** ("DNA: RG 59—DD—Diplomatic
Despatches, France.") -- there is no apparatus to have missed. Fetched and read 9 of the 13 previously-titled-only
document ids (99-01-02-2907 could not be reached, CDX timeout x2): none references the 20 Feb letter, a
duplicate, a changed cipher, or names a specific private-code correspondent. **Resolved the 7484-vs-7514
question**: 7484 is the same letter as 2745 (25 Feb, Madison to Jefferson, cross-listed between collections, not
a distinct letter); 7514 is a genuinely different letter (29 Feb, a Senate report on impressed seamen). New
context, not decisive: 8003/3082's own letter also says "I send letters from Armstrong, Pinkney & Harris"
together (routine mail-forwarding, not evidence of a shared cipher); 8006 and 8708 both show Erving being
forwarded alongside Armstrong at exactly this period, corroborating Erving as a live correspondent (one of
Kreider's own named candidates) without confirming a cipher link.

**loc.gov independent search**: built a 20-item pool (`pool/LOC-ARMSTRONG.tsv`) of Armstrong-Madison and
Armstrong-Jefferson correspondence, 1807-1809, from the James Madison Papers and Thomas Jefferson Papers
collections. **New finding: a standing, multi-year direct Armstrong<->Jefferson private correspondence channel
exists (13 items, March 1807 to September 1809), separate from the official Armstrong-Madison State Department
channel and not named in Kreider's own candidate list** (Pinkney, Monroe, Erving, Livingston, the New York
circle). Fetched page-1 thumbnails for 14 pool items and had one Sonnet subagent classify each: **all 14 read
clear_text, no numeral groups visible** -- a real negative at the page-1 granularity checked (2 of the 14 items
are 10-12 pages long; only page 1 of each was sampled, so a later coded passage is not ruled out). Two same-date
items (Armstrong to Madison and Armstrong to Jefferson, both 20 Oct 1808) are flagged, not resolved, as possibly
the same letter cross-filed.

**Livingston**: broad site-wide name-pair search returned 605 hits of pure noise; narrowed to the Madison Papers
collection, `dates=1807/1809`, dropping the "Armstrong" term (the combined query returned 0): found 5 genuine
Livingston-to-Madison letters in the window, including one dated **5 Feb 1808, fifteen days before the target
letter** -- confirms Livingston was an active State Department correspondent at exactly this time, though none of
these letters is Livingston<->Armstrong directly and none was read for content this pass (out of step 2's scope).
Flagged as the most promising unread lead for a successor.

**Pinkney**: name-pair query (`"William Pinkney" Armstrong`, Madison Papers, 1807-1809) returned **0 hits**;
broadened to Pinkney alone, 43 hits, all Pinkney<->Madison or Pinkney<->third-party, no direct Pinkney<->Armstrong
item found -- a genuine negative, extending ARM-REC's earlier "wrong direction" finding.

**Net effect on family E**: no key, decode, or coded sibling letter found in either the Founders apparatus or the
loc.gov Armstrong/Jefferson pool. The direct Armstrong-Jefferson channel is new information (not previously on
file, not in Kreider's list) but shows no cipher on the pages sampled; Livingston's 5 Feb 1808 letter is an
unread, plausible lead. Status stays open (rule 5); no NEAR.md row.

Requests: web.archive.org ~13 (1 reachability + CDX/fetches for 11 document ids, 2 CDX timeouts on one id, ~1-3
retries per successful fetch). loc.gov ~21 (2 collection searches, 14 item-metadata fetches, 4 name-pair
queries, 1 spot fetch). tile.loc.gov: 14 thumbnail fetches. All >=1.5s apart, descriptive User-Agent. No logins,
no credentials touched. 1 Sonnet subagent (thumbnail classification only, per this brief's cap).

## ARM-S2 pass, 26 Sept 2026 (LANE ARM worker ARM-S2) -- shorthand symbol-by-symbol match, exclusion not identification

Ran the finer, symbol-by-symbol method (the way Tomokiyo actually compared Taylor) against all five untested
period systems (Byrom, Gurney, Mavor, Weston, Macaulay), with Taylor as the known negative and Pitman as the
control. Full numbers in `HYPOTHESES.md`'s "ARM-S2 symbol match" section. Reconciled the two cycle-1 passes'
inventories into 12 shapes (visually verified by subagent crop checks, not just numeric coincidence -- some of
ARM-S1's own qualitative C1-C10 merges turned out to be only "partial" on inspection), covering 189 of ~221.5
total marks (85.3%). The dominant shape (33.9% of all marks) is too frequent to be any single English letter or
common word in every system tested including the control -- a script-based profile check
(`images/shorthand/profile_check.py`) confirms this fits neither a letter-alphabet nor a Zipf word/syllable-sign
hypothesis, and is more consistent with a structural/connector stroke. None of the five candidates clears both
of rule 3's bars (beat Taylor by a real margin AND give a frequency-consistent profile): Mavor and Byrom beat
Taylor on raw shape-match score but assign the two dominant shapes to letters whose real frequency is nowhere
near that high (Tomokiyo's own failure mode against Taylor); Macaulay ties Taylor (no resolving power);
Weston scores below even the Pitman control (a method failure, not evidence against Weston); Gurney's apparent
top score is an artifact of its specimen being running prose, not an alphabet chart -- most of its matches turned
out to be ordinary page furniture (scribal tittles, an ampersand, i-dots, a closing flourish), not real
shorthand signs. Result: **exclusion of all six systems checked (Taylor + the five candidates)**, with the
control on file, per rule 5/CLAUDE.md's near-solve conventions this stays `partial`/marks-as-shorthand-family
open, not `closed-negative` (no full family ladder has been run). The marks most plausibly remain a private
shorthand or the code's own device. Superscript tick above a numeral confirmed the same physical stroke as the
ordinary baseline dash, just repositioned, not a separate character; both Mavor's and Weston's subagents
independently (and without seeing each other's or ARM-S1's finding) suggested this stroke resembles those two
systems' own vowel-position marking convention -- an M-grade lead for a successor, not a claim. Attempted the
optional NARA superscript-tick check on Armstrong's ordinary office-code letter (frame M34-014-0025, the known
15 Feb 1808 letter); both allowed requests via the already-documented keyless IIIF route returned the site's
HTML app shell instead of the image (same failure signature as an invalid object path); not retried further
(request cap and the good-citizen one-retry rule both spent); flagged for a successor to re-derive the working
route before trying again. No numerals or ciphertext read or decoded this pass; rule 10 wording throughout.
Requests: catalog.archives.gov 2 (both unsuccessful, no image bytes received), >=1.5s apart, descriptive
User-Agent. No other hosts, no network for the reconciliation/comparison work itself (all against images
already on disk plus 9 Sonnet subagent calls: 2 reconciliation + 7 per-system symbol match).

## ARM-POOL2 (26 Sept 2026, LANE ARM worker ARM-POOL2) -- docket frame 0645 read; 4 of 6 items located, all THE=972, none a pool candidate

Full detail in `pool/DOCKET-0645.tsv` and `pool/SURVEY.tsv` (frames appended this pass). Fetched frame
M34-014-0645 at native resolution (committed, `images/M34-014-0645.jpg` -- the docket of record for this
pass's finds) and read it directly: its left page is headed "List of Genl Armstrong's letters. Extracts from
which were confidentially sent to [word illegible]", listing six items (1st-6th) by date; its right page is
an unrelated bound-in French printed document ("Douanes Imperiales... 1er Aout 1810"), not part of the list.

**Four of six docket items located and signature-screened, all THE=972 office code, none matching the
target's signature:**
1. **27 Dec 1807** -- NOT on roll 14 (which starts 22 Jan 1808). Found roll 13 instead (NAID 188671172,
   "Nov. 12, 1804-Dec. 27, 1807", 392 images, discovered via a `catalog.archives.gov` search restricted to
   `"Despatches from United States Ministers to France" "Reel 13"`; same IIIF container id, `603720`, as
   roll 14). Frame 0390, right at the end of the roll (0393 is the roll's own "END OF VOLUME" card): a
   "Duplicate" letter dated "Paris December 27 1807", signed John Armstrong, dense THE=972 numerals --
   screen 70% THE=972 coverage. Notably carries period interlinear pencil/ink plaintext glosses written
   directly above several numeral runs, consistent with this being one of the roll-13 marginal-annotation
   letters Bourdeau's own `THE972_bourdeau.tsv` was already built from (this file's own "What the cipher is"
   section), not a new key source.
2. **22 Feb 1808** -- roll 14, frames 0033 (right page)-0034. **Correction to ARM-TR2**: that pass read this
   frame's right-page letter as dated "Paris 27 february 1808"; a direct native-crop re-read this pass shows
   the date is **22**, not 27 (the hand's "2" and "7" are both loopy and easy to conflate) -- this is
   Armstrong-to-Madison, 22 Feb 1808, docket item 2, not a separate unidentified letter. Clear prose (signed
   John Armstrong, addressed "M. Madison") carrying two embedded THE=972 numeral passages -- screens 92% and
   71% THE=972 coverage. One passage is followed, in the same hand, by its own plain-English paraphrase
   ("972.1394.1090.1354.914.985.608.899.1482.1228.1492.297.1001. Prussia is to seize Finland, while France &
   Denmark take possession of Sweden. 76.736.1587.910.369.630.1478.860.1090.758.1282.1284.823. And it is
   certainly amongst the most cruel circumstances of the British attack on her capital") -- most plausibly
   Armstrong quoting an intercepted or reported foreign-cipher specimen together with its own decode as
   intelligence content, not this letter's own device. Not chased further (out of this job's scope; flagged
   for a successor interested in THE=972 provenance or period cipher specimens generally, not the target).
3. **9 March 1808** -- roll 14, frames 0039-0040 (heading "9 March 1808" on 0040; journal-style entries for
   "Friday" and "6 March" on 0039). Screen (frame 0040, 21 groups): 86% THE=972 coverage. **Resolves
   ARM-POOL's own open question about frames 0643-0644** ("date not legible... candidate sibling to the 20
   Feb 1808 target code"): a direct native read of 0643 this pass is a word-for-word, number-for-number match
   to frame 0039 (identical "Friday" heading, identical opening 16 groups
   `276.962.972.676.1354.395.1701.1248.1482.988.1092.1268.1090.1013.734.967`, identical opening sentence "I
   called yesterday & this morning to tell you what I could gather respecting our affairs. What has been
   transmitted to..."). Frames 0643-0644 are a duplicate filing of this 9 March 1808 despatch (period
   practice: despatches were often sent in duplicate via different routes, per the 27 Dec 1807 letter's own
   postscript about sending copies "via England" and another route) -- THE=972, not an unidentified letter,
   confirming ARM-POOL's own signature screen of that frame was correctly negative.
4. **15 March 1808** -- roll 14, frame 0045 alone: "Duplicate" header, "15 March 1808, Paris", signed John
   Armstrong, addressed "Mr Madison, Washington". Screen (23 groups): 83% THE=972 coverage.

**Item 5** ("Note referred in the above from Genl Armstrong", undated) is not a separately dated item: the 15
March letter's own text names it ("I accordingly wrote the note, a copy of which is subjoined to this
letter, pointing out in a few words the property to which that rule would apply"), immediately followed by
one more THE=972 numeral block within frame 0045 itself. The adjacent frame 0046 carries a French-language
clear-text item headed "Note." on a related neutral-property/sequestration subject -- plausibly this
enclosure, not confirmed, not screened further (clear text, not a numeral-code candidate).

**Item 6** ("Private to Mr M[adison]: 30th august", no year given) **not located within this job's budget.**
Searched roll 14 frames 0115-0134 (dated Armstrong-to-Madison letters found: 7 Aug 1808 f.0115, 23 Aug 1808
f.0121 already in `pool/SURVEY.tsv`, 26 Aug 1808 f.0125-0127 plain text with no numerals, 4 Oct 1808 f.0131);
no frame in that span carries a "30 August" header or an explicit "Private" designation. The docket gives no
year for this item (items 1-4 span Dec 1807-March 1808, so "30th August" could be 1808, 1809 or 1810) -- not
chased further past this job's per-date thumbnail budget.

**Verdict: no pool candidate found.** All four located docket items, plus the now-identified 0643-0644
duplicate, are THE=972 office-code usage (58-92% THE=972_bourdeau.tsv coverage on one-line screens, digit
shapes not matching the target's 0/1-dominant signature) -- consistent with ARM-A2's and ARM-C1's own
findings that THE=972 is not the target's code, and with ARM-POOL's own roll-14 stride survey finding no
sibling. This is a screen at N=14-27 groups per item, not a control-backed result (rule 3). The docket's own
significance is now explained (it lists a confidentially-forwarded batch of Armstrong's ordinary,
THE=972-coded despatches, not a private-code correspondence), which is itself useful: it removes one more
avenue (the frame-0645 batch) from the family-E sibling hunt without finding the target's own code.

Requests: catalog.archives.gov -- 1 info.json + 1 native (frame 0645) + 3 thumbnails (0034-0036) + 1 native
(0034) + 5 thumbnails (0038-0042) + 2 native (0039, 0040) + 5 thumbnails (0044-0048) + 1 native (0045) + 5
thumbnails (0122-0126) + 4 thumbnails (0127-0130) + 4 thumbnails (0131-0134) + 1 native (0643, to confirm the
0039/0643 match) + roll 13: 4 thumbnails (0388, 0390, 0392, 0393) + 1 native (0390) = 39 total, all >=1.5s
apart, descriptive User-Agent, no 429/403/challenge seen. `tools/browser_fetch.js` used 3 times (a roll-13
search query, a narrower "Reel 13" query, and the roll-13 item page) to find roll 13's NAID and its own IIIF
object-path prefix, per ARM-IMG's own documented route. No other hosts, no logins, no credentials touched.

## ARM-LIV pass, 26 Sept 2026 (LANE ARM2 worker ARM-LIV) -- the five Livingston-to-Madison letters read for content

Full detail in `crib_sources.md`'s "ARM-LIV pass" section; `pool/LIVINGSTON.tsv` has the per-letter table. ARM-REC3
(family E, above) located five Livingston-to-Madison letters in the loc.gov window 1807-1809 but did not read them;
this pass read all five, 5 Feb 1808 (fifteen days before the target) first. **Result: all five are wholly clear
text, no numeral groups on any page, and none references a cipher, a key, or private correspondence between
Livingston and Armstrong** -- the Livingston lead ARM-REC3 flagged as "the most promising unread lead" is now
closed as a negative (a search result, not a control-backed test, since there was no coded passage to screen).
Two letters are flagged for the record though neither bears on the target: 22 Mar 1807 contains a genuine period
"cypher" reference, but about the already-public Burr/Wilkinson conspiracy cipher, not Armstrong's ("What folly led
him to write in cypher without having previously settled a key? And by what means has his letters been
deciphered?"); 8 Jan 1808 mentions "keeping open the intercourse with Genl Armstrong" but only as the ordinary
diplomatic pouch for forwarding a personal family letter, not a private code. Founders Online text was reached for
2 of 5 (17 May 1807, 24 Jan 1809); the other 3 had no Founders id locatable by WebSearch and were read from
tile.loc.gov page images instead (thumbnails for all pages, native resolution for 22 Mar 1807's cipher-relevant
passage). This does not touch WE027 (Livingston's own unpublished code, Weber 1979 pp.154/188, NOTES.md line 96),
which stays untested for lack of a reachable table. Family E: no pool candidate from this lead; status stays open.

Requests: loc.gov 6 (1 collection search + 5 item-metadata fetches). tile.loc.gov 8 (7 thumbnails + 1 native-res
fetch). web.archive.org 5 (2 CDX + 2 document fetches all succeeded; 1 CDX query failed twice, not retried
further). All >=1.5s apart, descriptive User-Agent, no logins, no credentials touched. No subagent used.
