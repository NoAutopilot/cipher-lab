# es17: early-17th-c. Spanish prose for the judge's language check

Built 25 Sept 2026 (LANE R6 worker Y8, `.claude/briefs/runs/2026-09-25-lane-r6-y8-mercy-spec.md`) for
espagnol142-mercy-1648 (a 6 June 1648 letter, Spanish court correspondence). Two Internet Archive `_djvu.txt`
full texts of canonical early-17th-c. Spanish prose:

- Cervantes, *Don Quijote de la Mancha* (written/published 1605 and 1615; this scan is an 1876 reprint,
  modern typeface, clean OCR).
- Quevedo, *Vida del Buscón* (written c. 1603-1608, first printed 1626; this scan is a 1911 University of
  Toronto reprint, modern typeface, clean OCR -- a period edition scan of the actual 1626 printing
  (`bub_gb_GPiyjzSqQg8C`) was tried first and rejected: its long-s ("ſ") type OCRs pervasively as "f"
  ("feñor" for "señor"), which would bias letter frequencies; the 1911 reprint carries the same original-era
  text without that OCR artifact).

Both are literary prose, not letters, and neither is this target's own material (or any other cipher
target's) -- unrelated to espagnol142-mercy-1648's plaintext, so scoring a candidate reading against this
corpus is not circular. Front matter (title pages, "Digitized by Google" boilerplate, bare page numbers)
stripped; `donquijote00cervuoft` additionally cut at its own "*** END" OCR trailer. See MANIFEST.tsv for
URLs, byte counts and sha1 of the cleaned text.

Combined: 1,657,520 + 267,109 = 1,924,629 letters after `tools/judge_plaintext.py`'s `fold()`, well over the
~200k floor this job's brief set and the ~300k floor the language check generally needs.

Wired into `tools/judge_plaintext.py`'s `LANG_CORPORA["es"]` (unlike de20/fr19/nl20, there was no existing
`es` default to preserve -- `es` was previously absent from `LANG_CORPORA` entirely, per that file's own
comment). `python3 tools/judge_plaintext.py --selftest` still passes after the edit (the selftest is
corpus-agnostic, so this only confirms the edit didn't break the script's syntax/logic, not the corpus
itself; espagnol142-mercy-1648's own cheap-test run is the first real exercise of the `es` entry).

Requests: archive.org 2 (both djvu.txt downloads, >=1.5s apart, descriptive UA), plus 2 advancedsearch.php
metadata queries and 2 metadata.php lookups to pick the two identifiers above.
