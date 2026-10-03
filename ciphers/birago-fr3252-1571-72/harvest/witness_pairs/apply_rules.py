#!/usr/bin/env python3
"""CEPPO-WITNESS-PAIRS (3 Oct 2026): apply the PREREG.md witness shape rules to f.47r pair tiles.
Feature source: the value-blind third reader's per-tile shape note (f47/la/f47_reread.tsv, NEVBIR-47C), parsed by keyword;
the rule, not the reader's label, decides. Compares the rule label with readers A, B (split tiles) and D (third reader),
with a shuffle control on A and B labels (D's labels are one-sided per family, so a shuffle of D cannot differ: reported
but flagged non-discriminating, CLAUDE.md rule 3).
  python3 apply_rules.py [--shuffles 1000] [--seed 1]  -> writes f47_rule_labels.tsv, prints the table
"""
import csv, random, sys, re
from pathlib import Path
H = Path(__file__).resolve().parent
FAM = {'S74': '6', 'S54': '6', 'S80': '8', 'S65': '8', 'S24': 'h', 'S88': 'h'}

def rule(fam, note):
    n = note.lower()
    if fam == '8':
        if 'not an 8' in n: return 'UNDECIDED'
        if re.search(r'(bar|stroke|line)[^;]*through', n) or 'with bar' in n: return 'S80'
        if 'no bar' in n or 'plain 8' in n: return 'S65'
    if fam == '6':
        if 'no crossbar' in n or 'no bar through' in n: return 'S74'
        if 'crossbar' in n or 'bar through' in n: return 'S54'
    if fam == 'h':
        if 'upright' in n: return 'S24'
        if 'slant' in n or 'diagonal' in n: return 'S88'
    return 'UNDECIDED'

def main():
    ns = int(sys.argv[sys.argv.index('--shuffles') + 1]) if '--shuffles' in sys.argv else 1000
    seed = int(sys.argv[sys.argv.index('--seed') + 1]) if '--seed' in sys.argv else 1
    split = {(r['passage'], r['pos']): r for r in csv.DictReader(open(H.parent / 'f47/la/f47_split_tiles.tsv'), delimiter='\t')}
    rows = []
    for r in csv.DictReader(open(H.parent / 'f47/la/f47_reread.tsv'), delimiter='\t'):
        s = split[(r['passage'], r['pos'])]
        fams = {FAM.get(x) for x in (s['A'], s['B'], r['label']) if x in FAM}
        if len(fams) != 1 or not ({s['A'], s['B']} <= set(FAM)): continue
        f = fams.pop()
        rows.append(dict(passage=r['passage'], pos=r['pos'], family=f, A=s['A'], B=s['B'], D=r['label'],
                         rule=rule(f, r['note']), note=r['note']))
    with open(H / 'f47_rule_labels.tsv', 'w') as fh:
        w = csv.DictWriter(fh, list(rows[0]), delimiter='\t'); w.writeheader(); w.writerows(rows)
    rnd = random.Random(seed)
    print('family\tn\tdecided\trule_counts\tagree_A\tagree_B\tagree_D\tshufA_mean\tshufA_p95\tshufB_mean\tshufB_p95')
    for f in ('8', '6', 'h'):
        rs = [r for r in rows if r['family'] == f]; d = [r for r in rs if r['rule'] != 'UNDECIDED']
        if not d: print(f, len(rs), 0, sep='\t'); continue
        ag = lambda key, labs=None: sum((labs[i] if labs else r[key]) == r['rule'] for i, r in enumerate(d))
        out = []
        for key in ('A', 'B'):
            labs = [r[key] for r in d]; sh = []
            for _ in range(ns):
                rnd.shuffle(labs); sh.append(ag(key, labs))
            sh.sort(); out += [f'{sum(sh)/ns:.1f}', str(sh[int(0.95 * ns)])]
        cnt = {}
        for r in d: cnt[r['rule']] = cnt.get(r['rule'], 0) + 1
        print(f, len(rs), len(d), cnt, ag('A'), ag('B'), ag('D'), *out, sep='\t')

if __name__ == '__main__':
    main()
