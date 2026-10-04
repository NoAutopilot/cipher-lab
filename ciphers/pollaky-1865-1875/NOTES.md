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

## GAPS-pollaky-1865-1875 (2 Oct 2026, account-4)

The Verdict step of the 1 Oct 2026 section: fetch Schmeh's Pollaky posts with their comments, list every Pollaky ad
by date and system, and find the clear ad he dates "a few weeks" after 20 Feb 1871. Snapshots (unmodified, 4
requests to scienceblogs.de, 2.2 s apart, all HTTP 200, 0 vision calls): `sources/schmeh/posts/29a-pollaky-2014-12-27.*`
(part 1, 10 comments), `29c-pollaky-2015-01-06-teil2.*` (part 2, found through part 1's "the rest in two days" and the
2016 post's link; 10 comments), `29b-pollaky-2016-10-04.*` and `29b-pollaky-2016-10-04-all.*` (the 4 Oct 2016 post,
paginated and on one page; 1 comment). Manifest rows in `sources/schmeh/manifest.tsv`.

**The twelve Pollaky ads in Palmer/Gaffney's The Agony Column, as Schmeh lists them (parts 1 and 2):**

| # | Date | System | Text or note |
|---|---|---|---|
| 1 | 1862-01-31 | clear | PRIVATE CONTINENTAL INQUIRY OFFICE ... 14 George-street |
| 2 | 1862-03-08 | clear | MR. I.G. POLLAKY ... in daily attendance |
| 3 | 1864-07-25 | digit groups, "A.D." | 209.179.211.181.214.19.512-248.206.1163.861. 81165.1166. - 864-80905- (Sydon, Syria-); 15 groups, 50 digits |
| 4 | 1865-05-16 | invented signs (our ad 1) | the "Your telegram was duly forwarded" ad; part 1 gives an image only |
| 5 | 1865-05-24 | digit groups, "S.F." | 5634 (347.'0563) 574,0 - 9865 - 9005,1053 - 21753, 4175, 0,00'175,86 (54732) 8630'275 _ _ going southward on the 26th inst.; 17 groups, 56 digits |
| 6 | 1867-06-03 | clear | ELOPED ... a YOUNG LADY 17 years of age (Boyouk's candidate for ad 2) |
| 7 | 1867-08-21 | clear | S-SARDANA'PALUS ALL AFLY - use cipher marked "No. 4 reserve" A secret possessed by more than two is a secret no longer |
| 8 | 1868-10-08 | clear | Marquise - pass the Elm in Second Avenue on Friday, the 9th inst. |
| 9 | 1869-02-23 | clear, open code | MIDNIGHT VISITOR - Turkeys are in gangs - Eagles fly alone (comment #1, part 2: a Dumas phrase, The Countess de Charny) |
| 10 | 1869-07-06 | clear | I am not a medium for introductions; rather the other way - for separations |
| 11 | 1869-10-01 | clear | "XANTIPPE" Although possessing a thorough knowledge of eight languages I cannot deduct sense from your epistle |
| 12 | 1871-02-20 | digit groups (our ad 2) | TELEGRAM. - 56. 717. ... 150.; 36 groups, 114 digits |

Ads 3-4 of this folder (8 and 20 May 1875, signed "W.") are not among the twelve: Schmeh's list is of ads "signed by
Ignatius Pollaky". The 4 Oct 2016 post nevertheless counts them among "the Pollaky ads listed in Tony's book" that
are encrypted and shows their scans beside ads 1 and 2; the 2017 post 29 says only "some of the Pollaky ads listed
in Tony's book are encrypted". So the attribution of the W. ads to Pollaky rests on the 2016 sentence (and whatever
The Agony Column itself says, unread here, Escalation "print"), not on a signature or on the twelve-ad list.

**Findings against the step's three questions**

1. *Clear ad "a few weeks" after 20 Feb 1871:* not found. The telegram ad is the last of the twelve; no ad of any
   kind after 20 Feb 1871 appears in either part or in the 2016 post, and the only "clear" ad in the
   27 Dec 2014 list that Boyouk's comment points to is no. 6 (3 June 1867). Schmeh's question in post 29 comment #4
   ("the one that was published in the clear a few weeks later") names no date and no text, and his own list
   carries no such ad. Searched: all three posts' bodies and all 21 comments, by date and by the phrase. Not
   searched: The Agony Column itself (print step) and the Times for March-April 1871 (needs a Times Digital
   Archive login, part 2 comment #2 says the same; no LOCAL-QUEUE row filed, since no ad text to look for exists
   yet). Gap 2's test (a) therefore has one candidate clear ad only, Boyouk's 1867 one, already on disk.
2. *A second ad in ad 1's script:* none. Ad 4 (1865-05-16) is the only sign-script ad among the twelve. New on
   the ad: comment #4 (Laura, 25 Aug 2016, part 1) proposes a compositional rule, bars = 1-3 as a row and dots =
   1-6 as a column (1 bar 1 dot = a ... 3 bars 6 dots = r, bracketed 1-3 dots = s t u, ignoring arrangement), and
   reads the ten signs B E N D A B U C H P, glossed "bend a buc[k], HP [initials]". Her own reading is not an
   English clause in the frame "fortunately in time to ___ shall return to England"; it is an untested community
   reading (rule 10: a claim on a blog, no control), and exactly the "compositional design" gap 1 planned to test.
   It becomes the pre-registered candidate rule for that test.
3. *A second ad in ad 2's number code:* two candidates, nos. 3 and 5 (25 July 1864 and 24 May 1865), both digit
   groups signed Pollaky at 13 Paddington Green, both only as Gaffney's printed text (part 1 gives no image of
   either). These are the "two more encrypted Pollaky ads that might have been solved by Thomas Ernst" of post 29.
   Ernst's comments #5-#10 (7-8 Oct 2016, part 1) read both as a shared homophonic bigram substitution over the
   whole digit string, ignoring the printed group boundaries: no. 5 = "ALL GAME DEBT HOPE PAY TO YOU TODAY"
   (revised in #8 after "Thomas" #7 caught 00 = T and E), no. 3 = "ONCE THEY HAVEN'T DEBTS THEN DO", with his own
   caveats (#9-#10: 41 and 65 do not mesh across the two, "my deciphering of the '64 may require some tweaking",
   "4 Polybios a 5, or one 10 x 10", and of the telegram "may not be of the same built, but probably is of the same
   make"). Nobody on the thread confirms or refutes either reading; they are community claims, grade none,
   untested by any control. Checked here: the digit totals of nos. 3, 5 and 12 are 50, 56 and 114, all even
   (chance 1/8 jointly; consistent with a bigram design, evidence of nothing on its own). Ad 2's group lengths
   (1-6 digits, 36 groups) differ from nos. 3 and 5 (3-5 digits, 15 and 17 groups), which is Ernst's "same make,
   different build" remark in numbers.

**A second witness for ad 2's text.** Part 2 prints Gaffney's transcription of the telegram ad from the original.
Diffed group by group against this folder's image read (ciphertext.txt AD 2): 36/36 groups identical, including
the "9:77314" colon, the lone "." after "437.", and the two missing periods after "447" and "91". So the colon and
the lone dot are in the printed original too (Gaffney read them the same way), not artefacts of our clipping; the
image-check gap for ad 2 is narrowed to whether the original typesetting meant them as separators. Not a
transcription of ads 1, 3 or 4: part 1 gives ad 1 as an image only, and the W. ads are not printed in these posts.

**Other facts from the threads.** Kesselman (Pollaky's biographer, 6 Oct 2016, 2016 post comment #1): Pollaky
destroyed his records, "there are 100s of Times ads by him - many in code", "he evidently used many different
codes"; his letters survive in archives in England and America. Ad 7's clear text, "use cipher marked 'No. 4
reserve'", shows numbered cipher systems in use in 1867. Part 2 comments #2-#10 are readings of the clear ads
(Xanthippe, Sardanapalus, a jealousy drama); #3-#6 are a methodological exchange (Schmeh: a solution needs a
plausible mapping, such as a codebook). No comment on any of the three threads carries a decipherment of ad 1
or ad 2 beyond the Laura, Baertl, Boyouk and Ernst claims recorded here and in the 1 Oct section.

Status stays `partial`. Nothing read; 0 of 4 ads read here; 0 tokens graded. Hosts: scienceblogs.de 4 requests.

## GAPS156-pollaky-1865-1875 (3 Oct 2026, account-4): bigram design prior on ad 2

### Pre-registration (written and committed 3 Oct 2026 15:41 UTC, commit dca24eee, before any score was computed)

Step: Verdict gap 2 (a). Texts: ad 2 (114 digits, ciphertext.txt AD 2 with every non-digit dropped), the
25 July 1864 sibling (50 digits) and the 24 May 1865 sibling (56 digits), both as Gaffney's print in Schmeh part 1
(GAPS table above). Script: `scripts/bigram_prior.py` (seeded, deterministic).

- Split each digit string into non-overlapping bigrams from position 0 (Ernst ignores the printed group
  boundaries, so do we). Primary statistic: **bigram IC** = sum n(n-1) / (N(N-1)) over the N bigrams.
  Secondary: **repeat count** R = N - distinct bigrams. Phase-1 split (drop the first digit) reported, not gated.
- Null: 200 uniform random digit strings of the text's own length. Positive control (rule 3, same N, same
  design): 20 synthetic 10x10 homophonic encipherments of English letter text of the same bigram count, in two
  allocation variants -- (A) frequency-proportional (each letter gets max(1, round(100 x English frequency))
  codes, trimmed/padded to exactly 100; a well-built homophonic) and (B) random allocation (100 codes dealt to
  26 letters, at least 1 each, uniformly); homophone chosen uniformly per letter. Plaintext: random letter-only
  windows from `tools/data` en sources (pg1661 Holmes, pg76 Huck Finn, pg1342 Pride, pg64317 Gatsby;
  Moby-Dick left out as the register outlier of tools/data/en/README.md). Power is also estimated on 1,000
  synthetic texts per variant so the 20 are not the only estimate.
- Axis check: the statistic (bigram repeat structure) can differ between null and control by construction --
  a homophonic of English repeats bigrams more than uniform digits unless the allocation fully flattens it.
- **Decision rule.** For each text and variant: power = share of synthetic texts whose bigram IC exceeds the
  null's 95th percentile. (1) If power < 0.80 for variant A, the statistic cannot detect a well-built 10x10
  homophonic at this N: the test is a **non-test** for that design, logged "untestable by bigram IC at N=57"
  (not a negative, not a positive), whatever the target scores. (2) If power >= 0.80: target IC above the null
  p95 = "consistent with a bigram design" (an S-level observation, no reading, no token graded); target IC at
  or below the null median = "no bigram repeat signal; evidence against a frequency-skewed bigram design at
  this N"; between = inconclusive. (3) The siblings are scored the same way at their own N (25 and 28 bigrams)
  as Ernst's claimed positives: if they too fail to clear the null where power >= 0.80, Ernst's readings carry
  no support from this statistic. No reading is attempted; rule 4 grades only if a token is read (none will be).
- The en corpus here only supplies synthetic plaintext, it is not a judge; the en fold caveat
  (tools/data/en/README.md: per-file spread 0.44-0.64, unknown reliability as a judge) is reported anyway, and
  the per-source spread of synthetic power is printed so a source effect would show.

### Results (3 Oct 2026, `python3 ciphers/pollaky-1865-1875/scripts/bigram_prior.py`, seed 156, writes scripts/bigram_prior.tsv)

| text | digits / bigrams | bigram IC (R) | null p50 / p95 (200 random) | null P(IC >= target) | control A power (20 / 1000) | control B power (20 / 1000) |
|---|---|---|---|---|---|---|
| ad 2, 1871 | 114 / 57 | 0.0138 (17) | 0.0100 / 0.0144 | 0.085 | 0.05 / 0.053 | 0.70 / 0.869 |
| sibling 1864 | 50 / 25 | 0.0267 (5) | 0.0100 / 0.0200 | 0.010 | 0.00 / 0.030 | 0.20 / 0.345 |
| sibling 1865 | 56 / 28 | 0.0185 (6) | 0.0106 / 0.0185 | 0.125 | 0.05 / 0.048 | 0.50 / 0.440 |

Control mean bigram IC: A 0.0098-0.0104, B 0.0196-0.0206. Phase-1 split (not gated): ad 2 IC 0.0123 (R 14),
1864 0.0181, 1865 0.0142. Per-source power on ad 2, variant B: holmes 0.90, huckfinn 0.86, pride 0.86, gatsby 0.85
(variant A 0.03-0.07): no source effect, so the en fold caveat (tools/data/en/README.md, unknown reliability as a
judge) does not bear on this result; the corpus only supplied synthetic plaintext.

**Reading against the pre-registered rule.**
1. Variant A (frequency-proportional 10x10 homophonic, the well-built design): power 0.053 at N=57, 0.03-0.05 at
   N=25-28 -- a proportional allocation flattens bigram frequencies to the uniform null's (mean IC 0.0104 vs null
   median 0.0100). **Non-test: "untestable by bigram IC at N=57" for this design**, not a negative. The statistic
   can vary on this axis (variant B shows it does), so this is a power failure at this design, not a
   construction-identical control.
2. Variant B (random allocation, frequency-skewed): power 0.869 >= 0.80 on ad 2. Ad 2's IC 0.0138 sits between the
   null median (0.0100) and p95 (0.0144), null tail 0.085: **inconclusive** -- neither consistent with a skewed bigram
   design (would need > p95, which 87 pct of controls reach) nor evidence against it (would need <= median).
3. Siblings (Ernst's claimed positives): power below 0.80 for both variants at N=25 and 28, so neither licenses
   anything under the rule. Reported as an observation only: the 1864 text's IC 0.0267 is above its null p95
   (tail 0.010), the 1865 text exactly at p95 (tail 0.125); the 1864 repeats come partly from the printed
   "1163 / 81165 / 1166" groups, which may be a numbering structure rather than a cipher property. Ernst's
   readings get no support and no refutation from this statistic.

Rule 4: no token read, none graded. Rule 10: nothing here is a reading of any kind. Requests: 0 external hosts, 0
vision calls, 0 subagents. The bigram-IC instrument is now spent on ad 2 for design A at this N; a further tuning of
the same statistic (other phases, other allocations) would be rule 3's third-attempt shape and is not proposed.

## GAPS160-pollaky-1865-1875 (3 Oct 2026, account-4): gap 1 component test, Laura's rule on ad 1

**Pre-registration (written and committed before any scoring, 3 Oct 2026, about 16:00 UTC).**
Candidate rule (Laura, part 1 comment #4, 25 Aug 2016, sources/schmeh/posts/29a-pollaky-2014-12-27.txt line 262):
count the bars/dashes S and dots P of each sign regardless of arrangement; letter = alphabet[(S-1)*6 + P - 1] for
S=1..3, P=1..6 (a..r); a sign of k dots in parentheses = s, t, u for k = 1, 2, 3. Applied to this repo's sign table
(ciphertext.txt, single pass on a modern redrawing) the part counts are: 01 (1S,2P), 02 (1S,5P), 03 (3S,2P), 04 (1S,3P),
05 (1S,1P), 01, 07 (paren,3P), 08 (1S,3P), 09 (2S,2P), 10 (3S,4P). Laura reads sign 04 as four dots (D), our table as
three (C); both strings are scored, ours as the primary target, hers as a variant; the disagreement is a transcription
question for the image (not settled here: script only).
Statistic T (primary, crib-bearing): mean add-one-smoothed English letter-bigram log10 probability over the string
"timeto" + X + "shall" (the clear frame on both sides, so junction bigrams carry the crib), X the 10 decoded letters.
Bigram model from the four English sources scripts/bigram_prior.py uses. Statistic W (secondary): fraction of X's
letters covered by the best segmentation into corpus words (count >= 5; length >= 2, plus "a" and "i"), uncovered
letters allowed. Seed 160.
Controls, all N=10 under the same rule: (A) shuffled-sign: 2000 random orderings of the target's own 10 signs (same
letter multiset, order varies, so T and W can differ from the target by construction); (B) random-sign: 2000 strings
of 10 signs with (S,P) drawn uniformly from the rule's 21 cells; (C) rule-family (forking paths): the target's signs
under 104 sibling rules of the same component-count design (S-major or P-major cell order, forward or reversed
alphabet, 26 cyclic shifts) -- Laura's rule is one of them; report its rank. Positive control (power, ceiling check):
2000 random 10-letter windows of the corpus restricted to the encodable letters a-u, encoded to signs and decoded by
the rule (identity), scored by T and W; power = share above control B's p95. If power < 0.5 the test is "untestable at
N=10" (rule 3), not a negative; if control B's own p95 already equals the positive control's median the statistic
has no headroom and the same applies.
Decision: the rule is "supported (S-grade candidate)" only if the target T exceeds the p95 of both A and B AND ranks in
the top 5% of C AND power >= 0.5; "inconclusive" if power >= 0.5 and it fails any of the three; "untestable" if power
< 0.5. No token is graded above M unless supported; S needs two words (rule 4).

**Result (scored after the pre-registration commit 577aeea6; script scripts/laura_rule.py, output scripts/laura_rule.tsv,
seed 160, 0 vision, 0 subagents, 0 external requests).**

| string | X | T | A p95 (tail) | B p95 (tail) | C rank of 104 | W | W: A p95 / B p95 |
|---|---|---|---|---|---|---|---|
| target, our sign table | bencabuchp | -1.1405 | -1.2895 (0.002) | -1.2026 (0.019) | 1 | 0.6 | 0.5 / 0.6 |
| variant, Laura's sign 04 | bendabuchp | -1.1074 | -1.2555 (0.001) | -1.2045 (0.005) | 1 | 0.5 | 0.6 / 0.6 |
| positive control (2000 corpus windows, a-u) | -- | median -1.0589 | -- | power vs B p95 0.981 | -- | -- | W power 0.868 |

Rule-3 checks: control A varies on T by construction (same letters, order changes the bigrams); control B's p95
(-1.20) sits well below the positive control's median (-1.06), so the statistic has headroom; power 0.98 >= 0.5.
Pre-registered decision: T beats A p95 and B p95 and ranks 1 of 104 in C, so the rule is "supported (S-grade
candidate)" on T. Caveats that bound this, stated before anyone reads more into it: (1) the rule was proposed by
Laura after seeing these signs, and control C cannot price that selection fully -- the 26-shift siblings move letters
into rare v-z, so shift 0 of an alphabetic stroke-count rule is favoured structurally (C is weak evidence); control A
(the order of the signs carries English bigram structure under this rule, tail 0.002) is the substantive number.
(2) The secondary word statistic does not clear its control: W 0.6 equals B p95 0.6 (variant 0.5), so no word
segmentation of the output beats random sign strings; "bend a buc hp" is not a reading. (3) Sign 04 is three dots in
our single-pass table on a modern redrawing (C) and four in Laura's (D); both pass T, the image decides.
Grades (rule 4): 10 letters, all M (H 0, C 0, S 0, M 10, I 0) -- the letter values follow the rule, but no word clears
its control, so no S. Rule-10 wording: this is a statistical support for a component-count design under one candidate
rule, not a decipherment; the sense of the 10 letters is unread.

## GAPS164-pollaky-1865-1875 (3 Oct 2026, account-4): gap 2 (b), Boyouk's clear ad against ad 2's groups

**Pre-registration (written and committed before any scoring, 3 Oct 2026, about 16:3x UTC).**
Candidate (Hassan Boyouk, part 1 comment #3, 18 Mar 2022, sources/schmeh/posts/29-pollaky.txt line 309): ad 2's digit
groups encode the 1867-06-03 "ELOPED ... YOUNG LADY" clear ad (text from sources/schmeh/posts/29a-pollaky-2014-12-27.txt
line 175), about two words per group (his #5). Boyouk himself dates the clear ad 1867, four years before the cipher.
Design tested: any deterministic code that gives one digit group per chunk of 1-3 consecutive plaintext words (same
chunk -> same group), which is the only design his 74/36 ratio implies; no claim is tested for other designs.
Texts: ad 2 parsed into groups on spaces, '.', '=', '-' (primary: "9:77314" split at the colon, 36 groups; variant:
joined, 35). Plaintext, lower-cased, words = runs of letters/digits ("T....." -> t): (P1) the whole ad; (P2) the ad
minus its address tail from "Mr." on, since ad 2 prints "Pollaky, Private Inquiry Office, 13 Paddington Green" in clear.
Statistic S (design-free within the design above): the one repeated group in ad 2 is "91" (positions found by the
script); S = log10 of the fraction of monotone alignments (every group covers 1-3 consecutive words, all words covered)
in which the two "91" groups cover identical word chunks; floor -12 when no alignment does.
Matched control (rule 3): 2000 windows of the same word count from period English prose on disk (tools/data/pg1661_holmes
1892, en/pg76_huckfinn 1884, en/pg1342_pride 1813), same statistic at the same group positions -- unrelated text of the
same length, so S can differ from the target by construction (it depends on which words repeat where). No unrelated
period Agony Column ad of 74 words is on disk; corpus windows stand in for it. Positive control (power): 200 synthetic
codes made from fresh windows by a random 1-3-word chunking into the same group count, keeping one pair of identical
chunks (the pair whose gap is nearest the target's); S of the true window at that pair vs the p95 of 200 unrelated
windows at the same pair; power = share above p95. Seed 164. Script: scripts/boyouk_align.py, output boyouk_align.tsv.
Decision rule: target S above control p95 with power >= 0.5 -> "consistent beyond chance" (no reading); S at or below
p95 with power >= 0.5 -> control-backed negative for Boyouk's text under this design; power < 0.5 -> untestable by this
statistic at this N (one repeat), not refuted.

**Result (scored after the pre-registration commit f065906d; scripts/boyouk_align.py, output scripts/boyouk_align.tsv,
seed 164, 2000 control windows and 200 positive-control codes per row, 0 vision, 0 subagents, 0 external requests).**
The one repeated group "91" sits at group positions 15 and 23 (0-based; 14 and 22 with "9:77314" joined).

| plaintext | groups | words | S target | control p95 | control tail | controls at floor | power | verdict (pre-registered rule) |
|---|---|---|---|---|---|---|---|---|
| P1 whole ad | 36 (split) | 73 | -2.962 | -2.330 | 0.384 | 0.042 | 0.335 | untestable (power < 0.5) |
| P2 minus address | 36 (split) | 64 | -1.970 | -1.983 | 0.045 | 0.038 | 0.315 | untestable (power < 0.5) |
| P1 whole ad | 35 (joined) | 73 | -2.795 | -2.394 | 0.268 | 0.036 | 0.375 | untestable (power < 0.5) |
| P2 minus address | 35 (joined) | 64 | -2.080 | -2.088 | 0.048 | 0.036 | 0.320 | untestable (power < 0.5) |

Rule-3 checks: the control varies on S by construction (it depends on which words repeat where; 4 pct of windows reach
the floor, the rest spread); the positive control (true chunk codes) beats the unrelated-window p95 only 32-38 pct of
the time, so one repeated group at N=35-36 cannot tell Boyouk's text from unrelated prose of the same length. P2 sits
just above its control p95 (tail 0.045-0.048), which at power 0.32 licenses nothing; P1 (with the address that ad 2
prints in clear) sits inside the control bulk. Verdict: untestable by this statistic at this N, not refuted; Boyouk's own
1867 date and Mulliss's objection (#6) stand as they were. This tokenisation counts 73 words, not Boyouk's 74. No token
read (H 0, C 0, S 0, M 0, I 0 for ad 2). Rule-10 wording: a consistency test of a community candidate, not a decipherment.

## GAPS169-pollaky-1865-1875 (3 Oct 2026, account-4): gap 2 (c), Baertl's digit-sum rule on ad 2

Pre-registration (written before any scoring, 3 Oct 2026). Rule under test (Max Baertl, Schmeh post 29 comment #1,
16 June 2017; sources/schmeh/posts/29-pollaky.txt lines 256-273): replace each digit group by the sum of its digits,
change the one 27 to 26, then read the sums as a simple substitution (one sum value = one letter) by frequency.
Baertl's reading: NAMIM PLEARY FUND US TO THE WAS TO THE BATTSREINGASSILB (46 letters).
Facts checked before scoring (no statistic): our 36 groups give the sums
11 15 20 18 26 5 15 9 22 12 4 11 2 4 14 10 17 10 8 5 7 15 10 10 14 9 5 19 11 16 15 14 14 19 27 6.
Baertl's 46 values are these plus 10 more: "19 20" after the third value, and the run "14 10 17 10 8 5 7 15"
repeated (his values 25-32 copy 17-24). His second "TO THE" comes from that duplicated run, and his own letters give
sum 7 two letters (B, W), so the reading does not follow his stated rule exactly.
Statistic T: the best mean add-one letter-trigram log10 prob (English, the corpus in scripts/laura_rule.py) that a fixed
hill-climbing simple-substitution solver (value -> letter, many-to-one allowed; 8 restarts x 1500 swaps, the same
budget for every sequence) reaches on a sum sequence. Sequences scored: S1 our 36 sums with 27->26; S2 Baertl's 46.
Null control: 200 synthetic same-shape strings (uniform random digits, same group lengths; for S2 the same 46-group
shape including the duplicated run) -> digit sums -> same solver. T varies with the sequence's repeat pattern and value
spread, so the null can differ from the target on this axis. Positive control (power): 100 English windows of the same N
from the corpus, each letter sent to a random distinct sum value drawn from the target's own range, scored the same way;
power = share above the null p95. Ceiling check: if the null median is within 0.05 of the positive median, the test is a
non-test. Second statistic B: Baertl's own reading's mean trigram score against 200 same-length English windows (p05)
and against the solver outputs on the null. Pass: target above null p95 with power >= 0.5. Otherwise untestable (power
< 0.5) or not supported (power >= 0.5, target inside the null). Seed 169; script scripts/baertl_digitsum.py.

Result (scripts/baertl_digitsum.py, seed 169, scripts/baertl_digitsum.tsv; 200 null, 100 positive per row):

| sequence | N | K | T target | null p95 (tail) | null median | positive median | power | verdict |
|---|---|---|---|---|---|---|---|---|
| S1 our 36 sums, 27->26 | 36 | 19 | -0.9606 | -0.7747 (0.995) | -0.8479 | -0.8426 | 0.210 | non-test |
| S2 Baertl's 46, 27->26 | 46 | 19 | -0.8689 | -0.7674 (0.555) | -0.8608 | -0.8497 | 0.220 | non-test |
| B Baertl's reading as text | 46 | | -1.0120 | English p05 -1.0796 (0.200 of windows lower) | English median -0.9506 | | | inside English windows |

Rule-3 checks: the null does vary on T (spread -0.95 to -0.75), but its median sits within 0.01 of the positive
control's: a free 19-value substitution on 36-46 tokens reaches trigram scores above real English text (solver medians
about -0.85 against an English median of -0.95) from uniform random digits as easily as from enciphered English. The
statistic is at ceiling (pre-registered ceiling check fires), so it cannot tell a digit-sum letter code from noise at
this N. B only says Baertl's 46 letters are English-like as text, and the solver's random-digit outputs reach a better
score (null median -0.86 vs his -1.01): frequency-reading digit sums produces fragments like his from any same-shape
digit string. Add the facts checked before scoring: his input has 10 values ours does not (a duplicated 8-value run
that yields his second "TO THE", plus "19 20"), and his letters give sum 7 two letters (B, W). Verdict: untestable by
this statistic at N=36 (non-test, ceiling), not refuted; this instrument is retired for the digit-sum hypothesis
(a different instrument would be needed, e.g. a sibling digit ad read by the same rule). No token read (H 0, C 0, S 0,
M 0, I 0 for ad 2). Rule-10 wording: a consistency test of a community claim, not a decipherment.

## GAPS172-pollaky-1865-1875 (3 Oct 2026, account-4): gap 1 print step
Ran: IA be-api full-text (22 requests), archive.org metadata/djvu/page image (4) and fulltext/inside.php (1, ia801801), Google Books API with key and country=US (2). Scripts only, no vision, no subagents. Positive control per host: be-api and Google Books both returned Clay 1881 item 1459, whose text was then confirmed in the separately fetched djvu OCR (print/clay1881_items1458-1466_ocr.txt).
Found:
- **Newspaper and date of ad 1, three print witnesses:** The Times, Tuesday 16 May 1865. (a) Alice Clay (ed.), *The Agony Column of the "Times" 1800-1870* (Chatto and Windus, 1881), p. 257, item 1459 (IA agonycolumntime00claygoog, leaf n281; also agonycolumnoftim00clay and agonycolumntime00thegoog). (b) Kesselman, *'Paddington' Pollaky, Private Detective* (History Press 2015), quotes it as "The Times -- Tuesday, 16 May 1865" (IA paddingtonpollak0000kess, printdisabled, snippet only). (c) Winkworth, *Room Two More Guns* (1986) prints it dated "16 May 1865" after the signature (the "25 January 1865" in its snippet closes the preceding ad, Clay 1430/1431). The page image of (a) is on disk, images/clay1881-p257-n281.jpg: an 1881 typeset rendering independent of the modern redrawing (rule 2: still not the newspaper page). **It has not been read by eye. Sign 04 (3 vs 4 dots) is not settled here.**
- **The clear frame opens with an address, "T."** Clay's OCR has "T^ ♦ --", Kesselman's "T: o--" and Winkworth's "I:-". So our SIGN-A ("|:") is most likely the typeset letter T with its period, the addressee. It is not a code sign (inferred from OCR, image unread).
- **Sibling clear ad to the same addressee, eight days later:** Clay item 1465, Times, Wednesday 24 May 1865: "T. Citation duly served, all in best order. You may rely on my returning about the middle of June. -- Pollaky." It is in the clear and repeats ad 1's closing ("return ... about the middle of June"). It gives a probable-topic crib: a citation (legal summons) to be served, which the telegram arrived "in time to" allow. It is not known plaintext for the 10 signs, so nothing is graded C and the Laura rule was not re-scored against it. Laura's "bendabuchp" has no visible relation to that topic. That is an observation, not a test.
- **No reading in print.** Kesselman: "There is not enough information to decipher the lines and dots, but it forms an amusing challenge". He also quotes a contemporary critic who doubts "the existence of any meaning to those lines and dots which form so conspicuous a feature in the advertisement". Clay gives no gloss on the snippet seen. Found: no reading of ad 1 in Clay, Kesselman, Winkworth or Google Books, searched by phrase on 3 Oct 2026. Palmer/Gaffney's *Agony Column Codes & Ciphers* was not reached: no IA or Google Books full-text hit for the frame phrase.
- **Side find for gap 2 (not worked):** Clay prints 37 items naming Pollaky, 1861-1870 (print/clay1881_pollaky_items.tsv). Several are digit-group or mixed-number ads absent from Schmeh's twelve-ad list, e.g. 1430 (19/23 Jan 1865, 119 digits), 1466 (24 May 1865), the DIPLOMAT series 1499/1500/1502 (Nov 1865), 1582 (Feb 1867) and 1611 (Aug 1867). Some may be addressed to Pollaky rather than written by him. This is a larger sibling pool for ad 2's number family than the two on disk.
Requests per host: be-api.us.archive.org 22, archive.org 4, ia801801.us.archive.org 1, www.googleapis.com 2. No 429/403.

## GAPS174-pollaky-1865-1875 (3 Oct 2026, account-4): gap 1 eye pass on Clay 1881 and topic-crib test

**Step 1, the 1881 print of ad 1 (3 Oct 2026, 17:12-17:14 UTC).** The page image GAPS172 fetched, images/clay1881-p257-n281.jpg,
is **not** p. 257. IA leaf n281 is p. 258 (items 1460 end, 1461-1464; seen in vision call 1). Leaf n280 (fetched now, one
archive.org request, saved as images/clay1881-p256-n280.jpg; despite the filename, the page it shows is **p. 257**) carries item
1459 at y about 2760-3220 (line centres 2762 header, 2851, 2953, 3058, 3159, from `tools/iiif_lines.py --image ... --dry-run`).
Vision call 2 was on the wrong strip too (1460 plus the p. 258 head), so I did not spend a third. Instead I ran a
connected-component count on the two sign lines (scipy.ndimage, threshold 140, y 2905-3005 and 3010-3110 of n280; script inline,
counts in the table). That is a script reading of the 1881 typeset, not an eye reading:
| sign | 1881 components | our table | agrees |
|---|---|---|---|
| 01 | dash w162 + 2 dots above | 1S 2P | yes |
| 02 | 3 stacked dots, bar h81, 1 dot above-right, 1 below-right | 1S 5P | yes |
| 03 | 3 stacked dashes + 2 stacked dots right | 3S 2P | yes |
| **04** | **dash + 4 dots cascading down-right (x 1955/1983/2021/2045, y 2916/2933/2957/2973)** | **1S 3P** | **no: 4 dots, Laura's D** |
| 05 | bar h81 + 1 dot right | 1S 1P | yes |
| 01 | dash + 2 dots above | 1S 2P | yes |
| 07 | ( 3 stacked dots ) | paren 3P | yes |
| 08 | dash + 3 dots above | 1S 3P | yes |
| 09 | 2 stacked short dashes, dot above, dot below | 2S 2P | yes |
| 10 | 3 stacked dots, 3 bars, 1 dot | 3S 4P | yes |
The 1881 print has **"I shall return"** after sign 10, so the clear frame's right side is "I shall", not "shall" as ciphertext.txt
and GAPS160's T statistic have it. So sign 04 = 1 dash, 4 dots. The print agrees with the redrawing on the other nine signs.
This is still a print rendering (1881), not the Times page (rule 2).

**Step 2, pre-registration (written and committed before any scoring, 3 Oct 2026, 17:15 UTC, commit 587ce6ea).**
Hypothesis: under Laura's rule (GAPS160; sign 04 now 4 dots, X = rule(signs) = "bendabuchp"), the 10 signs read a phrase on the
topic of sibling clear ad Clay 1465 (24 May 1865, same "T.": "Citation duly served, all in best order. You may rely on my
returning about the middle of June."). The crib is a probable topic, not known plaintext.
Crib set, fixed here: S1 = every 10-letter window starting at a word start in the letters of the 1465 text;
S2 = the same windows from these paraphrases: "serve the citation", "have the citation served", "get the citation served",
"the citation served", "citation served", "serve it on him", "serve it on her", "serve the summons", "serve the writ",
"serve the papers", "have it served", "it was served", "it is served", "duly served". Phrases under 10 letters give no window.
Statistic M(X) = max over all crib windows c of the count of positions i with X[i] == c[i]; best window reported.
Controls at N=10, all under the same rule so M can differ from the target by construction: (A) 2000 shuffled orders of the
target's own signs (the alignment against the crib changes with order); (B) 2000 random 10-sign strings over the rule's 21
cells; (C) the target's signs under the 104 sibling rules (GAPS160), rank of Laura's. Positive controls: (P1) 2000 crib
windows restricted to a-u, encoded and decoded under the rule (exact crib, identity: M = 10); (P2) the same with 3 of 10
letters replaced at random (a near-topic or partly wrong crib); power = share of P above B's p95.
Decision: "topic crib supported" only if M > p95 of A and of B AND Laura ranks <= 5 of 104 in C AND P2 power >= 0.5. If
the powers are >= 0.5 and the target fails, the result is "these cribs are not read under Laura's rule" (control-backed for
this crib set and rule only, not a negative on the design or on the topic). If P2 power < 0.5, the result is "untestable
at N=10".
Descriptive, no decision: under any simple substitution, the share of crib windows that fit the sign-repeat pattern
ABCDEAFGHI (positions 1 and 6 equal, the other 8 letters distinct from each other and from A), against the same share in
2000 random English corpus windows.
Grades (rule 4): M at most unless supported. If supported, S only on letters inside a matched crib window of two or more
words. Seed 174. Script: scripts/topic_crib.py.

**Result (scored after the pre-registration commit 587ce6ea; scripts/topic_crib.py, output scripts/topic_crib.tsv, seed 174,
0 vision calls, 0 subagents, 0 external requests).**
| X | crib windows (encodable a-u) | M target (best window) | A p95 (tail) | B p95 (tail) | C rank | P1 / P2 median | P1 / P2 power |
|---|---|---|---|---|---|---|---|
| bendabuchp | 29 (11) | 2 ("bestordery") | 3 (0.813) | 3 (0.770) | 21/104 (56 ties) | 10 / 7 | 1.000 / 1.000 |
Rule-3 checks: A and B can differ from the target by construction (order and sign values change the alignment); both
positive controls clear B's p95 every time, so the statistic has power at N=10 for an exact or 70%-right crib.
Pre-registered decision: M 2 is below both null p95s and Laura's rule ranks 21st of 104 siblings, so **these cribs are not
read under Laura's rule** (control-backed, for this crib set and this rule only; not a negative on the component design or on
the topic). Structural note: 18 of the 29 windows cannot be written under the rule at all, because it has no letters v-z
("served", "you", "may", "every"); a citation topic in English needs "served"/"serve", which this alphabet
cannot carry, so a topic reading and Laura's rule pull against each other.
Descriptive (no decision): under any simple substitution, 0 of 29 crib windows fit the sign-repeat pattern ABCDEAFGHI
(random English windows: 0.55%), so no window of this crib set can be the plaintext under any letter-for-letter key
either. Expected for a set this small; it removes the literal 1465 wording and the listed paraphrases, not the topic.
Grades (rule 4): 10 letters, all M (H 0, C 0, S 0, M 10, I 0); no reading.
Side corrections from step 1, not re-scored (brief did not name it): GAPS160's T used the frame "shall"; the print has
"I shall", and ciphertext.txt's frame line lacks the "I". Sign 04's 4-dot value was already GAPS160's variant row (T -1.1074,
tails 0.001/0.005), which is now the primary row. One-line suggestion: re-run laura_rule.py with "ishall" (cheap, script only).

## GAPS178-pollaky-1865-1875 (3 Oct 2026, account-4): gap 1 re-score of Laura's rule with the print's frame

**PREREG-GAPS178 (written and committed before any scoring, 3 Oct 2026, 17:3x UTC).**
Is the frame change post hoc? GAPS160's pre-registration fixed the frame string as "timeto" + X + "shall" and allowed no
alternative frame, so this re-score is **not** covered by that pre-registration. It is a transcription correction (rule 2),
not a choice made by looking at scores: the 1881 print (GAPS174, Clay item 1459, IA leaf n280) has "I shall return", and the
print's wording does not depend on any score. But the decision to re-run was taken after GAPS160's result was known, so this
run is reported as a **sensitivity re-score of GAPS160's test under the corrected transcription**, not as a second
independent test, and it adds no evidence beyond GAPS160's own. Nothing else changes: same rule, same statistic T (mean
add-one bigram log10 probability, same four-source English model), same secondary W, same controls (A 2000 shuffled-sign,
B 2000 random-sign over the 21 cells, C 104 sibling rules, positive control 2000 a-u corpus windows), same seed 160, same
decision rule as GAPS160. The only changes: frame right side "ishall" (was "shall"); primary target sign 04 = 1 dash + 4
dots (X = bendabuchp, GAPS174), with our earlier 3-dot table kept as the variant row. Script: scripts/laura_rule.py with a new
`--right` option (default "shall" reproduces laura_rule.tsv byte for byte); output scripts/laura_rule_ishall.tsv.
Decision, fixed now: if the primary row still beats A p95 and B p95, ranks <= 5 of 104 and power >= 0.5, GAPS160's
"supported (S-grade candidate) on T" survives the correction; if it fails any of the three with power >= 0.5, GAPS160's
support is reported as **not robust to the corrected frame** and the NEAR row says so; if power < 0.5, untestable. Either
way W is reported, no word is graded above M unless W also clears its control (rule 4), and no reading is claimed (rule 10).

**Result (scored after the PREREG-GAPS178 commit b480322e; scripts/laura_rule.py --right ishall, output
scripts/laura_rule_ishall.tsv, seed 160, 0 vision, 0 subagents, 0 external requests; the default run still reproduces
laura_rule.tsv byte for byte).**

| string | X | T ("I shall") | A p95 (tail) | B p95 (tail) | C rank of 104 | W | W: A p95 / B p95 | GAPS160 T ("shall") |
|---|---|---|---|---|---|---|---|---|
| primary, sign 04 = 4 dots (print) | bendabuchp | -1.0835 | -1.2261 (<0.0005, 0 of 2000) | -1.1844 (0.003) | 1 | 0.5 | 0.6 / 0.6 | -1.1074 |
| variant, sign 04 = 3 dots (redrawing) | bencabuchp | -1.1150 | -1.2581 (0.002) | -1.1851 (0.013) | 1 | 0.6 | 0.5 / 0.6 | -1.1405 |
| positive control (2000 a-u corpus windows) | -- | median -1.0509 | -- | power vs B p95 0.985 | -- | -- | W power 0.868 | median -1.0589, power 0.981 |

Rule-3 checks: unchanged from GAPS160 (A and B vary on T by construction; B p95 -1.18 well below the positive median -1.05,
so there is headroom; power 0.985). Pre-registered decision: the primary row beats A p95 and B p95 and ranks 1 of 104, so
GAPS160's "supported (S-grade candidate) on T" **survives the corrected frame**; the margins are a little wider, not
narrower (A tail 0.001 -> under 0.0005, B tail 0.005 -> 0.003). Every number moved together with the frame (target,
control p95s and positive median all rise by about 0.02-0.03, since "is" adds the same junction bigrams to all), which is
what a correction looks like, not a new effect. This is a sensitivity re-score (PREREG-GAPS178), not independent evidence:
the post-hoc-rule caveat of GAPS160 stands (Laura proposed the rule after seeing the signs; control C is weak by construction).
W 0.5 still does not clear its random-sign p95 0.6, so no word segmentation of "bendabuchp" beats random sign strings.
Grades (rule 4): 10 letters, all M (H 0, C 0, S 0, M 10, I 0); no reading (rule 10).

## GAPS182-pollaky-1865-1875 (3 Oct 2026, account-4): gap 1, search for an independent test of Laura's rule

Aim (brief): test Laura's bars-x-dots rule independently, on a different ad in the same sign design, with GAPS160's statistic
and controls at that ad's N. That needs a second ad in ad 1's dot-and-bar script. Laura's rule maps sign components to
letters, so it cannot be applied to a digit-group ad. The 37 Clay Pollaky items (GAPS172) are clear or digit ads.
Search (script, no vision, 0 subagents, 1 request to archive.org): `scripts/sign_sibling_scan.py` over the whole djvu OCR of
Clay 1881 (agonycolumntime00claygoog, all items 1800-1870, not only the 37 Pollaky items). It flags lines with 4 or more
sign-like OCR glyphs, or the bracketed-dot and bar clusters that item 1459's own signs become in this OCR. Positive control:
item 1459 (ad 1) is flagged, both sign lines (12631, 12633). Output `scripts/sign_sibling_scan.tsv`: 20 lines flagged. 2 are
item 1459. The other 18 are frontispiece and publisher's-catalogue noise (9), or drop-cap or punctuation OCR noise in clear
and number ads (9; read in context). **No second sign-script ad is in Clay**, and none is among the twelve Pollaky ads in
Schmeh's list (2 Oct 2026 GAPS section: 1 sign-script ad). Clay is a selection, so this does not show that no sibling exists
in the Times.
Result: **the independent test is not runnable on the material on disk.** No target text means no N, no power figure and no
control, so nothing was scored and nothing was pre-registered. Laura's support on T is still the single-text,
post-hoc-rule result of GAPS160 (and GAPS178's sensitivity re-score), not replicated. Gap 1's independent test now needs new
material: a second ad in this script from Palmer/Gaffney's *Agony Column Codes & Ciphers* (not reached by full-text search,
GAPS172), or from the Times 1865-1871 beyond Clay's selection (Times Digital Archive, owner's desk). Grades (rule 4): 10
letters, all M (H 0, C 0, S 0, M 10, I 0); no reading (rule 10). Requests: archive.org 1 (HTTP 200).

