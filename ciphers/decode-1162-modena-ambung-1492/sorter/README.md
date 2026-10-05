# g/q/sigma sign sorter, decode-1162 + decode-1168 (D2-1162, 5 Oct 2026)

`modena-gq-sorter.html` is a built `tools/sign_sorter.py` page (1.06 MB) with 31 tiles: every sign labelled `g` or `q` on
DECODE R1162 p.1 (10, all from the cipher runs in `../ciphertext.tsv`) and in the 14 aligned groups of R1168 f.12r (21, from
`../../decode-1168-modena-costabili-1492/ciphertext.tsv`). Starting piles are the current labels (`g`, `q`), with up to 4
provisional shape clusters per pile (`--auto-clusters 4`; they are not atlas clusters). The 8 R1162 tiles whose readers marked
`?` are in the "Check these first" box (`focus.tsv`).

Not yet published. To publish: Artifact publish of `modena-gq-sorter.html` with capabilities `{"db": {}}` (load the
artifact-capabilities skill first), then an ASKS.md row "backlog, never blocking" with the URL. Rebuild from the full PNGs:
`sh ciphers/decode-1162-modena-ambung-1492/sorter/build.sh PAGES_DIR OUT.html` (see the script header for the two files).

Sign ids: `R1162_<line>_<pos>` = `../ciphertext.tsv` line and 1-based position; `R1168_<line>_<pos>` = the 1168 ciphertext.tsv
line and position. Boxes (`signs.tsv`) are in native pixels of the 2592x3888 PNGs, placed by eye on ruler crops and checked on
`tiles_contact.png` (every tile sits on one sign).

After the owner sorts: export the db collections (ArtifactData list ... out_dir=DIR), then
`python3 tools/sign_sorter_apply.py --labels ciphers/decode-1162-modena-ambung-1492/sorter/labels.tsv --db DIR
--out ciphers/decode-1162-modena-ambung-1492/sorter/settled_labels.tsv --summary .../summary.json`; then split the labels in both
ciphertext.tsv files, re-key 1168 (`align/run_align.py`) and re-run `score_g.py` and `decode_key.py --check` here.
