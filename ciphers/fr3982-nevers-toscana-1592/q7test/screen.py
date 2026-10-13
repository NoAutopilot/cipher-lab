#!/usr/bin/env python3
"""BNF-Q7-SCREEN: decode-level, order-sensitive key screen for a continuous digit cipher (PREREG-Q7-SCREEN.md).

Exact Viterbi (vit.c, compiled on first use into the scratch dir given by --build) over digit positions x 4-gram
context; every key code matching at a position is a transition, polyphones expanded; NULL -2.0, one-digit skip -3.0
(log10). Statistic S = LM log10-likelihood per letter on the best path. Nulls: (a) key meanings shuffled within class
(letters/words; nulls kept), (b) target digit order shuffled.

Key files: TSV `code<TAB>meaning` (q7test/key_no46_codes.tsv, key_no70_codes.tsv) or the 4-column key_no62.tsv
(value, meaning, grade, source). Meaning NULL or '-' = null; one letter, 'qu', 'et' = letter class; else word class
(folded letters). A code listed twice is a polyphone.

Usage:
  screen.py target --key KEYFILE [--lang it|fr] [--nulls 1000] [--seed 25]      f.25 (ciphertext.tsv, ? removed)
  screen.py validate --key KEYFILE [--texts 200] [--levels 0,0.05,0.10,0.15] [--nulls 100] [--small 50]
  screen.py specificity --enc-key K1 --key K2 [--texts 100] [--rate 0.10] [--nulls 100]
Outputs one JSON line per result on stdout. Seeds fixed; runs are deterministic for a given worker count.
"""
import argparse, ctypes, gzip, json, os, random, subprocess, sys, unicodedata
import numpy as np
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(T))
DATA = os.path.join(ROOT, 'tools', 'data')
V = 26; NULL_PEN = -2.0; SKIP_PEN = -3.0; BEAM = float(os.environ.get('Q7_BEAM', '6.0'))
IT_FILES = ['bub_gb_laRnTtJmsDAC.txt.gz', 'bub_gb_ZJMxff7r4LUC.txt.gz', 'gri_33125010469852.txt.gz',
            'letterediprincip01char.txt.gz', 'letterediprincip02char.txt.gz']   # letterediprincip03char held out
HELDOUT = os.path.join(DATA, 'it16dip', 'letterediprincip03char.txt.gz')
FR_FILES = ['lettresdecatheri01cathuoft_djvu.txt.gz', 'lettresdecatheri02cathuoft_djvu.txt.gz', 'lettresindites00marg_djvu.txt.gz']

def fold(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if 'a' <= c <= 'z')

def build_lp(lang, cache):
    p = os.path.join(cache, f'lp_{lang}.npy')
    if os.path.exists(p): return np.load(p)
    files = [os.path.join(DATA, 'it16dip', f) for f in IT_FILES] if lang == 'it' else [os.path.join(DATA, 'fr16', f) for f in FR_FILES]
    c4 = np.zeros(V**4, dtype=np.float64)
    for f in files:
        a = np.frombuffer(fold(gzip.open(f, 'rt', encoding='utf-8', errors='replace').read()).encode(), dtype=np.uint8).astype(np.int64) - 97
        idx = ((a[:-3]*V + a[1:-2])*V + a[2:-1])*V + a[3:]
        c4 += np.bincount(idx, minlength=V**4)
    c4 = c4.reshape(V**3, V); c3 = c4.sum(axis=1, keepdims=True); k = 0.01
    lp = np.log10((c4 + k)/(c3 + V*k)).ravel(); np.save(p, lp); return lp

def load_key(path):
    """-> list of entries (code, cls, letters); cls in L/W/N."""
    ent = []
    for line in open(path, encoding='utf-8'):
        r = line.rstrip('\n').split('\t')
        if not r or not r[0] or r[0].startswith('#') or r[0] == 'value' or len(r) < 2: continue
        code, m = r[0].strip(), r[1].strip()
        if not code.isdigit(): continue
        if m in ('NULL', '-', ''): ent.append((code, 'N', '')); continue
        if len(r) >= 3 and len(code) <= 2:          # key_no62.tsv alphabet row
            f = fold(m.split(' ')[0])
            if f in ('bc', 'fg'): ent += [(code, 'L', f[0]), (code, 'L', f[1])]
            elif f in ('qu', 'et'): ent.append((code, 'L', f))
            else: ent.append((code, 'L', f[0]))
            continue
        f = fold(m)
        if len(f) == 1 or f == 'qu': ent.append((code, 'L', f))
        elif f: ent.append((code, 'W', f))
    return ent

def shuffle_key(ent, rng):
    out = list(ent)
    for cls in ('L', 'W'):
        ix = [i for i, e in enumerate(ent) if e[1] == cls]; vals = [ent[i][2] for i in ix]; rng.shuffle(vals)
        for i, v in zip(ix, vals): out[i] = (ent[i][0], cls, v)
    return out

