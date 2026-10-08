# nl16: Dutch prose of 1569-1589 in its own spelling, for the judge's language check

Built 8 Oct 2026 (NL16-11106, LANE FAMILY, account 2; brief `.claude/briefs/runs/2026-10-08-ytbiz-family-1909-jobs.md`) for
`ciphers/wvo-11106-bergh-1572` (Willem van den Bergh to Willem van Oranje, 19 Sept [1572]), whose homophonic family had no
era-matched Dutch corpus: nl18 is 1770-1799, nl20 1880-1940, nl_dev a modern Bible, nl_repo targets' own readings. Opt in with
`"judge": {"language": "nl16"}`. The pattern is de1600's (`tools/data/de1600`).

## Sources (MANIFEST.tsv: ids, URLs, raw bytes, sha1, folded letters)

DBNL plain-text downloads (`https://www.dbnl.org/nieuws/text.php?id=ID`, fetched 8 Oct 2026, 15 requests: 4 author pages,
6 texts, 5 ids that returned an empty body). The works are 16th-century and public domain; DBNL's digital texts of such works are
offered for reuse with attribution to DBNL (credited here and in MANIFEST.tsv). Only the filtered text is committed.

| file | work | original | DBNL edition | folded letters |
|---|---|---|---|---|
| marn001bien01 | Marnix, De bijencorf der H. Roomsche Kerke | 1569 | Lacroix & Willems 1858, diplomatic | 450,152 (cap) |
| marn001trou01 | Marnix, Trouwe vermaninge aende christelicke gemeynten | 1589 | DBNL | 83,336 |
| coor001zede01 | Coornhert, Zedekunst dat is wellevenskunste | 1586 | Becker 1942 (1586 text, punctuation modernised) | 450,345 (cap) |
| spie001twes01 | Spieghel, Twe-spraack vande Nederduitsche letterkunst | 1584 | Caron 1962 | 294,265 |
| coor001boev01 | Coornhert, Boeventucht | 1587 | Gelderblom, Meijer Drees et al. 1985 | 38,581 |

Total **1,316,679 folded letters**, five files, three authors. **Register: moral, polemical and grammatical prose, not letters**
(no 1560s-1580s Dutch letter edition was found on DBNL in the time box; the brief's letter sources -- Groen's Dutch letters, Bor
-- would need IA djvu work). Held out for the offline test: `cice001offi01` (Coornhert, Officia Ciceronis, 1561). Not used: five
ids (`coor001vrer01`, `coor001gesp01`, `coor001vijf02`, `marn001heyl01`, `marn001onde01`) returned an empty text body.
None of the files contains the target, its KHA neighbours or any decipherment of them (they are printed books, not letters).

## Cleaning (build.py)

TEI header cut at "Verantwoording"; DBNL page markers dropped; 80-word chunks kept when Dutch function words are >= 15 pct AND
>= 3 period-spelling markers (ende, ofte, wt, ick, welck, oock, sulcx, vande, inden, totten, gh- words ...) AND < 3 modern-only
words (hij, zij, wij, ook, uitgave, werd, zijne ...). A few chunks of the editors' introductions that quote period titles survive
the filter (first lines of each file; a known impurity, as in de1600). Spieghel writes his reformed spelling (aa, ó, y) and
Marnix his Brabant spelling: 16th-c. Dutch had no standard, which drives the fold result below.

## Held-out calibration (CLAUDE.md rule 3, es17c / EN-FOLDS paragraphs)

`holdout_check.py` (the de1600 copy): leave-one-file-out, 200 windows per held-out file; false negative when a held-out window
scores at or below the in-model real_p05. Logs: holdout_nl16_N820.log, holdout_nl16_N200.log. N=820 is the target's length.

| N | Bijencorf 1569 | Trouwe verm. 1589 | Zedekunst 1586 | Twe-spraack 1584 | Boeventucht 1587 | blended | spread |
|---|---|---|---|---|---|---|---|
| 820 | 95.0 | 94.0 | 43.5 | 98.0 | 77.0 | **81.5%** | 43.5-98.0% (2.3x) |
| 200 | 77.0 | 63.5 | 23.5 | 80.0 | 67.5 | **62.3%** | 23.5-80.0% (3.4x) |

**Reading.** The in-model real_p05 gate rejects most genuine unseen 1569-1589 Dutch: the model learns each author's spelling,
and an unseen author's spelling falls below the in-model 5th percentile, the more so at long N where the real-window
distribution is tight. **A FAIL against nl16's real_p05 is not a negative.** Place a decode instead against unseen text:
`offi_calibration.py` scores 200 N=820 windows of the held-out 1561 Officia Ciceronis under the full model
(offi_calibration_N820.log): **unseen p05 -0.951**, p25 -0.893, median -0.859, min -1.019; model real_p05 -0.832, null_p99 -2.021.
A decode below about -0.95 at N=820 is outside genuine unseen 16th-c. Dutch as this model sees it; the shuffled-letter floor
sits near -2.0. More folds (more authors, letters rather than treatises) would be the next improvement.
