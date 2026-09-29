#!/bin/sh
# usage: heldout_ctl.sh TAG  -> fit on hA (c2-shape), score on hB (c1-shape); then fit on hB, score on hA
T=$1; W=work; S="$W/hsolve $W/train.txt"
FLOOR=-4 $S $W/hA_$T.cip 8 5000000 7 0.3 5 > $W/fitA_$T.txt 2>/dev/null
FLOOR=-4 $S $W/hB_$T.cip 8 2000000 7 0.3 5 > $W/fitB_$T.txt 2>/dev/null
grep -E '^[0-9]+ [a-z]$' $W/fitA_$T.txt > $W/keyA_$T.txt; grep -E '^[0-9]+ [a-z]$' $W/fitB_$T.txt > $W/keyB_$T.txt
# unseen signs stay unread: keep only signs that occur in the fit text
python3 - $T <<'PY'
import sys; T=sys.argv[1]
for fit in 'AB':
    seen=set(open(f'work/h{fit}_{T}.cip').read().split())
    ks=[l for l in open(f'work/key{fit}_{T}.txt') if l.split()[0] in seen]
    open(f'work/key{fit}_{T}.txt','w').writelines(ks)
PY
echo "$T fitA recov $(python3 evalk.py $W/fitA_$T.txt $W/hA_$T.ans | cut -d' ' -f1) -> B: $(FLOOR=-4 HELDOUT=$W/keyA_$T.txt $S $W/hB_$T.cip 1 1 1 0.3 5)"
echo "$T fitB recov $(python3 evalk.py $W/fitB_$T.txt $W/hB_$T.ans | cut -d' ' -f1) -> A: $(FLOOR=-4 HELDOUT=$W/keyB_$T.txt $S $W/hA_$T.cip 1 1 1 0.3 5)"
