# Shared sign atlas for fr.2980 (24 Sept 2026)

Built so both blind passes on f.30r-v use one code book (transcription brief, symbol-alphabet paragraph).

- `seg.py`: glyph segmentation of a line crop (paper-normalised image `<folio>_norm.jpg`, column runs in the x-height
  band). Needs the full-resolution regions from `../images/manifest.json` plus a normalised copy (see `normalise` below).
- `dp.py`: aligns the reconciled f.29r codes (`../ciphertext.txt`) to the segmented glyphs by dynamic programming with
  a shape template per code (24x24 correlation), iterated; output `f29_dp.json`.
- `atlas2.py` + `fix.json`: picks up to 3 exemplars per code, drops/crops the misaligned ones listed in fix.json (checked
  by eye) and draws `atlas_f29.png`; coordinates in `atlas_f29.tsv` (full-resolution pixel boxes).
- `cls30.py`: classifies every f.30 glyph against the f.29r templates and clusters the poor matches by shape; the
  clusters gave the f.30 additions (`atlas_f30add.png`: FL, HASH, BOX, ss2 arch, INF, TRI, QQ, ST, A2, CROSS, Rt).
- `PASS-BRIEF-f30.md`: the brief given to both Sonnet passes with the two atlas images and the 19 pass sheets
  (sheets.py restricted to f.30 lines).
normalise: bg = uniform_filter(maximum_filter(uniform_filter(a,15),61),61); out = clip(255-(bg-a)*1.6).
