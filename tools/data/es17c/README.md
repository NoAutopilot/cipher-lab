# es17c: 1643-1647 Spanish court-newsletter prose for the judge's register check

Built 25 Sept 2026 (LANE R6 worker MJ, `.claude/briefs/runs/2026-09-25-lane-r6-mj-mr-mercy-judge.md`) because
`tools/data/es17` (Cervantes' *Don Quijote*, Quevedo's *Buscón*) is literary fiction of the right *language* but
the wrong *register*: M2's graded reading of espagnol142-mercy-1648 (a 6 June 1648 chancery/diplomatic letter)
FAILs the es17 judge, and so do **the letter's own clear words** (-0.892 vs real_p05 -0.888, essentially at the
boundary) -- CLAUDE.md rule 3's V6-PTCORP lesson: a language corpus can be the wrong era or register even when
it is the right language.

## Source

Internet Archive `_djvu.txt` OCR of three volumes of *Memorial histórico español: colección de documentos,
opúsculos y antigüedades que publica la Real Academia de la Historia* (Madrid), specifically three of the seven
tomes of **"Cartas de algunos PP. de la Compañía de Jesús sobre los sucesos de la Monarquía entre los años de
1634 y 1648"** -- a contemporary Spanish newsletter/avviso correspondence about the political, military and
diplomatic affairs of the Spanish Monarchy, written to (and by) Jesuit fathers over fourteen consecutive years:

| identifier | MHE tomo | Cartas tomo | date range | folded letters |
|---|---|---|---|---|
| memorialhistri17realuoft | XVII | V | Feb 1643 - end 1644 | 717,113 |
| memorialhistri18realuoft | XVIII | VI | c.1645-1647 (per its own front matter, "sesto" of the Cartas) | 719,360 |
| memorialhistri19realuoft | XIX | VII (last) | 17 Feb 1645 - 4 Jun 1647 | 662,800 |

**Combined: 2,099,273 letters after `fold()`** -- well over the ~200k floor this job's brief set, and over the
es17 corpus's own 1.92M. See MANIFEST.tsv for URLs, byte counts and sha1.

This is a much closer register match to the target than es17: both are prose *letters* (not fiction) about
*contemporary war, diplomacy, troop levies and court affairs* (the same subject matter as the target: recruiting
troops, credential letters, an elector, a negotiation), written within 1-5 years of the target's own 6 June
1648 date, by the same general milieu (Spanish crown administration and its correspondents in the 1640s), not
a 1605-1626 novel.

## Hold-out check (per the brief's rule)

Grepped all three raw volumes for "Mercy", "Mercij", "Barneton", "Sumiller" and "Brandenburg" before cleaning.
Results, checked by hand against context -- **none of the hits are the target letter, its reply, or plausibly
connected to it**:

- **"Mercy"**: every hit in tomes XVIII/XIX is **Franz von Mercy** (French: François de Mercy), the
  Bavarian-Imperial general killed at the second Battle of Nördlingen in 1645 ("Francoís de Mercy, caballero
  lorenés... fué muerto mas adelante en la batalla de Nordlinghen") -- a different person from the target's
  addressee, the **Baron de Mercy, Sumiller de Cortina** to a Spanish prince, in 1648.
- **"Barneton"**: zero hits in any of the three volumes.
- **"Sumiller"**: hits are generic references to the court office ("sumiller de corps", "sumiller de cortina")
  held by other named individuals (D. Fernando ..., el Marqués de Croy as sumiller de cortina *del
  Infante-Cardenal*, whose household ended with his death in 1641) -- not the target's addressee.
  "Infante-Cardenal" further dates that Croy reference to before 1641, seven years before the target letter.
- **"Brandenburg"**: not searched as a single hold-out signal on its own merit (it is a common, generic term in
  any Thirty Years' War newsletter of this decade -- the Elector of Brandenburg appears constantly regardless
  of this specific letter) but checked anyway: no hit sits near "Cheureuse"/"Chevreuse", "Cleves", "tres mil
  hombres" or any other of the target's distinctive phrases. The handful of "Chevreuse" hits in tomo XIX are
  all in that volume's own cumulative seven-tomo name index (see below), citing earlier volumes/pages for the
  Duke and Duchess of Chevreuse as historical figures, not the 1648 letter.

No page of any of the three volumes could hold the target letter or its reply. Not flagged in ROOM.md (nothing
to flag).

## Cleaning

Each raw `_djvu.txt` was cut to the actual letter text only:

- **Front matter** (title page, "LIBRARY / UNIVERSITY OF TORONTO" ownership stamp, OCR garbage from an
  illustrated/blank leaf) cut before the volume's own `CARTAS` section heading (line 60 of tomo XVII, 66 of
  tomo XVIII, 52 of tomo XIX in the raw djvu text).
- **Tomo XIX only**: cut *after* its own `FIN.` (end of the letters proper, raw line 20453) to drop the
  volume's back matter -- a 92-page **cumulative alphabetical name index for all seven tomos of the Cartas**
  ("índice alfabético de nombres propios y materias contenidas en estos siete tomos de Cartas de Jesuitas"),
  which is citation-format text (`Alarcon (D. Francisco...). I 38, 92. II 46, 485...`), not prose, and would
  have polluted the n-gram model with proper-noun/Roman-numeral citation strings rather than sentences.
