# es18: Spanish letters, gazette and diplomatic prose of 1690-1725 for the judge's language check

Built 2 Oct 2026 (GAPS5-na-schonenberg-1678-1716, account-4, brief `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`,
the V6-PTCORP pattern of `tools/data/pt18`) because `ciphers/na-schonenberg-1678-1716` is a 1702-1716 Spanish letter and
the nearest Spanish corpus on disk, `es17c7` (1634-1648 Jesuit court newsletters), is 55-80 years off: under it the body
reading, the leaf's own period gloss and every control FAIL together (GAPS4, 2 Oct 2026), so the judge could not decide.

## Sources (Internet Archive `_djvu.txt` OCR, seven distinct items; MANIFEST.tsv has the URLs and fetch date)

| identifier | what | printed | text date | genre | folded letters |
|---|---|---|---|---|---|
| comentariosdelag01sanfuoft | Bacallar y Sanna, marqués de San Felipe, *Comentarios de la guerra de España e historia de su rey Phelipe V*, tomo I (Madrid 1792 reprint, Toronto scan) | 1792 | 1700-1715, written c.1725 by a Philip V diplomat (envoy at Genoa, plenipotentiary at Cambrai) | political/military/diplomatic narrative | 631,698 |
| comentariosdelag02sanfuoft | the same, tomo II | 1792 | 1715-1725 | political/military/diplomatic narrative | 606,656 |
| elembaxadorpolit00cara | Carlo Maria Caraffa, *El embaxador político-christiano* (Palermo 1691, Duke scan) | 1691 | 1691 | treatise on the ambassador's office | 242,400 |
| A092002 | Tomás de Puga y Rojas, *Crisol de la española lealtad* (1708, Universidad de Sevilla scan) | 1708 | 1708 | Succession-war political prose | 315,874 |
| A022134 | Pérez de Valenzuela, *Nuevo estilo y formulario de escrivir cartas missivas, y responder a ellas* (c.1700 printing, Sevilla scan) | c.1700 | c.1700 | letter-writing manual: model Spanish letters | 203,592 |
| A11100924 | *Gaceta de Madrid*, 1710 (Sevilla scan, 112 pages) | 1710 | 1710 | court gazette / newsletter | 231,675 |
| noticiashistoria00vera | Vera Tassis y Villarroel, *Noticias historiales de la enfermedad, muerte y exsequias de la reyna María Luisa de Orleans* (Madrid 1690) | 1690 | 1689-1690 | court narrative | 308,709 |

**Combined: 2,540,604 letters after `fold()`** (es17c7 has 4,923,218; pt18 3,226,102). The two San Felipe volumes are 49% of
the total; the smallest file is 8%. All seven are original Spanish prose, none a translation from a modern language, none verse,
none a dictionary. The San Felipe volumes are an 18th-century text in a 1792 printing (modernised accents, long s already
gone); the other five are the original 1690-1710 printings. Found with two `advancedsearch.php` queries (`language:spa AND
date:[1690 TO 1720]`, 602 rows, and a title query for cartas/correspondencia/gazeta with Felipe V-era terms, 79 rows); the
same searches turned up nothing in the way of a modern edition of 1690-1720 Spanish letters on archive.org (the Mayans,
Macanaz and Ursinos correspondences are not there as full text; the CODOIN volumes were not identified by title).

Requests to archive.org this job: 2 searches + 7 `_djvu.txt` fetches + 1 more `_djvu.txt` for the held-out test item
(A10903513) = 10, one at a time, >= 1.5 s apart, descriptive UA. Nothing refetched.

## Cleaning (`build.py --raw DIR`, reproducible from the raw files)

