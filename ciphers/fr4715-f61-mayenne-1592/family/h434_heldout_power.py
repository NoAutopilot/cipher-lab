#!/usr/bin/env python3
"""H434 (runner 16 session_01Vtwc6CEJD2BSnYdzzY4f8W, 29 Sept 2026), script-only, before any gloss: is H430's gate powered at the cell counts the
person's glosses would give? N per source = the two-way cells H430 would score if every agreed cell got a gloss letter (an upper bound; real
glosses cover fewer: f.108v's is sparse, about 40 words). Population = H423's per-cell record on f.61's own hand (f61 hidden spans + f108r
overlay, 97 cells: chooser right?, unigram right?), resampled with replacement (seed 434, 2000 draws); criterion (1) of H430's gate only (exact
McNemar one-sided p < 0.05 and chooser > unigram) -- (2) and (3) need chooser reruns and are not simulated, so this power is an upper bound.
A miss of H430 at an N whose power here is < 0.80 reads as 'untestable at this N', not a negative (rule 3, ARM3-ADJ).  [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); CHECK = "--check" in sys.argv; sys.argv = sys.argv[:1]; sys.path.insert(0, HERE)
import h423_ctx_chooser as c, h430_ctx_heldout as h
def main():
    pop = []
    for n in ("f61", "f108r"):
        segs = c.LEAVES[n](); ok, _ = c.run(segs)
        for (si, i), a in ok.items(): pop.append((a, max(segs[si][i]["c"], key=c.uni) == segs[si][i]["t"]))
    Ns = {}
    for name, (_, sf, _) in h.SOURCES.items():
        segs, _ = sf(); Ns[name] = sum(1 for s in segs for x in s if len(x["c"]) == 2 and x.get("ab", True))
    out = [f"population: f.61's hand, {len(pop)} cells, chooser {sum(a for a, _ in pop)}, unigram {sum(b for _, b in pop)}",
           "upper-bound N (agreed two-way cells if all glossed): " + "; ".join(f"{k} {v}" for k, v in Ns.items())]
    rng = random.Random(434)
    for label, N in (("f108r alone", Ns["f108r (ASKS 88)"]), ("f211r alone", Ns["f211r (ASKS 93)"]), ("f108v alone", Ns["f108v (ASKS 89)"]),
                     ("f108v at half coverage", Ns["f108v (ASKS 89)"] // 2), ("all three", sum(Ns.values())), ("N 30", 30), ("N 45", 45), ("N 60", 60)):
        hit = 0
        for _ in range(2000):
            s = [rng.choice(pop) for _ in range(N)]; k = sum(a for a, _ in s); u = sum(b for _, b in s)
            b_ = sum(1 for a, b in s if a and not b); cc = sum(1 for a, b in s if b and not a)
            hit += (k > u and b_ + cc > 0 and c.binom_p(b_, b_ + cc) < 0.05)
        out.append(f"{label} (N {N}): power of criterion (1) = {hit/2000:.3f}")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h434_heldout_power_result.txt"
    if CHECK:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
