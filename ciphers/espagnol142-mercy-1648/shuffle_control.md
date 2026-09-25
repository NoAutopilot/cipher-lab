# espagnol142-mercy-1648: shuffle control (LANE R7 MSHUF, 25 Sept 2026)

Question (AUDIT.md section 3 item 1, "Missing control"): the anneal gap between the target's best score
(-1154.3, marks variant, N=521 K=38) and the matched control's best score (-1321.7, same N/K, es17 corpus,
`cheap_test_1/rerun.sh`) -- is it because the target's own ciphertext carries real sequential (plaintext)
structure, or only because of its skewed symbol profile (38 codes, about 17 letters actually used)?

Test: anneal shuffles of the target's own code stream (`cipher_codes.tsv`), same multiset of signs, order
destroyed, same anneal settings as `rerun.sh` (`--corpus donquijote --corpus buscon --skip NONE --restarts 8
--iters 40000`). Script: `cheap_test_1/shuffle_control.py` (full shuffle across the whole stream, and
`--within-lines` shuffle that keeps each line's own sign multiset but destroys order inside it).

## Setup check

Reproduced `rerun.sh`'s target run, marks variant, anneal seed 3: best score -1154.3 (restarts
`[-1154.3, -1155.0, -1155.3, -1311.5, ...]`), matching the value on file. Setup confirmed.

## Results

| run | anneal seed(s) | best score(s) | best | mean | range |
|---|---|---|---|---|---|
| target (on file) | 2,3,5 | -1154.3 (repro'd seed 3) | -1154.3 | -- | -- |
| matched control, K=38 N=521 (on file) | 1-5 | -1321.7, -1356.6, -1326.0, -1337.4, -1339.1 | -1321.7 | -1336.2 | -1321.7 .. -1356.6 |
| full shuffle, 1 anneal seed each | 1-5 | -1474.3, -1481.7, -1505.6, -1491.4, -1489.4 | -1474.3 | -1488.5 | -1474.3 .. -1505.6 |
| full shuffle, shuffle seed 1, 3 anneal seeds | 1, 11, 12 | -1474.3, -1493.8, -1473.4 | -1473.4 | -1480.5 | -1473.4 .. -1493.8 |
| line shuffle (within-lines only) | 1,2,3 | -1478.3, -1508.9, -1466.1 | -1466.1 | -1484.4 | -1466.1 .. -1508.9 |

Files: `cheap_test_1/shuffled/shuffled_s{1..5}.tsv`, `cheap_test_1/shuffled/lineshuf_s{1..3}.tsv`,
`cheap_test_1/shuffle_s{1..5}.json`, `cheap_test_1/shuffle_s1_anneal{11,12}.json`,
`cheap_test_1/lineshuf_s{1..3}.json`.

## Verdict (rule fixed in advance, brief line 12-14)

Full-shuffle mean -1488.5 is not within 40 of the target (-1154.3 +/- 40 = -1114.3 .. -1194.3) -- nowhere
close. It is also well *below* the matched-control band, even below the control band's own floor minus 40
(-1356.6 - 40 = -1396.6): every one of the 8 shuffle anneals (5 full-shuffle seeds + 3 extra on shuffle 1)
and all 3 line-shuffle anneals scored worse than every one of the 5 matched-control seeds. Shuffling the
target's own sign multiset -- whether across the whole stream or only within each line -- destroys enough
structure that the anneal cannot even reach the control's band, let alone the target's own score.

**Verdict: sequence.** The gap between the target's -1154.3 and the matched control's -1321.7..-1356.6 is
carried by real sequential (plaintext) structure in the target's own code stream, not by its skewed symbol
profile alone. A control built only from the target's symbol multiset, with order destroyed, cannot
reproduce the target's score even approximately -- it does not even reach the matched-control band, which
itself represents a *real* Spanish plaintext enciphered and solved blind. This is cryptanalytic-grade
support (rule 4: S) for the target's anneal basis being a real property of its ciphertext, not an artifact
of scoring against a low-diversity symbol set; it does not by itself establish that the -1154.3 decode is
correct plaintext, only that the gap the reading rests on is not a profile artifact.
