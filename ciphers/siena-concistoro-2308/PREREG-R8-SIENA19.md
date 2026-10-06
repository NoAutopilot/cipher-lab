# PREREG R8-SIENA19 -- no. 19 against the no. 13/16 alignment (written 6 Oct 2026 ~04:24 UTC, before any score)

Job R8-SIENA19, account 4 worker for LANE LANE-RUN8-account-4. Committed and pushed before the scored run (rule 3).

## Key under test (the "no. 13/16 alignment")
Bourdeau, dbourdeau/cyphersolver `targets/siena1421/NOTES.md` (HEAD adbf9a1), no. 13 (R4801) + no. 16 (R4804, the clear
decipherment): "bologna = ∇ E 3 E 17 φ ₀⁰; accordi con = ₀ ⁿθ(cc) E ‡ + 15 ƥ E φ". Read as one sign per letter:
∇=b, E=o, 3=l, 17=g, φ=n, ₀⁰=a, ₀=a, ⁿθ=c (doubled), ‡=r, +=d, 15=i, ƥ=c. Twelve sign values, ten distinct letters
{a,b,c,d,g,i,l,n,o,r}. This is the whole alignment on disk: no transcript of no. 13 exists in either repository.

## Sign concordance to no. 19 (Bourdeau agent J legend, transcripts/no19.tok), fixed now
- Primary (P): TRI (inverted triangle ▽) = ∇ -> b; 3 = 3 -> l; CT (c-like curve crossed by a vertical, "¢ / ‡-like") = ‡ -> r.
- Variant (V2, wider): P plus 0 (small 0) = ₀ -> a; TT (double cross ŧŧ) = ‡ -> r.
- Not matched: E, 17, φ, ⁿθ, +, 15, ƥ have no counterpart in the no. 19 legend (no E; no 17 or 15 as written pairs; f is
  "ƒ with cross-bar", not φ). Stated, not tested.

## Statistics (computed on transcripts/no19.tok, N = 118 cipher tokens)
- S1, order-free count fit: for each matched sign s with value v, log10 P(X >= count_s) under Binomial(118, p_it(v)),
  p_it from the it16 corpus letter frequencies; S1 = sum over matched signs. Upper tail only (homophones may make a sign
  rarer than its letter, never commoner). Higher = better fit.
- S2, order fit: mean log10 P_it(v2 | v1) (it16 bigram, add-one) over adjacent covered pairs; adjacency runs across line ends
  except where "|" marks clear text; uncovered tokens break adjacency.

## Controls (rule 3: each must be able to differ from the target on its statistic)
- (a) value-shuffled keys, 2000 seeds: matched signs get distinct values drawn at random from the key's own ten letters.
  Varies S1 (expected counts change) and S2 (bigram values change). Used for both.
- (b) order-shuffled stream, 200 seeds (all 118 tokens permuted, "|" breaks dropped): varies S2 (which pairs are adjacent).
  Cannot vary S1 (counts are order-free) -- NOT used for S1.
- Positive control (power): 100 it16 passages of 118 letters (fixed seed). Under H1 the matched letters' every occurrence
  is written with the matched sign (variant H1a), or half of them (H1b, homophone thinning). Score the true values vs the
  same 2000-style value shuffle (500 per passage); power = share of passages where the true key reaches the gate.

## Gate
Fit claimed for a statistic iff the real key scores at or above the 95th percentile of control (a) (rank p <= 0.05).
A miss is a control-backed negative only where positive-control power >= 0.8 at this N for that statistic and variant;
otherwise it is logged "non-test at this N". No key rebuild, no decode beyond the matched signs (brief).
Script: specs/cheap-tests/siena-concistoro-2308/run_test_no19.py (seeds fixed).
