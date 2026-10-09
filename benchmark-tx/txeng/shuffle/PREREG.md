# PREREG TXE-L / idea M7: read the signs out of order (9 Oct 2026, 08:02 UTC by date -u; pushed BEFORE any read)

LANE TX-ENGINEER (account 4), worker TXE-L (Opus 5.5); brief `.claude/briefs/runs/2026-10-09-account4-txe-l.md`; binds
under `benchmark-tx/PREREG-txeng-2.md` (units, blindness, Amendment: single-instrument gate p < 0.01).

Question: does the line read's sequence prior cause errors (shuffled fixes more than it breaks against ordered on the same
tiles) or does context do work the floor needs (shuffled breaks more)?

## Subsample (fixed now)
The brief's cap rule (more than 4 sheets per arm -> the 4 dev lines with the most A/B disagreements) applies: 8 lines would
be about 230 tiles = 10 sheets per arm. Disagreements = rows whose `status` is not `agree` in
`harvest/f178v/passC_agreement.tsv` plus `harvest/f178v/passC_L11-23_agreement.tsv` (the same pair tx_compare uses for
merged confidence; L11 is in the second file): L08 6, L06 5, L11 5, then L01/L05/L09/L10 tied at 4; tie broken by the lowest
line number -> **f178v L08, L06, L11, L01**. Mapped positions (1:1 or 2:1 in `benchmark-tx/txeng/compare/box_pos.tsv`, the
label-blind map): **115 tiles**; 4 unmapped (L11 pos 9, 10, 17, 18; op 1:2), which take L's sign in both arms.
Deviation from the brief's 24 tiles a sheet: **29 tiles a sheet** (6 columns), so the 115 tiles fit the 4-sheet cap per arm
(24 a sheet would need 5). Both arms use the same 29.

## Tiles and sheets (built, commit before reads)
`python3 tools/tx_compare.py tiles --lines f178v_L08 f178v_L06 f178v_L11 f178v_L01 --order ordered|shuffled --per-sheet 29
--seed txe-l-m7`: each tile = the box plus its attached marks, grown 25% per side, every other sign/mark box blanked (no
neighbour ink), autocontrast, sign scaled to about 90 px tall (tile capped 150 px tall / 220 wide, shrunk not cropped).
(a) `ordered/sheet_01-04.png`: line order L08, L06, L11, L01, each tile labelled #n and "f178v Lxx pN" (key
`ordered_key.tsv`). (b) `shuffled/sheet_01-04.png`: one seeded shuffle across all 115, labelled #n only; key `key.tsv`
(md5 1109fc4f826bdab06ed96319f910a5ba), never given to a reader.

## Reader
One Opus 5.5 subagent call per sheet (8 calls), each a fresh agent given only the sheet image path, the reference sheet
`ciphers/nevers-birago-fr3251-1572/harvest/sign_sheet_blind_1572.png`, and the output path. Task: "for each numbered tile the
sheet cell T## that matches, or X_NEW / ?; tile, sign_id, conf". Raw reads `ordered/reads_NN.tsv`, `shuffled/reads_NN.tsv`,
committed and pushed per arm before any score. Order of reading: ordered sheets 1-4 then shuffled 1-4. If the cap/box stop
(80%) falls before all 8 calls, both arms are scored only on tiles read in BOTH arms, and that is stated.

## Resolve
`tools/tx_compare.py tiles-resolve` -> `benchmark-tx/outputs/birago1572-no87/passT_ordered_dev.tsv` and
`passT_shuffled_dev.tsv` (line, pos, sign; the 4 lines only). A T## read -> that sign; X_NEW, ?, missing and the 4 unmapped
positions -> L's sign (counted and listed per arm in `*/fallback.tsv`).

## Gate (fixed now)
Primary: `python3 tools/tx_bench.py passT_shuffled_dev.tsv --bench BENCHMARK-TX.tsv --item birago1572-no87 --paired
passT_ordered_dev.tsv`. fixed > broken with p < 0.01 -> the sequence prior hurts; broken > fixed with p < 0.01 -> context
helps; otherwise no detected effect at this N (115 tiles; reported as "untestable at this N" only if the discordant count
is too small for p < 0.01 to be reachable, i.e. fewer than 8 discordant positions).
Secondary (reported, not gating): each arm paired vs L (labels_dev_tune.tsv restricted to the 4 lines by tx_bench's common
positions) and vs passA_dev_tune.tsv.
Eval: no eval look unless the primary gate is met in the "shuffled fixes" direction AND shuffled beats L on these lines at
p < 0.01; then eval_heldout once, both arms (a new PREREG amendment first).
Agreed-wrong class: after both arms' reads are committed, open benchmark-tx/taxonomy/no87_positions.tsv and report, for the
positions among the 4 lines where A and B read the same wrong sign, how many each arm reads right.
Prediction (registered, not gating): no detected effect; the taxonomy says the errors sit in the glyph (class 1 look-alike
pairs), so removing order should change few positions, and the ordered arm should be slightly better on look-alike pairs.
