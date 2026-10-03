#!/usr/bin/env python3
"""FT4v (account-4, 3 Oct 2026): f.252r 15 groups vs their interlinear gloss (PREREG-FT4v.md, pushed before any pass or score).
No C pin and no repeated code in the pair, so E is scored only with key.tsv M values pinned: P188 lar, P121 ons, P10 a, PALL.
Solver/E: ft4s_seg.solve_pins / E unchanged (<= 1 edit, MAXLEN 12). Controls seed 3, n 40, (s) gloss words shuffled, (g) groups shuffled.
  python3 ft4v_pair.py --pins P10 --real [--text literal|primary|est]
  python3 ft4v_pair.py --pins P10 --ctrl s
  python3 ft4v_pair.py --ambig            (registered C readout: feasible chunk count per group, no pins, 0 edits)
"""
import argparse, os, random, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ft4s_seg as fs

HERE = os.path.dirname(os.path.abspath(__file__))
PINSETS = {'P188': {'188': 'lar'}, 'P121': {'121': 'ons'}, 'P10': {'10': 'a'},
           'PALL': {'188': 'lar', '121': 'ons', '10': 'a'}}
TEXTS = {'primary': 'general marulli en depuis plusieurs jours de retour a bologne',
         'literal': 'gnal marulli en depuis plrs jours de retour a bologne',
         'est': 'general marulli est depuis plusieurs jours de retour a bologne'}


def load(which):
    toks = [t for l in open(os.path.join(HERE, '..', 'ciphertext_f252r.txt')) if not l.startswith('#') for t in l.split()]
    words = TEXTS[which].split()
    assert len(toks) == 15 and len(set(toks)) == 15
    return toks, words


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pins', choices=list(PINSETS))
    ap.add_argument('--text', default='primary', choices=list(TEXTS))
    ap.add_argument('--real', action='store_true')
    ap.add_argument('--ctrl', choices=['s', 'g'])
    ap.add_argument('--ambig', action='store_true')
    ap.add_argument('--n', type=int, default=40)
    ap.add_argument('--seed', type=int, default=3)
    a = ap.parse_args()
    toks, words = load(a.text)
    text = ''.join(words)
    if a.ambig:
        n, L, M = len(toks), len(text), fs.MAXLEN
        for i, t in enumerate(toks):
            ch = set()
            for p in range(L):
                for l in range(1, M + 1):
                    if p + l <= L and i <= p <= M * i and (n - i - 1) <= L - p - l <= M * (n - i - 1):
                        ch.add(text[p:p + l])
            print(f'group {i} {t} feasible_chunks {len(ch)}')
        return
    pins = PINSETS[a.pins]
    if a.real:
        t0 = time.time()
        miss = [c for c, v in pins.items() if v not in text]
        e = fs.E(toks, text, pins, 10)
        print(f'real {a.pins} text {a.text} E {e} {time.time() - t0:.1f}s' + (f' nochunk {miss}' if miss else ''))
        return
    rng = random.Random(a.seed)
    js, jg = [], []
    for _ in range(a.n):
        x = words[:]; rng.shuffle(x); js.append((toks, ''.join(x)))
    for _ in range(a.n):
        x = toks[:]; rng.shuffle(x); jg.append((x, text))
    hits = unres = 0
    for i, (tk, tx) in enumerate(js if a.ctrl == 's' else jg):
        e = fs.E(tk, tx, pins, 10)
        hits += e != 0; unres += e is None
        print(f'draw {a.ctrl} {i} E {e}')
    print(f'ctrl {a.ctrl} {a.pins} text {a.text} E1 {hits}/{a.n} (unresolved {unres}) share {hits / a.n:.3f}')


if __name__ == '__main__':
    main()
