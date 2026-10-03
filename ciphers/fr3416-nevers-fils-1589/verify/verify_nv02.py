#!/usr/bin/env python3
"""verify_nv02.py -- VERIFY-NV02 (verifier, account 3, 3 Oct 2026): independent re-run of NV02-READ's statistics.

Usage: python3 verify/verify_nv02.py [--seeds 2,3] [--trials 20]
Reuses decode_f35.py's key, ciphertext, fr16 model and rank test (imported, not copied), and adds:
  (a) fresh-seed rank/z for target (all, H only), NV-03 positive control, shuffled-order control;
  (b) key-blind variants: blind passes A and B as the readers wrote them, paired naively from each line's first digit,
      with and without the one mechanical convention 0->8 (the looped-8 glyph, settled from the key sheet's hand);
  (c) the solver's disclosed key-coverage choices flipped: L03 pairing offset, L03 '59' second digit, L05 dropped,
      L10 dropped, and all four at once;
  (d) power at three digit-error levels: 0.239 (raw blind reader vs reconciled, the upper bracket), 0.10, 0.05.
"""
import sys, os, random, statistics
H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, H)
import decode_f35 as D

def pairs(s): return [s[i:i+2] for i in range(0, len(s) - 1, 2)]

def rt(codes, K, score, seed, n=200):
    return D.rank_test(codes, K, score, random.Random(seed), n)

def power(nlet, nnull, K, score, err, seed, trials):
    rng = random.Random(seed); t = D.corpus_text
    inv = {}
    for c, v in K.items(): inv.setdefault(v, []).append(c)
    hits = 0
    for _ in range(trials):
        s = rng.randrange(0, len(t) - nlet); w = t[s:s + nlet]
        cod = [rng.choice(inv[ch]) if ch in inv else rng.choice(inv['-']) for ch in w]
        for _ in range(nnull): cod.insert(rng.randrange(len(cod) + 1), rng.choice(inv['-']))
        ds = list(''.join(cod))
        for j in range(len(ds)):
            if rng.random() < err: ds[j] = str(rng.randrange(10))
        noisy = pairs(''.join(ds))
        real, rank, z, mx = D.rank_test(noisy, K, score, rng, 200)
        hits += rank == 1
    return hits

def main():
    seeds = [int(x) for x in (sys.argv[sys.argv.index('--seeds') + 1] if '--seeds' in sys.argv else '2,3').split(',')]
    trials = int(sys.argv[sys.argv.index('--trials') + 1]) if '--trials' in sys.argv else 20
    K = D.load_key(); runs = D.load_ct()
    D.corpus_text = D.corpus(); score = D.model(D.corpus_text)
    allc = [t for _, toks in runs for t, g in toks]
    Hc = [t for _, toks in runs for t, g in toks if g == 'H']
    print('== (a) fresh seeds')
    for sd in seeds:
        for name, codes in (('target all', allc), ('target H only', Hc), ('control NV-03 f.38v', D.NV03)):
            r, rk, z, mx = rt(codes, K, score, sd)
            print('seed %d %-22s letters %3d score %.3f rank %d/201 z %.2f shuf max %.3f' % (sd, name, len(D.keyed_text(codes, K)), r, rk, z, mx))
        rng = random.Random(sd * 101); real = score(D.keyed_text(allc, K)); sh = []
        for _ in range(200):
            c = allc[:]; rng.shuffle(c); sh.append(score(D.keyed_text(c, K)))
        print('seed %d shuffled-order: real %.3f vs max %.3f mean %.3f, >= real %d/200' % (sd, real, max(sh), statistics.mean(sh), sum(x >= real for x in sh)))
    print('== (b) key-blind variants (naive pairing from line start)')
    for pname, P in (('pass A', D.PASS_A), ('pass B', D.PASS_B)):
        for conv in (False, True):
            codes = []
            for k, s in P.items():
                codes += pairs(s.replace('0', '8') if conv else s)
            r, rk, z, mx = rt(codes, K, score, seeds[0])
            print('%s %-10s tokens %3d letters %3d score %.3f rank %d/201 z %.2f' % (pname, '0->8' if conv else 'as read', len(codes), len(D.keyed_text(codes, K)), r, rk, z))
    print('== (c) disclosed choices flipped (all tokens, seed %d)' % seeds[0])
    byrun = {rid: [t for t, g in toks] for rid, toks in runs}
    L03_alt = pairs(D.RECON['L03'])  # pairing from the first digit, no stray-1 offset
    def assemble(alt_offset=False, alt59=None, drop5=False, drop10=False):
        out = []
        for rid, toks in runs:
            codes = [t for t, g in toks]
            if rid == '2':
                if alt_offset: codes = L03_alt
                elif alt59: codes = [alt59 if c == '59' else c for c in codes]
            if rid == '4' and drop5: continue
            if rid == '8' and drop10: continue
            out += codes
        return out
    variants = [('as committed', {}), ('L03 offset 0', {'alt_offset': True})] + \
               [('L03 59->%s' % a, {'alt59': a}) for a in ('52', '53', '54')] + \
               [('drop L05', {'drop5': True}), ('drop L10', {'drop10': True}),
                ('L03 offset 0 + drop L05,L10', {'alt_offset': True, 'drop5': True, 'drop10': True}),
                ('drop runs 2,4,8 entirely', None)]
    for name, kw in variants:
        if kw is None:
            codes = [t for rid, toks in runs if rid not in ('2', '4', '8') for t, g in toks]
        else:
            codes = assemble(**kw)
        r, rk, z, mx = rt(codes, K, score, seeds[0])
        print('%-30s letters %3d score %.3f rank %d/201 z %.2f' % (name, len(D.keyed_text(codes, K)), r, rk, z))
    print('== (d) power, N=%d letters, %d trials per level' % (len(D.keyed_text(allc, K)), trials))
    nlet = len(D.keyed_text(allc, K)); nnull = sum(1 for c in allc if K.get(c) == '-')
    for err in (0.239, 0.10, 0.05):
        print('err %.3f: %d/%d rank 1 of 201' % (err, power(nlet, nnull, K, score, err, seeds[0] * 7, trials), trials))
    nletH = len(D.keyed_text(Hc, K)); nnullH = sum(1 for c in Hc if K.get(c) == '-')
    print('H-only size N=%d letters, err 0.10: %d/%d' % (nletH, power(nletH, nnullH, K, score, 0.10, seeds[0] * 11, trials), trials))

if __name__ == '__main__':
    main()
