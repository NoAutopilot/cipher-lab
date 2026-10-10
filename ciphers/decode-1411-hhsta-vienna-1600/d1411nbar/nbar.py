#!/usr/bin/env python3
"""D1411-NBAR (d1411nbar/PREREG-D1411NBAR.md): noise-matched gloss bar for the de1600 coverage of frozen T21r.
Encode gaps150/gloss_text.txt (tiled to N=308) through T21r into numbers drawn from the pooled independent numerals, inject
digit errors at registered rates, decode with T21r and score de1600 coverage; controls: noisy order-shuffle, noisy shifted rules.

  python3 d1411nbar/nbar.py           write d1411nbar/nbar.json, print the verdict
  python3 d1411nbar/nbar.py --check   exit 1 if nbar.json is stale (rule 7)
"""
import json, os, random, sys
H = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(H, "..")
sys.path.insert(0, os.path.join(F, "d1411pool"))
import score_pool as P  # noqa: E402
S5 = P.V.S  # d1411p5/score_p5 (dec, tabs, SEED)
J = P.J
N = 308; T21R_POOLED = 0.513; RATES = {"low": 0.06, "central": 0.123, "high": 0.25}; NSEED = 1000
SWEEP = [round(0.03 * i, 2) for i in range(14)]; NSWEEP = 200


def pool_numbers():
    ind = P.material(); counts = {k: len(v) for k, v in ind.items()}
    assert counts == P.EXPECT, counts
    return [n for _, n, _, _ in ind["p4"] + ind["p5"] + ind["p6"]]


def encoder(t, pool):
    by_res = {}
    for n in pool:
        by_res.setdefault(n % 24, []).append(n)
    res_of = {}
    for r in range(24):
        res_of.setdefault(t[r][0], []).append(r)

    def enc(text, rnd):
        out = []
        for ch in text:
            r = rnd.choice(res_of[ch])
            cand = by_res.get(r) or [n for n in range(1, 101) if n % 24 == r]
            out.append(rnd.choice(cand))
        return out
    return enc


def subst(n, rnd):
    d = list(str(n))
    while True:
        i = rnd.randrange(len(d)); x = d[:]
        x[i] = rnd.choice([c for c in "0123456789" if c != d[i]])
        v = int("".join(x))
        if v != 0:
            return v


def inject(nums, r, rnd, model="subst"):
    out = []; i = 0
    while i < len(nums):
        n = nums[i]
        if rnd.random() >= r:
            out.append(n); i += 1; continue
        kind = "sub" if model == "subst" else rnd.choices(("sub", "split", "merge"), weights=(70, 15, 15))[0]
        if kind == "split" and n >= 10:
            out.extend(int(c) for c in str(n)); i += 1; continue  # its digits as separate numbers
        if kind == "merge" and n < 10 and i + 1 < len(nums) and int(f"{n}{nums[i + 1]}") <= 100:
            out.append(int(f"{n}{nums[i + 1]}")); i += 2; continue
        out.append(subst(n, rnd)); i += 1
    return out


def run(model, t, enc, text, r, seed_base, nseed, controls=True, emodel="subst"):
    g, sh, sf = [], [], []
    for k in range(nseed):
        rnd = random.Random(seed_base + k)
        nums = enc(text, rnd)
        noisy = inject(nums, r, rnd, emodel)
        g.append(model.cover(S5.dec(noisy, t)))
        if controls:
            x = nums[:]; rnd.shuffle(x)
            sh.append(model.cover(S5.dec(inject(x, r, rnd, emodel), t)))
            sf.append(max(model.cover(S5.dec(noisy, t, s)) for s in range(1, 24)))
    return g, sh, sf


def q(xs, p):
    return round(J.pct(sorted(xs), p), 4)


def summ(g, sh, sf):
    B = q(g, .05)
    out = {"bar_p05": B, "median": q(g, .5), "p95": q(g, .95), "mean": round(sum(g) / len(g), 4)}
    if sh:
        out.update({"noisy_shuffle_p99": q(sh, .99), "noisy_shuffle_mean": round(sum(sh) / len(sh), 4),
                    "noisy_shifted_max_p99": q(sf, .99)})
        out["informative"] = bool(B > out["noisy_shuffle_p99"] and B > out["noisy_shifted_max_p99"])
    out["T21r_percentile"] = round(sum(x <= T21R_POOLED for x in g) / len(g), 4)
    return out


def main():
    model = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA["de1600"]])
    t = S5.tabs()["T21r"]; pool = pool_numbers(); enc = encoder(t, pool)
    g = open(os.path.join(F, "gaps150", "gloss_text.txt")).read().strip()
    text = (g * 5)[:N]
    res = {"prereg": "d1411nbar/PREREG-D1411NBAR.md", "N": N, "T21r_pooled": T21R_POOLED,
           "clean": {"gloss63": round(model.cover(g), 4), "tiled308": round(model.cover(text), 4),
                     "tiled308_T21r_roundtrip": round(model.cover(S5.dec(enc(text, random.Random(1411)), t)), 4)},
           "rates": RATES}
    for i, (name, r) in enumerate(RATES.items()):
        res[name] = summ(*run(model, t, enc, text, r, 1411 * 100000 + 10 ** 7 * i, NSEED))
    res["secondary_split_merge_central"] = summ(*run(model, t, enc, text, RATES["central"], 1411 * 100000 + 4 * 10 ** 7, NSEED,
                                                     emodel="splitmerge"))
    sw = []
    for j, r in enumerate(SWEEP):
        gg, _, _ = run(model, t, enc, text, r, 1411 * 100000 + (5 + j) * 10 ** 7, NSWEEP, controls=False)
        sw.append([r, q(gg, .5), q(gg, .05)])
    res["sweep_r_median_p05"] = sw
    cross = None
    for (r0, m0, _), (r1, m1, _) in zip(sw, sw[1:]):
        if m0 >= T21R_POOLED > m1:
            cross = round(r0 + (m0 - T21R_POOLED) / (m0 - m1) * (r1 - r0), 4); break
    res["rate_where_median_equals_T21r"] = cross
    c = res["central"]
    verdict = "NON-TEST" if not c["informative"] else ("PASS" if T21R_POOLED >= c["bar_p05"] else "FAIL")
    res["gate"] = {"bar_p05_central": c["bar_p05"], "informative": c["informative"], "T21r": T21R_POOLED, "verdict": verdict}
    txt = json.dumps(res, indent=1) + "\n"; pj = os.path.join(H, "nbar.json")
    if "--check" in sys.argv:
        ok = os.path.exists(pj) and open(pj).read() == txt
        print("d1411nbar", "current" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(pj, "w").write(txt); print(txt)


if __name__ == "__main__":
    main()
