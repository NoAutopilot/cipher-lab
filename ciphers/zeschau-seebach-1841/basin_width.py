#!/usr/bin/env python3
"""R10-ZESBASIN: basin width of the R9-ZESCH word-parse objective on its matched control (PREREG-R10-ZESBASIN.md).

Not a search for the target's key. Starts at the control's TRUE key, applies k random code-code swaps among the free
(non-pin) codes (k = 1, 2, 4, 8, 16, 32; DRAWS draws each), and records J (wordseg_syllabary.WordLM.llr summed over
20-token chunks, imported unchanged) and whether ONE greedy pass returns the key to the true key exactly.
One greedy pass = one sweep over every unordered pair of free codes in a fixed shuffled order, applying a swap
whenever it raises J (first-improvement); the pass ends after the last pair. "Returned" = every free code maps to its
true unit again. Also reported: codes still wrong after the pass, J after the pass, and whether it ends above true J.
Usage: python3 basin_width.py run | --check      (--check re-runs and exits 1 if basin_width.json is stale, rule 7)
"""
import itertools, json, random, sys
from multiprocessing import Pool
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import wordseg_syllabary as W  # noqa: E402

KS = (1, 2, 4, 8, 16, 32)
DRAWS = 50
SEED = 10100
OUT = HERE / "basin_width.json"
S = None


def init():
    global S
    held, lms, inv, segs, truth, pins, tm, units, K = W.build_control()
    ch = W.chunks_of(segs)
    codes = sorted({int(c) for _, cs in segs for c in cs})
    free = [c for c in codes if c not in pins]
    where = {c: set(k for k, (_, cs) in enumerate(ch) if (cs == c).any()) for c in codes}
    S = dict(lms=lms, inv=inv, ch=ch, free=free, where=where, tm=tm)


def score(m, k):
    lang, cs = S["ch"][k]
    return S["lms"][lang].llr("".join(S["inv"][m[c]] for c in cs))


def one(args):
    k, draw = args
    rng = random.Random(SEED * 1000 + k * 100 + draw)
    free, where, tm = S["free"], S["where"], S["tm"]
    m = tm.copy()
    for _ in range(k):
        a, b = rng.sample(free, 2)
        m[a], m[b] = m[b], m[a]
    wrong0 = sum(int(m[c] != tm[c]) for c in free)
    ss = [score(m, i) for i in range(len(S["ch"]))]
    J0 = sum(ss)
    pairs = list(itertools.combinations(free, 2))
    rng.shuffle(pairs)
    acc = 0
    for a, b in pairs:
        if m[a] == m[b]:
            continue
        m[a], m[b] = m[b], m[a]
        ks = where[a] | where[b]
        new = {i: score(m, i) for i in ks}
        d = sum(new[i] - ss[i] for i in ks)
        if d > 1e-9:
            for i in ks:
                ss[i] = new[i]
            acc += 1
        else:
            m[a], m[b] = m[b], m[a]
    wrong1 = sum(int(m[c] != tm[c]) for c in free)
    return {"k": k, "draw": draw, "codes_wrong_start": wrong0, "J_start": round(J0, 2),
            "codes_wrong_after": wrong1, "J_after": round(sum(ss), 2), "swaps_accepted": acc,
            "returned": wrong1 == 0}


def run():
    init()
    true_J = round(sum(score(S["tm"], i) for i in range(len(S["ch"]))), 2)
    jobs = [(k, d) for k in KS for d in range(DRAWS)]
    with Pool(4, initializer=init) as p:
        rows = p.map(one, jobs)
    summ = []
    for k in KS:
        r = [x for x in rows if x["k"] == k]
        n = len(r)
        summ.append({"k": k, "n": n,
                     "mean_codes_wrong_start": round(sum(x["codes_wrong_start"] for x in r) / n, 2),
                     "mean_J_start": round(sum(x["J_start"] for x in r) / n, 1),
                     "min_J_start": min(x["J_start"] for x in r), "max_J_start": max(x["J_start"] for x in r),
                     "share_J_start_below_true": round(sum(x["J_start"] < true_J for x in r) / n, 3),
                     "return_fraction": round(sum(x["returned"] for x in r) / n, 3),
                     "mean_codes_wrong_after": round(sum(x["codes_wrong_after"] for x in r) / n, 2),
                     "share_after_above_true_J": round(sum(x["J_after"] > true_J + 1e-6 for x in r) / n, 3)})
    width = max([s["k"] for s in summ if s["return_fraction"] >= 0.5], default=0)
    if width >= 8:
        verdict = "WIDE: a near-key instrument (crib- or partial-key-seeded) can use this objective"
    elif width == 0:
        verdict = "NO BASIN: objective retired at this N"
    else:
        verdict = "NARROW: usable only from a start within %d swaps; retire for search unless such a seed exists" % width
    res = {"objective": "wordseg_syllabary word-parse LLR (unchanged)", "control": "wordseg_syllabary.build_control()",
           "free_codes": len(S["free"]), "true_key_J": true_J, "draws_per_k": DRAWS, "seed": SEED,
           "summary": summ, "basin_width_k": width, "verdict": verdict, "rows": rows}
    return res


if __name__ == "__main__":
    if sys.argv[1:] == ["--check"]:
        new = run()
        old = json.loads(OUT.read_text())
        sys.exit(0 if new == old else 1)
    if sys.argv[1:] == ["--time"]:
        import time
        init(); t = time.time(); print(one((32, 0))["swaps_accepted"], time.time() - t)
        sys.exit(0)
    res = run()
    OUT.write_text(json.dumps(res, indent=1) + "\n")
    for s in res["summary"]:
        print(s)
    print("width", res["basin_width_k"], res["verdict"])
