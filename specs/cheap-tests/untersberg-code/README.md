# untersberg-code cheap test 1: abbreviation hypothesis

25 Sept 2026, LANE B3 worker bUNT. Spec `specs/untersberg-code.json`, `cheap_tests_in_order[0]`.

**Question.** Schmeh's own text leans toward a scribal-abbreviation reading over a substitution
cipher ("some knowledge of ancient German or Latin might be more helpful than codebreaking
skills"); before running any substitution-cipher control (test 3), check whether the
period-after-short-token structure the transcription shows is a real, non-random feature at
all, or would arise from the target's own character frequencies by chance.

**Method.** `test1_abbreviation.py` counts occurrences of the pattern "1-3 letters immediately
followed by a period" (the shape a suspension abbreviation like "S." "d." "occo." takes) in the
target's six transcribed lines (228 characters, spaces included). The control (set by the LANE
B3 orchestrator's brief) is a synthetic string of the same length, drawn i.i.d. per character
from the target's own unigram character distribution (same alphabet: letters, digits, '.', ',',
whitespace, same relative frequencies), tokenised and counted the same way, 500 trials.

**Result** (`test1_output.json`):

| | count |
|---|---|
| target | 36 |
| control mean (500 trials) | 12.0 |
| control range | 5-20 |
| target percentile in control | 100.0 |

Target is above every one of 500 control trials. The short-token+period clustering is a real
structural feature of the transcription, not an artifact of how often a period or a short
letter-run happens to occur in a string of this length and alphabet.

**What this test does and does not show.** It rules out "the periods are meaningless noise
given the letter frequencies" -- they are not. It does *not* by itself distinguish a real
16th-century Latin/German abbreviation convention from some other structured design (e.g. a
homophonic or code+mark cipher that also groups short symbol runs with a separator); no corpus
of known abbreviation conventions was on hand to test against directly (out of this brief's
disk-only, no-fetch scope), so this is a necessary-but-not-sufficient check, not a positive
identification. Per the spec's own note, the substitution-cipher control (test 3) still applies
if/when the abbreviation reading is rejected on other grounds (a Latin/German philologist's
read of the actual short forms against known suspension tables, e.g. via test 2's image fetch --
not run this pass).

**Verdict for CLAUDE.md rule 5/near-solve amendment.** This is not a reading and not a
closed-negative: it is a control-backed *positive* signal (the pattern exceeds its control) that
supports treating the target as abbreviation-shaped rather than assuming substitution outright,
but it does not itself solve or close the target. No candidate plaintext, no judge run. Per the
brief, do not run test 2 or test 3 this pass.

---

# untersberg-code -- NEAR.md step 1: abbreviation-expander control (25 Sept 2026, LANE B4 worker bUNT2)

Brief: `.claude/briefs/runs/2026-09-25-lane-b4-untersberg-expand.md`. Named next step after test 1
(period-after-short-token count, 36 vs control mean 12.0, 100th percentile -- the text is shaped like
scribal abbreviation, not meaningless periods; NEAR.md row). This step asks: can an expander recover
abbreviated words at all, at this length, before trying it on the real target?

## Corpus and era

`tools/data/de16/composed_enhg.txt` (Early New High German, 1389 words, see its own README: written
for this repository, NOT a historical source, only supplies n-gram statistics). No wired Latin corpus
exists in `tools/data` (CLAUDE.md's La note: only circular per-target files); the target's
`language_candidates` are `["de", "la"]` and Schmeh's own text leans towards "ancient German or Latin,"
so de16 is the best era-plausible stand-in on hand for a 16th-century chancery-abbreviation register.
This is stated, not hidden: the corpus is model-written prose in a Luther-1545-influenced register, so
its bigram statistics are more repetitive/predictable than a real 16th-century chancery hand would be
-- if anything this should make the control's score an *optimistic* upper bound on what a real period
corpus would support, not a pessimistic one.

## Method

`expand_lib.py` implements both the control-window builder and the beam-search expander;
`run_control.py` runs step (1), `run_target.py` runs step (2).

1. **Target shape**, derived straight from `specs/untersberg-code.json`'s own `ciphertext` field (71
   tokens total): 61 letter-tokens (abbreviations) with length histogram {1:50, 2:3, 3:1, 4:4, 5:1,
   6:1, 8:1}, and 10 digit-tokens with digit-length multiset {1:6, 2:2, 3:1} (`5.`, `6.`, `519.`,
   `55.`, `19.` etc. in the transcription).
2. **Synthetic windows**: 5 non-overlapping 71-word windows from de16 (seed 20260925, evenly spaced
   starts 0/263/526/789/1052). For each window, 10 of the 71 word-positions are picked at random to
   become digit tokens (arbitrary digit strings at the target's own digit-length multiset -- these
   words are simply discarded/unscored, matching that the target's digit tokens are not claimed to be
   abbreviated words either); the other 61 positions get the target's own length-histogram of
   abbreviation lengths (shuffled assignment), each abbreviated by **suspension**: first *k* letters of
   the real word + a period (the scheme the brief names), or the whole word + period if it is shorter
   than *k*.
3. **Expander**: beam search (width 25, top 40 unigram-ranked candidates per slot) over a word-bigram
   model with unigram backoff, trained on the corpus **with the window itself removed** (the two
   remaining contiguous runs, bigrams never bridging the gap) -- never on the window being expanded.
   Candidates for a token are vocabulary words whose lowercase form starts with the token's letters and
   is at least as long. A digit token resets bigram context (breaks the chain) since it is not a word.
