# RUN6-NOXALIGN pre-registration (LANE-RUN6 worker, account 1, 5 Oct 2026, committed before any statistic)

Brief: `.claude/briefs/runs/2026-10-05-acct1-run6-wave3.md`, job RUN6-NOXALIGN. Script: `aln/noxalign.py`. Disk only, 0 requests.
Inputs unchanged from RUN6-NOXREAD (PREREG-NOXREAD.md): stream `witness/c262rc_recon.tsv` (384 signs), label -> pile map
(noxread.label_pile), basin consensus key cL (six L runs), gloss = decode262.gold() (normalized, 315 letters).
interlinear_align.py is not used: its hard-EM learns values from the pairs, i.e. would re-key the stream; the question here is
what the gloss says at each label's positions when that label's own value cannot steer the alignment.

## Per-label masked alignment (leave-one-label-out)
For each label X of the 41: build the basin decode sign by sign (one letter per mapped sign; unmapped/'?' signs dropped), with
every sign of X written '*' (never in the gloss). difflib.SequenceMatcher(None, masked, gloss, autojunk=False).get_opcodes().
A '*' at position i is *recovered* iff it falls in a 'replace' opcode with i2-i1 == j2-j1 <= 3 (a short equal-length gap between
two 'equal' anchors, or at an end); its gloss letter is gloss[j1 + i - i1]. Otherwise unrecovered.
Label X is **settled to letter L** iff recovered >= 3 AND L is the strict majority-or-plurality (no tie) AND count(L) >= 2 AND
count(L)/recovered >= 0.5.

## Statistic
S = number of labels settled to their own basin letter (noxread label_letter).

## Nulls (both can move S: each changes which '*' positions are recovered and what letter lands there)
(g) gloss letter order shuffled, 200 draws, rng random.Random(20261005), same procedure on all 41 labels, gate p99 of S;
(k) basin key values permuted across piles, 200 draws, same rng continuing, same procedure, gate p99 of S.
**PASS iff S > (g) p99 AND S > (k) p99.** Otherwise FAIL, all numbers reported.

## Reported, not gated
- Tomokiyo-letter count: labels settled to their Tomokiyo letter (letter part of a lowercase id; o1/e2 -> e; D1, N5, W: none).
- For every label whose basin letter differs from its Tomokiyo letter: recovered n, settled letter (or none), and whether it
  matches basin, Tomokiyo or neither. "The gloss settles it" means settled to one of the two.
- Reference with Tomokiyo anchors: same masked procedure on the Tomokiyo decode (test0 rules; W: signs give their word, so only
  letter labels are masked), count of letter labels settled to their Tomokiyo letter.

## Grades
FAIL: all tokens stay M. PASS: a sign may move to C only if its label is settled to its basin letter AND that sign's own
recovered gloss letter equals it; every other sign stays M. Conditional on one reconciler's labels, RUN2-NXATL's unchecked
alignment and the owner's merges, as in RUN6-NOXREAD.
