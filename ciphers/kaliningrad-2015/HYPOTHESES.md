# kaliningrad-2015 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

## GOLD-KAL1, crib test and German homophonic (25 Sept 2026)

Two families, both control-first (CLAUDE.md rule 3), per the reserve brief
(`.claude/briefs/runs/2026-09-25-lane-gold-c4-kaliningrad-crib-and-homophonic.md`). Corpus: `tools/data/ru19`
(Russian Synodal Bible, 78 books, 1,362 chapters, 3.2M letters, fetched this job -- see its README.md). Solver:
`ciphers/kaliningrad-2015/scripts/pattern_crib.py` (beam-search word-pattern constraint propagation; see its
own docstring for why a beam and not a single greedy commit -- a pure greedy pass on one real control window
(convention A, seed 1) collapsed to 3 pct letters recovered from a single bad early pick, 100 pct once beam
search was added; this was found and fixed before any target run, per the brief's "fix the tool, never the
target" instruction, and is the only tool change made). Offline test: `tools/tests/test_pattern_crib.py`
(8 checks, <0.1 s, synthetic 120-letter fixture corpus, no network).

**Tokenisation.** Convention A: letter+apostrophe merges to one cipher sign (ic_analysis.py's own convention,
K=36); the matching plaintext merge is a Cyrillic consonant + trailing ь/ъ (soft/hard sign) into one token.
Convention B: apostrophe is its own sign (K=27 observed on the target after cleaning, see below); plaintext
tokens are individual Cyrillic letters, no merge (ь/ъ are already separate letters in Cyrillic). Of the
target's 206 space-separated tokens, 10 are the trailing-dot filler line (`eimat . . . . . . . . . .`, dropped
entirely, not signs), leaving 196; of those, 9 have >=2 internal dots and are classified as dotted abbreviation
groups (`x.s.f.d.`, `c.f.`, `f.t.'f.`, `x.l.b.`, `s.n.c.`, `x.l.n.`, `d.s.z.-`, `n.t.d.`, `n'.xn.`) and excluded
from crib matching (abbreviations do not appear as Bible vocabulary word forms), leaving 187 crib-matchable
words -- one short of the brief's "ten dotted abbreviation groups"; the discrepancy is that 8 further tokens
carry a single TRAILING dot immediately before one of Ernst's own running-count markers or a closing quote
(`nenet'se.`, `xf'uaf'np.`, `ngwsaetme.`, `eamdemn.`, `n'eêain.`, `wxixeheu.`, `kexeelxn."`, and `m'am'mt.`,
which precedes the clearly-abbreviation-shaped `f.t.'f.` on the same line but is not itself before a bracket
marker) -- these are read here as section/quote boundary punctuation, not abbreviation dots, and the trailing
dot is stripped before tokenising the word itself; a different judgement call on `m'am'mt.` would move the
abbreviation count to 10, matching the brief exactly, without changing which words are matched below.

### Control (rule 3), both conventions, seeds 1-3, `pattern_crib.py control`

