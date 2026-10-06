# es1600: 1598-1621 Spanish state letters, one printing kind (CODOIN, 1863-90)

Built 6 Oct 2026 (R12-OLDCORP, LANE-RUN12-account-2) for `ciphers/na-oldenbarnevelt-2442-1605` (a copied Spanish letter of
23 Dec 1605), step (d') of its NOTES.md section 12: es17a (1590-1625) mixes two 19th-century printings with three long-s
originals and its leave-one-file-out spread is 22.5-97% at N=634. Wired as `LANG_CORPORA["es1600"]`; a spec opts in with
`"judge": {"language": "es1600"}`. Offline test: `tools/tests/test_judge_plaintext_lang_es1600.py`. Rules pre-registered in
`ciphers/na-oldenbarnevelt-2442-1605/transcription/PREREG_R12-OLDCORP.md` (with its pre-build amendment).

| identifier | tomo | printed | text date | contents | folded letters |
|---|---|---|---|---|---|
| coleccindedocu42madruoft | XLII | 1863 | 1599-1602 (+ Archduke letters 1606) | letters of the Almirante de Aragon to the Archduke and court, Flanders | 650,011 (capped) |
| coleccindedocu43madruoft | XLIII | 1863 | 1598-1621 | documents of the Archduke Albert, mostly letters (to Lerma, Philip III) | 285,055 |
| coleccindedocu44madruoft | XLIV | 1864 | to 1613 (in-window text only) | documents of Pedro Giron, 3rd Duke of Osuna: Sicily/Naples correspondence | 532,876 |
| coleccindedocu45madruoft | XLV | 1864 | from Nov 1613 | Osuna correspondence, continued | 528,421 |
| coleccindedocu46madruoft | XLVI | 1865 | from May 1617 | Osuna correspondence, continued | 592,825 |
| coleccindedocu47madruoft | XLVII | 1865 (imprint OCR unclear) | from Aug 1618 | Osuna correspondence, continued | 514,599 |
| coleccindedocu96madruoft | XCVI | 1890 | 1615-18 | letters of Pedro de Toledo, marques de Villafranca, to Philip III; Consejo de Estado consultas | 536,921 |

About 3.64M folded letters. URLs in MANIFEST.tsv. Rebuild: download each `<id>_djvu.txt` to DIR as `<id>.txt`, then
`python3 tools/data/es1600/build.py --raw DIR` (`--survey` prints every volume's year share and writes nothing).

**Selection.** All 108 `coleccindedocuNNmadruoft` scans on archive.org fetched once (6 Oct 2026, 108 djvu requests + 5
metadata, >= 1.6 s apart; tomos XXXVI, LXI, LXVIII, LXXXII, XCI answered HTTP 500 on the djvu text and are unread). A
volume was a candidate when >= 40% of its four-digit years 1500-1700 fall in 1598-1621 (12 did); the five whose title or
first document is not 1598-1621 letters/state papers were dropped before the build (XLVIII Chile treatise, LX chronicle,
LXXXI/C/CVI medieval and 15th-century matter admitted by stray years). Only 7 of the 12 are kept.

**Stripping.** Within a volume, text is kept from a line naming a year in 1598-1621 to the next line naming a 1500-1700
year outside it; footnote lines ("(1) ..."), lines with >= 2 Latin/Italian/French function words and hold-out names are
dropped; then tools/data/es18/build.py's `clean()` unchanged (hyphen rejoin, no long-s repair, keep lines of >= 4 tokens
with >= half their 3+-letter tokens in an es17c7 + es17a reference vocabulary); cap 650k folded letters per file. The
editors' document headings (regestas such as "Copia de carta original del duque de Osuna a S. M., fecha en Napoles...") are
19th-century Spanish and remain in the text; they are a small share of each volume.

**Hold-out:** raw volumes grepped for Senisteros/Seniste*, Cisneros, "Juan de la Pena": zero hits in the 7 kept
volumes before the build; the build drops any such line regardless.

## Leave-one-file-out false-negative check, N=634 (the target's B/C1 length), 200 windows per fold

`python3 tools/data/es18/holdout_check.py --lang es1600 --N 634`, 6 Oct 2026 (log beside this file):

```
held_out=coleccindedocu42madruoft  real_p05=-0.824 false_negatives=38/200 (19.0%)
held_out=coleccindedocu43madruoft  real_p05=-0.833 false_negatives=18/200 (9.0%)
held_out=coleccindedocu44madruoft  real_p05=-0.854 false_negatives=10/200 (5.0%)
held_out=coleccindedocu45madruoft  real_p05=-0.835 false_negatives=23/200 (11.5%)
held_out=coleccindedocu46madruoft  real_p05=-0.856 false_negatives=24/200 (12.0%)
held_out=coleccindedocu47madruoft  real_p05=-0.836 false_negatives=19/200 (9.5%)
held_out=coleccindedocu96madruoft  real_p05=-0.847 false_negatives=23/200 (11.5%)
TOTAL false-negative rate: 155/1400 (11.1%); per-fold spread 5.0-19.0% (7 folds)
```

Beside es17a at the same N: 62.1%, 22.5-97.0% (5 folds); es17c: 21.0%, 8.0-35.5% (3 folds).

**Reliability.** By the pre-registered rule (unknown when fewer than ~5 files, or max fold > 2x min fold AND > 20 pct)
es1600 is not "unknown reliability" at N=634: 7 files, max fold 19.0% (under 20). The spread is still 3.8x, and the folds
are not independent: four of the seven are one sender's (Osuna) correspondence in one edition, so a held-out Osuna tomo
still has three Osuna tomos in its training model -- the 5.0-12.0% Osuna folds flatter the corpus; the two non-Osuna
letter folds (XLII 19.0%, XCVI 11.5%) and XLIII (9.0%) are the fairer estimate. Real 1598-1621 state letters held out of
this model fail its own gate about 9-19% of the time at N=634. A PASS is a gate for a verifier, never a reading.
