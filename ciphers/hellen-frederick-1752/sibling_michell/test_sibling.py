#!/usr/bin/env python3
"""Rule-3 test of the Michell sibling key (key_sibling.tsv) on the Hellen ciphertexts.
1. Range/overlap first: code range of the key vs each target's tokens; shared-code coverage.
2. Value-dependent statistic: mean fr18 word-unigram log-probability of the decoded covered tokens
   (frequent codes should land on frequent French words if the code is the same). Control: 200 shuffles
   of the key's values over its codes (coverage identical by construction; only the values move, which the
   statistic does depend on). p = share of shuffles >= real.
3. Positive control (power at matched N): key built from R1050 alone, applied to R1051's own codes, and the
   same statistic subsampled to the target's covered-token count.
Usage: python3 test_sibling.py [--seed 1]   (writes test_sibling_output.txt)"""
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

if __name__ == '__main__':
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
