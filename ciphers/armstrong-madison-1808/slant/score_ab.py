#!/usr/bin/env python3
"""SLANT-CROP A/B score (pre-registered in NOTES.md, 5 Oct 2026 04:53 UTC). Reads slant/reads/read_{X,Y}_{1,2}.tsv and
slant/reads/key.json (which set is old/new), writes slant/ab_results.tsv and prints the gate verdict.
Per unit agreement = 1 - |c1 - c2| / max(c1, c2) (1 when both 0); score = mean x 100. PASS iff new >= old + 5 and no
consensus unit loses a mark (max(new passes) < consensus <= max(old passes)).
Run: python3 ciphers/armstrong-madison-1808/slant/score_ab.py"""
import csv, json, os, sys
D = os.path.dirname(os.path.abspath(__file__))
units = list(csv.DictReader(open(os.path.join(D, 'units.tsv')), delimiter='\t'))
key = json.load(open(os.path.join(D, 'reads', 'key.json')))


def load(s, p):
    rows = csv.DictReader(open(os.path.join(D, 'reads', f'read_{s}_{p}.tsv')), delimiter='\t')
    return {r['unit'].strip(): int(r['count']) for r in rows}


def agree(a, b):
    return 1.0 if max(a, b) == 0 else 1 - abs(a - b) / max(a, b)


R = {c: (load(key[c], 1), load(key[c], 2)) for c in ('old', 'new')}
out, score, exact, cdev, lost = [], {}, {}, {}, []
for c in ('old', 'new'):
    p1, p2 = R[c]
    ag = [agree(p1[f'u{i:02d}'], p2[f'u{i:02d}']) for i in range(1, len(units) + 1)]
    score[c] = 100 * sum(ag) / len(ag)
    exact[c] = sum(p1[f'u{i:02d}'] == p2[f'u{i:02d}'] for i in range(1, len(units) + 1)) / len(units)
    devs = [abs(p - int(u['consensus'])) for i, u in enumerate(units, 1) if u['consensus'] for p in (p1[f'u{i:02d}'], p2[f'u{i:02d}'])]
    cdev[c] = sum(devs) / len(devs)
for i, u in enumerate(units, 1):
    k = f'u{i:02d}'
    o, n = R['old'], R['new']
    row = [u['stretch'], k, o[0][k], o[1][k], n[0][k], n[1][k], u['consensus']]
    if u['consensus']:
        cons = int(u['consensus'])
        if max(n[0][k], n[1][k]) < cons <= max(o[0][k], o[1][k]):
            lost.append(u['stretch'])
    out.append(row)
with open(os.path.join(D, 'ab_results.tsv'), 'w') as f:
    f.write('stretch\tunit\told_1\told_2\tnew_1\tnew_2\tconsensus\n')
    for r in out:
        f.write('\t'.join(map(str, r)) + '\n')
    f.write(f"#score\t{score['old']:.1f}\t{score['new']:.1f}\n#exact\t{exact['old']:.3f}\t{exact['new']:.3f}\n"
            f"#consensus_mean_abs_dev\t{cdev['old']:.2f}\t{cdev['new']:.2f}\n#lost\t{','.join(lost) or '-'}\n")
ok = score['new'] >= score['old'] + 5 and not lost
print(f"old {score['old']:.1f} new {score['new']:.1f} (diff {score['new'] - score['old']:+.1f}); exact {exact['old']:.2f} / "
      f"{exact['new']:.2f}; |count - consensus| {cdev['old']:.2f} / {cdev['new']:.2f}; lost: {lost or 'none'}")
print('GATE PASS' if ok else 'GATE FAIL')
sys.exit(0 if ok else 1)
