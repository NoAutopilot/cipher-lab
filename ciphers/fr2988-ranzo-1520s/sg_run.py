#!/usr/bin/env python3
"""Run Bourdeau's n20/solve2.py annealer on a pooled token file or a flip-injected control (A1B-RANZO-SG, 3 Oct 2026).

  python3 sg_run.py --vasto <clone>/targets/vasto1527 --seed N --iter I --arm C0|C1|C2|T0|T1|T2 [--out results.tsv]

solve2.py is github.com/dbourdeau/cyphersolver a439937 (D. Bourdeau, MIT); it is read from the clone and executed with two
textual patches, never copied or edited: (1) the real-mode token file -> bourdeau_relabelled/pooled_T<k>.txt; (2) for C1/C2,
after the control is encoded, s-code tokens in the control positions matching the flipped Ranzo files' places in the pooled
order are relabelled g (C1: c007 at rate 1.0; C2: + c018 0.5, c020 0.8; rng seed 7). Its key json goes to the scratch clone's n20/key_<arm>_<seed>.json
(a third patch), not here. Appends one row (arm, seed, iter, score, token_acc, type_acc, key path) to --out.
"""
import argparse, io, json, os, re, contextlib, random
HERE = os.path.dirname(os.path.abspath(__file__))
ORDER = ['f44r', 'f44v', 'f45r', 'f45v', 'f46r', 'f46v', 'ranzo_c006', 'ranzo_c007', 'ranzo_c017', 'ranzo_c018', 'ranzo_c019',
         'ranzo_c020']
RATES = {'C1': {'ranzo_c007': 1.0}, 'C2': {'ranzo_c007': 1.0, 'ranzo_c018': 0.5, 'ranzo_c020': 0.8}}


def spans(n20):
    out, i = {}, 0
    for f in ORDER:
        n = 0
        for l in open(os.path.join(n20, f + '.txt'), encoding='utf8'):
            if l.startswith('#'): continue
            if l.startswith('|'): n += 1; continue
            n += len([t for t in re.sub(r'\[[^\]]*\]', '', l).split() if t not in ('·', '/', '/.')])
        out[f] = (i, i + n); i += n
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--vasto', required=True); ap.add_argument('--seed', type=int, required=True)
    ap.add_argument('--iter', type=int, default=1000000); ap.add_argument('--arm', required=True)
    ap.add_argument('--out', default=os.path.join(HERE, 'sg_results.tsv')); a = ap.parse_args()
    src = open(os.path.join(a.vasto, 'n20', 'solve2.py')).read()
    mode = 'ctrl' if a.arm.startswith('C') else 'real'
    if mode == 'real':
        p = os.path.join(HERE, 'bourdeau_relabelled', f'pooled_T{a.arm[1]}.txt')
        old = "toks=open('n20/all_tokens.txt').read().split()"; assert old in src
        src = src.replace(old, f"toks=open({p!r}).read().split()")
    elif a.arm in RATES:
        sp = spans(os.path.join(a.vasto, 'n20')); inj = []
        rr = random.Random(7)
        for f, r in RATES[a.arm].items():
            lo, hi = sp[f]; inj += [i for i in range(lo, hi) if rr.random() < r]
        anchor = "        toks.append(code[w]); truth.append(w)\n"; assert anchor in src
        o2 = "ty_ok=sum(1 for t in types if assign[t]==inv[t])"; assert o2 in src
        src = src.replace(o2, "ty_ok=sum(1 for t in types if assign[t]==inv.get(t))")  # flipped g-codes have no true word
        src = src.replace(anchor, anchor + f"    _inj=set({sorted(inj)!r})\n    toks=[('g'+t[1:]) if (i in _inj and t[0]=='s') else t for i,t in enumerate(toks)]\n    print('INJECTED',sum(1 for i,t in enumerate(toks) if i in _inj and t[0]=='g' and truth[i][0]=='s'))\n", 1)
    o3 = "open(f'n20/s2key_{seed}.json','w')"; assert o3 in src
    src = src.replace(o3, f"open('n20/key_{a.arm}_{a.seed}.json','w')")
    cwd = os.getcwd(); os.chdir(a.vasto); buf = io.StringIO()
    import sys; sys.argv = ['solve2.py', str(a.seed), str(a.iter), mode]
    try:
        with contextlib.redirect_stdout(buf):
            exec(compile(src, 'solve2.py', 'exec'), {'__name__': '__main__'})
    finally:
        os.chdir(cwd)
    o = buf.getvalue()
    g = lambda pat: (re.search(pat, o) or [None, ''])[1]
    row = [a.arm, str(a.seed), str(a.iter), g(r'SCORE (\S+)'), g(r'CTRL token acc (\S+)'), g(r'CTRL type acc (\S+)'),
           g(r'INJECTED (\d+)'), os.path.join(a.vasto, 'n20', f's2key_{a.seed}.json')]
    row[-1] = f'key_{a.arm}_{a.seed}.json'  # in the scratch clone's n20/, not committed
    new = not os.path.exists(a.out)
    with open(a.out, 'a') as fh:
        if new: fh.write('arm\tseed\titer\tscore\ttoken_acc\ttype_acc\tinjected\tkey\n')
        fh.write('\t'.join(row) + '\n')
    print('\t'.join(row))


if __name__ == '__main__':
    main()
