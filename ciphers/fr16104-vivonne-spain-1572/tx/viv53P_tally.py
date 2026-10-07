#!/usr/bin/env python3
"""D07-VIV53: tally of the two blind shape-judge passes under PREREG-D07VIV53P (iv) control gate and (v) target rule.

    python3 tx/viv53P_tally.py

Reads tx/lookalike53P/viv53P_judge_{A,B}.tsv (cid, ref, conf, second, note), viv53P_key.tsv (cid -> item) and viv53P_refkey.tsv
(ref letter -> key cell). Writes tx/lookalike53P/viv53P_tally.json and, only if the control gate passes in both passes and any target
meets rule (v), viv53P_overlay.tsv (page, line, pos, label, cell, meaning). Exit 3 if the control gate fails (NON-TEST).
"""
import csv, json, os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); LA = os.path.join(HERE, 'lookalike53P')
CTRL = {'d': 'o1', 'm': 'e1', 'p': 'n1', 'g': 'r1'}
MEANING = {'f1': 'f', 'm1': 'm', 'm2': 'm', 'm5': 'm', 'p1': 'p', 'o1': 'o', 'e1': 'e', 'n1': 'n', 'r1': 'r'}   # g1: foil, no meaning


def rd(n):
    return list(csv.DictReader(open(os.path.join(LA, n)), delimiter='\t'))


def main():
    key = {r['cid']: r for r in rd('viv53P_key.tsv')}; ref = {r['ref']: r['cell'] for r in rd('viv53P_refkey.tsv')}
    ans = {}
    for p in 'AB':
        a = {}
        for r in rd(f'viv53P_judge_{p}.tsv'):
            c = (r.get('ref') or '').strip().upper()
            a[r['cid'].strip()] = (ref.get(c, 'NONE'), (r.get('conf') or 'L').strip().upper())
        ans[p] = a
    out = {'gate': {}, 'targets': {}, 'cells_by_label': {}}
    ok = True
    for p in 'AB':
        ctl = [c for c in key if key[c]['kind'] == 'control']
        right = sum(1 for c in ctl if ans[p].get(c, ('NONE', 'L')) == (CTRL[key[c]['label']], 'H') or
                    ans[p].get(c, ('NONE', 'L')) == (CTRL[key[c]['label']], 'M'))
        firm_wrong = sum(1 for c in ctl if ans[p].get(c, ('NONE', 'L'))[1] in 'HM' and ans[p][c][0] != CTRL[key[c]['label']])
        missing = sum(1 for c in key if c not in ans[p])
        g = right >= 8 and firm_wrong <= 2
        out['gate'][p] = {'controls': len(ctl), 'correct_HM': right, 'firm_wrong': firm_wrong, 'missing_rows': missing, 'pass': g}
        ok &= g
    out['gate']['pass'] = ok
    ov = []
    for c in sorted(key):
        k = key[c]
        if k['kind'] != 'target':
            continue
        A, B = ans['A'].get(c, ('NONE', 'L')), ans['B'].get(c, ('NONE', 'L'))
        agree = A[0] == B[0] and A[1] in 'HM' and B[1] in 'HM' and A[0] != 'NONE'
        applied = ok and agree and A[0] in MEANING
        out['targets'][c] = {'item': int(k['item']), 'pos': f"{k['page']}.{k['line']}.{k['pos']}", 'label': k['label'],
                             'A': '/'.join(A), 'B': '/'.join(B), 'agree_HM': agree, 'applied': applied}
        out['cells_by_label'].setdefault(k['label'], Counter())[A[0] + '|' + B[0]] += 1
        if applied:
            ov.append({'page': k['page'], 'line': k['line'], 'pos': k['pos'], 'label': k['label'], 'cell': A[0], 'meaning': MEANING[A[0]]})
    out['cells_by_label'] = {k: dict(v.most_common()) for k, v in out['cells_by_label'].items()}
    out['applied'] = len(ov)
    json.dump(out, open(os.path.join(LA, 'viv53P_tally.json'), 'w'), indent=1)
    if ov:
        with open(os.path.join(LA, 'viv53P_overlay.tsv'), 'w') as o:
            w = csv.DictWriter(o, fieldnames=list(ov[0]), delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(ov)
    print(json.dumps(out['gate']), 'applied', len(ov))
    sys.exit(0 if ok else 3)


if __name__ == '__main__':
    main()
