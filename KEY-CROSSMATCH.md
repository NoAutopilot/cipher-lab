# Key cross-match (LANE KX job 1, 25 Sept 2026)

**Method.** `tools/key_crossmatch.py`: 60 key tables found under `ciphers/**/key*.tsv|txt` + `tools/keys/key60.tsv`
(17 dropped as scratch: conflicts 5, pass 6, atlas 5, align 2, trial/draft/candidate/crosscheck/counts 1 each);
115 ciphertexts (39 dropped: draft 34, recon 25, atlas 3, pass 8 -- some files hit two reasons). Ciphertexts
tokenised via the folder's decode.json job (22), else decode_key.py's own format auto-detect (23 tsv, 3 rows,
1 pipe), else a whitespace/semicolon fallback treating a 4+-letter alphabetic run as clear prose (66 files --
most targets have no decode.json). Coverage >=0.5 gates scoring; decode with first alt of `a|b`; score with
judge_plaintext.py's NgramModel. Corpora: fr16/de16/it16/modern-en ship with the repo; la, nl, pt, es and
16-17th c. English (`en16`) do not, so this run built `tools/data/{la,nl,pt,es,en16}_repo/` from this repo's
own reading*.txt/plaintext*.txt files (source list in each `MANIFEST.tsv`), excluding a candidate ciphertext's
own folder from its own scoring corpus. Language per key: from its own folder's reading-file text (a
character-trigram match against a reference profile -- fr/de/it/en from the corpora above, la/nl/pt/es/en16
anchored on the Lord's Prayer, the standard low-resource bootstrap), else a NOTES.md keyword, else `?` (4 keys).
`judge_plaintext.py`'s FOLD table gained ã õ á í ó ú ñ (Portuguese/Spanish accents it was missing) -- its
`--selftest` still passes.

**Positive control (rule 5): 1 of 56 parseable keys rank their own ciphertext first with z>=4 against both
controls.** 16 rank their own text first at all; of those, 13 clear z_shuffled>=4 (the decode+score pipeline
reliably prefers the true key to a relabelling of itself). The bottleneck is z_unrelated: 5 have too few other
keys of the same design+sign-type to form a null (z_un unmeasurable, not failing), 7 score a real but
under-4 z_unrelated (0.49-3.73 -- short letters and thin non-fr/de/it corpora limit the model's resolving
power at this scale), and only `huntington-blathwayt-madrid-1728/key.tsv` clears both (z_sh 4.23, z_un 7.34).
29 keys' own text could not be scored at all (no corpus for their language, or <0.5 coverage on their own
text -- a tokenisation or key-adapter mismatch worth a follow-up, not chased further here). Every key besides
the one pass is marked `unusable` in KEY-CROSSMATCH.tsv and excluded from the hit list, per rule 5.

**Hits: 0. Weak: 0.** With only one key statistically validated on its own text, no cross-match row anywhere
in KEY-CROSSMATCH.tsv reaches `hit` or `weak` under rule 5's own bar -- reported as a clean negative, not
attempted. 271 pairs cleared coverage>=0.5 and were scored but did not beat both controls (`verdict=none`);
they are in the tsv sorted by z_shuffled for whoever tunes the scorer next. No candidate here is a reading;
rule 10 (novelty) and rule 3 (matched control) still apply in full to anything built on top of this.

**Next test, not run here:** raise per-design/sign-type key counts (the null population) before trusting
z_unrelated at all, or substitute a bootstrap resample of one design's own key pool where <4 keys exist.
