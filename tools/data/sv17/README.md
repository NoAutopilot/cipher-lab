# sv17: Swedish chancery letters of about 1620-1650 for the judge's language check

Built 3 Oct 2026 (GAPS67, account-4) for `ciphers/riksarkivet-r4282-1628` (a 1628 Swedish-court cipher letter whose
homophonic tests into Latin, German and French were each control-backed negatives), which had no Swedish corpus at all
(`tools/data` had none before this). The pattern is de17's / la17's. Opt in with `"judge": {"language": "sv17"}`.

## Sources (MANIFEST.tsv: identifiers, sizes, sha1, URLs; all public-domain archive.org `_djvu.txt` OCR of Google scans)

*Rikskansleren Axel Oxenstiernas skrifter och brefvexling* (AOSB, Kongl. Vitterhets Historie och Antiqvitets Akademien,
1888-1897), six volumes. The `docs_dated` column is the three commonest 16xx years in each OCR text, not a title-page
reading (the Google scans' metadata gives no volume number); the held-out test passage from 00palagoog is a 1632 field
letter, so the ranges are indicative only.

| file | commonest years in OCR | folded letters kept |
|---|---|---|
| rikskanslerenax00akadgoog | 1625-1627 | 268,185 (all that passed the filter) |
| rikskanslerenax00palagoog | 1644-1646 (also 1632 letters) | 450,401 (capped) |
| rikskanslerenax00styfgoog | 1629-1631 | 450,977 (capped) |
| rikskanslerenax01palagoog | 1617-1639 | 450,128 (capped) |
| rikskanslerenax02akadgoog | 1635-1638 | 450,889 (capped) |
| rikskanslerenax03akadgoog | 1640-1645 | 450,256 (capped) |

Total **2,520,836 folded letters**, six files from one edition (one edition only: a rule 3 caveat -- every fold is
AOSB, so the leave-one-out spread measures volume-to-volume, not edition-to-edition variation). Fetched and **dropped**:
rikskanslerenax01styfgoog (letters to the chancellor in German; 18 "och" in 2 MB). rikskanslerenax01akadgoog answered
HTTP 500 once and was not retried. *Svenska riksradets protokoll* (named in the brief) is not on archive.org under that
title (two title searches, 0 hits); not tried on runeberg.org. A grep of the six raw texts for R4282's own clear-Latin
phrases (futurus status dubitatur, tractatus magnas, Mittatur nobis responsum) found only unrelated uses of "dubitatur"
in Latin letters, which the filter removes anyway. Requests: archive.org 4 searches + 8 downloads (12), 1.6 s apart.

## Cleaning (build.py)

Long s to s and å to a (judge_plaintext.fold has no å and would drop the letter; ä and ö fold to ae/oe there); rejoin
hyphenated words; drop lines with "google"; keep OCR lines with >= 4 words; keep 15-line chunks where Swedish function
words are >= 12 pct of tokens AND at least three period-spelling markers occur (medh, uthi, thet, migh, sigh, effter,
haffuer, hwad, ähr, doch, sampt ...) -- drops the Latin, German and French letters and most of the editors' own 1880s
Swedish (med, det, mig, efter, hafva); cap each file at 450,000 folded letters. Editorial headnotes inside a kept chunk
remain (a known impurity), and the Google-scan OCR is noisy (h/b, n/u confusions in places).

## Held-out calibration (3 Oct 2026, CLAUDE.md rule 3 fold-count paragraph)

`holdout_check.py`: leave-one-file-out, 200 windows per held-out file, false negative when a held-out window scores at or
below the in-model real_p05. Logs: holdout_sv17_N1090.log, holdout_sv17_N300.log.

| check | per fold (00akad, 00pala, 00styf, 01pala, 02akad, 03akad) | blended | spread |
|---|---|---|---|
| sv17 LOO, N=1090 | 67.0, 48.5, 32.0, 51.5, 17.0, 73.0 | 48.2% | 17.0-73.0% (4.3x) |
| sv17 LOO, N=300 | 33.5, 31.5, 16.5, 39.5, 9.5, 54.5 | 30.8% | 9.5-54.5% (5.7x) |

**Reading.** As with la17 and de17, the in-model real_p05 gate is badly calibrated for held-out text at long N: about
half of genuine AOSB windows fail it at N=1090. By rule 3 a FAIL/PASS against sv17's own real_p05 is of **unknown
reliability**; place a candidate against the held-out distribution instead
(`ciphers/riksarkivet-r4282-1628/gaps67/heldout_dist.py`). Offline test: `tools/tests/test_judge_plaintext_lang_sv17.py`
(a held-out 1632 field-letter passage past the 00palagoog cap passes; shuffled and random fail).
