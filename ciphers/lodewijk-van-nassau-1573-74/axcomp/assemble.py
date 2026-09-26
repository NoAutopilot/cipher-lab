#!/usr/bin/env python3
"""AX-COMP: join reconciled page drafts (axcomp/recon_<prefix>_pN/ciphertext_draft.tsv or axcomp/recon_pN for 4614)
into ciphertext_<N>.tsv; clear words (w:word) become =word.   python3 axcomp/assemble.py N DIR [DIR ...]"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
n, dirs = sys.argv[1], sys.argv[2:]
rows = []
for d in dirs:
    with open(os.path.join(HERE, d, 'ciphertext_draft.tsv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            s = r['sign'].strip()
            if s.startswith('w:'):
                s = '=' + s[2:]
            rows.append([r['line'], r['position'], s, r['confidence'], r.get('alt', ''), r.get('why', '')])
with open(os.path.join(os.path.dirname(HERE), 'ciphertext_%s.tsv' % n), 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f, delimiter='\t', lineterminator='\n')
    w.writerow(['line', 'position', 'sign', 'confidence', 'alt', 'why'])
    w.writerows(rows)
print(n, len(rows), 'signs')
