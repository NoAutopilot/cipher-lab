#!/usr/bin/env python3
"""Code 15 (BnF Espagnol 144 f.22v, v04) from the key's side. Read-only on the target's committed files.

1. key structure (ours + Bourdeau's key.tsv): values per letter, value ranges, the even/odd series;
2. every occurrence of 15 with decoded context;
3. letter counts in the cipher runs vs es17c7 expectation (under-represented / unassigned letters);
4. candidate values for 15 scored on the WHOLE decoded cipher stream (all runs) with an order-5 letter model
   trained on es17c7 tomes I-VI (tome VII held out for the control), under three variants:
   A as transcribed; B v04:11 32->31 (n->i, one adjacent-value slip); C = B plus the best 0-2 letter fill
   at the trimmed edge after v04:19 (every candidate gets its own best fill);
5. matched known-answer control (rule 3): held-out tome VII, a letter occurring twice inside ~a line's span,
   both occurrences masked, contexts cut to the target's (the second occurrence's right context cut to the
   line end plus a 0-2 letter gap, one random adjacent substitution near the first), rank of the true letter
   among the same candidates; per-letter breakdown, with z/x reported separately.
Usage: python3 key15.py [--trials 3000] [--seed 1]
"""
import argparse, collections, gzip, math, random, re, sys, unicodedata, json, os
T = '/home/user/cipher-lab/ciphers/espagnol142-mercy-1648'
B = '/home/user/cipher-lab/sources/cyphersolver/2026-10-01/mercy1648'
D = '/home/user/cipher-lab/tools/data/es17c7'
OUT = os.path.dirname(os.path.abspath(__file__))
ALPH = 'abcdefghilmnopqrstuxyz'          # cipher plaintext alphabet (j->i, v->u, n~ -> n, k->c, w->u)
CANDS = list(ALPH)

def fold(s):
    s = s.lower().replace('ñ', 'n')
    s = ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
    s = s.replace('j', 'i').replace('v', 'u').replace('w', 'u').replace('k', 'c')
    return re.sub('[^a-z]', '', s)

def tsv(p):
    rows = [l.rstrip('\n').split('\t') for l in open(p, encoding='utf-8') if l.strip() and not l.startswith('#')]
    return rows[0], rows[1:]

def load_runs():
    _, ct = tsv(f'{T}/ciphertext.tsv')
    _, rt = tsv(f'{T}/reading_tokens.tsv')
    val = {(r[0], r[1]): r[4] for r in rt}
    runs, cur = [], []
    for r in ct:
        line, pos, sign = r[0], r[1], r[2]
        if sign.startswith('[PLAIN') or sign == '[MARK:box]':
            if cur: runs.append(cur); cur = []
            continue
        cur.append((line, int(pos), sign, val.get((line, pos), '?')))
    if cur: runs.append(cur)
    return runs

