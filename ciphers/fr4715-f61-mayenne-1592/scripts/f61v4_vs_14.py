#!/usr/bin/env python3
"""F61-V4-VS-14 (campaign step H145, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only table. Per sign
class on f.61r: key v4's letter set as the v4 decode gives it (family/f61_decode_period_v4_frac0.1_sbs.tsv, frac 0.1), the
14-cell pair (scripts/f61joint_h51_map.tsv, f.61 + f.108r fit), the number of f.61 signs, and v4's pooled period counts for
the class (family/key_period_v4.tsv, summed over leaves, top six letters). Where v4's set is wider than the pair, the
extra letters are the ones the frac-0.1 rule let in from the period counts. For the verifier and the family worker.
  -> scripts/f61v4_vs_14.tsv [--check]"""
import csv, os, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); FAM = os.path.abspath(f"{HERE}/../family")
def rows(p): return list(csv.DictReader((l for l in open(p) if not l.startswith("#")), delimiter="\t"))
def main():
    dec = rows(f"{FAM}/f61_decode_period_v4_frac0.1_sbs.tsv"); sets = defaultdict(Counter); n = Counter()
    for r in dec: n[r["class"]] += 1; sets[r["class"]][r["period_letters"]] += 1
    pair = {r["class"]: r["cell"] for r in rows(f"{HERE}/f61joint_h51_map.tsv")}
    per = defaultdict(Counter)
    for r in rows(f"{FAM}/key_period_v4.tsv"): per[r["class"]][r["letter"]] += int(r["n"])
    out = ["class\tf61_signs\tv4_set_on_f61\tcell_14\tv4_wider\tv4_period_counts_top6"]
    for c in sorted(n, key=lambda c: -n[c]):
        vs = "; ".join(f"{k} x{v}" for k, v in sets[c].most_common()); p14 = pair.get(c, "")
        wide = any(len(k.split("/")) > 2 for k in sets[c] if k not in ("-", ""))
        top = ", ".join(f"{l} {m}" for l, m in per[c].most_common(6))
        out.append(f"{c}\t{n[c]}\t{vs}\t{p14}\t{'yes' if wide else ''}\t{top}")
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61v4_vs_14.tsv"
    if "--check" in sys.argv:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
