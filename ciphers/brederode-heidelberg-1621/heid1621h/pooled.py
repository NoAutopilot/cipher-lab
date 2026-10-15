#!/usr/bin/env python3
"""HEID-1621H step 3 (PREREG-HEID1621H.md): test 1 at the pooled N (13 Aug 379 + 17 Sept 423 units) and the counted test of
"single = first number". Letters are excluded from the inventory keys (step 1's control FAILed: letters unreliable).

usage: python3 pooled.py [--check]
Reuses t1/inventory.py's nl16 pool, held-out file, window and rank-match functions. Control C3 first (synthetic word code with the
target's 45/14 division and form split, same keys, same decision rule); the target's band is read only if C3 >= 0.90 for that key.
Writes pooled_result.json; --check exits 1 if the committed file differs. No decode, no key, no reading.
"""
import csv, json, random, statistics, sys
from collections import Counter
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 't1'))
import inventory as T1

SEED, NWIN, NC3, NNULL = 1621, 2000, 300, 10000

def units_13aug():  # scan 379, as t1 (numeral tuple, letter)
    return T1.target_units()

def units_17sept():
    rows = [r for r in csv.DictReader((l for l in open(HERE.parent / 'heid1621g' / 'ciphertext_6021_423.tsv', encoding='utf-8')
                                        if not l.startswith('#')), delimiter='\t')]
    return [(tuple(int(x) for x in r['numbers'].split('.')), r['letter'] or None, r['form']) for r in rows]

KEYS = {'KT_as_transcribed': lambda t: t, 'KF_single_eq_first': lambda t: t[0]}

def band(K, st):
    w, l = st['word'], st['letter']
    if w['p05'] <= K <= w['p95'] and abs(K - w['median']) < abs(K - l['median']): return 'word band'
    if l['p05'] <= K <= l['p95']: return 'letter band'
    if l['p95'] < K < w['p05']: return 'below the word band'
    return 'undecided'

def two_piece(seq, rng, a=45, b=14):
    i, j = rng.randrange(len(seq) - a), rng.randrange(len(seq) - b)
    return seq[i:i + a], seq[j:j + b]

def synth(held, rng):
    """synthetic word code: two pieces (45, 14) of held-out words; type -> random (n, n+1); piece 2 in the 423 form split."""
    p1, p2 = two_piece(held, rng)
    firsts = rng.sample(range(10, 400), len(set(p1) | set(p2)))
    code = {w: (n, n + 1) for w, n in zip(sorted(set(p1) | set(p2)), firsts)}
    u1 = [code[w] for w in p1]
    forms = ['S1'] * 12 + ['R3', 'N']; rng.shuffle(forms)
    u2 = []
    for w, f in zip(p2, forms):
        n = code[w][0]
        u2.append((rng.randrange(1, 100), rng.randrange(1, 100), n) if f == 'R3' else (n,))
    return u1 + u2

