#!/usr/bin/env python3
"""OBRED-BAND (15 Oct 2026), PREREG obred187/PREREG-OBREDBAND.md.

Band-interval check of the 1619 glossed pairs (inv. 6019 scans 555-556, ciphertext_556.tsv): fit letter bands on one leaf, score the
other leaf's glossed codes (S = mean of hit/width), against a shuffled-band null (10,000 draws, seed 1619), with a synthetic power run
at the same pair counts (nl16 text, alphabetical homophonic list on 1..587, 200 simulations x 1,000 nulls, seed 92). Only if the gate
passes, writes the interval reading of no. 92 + the scan-187 postscript (grade M, names 588-751 left as codes).
Writes band_gate.json (and reading_92_187.tsv if the gate passes) beside this script; --check exits 1 if a regeneration differs.
Run: python3 ciphers/oldenbarnevelt-brederode-1605/obred187/band/band.py [--check]
"""
import bisect, glob, gzip, json, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.normpath(os.path.join(HERE, '..', '..'))
ROOT = os.path.normpath(os.path.join(T, '..', '..'))
sys.path.insert(0, os.path.join(T, 'obred187', 'try'))
from run_try import pairs556, fold, ALPHA  # OBRED-TRY's pair rule, unchanged

NA = len(ALPHA)
NAME_LO, NAME_HI = 588, 751


def interval(train, v):
    """train: sorted list of (code, idx); returns (lo, hi) letter-index interval."""
    codes = [c for c, _ in train]
    same = [g for c, g in train if c == v]
    if same:
        return min(same), max(same)
    i = bisect.bisect_left(codes, v)
    lo_g = train[i - 1][1] if i > 0 else None
    hi_g = train[i][1] if i < len(train) else None
    if lo_g is None:
        return 0, hi_g
    if hi_g is None:
        return lo_g, NA - 1
    return min(lo_g, hi_g), max(lo_g, hi_g)


def score(train, test):
    train = sorted(train)
    s = hits = wsum = nn = 0
    codes = [c for c, _ in train]
    for v, g in test:
        lo, hi = interval(train, v)
        w = hi - lo + 1
        h = lo <= g <= hi
        s += h / w; hits += h; wsum += w
        # nearest code (tie -> lower)
        i = bisect.bisect_left(codes, v)
        cand = [j for j in (i - 1, i) if 0 <= j < len(train)]
        j = min(cand, key=lambda k: (abs(codes[k] - v), codes[k]))
        nn += train[j][1] == g
    n = len(test)
    return dict(S=s / n, hit=hits / n, width=wsum / n, nn=nn / n, n=n)


def null_p(train, test, draws, rng):
    real = score(train, test)['S']
    codes = [c for c, _ in train]; letters = [g for _, g in train]
    ge = 0; vals = []
    for _ in range(draws):
        rng.shuffle(letters)
        s = score(list(zip(codes, letters)), test)['S']
        vals.append(s); ge += s >= real - 1e-12
    vals.sort()
    return dict(p=ge / draws, null_mean=sum(vals) / draws, null_p95=vals[int(0.95 * draws)], null_max=vals[-1])


def leaf_pairs(P, scan=None, hread=False):
    out = []
    for p in P:
        if p['letter'] is None:
            continue
        if scan and p['scan'] != scan:
            continue
        if hread and p['grade'] != 'H-read':
            continue
        out.append((int(p['group']), ALPHA.index(fold(p['letter']))))
    return out


def nl16_letters():
    txt = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'tools', 'data', 'nl16', '*.txt.gz'))):
        txt.append(gzip.open(f, 'rt', encoding='utf-8', errors='ignore').read())
    s = re.sub(r'[^a-z]', '', ''.join(txt).lower())
    return [ALPHA.index(fold(c)) for c in s if fold(c) in ALPHA]


def synth_list(seq, rng):
    freq = [0] * NA
    for g in seq:
        freq[g] += 1
    tot = sum(freq); ncode = NAME_LO - 1
    widths = [max(1, round(ncode * f / tot)) for f in freq]
    # trim/pad the most frequent letter so the list covers exactly 1..587
    k = widths.index(max(widths)); widths[k] += ncode - sum(widths)
    bands, c = [], 1
    for g, w in enumerate(widths):
        bands.append(list(range(c, c + w))); c += w
    return bands


