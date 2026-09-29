"""Group H: the Copiale decipherment method (Knight, Megyesi & Schaefer 2011) as a blind, automated pipeline.
Steps (see SOURCES.md for what the paper did by hand and what is automated here):
 a  space/null class: context-vector clustering (predecessor+successor counts, cosine, average linkage, as in the
    paper's Fig. 4); every cluster whose token share lies in [LO,HI] is tried as the word-space class; the one whose
    gaps give the word-length curve closest (KL) to the languages' curves is kept; 'no space class' is also tried.
 b  homophone clusters: the same clustering on the remaining signs (reported; purity measured on controls).
 c  language screen: the C annealer (hsolve_h) under each language model; per-char log-likelihood of the solve
    minus that language's held-out real-text per-char LL (a solve that reads like the language closes the gap).
 d  deeper solve in the best languages (more restarts).
usage:
  python3 pipeline.py copiale --n 1200 --start 0 [--seed 1]       known-answer control on real Copiale tokens
  python3 pipeline.py tsv FILE.tsv [--skip _,MULTI,?]               a Debosnys settled draft (sign column)
  python3 pipeline.py sid c2|c1|FR-HOMO.c2 --keyout KEY.tsv          a text id read through score.py's own loader
Keys: space-class signs get an empty value (score.py reads them as nulls).
Output: JSON on stdout / --out; keys to --keyout (sign<TAB>value)."""
import argparse, json, math, os, random, struct, subprocess, sys, array, collections
HERE = os.path.dirname(os.path.abspath(__file__))
LANGS = ['de', 'en', 'fr', 'fr18', 'la', 'it', 'es', 'pt', 'nl', 'da', 'pl', 'lt']
A = 27
_lm = {}
def lm(lang, tag):
    k = (lang, tag)
    if k not in _lm:
        a = array.array('f'); a.frombytes(open(f'{HERE}/lm/{lang}.{tag}.bin', 'rb').read()); _lm[k] = a
    return _lm[k]
def ll_text(text, lang, tag):
    t = lm(lang, tag); idx = {c: i for i, c in enumerate('abcdefghijklmnopqrstuvwxyz ')}
    s = [idx[c] for c in text if c in idx]
    if tag == 'ns': s = [x for x in s if x != 26]
    tot = 0.0; pad = [26, 26, 26] + s
    for i in range(3, len(pad)):
        a, b, c, d = pad[i-3:i+1]; tot += t[((a*A+b)*A+c)*A+d]
    return tot / max(1, len(s))
