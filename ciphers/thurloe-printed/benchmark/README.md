# Fauconberg solver benchmark (LANE T worker F, 24 Sept 2026)

Ciphertext-only runs of `tools/subst_hillclimb.py` and `tools/nomenclator_anneal.py` on the Fauconberg to
H. Cromwell groups (P16-P24, vol. 7), scored against Birch's printed decipherment, plus a synthetic control
of the same length and homophone structure. Write-up: `../NOTES.md` section 15.

- `data.py`: group sequence (3,024 groups, 243 fragments) and the scoring key (`python3 data.py` prints the votes)
- `corpus.py`: LM corpus (Gutenberg texts in tools/data + English lines of Thurloe vols 2, 3, 5) and the vol. 7
  control plaintext (with a long-s OCR repair)
- `bench.py`: all runs; writes `results.tsv`, `groundtruth_key.tsv`, `synth_key.tsv`
- `python3 bench.py --check` reruns everything (about 12 minutes on 4 cores) and exits 1 if `results.tsv`
  is stale; the `seconds` column is ignored. Needs numpy and gcc. Reads only files on disk: the OCR text is
  restored from `sources/ia-fulltext/thurloe-gz/` automatically. No network.
