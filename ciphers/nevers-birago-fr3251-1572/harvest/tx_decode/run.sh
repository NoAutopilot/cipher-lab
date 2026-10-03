#!/bin/sh
# TX-DECODE (3 Oct 2026): Birago no.87 known-answer run of tools/key_decode_lattice.py. Run from harvest/: sh tx_decode/run.sh
# Inputs: blind passes A/B of f178r, f178v (L01-10 + L11-23 files), f179r; committed ciphertext as position skeleton only
# (its signs are not candidates); confusion_1572.tsv; printed key key_1572_sheet.tsv; truth87.tsv = align87/align_real.tsv
# plain_chunk per committed (line, pos) (the clerk sheet). Outputs in tx_decode/: *_topk.tsv, no87_lam{1,4}.{json,decode.tsv,plain.txt}.
set -e
T=../../../tools/key_decode_lattice.py; O=tx_decode
cat f178v/passA.tsv > $O/f178v_A.tsv; tail -n +2 f178v/passA_L11-23.tsv >> $O/f178v_A.tsv
cat f178v/passB.tsv > $O/f178v_B.tsv; tail -n +2 f178v/passB_L11-23.tsv >> $O/f178v_B.tsv
python3 $T from-passes f178r/passA.tsv f178r/passB.tsv --ref ciphertext_f178r.tsv --confusion confusion_1572.tsv --out $O/f178r_topk.tsv
python3 $T from-passes $O/f178v_A.tsv $O/f178v_B.tsv --ref ciphertext_f178v.tsv --confusion confusion_1572.tsv --out $O/f178v_topk.tsv
python3 $T from-passes f179r/passA.tsv f179r/passB.tsv --ref ciphertext_f179r.tsv --confusion confusion_1572.tsv --out $O/f179r_topk.tsv
rm $O/f178v_A.tsv $O/f178v_B.tsv
{ cat $O/f178r_topk.tsv; tail -n +2 $O/f178v_topk.tsv; tail -n +2 $O/f179r_topk.tsv; } > $O/no87_topk.tsv
for lam in 1 4; do
  python3 $T decode $O/no87_topk.tsv --key key_1572_sheet.tsv --lang it16dip --truth $O/truth87.tsv --shuffles 200 --lam $lam --out-prefix $O/no87_lam$lam > /dev/null
done
