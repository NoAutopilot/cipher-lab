#!/usr/bin/env python3
"""SIG-4612C crib placement on 4612 v3 (9 Oct 2026, account 1, for LANE SIG-4). Pre-registration: PREREG.md beside this file
(pushed before any 4612 score). Slides fixed cribs over the numeral stream, keeps placements whose key_full letters agree on
>= 60% of the crib, derives the implied code reassignments, drops contradicted ones and scores the gain G in fr16 word share.

  python3 crib_place.py control     # (a) calibrate f on the 5811 cut, then 10 known-answer seeds; writes control.json
  python3 crib_place.py target      # refuses unless control.json passed; 4612 topical + (b) 200 off-topic + (c) 200 shuffles
  python3 crib_place.py selftest    # offline synthetic check (also tools/tests style: exit 0 = OK)
"""
import csv, json, os, random, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(T, 'ax4612tr')); sys.path.insert(0, os.path.join(T, '..', '..', 'tools'))
import word_share_check_v3 as WS

THETA = 0.60
TOPICAL = ('MASTRECHT MAESTRICHT MASTRICHT MASTRECH ENTREPRINSE ENTREPRISE STOCKEM STOKEM RIVIERE RIVIERES BATEAVLX BATEAVX '
           'CHEMIN BOMMEL INTELLIGENCES HOLLANDE LENNEMY ENNEMIS CAVALLERIE COMMISSION GOVVERNEVR PRINCES AFFAIRES INTENTION '
           'GVERRE').split()
F_GRID = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
N_CUT = 833


def load_key():
    rows = list(csv.DictReader(open(os.path.join(T, 'key_full.tsv'), encoding='utf-8'), delimiter='\t'))
    key, nulls = {}, set()
    for r in rows:
        try: c = int(r['code'])
        except ValueError: continue
        if r['value'] == 'NULL': nulls.add(c)
        elif 1 <= c <= 120 and len(r['value']) == 1: key[c] = WS.fold(r['value'])
    return key, nulls


def load_segments(path, nulls, max_tokens=None):
    segs, cur, n = [], [], 0
    for r in csv.DictReader(open(path, encoding='utf-8'), delimiter='\t'):
        s = r['sign'].strip()
        if s.isdigit() and int(s) in nulls: continue
        if s.isdigit() and 1 <= int(s) <= 120:
            cur.append(int(s)); n += 1
            if max_tokens and n >= max_tokens: break
        elif cur: segs.append(cur); cur = []
    if cur: segs.append(cur)
    return segs


def share(segs, key, words):
    c, t = WS.word_share(segs, key, words)
    return c / t if t else 0.0


def place(segs, key, cribs):
    """Steps 1-3 of PREREG: returns (kept placements, consistent reassignments {code: letter}, support counts)."""
    acc = []
    for ci, w in enumerate(cribs):
        L = len(w)
        for si, s in enumerate(segs):
            for i in range(len(s) - L + 1):
                win = s[i:i + L]; a = 0; seen = {}; ok = True
                for j, c in enumerate(win):
                    if seen.setdefault(c, w[j]) != w[j]: ok = False; break
                    a += key.get(c) == w[j]
                if ok and a / L >= THETA:
                    acc.append((-a / L, -L, ci, si, i, w))
    acc.sort()
    used = {}; kept = []
    for _, _, ci, si, i, w in acc:
        span = set(range(i, i + len(w)))
        if used.setdefault(si, set()) & span: continue
        used[si] |= span; kept.append((si, i, w))
    implied = {}; confirm = set(); support = {}
    for k, (si, i, w) in enumerate(kept):
        for j, c in enumerate(segs[si][i:i + len(w)]):
            if key.get(c) == w[j]: confirm.add(c)
            else:
                implied.setdefault(c, set()).add(w[j]); support.setdefault((c, w[j]), set()).add(k)
    cons = {c: next(iter(ls)) for c, ls in implied.items() if len(ls) == 1 and c not in confirm}
    multi = sum(1 for c, l in cons.items() if len(support[(c, l)]) >= 2)
    return kept, cons, multi


def gain(segs, key, cribs, words):
    kept, cons, multi = place(segs, key, cribs)
    k2 = dict(key); k2.update(cons)
    b = share(segs, key, words)
    return share(segs, k2, words) - b, kept, cons, multi, b


