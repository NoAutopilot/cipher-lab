# la17: Latin letters of about 1590-1649 (scholar-diplomats, the Swedish crown's agents) for the judge's language check

Built 3 Oct 2026 (GAPS57, account-4) for `ciphers/riksarkivet-r4282-1628` (a 1628 Swedish-court cipher letter whose clear
word "expensas" suggests Latin), whose spec fell back to `la`/la18 (Zaluski, Polish crown chancery, 1709-11): CLAUDE.md
rule 3's era paragraph (pt17 vs pt18). The pattern is TOOL-FR17's (`tools/data/fr17`). Opt in with
`"judge": {"language": "la17"}`; `"la"` stays la18.

## Sources (MANIFEST.tsv: identifiers, sizes, sha1, URLs; all public-domain archive.org `_djvu.txt` OCR)

| file | work | letters dated | folded letters |
|---|---|---|---|
| hugonisgrotiiepi00grot | Grotius, Epistolae ineditae to the Oxenstiernas and other Swedes (1806) | 1634-45 | 285,589 |
| hugonisgrotiiad00oxengoog | Grotius to Johan Oxenstierna and J. A. Salvius, and J. Oxenstierna's letters (1829) | 1630s-40s | 118,237 |
| bub_gb_WTkBFjX6G_UC | Bongars and Lingelsheim, Epistolae (1660) | 1590s-1612 | 21,032 |
| bub_gb_FK3cWikzFwsC | Vossius and correspondents, Epistolae (1693) | 1600s-1649 | 650,989 (capped) |
| bub_gb_mBpUAAAAcAAJ | Casaubon, Epistolae (1638) | 1590s-1614 | 650,507 (capped) |
| epistolaecelebe00grotgoog | Epistolae celeberrimorum virorum (Grotius, Vossius, Schottus, Woverius ...; 1715) | 1600s-40s | 114,347 |

Total **1,840,701 folded letters**, six files from five collections. The Swedish-crown Grotius letters are the closest
register to the target (diplomatic news Latin to the Swedish chancery), but they start six years after it; the rest are
scholarly-familiar letters of the same decades. Fetched and **dropped**: Grotius, Epistolae quotquot (1687,
bub_gb_7cDeih1PbMkC -- its scan reads e as c throughout, e 2.7 pct vs c 11.4 pct after filtering) and Ludovicus
Camerarius, Epistolae selectae (1625, 10514355bsb -- 2.7k letters survive the filter). None of the files contains the
target, its sibling R4284 or any decipherment of either.

## Cleaning (build.py)

Rejoin hyphenated words; drop lines with "google"; keep OCR lines with >= 4 words; keep 15-line chunks where Latin
function words are >= 12 pct of tokens AND e >= 1.5 x c (drops vernacular letters, prefaces, indexes, Greek and e/c-mangled
OCR); cap each file at 650,000 folded letters. The long s stays read as f, as in la18's Zaluski scans.

## Held-out calibration (3 Oct 2026, CLAUDE.md rule 3 fold-count paragraph)

`holdout_check.py`: leave-one-file-out, 200 windows per held-out file, false negative when a held-out window scores at or
below the in-model real_p05. Logs: holdout_la17_N1090.log, holdout_la17_N300.log, holdout_la17_against_la18_N1090.log.

| check | per fold (Grotius 1806, Grotius 1829, Bongars, Vossius, Casaubon, Ep. celeb.) | blended | spread |
|---|---|---|---|
| la17 LOO, N=1090 | 33.5, 42.0, 78.0, 100.0, 55.0, 82.0 | 65.1% | 33.5-100.0% (3.0x) |
| la17 LOO, N=300 | 28.0, 17.5, 48.5, 86.0, 41.0, 45.0 | 44.3% | 17.5-86.0% (4.9x) |
| la17 files vs la18 model, N=1090 | 60.0, 77.5, 97.0, 99.5, 73.5, 91.5 | 83.2% | 60.0-99.5% (1.7x) |

**Reading.** The in-model real_p05 gate is badly calibrated for held-out period Latin at long N, under both corpora: at
N=1090 genuine 1590-1649 letters fail it 65 pct of the time under la17 and 83 pct under la18 (the era gap costs about 18
points). The spread is wide (3-5x) and the Vossius fold is the outlier (100 pct at N=1090: its OCR and register differ most
from the rest). By rule 3 a FAIL/PASS against la17 on its own real_p05 is of **unknown reliability**; a FAIL at N around
1000 says little. A fairer gate is the held-out distribution itself (score a candidate against the scores of held-out real
windows, e.g. `ciphers/riksarkivet-r4282-1628/gaps57/heldout_dist.py`: la17 LOO held-out p05 -1.141, p01 -1.241, min
-1.345 at N=1090; la18 model on la17 windows p05 -1.122, p01 -1.214, min -1.283). Offline test:
`tools/tests/test_judge_plaintext_lang_la17.py` (a held-out Vossius passage past the cap passes; shuffled and random fail).
