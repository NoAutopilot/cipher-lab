#!/usr/bin/env python3
"""GAPS85 (3 Oct 2026, account-4): crib key from the GAPS79 reconciled R4284 key-test strip applied to the GAPS38
reconciled R4282, scored by la17 bigram log-prob against a shuffled-pair-assignment control and a positive control.
Pre-registered in PREREG.md. Disk only. --check re-derives and exits 1 if results.json is stale (rule 7)."""
import collections, csv, gzip, glob, json, math, os, random, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H); R = os.path.dirname(os.path.dirname(T))
CLEAR = ["effusorem", "sanguinis", "pestem", "patrie", "preter", "naturalem", "disturbatorem", "religionis"]
def norm(c): return {"j": "i", "v": "u"}.get(c, c)
def strip_words(path, relabel5):
    ws = []
    for line in open(path):
        if line.startswith("row"): continue
        row, codes = line.rstrip("\n").split("\t")
        for wi, w in enumerate(codes.split(" / ")):
            s = w.split()
            if row == "kt2" and wi == 0: s[0] = "L"
            if relabel5 and row in ("kt2", "kt4") and wi == 0: s[2] = "5" if s[2] == "s" else s[2]
            ws.append(s)
    return ws
def pairs_of(ws):
    return [(norm(l), s) for c, w in zip(CLEAR, ws) if len(c) == len(w) for l, s in zip(c, w)]
def key_of(pairs):
    by = collections.defaultdict(collections.Counter)
    for l, s in pairs: by[s][l] += 1
    return {s: sorted(cn.items(), key=lambda x: (-x[1], x[0]))[0][0] for s, cn in by.items()}
def lines_r4282():
    out = collections.OrderedDict()
    for r in csv.DictReader(open(os.path.join(T, "tx2/ciphertext_reconciled.tsv")), delimiter="\t"):
        out.setdefault(r["line"], []).append(r["sign"])
    return list(out.values())
A = "abcdefghiklmnopqrstuxyz"  # 23 after i/j, u/v merge (w absent in la17 Latin, kept below as rare)
def la17_text():
    t = []
    for f in sorted(glob.glob(os.path.join(R, "tools/data/la17/*.txt.gz"))):
        t.append(gzip.open(f, "rt", errors="ignore").read().lower())
    s = "".join(norm(c) for c in " ".join(t) if c.isalpha() and c.isascii())
    return s
def bigram_model(s):
    al = sorted(set(s)); c = collections.Counter(zip(s, s[1:])); u = collections.Counter(s[:-1]); V = len(al)
    return lambda a, b: math.log((c[(a, b)] + 1) / (u[a] + V))
def S(lines, key, lp):
    tot, n = 0.0, 0
    for ln in lines:
        for a, b in zip(ln, ln[1:]):
            if a in key and b in key: tot += lp(key[a], key[b]); n += 1
    return (tot / n if n else float("nan")), n
def perm_test(lines, pairs, lp, nperm, seed):
    real = S(lines, key_of(pairs), lp)
    rng = random.Random(seed); letters = [l for l, _ in pairs]; signs = [s for _, s in pairs]; ge = 0; vals = []
    for _ in range(nperm):
        rng.shuffle(letters); v = S(lines, key_of(list(zip(letters, signs))), lp)[0]; vals.append(v); ge += v >= real[0]
    vals.sort()
    return {"S_real": round(real[0], 4), "pairs_scored": real[1], "perm_mean": round(sum(vals) / len(vals), 4),
            "perm_p95": round(vals[int(0.95 * len(vals))], 4), "p": round((ge + 1) / (nperm + 1), 4)}
def main():
    nperm = 2000; text = la17_text(); lp = bigram_model(text); lines = lines_r4282()
    res = {"la17_letters": len(text), "r4282_signs": sum(map(len, lines)), "arms": {}}
    arms = [("A1", "passC_reconciled.tsv", True), ("A2", "passC_variant_kt3_onesign.tsv", True),
            ("A1_no5", "passC_reconciled.tsv", False)]
    for name, f, r5 in arms:
        pairs = pairs_of(strip_words(os.path.join(T, "r4284_leaf", f), r5)); key = key_of(pairs)
        cov = sum(1 for ln in lines for s in ln if s in key)
        d = perm_test(lines, pairs, lp, nperm, 85)
        d.update({"pairs": len(pairs), "key": dict(sorted(key.items())), "coverage": f"{cov}/{res['r4282_signs']}",
                  "gate": "PASS" if d["p"] < 0.05 else "FAIL", "gated": name != "A1_no5",
                  "sample": " ".join("".join(key.get(s, "_") for s in ln) for ln in lines[:4])})
        res["arms"][name] = d
    # positive control: la17 passages enciphered with the A1 key, 3.4% sign error
    pairs = pairs_of(strip_words(os.path.join(T, "r4284_leaf", "passC_reconciled.tsv"), True)); key = key_of(pairs)
    inv = collections.defaultdict(collections.Counter)
    for l, s in pairs: inv[l][s] += 1
    enc = {l: sorted(cn.items(), key=lambda x: (-x[1], x[0]))[0][0] for l, cn in inv.items()}
    signs = sorted(set(s for _, s in pairs)) + ["#"]; pc = []
    for seed in range(1, 6):
        rng = random.Random(seed); st = rng.randrange(0, len(text) - 1200); p = text[st:st + 1090]
        cs = [enc.get(c, "#") for c in p]
        cs = [rng.choice(signs) if rng.random() < 0.034 else c for c in cs]
        cl = [cs[i:i + 37] for i in range(0, len(cs), 37)]
        d = perm_test(cl, pairs, lp, nperm, 85); d["seed"] = seed
        d["coverage"] = f"{sum(1 for c in cs if c in key)}/{len(cs)}"; pc.append(d)
    res["positive_control"] = pc; res["positive_control_pass"] = f"{sum(d['p'] < 0.05 for d in pc)}/5"
    # post-hoc (not pre-registered; rule 3 subsample clause): same control with signs blanked to '#' so that
    # coverage matches R4282's A1 coverage (458/1090) and scored pairs fall near the target's 184
    pm = []
    for seed in range(1, 6):
        rng = random.Random(100 + seed); st = rng.randrange(0, len(text) - 1200); p = text[st:st + 1090]
        cs = [enc.get(c, "#") for c in p]
        cs = [rng.choice(signs) if rng.random() < 0.034 else c for c in cs]
        keep = 458 / sum(1 for c in cs if c in key)
        cs = [c if (c in key and rng.random() < keep) else "#" for c in cs]
        cl = [cs[i:i + 37] for i in range(0, len(cs), 37)]
        d = perm_test(cl, pairs, lp, nperm, 85); d["seed"] = seed
        d["coverage"] = f"{sum(1 for c in cs if c in key)}/{len(cs)}"; pm.append(d)
    res["posthoc_control_matched_coverage"] = pm
    res["posthoc_control_matched_coverage_pass"] = f"{sum(d['p'] < 0.05 for d in pm)}/5"
    out = json.dumps(res, indent=1, sort_keys=True) + "\n"; path = os.path.join(H, "results.json")
    if "--check" in sys.argv:
        ok = os.path.exists(path) and open(path).read() == out; print("OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(path, "w").write(out); print(out)
main()
