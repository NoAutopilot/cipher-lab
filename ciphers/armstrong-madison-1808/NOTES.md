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
