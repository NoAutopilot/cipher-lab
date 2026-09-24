#!/usr/bin/env python3
"""Step 2: run every combination of the rule family on the unchanged Z13 and count name hits.

Family: Params grid (move 4 x npass 0-3 x slide_dir 2 x count 6-10 x start1 2 x count_dir 2 x boundary 2 = 1,280)
times one op from {L, M, S, LM, X} for each of the 8 cipher letters (5^8 = 390,625): 500,000,000 combinations.
Counted exactly by a dynamic programme over positions (states = partial name matches), not by listing.
Writes enum.tsv (per Params row) and names_found.tsv (every distinct name7 label, with how many Params rows give it).
"""
import itertools, collections, sys
from mechanism import Params, T, op_out, chain, load, POSTER
from namecheck import feed_str

OPS = ["L", "M", "S", "LM", "X"]


def options(tokens, p):
    n8 = [k for k, t in enumerate(tokens, 1) if t == "8"]
    ch = chain(tokens[p.chain_from - 1], len(n8), p)
    seq = []
    for k, t in enumerate(tokens, 1):
        if t == "8":
            seq.append({ch[n8.index(k)]: 1})
        elif t.isalpha():
            d = collections.Counter()
            for op in OPS:
                s = op_out(t, op, p)
                if s is not None:
                    d[s] += 1
            seq.append(dict(d))
    return seq


def dp(seq, mode="name7", collect=True):
    """Returns (total combos, combos with a hit, set of labels reachable)."""
    states = {(frozenset(), False): 1}
    labels = set()
    for opts in seq:
        new = collections.Counter()
        for (act, hit), n in states.items():
            for s, m in opts.items():
                a2, h = feed_str(act, s, mode)
                if h:
                    labels |= h
                new[(a2, hit or bool(h))] += n * m
        states = new
    tot = sum(states.values())
    good = sum(n for (a, h), n in states.items() if h)
    return tot, good, labels


def grid():
    for mv, np_, sd, c, s1, cd, b in itertools.product(["UR", "UL", "DR", "DL"], range(4), [1, -1], range(6, 11),
                                                       [True, False], [-1, 1], ["reflect", "wrap"]):
        yield Params(mv, np_, sd, c, s1, cd, b, 3)


if __name__ == "__main__":
    z = load()
    cache = {}
    rows, allnames = [], collections.Counter()
    T_tot = T_good = 0
    fixed_ops_hits = 0
    for p in grid():
        seq = options(z, p)
        key = repr(seq)
        if key not in cache:
            cache[key] = dp(seq)
        tot, good, labels = cache[key]
        T_tot += tot; T_good += good
        for l in labels:
            allnames[l] += 1
        rows.append((p, tot, good, len(labels)))
    with open("enum.tsv", "w") as f:
        f.write("move\tnpass\tslide_dir\tcount\tstart1\tcount_dir\tboundary\tcombos\tcombos_with_name7\tdistinct_name7\n")
        for p, tot, good, nl in rows:
            f.write(f"{p.move}\t{p.npass}\t{p.slide_dir}\t{p.count}\t{p.start1}\t{p.count_dir}\t{p.boundary}\t{tot}\t{good}\t{nl}\n")
    with open("names_found.tsv", "w") as f:
        f.write("label\tletters\tparam_rows_giving_it\n")
        for l, n in sorted(allnames.items(), key=lambda t: (-len(t[0].replace('+', '')), -t[1], t[0])):
            f.write(f"{l}\t{len(l.replace('+', ''))}\t{n}\n")
    print(f"combos {T_tot} with name7 {T_good} share {T_good / T_tot:.4f}; distinct labels {len(allnames)}; "
          f"param rows with >=1 name7 {sum(1 for r in rows if r[2])}/{len(rows)}; distinct DP inputs {len(cache)}")
