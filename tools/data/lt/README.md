# tools/data/lt: Lithuanian Bible (getbible.net, register: religious/Bible)

Fetched 26 Sept 2026 (GOLD-KAL3, `.claude/briefs/runs/2026-09-26-lane-gold-c5-kaliningrad-polish.md`, unit C,
conditional on `api.getbible.net/v2/translations.json` listing a Lithuanian translation, which it does) for the
kaliningrad-2015 Lithuanian-homophonic cheap test (rank 5 in `ciphers/kaliningrad-2015/HYPOTHESES.md`'s
cycle-4 decision table). No Lithuanian corpus existed on disk before this. There is no Gutenberg prose corpus
for Lithuanian on the same easy route Polish used (brief's own note); this is a Bible translation, not prose,
same register caveat as `tools/data/ru19` (Old-Testament genealogical/name-heavy chapters skew unigram
frequency away from ordinary narrative prose, not corrected for) -- flag this when reading any judge verdict
against it.

**Source and route.** `https://api.getbible.net/v2/translations.json` (1 request) lists 117 translations,
including `lithuanian` (`lang: lt`, `distribution_license: "Copyrighted; Permission to distribute granted to
CrossWire"`, source "Tikejimo Zodis" church, version 1.7.2, 2017-08-17). `https://api.getbible.net/v2/lithuanian.json`
(1 request) is the whole translation, 66 books, one JSON document, 9,300,060 bytes.

**Extraction**, same shape as `tools/data/ru19`: verse text lower-cased, joined with newlines, one `.txt.gz`
per book (66 files, `NN_slug.txt.gz`, slug an informational ASCII transliteration of the book name, not used
by any tool for matching); each book file keeps a `== CHAPTER N ==` marker line before that chapter's verses.
`MANIFEST.tsv`: book number, name (native diacritics), slug, chapter count, raw UTF-8 byte count, sha1 of the
raw (pre-fold) text, letter count after `tools/homophonic_anneal.py`'s `fold()`, file.

**Totals.** 66 books, 2,599,750 letters after fold (marker lines' own letters included; the verse text alone,
without markers, is 2,591,427 letters by a direct count -- both numbers from this job, the difference is
the `== CHAPTER N ==` labels).

**fold() check (brief step 4).** Lithuanian's marked letters (ą ę ė į ų ū č š ž) are each built from a base
Latin letter plus a combining diacritic under Unicode NFKD, unlike Polish ł (its own code point, not
decomposable -- see `tools/data/pl19/README.md`), so `fold()`'s NFKD-normalize-then-strip-combining step folds
every one of them to its base letter (ą→a, ę→e, ė→e, į→i, ų→u, ū→u, č→c, š→s, ž→z) with nothing left over for
the final `[^a-z]` filter to drop. Checked directly on the whole corpus: raw own-alphabet letter count and
`len(fold(text))` are identical (0.0000% difference) -- no letter-drop fix needed here, unlike pl19.

## Licence

Copyrighted (CrossWire/"Tikejimo Zodis"), distribution permitted per getbible.net's own terms ("Permission to
distribute granted to CrossWire"); not public domain the way the Synodal Bible (`ru19`) or a Gutenberg text
is. Used here as a corpus for a judge/anneal language model (a statistical resource, not redistributed as a
reading text), same basis `ru19` and `nl_dev`'s Statenvertaling were used on this project.

## Requests

`api.getbible.net`: 2 (`translations.json` listing, `lithuanian.json` full fetch), 1.5s apart, descriptive
User-Agent, both HTTP 200 on first attempt, no retries. Matches the brief's "at most 2" cap for this host
exactly.
