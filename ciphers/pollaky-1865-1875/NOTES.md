partial

blocked (intake-gate sense only, LANE B2 bPOL2, 25 Sept 2026, corrected from `open`) -- under the Pipeline
intake gate, the standard source for ads 3-4 of this target is the same newspaper issue as
ciphers/catokwacopa-1875 (The Standard, 8 and 20 May 1875), which has never been independently opened by
anyone in this repo from the original: the British Newspaper Archive and newspapers.com stay login-gated
from the cloud (LOCAL-QUEUE.tsv row L13 already queues this for catokwacopa-1875; the same gap applies
here). The images this target works from (`images/`) come from Schmeh's Cipherbrain post 29, itself
scans supplied by Tony Gaffney and Nicole Gluecklich, not BNA. Ads 1 (secret script, 1865) and ad 2
(digit code, 1871) do not depend on the newspaper issue and are open on their own account (no standard
edition to cite): Cipherbrain post 29 (sources/schmeh/posts/29-pollaky.html, read in full including its
8-comment thread, 25 Sept 2026) says Bryan Kesselman (Pollaky's biographer) read several hundred
surviving Pollaky letters and found no cipher key, and that "Pollaky seems to have used several different
ciphers, but none of the ciphertexts seems to be long enough to decipher it" -- Schmeh/Kesselman's
characterisation, not a search this worker ran. The post's comment thread carries one claimed reading
(comment #3, Hassan Boyouk, 18 March 2022, ad 2 only, an unsourced "solution" paragraph) that Klaus
Schmeh himself disputed in the next comment ("You think that the content of this ad is identical with
the one that was published in the clear a few weeks later? Why do you think that this is the case?")
and that no later comment or published source confirms -- not treated as a solve. Bourdeau's
cyphersolver (github.com/dbourdeau/cyphersolver, shallow clone, grepped for `pollaky` and `catokwacopa`,
deleted after, 25 Sept 2026) has no pollaky-named target; its separate `catokwacopa/` directory documents
the ads-3-4 cipher with community readings (Bosbach, Estes, Ernst, Krajčovič, 2018-2026) still
incomplete on several lines -- see ciphers/catokwacopa-1875/NOTES.md (status `partial`) for the full
account; not a full solve anywhere. Aymeloglu's unsolved-ciphers (shallow clone, grepped for the same two
terms, deleted after, 25 Sept 2026) has no pollaky or catokwacopa hit. This is an intake-gate correction
plus a check-solved pass, not new research: line-1 stays `partial` (ads 3-4 track catokwacopa-1875's own
partial state; ads 1-2 remain genuinely open with no key found).

# pollaky-1865-1875

Ignatius Pollaky cryptograms: four encrypted classified ads by the Victorian private detective, dated
1865-05-16, 1871-02-20, 1875-05-08 and 1875-05-20. Schmeh, Cipherbrain post 29 (sources/schmeh/posts/29-pollaky.html),
scans supplied by Tony Gaffney and Nicole Gluecklich. check-solved (this worker's minimal pass, above) found
no key or full solve anywhere for any of the four ads; the spec (specs/pollaky-1865-1875.json) records
Schmeh's own account that Bryan Kesselman (Pollaky's biographer) read several hundred surviving Pollaky
letters and found no cipher key, and that "Pollaky seems to have used several different ciphers, but none of
the ciphertexts seems to be long enough to decipher it" -- that is Schmeh/Kesselman's characterisation, not
a search this worker ran.

## This pass (25 Sept 2026, worker bPOL, LANE B2 breadth, cheap test 1 of specs/pollaky-1865-1875.json)

Fetched the four ad images named in the spec (host scienceblogs.de, 4 GET requests, browser User-Agent,
2 s apart, all HTTP 200) to `images/`, with `images/manifest.json` (URL, id, sha1, size per image).
Ran **one blind transcription pass** (this worker, no second pass, no subagent -- rule 2/brief). All
counts and readings below are **single pass** and not cross-checked; treat as draft.

`ciphertext.txt` holds the as-transcribed text of all four ads, with a sign table for ad 1's invented
symbols. `scripts/stats.py` reproduces the N/K/IC numbers below (`python3 ciphers/pollaky-1865-1875/scripts/stats.py`).

### Per-ad numbers (N = token count, K = distinct tokens, IC = index of coincidence)

| Ad | Date | Alphabet | N | K | IC | English-text control (same N, 3 seeds) | Uniform-random control (same K, N, 3 seeds) |
|---|---|---|---|---|---|---|---|
| 1 | 1865-05-16 | invented signs | 10 | 9 | 0.0222 | 0.0889 / 0.0222 / 0.0444 | 0.0889 / 0.1556 / 0.1333 |
| 2 | 1871-02-20 | digits (number code) | 36 groups | 35 | 0.0016 | n/a -- not a letter ad, no corpus control run (brief) | not run |
| 3 | 1875-05-08 | letters (jumbled pseudo-words) | 224 | 25 | 0.0636 | 0.0661 / 0.0613 / 0.0591 | 0.0402 / 0.0393 / 0.0397 |
| 4 | 1875-05-20 | letters (jumbled pseudo-words, plaintext tail excluded) | 221 | 22 | 0.0656 | 0.0657 / 0.0622 / 0.0593 | 0.0459 / 0.0456 / 0.0464 |

Ad 1's run is only 10 signs -- too short for the IC to mean anything on its own (the English- and
random-text controls at N=10 scatter across almost the same range as the ad itself). Ad 2 is a digit
code, not letters, so no letter-corpus control applies; its IC is near zero because almost every
multi-digit group is unique (35 of 36 groups occur once; "91" is the only repeat).

**Ads 3 and 4 are the informative result of this pass**: their IC (0.0636, 0.0656) sits right next to
the matched English-text control (0.0591-0.0661) and well above the matched uniform-random control
(0.0393-0.0464). That is the letter-frequency signature of a **transposition** cipher (the same letters
as ordinary English, rearranged), not a substitution -- a whole-text substitution cipher would not, in
general, reproduce English single-letter frequencies this closely. This is a cryptanalytic observation
from a single blind pass at N in the low 200s, not a decipherment, and grades M (uncertain) until a
second pass and an actual transposition test confirm it. Visually, several of the jumbled "words" in
ads 3 and 4 look plausibly anagram-like (e.g. ad 4's "Wtubtrfftrstendinhofsvmnr", 25 letters) rather than
random.

### Textual observations (not interpretation, just what is printed)

- **Ad 3's plaintext contains the word "Catokwacopa"** -- the same word that names the existing
  `ciphers/catokwacopa-1875/` target (a different newspaper per that target's own NOTES.md, and per
  this spec's `ciphertext_pending` note about the shared 8/20 May 1875 dates). Whether ad 3 here and the
  Catokwacopa target's ad are the same underlying message, share a masthead/signature convention, or are
  a coincidence is not established by this pass -- flagging the overlap for whoever next works either
  target, per this spec's own pre-existing flag.
- **Ad 4's own plaintext tail states it is the second half of ad 3**: "This will be intelligible if read
  in connection with my communication published in this column on the 8th inst." This is the sender's
  own words in the ad, not an inference by this worker. Both ads open "W." and both carry "138"/"A.P. 138"
  as a shared reference number.
- Ad 1's cipher run has one repeated sign (SIGN-01, positions 1 and 6 of 10) and a leading sign before
  the plaintext resumes ("SIGN-A", shaped like a vertical bar plus a two-dot colon) that could be a
  signature-initial code parallel to the plaintext "W." that opens ads 3/4 -- an observation worth
  testing, not established.

### Uncertain readings (single pass, mark M)

- Ad 3: "caselcluchozamet" -- last few letters uncertain (o/e/c ambiguous at this resolution), flagged
  `[?]` in ciphertext.txt.
- All jumbled pseudo-words in ads 3/4 are transcribed as printed on one pass; letter-by-letter accuracy
  has not been checked against a second pass (this brief runs test 1 only; a second transcription pass
  is test 2, not this worker's).

### Grades (rule 4)

All tokens in this pass are grade **S** at best (cryptanalytic observation, no key, no crib) or **M**
(uncertain single-pass reading, e.g. the ad3 `[?]`). No H, no C.

### Next test (not run by this worker; brief names test 1 only)

Spec's `cheap_tests_in_order[1]` (check ad 2 against period telegraph/commercial codebooks) and
`[2]` (cross-check ads 3-4 against Gaffney's "The Agony Column") are unrun. Given this pass's IC result,
a worth-adding fourth candidate test: try word-length-preserving transposition (each jumbled "word"
anagrammed within its own boundaries) against an English dictionary/crib for ads 3 and 4 -- the IC match
to English is the kind of signal that specifically motivates a transposition search over a substitution
search. Left as a suggestion in this NOTES.md per Usage rule 7, not run.

### Hosts / requests

scienceblogs.de: 4 GET requests (one per image), browser User-Agent, ~2 s apart, all HTTP 200, no
retries needed. No other hosts touched.

### Search log

No check-solved sweep run this pass (out of scope for a breadth worker; see intake-gate note above).
No archive/library lookups run this pass -- only the fetch named in the brief.

## Test 2 (25 Sept 2026, worker bPOL2, LANE B2, `cheap_tests_in_order[1]` of specs/pollaky-1865-1875.json)

Intake gate (see status block above) re-run and re-confirmed exit 0 before this pass started
(`python3 tools/intake_gate_check.py pollaky-1865-1875` -> `blocked (line 3) -- already terminal,
nothing to gate`).

**Second blind transcription pass, ads 3-4 only.** This worker had already read pass 1's ciphertext.txt
(contaminated for ads 3/4), so a fresh Sonnet subagent (one, per brief) transcribed ads 3-4 blind from
`images/ad3-1875-05-08.jpg` and `images/ad4-1875-05-20.jpg` alone, no other file, no web search, output
written to `scripts/pass_b.tsv` (its own ambiguity notes in `scripts/pass_b_notes.txt`). This worker
converted pass 1's ciphertext.txt into the same wide TSV format (`scripts/pass_a.tsv`, dashes normalised
to the single `–` character both Bourdeau's transcription and pass B already use, and the `[?]`
uncertain-token marker converted to reconcile_passes.py's trailing-`?` convention) and ran
`tools/reconcile_passes.py scripts/pass_a.tsv scripts/pass_b.tsv --out-dir scripts --rows`:

```
ad3   31 31 30 31 0.97
ad4   49 49 48 49 0.98
lines 2  signs A 80  B 80  agree 78/80 = 97.5%  (nw)
```

**Pass agreement: 78/80 tokens (97.5%).** Two disagreements (`scripts/disagreements.tsv`), both settled
by this worker directly on the image (rule 2, image over transcription):

| line | pass A (test 1) | pass B (this pass) | settled | how |
|---|---|---|---|---|
| ad3, token 13 | `caselcluchozamet?` (pass 1's own `[?]` flag) | `caselcluchozamot` | **caselcluchozamot** | read directly off `images/ad3-1875-05-08.jpg`: the word is "...3 caselcluchozamot. 1. 6. 9...", an `o` not an `e` |
| ad4, token 16 | `Ngtndusdendo` | `Ngtndusdcndo` | **Ngtndusdcndo** | read directly off `images/ad4-1875-05-20.jpg`: "Ngtndusdcndo. Edrstneirs.", a `c` not an `e` (low-resolution scan, lower confidence than the ad3 call but consistent letter shape) |

Both settled readings applied to `ciphertext.txt` (with an inline note dated 25 Sept 2026); this pass's
tokens grade **S** (cryptanalytic reconciliation against the image, no key) except the ad4 `Ngtndusdcndo`
call, graded **M** (uncertain -- lower-confidence image read, see table).

**Diff against Bourdeau/Ernst's catokwacopa transcription.** Shallow-cloned `github.com/dbourdeau/
cyphersolver` (MIT, cited; deleted after use, per rule 8 and the brief), read `catokwacopa/ads.py`:
Thomas Ernst's transcription checked against the British Newspaper Archive originals (klausschmeh blog
comments #24-25, 27 July 2018) -- a different, independently-sourced route to the same two ads (BNA
scan vs. this target's scienceblogs.de/Gaffney-Gluecklich scan). `scripts/diff_bourdeau.py` normalises
both sides to letter-only word tokens (strips dashes, digits, punctuation -- the two sources notate
those differently, e.g. Bourdeau's plain-text string drops the `–` this target's scan clearly shows
before "Hrsclam"; per CLAUDE.md's PX-BRODEC lesson, that is a notation difference, not a letter
disagreement, so it is excluded rather than counted) and diffs word by word:

```
ad3/AD1: 26 vs 26 letter-words, 0 differences
ad4/AD2: 46 vs 46 letter-words, 0 differences
TOTAL: 0 differences out of 72 letter-words (100.0% agreement)
```

**Target-vs-Bourdeau agreement: 72/72 letter-words (100%), after the two pass-A/B disagreements above
are settled toward pass B.** Bourdeau's ads.py independently confirms both settled readings
(`caselcluchozamot`, `Ngtndusdcndo`) letter-for-letter -- two unrelated transcription routes (this
target's scan, image-read twice, vs. Ernst's separately BNA-checked text) now agree completely on the
72 letters that make up ads 3-4's jumbled-word content. This raises confidence in `ciphertext.txt`'s ad
3/4 lines from single-pass (test 1) to two-pass-plus-independent-source; it is not itself a decipherment
(rule 4: still grade S/M, no H, no C -- Ernst's BNA-checked status is `published`-key-adjacent evidence
for the *ciphertext*, not a plaintext key) and does not change ad 3/4's link to `ciphers/catokwacopa-1875`
(status `partial`, mechanism agreed, unique plaintext not fully reconstructable per that target's own
NOTES.md) -- this pass strengthens the shared-ciphertext identification, it does not solve it.

No substitution or transposition solving run this pass (out of scope, per brief).

### Hosts / requests (test 2)

github.com: 2 shallow clones (`dbourdeau/cyphersolver`, `aaymeloglu/unsolved-ciphers`), both deleted
after grepping/reading, no other requests. No other host touched this pass.

### Grades (rule 4), test 2 only

caselcluchozamot: **S** (settled from image + independent source, no key). Ngtndusdcndo: **M**
(settled from image + independent source, but a lower-confidence low-resolution read). All other
ad3/4 tokens carried forward from test 1 unchanged, still S/M (no H, no C).

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
Read so far: 0 of 4 ads read in this repo. Ad 1 is 0/10 signs, ad 2 is 0/36 digit groups (36 counts "9:77314" as two groups; 35 if it is one), and ads 3-4 are 0/72 letter-words re-derived here (NOTES.md Test 1 table, Test 2 diff). There is no key, decode script, AUDIT.md or HYPOTHESES.md here, and nothing is graded. The ads 3-4 ciphertext is corroborated: two passes agree on 78/80 tokens, and the text matches Ernst's BNA-checked text 72/72. Their community readings are tracked in ciphers/catokwacopa-1875, which has its own gaps section (1 Oct 2026). Pollaky's authorship of ads 3-4 is Schmeh's attribution (post 29). The ads are signed "W.", not Pollaky, and this repo has not established the attribution.
- Ad 1 (16 May 1865): 10 invented signs inside a plaintext sentence - blocker: not-attempted; statistics cannot help at N=10 (K=9, SIGN-01 repeats at positions 1 and 6; IC 0.0222 falls inside both N=10 control scatters, NOTES.md Test 1). Two cheap internal steps are still untried. First, the signs are built from a few parts (dots, dashes, bars, one bracket pair; ciphertext.txt sign table), so a compositional design (part counts or positions to letters or numbers) can be tested directly. Second, the clear frame "...fortunately in time to [10 signs] shall return to England..." is a crib. Also, the on-disk image is a modern redrawing (clean vector signs, modern serif type, no paper texture; viewed 1 Oct 2026), not the newspaper page (rule 2), so sign details are conditional on the redrawer; next: run a component-decomposition plus frame-crib test, scoring the same rules on shuffled-sign and random-sign controls of N=10 and reporting both numbers; find the original newspaper and date through the print step, ~$2
- Ad 2 (20 Feb 1871): "TELEGRAM" number code, 36 digit groups - blocker: not-attempted; only an IC check has run (0.0016; 35 of 36 groups unique, NOTES.md Test 1). The spec's original codebook test (cheap test 2's earlier wording) was restated for ads 3-4 and never ran. Two community claims sit untested on disk in sources/schmeh/posts/29-pollaky.txt. Boyouk's candidate clear ad (comment #3: the full 74-word "ELOPED ... YOUNG LADY" text, so no fetch is needed to test it) is dated 1867 by Boyouk himself (#5), four years before the cipher. That makes it a weak candidate, and probably not the ad Schmeh means in #4 ("published in the clear a few weeks later"). Mulliss (#6) rejects it. Baertl's digit-sum frequency reading (#1, "NAMIM PLEARY FUND US...", with a 27 changed to 26) has never been checked against a control; next: (a) test Boyouk's 74 words against the 36 groups (word and letter counts, order-preserving bracketing), beside a matched control: an unrelated period ad of the same length run through the same test. (b) Score Baertl's digit-sum rule on synthetic same-shape digit strings. (c) Find the clear ad "a few weeks later" in the 2014-12-27 list (siblings step), then grep IA djvu text of pre-1871 telegraph and commercial codebooks for the group structure (the Lima-1916 pattern), with a synthetic control of the same N, ~$4
- Ads 3-4 (8 and 20 May 1875, The Standard): line-pair reading of the 72 letter-words, including Bourdeau's unforced lines 9, 12, 23, 26 and 29 - blocker: not-attempted; there is no script re-derivation (rule 7) or per-token grade (rule 4) here. NOTES.md Test 2 says "No substitution or transposition solving run". The classifier called the five lines open-codes, but ciphers/catokwacopa-1875/NOTES.md "Remaining gaps" (1 Oct 2026) classes them as not-attempted. Bourdeau's line-29 Latin search had only a positive control and no matched uniqueness control, so "the omission rule fits almost anything" is untested and the lines are not yet open-codes. The work lives in that folder, so it is not duplicated here; next: run catokwacopa-1875's own cheapest step. Copy this folder's reconciled ads 3-4 text there with attribution, segment it into Ernst's [1]-[28]+[10a] pairs, snapshot Bourdeau's catokwacopa/ folder, re-run the pairing permutation test, then its tests 2-3 with a synthetic-line control. Leave a one-line pointer here. The merge of the two folders is a decision for the orchestrator, ~$2
- Ads 3-4 ciphertext against the original Standard issues of 8 and 20 May 1875 - blocker: waiting-on LOCAL-QUEUE.tsv row L13 (BNA re-check, owner's desk runner, filed under catokwacopa-1875); this blocks nothing above, because the two scans already agree 72/72 (NOTES.md Test 2)

## Escalation (1 Oct 2026)
- [ ] siblings: Partly done: ads 3-4 are the Catokwacopa ads (NOTES.md Test 2, 72/72 against Ernst's text in Bourdeau's catokwacopa/ads.py). Never opened: (1) Schmeh's list of the twelve Pollaky ads in Palmer/Gaffney's The Agony Column (Cipherbrain post of 27 Dec 2014, linked from post 29 line 158). (2) The 4 Oct 2016 "Sherlock Holmes and the Pollaky cryptograms" post and its comments. (3) The "two more encrypted Pollaky ads that might have been solved by Thomas Ernst" (post 29 line 165). (4) The 27 March 1875 W. ad that Ernst names (sources/schmeh/posts/08-catokwakopa.txt, comment #2), which may be one of those two. sources/schmeh/manifest.tsv holds only post 29 for Pollaky. Planned: fetch both Pollaky posts and their comments from scienceblogs.de (4 requests or fewer, 1.5 s apart). Run it in the same job as catokwacopa-1875's 2015/2018 thread fetch, which hits the same host. List every Pollaky ad by date and system, looking for a second ad in ad 1's script or ad 2's number code, and for the clear ad Schmeh dates "a few weeks" after 20 Feb 1871, ~$2
- [ ] clear-pages: Used: ad 4's plaintext tail, which ties it to ad 3. Not used: ad 1's clear frame as a crib (gap 1), and ad 2's clear tail ("Pollaky, Private Inquiry Office, 13 Paddington Green"), which shows only that the signature is outside the code. Never tested: Boyouk's candidate clear ad, already on disk in comment #3 but dated 1867 by Boyouk (#5), four years before the cipher. Planned: the gap 2 (a) and gap 1 crib tests, each with its matched control. Then test whichever clear ad the siblings fetch dates to weeks after 20 Feb 1871, ~$3
- [ ] known-keys: Mechanical sweep done: KEY-CROSSMATCH.tsv has 45 pollaky rows with 0 matches (28 none, 9 unusable-key, 8 no_corpus). All of those keys are diplomatic keys of 1446-1781 or 20th-century keys, so the era is wrong. KEY-DESIGN-PRIORS.tsv row 81 gives only a letter-for-letter design prior. KEY-OFFICES.tsv and KEY-DESIGN.tsv have no Pollaky row, and Kesselman found no code in several hundred surviving letters (post 29). Never run: period telegraph, commercial and dictionary codebooks for ad 2. Planned: grep IA djvu text of pre-1871 codebooks for ad 2's group structure, with a synthetic control of the same N, ~$3
- [ ] print: Never searched: Palmer/Gaffney's The Agony Column (spec cheap test 3, unrun) and Kesselman's Pollaky biography. Either may hold a reading, or name the original newspaper and date for ads 1-2 (needed to replace ad 1's redrawing). Planned: Google Books API (GOOGLE_BOOKS_KEY plus country=US) and IA be-api full-text queries for "Pollaky" with "telegram", "cipher" or "secret" in both books, ~$2
- [n/a] key-rebuild: no key, partial key or reading exists here for any of the four ads (0 tokens read), so there is nothing to extend. The ads 3-4 vocabulary and forced-fit searches are catokwacopa-1875's key-rebuild step (its own escalation, marked [ ] there), not this folder's.
- [ ] image-check: Ads 3-4 done: two blind passes agree 78/80, both disagreements were settled on the image, and the text matches Ernst's BNA-checked version 72/72 (NOTES.md Test 2). Ads 1-2 have had a single pass only (NOTES.md Test 1). Ad 1's image is a modern redrawing, not a scan (viewed 1 Oct 2026). Ad 2's image is a newspaper clipping, and its "9:77314" colon and the lone "." after "437." need a second read to decide whether they are glued or split groups. Planned: one blind subagent pass on each of ads 1 and 2 plus a reconciliation, 3 calls at about $1.5 each. The original pages need a LOCAL-QUEUE row once the print step names the newspaper, ~$4.5
- [n/a] retry: no key exists for any ad, so there are no unread groups to rerun with an extended key. This step becomes due once the ad 2 clear-ad or codebook test, ad 1's crib or component test, or a sibling in either script yields a key.
Verdict: keep going: 3 internal gaps; cheapest next: fetch the 27 Dec 2014 and 4 Oct 2016 Pollaky posts with comments from scienceblogs.de (4 requests or fewer, combined with catokwacopa-1875's thread fetch on the same host), list every Pollaky ad by date and system, and find the clear ad dated weeks after 20 Feb 1871 for the ad 2 test, ~$2