def fold_words(path, lines=None):
    t = open(path, encoding='utf-8').read().splitlines()
    if lines: t = [t[i - 1] for i in lines]
    t = [l for l in t if not l.startswith('#')]
    return [WS.fold(w) for w in re.findall(r"[A-Za-zÀ-ÿ]+", ' '.join(t))]


def draw(pool, lengths, rng):
    """One word per length, without replacement, nearest length if none left."""
    bylen = {}
    for w in sorted(set(pool)): bylen.setdefault(len(w), []).append(w)
    out = []
    for L in lengths:
        cands = [l for l in bylen if bylen[l]]
        best = min(cands, key=lambda l: (abs(l - L), l))
        w = rng.choice(bylen[best]); bylen[best].remove(w); out.append(w)
    return out


def perturb(key, codes, f, rng, alpha):
    ch = rng.sample(codes, round(f * len(codes))); out = dict(key)
    for c in ch: out[c] = rng.choice([l for l in alpha if l != key[c]])
    return out, set(ch)


def recoverable(segs, true_key, cribs, pert):
    out = set()
    for s in segs:
        txt = ''.join(true_key[c] for c in s)
        for w in cribs:
            for m in re.finditer('(?=%s)' % w, txt):
                out |= {c for c in s[m.start():m.start() + len(w)] if c in pert}
    return out


def lexicon():
    import french16_ngram as fr
    return {w for w in fr.load().words if len(w) >= 3}


def control():
    key, nulls = load_key(); words = lexicon(); alpha = sorted(set(key.values()))
    t_segs = load_segments(os.path.join(T, 'ciphertext_4612_v3.tsv'), nulls)
    base_t = share(t_segs, key, words)
    segs = load_segments(os.path.join(T, 'ciphertext_5811.tsv'), nulls, N_CUT)
    codes = sorted({c for s in segs for c in s if c in key})
    print(f'4612 v3 baseline word share under key_full (this segmenter): {base_t:.4f}; 5811 cut {sum(map(len, segs))} tokens, '
          f'{len(codes)} codes, true share {share(segs, key, words):.4f}', flush=True)
    calib = {}
    for f in F_GRID:
        v = [share(segs, perturb(key, codes, f, random.Random(9000 + s), alpha)[0], words) for s in range(20)]
        calib[f] = sum(v) / len(v); print(f'  calib f={f:.2f}: mean share {calib[f]:.4f}', flush=True)
    f = min(F_GRID, key=lambda x: (abs(calib[x] - base_t), x))
    pool = [w for w in fold_words(os.path.join(T, 'groen', 'groen_IV_CDLXXXIII.txt'), [162, 174]) if len(w) >= 6]
    lens = [len(w) for w in TOPICAL]
    rows = []
    for s in range(10):
        pk, pert = perturb(key, codes, f, random.Random(s), alpha)
        cribs = draw(pool, lens, random.Random(1000 + s))
        g, kept, cons, multi, b = gain(segs, pk, cribs, words)
        rec = sum(1 for c, l in cons.items() if c in pert and l == key[c])
        false = len(cons) - rec
        rcv = recoverable(segs, key, cribs, pert)
        hits = sum(1 for w in cribs if any(w in ''.join(key[c] for c in sg) for sg in segs))
        rows.append(dict(seed=s, perturbed=len(pert), cribs_in_cut=hits, kept=len(kept), consistent=len(cons), multi=multi,
                         recovered=rec, false=false, recoverable=len(rcv), base=round(b, 4), G=round(g, 4)))
        print('  seed', rows[-1], flush=True)
    R = sum(r['recovered'] for r in rows); RV = sum(r['recoverable'] for r in rows)
    recall = R / RV if RV else 0.0; mf = sum(r['false'] for r in rows) / 10; mg = sum(r['G'] for r in rows) / 10
    ok = RV > 0 and recall >= 0.50 and mf <= 2.0 and mg > 0
    res = dict(f=f, calib=calib, base_4612=base_t, rows=rows, pooled_recall=recall, mean_false=mf, mean_G=mg, PASS=ok)
    json.dump(res, open(os.path.join(HERE, 'control.json'), 'w'), indent=1)
    print(f'CONTROL (a): f={f} recall {R}/{RV}={recall:.3f} (>=0.50), mean false {mf:.1f} (<=2.0), mean G {mg:+.4f} (>0) -> '
          f'{"PASS" if ok else "FAIL (CONTROL BELOW GATE)"}')
    return ok


