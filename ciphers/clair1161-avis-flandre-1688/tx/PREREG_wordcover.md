# PREREG-C1161WC: word-cover value test of the M and contested S key signs (RUN5-C1161WC, 4 Oct 2026)

Written and pushed before any score below is computed (headroom numbers included). Disk only, no network, no subagent
calls. Script: `two/wordcover.py` (committed with or before the first scored row). Outputs: `two/wordcover_headroom.tsv`,
`two/wordcover.tsv` (per sign x value), `two/wordcover_gate.tsv`.

## Signs tested
All 27 M-graded signs of key.tsv (2 6 6r 8 K L Sorn blot c dia eloop iib l ls o phi psi rc rot spiralG sqc th to tz vdash x z)
plus the three contested S signs `4` (o), `S` (u), `qb` (a) (RUN4-C1161GJ). A = key.tsv value. Each sign alone, every
other sign at key.tsv. Floor: a sign with fewer than 3 tokens (Sorn, blot, spiralG: 1 each) is scored and reported but
cannot pass.

## Statistic
Text = letters-only decode of all cipher signs of `ciphertext.tsv` (`/` and PLAIN/NEW tokens contribute nothing, exactly
as two/glossjudge.py; reproduces `two/full_decode.txt` under key.tsv). Vocabulary = every word of length >= 3 occurring
>= 3 times in the union of the fr17 corpus (tools/data/fr17, six files, 1617-1644 letters, era nearer 1688) and the
spec's fr16 judge corpora; folded lowercase, accents stripped, j->i, v->u, non-letters split words. **Cover** = the
maximum number of decoded letters that can be covered by non-overlapping vocabulary words (dynamic programme over the
unsegmented text, words up to 15 letters), divided by the text length.

## Rule 3 headroom check (run first; a failure stops the job as "non-test", no per-sign row is gated)
- C0 = cover(key.tsv decode); Cs = mean cover of 200 token-order shuffles of the same decode (seed 0..199).
- Genuine: a 3375-letter stretch of fr17 file lettresducardina01maza (letters 300000-303375) scored against a vocabulary
  built WITHOUT that file (leave-one-file-out); Cg = its cover, Cgs = mean of 50 letter-shuffles of it.
- NON-TEST if any: C0 >= 0.95 (ceiling); Cs >= 0.90 (noise at ceiling); Cg - Cgs < 0.10 (no discrimination on real
  French at this N); C0 - Cs < 0.02 (the decode is indistinguishable from its own shuffle by this statistic).

## Nulls
1. **Order-shuffle null (200 draws).** Same key, the cipher token order shuffled (seed 1000+i); per draw, D_null =
   max over 26 letters v of cover(sign=v) - cover(sign=A). Can differ from the real D because cover depends on letter
   order; a gain that only reflects unigram frequency (B commoner than A) appears in the null too. p99 = 198th of 200.
2. **50-key anneal null.** The 50 shuffled-order anneal keys `two/cons/key_shuf*_s*.tsv` (as RUN4-C1161GJ; signs absent
   from a key take key.tsv's value): d_null = cover(sign=V) - cover(sign=A) under that key; p95 = 48th of 50.
3. **26-letter null.** Rank of every letter a-z for the sign.

## Gate
- **Change to V != A** (V = the argmax of the 26 letters on the real decode): (i) cover(V) > cover(A); (ii) D = cover(V) -
  cover(A) > order-shuffle p99 of D_null; (iii) D > the 50-key p95 of d_null for the same V vs A; (iv) >= 3 tokens.
- **Confirm A**: A is the argmax of 26 and its margin over the runner-up R exceeds (ii') the order-shuffle p99 of
  [cover(A) - max_{v!=A} cover(v)] and (iii') the 50-key p95 of cover(A) - cover(R); (iv) >= 3 tokens.

## Planted-value control (run before the target signs; both must recover or the whole run is "non-test")
The two most frequent C-graded signs, `p` (c, 112 tokens) and `a` (u, 98 tokens), each planted at the wrong value 'e'
in an otherwise key.tsv key; the same "change" gate with A = 'e' must pick the true value (c, u) as the argmax and pass
(i)-(iv). (If the control picks a different letter or fails a clause, it is reported and the target is not gated.)

## Actions
- Change passes: key.tsv value -> V, grade S, source note "RUN5-C1161WC word-cover gate PASS"; decode_key.py regenerates
  the reading; rule-7 re-derivation and AUDIT.md propagation are owed (not by this worker).
- Confirm passes: value unchanged; M -> S with source note "RUN5-C1161WC: key value confirmed by word cover"; S signs
  keep S with that note.
- Neither: nothing changes. Every sign's numbers are reported in NOTES.md either way.
- Multiple testing stated in advance: 30 signs x p99 order-shuffle clause -> about 0.3 false clears expected from that
  clause alone before the 50-key clause; reported, not corrected further.
