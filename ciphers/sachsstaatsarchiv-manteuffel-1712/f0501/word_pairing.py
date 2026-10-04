#!/usr/bin/env python3
"""RUN4-MANT (4 Oct 2026): PREREG-MANT-WORD whole-word code pairing on frame 0501's glossed multi-code runs.
Per run k = min(#codes, #words); both sides cut into k contiguous non-empty blocks, block i <-> block i. A code occurrence's
label is its block's word tuple. S_word = max over joint cuts of (recurring codes with one label at every occurrence) / (recurring
codes). Control: gloss strings permuted across runs, 200 draws, seed 409. Writes word_pairing.tsv and word_values.tsv.
Usage: python3 word_pairing.py [--check]   (--check: exit 1 if the committed word_pairing.tsv differs)"""
import csv, itertools, os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = ['C3', 'C4', 'C7', 'C9', 'C10', 'C12']
TRIM = {'C9': ['553', '716', '417', '646']}  # 84.406.108 unglossed on the image (RUN3-MANT run 9)

def cuts(n, k):
    for c in itertools.combinations(range(1, n), k - 1):
        b = (0,) + c + (n,); yield [(b[i], b[i + 1]) for i in range(k)]

def run_labelings(codes, words, rec):
    """Distinct tuples of (position, label) for recurring codes, over all cuts."""
    k = min(len(codes), len(words)); out = set()
    for cc in cuts(len(codes), k):
        for wc in cuts(len(words), k):
            lab = []
            for (a, b), (c, d) in zip(cc, wc):
                for p in range(a, b):
                    if codes[p] in rec: lab.append((p, codes[p], tuple(words[c:d])))
            out.add(tuple(lab))
    return out

def best(runs):
    cnt = Counter(c for codes, _ in runs for c in codes); rec = {c for c, n in cnt.items() if n >= 2}
    opts = [sorted(run_labelings(codes, words, rec)) for codes, words in runs]
    opts = [o if o else [()] for o in opts]
    bestn, bestlab = -1, None
    for combo in itertools.product(*opts):
        lab = defaultdict(set)
        for li in combo:
            for _, c, w in li: lab[c].add(w)
        n = sum(1 for c in rec if len(lab[c]) == 1)
        if n > bestn: bestn, bestlab = n, lab
    return len(rec), bestn, bestlab

def main():
    pairs = {r['cipher_line']: r for r in csv.DictReader(open(os.path.join(HERE, 'pairs.tsv')), delimiter='\t')}
    codes = [TRIM.get(r, pairs[r]['cipher_raw'].split()) for r in RUNS]
    gl = [pairs[r]['plain_raw'].split() for r in RUNS]
    nrec, ncons, lab = best(list(zip(codes, gl)))
    rows = [('real', nrec, ncons)]
    rng = random.Random(409)
    for d in range(200):
        g = gl[:]; rng.shuffle(g); n, c, _ = best(list(zip(codes, g))); rows.append((f'shuf{d:03d}', n, c))
    tsv = 'draw\tn_rec\tn_cons\n' + ''.join(f'{a}\t{b}\t{c}\n' for a, b, c in rows)
    vals = 'code\tlabels_at_best_cut\tconsistent\tgrade\n' + ''.join(
        f"{c}\t{' | '.join(' '.join(w) for w in sorted(lab[c]))}\t{'yes' if len(lab[c]) == 1 else 'no'}\tM\n" for c in sorted(lab, key=int))
    sh = sorted(c / n for _, n, c in rows[1:]); p95 = sh[int(0.95 * len(sh)) - 1]; mean = sum(sh) / len(sh)
    summ = f'S_word real {ncons}/{nrec} = {ncons / nrec:.3f}; shuffle mean {mean:.3f}, p95 {p95:.3f}'
    if '--check' in sys.argv:
        ok = open(os.path.join(HERE, 'word_pairing.tsv')).read() == tsv and open(os.path.join(HERE, 'word_values.tsv')).read() == vals
        print(summ, 'check', 'OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(os.path.join(HERE, 'word_pairing.tsv'), 'w').write(tsv); open(os.path.join(HERE, 'word_values.tsv'), 'w').write(vals)
    print(summ); print(vals)

if __name__ == '__main__':
    main()
