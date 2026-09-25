# tools/data/fr19: French prose 1800-1890

Fetched 25 Sept 2026 (GOLD-C, `.claude/briefs/runs/2026-09-25-lane-gold-corpora.md`) for the Debosnys 1883
judge (the spec's own note asks for a 19th-century French corpus; `fr16`, the `LANG_CORPORA["fr"]` default,
is 16th-century French letters, wrong period). Five Project Gutenberg plain-text novels, 1830-1888, no
verse. Authors: Stendhal (2), Balzac (1), Flaubert (1), Maupassant (1). See `MANIFEST.tsv` for book
numbers, years, URLs, sha1, and letters after folding.

Folding: `tools/judge_plaintext.py`'s own `fold()`. Total after folding: 2,664,273 letters (floor was 1M).

Header/footer stripped at the PG START/END markers as in `de20`/`nl20`; `LICENSE-gutenberg.txt` is the
same PG licence text (one copy, per the licence's redistribution terms). Each file gzip-compressed;
`tools/judge_plaintext.py`'s `read_corpus()` handles `.gz`.

Not wired into `tools/judge_plaintext.py`'s `LANG_CORPORA` default (brief: do not edit that file's
defaults) -- `specs/debosnys-1883.json`'s `judge.corpora` points here directly.
