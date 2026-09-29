#!/usr/bin/env python3
"""DEB-SWARM-B fitting script: the only thing that makes group B's key files (29 Sept 2026).

  python3 fit_key.py --text c2 --out KEY_fit_c2.tsv            real text (settled draft), reads ONLY that text
  python3 fit_key.py --control EN-HOMO --part c2 --out K.tsv   harness control, reads ONLY swarm/controls/<id>.tsv
                                                               (never controls/sealed/)
  options: --shuffle-seed S   refit null: the fit text's sign order shuffled (gaps kept in place) before fitting
           --xspace           X read as the word space (27-symbol model); default X is an ordinary sign
           --restarts R --iters I --seed S   (defaults 60 x 5,000,000, seed 1: the method of every Phase 1/2 row)

Method (fixed): hsolve5b = simulated annealing, one English letter per sign, Witten-Bell 5-gram conditional model
(model5_en.bin, built by build5.c from gb.LM_FILES: 21 public-domain books 1813-1925, Tennyson removed because the
harness's EN-HOMO plaintext is his), score = 5-gram log10 over runs of read signs minus N x KL(letters || English),
bounded-loss table q 0.1, beta 1, t0 2.5; best of R restarts. Real text: `_` and MULTI are gaps (break a run),
the H43 clear spans are dropped, punctuation-class boxes (BLOB, HOOK-L, DASH-H) are left out of the fit and written
to the key with an EMPTY value (score.py: reads nothing, does not break a run).
"""
import argparse, csv, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import gb

SWARM = os.path.dirname(HERE)


def control_stream(cid, part):
    rows = list(csv.DictReader(open(os.path.join(SWARM, 'controls', cid + '.tsv')), delimiter='\t'))
    out, last = [], None
    for r in rows:
        if part != 'all' and not r['line'].startswith(part + '_'): continue
        out.append(r['sign'])
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--text'); ap.add_argument('--control'); ap.add_argument('--part', default='all')
    ap.add_argument('--out', required=True); ap.add_argument('--shuffle-seed', type=int)
    ap.add_argument('--xspace', action='store_true')
    ap.add_argument('--restarts', type=int, default=60); ap.add_argument('--iters', type=int, default=5000000)
    ap.add_argument('--seed', type=int, default=1)
    a = ap.parse_args()
    gb.ROBUST = 0.1; gb.SPACE = a.xspace
    punct = set()
    if a.control:
        stream = control_stream(a.control, a.part)
    else:
        stream = gb.target_stream(a.text)
        punct = gb.PUNCT
    if a.shuffle_seed is not None:
        stream = gb.shuffled_stream(stream, a.shuffle_seed)
    signs, seq = gb.encode(stream)
    fix = {signs.index('X'): 26} if a.xspace and 'X' in signs else None
    best, key, rs = gb.run_solver(seq, len(signs), a.restarts, a.iters, a.seed, 1.0, 2.5, fix=fix,
                                  model=gb.MODELS['s' if a.xspace else 5])
    with open(a.out, 'w') as f:
        f.write('sign\tvalue\n')
        for s, v in zip(signs, key):
            f.write(f'{s}\t{"" if v == 26 else chr(97 + v)}\n')
        for s in sorted(punct):
            f.write(f'{s}\t\n')
    nwin = sum(1 for i in range(len(seq) - 4) if min(seq[i:i + 5]) >= 0)
    print(f'{a.out}\tN {sum(1 for c in seq if c >= 0)}\tK {len(signs)}\tscore {best:.3f}\tper_window {best / nwin:.4f}')


if __name__ == '__main__':
    main()
