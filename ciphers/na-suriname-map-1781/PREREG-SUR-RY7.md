# PREREG-SUR-RY7 (14 Oct 2026, account 4, LANE DEFAULT-A4-0935-14) -- written and pushed before any score is computed

Question: two r-vs-7 slots in the 4.VEL 2039 legend (Nieuw key: sign r = t, sign 7 = e).
- **k6** (2039_leg_k pos 6, transcribed r, conf M; shape looks split, two shape instruments retired by SUR-POS6/POS6B):
  decoded word s n e d e r [k6] y e n -- reading t "snedertyen" vs e "snedereyen".
- **l3** (2039_leg_l pos 3, transcribed r, conf H): decoded word b a k [l3] r e y -- reading t "baktrey" vs e "bakerey".
Honesty note: SUR-CRIB (13 Oct) already remarked by eye that e gives a word at both slots; the test below is designed to
say whether the family's own spellings support that beyond the letter-frequency prior (e is far commoner than t).

Corpus ("this map family's own spellings"): the two plain cribs on disk, crib_2038_legend.tsv and crib_2042_legend.tsv,
`text` column, every row. Normalisation (PX-BRODEC lesson, one convention for both sides): lower case; "ij" and "ÿ" -> "y"
(the decode writes ij as y); every non-letter -> word break; words of length >= 1 kept. No decoded text enters the corpus.

Statistic: character trigram model with word-boundary pads (^^w$), interpolated P = 0.6 P3 + 0.3 P2 + 0.1 P1, each order
add-0.5 smoothed over 27 symbols (a-z + boundary). For a slot, Delta = sum of log P(c_i | c_{i-2} c_{i-1}) over the three
trigrams whose last two..one positions cover the slot (i = slot, slot+1, slot+2), with letter e minus letter t
(Delta > 0 favours e). Decoded neighbours used as they stand in reading_2039_legend_nieuw_tokens.tsv with [u-dots] k1 = n
and "k|i" l2 = k (the reading's first option); word = the whole decoded line (no spaces in it).

Known-answer instrument check (must pass before either slot is scored): every t and every e in the normalised crib words;
for each, the model is trained on the corpus with that crib row held out (leave-one-row-out), and the call is
argmax over {t, e} of the same three-trigram sum. Report N, overall accuracy, per-class accuracy (truth t, truth e).
Letter-shuffle control: 200 seeds (seed 20261014 + s); letters shuffled within each word of the training corpus (unigram
counts kept, spelling order destroyed); recompute the known-answer accuracy and the two target Deltas each seed.
This control can differ from the target on the statistic (it changes trigram order, which is what Delta measures).

Gate:
- G1 (instrument): real accuracy >= 0.80 AND per-class accuracy >= 0.60 for both t and e AND real accuracy >=
  shuffle p95 accuracy + 0.10. If G1 fails: NON-TEST, nothing changes at either slot, logged untested-by-this-tool.
- G2 (per slot, only if G1 passes): Delta_real beyond the shuffle distribution in its own direction (Delta_real > p95 of
  shuffle Deltas if > 0; < p05 if < 0) AND |Delta_real| >= median |Delta| of the correct known-answer calls.
Actions (only on G1 and that slot's G2):
- k6 favours e: exceptions_nieuw_image.tsv row 2039_leg_k 6 -> value e, grade I (repaired: transcribed sign r, spelling-
  inferred 7), note in ciphertext_2039_legend.tsv; sign column NOT changed (ciphertext never silently repaired).
  k6 favours t: exceptions row value t grade S.
- l3 favours e: ciphertext_2039_legend.tsv conf H -> M with a note; value not changed. l3 favours t: note only.
- Any slot failing G2: no change, note only.
After: `python3 tools/decode_key.py ciphers/na-suriname-map-1781 --check` exit 0.