def power(n_train, n_test, n_pool, n_app, sims, draws, seed):
    rng = random.Random(seed)
    seq = nl16_letters()
    bands = synth_list(seq, rng)
    enc = lambda g: rng.choice(bands[g])
    win = lambda n: seq[(st := rng.randrange(0, len(seq) - 20 * n)):st + 20 * n]
    passes = 0; one_share = one_acc = app_hit = 0.0
    for _ in range(sims):
        tr = [(enc(g), g) for g in rng.sample(win(n_train), n_train)]
        te = [(enc(g), g) for g in rng.sample(win(n_test), n_test)]
        passes += null_p(tr, te, draws, rng)['p'] <= 0.05
        pool = sorted((enc(g), g) for g in rng.sample(win(n_pool), n_pool))
        st = rng.randrange(0, len(seq) - n_app); text = seq[st:st + n_app]
        ones = ok = hit = 0
        for g in text:
            lo, hi = interval(pool, enc(g))
            hit += lo <= g <= hi
            if lo == hi:
                ones += 1; ok += lo == g
        one_share += ones / n_app; one_acc += (ok / ones) if ones else 0; app_hit += hit / n_app
    return dict(power=passes / sims, sims=sims, draws=draws, app_one_letter_share=one_share / sims,
                app_one_letter_acc=one_acc / sims, app_interval_hit=app_hit / sims, n_app=n_app,
                design='alphabetical homophonic 1..587, widths ~ nl16 letter frequency (assumed)')


def tokens(name):
    return [int(x) for x in open(os.path.join(T, 'obred187', name)).read().split()]


def build():
    P = pairs556()
    p555, p556 = leaf_pairs(P, '555'), leaf_pairs(P, '556')
    res = {'n_pairs': {'555': len(p555), '556': len(p556)}}
    res['power'] = power(len(p555), len(p556), len(p555) + len(p556), 180, 200, 1000, 92)
    rng = random.Random(1619)
    prim = score(p555, p556); prim.update(null_p(p555, p556, 10000, rng))
    rev = score(p556, p555); rev.update(null_p(p556, p555, 10000, random.Random(1619)))
    h5, h6 = leaf_pairs(P, '555', True), leaf_pairs(P, '556', True)
    sens = score(h5, h6); sens.update(null_p(h5, h6, 10000, random.Random(1619)))
    res.update(primary_555_to_556=prim, reverse_556_to_555=rev, sensitivity_hread_555_to_556=sens)
    ok = res['power']['power'] >= 0.70 and prim['p'] <= 0.05
    res['gate'] = 'PASS' if ok else ('NON-TEST (power < 0.70)' if res['power']['power'] < 0.70 else 'FAIL (held-out p > 0.05)')
    res = json.loads(json.dumps(res), parse_float=lambda x: round(float(x), 4))
    rows = None
    if ok:
        pool = sorted(p555 + p556)
        rows = ['text\tpos\tcode\tinterval\twidth\tgrade']
        cnt = dict(one=0, two=0, name=0, n=0)
        for name, toks in (('92', tokens('tokens_92.txt')), ('187', tokens('tokens_187.txt'))):
            for i, v in enumerate(toks, 1):
                cnt['n'] += 1
                if NAME_LO <= v <= NAME_HI:
                    cnt['name'] += 1; rows.append(f'{name}\t{i}\t{v}\t[name code]\t\tM'); continue
                lo, hi = interval(pool, v); w = hi - lo + 1
                cnt['one'] += w == 1; cnt['two'] += w <= 2
                rows.append(f'{name}\t{i}\t{v}\t{ALPHA[lo:hi + 1]}\t{w}\tM')
        res['application'] = cnt
        rows = '\n'.join(rows) + '\n'
    return json.dumps(res, indent=1, sort_keys=True) + '\n', rows


def main():
    gate, rows = build()
    gp, rp = os.path.join(HERE, 'band_gate.json'), os.path.join(HERE, 'reading_92_187.tsv')
    if '--check' in sys.argv:
        bad = open(gp).read() != gate if os.path.exists(gp) else True
        if rows is not None:
            bad |= (open(rp).read() != rows) if os.path.exists(rp) else True
        print('stale' if bad else 'up to date'); sys.exit(1 if bad else 0)
    open(gp, 'w').write(gate)
    if rows is not None:
        open(rp, 'w').write(rows)
    print(gate)


if __name__ == '__main__':
    main()
