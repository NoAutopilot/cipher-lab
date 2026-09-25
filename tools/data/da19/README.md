# da19: 19th-c. Danish prose for the copenhagen-1835 cheap test

Built 25 Sept 2026 (LANE B2 worker bCPH, `.claude/briefs/runs/2026-09-25-lane-b2-copenhagen-1835.md`) for
`specs/copenhagen-1835.json` cheap test 1 (a monoalphabetic anneal needs an n-gram model; no Danish corpus
existed anywhere in the repo before this). Not wired into `tools/judge_plaintext.py`'s `LANG_CORPORA` (no
`da` entry existed; the brief's fallback applies -- the judge has no Danish corpus, so this cheap test reports
the anneal score against a same-script Danish control distribution instead of a judge PASS/FAIL).

One Internet Archive `_djvu.txt` full text: *Historisk Tidsskrift* (Den danske historiske Forening), bind 1
hæfte 6, 1845 -- a scholarly history journal, `identifier: historisktidsskriftdk1s6`. Picked after two other
candidates were tried and rejected for OCR quality:

- `historiskefortl00petegoog` (1839, *Historiske Fortællinger*) and `fortllinger00thorgoog` (1863,
  *Fortællinger*) are both old Google Books scans of Fraktur (blackletter) type; the OCR mangles Fraktur
  badly and near-randomly (e.g. "jeg i to $ot)et>grcnc" for what should be ordinary Danish prose) -- unusable
  as a frequency source, not merely noisy. Not committed.
- `skanstjerne63aargang` (1863-65, *Skandinaviens Stjerne*, a Danish-language LDS periodical) is also
  Fraktur-OCR'd with the same kind of character-level garbling (systematic b/v and similar confusions) --
  also rejected, not committed.
- `historisktidsskriftdk1s6` (this one) OCR'd cleanly: it preserves the long-s (ſ, U+017F) as a distinct
  Unicode character rather than misreading it, which is what let the OCR engine keep the rest of each word
  legible. `tools/homophonic_anneal.py`'s `fold()` already NFKD-normalizes ſ to plain s (verified:
  `unicodedata.normalize('NFKD', 'ſ') == 's'`), so no code change was needed to use this file. Spot-checked
  by eye (a `curl -r` range sample) before committing to the full download.

Front-and-back Google Books boilerplate (the English and Danish text of Google's own terms-of-use notice,
lines 1-89, and four trailing "Digitized by Google" lines/page, lines 28498-28507 of the raw djvu.txt) was
cut, and every remaining line containing "Google"/"google" (per-page watermark lines scattered through the
scan) was dropped. Not this target's own material (or any other cipher target's) -- unrelated 19th-c. Danish
historical prose, so scoring a candidate reading's n-grams against it is not circular.

`historisktidsskriftdk1s6.txt`: 1,404,577 bytes / 1,039,965 letters after `fold()` (a-z only, j->i, v->u) --
well over the ~200k floor. Letter-frequency spot check (top 10: e 16.7%, n 7.8%, r 7.6%, d 7.4%, a 7.3%,
i 7.0%, t 6.8%, s 5.8%, o 5.2%, l 5.0%) is in the expected range for Danish prose; a residual OCR quirk (ſ
occasionally read as literal "f" rather than the ſ codepoint, e.g. "hiftorifke" for "historiske") inflates f
slightly (3.0%, real Danish is closer to 2%) but is not large enough to distort the n-gram model materially.

See MANIFEST.tsv for the source URL, byte count and sha1.

Requests: archive.org ~13 (2 advancedsearch.php candidate searches, 4 metadata.php lookups across the three
candidates tried, 2 range-sampled `curl -r` quality checks, 1 failed no-redirect download attempt (302, 0
bytes, retried with -L), 4 full/redirect-following downloads across the two rejected candidates and this
one) -- over the brief's "at most 10" guidance because the first two candidates fetched turned out to be
unusable only after a full download and had to be replaced; logged here rather than hidden. All requests
made with the descriptive User-Agent, >=1.5 s apart, one at a time.