(a) = full vocabulary (the claim's own condition, "Frank had the plaintext to compare against"); (b) = the
control's own source chapter held out of the vocabulary. Score = share of the window's plaintext LETTERS
correctly recovered under the solver's derived sign->letter map.

| convention | seed | chapter | N letters | (a) full-vocab recovery | (b) held-out recovery |
|---|---|---|---|---|---|
| A | 1 | 2 Samuel 11 | 988 | 1.000 | 1.000 |
| A | 2 | Leviticus 27 | 1002 | 0.998 | 0.991 |
| A | 3 | Psalm 49 | 1003 | 1.000 | 1.000 |
| A | mean | -- | -- | **0.999** | **0.997** |
| B | 1 | 2 Samuel 11 | 978 | 1.000 | 1.000 |
| B | 2 | Leviticus 27 | 977 | 0.992 | 0.992 |
| B | 3 | Psalm 49 | 976 | 1.000 | 1.000 |
| B | mean | -- | -- | **0.997** | **0.997** |

GATE (>=0.9 on 3 seeds): **MET**, both conventions, both (a) and (b). (a) and (b) are numerically identical or
near-identical in every seed: the corpus (676,699 words, 3.2M letters) is about 3,000x the size of a single
~978-letter window, so holding out one chapter essentially never removes a word FORM from the vocabulary
entirely (checked directly: excluding chapter (10,11) drops the vocabulary's total word count by 687 but its
count of distinct word-pattern keys by zero) -- the held-out condition is honestly run but uninformative at
this corpus scale, not a second independent test of generalisation the way it would be on a smaller corpus.

Commands: `python3 ciphers/kaliningrad-2015/scripts/pattern_crib.py control --convention {A,B} --seed {1,2,3}
[--holdout]`

### Target, both conventions, `pattern_crib.py target`

| convention | words matched | letters mapped | best chapter | chapter cover |
|---|---|---|---|---|
| A | 22/187 (0.118) | 0.649 | John 6 | 14/22 (0.636) |
| B | 23/187 (0.123) | 0.714 | Ezekiel 39 | 19/23 (0.826) |

### Null (shuffle each cipher word's own signs), 3 seeds, `pattern_crib.py null`

| convention | seed | words matched | best-chapter cover (computed separately, not printed by the CLI) |
|---|---|---|---|
| A | 1 | 18/187 (0.096) | 13/18 (0.722) |
| A | 2 | 15/187 (0.080) | 7/15 (0.467) |
| A | 3 | 12/187 (0.064) | 7/12 (0.583) |
| B | 1 | 12/187 (0.064) | 9/12 (0.750) |
| B | 2 | 15/187 (0.080) | 11/15 (0.733) |
| B | 3 | 13/187 (0.070) | 7/13 (0.538) |

**Reading against the brief's two flag criteria.** (1) Target words-matched share above the null's max by
>=0.2: convention A 0.118 vs null max 0.096, diff 0.022; convention B 0.123 vs null max 0.080, diff 0.043 --
**neither clears the bar**. (2) A best chapter covering over half the decoded words: convention A 0.636, B
0.826 -- both literally clear 0.5, which by the brief's rule is a `flag:` line, posted to ROOM. But the null
runs above show a single best-matching chapter covers over half the (small number of) matched words in 5 of 6
shuffle-null seeds too (mean 0.632, range 0.467-0.750) -- indistinguishable from the target's own 0.636 (A) and
only modestly above the null's own range at 0.826 (B, +0.076 over the null max). With only 22-23 words matched
out of 187, this is expected: a handful of short, common decoded forms (the highest-frequency patterns, hardest
to pin to one specific chapter) concentrate wherever they happen to occur, in the null exactly as in the
target. **Conclusion: this criterion fires by the letter of the brief's rule, but the null control shows it
fires on pure noise too at this N, so it is not being read as evidence for Frank's claim** -- flagged per
instruction, not reported as a lead.

Ernst's 2017 "political... cross-language polyalphabetic" claim (comment #50-52) names no text and no method
and remains untestable as stated; no test was attempted against it.

### German homophonic (family_run.py, control-first)

`ciphers/kaliningrad-2015/ciphertext_signs.tsv` (convention A, generated by
`scripts/make_signs_tsv.py`, N=978 K=36, reproducible from `ic_analysis.py`'s own `tokenize_signs`).
`specs/kaliningrad-2015.json` judge.corpora repointed to `tools/data/de20` (1880-1940 German prose, the same
set koehler-1944.json uses) with a `corpora_note`; the LANG_CORPORA default for `de` (de16, Early New High
German) would have been wrong for a Soviet-era target.

Command: `python3 tools/family_run.py specs/kaliningrad-2015.json --family homophonic --cipher
ciphers/kaliningrad-2015/ciphertext_signs.tsv --corpus tools/data/de20 --param profile=target --seeds 3
--restarts 8 --gate 0.9 --label "GOLD-KAL1 homophonic de20 K36 profile=target, control before target"`

Control (profile=target, 3 seeds): recovery 0.992 / 0.960 / 0.994, mean **0.982** (0.960-0.994). GATE (>=0.9):
**MET**. Target: judge **FAIL** -- score -1.605 vs null_p99 -2.083, real_p05 -0.817, real_median -0.782 (N=978,
mode=both). Full row in the table below. **Control-backed negative for German light-homophonic substitution at
K=36, profile=target, de20 register.** No decoded text described (judge did not pass, rule 7/10).

### Dead ends / not attempted this job

- A Russian masc (simple substitution) control was not built: `homophonic_anneal.py` folds plaintext to a-z
  (26 Latin letters) and has no Cyrillic mode; building one was out of this job's scope (brief item, not
  attempted).
- Transposition was not tested (brief's own reasoning: a transposition preserves the source language's IC,
  the target's 0.0657 matches neither Russian's 0.056 nor German's 0.072-0.076 control range (LANE B2), and
  the apostrophes sit consistently after consonants in-word, a structure a transposition would scatter).
- Only prefix windows (from each chapter's start) were used for the crib control; a mid-chapter window was
  not tried and could plausibly read differently for a name-dense opening verse range.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 25 Sept 2026 23:48 | homophonic | N=978 K=36 restarts=8 corpus=pg15736_Der_Mann_von_vierzig_Jahren.txt.gz+pg36905_Schach_von_Wuthenow.txt.gz+pg41051_Peter_Camenzind.txt.gz+pg41907_Demian.txt.gz+pg43987_Die_drei_Spruenge_des_Wang_lun.txt.gz+pg46184_Frau_Jenny_Treibel.txt.gz+pg5323_Effi_Briest.txt.gz profile=target | 1 | 0.982 (0.960-0.994) | -3111.669 | FAIL language: score=-1.605, null_p99=-2.083, real_p05=-0.817, real_median=-0.782, mode=both, N=978 | yes (gate 0.9) | GOLD-KAL1 homophonic de20 K36 profile=target, control before target |
