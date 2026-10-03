#!/usr/bin/env python3
"""Score a primitive-level reading of the signature's 'H' (GAPS183, 3 Oct 2026) against Duployé phonetic spellings
of the hypotheses and against two nulls: random same-length strings from the 18-letter inventory, and decoy French
place names (northern front towns) spelt the same way. Statistic: best local edit similarity of the hypothesis
inside the reading (1 - edits/len(hyp)), so a hypothesis can match any span of the reading.

  python3 sig_hypothesis_score.py --read "A G A B T B" [--seed 183 --trials 2000]
"""
import argparse, random
from duploye_control import INVENTORY, lev

HYP = {"ARRAS (a-r-a)": "A R A", "AVANT ARRAS": "A V A N T A R A", "DEVANT ARRAS": "D E V A N T A R A",
       "VON ARAS (Gerry 2017)": "V O N A R A S"}
DECOY = {"LILLE": "L I L", "LENS": "L A N S", "METZ": "M E S", "LYON": "L I O N", "PARIS": "P A R I",
         "CALAIS": "K A L E", "VERDUN": "V E R D N", "DOUAI": "D O E", "NANCY": "N A N S I", "REIMS": "R E M S"}


def local(hyp, read):
    best = len(hyp)
    for i in range(len(read) + 1):
        for j in range(i, len(read) + 1):
            best = min(best, lev(hyp, read[i:j]))
    return 1 - best / len(hyp)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--read", required=True); ap.add_argument("--seed", type=int, default=183)
    ap.add_argument("--trials", type=int, default=2000)
    a = ap.parse_args()
    read = a.read.split(); rng = random.Random(a.seed)
    print(f"reading: {' '.join(read)} (n={len(read)})")
    for name, s in list(HYP.items()) + [("--", "")] + list(DECOY.items()):
        if not s:
            print("-- decoys --"); continue
        h = s.split(); obs = local(h, read)
        null = sorted(local(h, [rng.choice(INVENTORY) for _ in read]) for _ in range(a.trials))
        p = sum(x >= obs for x in null) / a.trials
        print(f"{name:24s} sim={obs:.3f} null_mean={sum(null)/len(null):.3f} null_p95={null[int(.95*len(null))]:.3f} p={p:.3f}")


if __name__ == "__main__":
    main()
