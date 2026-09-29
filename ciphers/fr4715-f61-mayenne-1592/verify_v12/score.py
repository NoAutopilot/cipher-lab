#!/usr/bin/env python3
"""VERIFY-F61-V12: score C1/C2 replies against v12_key.tsv under PREREG.md's gates and rules; C3 from c3_reply.txt; C4 if present.
python3 score.py [--check]"""
import csv, os, re, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
def rd(p): return dict(l.rstrip("\n").split("\t")[:2] for l in open(p) if l.strip())
def main():
    key = list(csv.DictReader(open(f"{HERE}/v12_key.tsv"), delimiter="\t")); c1 = rd(f"{HERE}/c1_reply.tsv"); c2 = rd(f"{HERE}/c2_reply.tsv")
    ans = {**c1, **c2}; out = []; reads = defaultdict(list)
    assert all(k["id"] in ans for k in key), "missing ids"
    for call in ("C1", "C2"):
        ks = [k for k in key if k["call"].startswith(call)]
        anc = [k for k in ks if k["role"] == "anchor"]; ok = sum(ans[k["id"]] == k["expected"] for k in anc)
        out.append(f"{call} anchors {ok}/{len(anc)}" + "".join(f"; miss {k['line']}/{k['pos']} {k['window']} exp {k['expected']} got {ans[k['id']]}" for k in anc if ans[k["id"]] != k["expected"]))
        rep = [k for k in ks if k["role"] == "repeat"]; own = {(k["line"], k["pos"]): ans[k["id"]] for k in ks if k["role"] in ("anchor", "oos")}
        rc = sum(ans[k["id"]] == own.get((k["line"], k["pos"]), k["expected"]) for k in rep); out.append(f"{call} repeats consistent {rc}/{len(rep)}")
    bc = [k for k in key if k["role"] == "betactl"]; out.append("C1 BETA control L11/1 (Part A): " + " ".join(f"{k['window']}={ans[k['id']]}" for k in bc))
    for k in key:
        if k["role"] in ("T1", "T2", "T3", "T4", "partB", "t3"): reads[(k["line"], k["pos"])].append(f"{k['call']}:{k['window']}={ans[k['id']]}")
    for (l, p), v in sorted(reads.items()): out.append(f"target {l}/{p}: " + " ".join(v))
    oos = [k for k in key if k["role"] == "oos"]; conf = [k for k in oos if ans[k["id"]] == k["expected"]]
    out.append(f"C2 out-of-span confirmed {len(conf)}/{len(oos)}; disagree: " + "; ".join(f"{k['line']}/{k['pos']} exp {k['expected']} got {ans[k['id']]}" for k in oos if ans[k["id"]] != k["expected"]))
    c3 = open(f"{HERE}/c3_reply.txt").read(); out.append("C3 cipher counts: " + " ".join(f"{m.group(1)}={m.group(2)}" for m in re.finditer(r"^(X\d):.*cipher_count=(\d+)", c3, re.M)))
    if os.path.exists(f"{HERE}/c4_reply.tsv"):
        k4 = list(csv.DictReader(open(f"{HERE}/v12_key_c4.tsv"), delimiter="\t")); a4 = rd(f"{HERE}/c4_reply.tsv")
        an = [k for k in k4 if k["expected"] != "?"]; out.append(f"C4 anchors {sum(a4[k['id']] == k['expected'] for k in an)}/{len(an)}; L02 opening mark: " + " ".join(f"{k['window']}={a4[k['id']]}" for k in k4 if k["expected"] == "?"))
    txt = "\n".join(out) + "\n"; p = f"{HERE}/score_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
