# L74 box check, Vivonne f.102r (12 lines): the owner's answers

Read 11 Oct 2026 about 00:0x UTC by the account-3 parent from https://claude.ai/artifact/8AEJf4uQPX3ayZs1YteWN3 (account 3;
same 541 boxes as the account-4 page Aqq2jWzu9t2vF6GC7ZH1iR, plus 5 possible-shadow questions added 10 Oct; page v5).
All 104 step-2 questions answered: 92 kept (44 re-cut first), 11 bad cut, 1 set aside; no split, no added box, nothing
trashed. Save stamps 23:45:23 to 23:54:15 UTC 10 Oct (8.9 min, no pause over 2 min), so about 8.6 min per 100 flagged boxes
(sprint item, single-task; the owner gave no minutes of his own). The 437 unflagged boxes carry no answer of their own.

## The owner's two rules (10 Oct 2026, verbatim) -- conventions for this reference
1. "If a symbol was connected to other symbols with no lift off of the pen I marked it as a single symbol. Feel free to add a
   check on these to see if it makes sense or perhaps better if separate."
2. "I marked a bunch a bad cut if when I clicked into it I couldn't move the manuscript to properly see around it or it didn't
   really display the full symbol."
So BAD-CUT here means "could not be judged on this page", not "the box is wrong". 10 of the 11 touch the edge of their line
crop (7 the right edge, others top/bottom): the card shows only the crop, so nothing beyond it can be seen. They need a
second look with a whole-page view, not a re-cut by rule.

## Joined shapes kept as one box: duplicates to merge (merged 11 Oct, see below)
Under rule 1 the owner widened each machine piece (…a/…b/…c) of 11 joined shapes to the whole shape, which leaves 2-3
near-identical boxes per shape (IoU 0.53-0.99 after his re-cuts): f102r_L03_b031, L06_b028, L09_b042, L17_b033, L17_b041,
L21_b022, L21_b041, L22_b035, L23_b006, L23_b018, L27_b022. One box per shape is what his rule means; the merge waits on his
yes. 27 re-cut boxes are now 1.8x or more the hand's median sign width (51 px), up to 188 px: these are the boxes his rule 1
check is about.

## Files
db/ as read; settled.tsv, summary.json, recuts.tsv from tools/sign_sorter_apply.py (as for ../luzerne/, ../birago/).

## Joined-shape duplicates merged (owner's yes, 11 Oct 2026)
Asked whether to merge, the owner answered 11 Oct 2026 about 00:2x UTC, verbatim: "Ya, so let say there were two or three
symbols connected this way. I'd drag the first box over all of them. Then on the next symbol I'd drag its box over them too. So
some dupes." Recorded 11 Oct about 00:5x UTC by the account-3 parent in merges.tsv (blind: box geometry and pixels only; db/,
settled.tsv and recuts.tsv are not changed).

- 11 groups, one box each; 28 member boxes, 17 sids absorbed, so 541 boxes become 524.
- Box used: 3 on the union of the members (L06_b028, L17_b033, L22_b035); 4 on the member both checks named as the better fit
  (L09_b042 -> b042c, L17_b041 -> b041b, L21_b041 -> b041c, L23_b018 -> b018c); 4 on the largest member and marked
  second-look, for the owner on the whole-page view (L03_b031, L21_b022, L23_b006, L27_b022).
- How: the groups were rebuilt from geometry (same 11 as above, none added or dropped): tiles on one line strip join at IoU >= 0.5
  of their final boxes, or as a/b/c siblings both re-cut by the owner with the smaller box at least half inside the other. Two
  independent blind image checks then looked at each group's crops (ok, too-wide or unsure): both ok -> the union; both too-wide
  and naming the same member -> that member's box; anything else -> the largest member box, second-look. No group was put back to
  separate boxes: the yes covers all 11, only the box differs. Boxes are line-image (strip) pixels, as in recuts.tsv.
- Corrections to the list above: not every a/b/c piece is a duplicate. L06_b028c, L17_b041a and L21_b022c are other shapes and
  stay as they are; L22_b035c (bad cut) and L23_b018a (kept) lie inside a re-cut sibling but are left as the owner cut them. Pair
  IoUs are 0.53-0.99 except in L03_b031 and L23_b006, which join on containment (those pairs at IoU 0.21-0.39).
- This does not settle whether a joined shape is one sign or several. In the four second-look groups the checks found two shapes
  with no ink link (L23_b006: only a pale hairline), and one check would keep the left piece as its own box (L03_b031, L21_b022,
  L23_b006; possibly L27_b022). That question belongs to the separate blind "one sign or several?" pass (the account-3 parent's
  scratch sorters/second-look/joined/, flags.tsv when it lands) and the box-check team's sign-unit decision.
- Applying: tools/sorter_apply_recuts.py has no merge step yet, so the box-check lane applies merges.tsv: it drops each absorbed
  sid and sets keep's box to the row's x y w h.
