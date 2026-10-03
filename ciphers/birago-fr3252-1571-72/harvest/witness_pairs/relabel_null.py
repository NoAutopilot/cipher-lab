#!/usr/bin/env python3
"""CEPPO-WITNESS-PAIRS (3 Oct 2026): value control for a rule relabel. Score (printed Ceppo-Nevers key, it16dip 4-gram,
decode_control.py's own scorer) of the rule-relabelled sequence vs N sequences in which the SAME positions get a random
other sheet sign instead (and, separately, vs N random position sets of the same size relabelled at random). A rule whose
gain is matched by random relabels at those positions licenses nothing.
  python3 relabel_null.py BASE.tsv RULE.tsv [--n 500] [--seed 1]
"""
import csv, random, sys
from pathlib import Path
CN = Path(__file__).resolve().parents[3] / 'ceppo-nevers-fr3251-1570s/harvest'
sys.path.insert(0, str(CN))
import decode_control as dc  # noqa: E402

def load(p):
    rows = list(csv.DictReader(open(p), delimiter='\t'))
    return rows

def passages(rows):
    d = {}
    for r in rows: d.setdefault(r['passage'], []).append(r['sign_id'].strip())
    return d

def main():
    base, rule = load(sys.argv[1]), load(sys.argv[2])
    n = int(sys.argv[sys.argv.index('--n') + 1]) if '--n' in sys.argv else 500
    rng = random.Random(int(sys.argv[sys.argv.index('--seed') + 1]) if '--seed' in sys.argv else 1)
    m = dc.load_map(['X_THETA2=r'])
    jp = dc.jp
    texts = [jp.read_corpus(p) if hasattr(jp, 'read_corpus') else jp.load_text(p) for p in jp.LANG_CORPORA['it16dip']]
    model = jp.NgramModel(texts)
    idx = [i for i, (a, b) in enumerate(zip(base, rule)) if a['sign_id'] != b['sign_id']]
    signs = list(m)
    sb, sr = dc.score(model, passages(base), m), dc.score(model, passages(rule), m)
    same, anyp = [], []
    keyed = [i for i, r in enumerate(base) if r['sign_id'] in m]
    for _ in range(n):
        for pool, out in ((idx, same), (rng.sample(keyed, len(idx)), anyp)):
            rr = [dict(r) for r in base]
            for i in pool: rr[i]['sign_id'] = rng.choice([s for s in signs if s != base[i]['sign_id']])
            out.append(dc.score(model, passages(rr), m))
    for name, xs in (('same positions, random signs', same), ('random positions, random signs', anyp)):
        xs.sort(); ge = sum(x >= sr for x in xs)
        print(f'{name}: n={n} mean {sum(xs)/n:.4f} p95 {xs[int(.95*n)]:.4f} max {xs[-1]:.4f}; >= rule: {ge}/{n} (p={(ge+1)/(n+1):.3f})')
    print(f'base {sb:.4f}  rule {sr:.4f}  positions changed {len(idx)}')



def family_flip(base_p, rule_p, n=500, seed=1):
    """Stricter control: flip the same number of randomly chosen in-family positions (S24<->S88, S65<->S80, S74<->S54)
    as the rule flipped per family, so the value set is the same and only WHICH tiles flip changes."""
    flip = {'S24': 'S88', 'S88': 'S24', 'S65': 'S80', 'S80': 'S65', 'S74': 'S54', 'S54': 'S74'}
    fam = {'S24': 'h', 'S88': 'h', 'S65': '8', 'S80': '8', 'S74': '6', 'S54': '6'}
    base, rule = load(base_p), load(rule_p)
    m = dc.load_map(['X_THETA2=r']); jp = dc.jp
    model = jp.NgramModel([jp.read_corpus(p) if hasattr(jp, 'read_corpus') else jp.load_text(p) for p in jp.LANG_CORPORA['it16dip']])
    rng = random.Random(seed)
    changed = [i for i, (a, b) in enumerate(zip(base, rule)) if a['sign_id'] != b['sign_id']]
    need = {}
    for i in changed:
        k = (fam[base[i]['sign_id']], base[i]['sign_id']); need[k] = need.get(k, 0) + 1
    sr = dc.score(model, passages(rule), m); xs = []
    for _ in range(n):
        rr = [dict(r) for r in base]
        for (f, s), c in need.items():
            pool = [i for i, r in enumerate(base) if r['sign_id'] == s]
            for i in rng.sample(pool, min(c, len(pool))): rr[i]['sign_id'] = flip[s]
        xs.append(dc.score(model, passages(rr), m))
    xs.sort(); ge = sum(x >= sr for x in xs)
    print(f'in-family flips {dict((f"{k[1]}->{flip[k[1]]}", v) for k, v in need.items())}: n={n} mean {sum(xs)/n:.4f} '
          f'p95 {xs[int(.95*n)]:.4f} max {xs[-1]:.4f}; >= rule {sr:.4f}: {ge}/{n} (p={(ge+1)/(n+1):.3f})')


if __name__ == '__main__':
    if '--family' in sys.argv:
        family_flip(sys.argv[1], sys.argv[2], int(sys.argv[sys.argv.index('--n') + 1]) if '--n' in sys.argv else 500)
    else:
        main()
