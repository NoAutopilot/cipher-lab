# fr18: French diplomatic and official prose of about 1680-1790, for the judge

Built 25 Sept 2026 (LANE ZX2 worker ZX2-FR18, `.claude/briefs/runs/2026-09-25-lane-zx2-fr18.md`) because this
lane's French targets (clair1161 1688, clairambault296 1713, hellen 1752, destaing-gerard-1779) would otherwise
be judged against `tools/judge_plaintext.py`'s `LANG_CORPORA["fr"]` default (`tools/data/fr16`, letters of
Catherine de Médicis, 16th century) or `fr19` (19th-century novels) -- both the wrong era and the wrong register
for late-17th/18th-century diplomatic correspondence (CLAUDE.md rule 3, the pt17 -> pt18 lesson).

Internet Archive OCR full text (`_djvu.txt`) of six volumes across three French sources, all named in the job
brief, all diplomatic-memoir, court-letter or official-gazette register, no fiction or verse:

- **Mémoires de monsieur de Torcy** (Jean-Baptiste Colbert, marquis de Torcy, Louis XIV's foreign minister,
  1665-1746), *pour servir a l'histoire des négociations depuis le Traité de Ryswyck jusqu'à la Paix d'Utrecht*,
  1757 edition, tomes I-II (identifiers `memoiresdemonsie01torc`, `memoiresdemonsie02torc`)
- **Mémoires du duc de Villars** (Claude Louis Hector de Villars, marshal of France, 1653-1734), 1758 edition,
  tomes I-II (identifiers `mmoiresduducde01invill`, `mmoiresduducde02vill`)
- **Mémoires et lettres de Madame de Maintenon** (Françoise d'Aubigné, marquise de Maintenon, 1635-1719),
  1778 edition, the volume containing the fifth tome of her Lettres (identifier `mmoiresetlettre01margoog`)
- **La Gazette de France**, the crown's official gazette, issues of January-June 1786 (identifier
  `lagazettedefran01unkngoog`)

See `MANIFEST.tsv` for per-file identifier, title, date, URL, letter counts after folding, fetch date and why
each was chosen. Fetched once, one request at a time, >=1.6 s apart (8 archive.org requests total: 4 IA
`advancedsearch.php` candidate searches, 4 `archive.org/metadata` lookups on the shortlist before fetching, and
6 `_djvu.txt` downloads for the committed files, plus 2 more for two volumes checked but not committed --
`memoiresdemonsie03torc`, held out for the offline test below, and the `recueildesinstr00diplgoog` volume
excluded per the note below).

Combined: 255097 + 285208 + 367845 + 304538 + 278017 + 866031 = **2,356,736 letters after fold()** -- well
over the 1,000,000-letter floor this brief set. No single source is more than 36.7 pct of the total (La
Gazette de France); the smallest is 10.8 pct (Torcy tome I). Two volumes were added beyond the minimum four
sources specifically to keep the Gazette (the largest single file) under the 40 pct cap: with only the four
"headline" sources (Torcy I, Villars I, Maintenon, Gazette) the Gazette would have been 47 pct of the total, so
a second Torcy volume and a second Villars volume were added for length and register diversity, not novelty.

**Excluded, per this brief:** Doniol (it may print destaing-gerard-1779 cribs); anything naming d'Estaing,
Gerard, Hellen, Paget, Noailles or Clairambault (checked by title and by spot-reading each volume; none of the
six committed volumes names any of these). A seventh candidate, `recueildesinstr00diplgoog` ("Recueil des
instructions données aux ambassadeurs et ministres de France ... Savoie-Sardaigne et Mantoue", ed. Horric de
Beaucaire, 1898), was fetched and inspected but **not committed**: its opening matter is a lengthy modern
(1898) editorial "Introduction" narrating the diplomatic history in the historian's own late-19th-century
prose, with the period instruction texts themselves only quoted in blocks further in and surrounded by dense
footnote apparatus (archive references, editorial cross-references) -- exactly the "print period text but check
the text is period, not editorial" risk the brief flagged for this series. Since the six committed volumes
already clear the 1,000,000-letter floor by more than double, this source was dropped rather than spending
time isolating the quoted-instruction blocks from the editorial frame.

**OCR-quality check** (leave-one-out cross-corpus word coverage, as `tools/data/pt18` did): for each of the
six files, `tools/judge_plaintext.py`'s `NgramModel.cover()` word list was built from the other five files
only, then used to score that file's own folded letters. Five of six land at 93.8-97.0 pct cross-corpus word
coverage; La Gazette de France (smaller print, denser newspaper columns) is lower but still clean at 88.0 pct.
Consistent with pt18's 90.5-95.6 pct range for a real, non-junk period corpus.

