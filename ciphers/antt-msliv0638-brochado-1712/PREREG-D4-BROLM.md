# PREREG-D4-BROLM (8 Oct 2026, LANE DEFAULT-account-4-20261008-0740)

Written and pushed before any score is computed. Script: `scripts/23_d4brolm_lm_rescore.py` (written after this file).

## Instrument
- Language model: `tools/judge_plaintext.py` `NgramModel` (letter 4-gram, add-k 0.01, a-z fold), trained on the `pt18`
  corpus files exactly as `LANG_CORPORA["pt18"]` lists them. pt17 is reported as a secondary run only; no gate uses it.
- Decoder: exact Viterbi (state = last 3 letters) over a span; every unmasked position is fixed to its key-decoded letter;
  each masked position ranges over all 26 letters with score log10 P_LM + log10 prior(letter | class). Spans are decoded
  separately (letter 134: Span A = m0275-r1 + m0276-r1, 50 tokens; Span B = m0276-r2, 20 tokens).
- Priors: class K (keyed code c): add-0.5 smoothed counts over 26 letters of the gloss letters aligned to code c in
  `align/align_mask_9.tsv` (kind=code rows with a one-letter plain_chunk, any status), fallback key.tsv
  all_observed_letters when c has no aligned row (only `ff`: {s:1}). A token whose transcription is M with a named
  alternative code (m0275-r1 pos 4: 10 vs 16; pos 2: 8 vs 9) takes the 50/50 mixture of the two codes' priors.
  Class U (no key row: m0275-r1 pos 31, m0276-r2 pos 16): uniform prior.

## Open tokens of letter 134 (the candidate set: all 26 letters at each)
Masked = every token graded M or U in reading_body_tokens.tsv for m0275-r1, m0276-r1, m0276-r2, plus every C token on
the thin codes x, z, d, f, 16, ff (the NOTES thin-code gap). Computed by the script from the file; expected 26 tokens
(Span A 19, Span B 7; U 2). The list the script prints is the list scored.

## Known-answer control (run first; target is not scored unless it passes)
- Units: windows from the appendix's own aligned stream (`align/align_mask_9.tsv`, 38 entries). Each row contributes its
  key-decoded letter (code rows, key.tsv value) or its folded clear word (clear rows), mirroring letter 134's context,
  which is key-decoded letters. Window lengths 50 and 20 letters (Span A / Span B). Truth at a masked code token = the
  aligned gloss letter (plain_chunk). Only code tokens with a one-letter plain_chunk can be masked.
- Mask load per window = the target span's own: Span-A-type and Span-B-type windows mask exactly as many K and U tokens as
  the target span has (counts printed by the script), positions drawn at random among eligible code tokens.
- Prior for a control K token: leave-one-entry-out (counts from every other entry); U tokens: uniform.
- 300 windows per span length, seed 20261008.
- Shuffled-context null: the same windows with the unmasked letters randomly permuted (seed 20261009), same masks/priors.

## Gates (all pre-set here)
- G-U (open slots, decides S3/S4): control top-1 accuracy on U-class tokens >= 0.40 (26-way) AND exceeds the
  shuffled-context null's U accuracy by >= 0.15. If met, the target's U slots get the decoder's letter at grade S.
- G-K (keyed overrides, decides any value change on K tokens): an override = decoder letter != prior argmax. Control
  override precision (override == truth) >= 0.60 with >= 20 overrides in the control, AND overall K accuracy (decoder)
  >= prior-only K accuracy. If met, a target K token whose decoder letter differs from its current value is changed at
  grade S (never higher); otherwise no K value changes.
- Headroom check (rule 3): prior-only K accuracy on the control is reported; if it is >= 0.95 the K gate is reported as
  "no headroom" and G-K is a non-test regardless of the numbers.
- If G-U and G-K both fail: stop, log "non-test at this N" in HYPOTHESES.md/NOTES.md, score nothing on the target.
- After any change: decode_key --check, scripts/20 --check, judge pt17 + pt18 on reading_body_letter134.txt.
