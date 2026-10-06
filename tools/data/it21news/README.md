# it21news: modern Italian prose (news, 2005-2026) for the judge's language check and as an LM

Built 6 Oct 2026 (R12D-ERBA3, LANE LANE-RUN12-account-4, `.claude/briefs/runs/2026-10-06-account4-run12-jobs.md`) because
`tools/data` held only 16th-century (`it16`, `it16dip`) and 1800-1830 (`it19`) Italian, and erba-2006 is a 2013 private
note. Method: V6-PTCORP's shape (one file per fold, capped, LOFO spread reported).

Source: the Italian Wikinews (Wikinotizie) XML dump `itwikinews-latest-pages-articles.xml.bz2` (dumps.wikimedia.org, dump of
1 Oct 2026, one request on 6 Oct 2026, sha1 in MANIFEST.tsv; the raw dump is not committed -- re-fetch it and run
`build.py --dump FILE` to rebuild byte-for-byte from the same dump). Licence: CC BY 2.5, attribution to the Wikinotizie
contributors (it.wikinews.org); the derived folded text keeps that licence. Late-20th-century Italian prose in the public
domain is essentially unavailable (copyright), so an openly licensed 21st-century source was used; it is closer to the
target's own date (2006-2013) than any 20th-century source would be.

`build.py`: main-namespace articles with a `{{data|... YYYY}}` template; wikitext stripped; paragraphs of >= 25 words with
Italian function-word share >= 22% kept; folded (no accents, lower case, letters and spaces); five year-folds, each capped at
500,000 folded letters: y2005_06, y2007, y2008, y2009_10, y2011_26 = **2,499,935 letters**. LANG_CORPORA key `it21news`
in `tools/judge_plaintext.py` (not the default `it`).

**Register caveat:** news reporting (politics, sport, science, crime), not private letters or love notes; quotes inside
articles are the only first-person speech. A gate on a private note against this corpus is era-matched, not register-matched.

## Calibration (rule 3 fold-count paragraph), 6 Oct 2026, 200 windows per fold

`python3 tools/judge_plaintext.py --holdout tools/data/it21news/*.txt.gz --N <N> --samples 200` (output: holdout_output.txt)

| N letters | blended LOFO false-negative | per-fold (05-06 / 07 / 08 / 09-10 / 11-26) |
|---|---|---|
| 114 | 14.1% | 16.0 / 8.0 / 12.5 / 13.0 / 21.0 (spread 8.0-21.0) |
| 300 | 18.7% | 30.0 / 15.5 / 11.0 / 16.0 / 21.0 (spread 11.0-30.0) |

Five folds of one source and one register, spread under 3x: tighter than it19 (9.5-65.5% at N=1000) or es17c, but the folds
are years of the same site, not independent authors, so the spread understates between-register variance. Treat a FAIL near
the gate as of limited reliability, and a FAIL on a letter-register text as not register-calibrated.
