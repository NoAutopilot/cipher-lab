# PREREG-C1161RA: joint re-anneal of the M signs (+ contested S 4, S) with C and agreed S held

RUN5-C1161RA (account-1 worker, LANE-RUN5), 4 Oct 2026, written and pushed before any anneal or score.
Brief: `.claude/briefs/runs/2026-10-04-acct1-run5-wave2.md`. Script: `two/reanneal.py` (pushed before it is run). Disk only.

**Stream.** All six leaves/blocks (`two_instr.stream()`), tokens not in key.tsv (the 33 U tokens) dropped, as
`two/full_decode.txt` is built.

**Held (never move).** The 6 C signs (a d e ee p sd) and the 13 agreed S signs (+ 3 7 9 box f iii q qb s tri w wb y).
**Free (target arm).** The 27 M signs plus the contested S signs `4` and `S` (29 signs). qb stays held (brief names 4 and S;
RUN4-C1161GJ found qb = a best of 26 on both statistics).

**Instrument, per seed.** Stage 1: `tools/homophonic_anneal.solve` with `fixed` = held values, model = fr17 corpus
(`tools/data/fr17/*.txt.gz`) at order 4 (4-grams), uni_w 1.0, restarts 32, iters 40000. Stage 2: coordinate ascent over the
free signs (each sign x 26 letters, sign order shuffled by the seed) on
J = (sum of 4-gram log-probs)/n + W x cover, cover = RUN5-C1161WC's word cover (fr17 + fr16 vocabulary, len >= 3, freq >= 3);
passes until no gain, at most 4. **W is fixed by formula before any target number:** on held-out genuine fr17 text (Mazarin
letters, chars 300000-303375 of lettresducardina01maza, excluded from both the calibration 4-gram model and the calibration
vocabulary), W = (L_real - L_shuf) / (C_real - C_shuf), mean over 20 letter shuffles -- the two terms then weigh the
real-vs-noise gap equally. Era note: the spec's judge uses fr16 (c.1570); the brief names fr17 4-grams; the planted control
below is what licenses the instrument at this corpus, not the corpus choice.

**Seeds.** 1-10, both arms. Consensus letter of a sign = its letter in >= 7 of 10 seeds' final keys.

**Planted control (runs first, gates the target).** k = 3 C signs freed and planted at a wrong starting value e:
`a` (true u), `p` (true c), `d` (true n), together with the same 29 free signs, all else held. A planted sign is
**recovered** when (i) its consensus (>= 7/10) is its true value and (ii) its gain dJ = J(K* with true) - J(K* with planted e),
K* = the consensus key (seed-1 key where no consensus), exceeds the p95 of the shuffled-value null below.
**Gate: >= 2 of 3 recovered.** If not: stop, log NON-TEST, do not run the target arm, do not tune W, seeds or recipe.

**Shuffled-value null (per sign).** 50 contexts: K* with the free signs' values (other than the tested sign) randomly
permuted among themselves (seeded 1-50); in each, dJ_null = J(sign = B) - J(sign = A). Can differ from the real dJ: the
permutation changes every neighbouring letter of the sign, so a gain that comes from the letter's own frequency survives in
the null and one that comes from the context does not.

**Target decision per free sign** (A = key.tsv value, B = consensus):
- B exists (>= 7/10), B != A, dJ(B vs A) > 0 and > null p95: value changes to B, grade S (cryptanalytic with a control).
- B exists, B == A, and the second-best letter's dJ vs A over K* is < 0 with -dJ > null p95 (A beats the best alternative
  beyond the null): M -> S (or 4/S confirmed S); otherwise grade unchanged.
- Else: no change. Every sign's numbers are reported (`two/ra/signs.tsv`).
key.tsv changes only for signs that clear; then `tools/decode_key.py ciphers/clair1161-avis-flandre-1688` and `--check`;
a changed letter owes a rule-7 re-derivation and AUDIT.md propagation (named in Remaining gaps, not done here).
