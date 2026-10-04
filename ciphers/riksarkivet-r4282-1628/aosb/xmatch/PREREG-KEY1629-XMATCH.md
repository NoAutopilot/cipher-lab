# PREREG KEY1629-XMATCH (4 Oct 2026, written and pushed before any target score)

Key: `aosb/key_aosb1629.tsv` (AOSB-PAIRS, 208f391c). Statistic, null and verdict thresholds: exactly PREREG-AOSB-PAIRS.md
(`aosb_crossmatch.py` functions loaded unchanged: decode_runs, S on la17 4-gram, C coverage, 200 meaning-permuted keys
seeds 1-200, real-text p05; FIT = C>=0.5 & S>null p99 & S>=real p05; WEAK = C>=0.5 & S>null p99; NO FIT = C>=0.5 &
S<=null p99; C<0.5 = inapplicable, coverage reported, not a negative).

Control first: the same LOFO control on the 16 AOSB footnotes is re-run in this script; if it does not pass
(C>=0.5, S>null p99) no target is scored.

Targets: every file flagged by `xmatch/inventory.py` (inventory.tsv; a = Swedish-related keyword in NOTES, b = 1620-1640,
c = numeric, 2-digit values >=80% in 12-91, >=3 codes of 3-4 digits), one canonical file per folder (the first of
ciphertext_verified / ciphertext / the longest draft), excluding R4284/R4282 (already scored by AOSB-PAIRS). Tokens are
the transcription's tokens with '?' and punctuation stripped; a token that is not in the key breaks the run (as in AOSB-PAIRS).

Caveat fixed now: S is a Latin model; a target in another language that genuinely used this table would score below real
p05 but should still beat the permuted null (WEAK). Any FIT or WEAK is a lead for a verifier, not a reading.
Multiple testing: about 25 targets at p99 each -> expect about 0.25 false WEAKs; a WEAK with share_null_ge_S > 0 is reported
as such. No threshold changes after scores are seen.
