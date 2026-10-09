# TXE-B geo unit re-cut (9 Oct 2026, LANE TX-ENGINEER round 2, instrument B)

- `gate_old/`, `gate_new/`: read-free dev gate on f178v (`--check-boxes atlas/signs.tsv --dry-run`), old midpoint bands vs
  `--band-extent 0.1 --mask-neighbours`; `band_check.tsv` and the console log in each.
- `crops/`: the geo unit re-cut, native resolution, with manifest.json, debug overlays, band_check.tsv, crops_note.md and the
  two command logs. Commands (sources on disk, no fetch):
  - f178r: `python3 tools/iiif_lines.py --image ciphers/nevers-birago-fr3251-1572/harvest/f178r/src_ark_12148_btv1b9060248g_f181_4700_3720_3050_620.jpg --out benchmark-tx/txeng/geo/crops --prefix f178r --max-width 1250 --centres 95,215,355 --deskew 300 --slope-local --band-extent 0.1 --mask-neighbours --check-boxes ciphers/nevers-birago-fr3251-1572/atlas/signs.tsv --overlap-note --note-scale 2 --debug`
  - f178v: `python3 tools/iiif_lines.py --image ciphers/nevers-birago-fr3251-1572/harvest/f178v/src_ark_12148_btv1b9060248g_f182_1703_848_2900_3452.jpg --out benchmark-tx/txeng/geo/crops --prefix f178v --max-width 1250 --band-extent 0.1 --mask-neighbours --only-lines 5,10,22 --check-boxes ciphers/nevers-birago-fr3251-1572/atlas/signs.tsv --overlap-note --note-scale 2 --debug`
- `crops2x/` (gitignored, regenerable): each crop upscaled 2x LANCZOS to PNG, as `harvest/make_2x.py` did for pass A; these are
  what the reader saw.
