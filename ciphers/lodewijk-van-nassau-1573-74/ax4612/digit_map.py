"""AX-4612 extension E3: is 4612 key.tsv's table read through a consistent digit misreading?

Hypothesis: the letter is in the 1574 table (key.tsv; 5810/5811/4503 of Jan-Apr 1574 read under it) but this hand's
digit shapes were read consistently wrong by both blind passes (pass-agreed numerals show no 5-block structure,
ic_by_conf.py). Search: a permutation pi of the ten digits applied to every numeral's written digits, the result
decoded under key.tsv (values outside 1-120 break the run), scored by a French order-3 model (fr16 corpora, via
tools/homophonic_anneal.Model) as total log-prob of the decoded letters plus -8 per unreadable token. Hill-climb on
digit swaps from the identity and from random starts.
Matched control: the real letter 5811 cut to 4612's numeral count, its digits passed through a random permutation
(3 seeds); the search must recover the inverse (all ten digits, or at least the digits that occur) and return
key.tsv's reading. Both numbers are printed side by side.
  python3 ciphers/lodewijk-van-nassau-1573-74/ax4612/digit_map.py [--restarts 40]"""
import csv, random, sys, argparse
sys.path.insert(0, 'tools')
import homophonic_anneal as ha, judge_plaintext as jp
D = 'ciphers/lodewijk-van-nassau-1573-74/'
KEY = {int(r['code']): r['value'].replace('v', 'u').replace('j', 'i') for r in csv.DictReader(open(D + 'key.tsv'), delimiter='\t')
       if r['code'].isdigit() and int(r['code']) <= 120}
SPEC = 'specs/lodewijk-4612.json'


def numerals(nr, limit=None):
    """runs of numeral strings (all values, 1574 of a date excluded), split at clear words."""
    runs, cur, n = [], [], 0
    for r in csv.DictReader(open(D + f'ciphertext_{nr}.tsv'), delimiter='\t'):
        s = r['sign']
        if s.startswith('='):
            if cur: runs.append(cur); cur = []
        elif s.isdigit() and s != '1574':
            cur.append(s); n += 1
            if limit and n >= limit: break
    if cur: runs.append(cur)
    return runs


def apply(runs, pi):
    t = str.maketrans('0123456789', ''.join(pi))
    return [[x.translate(t) for x in r] for r in runs]


def decode(runs):
    out = []
    for r in runs:
        seg = ''
        for x in r:
            v = int(x) if x[0] != '0' else 0
            seg += KEY.get(v, '#')
        out.append(seg)
    return out


def score(model, runs, pi):
    o = model.order; tot = 0.0; bad = 0
    for seg in decode(apply(runs, pi)):
        for part in seg.split('#'):
            tot += sum(model.logp(part[i:i + o]) for i in range(len(part) - o + 1))
        bad += seg.count('#')
    return tot - 8.0 * bad


def climb(model, runs, rng, restarts):
    ident = list('0123456789'); best = (score(model, runs, ident), ident)
    for r in range(restarts):
        pi = ident[:] if r == 0 else rng.sample(ident, 10)
        cur = score(model, runs, pi); improved = True
        while improved:
            improved = False
            for i in range(10):
                for j in range(i + 1, 10):
                    q = pi[:]; q[i], q[j] = q[j], q[i]
                    s = score(model, runs, q)
                    if s > cur + 1e-9: pi, cur, improved = q, s, True
        if cur > best[0]: best = (cur, pi)
    return best


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--restarts', type=int, default=40)
    a = ap.parse_args()
    import json
    spec = json.load(open(SPEC))
    model = ha.Model([jp.read_corpus(p) for p in spec['judge']['corpora']], 3)
    ident = list('0123456789')
    tgt = numerals('4612'); n = sum(map(len, tgt))
    print(f'target 4612: {n} numerals, identity score {score(model, tgt, ident):.1f}')
    for seed in (1, 2, 3):
        rng = random.Random(seed)
        ctl = numerals('5811', n)
        scram = rng.sample(ident, 10)                        # written digit d is read as scram[d]
        inv = ['0'] * 10
        for d, e in enumerate(scram): inv[int(e)] = str(d)   # the map the search must find
        ctl_s = apply(ctl, scram)
        sc, pi = climb(model, ctl_s, random.Random(seed + 50), a.restarts)
        used = sorted({c for r in ctl for x in r for c in x})
        ok = sum(pi[int(scram[int(d)])] == d for d in used)
        dec = ''.join(decode(apply(ctl_s, pi)))
        ref = ''.join(decode(ctl))
        agree = sum(x == y for x, y in zip(dec, ref)) / max(1, len(ref))
        print(f'CONTROL seed {seed}: 5811 N={sum(map(len, ctl))} scrambled {"".join(scram)}; found {"".join(pi)} '
              f'(needed {"".join(inv)}); digits recovered {ok}/{len(used)}; decode = key.tsv reading on {agree:.3f}; '
              f'score {sc:.1f} vs unscrambled {score(model, ctl, ident):.1f}')
    sc, pi = climb(model, tgt, random.Random(99), a.restarts)
    dec = decode(apply(tgt, pi))
    print(f'TARGET 4612: best map {"".join(pi)} score {sc:.1f} (identity {score(model, tgt, ident):.1f})')
    print('TARGET decode under best map:', ' / '.join(dec)[:700])


if __name__ == '__main__':
    main()
