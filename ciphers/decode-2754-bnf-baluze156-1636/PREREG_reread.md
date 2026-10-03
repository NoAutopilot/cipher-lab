# Pre-registration: f.157r re-read and merged-table re-score (GAPS35, account-4, 3 Oct 2026, written 06:2x UTC)

Committed and pushed before either blind pass returned and before any score of the re-read was computed.

**Step.** NOTES.md Verdict (FT4d): "re-read f.157r against Sabran's sign shapes and re-score under the merged f.146r+f.247 table".

**Transcription.** Native region of Gallica btv1b9001409q canvas f161 (x 3900, y 250, 3600 x 5400), cut by
`python3 tools/iiif_lines.py --image images/f157/src_ark_12148_btv1b9001409q_f161_3900_250_3600_5400.jpg --out images/f157
--prefix f157r --centres 2025,3041,3126,3220,3315,3403,3505,3877,3976,4073,4171,4282,4771 --lines-per-crop 1 --top-margin 60
--bottom-margin 40` (13 cipher-bearing lines, 26 crops; crop L01..L13 = draft lines L12, L23-L28, L32-L36, L41).
Two blind Opus passes read the cipher runs only, using a sign vocabulary named after the f.146r/f.247 keys' shapes
(Pc, 7d, a+, 6 vs b, Φ, ll, nn, tt, ff, ſ, epsilon-E, overbars) but given no values. The worker reconciles the
two passes (one reconciliation step) into `ciphertext_reread.tsv` (line, position, sign).

**Merged key** (`reread_trial.py`, fixed now): the 'kept' rows of images/fr4140/key_f146.tsv and images/f247/key_f247.tsv;
a sign in one key keeps its value; a sign in both keeps it if the letters agree, else it is dropped (a, d, ff, o, y
conflict); P = Pc = A. 31 sign names.

**Statistic and control.** French 5-gram bits/char of the decoded runs (unmapped token breaks a run), against 200
shuffled merged keys (letters permuted over signs). The permutation changes every decoded letter, so the control can
differ from the target on this statistic. Positive control: held-out French of the re-read's run lengths enciphered
with the merged key.
Rows: A = 24 Sept draft under the merged key (comparison), B = re-read under the merged key (the test).
**Gate:** B "reads" only if share of shuffles as good < 0.01 AND B bpc < positive-control bpc + 0.5; otherwise a
negative, matched. A variant read made after scoring is reported as a variant, never as the test.
