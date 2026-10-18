#!/usr/bin/env python3
"""Is the Cossit/Summer cypher an alphabetical dictionary code (first figure = page, rising with the word's spelling)?

SHERWOOD-PAGES, 18 Oct 2026. Two independent word lists for figure groups:
  gloss  -- words written above figure groups on p.347 itself (period interlinear hand, first gloss row plus "February"
            over 138-28 in the date line); alignment is the page's own, graded C where a gloss sits squarely over a group.
  sketch -- our alignment of Sherwood's own sketch of message No.4 (p.84-85) to the p.345 groups, by word order and
            repeats (sleigh 331-36 x2, towards 371-21 x2, the 364-32 x2, Albany 10-34 x2, from 131-22 x2); graded M.
Statistic: Spearman rho between the first figure and the word's alphabetical rank. Control: the same words assigned to
the same groups in a random order, 10,000 permutations (seeded); p = share of permutations with rho >= observed.
The control can differ from the target on this statistic (it changes which word sits on which group), unlike an
order-shuffle of a coverage figure (CLAUDE.md rule 3). Usage: python3 alpha_order_test.py [--check]
"""
import random, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
GLOSS = [('lameness', 203), ('ten', 96), ('liable', 210), ('being', 32), ('left', 209), ('february', 138)]
SKETCH = [('wednesday', 411), ('last', 206), ('sleighs', 331), ('men', 219), ('sleigh', 331), ('marched', 226),
          ('from', 131), ('albany', 10), ('towards', 371), ('vermont', 382), ('post', 274), ('alarmed', 10),
          ('them', 364), ('they', 365), ('expect', 131), ('said', 312), ('force', 146), ('was', 409), ('destined', 109),
          ('the', 364), ('reduction', 297), ('of', 246), ('new', 240), ('state', 344), ('colonel', 65), ('strong', 349),
          ('reported', 301), ('council', 81), ('my', 237), ('hearing', 168), ('saturday', 315), ('reports', 301),
          ('only', 247), ('february', 138)]

def rank(xs):
    o = sorted(range(len(xs)), key=lambda i: xs[i]); r = [0.0] * len(xs); i = 0
    while i < len(o):
        j = i
        while j + 1 < len(o) and xs[o[j + 1]] == xs[o[i]]: j += 1
        for k in range(i, j + 1): r[o[k]] = (i + j) / 2
        i = j + 1
    return r

def rho(a, b):
    ra, rb = rank(a), rank(b); n = len(a); ma = sum(ra) / n; mb = sum(rb) / n
    num = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    den = (sum((x - ma) ** 2 for x in ra) * sum((y - mb) ** 2 for y in rb)) ** 0.5
    return num / den

def test(name, pairs, n=10000):
    words = [w for w, _ in pairs]; pages = [p for _, p in pairs]
    obs = rho(words, pages); rng = random.Random(1783); ge = 0; tot = 0.0
    for _ in range(n):
        w2 = words[:]; rng.shuffle(w2); r = rho(w2, pages); tot += r; ge += r >= obs - 1e-12
    return f'{name}\tN={len(pairs)}\trho={obs:.3f}\tcontrol_mean={tot / n:.3f}\tp={ge / n:.4f}'

def main():
    text = '\n'.join([test('gloss', GLOSS), test('sketch', SKETCH)]) + '\n'
    path = os.path.join(HERE, 'alpha_order_test.out')
    if '--check' in sys.argv:
        ok = os.path.exists(path) and open(path).read() == text
        print('ok: alpha_order_test.out is current' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(path, 'w').write(text); print(text, end='')

if __name__ == '__main__':
    main()
