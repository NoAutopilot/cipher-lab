"""GAPS39 scorer: per-class control (G1-G3 of gaps39/PREREG.md, 6+6) per pass and reconciled, band calls, and the
pooled GAPS33+GAPS39 view. Usage: python3 gaps39/score.py (writes gaps39/result.tsv)."""
import csv, os, re
from collections import defaultdict
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def load(d, name):
    out = {}
    for line in open(os.path.join(T, d, name)):
        f = re.split(r"\s+", line.strip())
        if len(f) >= 2 and f[0].isdigit(): out[f[0]] = f[1].upper() if f[1].upper() in ("NULL", "SPLIT") else f[1].lower()
    return out
names = {}
for r in csv.DictReader(open(os.path.join(T, "names.tsv")), delimiter="\t"):
    v = r["value"].split(" ")[0]
    for loc in re.findall(r"\d{4} (\S+:\d+)", r["where (first 8 agreeing)"]): names[(r["code"], loc)] = v
def run(d, pname):
    ans = {r["item"]: r for r in csv.DictReader(open(os.path.join(T, d, "answers.tsv")), delimiter="\t")}
    c = load(d, pname); k = {"cnull": [0, 0], "cletter": [0, 0]}; fn = 0; band = defaultdict(list)
    for it, a in ans.items():
        call = c.get(it, "SPLIT")
        if a["kind"] == "cnull": k["cnull"][1] += 1; k["cnull"][0] += call == "NULL"
        elif a["kind"] == "cletter":
            k["cletter"][1] += 1; k["cletter"][0] += call not in ("NULL", "SPLIT"); fn += call == "NULL"
        else: band[a["code"]].append((call, names.get((a["code"], f"{a['line']}:{a['pos']}"), "")))
    return k, fn, band
rows = []
for p in ("passA.tsv", "passB.tsv", "recon.tsv"):
    k, fn, band = run("gaps39", p)
    gate = k["cnull"][0] >= 5 and k["cletter"][0] >= 5 and fn <= 1
    print(f"{p}: G1 null {k['cnull'][0]}/6 | G2 letter {k['cletter'][0]}/6 | G3 false-NULL {fn}/6 | gate {'PASS' if gate else 'FAIL'}")
    for code in sorted(band):
        print(f"   band {code}: " + ", ".join(cl + (f"[names {nv}]" if nv else "") for cl, nv in band[code]))
        rows.append((p, code, len(band[code]), sum(cl == "NULL" for cl, _ in band[code]),
                     sum(cl not in ("NULL", "SPLIT") for cl, _ in band[code]), " ".join(cl for cl, _ in band[code]),
                     " ".join(nv or "-" for _, nv in band[code])))
    rows.append((p, "GATE", f"G1 {k['cnull'][0]}/6", f"G2 {k['cletter'][0]}/6", f"G3 {fn}/6", "", "PASS" if gate else "FAIL"))
k3, fn3, b3 = run("gaps33", "recon.tsv"); k9, fn9, b9 = run("gaps39", "recon.tsv")
print(f"pooled control (reported): null {k3['cnull'][0]+k9['cnull'][0]}/31, letter {k3['cletter'][0]+k9['cletter'][0]}/31, false-NULL {fn3+fn9}/31")
for code in sorted(set(b3) | set(b9)):
    obs = b3.get(code, []) + b9.get(code, [])
    print(f"   pooled {code}: NULL {sum(c == 'NULL' for c, _ in obs)}, letter {sum(c not in ('NULL','SPLIT') for c, _ in obs)}, SPLIT {sum(c == 'SPLIT' for c, _ in obs)} :: " + " ".join(c for c, _ in obs))
with open(os.path.join(H, "result.tsv"), "w") as w:
    w.write("pass\tcode\tn\tnull_calls\tletter_calls\tcalls\tnames_tsv_at_occ\n")
    for r in rows: w.write("\t".join(map(str, r)) + "\n")
