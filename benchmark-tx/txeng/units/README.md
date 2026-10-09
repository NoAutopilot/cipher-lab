# TX-ENGINEER units (9 Oct 2026). Lines per unit; baselines are the committed passes restricted to the unit lines (tx_bench --paired compares on common positions).

- eval_heldout: f178v_L13 f178v_L14 f178v_L15 f178v_L16 f178v_L17 f178v_L18 f178v_L19 f178v_L20 f178v_L21 f178v_L22 f178v_L23 f179r_L01 f179r_L02 f179r_L03
- dev_tune: f178v_L01 f178v_L02 f178v_L03 f178v_L04 f178v_L05 f178v_L06 f178v_L07 f178v_L08 f178v_L09 f178v_L10 f178v_L11 f178v_L12
- geo: f178r_L01 f178r_L02 f178r_L03 f178v_L05 f178v_L10 f178v_L22
- f178r (added 9 Oct 2026 19:1x UTC, LANE TX-ENGINEER-2 incarnation 2, PREREG-txeng2-0 Amendment 4): f178r_L01 f178r_L02 f178r_L03 -- the geo unit's three new-ink lines as an EVAL unit of their own (labels_f178r.tsv = L restricted; passA_f178r.tsv); baseline L 7/84 as measured, 6/83 flagged-excluded (f178r_L03.23 flagged). Caveat declared: these lines tuned the follow-slope crop rule (TXE-D), which is now part of the baseline both arms share; reported as "tuned-letter lines" beside eval_heldout, never pooled with the held-out leaves in the split count. Never training ink (X2c on f178r cancelled for this reason).
