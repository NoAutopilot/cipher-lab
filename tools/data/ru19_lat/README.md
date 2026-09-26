# tools/data/ru19_lat: transliterated Russian, four schemes

Built 26 Sept 2026 (GOLD-KAL2, `.claude/briefs/runs/2026-09-26-lane-gold-c5-kaliningrad-russian.md`) from
`tools/data/ru19` (the Synodal Bible, 1876 translation, 78 books, 3,204,442 Cyrillic letters) with
`tools/translit_ru.py`, one `.txt.gz` per scheme, for the kaliningrad-2015 Russian-substitution hypothesis
(judge corpus for `tools/family_run.py --family homophonic`). No network: `tools/data/ru19` was already on
disk (fetched by GOLD-KAL1, 25 Sept 2026).

**Schemes** (letter-by-letter table in the job brief; `ё` folds to `е`'s letter except where a scheme's own
rule names `ё` explicitly; `ъ` always dropped; `й` and `ы` both become `y`; every scheme's alphabet stays
inside `homophonic_anneal.fold()`'s `ALPHA` -- 24 letters, a-z minus j and v):

| scheme | description | letters | q (soft-sign marker) share |
|---|---|---|---|
| s1 | scientific with digraphs (zh ch sh shch kh ts yu ya); q is the soft sign ь | 3,468,213 | 1.44 pct |
| s1s | s1 with q (soft sign) removed entirely; softness lost | 3,418,231 | 0.00 pct |
| s3p | phonemic partial: s1, but a paired consonant (б в г д з к л м н п р с т ф х) before я/ю/ё/ь writes consonant+q+vowel(a/u/o, nothing for ь); я ю ё elsewhere stay ya yu e | 3,468,300 | 2.89 pct |
| s3 | phonemic full: s3p, and also q before е and и after a paired consonant (vowel then e, i) | 3,813,869 | 11.69 pct |

Brief's estimates were s1 ~1.5 pct, s3p ~2.9 pct, s3 ~12.6 pct q; measured 1.44 / 2.89 / 11.69 pct, the same
order and close in magnitude (the small gap is this corpus's own letter mix, not a tool bug -- see
`tools/tests/test_translit_ru.py` for exact per-scheme output on a hand-computed fixture).

**Format.** One line of space-separated words per input line (chapter markers and all non-Cyrillic
punctuation/brackets/digits dropped as word separators, per book file, 78 books concatenated in filename
order); `tools/family_run.py`/`tools/homophonic_anneal.py`'s own `fold()` strips spaces and any remaining
non-`a-z` character when building the n-gram model, so word boundaries here are for readability only, not
read by the solver.

**Reproduce:** `python3 tools/translit_ru.py --scheme {s1,s1s,s3p,s3} tools/data/ru19 tools/data/ru19_lat/<scheme>.txt.gz`
(offline, about 6 s for all four; test: `python3 tools/tests/test_translit_ru.py`, under 2 s).

**Limits.** Same as `tools/data/ru19/README.md`'s (not independently checked against a facsimile of the
1876 print; the crib solver's own limits do not apply here since this corpus is read as unigram/n-gram text
only). The paired-consonant list and the choice of which vowels trigger softness marking are this project's
own hypothesis about how a period cipher-maker might have rendered Russian softness in the Latin alphabet,
not a scholarly transliteration standard -- see the job brief and `ciphers/kaliningrad-2015/HYPOTHESES.md`
for why these four and not others.
