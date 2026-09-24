import sys, json
sys.path.insert(0, "../../../tools")
import homophonic_anneal as ha

rows = [l.rstrip("\n").split("\t") for l in open("ciphertext.tsv") if l.strip()]
h = rows[0]
si = h.index("sign")
seq = [r[si] for r in rows[1:] if r[si] != "DOT"]

corpora = ["../../../tools/data/de16/composed_enhg.txt", "goethe_faust_2229.txt"]
model = ha.Model([open(f, encoding="utf-8").read() for f in corpora], 3)

def run(fixed, label, seeds=(1, 2, 3)):
    best_overall = None
    for seed in seeds:
        res = ha.solve(seq, model, restarts=8, iters=40000, seed=seed, uni_w=1.0, fixed=fixed)
        sc, key = res[0]
        dec = "".join(key[x] for x in seq)
        print(f"{label} seed={seed} N={len(seq)} K={len(set(seq))} score={sc:.1f} decode={dec}")
        if best_overall is None or sc > best_overall[0]:
            best_overall = (sc, dec, key, seed)
    return best_overall

print("=== baseline, no fix ===")
best_base = run({}, "baseline")

print()
print("=== fixed: segment 'glueck' hypothesis (4=g,n=l,==u,s=e,3=c,|=k) ===")
fixed = {"4": "g", "n": "l", "=": "u", "s": "e", "3": "c", "|": "k"}
best_fix = run(fixed, "glueck-fix")

json.dump({
    "baseline_best": {"score": best_base[0], "decode": best_base[1], "seed": best_base[3]},
    "glueckfix_best": {"score": best_fix[0], "decode": best_fix[1], "seed": best_fix[3]},
}, open("target_results.json", "w"), indent=1)
