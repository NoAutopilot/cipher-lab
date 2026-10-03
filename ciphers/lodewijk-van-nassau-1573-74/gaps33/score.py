"""GAPS33 scorer: per-class control accuracy (gate G1-G3 of PREREG.md) and band observations, per pass and reconciled.
Usage: python3 gaps33/score.py   (reads gaps33/{answers,passA,passB,recon}.tsv; writes gaps33/result.tsv)"""
import csv, os, re
from collections import defaultdict
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
ans = {r["item"]: r for r in csv.DictReader(open(os.path.join(H, "answers.tsv")), delimiter="\t")}
def calls(name):
    p = os.path.join(H, name)
    if not os.path.exists(p): return None
    out = {}
    for line in open(p):
        f = re.split(r"\t|\s+", line.strip())
        if len(f) >= 2 and f[0].isdigit(): out[f[0]] = f[1].upper() if f[1].upper() in ("NULL", "SPLIT") else f[1].lower()
    return out
# names.tsv agreeing observations per (line:pos) -> value
names = {}
for r in csv.DictReader(open(os.path.join(T, "names.tsv")), delimiter="\t"):
    v = r["value"].split(" ")[0]
    for loc in re.findall(r"\d{4} (\S+:\d+)", r["where (first 8 agreeing)"]): names[(r["code"], loc)] = v
rows = []
for pname in ("passA.tsv", "passB.tsv", "recon.tsv"):
    c = calls(pname)
    if c is None: continue
    k = {"cnull": [0, 0], "cletter": [0, 0]}; falsenull = 0; valright = 0
    band = defaultdict(list)
    for it, a in ans.items():
        call = c.get(it, "SPLIT")
        if a["kind"] == "cnull":
            k["cnull"][1] += 1; k["cnull"][0] += call == "NULL"
        elif a["kind"] == "cletter":
            k["cletter"][1] += 1; isl = call not in ("NULL", "SPLIT")
            k["cletter"][0] += isl; falsenull += call == "NULL"
            valright += call == a["true"].lower().replace("j", "i").replace("v", "u")
        else:
            loc = f"{a['line']}:{a['pos']}"; nv = names.get((a["code"], loc), "")
            band[a["code"]].append((call, nv))
    g1 = k["cnull"][0] / k["cnull"][1]; g2 = k["cletter"][0] / k["cletter"][1]; q = falsenull / k["cletter"][1]
    gate = g1 >= 0.80 and g2 >= 0.80 and q <= 0.316
    print(f"{pname}: G1 null {k['cnull'][0]}/{k['cnull'][1]} {g1:.3f} | G2 letter {k['cletter'][0]}/{k['cletter'][1]} {g2:.3f} | "
          f"G3 q {falsenull}/{k['cletter'][1]} {q:.3f} | letter value right {valright}/{k['cletter'][1]} | gate {'PASS' if gate else 'FAIL'}")
    for code in sorted(band):
        obs = band[code]
        print(f"   band {code}: " + ", ".join(f"{cl}" + (f"[names {nv}]" if nv else "") for cl, nv in obs))
        rows.append((pname, code, len(obs), sum(cl == "NULL" for cl, _ in obs), sum(cl not in ("NULL", "SPLIT") for cl, _ in obs),
                     " ".join(cl for cl, _ in obs), " ".join(nv or "-" for _, nv in obs)))
    rows.append((pname, "GATE", f"G1 {g1:.3f}", f"G2 {g2:.3f}", f"q {q:.3f}", f"value {valright}/25", "PASS" if gate else "FAIL"))
with open(os.path.join(H, "result.tsv"), "w") as w:
    w.write("pass\tcode\tn\tnull_calls\tletter_calls\tcalls\tnames_tsv_at_occ\n")
    for r in rows: w.write("\t".join(map(str, r)) + "\n")
