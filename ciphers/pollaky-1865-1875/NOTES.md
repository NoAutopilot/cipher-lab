# pollaky-1865-1875

Status: **open**

Ignatius Pollaky cryptograms: four encrypted classified ads by the Victorian private detective, dated
1865-05-16, 1871-02-20, 1875-05-08 and 1875-05-20. Schmeh, Cipherbrain post 29 (sources/schmeh/posts/29-pollaky.html),
scans supplied by Tony Gaffney and Nicole Gluecklich. check-solved has not been run on this target
(it entered the board via the breadth lane, spec-first, per CLAUDE.md 3a); say so explicitly rather
than implying a check-solved verdict. The spec (specs/pollaky-1865-1875.json) records Schmeh's own
account that Bryan Kesselman (Pollaky's biographer) read several hundred surviving Pollaky letters and
found no cipher key, and that "Pollaky seems to have used several different ciphers, but none of the
ciphertexts seems to be long enough to decipher it" -- that is Schmeh/Kesselman's characterisation, not
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
