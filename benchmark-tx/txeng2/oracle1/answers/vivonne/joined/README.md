# Vivonne f.102r joined shapes: one sign or several? (blind check of the owner's rule 1)

Recorded 11 Oct 2026 about 01:05 UTC by the account-3 parent. A machine reading of shapes, not a decision.

## What was asked

The owner's rule 1 for the L74 box check on Vivonne f.102r (10 Oct 2026, verbatim): "If a symbol was connected to other
symbols with no lift off of the pen I marked it as a single symbol. Feel free to add a check on these to see if it makes
sense or perhaps better if separate."

## Method

- 16 shapes (`shapes.tsv`): the 11 joined groups the owner kept as one shape (now one box each, `../merges.tsv`) and 5 more
  single boxes that are 1.8x or more the hand's median sign width (`kind` = group / wide).
- Two independent blind image passes (`pass1.tsv`, `pass2.tsv`), written 11 Oct 2026 00:51 and 00:59 UTC. Each pass saw
  only a crop of the shape and a crop of its line, and answered: how many signs this hand also writes on its own are inside
  the box, with a confidence (high / medium / low) and a shape description as evidence. No sign values, labels, readings or
  keys were shown or used; the evidence column describes strokes only. Ink belonging to a neighbouring box, or to the line
  above or below, is not counted.
- `flags.tsv` is mechanical from the two passes' counts and confidences (no third judgement): both 1 = one sign; both >= 2
  and both at least medium = likely several signs; a low-confidence pass, or one pass 1 and the other >= 2 = unclear.
  `flags_summary.txt` is the workflow's own summary.
- The crop images are not committed; the `crop` and `crop_ctx` columns in `shapes.tsv` point at the session scratchpad
  where the passes read them and are kept only as a record; the crops can be cut again from the line strip named in `page`
  with the box `x y w h` in the same row.

## Results

| | one sign | likely several | unclear |
|---|---|---|---|
| flags (16 shapes) | 1 | 9 | 6 |

- One sign: f102r_L17_b041 (both passes 1, high).
- Likely several: L03_b031, L06_b028, L17_b033, L21_b022, L21_b041, L22_b035, L23_b018, L06_b010, L11_b014.
- Unclear: L09_b042, L23_b006, L27_b022, L17_b004, L17_b011, L26_b035. Five of the six are unclear only because one or
  both passes gave low confidence while both still counted 2 or more; only L17_b004 is a one-against-several split.
- If "disagree" is read strictly (any different count), three of the nine move to unclear: several 6, unclear 9, one 1.

Per-pass count distributions (signs per shape):

| | 1 | 2 | 3 | 4 | total signs in 16 boxes | confidence high / medium / low |
|---|---|---|---|---|---|---|
| pass 1 | 1 | 5 | 6 | 4 | 45 | 3 / 9 / 4 |
| pass 2 | 2 | 6 | 6 | 2 | 40 | 4 / 8 / 4 |

The two passes give the same count on 11 of 16 shapes and differ by one on 5 (L06_b028 4 v 3, L22_b035 4 v 3,
L11_b014 3 v 2, L17_b011 3 v 2, L17_b004 2 v 1).

## The joins the passes split on

1. **A crossed upright run into a zigzag without a pen lift.** Pass 1 counts it as 2 signs, pass 2 as 1. This is the
   whole difference in L06_b028, L22_b035 and L11_b014, and pass 1's own stated alternative count equals pass 2's count
   each time. The same join is in L09_b042 and L17_b033 too, read the same way by each pass (pass 1 two, pass 2 one); the
   totals agree there only because the passes differ elsewhere in the box (L09_b042: pass 2 separates a small bowl from the
   large arching stroke; L17_b033: pass 2 counts the half-cut double-barred shape at the right edge that pass 1 leaves to
   the next box). Pass 1 also notes that in L06_b010 the zigzag stands in the box while its crossed upright lies in the box
   to the left.
2. **A small slanted eyelet with a descender sweeping back left, joined to a heavy diagonal or zigzag.** L17_b011: pass 1
   counts the unit as 2 (low), pass 2 as 1 (medium). L23_b006 and L27_b022: both passes count it as 2, both at low
   confidence, and both give one fewer as their alternative.

Not a join question: L17_b004 (pass 1 counts a pale upright smear fused to the sign as a second sign, low, "1 if it is a
blot"; pass 2 counts 1) and L26_b035 (both 2; both say the pointed third stroke could be its own sign, 3).

## What this does and does not settle

This is a machine reading of shapes. It does not decide the sign unit for the box reference. Under the owner's
convention (one box per pen-joined shape) these are 16 boxes; counted in signs this hand also writes alone they are about
40 to 45, so a sign-unit reference would add about 24 to 29 boxes to the 524 after the merge (about 5%). Whether the
Vivonne box reference is kept in pen units (the owner's convention) or in sign units is the box-check team's call
(TX-ENGINEER-2, account 4) with the owner. `../merges.tsv` (one box per joined shape, 11 Oct 2026) records the owner's
convention and the duplicate clean-up; it does not settle this question either way.
