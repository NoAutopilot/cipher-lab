#!/usr/bin/env python3
"""HEID-1621 structural test (PREREG-HEID1621.md): S1-S4 on the reconciled inv. 6021 scan-379 groups, C1 on no. 92
(obred187/tokens_92.txt), C2 order-shuffle null. --check re-runs and exits 1 if structure_6021.json is stale."""
import json, os, random, sys
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__))
rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(H, 'ciphertext_6021_379.tsv')) if l.strip() and not l.startswith('#')][1:]
toks = [(r[0], r[2], r[3], r[4] if len(r) > 4 else '') for r in rows]
# units: maximal numeral run + following letter (runs cross line ends; any word/sym ends a run)
units, cur = [], []
for _, k, t, _a in toks:
    if k == 'num': cur.append(int(t)); continue
    if cur: units.append((cur, t if k == 'let' else None)); cur = []
if cur: units.append((cur, None))
nums = [int(t) for _, k, t, _a in toks if k == 'num']
def cons_adj(seq): return sum(b == a + 1 for a, b in zip(seq, seq[1:])) / max(1, len(seq) - 1)
pairs = [u for u in units if len(u[0]) == 2]
s1 = sum(u[0][1] == u[0][0] + 1 for u in pairs) / len(pairs)
# alternative reading of the one unsettled numeral (L03 58/88) does not change pair consecutiveness count unless 88
s1_alt = (sum(u[0][1] == u[0][0] + 1 for u in pairs) - 1) / len(pairs)
firsts = Counter(u[0][0] for u in pairs)
lets = Counter(u[1] for u in units if u[1])
random.seed(1621); null = []
for _ in range(10000):
    s = nums[:]; random.shuffle(s); null.append(cons_adj(s))
null.sort()
# S4: units per numeral-only line (L05, L08; units starting on the line) vs clear lines (worker's eye, M)
units_line = {'L05': 6, 'L08': 7}
clear = {'L01': (6, 13), 'L15': (8, 16), 'C01': (9, 14), 'C02': (6, 14), 'C03': (6, 16), 'C04': (4, 13)}
w = sum(v[0] for v in clear.values()) / len(clear); sy = sum(v[1] for v in clear.values()) / len(clear)
u = sum(units_line.values()) / len(units_line)
c92 = [int(x) for x in open(os.path.join(os.path.dirname(H), 'obred187', 'tokens_92.txt')).read().split()]
# descriptive, not preregistered: letter shared by overlapping pairs (n,n+1) and (n+1,n+2)
bypair = {}
for u_ in pairs:
    bypair.setdefault(tuple(u_[0]), Counter())[u_[1]] += 1
overl = []
for (a, b), c in bypair.items():
    if (b, b + 1) in bypair: overl.append([f'{a}.{b}', dict(c), f'{b}.{b+1}', dict(bypair[(b, b + 1)])])
out = {
 'n_numeral_tokens': len(nums), 'n_units': len(units), 'unit_sizes': dict(Counter(len(x[0]) for x in units)),
 'S1_pair_consecutive_share': round(s1, 4), 'S1_pair_consecutive_if_88': round(s1_alt, 4), 'n_pairs': len(pairs),
 'non_consecutive_pairs': [x[0] for x in pairs if x[0][1] != x[0][0] + 1],
 'single_numeral_units': [x[0] for x in units if len(x[0]) == 1], 'longer_units': [x[0] for x in units if len(x[0]) > 2],
 'S1_adjacent_all_tokens': round(cons_adj(nums), 4),
 'C2_shuffle_adjacent_mean': round(sum(null) / len(null), 4), 'C2_shuffle_adjacent_p99': round(null[9899], 4),
 'S2_distinct_pairs': len(firsts), 'S2_repeats': {f'{k}.{k+1}': v for k, v in sorted(firsts.items()) if v > 1},
 'S2_value_range': [min(nums), max(nums)],
 'S3_distinct_letters': len(lets), 'S3_letters': dict(sorted(lets.items())),
 'S3_units_with_letter': f'{sum(1 for x in units if x[1])}/{len(units)}',
 'S4_units_per_numeral_line': u, 'S4_words_per_clear_line': round(w, 2), 'S4_syllables_per_clear_line': round(sy, 2),
 'S4_lead': ('unit~word' if abs(u - w) <= .25 * w else '') + ('unit~syllable' if abs(u - sy) <= .25 * sy else '') or 'indeterminate',
 'C1_no92_n': len(c92), 'C1_no92_adjacent_consecutive': round(cons_adj(c92), 4),
 'C1_no92_consecutive_pairs': [[a, b] for a, b in zip(c92, c92[1:]) if b == a + 1],
 'C1_no92_distinct': len(set(c92)), 'C1_no92_range': [min(c92), max(c92)], 'C1_no92_letters': 0,
 'descriptive_overlapping_pairs_letters': overl,
}
J = os.path.join(H, 'structure_6021.json'); s = json.dumps(out, indent=1, ensure_ascii=False)
if '--check' in sys.argv:
    ok = open(J).read() == s; print('structure_6021.json', 'current' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(J, 'w').write(s); print(s)