def p95(v):
    v = sorted(v); k = 0.95 * (len(v) - 1); lo = int(k)
    return v[lo] + (v[min(lo + 1, len(v) - 1)] - v[lo]) * (k - lo)


def target():
    c = json.load(open(os.path.join(HERE, 'control.json')))
    if not c['PASS']: print('CONTROL BELOW GATE: control.json did not pass; target not scored'); sys.exit(3)
    key, nulls = load_key(); words = lexicon()
    segs = load_segments(os.path.join(T, 'ciphertext_4612_v3.tsv'), nulls)
    g, kept, cons, multi, b = gain(segs, key, TOPICAL, words)
    print(f'TARGET topical: base {b:.4f} G {g:+.4f} kept {len(kept)} consistent {len(cons)} multi {multi}', flush=True)
    excl = set(fold_words(os.path.join(T, 'decipherment_7208.txt'))) | set(TOPICAL)
    pool = [w for p in ('decipherment_7205.txt', 'decipherment_4614.txt') for w in fold_words(os.path.join(T, p))
            if len(w) >= 6 and w not in excl]
    lens = [len(w) for w in TOPICAL]
    gb = [gain(segs, key, draw(pool, lens, random.Random(46120 + d)), words)[0] for d in range(200)]
    print(f'(b) off-topic: mean {sum(gb)/200:+.4f} p95 {p95(gb):+.4f} max {max(gb):+.4f}', flush=True)
    flat = [x for s in segs for x in s]; gc = []
    for k in range(200):
        r = random.Random(46220 + k); f2 = flat[:]; r.shuffle(f2); ss = []; p = 0
        for s in segs: ss.append(f2[p:p + len(s)]); p += len(s)
        gc.append(gain(ss, key, TOPICAL, words)[0])
    print(f'(c) shuffled: mean {sum(gc)/200:+.4f} p95 {p95(gc):+.4f} max {max(gc):+.4f}', flush=True)
    ok = g > p95(gb) and g > p95(gc)
    res = dict(base=b, G=g, kept=[(si, i, w, ''.join(key.get(x, '?') for x in segs[si][i:i + len(w)])) for si, i, w in kept],
               consistent={str(k): v for k, v in sorted(cons.items())}, multi=multi,
               b=dict(mean=sum(gb) / 200, p95=p95(gb), max=max(gb), values=gb),
               c=dict(mean=sum(gc) / 200, p95=p95(gc), max=max(gc), values=gc), PASS=ok)
    json.dump(res, open(os.path.join(HERE, 'target.json'), 'w'), indent=1)
    print(f'GATE: G {g:+.4f} > (b) p95 {p95(gb):+.4f} and > (c) p95 {p95(gc):+.4f} -> {"PASS" if ok else "FAIL"}')


def selftest():
    """Synthetic: a text containing a crib under a key with two planted errors must yield exactly those two reassignments."""
    key = {i + 1: ch for i, ch in enumerate('ABCDEFGHIKLMNOPQRSTVXYZ')}
    enc = {v: k for k, v in key.items()}
    segs = [[enc[ch] for ch in 'ZZQQMASTRICHTQQ']]
    bad = dict(key); bad[enc['S']] = 'X'; bad[enc['R']] = 'Y'
    kept, cons, multi = place(segs, bad, ['MASTRICHT'])
    assert kept == [(0, 4, 'MASTRICHT')], kept
    assert cons == {enc['S']: 'S', enc['R']: 'R'}, cons
    # contradiction: a second crib placed elsewhere confirming the code's wrong value cancels it
    segs2 = segs + [[enc['S'], enc['A'], enc['B'], enc['C'], enc['D']]]
    _, cons2, _ = place(segs2, bad, ['MASTRICHT', 'XABCD'])
    assert enc['S'] not in cons2 and cons2.get(enc['R']) == 'R', cons2
    # below threshold: a crib absent from the text places nothing
    assert place(segs, key, ['BOMMELX'])[0] == []
    assert p95(list(range(101))) == 95.0
    print('selftest OK')


if __name__ == '__main__':
    {'control': control, 'target': target, 'selftest': selftest}[sys.argv[1]]()