_LIB = None; _LP = {}
def _init(build, langs):
    global _LIB
    so = os.path.join(build, 'vit.so')
    if not os.path.exists(so):
        subprocess.check_call(['gcc', '-O3', '-shared', '-fPIC', '-o', so, os.path.join(HERE, 'vit.c')])
    _LIB = ctypes.CDLL(so); _LIB.viterbi.restype = ctypes.c_double
    for l in langs: _LP[l] = np.ascontiguousarray(build_lp(l, build))

def decode(s, ent, lang, want_path=False):
    """-> (S per-letter, n letters, total score, path letters or None)"""
    N = len(s); codes = {}
    for c, cls, v in ent: codes.setdefault(c, []).append(v if cls != 'N' else None)
    mlist, mid = [], {}
    tr_off, tr_len, tr_m, trinfo = [0], [], [], []
    lens = sorted({len(c) for c in codes})
    for i in range(N):
        for L in lens:
            c = s[i:i+L]
            if len(c) == L and c in codes:
                for v in codes[c]:
                    if v is None: m = -1
                    else:
                        if v not in mid: mid[v] = len(mlist); mlist.append(v)
                        m = mid[v]
                    tr_len.append(L); tr_m.append(m); trinfo.append((c, v))
        tr_len.append(1); tr_m.append(-2); trinfo.append((s[i], '~'))
        tr_off.append(len(tr_len))
    m_off = [0]; m_let = []
    for v in mlist: m_let += [ord(ch)-97 for ch in v]; m_off.append(len(m_let))
    A = lambda x: np.ascontiguousarray(np.array(x if x else [0], dtype=np.int32))
    a_off, a_len, a_m, a_moff, a_mlet = A(tr_off), A(tr_len), A(tr_m), A(m_off), A(m_let)
    cnt = ctypes.c_int(0); lm = ctypes.c_double(0); npath = ctypes.c_int(0)
    path = np.zeros(N+1, dtype=np.int32) if want_path else None
    P = lambda a: a.ctypes.data_as(ctypes.c_void_p)
    tot = _LIB.viterbi(ctypes.c_int(N), P(a_off), P(a_len), P(a_m), P(a_moff), P(a_mlet), P(_LP[lang]),
                       ctypes.c_double(NULL_PEN), ctypes.c_double(SKIP_PEN), ctypes.c_double(BEAM), ctypes.byref(cnt), ctypes.byref(lm),
                       P(path) if want_path else None, ctypes.byref(npath))
    S = lm.value/cnt.value if cnt.value else -9.9
    steps = [trinfo[t] for t in reversed(path[:npath.value])] if want_path else None
    return S, cnt.value, tot, steps

def _job(args):
    s, ent, lang, nk, nd, seed = args
    rng = random.Random(seed)
    obs = decode(s, ent, lang)[0]
    na = [decode(s, shuffle_key(ent, rng), lang)[0] for _ in range(nk)]
    nb = []
    for _ in range(nd):
        l = list(s); rng.shuffle(l); nb.append(decode(''.join(l), ent, lang)[0])
    return obs, na, nb

# ---------- synthetic texts ----------
def windows(rng, n, nwords=300):
    chunks = [l.split() for l in gzip.open(HELDOUT, 'rt', encoding='utf-8', errors='replace')]
    chunks = [c for c in chunks if len(c) > nwords + 50]
    out = []
    for _ in range(n):
        c = rng.choice(chunks); st = rng.randrange(0, len(c) - nwords); out.append([fold(w) for w in c[st:st+nwords] if fold(w)])
    return out

def encipher(words, ent, rng, ndig, null_share=0.03):
    let, wrd, nul = {}, {}, [e[0] for e in ent if e[1] == 'N']
    for c, cls, v in ent:
        if cls == 'L': let.setdefault(v, []).append(c)
        elif cls == 'W': wrd.setdefault(v, c)
    out = []
    for w in words:
        if w in wrd: toks = [wrd[w]]
        else:
            toks = []; i = 0
            while i < len(w):
                if w[i:i+2] == 'qu' and 'qu' in let: toks.append(rng.choice(let['qu'])); i += 2; continue
                if w[i] in let: toks.append(rng.choice(let[w[i]]))
                i += 1
        for t in toks:
            if nul and rng.random() < null_share: out.append(rng.choice(nul))
            out.append(t)
        if sum(map(len, out)) >= ndig + 20: break
    return ''.join(out)[:ndig]

def corrupt(s, rate, rng):
    out = []
    for x in s:
        r = rng.random()
        if r < rate*2/3: out.append(rng.choice([d for d in '0123456789' if d != x]))
        elif r < rate*5/6: pass
        elif r < rate: out.append(x); out.append(rng.choice('0123456789'))
        else: out.append(x)
    return ''.join(out)

