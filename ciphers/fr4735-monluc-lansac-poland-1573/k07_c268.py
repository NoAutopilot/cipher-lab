#!/usr/bin/env python3
"""MONLUC-K07 (9 Oct 2026): does the f.86 '2/Z' form split (MONLUC-2: form A peaked Z ~ t, form B flat 2 = g)
hold on c268 (f.138) lines 1-5?

Usage: python3 k07_c268.py [--draws 10000] [--seed 7] [--check]

Form labels (FORMS below) are this worker's reading of native band crops (images/c268cipher_L0*_s*.jpg), set by
eye BEFORE any score was computed; not a blind sort. Positions index ciphertext_c268.tsv (pass A base).
Test: decode c268 with the published table (key.tsv); at each position, delta = char-5-gram log-prob of the line
with the sign read as 't' minus with its table letter (fr16 corpus, the spec's judge corpus). Statistic = mean delta
over form-A positions. Controls: (1) the same mean over random equal-size sets of other keyed positions
(--draws); (1b) the same over other positions whose table letter is u, as form A's is; (2) a permutation of the form labels across the 12 '2/Z/3' instances (exact, all subsets);
(3) the best single letter for all form-A positions together, out of a-z.
Writes results_k07_c268.json; --check exits 1 when it is stale (rule 7).
"""
import argparse, gzip, itertools, json, math, random, re, sys, unicodedata
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE.parents[1] / 'tools' / 'data' / 'fr16'
# instance -> (line, pos, form, table cell as pass A read it)
FORMS = {
    1: ('L01', 32, 'A', 'K19'), 2: ('L01', 28, 'B', 'K07'), 3: ('L02', 16, 'A', 'K63'), 4: ('L02', 18, 'A', 'K63'),
    5: ('L03', 10, 'A', 'K63'), 6: ('L03', 34, 'C', 'K63'), 7: ('L04', 14, 'A', 'K63'), 8: ('L04', 20, 'A', 'K63'),
    10: ('L04', 24, 'A', 'K63'), 11: ('L04', 36, 'A', 'K63'), 12: ('L05', 8, 'A', 'K63'), 13: ('L05', 13, 'A', 'K63'),
}
N = 5


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if c.isalpha() and ord(c) < 128)
    return s.replace('j', 'i').replace('v', 'u').replace('y', 'i')


def model():
    txt = ''.join(norm(gzip.open(f, 'rt', errors='ignore').read()) for f in sorted(DATA.glob('*.txt.gz')))
    grams = Counter(txt[i:i + N] for i in range(len(txt) - N + 1))
    ctx = Counter(txt[i:i + N - 1] for i in range(len(txt) - N + 2))
    return grams, ctx


def lp(s, grams, ctx):
    tot = 0.0
    for i in range(len(s) - N + 1):
        g = s[i:i + N]
        tot += math.log((grams[g] + 0.01) / (ctx[g[:-1]] + 0.26))
    return tot


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--draws', type=int, default=10000)
    ap.add_argument('--seed', type=int, default=7)
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    key = {l.split('\t')[0]: l.split('\t')[2] for l in (HERE / 'key.tsv').read_text().splitlines()[1:]}
    lines = {}
    for l in (HERE / 'ciphertext_c268.tsv').read_text().splitlines()[1:]:
        f = l.split('\t')
        ln, pos, sign = f[0], f[1], (f[4] if len(f) > 4 and f[4] else f[2])  # pass-A label (before MONLUC-RELABEL)
        lines.setdefault(ln, []).append((int(pos), sign))
    dec = {ln: [norm(key[s]) if s in key else '' for _, s in toks] for ln, toks in lines.items()}
    pos_ix = {ln: {p: i for i, (p, _) in enumerate(toks)} for ln, toks in lines.items()}
    grams, ctx = model()

    def delta(ln, i, letter):
        letters = dec[ln]
        w0 = ''.join(letters[max(0, i - 6):i + 7])
        alt = letters[:]; alt[i] = letter
        w1 = ''.join(alt[max(0, i - 6):i + 7])
        return lp(w1, grams, ctx) - lp(w0, grams, ctx)

    for inst, (ln, p, f, cell) in FORMS.items():
        assert lines[ln][pos_ix[ln][p]][1] == cell, (inst, ln, p)
    A = [(ln, pos_ix[ln][p]) for ln, p, f, _ in FORMS.values() if f == 'A']
    per = {inst: round(delta(ln, pos_ix[ln][p], 't'), 3) for inst, (ln, p, f, _) in FORMS.items()}
    stat = sum(delta(ln, i, 't') for ln, i in A) / len(A)
    pool = [(ln, i) for ln in dec for i, c in enumerate(dec[ln]) if c and c != 't' and (ln, i) not in A
            and all(not (ln == l2 and i == pos_ix[l2][p2]) for l2, p2, _, _ in FORMS.values())]
    pdel = {x: delta(x[0], x[1], 't') for x in pool}
    rng = random.Random(a.seed)
    null = [sum(pdel[x] for x in rng.sample(pool, len(A))) / len(A) for _ in range(a.draws)]
    null.sort()
    p_rand = (1 + sum(v >= stat for v in null)) / (1 + a.draws)
    # (1b) matched control: random equal-size sets of other positions whose table letter is u, as form A's is (drawn with replacement: the pool is small)
    upool = [x for x in pool if dec[x[0]][x[1]] == 'u']
    unull = sorted(sum(pdel[x] for x in rng.choices(upool, k=len(A))) / len(A) for _ in range(a.draws))
    p_u = (1 + sum(v >= stat for v in unull)) / (1 + a.draws)
    # exact label permutation across the 12 instances: which 9-of-11 / 10-of-12 subsets reach the stat
    insts = list(FORMS)
    vals = [per[k] for k in insts]
    combos = list(itertools.combinations(range(len(insts)), len(A)))
    perm = [sum(vals[j] for j in c) / len(A) for c in combos]
    p_perm = sum(v >= stat - 1e-9 for v in perm) / len(perm)
    best = sorted(((sum(delta(ln, i, ch) for ln, i in A), ch) for ch in 'abcdefghilmnopqrstuxz'), reverse=True)[:5]
    out = {
        'form_counts': dict(Counter(f for _, _, f, _ in FORMS.values())),
        'form_A_cells_pass_A': dict(Counter(c for _, _, f, c in FORMS.values() if f == 'A')),
        'per_instance_delta_t': per,
        'stat_mean_delta_t_formA': round(stat, 3),
        'random_positions_null_p95': round(null[int(0.95 * len(null))], 3),
        'random_positions_null_max': round(null[-1], 3),
        'p_random_positions': round(p_rand, 5),
        'u_positions_pool': len(upool),
        'u_positions_null_p95': round(unull[int(0.95 * len(unull))], 3),
        'u_positions_null_max': round(unull[-1], 3),
        'p_u_positions': round(p_u, 5),
        'label_permutation_subsets': len(perm),
        'p_label_permutation': round(p_perm, 4),
        'best_letters_formA': [[ch, round(v, 2)] for v, ch in best],
        'draws': a.draws, 'seed': a.seed,
    }
    path = HERE / 'results_k07_c268.json'
    s = json.dumps(out, indent=1, sort_keys=True) + '\n'
    if a.check:
        ok = path.exists() and path.read_text() == s
        print('k07_c268: OK' if ok else 'k07_c268: STALE'); sys.exit(0 if ok else 1)
    path.write_text(s); print(s)


if __name__ == '__main__':
    main()
