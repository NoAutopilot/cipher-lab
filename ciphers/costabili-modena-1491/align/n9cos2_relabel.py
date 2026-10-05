# N9-COS2, 5 Oct 2026: PREREG-N9-COS2 step 1 relabel of the committed N8-COS passes (no new read).
# W = the dash + open-loop shape (N9-COSV "Ω"): a token is W in BOTH passes wherever pass A reads z and pass B reads o at the same
# position of the difflib-aligned sign strings. p1_u03 / p1_u18 first token -> g (widened crops, n9cos2_boxes_fix.tsv, eye check).
# Usage: python3 ciphers/costabili-modena-1491/align/n9cos2_relabel.py  (run from the repo root; writes n9cos2_pass{A,B}_W.tsv, n9cos2_relabel_log.tsv)
import csv, difflib, os
D = os.path.dirname(os.path.abspath(__file__))
def load(p): return list(csv.DictReader(open(os.path.join(D, p)), delimiter='\t'))
A, B = load('n8cos_passA_norm.tsv'), load('n8cos_passB_norm.tsv')
bi = {r['crop']: r for r in B}
log = [('crop', 'posA', 'posB', 'A', 'B', 'new')]
for ra in A:
    rb = bi[ra['crop']]; a, b = ra['signs'].split(), rb['signs'].split()
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes():
        if tag == 'replace' and i2 - i1 == j2 - j1:
            for k in range(i2 - i1):
                if a[i1 + k] == 'z' and b[j1 + k] == 'o':
                    a[i1 + k] = b[j1 + k] = 'W'; log.append((ra['crop'], i1 + k, j1 + k, 'z', 'o', 'W'))
    if ra['crop'] in ('p1_u03', 'p1_u18'):
        for s, n in ((a, 'A'), (b, 'B')):
            if s[0] != 'g': log.append((ra['crop'], 0, 0, a[0] if n == 'A' else '', b[0] if n == 'B' else '', 'g')); s[0] = 'g'
    ra['signs'], rb['signs'] = ' '.join(a), ' '.join(b)
for rows, n in ((A, 'A'), (B, 'B')):
    w = csv.DictWriter(open(os.path.join(D, f'n9cos2_pass{n}_W.tsv'), 'w'), fieldnames=list(rows[0]), delimiter='\t', lineterminator='\n')
    w.writeheader(); [w.writerow(r) for r in rows]
csv.writer(open(os.path.join(D, 'n9cos2_relabel_log.tsv'), 'w'), delimiter='\t', lineterminator='\n').writerows(log)
print(len(log) - 1, 'edits')
