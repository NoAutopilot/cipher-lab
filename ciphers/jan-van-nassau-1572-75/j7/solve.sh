#!/bin/sh
# J7 (24 Sept 2026): identical solver settings for the 5549 body and its matched control.
# usage: j7/solve.sh CIPHER MODEL OUT [extra args]   (run from ciphers/jan-van-nassau-1572-75)
C=$1; M=$2; O=$3; shift 3
exec python3 ../../tools/nomenclator_anneal.py solve "$C" --lang de --model "$M" --context clear --syl none \
  --extra-syl "en er ch ge ei ie un in st an de te ben den sch uer ten ich ung gen el es et ar or ur ter ber ein au" \
  --words "und der die das zu uon nicht nit mit den dem in auch ist wir ich sich so es ein haben dasz" \
  --max-homo 12 --max-syl 30 --max-word 40 --max-null 3 --p-syl 0.15 --out "$O" "$@"
