Gzipped copies of the Internet Archive OCR text (`_djvu.txt`) of Birch, *A Collection of the State Papers of
John Thurloe* (1742), vols 2, 3, 5, 7, fetched once on 24 Sept 2026 (archive.org/download/<id>/<id>_djvu.txt,
4 requests, 1.6 s apart) so LANE T workers read from disk instead of refetching in parallel.
`zcat <id>_djvu.txt.gz > ../<id>_djvu.txt` restores the gitignored path that tools/thurloe_extract.py and
tools/interlinear_align.py read. Line numbers in ciphers/thurloe-printed are lines of these files.
