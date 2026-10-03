# PREREG-GAPS193: bracketing the unglossed nomenclator groups (3 Oct 2026, 18:2x UTC, account-4)

Written and pushed before any statistic, control or bracket is computed. Script: `keys/bracket_gaps193.py` (not yet
written at push time).

## Third-attempt clause (rule 3)

NOTES.md, HYPOTHESES.md and AUDIT.md were grepped for "bracket": no bracketing, ordering or block test has ever been run
on this letter's nomenclator (NOTES "Remaining gaps" gap 3: "no key-rebuild, bracketing or context fill has ever been
run"). This is attempt 1, so the clause does not apply.

## Honest disclosure

The 18 gloss-pinned codes in key_gloss.tsv were visible when the statistics below were chosen. Their rough shape (a
Denmark cluster at 601-605, Kurbrandenburg at 651-681, 774/775 adjacent) was noticed by eye. So the topical statistic
(S2) is chosen *after* seeing the data. That is why S1 (alphabetical, the design the NOTES originally asked about) is
reported too, why both have a matched synthetic control, and why a PASS licenses at most M.

## Units

- Testable codes: the key_gloss.tsv rows graded C or M, excluding 690 (Bleinenk?l, referent unidentified) and 634 (I,
  the inferred value under test). That leaves 16 codes: 229, 303, 437, 447, 601, 602, 605, 641, 651, 653, 681, 768,
  774, 775, 834, 5756. 625 is M but is one of the groups under test, so it is excluded from the statistic too.
- Groups under test: 625 (x2 tokens), 634, 68, the margin 7480.
- 68 is a 2-digit group in the letter-table range (20-179), not a nomenclator code. No nomenclator bracket applies, and
  it is logged as out of scope for this statistic, with its letter-table reading unchanged.
- 7480 is a 4-digit margin number. The only other 4-digit group, 5756, may be a 3-digit code plus a sign (NOTES). There
  is no bracket either side, so it is logged as not bracketable.

## S1: one-part alphabetical order

Headword = the first word of the gloss as transcribed, lowercased, with the bracket and dots stripped: 229 berlin, 303
alliance, 437 hertzog, 447 kayser, 601 dennemarck, 602 konig, 605 k (K. = Konig), 641 von, 651 cur, 653 cur, 681 cur, 768
sueco (the ?ueco gloss, read as S), 774 holland, 775 gen, 834 rex, 5756 franckreich. Statistic: Kendall tau between code
and headword rank.

## S2: topical blocks

Topics are fixed here, before computing:

| topic | codes |
|---|---|
| DK | 601, 602, 605, 834 |
| BRAND | 229 (Berlin), 651, 653, 681 |
| HOLST | 437, 641 (the Hertzog von Ploen pair) |
| NL | 774, 775 |
| EMP | 447 |
| SWE | 768 |
| FRA | 5756 |
| OTHER | 303 |

Statistic: sort the 16 codes and count the adjacent pairs that share a topic. The p-value is the exceedance of the
target's count over 10,000 shuffles of the topic labels among the same 16 codes. Sensitivity variant (reported, not
gated): DK and HOLST merged as one topic.

## Matched control (code+mark design, the letter's own N and K)

The letter's design: a 2-digit letter table (key 255, 20-179) plus a 3-digit nomenclator, with N = 26 nomenclator
tokens and K = 16 testable distinct codes, in a range of about 200-850. For each control, 1,000 synthetic letters are
generated, each with 16 distinct codes drawn from a synthetic nomenclator of 650 codes (200-849) whose referents carry
the same topic multiplicities (4, 4, 2, 2, 1, 1, 1, 1). For S1 the referents carry the same headword multiset. Each
control is run under two designs:

- **Structured (power).** S1: a one-part alphabetical code list (the codes ascend with the headword's alphabetical
  rank, plus gap jitter). S2: a topical-block list (each topic occupies one contiguous block, and the block order is
  random).
- **Unstructured (size).** A two-part list: the codes are a random permutation of the referents.

Gloss noise is injected at 0, 0.2 and 0.4 (the share of M among the 16 testable codes is 6/16 = 0.375, so 0.4 brackets
it): each code's label is replaced by a random other label with that probability. The statistic is computed on the
synthetic letters exactly as on the target. Power = the share of structured letters with p < 0.05. Size = the share of
unstructured letters with p < 0.05. The control's statistic varies with the design (a structured list puts
same-topic codes adjacent, an unstructured one does not), so the control can differ from the target on the statistic
itself: this is not an orthogonal non-test.

## Gate

A statistic (S1 or S2) licenses a bracket only if all of the following hold:

1. its control has power >= 0.8 at noise 0.4 and size <= 0.07 at noise 0;
2. the target's p < 0.05.

If (1) fails, the result is "non-test at this N" for that statistic. If (1) holds and (2) fails, it is a
control-backed negative for that design at N = 16.

## What PASS / FAIL licenses

- **S2 PASS.** 625 and 634 sit between 605 (DK) and 641 (HOLST), so the bracket supports a DK/HOLST-topic referent
  for both. 625 [?_Ahlefeldt] stays M: the bracket corroborates the topic, not the name. 634 [Holstein] may move I -> M
  (margin-gloss alignment plus a topical bracket), but never above M. That change is made in key_gloss.tsv through
  merge_pages.py, and only if `merge_pages.py --check` and `tools/decode_key.py ciphers/hessen-daenemark-1672 --check`
  both exit 0.
- **S1 PASS.** An alphabetical window is given for 625 and 634 (the headwords between their neighbours), recorded as
  M-at-most candidates, with no key change unless the window contains the gloss value.
- **FAIL or non-test.** No key change. The unglossed groups stay as they are and are logged as open-codes by this
  method.

68 and 7480 are out of scope (see Units) whatever happens. Rule 10: nothing found here is called new.
