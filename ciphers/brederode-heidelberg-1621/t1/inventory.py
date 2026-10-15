#!/usr/bin/env python3
"""HEID-1621D first cheap test (PREREG-HEID1621D.md): unit inventory of the scan 379 block vs frozen nl16 pools.

Units as in ../../oldenbarnevelt-brederode-1605/heid1621/structure_6021.py: a maximal numeral run plus the following letter.
Control first (C1 discrimination, C2 rank-match on a synthetic word code); the target's rank-match runs only if C2 passes.
Writes t1/result.json. `--check` exits 1 if the committed result.json differs. No decode, no key.
"""
import csv, gzip, json, random, re, sys, statistics
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NL16 = ROOT / 'tools/data/nl16'
POOL = ['marn001bien01', 'marn001trou01', 'coor001zede01', 'spie001twes01']
HELD = 'coor001boev01'
SEED, NWIN, NCTL = 1621, 2000, 300

def target_units():
    rows = [r for r in csv.reader(open(HERE.parent / 'ciphertext.tsv'), delimiter='\t') if r and not r[0].startswith('#')][1:]
    units, cur = [], []
    for r in rows:
        k, t = r[2], r[3]
        if k == 'num': cur.append(int(t)); continue
        if cur: units.append((tuple(cur), t if k == 'let' else None)); cur = []
    if cur: units.append((tuple(cur), None))
    return units

def words(name):
    return re.findall(r'[a-zà-ÿ]+', gzip.open(NL16 / f'{name}.txt.gz', 'rt').read().lower())

def sylls(ws):
    out = []
    for w in ws:
        out += [p for p in re.findall(r'[^aeiouyàáèéëïóöü]*[aeiouyàáèéëïóöü]+(?:[^aeiouyàáèéëïóöü]+$)?', w) if p] or [w]
    return out

def windows(seq, n, k, rng):
    return [seq[s:s + n] for s in (rng.randrange(len(seq) - n) for _ in range(k))]

def kstat(win): return len(set(win))

def pct(dist, x): return round(sum(d < x for d in dist) / len(dist) + 0.5 * sum(d == x for d in dist) / len(dist), 4)

def q(dist, p): s = sorted(dist); return s[int(p * (len(s) - 1))]

def rankmatch(win, freqlist):
    # units ranked by count (ties by first occurrence) -> words of the frozen list in rank order
    c = Counter(win); order = sorted(c, key=lambda u: (-c[u], win.index(u)))
    guess = {u: freqlist[i] if i < len(freqlist) else None for i, u in enumerate(order)}
    return sum(guess[u] == u for u in win) / len(win)

def main():
    rng = random.Random(SEED)
    U = target_units(); N = len(U)
    K = kstat([u[0] for u in U]); KL = kstat(U)
    cnt = Counter(u[0] for u in U)
    pw = sum((words(f) for f in POOL), []); hw = words(HELD)
    pools = {'word': pw, 'syll': sylls(pw), 'letter': list(''.join(pw))}
    held = {'word': hw, 'syll': sylls(hw), 'letter': list(''.join(hw))}
    dist = {k: [kstat(w) for w in windows(v, N, NWIN, rng)] for k, v in pools.items()}
    med = {k: statistics.median(v) for k, v in dist.items()}
    # C1: held-out discrimination by nearest pool median
    c1 = {}
    for k, v in held.items():
        ks = [kstat(w) for w in windows(v, N, NCTL, rng)]
        c1[k] = sum(min(med, key=lambda m: abs(med[m] - x)) == k for x in ks) / NCTL
    wl = [x for x in held['word']]
    wv = [x for x in wl]
    def wl_vs_letter():
        ks_w = [kstat(w) for w in windows(held['word'], N, NCTL, rng)]
        ks_l = [kstat(w) for w in windows(held['letter'], N, NCTL, rng)]
        thr = (med['word'] + med['letter']) / 2
        return (sum(x > thr for x in ks_w) + sum(x <= thr for x in ks_l)) / (2 * NCTL)
    c1_wl = wl_vs_letter()
    # C2: synthetic word code of the same N and about the same K, rank-matched to the frozen pool's word list
    freq = [w for w, _ in Counter(pw).most_common(300)]
    cand = windows(held['word'], N, 20000, rng)
    near = [w for w in cand if abs(kstat(w) - K) <= 2]
    if len(near) < 20: near = sorted(cand, key=lambda w: abs(kstat(w) - K))[:20]
    near = near[:200]
    c2 = [rankmatch(w, freq) for w in near]
    c2_mean = round(statistics.mean(c2), 4)
    res = {
        'N_units': N, 'K_target_numeral_tuple': K, 'K_target_tuple_plus_letter': KL,
        'top_unit_share': round(cnt.most_common(1)[0][1] / N, 4), 'hapax': sum(1 for v in cnt.values() if v == 1),
        'pool': {k: {'median': med[k], 'p05': q(v, .05), 'p95': q(v, .95), 'target_pct': pct(v, K), 'target_pct_tuple_letter': pct(v, KL)} for k, v in dist.items()},
        'C1_nearest_median_acc': {k: round(v, 4) for k, v in c1.items()}, 'C1_word_vs_letter_acc': round(c1_wl, 4), 'C1_gate': 0.90,
        'C1_pass': c1_wl >= 0.90,
        'C2_windows': len(near), 'C2_K_range': [min(map(kstat, near)), max(map(kstat, near))], 'C2_rankmatch_mean': c2_mean,
        'C2_rankmatch_max': round(max(c2), 4), 'C2_gate': 0.50, 'C2_pass': c2_mean >= 0.50,
        'target_rankmatch': 'not run (C2 below gate: non-test at this N)' if c2_mean < 0.50 else 'gated: run separately',
        'seed': SEED, 'pool_files': POOL, 'held_out': HELD,
    }
    out = json.dumps(res, indent=1, ensure_ascii=False) + '\n'
    path = HERE / 'result.json'
    if '--check' in sys.argv:
        ok = path.exists() and path.read_text() == out
        print('check:', 'OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    path.write_text(out); print(out)

if __name__ == '__main__':
    main()
