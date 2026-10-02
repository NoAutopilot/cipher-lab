# sco16: Middle Scots prose of about 1550-1600 for the judge's language check

Built 2 Oct 2026 (GAPS6-moray-wood-1568, account-4, `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`) for
`ciphers/moray-wood-1568`, Regent Moray's cipher postscript to John Wood of 13 July 1568, which is Middle Scots. No corpus
on disk matched it: `tools/data/en16_repo` is about 104k letters of 1650s English (this repository's Thurloe printed
readings), ninety years later and a different variety, with no README and no fold check until this pass (below).

Sources: Internet Archive OCR full text (`_djvu.txt`) of five 19th-c. editions printed in the original spelling. See
MANIFEST.tsv for identifiers, dates and URLs. Fetched once on 2 Oct 2026, one request at a time, 2 s apart. There were
7 archive.org requests in all: 1 advancedsearch, 1 metadata and 5 downloads.

| file | text | folded letters |
|---|---|---|
| worksofjohnkn01knox | Knox, History of the Reformation, Books I-II (Laing 1846), c.1559-66 | 251,571 |
| worksofjohnkn02knox | Knox, History, Books III-V, with letters and acts (Laing 1848), c.1560-67 | 404,372 |
| adiurnalremarka00thomgoog | A Diurnal of Remarkable Occurrents, 1513-1575 (Bannatyne Club 1833), long-s repaired | 526,812 |
| historielifeofki00colvuoft | The Historie and Life of King James the Sext, c.1566-96 (Bannatyne Club 1825) | 443,182 |
| registerofprivyc0002jjoh | Register of the Privy Council of Scotland vol. 2, 1569-78 (Burton 1878), capped | 700,797 |

Total 2,326,734 folded letters. No file holds more than 30.1 pct.

Cleaning is done by `build.py`. Words hyphenated across lines are rejoined. Long s is repaired in the Diurnal only, with
es18's rule ("caftell" 305 -> "castell" 302, "faid" 590 -> "said" 587). A line is kept only with 4 or more words, mostly
in the vocabulary of the four long-s-free files. Kept lines are then grouped in chunks of 15, and a chunk is kept only when
its Scots spelling markers (thair, thame, quhilk, quha, sall, efter, nocht ...) are at least as many as its modern-English
markers (their, them, which, who, shall, after, not ...). That drops the editors' introductions and notes. Each file is
capped at 700,000 letters, which only bites on the Privy Council volume. The raw files are not committed; re-fetch them
from the MANIFEST URLs as `raw_<identifier>.txt` and run `python3 tools/data/sco16/build.py --raw DIR`.

Excluded: vol. 1 of the Privy Council Register (1545-1569, the target's own year), any Moray-to-Wood letter, anything from
`ciphers/moray-wood-1568`, and the peer repositories' own Scots corpora.

## Leave-one-file-out false negatives at N=134 (rule 3 fold-count paragraph)

`python3 tools/data/sco16/holdout_check.py --lang sco16` (log: holdout_sco16_N134.log):

| held out | real_p05 of the other four | held-out windows at or below it |
|---|---|---|
| Knox I | -0.929 | 33.0 pct |
| Knox II | -0.872 | 57.5 pct |
| Diurnal | -0.899 | 53.0 pct |
| James the Sext | -0.903 | 26.5 pct |
| Privy Council II | -0.880 | 16.0 pct |

Blended 37.2 pct (372/1000), per-fold spread 16.0-57.5 pct, five folds. **A FAIL against sco16 at N of about 134 is of
unknown reliability.** Unfixed Scots spelling at a short window makes about a third of unseen genuine prose fall below
the in-sample p05. A PASS is the stronger signal, and the shuffled-target band is the comparison to read beside any FAIL.

For en16_repo at the same N (`--glob 'tools/data/en16_repo/*.txt'`, log holdout_en16_repo_N134.log) the blend is 21.9 pct,
but the per-fold spread is 0.0-100.0 pct over 17 folds. Its real_p05 sits near -0.60, because the fauconberg files overlap
one another. It is not a usable judge corpus for a 16th-c. text.
