#!/bin/sh
# RUN2-NXTA: rebuild passA.tsv, passB.tsv, disagreements.tsv, agreement.tsv and reconciled.tsv from the raw blind passes.
# Run from the repository root.  --check: rebuild into a temp dir and exit 1 if any committed file differs.
set -e
D=ciphers/fr16142-noailles-constantinople-1571/run2/nxta
T=$(mktemp -d)
python3 $D/to_long_map.py $D/descmap.tsv $D/passA_raw.tsv > $T/passA.tsv
python3 $D/to_long_map.py $D/descmap.tsv $D/passB_raw.tsv > $T/passB.tsv
python3 tools/reconcile_passes.py $T/passA.tsv $T/passB.tsv --out-dir $T/rec > $T/rec.log; head -1 $T/rec.log
python3 $D/reconcile_rules.py $T/rec/ciphertext_draft.tsv $D/family_rules.tsv $T/reconciled.tsv
cp $T/rec/disagreements.tsv $T/rec/agreement.tsv $T/
if [ "$1" = "--check" ]; then
  rc=0; for f in passA.tsv passB.tsv disagreements.tsv agreement.tsv reconciled.tsv; do
    cmp -s $T/$f $D/$f || { echo "STALE: $D/$f"; rc=1; }; done
  [ $rc = 0 ] && echo "check OK: committed files match a rebuild"; rm -rf $T; exit $rc
fi
cp $T/passA.tsv $T/passB.tsv $T/disagreements.tsv $T/agreement.tsv $T/reconciled.tsv $D/; rm -rf $T
