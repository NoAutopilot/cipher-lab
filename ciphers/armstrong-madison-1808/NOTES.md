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


## Second-opinion checkpoint (SO-ARMSTRONG-CHECKPOINT 21:59, 27 Sept 2026)

Landed from PR 53 (`second-opinions/chatgpt-checkpoint-2026-09-27-2159.md`, PR-LAND-20). A runner checkpoint
report, not a leads-prompt answer or a reading; every citation below is a claim to verify, never a fact --
unchecked.

- lead; Monroe reel 9 frames 956-957 (the THE=812 table's alphabetical face) carry printed positional rules: a caret-like sign beneath the last/penultimate/antepenultimate digit doubles the corresponding letter from the right, a curved sign beneath a digit deletes it, and U/V and I/J are stated interchangeable; M-provisional, one reader, scoped to the THE=812 table only, not authenticated for Livingston's THE=968 witnesses or Armstrong's target -- unchecked.
- lead/correction; two occurrences of group 1583 (May "powerfull" and Sept 18 "his full powers that he") each carry a distinct closed/loop-shaped mark beneath the final digit, supporting a marked-token reading of "full" but NOT establishing unmarked 1583=full; the "ful plus a doubling operator" idea remains an unverified hypothesis -- unchecked.
- correction; the parent checkpoint's (#52) fixture reading "that any good could have resulted" is corrected by native crop inspection to "that any good would have resulted"; the twelve coded groups and their aligned plaintext span are otherwise unchanged -- unchecked.
- archival-route/lead; a domain-filtered search located Jefferson to Monroe, 11 May 1785 (Founders Archives), in which Jefferson describes completing a cipher to accompany the letter, identified by the edition as Code No. 9 -- an attribution lead only, not proof that Monroe reel 9 frames 954-957 are that enclosure -- unchecked.
- next-step; the checkpoint's own named next action is locating the original Code No. 9 enclosure or an identified copy, and comparing the three fingerprints 17=magistrate, 18=navigation, 812=the, before transferring any rule to Livingston or Armstrong -- unchecked.


## Second-opinion checkpoint (SO-ARMSTRONG-CHECKPOINT 22:11, 27 Sept 2026)

Landed from PR 54 (`second-opinions/chatgpt-checkpoint-2026-09-27-2211.md`, PR-LAND-20). A runner checkpoint
report, not a leads-prompt answer or a reading; every citation below is a claim to verify, never a fact --
unchecked.

- lead; LOC mcc.036 is identified as Madison to Jefferson, 23 May 1789, partially ciphered with Jefferson's own interlinear decipherment, and the catalogue links it to the cipher Jefferson sent Madison on 11 May 1785 -- a separate Madison-side lead from PR 53's Jefferson-to-Monroe/Code No. 9 lead, not to be merged with it -- unchecked.
- lead; a manuscript control on mcc.036 page 2 reproduces the printed THE=812 table's final-letter-doubling rule: groups 1109="sti", 416="more", and 1598 (caret beneath its final digit) doubles to "ll", giving "still more" matching Jefferson's own interlinear reading -- M-provisional, one reader, answer-aware (not a blind test) -- unchecked.
- caution; this control validates only the final-letter-doubling rule in this one case; it does NOT establish that Livingston's THE=968 system or Armstrong's target uses this key or operator, and does not validate the penultimate/antepenultimate/deletion/affix rules from PR 53 -- unchecked.
- correction; a preliminary reduced-image impression of group "1588" was corrected by native inspection to "1598" before entering the fixture -- unchecked.
- leads (unvalidated); a Jefferson Barbary-States memorandum catalogued as shorthand (LOC mtj1.004_1009_1009), a Bradford-to-Madison letter of 1 March 1773 discussing "personal strokes," and two further Jefferson/Madison 1785 letters as a possible provenance chain for the control key -- none inspected or validated as target controls -- unchecked.
- next-step; the checkpoint's own named next action is acquiring mcc.036 page 3 to check for an annotated deletion mark or a non-final-position doubling mark -- unchecked.


## Second-opinion checkpoint (SO-ARMSTRONG-CHECKPOINT 22:44, 27 Sept 2026)

Landed from PR 55 (`second-opinions/chatgpt-checkpoint-2026-09-27-2244.md`, PR-LAND-20). A runner checkpoint
report, not a leads-prompt answer or a reading; every citation below is a claim to verify, never a fact --
unchecked.

- lead/negative; mcc.036 page 3 continues in ordinary prose to the closing with no visible encoded span, so it supplies no deletion or non-final-position doubling control; page 4 not acquired -- a bounded one-leaf observation, not exhaustive -- unchecked.
- lead/negative; the Jefferson Barbary-States memorandum (mtj1.004_1009_1009) shows conventional cursive, abbreviations and corrections, not an annotated geometric alphabet or a secure Armstrong glyph match; no shorthand system identified or excluded -- unchecked.
- archival-route; Yale MS 857 finding aid (box 4 folder 116) lists a 25 April 1808 statement/covering memorandum about an Armstrong letter on the purchase of Florida, tentatively attributed to [Smith, John] and [John?] Armstrong; manuscript not acquired, no established link to the 20 Feb 1808 cipher -- unchecked.
- archival-route; Warden Papers holdings distinguished across LOC (ms012085 boxes 1/23/25), Maryland Historical Society (MCHC MS 0871, 8 reels, microfilm-only, public tree endpoint returns zero children), and APS (Mss.Film.1290, direct page did not load) -- no manuscript read in any of the three -- unchecked.
- lead/negative; both Sharon Howard/Newcastle project letter-metadata CSVs (dbw2/dbw3, pinned at commit b800c530) were audited for the sender/recipient and date fields: no row names "Armstrong" or carries an 1800-1809 year in those fields, but 97 rows are undated and coverage is bounded to this accessible metadata only -- unchecked.
- next-step; the checkpoint's own named next action is re-reading the interlinear over the Sept 17, 1803 Livingston witness's group run 1011 911 408 1105 1456 968 1426 1133 1221 978, focusing on 1426 1133 and 978, for a separate plaintext/copy witness -- unchecked.

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

## Campaign step H7 (27 Sept 2026, 22:26-22:35 UTC)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01H27tXgYoK6tVYXUGAN1h5T), second step of the
proof-sprint campaign (SPRINT.md, CAMPAIGN.md). Hypothesis H7: fetch the 1803 Livingston compact key images the ChatGPT
runner located (PR 50), verify them, and screen the key's value ranges against the target's groups before any
transcription pass.

**Fetched and verified.** Three frames from the James Monroe Papers (LOC mss33217) via the tile.loc.gov IIIF image API
(3 requests, 1.6 s apart, descriptive UA, all HTTP 200 image/jpeg), now `images/monroe/` with entries in
`images/manifest.json` (`monroe_papers`):

| frame | file | dims | SHA-256 vs PR 50 checkpoint |
|---|---|---|---|
| reel 3 fr.127 | mss33217-003-0127.jpg | 2891x4270 | match (eafdc2d4...) |
| reel 3 fr.128 | mss33217-003-0128.jpg | 4240x2735 | match (d1a4df4e...) |
| reel 9 fr.954 | mss33217-009-0954.jpg | 5141x4166 | match (4475fb0b...) |

Frame 127, one look by this runner at a one-third-scale render and one crop (grade M, one reader, not a transcription):
a compact key exactly as PR 50 describes it -- three letter alphabets 1-9 distinguished by marks ("signs of the first /
second / third line"), a short-word column (values 15-97 and 232-286), the null rule ("100 ... 900, 1000 ... 9000 may be
written but are to have no signification"), the worked example "The plan will not do" -- **plus a vocabulary column of
about 45 entries valued 334-897** (Atlantic States 334 ... Congress 338, Canada 421 ... France 429, French 442, ...
King 642, Louisiana 645, Money 647, ... Spain 842, Spy 864, Trade 869, United States 892, Union 893, West Florida 896,
Western Country 897) that PR 50's fixture deliberately omitted. Discrepancy for H11's blind passes to settle, not a
correction of record: the words_lower crop reads "this 15 / the 17 / would 75 / which 79 / over 248" where PR 50's
fixture has 15=the, 17=this, 75=want, 79=while, 248=our.

**Screen (`livkey1803/screen.py` -> `livkey1803/screen.tsv`), script-only, no plaintext read.** A group is *producible*
under this key iff its value with trailing zeros stripped (the leaf's own rule) is a key entry, or the group is a null.
Two value sets: strict (the entries read) and generous (any value inside a vocabulary-column band). Statistic: the
producible fraction of the 369 numeric groups in `ciphertext.txt`. Rule-3 controls: (positive) six en18 period-prose
windows encoded with this key (words where it has them, else letters, with its nulls and trailing-zero variants);
(null A) the target's digits permuted within each group, 200 draws -- the shuffled-value control H7 named; (null B)
each group replaced by a uniform random value of the same digit count, 200 draws.

| row | producible (generous) | producible (strict) |
|---|---|---|
| target (369 groups) | 0.257 | 0.244 |
| null A, digits permuted (200) | mean 0.249, p95 0.266, max 0.274 | mean 0.229, max 0.252 |
| null B, uniform same length (200) | mean 0.244, p95 0.276, max 0.285 | mean 0.225, max 0.282 |
| target percentile within null A / null B | 0.785 / 0.740 | |
| positive control, en18 encoded (6 texts) | 1.000 each | 1.000 each |
| positive controls' own null A | mean 0.967-0.982 | |
| target groups whose stripped value exceeds 899 (no key entry, not a null) | 75 of 369 (0.203) | |
| target four-digit groups with a nonzero last digit | 72 of 369 (0.195) | |

Reading: the target sits inside its own random-value band (74th-79th percentile, under p95 on both nulls) while
key-encoded prose reads 1.000 by construction; a fifth of the target's groups (1752, 1841, 1314, 1267, 1180 ...) have
no way to arise from this key under its stated rules. Caveat on the positive controls' own null: key-encoded prose is
mostly single-digit letter groups, which digit permutation cannot change, so that null sits near ceiling (0.97) and
shows little on its own -- the discriminating comparison is target 0.257 vs encoded 1.000 and vs the target's own
nulls, not the encoded texts' permuted nulls. Conditional on `ciphertext.txt` (Bourdeau's transcription; ARM-TR2
match_ratio 0.957 against the manuscript) and on the trailing-zero and null rules as read from the leaf.

**Verdict for the campaign:** the reel-3 frame-127 compact key, used as its own rules say, is not the target's key;
control-backed at this statistic. Not a verdict on WE027 (this leaf is not the 1,700-entry table, PR 50) nor on the
reel-9 frame-954 table, which was fetched but not inspected. Superscript ticks in `ciphertext_ms.txt` (a possible
alphabet mark under a compact-key design) number three, on 38, 1640 and 1276 -- none on a single-digit group -- so a
tick-as-alphabet-mark reading is weakly grounded at face value (recorded as H13, low rank). No reading, no control on
a reading, no class change. Requests per host: tile.loc.gov 3. Cost: no get_session figure available to this runner;
the row's estimate (1.5 USD) is what `campaign.py --spend` records. Environment note: Pillow and numpy were absent in
this runner's container and installed with pip for the crops; `tools/iiif_lines.py` needs both.

## Campaign step H12 (27 Sept 2026, 23:12-23:21 UTC)

Runner: campaign runner armstrong-madison-1808 (account 2, session_013E5jUS9GV1AsxLeUcwgbf6). Hypothesis H12: screen the
undated numbered table at Monroe Papers reel 9 frame 954 (on disk since H7, SHA-256 verified) against the target the
ARM3-LIVCODE way -- value range, digit signature, the 901-1099 block -- before any transcription pass. No plaintext read.

**What the table is (one reader, grade M, native crops + two neighbouring frames).** Frame 954 is the upper part of a
one-part sequential code: 17 columns x 100 rows, values 1-1700, each row a word or a syllable (901 consul, 902 mal,
903 ore, 907 twelve, 910 are, 912 find, 917 europe, 1007 june, 1016 friday, 1017 power, 1020 time, 1026 virginia;
1231 common, 1254 would, 1260 were, 1341 is, 1352 of, 1461 by, 1470 are, 1480 should ...); the decade rows (x10, x20 ...)
are written large for navigation and hold ordinary entries. Fetched to settle the range (3 requests to tile.loc.gov,
1.6 s apart, all HTTP 200, hashes in `images/manifest.json`, not committed because `images/` is at 27 MB of its 30 MB
line): frame 955 is the same sheet's lower half, rows 43-100 of every column, ending "1700 ac"; frame 956 is the
alphabetical encode side of the same key (A-Z columns, word -> number, no value above about 1700 seen, a right-hand
column of modifier rules -- plural / tense / a "last figure doubles the last letter" rule -- and a digit list 0-9);
frame 953 is unrelated (1810 notes for Monroe from a Spanish paper). Columns 1201-1700 are only partly filled: a fill map
of rows 1-81 in columns 1201/1301/1401/1501/1601 (`livkey1803/f954_fillmap.tsv`, blank rates 0.07 / 0.17 / 0.27 / 0.31 /
0.47) -- the key was still being filled in from the low values up. Not the 1,700-entry WE027 either (PR 50's warning
stands; nothing here identifies the table's owner or date).

**Screen (`livkey1803/screen954.py` -> `screen954.tsv`), script-only:**

| section | statistic | target | comparator |
|---|---|---|---|
| range | groups above 1700, the table's last entry | 34/369 = 0.092 (27 distinct: 1708 ... 1900) | a letter encoded with this table: 0 by construction |
| block | groups in 901-1099 vs flanking 200-blocks 701-900 / 1101-1300 | 4 vs 16 / 36 (the emptiest 200-window in 101-1700) | THE972 real usage pooled, same windows: 90 vs 58 / 101; the table has 200 ordinary entries in 901-1099 |
| units | units-digit shares 0..9 | .25 .18 .05 .03 .11 .03 .09 .12 .12 .02 (0+1 = 0.43) | THE972 usage .09 .10 .15 .07 .09 .10 .11 .14 .09 .06 (0+1 = 0.19); a sequential table gives no reason for a 0/1 skew |
| fill | of 64 target groups in the mapped cells, landing on a blank cell | 7/64 = 0.109 (1208 1314 1541 1628 1638 1641 1658) | key as it stands: 0 by construction; random cell of the same column: 0.219, P(<=7) = 0.019; random cell of the same column AND same units digit (null C): 0.168, P(<=7) = 0.134 |

Reading: excluded on range -- a tenth of the target's groups have no entry in this key, and its encode side confirms
there is no supplement above 1700. The 901-1099 trough sits exactly where this table is fully populated with common
entries, the opposite of what encoding with it would give, and the units-digit shape is the one ARM-DESIGN already
placed at percentile 100 against every contiguous design (this table is a contiguous one-part design). The fill screen
is reported for completeness: against the naive null the target avoids blanks more than chance (p 0.019), but that
null is on the wrong axis (the blanks are units-digit-skewed, the target is too -- rule 3's same-axis lesson); against
the units-matched null the difference vanishes (p 0.134), and 7 blank hits are 7 more than a key can produce.
Caveat: the fill statistic assumes the filled state on this copy is the state when used; the range and block
statistics do not depend on that. Conditional on `ciphertext.txt` (ARM-TR2 match_ratio 0.957).

**Verdict for the campaign:** the reel-9 frame-954/955/956 key is not the target's key, control-backed on range and
consistent on block and units; with H7 both keys located in the Monroe Papers are screened out, and H11's graded
transcription of frame 127 has no decode use unless H13 gives the leaf a role. Suggestion for the lane close-out (Usage
8a, `tools/key_design.py`): this key is a fully documented period design (one-part, 1-1700, 17x100, syllable+word,
alphabetical encode side, modifier-mark rules) worth a KEY-DESIGN.tsv row even though it is not this target's. New
hypothesis H14 from frame 956's modifier column: its plural / tense / doubling marks are the kind of thing the target's
superscript ticks could be under a *different* table -- a read of that column at native resolution and a count of the
target's marks by group length vs shuffled positions (cheap, script + one look). No reading, no class change.
Requests per host: tile.loc.gov 3. Cost: no get_session figure to this runner; the row's estimate (1.5 USD) is what
`campaign.py --spend` records. Vision: 17 native crops read by this runner directly, no subagent calls.

## Campaign step H2 (27 Sept 2026, 23:21-23:33 UTC)

Runner: campaign runner armstrong-madison-1808 (account 2, session_013E5jUS9GV1AsxLeUcwgbf6). Hypothesis H2: turn the
SO-ARMSTRONG-COMPONENTS glyph-null finding ("glyph 20 always null" target outranks all 20 of its own token shuffles,
0/20; "glyphs 20+22 null" 6/20; `second-opinions/chatgpt-components-2026-09-27.md`) into a rule-3-sized control at
this repository's 200-shuffle convention (ARM-A2, ARM3-DICT) and report the real percentile.

**Rebuild.** `glyphnull/h2_shuffles.py` reconstructs the second opinion's own reproducer: the codex-2026-09-27b
257-token / 36-shape provisional glyph transcription with glyph 20 (37 tokens) or glyphs 20+22 (50 tokens) deleted
(N=220/K=35 and N=207/K=34, 27 fragments), a character 5-gram model on en18 minus the Jefferson volume (backoff 5,
J->I, V->U), its incremental-scoring annealer (<=2 homophones per letter, 150 restarts x 50,000 proposals, seed 731),
its three matched positive controls from held-out Jefferson text at the same N, K and fragment lengths (gate >=98%
recovered, controls before target), and its token-shuffle nulls with the same seeds (270932+s), extended from 20 to
200. Reproduction is exact: controls 220/220, 218/220, 220/220 and 207/207, 205/207, 207/207; targets -274.415061677
and -263.987430959; all 40 recorded shuffle scores match to 1e-6 (`h2_shuffle_scores.tsv` rows 0-19 of each model).
Pre-registered reading: PASS = target above the 200-shuffle 95th percentile.

| model | N / K | controls | target (seed 731) | 200 shuffles: mean, sd, p95, max | at/above target | verdict |
|---|---|---|---|---|---|---|
| glyph 20 null | 220 / 35 | 220, 218, 220 of 220 | -274.415 | -287.867, 4.392, -279.625, -275.804 | 0/200 | PASS at seed 731 (z 3.06) -- see the seed test |
| glyphs 20+22 null | 207 / 34 | 207, 205, 207 of 207 | -263.987 | -263.567, 4.143, -257.430, -248.836 | 102/200 | FAIL (percentile 49) |

**Seed test (`h2_target_seeds.tsv`).** The seed-731 target's best-of-150 restart (-274.4) is 10 points above its own
second-best restart (-284.8), so the PASS rests on one optimum. Re-running the same target at seeds 732-741: best-of-150
= -288.7, -279.0, -288.8, -291.2, -287.7, -278.7, -278.4, -285.2, -287.8, -283.3 (11-seed mean -283.9, sd 5.3, median
-285.2). Against the 200-shuffle band (itself best-of-150 at seed 731 per shuffle): 4 of 11 seeds above p95, 1 of 11
(seed 731 itself) above the shuffle maximum, the median seed at the 33rd percentile. The 0/20 -- and this run's 0/200 --
is a property of one search seed, not of the sequence; on the average seed the target sits inside its shuffle band.

**Calibration (`h2_control_shuffles.tsv`).** 40 token-shuffles of each positive control score mean -309.7 / -302.2 /
-300.8 (p95 -301.9 / -296.8 / -292.9) against the controls' own -183.8 / -164.3 / -166.2: enciphered English of this N
sits 120-140 points above its shuffles under this model, the target 4 points above its shuffles on the seed average.
On that axis the glyph-20-null target is at about 3% of the way from "random order" to "English": whatever order
structure the glyph transcription carries, it is not the structure of a <=2-homophone English letter substitution with
glyph 20 as a null, and a shuffle null is in any case a necessary-not-sufficient test (any non-exchangeable sequence --
a transcription with copied repeated patterns, any language, any shorthand -- beats shuffles).

**Verdict for the campaign:** FAIL, control-backed; the second opinion's own wording ("not proof ... a small,
exploratory comparison") stands and its 0/20 is now explained as seed dependence. The raw seed-731 output
(`r|emcm|toftest|f|pstos|...`, audit only) is not English. No reading, no class change. Nothing here bears on the glyph
transcription itself (M-grade, one reader) or on shorthand/word-sign designs, which this model does not cover.
Suggestion: any future shuffle-null claim on this target (or any target) reports the target's best-of-R over several
seeds against the shuffle band, not one seed's -- the same "control can fail differently" rule 3 asks of controls,
applied to the search's own randomness. Requests: none (offline). Cost: no get_session figure to this runner; the row's
estimate (2 USD) is what `campaign.py --spend` records. Compute: 400 shuffle runs + 120 control-shuffle runs + 11 target
seeds, about 12 min on 4 cores; sequences and binaries in the scratchpad, tables in `glyphnull/`.

## Campaign step H3 (27 Sept 2026, 23:34-23:38 UTC)

Runner: campaign runner armstrong-madison-1808 (account 2, session_013E5jUS9GV1AsxLeUcwgbf6). Hypothesis H3, ARM-S3's
own named next step for Annet: do the target's shorthand marks group in twos, the way a two-digit numbered sign
index (ARM-S3's reading of Annet 1761, a 300-cell index, rows 0-29 x columns 0-9) written as digit strokes would?
Script `adj/pairs_test.py` -> `adj/pairs_test.tsv`, offline, stdlib. The row named the shuffled-position null of
`adj/adj_test.py`; that null moves runs among numeric gaps and keeps their lengths, so it cannot change a run's parity
or the positions within a run (rule 3, the bCAS/AX-5799 same-axis lesson) and was not used. Nulls that can differ:
a coin-flip parity null and a within-fragment token shuffle. Positive controls: pair-design sequences with the
target's own run lengths and per-mark transcription error e injected at 0 / 5 / 10 / 20% (a mark dropped or a stray
mark added), because the two transcriptions of the same marks disagree in count by about 16% (ciphertext_ms.txt 218
marks in 28 runs, ARM-TR/TR2; codex-2026-09-27b glyphs.tsv 257 tokens in 28 fragments), so the control's error band
has to bracket that (the SALV-DIAG lesson).

| test | source | target | null | pair-design control (p05 of even fraction, or share of 200 controls beating their own shuffle p95) at e = 0 / .05 / .10 / .20 |
|---|---|---|---|---|
| A parity: even-length runs | ms runs (28) | 8/28 = 0.286 | coin flip: P(<=8) 0.018 | 1.000 / 0.500 / 0.393 / 0.357 -- target below the control p05 at every level |
| A parity | glyph fragments (28) | 13/28 = 0.464 | coin flip: P(<=13) 0.425 | 1.000 / 0.464 / 0.393 / 0.357 -- target below p05 at e=0, at the line at e=.05, inside the band from e=.10 |
| B odd-vs-even position shapes, JSD bits (distinct shapes odd/even) | glyph fragments | 0.1599 (32 / 26) | within-fragment shuffle: mean 0.119, p95 0.1601, target percentile 94.8 | 30+10 shapes: 1.00 / 0.85 / 0.49 / 0.12; 3+10 shapes: 1.00 / 0.92 / 0.60 / 0.27 (control JSD means 1.00 / 0.18-0.22 / 0.12-0.16 / 0.12-0.13) |

Reading. On the manuscript transcription's own run lengths the marks run *odd* more often than a coin flip (20 of
28 odd; runs of 1, 3, 5, 9, 11, 13, 15, 25, 35 marks), the opposite of a two-stroke design, and below the pair
control's 5th percentile even when a fifth of the marks are miscounted: a pair design is excluded on this source at
every error level tried. On the glyph table the same statistic excludes pairs only for a near-clean transcription
(e <= 5%); from 10% error the parity control itself has no power (its p05 falls below the target). The positional
test agrees in shape: the target's odd/even shape divergence sits at the 94.8th percentile of its own shuffle null,
a hair under the p95 line, with 32 distinct shapes at odd positions against 26 at even -- nothing like the 3-30
row shapes vs 10 column shapes a numbered index would give -- and its JSD (0.16) is where the pair controls land
only once 10% of marks are wrong (0.12-0.16), far below the clean controls (1.0) or the 5%-error ones (0.18-0.22).
Conditional on two M-grade one-reader transcriptions that disagree with each other by about 16% in mark count.

**Verdict for the campaign:** FAIL for the two-strokes-per-sign reading, control-backed at e <= 5% on both sources
and both statistics and, on the manuscript run lengths, up to 20%; on the glyph table the test is untestable above
10% error (control power 49-60%), which is inside the two transcriptions' own disagreement, so the glyph-table half
is "untestable at this transcription's error level", not a second negative. This closes ARM-S3's named next step
for Annet as ARM-S3 framed it. It does not bear on Annet's actual design as the later checkpoints read the 1752/1770
manuals (alphabets, word signs and compounds -- single strokes, not numbers written out), which the checkpoints'
own answer-aware exercise alignments cover and this campaign has not re-tested. The marginal positional result
(percentile 94.8) is worth one cheap follow-up on a *reconciled* mark transcription rather than either single pass:
recorded as hypothesis H15. No reading, no class change. Requests: none. Cost: no get_session figure to this runner;
the row's estimate (1.5 USD) is what `campaign.py --spend` records. Compute 26 s.

## Campaign step H4 (27 Sept 2026, 23:39-23:42 UTC)

Runner: campaign runner armstrong-madison-1808 (account 2, session_013E5jUS9GV1AsxLeUcwgbf6). Hypothesis H4: re-derive
the keyless NARA IIIF route for frame M34-014-0025 (ARM-S2's flagged failure) and run the superscript-tick-vs-baseline-
dash check ARM-S2 left undone, on Armstrong's ordinary THE=972 office-code letter of 15 Feb 1808.

**Route (7 requests to catalog.archives.gov, 1.6 s apart, descriptive UA).** `info.json` for 0025 and 0024 both answer
200 today (native 3680x3264 and 3648x3264, maxArea 10,000,000). The request form is what failed ARM-S2, not the frame:
`full/full/0/default.jpg` answers HTTP 400 "Invalid size" (text/plain) on this IIIF Image API v3 service, whereas
`full/<w>,/0/default.jpg` (w*h under maxArea) and the exact native `full/<w>,<h>/0/default.jpg` both answer
image/jpeg. Both frames are now in `images/` (0024 at 3333x2982, 0025 at 3300x2927, sha1 in `images/manifest.json`,
folder 28 MB of the 30 MB line) with the route note in the manifest. Frame 0024 is the 15 Feb letter's cipher body
(header "Paris 15 february 1808", about 220 groups), 0025 its last three numeral lines, closing and P.S.

**Tick check (this runner's own reading of five native line bands of 0024 and the three lines of 0025, one reader,
grade M).** The office hand shows three kinds of extra mark, none of them the target's: (1) the digit 6 written
raised at the end of a group -- 1116 (= "s", the plural suffix in THE=972, Bourdeau H), 1086, 316, 426, 1016, 1216,
1146, 1416, 1596, and mid-group in 962 -- about 18 instances, a calligraphic habit for "6", not a separate stroke;
(2) a small subscript hook or "s"-like flourish under the last digit of a few groups (817, 741, 1165, 624, 66 --
five instances, possibly last-digit corrections or a suffix device; not read further); (3) one interlinear
correction ("1005" written above "888"). No horizontal bar above a numeral anywhere -- the target's R5 superscript
tick (over 38, 1640 and 1276 in `ciphertext_ms.txt`; `images/shorthand/INVENTORY_reconciled.tsv` R5: the same
stroke as the target's baseline dash, repositioned) does not occur in the sibling office letter. Counting it as a
test: 3 ticks in 358 target groups against 0 in about 243 office groups gives a one-sided Fisher P of 0.21 -- at
three events this is not a discriminating count, so the finding is qualitative (the office hand has a different
mark repertoire), not a control-backed exclusion of "tick = office convention". The office letter's subscript hooks
are a new lead the target's mark inventory can be checked against cheaply (R4 "backward comma" hooks, R5 baseline
dashes): recorded as H16.

**Verdict for the campaign:** route fixed and documented (done); tick check run, qualitative only -- the target's
bar-above-numeral tick is absent from about 243 groups of the same writer's office usage (Fisher P 0.21, not a test
at N=3). No reading, no class change. Requests per host: catalog.archives.gov 7. Cost: no get_session figure to
this runner; the row's estimate (1 USD) is what `campaign.py --spend` records. Vision: 9 crops read by this runner,
no subagent calls.

## Second-opinion checkpoint (SO-ARMSTRONG-CHECKPOINT 22:55, 27 Sept 2026)

Landed from PR 56 (`second-opinions/chatgpt-checkpoint-2026-09-27-2255.md`, PR-LAND-21). A runner checkpoint
report, not a leads-prompt answer or a reading; every citation below is a claim to verify, never a fact --
unchecked.

- correction; frame 1076's interlinear pencil above 715 (`715 1583[mark] 648[mark] 967 913`) reads "for", not "his" as read in PR 43 -- retraction of 715/his in favor of 715/for, still M-provisional -- unchecked.
- lead; frame 1064 pencil above group 318 (two occurrences) reads "much"; groups 1426 1133 run together read "habit" with no individual value or internal letter split assigned to either group -- unchecked.
- lead/negative; frames 1068/1069 (the copy of the Sept 17, 1803 Livingston-to-Madison letter, LOC mjm014121) corroborate the same ten-group numeric run and its order but not the pencil plaintext, and place the 1221/978 line break differently than frame 1064 does -- unchecked.
- lead/negative; none of groups 318, 715, 1426, 1133, 978 or 1459 occurs literally among the #48 target's 366 decimal groups -- a literal-overlap check only, not a proof against transformed keys or homophones -- unchecked.
- access-route; the Rotunda table-of-contents item links returned 403 on direct retrieval; Founders Online's robots restriction still blocks it; a March-item LOC metadata request timed out with no bytes -- unchecked.
- next-step; the checkpoint's own named next action is to inspect frame 1063 of the same LOC item for an independently annotated occurrence of 1426, 1133, 978 or 1459 -- unchecked.

No check-solved candidate (no printed decipherment of the Armstrong letter, its key, or the Livingston key is named).

## Second-opinion checkpoint (SO-ARMSTRONG-CHECKPOINT 23:36, 27 Sept 2026)

Landed from PR 57 (`second-opinions/chatgpt-checkpoint-2026-09-27-2336.md`, PR-LAND-21). A runner checkpoint
report, not a leads-prompt answer or a reading; every citation below is a claim to verify, never a fact --
unchecked.

- lead; frame 1063 of the Sept 17, 1803 Livingston witness reads `1634 1459` three times as "Baring" and `1409 1459` once as "going"; the cross-line `978 1459` "trusting" reading from frame 1064 remains tentative -- unchecked.
- lead/negative; treating 1459 as a shared suffix of Baring/going gives three conditional splits (g/ng/ing) with no way in the evidence shown to choose among them -- not a verified mapping for 1459 -- unchecked.
- lead/negative; all image surfaces of three Armstrong-to-Pinkney letters (Princeton C0027, dated 29 Jan, 15 Oct and 30 Nov 1808) were inspected -- clear prose throughout, no coded passage observed -- unchecked.
- lead/negative; two Armstrong-to-Monroe letters (LOC reel 4 frame 166, 4 April 1807; reel 3 frames 921-923, 9 July 1806) were inspected -- ordinary prose, no coded passage observed -- unchecked.
- archival-route; Huntington mssHM 22922 (John Quincy Adams to Armstrong, 27 Nov 1809) is catalogued as discussing the need for a cipher; no image is available online and no transcript was located -- unchecked.
- next-step; the checkpoint's own named next action is to locate Armstrong to Monroe, 30 May 1806, in LOC reel 3, bracketing backward from the confirmed 1 July 1806 docket at frame 900 -- unchecked.

No check-solved candidate (no printed decipherment of the Armstrong letter, its key, or the Livingston key is named).

## Campaign step H5 (27 Sept 2026, 23:43-23:47 UTC)

Runner: campaign runner armstrong-madison-1808 (account 2, session_013E5jUS9GV1AsxLeUcwgbf6). Hypothesis H5: a third
independent blind pass over page-1 lines 12-13 (frame 0030), the span ARM-TR2 could not resolve at any top margin,
to check whether Bourdeau's minimal "2, **, 44" at that position is an undercount.

**Finding: the unresolved residue was a crop-geometry bug again, on the LEFT edge this time.** ARM-TR's crop region
for frame 0030 starts at native x=250 (`images/crops_0030/manifest.json`, every box `[250, y0, 2096, y1]`), but the
writer's lines begin at x of about 130-250, so line heads that start with a numeral lost it. A widened band of lines
11-14 (x from 40, `images/crops_0030_wide/`, 2x upscaled single-line crops) read directly by this runner and by two
fresh blind Sonnet passes (one call each, three crops, no other file): line 11 ends "17. 1. 28. 14." with no "2";
lines 12 and 13 are pure shorthand runs (pass A about 14 and 18 marks, pass B about 16 and 14, both NONE for
numerals, confidence L-M); line 14 opens **"44. 176.. 564. 387. 840. 671.. 41. 431. 18. 640. 1780."** on both passes
(H and M) and on this runner's look. So Bourdeau's "44" is real and had been sheared off the ms transcription; his
"2" is not a numeral -- the ink at that position is the hook + "3"-shaped loop that opens line 12 (both passes flag a
"3"-like loop there), which a minimal notation plausibly rendered as "2". The same shear explains three more
residues of `tr/diff_ms_vs_ciphertext.py`: body line 2 head "1840. 240." (ms had marks only), line 15 head "1761. 13."
(ms had "73"), line 16 head "671." (ms had dropped it) -- each confirmed by this runner's direct look at a widened head
crop, each matching `ciphertext.txt` exactly.

Applied to `ciphertext_ms.txt` (header note added; "44" at grade H from two blind passes + direct look, the other
three heads at grade M, one reader, for a successor's blind pass to lift): diff before/after, `tr/diff_ms_vs_ciphertext.py`

| | substitutions | in ciphertext.txt not ms | in ms not ciphertext.txt | match_ratio |
|---|---|---|---|---|
| before | 9 | 12 | 3 | 0.9574 |
| after | 7 | 8 | 3 | 0.9672 |

Remaining `in_ciphertext_not_ms`: "2" (not a numeral, above) and seven on pages 2-3 (1, 1430, 18, 1, 12, 17, 1786)
that sit near line heads in the page 2-3 crops -- the same left-edge check on `crops_0031L/R` and `crops_0032L/R` is the
obvious next cheap step (H17). Also seen, not acted on: a small "36"-like interlinear mark above "36" in line 11 (ms
already reads 36). Units-digit distribution unchanged in shape (ms >=100: digit 0 91, 1 46, 2 9, 3 4).

**Verdict for the campaign:** resolved -- not an undercount by Bourdeau: "44" real, "2" a mark, lines 12-13 pure marks;
ms transcription corrected at four page-1 line heads, match_ratio 0.957 -> 0.967. No reading, no class change.
Lesson for the transcription brief: `tools/iiif_lines.py`'s region x0 must sit left of the leftmost ink on every
line (check the debug overlay's left edge, not only its top edge -- ARM-TR2's fix covered the top margin only).
Requests: none. Cost: no get_session figure to this runner; the row's estimate (1.5 USD) is what `campaign.py --spend`
records. Vision: 2 Sonnet subagent calls (three small crops each) + 8 crops read by this runner.

## Campaign step H17 (27 Sept 2026, 23:48-23:51 UTC)

Runner: campaign runner armstrong-madison-1808 (account 2, session_013E5jUS9GV1AsxLeUcwgbf6). Hypothesis H17: the same
crop-edge check on pages 2-3 (frames 0031/0032, the two exposures of the same leaf-spread) for the seven groups still
`in_ciphertext_not_ms` after H5 and the substitutions near line ends.

**Finding: page 2's RIGHT edge, same bug.** The crops_0031L/0032L region ends at native x=1900 but page 2's lines run
into the gutter (to about x=1960), so eight line tails lost their last group; page 3's crops start at x=1950, which
loses a digit only where a head touches the fold. Gutter strips of both witnesses (`images/crops_gutter/`, x 1450-2450,
native) read directly by this runner on 0031 and 0032, plus one blind Sonnet pass on the 0031 strips:

| ms line (page 2) tail before | manuscript | blind pass | grade |
|---|---|---|---|
| ... 1248 | 1248. 1430 | 1248. 1430 | H |
| ... 1267 | 1267. 18. 1 | 481. 1267. 18. | 18 H, 1 M (in the fold) |
| ... 1264 156 | 1264. 1567. | 1264. 1567. | H |
| ... 1240 143 | 1240. 1430. | 1240. 1430. | H |
| ... 1537 17 18 | 1537. 17. 1894 | 1537. 17. 1894 | H |
| ... 1480 1762 | 1480. 1762. 12. | 1480. 1762. 12. | H |
| ... 380 460 | 380. 460. 17 | 380. 460a. 17? | M |
| ... 3 47 | 3. 47. 1786 | 99. 3. 47. 1780 | M, written "1786?" (last digit in the fold; Bourdeau 1786) |

Page 3 head "130. 164. 180.": both witnesses and the pass read "130" where `ciphertext.txt` has "1 ** 1130"; a leading
"1" could sit under the fold on both exposures, so left as "130" (M), unresolved by these frames. Applied to
`ciphertext_ms.txt` with a header note. `tr/diff_ms_vs_ciphertext.py` now: 369 ms tokens against 369, substitutions 4,
in_ciphertext_not_ms 2, in_ms_not_ciphertext 3, **match_ratio 0.9837** (0.9574 at the start of this session, 0.9672
after H5). What remains is real: 1843/1841 and 200/203 (both confirmed digit disagreements with Bourdeau), the "2" at
the page-1 line-12 head (a mark), Bourdeau's "1" inside the page-3 mark line, the ms's own "31?", "13" and "3" read
inside mark runs (M), and the 130/1130 fold question.

**Verdict for the campaign:** resolved; the manuscript transcription and Bourdeau's now agree on 98.4% of groups
with every disagreement named, and no crop-geometry residue is left. Every family control on this target is
conditional on the transcription (SALV-DIAG), so this is the cheapest reliability gain on file. Lesson for the
transcription brief (with H5's): check `tools/iiif_lines.py`'s region against the debug overlay on all four edges;
on a two-page spread the region must reach into the gutter from both sides. No reading, no class change. Requests:
none. Cost: no get_session figure to this runner; the row's estimate (1.5 USD) is what `campaign.py --spend` records.
Vision: 1 Sonnet subagent call (two strips) + 6 strips read by this runner.

## Campaign step H13 (27 Sept 2026, 23:52-23:59 UTC)

Runner: campaign runner armstrong-madison-1808 (account 2, session_013E5jUS9GV1AsxLeUcwgbf6). Hypothesis H13: a
compact-key-style design (the Monroe reel-3 frame-127 leaf: single digits 1-9 as letters, three alphabets told apart
by a mark) would put marks on single-digit groups; the target's three superscript ticks sit on 38, 1640 and 1276 --
so re-read the tick crops and every single-digit group for marks, then count.

**Material.** Top-margin line sheets (`images/crops_h13/`, native, +55 px above each line) of every ms line carrying a
tick or a single-digit group on pages 1-3 (page 4's "4" and "5", ms lines 47 and 49, not cut -- frame 0033 has no crop
manifest; two of the 16 single-digit occurrences unchecked), 3x zooms of the four marked groups on both witnesses, read
by this runner and by one independent Sonnet second reader (three sheets, no other file).

| item | this runner | second reader |
|---|---|---|
| 38 (page 1 line 5) | small check/hook stroke attached after the group, mid-height | "small checkmark/tick attached directly after the group", H |
| 1640, 1276 (page 1 line 6) | faint diagonal at the top-left of the first digit of each, greyer than the ink -- possibly verso bleed-through (the page shows mirrored ghost text throughout) | not flagged |
| 1640 (page 2 line 28, `17 1640 19`) | colon-like double dot after 17 and after 1640, on both exposures (0031, 0032); ms transcription has no mark here | "two small tick/apostrophe-like marks directly after the group ... clearly separate from the separator dots", H |
| single-digit groups checked: 1 (p1 l9), 1 (p1 l13), 1 (p1 l14), 1 (p2 l20 tail, gutter strip), 3 (p2 l24), 1 (p2 l27), 3 (p2 l29), 2 (p2 l30), 3 (p3 l34, inside a mark run), 1 and 3 (p3 l36), 5 (p3 l37) | all plain; the p3 l34 "3" is a 3-shaped shorthand stroke, not clearly a numeral (M) | 1, 1, 1, 3, 1, 3 read PLAIN (the others were not on its sheets) |
| also flagged | interlinear "36"-like mark above "36" (p1 l9); "~" before 1480 (p2 l26) is a shorthand mark the ms already records as `*` | "36" arc above, M; curved stroke before 1480, M |

**Count.** Of 12 single-digit occurrences checked (14 of 16 seen, 2 M), none carries a mark. Under a frame-127-style
design in which single digits spell letters with alphabet 1 (a-i) unmarked and alphabets 2-3 (k-z) marked, the
share of marked letters in English text is about 0.53 (letter frequencies, j folded), so P(0 marked of 10 clean
singles) is about 5e-4 (0 of 12: 1.1e-4). The design's own positive expectation therefore fails on the target's single
digits; a design in which single digits are code values (not letters) is untouched by this. The shuffled-position
null the row named is not needed: the statistic is a plain count against the design's own prediction, and a
position shuffle could not change which groups are single-digit (rule 3, same-axis).

**Marks recorded, for the record and for H18.** The superscript "ticks" are not one thing: on 38 it is a check
attached after the group (both readers, H); on page-1 1640 and 1276 the strokes are faint and plausibly verso
bleed-through (M, disagreeing with ARM-S1/R5's "same stroke as the baseline dash, repositioned" -- that pass read
different crops); and on page-2 1640 both witnesses show a real double-dot mark after the group that neither ms pass
transcribed (H). The value 1640 carries a mark at both of its occurrences (page 1 faint, page 2 clear) -- the shape a
value-bound "marked form" would give (cf. the Livingston witnesses' marked 1295 and 1583, PRs 51-53), rather than a
positional device. Recorded as H18: a full inventory of marks attached to numeral groups over both witnesses (top
margin and mid-height, two blind passes), then a test of whether marks recur on the same values vs a shuffled-value
null.

**Verdict for the campaign:** FAIL for the compact-key alphabet-mark design element (0 of 12 single digits marked
against about 0.53 expected, P about 5e-4 to 1e-4), conditional on marks being visible at this resolution (two of the three
transcribed ticks are themselves faint). One correction to the mark record (page-2 1640 double dot, untranscribed)
and one new value-bound lead. No reading, no class change. Requests: none. Cost: no get_session figure to this
runner; the row's estimate (1.5 USD) is what `campaign.py --spend` records. Vision: 1 Sonnet subagent call (three
sheets) + 6 sheets/zooms read by this runner.

## Campaign step H14 (27-28 Sept 2026, 23:58-00:01 UTC)

Runner: campaign runner armstrong-madison-1808 (account 2, session_013E5jUS9GV1AsxLeUcwgbf6). Hypothesis H14: read the
right-hand modifier column of Monroe Papers reel 9 frame 956 (the encode side of the 1-1700 table screened out in H12)
and compare its marks with the target's.

**The column is printed, not handwritten (grade H, typeset text; native crops `images/monroe_rules/`).** Frame 956
is a pre-printed cipher form: typeset alphabetical headwords (X 1685, xy 1475, ya 1683, yea 1350 ... you 1243, your
1570, Z 1346, zeal 1566, &c 1677), a typeset digit and punctuation list with hand-filled numbers (0 102, 1 426, 2 739,
3 377, 4 980, 5 858, 6 271, 7 311, 8 642, 9 461; , 1240; ; 1342; : 1671; . 1462; ! 1234; ? 1563; -- 1668; ( ) 1230;
" 1344; ¶ 1560), and four typeset modifier rules, read verbatim:

1. "’ to a noun makes it's gen. or plur. to a verb makes it's 3.p.si.act" (an apostrophe-like mark after a group);
2. "‘ to a verb makes it's part pas. or imperf. indic." (a second, mirrored mark);
3. "^ under the last figure doubles the last letter of those represented by that n°. under the penult figure it
   doubles the penult letter: under the antepenult figure doubles the antepenult letter &c." -- a caret placed UNDER a
   specific digit of the number, the digit's position selecting which letter of the syllable is doubled;
4. "ʃ under a figure withdraws the letter corresponding as in the last article. u.& v. are convertible always so are
   i.& j." -- a long-s under a digit removes the corresponding letter.

So in this key family a group carries two classes of mark: a high mark AFTER the group (grammar: plural, genitive,
person, tense) and a low mark UNDER one particular digit (spelling: double or drop that letter). The reel-9 table's
hand-filled entries (H12) are largely syllables, which is what rules 3-4 serve. Bourdeau's THE=972 table for
Armstrong's office code is also syllable-heavy (741 = ce, 817 = al, 1116 = s, 1268 = ed, all H in
`tools/data/uscodes-1800/THE972_bourdeau.tsv`).

**Match against the marks already on file for this writer.** (a) The office letter of 15 Feb 1808 (frames 0024/0025,
step H4) has subscript hooks UNDER the last digit of five groups -- 741 (= ce), 817 (= al), 1165 (= to), 624, 66 -- the
placement rules 3-4 describe, on syllable/particle groups; H4 called them "possibly last-digit corrections". (b) The
target's page-2 1640 carries a double dot AFTER the group on both witnesses (step H13), the placement of rules 1-2;
38 carries a check after it; the R5 baseline dashes and R4 hooks of ARM-S1's inventory are low marks. (c) The
office letter's raised terminal 6s are not a modifier (a digit habit). No mark on the target was counted by digit
position yet (H18), so the positional test the row named is not run here: the inventory it needs does not exist.

**Verdict for the campaign:** the rule column is read (H); the mark grammar of this key family is now on file and it
matches, in placement, both the office letter's under-digit hooks and the target's after-group marks -- a lead, not a
result, since no mark has yet been tied to a decoded word. Two consequences recorded as hypotheses: H19, a
known-answer test on the office letter (Bourdeau's 15 Feb decode is known plaintext: do the five hooked groups read
as "double/withdraw the last letter" of ce, al, to ...? an H-grade check of the convention on this writer), and a
sharpening of H18 (inventory marks by class -- after-group vs under-digit -- and by the digit they sit under). For
the orchestrator and the verifier lane: frame 956 shows that reel-9 frames 954-956 are a commercially PRINTED
1,700-entry cipher form filled by hand; Weber 1979's WE027 (Livingston's own nomenclator, "over 1000 elements
reconstructed", ARM3-LIVCODE) is of that size, and this may be WE027 itself or its printed blank -- which bears on
ASKS row 77 (Brant Box 37) and on ARM3-LIVCODE's negative, and is a question for the verifier, not settled here. No
reading, no class change. Requests: none (frame 956 was on disk from H12). Cost: get_session read 28.99 USD for this
session at 23:57 UTC before this step; the row's estimate (1 USD) is what `campaign.py --spend` records. Vision: 3
native strips read by this runner, no subagent.

## Campaign step H19 (28 Sept 2026, 00:02-00:05 UTC) -- with H16 folded in

Runner: campaign runner armstrong-madison-1808 (account 2, session_013E5jUS9GV1AsxLeUcwgbf6). Hypothesis H19: a
known-answer test of the printed modifier rules (frame 956, step H14) on Armstrong's own office letter of 15 Feb 1808
(frames 0024/0025), whose plaintext is known through Bourdeau's THE=972 decode.

**Method (`marks/h19_known_answer.py` -> `h19_known_answer.tsv`).** The letter's 243-token numeric sequence
(`tools/data/uscodes-1800/stats.py`, THE972_USAGE) is mapped through Bourdeau's table and aligned to his decode tokens
(difflib, 205 of 243 aligned); the six groups that carry a mark under their last digit on frame 0024 (this runner's
reading, 3x zooms in `marks/h19_hooks_zoom.jpg`: the same small curl, "ʃ"- or "5"-shaped, under the LAST digit every
time -- 817, 741, 741, 662, 624, 1165) are read in context beside the unmarked occurrences of the same values.

| group (pos) | table | context (table words) | word the plaintext needs | rule fit |
|---|---|---|---|---|
| 741 (89), marked | ce | it suc **ce** d s | succee-ds: suc + ce**e** + d + s | double the last letter: yes (C) |
| 741 (121), marked | ce | does not suc **ce** d | succee-d | double the last letter: yes (C) |
| 662 (158), marked | pres | of im **pres** ment | impres**s**ment | double the last letter: yes (C) |
| 817 (55), marked | al | with **al** im [801] in | "with al(l) im..." plausible, not certain | consistent (M) |
| 624 (164), marked | {624} | it would be [624]s not only to re-is-t | value unknown | undetermined |
| 1165 (199), marked | to | s ag [1445] **to** ion s on | undetermined ("too"?) | undetermined |
| 741 (34), plain | ce | do not ac **ce** mp t this | accept-type reading, no doubling | control: no mark, no doubling |
| 817 (127), plain | al | the first [1172] **al** will also be | no doubling | control ok |
| 1165 (111, 148, 168), plain | to | be I [368] to; as to have; not only to re-is-t | plain "to" | control ok |

**Result: PASS on every decidable case.** Three of the six marked groups sit exactly where the plaintext needs the
syllable's last letter doubled (succeeds, succeed, impressment), a fourth is consistent, two are undecidable; none of
the five unmarked controls of the same values needs a doubled letter. So the office hand uses an under-last-digit
mark as the printed form's "under the last figure doubles the last letter" operator -- drawn as a curl rather than the
form's caret, and not the form's long-s "withdraw" (the known cases double, not drop). Grade C for the three decided
cases (known plaintext, H-grade table entries). Caveat: Bourdeau's own decode does not mark these doublings; this is
the first time (in this repository's record) the mark has been read as an operator, on one letter and six marks.

**What it means for the target.** The 20 Feb letter's marks under and after groups (H13: a check after 38, a double
dot after 1640 on both witnesses, R5 dashes, R4 curls) are now expected to be operators of this grammar rather than
shorthand or a separate alphabet -- which makes H18's inventory (mark class and the digit it sits under) the step that
turns them into evidence, and which raises the prior that the target's numeric part is a syllabic/spelling table of the
same printed family (a 17x100 form, the H12 table's shape) even though it is not that table's fill.

**H16, folded in (one look each side).** The office letter's under-digit curl and the target's R4 "backward comma"
hooks are the same curl shape (compare `marks/h19_hooks_zoom.jpg` with `images/shorthand/page1_L06_seq26-39_8marks.jpg`
idx2), but in the target the curls stand inside mark runs, not under digits; the R5 baseline dash has no counterpart in
the office letter. Same pen shape, different placement -- H16 answered as "shape yes, placement no" (M), no further
step of its own.

No reading, no class change. Requests: none. Cost: get_session read 28.99 USD at 23:57 before H14; the rows' estimates
(1 + 1) are what `campaign.py --spend` records for H19 and H16. Vision: 3 zoom/crop reads by this runner, no subagent.

## Campaign step H18 (28 Sept 2026, 00:12-00:25 UTC)

Runner: campaign runner armstrong-madison-1808 (account 2, session_013E5jUS9GV1AsxLeUcwgbf6). Hypothesis H18: a full
inventory of marks attached to numeral groups over all four pages and both witnesses, by class (a HIGH mark after or
above the group; a LOW mark under a specific digit, with the digit named) and a test of whether marks recur on the same
value.

**Method.** Top-margin line sheets (`images/crops_h18/`, five lines per sheet, each line box from the page's crop
manifest widened to reach into the gutter, +55 px above; page 4 cut with `tools/iiif_lines.py --image`; the sheets are
rebuilt by `images/crops_h18/regen_sheets.py`, not committed). Eight blind Sonnet passes, one per page per witness
(page 1 has one frame, so two readers on the same sheets; page 4 one frame, one reader), each reporting per line the
first groups and every marked group as GROUP:CLASS:DETAIL (`marks/h18_passes/*.tsv`). `marks/h18_inventory.py`
reconciles by page + group + class (the two witnesses' crop manifests number lines with an offset): a mark is
ACCEPTED when two independent sources report it, HELD when one does (`marks/h18_inventory.tsv`).

**Inventory: 33 reported, 5 accepted, 2 near-matches, 26 held (most of them flagged "faint" by their own reader).**

| page | group | class | detail | sources | status |
|---|---|---|---|---|---|
| 1 | 200 | HIGH | curl/loop above-left of the first digit (both readers; one says it may be the top of the 4-like "2") | 2 readers, 1 frame | accepted |
| 1 | 38 | HIGH | check mark immediately after the group | 2 readers, 1 frame (+ H13, both readers) | accepted |
| 1 | 36 | HIGH | small caret/arc above the group (the interlinear "36"-like mark of H5/H13) | 2 readers, 1 frame | accepted |
| 3 | 1580 | HIGH | short tick above the third digit / two dots above | both witnesses | accepted |
| 3 | 49 | LOW, under the LAST digit | curl swept beneath the group, attached to the 9 | both witnesses, both H | accepted |
| 2 | 1640 | HIGH | double dot / colon after the group (0031 reader explicit; 0032 reader put a caret on the same line at "1540", a value not on that line) | 2 witnesses, mis-attributed once | near-match, held (+ H13: both witnesses by this runner and a second reader) |
| 3 | 230 / 1254 | HIGH | a tick between "230." and "1254", attributed to either neighbour | both witnesses | near-match, held |
| 3 | 740 | LOW, under the last digit | small dot beneath the 0 | 0031 only | held |
| 1 | 1640, 1276 | HIGH | faint ticks above (one reader: "may be the ordinary 7 ligature") | 1 reader | held (H13: possibly verso bleed-through) |
| 4 | 1740, 124, 671, 1207, 14, 47 | HIGH | "tick bands" between rows | 1 reader | held -- this runner's look at the sheet: these are the descender tails of 7s and 9s from the line above caught by the top margin, not marks |
| 2, 4 | 78, 5 | LOW, under the first digit | faint curl / blot | 1 reader each | held |
| others (16) | | HIGH | faint ticks above, single reader | 1 | held |

**Value-recurrence test.** Accepted-marked values: 200 (1 occurrence in the letter), 38 (10), 36 (2), 1580 (1), 49 (1).
Marked at every occurrence: 0 of the 2 multi-occurrence values (38 is marked at 1 of its 10 occurrences, 36 at 1 of 2);
null (marked positions kept, values redrawn among groups of the same digit length, 2,000 draws): mean 0.01, p95 0.
The one value that carries a mark at both occurrences is 1640 (page 2 corroborated, page 1 faint), outside the
accepted set. Reading: marks are not labels bound to a value (a homophone or variant sign); they attach to a
particular occurrence -- the 38 case (marked once in ten) decides it -- which is what the printed form's operators are
(H14: plural / tense after the group, double / withdraw the letter under a digit), and what H19 found the same writer
doing in his office letter (a curl under the last digit = double the last letter). Rate: 7 corroborated marks in 369
groups (1.9%) against 6 in about 243 groups of the office letter (2.5%).

**By class, corroborated:** HIGH after/above 6 (200, 38, 36, 1580, 1640 double dot, 230/1254 tick); LOW under a digit
1 (49, under the last digit -- the printed form's "doubles the last letter"). Under the printed grammar the 49 group
would be a syllable whose last letter is doubled; 1640 and 38 carry a grammatical mark (plural / genitive / third
person, or participle / imperfect); that is a hypothesis about the design, not a reading, and it needs a key.

**Verdict for the campaign:** inventory on file (grade M per mark, corroborated ones listed); marks are per-occurrence
operators, not value-bound labels (control-backed: 38 marked 1 of 10; shuffle null p95 0); consistent with the printed
form's mark grammar this writer demonstrably used in office usage. What it changes: the design prior for the target
moves toward a syllabic / spelling nomenclator on a printed 17x100 form with modifier marks -- the family ARM-DESIGN's
contiguous designs did not include (its "units digit = fixed member slot" finding was on a different axis). Named next
steps: (1) H20: re-run ARM-DESIGN's design statistics with the marks stripped and with syllabic-table encoding
controls built from the H12 table's own entry classes (words vs syllables per hundred), since the target's 901-1099
trough and 0/1 units skew now need explaining against a syllabic printed-form design rather than a word nomenclator;
(2) H21: a second reader on the 26 held marks with single-line zooms (the eight passes read stacked sheets; the
page-3 readers who zoomed per group were the ones who agreed at H). No reading, no class change. Requests: none. Cost:
8 Sonnet passes plus this runner's reconciliation; the row's estimate (8 USD) is what `campaign.py --spend` records.
Housekeeping: `images/` tracked size was 37 MB after this session's sheets; the derived crops of H5, H13 and H18 are
now untracked with regeneration scripts (`images/regen_derived_crops.py`, `images/crops_h18/regen_sheets.py`), tracked
size 29.6 MB.

## Campaign step H24 (28 Sept 2026, 00:30-00:45 UTC)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01R2T5qwd7NBMWGnjRtj8ieX). Hypothesis H24 (the
orchestrator's 00:26 row, first numbered H20): Tomokiyo's six shorthand systems, with a different instrument from
ARM-S2/S3's shape-vs-letter scoring -- a per-system KNOWN-ANSWER control run first, and the target read only for a
system whose control passes.

**Instrument.** A Sonnet subagent that sees only one period alphabet plate and four line strips of shorthand, is told
nothing about the book, author, system or text, is forbidden web tools, and returns letters per word
(`h24/reader_*_control.tsv`). Gate, scorer and null were fixed before any output existed (`h24/PREREGISTRATION.md`,
00:39 UTC; `h24/score.py`: S1 = local-alignment match rate of the consonant skeleton against the reference passage,
S2 = reader words whose skeleton equals a reference word skeleton; null = 200 random bijections of the consonant
alphabet applied to the same output; PASS needs S1 > p95 and S2 >= 3 and S2 > p95). Self-test: reference words with
30% of characters randomized read S1 0.316 vs p95 0.029, S2 17 vs 7 -- the scorer discriminates.

**Known-answer specimens (fetched this step, archive.org, `h24/specimens/MANIFEST.tsv`).** Mavor 1792, the book's own
Plate V, Job xxix 7-22 (leaf 74, engraved by Terry, 17 lines; lines 1-4 used; reference KJV Job 29:7-22). Byrom 1796
abridgement, Plate I, the Lord's Prayer and Psalm 1 (leaf 94; the contents leaf 93 names them, "Common Prayer";
lines 1-4 of the body; reference BCP and KJV, best of the two). Plates: the ones ARM-S1 put on disk
(`images/shorthand/specimens/mavor1792_alphabet_plateI.jpg`, a clean engraved labelled alphabet with the vowel-place
table; `byrom1796_alphabet_p12.jpg`, the typeset consonant list).

**Results (both controls, rule 3 "whatever they say"):**

| system | specimen | reader words | "?" signs | S1 | null p95 | p | S2 | null p95 | verdict |
|---|---|---|---|---|---|---|---|---|---|
| Mavor 1792 | Job 29:7-10, engraved, clean | 63 | 34 | 0.108 | 0.135 | 0.315 | 1 | 1 | CONTROL FAIL |
| Byrom 1796 | Lord's Prayer, dark microfilm | 22 | most positions | 0.250 | 0.375 | 0.740 | 0 | 1 | CONTROL FAIL |

Both readers report low confidence in their own "#" blocks: the plate's hook/loop/cup families (b/d, m/n, p/f/g/v,
c/z, s/wh on Mavor; nearly every consonant on Byrom's typeset list) are not separable at line-strip scale, and the
reader cannot map Mavor's vowel-place table back onto the strips. Mavor's read is a shape match at chance level (16
of 63 words read as a bare "n" cup; the numeral-like "2" of the engraving read as a numeral), on the cleanest
possible input -- an engraved specimen of the system's own inventor, with the inventor's own labelled plate.

**Verdict for the campaign.** CONTROL BELOW GATE for both systems tried: the plate-only line-strip reader cannot read
even the systems' own specimens, so the target's marks were NOT read with it (family_run.py order, rule 3). This is a
non-test of the instrument, not a negative on Mavor or Byrom, and it says nothing about whether the target's marks
are in either system. What it does say, retroactively: ARM-S2/S3's symbol-match scores came from the same class of
reader (plate plus exemplar crops, no known-answer check), which this step shows reads a system's own specimen at
chance -- consistent with those passes' own "non-test / not an identification" wording, and a reason not to cite
their per-system numbers as exclusions. Weston, Macaulay, Gurney and Mitchell were not reached (4-call limit, 2 used;
cap reached). Specimen leaves for the next attempt are fetched and on disk untracked (Weston 1727 leaf 59, "The Lord's
Prayer"; Macaulay 1747 leaf 22, Psalm I "in the long shorthand, wherein all the vowels are inserted" -- the best
known-answer specimen of the six, since the vowels are written), refetch route in `h24/specimens/MANIFEST.tsv`.

**Named next step (one knob, once, per CLAUDE.md rule 3's "second attempt" paragraph):** the same control on Macaulay's
Psalm I with per-word magnified crops (the H18 lesson: the readers who zoomed per group were the ones who agreed at H)
and the plate's own worked examples on the same call; if that control also fails, the plate-only reader is retired
for this family and the shorthand question needs a different instrument (a person who reads one of these systems, or
a trained model), logged in HYPOTHESES.md as "untested-by-this-tool". Filed as H28.

Files: `h24/PREREGISTRATION.md`, `h24/score.py`, `h24/ref_*.txt`, `h24/reader_mavor_control.tsv`,
`h24/reader_byrom_control.tsv`, `h24/specimens/` (8 strips + MANIFEST.tsv), `h24/target_*.jpg` (five target line crops
prepared for the read that was not licensed), `h24/en18_skeletons.txt`. No reading, no class change, no target token
decoded. Requests: archive.org about 27 (metadata, fulltext inside.php, OCR/scandata downloads, 5 leaf images), all
>= 1.5 s apart, descriptive User-Agent, no 429/403; gutenberg.org 2 (one proxy reset, one retry). Cost: get_session
8.72 USD at 00:43 UTC for the session, about 7 USD on this step against a 6 USD cap (two Sonnet calls about 1.1 each;
the rest this runner's own image reads and setup); 2 of 4 vision calls used.

## Second-opinion checkpoint (SO-ARMSTRONG-CHECKPOINT 00:21, 28 Sept 2026)

Landed from PR 58 (`second-opinions/chatgpt-checkpoint-2026-09-28-0021.md`, PR-LAND-22). A runner checkpoint
report, not a leads-prompt answer or a reading; every citation below is a claim to verify, never a fact --
unchecked.

- lead/negative; Armstrong to Monroe, 30 May 1806 (LOC reel 3 frames 852-853) inspected -- ordinary prose, no coded passage observed -- unchecked.
- lead/negative; Armstrong to Monroe, 27 February 1806 (frames 749-751) inspected -- ordinary prose, no coded passage observed -- unchecked.
- lead; George W. Erving to Monroe, 5 Feb 1806 (frames 740-744) carries contemporary interlinear plaintext that agrees with the repository's WE028 table on 12 selected values (134+1379=Mister, 1399+1229+637=this government, 1576+1385+970=of the Floridas, 648=million(s), 794=dollar(s), 569+182=to him), with a small manuscript mark read as a suffix/plural operator in this witness -- a control for WE028, not for Armstrong's own cipher -- unchecked.
- lead/negative; the 366-decimal-group target transcription overlaps these same 12 WE028 values only once (648 at position 357), called not probative -- unchecked.
- lead/negative; the calendar-listed Armstrong-to-Monroe letter of 7 January 1806 is not in the immediate frame 739->740 chronological transition (frame 739 docketed 2 Jan 1806, frame 740 begins a 5 Feb 1806 letter) -- unchecked.
- next-step; use the Monroe Papers 1963 index and 1904 chronological calendar to get an item-level locator for the 7 January 1806 letter before further scanning -- unchecked.

No check-solved candidate (no printed decipherment of the Armstrong letter, its key, or the Livingston key is named; WE028 is stated to be a different code table from Armstrong's reported cipher).

## Second-opinion checkpoint (SO-ARMSTRONG-CHECKPOINT 00:31, 28 Sept 2026)

Landed from PR 59 (`second-opinions/chatgpt-checkpoint-2026-09-28-0031.md`, PR-LAND-22). A runner checkpoint
report, not a leads-prompt answer or a reading; every citation below is a claim to verify, never a fact --
unchecked.

- lead; the 1963 Index to the James Monroe Papers (LOC, PDF page 18) prints a row "*ARMSTRONG JOHN TO JM2, 1806 JA 7, series 1, 4 indexed pages" -- a precise archival locator for the 7 January 1806 letter -- unchecked.
- lead; the 1904 Calendar of the Correspondence of James Monroe (p.18) summarizes the same letter as "Negotiations with Spain... No time should be lost... The Emperor's arrival expected. fol. 3 pages" -- a content control, not a transcription -- unchecked.
- lead/negative; the indexed four-surface item is absent from its expected chronological position in the public LOC reel 3 image sequence -- frames 720-739 are continuously occupied by other, dated material and frame 740 opens a different letter, with no gap or failed frame between 739 and 740 -- unchecked.
- next-step; search for an alternate digital surrogate or duplicate of this exact four-surface item (another LOC reel/microfilm surrogate, an NYPL Monroe Papers duplicate, or a published quotation) matching the letter's heading/date, addressee and Spain/Emperor content -- unchecked.

No check-solved candidate (the 1963 index and 1904 calendar are catalogue entries, not a printed decipherment of the Armstrong letter, its key, or the Livingston key).

## Second-opinion checkpoint (SO-ARMSTRONG-CHECKPOINT 00:46, 28 Sept 2026)

Landed from PR 60 (`second-opinions/chatgpt-checkpoint-2026-09-28-0046.md`, PR-LAND-22). A runner checkpoint
report, not a leads-prompt answer or a reading; every citation below is a claim to verify, never a fact --
unchecked.

- retraction; withdraws the immediately preceding 00:31 checkpoint's "missing 7 January witness" claim: frame 739 is read as 2 Feby 1806, not 2 January, and the 1963 index's PDF page 28 independently lists a Monroe-to-Madison letter of 2 February 1806 (Series 1, 38 pages) at that position, so the 739->740 transition is Feb 2 to Feb 5, not a gap -- unchecked, and marks the 00:31 section's "expected chronological position is absent" lead superseded pending independent recheck.
- lead/negative; also corrects the 00:21 checkpoint's identification of the Erving letter's place as Paris -- frame 740 is read as Madrid -- unchecked; the WE028 interlinear examples from frames 742-743 are said to be unaffected by this correction.
- lead; Armstrong to Monroe, 7 January 1806, located and inspected at LOC reel 3 frames 687-689 (heading "7th Jan. 1806, Paris", docket "7 Jany 1806 / General Armstrong") -- ordinary prose on the Spanish negotiation and the Emperor's expected arrival, no coded passage observed -- unchecked.
- lead; Ford's Writings of John Quincy Adams vol. 3 (pp.322, 327-328 and 369-370) is cited as documenting a cipher shared among Short, Armstrong and Adams, and Adams's 3 Jan 1810 despatch acknowledging receipt of "Armstrong's cypher" -- said to verify transmission context only, not to recover a code table or connect it to the February 1808 target -- unchecked.
- archival-route; Tatum, "Ten Unpublished Letters of John Quincy Adams 1796-1837," Huntington Library Quarterly 4(3) (1941), DOI 10.2307/3815711, pp.369-388, cited as discussing the 27 Nov 1809 Adams-to-Armstrong letter (Huntington mssHM 22922) at p.376; article text not acquired (JSTOR client challenge) -- unchecked.
- next-step; use the MHS Adams Papers correspondence/letterbook calendar to find a publicly accessible copy of Adams to Armstrong, 27 Nov 1809 -- unchecked.

No check-solved candidate (Ford's volume documents cipher transmission context and correspondence, not a printed decipherment of the Armstrong-Madison letter, its key, or the Livingston key).

## Campaign step H25 (28 Sept 2026, 00:46-01:03 UTC)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01R2T5qwd7NBMWGnjRtj8ieX). Hypothesis H25: the
intended correspondent, Monroe -- list the Armstrong-to-Monroe letters 1804-1808 in the digitised LOC Monroe Papers
(mss33217), look at each for cipher, screen any coded page by digit signature against the target.

**Route.** loc.gov's collection search does not index the Monroe Papers by correspondent (`?q=armstrong` returns 0);
the reels are whole-reel items (Series 1 reel 3 = mss33217003, 1803 Oct 9-1807 Jan 16, 1159 frames; reel 4 =
mss33217004, 1807 Jan 24-1812 Mar 12, 1161 frames), each frame at
`tile.loc.gov/image-services/iiif/service:mss:mss33217:00R:HH00:FFFF/full/{pct:25|full}/0/default.jpg` (the H7 route;
pct:25 = 666 px is enough to read a date line, full for reading groups). The letters were dated from the 1904 LOC
*Calendar of the Papers of James Monroe* (archive.org papersofjamesmon00libr, OCR grepped): Armstrong to Monroe Dec
1804 (two, one "24"), Feb 1806 (two, one 27 Feb), 30 May 1806, 9 July 1806, 4 Apr 1807 (to Monroe and Pinkney), 7 July
1807; none in 1808 (Monroe was back in Virginia). The 1963 *Index* PDF (tile.loc.gov gdclccn 62060006) was fetched but
its text layer could not be read here (no pdftotext; pypdf's crypto import is broken in this container) -- not used.
Frames were found by date interpolation and contact sheets (about 160 frames looked at at pct:25, listed in
`h25/MANIFEST.tsv`).

**Armstrong-to-Monroe letters located: 6 of 8, all in clear (H at pct:25, no numeral group on any page):**

| letter (1904 calendar) | reel:frames | what the frames show |
|---|---|---|
| Feb 1806 (first) | not located (between reel 3 f0700 and f0740; the run 700-739 is Monroe's own 2 Feb 1806 despatch to Madison, 12 pp, and Monroe letterbook pages) | -- |
| 27 Feb 1806 | 3:0749-0751 | "Paris 27 feb 1806", one page, clear; docket f0751 "27 Feby 1806 Genl Armstrong" |
| 30 May 1806 | 3:0852 | short Paris 30 May 1806 note, clear (signature not read at pct:25, M) |
| 9 July 1806 | 3:0903-0907 | "Paris July 3 1806", four pages clear (mentions "my letters by Mr Skipworth"), address leaf "James Monroe Esq, Minister of the U.S., London" |
| 4 Apr 1807 | 4:0166 | "Paris April 4th 1807, Gentlemen ... John Armstrong", one page, clear |
| 7 July 1807 | 4:0302 | docket "J. Armstrong 7 July 1807"; the sheet photographed mirror-reversed, clear prose |
| Dec 1804 (two) | not located (the reel-3 anchor sheet for frames 300-650 failed on a truncated download; not retried within the box) | -- |

**Unlooked-for find, for H26 (Erving): a coded Erving-to-Monroe letter with a full interlinear period decode.** Reel 3
frames 0740-0744: "Private, To James Monroe, Madrid Feby 5th 1806", the writer at Madrid who has "written you on the
25 Oct, Nov 15 & 29" and encloses "the only letter which I have received from Mr Madison" -- George W. Erving, US
chargé at Madrid, Monroe's protégé (signature on f0744 read at pct:25 as Erving's, M). Frames 0741-0743 carry numeral
code groups inside clear prose, every group glossed above the line in a period hand: f0741 19 groups (1385 the, 1044
con, 1280 duct, 1576 of, 995 French, 28, 1229 govern, 837 ment, 1786 will, 1365 take, 1094 she, 835 de, 1369
liberation, 992 France; `h25/erving_1806-02-05_f0741_groups.tsv`, read at 1800 px, H for the digits, C for the glosses
since they are the leaf's own), f0742 about 150 groups (569 to, 1426 in, 888/668 and, 169 he, 1190 with, 184 his, 1384
that, 1310 be, 90 should, 182 him, 1592 this, 1393 they, 999 from, 1259 have, 1386 their, 934 our, 581 for, 361 not,
1351.854.1426 Bow-do-in, 970 Floridas, 987 four, 648 millions, 794 dollars, 240 six, 134.1379 "Mr [name]";
`h25/erving_1806-02-05_f0742_groups_M.tsv`, 115 pairs, grade M each -- one reader at 1800 px, to be re-read at native
by a proper pass). Views of both frames are committed at 1800 px in `h25/`; refetch URLs in the manifest.

**Screen against the target (rule 3, control-backed on a screen, not a solve):**
- 0 of 21 Erving common-word values occur in the target's 369 groups (the 1385, to 569, of 1576, and 888/668, in 1426,
  he 169, with 1190, his 184, that 1384, should 90, him 182, this 1592, they 1393, from 999, have 1259, their 1386, our
  934, for 581, not 361, an 1549; be 1310 once, as 680 once). "the" alone: 4 of 19 groups on f0741; P(0 of 369 | that
  rate) 1e-38, P at a conservative 5% 6e-9.
- distinct-value overlap: 13 of Erving's 121 values as read occur among the target's 216 (11 among values >= 100),
  against an independence null of 10.8 (p95 16) -- exactly chance.
- digit signature: Erving units 0/1 share 0.05 (f0741, n 19) and 0.28 (f0742, n 115) vs the target 0.43; units 2/3/5/9
  0.58 / 0.36 vs the target 0.12; Erving uses almost no groups under 100 (9, 21, 28, 90) where the target's ten most
  frequent groups are all under 100.
- Verdict: the Erving-Monroe private code of 1806 is not the target's code, control-backed on a screen; it is a
  different design (values to about 1600, syllable and word entries mixed, one-part traces such as France 992 / French
  995 and Bow 1351 / do 854 / in 1426, but govern 1229 / ment 637 and de 835 / liberation 1369 are not alphabetical --
  a two-part or mixed table, not decided here).

**What it changes.** For the target: the Monroe channel is screened clean for 6 of 8 letters (all clear), which lowers
H25/H26's expected value for Monroe and leaves the Dec 1804 pair and the first Feb 1806 letter as the only unlooked
items. For the repository: a US diplomatic private code of 1804-06 with about 200 known-plaintext pairs on three
frames is a key source in its own right (KEY-OFFICES/KEY-DESIGN at close-out, `tools/design_prior.py`), and a test
material for whether it is WE027 (Livingston's code, which Weber says Monroe also received) -- ARM3-LIVCODE's
Livingston specimens (LOC Madison Papers, 1803-04) can be checked for 1385 = the and 569 = to directly. Filed as H29.
Rule 10: nothing here is called new or first; the Erving letter is listed in the 1904 calendar and its decode is the
period's own. No target token decoded, no class change.

Requests: www.loc.gov 5 (collection/item JSON), tile.loc.gov about 175 frame fetches (pct:25) + 8 at full, all one at
a time >= 1.6 s apart, no 429/403; archive.org 2 (1904 calendar OCR, advancedsearch). Cost: the get_session figure had
not refreshed at 00:57 (still 8.72 from 00:43); this step's own work is about 170 small image fetches, 12 contact-sheet
looks and 5 native looks by this runner, no subagent -- the row's estimate (4 USD) is what `--spend` records, with the
parent's reconciliation to follow from get_session.

## Campaign step H20 (28 Sept 2026, 01:03-01:07 UTC)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01R2T5qwd7NBMWGnjRtj8ieX). Hypothesis H20 (the
account-2 runner's row from H18): are the target's 901-1099 trough and its 0/1 units-digit skew what a
syllable-spelling nomenclator on a 17x100 printed form with modifier marks produces -- the design family H14/H19
point at, which ARM-DESIGN's contiguous WORD-table controls did not cover?

**Method (`design/h20_form_syl.py`, script only, offline, 15 s; log `design/h20_run_log.txt`, table
`design/h20_stats_sim.tsv`).** Six printed-form designs, 60 simulated 369-group letters each from en18 text, scored
with ARM-DESIGN's own statistics (`design_stats.stats`, target vmax 1900, forms vmax 1700), target percentile per
statistic. A form is 1,700 cells; entries are 564 syllable/letter fragments taken from the two sibling tables (WE028
532 + THE972 116, deduped) plus 26 letters, and the commonest en18 forms for the rest; with or without a CATEGORY
block in cells 901-1100 (212 number words, ordinals, months, days, places, period personal names and titles -- the
kind of entries H12 read in that region of the reel-9 form: twelve 907, june 1007, friday 1016, virginia 1026); fill
alphabetical (one-part) or random; a 300-fragment variant for sensitivity. The printed form's marks are modelled as
free: a word is one group if the form holds it or its stem without -s/-es/-ed/-d (rules 1-2 make those a mark), or
its form with doubled letters collapsed (rule 3); otherwise it is spelled greedily from fragments (32-36% of groups
in every design; no word dropped). Each statistic can differ between the designs it compares (rule 3): the block
changes `block_pair_min`, alphabetical vs random changes `digit_order_rho`/`low_share`, fragment count changes `D/N`.

| statistic | target | form_alpha_cat | form_rand_cat | form_alpha_nocat | form_rand_nocat | F300 cat (alpha / rand) |
|---|---|---|---|---|---|---|
| block_pair_min (the 900-1099 trough) | 4 | 6.7 (p18) | 7.1 (p20) | 20.1 (p0) | 17.9 (p0) | 6.6 / 6.9 (p20) |
| share of groups in 901-1100 | 0.011 | 0.018 | 0.019 | 0.114 | 0.122 | 0.019 / 0.019 |
| units_top1 (values >= 100) | 0.388 | 0.200 (p100) | 0.164 (p100) | 0.152 (p100) | 0.165 (p100) | 0.150 / 0.171 (p100) |
| units_H (bits) | 2.57 | 3.15 (p0) | 3.24 (p0) | 3.25 (p0) | 3.24 (p0) | 3.25 / 3.22 (p0) |
| digits23_share | 0.083 | 0.137 (p0) | 0.239 (p0) | 0.171 (p0) | 0.228 (p0) | 0.197 / 0.219 (p0) |
| decade_units_z | 2.76 | 15.7 (p0) | 19.1 (p0) | 17.2 (p0) | 19.3 (p0) | 18.1 / 20.1 (p0) |
| low_share (groups < 100) | 0.358 | 0.083 (p100) | 0.059 (p100) | 0.074 (p100) | 0.055 (p100) | 0.075 / 0.060 (p100) |
| D/N | 0.585 | 0.494 (p100) | 0.483 (p100) | 0.497 (p100) | 0.486 (p100) | 0.458 / 0.447 (p100) |
| hi_distinct | 168 | 170 (p38) | 168 (p48) | 172 (p28) | 169 (p43) | 158 / 155 (p85-90) |

**Reading.** (1) The trough IS what a category block produces: with 200 rarely-used entries in 901-1100 the
simulated letters put 1.8-1.9% of their groups there and their pair-minimum sits at 6.6-7.1, the target's 4 inside
the band (p18-20); without the block the same forms give 18-20 (p0). A category block is therefore a second
sufficient explanation of the 901-1099 trough, alongside ARM-DESIGN's "sparsely occupied numbering" -- the two are
not distinguished by this statistic, and the design prior should carry both. (2) Nothing else about the target is a
syllabic printed form: the units-digit concentration (0.388 vs 0.15-0.20, p100 on every variant; entropy p0;
digits 2/3 share p0), the decade/units dependence (2.8 vs 16-20: in a form the frequent words repeat inside their
own decade, in the target they do not), the third of all groups under 100 (0.36 vs 0.06-0.08 even when the
alphabetical fill puts a/an/and/as/at in cells 1-99), and the diversity (D/N 0.585 vs 0.45-0.50: syllable spelling
repeats its fragments, the target repeats less than a 32-36%-spelled letter would). Sensitivity: halving the
fragment inventory moves D/N further from the target, not nearer. (3) Marks modelled as free grammar do not change
the picture (they only raise whole-word matches).

**Verdict for the campaign: control-backed FAIL for "the target is a syllable-spelling printed form of the reel-9
kind"** (six designs x 60 letters, the target outside the band on five independent statistics), with one retained
finding: the 901-1099 trough needs no sparse numbering -- a category block explains it as well. ARM-DESIGN's
conclusion stands and is sharpened: a separate particle list at 1-99 (the forms cannot make low_share), decade =
family and units = fixed slot above 100, and the trough undecided between sparse numbering and a category block.
Conditional on ciphertext.txt (match_ratio 0.984 after H17). Not a reading, no class change; rule 10 wording.
Suggestion (not filed as a row: too weak at 4 tokens): under the category-block reading the target's four groups in
901-1099 would be numbers, dates or names -- their positions in the text against the letter's date line and any sums
could be looked at when a reading exists. For the lane close-out: `tools/key_design.py` / KEY-DESIGN.tsv gain the
printed-form family (one-part 1-1700, category block, syllable+word, modifier marks) from H12/H14, with this step's
statistics as its plaintext-free signature.

Requests: none. Cost: script only, no subagent, no image; the row's estimate (3 USD) is what `--spend` records
(get_session had not refreshed its cost figure since 00:43).

**Addendum to step H25 (01:10 UTC clock read, same runner).** Two corrections after reading the second-opinion
checkpoints that PR-LAND-22 landed at 00:55 UTC while H25 was running: (1) credit -- the ChatGPT sprint's 00:21
checkpoint (`second-opinions/chatgpt-checkpoint-2026-09-28-0021.md`) had already inspected the same Erving-to-Monroe
letter (frames 740-744) and reported its interlinear glosses agreeing with the repository's WE028 table on 12 values;
"unlooked-for" above means unlooked-for by this runner, not by the project. (2) identification -- checked here by
script: of the 49 group/gloss pairs this runner read on frames 741-742 (grade M), 38 agree with
`tools/data/uscodes-1800/WE028.tsv` (1385 the, 1576 of, 569 to, 1426 in, 668 and, 169 he, 1190 with, 184 his, 1384
that, 1310 be, 90 should, 182 him, 1393 they, 999 from, 1259 have, 1386 their, 934 our, 1549 an, 1351 bow, 854 do,
970 florida, 987 four, 648 million, 794 dollar, 240 six, 215 prince, 256 spain, 1030 citizen, 1182 whose, 9
character, 1094 she, 995 french, 992 france, 1229 govern, 1044 con, 1280 duct, 1365 take, 361 noth-); the 11 misses
are this runner's low-resolution reads (837, 835, 1369, 888, 1592, 581, 680, 134, 137, 664, 1786) to be re-read
before they are held against the table. So the Erving-Monroe letter of 5 Feb 1806 is a usage specimen of WE028
(the "Livingston/Monroe" sibling table already on file), not a new key -- which is why the screen against the
target fails: ARM-A2 already showed WE028 does not transfer to the target (both rule-3 controls), and H25's
common-word screen is the same negative seen from the usage side. H29 is re-scoped accordingly (a real WE028 usage
control for `design/`, a KEY-OFFICES row "WE028: Erving at Madrid to Monroe at London, Feb 1806", est 1.5). (3) The
same checkpoints (00:31, 00:46) report the calendar's 7 January 1806 Armstrong-to-Monroe letter at reel 3 frames
687-689, clear prose -- unchecked by this runner; if it holds, it is the "first 1806 letter" H25 could not place,
leaving only the two December 1804 letters unlooked.

## Campaign step H30 (28 Sept 2026, 01:09-01:12 UTC)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01R2T5qwd7NBMWGnjRtj8ieX). Hypothesis H30 (from the
sprint's 00:46 checkpoint, unchecked there): Ford's *Writings of John Quincy Adams* documents "Armstrong's cypher"
shared with Adams in 1809-10 -- if Armstrong supplied Adams a private cipher, the Adams Papers would be a pool for it.

**Source read (archive.org OCR, `writingsofjohnqu03adam` vol. 3 1801-1810 and `fordsjohnadams04adamrich` vol. 4
1811-1813; 98 distinct cypher/cipher passages grepped, the five near Armstrong/Short/key read in full).** The lead
is real and it resolves the other way:
- Robert Smith (Secretary of State) to Adams, instructions of 1809, printed p. 327-328 (running head "328 THE WRITINGS
  OF [1809"): "The cypher with which you are furnished, being the same with that of our minister at London, you will
  be able to correspond confidentially with him ... You will do well to obtain at Paris, a copy of General
  Armstrong's cypher also, for the like purpose. The advantage of corresponding with those ministers, in cyphers
  KNOWN TO THIS DEPARTMENT, is, that in their transmitting hither information received from you, the labor and delay
  of translating it into another cypher may be avoided." (grade H, printed text.)
- Adams to the Secretary of State, early 1810 (the checkpoint's pp. 369-370; the despatch of 3 Jan 1810): "With these
  papers, I received also the copy of General Armstrong's cypher, of which I shall have immediate occasion to make
  use." (H)
- The same 1808-09 instructions also mention a cipher "of General Armstrong, a copy of which was transmitted to our
  consul at St. Petersburg" (Harris) -- the same departmental copy circulating.
- Vol. 4: Adams to Erving, St Petersburg 6/18 June 1811, footnoted "Cypher" (Adams and Erving corresponding in a
  Department cipher); p. 117 (1811) prints "[one-half line of cipher not deciphered]" in a despatch -- an
  undeciphered passage in Ford's edition, not this target's business (a scout note, below).

**Reading.** "General Armstrong's cypher" in Ford is the Department's own cypher issued to the Paris legation -- a
cypher "known to this Department", copied to the consul at St Petersburg and to Adams so that inter-legation traffic
could be forwarded to Washington without re-enciphering. Armstrong's Department cypher in 1808 is THE=972 (Bourdeau's
decodes of 15 Feb, 22 Feb and 30 Aug 1808, `tools/data/uscodes-1800/`), which does not read the target (Bourdeau;
ARM-A2). So the Adams Papers would hold THE=972 traffic, not a second letter in the target's code; the "private
cipher" premise of the row is not supported by the source it rests on.

**Verdict for the campaign: done, lead resolved, no pool** -- a source reading (H), no statistic and no control needed
(nothing here is a solver result). What stays useful: (a) the circulation of THE=972 copies (Paris, the St Petersburg
consul, Adams) is a KEY-OFFICES.tsv fact for the close-out; (b) for the scout, not this target: Ford's vol. 4 p. 117
"[one-half line of cipher not deciphered]" (Adams, St Petersburg, 1811) and the "few lines in cipher to the President"
(vol. 4 p. 55, 1811) are printed undeciphered US diplomatic cipher of 1811 in a Department cypher whose tables
(THE=972 / WE028 family) are partly on file -- a check-solved candidate for QUEUE.md, cheap because the key family is
known. Rule 10 wording; no reading, no class change. Requests: archive.org 3 (advancedsearch + two OCR downloads).
Cost: script only, no image; the row's estimate (1.5 USD) is what `--spend` records.

## Campaign step H21 (28 Sept 2026, 01:14-01:29 UTC)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01R2T5qwd7NBMWGnjRtj8ieX). Hypothesis H21 (from
H18): a second reader on the 26 held H18 marks with single-line zooms per group, promote or drop each, re-run the
inventory.

**Method.** `marks/h21/cut_zooms.py` cut one 2x line zoom per held mark (30 zooms for 28 held rows: 1540 and 1207 had
two candidate lines) from the witness frame the holding reader used, the pass line number mapped through that
witness's crop manifest (`marks/h21/zooms.tsv`; crops untracked in `images/crops_h21/`, rebuilt by the script). Two
blind Sonnet calls (pages 1+4, pages 2+3; `marks/h21/task_*.tsv`), each given only the crops and the group value to
examine -- never the holding reader's description or class -- and asked for MARK / NONE / UNSURE, class HIGH (after or
above) or LOW (under which digit), and what else the stroke could be (descender from the line above, show-through,
separator period, part of the digit). Verdicts `marks/h21/reader_p14.tsv`, `reader_p23.tsv`; merge `marks/h21/merge.py`
-> `verdicts.tsv`, `drops.tsv`, second-source pass files `marks/h18_passes/p1_w30_C.tsv`, `p2_w31_C.tsv`,
`p2_w32_C.tsv`; `marks/h18_inventory.py` now honours `h21/drops.tsv` and was re-run.

**Result: 28 held -> 4 promoted, 20 dropped, 4 still held.**

| outcome | groups | notes |
|---|---|---|
| promoted (second source, same class) | p1 31 HIGH; p2 1480 HIGH (curl after), p2 1640 HIGH (double dot after -- its third confirmation with H13), p2 28 HIGH (bar above) | 31 is the weakest: the readers agree on the class but describe different things (a colon before the group vs an ornate hook on its last digit) -- accepted by the reconciler's rule, graded M here |
| dropped (zoom: nothing attached; show-through, a descender from the line above, a recurring margin pattern, or the separator period) | p1 1640, 1276, 1350, 1320; p2 1540, 17, 1158, 1741; p3 230, 1254, 740, 1354; p4 1740, 124, 671, 1207, 14, 47 | the page-4 "tick bands" H18 already suspected as descender tails all fall here; p1 1640/1276 confirm H13's bleed-through reading |
| dropped (group not on its line at zoom) | p2 78 (line reads 17.86.316.582.1017.18...), p2 29 (line reads ...84.19.41...) | the holding reader's value is unconfirmed; the mark cannot be attached to anything |
| held, class disagreement | p1 65: zoom reads a solid black CARET UNDER THE LAST DIGIT (H) where the holding reader saw a faint hook above; p1 1141: a thin low stroke under the penult digit (M) vs a stroke above; p4 5: an X-shaped crossing at the top of the ascender (M) vs a curl under the first digit | 65 is the one to look at again: a caret under the last figure is frame 956's rule 3 exactly (H14) and the office letter's own device (H19); one more independent look at that group settles it |
| held, unsure | p3 760 (faint token beside a possible descender) | |

**Inventory after H21 (`marks/h18_inventory.tsv`): 9 accepted (8 HIGH after/above: 200, 38, 36, 31, 1480, 1640, 28,
1580; 1 LOW under the last digit: 49), 4 held, 20 dropped.** Rate 9 corroborated marks in 369 groups = 2.4% (office
letter 2.5%, H18). Value-recurrence test re-run on the 9: five accepted values occur two or more times in the letter,
none is marked at every occurrence (1640: marked on page 2, the page-1 tick dropped; 38: 1 of 10; 31, 28, 36 likewise
partial); null (marked positions kept, values redrawn within digit length, 2,000 draws) mean 0.05, p95 0, max 2;
target 0. H18's reading stands with a larger corroborated set: the marks attach to particular occurrences, the shape
of the printed form's grammar operators, not to values.

**Verdict for the campaign:** done; no reading, no class change. What it adds: a cleaner mark list for any future key
work (9 corroborated, all but one after/above), the page-4 and page-1 faint ticks retired, and one specific open item
-- the caret under the last digit of 65 (rule-3 shape) held on a class conflict, worth one more look when a reader is
on page 1 for any other reason (not filed as a row: one group). Requests: none. Cost: two Sonnet calls (15 crops
each; the second ran 11 minutes and about 210k tokens) plus this runner's merge; the row's estimate (2 USD) is what
`--spend` records, the real figure is nearer 2.5.

## Campaign step H26 (28 Sept 2026, 01:11-01:33 UTC)

Worker: PARENT WORKER ARM-CORR (account 2, Fable, session_01N9jSGgX5d2R8zEroPxtc5E), brief
`.claude/briefs/runs/2026-09-28-parent-arm-corr.md`. H25 was not taken (the owner-account runner had done it at 01:03).
Hypothesis H26: the Pinkney and Erving correspondent pools -- anything catalogued as cipher screened the ARM3-LIVCODE way;
catalogue-only leads cited exactly. Files: `corr/leads.tsv` (every item, one row each), `corr/screen.py` (the screen,
reusing `pool/cor/overlap_test.py` and the target/THE=972 baselines), `corr/screen_output.txt`, `corr/erving1807_groups.tsv`,
`corr/pinkney1808_groups.tsv`, `corr/images/` (25 surfaces, 6.4 MB), `corr/crops_erving1807/`, `corr/requests.log` (every
request, 67 lines), `corr/fetch.sh` (the logged fetch helper).

**Pinkney half.**
- Princeton C0027 (William Pinkney Papers, Series 1B letters received, Armstrong, Box 1 Folder 3): the three 1808 letters
  the sprint checkpoint reported clear (29 Jan, 15 Oct, 30 Nov 1808) fetched from Figgy's public IIIF (manifests in
  `corr/figgy_*_manifest.json`) at 1400 px and read directly by this worker: all twelve surfaces clear prose, no numeral
  group (H). The 29 Jan letter mentions Monroe's arrival in the Chesapeake; 30 Nov mentions Mr Short's Russian mission --
  ordinary friendly correspondence. A fourth item (21 June 1810) has no image link and is outside the window.
- LOC James Madison Papers, `q=pinkney+cipher`, 1807-09: one item, **Pinkney to Madison, London 24 Jan 1808, "Partly in
  cipher"** (mjm022250, 8 surfaces fetched at master resolution). Its only coded run is five groups on p.2,
  `134 1379 1123 1028 454`, glossed above the line in a period hand "Mister Percival"; `tools/data/uscodes-1800/WE028.tsv`
  reads 134=mis 1379=ter 1123=per 1028=ci 454=val -- a known-answer match on all five (grade C). So Pinkney's London
  legation used **WE028** with Madison in January 1808, the same table H25 found Erving using privately with Monroe in
  February 1806. Not the target's code (a known table; the target reads 25% under THE=972 and nothing under WE028 per
  ARM-A2). KEY-OFFICES.tsv gains the usage row.
- NARA M30 (Despatches from U.S. Ministers to Great Britain) is fully digitised (NARA's own "Digitized Microfilm" list,
  Feb 2023): Vol. 15, 24 Apr 1806-29 Dec 1808 = reel 11, **NAID 188514748**, 320 frames, served as one whole-reel PDF
  (`catalog.archives.gov/medialz/dc-metro/rg-059/603720/M30/M30-011/M30-011.pdf`, 289 MB, one request) besides the per-frame
  IIIF v3 route ARM-IMG found. All 324 PDF pages rendered at 400 px and swept by eye on 17 contact sheets (scratch, not
  committed): **no dense numeral-group passage on any frame** -- Pinkney's 1808 despatches and their enclosures (Canning
  notes, Gazette clippings, consular letters) are clear. Sensitivity control (rule 3): the known five-group WE028 run in the
  24 Jan 1808 despatch (frame 65 of this reel, the fair copy sent to the Department) is plainly readable at 1400 px but was
  NOT spotted at sheet scale, so this negative covers passages of roughly twenty groups or more, not short runs; a short
  Armstrong enclosure in cipher would need a frame-by-frame pass at 1400 px (324 frames, about 90 minutes of reads).
- Maryland Center for History and Culture, Pinkney papers MS 1388 (ArchivesSpace at mdhistory.libraryhost.com, tree read
  in full, 58 nodes): 41 family items 1796-1926, no Armstrong item, nothing catalogued as cipher; the only 1808 items are
  two letters to his brother Ninian (28 Apr, 29 Aug 1808). mdhistory.org itself is Cloudflare-blocked; libraryhost is not.

**Erving half** (H25 had already found the Erving-Monroe 5 Feb 1806 letter to be WE028 usage).
- LOC James Madison Papers, `q=erving+cipher`: one item, **Erving to Madison, Madrid 24 March 1807, "Private No 21
  Duplicate", headed "Cypher of the Legation", "Partly in cipher"** (mjm014714, 5 surfaces at master resolution, three
  openings dense with groups, about 400 in all, no interlinear decode). 211 groups read at native from the second opening
  (`corr/erving1807_groups.tsv`, grade S, one reader) and screened (`corr/screen_output.txt`): units 0/1 share on values
  >= 100 **0.27** vs the target 0.59 (target subsampled at n=211: p05 0.54); groups above 1700 **0 of 211** vs the target
  0.092 (p05 0.071); groups under 100 **0.07** vs 0.36 (p05 0.33); top-20 value overlap 5/211, exactly the random-draw
  chance (0.41 of draws reach 3). **MISS, not the target's code on this sample.** It is not WE028 either: 1651, 1661 and 1603
  (its three commonest values) are absent from the 1600-entry table and `926 594 524` would read "ou-lence-een"; the Madrid
  legation's official cypher of 1807 is a third table, values to at least 1694, a repeated stock phrase
  `1603 1583 926 594 524 1340 114 934 975` (three times on one opening) and superscript operator marks on some groups
  (424^ 162^ 335^ 765^ 293^ 163^) -- the same after-group mark grammar the printed form of H14 describes. Recorded in
  leads.tsv for KEY-OFFICES/KEY-DESIGN; not decoded (not this job).
- NARA M31 (Spain) is digitised too: Vol. 10, 24 Aug 1805-19 Apr 1808 = reel 12, NAID 188605361 (628 PDF pages, 158 MB,
  fetched); Vol. 9 = reel 11, NAID 188605226; Vol. 11, 14 May 1808-31 Dec 1810 = reel 13, NAID 188605987. Frames 481-628
  of reel 12 (Erving's March-April 1808 despatches with their Diario de Madrid enclosures) swept at sheet scale: no dense
  numeral passage. Frames 1-480 and reels 11 and 13 not swept in this box (H31 filed).
- LOC Manuscript Division, George William Erving papers (300 items, 3 containers, 1 microfilm reel; chargé at Madrid
  1804-09): the finding aid host findingaids.loc.gov is Cloudflare-challenged to curl and to `tools/browser_fetch.js`;
  Wayback answered 503 (offline) at the same time; loc.gov's own search does not return the collection record. Owner's
  desk: ASKS row 83. The 1890 memoir *Diplomatic services of George William Erving* (archive.org, OCR grepped) has no
  Armstrong and its one "cipher" is a Monroe letter of 1814.
- Founders Online / Rotunda: founders.archives.gov still answers 202 empty, Rotunda 403, Wayback 503 -- the Madison Papers
  calendar for Pinkney/Erving enclosures could not be read from the cloud this pass (the LOC item-title tags above are the
  substitute, and they are what found both coded letters).

**Verdict for the target.** No second letter in the target's code in either pool; both coded items found are known tables
(WE028 by known answer, the Madrid legation cypher by a control-backed screen at n=211). A pool that turns up nothing is a
search result, not a negative (cycle 3's wording); the M30 sheet sweep is a negative for dense passages only. No target
token decoded, no class change, status unchanged.

Requests (all logged in `corr/requests.log`, one at a time, >= 1.6 s apart, browser UA, no 429): figgy.princeton.edu 3,
iiif-cloud.princeton.edu 12, findingaids.library.upenn.edu 1, findingaids.princeton.edu 1 (Cloudflare), www.loc.gov 10,
tile.loc.gov 13, archive.org 3, www.archives.gov 3, catalog.archives.gov 10 (3 headless renders, 4 HEAD, 3 GET incl. two
whole-reel PDFs), mdhistory.libraryhost.com 3, www.mdhistory.org 1 (403), findingaids.loc.gov 2 (Cloudflare),
web.archive.org 2 (000/503), founders.archives.gov 1 (202), masshist.org 1, genealogycenter.net 1 (404). No subagents; all
image reads by this worker. Cost about 16 USD estimated (get_session carries no cost field on this session); the ROOM
line at 01:26 that said "01:56 UTC" was an estimate, corrected at 01:30 (rule 6). Rate-limit status read allowed_warning at
01:2x (BUDGETS.md: no new workers; none were started).

## Second-opinion checkpoint (SO-ARMSTRONG-CHECKPOINT 01:07, 28 Sept 2026)

Landed from PR 61 (`second-opinions/chatgpt-checkpoint-2026-09-28-0107.md`, PR-LAND-23). A runner checkpoint
report, not a leads-prompt answer or a reading; every citation below is a claim to verify, never a fact --
unchecked.

- lead; Adams to Armstrong, 27 Nov 1809 (Morrison, 2nd series, vol. I (A-B), 1893, pp.10-12; MHS OAC120595/120596, Huntington HM22922) is read as enclosing "a copy of a cypher, the corresponding part of which I retain," a temporary cipher distinct from the Department cipher Adams was still awaiting from Armstrong -- unchecked.
- lead; five MHS catalogue records of undated or loosely-dated Adams cipher/key sheets, on microfilm reel 602 (OAC081697, 120623, 120693, 130946) and reel 135 (OAC120739), none identified by the catalogue as the November 27 enclosure or connected to the 1808 target -- unchecked.
- archival-route; Tatum, "Ten Unpublished Letters of John Quincy Adams 1796-1837," Huntington Library Quarterly 4(3) (1941), DOI 10.2307/3815711, cited (refining PR 60's single-page locator) as discussing the 27 Nov 1809 letter across pp.374-376; article text still not acquired -- unchecked.
- next-step; Adams diary entry for 15 June 1813 (editorial transcription, not checked against the manuscript image) describes a cipher letter sent via Delprat toward Paris with a clear duplicate withheld for personal delivery, and Paris reporting the key unavailable; next step named is to locate both witness letters via the diary's surrounding entries -- unchecked.
- archival-route; a raw, pre-editing Rotunda transcription of an 8 Jan 1810 JQA-to-TBA letter (read via web reader after a direct curl 403) describes a sliding lock/key with four alternating letter columns; the checkpoint states no implementation or cryptanalytic exclusion was drawn from it -- unchecked.

No check-solved candidate (no printed decipherment of the Armstrong-Madison letter, its key, or the Livingston key is named; the checkpoint states explicitly that no numeric mapping, shape assignment, crib or plaintext candidate is licensed by these passages).

## Campaign step H27 (28 Sept 2026, 01:45-02:10 UTC)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01NuaRiPghx6VRXA6GuJE8ne, replacing
session_01R2T5qwd7NBMWGnjRtj8ieX at its context line). Hypothesis H27 (the orchestrator's 00:26 row): a power test
of ARM3-LOOP's crib loop on the two-level decade/slot design BEFORE any further crib round -- simulate the design on
en18 text at the target's length, give the solver the slot grammar, and run the loop on three synthetic letters;
30 percent of roots recovered licenses one target run, less does not. Pre-registration (gate, metric, reader
protocol, the known design caveat) written at 01:50 UTC before any letter was built: `h27/PREREGISTRATION.md`.

**Instrument (shared tool, Usage 8: an option, not a private copy).** `tools/families/nomenclator.py` gained
`--param slot_grammar=1`: the book above 100 is one root lemma per decade with its inflected forms at fixed slots --
0 root, 1 plural or past (the commoner of the two in the register; the other form becomes a root of its own), slots
2-9 one suffix class each (ing, er, ly, ion, ment, ness, est, able) in a per-book random order. `inflect`/`deinflect`
are deterministic and round-trip (offline test `tools/tests/test_nomenclator_grammar.py`). The control builder
(`make_control_grammar`) keeps ARM-C1's shape (Jefferson Vol IX held out of the LM, 369 coded tokens, the target's
wildcard runs, a cold 99-value particle block); the solver (`solve_grammar`) anneals over particle words and ONE ROOT
PER OCCUPIED DECADE, all of a decade's forms following the slot map, which it is TOLD (`params["slot_map"]`, the
most favourable case: its unknowns are the 99 particle words and 73-85 roots, against ARM3-LOOP's 181-216 free
values). Root candidates come from the LM's neighbour tables at every occurrence of every value in the decade,
de-inflected through the value's slot, plus the sibling-vocabulary prior. `tools/crib_rounds.py` writes the true
roots into hidden.json (never opened by the reader) and its score verb reports root recovery beside the ARM3-LOOP
columns. The plain path (`slot_grammar` unset) is unchanged: `tools/tests/test_nomenclator.py` and
`tools/tests/test_crib_rounds.py` re-run after the change: both pass (the latter needed a one-line fix unrelated to this step -- it asserted 353 ms tokens, stale since H17 restored the witness to 369; now read from the file).

**Synthetic letters (`h27/loop/seed{2,3,4}/`, state.json control_stats) beside the target.**

| | seed 2 | seed 3 | seed 4 | target (ciphertext.txt) |
|---|---|---|---|---|
| coded tokens / distinct / singletons | 369 / 131 / 76 | 369 / 122 / 58 | 369 / 114 / 52 | 369 / 216 / 139 |
| particle tokens / book tokens | 227 / 142 | 243 / 126 | 239 / 130 | 132 / 237 |
| distinct book values / decades used | 90 / 85 | 78 / 73 | 74 / 73 | 168 / 99 |
| repeated decades / single-token decades | 31 / 54 | 34 / 39 | 33 / 40 | 56 / 43 |
| book forms in the key (180 roots) | 322 | 322 | 320 | 900-1800 est. (ARM-DESIGN Q3) |
| wildcard tokens (OOV runs) | 142 | 141 | 139 | 35 |
| units-digit share slot 0 / slot 1 | 0.90 / 0.05 | 0.87 / 0.10 | 0.86 / 0.08 | 0.388 / 0.20 |

The design as the row states it (180 roots, fixed inflection slots) cannot reproduce the target's shape: a 180-root
book holds about 320 forms, so more than half the letter's content words fall out as wildcards (139-142 vs 35), the
book carries 126-142 tokens instead of 237, and the units digit sits at slot 0 nine times in ten where the target
has it four times in ten -- ARM-DESIGN Q2/Q3's `hdec` finding (top1 0.76, coverage ~0.45) reproduced from the other
side. This is the caveat the pre-registration named: the simulated letters are EASIER than the target on the book
(fewer unknowns, known grammar, more repetition per decade) and harder only on context (more wildcards).

**Results (rule 3: whatever they say; scores.tsv per seed; reader = this session from the view only, at most 12
cribs a round, two rounds).**

| seed | blind: blended (P / B) | roots | round 1: blended (P / B) | roots | round 2: blended (P / B) | roots | best roots | cribs right/new (r1, r2) |
|---|---|---|---|---|---|---|---|---|
| 2 | 29.0 (45.4 / 2.8) | 1/85 = 1.2% | 31.2 (49.8 / 1.4) | 2/85 = 2.4% | 32.5 (49.8 / 4.9) | 4/85 = 4.7% | 4.7% | 6/11, 0/1 |
| 3 | 17.1 (25.5 / 0.8) | 1/73 = 1.4% | 16.8 (25.1 / 0.8) | 1/73 = 1.4% | 8.9 (13.6 / 0.0) | 0/73 = 0.0% | 1.4% | 2/12, 2/5 |
| 4 | 17.1 (24.7 / 3.1) | 4/73 = 5.5% | 10.0 (14.2 / 2.3) | 3/73 = 4.1% | 0.5 (0.8 / 0.0) | 0/73 = 0.0% | 5.5% | 1/11, 0/11 |
| mean | 21.1 (spread 11.9) | 2.7% | 19.3 | 2.6% | 14.0 | 1.6% | **3.9%** | 11 right / 51 new (22%) |

Blended = share of coded tokens read right (percent); P particle class, B book class; roots = decades occurring in the
letter whose solved root equals the true root; top-30 repeated values right blind 6 / 3 / 2 (floor gate 10, failed
on every seed as in ARM3-LOOP). Headroom check passed (blind roots 1-6 percent, nowhere near ceiling).

**GATE VERDICT: NOT MET, by an order of magnitude.** Best root recovery 4.7 / 1.4 / 5.5 percent, mean 3.9 against the
row's 30; the blind solver with the grammar given reads 2.7 percent of roots, and the crib rounds move it by at most
+3.5 points on one seed and DOWN on the other two (the reader's cribs were right 22 percent of the time, below
ARM3-LOOP's 33 -- with the book collapsed to 320 forms the decoded neighbours the reader works from are the solver's
own wrong guesses, and the particle contexts that carried ARM3-LOOP's right cribs are thinner). ARM3-LOOP's crib
gate (10 points blended, above the blind spread of 11.9) is not met either: +3.5 / -8.2 / -16.6. The book class
never exceeds 4.9 percent. TARGET NOT RUN (the row's own condition). A slot-grammar constraint that hands the
solver the inflection map and halves its unknowns does not lift root recovery off the floor at this length: what
limits family C/D here is not the number of free values but the absence of any repeated content context to anchor
them -- 39-54 of the 73-85 decades occur once, and the wildcard runs cut the trigram windows around the rest.

**What this settles for the campaign.** Family D (model-in-the-loop crib rounds) on the two-level design is now
measured twice on matched controls -- ARM3-LOOP without the grammar, H27 with it -- with the gate failed both times
and every number moving the same way; per CLAUDE.md rule 3's "second attempt" paragraph the next attempt needs new
material (more ciphertext in the same code, a sibling letter, a key or an editor's gloss), not a further knob on the
loop. Logged as "untestable by this method at N=369" (not refuted): rule 5, the target stays `open`. Side finding
for the design prior (`design/`, `family_C_spec.md`): a book of decade roots with fixed inflection slots is
excluded as the target's design by its own slot-0 share (0.86-0.90 simulated vs 0.388), so the target's slots are
separate entries with a book-wide popularity order, ARM-DESIGN's own reading, and a solver that treats a decade as
one root has nothing extra to exploit on it -- the grammar the printed form of H14/H19 describes (marks as
operators) is a different mechanism from a units-digit slot grammar and is untouched by this result.

Files: `h27/PREREGISTRATION.md`; `h27/loop/seed{2,3,4}/` (cipher.tsv, hidden.json with `roots`, state.json with
the slot map, round0-2.{json,txt}, cribs1-2.txt, scores.tsv), `h27/loop/seedN.roundR.log`; tool changes in
`tools/families/nomenclator.py` (slot grammar block at the end), `tools/crib_rounds.py` (roots in hidden.json and
the score verb), `tools/tests/test_nomenclator_grammar.py`. Reproduce: `python3 tools/crib_rounds.py --family
nomenclator --spec specs/armstrong-madison-1808.json --target-cipher ciphers/armstrong-madison-1808/ciphertext.txt
--dir ciphers/armstrong-madison-1808/h27/loop/seed2 --seed 2 --restarts 3 --param sweeps=30 --param phase1=20
--param holdout=5 --param slot_grammar=1`, then `--round R --cribs .../cribsR.txt`, then `--score`. No network,
0 requests to any host; no subagent, 0 of 4 vision calls. No reading, no class change, no target token decoded;
rule 10: nothing here is called new or first. Cost: get_session carries no cost figure for this session; the
row's estimate (5 USD) is what `campaign.py --spend` records (about 25 minutes of one Fable session, three parallel
CPU runs of 2-3 minutes per round).

## Campaign step H28 (28 Sept 2026, 02:08-02:18 UTC)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01NuaRiPghx6VRXA6GuJE8ne). Hypothesis H28
(H24's named one-knob re-run): the H24 known-answer control on the best specimen of Tomokiyo's six systems --
Macaulay 1747, Psalm I "written in the long Short-hand, wherein all ye Vowels are included in each Word" -- with
PER-GROUP magnified crops and the book's own worked example on the same blind call; PASS licenses one target read,
FAIL retires the plate-only reader for this family. Pre-registration `h28/PREREGISTRATION.md` (02:11 UTC, before
any reader output); scorer, gate and null unchanged from H24 (`h24/score.py`, `h24/PREREGISTRATION.md`).

**Material.** Leaf 22 (the book's page 13) of archive.org `bim_eighteenth-century_polygraphy-or-short-hand_macaulay-
aulay_1747`, fetched at native 4136x7025 through the BookReaderImages.php `scale=1` form (H24's route; the full leaf
is kept out of git, images/ is at the 30 MB line). The leaf carries the worked example "In the Word Man" (m, a, n
joined, `h28/crops/leaf22_worked_example_man.jpg`) and five ruled lines of the Psalm, engraved, clean, with the
engraver's own captions "a stop" and "verse ends". Reference: KJV Psalm 1 (`h28/ref_psalm1_kjv.txt`, Gutenberg pg10).
Crops: five native line strips and 44 per-group crops at 2x (`h28/crops/`, `manifest.json` with native coordinates),
cut at ink gaps of 10 view px after dropping the printed rule rows (`PIL`/`numpy` installed this session; the
container had neither, so `tools/iiif_lines.py` could not run until then). Plate: the comparative alphabet on the
book's own page 3 (`images/shorthand/specimens/macaulay1747_alphabet_p3.jpg`, ARM-S1).

**Reader.** One Sonnet subagent, given the plate, the worked example, the five strips and the 44 crops in reading
order, told nothing of the book, author, system or text, web tools forbidden, letters per crop with `?` and `#`
for unreadable and non-letter strokes (`h28/reader_macaulay_control.tsv`, 48 rows after its own a/b splits).
Its own report: confidence low-to-medium throughout; the plain tall vertical (read as `l`) and the symmetric `V`
(read as `nw`) recur and have no clean plate match; only the "an" join learned from the worked example reached medium
confidence.

**Result (rule 3, the control's number whatever it says).**

| specimen | reader rows | `?` / `#` rows | S1 | null p95 | p | S2 | null p95 | verdict |
|---|---|---|---|---|---|---|---|---|
| Macaulay 1747 Psalm I, lines 1-5, per-group 2x crops + worked example | 48 | 1 / 15 | 0.057 | 0.075 | 0.745 | 0 | 3 | **CONTROL FAIL** |
| (H24, for comparison) Mavor 1792 Job xxix, line strips | 63 | 34 | 0.108 | 0.135 | 0.315 | 1 | 1 | CONTROL FAIL |
| (H24) Byrom 1796 Lord's Prayer, line strips | 22 | most | 0.250 | 0.375 | 0.740 | 0 | 1 | CONTROL FAIL |

The reader's letters against the Psalm's opening ("Blessed is the man that walketh not in the counsel") read `z an
l nw l mp w an lanpl`: chance-level alignment (S1 at the 25th percentile of its own consonant-bijection null) and not
one exact word skeleton, on the cleanest known-answer material the six systems offer (engraved, vowels written,
the system's own worked example on the same page, per-group zoom). The knob H24 named (per-group crops, worked
example) did not move the instrument at all -- S1 is lower than on Mavor's line strips.

**Verdict for the campaign: the plate-only reader is RETIRED for the shorthand family, "untested-by-this-tool"
(CLAUDE.md rule 3, second-attempt paragraph: two attempts, three specimens, the one named knob changed, the gate
failed every time with the numbers not moving toward it).** Target not read (no licence). Nothing here is a
negative on Macaulay, Mavor or Byrom as the target's system, and nothing is a negative on the target's marks
being shorthand: it says a model reader given a period plate cannot read even the plate's own author's specimen,
so no "does not read as system X" result from this instrument class -- including ARM-S2/S3's symbol-match scores
-- can be cited as an exclusion. The shorthand question now needs a different instrument: a person who reads one
of these systems (an ASKS row when a name exists), a trained recogniser (the repository has none), or an
independent crib that fixes what one passage says. HYPOTHESES.md family S gains the retirement line.

Files: `h28/PREREGISTRATION.md`, `h28/ref_psalm1_kjv.txt`, `h28/crops/` (2.5 MB: 5 strips, 44 crops, the worked
example, manifest.json), `h28/reader_macaulay_control.tsv`, `h28/score_output.txt`. Requests: archive.org 3
(metadata JSON, djvu.txt -- answered 302, not followed -- and one leaf image), gutenberg.org 1, all with the
descriptive User-Agent, >= 1.5 s apart, no 429/403; PyPI 2 (pillow, numpy). Vision: 1 of 4 subagent calls (Sonnet,
about 146k tokens, 5 minutes) plus this runner's two looks (the leaf view, one overlay). No reading, no class
change, no target token decoded; rule 10: nothing here is called new or first. Cost: get_session carries no cost
figure for this session; the row's estimate (3 USD) is what `campaign.py --spend` records.

## Campaign step H29 (28 Sept 2026, 02:19-02:42 UTC)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01NuaRiPghx6VRXA6GuJE8ne). Hypothesis H29 (from
H25): Erving to Monroe, Madrid 5 Feb 1806 (LOC Monroe Papers, Series 1 reel 3, frames 0741-0743), the one coded letter in
the Monroe run with a full period interlinear decode, read blind at native resolution as a REAL WE028 usage control --
a real-usage row beside the four THE=972 letters in `design/stats_real.tsv` (ARM-DESIGN had only simulated WE028
letters), and a witness for `KEY-OFFICES.tsv`. Not a target key (ARM-A2, H25) -- that is re-checked below, not assumed.

**Route and crops.** Frames 0741, 0742, 0743 fetched at native (4327x2656, 4306x2750, 4216x2716; tile.loc.gov IIIF
`full/full`, 3 requests, kept out of git, `h29/MANIFEST.tsv`). Code sits on 0741's right page, both pages of 0742 and
0743's left page (right page clear). `tools/iiif_lines.py --image` found only 20-23 of about 27 lines per page on 0742
at every prominence tried -- the interlinear glosses fill the interlines and flatten the row ink profile -- so the
crops were cut by `h29/band_cut.py`: fixed-pitch two-line windows (pitch 88-92.5 px, from the detected centres where
regular) with two red guide lines around the target line, every line the target of exactly one crop, the reader told
to read only between the guides (a variant worth adding to iiif_lines.py as an option if a third target needs it;
noted, not done). Two bands straddled one line twice (0742L 26/27, 0743L 13/14); both readers flagged the duplicate
and `check_we028.py` drops a crop whose group sequence repeats the previous crop's.

**Readers.** Four blind Sonnet calls, one page each (0741R, 0742L, 0742R, 0743L; 27 crops per call), told nothing of
the letter, the key or the earlier H25 reads; output group + gloss per crop (`h29/reads/f*.tsv`), merged in reading
order by `h29/check_we028.py` -> `h29/erving_groups.tsv`, checked against `tools/data/uscodes-1800/WE028.tsv`
(gloss folded; exact = equal, partial = prefix/suffix of 3+ letters, shifted = matches the neighbouring group's entry,
the interline word sitting between two groups in dense lines).

**Result: 251 groups (19 / 62 / 104 / 66 per page), 250 with clean digits, 166 distinct values, 206 glossed.**

| check | number |
|---|---|
| glossed groups whose gloss matches WE028 at the value read | 114 exact + 11 partial + 8 shifted = 133 of 206 (0.646) |
| misses | 73 (35 at the reader's own low confidence, 44 medium, 2 high; mostly gloss misreads of tiny interline script -- "rich" for ide, "di" for ling -- and a few value misreads: 837 for 637 = ment, 1357 for 1351 = bow) |
| CONTROL A, gloss-shuffle null (1,000 permutations of the 206 glosses over the same groups, exact+partial) | real 125 vs null mean 3.3, p95 6, max 10 -- the pairing is 21x its p95 (`h29/controls.txt`) |
| two-reader agreement on frame 0741 (H25's one reader at 1800 px vs this blind reader at native) | 16 of 19 digit groups identical; the 3 disagreements arbitrated by WE028: 637 = ment (native right, H25's 837 wrong), 1369 = tation and 1094 = she (native right), 835 = die (native "dic" nearer than H25's "de"); "will" at 1786 (H25) / 1106 (native) matches neither entry, open |
| CONTROL B, value overlap with the target: 166 Erving distinct vs the target's 216 | 15 shared vs a random-draw null (166 values from 1-1600, 2,000 draws) mean 19.1, p05 13, p95 25 -- at chance |
| the 12 commonest Erving values (WE028 the, to, of, in, he, ter, ment, character, mis, french, govern, our; 25.2% of Erving's groups) in the target's 369 | expected about 93 if the target were WE028 usage, observed 0 |

So the letter IS WE028 usage, established from the manuscript rather than inferred from H25's 49 values (65% of the
glossed groups agree with the published table at the value read, 21x the shuffle null; the residue is gloss
legibility, not the table), and the target is NOT WE028 usage (H25/ARM-A2 reproduced on the full 251-group stream:
none of the twelve commonest values appears once in 369 groups where 93 would be expected). Per-token grades: the
group digits H where both readers agree or WE028 arbitrates (about 240), M elsewhere; the glosses are C where they
match the table (133) and M otherwise; nothing here is a reading of the target.

**Design row (`design/stats_real.tsv`, `REAL WE028 usage erving-monroe_1806-02-05`, via `h29/append_stats_real.py`;
`design_stats.py` now reads `design/real_extra.tsv` so a full re-run keeps it).** N 250, D 166 (D/N 0.664), values
under 100 share 0.048, units_top1 0.164, units_top2 0.298, units_H 3.225, decade_units_z 9.1, block_trough 0.000,
block_pair_min 14, digits23_share 0.142 -- the first REAL WE028 stream lands where ARM-DESIGN's simulated WE028
letters sit (units_top1 0.14-0.17, entropy 3.2-3.3) and where the four real THE=972 letters sit (0.15-0.20), and
nowhere near the target (0.388 / 2.572 / trough 4): a fifth independent real letter confirming that the target's
units skew and 901-1099 trough are not what a contiguous State Department table produces in use.

**KEY-OFFICES.tsv.** The WE028 row (added by ARM-CORR at H26) already names this letter; its cell now carries the
count and the match figure from this step. KEY-DESIGN.tsv is tool-built (`tools/key_design.py`) and not edited here.

No target token decoded, no class change, no reading; rule 10: nothing here is called new or first (the letter is
listed in the 1904 LOC calendar and the glosses are the period's own; WE028 is Weber's published table). Requests:
tile.loc.gov 3 (native frames), >= 1.7 s apart, descriptive User-Agent, no 429/403; no other host. Vision: 4 of 4
subagent calls (Sonnet; about 136k, 153k, 191k and 201k tokens; 6-18 minutes each) plus this runner's five looks
(three page views, one band overlay, two crop checks). Cost: get_session carries no cost figure; four Sonnet calls
of that size are about 5 USD by H21's rate (two calls of ~210k tokens ~ 2.5 USD), so `--spend` records 5 against the
row's 1.5 estimate -- the estimate priced one pass per frame (H25's wording) but the letter has four coded pages and
needs one call each (CLAUDE.md Usage 6: price per pass, not per frame).

Files: `h29/MANIFEST.tsv`, `h29/band_cut.py`, `h29/check_we028.py`, `h29/append_stats_real.py`, `h29/reads/`
(4 TSV), `h29/erving_groups.tsv`, `h29/summary.txt`, `h29/controls.txt`; `design/real_extra.tsv`,
`design/stats_real.tsv` (one row added), `design/design_stats.py` (real_extra hook).

## Campaign step H31 (28 Sept 2026, 02:42-02:55 UTC)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01NuaRiPghx6VRXA6GuJE8ne). Hypothesis H31 (from
H26): finish the NARA whole-reel sweeps at a scale that can catch a short coded enclosure -- M30 reel 11 (Pinkney,
Apr 1806-Dec 1808) frame by frame, M31 reel 12 frames 1-480 (Erving, Aug 1805-Apr 1808), M31 reels 11 and 13; the
control is the 5-group WE028 run on M30 reel 11 frame 65 (Pinkney to Madison 24 Jan 1808, H26 known answer), which
must be flagged blind at the sweep scale before any negative is logged.

**Route (new for this target: the whole-reel PDF, not per-frame IIIF).** `catalog.archives.gov/medialz/.../M30-011.pdf`
etc. answer plain curl with the browser User-Agent at about 20 MB/s (four reels, 609 MB, 13 seconds; `h31/MANIFEST.tsv`),
and `pymupdf` (installed this session) rasterises a page in about 0.15 s -- 1,749 frames on disk in under a minute, no
per-frame request, no rate question. PDF page index i is microfilm frame i+1 (page 64 is pixel-identical to IIIF frame
0065, `h31/control_compare.jpg` in scratch). Sweep scale: `h31/sheets.py` puts two frames side by side at 700 px each
(sheet 1408 px wide, under the vision long edge of about 1568 px, so nothing is silently downscaled -- a 2x2 sheet at
2266 px tall would have been shrunk to about 480 px per frame, H26's failing scale). Four blind Sonnet calls of 50-54
sheets each: M30 reel 11 frames 1-108, 109-216, 217-324; M31 reel 12 frames 381-480 (the 1807 span nearest H26's
400-px sweep of 481-628). M31 reel 12 frames 1-380 and reels 11 and 13 were NOT swept (four-call limit); their PDFs
refetch in seconds.

**CONTROL PASS.** The screener of frames 1-108, told nothing of frame 65, flagged it alone: "run 184.1779. 1023.1038.654
mid-sentence in otherwise clear prose" -- the digits misread at 700 px (the run is 134 1379 1123 1028 454) but the
frame flagged, which is what a sweep needs. So a "none" from this instrument at this scale is a test for a run of
five groups in clear prose; it says nothing about a run of one or two.

**M30 reel 11, 324 frames: no coded frame beyond the control.** 317 none, 6 blank/target cards, 1 code (frame 65).
The screeners' notes name the ordinary numerals they set aside (enclosure numbers, tariff tables at 231-232 and 319,
crew lists, "150,000 persons"). Pinkney's 1808 despatches to Madison carry no second coded item and no enclosure
from Armstrong in cipher (`h31/reads/m30r11_*.tsv`).

**M31 reel 12 frames 381-480: ten frames of dense code, one low-confidence flag.** Frames 389, 390, 403, 404, 408,
409, 426, 427, 428, 429 flagged as dense numeral runs with interlinear words; 397 flagged low ("1607.1794 n.62 / 1603
n.91" in a corner, an archival reference by the screener's own reading, not looked at further). One look at frame 403
at 1500 px (this runner): a fully coded despatch on a faint microfilm, every group glossed interlinearly by a period
hand -- "no doubt in the minds of those best acquainted with the intrigues of the court ... the object of the Prince of
Peace ... the Prince of Asturias is under the special protection of the Emperor ... Buonaparte ... insurrection" -- the
Escorial affair of October-November 1807, Erving to Madison. Its values (1651 and 133 the commonest, then 1657, 244,
1578, 1104, 628, 65 ...) are the values of the "Cypher of the Legation" letter of 24 Mar 1807 that H26 read at n=211
(1651 x17 and 133 x7 are that letter's two commonest values too; 5 of the 18 values noted on frame 403 occur there),
so this is the same Madrid legation table, now with about ten frames of usage and a full period decode -- and NOT the
target's code: H26 screened that table MISS at n=211, and the target's 369 groups contain no 1651 and no 133 at all
(2 of the 18 frame-403 values appear in the target, once each, at chance). No transcription was made (no vision call
left, and a screen of this table against the target is already on file); the frames are a pool for the record.

**Verdict for the campaign.** Done, control-backed for M30 reel 11 (no coded enclosure at the five-group scale, control
flagged blind) and for M31 reel 12 frames 381-480 (coded frames found, identified as the Madrid legation cipher already
screened out). What it adds: the PDF route and `h31/sheets.py` make the remaining 1,177 unswept frames (M31 reel 12
1-380, reels 11 and 13) a one-call-per-100-frames job; and the Erving-Madison legation cipher now has a pool of about
ten frames with a period decode (frames 389-390, 403-404, 408-409, 426-429; probably three or four despatches of
1807), a key-recovery candidate in its own right for the scout (a US diplomatic private cipher of 1807 with its
plaintext beside it), filed as H32 for a transcription-plus-screen at n of several hundred, not for the target. No
reading, no class change; rule 10: the letters are catalogued NARA despatches and the decode is the period's own.

Requests: catalog.archives.gov 5 (four PDFs, one IIIF frame), browser User-Agent per the playbook, 1.6 s apart, no
429/403; no other host (`corr/requests.log`). Vision: 4 of 4 subagent calls (Sonnet, 163-177k tokens, 2.5-5 minutes
each) plus this runner's three looks (the control comparison, frame 403, one sheet check). Cost: get_session carries
no cost figure; four Sonnet calls of that size are about 5 USD by H21's rate plus this runner's reads -- `--spend`
records the row's 6. Files: `h31/MANIFEST.tsv`, `h31/sheets.py`, `h31/reads/` (4 TSV, one row per frame); PDFs,
sheets and native renders in scratch only (609 MB), refetch per the manifest.

## Second-opinion checkpoint (SO-ARMSTRONG-CHECKPOINT 01:50, 28 Sept 2026)

Landed from PR 62 (`second-opinions/chatgpt-checkpoint-2026-09-28-0150.md`, PR-LAND-24). A runner checkpoint
report, not a leads-prompt answer or a reading; every citation below is a claim to verify, never a fact --
unchecked.

- lead; Adams diary, manuscript p457, 14 Feb 1813 (primarysourcecoop.org, editorial text and page image both read) is read as saying Adams gave Delprat two copies of a letter to the US chargé d'affaires at Paris, one enciphered to forward if detained, one plain to deliver personally -- unchecked.
- lead; Adams diary, manuscript p490, 15 June 1813 (primarysourcecoop.org) is read as saying Delprat, detained at Vienna, forwarded the cipher copy by post, and Adams's 14 June answer reported no key at Paris; does not name the predecessor or the table -- unchecked.
- archival-route; MHS OAC131078, Adams to the chargé d'affaires at Paris, St Petersburg, 12 Feb 1813, letterbook copy reel138, catalogued with "[David B. Warden]" in brackets, named as the candidate locator for the Delprat dispatch; neither the letterbook pages nor a received cipher/plain pair were obtained -- unchecked.
- lead; Ford, *Writings of John Quincy Adams* vol4, Adams to John Speyer, 20 Apr 1813, pp474-475 (archive.org, printed pages visually read) is read as saying the legation's seal, cipher and archives properly remain with Barlow, questioning both Barlow's and Warden's authority to act as chargé -- unchecked.
- lead; same volume, Adams to Secretary of State, 16 Feb 1813 no106, pp441-444 (archive.org, printed pages visually read) is read as explaining Romanzoff's request to locate Russian embassy archives deposited with Joel Barlow, and Adams's own wish to learn who handled US affairs after Barlow's death -- unchecked.
- archival-route; MHS OAC131142, Warden to Adams, Paris, 4 March 1813, reel415, the sole hit of an author-scoped catalogue query for Warden 1 March-14 June 1813; text not obtained, not asserted to be the cipher-key reply -- unchecked.
- next-step; the checkpoint's own next bounded action is to identify and read the incoming Paris answer Adams received 14 June 1813, searching both T. Barlow and Warden via MHS catalogue and printed sources, checked against the OAC131078/reel138 outgoing letter -- unchecked.

No check-solved candidate (no printed decipherment of the Armstrong-Madison letter, its key, or the Livingston key is named).

## Second-opinion checkpoint (SO-ARMSTRONG-CHECKPOINT 01:57, 28 Sept 2026)

Landed from PR 63 (`second-opinions/chatgpt-checkpoint-2026-09-28-0157.md`, PR-LAND-24). A runner checkpoint
report, not a leads-prompt answer or a reading; every citation below is a claim to verify, never a fact --
unchecked.

- archival-route; MHS OAC131321, Thomas Barlow to JQA, Paris American Legation, 20 April 1813, reel415, named as the specific incoming candidate for the 14 June answer Adams reported receiving; text and receipt docket not read -- unchecked.
- archival-route; MHS OAC131335, JQA to Thomas Barlow, St Petersburg, 22 April 1813, letterbook copy reel138, named as an outgoing witness candidate; the checkpoint states the two April 20/22 letters are not established as a letter-and-reply pair -- unchecked.
- archival-route; MHS OAC131200 (Delprat to JQA, Brodie, 23 March 1813) and OAC131252 (Delprat to JQA, Vienna, 7 April 1813), reel415, named as potential transit/forwarding evidence; contents unverified -- unchecked.
- archival-route; MHS OAC131327, JQA to David B. Warden, St Petersburg, 21 April 1813, letterbook copy reel138, named as parallel outgoing correspondence; contents unverified -- unchecked.
- lead; a date-bounded MHS catalogue query (1 March-14 June 1813, num=1000) reported 480 of 480 results, and a Thomas Barlow author/recipient query for all of 1813 reported exactly 2 results (OAC131321, 131335) -- catalogue scope only, not asserted to be exhaustive of surviving letters -- unchecked.
- lead; the 1913 AAS pamphlet *Correspondence of John Quincy Adams, 1811-1814* (archive.org `correspondenceof01adam`), full OCR searched case-insensitively for Barlow, Delprat, cypher, cipher, returned zero hits; stated as one OCR witness, not proof of absence from all editions -- unchecked.
- next-step; the checkpoint's own next bounded action is to retrieve the contents or receipt docket of MHS OAC131321 (Thomas Barlow to JQA, 20 April 1813, reel415) via a public image or printed witness, checking whether it names the February dispatch and lack of key and whether its receipt is dated 14 June, else checking OAC131252 or OAC131335 -- unchecked.

No check-solved candidate (no printed decipherment of the Armstrong-Madison letter, its key, or the Livingston key is named).

## Campaign step H34 (28 Sept 2026, 03:12-03:4x UTC) -- Armstrong's own papers and the Livingston papers, catalogue-first (ARM-OWN, account 3)

Search result, not a negative. Line B's step B3 (02:52 UTC, `line-b/NOTES.md`) is the prior pass and is not repeated here
(Skeen's Rokeby citations, NYPL MssCol 6743, the NYHS Livingston papers' missing public aid, MdHS Warden). What this step
adds, per collection:

**1. Library of Congress, John Armstrong papers, 1784-1834 (`mm78000058`, Miscellaneous Manuscripts, digitised, 15 images
under `mssmmc.00129567533`).** All 15 pages fetched at pct:25 (`h34/loc_armstrong/`) and read by this worker: (1) Wyoming,
24 Aug 1784, to John Dickinson (militia, the Pennsylvania claimants), pp.1-2; (2) War Department, 17 Aug 1814, to Gen. E. P.
Gaines, pp.3-4; (3) pay warrant for William H. Paulding, 24th Infantry, 7 June 1814, signed as Secretary of War, pp.5-6;
(4) Red Hook, 1 Dec 1824, to Ambrose Spencer, Albany (New York politics, the U.S. election), pp.7-11 with address leaf;
(5) Red Hook, 30 March 1834, to Major Henry Lee at Mouy (Oise), postmarked 28 Mars 1834, pp.12-15. **Nothing from 1804-1810;
no cipher.** The House history page's "1814-1834, 5 items" matches (the 1784 letter is the sixth).

**2. Where the rest of Armstrong's papers are (House of Representatives History, Art & Archives, "Research Collections",
read through the WebFetch route; the bioguideretro page itself 403s).** New-York Historical Society: **200 letters
(1777-1843); microfilm of privately owned letters (1798-1833); a letterbook (1804); an unpublished biography; photostats of
about 1,000 items in other collections.** Massachusetts Historical Society: about 90 items, 1778-1827. Pierpont Morgan
Library: 17 items, 1785-1841. Historical Society of Pennsylvania: several collections (the letters to Callender Irvine
1803-1843 are mostly 1813-14 War Department, per the HSP guide snippet). New York State Library: 15 items 1811-1836.
Franklin D. Roosevelt Library: the Aldrich family papers (below). Library of Congress: the 5 items above plus the Henry
Mason Morfit papers. Indiana Historical Society's "John Armstrong papers 1772-1950" are a different man (1755-1816, the
frontiersman) -- dropped. **The 1804 letterbook is the only retained-copy series named anywhere, and it is dated 1804; no
source names a letterbook or retained drafts for 1807-1808.** Whether the NYHS "microfilm of privately owned letters
1798-1833" is the Rokeby roll (item 3) is inferred (I), not read.

**3. Rokeby: FDR Library, Hudson River Valley and Dutchess County manuscript collection, Appendix I (PDF pp.17-18, read
with pymupdf; line B could not parse it).** "Aldrich Family Papers, 1770-1895 (one roll). The collection consists of circa
200 items, most of which deal with the career of John Armstrong (1758-1843) ... Correspondents include George Washington,
Thomas Jefferson, Alexander Hamilton, James Madison, James Monroe, Lafayette, Kosciuszko, Talleyrand, Robert R. Livingston
... Over half of the material deals with Armstrong's French ministry ... The papers are unarranged. Access to the papers
is restricted; the permission of one of the collection's owners is required prior to its use. Citations ... 'From the
Rokeby Collection, Barrytown, Dutchess County, New York, courtesy of Richard Aldrich and others.' The Library microfilmed
the papers in 1966 for the National Historical Publications Commission; it received a positive copy of the microfilm from
the Commission in 1972." This verifies the ChatGPT 22:44 checkpoint's sentence that B3 left unverified. Not digitised; a
person's step (ASKS row 85).

**4. Founders Online, read directly (the CloudFront 202 challenge passes for headless Chromium once the container's proxy
CA is in Chromium's NSS store -- `certutil -N -d sql:$HOME/.pki/nssdb -f <empty-password file>` then `-A`; the
`--empty-password` form hangs on a password prompt in this container).** (a) Source note of 99-01-02-2728 (20 Feb 1808)
and of 99-01-02-2703 (15 Feb): "DNA: RG 59--DD--Diplomatic Despatches, France", nothing else -- the early-access documents
carry no letterbook, draft, duplicate or decipherment note. (b) The live 20 Feb text has 369 numeral groups and 29 "symbol"
markers and agrees with `ciphertext.txt` group for group (difflib on the integer sequence: no substitution; the three extra
integers are the date and the record group). (c) Calendar, Author = "Armstrong, John, Jr." (the early-access facet; plain
"Armstrong, John" returns nothing for 1808), 1 Jan-30 Jun 1808: 28 documents (26 to Madison, 2 to Jefferson), listed in
`h34/founders_list_1808b.html`; the only coded ones are 20 Feb (the target) and **5 March 1808 with a 9 March postscript
(`h34/founders_1808-03-05_groups.tsv`, 354 groups; `_03-09_`, 58) -- not in the repo before this step** (the known 15 March
duplicate is roll 14 f.0045). Screened with `corr/screen.py` (the H26/ARM3-LIVCODE statistics, target and THE=972 usage
beside it): 5 March units-digit 0/1 share on values >= 100 **0.19** vs target 0.59 (target-at-n p05 0.575), above 1700
0.003 vs 0.092, under 100 0.02 vs 0.36, top-20 overlap 0/354; its top values are 972 x15, 1165 x12, 1116 x11, 962 x9 --
the office code's own. **MISS: a THE=972 despatch, not a second letter in the target's code** (grade S screen, n=354).
It is a fifth Armstrong THE=972 letter for Bourdeau's table, not for this target; noted in `corr/leads.tsv`.

**5. Livingston side.** The NYHS Robert R. Livingston papers have a printed reel guide: **Jack T. Ericson and Donald L.
Haggerty (eds), *The Robert R. Livingston Papers, 1658-1888: A Guide to the Microfilm Edition* (Sanford, N.C.: Microfilming
Corporation of America, 1980), 53 pp., OCLC 7776177, LCCN 81137544** (Open Library work OL6123259W; Google Books
NO_PAGES; HathiTrust bib API: no volume). Not online anywhere reached; it is the document a person needs to find the
Armstrong-to-Livingston letters of 1806-1809 by reel (ASKS row 86). Reel count unresolved from the cloud: the ArchiveGrid
record snippet says 18 reels 1658-1888, line B recorded 57 (NJHS MG 1194 page); the guide settles it. Museum of the City of
New York, Livingston family papers 1719-1929 (aid PDF, 11 pp., read): no Armstrong, one Robert R. Livingston folder dated
Aug 1807 -- not a pool. Columbia (Livingston family papers 1787-1915, James Duane Livingston, estate) and Yale (Livingston
Family Papers, MS 808 -- host 202/403) not read. LOC `q="Livingston, Robert R."` manuscripts: only the Madison Papers items
already screened by ARM-LIV/ARM3-LIVCODE; no LOC-held Livingston collection surfaces by that search (the NYHS microfilm copy
in the Manuscript Reading Room is not item-catalogued on loc.gov).

**6. Not reachable from the cloud (one attempt each, no retry loops; WebFetch tried where noted):** archives.nypl.org
(403 curl and WebFetch), researchworks.oclc.org ArchiveGrid (403 both), hsp.org and discover.hsp.org (403 both),
corsair.themorgan.org (403), archives.yale.edu (202 curl, 403 WebFetch), masshist.org collection-guide search (500 both;
the browse list answers 200 and has no Armstrong-titled guide, so the ~90 items sit inside other collections),
bioguideretro.congress.gov (403), bobcat.library.nyu.edu REST guess (404), web.archive.org (000), catalog.loc.gov (JS shell),
lccn.loc.gov marcxml (404). These catalogue reads go to the owner's desk as LOCAL-QUEUE L27.

**Result.** No retained copy of the 20 Feb 1808 letter and no letterbook or drafts for 1807-1808 are catalogued online
anywhere reached; the two places a retained copy could still sit are the NYHS Armstrong papers (200 letters plus the
microfilm of privately owned letters 1798-1833) and the Rokeby/Aldrich roll (over half French-ministry), both needing a
person (ASKS 84, 85); the Livingston side needs the 1980 reel guide (ASKS 86). One digitised coded page found and screened
(5 March 1808): MISS. Candidate plaintext: none.

Requests (container, all >= 1.6 s apart, browser User-Agent, logged in `corr/requests.log` lines 73-122): tile.loc.gov 15,
founders.archives.gov 9 (headless Chromium), www.loc.gov 4, openlibrary.org 3, masshist.org 2, bobcat.library.nyu.edu 2,
archive.org 2, and one each to www2.hsp.org, discover.hsp.org, www.nypl.org, www.googleapis.com, www.fdrlibrary.org,
web.archive.org, mcnycatablog.org, lccn.loc.gov, corsair.themorgan.org, catalog.loc.gov, catalog.hathitrust.org,
bioguideretro.congress.gov, archives.yale.edu: 50 in all. Plus 7 WebFetch tool calls (a separate egress; 5 of them 403) and
12 WebSearch calls. No logins, no credentials printed (the Google Books key is redacted in the log), no subagents. Cost:
own estimate about 8 USD; `get_session` carries no cost field for this session.

## Campaign step H32 (28 Sept 2026, 02:55-05:05 UTC, interrupted 02:58-04:27 by the account session limit)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01NuaRiPghx6VRXA6GuJE8ne). Hypothesis H32 (from
H31): the Erving-Madison Madrid "Cypher of the Legation" pool, part 1 -- blind reads of the densest coded frames of
NARA M31 reel 12 with their period interlinear decode, merged into a glossed group stream, screened against the
target with `corr/screen.py`, and handed to the scout as a key-recovery candidate (not a target key: H26 MISS at n=211).

**What happened to the box.** Four blind Sonnet reads (frames 403, 404 both pages, 408, 409) were launched at 02:57 UTC
and all four died at about 02:58 on the account's session limit (HTTP 429 rate_limit, reset 03:40 UTC), with nothing
written. Relaunched at 04:27 with two of the four (403 right page, 408 right page) because spent_today then read
116.13 of 120 after the parent's reconciliations; frames 404 and 409 moved to H33 (their band crops are cut, refetch
route in `h32/MANIFEST.tsv`). The two reads ran 15 and 35 minutes (201k and 325k tokens: the 408 page is dense and
its numerals sit below the gloss line, so the reader cross-checked neighbouring crops throughout).

**Material and crops.** Embedded microfilm images from the whole-reel PDF (1700x1556 and 1964x1780 for a two-page
spread, so about 850-980 px per page -- the scan's own limit), coded pages cut by `h29/band_cut.py --scale 2.5` into
fixed-pitch two-line windows with red guides (`tools/iiif_lines.py` centres are irregular under the glosses at this
resolution); `h32/MANIFEST.tsv`.

**Result: 245 groups (403R 103, 408R 142), 238 with clean digits, 172 distinct values, 154 glossed** (`h32/reads/`,
`h32/legation_groups.tsv`, `h32/legation_screen_input.tsv`, `h32/summary.txt`, `h32/screen_output.txt`). Both readers
report low-to-medium confidence on most digits (faint pencil numerals on an upscaled microfilm) -- grade M for the
digits, C for glosses that recur consistently (1657 = "the" and 133 = "of" on six or more lines each, the 408 reader's
own cross-check), M otherwise.

| check | number |
|---|---|
| same-table check vs H26's 24 Mar 1807 letter of this cipher (n=211, 128 distinct) | 36 distinct values shared vs a random-draw null mean 12.9, p95 18 -- the same table; the commonest value reads 1651 in H26's native-crop eye transcription and 1657 here (both glossed "the"), a digit-level disagreement between readers at two resolutions, unresolved (M) |
| target overlap (172 legation distinct vs the target's 216) | 18 shared vs random null mean 19.2 (p05 13, p95 26) -- chance |
| the 12 commonest legation values (1657, 133, 244, 624, 424, 1578, 628, 165, 33, 400, 926, 1147; 26% of the stream) in the target's 369 groups | expected about 99 at the legation rate, observed 0 |
| `corr/screen.py` (ARM3-LIVCODE/H26 statistics) | units 0/1 share on values >= 100: 0.19 vs the target's 0.55-0.63 at n; above 1700: 0.000 vs 0.08-0.11; under 100: 0.13 vs 0.33-0.39; top-20 overlap 5/238 (chance 0.475 for >= 3); **VERDICT: MISS** |

So the Madrid legation cipher is not the target's code, now at n=238 on two more letters (H26's MISS at n=211 stands
and is reinforced: the target does not contain the cipher's "the" or "of" once), and the pool is on file for the
record: with H26's letter, about 450 groups of a 1807 US legation private cipher with the period's own decode beside
them, plus frames 389-390, 404, 409, 426-429 still unread (H33). For the scout: a key-recovery candidate in its own
right (values 1-1698 seen, syllable and word entries mixed, the/of at 1657(1651)/133), not for this target.
`KEY-OFFICES.tsv` gets no row from this step: that register lists key files, and no table has been rebuilt here (a
rebuilt table from the glosses is the recovery job the scout would file, not a campaign step on this target).

No reading of the target, no class change; rule 10: the despatches are catalogued NARA items and the decode is the
period's own. Requests: none this step (all images from the PDFs fetched in H31). Vision: 2 of 4 subagent calls
completed (two more died on the rate limit before reading anything); this runner's one look (the four-frame view).
Cost: get_session carries no cost figure; two Sonnet calls of 201k and 325k tokens are about 4-5 USD by H21's rate --
`--spend` records 5, which takes spent_today past the 120 daily budget (116.13 before this step), so the runner stops
after this step per the campaign brief.

**Correction (05:05 UTC):** the budget line above was written against a 120 USD daily budget; the orchestrator raised it to 240 during this step (CAMPAIGN.md header, spent 144.38/240 after this step), so the runner continues rather than stopping.

## Campaign step H15 (28 Sept 2026, 05:05-05:16 UTC)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01NuaRiPghx6VRXA6GuJE8ne). Hypothesis H15 (from
H3): reconcile the two mark transcriptions -- `ciphertext_ms.txt` ('*' per mark, 35 runs, 218 marks, ARM-TR/TR2 with
the H5/H17 corrections) and `codex-2026-09-27b/glyphs.tsv` (Tomokiyo-labelled shape tokens, 25 passages with '|'
sub-runs, 257 tokens) -- into one graded mark sequence, then re-run `adj/pairs_test.py` test B and the H2 glyph-null
shuffle on it, since the H2 and H3 caveats rest on the one-reader transcriptions. Line B's B28 (account 3, 04:47 UTC)
had just shown that the codex inventory is Tomokiyo's own labelling re-tokenised and that ARM-S1's independent inventory
differs on one point (Tomokiyo's three wave types 20/22/23 are one compound filler class there); this step does not
redo B28, it takes that finding as the one defined alternative segmentation.

**Alignment (`h15/align.py` -> `h15/runs.tsv`).** Each codex passage keyed to the ms runs it spans by its numeric
context (spans fixed by hand after the automatic walk stopped one run short at every line break); 34 of the 35 ms
runs matched (the lone '*' before "5" on page 4 has no codex passage; the p1d "passage" is the tick after 38, a mark on
a numeral, not a run). Over the matched runs the ms counts 217 marks and the codex 257 tokens; 11 of 25 passages agree
exactly (all short runs: 1-9 marks), the 40 extra codex tokens sit in the six longest runs (p1e 22 vs 32, p3d 12 vs
20, p2a 20 vs 25, p1f 35 vs 39, p2b 5 vs 8, p3c 6 vs 8) and one passage runs the other way (p2c 6 vs 5).

**What the image says at the two largest gaps (this runner's two looks, M).** `page1_L09_seq61-79_17marks.jpg` (ms line
7, 15 marks; codex sub-run 17) shows about 21 separable signs plus 4 dots; `page3_L05_seq417-426_7marks.jpg` (ms line
36, 7 marks; part of p3d) about 13-14 signs. So the two sources count different units: on long runs the ms '*' is a pen
cluster (a joined group of two or three signs written without lifting), the codex/Tomokiyo token a single sign, and
the codex count is the nearer to what the eye separates. The disagreement is a unit convention, not a reading error,
so the "graded sequence" is the codex token sequence with grade H on the 11 passages where the cluster count equals
the sign count and M on the rest (`h15/glyphs_reconciled.tsv`); a position-by-position reconciliation of the long runs
would need fresh line crops (the `images/shorthand` crops are cut to the pre-H5/H17 ms) and a second sign-level reader,
neither in this step's box.

**Wave-merged variant (`h15/glyphs_wavemerged.tsv`, `.txt`).** ARM-S1's reading applied mechanically: consecutive
tokens of Tomokiyo's wave types 20/22/23 collapsed to one -- it removes only 5 of 257 tokens (252 left), so it does
not explain the 40-token gap either; it is the one alternative segmentation on file, and the two tests were re-run on it.

| test | original (H2 / H3 on the codex tokens) | wave-merged variant |
|---|---|---|
| pairs_test B, odd-vs-even shape JSD vs the within-fragment shuffle null | 0.160, percentile 94.8 (32 vs 26 distinct shapes) | 0.135, percentile 74.8 (32 vs 27); pair controls unchanged (`h15/pairs_test_wavemerged.tsv`) |
| H2 glyph-null shuffle, glyph-20-null model (150 restarts x 50,000, seed 731, 200 shuffles) | PASS at seed 731, inside the band over 11 seeds | CONTROL BELOW GATE: control 0 read 88/218 (controls 1-2 216/218, 218/218) -- one of three matched controls not solved at this K, target not run (rule 3; `h15/h2_results_wavemerged.tsv`) |
| H2, glyphs 20+22 null model | FAIL, percentile 49 (102/200) | FAIL, percentile 33 (134/200 at or above the target; controls 204/206 x3) |

**Verdict for the campaign.** Done; no reading, no class change. The marginal test-B signal of H3 (percentile 94.8)
does not survive the only alternative segmentation on file (74.8), and the H2 glyph-null picture is unchanged (no
model separates the target from its own shuffles; one control failure shows the solver's own restart luck at this K).
What H15 establishes is that the two transcriptions are not two readings of the same units: any future sign-level
work (line B's B32 solver, a per-position reconciliation) should start from Tomokiyo's/the codex token stream with the
ms run counts as cluster boundaries, not treat the ms '*' count as a sign count. Suggested follow-up, not filed as a
row (line B holds the glyph work): fresh line crops on the current ms lines for the six long runs and a second
sign-level reader, then `tools/reconcile_passes.py` on the two sign-level passes.

Files: `h15/align.py`, `h15/runs.tsv`, `h15/glyphs_reconciled.tsv`, `h15/glyphs_wavemerged.tsv`,
`h15/glyphs_wavemerged.txt`, `h15/pairs_test_wavemerged.tsv`, `h15/h2_results_wavemerged.tsv`,
`h15/h2_shuffle_scores_wavemerged.tsv`; `adj/pairs_test.py` and `glyphnull/h2_shuffles.py` gained environment
overrides for the glyph table and output paths (defaults unchanged). No network; no subagent (0 of 4 vision calls);
this runner's two crop looks. Cost: the row's estimate (3 USD) is what `--spend` records (script work plus the H2
C++ re-run, about 5 minutes on 4 cores).

## Campaign step H33 (28 Sept 2026, 05:16-05:42 UTC)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01NuaRiPghx6VRXA6GuJE8ne). Hypothesis H33 (from
H31/H32): the Madrid legation cipher pool, part 2 -- the remaining coded frames of NARA M31 reel 12 read blind and
merged into H32's stream, re-screened against the target; the record sweeps of the unswept reels were beyond the
four-call limit and are left in a follow-on row (H38).

**Reads.** Two blind Sonnet calls: frame 404 both pages (50 crops, cut in H32; 69 + 16 groups -- the right page's
numeral layer is faint to absent from its fifth line on at this resolution, logged as NONE rather than guessed) and
frame 409 left page (24 crops; 128 groups, 86 without an alignable gloss). Frames 389 and 390 are a clerk's fair copy
in a neat hand with three short coded runs and no interlinear gloss, so this runner read them directly from 3x strips
instead of spending two calls (`h33/reads/f389R.tsv`, `f390L.tsv`, 14 + 15 groups, M): "the Emperor has destined
Augereau 677. 390. 475. 934. 38. 831. 594. 268. 869. 457. 742. 226. 525. 825 ..." and "what I have learnt here from
891. 677. 704. 870. 138?. 1107. 1685. 248. 1407. 1651. 807. 1473. 133. 1286. 916. ought to be well informed" -- the
neat hand writes 1651 plainly, which settles H32's open digit question: the value the faint-hand readers gave as 1657
(12 tokens) and H26's native-crop reader as 1651 is 1651 (9 tokens read so here), one value, glossed "the".

**Pool after H33 (`h32/legation_groups.tsv`, `h32/legation_screen_input.tsv`, `h33/summary.txt`,
`h33/screen_output.txt`): 497 groups over seven coded pages (403R 103, 404L 69, 404R 16, 408R 142, 409L 138, 389R 14,
390L 15), 489 clean digits, 311 distinct values, 275 glossed; with H26's 211 about 700 groups of the cipher on file.**

| check | number |
|---|---|
| same-table check vs H26's 24 Mar 1807 letter (128 distinct) | 59 distinct values shared vs random-draw null mean 23.3, p95 30 -- one table |
| target overlap (311 legation distinct vs the target's 216) | 43 shared vs random null mean 34.6, p05 27, p95 43 -- at the null's edge with 311 of 1,700 values drawn, not a signal on its own |
| the 12 commonest legation values (133, 1657/1651, 624, 244, 1481, 628, 69, 165, 1578, 424, 1114; 21% of the stream) in the target's 369 groups | expected about 71 at the legation rate, observed 0 |
| `corr/screen.py` at n=489 | units 0/1 share 0.24 vs the target's 0.59; above 1700 0.008 vs 0.09; under 100 0.12 vs 0.36; top-20 overlap 11/489 (chance); **MISS** |

So the Madrid legation cipher is not the target's code at n=489 (third screen, same verdict as H26 at 211 and H32 at
238), and the pool is on file for the scout as a key-recovery candidate of its own: a 1807 US legation private cipher
(values 1-1698, syllable and word entries, the/of at 1651/133, Augereau, Prince of Asturias, Junot-era Portugal
matter) with the period's interlinear decode beside about 275 of its groups. Digits are M throughout (faint pencil on
an upscaled microfilm; two readers agree on the commonest values), glosses C where they recur consistently and M
otherwise. Frames 426-429 (the last coded despatch of the run) are unread; the record sweeps of M31 reel 12 frames
1-380 and reels 11 and 13 (about 1,177 frames) are unrun: H38.

No reading of the target, no class change; rule 10: catalogued NARA despatches, the period's own decode, nothing
called new or first. Requests: none (all images from the H31 PDFs). Vision: 2 of 4 subagent calls (Sonnet, 152k and
329k tokens, 10 and 23 minutes) plus this runner's three looks (the two-frame view, two 3x strips). Cost: get_session
carries no cost figure; about 6 USD by H21's rate -- `--spend` records 6 against the row's 8.

## Campaign step H38 (28 Sept 2026, 05:41-06:10 UTC)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01NuaRiPghx6VRXA6GuJE8ne). Hypothesis H38 (from
H33): the last coded despatch of the M31 reel 12 run -- frames 426-429 -- into the legation cipher pool, for the
record and the scout; the record sweeps of the unswept reels need twelve more calls and stay in H39.

**Material.** Frame 426 heads "Private No 24, In the cypher of the Legation, Duplicate, Madrid Dec 22 1807" (Erving to
Madison); coded pages 426 right, 427 both, 428 left (lower half) and right (upper part); 429 is the closing, signature
and a postscript in clear (H31's screener flag on it was the letter's end, not code). Embedded microfilm images from
the H31 PDF (1716-1804 px per spread), band crops by `h29/band_cut.py --scale 2.5` (`h38/MANIFEST.tsv`).

**Reads.** Four blind Sonnet calls: 426R 97 groups, 427L 169, 427R 153, 428L 55 + 428R 79 = 553 groups; every reader
reports the recurring cursive "4" that reads like an "A" (resolved by recurring values), gloss alignment mostly low
or medium confidence, and 1651 = "the" at high confidence wherever the gloss is legible (six lines on 427R alone);
`h38/reads/`.

**Pool after H38 (`h32/legation_groups.tsv`, twelve coded pages of four despatches; `h38/summary.txt`,
`h38/screen_output.txt`): 1,050 groups, 1,030 clean digits, 484 distinct values, 500 glossed; with H26's 211 about
1,260 groups of the Madrid legation cipher on file.** Commonest values: 133 x41, 1651 x34 (+14 read as 1657 in the
faint hand), 244 x20, 624 x19, 1481 x17, 926 x14, 69 x14, 1362 x12, 1114 x11, 1578 x10, 525 x10.

| check | number |
|---|---|
| same-table check vs H26's 24 Mar 1807 letter (128 distinct) | 82 distinct values shared vs random-draw null mean 36.4, p95 44 -- one table across all five despatches |
| target overlap (484 legation distinct vs the target's 216) | 66 shared vs random null mean 53.8, p05 44, p95 63 -- just above the null, which at 484 of 1,700 values drawn is the range effect of two 1-1700 codes, not a shared vocabulary: see the next row |
| the 12 commonest legation values (21% of the stream; 133 and 1651 alone are 7%) in the target's 369 groups | expected about 77 at the legation rate, observed 0 |
| `corr/screen.py` at n=1,030 | units 0/1 share 0.23 vs the target's 0.59; above 1700 0.006 vs 0.09; under 100 0.09 vs 0.36; top-20 overlap 18/1,030 (chance 1.0 for >= 3); **MISS** |

Verdict for the campaign: done. The Madrid legation cipher is not the target's code at n=1,030 (fourth screen, the
same verdict as at 211, 238 and 489; the target never uses the cipher's "the" or "of" once), and the pool is complete
for the reel: every coded frame H31's sweep of frames 381-480 found is now read. For the scout (rule 10 wording: a
catalogued NARA despatch series with the period's own interlinear decode): about 1,260 groups of a 1807 US Madrid
legation private cipher, 500 of them glossed, values 1-1698, syllable and word entries mixed, the/of at 1651/133 --
a key-recovery candidate in its own right, not for this target; digits M throughout (faint microfilm; recurring
values corroborate the commonest), glosses C where they recur consistently, M otherwise.

No reading of the target, no class change. Requests: none. Vision: 4 of 4 subagent calls (Sonnet, 175k-239k tokens,
13-25 minutes each) plus this runner's one look (the four-frame view). Cost: get_session carries no cost figure;
about 8 USD by H21's rate -- `--spend` records 8 against the row's 12.

## Campaign step H39, step 1 of 3 (28 Sept 2026, 06:09-06:20 UTC)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01NuaRiPghx6VRXA6GuJE8ne). Hypothesis H39 (from
H31/H38): the record sweeps of the NARA reels H26 and H31 left unswept, at the 700-px two-frame sheet scale whose
control passed in H31; this step is M31 reel 12 frames 1-380 (Erving, Aug 1805-early 1807). Reels 11 and 13 follow (H40).

**Method.** `h31/sheets.py` on the H31 PDF (190 sheets), four blind Sonnet screeners of 95 frames each; the M30 reel
11 sheet holding frame 65 (the 5-group WE028 run, H26 known answer) was appended to every call's file list without
comment. **CONTROL PASS 4 of 4:** every screener flagged m30-65 as code (three read the run's digits approximately,
one flagged it "possible, closer look" -- flagged either way, which is what a sweep needs). `h39/reads/m31r12_*.tsv`,
one row per frame; `h39/MANIFEST.tsv`.

**Result: 24 coded frames in 5 clusters, no key table, all in the two tables already on file.**

| frames | letter | cipher (from the screeners' noted values and this runner's one look) |
|---|---|---|
| 19, 31, 34, 37 | Erving to Madison, 1805, the despatch itself naming "Mr Pinckney's Cypher" | WE028: in/of/to/him at 1426/1576/569/182 among the noted values (14 of 56 in H29's Erving-Monroe WE028 stream) |
| 114, 115, 130 | late 1806, short runs and one dense opening with interlinear glosses | legation cipher (133, 1114, 1657/1651 among the noted values) |
| 151, 152, 153 | "Private No. 14 Duplicate", Madrid 27 Sept 1806, three frames in cipher, a clerk's note that "the whole of these letters are in Cipher, but the French translation of them interlined" | WE028, read from the leaf (this runner, 1400 px): 1385 the, 1576 of, 569 to, 182 him, 184 his, 1426 in, 999 from, 992 France, 169 he -- a received original without glosses |
| 169, 170 | "Private No. 16", Madrid 7 Oct 1806, two frames in cipher, opening 1385 | WE028 (by the opening value; M, not looked at) |
| 284, 285, 286 | "No. 21, In the Cipher of the Legation", Madrid 24 Mar 1807, three frames with pencilled decode words | the legation cipher: the NARA original of the letter H26 read from the LOC copy (`corr/erving1807_groups.tsv`) |
| 362, 363, 364, 365, 367, 368, 372, 373 | spring 1807, a despatch naming "Cypher writing", letter no. 2 (private) and no. 26, six full cipher pages and a worksheet with words interlined (373) | legation cipher (1651 x4 and 133 x2 among 18 noted values; 23 of 29 in the H32-H38 pool) |

Neither table is the target's (WE028: ARM-A2 and H29; the legation cipher: H26/H32/H33/H38), so no frame goes to
`corr/screen.py`; a third cipher would have. For the record and the scout: the legation pool can grow by about ten
more full pages (284-286, 363-373, with the 373 worksheet a decode source), and WE028 usage by about eight
(19-37, 151-153, 169-170); the reel's earlier and later runs are now both swept (H26 481-628 at 400 px, H31 381-480
and this step 1-380 at 700 px). Blank/target frames: 1-5, 328, 330, 340.

No reading of the target, no class change; rule 10: catalogued NARA despatches, nothing called new or first.
Requests: none. Vision: 4 of 4 subagent calls (Sonnet, 168-177k tokens, 3.5-6.5 minutes each) plus this runner's one
look (frame 151 right page). Cost: about 4 USD by H21's rate -- `--spend` records 4 of the row's 12.

## Campaign step H40, step 1 of 2 (28 Sept 2026, 06:19-06:28 UTC)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01NuaRiPghx6VRXA6GuJE8ne). Hypothesis H40 (H39's
steps 2-3): the record sweeps of M31 reel 11 (Bowdoin's Madrid despatches, Dec 1804-Apr 1808, 137 frames) and reel 13
(Erving, May 1808 on, 660 frames); this step reel 11 whole and reel 13 frames 1-300. Same method as H31/H39
(`h31/sheets.py`, 700-px two-frame sheets, four blind Sonnet screeners, the M30 reel 11 frame-65 control sheet in
every call's file list; `h40/MANIFEST.tsv`, `h40/reads/`).

**CONTROL PASS 4 of 4** (frame 65 flagged code by every screener, its digits read approximately each time).

**Result: no coded frame and no key table on reel 11 (137 frames: 7 target/title cards, 130 clear prose) or on reel 13
frames 1-300 (clear despatches, printed Gazeta/Diario de Madrid enclosures, the Bayonne and Fontainebleau documents, a
Gerona lottery table; blank leaves at 1-4 and 135).** Reel 11 frames 24 and 110 mention a cipher in passing (an
enclosure, "my cipher" carried) with no coded numbers on the page. So Bowdoin's channel and Erving's 1808 despatches
carry nothing in any table, which closes the M31 series for this target except reel 13 frames 301-660 (H41).

No reading of the target, no class change; rule 10: catalogued NARA despatches, nothing called new or first.
Requests: none. Vision: 4 of 4 subagent calls (Sonnet, 173-180k tokens, 3.5-5 minutes each); no runner look. Cost:
about 4 USD by H21's rate -- `--spend` records 4 of the row's 8.

## Campaign step H41 (28 Sept 2026, 06:28-06:36 UTC)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01NuaRiPghx6VRXA6GuJE8ne). Hypothesis H41 (H40's
step 2): the last unswept span of the M31 series, reel 13 frames 301-660 (Erving, 1809-1810), same method as H31/H39/H40
(`h31/sheets.py` 700-px sheets, four blind Sonnet screeners of 90 frames, the M30 reel 11 frame-65 control sheet in every
call; `h41/MANIFEST.tsv`, `h41/reads/`).

**CONTROL PASS 4 of 4.** **Result: no coded frame and no key table in frames 301-660** (clear despatches, printed Spanish
gazettes, decrees and university fee tables, financial accounts; blank or docket frames 301, 354, 411, 413, 658-660).
One frame, 396, is too dark and rotated to screen (its right column looks like an enclosure index): logged as
unscreened, not as clear.

**What the record sweeps add up to (H26, H31, H39, H40, H41).** M30 reel 11 (Pinkney, 324 frames) and M31 reels 11, 12
and 13 (Bowdoin and Erving, 1,425 frames) are now swept end to end at a scale whose control passed 13 of 13 times.
Every coded frame found belongs to one of two tables -- WE028 (Pinkney's and Erving's ordinary despatches, 1805-1808)
and the Madrid legation private cipher (Erving to Madison, 1806-1807, about 1,260 groups on file with the period's
decode) -- and neither reads the target (ARM-A2, H29; H26/H32/H33/H38). No key table and no third cipher anywhere in
the four reels. The Armstrong-adjacent NARA despatch series that a coded enclosure from Paris could have reached are
exhausted for this target; the remaining pools are people-gated (H8-H10, H35-H37).

No reading of the target, no class change; rule 10: catalogued NARA despatches, nothing called new or first.
Requests: none. Vision: 4 of 4 subagent calls (Sonnet, 160-170k tokens, 3-5 minutes each); no runner look. Cost:
about 4 USD by H21's rate -- `--spend` records 4.

## Campaign step H42 (28 Sept 2026, 14:19-14:28 UTC, container clock)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01BuquErzUYdSB116KPAM8qh, runner 3). Hypothesis
H42: M31 reel 12 frame 373 (H39's "worksheet with words interlined", spring 1807) is a period KEY SHEET of the Madrid
legation cipher rather than usage.

**Method.** Reel PDF refetched once (catalog.archives.gov medialz, M31-012.pdf, 158 MB, one request; not committed);
frame 373 rendered at native (1700x1564, pymupdf page 372). The runner looked at the whole frame first; then
`h29/band_cut.py n373.png ... f373L 30 0 905 1030 82 43 22 --scale 2.0` (19 code lines of the left page used, 20-22 are the
subscription), one blind Sonnet call on the 19 crops (`h42/reads/f373L.tsv`: 129 group rows, 88 distinct, 64 glossed),
scored by `h42/check.py` against the majority period gloss per value in `h32/legation_groups.tsv` (1,050 groups), with a
gloss-shuffle null (the frame's own glosses permuted over its glossed groups, 2,000 draws). Output: `h42/check_output.txt`.

**Result: usage, not a key sheet -- H42's key-sheet hypothesis is dropped by the look.** The left page of frame 373 is
the closing page of an Erving letter to Madison written in mixed clear text and legation-cipher groups, with a period
decode interlined over the groups, closing "Dear Sir with sincere respect and very truly your most obliged ... George W.
Erving"; the right page is "No. 30 Duplicate", Madrid 26 July 1807, in clear (the Tilsit armistice gazette). There is no
value-to-word list anywhere on the frame. The "worksheet look" H39's screener reported is the mixed clear/code layout.

**Same table, control-backed:** of 43 glossed groups whose value has a pool gloss, 20 agree with the pool's majority gloss
(1651 the x5, 133 of x4, 244 to x2, 926 he x2, 1407 with x2, 624 a, 579 Portugal, 1661 prince, 1411 will, 1027 be) vs a
gloss-shuffle null mean 2.3, p95 5. Most of the 23 disagreements are the reader's alignment of one gloss phrase over
several groups (e.g. "conducted of the Emperor as formerly" spread over 1387 805 133 1651 738 916, putting "the" on 133
and "emperor" on 1651), not conflicting period values; digits and glosses are single-reader, grade M. 21 glossed values
had no pool gloss (e.g. 1210 Spain, 1643 promises, 1696 an advice, 571 president); they go to H43's table at grade M.

**Target:** not re-screened -- the legation cipher is already a control-backed MISS against the target at n=1,030 (H38).
For the record: 14 of the frame's 88 distinct values also occur in the target's 216, mostly low values (1, 2, 10, 15, 16,
21, 38, 88) that any 1-1999 code shares; no reading of the target, no class change. Rule 10: a catalogued NARA despatch;
nothing here is called new or first.

Vision: 1 of 4 subagent calls (Sonnet, about 135k tokens, 6.4 minutes) plus the runner's two looks at the frame.
Requests: catalog.archives.gov 1. Cost: about 2 USD by H21's rate (`--spend` records 2 of the row's 3).

## Campaign step H43 (28 Sept 2026, 14:28-14:32 UTC, container clock)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01BuquErzUYdSB116KPAM8qh, runner 3). Hypothesis
H43: the Madrid legation cipher's value-to-gloss table, written down and entered in KEY-DESIGN.tsv so the design prior
knows this 1806-1807 US private cipher. Offline, no vision.

**Built:** `h43/build_key.py` (rerunnable, `--check`) -> `tools/data/uscodes-1800/key_legation_madrid_1807.tsv`, from
the blind single-reader reads with period interlinear glosses: h32/legation_groups.tsv (H32/H33/H38, 1,050 groups) and
h42/reads/f373L.tsv (H42, 129 groups). H26's letter (corr/erving1807_groups.tsv, the LOC copy) carries no glosses and
adds nothing; its NARA original (M31 reel 12 frames 284-286) has pencilled decode words, unread. **520 values seen, 313
glossed (561 glossed occurrences); grade C 21, M 292.** C = majority gloss attested at least twice and more than twice
the runner-up (the two-thirds share first tried was rejected before use on the table: the reader's phrase alignment
scatters 13 of 31 glosses of 133 over neighbouring words). C values: 69 in, 133 of, 244 to, 356 visit, 390 was, 408 his,
553 not, 579 Portugal, 624 a, 628 peace, 878 they, 926 he, 1027 be, 1178 secretary, 1407 with, 1422 one, 1484 is,
1578 that, 1651 the, 1657 the, 1661 prince. 1657 = the duplicates 1651 = the: H33 found 1657 is a misreading of 1651 in a
faint hand (frames 389/390), so 1657 stays in the table as read and is flagged here, not merged. Every digit string is
single-reader (M on digits whatever the gloss grade); some rows are misreads (numeral_max 7411 in a 1-1999 code).

**Where it lives and why not `corr/legation_key.tsv` as the row said:** a key*.tsv in this folder would be the folder's
only key, and tools/key_crossmatch.py's `compute_own_cts` would then pair it with the Armstrong target's own
ciphertexts as its "own text" -- a false self-pair for a table that is not the target's (H38 MISS at n=1,030). It sits
beside WE028 in `tools/data/uscodes-1800/` with `# home: none` header lines, and `tools/key_crossmatch.py`'s
EXTRA_KEY_GLOBS gains `tools/data/uscodes-1800/key*.tsv` (only key-named files; WE028.tsv and THE972_*.tsv are not
picked up). Offline tests: test_key_crossmatch, test_key_crossmatch_gate, test_design_prior all pass.

**KEY-DESIGN.tsv** rebuilt (183 rows, 118 usable; `--check` current). The rebuild also picked up two spinelli files that
another session had added without a rebuild (key_domnina_2016_atlasmap_v7.tsv, verify2/keymap_compare.tsv). The legation
row: design family **code numbers** (313 codes, 312 valued, 306 words, 114 short values, 3 single letters -- no alphabet
block among the values read), digit lengths 1:3, 2:29, 3:182, 4:99, no own ciphertext (home none).

**design_prior.py on the target** (`--no-write`, ciphers/armstrong-madison-1808/ciphertext.txt, 404 tokens, 219
distinct): multi-sign (homophonic/nomenclator/syllabary) plausible (d 0.66 vs null p05 0.69); code excluded (d 2.00 vs
envelope 0.93); letter-for-letter excluded; shuffled-input false-positive rate 0.060; nearest keys Huntington
Luzerne-Destouches 1781 (syllabary, d 0.49), van Beuningen-De Witt 1657, Thurloe Montagu. The prior's "code" exclusion
agrees with the legation table's family and with H38's MISS; the legation table does not change the target's prior
(it has no ciphertext signature for design_prior to compare). No reading of the target, no class change; rule 10: the
glosses are the period clerk's decode of catalogued NARA despatches, nothing called new or first.

Requests: none. Vision: 0. Cost: about 1.5 USD (`--spend` records 1.5 of the row's 2).

## Campaign step H45 (28 Sept 2026, container clock; see the CAMPAIGN.md log line)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01BuquErzUYdSB116KPAM8qh, runner 3). Hypothesis
H45: a cloud route to the Wouves 1797 table (H6's blocker) before H6 files an ASKS row.

**Routes tried (one request each unless stated, 1.6 s apart):** Wellcome catalogue API (works/jegb9q9f): "Tableau
syllabique et steganographique ... = A Syllabical and steganographical table", P. R. Wouves, Philadelphia, Benjamin
Franklin Bache, 1797; availability "Online" only through EBSCO/ECCO (ebs13612692e), no Wellcome digitisation. Internet
Archive advancedsearch (Wouves; title words in English and French): no item. Google Books API (key, country=US): the
1797 volume EQtQkgAACAAJ, NO_PAGES; nothing else. HathiTrust bibliographic API (OCLC 55825890 from Open Library): no
record. DPLA (key): 0. Gallica SRU: no hit. Evans-TCP at quod.lib.umich.edu: HTTP 403 (not retried). **Library of
Congress, "Copyright Title Pages, 1790-1801" (item 2020365001, full-text file): Wouves's own copyright deposit No. 192,
9 Nov 1797** -- the English and French title pages and the full printed "Elucidations", but **not the table**. Excerpt
kept unmodified in `sources/loc-copyright-title-pages/` (README gives the URLs and sha1). So the table is still only
behind ECCO (CB0131087164) or a physical copy: ASKS row filed (below), H6 stays `doc`.

**What the deposit gives (primary, the author's own words; grade H for the mechanism, not for any value):** 62
alphabetical columns; every numerical column "numbered from 1. to 99." (row 0 does not exist); each column gets a
hundred "taken at random", recommended 100 to 6200 (one per column, so a full table spans 62 hundred-blocks); an
entry is hundred + row (their example: third column at 6200, row 22 -> 6222); at most three letters per entry, a
word divided into parts is hyphenated (5347-3928-6222) and every word ends with a stop; a dot under a number marks an
accent; a list of hundreds and a sliding paper slip let one table serve several correspondents; and (French text,
"De la Sureté du Secret") correspondents may add or subtract an agreed constant from every number.

**Mechanism-level screen of the target (offline, counting; the table's syllables are not needed for it):** the target
(ciphertext.txt, 369 groups, 216 distinct, values 1-1900) has 132 groups (48 distinct values) below 100 and uses 20
hundred-blocks (0-19), none of them hyphen-joined (0 hyphens). Under the printed design without an offset, values below
101 cannot occur: excluded. With the agreed-constant variant, a letter's values fall inside a 20-block window only if
every column it uses drew its hundred from the same 20 consecutive of the 62; with m >= 20 columns used (each observed
block needs at least one) and hundreds assigned at random as the author instructs, that probability is at most 43 x
C(20,m)/C(62,m) <= 43/C(62,20), about 6e-15. And one column (two initial-letter classes of syllables) would carry 36
percent of the text (the sub-100 block). So Wouves as printed and used as its author instructs does not fit the
target's value range; what survives is a non-random hundred assignment (the text's columns all given hundreds 1-19),
which the counting cannot exclude. This agrees with the ChatGPT continuity note (second-opinions/chatgpt-continuity-
2026-09-27.md: offsets constrain but do not exclude) and line B's B1 (Wouves layout r_row -0.063). It is a structural
screen, not H6's value-level screen, and is not logged as a design-family negative (no matched synthetic control:
building one needs the table's column contents); H6 stays open on the document.

No reading of the target, no class change; rule 10: a catalogued 1797 imprint, nothing called new or first.
Requests: api.wellcomecollection.org 1, archive.org 4, googleapis.com 4, openlibrary.org 2, catalog.hathitrust.org 1,
api.dp.la 1, gallica.bnf.fr 1, quod.lib.umich.edu 1 (403), loc.gov 4 (one HTTP/2 stream reset, not retried),
tile.loc.gov 1. Vision 0. Cost: about 1 USD (`--spend` records 1 of the row's 2).

## Campaign step H46 (28 Sept 2026, to 14:41 UTC, container clock)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01BuquErzUYdSB116KPAM8qh, runner 3). Hypothesis
H46: tools/key_crossmatch.py on every pair the H43 legation table touches.

**Run:** `python3 tools/key_crossmatch.py --since-hours 1 --out-tsv <scratch>` (8.9 s; 2 key files changed since
f85334f0, the legation table and a spinelli verify2 file; KEY-CROSSMATCH.tsv not touched). Legation rows kept in
`h46/xmatch_legation.tsv`: **64 pairs, 0 scored.** The tool's calibrated gate (stat >= 3.292, n >= 100) applies only
at coverage >= 0.5, and no ciphertext on disk reaches it with this table: the highest are maurice-rupert-1645 0.444 (n
99), lodewijk-van-nassau 4503/4612/4614 0.41-0.42, the Armstrong target 0.181 (n 404). **A non-test, not a MISS:** a
partial table of 313 glossed values out of a code of about 2,000 cannot cover half of any other text, the target
included; the coverage floor is the instrument saying it cannot decide. The target's evidence stays H38's
corr/screen.py MISS at n=1,030 (usage frequency, not table coverage). What would make the crossmatch able to test:
the table's coverage of the whole code, i.e. more glossed legation pages (H47 adds the 24 Mar 1807 letter's three
frames) -- a matter for the scout, not the target. No reading, no class change; nothing called new or first.
Requests 0, vision 0. Cost: about 0.5 USD (`--spend` records 0.5 of the row's 1).

## Campaign step H47 (28 Sept 2026, to 14:59 UTC, container clock)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01BuquErzUYdSB116KPAM8qh, runner 3). Hypothesis
H47 (record and scout, not the target): the NARA original of Erving to Madison No 21, Madrid 24 Mar 1807 ("In the
Cipher of the Legation"), M31 reel 12 frames 284-286, read into the legation table.

**Method.** Reel PDF on disk from H42 (not committed); frames rendered at native (1764x1180, 1684x1612, 1724x1188).
`h29/band_cut.py --scale 2.0` on five regions, each checked on its debug overlay and re-cut where the guides sat a
half pitch off: f284L (20,470-880,1010; centre 56, pitch 43, 12 lines), f284R (875,40-1730,1125; 37, 44.5, 24), f285L
(0,0-860,1110; 82, 39.3, 26), f285R (790,470-1684,1612; 42, 43, 24), f286L (20,0-880,200; 90, 46, 2), f286R
(815,0-1724,660; 80, 48, 12) -- 100 crops. Three blind Sonnet calls (the row's cap): f284L+R, f285L+f286L, f285R+f286R,
reads in `h47/reads/`. Scored by `h47/check.py` (output `h47/check_output.txt`); a crop repeating the previous
crop's group sequence is dropped as the same physical line (6 dropped: f284L 6, 11; f284R 17, 24; f285L 13, 20).

**Results (564 groups, 273 distinct, 270 glossed):**
- **Digits, against an independent witness of the same letter:** ARM-CORR's eye transcription of the LOC "Duplicate"
  (corr/erving1807_groups.tsv, pages 2-3, 211 groups) is matched in order by 172 groups of the NARA read, against a
  shuffled-NARA null mean 22, p95 31. On the 185 groups difflib pairs one-for-one, 13 differ (7.0 percent, an upper
  bound on this read's digit error there, since the LOC transcription is itself one reader). The same letter, and the
  two witnesses agree group for group.
- **Glosses, against the legation table's majority** (recomputed in check.py from H43's inputs only, so no leakage):
  64 of 168 testable glossed groups agree, against a gloss-shuffle null mean 6.3, p95 10. Most disagreements are the
  readers' positional alignment of a phrase over a run of groups (the readers say so); 97 glossed values were new to
  the table (e.g. 421 intercepted, 523 Russian, 763 disposition, 769 despatches, 1560 contents).
- Readers' flags carried as M: leading 2-3 digit fragments at the fold of f285R (groups cut at the page edge, kept as
  read), caret marks after some groups (noted), one struck gloss.

**Table rebuilt** (`h43/build_key.py`, now with the H47 reads and the same duplicate guard): 622 values seen, 395
glossed (831 glossed occurrences), **grade C 34** (was 21), M 361; KEY-DESIGN.tsv rebuilt, still **code numbers**
(395 codes, 394 valued), `--check` current. Newly C: 293 means, 347 has, 478 for, 523 Russian, 674 which, 720
more, 723 had, 870 their, 1340 an, 1343 and, 1370 she, 1560 contents, 1583 Henry (with 1603 = "Mister" before it: a
two-group name, per the glosses). Not the target's code (H38 MISS at n=1,030); nothing here touches the target's
reading or class. Rule 10: catalogued NARA despatches decoded by the period clerk; nothing called new or first.

Vision: 3 of 4 subagent calls (Sonnet, about 167-183k tokens each, 11-13 minutes) plus the runner's looks at the
three frames and five overlays. Requests: 0 (reel on disk). Cost: about 3 USD (`--spend` records 3, the row's est).

## Campaign step H48 (28 Sept 2026, to 15:01 UTC, container clock)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01BuquErzUYdSB116KPAM8qh, runner 3). Question:
is the Madrid legation cipher (the one 1806-1807 US private code on file with its decode, H43/H47) a period precedent
for the target's design family C (a 1-99 particle block, a book >= 100)? Offline.

**Test** (`h48/particle_block.py`, output `h48/output.txt`): per table, the share of valued codes below 100 whose
value is an English function word (a fixed list of about 120 in the script) minus the same share at >= 100; null = the
table's own values permuted over its codes, 2,000 draws.

| table | codes < 100 | FW share | codes >= 100 | FW share | diff | null p95 | p |
|---|---|---|---|---|---|---|---|
| legation, all glossed | 39 | 0.513 | 356 | 0.463 | +0.049 | +0.135 | 0.33 |
| legation, grade C only | 1 | -- | 33 | 0.727 | -- | -- | (n too small) |
| WE028 (Department) | 98 | 0.020 | 1164 | 0.060 | -0.040 | +0.038 | 0.98 |
| THE972 Bourdeau (Department) | 14 | 0.071 | 566 | 0.166 | -0.095 | +0.198 | 0.92 |
| control: legation values, function words moved into all 39 low codes | 39 | 1.000 | 356 | 0.410 | +0.590 | +0.135 | 0.0000 |
| control: half the low codes function words | 39 | 0.487 | 356 | 0.466 | +0.021 | +0.135 | 0.47 |

**Result:** no full particle block in the legation cipher (its low codes are no likelier to be function words than
its high ones), a result the full-block control shows the test could have detected. A partial block is **untestable**
here: the half-block control does not clear either, because 46 percent of the legation's glossed values are already
function words (the letters' glossed runs are short connective words plus the readers' phrase-alignment spread), so
the base rate leaves no headroom (rule 3, headroom clause). Neither Department table has one either (known: they are
alphabetical one-part codes). So no period table on file is a real instance of family C; H27's synthetic slot design
stays the only family-C control, and this step gives it no period grounding. No reading, no class change; nothing
called new or first. Vision 0, requests 0. Cost: about 0.5 USD (`--spend` records 0.5).

## Campaign step H49 (28 Sept 2026, to 15:03 UTC, container clock)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01BuquErzUYdSB116KPAM8qh, runner 3). Question:
do the target and the Madrid legation cipher share a particle list (the same values 1-99 used at the same rates)?
H38's screen used the commonest legation values, all >= 100; the particle block alone was never compared. Offline.

**Test** (`h49/particle_list.py`, output `h49/output.txt`): Spearman rho between the target's count of each value
1-99 and a reference stream's count of the same value, over all 99 values; null = the reference's counts permuted over
the values, 5,000 draws. Streams: target 369 groups (132 below 100, 48 distinct); legation usage 1,738 groups (h32 +
h42 + h47 with the duplicate guard; 174 below 100, 64 distinct); WE028 usage (h29, Erving to Monroe 1806; 12 below
100) as a negative reference. Control (power at the target's N): 50 windows of 369 groups from the legation stream,
each against the rest of the stream.

| comparison | rho | null p95 | p |
|---|---|---|---|
| target vs legation | +0.002 | +0.172 | 0.50 |
| target vs WE028 usage | -0.093 | +0.169 | 0.82 |
| control: legation 369-windows vs rest | mean +0.284 | -- | clear their null p95 in 39 of 50 |

**Result: MISS, control-backed** (78 percent power at N=369; the windows share their letter's vocabulary with the
neighbouring rest of the stream, so that figure is if anything optimistic). The target does not use the legation
cipher's low values the way the legation letters do, so no shared particle list; and the shares differ outright
(36 percent of the target's groups are below 100, 10 percent of the legation's). With H38 (commonest values) and H48
(no particle block in the legation code), the Madrid legation cipher is excluded as the target's code or its
particle source at every level tested. No reading, no class change; nothing called new or first. Vision 0, requests
0. Cost: about 0.5 USD (`--spend` records 0.5).

## Campaign step H50 (28 Sept 2026, to 15:04 UTC, container clock)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01BuquErzUYdSB116KPAM8qh, runner 3). Question:
are the target's two oddities that ARM-CODES could not reproduce from any Department table or THE=972 usage -- the
last-digit-0/1 excess and the 900-1099 gap -- a habit of period PRIVATE codes? The Madrid legation cipher is the
first private sibling on file. Offline.

**Test** (`h50/private_habits.py`, output `h50/output.txt`; streams loaded by h49/particle_list.py): on 1,000 random
contiguous 369-group windows of the legation usage (1,738 groups), z0 = share of tokens >= 100 ending in 0, d01 =
share of all tokens ending in 0 or 1, gap = distinct values in 900-1099.

| statistic | target | legation windows p05 / median / p95 | target percentile | WE028 usage (250) |
|---|---|---|---|---|
| z0 | 0.388 | 0.074 / 0.097 / 0.121 | 100 | 0.109 |
| d01 | 0.431 | 0.203 / 0.236 / 0.271 | 100 | 0.208 |
| gap (distinct in 900-1099) | 4 | 14 / 19 / 24 | 0 | 23 |

**Result:** the legation cipher's usage is flat in the last digit and fills 900-1099 like any other range; the target
lies outside its whole band on all three. The statistics do vary across windows (the band is the null), so the test
could have placed the target inside. So the oddities are not a habit of the one period private code on file; they
stay target-specific design clues (ARM-DESIGN's decade/slot reading of the last digit, B1/B2's row design), as
ARM-CODES left them. No reading, no class change; nothing called new or first. Vision 0, requests 0. Cost: about 0.3
USD (`--spend` records 0.5).

## Campaign steps H51 and H53 (28 Sept 2026, to 15:07 UTC, container clock)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01BuquErzUYdSB116KPAM8qh, runner 3). The Yale
Humphreys-Marvin-Olmstead Collection (MS 857) lead that the owner's ChatGPT checkpoint of 27 Sept 22:44 UTC located
in the finding aid but did not acquire (second-opinions/chatgpt-checkpoint-2026-09-27-2244.md).

**Route.** archives.yale.edu answers curl with an empty HTTP 202 (bot check); `tools/browser_fetch.js` renders it
(4 page loads, 2 s apart). Finding aid PDF fetched once by curl (ead-pdfs.library.yale.edu/4476.pdf, 48 pp.).

**H51, b.4 f.116** (archival object 1473122, Series I David Humphreys Papers > Diplomatic Miscellany > [Smith, John,
1735-1816?]): "Statement re letter of [John?] Armstrong, 1758-1843, about the purchase of Florida by the United
States, with a covering memorandum of the same date, 1808 April 25". Holding record: "Box: 4, Folder: 116 (Mixed
Materials) -- Stored offsite", "The materials are open for research", **no digital object**; Yale's digital
collections search returns 0 results for the collection. Not digitised, not readable from the cloud: **ASKS row 91**
(a scan request to Yale; contact address as printed on the record page). H52 (which Armstrong letter it concerns,
and any crib) waits on it. The same search also lists, in Series II, a pre-1803 copy letter to Barbe-Marbois with an
Erving memorandum on the purchase of Florida (the Louisiana-era negotiation, not 1808).

**H53, Series II George William Erving Papers 1803-1808** (archival object 1473249): scope note -- "No correspondence
of Erving is preserved here"; a memoranda book "in the form of a diary" for Oct 1805-Feb 1806 "with scattered entries
through July 1808", plus printed matter and copies of documents on Spain and the Napoleonic wars; one fifth of a box;
no digital object. A diary of conversations is an unlikely home for a key list; its 1808 entries go into ASKS 91 as
the lower-priority half.

No reading, no class change; a catalogue search, nothing called new or first. Vision 0. Requests: archives.yale.edu
4 (browser), collections.library.yale.edu 1 (browser), ead-pdfs.library.yale.edu 1. Cost: about 1 USD each (H51
records 1, H53 records 0.5).

## Campaign step H54 (28 Sept 2026, to 15:10 UTC, container clock)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01BuquErzUYdSB116KPAM8qh, runner 3). Question:
how coarse must the shorthand glyph inventory be before two blind readers agree? B35 (line B) found 80 percent label
disagreement on Tomokiyo's 38 types and tried one merge (23/29 classes). Offline; line B's files read, not edited.

**Method** (`h54/coarse_curve.py`, output `h54/output.txt`): B35's passes A and B via its own reconcile.py loader;
greedy agglomeration on one half of the crops (merge the pair of classes the readers confuse most), scored on the other
half at every class count from 29 down to 2: positional agreement, the agreement expected by chance from the readers'
own class marginals, and Cohen's kappa. Both splits.

| held-out half | aligned pairs | best kappa (classes, agreement) | agreement at 10 / 5 / 2 classes (chance) | 90 pct reached |
|---|---|---|---|---|
| crops 16-29 | 22 | +0.263 (10, 0.727) | 0.727 (0.630) / 0.727 (0.711) / 0.773 (0.723) | never |
| crops 1-15 | 90 | +0.357 (about 20-22, 0.422) | 0.422 (0.185) / 0.511 (0.281) / 0.578 (0.449) | never |

**Result:** at no inventory size, down to two classes, do the two readers reach B35's 90 percent gate, and kappa never
passes 0.36 (fair agreement at best): the coarse merges raise raw agreement only as fast as chance agreement rises.
So the readers' disagreement is not a granularity problem that a smaller sign list fixes; at this image quality the
type assignment is unreproducible at every granularity (the 16-29 split rests on only 22 aligned pairs; the 1-15 split
on 90 carries the weight). Consequences: H56 (a pattern-only name test) is dropped on its own condition; H55 (fusing
the two exposures of frames 31/32 as better material) is the only glyph step left, to be judged against this curve at
the best-kappa size (about 10-20 classes). No reading, no class change; nothing called new or first. Vision 0,
requests 0. Cost: about 0.3 USD (`--spend` records 0.5).

## Campaign step H55 (28 Sept 2026, to 15:12 UTC, container clock)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01BuquErzUYdSB116KPAM8qh, runner 3). Hypothesis
H55: fusing the two exposures of the page-2/3 spread (frames 0031, 0032) gives readers better material (B35's named
next step). Answered offline; the two vision calls were not spent.

**Registration** (`h55/fuse.py`, log `h55/fuse_log.tsv`; fused images in scratch, not committed): each of the 19
page-2/3 shorthand crops located in both frames by normalized cross-correlation (0.77-1.00) and registered by an ECC
affine fit (0.93-0.98). The check images show the two exposures essentially identical and already crisp: the readers'
disagreement is not microfilm noise, so averaging them cannot help much.

**Found on the way (for line B, whose files were not edited):** B35's crops 12/13 (images/shorthand/page2_L02 and
page2_L03) are the same physical line, one cut from frame 0032 and one from 0031 (both at y about 411/422, NCC 1.000
and 0.999 in their own frames), and so are crops 15/16 (page2_L06 / page2_L07, y about 955/953). B35 took them for
"two adjacent, similar lines"; ARM-TR2's page-2 off-by-one crop naming is the likely cause. So page 2 has two lines
read twice and (probably) two lines not cut at all.

**The duplicates are a free within-reader test** (`h55/self_consistency.py`, output `h55/self_consistency_output.txt`):
on crops 15/16 (the same line, near-identical image) reader A agrees with itself at 0.08 positionally (sequence ratio
0.17) and reader B at 0.20 (0.45) -- no better than the two readers agree with each other (0.00-0.42). Crops 12/13
give reader A 1.00 but are not independent (B35's readers flagged them as identical). Two lines only, but the same
verdict as H54: **the model reader with Tomokiyo's sheet is the limit, not the image.** By rule 3's unchanged-approach
clause, glyph type-reading by model readers is retired for this target as untested-by-this-tool (not refuted); the
next attempt needs a different instrument (H57, added) or a person. No reading, no class change; nothing called new
or first. Vision 0 (the step's two calls not spent), requests 0. Cost: about 0.5 USD (`--spend` records 0.5).

## Campaign step H58 (28 Sept 2026, to 15:15 UTC, container clock)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01BuquErzUYdSB116KPAM8qh, runner 3). Hypothesis
H58: audit the 29 shorthand line crops (images/shorthand/) that every glyph step used (B35 and its successors, H54,
H55), after H55's registration put page-2 crops on the wrong lines. Offline; one overlay look per page.

**Method.** `h58/boxes.py` locates each crop in its frame by normalized cross-correlation (1.000 on page 1 in frame
0030, 0.999 on pages 2-3 in frame 0031; `h58/crop_positions.tsv`) and draws the boxes; page 2's line centres from the
row-ink profile of frame 0031. Result table: `h58/shorthand_lines.tsv`.

**Result.** Pages 1 and 3: every shorthand-bearing line sits in a crop (page1_L03 is an empty band above the first
line; the page-1 crop names run one line ahead of the leaf, the content is right). **Page 2 is wrong in six of nine
crops:** page2_L01 is the blank header; L02/L03 and L06/L07 are each one physical line cut once per exposure (frames
0032 and 0031); L10 and L13 are numeral-only lines (B35's readers found 0 and 1 glyphs there). **Five shorthand-bearing
lines were never cut** -- physical lines 1, 4, 7, 11 and 13, about 14 signs in all (line 13's run and line 1's tail go
into the gutter) -- now cut from frame 0031 into `h58/crops/` (five JPEGs, 72-91 KB). images/shorthand/ itself is left
as it is (other steps cite it); the corrected map is h58/shorthand_lines.tsv.

**What rests on the wrong crops.** B35's crop set (line B) held 29 crops of which 5 show no new shorthand (crops 11,
13 or 12, 16 or 15, 17, 19); its agreement figures are unaffected in kind (the readers disagreed on real signs too,
H54/H55) but its glyph totals (A 244, B 239 vs Tomokiyo 257) miss about 14 signs and double about 25; any sequence
statistic over the B35 tokens (B30, B32, B38) mixed a duplicated line and missed five. The ms mark counts in
ciphertext_ms.txt and images/shorthand/index.tsv's per-line mark counts come from the transcription, not the crops,
and are not checked here; H18's attached-mark inventory used its own per-group crops (not re-checked). No reading, no
class change; nothing called new or first. Vision: the runner's three overlay looks and one look at the new crops;
requests 0. Cost: about 0.5 USD (`--spend` records 0.5).

## Campaign step H59 (28 Sept 2026, to 15:17 UTC, container clock)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01BuquErzUYdSB116KPAM8qh, runner 3). Hypothesis
H59: a person-read labelling pack for the shorthand signs, the one instrument H54/H55 leave. Offline build.

Built by `h59/build_pack.py` into `h59/person_pack/`: four lines that are shorthand end to end (page 1 physical
lines 9 and 10, page 2 physical line 2, page 3's last shorthand line; all four checked right by H58), each at 2x in two
overlapping halves with a position ruler, Tomokiyo's 38-type sheet, README with the answer template, and an empty
`h59/person_labels.tsv`. Automatic component numbering was tried first and abandoned: on these crops it split signs
and dropped real ones where a crop cuts them (page 2's crop is tight), so the person marks positions on a ruler and
H60 matches them to components. **ASKS row 92** filed. H60 waits on it. No reading, no class change; nothing called
new or first. Vision: the runner's four looks at trial sheets; requests 0. Cost: about 0.5 USD (`--spend` 0.5).

## Campaign steps H62 and H63 (28 Sept 2026, to 15:19 UTC, container clock)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01BuquErzUYdSB116KPAM8qh, runner 3). Question:
Jefferson wrote Madison on 17 May 1808 "I retain till another post Pinckney's, Armstrong's, Livingston's & mr
Gallatin's letters" (Founders Jefferson 99-01-02-8015, line B B6) -- did an Armstrong letter, a copy or a numeral
enclosure stay in Jefferson's own papers?

**H62, LOC Thomas Jefferson Papers** (loc.gov collection JSON; 4 requests): "armstrong" in 1808 gives 17 items -- the
Armstrong-Jefferson letters of 15 Feb, 15 June, 28 July, 9 Aug and 20 Oct 1808 and Jefferson's to Armstrong of 2 May
and 2 Dec (all read on Founders by line B, B20/B31), plus unrelated hits; no Armstrong-to-Madison letter, copy or
enclosure. "cypher" in 1808: one item (Monroe to Jefferson, 22 Mar 1808); "cipher": none. The full item list for 15
May-10 June 1808 (96 items) has only the Madison-Jefferson letters themselves (15, 16, 17, 19, 24, 27, 31 May; 2, 3
June), no Armstrong item, no enclosure and no undated numeral page. Search result: the letters Jefferson retained were
returned "by another post", as he wrote; nothing of them is catalogued in his papers at LOC.

**H63, MHS Coolidge Collection:** the MHS Jefferson site says only "selections" of its single items are digitised;
Founders' Jefferson series prints the MHS letters too, and line B read that series for 11 Feb-19 Oct 1808 (B20, B31;
ids 7400-8900, 1,378 of 1,413 fetched), finding nothing on the 20 Feb letter. Covered; no separate MHS search run.

No reading, no class change; search results, not negatives about the letter's existence. Requests: loc.gov 4,
masshist.org 2. Vision 0. Cost: about 0.5 USD for both (`--spend` 0.5 and 0).

## Campaign step H61 (28 Sept 2026, to 15:20 UTC, container clock)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01BuquErzUYdSB116KPAM8qh, runner 3). Question:
after H58, does ciphertext_ms.txt's page-2 line numbering (and images/shorthand/index.tsv's seq numbers and mark
counts) follow the leaf? Offline; the numerals of each ms line read against frame 0031's lines (the runner's look at
H58's page-2 overlay).

**Result: the transcription is right, the crop images are shifted.** ciphertext_ms.txt's page-2 lines 1-15 are the
leaf's physical lines 1-15 in order (54 1631 ... 1801 *; the all-shorthand line; * * * * 78 1364 ...; 17 86 316 ...;
1176 1164 ...; * 45 147 1158 ...; * * 48 1240 ...; 45 38 18 ...; 1776 1830 ...; ... 13 230 481 ...; 1110 1267 ...;
1 1471 1480 ...; 17 1640 ... 1540 * ...; 1161 14 ...; 2 471 ...), and index.tsv's page-2 names, seq ranges and mark
counts match those lines (e.g. L01 = 9 numerals + 1 mark = seq 188-197; L02 = 15 marks; L04 = 6 marks). So the
position statistics built on the transcription (B27, B29, B30's positions, H3, H18's per-group work on its own crops)
are not affected. **The error is only in the crop image files:** seven of the nine page-2 files (L01, L03, L04, L07,
L10, L11, L13) show the physical line above the one they are named for; L02 and L06 are named right. Any join of a
crop-based read to an ms line (B35's per-crop glyph reads against the ms mark counts; the page-2 half of the H18 and
H15 crop work, if it used these files) is off by one line on those seven. This corrects H58's own table, which had
called the L04 and L11 files "ok"; h58/shorthand_lines.tsv now says which file shows which line. No reading, no class
change; nothing called new or first. Vision 0 beyond H58's overlay; requests 0. Cost: about 0.2 USD (`--spend` 0.5).

## Web and blog check (CHECK-SOLVED-WEB, 28 Sept 2026)

Parent worker CHECK-SOLVED-WEB, 28 Sept 2026 15:23-15:27 UTC (clock-read), after the Spinelli N0 (a reading sitting in a Cipherbrain
comment thread). Plain web search (WebSearch) plus WebFetch of every plausible hit. **Verdict: no prior reading of the
20 Feb 1808 letter found beyond the AFIO contest claim already on file (and already rejected: "The AFIO claimed
solution and its adjudication" above).**

| # | Query / page | Hits and what they say |
|---|---|---|
| 1 | `Armstrong Madison 20 February 1808 cipher letter solved` | AFIO "We Have a Winner" (27 May 2025, the known claim); LoC mjm015002 (30 Aug 1808 postscript, a different letter, THE=972, read by Bourdeau); dbourdeau/cyphersolver + two forks (aryasn2026, arya1515); Founders 99-01-02-2728; our own SO PRs. The search engine's summary quotes the AFIO plaintext ("The French government has declared that American ships must not enter its ports ...") -- that is the AFIO claim, not a new source. |
| 2 | `"Armstrong" 1808 cipher Madison "undecyphered" decrypted` | same set; no new site. |
| 3 | `site:scienceblogs.de klausis-krypto-kolumne Armstrong Madison` (Cipherbrain) | two 2015 posts (1 and 3 Aug 2015) on a **1780** Madison cryptogram from Italy solved by Armin Krauß -- a different item; nothing on Armstrong 1808. |
| 4 | `Cipherbrain "Armstrong" "1808" encrypted letter Madison` | same AFIO/LoC/Bourdeau set; Founders 28 and 30 Aug 1808; puzzculture.com/tag/codecracking (fetched: no Armstrong post). |
| 5 | `ciphermysteries Armstrong Madison 1808 code`; `"Armstrong" 1808 Madison cipher site:ciphermysteries.com` | Cipher Mysteries: no Armstrong post (only generic pages, "Early American ciphers" 2009). |
| 6 | `cryptiana blogspot Armstrong letter 1808 undecoded`; `"Armstrong" "Madison" 1808 "shorthand" code letter Paris unsolved cipher` | Cryptiana blog; same solver-repo set. |
| 7 | WebFetch cryptiana.blogspot.com/2026/06/ | "Undecoded Armstrong's Letter (1808) Sent to Madison by Mistake", 4 June 2026: **0 comments**. |
| 8 | WebFetch cryptiana.blogspot.com/2025/10/ | "Decoding Armstrong's Letter: Help Wanted for Madison Papers", 22 Oct 2025: **0 comments**. |
| 9 | WebFetch github.com/aryasn2026/cyphersolver and github.com/arya1515/cyphersolver (forks of Bourdeau) | both list the 20 Feb letter under "Attempted and closed from the evidence": "The claim does not hold; the letter stays unsolved." |
| 10 | WebFetch dbourdeau.github.io/cyphersolver/index.html | only the 30 Aug 1808 postscript (solved, 49/49 groups); no 20 Feb entry claiming a reading. |

No flag raised. Conditional on the search engine's index (blog comment threads beyond the two Cryptiana posts fetched
were not reachable except through search). Not a novelty statement (rule 10).

## Campaign step H64 (28 Sept 2026, to 16:32 UTC, container clock)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01BuquErzUYdSB116KPAM8qh, runner 3). The key-hunt
rule (a) added to the campaign brief at 15:31 (CHECK-SOLVED-WEB): LOCAL-QUEUE L27's catalogue reads (ARM-OWN H34, which
tried curl and WebFetch only) retried once each through `tools/browser_fetch.js`, then Wayback.

| catalogue | browser tool (one load each, 2 s apart) | Wayback |
|---|---|---|
| archives.nypl.org/mss/6743 (MssCol 6743) | Akamai "Access Denied" (303 B) | not reachable (below) |
| discover.hsp.org, 'Armstrong, John, 1758-1843' | Cloudflare "Just a moment..." | not reachable |
| corsair.themorgan.org, same heading | Cloudflare "Attention Required!" | not reachable |
| researchworks.oclc.org/archivegrid, same heading | Cloudflare challenge (redirect with __cf_chl_rt_tk) | not reachable |
| masshist.org collection-guide browse list | loaded (94 KB, 704 guides): no Armstrong, John guide; only "William Livingston Family Collection 1664-1839" (the New Jersey family, not Robert R.) and an unrelated Erving Winslow | -- |

**Wayback:** web.archive.org resets the TLS handshake from this container (curl error 35, the agent proxy logs the
tunnel "closed mid-exchange"; three tries between 16:28 and 16:32 UTC), while archive.org answers 200 -- an
egress-path failure for that host in this environment, not a site verdict; per the good-citizen rule not retried
further. **Result:** no catalogue opened beyond H34's; L27 stays on the owner's desk, now with the browser-tool and
Wayback attempts logged, as rule (a) asks. No challenge was bypassed. No reading, no class change. Requests:
archives.nypl.org 1, discover.hsp.org 1, corsair.themorgan.org 1, researchworks.oclc.org 1, masshist.org 1,
web.archive.org 3 (reset). Cost: about 0.5 USD (`--spend` 0.5).

## Campaign steps H65 and H66 (28 Sept 2026, to 16:34 UTC, container clock)

Runner: campaign runner armstrong-madison-1808 (owner account, session_01BuquErzUYdSB116KPAM8qh, runner 3). Rule (a)
retries of two more desk rows.

**H65, ASKS 83 (LOC George William Erving papers finding aid):** web.archive.org resets from this container (H64);
loc.gov JSON search for the collection record: '"George William Erving papers"' 0 results, 'Erving papers Madrid' in the
Manuscript Division 16 unrelated hits, a manuscript-format facet query returned a non-JSON page (not retried); one guessed
finding-aid PDF id was a different collection (logged, not used). Not reached; ASKS 83 stays on the desk. Low value for
the target in any case: the Madrid legation cipher is excluded at every level tested (H38, H48-H50).

**H66, ASKS 86 (Ericson and Haggerty 1980, Livingston papers microfilm guide, OCLC 7776177):** HathiTrust bibliographic
API by OCLC: no record; Internet Archive advancedsearch: 0; Google Books API (country=US): 0; Open Library: the
catalogue record (OL6123259W, OCLC 7776177) with no IA scan. Not online; ASKS 86 stays with the owner.

No reading, no class change. Requests: loc.gov 3, tile.loc.gov 1, catalog.hathitrust.org 1, archive.org 1,
googleapis.com 1, openlibrary.org 1. Cost: about 0.5 USD for both (`--spend` 0.5).

## ARM-KEYHUNT (28 Sept 2026)

Parent worker ARM-KEYHUNT (owner account, Opus), brief `.claude/briefs/runs/2026-09-28-parent-arm-keyhunt.md`, 16:36-17:1x UTC
(container clock). Job: a key or a second letter in the target's private code in Bowdoin's, Pinkney's, Erving's and
Armstrong's own papers; screen every numeral-cipher item; draft requests for undigitised holdings (nothing sent). Files:
`keyhunt/` (requests.log, the extraction and screen scripts and outputs, the Founders texts read). Prior steps not repeated:
ARM3-COR, ARM-CORR H26 (Princeton C0027, LOC Pinkney 24 Jan 1808 = WE028, MdHS MS 1388), H25 (LOC Monroe Papers 1806-07),
H34 (Armstrong's own papers), H39-H41 (NARA M30/M31 sweeps), H64-H66.

**Result: no key and no sibling letter found online; one new, documented lead on who the "other correspondent" could be.**

**1. The lead: a private Armstrong-Monroe cipher existed, and Armstrong made the same mistake with it once before.**
Founders Online (read in headless Chromium, `keyhunt/founders/r4.txt`, `r5.txt`, `r6.txt`):
- Armstrong to Madison, 18 March 1805 (PJM-SS 9, Founders Madison/02-09-02-0150): the RC is docketed by Wagner "N.B. One of
  the enclosures contains passages of inexplicable cypher"; the enclosures were copies of Armstrong's letters to Monroe
  (then at Madrid) of 12 and 18 March 1805.
- Armstrong to Madison, 2 April 1805 (02-09-02-0222): "In copying my letter of the 16th [sic, = 18th] March to Mr Monroe,
  **the cypher established between him and me was employed, instead of that common to you and myself.** This error is now
  corrected in the duplicate copy transmitted herewith."
- Madison to Monroe, 23 May 1805 (02-09-02-0438): "The passages of this last in cypher, having not been copied into that
  used by this Department with Genl Armstrong remain locked up".
So in 1805 Armstrong's office sent Madison a letter in a private cipher concerted with another correspondent, and the
Department could not read it -- the same event Madison describes in 1808 ("No such Cypher is in the office, and must be one
concerted with another correspondent"). This does not show the 1808 letter is in the Armstrong-Monroe cipher (grade I,
inference only); it names a concrete private code of Armstrong's, with a known partner, that nobody has screened.
Against it: Armstrong to Bowdoin, Paris 22 July 1806 (printed, item 3 below): "Having no cypher in which I can write to
Messrs Monroe & Pinckney, and recollecting that you have ..." -- by mid-1806 Armstrong either no longer held the Monroe
cipher or did not use it for the joint London mission; and Monroe was back in Virginia from December 1807.
- Where the specimens are: NARA M34 roll 13 (NAID 188671172, vol. 10, whole-roll PDF fetched once, 395 pages) frames 29-35
  are the 18 March 1805 despatch and its enclosures, frames 56-58 the 2 April duplicate and a copy of Armstrong to Monroe
  5 April 1805. **Both coded copies on the roll are in the office code THE=972** (972 = the throughout, a period interlinear
  decode on each; `keyhunt/m34r13_1805_groups.tsv`, 170 groups read at the PDF's resolution, grade S one reader; screen
  `keyhunt/screen_m34r13_1805.txt`: units 0/1 0.19 vs target 0.59, above 1700 0.006 vs 0.092, under 100 0.01 vs 0.36, top-20
  overlap 0 -- MISS). The "inexplicable cypher" copy itself was not found on roll 13 at this pass (frames 1-60 looked at on
  contact sheets and 34, 35, 58 at page resolution): either it was withdrawn when the corrected duplicate came, or it sits
  elsewhere in the roll. The Monroe side: where the RCs of Armstrong to Monroe of 12 and 18 March and 1 and 5 April 1805
  (addressed to Madrid) are is not established -- the 1904 LOC calendar lists no 1805 Armstrong letter (H25); the Madison
  Papers cite Monroe's Madrid-period incoming letters to "NN: Monroe Papers" (NYPL, MssCol 2035; e.g. Erving to Monroe 2 Mar
  1805, 02-09-02-0094), and a web-search snippet of the LOC Monroe finding aid places Monroe's letterbook Nov 1804-May 1805
  at NYPL (I, not read on the page) -- so NYPL is the likeliest home. archives.nypl.org is Akamai-blocked and digitalcollections.nypl.org behind a bot check from
  here (H34/H64 and this pass). Request drafted (below).
- LOC Monroe Papers (mss33217, series 1 reel 3): H25's two unlocated "Dec 1804" Armstrong-to-Monroe letters -- one found,
  **reel 3 frame 0638, Armstrong to Monroe, Paris 24 Dec 1804, clear** (frames 562-650 sampled every third at pct:15, then
  626-650 every frame; frame 0638 read at pct:40); Dec 1804-Apr 1805 spans frames about 589-648, no numeral page seen at that
  scale (a negative for dense pages only). No key sheet seen.
- Printed Monroe: *Writings of James Monroe* vol. IV (Hamilton, 1900; IA writingsjamesmo03monrgoog) prints Monroe to
  Armstrong 2 July, 26 Aug, 2 Sept, 14 Nov 1805 and 11 Mar 1806 in clear; a footnote says the *Bulletin of the NYPL* IV no. 2
  (Feb 1900) print "gives also cipher numbers". Read that Bulletin (IA bulletinnewyork34librgoog): its cipher numbers belong
  to Monroe's letters **to Madison** (6 July and 22 Nov 1805: 1385 the, 569 to, 1576 of -- WE028), not to Armstrong; the
  Armstrong letters are clear there too. Negative for a printed Armstrong-Monroe specimen.

**2. Pinkney (brief item 3).** Nothing new to screen: Pinkney to Madison 24 Jan 1808 is WE028 by known answer (H26); Princeton
C0027 and MdHS MS 1388 read (H26); M30 reel 11 swept (H26/H31). Founders adds Madison to Pinkney 19 Feb 1808 with a cipher
postscript (office-to-legation, the Department's own code) -- not Armstrong's. No Pinkney letterbook found digitised in this
pass (not searched beyond Founders and the H26 catalogues). No draft: every Pinkney holding named is already read.

**3. Bowdoin (brief item 2).** Reachable and read: *The Bowdoin and Temple Papers* pt. II (Collections MHS 7th ser. vol. 6,
1907; IA collectionsofmas00mass_17, full text, public; pt. I = 6th ser. vol. 9, IA bowdointemplepap00bowdrich, 1756-1782, no
Armstrong). Pt. II prints 17 Armstrong-Bowdoin items 1806-07 and dozens of Bowdoin-Erving letters with **bracketed period
decipherments** (`keyhunt/extract_bt.py` -> `bt_pairs.tsv`, 123 runs). Screened: 78 of 123 runs read MATCH under WE028
("Mr Monroe's cypher"; most of the rest are OCR damage or entries missing from our WE028 table; `bt_we028_check.tsv`), and
Madison to Bowdoin 25 May 1807 (four runs, 1651 frequent) is in the Madrid legation cipher ("Mr Pinckney's cypher"). Screen
of all 512 groups (`screen_bt.txt`): MISS (units 0/1 0.17, above 1700 0.008, under 100 0.03, top-20 overlap 0). What the
volume says about Armstrong: the 22 July 1806 "no cypher" letter above; Bowdoin to Erving 1807, "for my own part with the
exception of a few lines in one of my letters to the President, I have used no cyphers"; and the Aug-Sept 1807 exchanges
between Armstrong and Bowdoin are open quarrels ("On these points I disdain to answer your questions") -- a private cipher
between the two by Feb 1808 is unlikely (inference). Bowdoin was in London by 17 Feb 1808 (ARM3-COR). Bowdoin College's
own holdings (Bowdoin family collection, James Bowdoin III letterbooks 1791-1811 incl. 1806-1811): archivesspace.bowdoin.edu
is Cloudflare-challenged to curl, the browser tool and WebFetch; Wayback resets from this container; Bowdoin Digital
Collections (reachable) has no letterbook scan ("Armstrong cipher", "Bowdoin Armstrong 1807": no results). Request drafted.

**4. Erving (brief item 4).** No catalogue shows Armstrong correspondence in Erving's private papers (LOC Erving papers aid
unreachable, ASKS 83; Yale MS 857 Series II: "No correspondence of Erving is preserved here", H53). The printed Bowdoin volume
shows Erving and Bowdoin in WE028 1805-07. No draft (brief: only if a catalogue shows Armstrong correspondence in 1808).

**5. Armstrong's own key copy (brief item 5).** Nothing online beyond H34/H64: NYHS aids 403 (WebFetch too), NYPL Akamai.
Requests drafted for NYHS (ASKS 84) and the FDR Library (Rokeby/Aldrich roll, ASKS 85).

**6. Printed editions (brief item 6).** Founders Online full-text "Armstrong AND cypher" (27 hits, all read in the list,
twelve opened, `keyhunt/founders/`): nothing names a private cipher between Armstrong and anyone other than Monroe; Graham to
Madison 10 and 20 May 1808 (the target and its duplicate with a postscript, "a Cypher to which we have no Key") already known
(H62, line B). The Livingston microfilm guide (ASKS 86) is still not online (H66).

**Numeral-cipher items screened this pass: 3 sets** -- Bowdoin-Temple printed runs (WE028 + legation, 512 groups, MISS),
M34 roll 13 1805 enclosures (THE=972, 170 groups, MISS), NYPL Bulletin 1900 Monroe-Madison runs (WE028 by values read,
not screened further). Candidate key or sibling: none. Status unchanged (`open`). Rule 10: printed and catalogued material,
nothing called new; the Armstrong-Monroe cipher is named in the printed Madison Papers (PJM-SS 9) and its annotation.

Requests (all logged in `keyhunt/requests.log`): archive.org 31, catalog.archives.gov 4 (one whole-roll PDF, 91 MB),
founders.archives.gov 16 (headless Chromium), tile.loc.gov 84, www.loc.gov 2, archivesspace.bowdoin.edu 4 (Cloudflare),
digitalcollections.bowdoin.edu 5, digitalcollections.nypl.org 1 (bot check), web.archive.org 1 (reset), contact pages 6;
WebSearch 9, WebFetch 5. No logins, no credentials, no subagents; images read by this worker. Request drafts (not sent):
`outreach/armstrong-keyhunt-nypl.md`, `-nyhs.md`, `-fdr.md`, `-bowdoin.md`; ASKS rows 95-96 and notes on 84/85.

## ARM-KEYHUNT-2 (28 Sept 2026)

Parent worker ARM-KEYHUNT-2 (owner account, Opus), brief `.claude/briefs/runs/2026-09-28-parent-arm-keyhunt-2.md`,
17:18-17:4x UTC (container clock). Job: find a surviving 1805 specimen of the cipher Armstrong kept with Monroe (the
ARM-KEYHUNT lead above), screen it against the target, draft requests for what is not online. Files: `keyhunt2/`
(MANIFEST.tsv, requests.log, contact sheets). **Result: no specimen of the Armstrong-Monroe cipher and no key found
online; one correction to the lead's premise; one new request draft.**

**1. The Madison side.**
- Founders Online editorial notes (PJM-SS 9, re-read from `keyhunt/founders/r4.txt`, `r5.txt`): they **describe but do
  not print** the cipher numbers. 18 Mar 1805 n.1: the enclosed copy of Armstrong to Monroe 18 Mar 1805 is "3 pp.;
  partly in code; ... interlinearly decoded", with pencil notes "copies [...] as before stated" and "to be decyphered--
  the cypher being here that [of] Genl. A."; 2 Apr 1805 n.8: the corrected duplicate "has not been found"; n.12: a copy
  of Armstrong to Monroe 5 Apr 1805, "partially in code, interlinearly decoded by JM".
- **Correction to the lead's premise (H for the digits and the decode, I for what it implies).** The one surviving
  18 Mar 1805 copy -- NARA M34 roll 13 frames 0034 (right page, "(Copy) Paris March 18. 1805 Dear Sir") and 0035 (left
  page, coded lines with an interlinear period decode) -- is in the **office code THE=972**, not in a private cipher:
  60 of the 70 groups ARM-KEYHUNT read there are in Bourdeau's THE=972 table and decode to the Joseph Bonaparte passage
  PJM summarises ("Joseph had embarked with us and had carried up ... directly to the Emperor ... his interposition had
  hitherto been ineffectual ... I enclose a copy of a letter by which you will perceive the temper with which he
  undertook the business"), with plain words ("and", "a") between groups as in the office code's usage; the 5 Apr copy
  (frame 0058) likewise, 84 of 100. Frames 0028-0037 looked at at 1600 px (`keyhunt2/r13/`): there is only one copy of
  the 18 Mar letter on the roll. So the copy "in the cypher established between him and me" is **not in RG 59 as
  filmed**; the surviving copy is either the original re-enciphered or the corrected duplicate filed in its place
  (inference, I; PJM calls the duplicate not found). Where a specimen of the private cipher survives, if anywhere, is
  on Monroe's side (his received originals, 12 and 18 Mar, 1 and 5 Apr 1805, at Madrid).
- LOC James Madison Papers (loc.gov item search, "John Armstrong to James Madison" / "Armstrong to James Monroe" /
  "cipher Armstrong", dates 1804-1808): no item for 18 Mar or 2 Apr 1805 (both RCs are at NARA per PJM); Armstrong items
  there are 2 and 15 July 1804, 4 May 1806 (THE=972, Tomokiyo's known-plaintext letter) and 30 Aug 1808 (THE=972,
  already on file). Negative for the Madison side.

**2. The Monroe side.**
- LOC James Monroe Papers (mss33217; no whole-reel PDF exists, `resources[0].files` has jpeg/jp2/tiff per frame, so the
  h31/sheets.py route does not apply; contact sheets were built from pct:12 frames instead): reel 3 frames 589-625 not
  sampled by ARM-KEYHUNT (24 frames: Monroe's own long Madrid despatches, numbered pages, clear) and odd frames
  651-699 (25: mid-1805 to Jan 1806, incl. Bowdoin's enclosure list f0671, a claimant's "Private, Paris 24 Nov 1805"
  f0675 read at pct:50 -- clear, not Armstrong -- and the Jan 1806 run); reel 4 frames 5-447 every 13th (35: Jan-Dec
  1807). **No page of numerals and no key table in any of the 84 frames** (a negative for dense numeral pages at this
  scale only; a short coded passage inside prose would not show at pct:12). With H25 and ARM-KEYHUNT, every Armstrong
  letter to Monroe in the 1904 calendar has now been seen except the second Dec 1804 letter (still unlocated), and all
  seen are clear.
- NYPL Digital Collections (headless Chromium, which loaded this time): searches "James Monroe papers Armstrong",
  "Monroe Armstrong", "Monroe, James", "John Armstrong letter", "Armstrong cipher", "cypher" -- no MssCol 2035 item
  digitised; the Monroe/Armstrong hits are portraits, Emmet-collection Revolutionary letters and single items. The
  collection is not online; the ARM-KEYHUNT NYPL draft stands.

**3. Printed Monroe.** *Writings* (Hamilton) and the NYPL *Bulletin* 1900 were read by ARM-KEYHUNT (clear). *The Papers
of James Monroe* vol. 5 (1803-1811, Preston, 2014): Google Books NO_PAGES for every edition record (keyed API,
country=US), and the Rotunda digital edition is subscription -- not read (unreachable, not a negative). The UMW project's
online "calendar" is a biographical day-calendar, not a document calendar. American State Papers FR 2:636 prints only an
extract of the 18 Mar 1805 letter (Google Books snippet) -- no cipher numbers. Peter P. Hill, *Napoleon's Troublesome
Americans* (2005), snippet: Armstrong wrote "angrily to Monroe" when Bowdoin failed to use cipher in 1806 -- no specimen.
Google Books phrase search "cypher established between": only the Jefferson 1784-85 and Marshall-Pinckney 1797 uses.

**4. Specimen screen.** Nothing to screen: no Armstrong-Monroe cipher specimen found. (Frame 0035's THE=972 groups were
already screened by ARM-KEYHUNT: MISS, `keyhunt/screen_m34r13_1805.txt`.)

**5. Requests.** New: `outreach/armstrong-keyhunt-monroe-papers.md` -- to the Papers of James Monroe editors (UMW),
asking only where the recipient's copies of the four 1805 letters are and whether any Armstrong-Monroe cipher or key is
known in their document files (they calendar Monroe documents across repositories, the one finding aid that answers
the "where" question); ASKS row 97. Standing: the ARM-KEYHUNT NYPL draft (the likeliest holder), ASKS 95.

Requests (`keyhunt2/requests.log`): catalog.archives.gov IIIF 10, tile.loc.gov 87 (97 image requests of 120), www.loc.gov
5, digitalcollections.nypl.org 8 (browser), academics.umw.edu 3 (browser) + 1 curl (403), libraries.wm.edu 1, Google
Books API 12; WebSearch 1; project mailbox search 1. Vision screener calls: 0 (sheets read by this worker). No logins.
Status unchanged (`open`). Rule 10: nothing called new.

## ARM-MONROE-CAT (28 Sept 2026)

Parent worker ARM-MONROE-CAT (owner account, Opus), brief `.claude/briefs/runs/2026-09-28-parent-arm-monroe-cat.md`,
20:16-20:2x UTC (container clock). Job: query the Papers of James Monroe's public Monroe Catalogue Online (UMW; FileMaker
WebDirect at fms14.longtermsolutions.com, guest sign-in printed on
https://academics.umw.edu/jamesmonroepapers/search-the-letters/catalogue/) for Armstrong to/from Monroe 1804-1808, above all
12, 16/18 Mar and 1, 5 Apr 1805. **Result: not searched.** The catalogue page loaded (headless Chromium; it confirms ~38,000
entries with "repository location of the original") and the WebDirect sign-in screen was reached, but this session's
permission policy refused the sign-in step, and the worker did not try another route to it. No hit recorded;
`keyhunt/monroe_catalogue.tsv` holds a single not-searched row. This is an unrun step, not a negative: the catalogue may
well answer the draft's first question. Handed to the owner (ASKS 97): sign in as guest from the catalogue page, Quick
Find "Armstrong", restrict to 1804-1808 (or search author Armstrong / recipient Monroe), and note date, repository and
any cipher remark for 12, 18 Mar, 1, 5 Apr 1805 -- about five minutes in a browser. Or allow the sign-in for a cloud
worker and re-run this brief. `outreach/armstrong-keyhunt-monroe-papers.md` kept, held until that lookup is done.
Requests: academics.umw.edu 1, fms14.longtermsolutions.com 1 (`keyhunt/requests.log`). Rules 9 and 10: nothing named,
nothing claimed.

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/armstrong/NOTES.md ; TARGETS.md "Armstrong to Madison, 20 Feb 1808" ; README.md
- Their extent, in their words: 20 Feb 1808 letter: attempted, "adjudicated 2026-09-16: AFIO claim does not hold", unread; the separate 30 Aug 1808 postscript is their solved item (48 of 49 groups)
- Their date: 16 Sept 2026
- Note: already cited in our NOTES.md
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## Premise check (GF4-BATCH16, account-4, 3 Oct 2026)

Adversarial pass, asked to prove the 20 Feb 1808 letter already read. Standard edition: Papers of James Madison,
Secretary of State Series, via Founders Online 99-01-02-2728 (line 2 above; ARM-REC3 re-read the page, 26 Sept 2026:
"its own Early Access page carries no editorial note or footnote at all, only the bare source citation"). Not re-fetched
this pass (founders.archives.gov answers scripts with a CloudFront 202; the reads on file are via Wayback and headless
Chromium).

- (a) Decipherments the folder itself mentions: **found, rejected on file.** The AFIO claimed solution (Apelbaum, 27 May
  2025) is the only claimed reading; Bourdeau's matched control (`adjudicate_feb20.py`: 500 shuffled-ciphertext keys fit
  better than the AFIO key, 70%/41% vs 59%/30%) and Tomokiyo both reject it -- a control-backed negative, so not
  found-solved. Kreider's statement "we've found no evidence that it ever was decoded, nor that Madison acknowledged
  receiving it" stands; LOC's finding-aid abstract of Armstrong's letters jumps 4 May 1805 -> 30 Aug 1808 (ARM-REC).
  The 1805 "passages of inexplicable cypher" docket (ARM-KEYHUNT) is a different letter in the Armstrong-Monroe cipher,
  no decipherment printed (PJM-SS 9 notes describe the numbers, do not print them; ARM-KEYHUNT-2). No interlinear,
  docket decode or clear copy of the 20 Feb letter is recorded on frames 0029-0032 (ARM-IMG/ARM-TR/ARM-TR2).
- (b) Other solvers' working files: fresh clones 3 Oct 2026. dbourdeau/cyphersolver 841111b (2 Oct): `targets/armstrong/`
  holds `feb20_ciphertext.txt`, `afio_key.txt`, `adjudicate_feb20.py` and the THE=972 machinery (`decode972.py`,
  `additions972.tsv`, 160 new values); his NOTES says "The 20 Feb 1808 letter (369 groups) is a different code and
  stays out" and "the 20 Feb 1808 code is a different key" -- no rendering of the 20 Feb letter, no key run on it beyond
  the AFIO adjudication. Not found. One lead to hand on: his "Remaining gaps" lists "27/29 Dec 1807, 25 groups, including
  1701 and 1723 (values above 1600, as in the 20 Feb letter's code) ... The manuscript was not located on roll 13 or 14
  at grid scale" -- ARM-POOL2 (26 Sept) located a 27 Dec 1807 Duplicate on roll 13 frame 0390 and screened it 70% THE=972
  with period interlinear glosses; whether its >1600 groups overlap the 20 Feb letter's values was not tested by either
  side. aaymeloglu/unsolved-ciphers d2800bb (27 Sept): no Armstrong target or file. Not found.
- (c) Physical neighbours: **not found.** M34 roll 14 frames 0028-0034 viewed natively on file (ARM-IMG, ARM-POOL,
  ARM-TR2): 15 Feb (0024-25, faint pencil decodes in THE=972), 22 Feb (0033-0034), docket 0645; none carries a decode,
  clear copy or slip for the 20 Feb letter. No duplicate of 20 Feb located on rolls 13-14 (ARM-POOL, ARM-POOL2).
- (d) Recipient side: the recipient is Madison, whose edition (PJM-SS) is the standard edition above -- no decode. The
  forwarding side (Madison to Jefferson, Founders; ARM-JEF) and the other correspondents (Pinkney, Monroe, Erving,
  Livingston; ARM-REC3, ARM3-COR, ARM-LIV, ARM3-LIVCODE, ARM-KEYHUNT/-2) were read on file: no decode, no paraphrase of the
  20 Feb content. Not found. Unrun: the Monroe Catalogue Online lookup (ASKS 97, guest sign-in refused to a cloud worker).

Verdict unchanged: `open` (no printed or posted decipherment of this letter; the one claimed solution fails its control).

## While waiting (GF4-BATCH16, account-4, 3 Oct 2026)

Waits on the owner's Monroe Catalogue Online lookup (ASKS 97) for the Armstrong-Monroe cipher's 1805 specimens.
- Action that depends on nobody: screen M34 roll 13 frame 0390 (27 Dec 1807 Duplicate, already located by ARM-POOL2) for
  its groups above 1600 (Bourdeau lists 1701, 1723) and test their overlap with the 20 Feb 1808 letter's value set --
  a two-letter value-overlap count against random value sets of the same size drawn from the same numeric range
  (a reordering control could not differ, rule 3), no reading. S.
- H70 (ARM-A-H70, 3 Oct 2026): context crib sheet for the letter's probable content and its clear frame is in
  `crib_sources.md` "## H70 context crib sheet" (timeline, ranked cribs, formulas); scoring it is LANE-ARM-B's.

## Campaign step H67 (2026-10-03 05:32 UTC)

New outside material: Bourdeau's 2 Oct gap list (dbourdeau/cyphersolver 841111b, targets/armstrong/NOTES.md) puts groups 1701
and 1723, "values above 1600, as in the 20 Feb letter's code", in the 27 Dec 1807 letter. Fetched M34 roll 13 frame 0390 natively
(NARA IIIF v3, `.../M34-013/M34-013-0390.jpg`, 3936x3328; 2 requests; full frame not kept, folder over 30 MB already -- re-fetch from
that path; four band crops kept in h67/). The letter is the 27 Dec 1807 Duplicate in THE=972 (972 'the', 1001, 1105 ...) with period
pencil glosses over nearly every numeral line (e.g. "to go farther than any other person, dare not avow his opinion of it";
P.S. "there is no longer a doubt that the Emperor wished to get hold of the royal family of Portugal"). Two reads of every 12xx/17xx
group (runner's own read of the crops; one blind Sonnet subagent): h67/reads.tsv. Firm 17xx in both passes: 1717 (x2), 1716 (x2,
one glossed "of Aranjuez"); seven more are 12xx/17xx splits (the hand's 2 and 7 look alike). Bourdeau's 1723 was not seen as such
(nearest: 1725/1225). These values sit inside THE=972 usage, which already tops out near 1687 in the tables on file, so the
simplest reading is that THE=972 runs past 1700, not that this letter carries the target's code.

## Campaign step H68 (2026-10-03 05:32 UTC)

h68/overlap.py: overlap of f.0390's >1600 values with the target's 34 distinct values in 1601-1999, against 2,000 random sets of the
same size from 1601-1800 (an order shuffle could not differ, rule 3). Firm set {1716,1717}: overlap 1 (1716), null mean 0.22,
P(null>=obs) 0.207. Maximal set (every 17xx reading, 9 values): overlap 1, null mean 0.94, p99 3, P 0.648. **No overlap beyond
chance; H68 fails its gate (p99).** H69 (align the glosses as known plaintext onto the target) is not licensed and is dropped. A
by-product for whoever extends THE=972: f.0390 carries period glosses over 17xx groups (1716 'Aranjuez'?, 1717 in "and I wait",
"and abandoned"), i.e. THE=972 entries above the tables' current ceiling -- out of this target's scope.

## H71 catalogue retry (ARM-A-H71)

3 Oct 2026, 19:22-19:28 UTC (clock read). Worker ARM-A-H71 (account 1, LANE-ARM-A). H64's five catalogue reads (28 Sept)
retried once each, per host in order: plain curl with the descriptive UA; `tools/browser_fetch.js`; Wayback CDX + `if_`.
Saved pages: `sources/h71/` (HTML only).

| catalogue | curl | browser_fetch.js | Wayback | result |
|---|---|---|---|---|
| archives.nypl.org/mss/6743 (MssCol 6743) | 403 | Akamai "Access Denied" (301 B) | CDX reset (curl 35), twice; availability API on archive.org (200) says a capture exists: `web.archive.org/web/20260607012625/https://archives.nypl.org/mss/6743` | not opened |
| discover.hsp.org, 'Armstrong, John, 1758-1843' | 403 | Cloudflare "Just a moment..." | no capture of a search URL (availability API) | not opened |
| corsair.themorgan.org, same heading | 403 | Cloudflare "Attention Required!" | only the home page captured (2025-07-13) | not opened |
| researchworks.oclc.org/archivegrid/collection/data/81461497 (Livingston microfilm) | 403 | Cloudflare "Just a moment..." | no capture (availability API) | not opened |
| MHS ABIGAIL (balthazaar.masshist.org Voyager) | **200, opens** | -- | -- | **read** |

**MHS (new route).** The library catalogue (ABIGAIL) is the Voyager OPAC at `http://balthazaar.masshist.org/cgi-bin/Pwebrecon.cgi`
(linked from masshist.org; `abigail.masshist.org` gives a proxy 502). A plain keyword GET works without a session:
`?DB=local&Search_Arg=Armstrong+John+1758-1843&Search_Code=GKEY%5E*&CNT=50` (the name-heading browse works too, but its
title links are session-bound). Heading 'Armstrong, John, 1758-1843' carries 18 titles; the keyword search 26
(`sources/h71/mhs_abigail_titles.html`). Manuscripts among them:
- **James Bowdoin papers, 1804-1806, Ms. N-2059 (XT)**, 1 extra-tall vol.: copies of Bowdoin's correspondence as minister to
  Spain "and letters between other diplomats copied for his information", correspondents including Jefferson, Madison,
  Monroe, Dearborn, "John Armstrong, Charles Pinckney, and George William Erving"; written mostly from London and Paris
  (`sources/h71/mhs_abigail_bowdoin_search.html`). Not 1807-1808; a possible place for a copied Armstrong cipher letter or
  key 1804-1806 (the catalogue names no cipher). Not digitised per the record (no viewer link). Earlier work read
  Bowdoin's own letters at LOC/M31 (all clear, H-row table); this letterbook of copies was not on file.
- Henry Dearborn papers 1779-1838 and Jacob Brown papers 1812-1884 (multiple holdings, Armstrong as correspondent; war
  years, outside 1807-1808 as catalogued); three 1778 letters to Armstrong and one from him (Misc. Bd. 1778).
- Printed 1808 items (microform, Shaw/Shoemaker 16392 'Mr. Madison's letters to General Armstrong'; 'Papers relative to
  French affairs communicated by General Armstrong'; 'Further and still more important suppressed documents') -- printed
  State Department documents of 1808, already the target's crib-source family, not new material.
- The masshist.org collection-guide list (H64) still shows no Armstrong guide; ABIGAIL shows no 1807-1808 Armstrong
  manuscript, no retained copy or letterbook, and no cipher or key item 1804-1810 beyond the Bowdoin copy volume.

**Result.** One of five catalogues opened (MHS, through a different host than H64 used). No 1807-1808 Armstrong item,
retained copy or key located; one 1804-1806 copy volume naming Armstrong as correspondent (Bowdoin, Ms. N-2059). NYPL, HSP,
Morgan and ArchiveGrid stay on the owner's desk (L27 narrowed to those four plus the NYPL Wayback capture URL). No
challenge bypassed. No reading, no grade change. Search result, not a negative.

Host facts (for the parent to port to the CLAUDE.md host table):
- archives.nypl.org: 403 to curl, Akamai "Access Denied" to browser_fetch.js (3 Oct 2026, unchanged from 28 Sept); a Wayback capture exists but web.archive.org resets from the container.
- discover.hsp.org: 403 to curl, Cloudflare "Just a moment..." to browser_fetch.js (3 Oct 2026).
- corsair.themorgan.org: 403 to curl, Cloudflare "Attention Required!" to browser_fetch.js (3 Oct 2026).
- researchworks.oclc.org (ArchiveGrid): 403 to curl, Cloudflare "Just a moment..." to browser_fetch.js (3 Oct 2026).
- MHS ABIGAIL: `balthazaar.masshist.org/cgi-bin/Pwebrecon.cgi` Voyager keyword GET works by plain curl, descriptive UA (3 Oct 2026); `abigail.masshist.org` 502 through the proxy.
- web.archive.org: still TLS-reset from this container (curl 35, proxy logs "tunnel closed mid-exchange", 3 Oct 2026, 2 tries); `archive.org/wayback/available` answers 200 and names the capture URL, which a desk browser can open.

Requests: archives.nypl.org 2, discover.hsp.org 2, corsair.themorgan.org 2, researchworks.oclc.org 2, www.masshist.org 3,
balthazaar.masshist.org 5 (one a 403 from an empty URL of mine), abigail.masshist.org 1 (502), web.archive.org 2 (reset),
archive.org 4. Verdict unchanged: `open`; next step for this row: the owner's desk browser for L27 (four catalogues + Bowdoin
N-2059 contents at MHS reference if wanted).

## Step H74 (3 Oct 2026, 19:26-19:32 UTC, ARM-H74 for LANE-ARM-B)

H59's person-read pack rebuilt as a sign-sorter page (tools/sign_sorter.py), for the owner to settle the shorthand
alphabet by sorting tiles instead of typing a TSV. Offline build, no model read of any sign.

- Tiles: `h74/cut_tiles.py` (rule in its docstring: grey < 150 ink, 3x3 closing, 8-connected components, area >= 12,
  darkest pixel < 80, width < 25 pct and height < 85 pct of the crop, centre within 50 px of the line's row-ink peak)
  on the 28 shorthand-bearing lines of H58/H61's corrected mapping (page 2 by physical line: phys 2 = page2_L02,
  3 = page2_L04, 6 = page2_L06, 10 = page2_L11, 1/4/7/11/13 = h58/crops; page2_L01/L03/L07/L10/L13 and page1_L03
  left out). 997 tiles; count per line in `h74/lines.tsv` (22-66). Numerals are cut as well (several lines are mostly
  numerals); joins and splits are left as cut for the BAD-CUT pile. Overlays checked on p1L09 and p2L11.
- Starting piles: all '?'. Tomokiyo's 38-type labels could not seed any tile: h59/person_labels.tsv is still empty,
  and B35's pass files and Tomokiyo's glyphs.txt give type sequences per line with no x positions, so matching them to
  components would be a guess. In place of piles the page shows 24 provisional shape clusters (`--auto-clusters 24`,
  page-local, never written to an atlas).
- Check these first: the 22 tiles of page 3 line 13 (B35 crop 29, the readers' 94 pct disagreement line); the question
  names B35's commonest splits (Tomokiyo 29/35, 10/14, 35/48).
- Build: `python3 tools/sign_sorter.py --signs .../h74/signs.tsv --labels .../h74/labels.tsv --pages .../h74/pages.json
  --title "Armstrong 1808 shorthand" --lede ... --focus .../h74/focus.tsv --auto-clusters 24 --out .../h74/sorter.html
  --data-out .../h74/data.json` -> `h74/sorter.html` (4.0 MB) + `h74/data.json`; renders headless (browser_fetch.js
  --shot). Folder about 8 MB.
- Hand-off: not published here. The account-3 orchestrator publishes `h74/sorter.html` with capabilities {"db": {}},
  with `h59/person_pack/tomokiyo_38_types.png` as a supporting file (the lede points to it). After the owner sorts,
  export the db collections and run `tools/sign_sorter_apply.py --labels ciphers/armstrong-madison-1808/h74/labels.tsv
  --db DIR --out ciphers/armstrong-madison-1808/h74/settled_labels.tsv`; those settled labels (tile sid + box in
  signs.tsv) stand in for h59/person_labels.tsv as H60's known answer. ASKS row 92 updated in place.
- Not done: no reading, no statistic, no class change. Suggestion (not run): a lighter page with numeral tiles pre-piled
  if the owner finds the digits in the way, by excluding the numeral-group x-spans read from ciphertext_ms.txt.

## H72 finding-aid retry (ARM-A-H72)

3 Oct 2026, 19:22-19:35 UTC, ARM-A-H72 (account-1 worker for LANE-ARM-A, session_011LsfWjmjanzg358BoQzfKe). Brief
`.claude/briefs/runs/2026-10-03-acct1-arma-h72-cat.md`; retries H65/H66 and the cloud parts of H34 (ASKS 83-86). Search
result only: no reading, no class change, nothing graded. Saved pages under `sources/h72/`.

| Item | Routes tried (3 Oct 2026) | Result |
|---|---|---|
| (1) LOC George William Erving papers finding aid (ASKS 83) | findingaids.loc.gov/search?q=Erving via `tools/browser_fetch.js` (default, then `--wait 25000 --profile`); www.loc.gov JSON by curl (403 Cloudflare, one retry 403); loc.gov JSON via the browser: `q="Erving, George William"` (14 results) and `q=Erving` in the manuscripts facet (249 hits, first 100 read); ArchiveGrid via the browser; web.archive.org CDX | findingaids.loc.gov and ArchiveGrid: Cloudflare "Performing security verification" both times; web.archive.org: connection reset. loc.gov index: item-level Erving letters only (Jefferson, Madison, Jackson Papers; Erving to Madison 24 Mar 1807 "Partly in cipher", mjm014714, already used in H38) plus the Monroe and Cathcart EADs -- no collection or EAD record for the Erving papers. **Not reached; no container numbers; ASKS 83 stays as written.** New since H65: www.loc.gov itself now challenges plain curl (the host table says "yes, reliable" -- it answered the browser tool). |
| (2) NYHS John Armstrong papers (ASKS 84) | nyhistory.org/library/finding-aids, digitalcollections.nyhistory.org search (curl); findingaids.library.nyu.edu/nyhs/ plus four guessed slugs and `/livingston/` (curl); specialcollections.library.nyu.edu search (curl, then browser with 12 s wait) | nyhistory.org hosts 403; the NYU S3 host answers AccessDenied to every path including the root, so a real slug cannot be told from a missing one; specialcollections: CAPTCHA "Human Verification" to curl and browser. **Not reached; no box/folder; ASKS 84 stays as drafted (outreach/armstrong-keyhunt-nyhs.md).** |
| (3) FDR Library Rokeby / Aldrich family papers roll (ASKS 85) | fdrlibrary.org/finding-aids (200); the Hudson River manuscripts PDF re-fetched; NARA catalog via browser: "Aldrich Family Papers", "Rokeby Armstrong" | The finding-aids page lists no separate Aldrich/Rokeby aid, only the Hudson River Valley and Dutchess County manuscripts PDF -- byte-identical to H34's `h34/fdr_hudson.pdf` (sha256 700f74d4...e633), whose Appendix I pp.17-18 H34 already read. NARA catalog: 1 unrelated hit (Clinton speechwriting file) for the first, NRHP house files for the second. **No item list online; ASKS 85 stays as drafted.** |
| (4) Ericson and Haggerty 1980 Livingston reel guide, OCLC 7776177 (ASKS 86) | IA advancedsearch; be-api fts quoted phrase; HathiTrust bib API by OCLC; Google Books API (key, country=US) twice | IA 0; fts 116 hits, all citations of the guide in other books (e.g. `guidestoarchives0000dewi`), not the guide; HathiTrust `{"records": {}}`; Google Books 9 unrelated / 0 for intitle:Livingston inauthor:Ericson. **Still not online.** |

What this changes: nothing about the target; the four desk rows keep their text, each now carrying a dated 3 Oct line
naming exactly which route failed and how. The person's step is unchanged (a browser at the desk for ASKS 83, the two
drafted letters for 84/85, an ILL or the NYHS reading room for 86).

Requests per host: findingaids.loc.gov 2 (browser), www.loc.gov 2 curl (403) + 2 browser, researchworks.oclc.org 1
(browser), web.archive.org 1, findingaids.library.nyu.edu 6, specialcollections.library.nyu.edu 2, www.nyhistory.org 1,
digitalcollections.nyhistory.org 1, www.fdrlibrary.org 4, catalog.archives.gov 2 (browser), archive.org 1,
be-api.us.archive.org 1, catalog.hathitrust.org 1, www.googleapis.com 2. Vision calls 0.

Verdict (target stays `open`, 0/369 read): keep going on the lane's other rows; H72's own next step is the owner's
(ASKS 83-86), not a further cloud retry of the same hosts (rule 3's third-attempt clause: H34/H64-H66/H72 are the
third pass at these catalogues from the cloud; retired for the cloud routes, browser_fetch/curl/Wayback named).

## H76 French side (ARM-A-H76)

3 Oct 2026, 19:40-19:5x UTC, ARM-A-H76 (account-1 worker, LANE-ARM-A). Question: did Napoleon's ministry or the
cabinet noir intercept, copy or decipher Armstrong's 1808 dispatches? Scripts read, the worker read only the hits.
No decoding, no scoring, 0 vision. Texts fetched once to `sources/h76/` (IA djvu.txt).

**Answer: not found.** No printed source read this pass says Armstrong's dispatches (or any American legation
mail) were opened, copied or deciphered by the French. One nearby fact: the Paris police opened and examined
*inbound* private letters from the United States in April 1808 (below) -- mail to France, not Armstrong's outbound
dispatches.

| Family | Source and route | Queries | Result |
|---|---|---|---|
| (1) Napoleon's printed correspondence | *Correspondance de Napoleon Ier* vol. 16 (1 Sept 1807-mid Apr 1808; IA `correspondancede16napouoft`) and vol. 17 (Apr-Sept 1808; `correspondancede17napouoft`), djvu.txt grep | Armstrong; americ*; ministre d'Amerique / americain / des Etats-Unis; Etats-Unis; Floride(s); embargo; chiffr*; intercept*; decachet*; cabinet noir | Found: 4 instructions bearing on Armstrong Jan-Mar 1808 (No. 13446, 12 Jan; No. 13516, 2 Feb; No. 13545, 11 Feb; 31 Mar), copied to crib_sources.md "## H76". All of Napoleon's chiffre/intercept hits concern French army ciphers or intercepted Spanish/British mail -- none Armstrong or American. Not found: any order to open, copy or decipher American legation mail. Caveat: this 1858-69 edition is selective; the complete *Correspondance generale* (Fondation Napoleon, vol. 8, 1808) was not reachable this pass. |
| (1b) Fouche's police bulletins | Hauterive, *La police secrete du premier Empire* vols 3 (1806-07) and 4 (1808), IA `lapolicesecrte03hautuoft`, `...04hautuoft` | same set | Found (vol. 4): bulletin of 14 Apr 1808, item 294 "Lettres d'Amerique", with footnote "Examen de 4000 lettres expediees des Etats-Unis sur L'Osage": the police read the letters the *Osage* brought, noting all had been "decachetees, sans doute en Amerique, et recachetees". 31 Mar 1808: arrival of the *Osage* at Lorient "qui apporte des depeches a l'ambassadeur des Etats-Unis" (bearer named). 29 Apr: Armstrong forbids Lewis, commanding the *Osage*, to take passengers for England. 19 Jul / 27 Aug: Pinckney's dispatches to Armstrong by the *Saint-Michel*. 9 and 25 Feb 1808: Paris rumours on US-British relations. No bulletin says Armstrong's own dispatches were opened. |
| (2) Cabinet noir literature | Vaille, *Le Cabinet noir* (1950): not on IA (advancedsearch title/creator), no Google Books record (keyed, country=US). Herisson, *Le cabinet noir* (1887), IA `lecabinetnoirloi00hruoft`, grep | Armstrong; americ*; Etats-Unis | Vaille: unreachable (not a negative). Herisson: 0 hits for Armstrong or America. |
| (2b) Scholarship | OpenAlex (key), 4 queries (cabinet noir interception; Armstrong intercepted dispatches; Napoleonic postal espionage Lavalette; American diplomatic correspondence intercepted France 1808); Semantic Scholar 1 query; Google Books 9 queries incl. Hill, *Napoleon's Troublesome Americans* (2005) searched for intercepted / cabinet noir / decipher / cipher / opened | as listed | Nothing on French interception of US dispatches. One context item: *Bulletin de l'Institut francais de Washington* (1951, snippet, on David Bailie Warden): when Armstrong toured France in Aug 1808 the legation was left in Warden's care "except the opening of secret dispatches from the State Department" -- Armstrong kept the cipher work himself. Hill cites the AAE series as "AECP-EU" (snippet). |
| (3) Archive finding aids | archives.diplomatie.gouv.fr: proxy CONNECT 502 (000). francearchives.gouv.fr: HTTP 200 but a JavaScript redirect stub (`sources/h76/fa_*.html`), as the host table says -- logged, not retried. Archives nationales SIV: answers 200, app shell, not searched. Gallica SRU ("correspondance politique" + Etats-Unis + 1808): 30,220 noisy records, no AAE volume. Google Books: Bonnel, *La France, les Etats-Unis et la guerre de course* (1961) cites **AN AF IV 1192 (Secretairerie d'Etat)** for 1808 American shipping. | -- | Digitisation status: AAE Correspondance politique, Etats-Unis, the 1808 volume -- volume number not established this pass (Hill 2005 cites the series as AECP-EU); no online images found. AF IV 1192: no online images found. ASKS row appended for both. |

Requests this pass: archive.org 7 (2 advancedsearch, 5 djvu.txt), googleapis.com/books 13, api.openalex.org 4,
api.semanticscholar.org 1, francearchives.gouv.fr 3, archives.diplomatie.gouv.fr 1 (blocked), siv.archives-nationales 1,
gallica.bnf.fr 1. One at a time, >=1.5 s apart.

Next step (one line): the complete *Correspondance generale* vol. 8 (1808), and AAE CP Etats-Unis 1808 plus AN AF IV
1192 read on site or by copy order (ASKS row) for any copy of an American legation dispatch; until then the French-side
route has produced context cribs only, no intercept.

## H75 Bowdoin (ARM-A-H75)

Worker ARM-A-H75 (account 1, for LANE-ARM-A), 3 Oct 2026, 19:41-19:47 UTC (clock read). Brief
`.claude/briefs/runs/2026-10-03-acct1-arma-h75-bowdoin.md`. Builds on ARM-KEYHUNT item 3 (28 Sept 2026), which had
already read *The Bowdoin and Temple Papers* pt. II and screened its 512 printed cipher groups (MISS); not redone.
0 vision, 0 subagents.

**Editions.** IA advancedsearch (title:bowdoin, texts, 1800-1930) finds no edition of James Bowdoin III's letters
other than *The Bowdoin and Temple Papers* (pt. I = MHS Coll. 6th ser. 9, 1897, IA bowdointemplepap00bowdrich,
1756-1782, no Armstrong; pt. II = 7th ser. 6, 1907, IA collectionsofmas00mass_17). Pt. II full text fetched once to
`sources/h75/bt2_djvu.txt`.

**Every Armstrong-Bowdoin item printed in pt. II (14, plus joint addresses):** Armstrong to Bowdoin, Paris 22 July,
7 Aug, 14 Sept (two), 16 Sept, 25 Oct (two) 1806; 30 Aug (two), 11 Sept, 16 Sept 1807. Bowdoin to Armstrong 29 Oct
1806; [Aug-Sept] 1807; 14 Sept 1807. Joint: Gallatin to Armstrong and Bowdoin 18 Mar 1806; Madison to Armstrong and
Bowdoin 15 July 1807 (the editors: the duplicate original "is almost wholly in cipher"; the volume prints the
contemporary clear copy). Also Armstrong to the Prince of Benevento 12 June and 8 Aug 1807 (copies in Bowdoin's
papers). **The last item between them is 16 Sept 1807; the volume has no letter from Oct 1807 (Bowdoin at
Cherbourg, 26 Oct) to 29 May 1808** -- nothing printed covers Jan-Apr 1808.

**Numerals in Armstrong's hand: none printed.** Every Armstrong-authored letter in pt. II was scanned line by line
for runs of three or more 2-4 digit numbers: 0 runs. The one cipher passage *between the two* is Bowdoin to
Armstrong, Paris 29 Oct 1806 (pp. 347-348): 5 runs, 26 groups, with the editors' bracketed glosses ("your private
instructions", "those common to us both"). `sources/h75/numerals.tsv`. Already inside ARM-KEYHUNT's screen
(`keyhunt/bt_we028_check.tsv` lines 17243-17253: 3 of 4 runs MATCH WE028, "Mr Monroe's cypher"). Pool screen on
these 26 groups alone (`pool/cor/overlap_test.py`, unchanged; one OCR "13885" read as 1385): **candidate 0/26 shared
with the target's top-20; control 1 THE=972 pooled sample 1/81; control 2 random draws of N=26 over 1-1899: 0.0%
reach >=3 (mean 0.34) -- not a pool candidate.** Digit shape: units 0/1 among values >=100 0.136 (target 0.59),
values >1700 0.000 (target 0.092), values <100 0.154 (target 0.36), values 900-1099 1 of 26 (target: 4 digit tokens of
`ciphertext.txt`). WE028 itself was already scored on the target (HYPOTHESES.md, A2 table transfer: FAIL).

**What the volume adds about Armstrong's ciphers (cited, grade I where inferred):**
- 1805: Bowdoin to Erving, "General A. must therefore decypher it for you, & you can send it to me in Mr Monroe's
  cypher" -- Armstrong held the Department's Paris code in 1805 (consistent with H25/ARM-KEYHUNT).
- 22 July 1806: Armstrong, "Having no cypher in which I can write to Messrs Monroe & Pinckney" (ARM-KEYHUNT).
- **29 Oct 1806: Bowdoin writes to Armstrong in WE028 (Monroe's cypher)** -- so by October 1806 Armstrong could read
  WE028 (new to this folder's record; ARM-KEYHUNT screened the runs but did not note the recipient). WE028 does not
  fit the target (above), so this narrows rather than opens.
- 1807 (Bowdoin to Erving): Monroe wrote that "both you & I have written him in cyphers of which they have no
  copies" -- Armstrong was already, in 1807, sending Monroe cipher the recipient could not read; Bowdoin: "with the
  exception of a few lines in one of my letters to the President, I have used no cyphers". A second documented case
  of the 1805 / 1808 pattern (Armstrong writing in a cipher his correspondent lacks); grade I.

**Founders Online (headless, `h75/`): Bowdoin <-> Madison and Bowdoin <-> Jefferson, Jefferson Presidency.**
40 Bowdoin-Madison items, 1807-08 tail: Bowdoin to Madison 1 May, 25 July, 2 Oct 1807, then **19 April 1808 (Boston,
arrival note only)** -- no Bowdoin-to-Madison letter Nov 1807-Mar 1808 in Founders. Bowdoin to Jefferson: 24 Sept,
7 Nov 1807 (Cherbourg, embarking), 17 Feb 1808 (London, already screened clear, `pool/cor/`), 9 and 12 June, 18 July
1808 (Boston). None of the 1808 letters names Armstrong or a cipher (grep: 0). Bowdoin to Madison 2 Oct 1807 (Paris):
"I think it unnecessary to trouble you with the continuance of my correspondence with general Armstrong", and "I
shall leave such Papers as I have, belonging to the public ... in the hands of Mr. Skipwith, subject to Mr. Erving's
orders" -- Bowdoin's public papers, presumably including his cipher tables (WE028, "Mr Pinckney's cypher"; grade I),
stayed in Paris with Skipwith from Oct 1807. **So Bowdoin was out of Paris from late Oct 1807 and out of Europe
from mid-March 1808; he cannot report what Armstrong was writing in Feb 1808, and nothing he wrote does.**

**Where it was not found:** printed Bowdoin and Temple Papers pt. I-II; IA title search for any other Bowdoin III
edition; Founders Bowdoin-Madison (40) and Bowdoin-Jefferson (Jefferson Presidency) lists, 7 documents opened. Not
reachable (already logged by H71/ARM-KEYHUNT, not retried): MHS Ms. N-2059 (not digitised), Bowdoin College
letterbooks 1806-1811 (archivesspace Cloudflare; request draft `outreach/armstrong-keyhunt-bowdoin.md`). No new
ASKS/LOCAL-QUEUE row: both holdings already have their request on file, and nothing found here raises the chance
that either holds a numeral item from 1808 (Bowdoin left Paris before the target was written). Nothing graded,
nothing read on the target.

Next step this suggests (not run, suggestion only): Skipwith as custodian of Bowdoin's public papers and ciphers in
Paris from Oct 1807 -- whether Armstrong's office had Bowdoin's Madrid legation cipher ("Mr Pinckney's cypher",
Madison to Bowdoin 25 May 1807, four runs on file) at hand in Feb 1808; that cipher's 4 printed runs are already in
the MISS screen, so only a fuller specimen would test it.

Requests: archive.org 2 (advancedsearch 1, djvu.txt download 1); founders.archives.gov 14 (headless page loads, one at a time,
>=2 s apart); 0 challenges, 0 retries. Logs `sources/h75/requests.log`, `h75/requests.log`.

## Step H73 (3 Oct 2026, 19:27-19:48 UTC, worker ARM-H73 for LANE-ARM-B): vocabulary-prior solver -- control below gate, target not run

Intake gate, run before any work (`python3 tools/intake_gate_check.py armstrong-madison-1808`, exit 0):
```
armstrong-madison-1808: open (line 1) -- edition/page or full-text-search citation found within 6 lines
```
Pre-registration `h73/PREREGISTRATION.md`, committed and pushed (ac380695) before any control was built or solved.

**Instrument.** Tomokiyo's suggestion (a model reading the letter after learning a sibling code's vocabulary) as an
ORDER constraint: `tools/families/nomenclator.py --param vocab_order=1 prior=WE028|THE972` (offline test
`tools/tests/test_nomenclator.py::test_vocab_order`) assumes the book is one-part at decade level, so the target's
sorted decades must sit in the same order on one sibling's alphabetical whole-word list; particles are restricted
to the siblings' short-word entries that are en18 function words; the score is the en18 word-trigram LM. V2
(vocabulary only, no order) was judged before running to be ARM-C1's soft sibling prior with one knob turned, so it
was not run as a variant (prereg, same-instrument check); the unchanged ARM-C1 solver is the blind baseline.

**Matched control.** Bourdeau's THE=972 decodes of Armstrong's 15 and 22 Feb 1808 letters, with words rebuilt
from fragments by the pre-registered DP and unread groups as `*` (`h73/control_plain.txt`, 528 words), re-encoded
into a synthetic code of the target's design at N=369. The particle block is cold at 1-99. The book is the OTHER
sibling's whole-word list in alphabetical blocks of 6 per decade, with members on the target's slot order and
decades spread over 100-1999. Shape (`h73/controls.tsv`): C-A (book THE=972, prior WE028) has 369 coded tokens, 153
distinct, 83 singletons, 199 particle / 170 book tokens and a slot-0 share of 0.288 (target 0.388). 92.5% of its
book-list entries are in the prior, and 0.965 of its book tokens. C-B (book WE028, prior THE=972) has 158 distinct,
89 singletons, 34.7% list overlap and 0.931 token coverage. The seeds change only the code: the particle
permutation and the decade placement.

| control (h73/results.tsv) | seed | V1 blended / particle / book | ARM-C1 solver (blind baseline) blended / particle / book |
|---|---|---|---|
| C-A prior WE028 -> book THE=972 (gating) | 1 | 0.154 / 0.266 / 0.024 | 0.144 / 0.241 / 0.029 |
| C-A | 2 | 0.179 / 0.266 / 0.076 | 0.117 / 0.211 / 0.006 |
| C-A | 3 | 0.127 / 0.216 / 0.024 | 0.130 / 0.211 / 0.035 |
| **C-A mean** | | **0.153 (0.127-0.179); 0 of 3 seeds >= 0.6: GATE NOT MET** | 0.130 (0.117-0.144); headroom fine (not near ceiling) |
| C-A thinned to 0.75 token coverage (prereg: C-A coverage > 0.90) | 1 | 0.117 / 0.211 / 0.006 | - |
| C-B prior THE=972 -> book WE028 (leak-side, not gating) | 1 | 0.108 / 0.195 / 0.011 | - |

The 19:33 single-restart timing pilot (seed 1, 0.133) is kept in results.tsv labelled as such and is not in the gate.
V1 gains about 2 points over the blind solver, which is inside the baseline's own 2.7-point seed spread. The book
class, which carries the letter's content, reads 0.6-7.6%.

**Why (`h73/diag_fixedpoint.py` -> `diag_fixedpoint.tsv`, run after the gate and used for no tuning):** on every
control the en18 LM scores V1's own wrong decode 470-550 nats ABOVE the true plaintext (-2223 to -2253 against
-2777 on C-A; -2428 against -2702 on C-B). So the objective, not the search, rules out the reading at this N. This
is the same finding as ARM-C1's truth-start diagnostic, now with the order constraint and a 1,079-word sibling list
in place. Caveat: the control plaintext keeps THE=972's syllable fragments wherever the DP could not rebuild a word
(for example "ac ce mp t"). That lowers the truth's LM score, so the control is harder than a letter written in
whole words would be. ARM-C1's whole-word Jefferson control read 0.135 with the same objective, so the fragments do
not explain the failure.

**Verdict.** Untestable by this tool at N=369 (vocabulary prior with decade order, matched control 0.153 vs gate
0.6). Target not run, no decode and no judge line. This is the third attempt at the nomenclator objective on this
design (ARM-C1, H27, now H73), and every number moved the same way. Under rule 3's third-attempt clause the
next attempt needs new material: a second letter in this code, a key or a gloss. A further prior, order or
annealer setting is not a new attempt. Status stays `open`.
Found: nothing about the target. Not found: no reading. The instrument fails on its own matched control.
Files: `h73/` (PREREGISTRATION.md, run_h73.py, control_plain.txt, controls.tsv, results.tsv, battery_*.log, out/,
diag_fixedpoint.py/.tsv). No network requests, no vision calls.
