#!/usr/bin/env python3
"""VERIFY-F61-V6 task 1 scorer for the three blind calls (passes/call{1,2,3}_reply.tsv, items_v6.tsv). Gate per call: runner's H193 anchor
strips K >= 17/20 AND the verifier-framed anchors FA >= 17/20 (CP yes, AN no). Then, per leaf:
 f.176r  RT (H193's 40 targets re-cut): agreement with the runner's H193 answers; bowl vs the runner-alignment letter (c/p vs a/n), Fisher.
         RN (40 fresh 4-family columns, any code, 20 c/p + 20 a/n): bowl vs letter, Fisher; the same split by reader code.
 f.108v  V8 (H199's 74 columns): agreement with the runner's H199 answers; bowl by reconciled code.
 f.108r  R8 (H202's 20 gloss positions): bowl vs gloss letter, Fisher; the registered H202 read-out (every c/p yes, <=1 a/n yes, p<0.05).
 f.61    list method: per line, listed count vs the line's 4-family code count; matched positions beside Tomokiyo's letter (h194's table).
  python3 score_v6.py [--check]"""
import csv, os, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); F = os.path.abspath(f"{HERE}/../family"); sys.path.insert(0, F)
from h190_4fam import fisher
def rd(f): return list(csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t"))
def main():
    items = rd(f"{HERE}/items_v6.tsv"); out = []
    K = [r for r in items if r["set"] == "K"]; gates = {}
    for call in ("1", "2", "3"):
        ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{HERE}/passes/call{call}_reply.tsv")}
        k = sum((ans.get(r["item"]) == "yes") == r["source"].startswith("CP") and ans.get(r["item"]) in ("yes", "no") for r in K)
        fa = [r for r in items if r["call"] == call and r["set"] == "FA"]
        f = sum((ans.get(r["item"]) == "yes") == (r["source"] == "CP") and ans.get(r["item"]) in ("yes", "no") for r in fa)
        gates[call] = (k >= 17 and f >= 17, ans)
        out.append(f"call {call}: control K (runner's H193 strips) {k}/20, FA (verifier framing) {f}/20 -> {'PASS' if gates[call][0] else 'CONTROL FAIL'}")
    def tab(rows, ans, lab):
        t = {"yes": [0, 0], "no": [0, 0]}; nn = 0
        for r in rows:
            a = ans.get(r["item"]); L = r["letter"]
            if a in t and L in list("cpan"): t[a][0 if L in "cp" else 1] += 1
            elif a not in t: nn += 1
        y, n = t["yes"], t["no"]
        out.append(f"  {lab}: bowl yes c/p {y[0]} a/n {y[1]}; bowl no c/p {n[0]} a/n {n[1]}; n/other {nn}; Fisher p {fisher(y[0], y[1], n[0], n[1]):.2g}")
        return t
    ok, ans = gates["1"]
    if ok:
        out.append("f.176r (call 1)")
        h193 = {r["item"]: r["answer"].strip().lower() for r in rd(f"{F}/passes/h193_attribute.tsv")}
        RT = [r for r in items if r["set"] == "RT"]
        ag = sum(ans.get(r["item"]) == h193.get(r["source"]) for r in RT)
        out.append(f"  RT: same answer as the runner's H193 reader on {ag}/40 (verifier yes {sum(ans.get(r['item']) == 'yes' for r in RT)}, runner yes {sum(h193.get(r['source']) == 'yes' for r in RT)})")
        for r in RT:
            if ans.get(r["item"]) != h193.get(r["source"]): out.append(f"    differs: {r['source']} {r['line']} {r['segment']} x{r['x_px']} letter {r['letter']}: runner {h193.get(r['source'])}, verifier {ans.get(r['item'])}")
        tab(RT, ans, "RT (H193's targets, verifier's answers)")
        RN = [r for r in items if r["set"] == "RN"]; tab(RN, ans, "RN (fresh, any code)")
        bc = defaultdict(Counter)
        for r in RN: bc[r["code"]][(ans.get(r["item"]), "cp" if r["letter"] in "cp" else "an")] += 1
        for c in sorted(bc): out.append(f"    RN code {c}: " + ", ".join(f"{a}/{l} {v}" for (a, l), v in sorted(bc[c].items(), key=str)))
        tab(RT + RN, ans, "f.176r pooled RT+RN")
    ok, ans = gates["2"]
    if ok:
        out.append("f.108v and f.108r (call 2)")
        h199 = {(r["line"], r["column"]): r["bowl"] for r in rd(f"{F}/h199_bowl_positions.tsv")}
        V8 = [r for r in items if r["set"] == "V8"]; ag = sum(ans.get(r["item"]) == h199.get((r["line"], r["segment"])) for r in V8)
        out.append(f"  V8: same answer as the runner's H199 reader on {ag}/74 (verifier yes {sum(ans.get(r['item']) == 'yes' for r in V8)}, runner yes {sum(v == 'yes' for v in h199.values())})")
        byc = defaultdict(Counter)
        for r in V8: byc[r["code"].split("|")[0]][ans.get(r["item"])] += 1
        out.append("  V8 bowl by reconciled code: " + "; ".join(f"{c} " + ", ".join(f"{a} {v}" for a, v in sorted(byc[c].items(), key=str)) for c in sorted(byc)))
        with open(f"{HERE}/v8_bowl_positions.tsv", "w") as fh:
            fh.write("line\tcolumn\tbowl_verifier\tbowl_runner\n" + "".join(f"{r['line']}\t{r['segment']}\t{ans.get(r['item'])}\t{h199.get((r['line'], r['segment']))}\n" for r in V8))
        R8 = [r for r in items if r["set"] == "R8"]; t = tab(R8, ans, "R8 f.108r gloss letters")
        cpn = [r for r in R8 if r["letter"] in "cp" and ans.get(r["item"]) in ("yes", "no")]
        reg = all(ans.get(r["item"]) == "yes" for r in cpn) and t["yes"][1] <= 1 and fisher(*t["yes"], *t["no"]) < 0.05
        out.append(f"  H202 registered read-out on the verifier's answers: {'MET' if reg else 'NOT met'}")
        for r in sorted(R8, key=lambda r: (r["line"], int(r["segment"]))): out.append(f"    {r['line']} pos {r['segment']} {r['code']} {r['letter']}: {ans.get(r['item'])}")
    ok, ans = gates["3"]
    if ok:
        out.append("f.61 (call 3, list method)")
        sys.path.insert(0, os.path.abspath(f"{HERE}/../scripts"))
        from f61crib import load_read
        from f61crib4 import split_lines
        from sbs_relabel import relabel
        L = split_lines(load_read()); relabel(L); FAM = ("4TRI", "C43", "4STEM", "4PI")
        tom = {}
        for l in open(f"{F}/h194_bowl_f61_result.txt"):
            p = l.rstrip("\n").split("\t")
            if len(p) == 5 and p[1].isdigit(): tom[(p[0], int(p[1]))] = p[4]
        t = {"yes": [0, 0], "no": [0, 0]}
        for ln in ("L01", "L03", "L05", "L07", "L08", "L11"):
            codes = [c for c in L.get(ln, []) if c in FAM]; lst = [(k, v) for k, v in ans.items() if k.startswith(ln + ":") and v != "none"]
            if len(lst) != len(codes): out.append(f"  {ln}: listed {len(lst)}, codes {len(codes)} -- left out"); continue
            for i, (c, (k, v)) in enumerate(zip(codes, lst), 1):
                tl = tom.get((ln, i), "?"); out.append(f"  {ln} {i} {c} bowl {v} Tomokiyo {tl}")
                if v in t and tl in list("cpan"): t[v][0 if tl in "cp" else 1] += 1
        y, n = t["yes"], t["no"]; out.append(f"  f.61: bowl yes c/p {y[0]} a/n {y[1]}; bowl no c/p {n[0]} a/n {n[1]}; Fisher p {fisher(y[0], y[1], n[0], n[1]):.2g}")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/score_v6_result.txt"
    if "--check" in sys.argv:
        good = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if good else "STALE"); sys.exit(0 if good else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
