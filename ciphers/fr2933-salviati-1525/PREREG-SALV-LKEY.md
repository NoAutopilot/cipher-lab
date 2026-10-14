# PREREG-SALV-LKEY (14 Oct 2026, written 07:3x UTC by date -u, before any mapping result or score)

Worker SALV-LKEY (Opus), LANE DEFAULT-A1-0640-14 (account 1), brief `.claude/briefs/runs/2026-10-14-acct1-default-0640-jobs.md`
"Wave 3" + row SALV-LKEY. Instrument: George Lasry's published 78-symbol key sheet for this letter
(`sources/cyphersolver/2026-10-14-lasry/salviati1525/lasry_p031_1.png`; credit George Lasry, published by D. Bourdeau,
cyphersolver dde5b0ea; text CC BY 4.0). Our transcription: `ciphertext_with_plain.txt` / `ciphertext_f5*.tsv` (code^mark tokens,
2,932 sign tokens, 324 sign runs; measured pass-to-pass disagreement 14.6%, residual error per sign ~6.4-6.9%).

1. Mapping. Two blind subagent passes, each matching our atlas exemplars (glyphs/atlas_part1.png, atlas_part2.png, one call per part)
   to his sheet's exemplars, neither shown the other. Each pass gives, per our base code, the his-sheet entries that share its base
   sign, and per our mark label, his superscript. A (base, mark) -> value is mapped only where both passes agree on the base family
   and the mark; disagreement or a value his sheet marks "?" -> grade M; agreement on an unmarked value -> grade H (published key,
   key source `published`). Our token types whose (base, mark) has no cell on his sheet stay unread ([code^mark]).
2. Decode. key_lasry.tsv + decode_lasry.json through tools/decode_key.py (--check exit 0); plain boxes pass through as clear words.
3. Statistic. The cipher-run decode only (plain boxes excluded; unread tokens dropped), folded to a-z, scored by the spec judge
   (`tools/judge_plaintext.py specs/fr2933-salviati-1525.json --file`, it16 4-gram mean log10/letter). The official judge output is
   pasted as is (its length check may FAIL on the 2,500-4,500 window; the language score is the statistic used here).
4. Control (rule 3). The same decode under >= 200 keys with the mapped values permuted within sign class (single letters among
   single-letter signs, syllables among syllable signs, words/doubles among those), same coverage, same tokens; scored by the same
   NgramModel.score on the same letters. The control can differ from the target on this statistic (the key changes the text).
5. Gate. Target score > permuted-key p99 => "the published key, applied through our transcription, reads above chance". Else
   "does not beat its control on our transcription" -- logged as a non-test of the key at our 14.6% disagreement, not a negative
   against his key (his transcription is not ours). Also reported: per leaf share of tokens mapped, per leaf score vs per-leaf p99,
   best stretch (highest-scoring 40-letter window of one run, hand-read for words), and the in-lexicon word count (>= 4 letters,
   it16 words) for target vs permuted p99 as a secondary number.
6. No key edits to any existing file; no re-grading of earlier tokens; no novelty classification.
