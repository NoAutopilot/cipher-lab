# TXE2-PAIR (LANE TX-ENGINEER-2 experiment X2: pair classifiers from known-answer tiles; read-free; Opus 5.5; cap 5; box 60 min from claim, 80% at 48)

For LANE TX-ENGINEER-2 (account 4, session_01NmaB9fhuaMSMYexV4NaVsR). Written 9 Oct 2026 15:2x UTC by date -u. PREREG
`benchmark-tx/PREREG-txeng2-1.md` section X2 (binding) and `benchmark-tx/PREREG-txeng2-0.md` (gate, blindness). First: `git
fetch origin && git checkout -B main origin/main`; `export CIPHERLAB_ACCOUNT=account-4`; `python3 tools/room.py --start`; ROOM.md
last 30 lines; claim with `python3 tools/room.py "TXE2-PAIR worker (account 4, Opus)" "claim ..." --push`. Read TRANSCRIPTION.md,
`research/TX-TAXONOMY-2026-10-09.md` section 1 (the pairs), `tools/tx_pair_reread.py` (its `select` maps atlas boxes to line
positions label-blind: reuse that code path), `ciphers/nevers-birago-fr3251-1572/atlas/README.md`, `tools/glyph_atlas.py`'s tile
bitmap format (bitmaps.npz, signs.tsv), `tools/tests/test_tx_pair_reread.py` for the test shape. No vision call, no reader.

## Job
1. `tools/tx_pair_clf.py` with `--help`, subcommands `train` (pairs, training leaves = every atlas page except f178r/f178v/f179r;
   tiles = `atlas/secure_tokens.tsv` rows whose code is a pair member, bitmaps from `atlas/bitmaps.npz`; features: tile resized
   to 32x32 on its bounding box, 4x4 zoned ink density + the raw 32x32, HOG from scikit-image if importable (say which); model:
   logistic regression from scikit-learn if importable else a numpy nearest-centroid/kNN; threshold per pair = the margin that
   maximises leave-one-leaf-out accuracy on the training leaves, never touching no.87), `apply` (unit = dev_tune or
   eval_heldout: for every position of the unit whose L sign is a member of a pair, find its atlas box via the box<->position
   map reading ONLY columns sid, fol, line, pos, sign, op of `atlas/no87_box_token.tsv` -- never `truth`, enforce it in code --
   classify, output L's sign unless the margin exceeds the pair's threshold; write `benchmark-tx/outputs/birago1572-no87/
   passX2_pair_<unit>.tsv` (line pos sign) covering every unit position), `control` (the same with labels permuted within each
   pair's training set, seeds 1-5). Offline test `tools/tests/test_tx_pair_clf.py` (synthetic 2-class tiles: train, apply,
   threshold chosen leave-one-group-out; a permuted-label control near chance). SYSTEM.md row, tool_shelf.tsv row
   (system_map_check passes).
2. Run: train; report per pair the training tile counts, leave-one-leaf-out accuracy and the chance rate (majority share),
   the chosen threshold. Apply to dev_tune; commit the output; THEN score: `python3 tools/tx_bench.py benchmark-tx/outputs/
   birago1572-no87/passX2_pair_dev_tune.tsv --bench BENCHMARK-TX.tsv --item birago1572-no87 --paired benchmark-tx/txeng/units/
   labels_dev_tune.tsv --exclude-flagged`; the five permuted controls the same way. Report fixed/broken/p for the real and each
   control, the number of positions touched, and per pair fixed/broken.
3. If the dev gate (fixed > broken, p < 0.05) is met: apply to eval_heldout, commit `passX2_pair_eval_heldout.tsv`, DO NOT
   score it (the lane spends the look). If not met: say so; no eval file.
4. `benchmark-tx/txeng2/pair/RESULTS.md` with every number; register row for the lane (paste in the ROOM done line: dev
   fixed/broken/p, controls, positions touched); commit by path, push; ROOM done line "for LANE TX-ENGINEER-2", "cost: the
   orchestrator get_session reading".

Stop at 80% of cap or box with what exists committed. Never read the truth column or any *.truth.tsv before step 2's score;
never edit a truth file; never AskUserQuestion. + `.claude/briefs/README.md` common tail.
