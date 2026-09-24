#!/usr/bin/env python3
"""Step 3, matched control (rule 3): 1,000 random 13-symbol strings with Z13's layout (8 at positions 5, 7, 9;
non-letter symbols at 4 and 10; uniform random A-Z at the 8 letter positions 1, 2, 3, 6, 8, 11, 12, 13), seed 13.
 (a) the poster's exact fixed rules (Params() and POSTER_OPS): share with a name6 hit (given name >= 6 letters)
 (b) the poster's global Params, with each letter free to take any op in {L, M, S, LM, X}: share with name6, name7
 (c) the whole step-2 family (1,280 Params rows x free ops): share with name7
 (d) the same family: share with name6 (a given name of >= 6 letters, the class ARTHUR belongs to)
Writes control.tsv (one row per string) and prints the rates.
"""
import random, sys
from multiprocessing import Pool
from mechanism import run, POSTER, load
from namecheck import names_in
from enumerate import options, dp, grid

LETTER_POS = [1, 2, 3, 6, 8, 11, 12, 13]
N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000


def make(rng):
    z = load()
    t = list(z)
    for k in LETTER_POS:
        t[k - 1] = rng.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return t


def one(t):
    o = run(t)
    a = bool(o and names_in(o, "name6"))
    seq = options(t, POSTER)
    _, g6, l6 = dp(seq, "name6")
    _, g7, l7 = dp(seq, "name7")
    c = d = False
    dl = set()
    for p in grid():
        seq = options(t, p)
        c = c or bool(dp(seq, "name7")[1])
        _, g, l = dp(seq, "name6")
        if g:
            d = True
            dl |= l
    return "".join(t), o or "", a, g6 > 0, g7 > 0, c, d, ";".join(sorted(dl))[:200]


if __name__ == "__main__":
    rng = random.Random(13)
    strings = [make(rng) for _ in range(N)]
    real = one(load())
    with Pool(4) as pool:
        res = pool.map(one, strings, chunksize=10)
    with open("control.tsv", "w") as f:
        f.write("string\tfixed_rule_output\ta_fixed_name6\tb_freeops_name6\tb_freeops_name7\tc_family_name7\td_family_name6\td_name6_labels\n")
        f.write("\t".join(map(str, real)) + "\t# the real Z13\n")
        for r in res:
            f.write("\t".join(map(str, r)) + "\n")
    for i, lab in [(2, "a fixed rules, name6"), (3, "b free ops, name6"), (4, "b free ops, name7"), (5, "c family, name7"), (6, "d family, name6")]:
        print(f"{lab}: {sum(r[i] for r in res)}/{N}   real Z13: {real[i]}")