**Known OCR characteristic, not corrected:** all six sources are printed in the 18th-century long-s typeface
(ſ), which both Google's and other scanners' OCR frequently misread as "f" ("fervir" for "servir", "fages" for
"sages", etc. -- visible throughout the raw text). This is left as raw OCR, exactly as `tools/data/pt18`'s own
README notes doing for its long-s/digit misreads and as `tools/tests/test_judge_plaintext_lang_pt18.py`'s
held-out passage does deliberately: the corpus should look like what OCR actually produces from these sources,
since that is what any other IA-scanned volume of the same period will also look like. It is *not* necessarily
representative of a hand-transcribed manuscript letter (this lane's actual targets), where a human transcriber
reading cursive script would not reproduce a print typeface's long-s/f OCR confusion at all -- so the corpus's
s/f letter-frequency balance is skewed toward "f" relative to a manuscript transcription of the same register,
a caveat worth remembering if a fr18 judge run ever turns on s/f-sensitive statistics specifically. It has no
effect on the 4-gram language-model check itself (both real text and target manuscripts would go through the
same `fold()` step, and the shared long-s bias in this corpus does not appear in a clean manuscript
transcription either way), but it means a strict letter-frequency comparison should not treat this corpus's
f-count as the "true" 18th-century French rate.

Never add clair1161, clairambault296, hellen-1752, destaing-gerard-1779 or any of their own material to this
folder -- same circularity concern as pt17/pt18's own warnings.

## Held-out calibration: fr18 vs fr16 vs fr19 (25 Sept 2026)

Leave-one-file-out test: for each of the six fr18 files, a model was built from the other five, its
`null_p99`/`real_p05` thresholds computed from that five-file training set exactly as `judge()` does, then 30
real windows of length N were drawn from the *held-out* file (genuinely unseen text) at N=200 and N=500 and
scored against those thresholds -- a real window that fails to clear both thresholds is a false negative; the
same 30 windows, letter-shuffled, that clear both thresholds are false positives (the null). 180 held-out real
windows total per N (30 x 6 files), fixed seed. The identical 180 held-out real windows (real fr18-era,
diplomatic/official French) were then scored a second and third time against the existing `fr16` (16th-c.,
`LANG_CORPORA`'s default for `fr`) and `fr19` (19th-c. novels) models, using each model's own thresholds from
its own full corpus -- this isolates whether the corpus era/register, not the text, drives the rejection rate.

| N | corpus | real-prose false-negative rate | shuffled-null false-positive rate |
|---|---|---|---|
| 200 | fr18 (leave-one-file-out, era/register-matched) | 0.183 (33/180) | 0.000 |
| 200 | fr16 (16th-c., scored on the same 180 windows) | 0.961 (173/180) | 0.000 |
| 200 | fr19 (19th-c. novels, scored on the same 180 windows) | 0.983 (177/180) | 0.000 |
| 500 | fr18 (leave-one-file-out, era/register-matched) | 0.189 (34/180) | 0.000 |
| 500 | fr16 (16th-c., scored on the same 180 windows) | 0.989 (178/180) | 0.000 |
| 500 | fr19 (19th-c. novels, scored on the same 180 windows) | 1.000 (180/180) | 0.000 |

Genuinely held-out c.1680-1790 diplomatic/official French is rejected by the era-matched fr18 model about 1 time
in 5 (18-19 pct, both window lengths) but rejected by the 16th-century and 19th-century corpora 96-100 pct of
the time -- almost never passing. This is the same shape as the pt17->pt18 finding (CLAUDE.md rule 3): the
wrong-era/register corpus does not merely add noise, it makes the language check fail on real prose almost
every time, whatever the candidate reading actually says. The null (shuffled) false-positive rate is 0.000 for
every corpus and both N, so none of the three corpora is simply looser -- fr18's lower false-negative rate is a
genuine register/era match, not a wider net. fr18's own 18-19 pct false-negative rate is higher than pt18's
reported 4.0-8.5 pct (V6-PTCORP; smaller, more homogeneous held-out passages there); a FAIL on this lane's
targets under fr18 should be read as still-real evidence, similarly to a FAIL under pt18, not dismissed, but a
PASS is stronger evidence than a PASS under fr16 or fr19 would have been.
