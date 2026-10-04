# tools/data/pl18: Polish prose 1683-c.1790 (Saxon era and neighbours)

Built 4 Oct 2026 by A3V3-SANGP (account 3, LANE-A3V3) for `ciphers/sanguszkow-mniszech-dunin-1714` (Mniszech to
Dunin, Dukla 1714), whose clear anchors are Polish with Latin phrases. `pl19` (Gutenberg fiction 1888-1934) is the
wrong era and register. Judge key: `"language": "pl18"` (wired in `tools/judge_plaintext.py` LANG_CORPORA).

Five Internet Archive `_djvu.txt` files (19th-c. editions of period texts; see `MANIFEST.tsv` for ids, editions,
URLs and folded letter counts), rebuilt by `python3 tools/data/pl18/build.py RAW_DIR`: scanner boilerplate and
French/Latin-dominated lines dropped, hyphenated line breaks joined, Polish letters ą ę ć ł ń ś ź ż pre-folded to
a e c l n s z z (the judge's `fold()` would otherwise drop them outright -- the pl19 ł finding, extended to every
Polish letter outside its FOLD table), each file capped at 650k folded letters from the middle of the body.
Total about 2.27M folded letters. The 1823 Listy keep period spelling (iest, ieżli); the others are 19th-c.
normalised editions, so period orthography is only partly represented. The Google scans (Ojczyste spominki,
Kitowicz) carry OCR noise.

## Leave-one-file-out false-negative rate (rule 3), `judge_plaintext.py --holdout`, 200 windows per fold

| N | blended FN | per-fold FN (Otwinowski / Pasek / Listy Jana III / Ojczyste spominki / Kitowicz) | held-out p05 |
|---|---|---|---|
| 132 | 38.4% | 10.5 / 15.5 / 71.0 / 68.5 / 26.5 | -1.206 |
| 232 | 42.2% | 11.0 / 27.0 / 80.5 / 74.0 / 18.5 | -1.166 |

For comparison, `pl19` at N=232: blended 91.5%, spread 78.5-98.0% (4 folds). pl18 is far better calibrated than
pl19 for this period but the spread is wide: the two outlier folds are the 1823 Listy (period spelling the other
four lack) and the OCR-noisy Ojczyste spominki. By rule 3's fold-count paragraph a p05-gate FAIL/PASS against
`pl18` is of **unknown reliability**; a test that compares a target with a matched control scored through the same
model (as `ciphers/sanguszkow-mniszech-dunin-1714/potocka/potocka_trial.py` does) does not depend on the p05 gate.
A cleaner build would add period-spelling sources (Polona or Wikisource transcriptions of 1700-1730 letters) and
drop or clean the Google scans; not done here.
