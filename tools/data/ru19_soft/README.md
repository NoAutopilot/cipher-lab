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
a transliteration standard. Judge calibration: no leave-one-file-out false-negative rate has been measured for these
corpora (CLAUDE.md rule 3's fold-count lesson); a FAIL/PASS against them is of unknown per-fold reliability. The OT
genealogical windows are hard for the anneal in any alphabet (a K-36 control at offset 200000 read 0.12-0.25 in both
the 24-letter and the 35-letter alphabet, with the true key scoring far above the one found): a search limit of that
register, not of the alphabet.
