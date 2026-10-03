#!/usr/bin/env python3
"""GF4c (3 Oct 2026): is the 22 Dec 1812 Berthier page in the Napoleon-Davout Nov 1813 grand chiffre?

Source: Bazeries 1896, *Les chiffres de Napoleon Ier pendant la campagne de 1813*, pp.38-45, as reproduced
verbatim by J.-F. Bouchaudy, jfbouch.fr/crypto/napoleon/ex_grd_chif.fr.html (snapshot
sources/jfbouch/2026-10-03/, fetched 3 Oct 2026; Bouchaudy marks plain-text numbers with a leading '_').
Bouchaudy did not publish his key; no value->meaning table is used here. Key source class: `published`
(Bazeries' cipher text and translation), not H.

Statistic: S = sum over test tokens of the reference letters' count of that value (value-frequency overlap).
If two texts share a code, the code's frequent values (de, a, et, la...) recur in both.
Shuffled-key control (rule 3): the reference's values are relabelled by a random permutation of 1..VMAX,
which keeps the reference's frequency profile but breaks the value identity; p = share of draws >= observed.
Positive control: Davout letters 2+3 (same code) subsampled to the target's N, against the same reference
(letter 1). Exit 1 if the committed results file is stale (--check).
"""
import collections, json, random, re, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SNAP = ROOT / "sources/jfbouch/2026-10-03/ex_grd_chif.fr.html"
# cipher-block line numbers in the snapshot (read by eye from the page, 3 Oct 2026)
RANGES = {1: [(41, 41), (45, 56), (65, 81), (88, 91), (95, 102), (112, 114)],
          2: [(142, 145), (155, 172), (182, 187)],
          3: [(205, 207), (209, 216)]}
VMAX, DRAWS, SEED = 1200, 20000, 1812

def codes():
    lines = SNAP.read_bytes().decode("cp1252", "replace").split("\n")
    out = {}
    for let, rr in RANGES.items():
        toks = []
        for a, b in rr:
            for ln in lines[a - 1:b]:
                toks += [int(x) for x in re.findall(r"(?<![_\d/])(\d+)(?![\d/])", ln) if int(x) <= VMAX]
        out[let] = toks
    return out

def S(test, ref):
    c = collections.Counter(ref)
    return sum(c[v] for v in test)

def pval(test, ref, rng):
    obs = S(test, ref); perm = list(range(1, VMAX + 1)); ge = 0; tot = 0.0
    for _ in range(DRAWS):
        rng.shuffle(perm); m = {v: perm[v - 1] for v in set(ref)}
        s = S(test, [m[v] for v in ref]); tot += s; ge += s >= obs
    return obs, tot / DRAWS, (ge + 1) / (DRAWS + 1)

def main():
    rng = random.Random(SEED)
    d = codes()
    target = [int(x) for x in (HERE.parent / "structure/flat.txt").read_text().split()]
    N = len(target)
    ref = d[1]
    pos_pool = d[2] + d[3]
    res = {"n_letter1": len(d[1]), "n_letter2": len(d[2]), "n_letter3": len(d[3]), "n_target": N,
           "vmax": VMAX, "draws": DRAWS, "seed": SEED}
    o, m, p = pval(target, ref, rng); res["target_vs_L1"] = {"obs": o, "null_mean": round(m, 2), "p": round(p, 5)}
    o, m, p = pval(target, d[1] + pos_pool, rng); res["target_vs_all"] = {"obs": o, "null_mean": round(m, 2), "p": round(p, 5)}
    rows = []
    for s in range(5):
        sub = random.Random(100 + s).sample(pos_pool, min(N, len(pos_pool)))
        o, m, p = pval(sub, ref, rng); rows.append({"seed": 100 + s, "n": len(sub), "obs": o, "null_mean": round(m, 2), "p": round(p, 5)})
    res["positive_control_L23_vs_L1"] = rows
    # positive control at a smaller N too (power check at the Davout letters' own scale)
    sub = random.Random(7).sample(pos_pool, 150); o, m, p = pval(sub, ref, rng)
    res["positive_control_N150"] = {"obs": o, "null_mean": round(m, 2), "p": round(p, 5)}
    out = json.dumps(res, indent=1)
    f = HERE / "value_overlap_results.json"
    if "--check" in sys.argv:
        if not f.exists() or f.read_text() != out + "\n": print("STALE"); sys.exit(1)
        print("OK"); return
    f.write_text(out + "\n"); print(out)

if __name__ == "__main__":
    main()
