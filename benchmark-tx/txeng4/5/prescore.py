#!/usr/bin/env python3
"""R3/R6 helper (TXE4-5): append sha256 of OUTPUT files to benchmark-tx/txeng4/5/SHA256SUMS.prescore before any score, and for an
eval unit append one row per output to benchmark-tx/txeng4/LOOKS.tsv (job, item, unit, sha256, utc; created with that header if
absent; only ever appended). Usage: prescore.py [--look ITEM UNIT] FILE...  (run after git fetch/rebase; commit before scoring)."""
import hashlib, sys, os, time
a = sys.argv[1:]; look = None
if a and a[0] == '--look':
    look = (a[1], a[2]); a = a[3:]
O = 'benchmark-tx/txeng4/5'
utc = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
with open(f'{O}/SHA256SUMS.prescore', 'a') as f:
    for p in a:
        h = hashlib.sha256(open(p, 'rb').read()).hexdigest()
        f.write(f'{h}  {p}  {utc}\n')
        if look:
            L = 'benchmark-tx/txeng4/LOOKS.tsv'
            new = not os.path.exists(L)
            with open(L, 'a') as g:
                if new:
                    g.write('job\titem\tunit\toutput_sha256\tutc\n')
                g.write(f'TXE4-5\t{look[0]}\t{look[1]}\t{h}\t{utc}\n')
print(f'prescore: {len(a)} files hashed at {utc}' + (f'; LOOKS rows for {look}' if look else ''))
