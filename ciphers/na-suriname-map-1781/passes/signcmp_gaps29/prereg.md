# GAPS29-na-suriname-map-1781 (account-4), 3 Oct 2026 -- pre-registration (pushed before the vision call)

Why: readers' code g (46 tokens on 2077) is keyed g|l (key_period_codes_nieuw.tsv: the Nieuw sheet's G row is a 9, its L
row a g with a tail; readers' g may cover both). GAPS21's line-level call could not separate them (every instance 0.55 on
one tile). GAPS25's masked-instance method worked for d/n/q, so the same method is used here, one blind Opus call.

Instances (queries_key.tsv, 68): targets = every 2077 token of reader code g (46). Partners (calibration) = every 2077
token of reader code c (5; key l H, the L-row c) and [u-dots] (17; key n H, settled 17/17 on the N-row ij by GAPS25). The
[u-dots] partners include the three tokens GAPS23/25 align to 2078 m (2077_L11:10, L11:23, L12:37; "nonteerings" ~
"monteerings"); they are asked again here at no extra call cost.

Crops: the GAPS19 tools/iiif_lines.py half-line crops (images/crops_2077_leg), targets masked as #k in the line's reader-code
sequence (query_sequences.txt); no sign-level boxes (GAPS25: the ruled diagonals defeat registration).
References: blind_refs.jpg = GAPS25's 26 Nieuw-sheet tiles relabelled (seed 20261004, blind_key.json): includes G-row 9 (g),
L-row g and L-row c (l), M-row y (m), N-row ij/l/h (n), I-row 8 (i), P-row q (p) and the rest as distractors.

Rule (per instance, as GAPS25): settled = best_conf >= 0.6, located = sure, second choice a tile of a different value (or NONE).
Calibration gate (run first): of the 22 partners, at least 2/3 settled on their key value (c -> l, [u-dots] -> n); otherwise
no g result is applied and the step is logged "non-test (partners below gate)".
Targets (g, two candidate values g and l):
- If >= 3 settled and >= 2/3 of them on one value v in {g, l}: class moves to v; settled-on-v -> v at H ("sheet's own sign
  identified by image"), unsettled -> v at M, settled on the other value w -> w at M.
- Otherwise (a genuine mix: both g and l settled, neither >= 2/3) every settled instance takes its settled value at H, per
  instance (the key note expects two sheet signs under one reader code); unsettled stay g|l at M.
- A settled target on a value outside {g, l} -> no change (logged).
Partners: a [u-dots] or c settled on a different value -> that value at M (GAPS25 rule); the three n->m tokens move to m only
this way. Existing C exceptions (GAPS23/24) are not overwritten. Codes in key_period_codes_nieuw.tsv are not changed (2077 only).
Then: tools/decode_key.py --check exit 0; GAPS23's registered gate re-run unchanged (passes/nota2078_gaps25/score.py and
nota2078.tsv byte-identical copies in passes/nota2078_gaps29/, same pairs, seed, draws), old vs new pooled A per pair, beside H/C/M/U.
