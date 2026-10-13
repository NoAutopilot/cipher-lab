#!/bin/bash
# DEC4450-INIT (13 Oct 2026): re-derive every image and crop used (none is committed). Run from the repository root.
# openapi.bnf.fr: one request at a time, >= 3 s apart; take/release ROOM lines around the batch.
set -e
D=ciphers/decode-4450-bnf-fr20506-1525/images/f4scratch; mkdir -p $D
UA="cipher-lab research script (contact via repository)"
B=https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9059908w
for v in 9 10 11 12 13; do curl -sS -A "$UA" -o $D/fr2988_v${v}_600.jpg "$B/f$v/full/600,/0/default.jpg"; sleep 3.2; done
curl -sS -A "$UA" -o $D/f9_open.jpg "$B/f9/700,70,3500,860/2400,/0/default.jpg"; sleep 3.2
curl -sS -A "$UA" -o $D/f13_close.jpg "$B/f13/850,1524,3330,1260/2400,/0/default.jpg"
for v in 9 10 11 12 13; do python3 tools/iiif_lines.py --image $D/fr2988_v${v}_600.jpg --out $D/lines_v$v --debug; done
for f in f9_open f13_close; do python3 tools/iiif_lines.py --image $D/$f.jpg --out $D/crops_$f --debug; done
# sha1 check against images/manifest.json (entries dated 13 October 2026)
python3 - <<'PY'
import json,hashlib
m=json.load(open('ciphers/decode-4450-bnf-fr20506-1525/images/manifest.json'))
for e in m['images']:
    if e.get('file','').startswith('f4scratch/'):
        p='ciphers/decode-4450-bnf-fr20506-1525/images/'+e['file']
        print(e['file'], 'ok' if hashlib.sha1(open(p,'rb').read()).hexdigest()==e['sha1'] else 'DIFFERS (server re-encode?)')
PY
