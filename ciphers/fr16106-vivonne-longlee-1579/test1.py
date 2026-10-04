#!/usr/bin/env python3
"""VIV-T test 1 (PREREG_test1.md): held-out known-answer test of a stream-aligned key, fr.16107 c107 vs c110 f.105r.

    python3 test1.py            # power control (5 seeds x e in {0.576, 0.10}), then target (pass A gating, pass B reported)
    python3 test1.py --check    # recompute and exit 1 if test1_result.json or key.tsv / heldout_decode.txt differ
Writes test1_result.json, key.tsv (pass A fit-half key, grade C), heldout_decode.txt.
"""
import json, os, random, re, sys, unicodedata
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
import stream_align as sa

FIT_LINES = 20


def fold(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def plain_words():
    t = [l for l in open(os.path.join(HERE, 'tx', 'plain_c110_f105r.txt')) if not l.startswith('#')]
    t = fold(' '.join(t)).lower().replace('{?}', ' ')
    t = re.sub(r'[\[\]?]', '', t)
    return re.findall(r'[a-z]+', t.replace("'", ' '))


def lets(words):
    return np.array([ord(c) - 97 for w in words for c in w], dtype=np.int64)


def load_pass(p):
    lines = []
    for l in open(os.path.join(HERE, 'tx', f'pass{p}.tsv')):
        if l.startswith('row'):
            continue
        r, c = l.rstrip('\n').split('\t', 1)
        lines.append(c.split())
    return lines


def run(lines_sym, plain, K, rng, n_shuf=1000):
    fit = np.array([s for ln in lines_sym[:FIT_LINES] for s in ln])
    held = np.array([s for ln in lines_sym[FIT_LINES:] for s in ln])
    counts, path = sa.learn(fit, plain, K)
    key = sa.decode(counts)
    jend = path[-1][1] if path else 0
    W = min(len(plain) - jend - 1, round(len(held) * (jend + 1) / len(fit)))
    out = dict(n_fit=int(len(fit)), n_held=int(len(held)), jend=int(jend), W=int(W),
               n_valued=int((key >= 0).sum()), K=int(K))
    if len(held) < 3 * out['n_valued'] or W < 150:
        out['verdict'] = 'NON-TEST'
        return out, key, None
    ref = plain[jend + 1: jend + 1 + W]
    dec = np.array([key[s] for s in held])
    # null (a): value shuffle
    valued = np.where(key >= 0)[0]
    na = []
    for _ in range(n_shuf):
        k2 = key.copy(); k2[valued] = rng.permutation(key[valued])
        na.append(sa.nw_score(np.array([k2[s] for s in held]), ref))
    # null (b): wrong windows inside the fit-side text
    hi = jend + 1 - 20 - W
    offs = list(range(0, hi + 1)) if hi >= 0 else []
    short = max(0, 200 - len(offs))
    if 0 < len(offs) < 200:
        offs = [offs[int(i * len(offs) / 200)] for i in range(200)]
    nb = [sa.nw_score(dec, plain[o:o + W]) for o in offs]
    real = sa.nw_score(dec, ref)
    pa = float(np.percentile(na, 99)); pb = float(np.percentile(nb, 99)) if nb else float('nan')
    out.update(real=round(real, 4), null_a_p99=round(pa, 4), null_a_mean=round(float(np.mean(na)), 4),
               null_b_p99=round(pb, 4), null_b_mean=round(float(np.mean(nb)), 4) if nb else None,
               null_b_windows=len(offs), null_b_shortfall=short,
               verdict='PASS' if (nb and real > pa and real > pb) else 'FAIL')
    return out, key, dec


def synth(plain_words_list, K, e, n_lines, line_len_list, rng):
    pl = lets(plain_words_list)
    freq = np.bincount(pl, minlength=26).astype(float) + 0.01
    alloc = np.ones(26, int); rest = K - 26
    share = freq / freq.sum() * rest
    alloc += np.floor(share).astype(int)
    for i in np.argsort(-(share - np.floor(share)))[:K - alloc.sum()]:
        alloc[i] += 1
    homs, n = [], 0
    for c in range(26):
        homs.append(list(range(n, n + alloc[c]))); n += alloc[c]
    cip = [rng.choice(homs[c]) if rng.random() >= e else rng.randrange(K) for c in pl]
    lines, i = [], 0
    for L in line_len_list:  # same line lengths as pass A, scaled to the synthetic length
        lines.append(cip[i:i + L]); i += L
    lines[-1].extend(cip[i:])
    seen = [w for w in plain_words_list if rng.random() >= 0.20]
    return lines, lets(seen)


def main(check=False):
    words = plain_words(); plain = lets(words)
    res = {'plain_letters': int(len(plain))}
    A = load_pass('A'); B = load_pass('B')
    # control first (rule 3)
    allsym = sorted({s for ln in A for s in ln})
    K = len(allsym)
    tot = sum(len(l) for l in A)
    ll = [round(len(l) * len(plain) / tot) for l in A]
    ctrl = {}
    for e in (0.576, 0.10):
        rows = []
        for seed in range(5):
            rng = random.Random(seed); nrng = np.random.default_rng(seed)
            lines, seen = synth(words, K, e, len(A), ll, rng)
            o, _, _ = run(lines, seen, K, nrng, n_shuf=300)
            rows.append(o)
        ctrl[str(e)] = dict(passes=sum(r['verdict'] == 'PASS' for r in rows), rows=rows)
    res['control'] = ctrl
    res['control_licenses_fail'] = ctrl['0.576']['passes'] >= 4
    for p, lines in (('A', A), ('B', B)):
        ids = {s: n for n, s in enumerate(sorted({s for ln in lines for s in ln}))}
        L = [[ids[s] for s in ln] for ln in lines]
        o, key, dec = run(L, plain, len(ids), np.random.default_rng(1))
        if o['verdict'] == 'FAIL' and not res['control_licenses_fail']:
            o['verdict'] = 'FAIL -> NON-TEST (control below gate at e=0.576)'
        res['target_' + p] = o
        if p == 'A':
            inv = {v: k for k, v in ids.items()}
            fit = [s for ln in L[:FIT_LINES] for s in ln]
            cnt = {}
            for s in fit:
                cnt[s] = cnt.get(s, 0) + 1
            keytxt = 'symbol\tvalue\tfit_count\tgrade\n' + ''.join(
                f"{inv[i]}\t{chr(97 + key[i]) if key[i] >= 0 else '?'}\t{cnt.get(i, 0)}\tC\n" for i in range(len(ids)))
            dectxt = ''.join(chr(97 + d) if d >= 0 else '?' for d in dec) + '\n' if dec is not None else 'NON-TEST\n'
    outs = {'test1_result.json': json.dumps(res, indent=1) + '\n', 'key.tsv': keytxt, 'heldout_decode.txt': dectxt}
    if check:
        bad = [f for f, t in outs.items() if not os.path.exists(os.path.join(HERE, f)) or open(os.path.join(HERE, f)).read() != t]
        print('stale: ' + ', '.join(bad) if bad else 'check OK'); sys.exit(1 if bad else 0)
    for f, t in outs.items():
        open(os.path.join(HERE, f), 'w').write(t)
    print(json.dumps({k: v for k, v in res.items() if k != 'control'}, indent=1))
    for e, c in ctrl.items():
        print('control e=%s passes %d/5 real %s' % (e, c['passes'], [ (r.get('real'), r.get('null_a_p99'), r.get('null_b_p99')) for r in c['rows']]))


if __name__ == '__main__':
    main('--check' in sys.argv)
