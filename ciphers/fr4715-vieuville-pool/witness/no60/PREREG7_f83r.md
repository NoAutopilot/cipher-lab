# PREREG7 -- no.60 f.83r: blind read of the top block vs Tomokiyo's no.60 DUMP (GAPS96, account-4)

Written 3 Oct 2026, about 11:55 UTC (clock read), BEFORE the native fetch and before the vision call; pushed first.

Question: the data conflict logged in NOTES.md (GAPS-12 called f.83r "a symbol alphabet" at 1000 px; Tomokiyo,
bnf4715.htm#no60, prints a digit-group DUMP and a clear reading for "no.60 (f.83)"). The 1000-px re-look this
session (canvas f181, label '83r') shows one pasted slip of about 17 lines in a cursive hand, the same family of
shapes as no.58 f.81r, whose digits earlier workers found hard (0/6, 1/7, 2/3, 3/5, 3/8, 9/g confusions).

Read: one blind Opus 5.5 subagent call over iiif_lines crops of the slip's top block only (the short first line and
the first three full lines). The prompt gives no key, no Tomokiyo text, no expected values; it says the hand may be
cursive Arabic numerals and asks for digit groups with any dot/bar mark, `?` for an unreadable group, or shape
labels if the signs are not numerals.

Statistic (scripts/f83r_compare.py, written before the call, unchanged after):
- B = the blind read's group sequence, bare digit strings (marks stripped; `?` groups kept as never-matching).
- T = Tomokiyo's no.60 DUMP, first 250 groups, bare codes (marks stripped; `▽` kept as its own symbol).
- LCS(B, T) = longest common subsequence length; R = LCS / len(B).
- Shuffle control: 1000 permutations of T (composition kept), LCS with B each; p99 and max.
- Cross-letter control (same key, same hand family, different text): LCS of B with the first 250 groups of
  Tomokiyo's no.27 DUMP and of no.58's DUMP (both in bnf4715.htm).

Gate, registered: PASS iff R >= 0.40 AND LCS > shuffle p99 AND LCS > both cross-letter LCS values.
NON-TEST iff len(B) < 30 or the reader gives shape labels / declines (a digit comparison cannot run).
Otherwise FAIL.

What PASS would mean: f.83r carries the digit cipher Tomokiyo dumped as no.60; GAPS-12's "symbol alphabet" was the
cursive digit hand at 1000 px; the conflict closes, and no.60 is covered by Tomokiyo's published partial reading
(a modern published key reading -- nothing of ours is graded, and no reading is claimed here).
What FAIL would mean: the conflict stands (either the read is too noisy at this hand or Tomokiyo's no.60 is a
different leaf); logged as a FAIL of this comparison, not as a negative on the leaf, with the next step named.
No grade change in this folder either way (no.60 has no reading of ours).
