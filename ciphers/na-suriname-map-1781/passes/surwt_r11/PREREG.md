# PREREG R11-SURWT -- y = m|n (inv. 373 letter gloss) vs y = d (map context) word test, 2039/2061 readings

Written and pushed 6 Oct 2026 before any score was computed (worker R11-SURWT, LANE-RUN11-account-2).

**Material.** reading_2039_legend_nieuw_tokens.tsv and reading_2061_battery_nieuw_tokens.tsv as committed (Nieuw key).
Target positions: every token whose sign is `y` and whose current value is `d` (grade M) -- 19 on 2039, 5 on 2061 (24).
The two 2061 `y` tokens resolved to s by the blind image call (L04:10, L06:22, exceptions_nieuw_image.tsv) are held fixed
at s and are not target positions. All other tokens keep their current values.

**Line strings.** Per line, token values in order. A token that is a code word (`[..]` group name of more than one letter
value, e.g. stukgeschut, buskruit), a `{plain}` entry, `?` (U) or `·` is a hard break (segment boundary). Two-valued
values `x|y`: first alternative (primary); second alternative as a sensitivity run (reported, not gated).

**Language model.** tools/judge_plaintext.py NgramModel(n=4, k=0.01) trained on LANG_CORPORA["nl18"] (Dutch printed prose
1760s-1790s built for this target, NL18-CORPUS 3 Oct 2026; era matched to 1781). Letters only, no spaces (the cipher
writes no word spaces).

**Per-position score** w(p, v): sum of log10 P over every complete 4-gram inside the segment that contains position p,
with every target position of that line set to v. **Statistic** S(v) = sum of w over the target positions.

**Candidates** d, m, n (scored separately; the letter's gloss "m|n" is supported if m or n passes).

**Null (control that can vary on the statistic):** 10,000 draws (seed 1781), each target position independently
replaced by a letter drawn from the nl18 unigram distribution; S_null per draw. p99 of S_null.

**Pass rule for candidate v:** (a) S(v) > null p99, AND (b) in a paired bootstrap over the target positions
(10,000 resamples, seed 1781) v's summed w beats each of the other two candidates in >= 95% of resamples.
Exactly one candidate passing = that value is a candidate for a verifier (no key change in this job). Two or none
passing = tie / FAIL: y stays M = d, conflict stays as logged in conflicts.tsv.

**Calibration gate (run first; the target is run only if it passes).** Positive control on the same readings, same
window, same candidate set {d, m, n}: the H-graded tokens whose value is n (true answer n). 200 random subsamples of
24 positions (the target's N), seed 1781; each run through the identical pass rule with its own null. Gate: n passes in
>= 80% of subsamples AND d or m passes in <= 5%. If the gate fails, stop: the target test is a non-test at this N,
logged as such. Descriptive (not gated): the same on all H-graded d tokens (N as available).

**Descriptive only (not gated):** count of decoded m in the two readings as they stand, vs the nl18 expected count at
the same letter total.
