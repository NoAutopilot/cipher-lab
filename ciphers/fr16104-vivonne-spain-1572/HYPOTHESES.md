# Hypotheses and control-backed tests (fr16104-vivonne-spain-1572)

| date | job | hypothesis / family | control (both numbers) | target | verdict |
|---|---|---|---|---|---|
| 8 Oct 2026 | VIV-ANCHOR (PREREG-VIVANCHOR, tx/vivanchor.py) | word-anchored known plaintext, ink 40 vs clerk ink 41: values for unkeyed labels and for f, m, p, u-after-q | known-answer hold-out of d t o r c n s: 5 of 7 recover (gate >= 5): d 3/3 1.00, t 11 1.00, o 8 1.00, r 9 0.78, c 4 0.75; n 28 0.54 (V carries 7 of the n slots), s 22 0.27 FAIL; shuffled-order null 3 anchoring windows median (max 7, 20 shuffles) vs 110 real | V -> n 7/8 (0.875) assigned, grade C; f cell: label p 4/6 (0.67) = CONFLICT (p is keyed n; "affaires" ff written p p twice), key unchanged; m 4 positions split 3:2 2:1 z:1, p 3 split o:2 c:1, qu 4 split z:2 2:2 -- none assigned; labels 2 (u 2, m 1), o (p 2), c (p 1), e (0) undecided | PASS control; 1 assignment |
