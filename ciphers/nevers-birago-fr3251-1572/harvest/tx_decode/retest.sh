#!/bin/sh
# TX-DECODE re-tests (3 Oct 2026), run from ciphers/: sh nevers-birago-fr3251-1572/harvest/tx_decode/retest.sh
# lam 4 was chosen on no.87 f178v L01-L11 (tune) and checked on the rest of no.87 (held out) BEFORE these runs; lam 1 is the
# pre-registered setting that failed the no.87 known-answer gate. Printed 1572 key; f144r/f168 it16dip, f117 fr (as NEVBIR-3252-B).
set -e
O=nevers-birago-fr3251-1572/harvest/tx_decode; T=../tools/key_decode_lattice.py; K=nevers-birago-fr3251-1572/harvest/key_1572_sheet.tsv
C=nevers-birago-fr3251-1572/harvest/confusion_1572.tsv
for x in f144r:it16dip f168:it16dip f117:fr; do L=${x%%:*}; G=${x##*:}
  for lam in 1 4; do python3 $T decode $O/${L}_topk.tsv --key $K --lang $G --shuffles 200 --lam $lam --out-prefix $O/${L}_lam$lam > /dev/null; done
  for e in 0.08 0.25; do python3 $T decode $O/${L}_topk.tsv --key $K --lang $G --lam 4 --power-err $e --confusion $C --power-windows 20 --power-shuffles 50 --seed 2 > $O/${L}_power_lam4_err$e.json; done
done
