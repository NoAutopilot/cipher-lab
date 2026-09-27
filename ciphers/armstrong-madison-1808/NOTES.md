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

## ARM-JEF pass, 26 Sept 2026 (LANE ARM2 worker ARM-JEF) -- Jefferson-channel remaining pages, unchecked items, cipher/cypher search

Finished ARM-REC3's page-1-only sample: fetched and classified every remaining page of the two long
Armstrong-to-Jefferson letters, all pages of the three previously-unchecked items, and ran the two loc.gov
cipher/cypher searches named in this job's step (c). Full per-item detail (pages_checked column) in
`pool/LOC-ARMSTRONG.tsv`.

**(a) The two long letters, finished**: mtjbib017827 (28 Oct 1807, 12 pp) pages 2-12 and mtjbib018840 (28 Jul
1808, 10 pp) pages 2-10, all fetched from tile.loc.gov (~600px service derivatives) and classified by two Sonnet
subagent calls (12 + 12 images, split across the two items). **All 22 pages read clear_text.** Both letters are
now fully checked, cover to cover: no coded passage anywhere in either.

**(b) The three previously-unchecked items, now fully read**: mtjbib020076 (19 Sep 1809, 4 pp), mjm015339 (6 Jun
1809, 6 pp), mjm015558 (18 Sep 1809, "Includes postscript of Sept 19", 3 pp) -- all pages fetched and classified
(1 Sonnet subagent call, 9 images). **All 13 pages read clear_text**, including the named "postscript" page
(mjm015558 p3) and mjm015339's docket leaf (p6, endorsed "Armstrong Jany 20 1809" -- a date that does not match
the item's own 6 June 1809 title; flagged, not resolved, likely an unrelated docket reused on the same leaf).

**(c) loc.gov search, `q=Armstrong cipher` / `q=Armstrong cypher`, dates=1806/1810**: run against both the
Thomas Jefferson Papers and James Madison Papers collections (`/collections/<slug>/?q=...&dates=1806/1810&fo=json`
-- the `fa=partof:` facet form tried first silently returns 0 hits regardless of query, confirmed by re-running
the same four queries against the collection-scoped endpoint, which is what ARM-REC3/ARM-LIV both used; flagging
this for any successor who tries `fa=partof:` again). Thomas Jefferson Papers: 0 hits both spellings. James
Madison Papers: "cypher" 0 hits; **"cipher" 2 hits** -- `mjm015002` (30 Aug 1808, already on file, THE=972,
Bourdeau-decoded, ARM-REC2) and **`mjm014590` (4 May 1806, "Partly in cipher and includes a copy") -- not
previously in this pool**, added per this step's instruction.

