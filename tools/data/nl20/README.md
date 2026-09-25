# tools/data/nl20: Dutch prose 1880-1940

Fetched 25 Sept 2026 (GOLD-C, `.claude/briefs/runs/2026-09-25-lane-gold-corpora.md`) for the Köhler 1944
book-cipher judge (the FBI-run Köhler channel used a Dutch prayer book, per CLAUDE.md/the spec's `known`
field) -- there was no Dutch corpus at all before this (`tools/data/nl_repo` held only ~12KB of targets'
own committed readings, not usable per rule against circularity). Seven Project Gutenberg plain-text
novels/novellas/story collections, 1880-1940, no verse. Authors: Couperus (2), Van Eeden (1), Van Deyssel
(1), Buysse (2, both volumes of the same novel), Nescio (1, three novellas in one release). See
`MANIFEST.tsv` for book numbers, years, URLs, sha1, and letters after folding.

**Dutch Catholic prayer book/devotional (brief item 2):** searched Gutenberg's catalogue (title/author/
subject fields) for `missaal`, `misboek`, `getijdenboek`, `navolging`, `kerkelijk gebed`, `roomsch`,
`katholiek`, `devotie`, `bidprentje`, `godsvrucht` -- zero hits in any field for any term. No Dutch prayer
book or devotional text of the period was found on Gutenberg; none is included. (This is a catalogue
search result, not a claim that none exists anywhere -- rule 10.)

Folding: `tools/judge_plaintext.py`'s own `fold()`. Total after folding: 2,291,438 letters (floor asked was
1M; Dutch holdings turned out not as thin as the brief warned for this selection of authors).

Header/footer stripped at the PG START/END markers as in `de20`; `LICENSE-gutenberg.txt` is the same PG
licence text (one copy, per the licence's redistribution terms). Each file gzip-compressed;
`tools/judge_plaintext.py`'s `read_corpus()` handles `.gz`.

Not wired into `tools/judge_plaintext.py`'s `LANG_CORPORA` default (rule: don't edit that file's
defaults). No spec currently sets `judge.language: "nl"` with a `corpora` pointer here -- a future nl
target's spec should point `judge.corpora` at this folder's files the way `koehler-1944.json` does for
`de20`.
