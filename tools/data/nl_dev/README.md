# tools/data/nl_dev: Dutch devotional prose (Statenvertaling)

Fetched 25 Sept 2026 (GOLD-K1, `.claude/briefs/runs/2026-09-25-lane-gold-c2-koehler-devotional-key.md`) for the
Köhler 1944 book-cipher rerun: every Family B and B' negative logged so far (GOLD-2A, GOLD-2C) is conditional on
`tools/data/nl20`'s 1880-1920 novel-prose Dutch models, while the one documented Koehler key is a Dutch prayer
book. This corpus swaps the register: the Statenvertaling (the 17th-century Dutch Bible translation, in period
De Vries-Te Winkel-compatible spelling in this particular digitisation -- see limits below), split one file per
book (67 books, Genesis through Openbaring), so a control can hold one book out.

**Source and route (Access playbook order).** (a) dbnl.org: unreachable, TLS `SSL_ERROR_SYSCALL` on the bare
handshake (curl, `--max-time 15`) -- logged, not retried (one attempt only). (b) statenvertaling.net (HTTP 200)
and bijbel-statenvertaling.com (HTTP 200) both reachable but serve one HTML page per chapter (1,189 chapters
across 66-67 books would cost far more than the 40-request budget) -- not used once (c) answered. (c) the
getbible API, `https://api.getbible.net/v2/statenvertaling.json`: one request, HTTP 200, 9,158,346 bytes,
returns the entire translation as one JSON document (`distribution_license: "Public Domain"`,
`distribution_source: "https://bijbel.coas.nl/bijbel/"`). Used this route: one HTTP request total for the whole
corpus, well inside budget. (d) Gutenberg (gutendex.com) for a Catholic Dutch prayer book/devotional (missaal,
misboek, getijdenboek, navolging, kerkelijk gebed, roomsch, katholiek, devotie, godsvrucht): `gutendex.com`
timed out with 0 bytes received on both the first attempt and the one permitted retry (`--max-time 20`,
2 s apart) -- logged as unreachable this session, not a claim that no such book exists on Gutenberg (rule 10;
this echoes nl20's own catalogue-search null result for the same terms, GOLD-C, `tools/data/nl20/README.md`).
No Catholic prayer text is included; only the Bible (route c).

**Extraction.** `build_corpus.py` (this job, not committed -- ran once from the scratchpad, reproducible from the
JSON's own structure: `books[i].chapters[j].verses[k].text`) joins every verse's text with newlines per book,
one `.txt.gz` per book, named `NN_bookslug.txt.gz`. No PG START/END markers (not a Gutenberg text); the file is
the verse text only, no chapter/verse numbers, no front matter. Folding is `tools/judge_plaintext.py`'s own
`fold()`.

**Totals.** 67 files (Genesis .. Openbaring, `MANIFEST.tsv`: book number, name, chapter count, source URL,
raw UTF-8 byte count, sha1 of the raw (pre-fold) text, letters after folding, file). 3,426,073 letters after
folding (floor asked was 1,000,000; the Bible is far larger than nl20's novel selection). Any book can be held
out for a control and the corpus still holds >2.5M letters (e.g. holding out the whole Torah, Genesis-Deuteronomy,
leaves the other 62 books).

**Limits (say so, not silently repaired).** (1) This is the Bible, not a prayer book -- the closest reachable
devotional register to what Koehler is documented to have used, not the item itself; a Catholic Getijdenboek or
Roomsch Missaal would be closer still and was searched for and not found (limit (d) above). (2) The digitisation's
orthography was not checked letter-by-letter against a facsimile of the 1637 or a 19th-century printed
Statenvertaling; `bijbel.coas.nl`'s own edition note is embedded in the JSON's `distribution_about`/`distribution_history`
fields (not reproduced here) and was not read in full this pass. (3) Old Testament long genealogical/name-heavy
books (Numeri, Kronieken) may skew the unigram profile away from ordinary devotional prose; not corrected for.
(4) Licence: `distribution_license: "Public Domain"` per the API's own metadata; not independently verified against
`bijbel.coas.nl`'s own terms page this pass.

Not wired into `tools/judge_plaintext.py`'s `LANG_CORPORA` default (same rule as nl20: don't edit that file's
defaults). Used via `--kcorpus tools/data/nl_dev` / `--param kcorpus=tools/data/nl_dev` as in this job's brief.