class LM:
    def __init__(self, text, n=5):
        self.n = n; self.c = [collections.Counter() for _ in range(n + 1)]
        for k in range(1, n + 1):
            c = self.c[k]
            for i in range(len(text) - k + 1): c[text[i:i + k]] += 1
        self.V = len(ALPH)
    def lp(self, ctx, ch):   # interpolated (stupid-backoff-like, normalised by add-0.1 at each order) log prob
        ctx = ctx[-(self.n - 1):]
        p = 0.0; w = 1.0; lam = 0.0
        # simple Jelinek-Mercer with fixed weights, highest order first
        ws = [0.55, 0.25, 0.12, 0.05, 0.03][: len(ctx) + 1]
        tot = 0.0
        for j, wt in enumerate(ws):
            h = ctx[j:] if j < len(ctx) else ''
            k = len(h)
            num = self.c[k + 1][h + ch]
            den = self.c[k][h] if k else sum(self.c[1].values())
            tot += wt * ((num + 0.01) / (den + 0.01 * self.V))
        return math.log(tot / sum(ws))
    def score(self, s):
        return sum(self.lp(s[max(0, i - self.n + 1):i], s[i]) for i in range(len(s)))

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--trials', type=int, default=3000); ap.add_argument('--seed', type=int, default=1)
    a = ap.parse_args(); rnd = random.Random(a.seed)
    out = {}
    # ---- 1. key structure
    _, ours = tsv(f'{T}/key.tsv'); _, bour = tsv(f'{B}/key.tsv')
    ok = {r[0]: r[1] for r in ours if r[0].isdigit()}; bk = {r[0]: r[1] for r in bour if r[0].isdigit()}
    runs = load_runs()
    counts = collections.Counter(t[2] for run in runs for t in run)
    print('# 1. key, value -> letter (ours / Bourdeau), count in 529-token stream')
    for v in range(1, 36):
        s = str(v); print(f'{v:>3} {ok.get(s, "-"):>2} / {bk.get(s, "-"):>2}  n={counts.get(s, 0)}  {"even" if v % 2 == 0 else "odd"}')
    byl = collections.defaultdict(list)
    for v, l in ok.items(): byl[l].append(int(v))
    print('\n# per letter (ours): values')
    for l in sorted(byl): print(f'  {l}: {sorted(byl[l])}  tokens={sum(counts.get(str(x),0) for x in byl[l])}')
    print('  unassigned letters of', ALPH, ':', [c for c in ALPH if c not in byl])
    print('  unused values 1-35:', [v for v in range(1, 36) if str(v) not in ok])
    print('  even 10-34:', ''.join(ok.get(str(v), '?') for v in range(10, 35, 2)), '| 2-8:', ''.join(ok.get(str(v), '?') for v in range(2, 9)),
          '| odd 9-33:', ' '.join(f'{v}{ok.get(str(v),"?")}' for v in range(9, 34, 2)))
    # ---- 2. occurrences of 15
    flat = [t for run in runs for t in run]
    print('\n# 2. occurrences of 15 (decoded context; 15 shown as [15]; | = run boundary)')
    for ri, run in enumerate(runs):
        for i, t in enumerate(run):
            if t[2] == '15':
                L = ''.join(x[3] for x in run[max(0, i - 15):i]); R = ''.join(x[3] for x in run[i + 1:i + 16])
                print(f'  {t[0]}:{t[1]}  ...{L}[15]{R}...   (run {ri}, end-of-run={i == len(run) - 1})')
    # ---- 3. letter frequencies
    corpus = {}
    for f in sorted(os.listdir(D)):
        if f.endswith('.txt.gz'): corpus[f] = fold(gzip.open(f'{D}/{f}', 'rt', encoding='utf-8', errors='ignore').read())
    allc = ''.join(corpus.values()); cf = collections.Counter(allc); N = len(allc)
    dec = ''.join(t[3] for t in flat if t[2] != '15' and t[3] not in ('?', '_'))
    df = collections.Counter(dec); n = len(dec)
    print(f'\n# 3. letters in cipher runs (n={n}, 15 excluded) vs es17c7 expectation')
    print('  letter obs  exp   (obs-exp)/sqrt(exp)')
    for c in ALPH:
        e = cf[c] / N * n; print(f'  {c}  {df[c]:>4} {e:6.1f}  {(df[c]-e)/math.sqrt(e) if e else 0:+.2f}')
    # ---- 4. candidate scoring on the whole stream
    train = ''.join(v for k, v in corpus.items() if '19' not in k); held = corpus['memorialhistri19realuoft.txt.gz']
    lm = LM(train)
    def stream(fill15, slip=False, edge=''):
        segs = []
        for run in runs:
            s = ''
            for t in run:
                v = t[3]
                if (t[0], t[1]) == ('v04', 11) and slip: v = 'i'
                if t[2] == '15': v = fill15
                if v in ('_',): v = ''
                s += v
                if (t[0], t[1]) == ('v04', 19): s += edge
            segs.append(s)
        return segs
    def total(segs): return sum(lm.score(s) for s in segs)
    print('\n# 4. whole-stream log-likelihood by candidate (higher is better), delta vs best in each variant')
    res = {}
    fills = [''] + list(ALPH) + [x + y for x in ALPH for y in ALPH]
    for var in ('A', 'B', 'C'):
        sc = {}
        for c in CANDS + ['']:
            if var == 'C':
                best = max(((total(stream(c, True, e)), e) for e in fills), key=lambda z: z[0]); sc[c or 'null'] = best
            else:
                sc[c or 'null'] = (total(stream(c, var == 'B')), '')
        bestv = max(v[0] for v in sc.values())
        rk = sorted(sc.items(), key=lambda kv: -kv[1][0])
        res[var] = [(k, round(v[0] - bestv, 2), v[1]) for k, v in rk]
        print(f'  {var}: ' + '  '.join(f'{k}{"+" + e if e else ""}:{d:+.1f}' for k, d, e in res[var][:8]))
        for want in ('z', 'n', 'c', 'x'):
            r = [k for k, _, _ in res[var]].index(want) + 1; print(f'     rank of {want}: {r}/{len(res[var])}  delta {dict((k, d) for k, d, _ in res[var])[want]:+.2f}')
    # per-occurrence decomposition under C (each occurrence scored with the other fixed at the same candidate is what C does;
    # here: occurrence 1 alone (occ2 masked as null) and occurrence 2 alone)
    print('\n# 4b. each occurrence alone (variant B/C; the other 15 held at null)')
    for which in (1, 2):
        sc = {}
        for c in CANDS:
            def st(e):
                segs = []
                for run in runs:
                    s = ''
                    for t in run:
                        v = t[3]
                        if (t[0], t[1]) == ('v04', 11): v = 'i'
                        if t[2] == '15': v = c if ((t[1] == 9) == (which == 1)) else ''
                        if v == '_': v = ''
                        s += v
                        if (t[0], t[1]) == ('v04', 19): s += e
                    segs.append(s)
                return total(segs)
            sc[c] = max((st(e), e) for e in (fills if which == 2 else ['']))
        bestv = max(v[0] for v in sc.values()); rk = sorted(sc.items(), key=lambda kv: -kv[1][0])
        print(f'  occ{which} ({"v04:9" if which == 1 else "v04:19"}): ' + '  '.join(f'{k}{"+" + v[1] if v[1] else ""}:{v[0]-bestv:+.1f}' for k, v in rk[:8]))
    # ---- 5. matched control on held-out tome VII
    # target shape: occ1 has 8 letters left context on its line run (+ previous lines), right context 10 letters to occ2;
    # occ2 at the line end, right context lost (0-2 letters) then the next line continues. One slip 2 letters after occ1.
    print(f'\n# 5. control: held-out tome VII, {a.trials} trials, two occurrences of one letter 10 apart, masked; slip at occ1+2;')
    print('#    a 1-2 letter gap after occ2 (lost edge, filled best-of by each candidate); context 25 letters each side')
    hits = collections.Counter(); tri = collections.Counter(); top3 = collections.Counter(); Ltrials = []
    per = max(1, a.trials // len(ALPH))
    FILL2 = [''] + list(ALPH) + [x + y for x in 'aeiounrsltcdg' for y in 'aeiounrsltcdg']
    for ch in ALPH:
        cand = [i for i in range(40, len(held) - 60) if held[i] == ch and ch in held[i + 6:i + 16]]
        rnd.shuffle(cand)
        for i in cand[:per]:
            j = held.index(ch, i + 6, i + 16); gap = rnd.choice([1, 2])
            left = held[i - 25:i]; mid = list(held[i + 1:j]); right = held[j + 1 + gap:j + 1 + gap + 25]
            if len(mid) > 2: mid[1] = rnd.choice([c for c in ALPH if c != mid[1]])   # one slip, as v04:11
            mid = ''.join(mid)
            scores = {}
            for c in CANDS:
                pre = left + c + mid + c
                scores[c] = max(lm.score(pre + e + right) for e in FILL2 if len(e) <= gap)
            rk = sorted(scores, key=lambda k: -scores[k]); r = rk.index(ch) + 1
            tri[ch] += 1; hits[ch] += (r == 1); top3[ch] += (r <= 3); Ltrials.append((ch, r))
    T_ = sum(tri.values()); H = sum(hits.values()); H3 = sum(top3.values())
    wf = sum(cf[c] / N * hits[c] / tri[c] for c in ALPH if tri[c])
    print(f'  stratified ({per}/letter): top-1 {H}/{T_} = {H/T_:.3f}; top-3 {H3/T_:.3f}; frequency-weighted top-1 {wf:.3f}; chance top-1 = {1/len(CANDS):.3f}')
    for c in ALPH:
        if tri[c]: print(f'   {c}: n={tri[c]:>4} top1 {hits[c]/tri[c]:.3f} top3 {top3[c]/tri[c]:.3f}  rank>=13 {sum(1 for x, r in Ltrials if x == c and r >= 13)/tri[c]:.3f}')
    print(f'  all letters: share of true letters ranked >=13 (z on the target, variant C): {sum(1 for _, r in Ltrials if r >= 13)/T_:.3f}')
    json.dump({'variants': res, 'control': {'trials': T_, 'top1': H / T_, 'top3': H3 / T_,
               'per_letter': {c: [tri[c], hits[c], top3[c]] for c in ALPH}, 'ranks': Ltrials}}, open(f'{OUT}/key15_results.json', 'w'), indent=1)

if __name__ == '__main__':
    main()