4. **Score** = share of the 61 scored positions where the beam's final top hypothesis equals the true
   word.
5. **Floor**: the identical procedure (windows, digit assignment seed, abbreviation-length assignment,
   beam expander) run against the same corpus with word order shuffled once (seed 20260925) before
   windowing -- this breaks the bigram signal while keeping the same vocabulary and unigram
   frequencies, isolating how much of the control's score comes from bigram context vs. from
   prefix-matching plus raw word frequency alone.

## Control result (gate >= 0.30 mean across 5 windows)

| window (corpus word offset) | correct / scored | score |
|---|---|---|
| 0 | 9/61 | 0.148 |
| 263 | 28/61 | 0.459 |
| 526 | 21/61 | 0.344 |
| 789 | 24/61 | 0.393 |
| 1052 | 16/61 | 0.262 |
| **mean** | | **0.321** |

**GATE MET** (0.321 >= 0.30).

Floor (same expander, shuffled word order, breaks bigram structure):

| window | correct / scored | score |
|---|---|---|
| 0 | 17/61 | 0.279 |
| 263 | 14/61 | 0.230 |
| 526 | 21/61 | 0.344 |
| 789 | 20/61 | 0.328 |
| 1052 | 16/61 | 0.262 |
| **mean** | | **0.289** |

**Caveat the brief's floor step was designed to surface, reported plainly**: the floor (0.289) sits only
0.032 below the control mean (0.321), and the two distributions overlap heavily (floor's own best window,
0.344, beats three of the five control windows). At this corpus size (1389 words, heavily repetitive
Luther/formula prose) most of the "control" score is coming from prefix-matching against a small,
high-frequency vocabulary (many single-letter tokens resolve to `vnd`/`das`/`der`/`die` regardless of
context), not from genuine word-bigram context the way real chancery prose with a richer vocabulary would
give. The control clears its stated gate, so per the brief step (2) runs -- but the pass should be read as
weak evidence that an expander *could* work at this length, not strong evidence that it *would* against a
harder, less repetitive real corpus. A larger/less repetitive period corpus (German or, ideally, Latin --
still unbuilt, see below) is the natural next lever if this line is pursued further.

## Target result (step 2, run because the control met its gate)

`target_expansion.txt` (top beam-search expansion of the real six lines, de16 vocabulary/bigrams, no
leave-out needed since the target is not in the corpus):

```
sagt das der occo.[?] x.[?] Satrnrop[?] 5. auch freundtlicher 5. L dem printzen 6. mit 6. auch tag 5.
q.[?] Octobris tag mit 5. religion u.[?] auch tag mit 519. Regentin L vnd E Pfaltzgraff 55. auch tt.[?]
tt.[?] L x.[?] missm[?] ariu.[?] auch Octobris u[?] stadt Gott Conde x[?] 5. L 19. alto[?] mvraco[?]
mic[?] Regentin L y.[?] pymi.[?] lust Octobris Pfaltzgraff mit in vnd man L tag tag Gott
```

44/61 letter-tokens got a beam proposal; 17 had no de16 vocabulary word starting with their letters
(left as `token[?]`, grade **I**, no candidate). Every proposed word is grade **M** (uncertain,
cryptanalytic/model-chosen, no key or crib): rule 4 -- no H, no C, no S is possible here, there is no
known plaintext or key for this target.

`tools/judge_plaintext.py specs/untersberg-code.json --file specs/cheap-tests/untersberg-code/target_expansion.txt`:

```
FAIL length: got=240, min=90, max=130
FAIL language: score=-1.169, null_p99=-1.616, real_p05=-0.464, real_median=-0.428, mode=both, N=240
FAIL - untersberg-code (a PASS is a gate for a verifier, not a reading; rule 10)
```

FAIL on both length (the `[?]`-tagged unexpanded tokens inflate the character count past the judge's
90-130 window) and language score (-1.169 vs. the real-text 5th percentile of -0.464 -- well below,
not a borderline miss). **Reported plainly per the brief: a `de` judge run on an expansion the model
itself chose from its own candidate list is circular (the beam search already optimized for a
bigram-plausible German sequence) and this FAIL, like a hypothetical PASS, counts for very little either
way** -- it is not independent evidence, just a sanity check that the top expansion is not fluent German,
which it is not.

## Bottom line

Control mean 0.321 clears the 0.30 gate, but the floor (0.289) is close enough that the "pass" mostly
reflects the corpus's small, repetitive vocabulary rather than a strong bigram signal; the target's own
top expansion is not fluent (judge FAIL by a wide margin) and 17/61 tokens have no candidate at all in
this small corpus. This is consistent with either (a) the abbreviation hypothesis being right but needing
a larger/real period corpus (ideally Latin, still unbuilt -- one-line suggestion, not built this pass per
the brief's no-Latin-corpus-build instruction) and a real abbreviation-convention word list (Cappelli/
Grun) rather than a generic Luther-prose vocabulary, or (b) the six lines not being expandable
scribal-abbreviation German/Latin prose at all. No reading. Status stays `open`/`partial` per NEAR.md
(the orchestrator's file, not touched here).
