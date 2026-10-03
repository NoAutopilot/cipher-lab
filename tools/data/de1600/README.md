# de1600: German princely letters and chancery acts of about 1575-1611 for the judge's language check

Built 3 Oct 2026 (CORP-DE16, account-4) for `ciphers/decode-1411-hhsta-vienna-1600` (HHStA Kt. 14 Fasc. 20, a German
Habsburg court/chancery cipher letter of c.1575-1600), whose judge under de17 (1630-1660) could not recognise even the
leaf's own period gloss (GAPS150). The pattern is de17's (`tools/data/de17`). Opt in with `"judge": {"language": "de1600"}`;
`"de"` stays de16 (an 8.5 KB model-composed text, `tools/data/de16`, not a source -- this corpus is named de1600 so as not to
collide with that folder).

## Sources (MANIFEST.tsv: identifiers, sizes, sha1, URLs; all public-domain archive.org `_djvu.txt` OCR)

| file | work | documents dated (year frequency in the OCR) | folded letters |
|---|---|---|---|
| briefedespfalzgr01joha | Bezold, Briefe des Pfalzgrafen Johann Casimir, vol 1 (1882) | 1575-1582 | 192,347 |
| briefedespfalzgr02joha | the same, vol 2 (1884) | 1582-1586 | 181,066 |
| bub_gb_zc4FAAAAQAAJ | Briefe und Acten zur Geschichte des Dreissigjaehrigen Krieges (Munich series), a volume | 1599-1608 | 205,681 |
| bub_gb_6M4FAAAAQAAJ | the same series, a volume | 1607-1609 | 194,751 |
| briefeundactenz01mayrgoog | the same series, a volume | 1609-1610 | 189,784 |
| bub_gb__s4FAAAAQAAJ | the same series, a volume | 1610 | 190,294 |

Total **1,153,923 folded letters**, six files from two editions (the per-volume cap of 450k was never reached; the filter
binds first). The IA metadata does not carry the series volume numbers; the date column is the most frequent years in each
OCR text. Fetched and **dropped**: Klarwill, Fugger-Zeitungen 1568-1605 (fuggerzeitungenu00klaruoft, 1923 -- the editor
modernises the spelling, wrong register for a spelling-level n-gram model); Kluckhohn, Briefe Friedrich des Frommen
(bub_gb_3U8VAAAAYAAJ, 1567-1572 -- Fraktur OCR unreadable); Briefe und Acten briefeundactenz00mayrgoog (1611) kept out as the
offline test's held-out source. The Deutsches Textarchiv was reachable but its catalogue lists 100 works per page and its
first pages showed only devotional and literary prints for 1565-1635, so no DTA text was used. None of the files contains the
target, its fascicle siblings (Kopal 2023's Chodkiewicz letters, ff. 174-212) or any decipherment of them.
Requests: archive.org 4 searches + 8 metadata + 9 downloads = 21; deutschestextarchiv.de 3 (API page, list, timeline).

## Cleaning (build.py)

Long s to s; rejoin hyphenated words; drop lines with "google"; keep OCR lines with >= 4 words; keep 8-line chunks where
German function words are >= 12 pct of tokens AND at least two strictly period spellings occur (vnd, dz, seind, dero, umb,
nit, uff, alß, sambt, itzo, gnedig, underthenig, wöllen, het, ime, inen, irer, khay, mt, vns, wirdt, maist, dise, gwalt ...
-- words the 1870s-1880s editors never write). A stricter run (>= 4 markers) kept only 50-75k letters per file; >= 2 keeps
about 190k. Editorial regest lines inside a kept chunk remain (a known impurity, as in de17).

## Held-out calibration (3 Oct 2026, CLAUDE.md rule 3 fold-count paragraph)

`holdout_check.py` (the de17 copy): leave-one-file-out, 200 windows per held-out file, false negative when a held-out window
scores at or below the in-model real_p05. Logs: holdout_de1600_N176.log, holdout_de1600_N62.log, holdout_de17_N176.log.
N=176 is R1411's GAPS146 decode length; N=62 its glossed-letter count.

| check | per fold (Casimir 1, Casimir 2, B&A 1599-1608, B&A 1607-09, B&A 1609-10, B&A 1610) | blended | spread |
|---|---|---|---|
| de1600 LOO, N=176 | 31.0, 38.5, 22.0, 18.0, 56.5, 17.0 | 30.5% | 17.0-56.5% (3.3x) |
| de1600 LOO, N=62 | 16.5, 29.0, 18.5, 15.0, 44.5, 20.0 | 23.9% | 15.0-44.5% (3.0x) |
| de17 LOO, N=176 (for comparison; its own five folds) | 13.5, 91.0, 32.0, 17.5, 40.5 | 38.9% | 13.5-91.0% (6.7x) |

**Reading.** Tighter than de17 (no 91-100 pct outlier fold) but still a wide spread and a high blended rate: about one genuine
1575-1610 window in four fails the in-model real_p05 gate at these short lengths. By rule 3 a FAIL/PASS against de1600's
own real_p05 is of **unknown reliability**; place a candidate against the held-out distribution (as gloss_calibration.py
does) rather than the single gate.

## Calibration on R1411's own period gloss (gloss_calibration.py, log gloss_calibration_r1411.log)

The leaf's 62 interlinear gloss letters (`ciphers/decode-1411-hhsta-vienna-1600/gaps150/gloss_text.txt`, as GAPS141/150
reconciled them), no decode scored:

| corpus | gloss score | real_p05 | null_p99 | letter-shuffled gloss mean / max |
|---|---|---|---|---|
| de17 | -1.524 (FAIL; reproduces GAPS150) | -0.911 | -1.748 | -2.202 / -1.781 |
| de1600 | -1.423 (FAIL) | -0.917 | -1.731 | -2.111 / -1.773 |

Under each de1600 leave-one-out model the gloss scores -1.39 to -1.47 and sits at or below only 0-1 of 200 genuine held-out
N=62 windows (lowest genuine window per fold -1.21 to -1.65). The era-matched corpus moves the gloss up by 0.10, and both the
gloss and the corpus's own held-out windows moved, but the gloss is still below 99.5 pct of real period text: **the corpus era
is not what keeps the judge from recognising this leaf's text**. The likelier limit is the gloss transcription itself (the
open r/z and h/s letterforms, GAPS150; abbreviations; possible names or a non-running gloss), which no corpus fixes. A gate on
the R1411 decode should be placed against the gloss's own score and the shuffled controls, not against real_p05.
