#!/usr/bin/env python3
"""H6 (28 Sept 2026): which inventory ids do three independent readers confuse on cryptogram 1, and what does folding
them buy? From passA_c1/passB_c1/passC_c1 on the 52 disputed boxes: count every unordered id pair that appears in one
box's (A, B, C) triple; fold pairs confused at least T times (T = 2, 3, 5) into components (union-find); re-run the
H2 majority adjudication at the folded level and report agreement over 136 boxes, K_fold over the whole 1251-sign
inventory (ciphertext_draft.tsv) and the components. Rule 5 of PROMPTS_c1.md's numbers are the comparison (81.6 pct
full id). Writes h6_folds.json."""
import csv, os, json, collections, itertools
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
def load(p): return {(r['line'], int(r['position'])): r['sign'] for r in csv.DictReader(open(os.path.join(root, p)), delimiter='\t')}
A, B, C = load('passA_c1.tsv'), load('passB_c1.tsv'), load('passC_c1.tsv')
pairs = collections.Counter()
for k in C:
    for a, b in itertools.combinations(sorted({A[k], B[k], C[k]}), 2): pairs[(a, b)] += 1
allsigns = [r['sign'] for r in csv.DictReader(open(os.path.join(root, 'ciphertext_draft.tsv')), delimiter='\t') if r['sign'] not in ('_', 'MULTI')]
out = {'pairs': [[a, b, n] for (a, b), n in pairs.most_common()], 'folds': {}}
for T in (2, 3, 5):
    parent = {}
    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for (a, b), n in pairs.items():
        if n >= T and '_' not in (a, b) and 'MULTI' not in (a, b): parent[find(a)] = find(b)
    F = lambda s: find(s)
    comps = collections.defaultdict(set)
    for s in set(allsigns) | set(A.values()) | set(B.values()) | set(C.values()): comps[F(s)].add(s)
    comps = [sorted(c) for c in comps.values() if len(c) > 1]
    agree = sum(F(A[k]) == F(B[k]) for k in A); settled = 0; three = 0
    for k in C:
        v = collections.Counter([F(A[k]), F(B[k]), F(C[k])]); top, n = v.most_common(1)[0]
        if F(A[k]) == F(B[k]): continue
        if n >= 2: settled += 1
        else: three += 1
    K_fold = len({F(s) for s in allsigns})
    out['folds'][T] = dict(components=comps, AB_agree=agree, settled=settled, three_way=three, agreement=(agree + settled) / 136, K_fold=K_fold, K_full=len(set(allsigns)))
    print(f"T>={T}: {len(comps)} components {comps if len(comps) <= 6 else str(len(comps)) + ' comps, largest ' + str(max(len(c) for c in comps))}; A=B {agree}, settled {settled}, three-way {three}, agreement {(agree+settled)/136:.3f}, K_fold {K_fold} of {len(set(allsigns))}")
json.dump(out, open(os.path.join(root, 'h6_folds.json'), 'w'), indent=1)
