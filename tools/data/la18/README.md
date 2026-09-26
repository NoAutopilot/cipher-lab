# la18: 1680-1740 Polish crown-chancery Latin for the judge's language check

Built 26 Sept 2026 (LANE B7 worker bLAJ, `.claude/briefs/runs/2026-09-26-lane-b7-lajudge.md`) because `"la"`
was commented in `tools/judge_plaintext.py`'s `LANG_CORPORA` as "Not wired" (25 Sept 2026, YX-PTJUDGE):
`tools/data/la_repo` is not a period corpus at all, only a placeholder holding a different target's own
committed reading (`dupuy468-anhalt`) -- circular per CLAUDE.md rule 3 ("never use a target's own reading" as
its corpus) and nowhere near a usable letter count. `ciphers/szembek-bk1560/reading.txt` (18th-c. Polish crown
chancery Latin, catalogued 1698-1731, read via its own interlinear gloss, grade C) needed a real `la` judge to
back rule 7's judge line.

## Source

Internet Archive `_djvu.txt` OCR (Bavarian State Library Google Books scans, `bub_gb_*` identifiers) of all
three volumes of **Andreae Chrysostomi in Zaluskie Zaluski ... Epistolarum historico-familiarium** (Brunsberg,
1709-1711) -- the collected historical-familiar Latin letters of **Andrzej Chryzostom Załuski**, who held the
office of **Crown Referendary, then Crown Vice-Chancellor, then Grand Crown Chancellor of Poland** across
these same years, writing to and about the same royal-chancery milieu as the target (Jan Szembek, Crown Vice-
Chancellor then Crown Chancellor of Poland 1700-1731, under Augustus II). This is as close an era-and-office
match as this repository has built for any language: both authors sat in the same Polish crown chancery within
a few years of each other, writing the same genre (chancery/political prose letters, not fiction, not treaty
boilerplate), in the same institutional Latin register.

| identifier | tomus | year | folded letters |
|---|---|---|---|
| bub_gb_RMM33dayMRYC | I | 1709 | 2,295,642 |
| bub_gb_aVIDeEpVPPYC | II | 1711 | 2,552,418 |
| bub_gb_OI0Su4YVRowC | III | 1711 | 2,420,931 |

**Combined: 7,268,991 letters after `fold()`** -- well over the ~200k floor this job's brief set. See
MANIFEST.tsv for identifiers, byte counts, sha1 and fetch date.

**Confirmed independent of the target, not circular:** tomus II and III mention "Szembek" (2 and 28 hits) --
by name, as **Joannes Szembek, Referendarius Regni** (a real correspondent of Załuski's in the 1700s-1710s,
before he became Crown Chancellor), not the target letter, its cipher, its plaintext, or any decipherment of
it. Checked by eye: every hit is Załuski writing about or to Szembek as a contemporary office-holder (e.g.
"EIUSDEM EPISCOPI VARMIENSIS JOANNI SZEMBEK REFERENDARIO REGNI"), which is exactly the expected background
noise of two chancery officials' correspondence overlapping, not the target's own material. No page of any
volume is the target's ciphertext, gloss, key or reading.

## Cleaning

Each raw `_djvu.txt` was cut to the letters proper:

- **Front matter** (engraved title page, dedication heading, "Digitized by Google"/"Digitized by Googie" OCR
  noise scattered through the scan) cut before each volume's own opening address (`HONORI DEI` t.I line 70,
  `LECTORI` t.II line 122, `4 LECTORI` t.III line 102 of the raw djvu text).
- **Back matter**: each volume ends in an alphabetical subject/name index (`INDEX RERUM`, citation-format
  text: "Zbrozeck fortiter adb contra Sejthas 602", not prose) -- cut at that heading (t.I line 55320, t.II
  line 60654, t.III line 57445), the same reason es17c (25 Sept 2026) cut tomo XIX's cumulative index.
- Lines containing "google" (case-insensitive, 35-200 per volume, OCR page-footer artefacts) removed.
- No other stripping. The OCR itself is noisy (18th-c. long-s and ligatures misread as f/other letters), the
  same class of noise as es17c/pt18's own Google Books scans; not stripped further given the volume of real
  text surrounding it.

## Wired into `tools/judge_plaintext.py`

Added as `LANG_CORPORA["la18"]` and as `LANG_CORPORA["la"]` (the code the szembek-bk1560 spec already names,
previously unwired/commented-out). A future target that wants a different-era Latin corpus can add a new key
and switch its own spec's `"language"` value without disturbing this one. `python3 tools/judge_plaintext.py
--selftest` passes after the edit (corpus-agnostic; only confirms the edit did not break the script).

## Held-out real-prose false-negative rate

`holdout_check.py`: leave-one-file-out (build the model from two of the three tomes, sample 200 windows of
N=400 letters from the third, held-out tome never used to build that model, count how many score at or below
that model's own real_p05 threshold). Run:

```
$ python3 tools/data/la18/holdout_check.py
```

See its printed output, pasted in full below (rule 3's per-fold-spread paragraph: 3 files is on the low side,
same count as es17c, so report per-fold spread alongside the blended rate rather than trusting one number).

```
held_out=zaluski_epistolae_t1.txt.gz N=400 samples=200 real_p05=-0.969 false_negatives=66/200 (33.0%)
held_out=zaluski_epistolae_t2.txt.gz N=400 samples=200 real_p05=-0.980 false_negatives=45/200 (22.5%)
held_out=zaluski_epistolae_t3.txt.gz N=400 samples=200 real_p05=-0.990 false_negatives=8/200 (4.0%)
TOTAL false-negative rate: 119/600 (19.8%)
per-fold spread: 4.0% - 33.0% (3 files: fewer than 5 -- CLAUDE.md rule 3, treat as a corpus of unknown
reliability, not a single trustworthy number)
```

Same shape as es17c's own finding (23.5% blended, 10.0-39.5% spread across 3 tomes of the same multi-tomo
work): the earliest-held-out tome (I, 1709) false-negatives at 8x the rate of the latest (III, 1711),
consistent with real stylistic drift within Zaluski's own corpus across these two years (denser
name/date/administrative passages in some stretches, more narrative prose in others) rather than noise from
switching corpora. **A FAIL against `la`/`la18` at N~400-600 is of unknown reliability by CLAUDE.md rule 3's
own amendment; a PASS is still informative.** A fourth independent volume (a different author/office, same
1680-1740 window -- Leibniz's Codex juris gentium diplomaticus, already checked reachable on archive.org,
`bub_gb_8cMJ0H457Y0C` 1693 / `bub_gb_1PxJc36NoH8C` 1700 Mantissa, not fetched this pass for budget) would both
widen the fold count past the rule-3 floor and add register diversity (treaty/legal Latin instead of only
epistolary prose); left as a named next step rather than done here.

## Excluded

Other candidates found on Internet Archive but not fetched this pass (budget): Leibniz's *Codex juris gentium
diplomaticus* (1693) and its *Mantissa* (1700) -- both real period diplomatic Latin but a different genre
(treaty texts, legal boilerplate, signatory lists) and noisier OCR than the Zaluski scans; a short excerpt
from the 1693 volume was hand-corrected instead for this job's own offline test
(`tools/tests/test_judge_plaintext_lang_la18.py`), confirming it is a real, independent, uncommitted source
rather than fetching and cleaning the whole volume under this job's cap.

