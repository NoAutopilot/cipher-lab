# Michell sibling-key test (FT4, account-4, 3 Oct 2026)

Source: DECODE (de-crypt.org) R1050 (Michell, London, 28 Aug/8 Sept 1752, KHA PWV inv. 198, 2 pp.) and R1051
(Michell, London, 1/12 Nov 1751, same inv., 1 p.), both "Decrypted". Fetched after one browser login, 3 Oct 2026:
DOC_R1050_D1938_1938.txt and DOC_R1051_D1940_1940.txt (DECODE transcriber "XZ", March 2020; the period Dutch
decipherer's interlinear French over each 4-digit code line), committed here unchanged. Full-size page images were also served
(not committed, 19-20 MB each; re-fetch with tools/decode_browser_login.js 1050 OUT --fetch-page ... --guess-fullsize):

| file | px | sha1 |
|---|---|---|
| IMG_R1050_I5502_P1.png | 5472x3648 | 7bde68180265867ba644415b6199471150f7db6f |
| IMG_R1050_I5503_P2.png | 5472x3648 | 7073f7b4be62b2ad2859e14430e6a38a8b815a64 |
| IMG_R1051_I5504_P1.png | 5472x3648 | 910ba1b99c6761e881980159f19f1ddc8fc94935 |

- `build_key.py [--check]` -> `key_sibling.tsv` (268 codes, 14 with conflicting glosses, grade S: a sibling key's values, rule 4).
  Pairs word-for-code only on lines whose word and code counts match (47 lines paired, 5 skipped). Built from the
  DECODE transcription, not from the image (rule 2: conditional on it).
- `test_sibling.py` -> `test_sibling_output.txt` (overlap, value-shuffle control x200, positive control, power).
- `decode.json` -> `reading_R1953_sibling.txt` via `tools/decode_key.py ciphers/hellen-frederick-1752/sibling_michell [--check]`.
  NOT a reading; kept so the negative is reproducible.