def main():
    rng = random.Random(SEED)
    U13, U17 = units_13aug(), units_17sept()
    pw = sum((T1.words(f) for f in T1.POOL), []); hw = T1.words(T1.HELD)
    pools = {'word': pw, 'syll': T1.sylls(pw), 'letter': list(''.join(pw))}
    dist = {k: [T1.kstat(a + b) for a, b in (two_piece(v, rng) for _ in range(NWIN))] for k, v in pools.items()}
    st = {k: {'median': statistics.median(v), 'p05': T1.q(v, .05), 'p95': T1.q(v, .95)} for k, v in dist.items()}
    tup = [u[0] for u in U13] + [u[0] for u in U17]
    res = {'N_units': len(tup), 'N_13aug': len(U13), 'N_17sept': len(U17), 'pools_two_piece_45_14': st, 'keys': {}}
    for kn, kf in KEYS.items():
        # C3 control first: synthetic word codes under the same key and decision rule
        c3 = [band(T1.kstat([kf(t) for t in synth(hw, rng)]), st) for _ in range(NC3)]
        c3_acc = round(c3.count('word band') / NC3, 4)
        K = T1.kstat([kf(t) for t in tup])
        entry = {'C3_word_band_share': c3_acc, 'C3_outcomes': dict(Counter(c3)), 'C3_gate': 0.90, 'C3_pass': c3_acc >= 0.90, 'K_target': K}
        if c3_acc >= 0.90:
            entry.update({'target_pct_in_pool': {k: T1.pct(v, K) for k, v in dist.items()}, 'target_band': band(K, st)})
        else:
            entry['target_band'] = 'not read (C3 below gate: non-test for this key at N=59)'
        res['keys'][kn] = entry
    # C2 rank-match at N=59 (carried from t1): held-out windows near the KF K, ranked onto the frozen word list
    Kf = res['keys']['KF_single_eq_first']['K_target']
    freq = [w for w, _ in Counter(pw).most_common(300)]
    cand = [a + b for a, b in (two_piece(hw, rng) for _ in range(20000))]
    near = [w for w in cand if abs(T1.kstat(w) - Kf) <= 2] or sorted(cand, key=lambda w: abs(T1.kstat(w) - Kf))[:20]
    near = near[:200] if len(near) >= 20 else sorted(cand, key=lambda w: abs(T1.kstat(w) - Kf))[:20]
    c2 = [T1.rankmatch(w, freq) for w in near]
    res['C2'] = {'windows': len(near), 'K_range': [min(map(T1.kstat, near)), max(map(T1.kstat, near))],
                 'rankmatch_mean': round(statistics.mean(c2), 4), 'rankmatch_max': round(max(c2), 4), 'gate': 0.50,
                 'pass': statistics.mean(c2) >= 0.50, 'target_rankmatch': 'not run (C2 below gate)' if statistics.mean(c2) < 0.50 else 'gated: run separately'}
    # 3b: "single = first number" counted test (letters as transcribed, M)
    P = [(t, (l or '').lower()) for t, l in U13 if len(t) == 2 and l]
    S1 = [(t[0], (l or '').lower()) for t, l, f in U17 if f == 'S1']
    lo, hi = min(min(t) for t, _ in U13), max(max(t) for t, _ in U13)
    def stats(s1):
        return {'k_first': sum(any(n == t[0] for t, _ in P) for n, _ in s1),
                'k_either': sum(any(n in t for t, _ in P) for n, _ in s1),
                'k_first_letter': sum(any(n == t[0] and l == pl for t, pl in P) for n, l in s1),
                'k_either_letter': sum(any(n in t and l == pl for t, pl in P) for n, l in s1)}
    obs = stats(S1)
    nr = random.Random(SEED)
    V = [stats([(nr.randint(lo, hi), l) for _, l in S1]) for _ in range(NNULL)]
    Pn = []
    for _ in range(NNULL):
        ls = [l for _, l in S1]; nr.shuffle(ls); Pn.append(stats([(n, l) for (n, _), l in zip(S1, ls)]))
    p = lambda null, k: round(sum(d[k] >= obs[k] for d in null) / NNULL, 4)
    res['single_eq_first'] = {
        'n_S1': len(S1), 'P_units_13aug_379': len(P), 'numeral_range_13aug': [lo, hi], 'observed': obs,
        'value_null': {k: {'mean': round(statistics.mean(d[k] for d in V), 3), 'p': p(V, k)} for k in ('k_first', 'k_either')},
        'pairing_null': {k: {'mean': round(statistics.mean(d[k] for d in Pn), 3), 'p': p(Pn, k)} for k in ('k_first_letter', 'k_either_letter')},
        'note': 'letters M (step 1 control FAIL); a p < 0.01 is a counted lead (M), never a key or a reading'}
    res['seed'] = SEED
    out = json.dumps(res, indent=1, ensure_ascii=False) + '\n'
    path = HERE / 'pooled_result.json'
    if '--check' in sys.argv:
        ok = path.exists() and path.read_text() == out
        print('check:', 'OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    path.write_text(out); print(out)

if __name__ == '__main__':
    main()
