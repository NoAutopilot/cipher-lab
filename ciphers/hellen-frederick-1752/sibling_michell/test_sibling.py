#!/usr/bin/env python3
"""Rule-3 test of the Michell sibling key (key_sibling.tsv) on the Hellen ciphertexts.
1. Range/overlap first: code range of the key vs each target's tokens; shared-code coverage.
2. Value-dependent statistic: mean fr18 word-unigram log-probability of the decoded covered tokens
   (frequent codes should land on frequent French words if the code is the same). Control: 200 shuffles
   of the key's values over its codes (coverage identical by construction; only the values move, which the
   statistic does depend on). p = share of shuffles >= real.
3. Positive control (power at matched N): key built from R1050 alone, applied to R1051's own codes, and the
   same statistic subsampled to the target's covered-token count.
Usage: python3 test_sibling.py [--seed 1]   (writes test_sibling_output.txt)
       python3 test_sibling.py --key KEY.tsv --out OUT.txt [--seed 1]   (any key; see run_key, READ2-HEL 3 Oct 2026)"""
import re, os, sys, gzip, glob, math, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, HERE)
import build_key

def unigram():
    c = collections.Counter()
    for f in sorted(glob.glob(os.path.join(ROOT, 'tools/data/fr18/*.txt.gz'))):
        txt = gzip.open(f, 'rt', encoding='utf-8', errors='ignore').read().lower()
        c.update(re.findall(r"[a-zàâçéèêëîïôûùüÿœ]+", txt))
    tot = sum(c.values())
    return lambda w: math.log((c.get(w, 0) + 0.5) / tot)

def wordlp(lp, v):
    parts = re.findall(r"[a-zàâçéèêëîïôûùüÿœ]+", v.lower().split('|')[0])
    return sum(lp(p) for p in parts) / len(parts) if parts else lp('zzz')

def load_key(path):
    k = {}
    for l in open(path, encoding='utf-8').read().splitlines()[1:]:
        c, v = l.split('\t')[:2]; k[c] = v
    return k

def target_tokens(fn):
    out = []
    for t in open(fn).read().split():
        t = re.sub(r'[_^]', '', t)
        if re.fullmatch(r'\d+', t): out.append(t)
    return out

def stat(key, toks, lp):
    cov = [key[t] for t in toks if t in key]
    return (sum(wordlp(lp, v) for v in cov) / len(cov) if cov else float('nan')), len(cov)

def shuffled(key, rng):
    cs = list(key); vs = [key[c] for c in cs]; rng.shuffle(vs); return dict(zip(cs, vs))

def run(name, key, toks, lp, rng, out, n=200):
    real, ncov = stat(key, toks, lp)
    sh = sorted(stat(shuffled(key, rng), toks, lp)[0] for _ in range(n))
    p = sum(s >= real for s in sh) / n
    mean = sum(sh) / n
    out.append(f'{name}\tN_tokens={len(toks)}\tcovered={ncov} ({ncov/len(toks):.1%})\treal={real:.3f}\tshuffle_mean={mean:.3f}\tshuffle_p95={sh[int(.95*n)-1]:.3f}\tp={p:.3f}')
    return real, ncov, p

def fr18_counts():
    u = collections.Counter(); b = collections.Counter()
    for f in sorted(glob.glob(os.path.join(ROOT, 'tools/data/fr18/*.txt.gz'))):
        ws = re.findall(r"[a-zàâçéèêëîïôûùüÿœ]+", gzip.open(f, 'rt', encoding='utf-8', errors='ignore').read().lower())
        u.update(ws); b.update(zip(ws, ws[1:]))
    return u, b

def pmi_from(u, b, oov_floor=False):
    """oov_floor=True (N5-HEL7, 4 Oct 2026): an out-of-vocabulary LEFT word scores at the unseen-pair floor log(0.3), not 0
    (N4-HEL6's tool note). Default False keeps every output committed before 4 Oct 2026 reproducible."""
    tot = sum(u.values())
    def pmi(a, c):  # log P(c|a)/P(c), interpolated with the unigram so unseen pairs score about 0 - small
        pc = (u.get(c, 0) + 0.5) / tot
        if not u.get(a): return math.log(0.3) if oov_floor else 0.0
        return math.log((0.7 * b.get((a, c), 0) / u[a] + 0.3 * pc) / pc)
    return pmi

def bigram(oov_floor=False):
    """fr18 word bigram and unigram counts, for the order-sensitive statistic (READ2-HEL, 3 Oct 2026)."""
    u, b = fr18_counts()
    return pmi_from(u, b, oov_floor)

def words(v):
    return re.findall(r"[a-zàâçéèêëîïôûùüÿœ]+", v.lower().split('|')[0])