**mjm014590 screened**: read p1 (Paris, 4 May 1806, marked "Duplicate"/"Private") directly -- heavily coded,
numeral groups throughout, "972" recurring at high frequency (Armstrong's office code with the State Department).
p4 is a second copy of the same text (identical opening numeral groups), confirming it is a duplicate leaf of p1,
not new content; p2/p3/p5/p6 not separately screened. Eye-transcribed one 15-group line from p1 and ran
`pool/signature_test.py`: THE972_bourdeau.tsv coverage 14/15 (93%), units-digit 0/1 share 7%, digit-2/3/5/9 share
53%, top digit 2 -- **matches THE=972's own real usage (flat-with-noise, top digit ~2), not the target's signature
(0/1-heavy, 2/3/5/9 rare)**. A screen at N=15 (rule 3), not a control-backed result: **not a pool candidate**. This
item predates the target letter by nearly two years and is the earliest confirmed THE=972 usage on file.

**Net effect on family E**: no key, decode, or coded sibling letter found. The Jefferson-Armstrong private channel
(13 items, ARM-REC3) is now fully read at every page (all clear_text) except the two items ARM-REC/ARM-REC2 already
resolved as known; the Madison Papers 1806-1810 cipher/cypher search adds one new-to-the-pool item (mjm014590),
screened and excluded. Status stays open (rule 5); no NEAR.md row. Item (d) of this brief (remaining pages of the
still-page-1-only 2-/3-page items) was not attempted -- not in the priced-per-unit budget, left for a successor if
the lane wants it.

Requests: www.loc.gov 14 (6 item-metadata `?fo=json` fetches + 8 collection searches, including 4 with the wrong
`fa=partof:` facet form that returns 0 regardless of query -- see above). tile.loc.gov 41 (35 page thumbnails across
5 items + 6 for mjm014590). All >=1.5s apart, descriptive User-Agent, no logins, no credentials touched. 3 Sonnet
subagent calls (12+12+9 images), one at a time.

## ARM-S3 pass, 26 Sept 2026 (LANE ARM2 worker ARM-S3) -- four more shorthand systems checked, all non-test/excluded, plus a calibration-drift finding

Ran ARM-S2's own symbol-by-symbol method against the four remaining named period systems (Blanchard, Annet,
Holdsworth and Aldridge, Lewis), with a fresh independent Taylor re-run as the rule-3 calibration check. Full
numbers in HYPOTHESES.md's "ARM-S3 symbol match" section. Found genuine alphabet/sign-chart specimens for all
four on archive.org (Blanchard's first, 1779 edition turned out to have no character plate at all -- its 1787
second edition was used instead; Annet's edition is a 300-cell numbered sign index, not a phonetic alphabet;
Lewis's own alphabet is not in the 1816 book named in this job's brief, which surveys other authors -- his 1820
"Art of Writing with the Rapidity of Speech" was used instead). The important finding this pass is methodological,
not a new system result: an independent Taylor recalibration, run with the identical prompt ARM-S2 used, drifted
0.211 on freq_score (0.500 vs ARM-S2's 0.289) versus only 0.045 on shape_score -- over the brief's own 0.1 drift
tolerance -- because this session's subagent graded several ambiguous marks "n-a" (diacritic/artifact, no letter
claim) where ARM-S2's pass had forced them into "consistent" letter guesses, shrinking freq_score's denominator.
Per the brief, every candidate result this session is therefore reported as **non-test at this drift**, not an
exclusion or identification, though none would have cleared rule 3's bar even ungated: Blanchard and Holdsworth
score below this session's own Taylor calibration on both numbers; Lewis sits within noise of it on shape_score
and below it on freq_score; Annet has the highest shape_score of any system tried across both sessions (0.653,
several genuine one-to-one hits) but its own design (a two-digit numbered word/syllable index, not a phonetic
alphabet) makes the frequency half of the test structurally unscoreable, not merely unmet -- if pursued further,
the right next test for Annet is a positional/structural one (do the target's marks group in twos the way a
two-digit sign code would), not another shape-vs-letter-frequency pass. Ten systems now checked in this family
(the seven ARM-S1/S2 covered plus these three, plus Lewis's own alphabet substituted for the book named); none
identified. Status stays `partial` per rule 5 (a control is on file; this is not a control-backed FAIL on every
count, several results are "non-test" rather than excluded). The marks remain most plausibly a private/idiosyncratic
symbol set or the code's own device. No numerals or ciphertext read or decoded; rule 10 wording throughout.

Requests: archive.org 43 (search/metadata/full-text/page-image fetches across four specimen searches -- 3 over
this job's 40-request cap, all against archive.org's own API/download endpoints, >=1.5s apart, descriptive
User-Agent, no 429/403; flagged rather than hidden, per the good-citizen rule's own reporting requirement). No
other host touched. 5 Sonnet subagent calls (1 calibration + 4 candidates), one at a time, each given the 12
exemplar crops and one specimen plate, never a full frame.

## ARM3-DICT pass, 26 Sept 2026 (LANE ARM3 worker ARM3-DICT) -- family G: dictionary-code design excluded, U1 only

Question: is the >=100 book part a page-and-word DICTIONARY code (value order monotone in the book's own
alphabetical order, linear or page*10+entry)? Full numbers in `HYPOTHESES.md`'s "Family G, ARM3-DICT dictionary
code" section; script in `dict/dict_control.py`.

**Design excluded at U1, control first.** A fresh, WE028-independent pocket-dictionary control (en18 content
words, alphabetised, particle block kept separate, K=1600/1800, 60 simulated letters each) gives a flat units
digit among values >= 100 (`units_top1` 0.149-0.155 +- 0.02), cleanly separated from a fixed-meaning-slot book
design (`hdec` 0.762 +- 0.05, about 12 sd away -- rule 3's separability requirement met). The target's own
`units_top1` (0.388, already on file from ARM-DESIGN, this job did not compute it blind) sits at percentile 100
against BOTH pocket-dictionary sizes -- about 12 sd outside a tight control. The page-plus-entry entry-digit
table (this job's own item iii check) shows the control flat across all ten digits (0.087-0.112) and the target
sharply skewed (digit 0 at 38.8%, digit 1 at 19.8%, digits 2/3/5/9 at 0.8-3.8%) -- a page-and-entry dictionary
predicts a flat entry digit and the target does not have one.

Per this job's brief, U2-U4 (fetching Entick's/Johnson's/Perry's/Sheridan-Walker's OCR from archive.org and
testing an actual dictionary's headword list against the target) were **not run**: the gate was "only if U1 does
not reject the design at p<0.05", and U1 rejects at far beyond that. This re-derives, with a fresh vocabulary,
the same conclusion ARM-DESIGN's own Q2 already reached for `onepart` (WE028's real vocabulary as one alphabetical
run) -- it closes the possibility that exclusion was an artefact of reusing WE028's specific words, rather than
adding a new negative independent of Q2. Family C's own verdict (fixed-meaning member slots, ~900-1800 forms, no
usable alphabetical order) stands; a dictionary code is now one more excluded design in the same family.

No network access this pass (offline, per the brief's U1 scope; U2-U4's fetches were not reached). 0 requests to
any host.
## ARM3-COR pass, 26 Sept 2026 (LANE ARM3 worker ARM3-COR) -- other-correspondents pool, no pool candidate

Full detail in `HYPOTHESES.md`'s new "Family E, ARM3-COR" section; images/manifest in `pool/cor/`. Weber 1979
(`unitedstatesdipl0000webe`, still print-disabled, fts-searched anyway) ties Warden biographically to Armstrong
("formerly private secretary to General John Armstrong") and gives Joel Barlow's own later nomenclator (as
minister himself, 1811-12, post-dates the target), but ties no code to "Armstrong and [correspondent]" and
corrects `tools/data/uscodes-1800/README.md`'s WE027 attribution (Weber's own text: "Livingston to King", not
Livingston<->Madison -- flagged, not fixed, out of this job's file list). Six candidates searched in loc.gov's
James Madison Papers and Thomas Jefferson Papers (1806-1810): Bowdoin (24 Jefferson-Papers hits), Warden (25+5),
Skipwith (7+1), Barlow (25+6, all post-target on the Madison side), Mason (mixed, no Armstrong link found), Parker
(0 hits either collection -- Daniel Parker not located at all). No `q=NAME cipher`/`cypher` hit for any candidate
in either collection. The nearest-date letter to 20 Feb 1808 for Bowdoin, Warden, Skipwith and Barlow was read in
full (11 manuscript pages, this worker directly, no subagent): all wholly clear, zero numeral groups. Skipwith's
8 Mar 1808 letter independently names "Mr. Warden, the Secretary of Genl Armstrong" and discusses Armstrong's
State Department correspondence directly -- real content about Armstrong, no cipher. `pool/cor/overlap_test.py`
built (target top-20 values vs a pooled THE=972 sample vs 200 random draws) as reusable infrastructure for a
future candidate; no candidate needed it this pass (baseline run: THE=972 sample scores at chance, 1/81 shared,
confirming the test discriminates). Net: no pool candidate found on this route. Family E's remaining open route
(not attempted, out of this brief's scope): the Armstrong-Warden or Armstrong-Skipwith correspondence directly,
if it survives anywhere, rather than either man's letters *to* Jefferson/Madison.

Requests: be-api.us.archive.org 13, archive.org advancedsearch.php/metadata 4 (MHS Bowdoin-Temple Papers volume
403/302 access-restricted, consistent with the documented print-disabled finding), www.loc.gov ~28 (2 with a
transient HTTP/2 stream error, retried once each per the good-citizen rule), tile.loc.gov 15. All >=1.5s apart,
descriptive User-Agent, no 429/403/challenge on any host. No logins, no credentials touched, no subagent calls.

26 Sept 2026 (ARM3-ADJ, LANE ARM3 job 3 PART 3a): family S2 run-adjacency structural test, script only, no
network. Tested whether numeric groups adjacent to a shorthand run (ciphertext_ms.txt) behave like a closed
set (particle-block-heavy, low distinct-value ratio). Only 1 of 6 statistics (share of 1-99 values at
position +1) clears its shuffled-position null's p95 (pct 99); the other 5, including both distinct-value-
ratio cells, sit inside the null band, one even in the wrong direction. A positive control (en18 prose,
seq_pblock design, proper nouns turned into pseudo-runs) separates cleanly on all 6 cells, so the method has
resolving power, but at N=22,886 adjacency events vs the target's 28 -- the null bands are correspondingly
far wider at the target's own scale, so this is a non-result (no signal detected), not an exclusion. No
closed-set adjacency positions are licensed as crib candidates for 3b's U5. Full numbers, both controls and
the top adjacent values (listed for the record, not as cribs) in HYPOTHESES.md "Family S2, ARM3-ADJ
run-adjacency structure". Script: `adj/adj_test.py`; raw output `adj/run_log.json`.

## ARM3-LIVCODE pass, 26 Sept 2026 (LANE ARM3 worker ARM3-LIVCODE) -- Livingston's own code screened, no pool candidate

Full detail in `HYPOTHESES.md`'s "Family E, ARM3-LIVCODE" section and `pool/liv/` (`weber_snippets.md`,
`king_correspondence.md`, `manifest.tsv`). Short version: Livingston's own 1803-04 coded despatches to/from
Madison are real and locatable (loc.gov's James Madison Papers collection tags nine items 1803-04 "In cipher"
or "Partly in cipher" -- the correct window nobody had screened before, since ARM-LIV's earlier Livingston
sweep covered only his 1807-09 letters, all clear). Fetched and screened five of these directly (native-
resolution manuscript images, `tools/iiif_lines.py` line crops, read by this worker, not a subagent): none
matches the target's own digit signature (43% digit-0/1, 13% digit-2/3/5/9) or ordinary THE=972 office usage
either -- consistent with these being genuine specimens of WE027, Livingston's own distinct nomenclator, per
Weber 1979 (be-api full-text search, print-disabled item): "reconstructed over 1000 of the elements in the
WE027 code. Livingston to King, Paris, January 25, 1802" and, separately, that despatches to Secretary of
State Madison "continued to be masked in the WE027 nomenclator" -- both facts resolve, not deepen, ARM3-COR's
own flagged README discrepancy (WE027 is Livingston's code used with both King and Madison, not King-only).
The printed *Life and Correspondence of Rufus King* (vol. IV, 1802-04) supplied one genuine raw specimen the
1894-1900 edition's own editor marked "Not deciphered": a single group **786** and a repeated three-number
group **128. 55. 28**, too few values for a screen but structurally distinct from the target's flat
one-group-per-word design. No family-C-relevant discovery (no key, no larger WE027 table, no match); named
for a successor: the Irving Brant Papers (LOC), Weber's own worksheets source, as the likeliest place an
actual WE027 table survives.

Requests: be-api.us.archive.org 12 (Weber). www.loc.gov 4 (collection searches) + item-metadata fetches folded
into the same host count. tile.loc.gov 11 (6 thumbnails + 5 native-resolution page fetches). archive.org 4
(2 advancedsearch.php + 2 `_djvu.txt`, King vols III-IV; both djvu fetches needed `-L` to follow a redirect a
bare `curl -sS` silently swallowed as 0 bytes -- worth a playbook note, not added here). All >=1.5s apart,
descriptive User-Agent, no 429/403/challenge on any host. No logins, no credentials touched, no subagent
calls (numpy/Pillow installed via pip this session to run `tools/iiif_lines.py` locally; not present at
session start).

26 Sept 2026 19:56 UTC (LANE ARM3 worker ARM3-LOOP, Fable): family D, model-in-the-loop crib rounds on the nomenclator
design, control first (HYPOTHESES.md "Family D, ARM3-LOOP"). Three matched controls (seeds 2-4, `loop/`), blind 15.6 /
2.3 / 11.3 percent blended, three reader rounds each: best gains +10.7 / +14.4 / +2.6, mean 9.2 at the most favourable
count, under the 10-point gate and under the 13.3-point blind spread; the gain is particle-only (book class never above
3.3 percent); 18 of 55 cribs right. Gate not met, target not run; family D is a control-backed non-test at this N. Tools:
`tools/families/nomenclator.py` cribs option, `tools/crib_rounds.py --family nomenclator`, tests pass. Next step
unchanged from family C: more ciphertext in the same code, or a crib source outside the ciphertext.

## ARM-BRANT, 26 Sept 2026 (parent worker ARM-BRANT) -- Irving Brant Papers finding aid located, item found, not digitised

Intake gate: `ciphers/armstrong-madison-1808: open (line 1) -- edition/page or full-text-search citation found
within 6 lines` (exit 0), re-run this pass.

Archive lookup only (Pipeline 4), no decoding, no cryptanalysis. Following ARM3-LIVCODE's own named next step
(HYPOTHESES.md "Family E, ARM3-LIVCODE"): Weber 1979 sources his WE027 reconstruction to the Irving Brant
Papers, LOC.

**U1, finding aid.** `www.loc.gov/search/?fo=json&q=Irving+Brant+papers` (1 request) returns the finding aid
itself as the top hit: *Irving Brant papers, 1910-1977*, `hdl.loc.gov/loc.mss/eadmss.ms011060`, LC Catalog
record `lccn.loc.gov/mm79013656`. The modern ArchivesSpace-hosted finding aid page
(`findingaids.loc.gov/repositories/19/resources/4635`, the handle's redirect target) and its legacy XQuery
mirror (`findingaids.loc.gov/db/search/xq/searchMfer02.xq?_id=loc.mss.eadmss.ms011060...`) are both Cloudflare-
challenged to curl and to a real headless-Chromium fetch alike (`tools/browser_fetch.js`, 9 s wait, still
"Just a moment..."); stopped at the one-retry limit and did not hit that host again (4 attempts total: 2 curl,
2 browser). Wayback Machine's CDX API was also tried as the documented fallback but this container's TLS
tunnel to `web.archive.org` failed outright (`Recv failure: Connection reset by peer` on three separate
attempts including a bare root fetch, not a Cloudflare/bot signal -- logged, not retried further).

Recovered instead: a WebSearch turned up the finding aid's own PDF, served from `tile.loc.gov` (a host already
confirmed working in this repo, ARM3-LIVCODE), fetched directly and cleanly (HTTP 200, 6 pages,
`tile.loc.gov/storage-services/service/gdc/gdcfindingaidpdfs/ms011060/ms011060.pdf`, 204,504 bytes). Saved to
`sources/loc-ms011060-finding-aid.pdf`. This is the real, current (encoded 2011, revised January 2023) LC
Manuscript Division finding aid text, not a stub: **Collection Summary** -- Extent 37,000 items, 64 containers
plus 1 oversize, 24 linear feet; eight series (Family Correspondence, General Correspondence, Conservation
Papers, Speeches and Writings, Research File, Miscellany, Addition, Oversize).

Grepped the extracted text (`pdftotext -layout`) for cipher/cypher/code/Livingston/Weber/nomenclator/WE027/
Armstrong/worksheet/Monroe/decipher -- one hit on "cipher", none on the others:

> BOX 37 -- **Research File** series (Box 35-59, "Notes, card files, and other material used in researching
> various books... arranged alphabetically by title") -- subsection **James Madison** (3 folders), item list
> including "Notes on electoral college", **"Official cipher used by Robert R. Livingston, copy, 1801-1804"**,
> "'Road to Armageddon'", "Trip to Poland", "Miscellaneous notes".

**Digitised: no.** The Access and Restrictions section (finding-aid text, verbatim): "The papers of Irving
Brant are open to research. Researchers are advised to contact the Manuscript Reading Room prior to visiting.
Many collections are stored off-site and advance notice is needed to retrieve these items for research use."
No viewer link, no online-format tag on this item anywhere in the finding aid; the `digitized: true` /
`online_format: [pdf, web page]` fields in loc.gov's own search JSON refer to the finding-aid document itself
(the PDF/HTML text just quoted), not to the manuscripts it describes -- consistent with every other LC finding
aid in this repo's own table (CLAUDE.md Access playbook: loc.gov row).

**U2, Weber's own trail.** be-api full-text search on `unitedstatesdipl0000webe` (6 queries, all page 670 of
the book, the same page each time -- Weber's endnote/acknowledgements discussion of his sources): "...their
worksheets on codes, located in the **Irving Brant Papers** in the Library of Congress, provided another
source of information. **Mrs. Brant** had taken many of **Madison's encoded dispatches with Robert Livingston,
Edmund Randolph and James Monroe, which had the plaintext written**[in, presumably, above the code groups --
cut off at the snippet boundary]... Mrs. Hazeldean Brant **reconstructed over 1000 of the elements in the
WE027 code**. Livingston to King, Paris, January 25, 1802, in DUSMF, R 11." This resolves exactly onto Box 37's
item: the "Official cipher... copy" is (or is adjacent to) the worksheet Hazeldean Brant (Irving Brant's wife)
built her WE027 reconstruction from, working from Madison's own encoded dispatches with plaintext annotated in.
A second, unrelated passage on the same page: "successor as minister to France, General John Armstrong, wrote
40 letters in code to James Madison beginning in late 1804..." -- this is Weber's general survey of ministers
who used codes (Livingston, Armstrong, Crawford all "sent encoded dispatches"), read as confirming Armstrong's
routine 1804-1810 office-code correspondence (THE=972, already on file), not as naming a second WE027-linked
Armstrong item; no Brant-Armstrong connection found beyond this.

Two loc.gov JSON searches for a separately-deposited Weber/Brant cipher-worksheets collection: `q=Ralph+E.+
Weber+cipher+worksheets` (43 results, all unrelated -- phone directories, newspapers) and `q=Brant+Madison+
cipher` (8,697 results, all unrelated -- Joseph Brant, Madison County/S.D./Ky. newspapers). Neither found a
separate Weber deposit; consistent with U1 -- the worksheets are inside the Irving Brant Papers itself.

**Next action.** The item is real, located (Box 37, Research File > James Madison), and not online. The
Manuscript Reading Room's own contact page is `lcweb.loc.gov/rr/mss/address.html` (the redirect target of the
finding aid's own printed "Contact information: hdl.loc.gov/loc.mss/mss.contact" link, resolved 26 Sept 2026;
the page itself did not load past loc.gov's Cloudflare challenge to curl from this container, so its address
text is not quoted here -- a person or a browser-tool pass can read it directly). Preferred citation per the
finding aid: "Container number [Box 37], Irving Brant Papers, Manuscript Division, Library of Congress,
Washington, D.C." REQUEST.md and ASKS.md row appended.

Requests this pass: www.loc.gov 4 (2 `?fo=json` searches + 2 `www.loc.gov/rr/mss/` HTML attempts, the second
403'd, Cloudflare). findingaids.loc.gov 4 (2 curl, 2 browser_fetch.js, all Cloudflare-challenged; stopped,
logged, not retried again). tile.loc.gov 1 (the PDF, clean 200). be-api.us.archive.org 6 (Weber snippet
queries). web.archive.org 3 (CDX + root, all TLS connection resets, not a bot block; stopped). hdl.loc.gov 2
(HEAD only, to read redirect targets). WebSearch 1 (recovered the working tile.loc.gov PDF URL after
findingaids.loc.gov failed). All >=1.5s apart per host, descriptive User-Agent except where the playbook
already documents a browser UA is needed. No logins, no credentials. No subagents.

Rule 10: this is a location and a container-list quotation, not a reading and not a novelty claim; nothing
here is "new", "unpublished" or "first".


## 27 September 2026 — Codex ARM-REATTACK (owner-directed; unsolved)

See [report, scripts and final results](codex-2026-09-27/REPORT.md), commit `06c48356ce5cd427c2791363f988c9016e95f58f`.

Corrections to earlier notes: Krajčovič's Armstrong crib **does exist**, in August 2026 comments on Klaus Schmeh's article, and its source opening is in Armstrong to Jefferson, 15 February 1808. The proposed reading is unverified: the first repeated `240`, assigned **of**, falls where the source letter has **and** after **man**, so exact copying fails under that alignment. `ciphertext.txt` contains three spurious numeric tokens copied from editorial line-count labels (2, 1, 1); the new derivative removes only those, giving N=366, K=216. `ciphertext_ms.txt` also omits visible groups and should not be treated as certified complete. Originals preserved.

New screens: exhaustive 4-digit position/digit permutations (87,091,200 candidates each), invertible affine maps and rectangular grid renumberings against THE972 and WE028, each compared with 20 fully optimized order shuffles. All three synthetic THE972 controls recover 100% of original groups; target maxima remain within shuffle ranges, with no coherent reading. Controls are not fully design-matched (K=189, no graphic breaks, greater known coverage); no code family is excluded. MCMC preserving occupied-decade and units-digit margins gives 26 observed x/10x pairs vs mean 21.58, upper-tail estimate 0.075, not proof of zero equivalence. No target key entries or solved-status promotion. Glyph transcription and the previously recorded Brant/Livingston archival lead remain unresolved; no outreach performed.


## Codex ARM-GLYPHS, 27 September 2026

Continued owner-directed attack: `codex-2026-09-27b/REPORT.md`, provisional image-based glyph inventory (257 tokens, 36 types), homophonic-letter solver and controls. Three clean held-out English controls recover 99.22%, 100%, 99.22%; the retained mixed French/Latin bibliography stress sample recovers 35.02% at the smaller budget, 52.92% at the larger. Neither target run reads; transcription is M-grade and controls do not match unknown shorthand design. French, vowel-deletion, separator and coarse-merger explorations have no dedicated positive controls and license no exclusions. Pinckney-Erving partial anchors checked: six common-word numbers absent from target, no direct-key anchor, renumbering not excluded. No target key, plaintext, solved status or outreach.


## Codex ARM-PIECES, 27 September 2026 — variable-length glyph search

Status remains **unsolved**. See [codex-2026-09-27c/REPORT.md](codex-2026-09-27c/REPORT.md) for source inspection, code and retained results.

Primary Annet 1752 and 1770 manuals contain alphabets, standalone word signs and compounds. The earlier ARM-S3 description of Annet as a nonalphabetic sign index is insufficient; the 1761 instructions were not retrieved, and edition mappings must not be interchanged. The 1770 dotted-cup/WITH resemblance is a visual hypothesis only; no Armstrong sign was assigned WITH. See [MANUALS.md](codex-2026-09-27c/MANUALS.md).

The new letter/digraph substitution surrogate uses the previous provisional transcription (257 tokens, 36 types, 28 fragments), the existing historical English character model, and five held-out Jefferson controls. Initial positive per-character bonuses failed the controls by overusing digraphs. With bonus zero and deeper search, tuning recovery was 240/257, 221/257 and 239/257 exact token pieces. Fresh validation recovered 219/257 (85.21%) and 251/257 (97.67%), clearing the recorded exploratory threshold. All controls' optimized approximations outscore their true plaintext: this is partial recovery, not an exact-key guarantee.

Target and three position-shuffled copies received equal two-stage budgets (120 x 45,000 then 1,000 x 120,000 iterations). Best log10 scores were target -294.031441 and shuffles -300.026775, -297.181649, -301.153413. Every output is unreadable. Three shuffles establish no significance claim. No coherent crib was available for numerical/repeated-passage confirmation. This does not exclude shorthand or digraph encodings, and it does not validate the uncertain transcription. No target key entry was added.

The primary Madison-to-Jefferson transcription of 15 May 1808 was opened at https://rotunda.upress.virginia.edu/founders/default.xqy?keys=FOEA-print-02-01-02-3083 (early-access text). Its postscript corroborates the private-correspondent-key possibility; it supplies no key. No outreach occurred.


## Codex ARM-GLYPH-ALT, 27 September 2026 — local transcription uncertainty

**Unsolved.** [Report and reproducible files](codex-2026-09-27d/REPORT.md). Image inspection yielded ten two-way class alternatives in p1e, p1f and p3h, anchored to source crops and hashes. They are provisional judgments by the same reader; they neither replace the original transcription nor constitute independent reconciliation.

The joint alphabet/label search used 1,000 x 90,000 iterations and a fixed 0.3-log10 penalty per changed label. Two new held-out Jefferson controls with five deliberately wrong first choices each recovered 256/257 (99.61%) and 257/257 letters, restoring 4/5 and 5/5 planted label errors with no false label changes. Both cleared the prospectively recorded gate. Warm starts differ from the hard-label baseline, so the recovery improvement is not a clean ablation; the explicit error-restoration result tests the new operation.

The target remains incoherent. Its best penalized score is -299.499256129 (raw -298.899256129), selecting p1f glyph 14: 29->26 and p3h glyph 3: 22->20. Neither change is confirmed by plaintext or repeated-context evidence. No numerical crib, new key assignment, family exclusion or statistical-separation claim follows. Original ciphertext and solved status are unchanged. Source frames 0031 and 0032 are duplicate captures of the same two leaves; first-page existing crops starting at x=250 can omit left-edge signs, which were checked against the full source image. No outreach occurred.


## Codex ARM-PRIVATE, 27 September 2026 — private-correspondence source search

**Unsolved.** [Source report](codex-2026-09-27e/REPORT.md) records two specific image leads: the Livingston key indexed in the **Monroe** Papers (1963 index p.11, PDF p.27, Series 1, year 1803, two pages), and the privately addressed 1803 Livingston letter in Brooklyn CBH 1974.002 Box 1 Folder 25. Neither image was obtained or tested. The 1904 catalogue likely describes the same Monroe key; do not count it as another witness or assume WE027. The initial working attribution of the index to Madison was erroneous and is corrected. Likely reel 3 placement is an inference; the image number is unresolved.

Hoyt's 1943 Warden collection description identifies twenty Armstrong letters spanning 1804-1810. Maryland's microfilm holdings, the separate LOC Warden collection, and Newcastle's 1817-1845 edition must not be conflated. The bearer in Armstrong's 15 February 1808 Jefferson letter remains unnamed here; no crib from that letter is validated. No solver run, target reading, key assignment, or family exclusion this pass. Requests appended to REQUEST.md and ASKS.md; no outreach.


## Second-opinion leads (SO-ARMSTRONG-RESUME, 27 Sept 2026)

Landed from PR 40 (`second-opinions/chatgpt-resume-2026-09-27.md`, PR-LAND-15). A resume/continuation checkpoint,
not a leads-prompt answer or a reading; every citation below is a claim to verify, never a fact -- unchecked.

- archival-route; LOC 2023 finding aid for the James Monroe Papers (PDF p.15, `tile.loc.gov/storage-services/service/gdc/gdcfindingaidpdfs/ms009142/ms009142.pdf`), reel 3 flagged "Digital content available" for span 1803 Oct. 9-1807 Jan. 16 -- does not identify the Livingston key's own frame or certify its inclusion in the scans -- unchecked.
- archival-route; public GetArchive mirror of reel 3 returned a page and thumbnail link through the web reader (curl 403); no verified key image or LOC frame number obtained from it -- unchecked.
- archival-route; Internet Archive OCR for the 1893 chronological calendar `cu31924032751665_djvu.txt` returned HTTP 502, not retrieved; the 1904 catalogue's p.29 citation for the key is unconfirmed independently of this OCR -- unchecked.
- archival-route (already logged, ARM-PRIVATE); Brooklyn CBH 1974.002 Box 1 Folder 25 (privately addressed 1803 Livingston letter) and the Brant Box 37 request named as fallback inputs if LOC image access stays blocked -- unchecked.
- internal-flag; a ROOM entry timestamped 17:43 UTC from Codex ARM-KEYIMAGE claims retrieval of the Livingston key image under a folder `codex-2026-09-27f`, but that folder and any completion report are absent from the repository as fetched for this PR (based on remote `main` commit `d134ed2d68eede9b88308aa37aa171f0380f7e20`) -- not confirmed lost or superseded, just unreconciled -- unchecked.


## Second-opinion leads (SO-ARMSTRONG-SPACE, 27 Sept 2026)

Landed from PR 41 (`second-opinions/chatgpt-space-2026-09-27.md`, PR-LAND-16). A space-aware homophonic
glyph-attack report, not a leads-prompt answer or a reading; every citation below is a claim to verify,
never a fact -- unchecked.

- experiment-result; a space-aware model (encoded spaces, up to four cipher types per plaintext character) recovers 96.5-100% on three synthetic known-answer controls and its Armstrong candidate beats all 20 positional shuffles (target -342.574535 vs shuffle mean -359.175970) but remains incoherent -- no key or decipherment claimed -- unchecked.
- experiment-negative; a separate no-space variant (same four-homophone cap, spaces stripped) fails two of its three known-answer controls at both budgets (150x50,000 and 600x100,000 restarts; e.g. control1 falls from 42/257 to 12/257 correct with more search), so no Armstrong target or shuffled-target run was attempted for it and it licenses no negative evidence against unspaced homophonic spelling -- unchecked.
- archival-route; a newly indexed reel-3 image-page reference (`loc.gov/resource/mss33217.003/?sp=1111&st=image`) for the Livingston key returned HTTP 403; not an identified key frame -- unchecked.
- archival-route; the LOC finding aid PDF (`tile.loc.gov/storage-services/service/gdc/gdcfindingaidpdfs/ms009142/ms009142.pdf`) and existing index evidence locate the research lead but no key image was obtained or compared -- unchecked.
- lead; Klaus Schmeh's article comment thread (30-31 August) was checked: its author reports unsuccessful continuation searches and withdraws two additional phrase proposals; no verified complete reading or usable key -- unchecked.
- lead; a brief Wouves 1797 syllabic-table search did not yield an inspected key plate, and a numerical coordinate-code idea was considered but not implemented as a controlled decoder -- neither is promoted to a result -- unchecked.


## Second-opinion checkpoint (SO-ARMSTRONG-COMPONENTS, 27 Sept 2026)

Landed from PR 42 (`second-opinions/chatgpt-components-2026-09-27.md`, PR-LAND-17). A runner checkpoint
report, not a leads-prompt answer or a reading; every citation below is a claim to verify, never a fact --
unchecked.

- experiment-negative; a three-decimal-field spelling-table model (150x50,000 search, en18-corpus positive controls at 729/729, 731/731, 769/769 correct characters) produces no readable English on the target, whose output beats only 1 of 20 positional shuffles -- unchecked.
- experiment-negative; two glyph-null homophonic models (shape 20 fixed null, or shapes 20+22 fixed null, ≤2 homophones/letter, controls 205-220 of 207-220 correct) also produce no readable English; the shape-20-only variant outranks all 20 of its own shuffles while the 20+22 variant is outranked by 6 of 20 -- neither validated as an exclusion or a confirmation -- unchecked.
- archival-route; Annet's 1752 and 1770 shorthand manuals inspected directly (Dropbox PDF mirrors via Stenophile's historical collection, SHA-256 hashes recorded); the 1770 manual's PDF pp.16-17 give plaintext for twenty engraved examples, an untried literal-decode source not yet implemented -- unchecked.
- archival-route; Narváez's article on the Wouves numeric-table cipher (AGN IV c.2610 exp.026 f.19, Mexico) gives the coordinate mechanism (62 alphabetic columns, arbitrary hundred-bases + row 1-99) but not the complete table; the Wellcome-catalogued ECCO item `CB0131087164` holding the full table was not retrieved -- unchecked.
- lead (Livingston witness); re-examination of frame `mjm014253_0303.jpg` locates a short cipher passage with one-reader interlinear associations (grade M), including groups `1523 518 1126 1467` read as the "Marbois" run and `715 1583 648 967 913` as "his full power(s) that he"; developed further in PR 43 -- unchecked.


## Second-opinion checkpoint (SO-ARMSTRONG-LIVINGSTON-WITNESSES, 27 Sept 2026)

Landed from PR 43 (`second-opinions/chatgpt-livingston-witnesses-2026-09-27.md`, PR-LAND-17). A runner
checkpoint report, not a leads-prompt answer or a reading; every citation below is a claim to verify, never
a fact -- unchecked.

- lead; a 19-entry provisional Livingston base-reading table (grade M-provisional, one reader, unblinded) built from four existing manuscript image crops (`mjm014253_0303.jpg`, `mjm014121_p_1064.jpg`, `mjm014224_0205.jpg`, `mjm014123_1076.jpg`, hashes and crop boxes recorded) -- not a certified WE027 key -- unchecked.
- experiment-negative; applying the same 19 group values to the unchanged 366-group Armstrong ciphertext gives only two literal hits, each occurring once (group 648="power" at numeric position 357, group 967="that" at position 285) -- sparse overlap, not proposed as Armstrong readings -- unchecked.


## Second-opinion checkpoint (SO-ARMSTRONG-CONTINUITY, 27 Sept 2026)

Landed from PR 44 (`second-opinions/chatgpt-continuity-2026-09-27.md`, PR-LAND-18). A runner checkpoint
report, not a leads-prompt answer or a reading; every citation below is a claim to verify, never a fact --
unchecked.

- experiment-negative; a six-decimal-field-order spelling model (150x50,000 search per case) recovers all 18 positive controls exactly, but the target remains unreadable in every order; the best order (012, score -1379.94) beats only 1/20 same-order shuffles, and 3/20 shuffled maxima taken across all six orders (accounting for order selection) meet or beat it -- unchecked.
- archival-route; Irving Brant Papers, LOC Box 37, "Official cipher used by Robert R. Livingston, copy, 1801-1804" named as a concrete full-key lead; no digital table obtained -- unchecked.
- archival-route; Monroe Papers Series 1, reel 3, end of 1803, catalogued Livingston cipher-key lead; no key image obtained -- unchecked.
- archival-route/negative; repeated www.loc.gov requests returned HTTP 403 and Rotunda document-page clicks failed, so Founders' own editorial notes and its 21 Feb-31 Aug 1808 letter index remain unfetched -- unchecked.
- lead; a printed 20 June 1804 Livingston passage (Hunt's Madison Writings VII, p.124) located by public search but not aligned to any particular coded manuscript span -- unchecked.
- next-step; the checkpoint's own named next action is transcribing Annet 1770 PDF pp.16-17's paired known-answer examples before any further target test -- unchecked.


## Second-opinion checkpoint (SO-ARMSTRONG-CHECKPOINT 20:04, 27 Sept 2026)

Landed from PR 45 (`second-opinions/chatgpt-checkpoint-2026-09-27-2004.md`, PR-LAND-18). A runner checkpoint
report, not a leads-prompt answer or a reading; every citation below is a claim to verify, never a fact --
unchecked.

- archival-route; two Annet shorthand manual PDFs (labelled 1770, primary; 1752, comparison) fetched via Dropbox mirrors linked from Stenophile's historical collection, SHA-256 hashes recorded; PDF p.16 gives 20 numbered plaintext explanations and p.17 the matching engraved exercises -- unchecked.
- lead; item 20's printed answer ("For there is no work nor device nor knowledge nor wisdom in the grave whither thou goest") aligned to 17 provisional (grade M, one reader, answer-aware) sign/component readings, explicitly not a validated decoder -- unchecked.
- lead; the engraved title page (PDF p.1, "Eccles. IX. 10.") carries a second shorthand rendering of the same verse for comparison, with visible differences from item 20 not yet resolved -- unchecked.
- bibliographic-note; Stenophile's catalogue labels the scan "1770" but the letterpress title itself (p.7, "second edition... J. Smeeton") shows no visible year, and the Pocknell Collection list catalogues a matching Smeeton second-edition item as "[1760?]" (Alston 207, P28) -- edition date remains bibliographically unsettled -- unchecked.
- next-step; the checkpoint's own named next action is transcribing exercise 2 on PDF p.17 into primitive/word-sign alternatives as held-out evidence, before any Armstrong target application -- unchecked.


## Second-opinion checkpoint (SO-ARMSTRONG-CHECKPOINT 20:26, 27 Sept 2026)

Landed from PR 46 (`second-opinions/chatgpt-checkpoint-2026-09-27-2026.md`, PR-LAND-18). A runner checkpoint
report, not a leads-prompt answer or a reading; every citation below is a claim to verify, never a fact --
unchecked.

- experiment-negative; a mixed letter/whole-word-sign model (44-piece alphabet, <=2 homophones) recovers 94-97% of controls overall but only 54-63% of word-sign tokens specifically, and incorrect fitted readings score above the true key on all three controls -- the pooled 90% launch gate is too coarse to validate word-sign recognition -- unchecked.
- experiment-result; the target (-343.10) beats 0/20 of its own symbol-order shuffles yet remains incoherent, with only six fitted word-sign tokens -- no reading or key claimed -- unchecked.
- lead; a 16-shape/primitive answer-aware candidate lattice for Annet 1770 exercise 2 (13/16 candidate coverage, all grade M) is explicitly flagged as development/calibration data, not a held-out or blind recognition result -- unchecked.
- archival-route/negative; the LOC Monroe-collection "about" page again returned HTTP 403 via the web reader, no key image obtained -- unchecked.
- lead/negative; a 1811 pasigraphy exposition (Firmas, *Pasitélégraphie*, e-rara) was inspected but post-dates the 1808 target and describes Maimieux's earlier system without matching it; the actual 1797 source remains unretrieved (Internet Archive 502, Google Books image unavailable) -- unchecked.


## Second-opinion checkpoint (SO-ARMSTRONG-CHECKPOINT 20:48, 27 Sept 2026)

Landed from PR 47 (`second-opinions/chatgpt-checkpoint-2026-09-27-2048.md`, PR-LAND-18). A runner checkpoint
report, not a leads-prompt answer or a reading; every citation below is a claim to verify, never a fact --
unchecked.

- correction; PDF p.14 rule 8 licenses a comma only for the suffixes "ing/ed" in context, not the whole-word "or" the prior checkpoint's fixture assumed; withdrawing it drops Annet exercise-2 development coverage from 13/16 to 12/16 -- unchecked.
- correction; PDF p.3's hooked sign reads "their, there", not "then, there" as the prior checkpoint labelled it -- unchecked.
- lead; exercise-2 position 15's outline is a descending diagonal stroke resembling the AND marks at positions 6 and 9, not a comma, so it is now DIAGONAL_UNRESOLVED rather than a certified OR sign -- unchecked.
- next-step; the checkpoint's own named next action is aligning exercise 11's conjunction region (AND/ARE/OR/OUGHT) against p.16's printed words before any target application -- unchecked.


## Second-opinion checkpoint (SO-ARMSTRONG-CHECKPOINT 20:50, 27 Sept 2026)

Landed from PR 48 (`second-opinions/chatgpt-checkpoint-2026-09-27-2050.md`, PR-LAND-18). A runner checkpoint
report, not a leads-prompt answer or a reading; every citation below is a claim to verify, never a fact --
unchecked.

- lead; a full source-line alignment of all 366 numeric groups and 25 graphic passages against manuscript images (frames 0030-0033) finds two preferred-reading differences from the editorial baseline -- numeric position 8 (1841 -> 1843) and position 32 (203 -> 200) -- plus four newly flagged unresolved ink locations -- unchecked.
- correction; the apparent equality between numeric positions 8 and 253 (both previously 1841) disappears under the image-preferred reading (position 8 now reads 1843), so an opening crib should not be propagated to position 253 on that equality -- unchecked.
- correction; the same Annet comma/OR fixture error PR 47 also found (standalone "or" unsupported; coverage 13/16 -> 12/16) -- unchecked.
- correction; the 17:43 UTC Codex ARM-KEYIMAGE ROOM line ("claim: recover/identify...") is a task claim, not evidence the Livingston key was actually retrieved; no `codex-2026-09-27f` result was located by this checkpoint -- unchecked (answers PR-LAND-15's 18:49 UTC flag on this same discrepancy, above).
- next-step; the checkpoint names resolving the clipped gutter material from an additional manuscript capture, and a repeatable literal shorthand reading on control material, as the next substantive steps -- unchecked.


## Second-opinion checkpoint (SO-ARMSTRONG-CHECKPOINT 20:55, 27 Sept 2026)

Landed from PR 49 (`second-opinions/chatgpt-checkpoint-2026-09-27-2055.md`, PR-LAND-19). A runner checkpoint
report, not a leads-prompt answer or a reading; every citation below is a claim to verify, never a fact --
unchecked.

- lead; Annet 1770 PDF p.17 exercise-11 engraving aligns four connective words to strokes (AND: descending diagonal; ARE: right-facing curve, alphabet r; OR: loop joined to a right-facing curve, provisionally o+r; OUGHT: forked aught/ought sign from p.3), all grade M, answer-aware, one reader -- unchecked.
- correction; the ARE/OR contrast makes it unsafe to generalize exercise 2's diagonal-at-OR-position reading into a general OR sign; the exercise-2 discrepancy (plate/text mismatch, abbreviation, or omitted-word punctuation) remains unresolved and no new OR or AND alias was installed -- unchecked.
- next-step; the checkpoint's own named next action is comparing the source-grounded Annet primitives against the target's native page-1 long passages and page-3 tail, to test whether a literal match can be made before moving to primary-key recovery -- unchecked.


## Second-opinion checkpoint (SO-ARMSTRONG-CHECKPOINT 21:17, 27 Sept 2026)

Landed from PR 50 (`second-opinions/chatgpt-checkpoint-2026-09-27-2117.md`, PR-LAND-19). A runner checkpoint
report, not a leads-prompt answer or a reading; every citation below is a claim to verify, never a fact --
unchecked.

- archival-route; James Monroe Papers Series 1 reel 3 frames 127-128 identified as a compact cipher key and worked example, matched (by chronological placement, not independent authentication) to the 1963 index and 1904 catalogue's Livingston 1803 cipher-code entry -- unchecked.
- lead; the compact key is NOT the anticipated ~1700-entry WE027 table -- three letter alphabets, a short-word column, a vocabulary column, a trailing-zero rule and explicit null numbers; M-grade, one-reader transcription of 25 letter entries and 45 word entries -- unchecked.
- lead; a separate undated table at reel 9 frame 954 gives different M-grade readings for groups 911/967 than PR 43's provisional Livingston witness table (911 "ven" vs "have", 967 "trade" vs "that"), and is not identified as WE027 or WE028 -- unchecked.
- correction; the PR 49 lease on comparing Annet primitives against the target's glyph passages is released with no secure literal reading established -- not claimed as a validated negative -- unchecked.
- archival-route; loc.gov's ordinary web reader returns 403 but the public JSON catalogue (`?fo=json`) and tile.loc.gov IIIF image endpoints answer 200 with valid image URLs, a route not previously documented here -- unchecked.
- next-step; the checkpoint's own named next action is locating and reading Livingston-to-Monroe, 11 September 1803 (catalogue title reproduced at PICRYL), to test whether its cipher table matches the compact key, the PR 43 witness table, or neither -- unchecked.


## Second-opinion checkpoint (SO-ARMSTRONG-CHECKPOINT 21:28, 27 Sept 2026)

Landed from PR 51 (`second-opinions/chatgpt-checkpoint-2026-09-27-2128.md`, PR-LAND-19). A runner checkpoint
report, not a leads-prompt answer or a reading; every citation below is a claim to verify, never a fact --
unchecked.

- lead; the Livingston-to-Monroe 11 September 1803 witness (LOC mjm014115, resource mjm.07_1031_1040) was located: two manuscript copies (1031d, and 1036d marked "Duplicate"), with a 10-token span where three tokens (968, 1221, 968) match PR 43's already-frozen THE/OF/THE readings -- an out-of-document consistency check on three tokens, not a whole-letter recognition score -- unchecked.
- lead; a copy-substitution alignment: numbers 640 1295 in 1031d correspond to plain prose "no right" in 1036d; the individual splits 640=no, 1295=right are M-grade and provisional, with the two-number run treated as the authoritative alignment -- unchecked.
- correction/caution; a marked (diamond-like) 1295 in PR 43's May witness (under the annotation "Talleyrand") has no comparable mark below the September occurrence of 1295 -- the two observations are not to be collapsed into one dictionary entry -- unchecked.
- lead; Monroe reel 9 frame 955 extends frame 954's undated table down through numbered value 1700; a new crop reads 812=the (M), making it provisionally a THE=812 table distinct from THE=968/972/15 -- unchecked.
- archival-route; the 1963 Monroe index lists an undated "Jefferson Thomas -- Cipher Key" printed form (Series 1) and a key "prepared for JM2" (Series 2) as possible identification leads for the frame 954/955 table, not proof of attribution -- unchecked.
- next-step; the checkpoint's own named next action is checking further occurrences of marked versus unmarked 1295 across mjm014115's remaining untranscribed pages (1033, 1038) before further primary-key work -- unchecked.


## Second-opinion checkpoint (SO-ARMSTRONG-CHECKPOINT 21:37, 27 Sept 2026)

Landed from PR 52 (`second-opinions/chatgpt-checkpoint-2026-09-27-2137.md`, PR-LAND-19). A runner checkpoint
report, not a leads-prompt answer or a reading; every citation below is a claim to verify, never a fact --
unchecked.

- lead; a source-grounded plaintext/cipher alignment in the Livingston-to-Monroe 11 September 1803 duplicate (images 1033/1038) aligns a 12-group whole-run (476 168 510 1031 1601 1675[diamond] 976 164 1021 91 351 905[quote-mark]) to copy A's prose "you did make it after all those difficulties were removed" -- a whole-run alignment only, no word-by-word split licensed -- unchecked.
- lead; two provisional anchors within that run (476=you, 510=make) are supported by separate interlinear annotations on images 1034.jpg and sep11-1031.jpg respectively -- unchecked.
- correction/caution; a numeral discrepancy between the two manuscript copies is now recorded explicitly: copy A reads 1070, copy B reads 1072, at the same position (between groups 510 and 1421) -- both preserved, neither reading "repaired" to match the other -- unchecked.
- lead/negative; no additional occurrence of the marked (diamond) 1295 was found in this batch's review of images 1033/1034/1038/1039, but this is not an exhaustive transcription or a verified-absence claim; images 1035 and 1040 remain unretrieved -- unchecked.
- next-step; the checkpoint's own named next action is inspecting PR 43's existing 17/18 September Livingston images for a second annotated occurrence of the marked Talleyrand run or unmarked 1295, to decide whether the May/September 1295 discrepancy is a copying error, an alternate marked entry, or a key change -- unchecked.

## Campaign step H1 (2026-09-27 22:15 UTC)

Runner: campaign runner armstrong-madison-1808 (account 2, session_013E5jUS9GV1AsxLeUcwgbf6), first step of the
proof-sprint campaign (SPRINT.md, CAMPAIGN.md). Question: does the retrieval claimed by the 17:43 UTC ROOM line
"Codex ARM-KEYIMAGE ... codex-2026-09-27f" exist anywhere, before it is treated as lost or as evidence.

What was searched (all on a fresh checkout at origin/main 6a3cc79, 22:10 UTC):

| Where | Method | Result |
|---|---|---|
| every local and remote ref | `git log --all --grep` (keyimage, 09-27f, 27f) and `git log --all -- '*codex-2026-09-27f*'` | 0 commits |
| every remote branch (`git ls-remote --heads`, 60 heads) | tree listing of all 15 `second-opinion/armstrong-*` heads for a `codex-2026-09-27f` path | 0 paths; those branches carry only the Codex folders 27, b, c, d, e plus the ChatGPT runner's own g/h/i/j |
| unreachable objects | `git fsck --unreachable --no-reflogs`: 50 commits, 202 trees, 241 blobs, each tree listed and each blob grepped for the folder name | 0 hits (the 50 commits are all 26 Sept `room.py --push` rebase leftovers) |
| ROOM.md, whole file | every line mentioning KEYIMAGE or 27f | one Codex line only, 17:43 UTC, a `claim:` line; no `done` line from that role ever (lines 3475, 3478, 3515, 3525 are other sessions referring to it) |
| the Codex folder chain and the landed second opinions | grep for 27f / key image | codex-2026-09-27e/REPORT.md (ARM-PRIVATE, done 17:36 UTC): "exact image unresolved, LOC fetches failed"; chatgpt-resume (PR 40, 18:29 UTC): latest recoverable checkpoint 17:37 UTC, no later result, "no codex-2026-09-27f directory is present"; chatgpt-checkpoint 20:50 (PR 48): the 17:43 line "is a task claim, not evidence of successful retrieval" |
| PRs 40-53 (GitHub, all states) | titles, bodies, head branches | none adds or names a 27f file |

Verdict: `codex-2026-09-27f` never reached GitHub in any form (no ref, no branch, no unreachable object), so it is
neither lost nor superseded here: the 17:43 UTC line is an unfinished task claim from a session whose work, if any,
stayed on the owner's machine. It is not evidence for anything and is now over six hours old with no done line
(CLAUDE.md "Collaborators": a stale claim), so the target is free to take.

What the claim aimed at was reached by a different route: the ChatGPT checkpoint runner (PR 50, 21:17 UTC, landed as
`second-opinions/chatgpt-checkpoint-2026-09-27-2117.md`) locates the 1803 Livingston compact cipher key at James
Monroe Papers, Series 1, reel 3, frames 127-128 (frame 128 the docket "Cyphers / 1803 - La Treaty"), with SHA-256
hashes for both frames and for an undated large numbered table at reel 9 frame 954, and reports that the LOC item
JSON (`https://www.loc.gov/item/mss33217003/?fo=json`, `resources[0].files`, array position = frame - 1) supplies
the real image URLs. Those images are not in this folder: `images/manifest.json` has no Monroe/mss33217 entry.
Reachability from this container, 22:13 UTC, one request each, descriptive UA: the item JSON answers HTTP 200
(application/json); the guessed `resource/mss33217.003_0001_1159/?sp=127&fo=json` form answers 404, so the file
list in the item JSON is the route, not the `?sp=` form. Per PR 50 the compact key is not the 1,700-entry WE027
table (three marked letter alphabets, a short-word column, a vocabulary column, trailing-zero rule, explicit nulls
100..900 and 1000..9000; worked example "The plan will not do", answer-aware, not an independent control).

Consequences recorded in CAMPAIGN.md: H1 done; H7 (locate the reel-3 image) re-ranked to 1 with `needs: nobody`,
rewritten as fetch + hash-verify + manifest + a value-range screen against a shuffled-value control; H11 (two blind
passes of frame 127 into a graded key TSV, decode with `tools/decode_key.py`, en18 judge vs 200 shuffled keys) and
H12 (screen the reel-9 frame-954 table's digit signature the ARM3-LIVCODE way) added behind it; H2-H6 each move down
one rank. For the orchestrator: ASKS.md row 80's "locate exact LOC reel-3 image" half is answered by PR 50 (frames
127-128); the Brooklyn CBH half is not. No reading, no control, no class change in this step. Cost: no figure from
get_session for this session; the row's estimate (1 USD) is what `campaign.py --spend` records. Requests per host:
loc.gov 2, github.com API 1 (PR list).
