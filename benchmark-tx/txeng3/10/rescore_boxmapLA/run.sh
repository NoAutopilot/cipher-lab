#!/bin/bash
# BOXMAP-RESCORE (others), 11 Oct 2026, account 3: TXE3-10 PAIR re-run with only the box<->position map changed.
# usage (repo root): bash benchmark-tx/txeng3/10/rescore_boxmapLA/run.sh MAP OUTDIR
#   MAP    ciphers/nevers-birago-fr3251-1572/atlas/no87_box_token_labelaware.tsv (or the old no87_box_token.tsv: then every
#          output is byte-identical to the committed TXE3-10 files, checked 11 Oct 2026)
#   OUTDIR where the instrument files go (same names as benchmark-tx/txeng3/10/, eval/dev passes as pass*.tsv)
# The patch is applied to tools/glyph_atlas.py as of 1b50c66c (the commit it was made against) in a temp copy; the run arguments
# are the ones TXE3-10's VERIFY.md rebuilt (base + (a) eval + shuffle-lolo, (b) seeds 1-5 with/without --force-t 0, (c) dev
# --loo-lines, (d) T90/T53 for (a) and (c)). No truth file is read by the apply step; --truth feeds the dev pool only.
set -e
MAP=$(realpath "$1"); O=$(realpath -m "$2"); mkdir -p "$O"
R=$(git rev-parse --show-toplevel); cd "$R"
T=$(mktemp -d); mkdir -p $T/tools
git show 1b50c66c:tools/glyph_atlas.py > $T/tools/glyph_atlas.py
(cd $T && patch -s -p1 < "$R/benchmark-tx/txeng3/10/glyph_atlas_pair.patch")
C=ciphers/nevers-birago-fr3251-1572; U=benchmark-tx/txeng/units
base() { python3 $T/tools/glyph_atlas.py classify --pair $1 $2 --out $C/atlas --pool-dev $U/labels_dev_tune.tsv \
  --truth benchmark-tx/birago1572-no87.truth.tsv --pool-secure $C/atlas/secure_tokens.tsv \
  --pool-owner $C/sorter/owner-sort-2026-10-04/settled_labels.tsv --owner-map $C/sorter/no87/owner_map.tsv --map "$MAP" \
  --exclude-pool-page f178r --exclude-pool-page f178v --exclude-pool-page f179r "${@:3}"; }
E=$U/labels_eval_heldout.tsv; D=$U/labels_dev_tune.tsv
base T18 T98 --apply-unit $E --shuffle-lolo 20 --tsv $T/x.tsv --report $O/g1_T18_T98.tsv > /dev/null
base T18 T98 --apply-unit $E --tsv $O/passX30_topo_eval_heldout.tsv --report $O/apply_T18_T98_eval.tsv --touched $O/touched_T18_T98_eval_heldout.tsv
for s in 1 2 3 4 5; do
  base T18 T98 --apply-unit $E --seed $s --tsv $O/passX30_topo_ctrl${s}_eval_heldout.tsv --report $O/apply_T18_T98_ctrl${s}_eval.tsv --touched $O/touched_T18_T98_ctrl${s}_eval_heldout.tsv > /dev/null
  base T18 T98 --apply-unit $E --seed $s --force-t 0 --tsv $O/passX30_topo_ctrl${s}f_eval_heldout.tsv --report $O/apply_T18_T98_ctrl${s}f_eval.tsv --touched $O/touched_T18_T98_ctrl${s}f_eval_heldout.tsv > /dev/null
done
base T18 T98 --apply-unit $D --loo-lines --tsv $O/passX30_topo_dev_tune.tsv --report $O/g2_T18_T98_dev_tune.tsv --touched $O/touched_T18_T98_dev_tune.tsv
base T90 T53 --apply-unit $E --shuffle-lolo 20 --tsv $T/y.tsv --report $O/g1_T90_T53.tsv > /dev/null
base T90 T53 --apply-unit $D --loo-lines --tsv $O/passX30b_topo_T90T53_dev_tune.tsv --report $O/g2_T90_T53_dev_tune.tsv --touched $O/touched_T90_T53_dev_tune.tsv > /dev/null
# C2 on eval: PREREG-txeng3-10 C2 applies T90/T53 to eval only if it passes G1 and G2 on dev. With the old map it failed G2
# (0 fixed / 2 broken, both on the shifted line L11) and was never applied; with the label-aware map it passes both, so the
# registered C2 eval step runs here (an extra file; the old-map file set above is unchanged).
base T90 T53 --apply-unit $E --tsv $O/passX30b_topo_T90T53_eval_heldout.tsv --report $O/apply_T90_T53_eval.tsv --touched $O/touched_T90_T53_eval_heldout.tsv > /dev/null
rm -rf $T
