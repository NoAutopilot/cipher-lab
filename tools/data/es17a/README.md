# es17a: 1590-1625 Spanish state, diplomatic and court prose for the judge's era check

Built 3 Oct 2026 (OLD-ES17A, LANE-A1, account 1; brief `.claude/briefs/runs/2026-10-03-acct1-old-es17a.md`) for
`ciphers/na-oldenbarnevelt-2442-1605` (a copied Spanish letter of 23 Dec 1605), whose B/C1 reading FAILed the spec's
own corpus (Don Quijote 1605, fiction) and for which the nearest state-prose corpus on disk, es17c, is 1643-47
(CLAUDE.md rule 3, pt18/es17c lessons). Wired as `LANG_CORPORA["es17a"]`; a spec opts in with
`"judge": {"language": "es17a"}`. Offline test: `tools/tests/test_judge_plaintext_lang_es17a.py`.

| identifier | text | printed | text date | genre | long-s repair | folded letters |
|---|---|---|---|---|---|---|
| relacionesdelasc00cabr | Cabrera de Córdoba, *Relaciones de las cosas sucedidas en la corte de España 1599-1614* | 1857 | 1599-1614 | court newsletters | no | 650,062 (capped; file runs to 1614) |
| correspondencia01clemgoog | *Correspondencia inédita de D. Guillén de San Clemente, embajador en Alemania* | 1892 | 1581-1608 | ambassador's letters | no | 366,756 |
| bub_gb_zb0d4P6LU2oC | Carlos Coloma, *Las guerras de los Estados Baxos 1588-1599* | 1625 | 1588-1599 | soldier-diplomat's history | yes | 650,040 (capped) |
| bub_gb_54G5MclHRpUC | Bernardino de Mendoza, *Comentarios ... guerras de los Payses Baxos* | 1592 | 1567-1577 | ambassador's history | yes | 650,071 (capped) |
| bub_gb_CujQp6gW1dQC | Antonio Pérez, *Relaciones* (with the *Cartas*) | 1624 | 1591-1603 | secretary of state's relations and letters | yes | 202,212 |

Combined about 2.52M folded letters. URLs and the long-s flag in MANIFEST.tsv. Rebuild: download each
`<id>_djvu.txt` into a directory, `python3 tools/data/es17a/build.py --raw DIR`.
Not used: `correspondencia00clemgoog` (a second scan of the same San Clemente book, 81% six-word-shingle overlap with
01); `A331141` (1597 *Registro de las cartas*, manuscript, OCR is noise); the 2020/1997 Cabrera re-uploads (same book).

**Cleaning:** tools/data/es18/build.py's `clean()` unchanged (hyphen rejoin, long-s repair for the three original
printings, keep lines with >= 4 tokens and >= half their 3+-letter tokens in a reference vocabulary of es17c7 plus
Cabrera and San Clemente), then lines with two or more Italian function words dropped (Pérez prints Italian
passages; only 6 lines caught, some single-marker Italian lines remain), then each file capped at 650k folded letters.
The long-s repair is partial on these OCRs (residue such as "efíando", "nueflra", "Efpañola" remains in Coloma and
Mendoza).

**Hold-out:** all six raw files grepped for "Senisteros"/"Seniste*", "Cisneros", "Juan de la Peña", "García de
Sen*": zero hits. Cabrera covers 1605 (his letters "De Valladolid ... 1605") but not this letter.

## Leave-one-file-out false-negative check, N=634 (the target's B/C1 length), 200 windows per fold

`python3 tools/data/es18/holdout_check.py --lang es17a --N 634` (and `--lang es17c`), 3 Oct 2026; logs beside this file.

```
es17a (5 folds)
held_out=relacionesdelasc00cabr     real_p05=-0.917 false_negatives=45/200 (22.5%)
held_out=correspondencia01clemgoog  real_p05=-0.898 false_negatives=153/200 (76.5%)
held_out=bub_gb_zb0d4P6LU2oC        real_p05=-0.921 false_negatives=153/200 (76.5%)
held_out=bub_gb_54G5MclHRpUC        real_p05=-0.914 false_negatives=76/200 (38.0%)
held_out=bub_gb_CujQp6gW1dQC        real_p05=-0.901 false_negatives=194/200 (97.0%)
TOTAL false-negative rate: 621/1000 (62.1%); per-fold spread 22.5-97.0% (5 folds)

es17c (3 folds), same N
TOTAL false-negative rate: 126/600 (21.0%); per-fold spread 8.0-35.5% (3 folds)
```

**Reliability: unknown** (rule 3 fold-count paragraph; the pre-registered rule in
ciphers/na-oldenbarnevelt-2442-1605/transcription/PREREG_OLD-ES17A.md). The five sources are each other's outliers --
two 19th-century editorial printings and three noisy long-s originals -- the EN-FOLDS / es18p shape (heterogeneous
sources widen the spread), not the es17c7 shape. Real 1590-1625 state prose held out of this model FAILs its own gate
62% of the time at N=634, so a FAIL against es17a says little; a PASS would still be a gate for a verifier, never a
reading. A tighter corpus would need more files of one register and one printing kind (e.g. several CODOIN volumes of
1598-1621 state letters, all 19th-century printings), not more originals.
