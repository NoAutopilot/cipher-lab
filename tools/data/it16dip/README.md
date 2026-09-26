# it16dip: 16th-c. Italian diplomatic letters (SALV-CTX, LANE SALV, 26 Sept 2026)

Built for fr2933-salviati-1525 (Cardinal Giovanni Salviati, Toledo, 16 Oct 1525) after the V6-PTCORP lesson (CLAUDE.md
rule 3): `it` (tools/data/it16) is Caro/Tasso/Cibrario-era familiar letters, mostly later than 1525 and not diplomatic.
Wired in tools/judge_plaintext.py as `LANG_CORPORA["it16dip"]`; `it` stays the default.

Sources (archive.org `_djvu.txt`, 6 requests + 6 metadata calls, 26 Sept 2026; details in MANIFEST.tsv):
- Castiglione, *Lettere*, ed. Serassi, vols 1-2 (1769-71): the Negozi books are his despatches as papal nuncio at
  Charles V's court 1525-29 -- the same court, the same months as the target.
- Desjardins/Canestrini, *Negociations diplomatiques de la France avec la Toscane*, t. II: the Italian despatches
  (including the printed Salviati correspondence, Jan-Apr 1525); the French editorial prose is dropped by the filter.
- *Lettere di principi*, vols 1-3 (Venice, Ziletti, 1564): letters of popes, cardinals, nuncios, 1510s-1560s.

Build: `python3 tools/data/it16dip/build.py --raw DIR` (DIR holds `<identifier>.txt` fetched from the URLs in
MANIFEST.tsv). It rejoins hyphenated words, repairs the long s / st ligature the OCR reads as `f` / `fl` against a
long-s-free vocabulary from tools/data/it16, merges OCR paragraphs into >=60-word chunks, and keeps a chunk when
tools/italian16_corpus.py's keep() or a relaxed variant accepts it (build.py docstring). Output: one chunk per line,
folded lower-case words, space-separated, gzipped. Kept: 4,423 of 8,625 chunks, 3.77M letters (MANIFEST.tsv per file).
Residual OCR noise is heavy in the 1564 print (e.g. "diffojtia", "pojfa"); running headers survive in Desjardins.

## Leave-one-file-out false-negative check (rule 3 fold-count paragraph)

`python3 tools/data/it16dip/holdout_check.py --lang it16dip` and `--lang it`, N=2500 (the spec's judge letters_min),
200 held-out windows per fold, threshold = the in-model files' own real_p05. Run 26 Sept 2026.

| corpus | fold (held out) | false negatives |
|---|---|---|
| it16dip | bub_gb_laRnTtJmsDAC (Castiglione 2) | 111/200 (55.5%) |
| it16dip | bub_gb_ZJMxff7r4LUC (Castiglione 1) | 64/200 (32.0%) |
| it16dip | gri_33125010469852 (Desjardins II) | 4/200 (2.0%) |
| it16dip | letterediprincip01char | 87/200 (43.5%) |
| it16dip | letterediprincip02char | 192/200 (96.0%) |
| it16dip | letterediprincip03char | 108/200 (54.0%) |
| **it16dip** | **blended** | **566/1200 (47.2%), spread 2.0-96.0%** |
| it | alcuneletteredip00ferr | 79/200 (39.5%) |
| it | delleletterefam02seghgoog | 102/200 (51.0%) |
| it | lettereinedited00tassgoog | 64/200 (32.0%) |
| it | lettereinedited01cibrgoog | 119/200 (59.5%) |
| it | lettereineditedi01carouoft | 25/200 (12.5%) |
| it | letterescrittea01vanzgoog | 26/200 (13.0%) |
| **it** | **blended** | **415/1200 (34.6%), spread 12.5-59.5%** |

Reading: at N=2500 neither corpus is a reliable judge -- a held-out file differs from the rest by print and OCR
quality more than by language, and at that length the real-prose p05 band is narrow enough that the shift alone fails
it. it16dip is worse, driven by the 1564 print's OCR (vol. 2 at 96%); the one clean modern print (Desjardins) reads 2%.
A FAIL/PASS against either at this length is of unknown reliability (rule 3). it16dip's use in SALV-CTX is as the
wordcode family's training and control corpus (era and register), not as a judge. Next step if a judge is needed:
drop or re-OCR the 1564 volumes and add a second clean 19th-c. printing of 1520s despatches.
