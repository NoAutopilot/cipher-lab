# PREREG-K60 -- order-sensitive local-anchor test of key no.60 on f.91 (BNF-K60, 13 Oct 2026, account 2)

Written and committed before any score (target or control) was computed. Brief: .claude/briefs/runs/2026-10-13-ytbiz-bnf-k60.md.
Only a timing probe on one random tag string was run before this file (stat speed 0.5 ms; no S value read or kept).

Hypothesis: the cipher lines of BnF fr.3622 f.91 (Nevers to Gondi, 27 Mar 1594), L02-L05, are in Nevers key no.60.

## Instrument (`scripts/k60_order_test.py`)
- Key: `ciphers/fr3986-nevers-revol-1593/key.tsv` as synced to D. Bourdeau's key60 @c60e6dd in this job (commit before this
  file). Every table alternative of an M tag is allowed (a|b|c); values folded with `judge_plaintext.fold` (a-z only), so
  word- and syllable-valued tags contribute their letters ("le Roy" -> leroy).
- Tokens: `ciphertext.tsv` L02-L05 as committed, `w:` clear tokens dropped, trailing `?` stripped (as G60R): 134 tokens.
  A tag absent from key.tsv is unkeyed and breaks a run.
- Lexicon: tools/data/fr16 (the three `_djvu.txt.gz` files: Lettres de Catherine de Medicis t.1 and t.2, Lettres
  inedites de Marguerite de Valois), words folded, length >= 4, seen >= 2 times. Built in code, not copied from Bourdeau.
- Statistic S: length in letters of the longest lexicon word spelled inside any contiguous run of keyed tokens, under
  any choice of alternatives; a word may start and end inside a token's value (substring of the run's letters). This
  differs from Bourdeau's f88 control, which needs a word to start and end on token boundaries, first variant only.
  S = 0 if no word of length >= 4.
- Null: 5000 random permutations of the token POSITIONS within L02-L05 (all 134 tokens, unkeyed included; values and
  multiset unchanged). p = share of shuffles with S >= real S (also reported: (ge+1)/(n+1)).
- Orthogonality check (rule 3): S depends on which tokens are adjacent, and a permutation changes adjacency while keeping
  the values; so the null CAN differ from the target. (Unlike G60R's word cover, which was order-blind in effect.)

## Controls
- Positive: 200 synthetic texts, windows of fr16 Catherine t.2 (`lettresdecatheri02`), enciphered with the same key.tsv by
  G60D's greedy longest-value rule (word/syllable entries where the window has them, uniform homophone), N = 135 tokens;
  then sign substitution: each token replaced by a uniformly drawn key tag with probability ERR; then 18% of positions
  (24 of 135, f.91's 24/135) set to an unkeyed tag. Control lexicon = fr16 WITHOUT Catherine t.2 (held out, so the
  control's words are not guaranteed to be in its lexicon). Each text: S vs 5000 position shuffles, same p rule.
  ERR in {0.00, 0.15, 0.25, 0.35}; 0.35 = f.91's measured reader disagreement (G60E pass agreement 0.65). Power = share of
  the 200 texts with p <= 0.01.
- Negative: 200 random tag strings, N = 135, tags drawn i.i.d. from f.91's own L02-L05 tag frequencies (unkeyed tags
  included as they occur); same S, same 5000 shuffles. False-positive rate = share with p <= 0.01.
- Seeds fixed in the script (texts 60000+i, shuffles 70000+i, target shuffles seed 91).

## Gate (fixed now)
1. Instrument valid only if negative-control false-positive rate <= 0.05.
2. Control power at ERR = 0.35 must be >= 0.80 at p <= 0.01. If below: the target result is a **non-test** at this N and
   error, whatever its p ("non-test (control power .. at 35%)").
3. If 1 and 2 hold: target p <= 0.01 -> "beats order-shuffle at p=..; control power .. at the 35% error band";
   target p > 0.01 -> "control-backed negative at this N" (for this instrument and transcription, not of key no.60 in general).
4. Order of runs: negative control, positive control (0, 0.15, 0.25, 0.35), then the target once. No parameter changes
   after any score; any deviation is logged here as an amendment with the reason, and the result is then reported as
   unregistered.
5. A pass is not a reading: it goes to a separate verifier; nothing is graded above M by this job.

Credit: shape of D. Bourdeau's `targets/nevers1593/f88/shuffle_control.py` (cyphersolver, MIT, c60e6dd, 12 Oct 2026, from
issue #32 by R. Weglarek); key no.60 transcription D. Bourdeau (CC BY 4.0), numbering S. Tomokiyo.
