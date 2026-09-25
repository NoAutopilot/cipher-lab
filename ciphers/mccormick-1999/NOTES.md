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
