# Pre-registration, DUCH-KEY1B (account 1 for LANE-A1), 3 Oct 2026, written before any score below was computed

Key: keys/key_no1.tsv (fr.3995 f.2r [Gallica canvas 10; Tomokiyo's "no.1, fol.1", docketed "Juin 1580" on f.1r]).
Ciphertext: ciphertext_f10_digits.tsv (raw digit strings per line, this worker's read of f.10r).
Segmentations scored: S1 Tomokiyo's 37 numbers as printed; S2 each line's digit run paired from its start (two-digit
units, the key's own instruction "keep even space so as not to reveal the figures are in units of two"); S3 each line
paired from offset 1 (first digit dropped). The non-numeric sign that opens lines 2 and 3 is skipped (no key value).
Decoding: letters from the alphabet table, code numbers expanded to their written name, nulls dropped, unkeyed
numbers dropped and counted.
Statistic: tools/judge_plaintext.py NgramModel over LANG_CORPORA["fr"] (fr16), mean log10 4-gram per letter.
Null: 200 value-shuffled keys (the value column permuted over the same code set, seed 1..200), same decode.
Report: rank of the real key among 201, z against the 200 shuffles, and judge_plaintext verdict (spec
specs/fr4712-nevers-duchesse.json, language fr, min_word_cover 0.5).
Gate: a segmentation "reads" only if rank = 1 of 201 AND z >= 3 AND judge PASS.
Power control: 20 synthetic texts, each a random fr16 window enciphered with key no.1 (random homophone, no codes, no
nulls) truncated to 37 tokens, then digit errors injected at 3% per digit (1 uncertain digit of 74 read on f.10r,
rounded up), segmented as S2; power = share of the 20 with rank 1 and z >= 3. Power < 0.8: the target result is a
non-test, whatever it is.
