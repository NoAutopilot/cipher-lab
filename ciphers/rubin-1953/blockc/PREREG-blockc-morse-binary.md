# PREREG: Block C as Morse-like or binary (R9-RUBIN4, LANE LANE-RUN9-account-2, 6 Oct 2026)

Committed and pushed before the scored run (rule 3). Script: `scripts/blockc_test.py` (same commit). Not to be edited after the run.

**Target.** Block C of ciphertext.txt as reconciled (R8-RUBIN3): 3 lines, 136 chars (60/37/39), 0/1/'.'/'x'. Line breaks count as
separators. Tokens = maximal runs of 0/1: 31 tokens, 97 bits (token lengths 1-7).

**Encodings (k = 74, enumerated in the script's `encodings()`):**
- M (2): International Morse per token, polarity 0=dot/1=dash and 1=dot/0=dash. '.' and 'x' both act as separators; which is
  letter- vs word-separator does not change the letter sequence the scorer sees, so separator roles are not separate encodings.
  Table: letters, digits, standard punctuation; digit/punct tokens are valid but carry no letter.
- G (2): each token read as a binary number, A1Z26 (A=1..Z=26; 0 or >26 invalid), both polarities.
- BAC26 (10): separators dropped, 97-bit stream, 5-bit chunks A=00000..Z=11001 (>25 invalid), offsets 0-4, both polarities.
- BAC24 (10): same, classic 24-letter Bacon (I/J, U/V merged; >23 invalid).
- ITA2 (20): 5-bit Baudot-Murray letters shift, offsets 0-4 x polarity 2 x bit order (MSB/LSB first); space valid (no letter),
  other non-letter codes invalid.
- A7 (14): 7-bit ASCII, offsets 0-6 x polarity 2; A-Z/a-z letters, space valid, else invalid.
- A8 (16): 8-bit ASCII, offsets 0-7 x polarity 2; same.

**Statistic T** (per decode): letters scored with `tools/judge_plaintext.py`'s NgramModel (en corpus = LANG_CORPORA["en"], 4-gram,
mean log10 P per letter, its own -9.9 for <4 letters); T = (n_letters*score + n_invalid*(-3.0)) / (n_letters + n_invalid).
(The `en` corpus is of unknown reliability per CLAUDE.md rule 3 EN-FOLDS; it is used only as a relative scorer here.)

**Shuffle null** (rule 3): the 136 Block C characters permuted (separators included), 3000 shuffles, seed 1, each decoded under
the same encoding. p_e = (1 + #shuffles with T >= T_target) / 3001. theta_e = the shuffle-null quantile at 1 - 0.05/74.

**Matched control** (same design and length): 200 English windows (en corpus, seed 2), each encoded under encoding e with the
same design (Morse/G: letters as tokens, '.' between letters, 'x' between words, truncated to 31 tokens; bitstream designs:
encoded bits truncated to 97 bits at the same offset convention), then decoded and scored with T. G controls write each letter's
binary with no leading zeros (the target has some leading zeros; a decoder reads either the same way). Control power_e = fraction of control texts with T > theta_e.
An encoding is a TEST only if power_e >= 0.8; otherwise its result is logged "non-test at this length".

**Gate (per encoding, Bonferroni over k = 74):** PASS iff p_e < 0.05/74 AND T_target >= control p05_e AND power_e >= 0.8.
**Shuffled-target check:** for each encoding, the fraction of shuffles with T >= control p05_e is reported; if it exceeds 0.05,
the English-range half of the gate is void for that encoding (the shuffled target already reads "English-range").
No reading is claimed unless an encoding PASSes and its shuffle check is not void. Report target, control and shuffle numbers
for every encoding (blockc/results.tsv). Outcome on a test encoding with no PASS: control-backed negative for that encoding,
conditional on the transcription (rule 2: no image of Q5 itself).
