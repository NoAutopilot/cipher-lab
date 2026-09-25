# tools/data/de20: German prose 1880-1940

Fetched 25 Sept 2026 (GOLD-C, `.claude/briefs/runs/2026-09-25-lane-gold-corpora.md`) for the Köhler 1944
running-key/book-cipher judge, which had no 20th-century German corpus on disk (de16 is Early New High
German). Seven Project Gutenberg plain-text novels/novellas, 1880-1940, no verse, no Fraktur-OCR garbage
(all clean UTF-8 `pgN.txt` releases). Authors: Fontane (3), Hesse (2), Döblin (1), Wassermann (1). See
`MANIFEST.tsv` for book numbers, years, URLs, sha1 of the stripped body, and letters after folding.

Folding: `tools/judge_plaintext.py`'s own `fold()` (lowercase, ä/ö/ü/ß etc. transliterated, non-letters
dropped). Total after folding: 2,485,657 letters (floor was 1.5M).

The Project Gutenberg header/licence banner and footer were stripped from each file at the
`*** START OF THE PROJECT GUTENBERG EBOOK ... ***` / `*** END ... ***` markers before gzipping; the PG
licence permits redistribution of the text together with the licence, so one copy of it is kept as
`LICENSE-gutenberg.txt` (identical text ships with every PG release; extracted once from book 5323's
footer). Each corpus file is `gzip`-compressed; `tools/judge_plaintext.py`'s `read_corpus()` already
handles `.gz` (see `fr16`, `pt17`).

Not wired into `tools/judge_plaintext.py`'s `LANG_CORPORA` default (CLAUDE.md rule: "do not edit
tools/judge_plaintext.py's defaults" per this brief) -- `specs/koehler-1944.json`'s `judge.corpora` points
here directly instead.
