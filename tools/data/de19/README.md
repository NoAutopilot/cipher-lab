# tools/data/de19: German prose, first printed 1800-1840

Built 26 Sept 2026 (LANE B9, job bHCP3, `.claude/briefs/runs/2026-09-26-lane-b9-hcp3.md`) because
`tools/data/de20` (the `LANG_CORPORA["de"]` default) is 1880-1940 German prose and `tools/data/de16`
(Early New High German) is further off in the other direction -- an era gap flagged but not fixed by
`specs/hessen-1824.json`'s own `constraints.era_note` (target dated 20 Feb 1824). Same method as
`tools/data/pt18`/`tools/data/es17c` (CLAUDE.md rule 3's era-matching paragraph): match the judge corpus
to the target's own period and register before trusting a FAIL or a PASS.

Three Project Gutenberg (gutenberg.org, `www.gutenberg.org` only, this brief's one allowed host) plain-text
works, first printed 1814-1817, all clean UTF-8 `pgN.txt` releases with the standard PG header/footer:

- **Johann Wolfgang von Goethe, *Italienische Reise*, Band 1** (travel narrative/letters from Goethe's
  1786-88 Italian journey, first published 1816). `ebooks/2404`, `cache/epub/2404/pg2404.txt`.
- **Johann Wolfgang von Goethe, *Italienische Reise*, Band 2** (same work, second volume, first published
  1817). `ebooks/2405`, `cache/epub/2405/pg2405.txt`.
- **Adelbert von Chamisso, *Peter Schlemihls wundersame Geschichte*** (novella, first published 1814).
  `ebooks/31538`, `cache/epub/31538/pg31538.txt`.

See `MANIFEST.tsv` for per-file author, title, first-print year, source URL, body size, folded letter
count and a 12-hex-char sha1 of the stripped body.

## Why only three files, not the brief's "5-8"

The brief's own host cap for this job (`www.gutenberg.org` only, >=1.5 s apart, **at most 12 requests**)
was the binding constraint, not source scarcity. Nine requests went to `ebooks/search/?query=...` locating
candidates (Heinrich von Kleist -- his listed prose is bundled into "Ausgewählte Schriften", ebook 6645,
content not verified as pure narrative prose within the request budget, so left out rather than guessed
into the corpus; Heinrich Heine's *Reisebilder* -- no clean single-work German-language hit, only an
English "Prose Writings" translation; Clausewitz *Vom Kriege* -- no hit at all, only a secondary English
commentary; E. T. A. Hoffmann -- no clean single-author hit within budget), leaving three requests for
downloads, spent on the two candidates found clean (Goethe, two volumes of one work) plus one more
(Chamisso, found on the fifth search). A future pass with a fresh request budget should add Kleist's
actual novellas (*Michael Kohlhaas*, *Die Marquise von O....*) once their Gutenberg ebook number is
confirmed to be prose-only, and Hoffmann, to raise the file count past the CLAUDE.md rule 3 fold-count
amendment's informal "~5 source files" reliability floor (the es17c/EN-FOLDS lesson: a corpus under that
count gives a per-fold spread of unknown reliability, not just a lower one) -- see `holdout_check.tsv`
below, computed on these three anyway per this job's brief (step U2), and flagged accordingly.

## Folding and stripping

Same convention as `tools/data/de20`/`tools/data/pt18`: each file's Project Gutenberg header/licence
banner and footer stripped at the `*** START OF THE PROJECT GUTENBERG EBOOK ... ***` / `*** END ... ***`
markers before gzipping (one copy of the licence text kept at `LICENSE-gutenberg.txt`, extracted once from
book 2404's footer -- identical text ships with every PG release). Letters counted with
`tools/judge_plaintext.py`'s own `fold()` (lowercase, umlaut/eszett transliteration, non-letters dropped).

Combined: 581,677 + 349,134 + 110,186 = **1,040,997 letters after fold()** -- just over the ~1M floor
other era corpora in this project used (es17c ~2.1M, pt18 ~3.2M, de20 ~2.5M; this one is the thinnest of
the four, consistent with having a third of their file count).

Not wired into `tools/judge_plaintext.py`'s `LANG_CORPORA` default -- `specs/hessen-1824.json`'s
`judge.corpora` (or a `--corpus tools/data/de19` argument to `tools/family_run.py`) points here directly,
the same way `specs/koehler-1944.json` points at de20.