def stat_bi(key, toks, pmi):
    """Mean PMI of the junction word pair over adjacent token pairs that are both covered and both have words.
    Depends on token ORDER (unlike stat), so an order-shuffle control can differ from the target."""
    s = []
    for x, y in zip(toks, toks[1:]):
        if x in key and y in key:
            a, c = words(key[x]), words(key[y])
            if a and c: s.append(pmi(a[-1], c[0]))
    return (sum(s) / len(s) if s else float('nan')), len(s)

def synth_stream(key, rng, n_words=60000):
    """Positive control plaintext: real fr18 prose encoded with this key (a word whose spelling is one of the key's
    meanings gets one of its codes at random; any other word becomes an uncovered token 'x')."""
    inv = collections.defaultdict(list)
    for c, v in key.items():
        w = ' '.join(words(v))
        if w: inv[w].append(c)
    f = sorted(glob.glob(os.path.join(ROOT, 'tools/data/fr18/*.txt.gz')))[0]
    ws = re.findall(r"[a-zàâçéèêëîïôûùüÿœ]+", gzip.open(f, 'rt', encoding='utf-8', errors='ignore').read().lower())
    i0 = rng.randrange(0, max(1, len(ws) - n_words)); ws = ws[i0:i0 + n_words]
    out = []; i = 0
    while i < len(ws):
        two = ws[i] + ' ' + ws[i + 1] if i + 1 < len(ws) else None
        if two in inv: out.append(rng.choice(inv[two])); i += 2
        elif ws[i] in inv: out.append(rng.choice(inv[ws[i]])); i += 1
        else: out.append('x'); i += 1
    return out

def run_key(keypath, outpath, seed, n=200):
    """--key mode (READ2-HEL, 3 Oct 2026): test any key TSV (code, meaning, ...) on every ciphertext_R*.txt.
    (a) value shuffle x n on the unigram stat and on the bigram stat; (b) token-ORDER shuffle x n of the target on the
    bigram stat (the unigram stat cannot move under an order shuffle, so (b) is not run on it); (c) positive control:
    contiguous windows of real fr18 prose encoded with this key, at the target's covered count, power = share of 200
    windows reaching p<=0.05 against 50 value shuffles (unigram, windows at the covered count) and 50 order shuffles
    (bigram, windows holding the target's own number of adjacent covered pairs)."""
    rng = random.Random(seed); lp = unigram(); pmi = bigram(); out = []
    key = {c: v for c, v in load_key(keypath).items() if v.strip()}
    nums = sorted(int(re.sub(r'\D', '', c)) for c in key if re.search(r'\d', c))
    out.append(f'key {os.path.relpath(keypath, T)}: {len(key)} codes with a meaning, range {nums[0]}-{nums[-1]}')
    out.append('item\tN\tcovered\tuni_real\tuni_shuf_mean\tuni_p95\tuni_p\tpairs\tbi_real\tbi_valshuf_mean\tbi_val_p'
               '\tbi_ordshuf_mean\tbi_ord_p95\tbi_ord_p\tpow_uni\tpow_bi_order')
    stream = synth_stream(key, rng)
    for f in sorted(glob.glob(os.path.join(T, 'ciphertext_R*.txt')), key=lambda f: (('R1953' not in f), f)):
        toks = target_tokens(f)
        ur, nc = stat(key, toks, lp)
        us = sorted(stat(shuffled(key, rng), toks, lp)[0] for _ in range(n))
        br, npairs = stat_bi(key, toks, pmi)
        bv = sorted(stat_bi(shuffled(key, rng), toks, pmi)[0] for _ in range(n))
        bo = []
        for _ in range(n):
            t2 = toks[:]; rng.shuffle(t2); bo.append(stat_bi(key, t2, pmi)[0])
        bv = [x for x in bv if x == x]; bo = sorted(x for x in bo if x == x)
        p = lambda xs, r: sum(x >= r for x in xs) / len(xs) if xs and r == r else float('nan')
        mean = lambda xs: sum(xs) / len(xs) if xs else float('nan')
        q95 = lambda xs: sorted(xs)[max(0, int(.95 * len(xs)) - 1)] if xs else float('nan')
        # power at this covered count
        pu = pb = 0; draws = 200 if nc else 0
        cov_idx = [i for i, t in enumerate(stream) if t in key]
        pair_idx = [i for i in range(len(stream) - 1) if stream[i] in key and stream[i + 1] in key
                    and words(key[stream[i]]) and words(key[stream[i + 1]])]
        for _ in range(draws):
            if len(cov_idx) <= nc: break
            j = rng.randrange(0, len(cov_idx) - nc); win = stream[cov_idx[j]:cov_idx[j + nc - 1] + 1]
            r = stat(key, win, lp)[0]
            pu += p([stat(shuffled(key, rng), win, lp)[0] for _ in range(50)], r) <= 0.05
            if not npairs or len(pair_idx) <= npairs: continue
            j = rng.randrange(0, len(pair_idx) - npairs); win = stream[pair_idx[j]:pair_idx[j + npairs - 1] + 2]
            rb = stat_bi(key, win, pmi)[0]
            sh = []
            for _ in range(50):
                w2 = win[:]; rng.shuffle(w2); sh.append(stat_bi(key, w2, pmi)[0])
            pb += p(sh, rb) <= 0.05
        name = os.path.basename(f)[11:-4]
        out.append(f'{name}\t{len(toks)}\t{nc} ({nc/len(toks):.1%})\t{ur:.3f}\t{sum(us)/n:.3f}\t{us[int(.95*n)-1]:.3f}\t{p(us, ur):.3f}'
                   f'\t{npairs}\t{br:.3f}\t{mean(bv):.3f}\t{p(bv, br):.3f}\t{mean(bo):.3f}\t{q95(bo):.3f}\t{p(bo, br):.3f}'
                   f'\t{pu/max(draws,1):.2f}\t{pb/max(draws,1):.2f}')
    out.append(f'# positive-control stream: {len(stream)} fr18 words, {sum(t in key for t in stream)} encoded with this key')
    txt = '\n'.join(out) + '\n'
    open(outpath, 'w').write(txt); print(txt)

