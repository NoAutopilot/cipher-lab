# PREREG WVH-CROP (account 2, LANE DEFAULT-A2-1410-15), 15 Oct 2026, written before either crop is viewed

Job: `.claude/briefs/runs/2026-10-15-ytbiz-default-1410-jobs.md` "WVH-CROP". Two taller crops of WVO 1068 p.2 (600 dpi render of
`01068.pdf` p.2, scratchpad only) to settle the two unkeyed classes of `key_1068.tsv`: `nine` (H tokens l 6, a 1, i 1) and
`compact-8` (H tokens e 2, o 1). One low-resolution overview of lines 2-4 (half scale) was viewed only to place the crops.
Not blind: this worker knows the gloss values already on file. No reading of 1127.

Crops (one look each; full sign height plus the gloss row above):
- C1: cipher row L2 through cipher row L3, x covering L2 p12-18 and L3 p6-18. In-crop tokens: nine 2.12, 2.15, 3.7 (all l);
  compact-8 2.18 (o), 3.11 (e); the L3 p12-17 gloss ("gesch?dd", under L2's descenders).
- C2: gloss + cipher row L4, x covering p6-26. In-crop tokens: nine 4.8 (a), 4.21 (i), 4.24 (i).
  (Not in either crop: compact-8 1.21 and 9.11; nine 5.x-8.x, all l.)

Decision rules (fixed now):
1. `nine`. Record per token: foot (hook curving left / straight / descending loop or tail), head (closed loop / open), size relative
   to the line. If the three L4 tokens (4.8, 4.21, 4.24) share a feature visibly absent from all three in-crop l tokens (2.12, 2.15,
   3.7), they leave `nine` for a separate class `nine-g`; `nine` is then keyed l (H, its H tokens agree); `nine-g` takes the value
   its own H tokens give, and stays '?' if they still conflict (a vs i). If no feature separates them, `nine` stays '?' and the
   conflict is logged as a same-shape homophone conflict. A gloss re-read that differs from both passes changes the token's
   value only with grade M.
2. `compact-8`. Compare 2.18 (o) with 3.11 (e) on shape and on the gloss letter above. If 2.18 is visibly another shape (tall-8,
   open-8, loop-splayed-legs or a shape of its own), it is reclassified and `compact-8` is keyed e (H 3.11, 9.11). If 2.18 is the
   same shape and its gloss is o, `compact-8` stays '?'. If the gloss over 2.18 reads e at this height, the token goes to e at M
   (both passes read o) and `compact-8` is keyed e from its remaining H tokens.
3. L3 p12-17: record the gloss letters legible over each sign. Any change from this single own read is grade M; the hash class
   (no gloss so far) is keyed only if a letter stands legibly over it, at M.
4. Every change goes through `w1068/reconcile_1068.py` (TOKCLASS / VALUES / a grade override) and `check_1068.py --check`;
   the shuffle control `w1068/control_shuffle_1068.py` is re-run and its output pasted. If it no longer PASSes, the change is
   reverted and logged.
5. Stop after C2 whatever it shows; no third look. Unsettled stays unsettled.
