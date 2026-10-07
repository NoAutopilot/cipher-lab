#!/usr/bin/env python3
"""D07-NOXREAD (7 Oct 2026, PREREG-D07NOXREAD.md): reader transcription of c510 L05-L14 decoded with Tomokiyo's key
(letter part of each id, W: words as their table word) and scored by exact LCS ratio against Dupuy 521 221R ff.
Controls: (k) key shuffle 1000, (o) decode letter-order shuffle 1000, (c) Dupuy window word-shuffle 10, (w) wrong Dupuy
windows at offsets 1500, 2500, ... Usage: noxread510.py CT.tsv [--hash e|o] [--out results.json] [--check]."""
import sys, os, re, json, math, random, argparse, importlib.util
D = os.path.dirname(os.path.abspath(__file__)) + '/..'
src = open(f'{D}/scripts/test0.py').read().replace('\nmain()\n', '\n')
t0 = {'__file__': f'{D}/scripts/test0.py'}; exec(compile(src, 'test0', 'exec'), t0)
norm, lcs_len = t0['norm'], t0['lcs_len']
def R(a, b): return 2 * lcs_len(a, b) / (len(a) + len(b)) if (a or b) else 1.0

def dupuy():
    T = f'{D}/run2'
    pages = [l.rstrip('\n').split('\t') for l in open(f'{T}/nxdup/dupuy221_226_norm.txt') if not l.startswith('#')]
    txt = ' '.join(p[1] for p in pages)
    a = txt.index('la reception d icelle que') + len('la reception d icelle que')
    b0 = txt.index('sire quelques jours avant'); b1 = txt.index('me mander', b0) + len('me mander')
    return (txt[a:b0] + ' ' + txt[b1:]).strip()

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('ct'); ap.add_argument('--hash', choices=['e', 'o'], default='e')
    ap.add_argument('--out'); ap.add_argument('--check', action='store_true'); a = ap.parse_args()
    toks = []
    for ln in open(a.ct):
        if ln.startswith('#') or not ln.strip(): continue
        p = ln.rstrip('\n').split('\t'); toks += [t.split('{')[0].rstrip('?') or '?' for t in (p[1].split() if len(p) > 1 else [])]
    toks = [('e2' if a.hash == 'e' else 'o1') if t == 'o1/e2' else t for t in toks]
    ids = sorted({t for t in toks if re.fullmatch(r'[a-z]\d+', t)})
    key = {t: t[0] for t in ids}
    dec = lambda k: norm(''.join(t[2:] if t.startswith('W:') else k.get(t, '') for t in toks))
    d = dec(key); n = len(d)
    dw = dupuy(); dl = norm(dw); L = math.ceil(1.2 * n); ref = dl[:L]
    real = R(d, ref)
    rng = random.Random(16142); vals = [key[t] for t in ids]
    k = []
    for _ in range(1000):
        v = vals[:]; rng.shuffle(v); k.append(R(dec(dict(zip(ids, v))), ref))
    o = []
    for _ in range(1000):
        s = list(d); rng.shuffle(s); o.append(R(''.join(s), ref))
    # window words: words of dw whose letters fall in the first L letters
    words, acc = [], 0
    for w in dw.split():
        if acc >= L: break
        words.append(w); acc += len(norm(w))
    c = []
    for _ in range(10):
        w = words[:]; rng.shuffle(w); c.append(R(d, norm(''.join(w))[:L]))
    ww = [R(d, dl[s:s + L]) for s in range(1500, len(dl) - L + 1, 1000)]
    p99 = lambda x: sorted(x)[int(0.99 * len(x)) - 1]
    res = {'hash': a.hash, 'tokens': len(toks), 'unread': toks.count('?'), 'letter_ids': len(ids), 'decoded_letters': n,
           'window_letters': L, 'real': round(real, 4),
           'k_mean': round(sum(k)/len(k), 4), 'k_p99': round(p99(k), 4), 'k_max': round(max(k), 4),
           'o_mean': round(sum(o)/len(o), 4), 'o_p99': round(p99(o), 4), 'o_max': round(max(o), 4),
           'c_max': round(max(c), 4), 'w_n': len(ww), 'w_max': round(max(ww), 4), 'w_mean': round(sum(ww)/len(ww), 4)}
    res['PASS'] = real > res['k_p99'] and real > res['o_p99'] and real > res['c_max'] and real > res['w_max']
    res['decode'] = d
    if a.check:
        if json.load(open(a.out)) != res: print('STALE'); sys.exit(1)
        print('OK'); return
    if a.out: json.dump(res, open(a.out, 'w'), indent=1)
    print(json.dumps({x: y for x, y in res.items() if x != 'decode'}))
main()
