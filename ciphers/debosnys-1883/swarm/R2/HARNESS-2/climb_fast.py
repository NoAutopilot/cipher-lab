#!/usr/bin/env python3
"""HARNESS-2 reference climber (29 Sept 2026): selftest_climb.py's method (same pool, moves, schedule, 6 x 60000
default here as in README's reachability runs) with the inner loop in C (climb_fast.c, compiled on first use).
Reads its fit text through score.load_text, so it takes any score.py text id, including the harness's shuffled
refit texts (file:PATH). Usage: climb_fast.py FIT_ID OUT.tsv [--lang fr] [--restarts 6] [--iters 60000] [--seed 1]
As a refit command: --refit-cmd "python3 R2/HARNESS-2/climb_fast.py {fit} {out} --seed {seed}" (run from swarm/)."""
import argparse, os, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
sys.path.insert(0, str(HERE))
import score_v21 as score
FREQ = {'fr': 'eeeeeeeeeeeeeeesssssssaaaaaaaiiiiiiittttttnnnnnnnrrrrrruuuuuulllllooooodddcccmmmpppvvqfbgh',
        'en': 'eeeeeeeeeeeettttttttaaaaaaaaoooooooiiiiiiinnnnnnnsssssshhhhhhrrrrrrddddllllcccuuummwwffggyypbvk',
        'pt': 'aaaaaaaaaaaaaeeeeeeeeeeeeooooooooooossssssrrrrrriiiiiinnnnnddddmmmmuuuutttccclllpppvvgqhf'}
_TAB = {}
def table(lang):
    p = HERE / f'_quad_{lang}.txt'
    if not p.exists():
        lp, floor, _ = score.model(lang)
        import itertools
        L = 'abcdefghijklmnopqrstuvwxyz'
        tmp = p.with_suffix(f'.{os.getpid()}')
        with open(tmp, 'w') as f:
            f.write('\n'.join(f'{lp.get(a+b+c+d, floor):.6f}' for a in L for b in L for c in L for d in L) + '\n')
        os.replace(tmp, p)
    return p.read_text()
if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('fit'); ap.add_argument('out')
    ap.add_argument('--lang', default='fr'); ap.add_argument('--restarts', type=int, default=6)
    ap.add_argument('--iters', type=int, default=60000); ap.add_argument('--seed', type=int, default=1)
    a = ap.parse_args()
    exe = HERE / 'climb_fast'
    if not exe.exists():
        subprocess.run(['gcc', '-O2', '-o', str(exe), str(HERE / 'climb_fast.c'), '-lm'], check=True)
    toks = score.flat(score.load_text(a.fit))
    signs = sorted(set(toks)); idx = {s: i for i, s in enumerate(signs)}
    inp = f'{len(signs)} {len(toks)}\n' + ' '.join(str(idx[t]) for t in toks) + '\n' + table(a.lang) + \
          f'{FREQ.get(a.lang, FREQ["fr"])}\n{a.restarts} {a.iters} {a.seed}\n'
    o = subprocess.run([str(exe)], input=inp, capture_output=True, text=True, check=True).stdout.split('\n')
    open(a.out, 'w').write(''.join(f'{s}\t{v}\n' for s, v in zip(signs, o[0])))
    print(f'{a.fit} lang={a.lang} best={float(o[1]):.3f} per quad')
