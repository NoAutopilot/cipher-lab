# yogtze-1984 cheap test 1: acrostic/initialism feasibility (25 Sept 2026, bYOG)

Ran `cheap_tests_in_order[0]` from `specs/yogtze-1984.json`, exactly: an initials/acrostic feasibility
search for the six letters Y-O-G-T-Z-E, German and English, each against its own matched control (per
the LANE B3 brief: 20 random 6-letter strings drawn from that language's own word-initial-letter
frequency distribution, same wordlist, same search). N=6 is below any unicity (spec's own
`constraints.unicity_note`), so this is reported hit/no-hit against a distribution, not scored as a
cryptanalytic negative, and no phrase is proposed as a reading.

Script: `test1_initials.py`. Wordlists: `tools/data/de20/` (1880-1940 German prose, 42,047 distinct
words) and `tools/data/pg1661_holmes.txt` + `pg2701_mobydick.txt` (19th-c. English, 19,547 distinct
words) -- the same corpora `tools/judge_plaintext.py`'s LANG_CORPORA already vets as real, unrelated
prose, never a target's own reading. de20 was used over the wired de16 default (Early New High German)
as closer in period to 1984. Full output: `test1_output.json`.

## Method

For a 6-letter string, the "match count" at each position is the number of distinct wordlist entries
starting with that letter; the reported statistic is the **minimum across the six positions** (the
acrostic's bottleneck letter -- one position with very few candidate words makes any six-word phrase
using that letter rare, whatever the other five positions offer). The control draws 20 random 6-letter
strings from the same wordlist's own first-letter frequency distribution and computes the same minimum,
so the comparison is target-vs-realistic-random-string, not target-vs-uniform-random.

## Result

| Language | Target min-count (bottleneck letter) | Control min-count range (20 draws) | Control mean | Target's percentile |
|---|---|---|---|---|
| German (de20) | **12** (Y: yacht, yaks, yang, yangs, yao) | 337 - 1879 | 997.9 | 0.0 (below every control) |
| English (Holmes+Moby-Dick) | **18** (Z: zag, zay, zeal, zealand, zealanders) | 57 - 825 | 456.3 | 0.0 (below every control) |

In both languages the target's own bottleneck letter (Y in German, Z in English) offers far fewer
candidate words than any of the 20 control draws' own bottleneck letters -- Y is close to absent as a
German word-initial (a handful of loanwords: Yacht, Yak, Yoga-family terms) and Z is comparatively rare
in English. **No hit**: this is not evidence for the acrostic hypothesis in either language -- if
anything it is a small, N=6-scale piece of support for Schmeh's own stated observation ("no language in
the world... knows this word") extended to *initials of a phrase* as well as to the word itself, since a
real six-word acrostic in either language would need to clear a bottleneck this repository's wordlists
say is unusually narrow for these particular six letters. This is one test on two general-prose corpora,
not a claim that no German or English six-word phrase with these initials could ever be found by a
person searching idiom books directly (test 2 in the spec, not run this pass, per the brief).

No candidate phrase is reported; none was assembled or claimed as a reading.

Requests: none (disk-only test; the intake step's network calls -- solver-repo clones and one OpenAlex/
one Semantic Scholar query -- are logged in `ciphers/yogtze-1984/NOTES.md`, not here).
