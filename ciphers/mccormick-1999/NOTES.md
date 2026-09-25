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
