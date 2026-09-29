#!/usr/bin/env python3
"""H203 (runner 8 session_011Taenrv3JSdk7VjpiBjids, 29 Sept 2026), script-only, descriptive, for the verifier. Written before the run.
H190/H194/H199 found that the two 4-signs (bowl = c/p, r/3-tail = a/n; H193/H194/H201) are written under different reader codes in different reading
sessions (f.176r: both as 4TRI; f.176v: 4TRI / C43; f.61: 4TRI / C43; f.108v: 4STEM / C43). This tabulates, per 4-family code and per leaf, the
{c,p} and {a,n} counts in the period evidence on disk (key_period_v5.tsv rows other than CELL rows, and key_period_f176.tsv), and flags a (code, leaf)
as MIXED when both groups have >= 5 and the smaller is >= 0.25 of the two together: such support pools the two signs, so the code's cell on that
leaf cannot be read from the counts alone. Also lists the code the c/p majority sits under on each leaf.  -> h203_4fam_mix_result.txt [--check]"""
import csv, os, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); FAM = ("4TRI", "C43", "4STEM", "4PI")
def rows(f):
    for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t"):
        if r["class"] in FAM and not (r.get("bands") or "").startswith("CELL"): yield r
def main():
    T = defaultdict(lambda: [0, 0, 0]); seen = set()
    for f in ("key_period_v5.tsv", "key_period_f176.tsv"):
        for r in rows(f"{HERE}/{f}"):
            k = (r["class"], r["leaf"], r["letter"])
            if k in seen: continue      # v5 may already carry the f.176 rows
            seen.add(k); t = T[(r["class"], r["leaf"])]; n = int(r["n"])
            t[0 if r["letter"] in "cp" else 1 if r["letter"] in "an" else 2] += n
    out = ["code\tleaf\tc/p\ta/n\tother\tflag"]; cpcode = defaultdict(dict)
    for (c, leaf), (cp, an, ot) in sorted(T.items(), key=lambda x: (x[0][1], x[0][0])):
        mix = cp >= 5 and an >= 5 and min(cp, an) / (cp + an) >= 0.25
        out.append(f"{c}\t{leaf}\t{cp}\t{an}\t{ot}\t{'MIXED' if mix else ''}"); cpcode[leaf][c] = cp
    out.append("code holding most c/p per leaf: " + "; ".join(f"{leaf}: {max(d, key=d.get)} ({d[max(d, key=d.get)]})" for leaf, d in sorted(cpcode.items())))
    out.append(f"MIXED (code, leaf): {sum(1 for l in out[1:] if l.endswith('MIXED'))}")
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/h203_4fam_mix_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(rp) and open(rp).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
