# PREREG R8-UNTB (6 Oct 2026, ~03:55 UTC, written and pushed before any concordance crop is viewed)

Question (F4 of PREREG-A2P4-UNT): does symA's descender carry a crossbar (a crossing stroke, as on the
per/par/pro p "ꝑ") or only a curl continuous with the descender?

Units: leaves of BIB HS 2398 (Salzburg Museum IIIF). Leaf 1 = opening 11 (on disk, inscription + facing prose);
further prose openings fetched at most 5 (one IIIF request each, >=2 s apart), at most 6 leaves in all.

Reference class R ("crossed-descender p in this hand"): every p-shaped sign on the viewed leaves whose descender
is cut by a stroke that visibly extends on BOTH sides of the descender (left and right of the stem).
Test class S: the 5 symA instances (L2 tok1 final, L4 tok5, L4 tok7, L6 tok2 first glyph, L6 tok3) + symA-rev.

Per instance, at native resolution (crop only, 2x upscale allowed), record one of:
  X = crossing stroke: a stroke that extends on both sides of the descender below the bowl/loop;
  C = curl: any leftward mark is continuous with the descender (no part to the right of the stem);
  U = cannot tell at this resolution.

Decision rule:
  - Resolution control first: if fewer than 3 R instances are found, OR fewer than 3 of the R instances found
    read X at the same zoom and crop procedure, the crops cannot show a crossbar reliably -> F4 UNSETTLED
    (non-test), whatever symA shows.
  - Control passes: F4 = "crossbar" if >=3 of the 5 symA instances read X; F4 = "no crossbar (curl)" if >=3 of 5
    read C; otherwise UNSETTLED. symA-rev is reported but not counted.
  - Same-scribe caveat: R instances from the cursive prose and S from the painted inscription may differ in
    ductus; the tally is reported per leaf and per script (prose vs inscription).
No token is graded from this (rule 4: shape evidence only, H 0 C 0 S 0). The outcome changes only F4 in the
PREREG-A2P4-UNT feature list for future reference-dictionary comparisons.