## GAPS194-pollaky-1865-1875 (3 Oct 2026, account-4): gap 2 (d), ad 2 group structure against period codebooks

Pre-registered in PREREG-GAPS194.md (commit 5835d065, pushed before any statistic). Script only, 0 vision calls.
`scripts/codebook_screen.py` (seed 194, `--check` exits 0) writes `scripts/codebook_screen.tsv`. The djvu texts are in
`scripts/codebooks/`. Five archive.org advancedsearch queries for telegraph/telegraphic code, cipher or vocabulary
titles dated 1840-1871 returned two number codebooks. The Mercantile Navy List hits are flag-signal letter codes,
so they are out. The two books:
- F.O.J. Smith, *The Secret Corresponding Vocabulary* (1845). Its preface says word codes carry a letter prefix and
  bare numbers are phrases. Ad 2 has no letter prefixes, so only the phrase list (about 70 entries, an upper bound by
  line count) applies.
- R. Slater, *Telegraphic code, to ensure secrecy*. The IA copy is the 1888 edition; the first edition was 1870, so
  the numbering is a proxy. 15,847 word-number pairs were parsed and kept only where consistent with alphabetical
  order. Highest number R = 24999.

| book | R_B | S0 target (of 36) | S0 if "9:77314" = 977314 | positive control power (plain / additive key) | null mean / p95 | verdict |
|---|---|---|---|---|---|---|
| Slater 1888 | 24999 | 31 | 30 | 1.0 / 1.0 | 29.99 / 32 | FAIL |
| Smith 1845 phrases | 70 | 6 | 5 | 1.0 / 1.0 | 7.08 / 9 | FAIL |