if __name__ == '__main__':
    if '--key' in sys.argv:
        a = sys.argv
        run_key(os.path.abspath(a[a.index('--key') + 1]), os.path.abspath(a[a.index('--out') + 1]),
                int(a[a.index('--seed') + 1]) if '--seed' in a else 1)
        sys.exit(0)
    seed = int(sys.argv[sys.argv.index('--seed') + 1]) if '--seed' in sys.argv else 1
    rng = random.Random(seed); lp = unigram(); out = []
    key = load_key(os.path.join(HERE, 'key_sibling.tsv'))
    plain = sorted(int(re.sub(r'\D', '', c)) for c in key)
    out.append(f'key: {len(key)} codes, range {plain[0]}-{plain[-1]}, {sum("½" in c for c in key)} with a ½ mark')
    # positive control: key from R1050 only -> R1051's own code stream
    pairs, _, _ = build_key.build()
    k1050 = {c: max(((w, n) for (w, r), n in d.items() if r == 'R1050'), key=lambda x: x[1], default=(None, 0))[0]
             for c, d in pairs.items()}
    k1050 = {c: v for c, v in k1050.items() if v and re.fullmatch(r'\d+½?', c)}
    r1051 = []
    for i, l in enumerate(open(os.path.join(HERE, 'DOC_R1051_D1940_1940.txt'), encoding='utf-8').read().splitlines()):
        if re.match(r'^[\d_ ,/]+$', l.strip()) and l.strip(): r1051 += build_key.codes(l)
    out.append('# positive control (same code, held-out letter): key from R1050 only, applied to R1051 code stream')
    _, ncov_pos, _ = run('R1051 (control)', k1050, r1051, lp, rng, out)
    out.append('# targets: full sibling key (R1050+R1051)')
    covs = {}
    for f in sorted(glob.glob(os.path.join(T, 'ciphertext_R*.txt'))):
        toks = target_tokens(f)
        nums = sorted(map(int, toks))
        inr = sum(plain[0] <= x <= plain[-1] for x in nums)
        out.append(f'# {os.path.basename(f)}: {len(toks)} numeric tokens, in key range {inr} ({inr/len(toks):.1%}), target median {nums[len(nums)//2]}')
        _, ncov, _ = run(os.path.basename(f)[11:-4], key, toks, lp, rng, out)
        covs[f] = (toks, ncov)
    out.append('# power check: positive control subsampled to each target\'s covered count (200 draws of the R1051 stream, '
               'share with p<=0.05 against 50 shuffles each)')
    for f, (toks, ncov) in covs.items():
        cov_stream = [t for t in r1051 if t in k1050]
        if ncov == 0: continue
        hits = 0
        for _ in range(200):
            sub = rng.sample(cov_stream, min(ncov, len(cov_stream)))
            real = stat(k1050, sub, lp)[0]
            sh = [stat(shuffled(k1050, rng), sub, lp)[0] for _ in range(50)]
            hits += sum(s >= real for s in sh) / 50 <= 0.05
        out.append(f'{os.path.basename(f)[11:-4]}\tcovered={ncov}\tpower(control at this N)={hits/200:.2f}')
    txt = '\n'.join(out) + '\n'
    open(os.path.join(HERE, 'test_sibling_output.txt'), 'w').write(txt); print(txt)
