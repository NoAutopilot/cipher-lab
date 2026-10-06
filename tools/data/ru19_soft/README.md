# tools/data/ru19_soft: Russian with each softened consonant its own letter

Built 3 Oct 2026 (A2P4-KAL4, `.claude/briefs/runs/2026-10-03-acct2-a2p4-kal4.md`, LANE-A2PUSH4, account 2) for
kaliningrad-2015's cycle-4 rank 6 hypothesis (`ciphers/kaliningrad-2015/HYPOTHESES.md`): the plaintext is Russian in a
Latin transliteration in which a softened consonant is one letter, matching the cipher's convention A (an apostrophe
attaches to the sign before it and the pair is one sign, K 36). No network: built from `tools/data/ru19` (Synodal
Bible, 1876 translation, 78 books) through `tools/data/ru19_lat`'s schemes.

**Softening rule.** Start from the S3' (`s3p`) or S3 (`s3`) scheme of `tools/translit_ru.py` (`tools/data/ru19_lat/README.md`):
a paired consonant (б в г д з к л м н п р с т ф х) before я ю ё ь is written consonant + q, then the vowel as a u o
(nothing for ь); S3 also writes q before е и after a paired consonant. A soft sign after an unpaired consonant
(ж ш ч щ ц) is q as in S1. Then `--soft-letters` merges every q into the Latin letter written immediately before it,
upper-cased: nq -> N, tq -> T, lq -> L, khq -> kH (and zhq/chq/shq -> zH/cH/sH: H pools every soft letter whose
Latin spelling ends in h, exactly as the cipher's convention A would pool an apostrophe after the same final sign).
Upper case is a separate letter, never a capital; nothing else is upper-case in these files.

| file | scheme | letters | alphabet (distinct) | soft (upper-case) share |
|---|---|---|---|---|
| s3p_soft.txt.gz | S3' + merge | 3,368,131 | 35: `BDFHLMNPRSTWZ` + 22 base `abcdefghiklmnoprstuwyz` | 2.97 pct |
| s3_soft.txt.gz | S3 + merge | 3,368,131 | 37: `BDFGHKLMNPRSTWZ` + the same 22 | 13.23 pct |

The cipher's convention A carries 88 apostrophe-bearing signs of N 978 (9.0 pct): between the two files, as the
scheme table in HYPOTHESES.md (cycle 4) bounds it.

**Use.** `tools/homophonic_anneal.py --alphabet ru-s3p-soft` (or `ru-s3-soft`), `tools/family_run.py --family
homophonic --param alphabet=ru-s3p-soft`, and the spec's judge block `"alphabet": "ru-s3p-soft"` with these files as
`corpora`. Those alphabet names are defined in `homophonic_anneal.ALPHABETS`; their fold keeps only the alphabet's
characters, case-sensitive.

**Reproduce:** `python3 tools/translit_ru.py --scheme s3p --soft-letters tools/data/ru19 tools/data/ru19_soft/s3p_soft.txt.gz`
(and `--scheme s3 ... s3_soft.txt.gz`); offline, a few seconds. Test: `python3 tools/tests/test_homophonic_alphabet.py`.

**Limits.** Inherits `tools/data/ru19`'s (getbible digitisation, not checked against the 1876 print; Bible register,
OT name lists). The softening rule is this project's hypothesis about a period writer's Latin rendering of Russian, not
a transliteration standard. Judge calibration: measured 3 Oct 2026 (A2P4-KAL5, section below); before that, no leave-one-file-out false-negative rate had been measured for these
corpora (CLAUDE.md rule 3's fold-count lesson); a FAIL/PASS against them is of unknown per-fold reliability. The OT
genealogical windows are hard for the anneal in any alphabet (a K-36 control at offset 200000 read 0.12-0.25 in both
the 24-letter and the 35-letter alphabet, with the true key scoring far above the one found): a search limit of that
register, not of the alphabet.

## Held-out calibration (3 Oct 2026, A2P4-KAL5, CLAUDE.md rule 3 fold-count paragraph)

Each corpus is one file, so folds are 8 book groups rebuilt with the same command from `tools/data/ru19` (Pentateuch
01-05, Historical 06-17, Poetic 18-22, Major prophets 23-27, Minor prophets 28-39, Gospels+Acts 40-44, Epistles+Rev
45-66, Deuterocanon 67-84): `python3 tools/judge_plaintext.py --holdout <folds> --N N --alphabet ru-s3-soft|ru-s3p-soft`,
200 windows per fold. Logs: holdout_s3_N978.log, holdout_s3_N1066.log, holdout_s3p_N1066.log, holdout_s3p_N978.log (R9-KAL6, 6 Oct 2026: blended FN 29.4 pct, folds 9.0-41.0, held-out p05 -0.953, p01 -1.026, min -1.156).

| check | per fold (Pent, Hist, Poet, MajP, MinP, Gosp, Epis, Deut) | blended | spread | held-out p05 / p01 / min |
|---|---|---|---|---|
| s3_soft, N 978 | 33.0, 39.5, 46.0, 35.0, 14.5, 42.5, 47.0, 49.5 | 38.4% | 14.5-49.5% (3.4x) | -0.952 / -1.054 / -1.201 |
| s3_soft, N 1066 | 28.0, 50.0, 55.5, 42.5, 26.5, 52.5, 56.0, 56.0 | 45.9% | 26.5-56.0% (2.1x) | -0.948 / -1.044 / -1.197 |
| s3p_soft, N 1066 | 26.0, 44.0, 45.5, 38.5, 25.0, 46.5, 46.5, 48.5 | 40.1% | 25.0-48.5% (1.9x) | -0.947 / -1.033 / -1.156 |

**Reading.** The in-model real_p05 gate false-negatives about 40 pct of genuine held-out Russian at N about 1000, the
folds disagree by 2-3x, and all 8 folds are one translation (one independent source, below rule 3's ~5): a FAIL/PASS
against real_p05 here is **of unknown reliability**. A fairer gate is the held-out distribution (p05 about -0.95, p01
about -1.05, minimum about -1.20 at N about 1000). Offline test of the option: `tools/tests/test_judge_holdout.py`.
