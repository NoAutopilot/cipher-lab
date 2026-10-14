# tx/viv63_esplit (VIV-ESPLIT, 14 Oct 2026) -- measurement only

Nothing here changes key.tsv, a ciphertext file the decode scripts read, or any committed reading (PREREG-VIVESPLIT.md
Addendum B: the per-class licence for the y split is post-hoc, so no key edit in this job). `y_l` is a provisional
sub-label used only inside tx/vivesplit/step2.py's gate run.

- `tokens.tsv`: every label-y token on ink 63 f.193v, f.193r, f.192v (line = `<page>_<Lnn>`, pos = 1-based index in
  `viv63_decode.lines()`'s sequence for that line), the tile tier (T1 one box 1:1; T2 union of boxes; T3 half of a box shared
  with a neighbour; none), the crop and x-span in that crop, the six-class top sub-label and posterior, P(l), P(h), and
  `split` = `y_l` where P(l) >= 0.6.
- `gates.json`: b2 order gate + 200 wrong keys on the three pages, unsplit vs split (seeds 20261014ES-63u / -63s), and the
  200-draw random-split null (the same count of y positions sent to l at random, seed 20261014).
- `owner_questions.tsv`: label-e tokens on the three pages (with next-label context hints for VIV-KEYV's groups A/B) and
  label-y tokens whose top posterior is under 0.6 -- tile references for a later sorter ask; no page built.

Rebuild (crops untracked; boxes equal images/p63/manifest.json's, checked 72/74/72):
```
python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 199 --iiif-host openapi --region 1300,600,2980,4560 --out ciphers/fr16104-vivonne-spain-1572/images/p63/esplit/c199_f193v --prefix c199_f193v --follow-slope 400 --distance 70 --max-width 1600 --overlap 150
python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 198 --iiif-host openapi --region 4880,500,3050,4220 --out ciphers/fr16104-vivonne-spain-1572/images/p63/esplit/c198_f193r --prefix c198_f193r --follow-slope 400 --distance 70 --max-width 1600 --overlap 150
python3 tools/iiif_lines.py --ark btv1b9009663p --canvas 198 --iiif-host openapi --region 1200,700,2900,4250 --out ciphers/fr16104-vivonne-spain-1572/images/p63/esplit/c198_f192v --prefix c198_f192v --follow-slope 400 --distance 70 --max-width 1600 --overlap 150
python3 ciphers/fr16104-vivonne-spain-1572/tx/vivcls/seg.py          # truth-leaf atlas (f.201r crops: images/manifest.json "vivcls")
python3 ciphers/fr16104-vivonne-spain-1572/tx/vivesplit/esplit.py tiles && python3 .../esplit.py gate
python3 ciphers/fr16104-vivonne-spain-1572/tx/vivesplit/step2.py seg && python3 .../step2.py label && python3 .../step2.py gates
```
