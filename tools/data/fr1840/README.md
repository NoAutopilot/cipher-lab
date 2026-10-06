# fr1840: 1835-1850 diplomatic French (era/register-matched corpus)

Built 6 Oct 2026 (account-4 worker R11-ZESCORP, `.claude/briefs/runs/2026-10-06-account4-run11-jobs.md`) because
`ciphers/zeschau-seebach-1841` (Saxon foreign minister to the St Petersburg legation, French, 1841-42) had no French corpus
on disk of its era and register: `fr1810` is Napoleonic military/official prose 30 years earlier, `fr19` is novels.
R10-ZESCRIB's crib control was a non-test because its Napoleonic plaintext held none of the 1840s formulae
(CLAUDE.md rule 3, the pt18/V6-PTCORP era paragraph).

Five Internet Archive OCR volumes (`_djvu.txt`), see MANIFEST.tsv for identifiers, dates, the raw-line cuts and why
each was chosen: Nesselrode's Lettres et papiers VIII-IX (1840-50), Metternich's Memoires VI (1835-48, French edition),
Guizot's Memoires VI-VII (1840-47). `build.py RAW_DIR` reproduces the gz files from the raw downloads (trim front matter
and the end index, drop running heads and page numbers, join hyphenated breaks); no network in the script. Fetched once,
one request at a time, >= 2 s apart (archive.org: 3 advancedsearch queries, 7 `_djvu.txt` downloads -- one Metternich
item, mmoiresdocumen06mettuoft, turned out to be a mislabelled 1845 War-of-Spanish-Succession volume and was dropped;
Guizot VIII was fetched only for the held-out passage in tools/tests/test_judge_plaintext_lang_fr1840.py).

Combined: 383,767 + 357,612 + 1,117,133 + 652,694 + 660,666 = **3,171,872 letters after fold()**.

Register caveats, stated plainly: Nesselrode's volumes are mostly private political letters (to Meyendorff, to his
wife and son), not formal dispatches; Metternich VI includes Princess Melanie's journal; Guizot's volumes are 1860s
memoir narrative around the dispatches they quote. Raw OCR noise is left in, as in the other corpora.

## Leave-one-file-out false-negative rate (rule 3, es17c/MJ paragraph)

`python3 tools/data/fr1810/holdout_check.py --corpus fr1840 --N 325 --samples 200` (6 Oct 2026, holdout_2026-10-06.log):

| held-out file | real_p05 | false negatives |
|---|---|---|
| lettresetpapiers08ness | -0.860 | 13.5% |
| lettresetpapiers09ness | -0.859 | 15.5% |
| memoiresdocume06mett | -0.853 | 25.0% |
| mmoirespourse06guiz | -0.857 | 10.0% |
| mmoirespourse07guiz | -0.844 | 49.5% |
| blended | | **22.7%** (227/1000), per-fold spread 10.0-49.5% (5.0x) |

Five folds but a wide spread (Guizot VII is the outlier, probably its OCR quality): a judge FAIL/PASS against fr1840 at
N=325 is of unknown reliability until a spec's own register is checked against the folds; read the per-fold numbers.

## First use

`ciphers/zeschau-seebach-1841/crib_rarity.py` (R11-ZESCORP): control plaintext from the held-out Nesselrode VIII, training
for the crib n-grams and the unit inventory from the other four.
