#!/usr/bin/env python3
"""N7-HELBC blank-cell test of R4388 on the 1763 letters (PREREG-N7HELBC.md).

  --targets   write cells.tsv (270 target codes + 100 null codes, shuffled, seed 4388)
  --score     read cells_read.tsv (code, state F/B/X/?) and print S, null, control, verdict
"""
import argparse, collections, csv, os, random, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); UP = os.path.dirname(HERE)
LETTERS = ['R1045', 'R1046', 'R1047', 'R1048', 'R1060', 'R1061']

def target_counts():
    c = collections.Counter()
    for r in LETTERS:
        for tok in open(os.path.join(UP, f'ciphertext_{r}.txt')).read().split():
            if re.fullmatch(r'\d+', tok) and 2001 <= int(tok) <= 3900:
                c[int(tok)] += 1
    return c

def targets():
    c = target_counts()
    rng = random.Random(4388)
    pool = [k for k in range(2001, 3901) if k not in c]
    null = rng.sample(pool, 100)
    cells = [(k, 'T') for k in sorted(c)] + [(k, 'N') for k in sorted(null)]
    rng.shuffle(cells)
    with open(os.path.join(HERE, 'cells.tsv'), 'w') as f:
        f.write('order\tcode\tset\ttokens\n')
        for i, (k, s) in enumerate(cells):
            f.write(f'{i}\t{k}\t{s}\t{c.get(k, 0)}\n')
    print(f'targets {len(c)} codes / {sum(c.values())} tokens; null {len(null)}; cells.tsv written')

def pct(xs, p):
    xs = sorted(xs); return xs[min(len(xs) - 1, int(p * len(xs)))]

def score(xblank=False):
    c = target_counts()
    st = {int(r['code']): r['state'] for r in csv.DictReader(open(os.path.join(HERE, 'cells_read.tsv')), delimiter='\t')}
    isb = lambda s: s == 'B' or (xblank and s == 'X')
    num = sum(v for k, v in c.items() if st.get(k) not in ('?', None) and isb(st[k]))
    den = sum(v for k, v in c.items() if st.get(k) not in ('?', None))
    drop = sum(v for k, v in c.items() if st.get(k) in ('?', None))
    S = num / den
    strip = [(k, v) for k, v in c.items() if 3001 <= k <= 3100 and st.get(k) not in ('?', None)]
    Ss = sum(v for k, v in strip if isb(st[k])) / max(1, sum(v for k, v in strip))
    cells = [isb(st[k]) for k in range(2001, 3901) if k not in c and k in st and st[k] != '?']
    p0 = sum(cells) / len(cells)
    rng = random.Random(1)
    mult = [v for k, v in c.items() if st.get(k) not in ('?', None)]
    tot = sum(mult); null = []
    for _ in range(10000):
        null.append(sum(m for m in mult if rng.choice(cells)) / tot)
    toks = [r for r in csv.DictReader(open(os.path.join(UP, 'key_r4369', 'reading_R1953_tokens.tsv')), delimiter='\t')
            if r['sign'].isdigit() and 801 <= int(r['sign']) <= 1796]
    ctl = [r['grade'] == 'U' for r in toks]
    cs = []
    for _ in range(10000):
        cs.append(sum(rng.choice(ctl) for _ in range(den)) / den)
    n01, n05, nmed = pct(null, .01), pct(null, .05), pct(null, .5)
    c95, c99 = pct(cs, .95), pct(cs, .99)
    power = c99 < n01
    if not power: v = 'NON-TEST (control p99 >= null p01)'
    elif S <= 0.10 and S < n01: v = 'PASS -> candidate for full transcription'
    elif S >= n05: v = 'FAIL -> R4388 retired as the 1763 key (blank-cell test)'
    else: v = 'INCONCLUSIVE'
    print(f'X counted as {"blank" if xblank else "filled"}')
    print(f'S = {num}/{den} = {S:.3f} (tokens dropped as ?: {drop}); strip 3001-3100 S = {Ss:.3f} (not gated)')
    print(f'null cells {len(cells)}, p0 = {p0:.3f}; null of S: p01 {n01:.3f}, p05 {n05:.3f}, median {nmed:.3f}')
    print(f'control R4369/R1953 ({sum(ctl)}/{len(ctl)}) at N={den}: p95 {c95:.3f}, p99 {c99:.3f}; power {"OK" if power else "FAIL"}')
    print(f'verdict: {v}')

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--targets', action='store_true'); ap.add_argument('--score', action='store_true')
    ap.add_argument('--x-blank', action='store_true')
    a = ap.parse_args()
    if a.targets: targets()
    if a.score: score(a.x_blank)
