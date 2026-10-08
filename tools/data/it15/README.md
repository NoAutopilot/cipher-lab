# it15: 15th-c. Lombard chancery Italian (SFZ-NEXT, account 2, 8 Oct 2026)

Built for the Sforza 1446-47 cipher slips (ciphers/sforza-pusterla-1447-f13, sforza-duke-1447-f15, pool
ciphers/sforza-italien1584-1447) after the V6-PTCORP lesson (CLAUDE.md rule 3): it16dip is 16th-c. diplomatic letters, the
slips are 1447. Wired as `LANG_CORPORA["it15"]` in tools/judge_plaintext.py.

Sources (MANIFEST.tsv; raw OCR not committed, re-fetch from the URLs):
- Osio, *Documenti diplomatici tratti dagli archivj milanesi* II (1869), https://archive.org/download/bub_gb_XkUAjq5V07wC/bub_gb_XkUAjq5V07wC_djvu.txt
  (mostly Latin: 67 Italian paragraphs kept, 37k letters, one file `osio2`).
- Osio III (1872, Visconti documents to 1447), https://archive.org/download/bub_gb_88IStucIdgAC/bub_gb_88IStucIdgAC_djvu.txt
  (1,163 paragraphs kept, cut in four quarters by order, `osio3a`-`osio3d`, ~160k letters each).
- Mazzatinti, *Archivio storico lombardo* X (1883), OCR `targets/it1583/asl1883.txt` in dbourdeau/cyphersolver (text CC BY 4.0,
  credit Bourdeau), 378 paragraphs, 150k letters, `asl`.
Build: `python3 tools/data/it15/build.py --raw DIR --exclude ciphers/sforza-italien1584-1447/pusterla/clear_*.txt`
(filter = tools/italian_ngram.py's archaic-ratio rule at min-ratio 1.0; the leak guard dropped 1 Osio III paragraph, the print
of Pusterla's f.71 letter, used as a key unit). OCR is noisy and the Osio regests' Italian summaries are 19th-c.; the archaic
filter keeps period-letter paragraphs but some editorial Italian may survive.

## Leave-one-file-out false-negative check (rule 3 fold-count paragraph)

`python3 tools/data/it16dip/holdout_check.py --lang it15 --n N` (generic script), 200 windows per fold, 8 Oct 2026.

| fold (held out) | N=360 (f.13's length) | N=1000 |
|---|---|---|
| osio2 | 85/200 (42.5%) | 81/200 (40.5%) |
| osio3a | 81/200 (40.5%) | 49/200 (24.5%) |
| osio3b | 69/200 (34.5%) | 43/200 (21.5%) |
| osio3c | 39/200 (19.5%) | 31/200 (15.5%) |
| osio3d | 36/200 (18.0%) | 42/200 (21.0%) |
| asl | 150/200 (75.0%) | 172/200 (86.0%) |
| **blended** | **460/1200 (38.3%), spread 18.0-75.0%** | **418/1200 (34.8%), spread 15.5-86.0%** |

For comparison it16dip at N=360: 384/1200 (32.0%), spread 5.0-65.5%. Verdict by the rule: a FAIL/PASS against it15 is of
**unknown reliability** (wide spread; four folds are quarters of one volume, so the effective source count is three). It is
era- and register-nearer than it16dip, not better calibrated.
