#!/usr/bin/env python3
"""MONL-KING (20 Oct 2026): is f.166 (aid item 66, decipherment, 2 May 1573) the decipherment of the king's letter ff.132-136?

Usage: python3 king_f166.py [--draws 200] [--seed 166]
Registered in PREREG-MONL-KING.md before the first run. Reads leaf/passes/{c258,c264,c269}_read.tsv (MONL-LEAF blind reads, unchanged),
clear_f166.tsv and clear_f140.tsv; uses align_c268.py's DP and key.tsv. Per (read, clear letter): confirm share of keyed tokens
aligned against the whole letter (local span), and the longest exact run of decoded letters found in the letter; null = word-shuffled
copies of the same letter. Prints one JSON line per pair and writes results_king_f166.json.
"""
import argparse, json, random, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / 'leaf'))
import align_c268 as A
import leaf_score as LS


def letter(name):
    A.CLEAR = name
    return [w[2] for w in A.load_clear()]


def longest_run(dec, text):
    best = 0
    for i in range(len(dec)):
        for j in range(i + best + 1, len(dec) + 1):
            if dec[i:j] in text: best = j - i
            else: break
    return best


def decoded(toks):
    return ''.join(t['value'] for t in toks if t['value'])


def run(read, clear_name, draws, seed):
    toks = LS.tokens(HERE / 'leaf' / 'passes' / read)
    ws = letter(clear_name); text = ''.join(ws); dec = decoded(toks)
    real = LS.share(toks, text); rrun = longest_run(dec, text)
    rng = random.Random(seed); sh, rn = [], []
    for _ in range(draws):
        w = ws[:]; rng.shuffle(w); s = ''.join(w)
        sh.append(LS.share(toks, s)); rn.append(longest_run(dec, s))
    sh.sort(); p95 = sh[int(0.95 * (draws - 1))]
    return {'read': read, 'clear': clear_name, 'tokens': len(toks), 'keyed': sum(t['value'] is not None for t in toks),
            'real': real, 'p95': p95, 'margin': round(real - p95, 4), 'run': rrun, 'run_null_max': max(rn),
            'run_null_p95': sorted(rn)[int(0.95 * (draws - 1))],
            'placed': real - p95 >= 0.10 and rrun > max(rn)}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--draws', type=int, default=200); ap.add_argument('--seed', type=int, default=166)
    a = ap.parse_args()
    out = []
    for read, clear in (('c269_read.tsv', 'clear_f140.tsv'), ('c269_read.tsv', 'clear_f166.tsv'),
                        ('c258_read.tsv', 'clear_f166.tsv'), ('c264_read.tsv', 'clear_f166.tsv')):
        r = run(read, clear, a.draws, a.seed); out.append(r); print(json.dumps(r), flush=True)
    (HERE / 'results_king_f166.json').write_text(json.dumps(out, indent=1) + '\n')


if __name__ == '__main__':
    main()