_held = {}
def held_ll(lang, tag, n):
    k = (lang, tag, n)
    if k not in _held:
        txt = open(f'{HERE}/lm/{lang}.held.txt').read()
        vals = []
        for st in range(0, len(txt) - n, max(1, (len(txt) - n) // 10)):
            vals.append(ll_text(txt[st:st+n], lang, tag))
        _held[k] = sum(vals) / len(vals)
    return _held[k]
_wl = None
def wordlen_ref():
    global _wl
    if _wl is None:
        c = collections.Counter()
        for lang in LANGS:
            for w in open(f'{HERE}/lm/{lang}.held.txt').read().split(): c[min(len(w), 15)] += 1
        tot = sum(c.values()); _wl = [c[i] / tot for i in range(16)]
    return _wl
def cosine(u, v):
    num = sum(u[k] * v.get(k, 0) for k in u)
    du = math.sqrt(sum(x*x for x in u.values())); dv = math.sqrt(sum(x*x for x in v.values()))
    return num / (du * dv) if du and dv else 0.0
def cluster(seq, signs):
    """average-linkage agglomerative clustering on context vectors; returns list of merged clusters (sets)"""
    vec = {s: collections.Counter() for s in signs}
    for i, s in enumerate(seq):
        if s not in vec: continue
        if i > 0: vec[s][('p', seq[i-1])] += 1
        if i + 1 < len(seq): vec[s][('n', seq[i+1])] += 1
    items = [s for s in signs if sum(vec[s].values()) > 0]
    sim = {}
    for i, a in enumerate(items):
        for b in items[i+1:]:
            sim[(a, b)] = sim[(b, a)] = cosine(vec[a], vec[b])
    clusters = {i: {s} for i, s in enumerate(items)}
    merges = []
    def csim(x, y):
        return sum(sim[(a, b)] for a in x for b in y) / (len(x) * len(y))
    link = {}
    keys = list(clusters)
    for i, a in enumerate(keys):
        for b in keys[i+1:]: link[(a, b)] = csim(clusters[a], clusters[b])
    nid = len(items)
    while len(clusters) > 1:
        (a, b), v = max(link.items(), key=lambda kv: kv[1])
        new = clusters.pop(a) | clusters.pop(b)
        link = {k: w for k, w in link.items() if a not in k and b not in k}
        for c in clusters: link[(c, nid)] = csim(clusters[c], new)
        clusters[nid] = new; merges.append((v, frozenset(new))); nid += 1
    return merges
def wl_kl(seq, space):
    lens = []; cur = 0; zero = 0
    for s in seq:
        if s in space:
            if cur == 0: zero += 1
            else: lens.append(min(cur, 15))
            cur = 0
        else: cur += 1
    if cur: lens.append(min(cur, 15))
    ref = wordlen_ref(); c = collections.Counter(lens); tot = len(lens) + zero
    if tot == 0: return 99
    p = [(zero + 0.5) / (tot + 8)] + [(c[i] + 0.5) / (tot + 8) for i in range(1, 16)]
    q = [1e-3] + [max(ref[i], 1e-4) for i in range(1, 16)]
    return sum(pi * math.log(pi / qi) for pi, qi in zip(p, q))
def step_a(seq, lo=0.08, hi=0.30):
    cnt = collections.Counter(seq); n = len(seq)
    signs = [s for s in cnt if cnt[s] >= 2]
    merges = cluster(seq, signs)
    cands = []
    seen = set()
    for v, cl in merges:
        share = sum(cnt[s] for s in cl) / n
        if lo <= share <= hi and cl not in seen:
            seen.add(cl); cands.append((wl_kl(seq, cl), share, v, cl))
    cands.sort(key=lambda x: x[0])
    none_kl = 99.0
    return cands, merges
def expand(seq, cl, target=0.17):
    """grow a cluster by the signs whose contexts are most similar to its members (the paper's 'once y=I, add Y and !')"""
    cnt = collections.Counter(seq); n = len(seq)
    vec = collections.defaultdict(collections.Counter)
    for i, s in enumerate(seq):
        if i > 0: vec[s][('p', seq[i-1])] += 1
        if i + 1 < len(seq): vec[s][('n', seq[i+1])] += 1
    cl = set(cl)
    while sum(cnt[s] for s in cl) / n < target:
        best = max((s for s in cnt if s not in cl and cnt[s] >= 2),
                   key=lambda s: sum(cosine(vec[s], vec[m]) for m in cl) / len(cl), default=None)
        if best is None: break
        cl.add(best)
    return frozenset(cl)
def pick_space(seq, cands, langs, seed, top=6):
    """judge each candidate space class (and 'none') by the best calibrated gap of a quick solve over the languages"""
    options = []
    for k, sh, v, c in cands[:top]:
        options.append(frozenset(c)); options.append(expand(seq, c))
    options = list(dict.fromkeys(options)) + [frozenset()]
    scored = []
    rng = random.Random(seed); shuf = seq[:]; rng.shuffle(shuf)
    for o in options:
        best = None
        for l in langs:
            g = solve(seq, set(o), l, 3, 150000, seed)['gap'] - solve(shuf, set(o), l, 3, 150000, seed)['gap']
            if best is None or g > best[0]: best = (g, l)
        scored.append((best[0], best[1], o))
    scored.sort(key=lambda x: -x[0])
    return scored
def run_solver(ids, lang, tag, restarts, iters, seed, init=None):
    fn = f'/tmp/gh_{os.getpid()}_{seed}_{lang}.txt'
    open(fn, 'w').write(' '.join(map(str, ids)))
    cmd = [f'{HERE}/hsolve_h', f'{HERE}/lm/{lang}.{tag}.bin', fn, str(restarts), str(iters), str(seed)]
    env = dict(os.environ)
    if init is not None:
        fi = fn + '.init'; open(fi, 'w').write(' '.join(map(str, init))); cmd += ['-', fi]; env['HS_SPACE'] = '1'
    out = subprocess.run(cmd, capture_output=True, text=True, env=env).stdout.split()
    os.remove(fn)
    if init is not None: os.remove(fi)
    return float(out[0]), out[1]
def solve(seq, space, lang, restarts, iters, seed):
    signs = sorted(set(s for s in seq if s not in space))
    sid = {s: i for i, s in enumerate(signs)}
    ids = [-1 if s in space else sid[s] for s in seq]
    tag = 'sp' if space else 'ns'
    if not space: ids = [x for x in ids if x >= 0]
    sc, key = run_solver(ids, lang, tag, restarts, iters, seed)
    kmap = {s: key[sid[s]] for s in signs}
    text = ''.join(' ' if s in space else kmap[s] for s in seq)
    ll = ll_text(text, lang, tag)
    raw = ll - held_ll(lang, tag, len(text))
    kl = uni_kl(text, lang)
    gap = raw - kl   # a solve that reads like the language closes the n-gram gap without a skewed letter curve
    return {'lang': lang, 'tag': tag, 'll': round(ll, 4), 'rawgap': round(raw, 4), 'unikl': round(kl, 4), 'gap': round(gap, 4), 'key': kmap, 'text': text}
_uni = {}
def uni_kl(text, lang, withspace=False):
    k = (lang, withspace)
    if k not in _uni:
        c = collections.Counter(ch for ch in open(f'{HERE}/lm/{lang}.held.txt').read() if withspace or ch != ' ')
        tot = sum(c.values()); _uni[k] = {ch: (c[ch] + 0.5) / (tot + 13.5) for ch in 'abcdefghijklmnopqrstuvwxyz '}
    q = _uni[k]; c = collections.Counter(ch for ch in text if withspace or ch != ' '); tot = sum(c.values())
    return sum((c[ch] / tot) * math.log((c[ch] / tot) / q[ch]) for ch in c if c[ch])
def solve_free(seq, init_space, lang, restarts, iters, seed):
    """space as a 27th value: the solve decides which signs are word spaces, seeded from init_space"""
    signs = sorted(set(seq)); sid = {s: i for i, s in enumerate(signs)}
    sc, key = run_solver([sid[s] for s in seq], lang, 'sp', restarts, iters, seed,
                         init=[sid[s] for s in init_space if s in sid])
    kmap = {s: key[sid[s]] for s in signs}
    space = {s for s in signs if kmap[s] == '_'}
    text = ''.join(' ' if kmap[s] == '_' else kmap[s] for s in seq)
    text1 = ' '.join(text.split())
    ll = ll_text(text, lang, 'sp'); raw = ll - held_ll(lang, 'sp', len(text))
    kl = uni_kl(text, lang, withspace=True)
    return {'lang': lang, 'tag': 'free', 'll': round(ll, 4), 'rawgap': round(raw, 4), 'unikl': round(kl, 4),
            'gap': round(raw - kl, 4), 'key': kmap, 'text': text, 'space': space}
def screen(seq, space, restarts, iters, seed, langs=LANGS):
    res = [solve(seq, space, l, restarts, iters, seed) for l in langs]
    res.sort(key=lambda r: -r['gap'])
    return res
# ---------- known-answer control ----------
def copiale_window(n, start):
    rows = [l.rstrip('\n').split('\t') for l in open(f'{HERE}/data/copiale_tokens.tsv')][1:]
    toks = [(r[3], r[4]) for r in rows]
    return toks[start:start + n]
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('mode'); ap.add_argument('file', nargs='?')
    ap.add_argument('--n', type=int, default=1200); ap.add_argument('--start', type=int, default=0)
    ap.add_argument('--seed', type=int, default=1); ap.add_argument('--restarts', type=int, default=6)
    ap.add_argument('--iters', type=int, default=400000); ap.add_argument('--deep', type=int, default=24)
    ap.add_argument('--skip', default='_,MULTI,?'); ap.add_argument('--langs', default=','.join(LANGS))
    ap.add_argument('--oracle-space', action='store_true'); ap.add_argument('--out'); ap.add_argument('--keyout')
    ap.add_argument('--lo', type=float, default=0.08); ap.add_argument('--hi', type=float, default=0.30)
    ap.add_argument('--allow-nospace', action='store_true', help='also try a no-space solve per language (LOG attempt 7: overfits, off)')
    ap.add_argument('--noise', type=float, default=0.0, help='copiale mode: replace this share of tokens by a sign drawn from the window curve (gold kept)')
    ap.add_argument('--shuffle', action='store_true', help='null: shuffle the token order first (seeded)')
    a = ap.parse_args()
    langs = a.langs.split(',')
    gold = None
    if a.mode == 'copiale':
        w = copiale_window(a.n, a.start)
        seq = [t for t, g in w]; gold = [g for t, g in w]
        if a.noise:
            rng = random.Random(a.seed + 7); pool = seq[:]
            seq = [rng.choice(pool) if rng.random() < a.noise else t for t in seq]
    elif a.mode == 'sid':
        sys.path.insert(0, os.path.join(HERE, '..'))
        import score
        seq = score.flat(score.load_text(a.file))
    else:
        import csv
        skip = set(a.skip.split(','))
        seq = [r['sign'] for r in csv.DictReader(open(a.file), delimiter='\t') if r['sign'] not in skip]
    if a.shuffle:
        z = list(zip(seq, gold or [None]*len(seq))); random.Random(a.seed).shuffle(z)
        seq = [x for x, y in z]; gold = [y for x, y in z] if gold else None
    res = {'mode': a.mode, 'file': a.file, 'n': len(seq), 'K': len(set(seq)), 'start': a.start, 'seed': a.seed,
           'shuffled': a.shuffle, 'restarts': a.restarts, 'iters': a.iters, 'deep': a.deep}
    # step a: context clusters as candidate space classes (seeds for the solve)
    cands, merges = step_a(seq, a.lo, a.hi)
    res['a_candidates'] = [{'kl': round(k, 4), 'share': round(s, 3), 'link': round(v, 3), 'signs': sorted(c)}
                           for k, s, v, c in cands[:6]]
    inits = list(dict.fromkeys([frozenset(c) for k, s, v, c in cands[:6]] + [frozenset()]))
    if a.oracle_space and gold: inits = [frozenset(t for t, g in zip(seq, gold) if g == '_')]
    # step c: language screen; each language keeps its best solve over the seeds (the solve assigns spaces itself)
    scr = []
    for l in langs:
        runs = [solve_free(seq, set(i), l, a.restarts, a.iters, a.seed + j) for j, i in enumerate(inits)]
        if a.allow_nospace and not a.oracle_space:   # attempt 7 (LOG.md): breaks the Copiale control; off by default. 'no space class' under the no-space model (a text like FR-HOMO carries none)
            r0 = solve(seq, set(), l, a.restarts, a.iters, a.seed + 50); r0['space'] = set(); runs.append(r0)
        j = max(range(len(runs)), key=lambda j: runs[j]['gap']); b = runs[j]; b['init_rank'] = j; scr.append(b)
    scr.sort(key=lambda r: -r['gap'])
    res['c_screen'] = [{'lang': r['lang'], 'gap': r['gap'], 'rawgap': r['rawgap'], 'unikl': r['unikl'],
                        'n_space_signs': len(r['space']), 'init': r['init_rank']} for r in scr]
    # step d: deeper solve in the two best languages, seeded from each one's best space class
    deep = []
    for r in scr[:2]:
        d = (solve_free(seq, r['space'], r['lang'], a.deep, a.iters, a.seed + 100) if r['space']
             else dict(solve(seq, set(), r['lang'], a.deep, a.iters, a.seed + 100), space=set()))
        deep.append(d if d['gap'] > r['gap'] else r)
    deep.sort(key=lambda r: -r['gap'])
    best = deep[0]; space = best['space']
    res['d_best'] = {'lang': best['lang'], 'gap': best['gap'], 'space_signs': sorted(space),
                     'text_head': best['text'][:200] if gold else None}
    res['d_all'] = [{'lang': r['lang'], 'gap': r['gap']} for r in deep]
    if gold:
        gsp = [g == '_' for g in gold]; psp = [t in space for t in seq]
        tp = sum(x and y for x, y in zip(gsp, psp))
        res['a_space_precision'] = round(tp / max(1, sum(psp)), 3); res['a_space_recall'] = round(tp / max(1, sum(gsp)), 3)
        def rec(r):
            ok = tot = 0
            for t, g, ch in zip(seq, gold, r['text']):
                if g in ('_', '#', '?'): continue
                tot += 1; ok += (ch == g[0])
            return round(ok / max(1, tot), 4)
        res['recovery'] = rec(best)
        res['recovery_screen_de'] = next((rec(r) for r in scr if r['lang'] == 'de'), None)
        res['screen_rank_de'] = [r['lang'] for r in scr].index('de') + 1 if 'de' in langs else None
    # step b: homophone clusters on the non-space signs (pair precision against gold letters on controls)
    rest = [s for s in seq if s not in space]; cnt = collections.Counter(rest)
    m2 = cluster(rest, [s for s in cnt if cnt[s] >= 3])
    res['b_tight_merges'] = [sorted(cl) for v, cl in m2[:12]]
    if gold:
        glet = collections.defaultdict(collections.Counter)
        for t, g in zip(seq, gold):
            if t not in space and g not in ('_', '#', '?'): glet[t][g[0]] += 1
        maj = {t: c.most_common(1)[0][0] for t, c in glet.items()}
        good = tot = 0
        for v, cl in m2[:20]:
            cl = [s for s in cl if s in maj]
            for i, x in enumerate(cl):
                for y in cl[i+1:]: tot += 1; good += maj[x] == maj[y]
        ss = list(maj); same = sum(maj[x] == maj[y] for i, x in enumerate(ss) for y in ss[i+1:]); allp = len(ss)*(len(ss)-1)//2
        res['b_tight_merge_pair_precision'] = round(good / max(1, tot), 3); res['b_pairs'] = tot
        res['b_chance_pair_precision'] = round(same / max(1, allp), 3)
    if a.keyout:
        with open(a.keyout, 'w') as f:
            f.write('sign\tvalue\n')
            for s in sorted(set(seq)): f.write(f"{s}\t{'' if s in space else best['key'].get(s, '')}\n")
    js = json.dumps(res, ensure_ascii=False, indent=1)
    if a.out: open(a.out, 'w').write(js)
    print(js)
if __name__ == '__main__': main()
