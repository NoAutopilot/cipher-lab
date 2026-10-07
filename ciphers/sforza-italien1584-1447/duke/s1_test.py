#!/usr/bin/env python3
"""SFZ-D step S1 (pre-registered, brief .claude/briefs/runs/2026-10-07-acct2-st-rebuild-workers.md, Wave 2):
decode one glossed Duke slip with the Amidani pooled key (../amidani/key.tsv learned by ../amidani/g1.py) and score
letter accuracy against its own clear copy with g1.py's statistic; control = 200 shuffles of the Amidani key's
sign -> value map. PASS (>= 0.60 and > p95) = same key family.
    python3 ciphers/sforza-italien1584-1447/duke/s1_test.py [unit ...]   (default f8)
"""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'amidani'))
import g1  # noqa: E402  (g1.sa is tools/stream_align)
sa = g1.sa
UNITS = {'f8': ('ciphertext_f8.tsv', 'clear_f10.txt')}


def load(ct, cl):
    syms = [t for l in open(os.path.join(HERE, ct)) if l.strip() and not l.startswith('#')
            for t in l.rstrip('\n').split('\t')[1].split()]
    txt = ' '.join(l.strip() for l in open(os.path.join(HERE, cl)) if not l.startswith('#'))
    return syms, sa.letters(txt)


def main(names):
    am = [g1.load(u) for u in g1.UNITS]
    for name in names:
        syms, let = load(*UNITS[name])
        allsyms = sorted({s for _, ss, _ in am for s in ss} | set(syms))
        ids = {s: n for n, s in enumerate(allsyms)}
        c, _ = g1.learn(am, ids)
        key = sa.decode(c)
        trained = np.where(key >= 0)[0]
        # nulls: the held-out slip's own self-alignment unmatched positions (as g1.py)
        cs, path = sa.learn(np.array([ids[s] for s in syms]), let, len(ids), **g1.OPTS)
        matched = {i for i, j in path}
        nulls = {i for i in range(len(syms)) if i not in matched}
        real = g1.score(key, syms, let, ids, nulls)
        rng = np.random.default_rng(g1.SEED)
        sh = []
        for _ in range(g1.NSHUF):
            k2 = key.copy(); k2[trained] = key[rng.permutation(trained)]
            sh.append(g1.score(k2, syms, let, ids, nulls))
        sh = np.array(sh); p95 = float(np.quantile(sh, 0.95))
        unseen = sum(1 for s in syms if key[ids[s]] < 0)
        dec = ''.join(chr(97 + key[ids[s]]) if key[ids[s]] >= 0 else '.' for s in syms)
        v = 'PASS' if real >= 0.60 and real > p95 else 'FAIL'
        print(f'{name}\tsigns {len(syms)}\tnulls {len(nulls)}\tunseen-in-Amidani-key {unseen}\treal {real:.3f}\t'
              f'shuffle mean {sh.mean():.3f}\tp95 {p95:.3f}\t{v}')
        print(f'# decode head: {dec[:120]}')
        print(f'# copy head:   {"".join(chr(97 + x) for x in let[:120])}')


if __name__ == '__main__':
    main(sys.argv[1:] or ['f8'])
