open

check-solved (25 Sept 2026, LANE B2 worker bMCC2, minimal per intake step added 18:14 UTC to
`.claude/briefs/breadth.md`): Cipherbrain post 10 (Klaus Schmeh, 1 May 2018, "The Top 50 unsolved
encrypted messages: 10. Ricky McCormick's encrypted notes"), `sources/schmeh/posts/10-mccormick.txt`,
read in full including its 6-comment thread; grepped for solved/unsolved/decrypt/cracked/FBI. No
verified solution on record: the FBI's own codebreaking unit CRRU (Schmeh: "success rate of about 99
percent") and the American Cryptogram Association (ACA) both failed (post lines 135, 173). A claimed
Spanish-language "solution" posted to taringa.net (comment #1, "Descrifrado el Codigo McCormick que el
FBI no pudo") is discussed and dismissed in the same comment thread by two other commenters (#3 HF(de),
#5 HF(de)) as homophone guessing ("sounds like", e.g. 8=eight=ai=a), not a real decipherment -- so this
is not a fresh finding, it is already on the record and rejected by the blog's own readers.
Solver-repository grep (github.com/dbourdeau/cyphersolver, github.com/aaymeloglu/unsolved-ciphers) and
one OpenAlex plus one Semantic Scholar query (rule 1's remaining legs) were skipped this run: this
worker's brief (`.claude/briefs/runs/2026-09-25-lane-b2-mccormick-1999-t2.md`) states "No subagents, no
network," so no network call was made. A future check-solved pass with network access should complete
those two legs before any campaign above breadth cap ($10, CLAUDE.md 3a).

Status vocabulary: `open` (CLAUDE.md rule 5). This folder holds only the intake note and
HYPOTHESES.md for the breadth-lane cheap tests on specs/mccormick-1999.json; transcription and
ciphertext live in that spec (Schmeh's own re-typing of the FBI's images, rule 2), not here -- no
images were fetched by this worker (CLAUDE.md's "LANE B, 24 Sept 2026" rule: a breadth worker has no
target folder unless its test fetches images; this folder exists only because this brief's cheap
test 2 asked for one to hold HYPOTHESES.md).

## Cheap test 2 (25 Sept 2026, LANE B2 bMCC2)

`tools/family_run.py --family masc` run twice at N=746, K=24 (letters-only fold, both notes, 3
control seeds, gate 0.6, restarts 8): once against the default English corpus
(`tools/data/pg1661_holmes.txt` + `pg2701_mobydick.txt`), once against a new vowel-dropped English
corpus built for this test (`tools/data/en_vdrop/`, word-initial vowels kept, word-internal a/e/i/o/u
dropped, README and offline test there). Rows in `HYPOTHESES.md`; full numbers, method and caveat in
`specs/mccormick-1999.json`'s `cheap_test_done.2`.

Both controls read at or above ~0.98 recovery (mean 0.994 default English, 0.985 vowel-dropped) --
already at the near-ceiling line CLAUDE.md rule 3 warns has no headroom to show a gain: a masc anneal
at this N, K essentially always recovers a random simple-substitution key, whatever the corpus. Both
target decodes got a mechanical judge PASS (`tools/judge_plaintext.py`; a PASS is a gate for a
verifier, not a reading, rule 10) but read as letter salad, not English, under either corpus --
`ciphers/mccormick-1999/families/masc-1-default_en.txt` and `masc-1-vdrop_en.txt` (the shared
`masc-1.txt` path holds only the more recent, vowel-dropped run; both are kept separately since the
tool overwrites that path per run). This is consistent with the spec's own `schema_note`: the notes'
heavy repeated-token structure (test 1: NCBE, the -RSE family) inflates n-gram likelihood under any
consistent key, so a PASS here is not evidence either English design is right. Neither run supports
or rules out the source's shorthand/nomenclator hypothesis over the null. Next step (not run here,
out of this brief's scope): a bespoke tokenizer-aware judge treating the repeated multi-character
tokens as signs, per test 1's and this spec's own schema_note.

**Update 25 Sept 2026 (LANE B2 orchestrator, 19:02 flag):** `tools/judge_plaintext.py` was fixed to fail
closed when a judge block has no `language`/corpora; the spec's judge block now carries `language: en,
min_word_cover: 0.6` (added by that same flag). Re-judged under the fixed judge, both cheap test 2
decodes above are **FAIL**, not PASS -- the earlier PASS lines in this section and in HYPOTHESES.md were
a length-only check, not a real language check; masc is excluded at N=746, K=24 under both corpora.

## Cheap test 3 (25 Sept 2026, LANE B3 bMCC3) -- homophonic family, NEAR.md's named next step

`tools/family_run.py specs/mccormick-1999.json --family homophonic --cipher
specs/cheap-tests/mccormick-1999/cipher_both_notes.txt --tokens letters --seeds 3 --gate 0.6`, same
letters-only fold as test 2 (N=746, K=24 auto-derived from the ciphertext), homophonic_anneal's own K
(one homophone slot per sign actually present, i.e. K=24 -- the spec carries no separate declared K),
run three times, plus a false-positive floor (`--shuffle-target SEED`, new option added to
`tools/family_run.py` this run with an offline test in `tools/tests/test_family_run.py`, check (7)):

| run | CONTROL mean (range), 3 seeds | TARGET judge |
|---|---|---|
| default English corpus | 0.998 (0.997-0.999) | **FAIL** score=-1.48 vs null_p99=-2.071, real_p05=-0.864 |
| vowel-dropped English corpus (`tools/data/en_vdrop`) | 0.652 (0.058-0.992) | **FAIL** score=-2.329 (below even null_p99) |
| shuffled target, default corpus, shuffle seed 1 | 0.998 (0.997-0.999) | **FAIL** score=-1.807 |
| shuffled target, default corpus, shuffle seed 2 | 0.998 (0.997-0.999) | **FAIL** score=-1.839 |
| shuffled target, default corpus, shuffle seed 3 | 0.998 (0.997-0.999) | **FAIL** score=-1.896 |

Default-English control is near ceiling (0.998), same as test 2's masc controls, so it has no headroom
to show a gain (rule 3 caveat) but the target still FAILs the judge outright this time (the earlier
"PASS" in test 2 was the judge's own bug, now fixed -- see the update note above). The vowel-dropped
control is markedly less reliable for homophonic than it was for masc (test 2: 0.985; here: mean 0.652,
range 0.058-0.992 -- one of the three seeds essentially failed to anneal at all), barely clearing the
0.6 gate; a control that unstable is weak evidence either way from that run alone.

The false-positive floor is the important number here: three independent shuffles of the target's own
746 letters (same multiset, same K=24, random order -- CLAUDE.md rule 3's "same length, symbol count,
design" synthetic negative, built from the target itself rather than a corpus) all FAIL, with scores
(-1.807, -1.839, -1.896) in the *same range* as the real target's own default-corpus score (-1.48) --
if anything the real target scores slightly *better* than the shuffled noise, but all four sit well
inside FAIL territory, nowhere near real_p05 (-0.864). This means the homophonic anneal's best decode
of the real 746-letter target is statistically indistinguishable from its best decode of random letter
salad of the same shape: no signal above noise. Combined with test 2 (masc excluded, same target, same
judge fix), both families tried so far are excluded at this N, K under the letters-only fold.

Decodes: `ciphers/mccormick-1999/families/homophonic-1-default_en.txt`,
`homophonic-1-vdrop_en.txt`, `homophonic-1-shuffle1.txt`, `homophonic-1-shuffle2.txt`,
`homophonic-1-shuffle3.txt` (all read as letter salad on inspection, consistent with the FAIL judge
lines). Full rows in `HYPOTHESES.md` (includes one earlier `--control-only` calibration row at 19:13,
kept per the tool's append-only rule, and one rerun of the default-corpus row at 19:20 to save its
decode file separately before the vowel-dropped run's file overwrote the shared `homophonic-1.txt`
path -- same numbers both times, confirming determinism). This is a control-backed negative for the
homophonic family at this N/K/fold, not a `closed-negative` for the target as a whole (CLAUDE.md rule 5
amendment): the letters-only fold itself remains untested against the source's own repeated-token/
shorthand hypothesis (test 1's schema_note, tests 2 and 3's `hypothesis_note`) -- a tokenizer-aware
judge treating NCBE/-RSE/etc. as signs is still the more promising untried step, not a straight
letter-substitution family at any K.

## Cheap test 4 (25 Sept 2026, LANE B3 bMCC4) -- token/nomenclator test, NEAR.md's named next step

`specs/cheap-tests/mccormick-1999/token_anneal.py` (new script -- `tools/nomenclator_anneal.py` is
Italian/German-only and needs numpy, so it did not fit; a fresh, small, numpy-free script was written
instead, per the brief). Tokenizes both notes as written on the documented separators (whitespace,
hyphen, slash, comma, `?`; parentheses stripped as brackets not characters): 132 tokens total -- 116
code-token occurrences (99 distinct multi-letter types: NCBE x11, six other types x2, 92 singletons),
14 number tokens, 2 single-letter tokens (`N` x2). Numbers and single letters pass through unchanged
(rule: "each single letter as itself"); a simulated anneal (8000 iterations, 2 restarts per run)
assigns each of the 99 distinct code types to a word from a 350-word pool drawn from the same `en`
corpus `tools/judge_plaintext.py` itself uses (pg1661_holmes.txt + pg2701_mobydick.txt), scored by that
script's own character 4-gram `NgramModel` -- the test's language model is exactly the judge's, nothing
separate to keep in sync.

**Matched control** (3 seeds): a same-length (132-token), same-per-position-kind-sequence synthetic
English stream drawn from the same corpus. Code slots get a fresh unique 4-letter placeholder, except
words from the corpus's 60 most frequent types get one placeholder reused on every recurrence (mirrors
the real target's NCBE-heavy, mostly-singleton structure); number slots get a random small integer; the
two letter slots get `a`/`I`. No vowel-dropped share: the target's own non-code share (10.6% number +
1.5% single-letter = 12.1% of 132 tokens) is covered exactly by the number+letter slots, so there is no
remainder to vowel-drop (documented choice, per the brief). Recovery = fraction of the control's own
known code-type-to-word truth the anneal reconstructs.

| run | control recovery | target score | shuffled-target score (3 shuffles) |
|---|---|---|---|
| iters=8000, restarts=2 | mean 0.8% (0.0%, 1.1%, 1.3% across 3 seeds; 76-99 truth types/seed) | -0.7497 | -0.752, -0.745, -0.762 |

**Gate NOT met** (control recovery 0.8% is far below the brief's 0.5 gate): per CLAUDE.md rule 3 and the
brief, this is "not a test," reported as such rather than as a control-backed negative. The design is
degenerate at this token count: 99 largely-singleton code types drawn from a ~350-word pool is an
effectively unconstrained assignment problem -- cross-word 4-gram context at word boundaries is far too
weak a signal to pin down a specific word choice, so the anneal cannot even recover the *control's own
known ground truth*. The target decode does get a language-check PASS from `judge_plaintext.py` (score
-0.75 > real_p05 -0.873, word cover 0.971) but this is not meaningful: it is an artifact of plugging real
dictionary words into 99 free slots (any assignment looks locally plausible), exactly as shown by the
control's near-zero true-mapping recovery and by the shuffled-target floor (-0.745 to -0.762, the same
range as the real target's own -0.7497 -- no discrimination between the real token order and three
shuffles of it). The judge's overall verdict is FAIL regardless, but only on the length check (got 408
letters vs the 700-800 the block expects, because the token scheme replaces code tokens with words of a
different length -- not a language finding). Full numbers and method in `specs/mccormick-1999.json`
`cheap_test_done.4`; decode preview and script in
`specs/cheap-tests/mccormick-1999/token_anneal.py` and `test4_result.json`;
`ciphers/mccormick-1999/families/token-anneal-target.txt` (candidate only, not a reading -- rule 10).

This matches the spec's own prediction for this test ("the FBI/ACA's own presumed approach ... expect a
negative"). Combined with tests 2 and 3, all three of the spec's cheap tests are now run: masc excluded,
homophonic excluded (both control-backed), and this token/nomenclator test's own control falls short of
its gate so it cannot be read either way. None supports a reading. The source's shorthand/phonetic
hypothesis remains the only untested account, but turning it into a scoreable, testable family (e.g. a
hand-built sign inventory checked against a period shorthand system such as Gregg) is a campaign-scale
task, not a further breadth-lane cheap test -- out of this brief's scope; left as a one-line suggestion
for the orchestrator, not started here.

**Fold-count backfill (parent worker EN-FOLDS, 25 Sept 2026 22:17 UTC, CLAUDE.md rule 3 amendment):** cheap
test 4's language model reuses `tools/judge_plaintext.py`'s own `en` corpus (pg1661_holmes.txt +
pg2701_mobydick.txt), which had no per-fold spread on file at the time; it now does --
leave-one-file-out false-negative spread 0.44 (N=200)/0.11 (N=500) on those 2 files, worse (0.64/0.75) after
adding 3 more sources, per `tools/data/en/README.md`. This does not change the verdict above (test 4's own
result turns on the control's near-zero recovery, not on the language-check PASS, which the note above
already calls not meaningful) -- the verdict stands as written, with that caveat on record.
