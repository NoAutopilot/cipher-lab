#!/usr/bin/env python3
"""GAPS185 crib test (PREREG-GAPS185.md): does R5006 share R5005's two-digit pair profile, and do
Bourdeau's 7 published gloss values (grade I, dbourdeau/cyphersolver, CC BY 4.0) occur in R5006 above chance?

Usage: python3 crib_test.py [--target r5007] [--check]   (--check exits 1 if the output json is stale)
Default target r5006 -> crib_test.json (GAPS185). --target r5007 -> crib_test_r5007.json (PREREG-GAPS196: same
statistics, seed 196, power windows of the target's own N, plus T1 against R5006 as a descriptive extra).
"""
import json, math, random, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SRC = ROOT / "sources/cyphersolver/2026-10-03/zeschau1841"
PINS = {"11": "la", "70": "pre", "82": "m", "34": "i", "29": "er", "40": "e", "46": "que"}
SEED, NDRAW, NWIN, NWDRAW = 185, 2000, 200, 200


def pairs(s, phase):
    s = s[phase:]
    return [s[i:i + 2] for i in range(0, len(s) - 1, 2)]


def counts(ps):
    c = [0] * 100
    for p in ps:
        c[int(p)] += 1
    return c


def ic(c):
    n = sum(c)
    return sum(x * (x - 1) for x in c) / (n * (n - 1))


def best_pairs(s):
    a, b = pairs(s, 0), pairs(s, 1)
    return a if ic(counts(a)) >= ic(counts(b)) else b


def cos(u, v):
    return sum(x * y for x, y in zip(u, v)) / math.sqrt(sum(x * x for x in u) * sum(y * y for y in v))


def cover(ps):
    return sum(p in PINS for p in ps) / len(ps)


def spearman(x, y):
    def rank(v):
        o = sorted(range(len(v)), key=lambda i: v[i]); r = [0.0] * len(v); i = 0
        while i < len(o):
            j = i
            while j + 1 < len(o) and v[o[j + 1]] == v[o[i]]:
                j += 1
            for k in range(i, j + 1):
                r[o[k]] = (i + j) / 2
            i = j + 1
        return r
    rx, ry = rank(x), rank(y); mx, my = sum(rx) / len(rx), sum(ry) / len(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = math.sqrt(sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry))
    return num / den if den else 0.0


TARGETS = {"r5006": (("r5006p1_ciphertext.txt", "r5006p2_ciphertext.txt"), SEED, "crib_test.json"),
           "r5007": (("r5007p2l_ciphertext.txt", "r5007p2r_ciphertext.txt"), 196, "crib_test_r5007.json")}


def stream(files):
    return "".join(l.split()[-1] for f in files
                   for l in (HERE / "transcription" / f).read_text().splitlines() if l.strip())


def main():
    tgt = sys.argv[sys.argv.index("--target") + 1] if "--target" in sys.argv else "r5006"
    files, seed, outname = TARGETS[tgt]
    r6 = stream(files)
    assert r6.isdigit() and (tgt != "r5006" or len(r6) == 692), len(r6)
    N = len(r6)
    off = json.loads((SRC / "offsets.json").read_text())
    r5_lines = []
    for l in (SRC / "ct_R5005.txt").read_text().splitlines():
        if l.strip():
            tag, d = l.split()[:2]
            r5_lines.append((tag, d))
    r5_pairs = [p for tag, d in r5_lines for p in pairs(d, off.get(tag, 0))]
    c5 = counts(r5_pairs)
    rng = random.Random(seed)

    p6 = best_pairs(r6); c6 = counts(p6)
    phase = 0 if p6 == pairs(r6, 0) else 1
    t1, t2 = cos(c6, c5), cover(p6)
    null1, null2 = [], []
    digs = list(r6)
    for _ in range(NDRAW):
        rng.shuffle(digs); q = best_pairs("".join(digs))
        null1.append(cos(counts(q), c5)); null2.append(cover(q))
    pv = lambda t, nl: (1 + sum(x >= t for x in nl)) / (1 + len(nl))
    pc = lambda nl: sorted(nl)[int(0.95 * len(nl))]

    # positive control: N-digit windows (N=692 for R5006) of R5005 (stream in Bourdeau's line order) vs the rest of R5005
    s5 = "".join(d for _, d in r5_lines)
    hits, wt, wn = 0, [], []
    for _ in range(NWIN):
        st = rng.randrange(0, len(s5) - N)
        w = s5[st:st + N]; rest = counts(best_pairs(s5[:st])) if st > 1 else [0] * 100
        r2 = counts(best_pairs(s5[st + N:])) if len(s5) - st - N > 1 else [0] * 100
        crest = [a + b for a, b in zip(rest, r2)]
        t = cos(counts(best_pairs(w)), crest); wd = list(w); nl = []
        for _ in range(NWDRAW):
            rng.shuffle(wd); nl.append(cos(counts(best_pairs("".join(wd))), crest))
        p = pv(t, nl); hits += p < 0.01; wt.append(t); wn.append(sum(nl) / len(nl))

    pin_r6 = {k: c6[int(k)] for k in PINS}; pin_r5 = {k: c5[int(k)] for k in PINS}
    out = {
        "n_digits_r6": len(r6), "phase_r6": phase, "n_pairs_r6": len(p6), "ic_r6": round(ic(c6), 4),
        "n_pairs_r5": len(r5_pairs), "ic_r5": round(ic(c5), 4),
        "T1_cosine_target": round(t1, 4), "T1_null_mean": round(sum(null1) / NDRAW, 4),
        "T1_null_p95": round(pc(null1), 4), "T1_p": round(pv(t1, null1), 5),
        "T2_pin_cover_target": round(t2, 4), "T2_null_mean": round(sum(null2) / NDRAW, 4),
        "T2_null_p95": round(pc(null2), 4), "T2_p": round(pv(t2, null2), 5),
        "T2_pin_cover_r5005": round(cover(r5_pairs), 4),
        "T3_spearman_pins_r6_vs_r5": round(spearman(list(pin_r6.values()), list(pin_r5.values())), 3),
        "pin_counts_r6": pin_r6, "pin_counts_r5": pin_r5,
        "power_windows": NWIN, "power_share_p_lt_0.01": round(hits / NWIN, 3),
        "power_window_cos_mean": round(sum(wt) / NWIN, 4), "power_window_null_mean": round(sum(wn) / NWIN, 4),
        "top10_pairs_r6": sorted(((c6[i], f"{i:02d}") for i in range(100)), reverse=True)[:10],
        "top10_pairs_r5": sorted(((c5[i], f"{i:02d}") for i in range(100)), reverse=True)[:10],
    }
    if tgt != "r5006":
        out = {"target": tgt, "files": list(files), "seed": seed, **out}
        c6ref = counts(best_pairs(stream(TARGETS["r5006"][0])))
        out["descriptive_T1_cosine_vs_r5006"] = round(cos(c6, c6ref), 4)
        out["descriptive_T1_null_mean_vs_r5006"] = round(sum(cos(counts(best_pairs("".join(rng.sample(r6, N)))), c6ref)
                                                             for _ in range(NDRAW)) / NDRAW, 4)
    js = json.dumps(out, indent=1) + "\n"
    f = HERE / outname
    if "--check" in sys.argv:
        if not f.exists() or f.read_text() != js:
            print("STALE", outname); sys.exit(1)
        print(outname, "up to date"); return
    f.write_text(js); print(js)


if __name__ == "__main__":
    main()
