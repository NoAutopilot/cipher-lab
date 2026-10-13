# PREREG V-SUR2046 (verifier, account 2, LANE DEFAULT-A2-0710, 13 Oct 2026) -- pushed before the vision call

Question: do SUR-2046's 16 M relabels on 4.VEL 2046 (exceptions_nieuw_image.tsv rows "SUR-2046 blind sign call") reproduce in an
independent blind call with a fresh known-answer control?

Instrument (passes/signcmp_vsur2046/, build_call.py): the same 54 Nieuw-sheet tiles as SUR-2046, relabelled with a fresh seed
(20261013); the same GAPS18 half-line crops images/crops_2046_leg (no full image); query numbers reshuffled (seed 1013). Targets: the
16 relabelled tokens only. Controls: 20 H tokens NOT used as SUR-2046 controls, 2 each of o, 6, [delta], 5, 3, h, p, a, [hash], 7
(seed 20461013) -- weighted to the classes nearest the winning tiles (o vs B-row sigma = the #30 miss; 6 and [delta] vs E-row
flagged delta; 5 and 3 vs U-row 5; h vs N h; p = the A-row p tile [p-grave] went to; a = the E-row a tile). One blind Opus subagent
(brief.md), told to judge each instance separately. No values, no decode, no repository context.

Settle rule (SUR-2046 / GAPS25/29, unchanged): best_conf >= 0.6, located = sure, second a tile of a different value or NONE.
Gate (unchanged): >= 14/20 controls settled on the key value. Below gate: no relabel confirmed, none reverted; verdict for all 16
"unconfirmed, held at M pending a stronger instrument".

If the gate passes, per relabelled token (value v = SUR-2046's relabel):
- CONFIRMED (stands at M): settled on a tile of value v.
- CONTRADICTED (reverts to U, row removed from exceptions_nieuw_image.tsv): settled on a tile of another value, or best = NONE >= 0.6.
- NOT REPRODUCED, best value v but unsettled: held at M, unconfirmed.
- NOT REPRODUCED, best value not v and unsettled: reverts to U.
Look-alike withhold (the #30 rule applied evenly): if any fresh control whose key value differs from v settles on the same tile as a
target's settled answer, that target is "held at M, unconfirmed" instead of CONFIRMED (the call does not separate it from the
control's sign on this hand); a control MISSING its value onto the target's tile, unsettled, is logged but does not withhold.
No key_period_codes_nieuw.tsv change; no grade above M; no N-class change. decode_key.py --check exit 0 after any removal.
