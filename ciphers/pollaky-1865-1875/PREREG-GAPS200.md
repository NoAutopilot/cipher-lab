# PREREG-GAPS200 (pollaky-1865-1875, gap 1): v-z-capable second instrument for the topic crib

Written and pushed 3 Oct 2026, 18:4x UTC (clock read 18:45), by worker GAPS200-pollaky-1865-1875 (account-4), before any
scoring. Script: scripts/vz_family_crib.py (written after this file is pushed). Seed 200. 0 vision, 0 subagents, 0 requests.

## Hypothesis
Ad 1's 10 signs (1881 print, GAPS174: sign 04 = 1 dash + 4 dots) are a component design, letter = f(S, P), that reads a
phrase on the topic of sibling clear ad Clay 1465 ("Citation duly served ..."). GAPS174 found the crib set unread under
Laura's fixed rule, but 18 of its 29 windows could not be written at all (Laura's alphabet stops at u: no v-z, so no
"served"). This test asks the same question of a rule family that can write every letter.

## Instrument (how it differs from GAPS160/174/178 -- rule 3's third-attempt clause)
GAPS160/178 scored Laura's single rule by frame bigrams (T) and word cover (W); GAPS174 scored the topic crib by positional
matches under Laura's single fixed rule, with 104 shifted/reversed siblings as a rank check only. This is not a further
tuning of that knob. Different instrument on three axes:
1. **Rule family, not one rule.** letter = alpha_n[(a*S + b*P + c) mod n] for every a, b, c in 0..n-1, over three period
   alphabets: n=26 (a-z), n=25 (I=J), n=24 (I=J, U=V); a parenthesised k-dot sign takes S = 0 or S = 4 (two conventions).
   2 x (26^3 + 25^3 + 24^3) = 97,806 rules. Every letter is reachable (wrap-around), so v-z windows such as "served" are
   writable; non-injective rules (e.g. a = 0, or sums) are allowed, so the sign-repeat pattern ABCDEAFGHI is no longer forced.
2. **Look-elsewhere priced inside the statistic.** Statistic F(signs) = max over all 97,806 rules and all crib windows of the
   number of positions where the decoded letter equals the window letter (crib letters mapped j->i for n<=25, v->u for n=24).
   The same max is taken for every control string, so the family's flexibility is in the null, not only in the target.
3. **Crib set unchanged** (the hypothesis, not the instrument): exactly GAPS174's 29 windows (Clay 1465 text plus the 14
   fixed paraphrases, every 10-letter word-start window), now all 29 usable.

## Controls (both can differ from the target on F by construction, rule 3)
- (A) shuffled-sign: 1000 random orders of the target's own 10 (S, P) signs. F depends on order (position-wise match against
  ordered windows), so A can differ from the target.
- (B) random-sign: 1000 strings of 10 signs drawn uniformly from GAPS160's 21 cells (S 1-3 x P 1-6, paren 1-3 dots).
  F depends on the sign values, so B can differ.

## Power (synthetic same-length positive, same family, same crib set)
- (P1) exact: draw a rule at random from the family and a crib window at random; build a 10-sign string over the 21 cells
  that this rule maps to the window (resample if some letter has no cell); score F. 1000 draws.
- (P2) partly wrong: as P1 with 3 of the 10 signs replaced by random cells. 1000 draws.
- power = share of P with F > B p95.

## Gate (fixed now)
- "topic crib supported under the v-z family" only if target F > A p95 AND F > B p95 AND P2 power >= 0.5.
- If P2 power >= 0.5 and the target fails: "crib set not read under the v-z component family" (control-backed for this crib
  set and family only; not a negative on the topic or on component designs outside the family).
- If P2 power < 0.5: "untestable by this instrument at N=10" (rule 3), not a negative. If B's own p95 already equals 10
  (ceiling), the same applies.
- Reported beside the decision: F, best rule (n, paren convention, a, b, c), best window, A and B p95 and tails (share >= F),
  P1/P2 medians and powers; the descriptive count of rules reaching the target's F.

## Grades and wording
Rule 4: no token above M unless supported; even if supported, S only for letters inside a matched window of two or more words,
and a family-max fit is a candidate, not a reading. Rule 10: no reading is claimed; status stays partial.