Five groups are above Slater's range: 81720, 77314, 72050, 67321 and 438921. The target's S0 sits inside the null
made from its own digit-length profile, so the number of in-range groups is what the group lengths alone predict.
What the FAIL rules out: ad 2 is not a message written one group per code number in either book's numbering,
whether plain or with an additive key that wraps inside the book. This holds for these two books only, and the
Slater result is conditional on the 1888 numbering matching the 1870 edition.
What it does not rule out: groups built from several concatenated codes, other codebooks (none other found on IA
by these queries), or a private or Pollaky-made code (Kesselman found none in his letters, post 29).
No reading was made, and nothing is graded. Requests: archive.org 7 (5 search, 2 djvu text).
The rule-3 third-attempt clause does not apply: this is the first use of this instrument on gap 2.

## GAPS200-pollaky-1865-1875 (3 Oct 2026, account-4): gap 1, v-z-capable second instrument for the topic crib

Pre-registered in PREREG-GAPS200.md (commit 34dc70a4, pushed before scoring). Script scripts/vz_family_crib.py, output
scripts/vz_family_crib.tsv, seed 200, 0 vision calls, 0 subagents, 0 external requests. How this differs from GAPS160/174/178
(rule 3's third-attempt clause): a rule family, not Laura's single rule -- letter = alpha_n[(a*S + b*P + c) mod n] for every
a, b, c, over n = 26, 25 (I=J), 24 (I=J, U=V), paren sign S = 0 or 4 -- so every letter v-z is writable and non-injective rules
are allowed; the statistic F is the max over the whole family and GAPS174's unchanged 29 crib windows (all 29 now usable),
and the controls take the same max, so the family's freedom sits in the null. Correction to the prereg's arithmetic: the
family is 2 x (26^3 + 25^3 + 24^3) = 94,050 rules, not 97,806; the family itself is as defined, only the count was wrong.
| F target (best rule, window) | A shuffled-sign p95 (share >= F) | B random-sign p95 (share >= F) | P1 exact median / power | P2 3-wrong median / power |
|---|---|---|---|---|
| 5 (n=26, a=0, b=13, c=17: "rerrereerr" vs "servethewr") | 6 (1.000) | 6 (1.000) | 10 / 1.000 | 7 / 1.000 |
A distribution {5: 301, 6: 661, 7: 37, 8: 1}; B {5: 307, 6: 648, 7: 43, 8: 2} (1000 each). Rule-3 checks: A and B can differ
from the target by construction (order and sign values change position-wise matches), and both did (5 to 8); B's p95 6 is
below the ceiling 10 and below P2's median 7, so the statistic has headroom; P2 power 1.0 >= 0.5. Pre-registered decision:
**crib set not read under the v-z component family** -- the target's F 5 is the floor of both null distributions (every
control string reached at least 5), so the best family fit is what any 10 signs get, and its best rule is a degenerate
two-letter one. Control-backed for this crib set and this family only; not a negative on the topic or on component designs
outside the family (e.g. positional rules, syllable or word values). With GAPS174 (Laura's rule) this closes the
Clay 1465 crib set on both instruments on disk. Grades (rule 4): 10 letters, all M (H 0, C 0, S 0, M 10, I 0); no reading
(rule 10).

## GAPS205-pollaky-1865-1875 (3 Oct 2026, account-4): gap 3, catokwacopa-1875's pairing step

The work is in ciphers/catokwacopa-1875 ("GAPS205" section, PREREG-GAPS205.md, gaps205_content.py, content_test.json).
The copy of this folder's ads 3-4 text, Ernst's pair segmentation and the length pairing test were already there (step
NEXT-CAT, 2 Oct 2026; `pairs.py --check` exit 0, S 33, 0/100,000, control power 0.80/1.00). This step added the
content-axis test. T was a non-test (unpaired-control FPR 0.75: it leaks length). For T', **T' (length-corrected merge score) is a valid test and does not detect W.'s pairing**: target p 0.254 (T' -35.05, 20,000 re-pairings) vs positive controls P-coin/P-half power 0.95/1.00 at p < 0.001 and unpaired control U-half false-positive rate 0.05 at p < 0.05: not detected, at control
omissions 0-3 against the design's 3-12. No reading, nothing graded. Merging the two folders stays the orchestrator's decision.

