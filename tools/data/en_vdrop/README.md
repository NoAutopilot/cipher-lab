# tools/data/en_vdrop: vowel-dropped English corpus

Built 25 Sept 2026 (LANE B2 worker bMCC2, cheap test 2 of `specs/mccormick-1999.json`) as a matched-design
corpus for `tools/family_run.py --family masc`: the spec's own `hypothesis_note` flags a possible personal
phonetic/shorthand system, so test 2 runs the masc control and target against both plain English and this
vowel-dropped English, side by side (CLAUDE.md rule 3).

Source: the same two on-disk Project Gutenberg novels already wired as `LANG_CORPORA["en"]` in
`tools/judge_plaintext.py` -- `tools/data/pg1661_holmes.txt`, `tools/data/pg2701_mobydick.txt`. No network
fetch (CLAUDE.md Usage rule 4: reuse, do not refetch).

Transform (`build_en_vdrop.py`'s `transform_text()`): word-internal vowel drop, word-initial vowels kept.
Every maximal run of ASCII letters is one word; its first letter is always kept; every other letter that is
a/e/i/o/u (either case) is dropped; consonants, digits, punctuation and whitespace pass through unchanged.
`"encryption"` -> `"encryptn"`; `"I am here"` -> `"I am hr"`.

Rebuild: `python3 tools/data/en_vdrop/build_en_vdrop.py` (idempotent, overwrites the two output files).
Test: `python3 tools/tests/test_en_vdrop.py` (offline, exercises the transform directly).

| File | Source | Letters folded (jp.fold) before | after | retained |
|---|---|---|---|---|
| pg1661_holmes_vdrop.txt | pg1661_holmes.txt | 431477 | 296334 | 0.687 |
| pg2701_mobydick_vdrop.txt | pg2701_mobydick.txt | 955178 | 657288 | 0.688 |
| total | | 1386655 | 953622 | 0.688 |

Usage in `tools/family_run.py`: `--corpus tools/data/en_vdrop` (reads every `.txt`/`.txt.gz` in the
directory). Not added to `tools/judge_plaintext.py`'s `LANG_CORPORA` (that dict is for real-language
judging; this is a synthetic shorthand transform of English, not a language in its own right) -- pointed
to directly with `--corpus`, the same pattern as `de20`/`fr19` for per-spec corpora.