- No other stripping. As with pt18 (V6-PTCORP), scattered low-volume OCR noise (broken hyphenation, stray
  library stamps, a handful of footnote markers) remains and was judged not worth further stripping given the
  size of the surrounding real text.

## Wired into `tools/judge_plaintext.py`

Added as a **new, separate key `LANG_CORPORA["es17c"]`**, not a replacement for `"es"` (es17 stays the
default for `"language": "es"`, per this job's brief: "keep es17 the default"). A spec opts in with
`"judge": {"language": "es17c", ...}`. `python3 tools/judge_plaintext.py --selftest` passes after the edit
(selftest is corpus-agnostic; it only confirms the edit didn't break the script).

## Held-out real-prose false-negative rate

`holdout_check.py`: leave-one-file-out (build the model from two of the three files, sample 200 windows of
N=519 letters -- matching the target's own code-only reading length -- from the third, held-out file never
used to build that model, and count how many score at or below that model's own real_p05 threshold):

```
held_out=memorialhistri17realuoft.txt.gz N=519 samples=200 real_p05=-0.847 false_negatives=79/200 (39.5%)
held_out=memorialhistri18realuoft.txt.gz N=519 samples=200 real_p05=-0.866 false_negatives=42/200 (21.0%)
held_out=memorialhistri19realuoft.txt.gz N=519 samples=200 real_p05=-0.892 false_negatives=20/200 (10.0%)
TOTAL false-negative rate: 141/600 (23.5%)
```

**This is notably higher than pt18's 4.0% (V6-PTCORP).** Reported as found, not smoothed over: the three
volumes are less internally uniform than pt18's four periodical volumes -- tomo XVII (Feb 1643-1644, held out
first) false-negatives at nearly 4x the rate of tomo XIX (1645-1647, held out last), suggesting real
stylistic drift across these three tomes (different correspondents, or denser/sparser passages of names,
dates and administrative detail versus narrative). A FAIL against es17c is therefore **less trustworthy as a
negative signal than a FAIL against pt18 was** for the Linhares target; a PASS would still be informative,
but this corpus's own real-text threshold has real internal noise. Flagged here for whoever next tunes this
corpus (a fourth, more homogeneous volume, or splitting by correspondent/date, would likely tighten it).

## Judge output, clear words and the reading, against es17c (rule 7, pasted)

Spec variant `{"judge": {"language": "es17c", "letters_min": 200, "control_samples": 200}}` (not committed as
a separate `specs/` file -- see `ciphers/espagnol142-mercy-1648/NOTES.md`'s MJ section for the exact commands
and full pasted output; the file used to run it lived only in scratch and is reproducible from this line).

```
clear words only (m2/clear_words_only.txt, N=782): FAIL language: score=-0.891, null_p99=-1.944, real_p05=-0.867, real_median=-0.787
reading, codes only (m2/reading_codes_only.txt, N=519): FAIL language: score=-1.052, null_p99=-1.928, real_p05=-0.874, real_median=-0.786
full reading.txt (N=1341): FAIL language: score=-1.04, null_p99=-1.998, real_p05=-0.87, real_median=-0.794
```

**Register-matching es17c did not flip the FAIL to a PASS, on the clear words or the reading.** The letter's
own clear words score -0.891 against es17c's real_p05 of -0.867 (a 0.024 gap) versus -0.892 against es17's
-0.888 (a 0.004 gap) -- essentially the same borderline FAIL either way, if anything a slightly wider gap on
es17c. Combined with the 23.5% held-out false-negative rate above, the honest read is: **the register-mismatch
hypothesis from M2's NOTES.md is not confirmed by this corpus** -- swapping Cervantes/Quevedo for contemporary
Jesuit newsletters did not rescue the calibration the way pt18 rescued Linhares. Two explanations are left
open for the next worker, neither tested here: (a) N=519-782 is short enough that any add-k 4-gram real_p05
threshold is noisy regardless of corpus (this check's own 10-40% false-negative spread across held-out tomes
at this N supports that), or (b) the letter's own idiom (heavy abbreviation, place/person names, a terse
secretarial register even by 1640s standards) genuinely scores lower than continuous narrative prose on any
corpus tried so far, independent of era.

## Excluded

Not fetched: CODOIN (Colección de documentos inéditos para la historia de España, ~112 volumes) -- searched by
title only (`title:(coleccion documentos ineditos historia espana)`), no volume identified by title alone as
covering the Spanish plenipotentiaries' Münster correspondence specifically (the brief's other named lead);
not ruled out, just not found within this job's 40-minute/archive.org-only box -- a named volume number from a
future search is the cheap next step, not a blind fetch-and-check of 112 volumes. Also not used: the "Sor
María de Ágreda y Felipe IV" royal correspondence (found via search, archive.org id A333171 among others) --
a real period match but a personal/devotional-political register (letters between the King and a nun-adviser),
further from a chancery-office minute than the Jesuit newsletters, and not fetched.

Requests this pass: archive.org 3 advancedsearch.php metadata queries, 3 `/metadata/<id>` lookups, 3
`_djvu.txt` downloads (302-redirected, `-L` needed), all >=1.6s apart, descriptive UA.
