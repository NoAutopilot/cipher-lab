# PREREG VILL-NOMEN (3 Oct 2026, committed before any f159 nomenclator/Nulles crop is viewed)

Reads: native crops of canvas f159 (btv1b525085665) outside the alphabet strip -- the Nulles box and the nomenclator
(codes about 20-80) -- via tools/iiif_lines.py; one blind read (worker) + one check read (subagent, blind to the first).
Output keys/key_f159_nomen.tsv (code or sign -> meaning, grade: M where both reads agree, I where they differ or one
read is illegible). Nothing in the target is graded from this table unless a gate below passes.

Nomenclator match (disk only, report counts): (i) the number of nomenclator codes read and agreed; (ii) of the target's
adjacent figure pairs (bourdeau/ct_f148r.txt + ct_f148v_149r.txt, 'o' = 0), how many form a value in the agreed code
set, against the same count for the code set shifted to random disjoint two-figure values (200 draws, mean and p95).
Reported as an observation; no reading is committed from it.

Nulles decision: the target's frequent symbols are P (pi), V (varpi), Q (theta), W (infinity), T (tau), R (reversed c).
A target sign is a "certified null" only if BOTH readers, comparing the Nulles box crop with the committed target stack
images/f148r_ct_stack.jpg, call it SAME (as VILL-SIGNS certified L/w/+).
- If at least one of P V Q W T R is a certified null: re-run VILL-SIGNS's power control (signs_score.py method, key
  keys/key_f159_full.tsv unchanged) with every certified-null token deleted from the target stream before coverage and
  length are computed (script nulls_score.py -> nulls_score.tsv). Power gate first: < 16/20 at rank 1 of 201 =>
  non-test, no target score, no judge. Only if >= 16/20: target rank 1/201 and z >= 3 => PASS (judge fr16 pasted), else
  FAIL, control-backed negative for the f159 figure values with those nulls.
- If none is certified: log "f159 nomenclator/nulles do not explain the target's symbols" and stop.