## GAPS211-pollaky-1865-1875 (4 Oct 2026, STALE4 for account 4, account 1 worker): gap 3, T' at 3-12 omissions

Work in ciphers/catokwacopa-1875 ("GAPS211" section, PREREG-GAPS211.md, gaps211_content.py, content_test_gaps211.json).
T' (statistic unchanged from GAPS205) with controls at the design's 3-12-letter omission budget: target p 0.254 (T' -35.05, 20,000 re-pairings, reproduced exactly) vs positive controls P-coin/P-half power 0.65/0.45 at p < 0.001 (0.90/0.95 at p < 0.05) and unpaired control U-half FPR 0.05: valid by the registered gate, **not detected at the design's omission budget** (T' only; no bearing on any
reading). GAPS205's 0-3-omission negative is now bracketed. Next for gap 3, in catokwacopa-1875: spec tests 2-3, ~$5.

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
Read so far: 0 of 4 ads read in this repo. Ad 1 is 0/10 signs, ad 2 is 0/36 digit groups (36 counts "9:77314" as two groups; 35 if it is one), and ads 3-4 are 0/72 letter-words re-derived here (NOTES.md Test 1 table, Test 2 diff). There is no key, decode script, AUDIT.md or HYPOTHESES.md here, and nothing is graded. The ads 3-4 ciphertext is corroborated: two passes agree on 78/80 tokens, and the text matches Ernst's BNA-checked text 72/72. Their community readings are tracked in ciphers/catokwacopa-1875, which has its own gaps section (1 Oct 2026). Pollaky's authorship of ads 3-4 is Schmeh's attribution (post 29; 2 Oct 2026: the W. ads are not among the twelve ads "signed by Pollaky" in his 2014-15 list, only in the 2016 post's sentence, GAPS section above). The ads are signed "W.", not Pollaky, and this repo has not established the attribution.
- Ad 1 (16 May 1865): 10 invented signs inside a plaintext sentence - blocker: not-attempted; statistics cannot help at N=10 (K=9, SIGN-01 repeats at positions 1 and 6; IC 0.0222 falls inside both N=10 control scatters, NOTES.md Test 1). Two cheap internal steps are still untried. First, the signs are built from a few parts (dots, dashes, bars, one bracket pair; ciphertext.txt sign table), so a compositional design (part counts or positions to letters or numbers) can be tested directly. Second, the clear frame "...fortunately in time to [10 signs] shall return to England..." is a crib. Also, the on-disk image is a modern redrawing (clean vector signs, modern serif type, no paper texture; viewed 1 Oct 2026), not the newspaper page (rule 2), so sign details are conditional on the redrawer; next: run a component-decomposition plus frame-crib test with Laura's bars-x-dots rule (part 1 comment #4, 25 Aug 2016, reads B E N D A B U C H P; recorded 2 Oct 2026) as the pre-registered candidate, scoring the same rules on shuffled-sign and random-sign controls of N=10 and reporting both numbers; find the original newspaper and date through the print step, ~$2; 3 Oct 2026 (GAPS160 section above): the component test ran -- Laura's rule gives "bencabuchp" (our sign 04) / "bendabuchp" (hers); frame-bigram T -1.14 beats shuffled-sign p95 -1.29 (tail 0.002) and random-sign p95 -1.20 (tail 0.019), rank 1 of 104 sibling rules, positive-control power 0.98: supported as a design candidate on T; word coverage W 0.6 = random p95 0.6, so no word reading clears its control; 10 letters M, none read. 3 Oct 2026 (GAPS172 section above): print step ran -- The Times, 16 May 1865 (Clay 1881 item 1459, p. 257, page image on disk, unread); SIGN-A is the addressee "T."; sibling clear ad Clay 1465 (24 May 1865, same "T.") gives a probable topic, "Citation duly served"; no printed reading found. 3 Oct 2026 (GAPS174 section above): the 1881 print (Clay item 1459 is on IA leaf n280, p. 257; n281 is p. 258) settles sign 04 as 1 dash + 4 dots (Laura's D) by component count, the other nine signs agree with the redrawing, and the frame reads "I shall"; the pre-registered topic-crib test (Clay 1465 wording plus 14 paraphrases, 29 windows) is not read under Laura's rule: M 2 vs shuffled-sign p95 3 (tail 0.81) and random-sign p95 3 (tail 0.77), rank 21/104, positive-control power 1.0; 18/29 windows unencodable (no v-z), and 0/29 fit the sign-repeat pattern under any simple substitution; 10 letters M. 3 Oct 2026 (GAPS178 section above): re-score with the print's frame "I shall" and sign 04 = 4 dots (sensitivity re-score, PREREG-GAPS178; not covered by GAPS160's pre-registration): T -1.0835 vs shuffled-sign p95 -1.2261 (0 of 2000 above) and random-sign p95 -1.1844 (tail 0.003), rank 1/104, power 0.985: GAPS160's support on T survives the correction; W 0.5 vs random p95 0.6, no word; 10 letters M. 3 Oct 2026 (GAPS182 section above): an independent test of Laura's rule on a sibling sign ad was sought; a script scan of all of Clay 1881 (positive control: ad 1 found) finds no second ad in this script, and Schmeh's list has none, so the test is not runnable on the material on disk (no N, nothing scored); T support stays single-text and unreplicated. Next for gap 1: the original Times page of 16 May 1865 (the redrawing and the 1881 print are both renderings; a LOCAL-QUEUE row for the Times Digital Archive via the owner's desk); 3 Oct 2026 (GAPS200 section above): the v-z-capable second instrument ran (94,050 linear-modular component rules over 24/25/26-letter alphabets, family-max matches against GAPS174's 29 windows): F 5 vs shuffled-sign p95 6 and random-sign p95 6 (target at the null floor), P2 power 1.0 -- the crib set is not read under that family either; a further crib needs new material (a different topic source, or a non-component design), not a larger paraphrase list or another tuning of these two instruments; an independent test of Laura's rule needs new material, a second sign-script ad (Palmer/Gaffney, or the Times 1865-1871 beyond Clay), sought in the same desk row
- Ad 2 (20 Feb 1871): "TELEGRAM" number code, 36 digit groups - blocker: not-attempted; only an IC check has run (0.0016; 35 of 36 groups unique, NOTES.md Test 1). The spec's original codebook test (cheap test 2's earlier wording) was restated for ads 3-4 and never ran. Two community claims sit untested on disk in sources/schmeh/posts/29-pollaky.txt. Boyouk's candidate clear ad (comment #3: the full 74-word "ELOPED ... YOUNG LADY" text, so no fetch is needed to test it) is dated 1867 by Boyouk himself (#5), four years before the cipher. That makes it a weak candidate, and probably not the ad Schmeh means in #4 ("published in the clear a few weeks later"). Mulliss (#6) rejects it. Baertl's digit-sum frequency reading (#1, "NAMIM PLEARY FUND US...", with a 27 changed to 26) has never been checked against a control 2 Oct 2026 (GAPS section above): the sibling step ran; no clear Pollaky ad dated after 20 Feb 1871 exists in Schmeh's twelve-ad list or the three threads, so Boyouk's 1867 ad is the only clear candidate; the printed Agony Column text matches our 36 groups 36/36; two sibling digit-group ads by Pollaky (25 July 1864, 50 digits; 24 May 1865, 56 digits) are now on disk with Ernst's untested homophonic-bigram readings of both (part 1 comments #5-#10), a design prior for ad 2 (114 digits, even); 3 Oct 2026 (GAPS156 section above): step (a) ran -- ad 2 bigram IC 0.0138 vs random p95 0.0144 (tail 0.085); a frequency-proportional 10x10 homophonic control is undetectable by this statistic at N=57 (power 0.053: non-test, retired for that design), a random-allocation one is detectable (power 0.869) and ad 2 is inconclusive against it; siblings below power at N=25/28; 3 Oct 2026 (GAPS164 section above): step (b) ran -- under a one-group-per-1-3-word-chunk code, the two "91" groups cover identical chunks of Boyouk's text in a log10 share -1.970 of alignments (address dropped) vs -1.983 p95 of 2000 same-length period-prose windows (tail 0.045), -2.962 vs -2.330 with the address, but the positive control's power is 0.32-0.38: untestable by this statistic at N=36 (one repeat), not refuted; 3 Oct 2026 (GAPS169 section above): step (c) ran -- Baertl's digit-sum rule is a non-test at this N: a fixed substitution solver on the sums scores -0.961 (our 36) and -0.869 (his 46) against random same-shape digit nulls with p95 -0.775/-0.767, but the null median sits within 0.01 of the English positive control's (power 0.21-0.22, ceiling), and his 46 values carry a duplicated 8-value run plus 2 extra values not in the ad; [retired] for this hypothesis (instrument: free-substitution trigram score on digit sums), untested-by-this-tool, not refuted; 3 Oct 2026 (GAPS194 section above): step (d) ran -- a range screen of the groups against the two number codebooks IA holds for 1840-1871. Slater (1888 copy of the 1870 code, R 24999) gives S0 31/36 against a gate of 34. Smith 1845 (bare numbers are phrases only, R about 70) gives S0 6/36. Positive-control power is 1.0 for both, and the target sits inside the digit-length null (Slater p95 32, Smith p95 9). Verdict: FAIL for both books. Ad 2 is not one group per code number in either book, plain or with a wrapping additive key. Concatenated codes, other books, and the 1870 Slater numbering itself are untested; no cheap internal step is left on disk for gap 2; next: a codebook named by new material (Palmer/Gaffney or Kesselman, owner's desk), then the same range screen with its controls, ~$2
- Ads 3-4 (8 and 20 May 1875, The Standard): line-pair reading of the 72 letter-words, including Bourdeau's unforced lines 9, 12, 23, 26 and 29 - blocker: not-attempted; there is no script re-derivation (rule 7) or per-token grade (rule 4) here. NOTES.md Test 2 says "No substitution or transposition solving run". The classifier called the five lines open-codes, but ciphers/catokwacopa-1875/NOTES.md "Remaining gaps" (1 Oct 2026) classes them as not-attempted. Bourdeau's line-29 Latin search had only a positive control and no matched uniqueness control, so "the omission rule fits almost anything" is untested and the lines are not yet open-codes. The work lives in that folder, so it is not duplicated here; next: run catokwacopa-1875's own cheapest step. Copy this folder's reconciled ads 3-4 text there with attribution, segment it into Ernst's [1]-[28]+[10a] pairs, snapshot Bourdeau's catokwacopa/ folder, re-run the pairing permutation test, then its tests 2-3 with a synthetic-line control. Leave a one-line pointer here. The merge of the two folders is a decision for the orchestrator, ~$2; 3 Oct 2026 (GAPS205 section above): the step is done. Copy, segmentation and length test were already on disk (NEXT-CAT, 2 Oct 2026; --check exit 0). The added content-axis test T' gives target p 0.254 against control power 0.95/1.00 and unpaired FPR 0.05, so the pairs are not detected by letter content; the controls drop 0-3 letters and the design drops 3-12, so this is not a design negative. 4 Oct 2026 (GAPS211): T' with controls at 3-12 omissions ran: p 0.254 vs power 0.65/0.45 (p < 0.001), FPR 0.05, valid, not detected at the design's budget. Next for gap 3, in catokwacopa-1875: its spec tests 2-3, ~$5
- Ads 3-4 ciphertext against the original Standard issues of 8 and 20 May 1875 - blocker: waiting-on LOCAL-QUEUE.tsv row L13 (BNA re-check, owner's desk runner, filed under catokwacopa-1875); this blocks nothing above, because the two scans already agree 72/72 (NOTES.md Test 2)

## Escalation (1 Oct 2026)
- [x] siblings: Done 2 Oct 2026 (GAPS section above): both Pollaky posts and the part 2 they point to fetched with all 21 comments (sources/schmeh/posts/29a-*, 29c-*, 29b-*; 4 requests). All twelve Agony Column Pollaky ads listed by date and system: 3 digit-group ads (1864-07-25, 1865-05-24, 1871-02-20 = ad 2), 1 sign-script ad (1865-05-16 = ad 1), 8 clear. No second ad in ad 1's script; two siblings in ad 2's family (digit groups), with Ernst's untested bigram readings of both; the "two more encrypted Pollaky ads" of post 29 are these two. No clear ad after 20 Feb 1871 in the list. Earlier state: Partly done: ads 3-4 are the Catokwacopa ads (NOTES.md Test 2, 72/72 against Ernst's text in Bourdeau's catokwacopa/ads.py). Never opened: (1) Schmeh's list of the twelve Pollaky ads in Palmer/Gaffney's The Agony Column (Cipherbrain post of 27 Dec 2014, linked from post 29 line 158). (2) The 4 Oct 2016 "Sherlock Holmes and the Pollaky cryptograms" post and its comments. (3) The "two more encrypted Pollaky ads that might have been solved by Thomas Ernst" (post 29 line 165). (4) The 27 March 1875 W. ad that Ernst names (sources/schmeh/posts/08-catokwakopa.txt, comment #2), which may be one of those two. sources/schmeh/manifest.tsv holds only post 29 for Pollaky. Planned: fetch both Pollaky posts and their comments from scienceblogs.de (4 requests or fewer, 1.5 s apart). Run it in the same job as catokwacopa-1875's 2015/2018 thread fetch, which hits the same host. List every Pollaky ad by date and system, looking for a second ad in ad 1's script or ad 2's number code, and for the clear ad Schmeh dates "a few weeks" after 20 Feb 1871, ~$2
- [ ] clear-pages: Used: ad 4's plaintext tail, which ties it to ad 3. Not used: ad 1's clear frame as a crib (gap 1), and ad 2's clear tail ("Pollaky, Private Inquiry Office, 13 Paddington Green"), which shows only that the signature is outside the code. Never tested: Boyouk's candidate clear ad, already on disk in comment #3 but dated 1867 by Boyouk (#5), four years before the cipher. Planned: the gap 2 (a) and gap 1 crib tests, each with its matched control. Then test whichever clear ad the siblings fetch dates to weeks after 20 Feb 1871, ~$3
- [ ] known-keys: 3 Oct 2026 (GAPS194): the pre-1871 codebook range screen ran. Slater (R 24999) and Smith phrases (R about 70) both FAIL at power 1.0 (S0 31/36 and 6/36, gate 34), both books are excluded for one group per code number, and concatenated-code use of either is untested; no other period number codebook was found on IA. Earlier: Mechanical sweep done: KEY-CROSSMATCH.tsv has 45 pollaky rows with 0 matches (28 none, 9 unusable-key, 8 no_corpus). All of those keys are diplomatic keys of 1446-1781 or 20th-century keys, so the era is wrong. KEY-DESIGN-PRIORS.tsv row 81 gives only a letter-for-letter design prior. KEY-OFFICES.tsv and KEY-DESIGN.tsv have no Pollaky row, and Kesselman found no code in several hundred surviving letters (post 29). Never run: period telegraph, commercial and dictionary codebooks for ad 2. Planned: grep IA djvu text of pre-1871 codebooks for ad 2's group structure, with a synthetic control of the same N, ~$3
- [x] print: Done 3 Oct 2026 (GAPS172 section): The Times, 16 May 1865, Clay 1881 item 1459 (page image on disk), Kesselman 2015 and Winkworth 1986 agree. No printed reading. Sibling clear ad Clay 1465 found, and 37 Clay Pollaky items listed for gap 2. Palmer/Gaffney not reached by full-text search. Earlier state: Never searched: Palmer/Gaffney's The Agony Column (spec cheap test 3, unrun) and Kesselman's Pollaky biography. Either may hold a reading, or name the original newspaper and date for ads 1-2 (needed to replace ad 1's redrawing). Planned: Google Books API (GOOGLE_BOOKS_KEY plus country=US) and IA be-api full-text queries for "Pollaky" with "telegram", "cipher" or "secret" in both books, ~$2
- [n/a] key-rebuild: no key, partial key or reading exists here for any of the four ads (0 tokens read), so there is nothing to extend. The ads 3-4 vocabulary and forced-fit searches are catokwacopa-1875's key-rebuild step (its own escalation, marked [ ] there), not this folder's.
- [ ] image-check: Ads 3-4 done: two blind passes agree 78/80, both disagreements were settled on the image, and the text matches Ernst's BNA-checked version 72/72 (NOTES.md Test 2). Ads 1-2 have had a single pass only (NOTES.md Test 1). Ad 1's image is a modern redrawing, not a scan (viewed 1 Oct 2026). Ad 2's image is a newspaper clipping, and its "9:77314" colon and the lone "." after "437." need a second read to decide whether they are glued or split groups. Planned: one blind subagent pass on each of ads 1 and 2 plus a reconciliation, 3 calls at about $1.5 each. The original pages need a LOCAL-QUEUE row once the print step names the newspaper, ~$4.5
- [n/a] retry: no key exists for any ad, so there are no unread groups to rerun with an extended key. This step becomes due once the ad 2 clear-ad or codebook test, ad 1's crib or component test, or a sibling in either script yields a key.
Verdict: keep going: 3 internal gaps; cheapest next: image-check of ads 1-2 (one blind pass each plus a reconciliation), ~$4.5; then gap 3 (ads 3-4), in catokwacopa-1875: spec tests 2-3 with a synthetic-line control, ~$5. GAPS211, 4 Oct 2026: T' re-run with controls at the 3-12-letter omission budget: p 0.254 vs power 0.65/0.45 at p < 0.001 (0.90/0.95 at p < 0.05), FPR 0.05: valid, not detected at the design's budget. Earlier plan: image-check of ads 1-2 (one blind pass each plus a reconciliation), ~$4.5. GAPS205, 3 Oct 2026: gap 3's named step ran. The copy, segmentation and length test were already on disk from NEXT-CAT. The content-axis test T' does not detect the pairing (p 0.254, control power 0.95/1.00, FPR 0.05, controls at 0-3 omissions). GAPS200, 3 Oct 2026: gap 1's v-z-capable second instrument ran: F 5 vs shuffled-sign and random-sign p95 6 (target at the null floor), power 1.0, so the Clay 1465 crib set is not read under that family; gap 1's remaining steps need new material (the Times page of 16 May 1865, a second sign-script ad; owner's desk). Earlier: GAPS194 found gap 2 (ad 2) has no cheap step left on disk (Slater 31/36, Smith 6/36, gate 34, power 1.0); GAPS182 found no sibling sign-script ad; GAPS178 found Laura's rule beats both controls on T (rank 1/104, power 0.985), with no word clearing W

## While waiting (RUN4-WAITBF, 4 Oct 2026)

- Action that depends on nobody: the Verdict's cheapest next -- image-check of ads 1-2 (one blind pass each plus a reconciliation, crops first), ~$4.5; then gap 3 (ads 3-4) through catokwacopa-1875's spec tests 2-3 with the synthetic-line control.
