# tools/data/ru19: Russian Synodal Bible (1876 translation)

Fetched 25 Sept 2026 (GOLD-KAL1, `.claude/briefs/runs/2026-09-25-lane-gold-c4-kaliningrad-crib-and-homophonic.md`)
for the kaliningrad-2015 crib test: "Frank" (Cipherbrain post 19 comment #58, 19 Feb 2021) claimed the
plaintext is "a chapter of the first Orthodox bible translation which was edited by the Metropolitan of Moscow
Filaret and released in 1876" -- the Synodal translation. This corpus is that translation's own text, used
as both a word-frequency vocabulary and a chapter index for a word-pattern crib solver.

**Source and route (Access playbook order).** getbible API, `https://api.getbible.net/v2/synodal.json`
(the same host and route GOLD-K1 used for `tools/data/nl_dev`'s Statenvertaling): one HTTP request, HTTP 200,
27,127,350 bytes, the whole translation (`Синодального Перевода Библии`, 78 books including deuterocanonicals)
as one JSON document (`distribution_license: "Public Domain"`, `distribution_version: "1.9.1"`,
`distribution_source`: `www.rbo.ru`/`patriarchia.ru`). No second host tried; one fetch covered the whole corpus.

**Extraction.** Verse text lower-cased, joined with newlines, one `.txt.gz` per book (78 files, `NN_slug.txt.gz`,
slug is an informational transliteration of the Russian book name, not used by any tool for matching). Each
book file keeps a `== CHAPTER N ==` marker line before that chapter's verses, so a chapter can be recovered
from the file by splitting on that marker -- needed for the crib solver's "best-matching chapter" report.
`MANIFEST.tsv`: book number, name (Cyrillic), slug, chapter count, raw UTF-8 byte count, sha1 of the raw
(pre-fold) text, Cyrillic-letter count after lower-casing, file.

**Totals.** 78 books, 1,362 chapters, 3,204,442 Cyrillic letters (а-я plus ё) after lower-casing. Any book, or
just the Synodal chapter used to build a control cipher, can be held out and the corpus still holds well over
3,000,000 letters.

**Limits (say so, not silently repaired).** (1) This is the getbible API's own digitisation of the Synodal
text, not checked letter-by-letter against a facsimile of the 1876 print or a modern critical edition; the
API's own metadata claims Public Domain and cites `rbo.ru`/`patriarchia.ru` as sources, not independently
verified against those sites this pass. (2) Old-Testament genealogical/name-heavy chapters may skew the
unigram/word-frequency profile away from ordinary narrative prose; not corrected for. (3) The crib test's
"vocabulary" is exact word forms as they appear in this text (Russian is heavily inflected, so a paraphrase or
different verse numbering in the plaintext, if it is a Synodal chapter at all, would not match on word form
alone) -- a limit of the crib design, not of this corpus.

Not wired into `tools/judge_plaintext.py`'s `LANG_CORPORA` (no Russian judge exists in this repository as of
25 Sept 2026; see CLAUDE.md rule 3's language-corpus lessons for pt18/es17c/en -- a Russian judge is future
work, not this job's). Used directly by `ciphers/kaliningrad-2015/scripts/pattern_crib.py`.
