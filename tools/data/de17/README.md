# de17: German chancery and diplomatic documents of about 1630-1660 for the judge's language check

Built 3 Oct 2026 (GAPS62, account-4) for `ciphers/riksarkivet-r4282-1628` (a 1628 Swedish-court cipher letter; the
Swedish chancery wrote German as well as Latin, and the Latin homophonic tests failed under la17 and la18), whose German
judge would otherwise fall back to `de` = de16 (an 8.5 KB model-composed text, not a source) or de19/de20 (19th-20th c.).
The pattern is la17's (`tools/data/la17`). Opt in with `"judge": {"language": "de17"}`; `"de"` stays de16.

## Sources (MANIFEST.tsv: identifiers, sizes, sha1, URLs; all public-domain archive.org `_djvu.txt` OCR)

| file | work | documents dated | folded letters |
|---|---|---|---|
| dieverhandlungen01irme | Irmer, Die Verhandlungen Schwedens und seiner Verbuendeten mit Wallenstein und dem Kaiser 1631-1634, vol 1 (1888) | 1631-32 | 450,071 (capped) |
| dieverhandlungen02irme | the same, vol 2 (1889) -- Fraktur OCR, noisiest (s/j, f/s confusions) | 1632-33 | 172,037 |
| dieverhandlungen03irme | the same, vol 3 (1891) | 1633-35 | 450,307 (capped) |
| urkundenundacten1601berluoft | Urkunden und Actenstuecke zur Geschichte des Kurfuersten Friedrich Wilhelm von Brandenburg (1865 vol.) | 1640s-50s | 450,980 (capped) |
| urkundenundacte32kommgoog | the same series, a further volume (Google scan) | 1640s-60s | 450,380 (capped) |

Total **1,973,775 folded letters**, five files from two editions. Irmer prints the Swedish crown's own negotiation papers
(Oxenstierna, Arnim, Thurn, the Saxon and Brandenburg courts) three to six years after the target -- the closest register
on archive.org found this pass. The editors regularise u/v and i/j ("und", not "vnd"), otherwise period spelling stands
(seind, dero, umb, derowegen, undt, feindtlich). Fetched and **dropped**: Urkunden und Actenstuecke, bub_gb_PggKAAAAIAAJ
(OCR noise plus long editorial regests; its leave-one-out fold false-negatived 100 pct at N=1090), Duch, Briefe und Akten
zur Geschichte des Dreissigjaehrigen Krieges (1907, mostly Italian nuncio reports and modern summaries) and Thurn als Zeuge
(1883, unreadable Fraktur OCR). None of the files contains the target, its sibling R4284 or any decipherment of either.
Requests: archive.org 6 searches + 8 downloads.

## Cleaning (build.py)

Long s to s; rejoin hyphenated words; drop lines with "google"; keep OCR lines with >= 4 words; keep 15-line chunks where
German function words are >= 12 pct of tokens AND at least two period-spelling markers occur (seind, dero, umb, derowegen,
nit, uff, sambt, itzo, gnedig ...) -- drops Latin/French/Italian documents and most of the editors' own 1880s prose, which
never uses them; cap each file at 450,000 folded letters. Editorial headnotes inside a kept chunk remain (a known impurity).

## Held-out calibration (3 Oct 2026, CLAUDE.md rule 3 fold-count paragraph)

`holdout_check.py`: leave-one-file-out, 200 windows per held-out file, false negative when a held-out window scores at or
below the in-model real_p05. Logs: holdout_de17_N1090.log, holdout_de17_N300.log, holdout_de17_against_de16_N1090.log.

| check | per fold (Irmer 1, Irmer 2, Irmer 3, Urkunden 1865, Urkunden goog) | blended | spread |
|---|---|---|---|
| de17 LOO, N=1090 | 13.0, 100.0, 25.5, 14.5, 54.0 | 41.4% | 13.0-100.0% (7.7x) |
| de17 LOO, N=300 | 4.0, 97.0, 32.0, 19.5, 38.5 | 38.2% | 4.0-97.0% (24x) |
| de17 files vs de16 model, N=1090 | 100, 100, 100, 100, 100 | 100% | -- |

**Reading.** As with la17, the in-model real_p05 gate is badly calibrated for held-out text at long N: 41 pct of genuine
1630-60 German windows fail it at N=1090, and the Fraktur-OCR Irmer vol 2 fold is the outlier (100 pct). Without that fold
the rate is 13-54 pct. de16 is useless as a judge of real period German (every window fails). By rule 3 a FAIL/PASS against
de17's own real_p05 is of **unknown reliability**; place a candidate against the held-out distribution instead
(`ciphers/riksarkivet-r4282-1628/gaps62/heldout_dist.py`). Offline test: `tools/tests/test_judge_plaintext_lang_de17.py`
(a held-out 1635 deposition passage past the Irmer vol 3 cap passes; shuffled and random fail).
