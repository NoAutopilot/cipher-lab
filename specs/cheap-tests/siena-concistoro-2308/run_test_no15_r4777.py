"""R10-SIENA4777 (6 Oct 2026): no. 15 (R4803) against key R4777 through the shape concordance
ciphers/siena-concistoro-2308/concordance_R4777_no15.tsv. Pre-registered in PREREG-R10-SIENA4777.md (pushed in f2a3c5e6c first;
concordance pushed before scoring). Same statistic S2, controls, gate and positive control as run_test_no15.py (R9-SIENA15),
whose functions are reused; only the concordance and the null rate r (per variant, from the target's own null count) differ.
Run: python3 specs/cheap-tests/siena-concistoro-2308/run_test_no15_r4777.py [--check]  (deterministic; --check exits 1 if
results_no15_r4777.json is stale)
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import run_test_no15 as base

def load_conc():
    P, V = {}, {}
    for l in open(os.path.join(base.FOLD, "concordance_R4777_no15.tsv")):
        if l.startswith("# ") or l.startswith("no15_sign"): continue
        f = l.rstrip("\n").split("\t")
        (P if f[1] == "P" else V)[f[0]] = f[2]
    Vf = dict(P); Vf.update(V)
    return {"P": P, "V": Vf}

def run():
    T = base.load_tokens(); conc = load_conc(); n = sum(1 for t in T if t != "|")
    res = {"N": n, "variants": {}}
    for vn, key in conc.items():
        nulls = sum(1 for t in T if key.get(t) == "NULL")
        base.R_NULL = nulls / (n - nulls)
        base.load_conc = lambda vn=vn, key=key: {vn: key}
        r = base.run()["variants"][vn]; r["r_null"] = round(base.R_NULL, 4)
        res["variants"][vn] = r
    return res

if __name__ == "__main__":
    out = os.path.join(HERE, "results_no15_r4777.json")
    r = run(); js = json.dumps(r, indent=1, sort_keys=True)
    if "--check" in sys.argv:
        ok = os.path.exists(out) and open(out).read() == js + "\n"
        print("results_no15_r4777.json", "current" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(out, "w").write(js + "\n"); print(js)
