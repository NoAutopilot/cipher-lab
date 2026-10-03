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

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
Read so far: 0 of 4 ads read in this repo. Ad 1 is 0/10 signs, ad 2 is 0/36 digit groups (36 counts "9:77314" as two groups; 35 if it is one), and ads 3-4 are 0/72 letter-words re-derived here (NOTES.md Test 1 table, Test 2 diff). There is no key, decode script, AUDIT.md or HYPOTHESES.md here, and nothing is graded. The ads 3-4 ciphertext is corroborated: two passes agree on 78/80 tokens, and the text matches Ernst's BNA-checked text 72/72. Their community readings are tracked in ciphers/catokwacopa-1875, which has its own gaps section (1 Oct 2026). Pollaky's authorship of ads 3-4 is Schmeh's attribution (post 29; 2 Oct 2026: the W. ads are not among the twelve ads "signed by Pollaky" in his 2014-15 list, only in the 2016 post's sentence, GAPS section above). The ads are signed "W.", not Pollaky, and this repo has not established the attribution.
- Ad 1 (16 May 1865): 10 invented signs inside a plaintext sentence - blocker: not-attempted; statistics cannot help at N=10 (K=9, SIGN-01 repeats at positions 1 and 6; IC 0.0222 falls inside both N=10 control scatters, NOTES.md Test 1). Two cheap internal steps are still untried. First, the signs are built from a few parts (dots, dashes, bars, one bracket pair; ciphertext.txt sign table), so a compositional design (part counts or positions to letters or numbers) can be tested directly. Second, the clear frame "...fortunately in time to [10 signs] shall return to England..." is a crib. Also, the on-disk image is a modern redrawing (clean vector signs, modern serif type, no paper texture; viewed 1 Oct 2026), not the newspaper page (rule 2), so sign details are conditional on the redrawer; next: run a component-decomposition plus frame-crib test with Laura's bars-x-dots rule (part 1 comment #4, 25 Aug 2016, reads B E N D A B U C H P; recorded 2 Oct 2026) as the pre-registered candidate, scoring the same rules on shuffled-sign and random-sign controls of N=10 and reporting both numbers; find the original newspaper and date through the print step, ~$2; 3 Oct 2026 (GAPS160 section above): the component test ran -- Laura's rule gives "bencabuchp" (our sign 04) / "bendabuchp" (hers); frame-bigram T -1.14 beats shuffled-sign p95 -1.29 (tail 0.002) and random-sign p95 -1.20 (tail 0.019), rank 1 of 104 sibling rules, positive-control power 0.98: supported as a design candidate on T; word coverage W 0.6 = random p95 0.6, so no word reading clears its control; 10 letters M, none read. Next for gap 1: settle sign 04 (3 vs 4 dots) and find the newspaper page (print step), then a word-level crib with v-z/other signs tested against the frame, ~$2
- Ad 2 (20 Feb 1871): "TELEGRAM" number code, 36 digit groups - blocker: not-attempted; only an IC check has run (0.0016; 35 of 36 groups unique, NOTES.md Test 1). The spec's original codebook test (cheap test 2's earlier wording) was restated for ads 3-4 and never ran. Two community claims sit untested on disk in sources/schmeh/posts/29-pollaky.txt. Boyouk's candidate clear ad (comment #3: the full 74-word "ELOPED ... YOUNG LADY" text, so no fetch is needed to test it) is dated 1867 by Boyouk himself (#5), four years before the cipher. That makes it a weak candidate, and probably not the ad Schmeh means in #4 ("published in the clear a few weeks later"). Mulliss (#6) rejects it. Baertl's digit-sum frequency reading (#1, "NAMIM PLEARY FUND US...", with a 27 changed to 26) has never been checked against a control 2 Oct 2026 (GAPS section above): the sibling step ran; no clear Pollaky ad dated after 20 Feb 1871 exists in Schmeh's twelve-ad list or the three threads, so Boyouk's 1867 ad is the only clear candidate; the printed Agony Column text matches our 36 groups 36/36; two sibling digit-group ads by Pollaky (25 July 1864, 50 digits; 24 May 1865, 56 digits) are now on disk with Ernst's untested homophonic-bigram readings of both (part 1 comments #5-#10), a design prior for ad 2 (114 digits, even); 3 Oct 2026 (GAPS156 section above): step (a) ran -- ad 2 bigram IC 0.0138 vs random p95 0.0144 (tail 0.085); a frequency-proportional 10x10 homophonic control is undetectable by this statistic at N=57 (power 0.053: non-test, retired for that design), a random-allocation one is detectable (power 0.869) and ad 2 is inconclusive against it; siblings below power at N=25/28; next: (b) test Boyouk's 74 words against the 36 groups beside an unrelated period ad of the same length; (c) score Baertl's digit-sum rule on synthetic same-shape digit strings; (d) grep IA djvu text of pre-1871 telegraph and commercial codebooks for the group structure, with a synthetic control of the same N, ~$4
- Ads 3-4 (8 and 20 May 1875, The Standard): line-pair reading of the 72 letter-words, including Bourdeau's unforced lines 9, 12, 23, 26 and 29 - blocker: not-attempted; there is no script re-derivation (rule 7) or per-token grade (rule 4) here. NOTES.md Test 2 says "No substitution or transposition solving run". The classifier called the five lines open-codes, but ciphers/catokwacopa-1875/NOTES.md "Remaining gaps" (1 Oct 2026) classes them as not-attempted. Bourdeau's line-29 Latin search had only a positive control and no matched uniqueness control, so "the omission rule fits almost anything" is untested and the lines are not yet open-codes. The work lives in that folder, so it is not duplicated here; next: run catokwacopa-1875's own cheapest step. Copy this folder's reconciled ads 3-4 text there with attribution, segment it into Ernst's [1]-[28]+[10a] pairs, snapshot Bourdeau's catokwacopa/ folder, re-run the pairing permutation test, then its tests 2-3 with a synthetic-line control. Leave a one-line pointer here. The merge of the two folders is a decision for the orchestrator, ~$2
- Ads 3-4 ciphertext against the original Standard issues of 8 and 20 May 1875 - blocker: waiting-on LOCAL-QUEUE.tsv row L13 (BNA re-check, owner's desk runner, filed under catokwacopa-1875); this blocks nothing above, because the two scans already agree 72/72 (NOTES.md Test 2)

## Escalation (1 Oct 2026)
- [x] siblings: Done 2 Oct 2026 (GAPS section above): both Pollaky posts and the part 2 they point to fetched with all 21 comments (sources/schmeh/posts/29a-*, 29c-*, 29b-*; 4 requests). All twelve Agony Column Pollaky ads listed by date and system: 3 digit-group ads (1864-07-25, 1865-05-24, 1871-02-20 = ad 2), 1 sign-script ad (1865-05-16 = ad 1), 8 clear. No second ad in ad 1's script; two siblings in ad 2's family (digit groups), with Ernst's untested bigram readings of both; the "two more encrypted Pollaky ads" of post 29 are these two. No clear ad after 20 Feb 1871 in the list. Earlier state: Partly done: ads 3-4 are the Catokwacopa ads (NOTES.md Test 2, 72/72 against Ernst's text in Bourdeau's catokwacopa/ads.py). Never opened: (1) Schmeh's list of the twelve Pollaky ads in Palmer/Gaffney's The Agony Column (Cipherbrain post of 27 Dec 2014, linked from post 29 line 158). (2) The 4 Oct 2016 "Sherlock Holmes and the Pollaky cryptograms" post and its comments. (3) The "two more encrypted Pollaky ads that might have been solved by Thomas Ernst" (post 29 line 165). (4) The 27 March 1875 W. ad that Ernst names (sources/schmeh/posts/08-catokwakopa.txt, comment #2), which may be one of those two. sources/schmeh/manifest.tsv holds only post 29 for Pollaky. Planned: fetch both Pollaky posts and their comments from scienceblogs.de (4 requests or fewer, 1.5 s apart). Run it in the same job as catokwacopa-1875's 2015/2018 thread fetch, which hits the same host. List every Pollaky ad by date and system, looking for a second ad in ad 1's script or ad 2's number code, and for the clear ad Schmeh dates "a few weeks" after 20 Feb 1871, ~$2
- [ ] clear-pages: Used: ad 4's plaintext tail, which ties it to ad 3. Not used: ad 1's clear frame as a crib (gap 1), and ad 2's clear tail ("Pollaky, Private Inquiry Office, 13 Paddington Green"), which shows only that the signature is outside the code. Never tested: Boyouk's candidate clear ad, already on disk in comment #3 but dated 1867 by Boyouk (#5), four years before the cipher. Planned: the gap 2 (a) and gap 1 crib tests, each with its matched control. Then test whichever clear ad the siblings fetch dates to weeks after 20 Feb 1871, ~$3
- [ ] known-keys: Mechanical sweep done: KEY-CROSSMATCH.tsv has 45 pollaky rows with 0 matches (28 none, 9 unusable-key, 8 no_corpus). All of those keys are diplomatic keys of 1446-1781 or 20th-century keys, so the era is wrong. KEY-DESIGN-PRIORS.tsv row 81 gives only a letter-for-letter design prior. KEY-OFFICES.tsv and KEY-DESIGN.tsv have no Pollaky row, and Kesselman found no code in several hundred surviving letters (post 29). Never run: period telegraph, commercial and dictionary codebooks for ad 2. Planned: grep IA djvu text of pre-1871 codebooks for ad 2's group structure, with a synthetic control of the same N, ~$3
- [ ] print: Never searched: Palmer/Gaffney's The Agony Column (spec cheap test 3, unrun) and Kesselman's Pollaky biography. Either may hold a reading, or name the original newspaper and date for ads 1-2 (needed to replace ad 1's redrawing). Planned: Google Books API (GOOGLE_BOOKS_KEY plus country=US) and IA be-api full-text queries for "Pollaky" with "telegram", "cipher" or "secret" in both books, ~$2
- [n/a] key-rebuild: no key, partial key or reading exists here for any of the four ads (0 tokens read), so there is nothing to extend. The ads 3-4 vocabulary and forced-fit searches are catokwacopa-1875's key-rebuild step (its own escalation, marked [ ] there), not this folder's.
- [ ] image-check: Ads 3-4 done: two blind passes agree 78/80, both disagreements were settled on the image, and the text matches Ernst's BNA-checked version 72/72 (NOTES.md Test 2). Ads 1-2 have had a single pass only (NOTES.md Test 1). Ad 1's image is a modern redrawing, not a scan (viewed 1 Oct 2026). Ad 2's image is a newspaper clipping, and its "9:77314" colon and the lone "." after "437." need a second read to decide whether they are glued or split groups. Planned: one blind subagent pass on each of ads 1 and 2 plus a reconciliation, 3 calls at about $1.5 each. The original pages need a LOCAL-QUEUE row once the print step names the newspaper, ~$4.5
- [n/a] retry: no key exists for any ad, so there are no unread groups to rerun with an extended key. This step becomes due once the ad 2 clear-ad or codebook test, ad 1's crib or component test, or a sibling in either script yields a key.
Verdict: keep going: 3 internal gaps; cheapest next: gap 2 (b) Boyouk's 74 words against ad 2's 36 groups beside an unrelated same-length period ad, ~$1 (gap 1's component test ran 3 Oct 2026, GAPS160: Laura's rule supported on frame-bigram T against shuffled- and random-sign N=10 controls, power 0.98, but no word clears its control; gap 1's next is the print step to find the newspaper page and settle sign 04, ~$2)