def load_target():
    s = ''
    for line in open(os.path.join(T, 'ciphertext.tsv')):
        r = line.rstrip('\n').split('\t')
        if r[0].startswith('f25_'): s += r[1]
    return s.replace('?', '')

def detect(obs, na, nb):
    return obs > max(na) and obs > max(nb)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('mode', choices=['target', 'validate', 'specificity'])
    ap.add_argument('--key', required=True); ap.add_argument('--enc-key')
    ap.add_argument('--lang', default='it', choices=['it', 'fr'])
    ap.add_argument('--nulls', type=int); ap.add_argument('--seed', type=int)
    ap.add_argument('--texts', type=int); ap.add_argument('--levels', default='0,0.05,0.10,0.15')
    ap.add_argument('--small', type=int, default=0, help='texts for the non-10%% levels (0 = all)')
    ap.add_argument('--rate', type=float, default=0.10); ap.add_argument('--workers', type=int, default=4)
    ap.add_argument('--build', default=os.environ.get('Q7_BUILD', '/tmp/q7screen'))
    a = ap.parse_args(); os.makedirs(a.build, exist_ok=True)
    ent = load_key(a.key); keyname = os.path.basename(a.key)
    _init(a.build, [a.lang])
    with Pool(a.workers, initializer=_init, initargs=(a.build, [a.lang])) as pool:
        if a.mode == 'target':
            s = load_target(); n = a.nulls or 1000; seed = 25 if a.seed is None else a.seed
            obs, n_let, tot, steps = decode(s, ent, a.lang, want_path=True)
            per = 50; jobs = [(s, ent, a.lang, per, per, seed*1000 + k) for k in range(n // per)]
            na, nb = [], []
            for _, x, y in pool.map(_job, jobs): na += x; nb += y
            pa = (1 + sum(x >= obs for x in na))/(1 + len(na)); pb = (1 + sum(x >= obs for x in nb))/(1 + len(nb))
            draft = ''.join(('[' + v + ']' if v not in (None, '~') and len(v) > 2 else (v if v not in (None, '~') else ('.' if v is None else '_'))) for c, v in steps)
            print(json.dumps(dict(mode='target', key=keyname, lang=a.lang, N=len(s), S=round(obs, 4), letters=n_let,
                  null_a_mean=round(float(np.mean(na)), 4), null_a_p99=round(float(np.percentile(na, 99)), 4),
                  null_b_mean=round(float(np.mean(nb)), 4), null_b_p99=round(float(np.percentile(nb, 99)), 4),
                  p_a=round(pa, 4), p_b=round(pb, 4), fit=(pa <= 0.01 and pb <= 0.01),
                  nulls=len(steps and [x for x in steps if x[1] is None]), skips=sum(1 for x in steps if x[1] == '~'),
                  draft=draft, steps=' '.join(f'{c}={v if v else "NULL"}' for c, v in steps))))
        elif a.mode == 'validate':
            n = a.texts or 200; nn = a.nulls or 100; seed = 46 if a.seed is None else a.seed
            rng = random.Random(seed); base = [encipher(w, ent, rng, 260) for w in windows(rng, n)]
            for lev in [float(x) for x in a.levels.split(',')]:
                m = n if (abs(lev - 0.10) < 1e-9 or not a.small) else a.small
                r2 = random.Random(seed*100 + int(lev*100))
                tx = [corrupt(s, lev, r2) for s in base[:m]]
                res = pool.map(_job, [(s, ent, 'it', nn, nn, seed*10000 + int(lev*100)*1000 + i) for i, s in enumerate(tx)])
                det = [detect(*r) for r in res]
                print(json.dumps(dict(mode='validate', key=keyname, level=lev, texts=m, nulls_each=nn, power=round(sum(det)/m, 3),
                      mean_S=round(float(np.mean([r[0] for r in res])), 4), mean_null_a=round(float(np.mean([np.mean(r[1]) for r in res])), 4),
                      mean_null_b=round(float(np.mean([np.mean(r[2]) for r in res])), 4),
                      det_a=round(sum(r[0] > max(r[1]) for r in res)/m, 3), det_b=round(sum(r[0] > max(r[2]) for r in res)/m, 3))), flush=True)
        else:
            n = a.texts or 100; nn = a.nulls or 100; seed = 70 if a.seed is None else a.seed
            enc = load_key(a.enc_key); rng = random.Random(seed)
            tx = [corrupt(encipher(w, enc, rng, 260), a.rate, rng) for w in windows(rng, n)]
            res = pool.map(_job, [(s, ent, 'it', nn, nn, seed*10000 + i) for i, s in enumerate(tx)])
            det = [detect(*r) for r in res]
            print(json.dumps(dict(mode='specificity', enc_key=os.path.basename(a.enc_key), key=keyname, rate=a.rate, texts=n,
                  false_detect=round(sum(det)/n, 3), mean_S=round(float(np.mean([r[0] for r in res])), 4))), flush=True)

if __name__ == '__main__':
    main()
