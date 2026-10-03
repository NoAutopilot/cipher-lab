# tools/data/nl18: Dutch prose 1770-1799, colonial/official register

Built 3 Oct 2026 by NL18-CORPUS (account-4) for `ciphers/na-suriname-map-1781` (J.F.F. Wollant's 1781 Suriname
fortification-survey legends), because `tools/judge_plaintext.py` had no 18th-c. Dutch corpus (`nl20` is 1880-1940
novels, `nl_dev` the 17th-c. Statenvertaling) -- CLAUDE.md rule 3, V6-PTCORP lesson. Seven files from six works,
all printed 1770-1799 and public domain, OCR from the Internet Archive's `_djvu.txt` (one request per file, 1.5 s
apart; 9 metadata + 9 text requests to archive.org, 2 advancedsearch calls, 1 to dbnl.org which answered 200 but was
not used). Details, URLs, years, letters after folding and sha1 in `MANIFEST.tsv`. Total 3,410,852 letters.

Not used: `bub_gb_aYlaAAAAQAAJ` (Reize in de binnenlanden van Suriname, 1799: OCR full of diacritic garbage) and
`aandehoogmogende00unse` (a 1781 petition, 16 KB -- kept out so it can serve as the held-out passage in
`tools/tests/test_judge_plaintext_lang_nl18.py`).

## Build (`build_nl18.py RAW_DIR`)

1. English lines dropped (Google boilerplate).
2. **Long-s repair.** The prints' long s is read as 'f' by the OCR ("Amfterdam", "eerft"), while the target is decoded
   to a round s. Each word with an 'f' takes whichever f->s variant is most frequent in `nl20` (original included, so
   "heeft"/"of" stay); words unattested there get 'f' before c/t/p/k/m/n/w -> 's'. Heuristic: it leaves residual errors
   both ways ("vergift" -> "vergist", "Dansfeeften" half-repaired), and the Google scans carry other OCR noise.

## Reliability (rule 3 fold-count amendment) -- read before trusting a FAIL or PASS

Leave-one-file-out false-negative rate on clean held-out prose (`ciphers/na-suriname-map-1781/judge_nl18.py`,
200 windows per fold, gate = real_p05 and null_p99 of the 6-file model):

| N | blended FN | per-fold spread |
|---|---|---|
| 249 | 26.8% | 9.0-60.0% |
| 277 | 28.1% | 6.0-76.0% |
| 323 | 29.1% | 1.5-69.0% |
| 468 | 30.6% | 9.0-71.5% |
| 605 | 30.7% | 5.5-89.5% |

The outlier fold is the Stedman translation (`bub_gb_mGdCAAAAcAAJ`, 89.5% at N=605), then Ceilon (41.5%) and
Verzameling (35.5%): the worst OCR files are the ones that fail when held out, i.e. the spread is OCR quality more
than register. Seven files is above the ~5-file floor, but the spread is wide, so **a FAIL/PASS against nl18 is of
unknown reliability** by the amendment's own rule. Shuffled windows never pass (null side is fine).

Power against letter error (`judge_nl18_sweep.py`, held-out prose corrupted with random letters): the PASS rate falls
from about 70% clean to 5-17% at 5% error and 0-1% at 10% error, at both N=249 and N=605. **The judge has no power on a
reading whose letter-error rate is above about 5%.** Fixes worth trying next: a cleaner-OCR file set (Delpher-quality
newspaper text 1780s, or dbnl.org transcriptions, which answered HTTP 200 on 3 Oct 2026), or a rate-matched gate.
