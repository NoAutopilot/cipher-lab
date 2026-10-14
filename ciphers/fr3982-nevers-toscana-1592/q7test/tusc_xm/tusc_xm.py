#!/usr/bin/env python3
"""tusc_xm.py: pre-registered screen of Tomokiyo's two Tuscan tables against fr3982 f.25 (PREREG-TUSC-XM.md).

  python3 q7test/tusc_xm/tusc_xm.py target          score both tables on ciphertext.tsv with both nulls
  python3 q7test/tusc_xm/tusc_xm.py power [--n 100] power check (synthetic texts, conditions C0-C3)
  python3 q7test/tusc_xm/tusc_xm.py --help

Run from the repository root. Output: JSON lines on stdout (redirect to tusc_xm/*.out). Tables: S. Tomokiyo,
Cryptiana guicciardini.htm (after Speziali 1955, Monts de Savasse 1997). No reading, no key edit.
"""
import argparse, json, random, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'tools'))
import judge_plaintext as jp
import key_crossmatch as kx

FOLDER = ROOT / 'ciphers/fr3982-nevers-toscana-1592'
KEYS = {'T1': ROOT / 'ciphers/_keys/tuscany-guicciardini/key_tomokiyo_guicciardini1.tsv',
        'T2': ROOT / 'ciphers/_keys/tuscany-guicciardini/key_tomokiyo_guicciardini2.tsv'}
HELD_OUT = 'lettereinedited01cibrgoog.txt'
SUBST = {'j': 'i', 'k': 'c', 'w': 'u', 'v': 'u', 'x': 's', 'y': 'i', 'z': 's'}


def load_key(path):
    key = {}
    for ln in path.read_text(encoding='utf-8').splitlines():
        if not ln or ln.startswith('#') or ln.startswith('value\t'):
            continue
        f = ln.split('\t')
        key[f[0]] = {'value': f[1]}
    return key


def target_digits():
    out = []
    for ln in (FOLDER / 'ciphertext.tsv').read_text().splitlines():
        if ln.startswith('f25_L'):
            out.append(ln.split('\t')[1].replace('?', ''))
    return ''.join(out)


def frames(d):
    return [[d[i:i + 2] for i in range(o, len(d) - 1, 2)] for o in (0, 1)]


def tscore(key, fr, model):
    best = -9.9
    for signs in fr:
        t, _ = kx.decode_with(key, signs)
        s = model.score(t) if t.strip() else -9.9
        best = max(best, s)
    return best


def p99(xs):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(0.99 * len(xs)))]


def test(key, d, model, n_key, n_order, seed):
    fr = frames(d)
    T = tscore(key, fr, model)
    rnd = random.Random(seed)
    nk = [tscore(kx.shuffled_key_by_class(key, rnd), fr, model) for _ in range(n_key)]
    no = []
    for _ in range(n_order):
        fs = [list(f) for f in fr]
        for f in fs:
            rnd.shuffle(f)
        no.append(tscore(key, fs, model))
    k = sum(1 for x in nk if x >= T)
    p = (1 + k) / (1 + n_key)
    o = p99(no)
    return dict(T=round(T, 4), p_key=round(p, 4), null_key_max=round(max(nk), 4), order_p99=round(o, 4),
                cov_f0=round(kx.coverage_of(key, fr[0]), 3), cov_f1=round(kx.coverage_of(key, fr[1]), 3)), p, T > o


def model_and_plain():
    files = sorted((ROOT / 'tools/data/it16').glob('*.txt'))
    train = [f.read_text(encoding='utf-8', errors='replace') for f in files if f.name != HELD_OUT]
    plain = jp.fold((ROOT / 'tools/data/it16' / HELD_OUT).read_text(encoding='utf-8', errors='replace'))
    return jp.NgramModel(train), plain


def enc_table(key, singles):
    """meaning (folded alternative) -> list of codes; two-figure codes only unless singles."""
    m = {}
    for c, row in key.items():
        if len(c) == 1 and not singles:
            continue
        for alt in row['value'].split('|'):
            a = jp.fold(alt)
            if a:
                m.setdefault(a, []).append(c)
    return m


def encipher(plain, start, table, rnd, ndig=260):
    letters = set(k for k in table if len(k) == 1)
    out, i = '', start
    while len(out) < ndig and i < len(plain):
        ch = plain[i]
        if ch not in letters:
            ch = SUBST.get(ch, ch)
        syl = [s for s in table if len(s) > 1 and plain.startswith(s, i)]
        if syl and rnd.random() < 0.5:
            s = rnd.choice(syl)
            out += rnd.choice(table[s]); i += len(s); continue
        if ch in table:
            out += rnd.choice(table[ch])
        i += 1
    return out[:ndig]


def corrupt(d, rate, rnd, eight_loss=False):
    if eight_loss:
        d = ''.join(rnd.choice(['6', '3', '01', '']) if c == '8' else c for c in d)
    out = []
    for c in d:
        if rnd.random() < rate:
            r = rnd.random() * 38
            if r < 19:
                out.append(rnd.choice('0123456789'))
            elif r < 31:
                out.append(c); out.append(rnd.choice('0123456789'))
            # else deletion
        else:
            out.append(c)
    return ''.join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('mode', choices=['target', 'power'])
    ap.add_argument('--n', type=int, default=100)
    a = ap.parse_args()
    model, plain = model_and_plain()
    keys = {k: load_key(p) for k, p in KEYS.items()}
    if a.mode == 'target':
        d = target_digits()
        for name, key in keys.items():
            res, p, ok_o = test(key, d, model, 1000, 200, 0)
            res.update(table=name, digits=len(d), verdict='PASS' if (p <= 0.005 and ok_o) else 'FAIL')
            print(json.dumps(res), flush=True)
        return
    conds = [('C0', 0.0, False), ('C1', 0.115, False), ('C2', 0.160, False), ('C3', 0.07, True)]
    variants = [('T1', 'T1', False), ('T2a', 'T2', False), ('T2b', 'T2', True)]
    for vname, kname, singles in variants:
        table = enc_table(keys[kname], singles)
        for cname, rate, el in conds:
            rnd = random.Random(f"{vname}-{cname}")
            passes = 0
            for t in range(a.n):
                start = rnd.randrange(0, len(plain) - 2000)
                d = corrupt(encipher(plain, start, table, rnd), rate, rnd, el)
                _, p, ok_o = test(keys[kname], d, model, 200, 50, t)
                passes += (p <= 1 / 201 + 1e-9 and ok_o)
            print(json.dumps(dict(variant=vname, cond=cname, rate=rate, eight_loss=el, n=a.n,
                                  power=round(passes / a.n, 3))), flush=True)
    # specificity: cross-table synthetics at C0
    for enc_k, sc_k in (('T1', 'T2'), ('T2', 'T1')):
        table = enc_table(keys[enc_k], enc_k == 'T2')
        rnd = random.Random(7)
        fp = 0
        for t in range(a.n):
            d = encipher(plain, rnd.randrange(0, len(plain) - 2000), table, rnd)
            _, p, ok_o = test(keys[sc_k], d, model, 200, 50, t)
            fp += (p <= 1 / 201 + 1e-9 and ok_o)
        print(json.dumps(dict(specificity=f'enc {enc_k} scored {sc_k}', n=a.n, false_pass=round(fp / a.n, 3))), flush=True)


if __name__ == '__main__':
    main()
