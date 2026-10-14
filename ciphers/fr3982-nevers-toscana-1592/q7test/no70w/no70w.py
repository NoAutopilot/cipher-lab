#!/usr/bin/env python3
"""NO70-WORDS (PREREG-NO70-WORDS.md): power of q7test/screen.py for key no.70 alphabet + barred-figure word codes at the
measured f.25 transcription error, then the f.25 target run (only screen.py's own target mode; this file adds the 8-loss
condition and the 0.115/0.160 levels).

  python3 q7test/no70w/no70w.py power [--texts 50] [--nulls 100]   C1 0.115, C2 0.160, C3 8-loss + 0.07 (seed 70)
The target run is: python3 q7test/screen.py target --key q7test/key_no70_full_codes.tsv
Offline; deterministic for a given worker count.
"""
import argparse, json, os, random, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import numpy as np
from multiprocessing import Pool
import screen

KEY = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'key_no70_full_codes.tsv')

def eight_loss(s, rng):
    return ''.join(rng.choice(['6', '3', '01', '']) if c == '8' else c for c in s)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('mode', choices=['power']); ap.add_argument('--texts', type=int, default=50)
    ap.add_argument('--nulls', type=int, default=100); ap.add_argument('--workers', type=int, default=4)
    ap.add_argument('--build', default=os.environ.get('Q7_BUILD', '/tmp/q7build'))
    a = ap.parse_args()
    ent = screen.load_key(KEY); screen._init(a.build, ['it'])
    seed = 70; rng = random.Random(seed)
    base = [screen.encipher(w, ent, rng, 280) for w in screen.windows(rng, a.texts)]
    conds = [('C1', 0.115, False), ('C2', 0.160, False), ('C3', 0.07, True)]
    with Pool(a.workers, initializer=screen._init, initargs=(a.build, ['it'])) as pool:
        for name, lev, loss in conds:
            r2 = random.Random(seed * 100 + int(lev * 1000) + (7 if loss else 0))
            tx = []
            for s in base:
                t = eight_loss(s, r2) if loss else s
                tx.append(screen.corrupt(t, lev, r2)[:260])
            res = pool.map(screen._job, [(s, ent, 'it', a.nulls, a.nulls, seed * 10000 + i + (500 if loss else int(lev * 1000))) for i, s in enumerate(tx)])
            det = [screen.detect(*r) for r in res]
            print(json.dumps(dict(cond=name, level=lev, eight_loss=loss, texts=len(tx), nulls_each=a.nulls,
                  power=round(sum(det) / len(tx), 3), mean_S=round(float(np.mean([r[0] for r in res])), 4),
                  det_a=round(sum(r[0] > max(r[1]) for r in res) / len(tx), 3),
                  det_b=round(sum(r[0] > max(r[2]) for r in res) / len(tx), 3))), flush=True)

if __name__ == '__main__':
    main()