1. Hyphenated line breaks rejoined.
2. **Long-s repair** for the five original printings, which OCR long s as `f` ("defpues", "eftado", "fe"): each word holding
   an `f` is replaced by its best variant (every f kept or read as s, at most four f's) when that variant is at least 3x as
   frequent as the f-form in a long-s-free reference vocabulary (`tools/data/es17c7` plus the two 1792 San Felipe volumes),
   or when the f-form is unattested there and the s-form is attested. The same rule as `tools/data/it16dip/build.py`.
3. An OCR line is kept only when it has >= 4 word tokens and at least half of its tokens of 3+ letters are in that reference
   vocabulary: this drops the Latin papal-bull pages of the letter manual, library stamps, column-garbled gazette lines and
   title-page scatter (kept lines per file in build.py's output: 10273/10274, 9953/9953, 5436/5982, 6663/7570, 4987/5378,
   3752/4074, 6230/8541).
4. Kept lines written gzipped as `<identifier>.txt.gz`; the judge folds letters itself.

**Cross-corpus word coverage** (share of each file's folded letters in word types seen in the other six files, pt18's
OCR-quality check): San Felipe I/II 0.898 / 0.902; Caraffa 0.777; Crisol 0.719; letter manual 0.755; Gaceta 0.759; Vera
Tassis 0.687. pt18 landed at 0.905-0.956. The five originals sit lower for two reasons that the repair cannot remove:
period orthography that the modernised San Felipe print does not share (hazer, vna, qual, dize, assi) and residual OCR
noise after the long-s pass ("coníuelo", "manfion"). Reported as found.

**Hold-out check:** the seven raw files grepped for Schonenberg / Schonemberg / Albanilla / Albanylla: 0 hits in every file.
Nothing from the target's own fonds (NA 1.02.04) or from the Heinsius correspondence is in this corpus.

## Leave-one-file-out false-negative check (CLAUDE.md rule 3's fold-count paragraph), N=245, 200 windows per fold

`python3 tools/data/es18/holdout_check.py --lang es18` (and `--lang es18p`, `--lang es17c7`), run 2 Oct 2026, N=245 =
the target's body length (GAPS4/GAPS5), threshold = the in-model files' own real_p05. Logs beside this file
(`holdout_es18_N245.log`, `holdout_es18p_N245.log`, `holdout_es17c7_N245.log`).

```
es18 (7 folds)
held_out=comentariosdelag01sanfuoft  real_p05=-0.969  false_negatives=2/200   (1.0%)
held_out=comentariosdelag02sanfuoft  real_p05=-0.985  false_negatives=0/200   (0.0%)
held_out=elembaxadorpolit00cara      real_p05=-0.971  false_negatives=38/200  (19.0%)
held_out=A092002                     real_p05=-0.968  false_negatives=85/200  (42.5%)
held_out=A022134                     real_p05=-0.960  false_negatives=131/200 (65.5%)
held_out=A11100924                   real_p05=-0.956  false_negatives=91/200  (45.5%)
held_out=noticiashistoria00vera      real_p05=-0.932  false_negatives=158/200 (79.0%)
TOTAL false-negative rate: 505/1400 (36.1%); per-fold spread 0.0-79.0% (7 folds)

es18p (the five original printings only, 5 folds)
TOTAL false-negative rate: 601/1000 (60.1%); per-fold spread 29.5-74.0% (5 folds)

es17c7 at the same N=245 (for the side-by-side; its README reports N=519)
TOTAL false-negative rate: 108/1400 (7.7%); per-fold spread 4.0-14.5% (7 folds)
```

**What this means (reported as found, not smoothed over).** es18 is era-matched but not internally uniform: the two
1792-print San Felipe volumes (49% of the letters, modernised spelling, clean OCR) set the model's real_p05 from their own
register, and every held-out original printing then false-negatives at 19-79%. Dropping them (es18p) does not help -- the
five originals are each other's outliers too (29.5-74%), the EN-FOLDS shape (more heterogeneous sources, worse spread),
not the es17c-to-es17c7 shape (more folds of one series, tighter spread). By rule 3's own wording a FAIL/PASS against
**es18 at N=245 is of unknown reliability**; es17c7 at the same N is uniform (4.0-14.5%) but 55-80 years off.

The era match itself is real, measured on a genuine period letter outside the corpus: Philip V's 1709 circular to the cities
on the peace negotiations (archive.org A10903513, N=1069, long-s repaired like the corpus) scores **-0.920 vs real_p05 -0.947
under es18 (PASS)**, -0.919 vs -0.932 under es18p (PASS), and **-1.033 vs -0.865 under es17c7 (FAIL)**; its shuffle and a
random string fail all three. That passage is the offline test (`tools/tests/test_judge_plaintext_lang_es18.py`).

## Result on the target it was built for (ciphers/na-schonenberg-1678-1716/body/judge_body_results.tsv, 2 Oct 2026)

| corpus | SENSE (candidate) | real_p05 | gap | GLOSS (the leaf's own period gloss) | shuffled-null / shuffled-target PASS |
|---|---|---|---|---|---|
| es18 | -1.140 | -0.962 | 0.178 | -1.352 | 0/20, 0/20 |
| es18p | -1.168 | -0.973 | 0.195 | -1.341 | 0/20, 0/20 |
| es17c7 | -1.204 | -0.922 | 0.282 | -1.346 | 0/20, 0/20 |
| es | -1.153 | -0.894 | 0.259 | -1.311 | 0/20, 0/20 |

Both sides of the gate moved together under es18 (the candidate up 0.064, the gate down 0.040; the gap closed from 0.282 to
0.178) -- the calibration-fix shape, not threshold-shopping -- but the candidate still FAILs, and the leaf's own genuine gloss
scores 0.21 *below* the candidate under every corpus (the ZX-DEC349 clause: the judge cannot decide at this N and register).
Three corpora (es, es17c7, es18) now give the same verdict with the gloss failing beside the candidate each time; rule 3's
third-attempt clause applies to the judge as an instrument for this body at N=245 -- a fourth corpus is not the next step.

## Excluded

Not fetched: the two other Gaceta de Madrid items found (A064285002051, 33 pages of Oct-Dec 1702; A1140252, 60 pages of
1697) and the 1701 Barcelona *Lágrimas amantes* (lagrimasamantesd00roca) -- the request cap (12) and the fold result above
(more small heterogeneous originals widen the spread) argued against them; a future worker who wants a larger gazette
share fetches those two first. Never add the target's own reading, the Heinsius Briefwisseling, or any NA 1.02.04 material.
