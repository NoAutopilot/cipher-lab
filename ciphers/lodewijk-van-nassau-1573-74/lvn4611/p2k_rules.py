"""LVN-P2K (15 Oct 2026): the pre-registered disk rules R1/R2/P of PREREG-LVN-4611.md addendum LVN-P2K, run mechanically on the
pre-P2K ciphertext (git show <pre-P2K commit>:.../ciphertext_4611.tsv, passed as FILE), to (a) classify the unplaced p2_K rows and (b) run
the positive control: the 7 LVN-P2B block duplicates (retired_p2.tsv) and the 2 VER-LVN2 eye-retired duplicates restored as unplaced.
The rulings applied are lvn4611/corrections_p2k.tsv (every R1/R2 row was also looked at by eye; the eye decides). Prints a TSV.
usage: python3 lvn4611/p2k_rules.py FILE [--control]"""
import csv, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
WAS = re.compile(r"LVN-P2B order: was (p2_[LR]\d\d\w?)/(\d+)")
INS = re.compile(r"\b(K\d\d)/(\d+);")


def load(fn):
    return list(csv.DictReader(open(fn, newline="", encoding="utf-8"), delimiter="\t"))


def classify(rows, targets):
    """rows: p2_K rows in file order (dicts); targets: set of id() of rows treated as unplaced."""
    mp = {(r["line"], r["position"]): r for r in load(HERE / "retx_p2_map.tsv")}
    ink = {}
    for t in load(HERE / "retx_p2_lines.tsv"):
        ink.setdefault(t["K"], {})[int(t["pos"])] = t["token"]
    lines = {}
    for r in rows:
        lines.setdefault(r["line"][3:], []).append(r)
    info = {}
    for K, L in lines.items():
        for r in L:
            if id(r) in targets: info[id(r)] = ("U", None); continue
            m = WAS.search(r["why"] or "")
            if m and m.group(1).startswith("p2_R") or (not m and INS.search(r["why"] or "")):
                mi = INS.search(r["why"]); info[id(r)] = ("I", int(mi.group(2))); continue
            s = mp.get((m.group(1), m.group(2))) if m else None
            if s and s["K"] == K: info[id(r)] = ("A", int(s["kpos"]))
            elif "VER-LVN2 eye" in (r["why"] or ""): info[id(r)] = ("V", None)
            else: info[id(r)] = ("X", None)
    out = {}
    for K, L in lines.items():
        carried = {info[id(r)][1] for r in L if info[id(r)][0] in "AI"}
        if K == "K18": carried |= {11, 12, 13}          # VER-LVN2 moved =Que 94 carry the RETX =gur 9 4 span
        # R1: unplaced rows of one old line vs the carriers of K-1 / K+1
        for nb in (int(K[1:]) - 1, int(K[1:]) + 1):
            NB = lines.get(f"K{nb}", [])
            V = [r["sign"] for r in NB if info[id(r)][0] in "AI"]
            byold = {}
            for r in L:
                if id(r) in targets:
                    byold.setdefault(WAS.search(r["why"]).group(1) if WAS.search(r["why"] or "") else "?", []).append(r)
            for U in byold.values():
                u = [r["sign"] for r in U]
                for i in range(len(u) - 1):
                    for j in range(len(u), i + 1, -1):
                        seg = u[i:j]
                        if any(V[k:k + len(seg)] == seg for k in range(len(V))):
                            for r in U[i:j]: out.setdefault(id(r), ("R1", f"K{nb}"))
                            break
                if len(u) >= 3:
                    for k in range(len(V)):
                        w, q = V[k:k + 2 * len(u)], 0
                        for x in w:
                            if q < len(u) and x == u[q]: q += 1
                        if q == len(u):
                            for r in U: out.setdefault(id(r), ("R1", f"K{nb}"))
                            break
        for i, r in enumerate(L):
            if id(r) not in targets or id(r) in out: continue
            if r["confidence"] == "M":
                a = next((info[id(x)][1] for x in reversed(L[:i]) if info[id(x)][0] == "A"), None)
                bi = next((j for j in range(i + 1, len(L)) if info[id(L[j])][0] == "A"), None)
                if a is not None and bi is not None:
                    b = info[id(L[bi])][1]
                    span = list(range(a + 1, b))
                    ai = max(j for j in range(i) if info[id(L[j])][0] == "A")
                    nun = sum(1 for x in L[ai + 1:bi] if id(x) in targets)
                    if span and all(k in carried for k in span) and nun <= len(span):
                        out[id(r)] = ("R2", f"{a}-{b}"); continue
            if r["sign"].startswith("="):
                for x in (L[i - 1] if i else None, L[i + 1] if i + 1 < len(L) else None):
                    if x is None or info[id(x)][0] != "A": continue
                    w = ink[K].get(info[id(x)][1], "")
                    p = [x, r] if x is L[i - 1] else [r, x]
                    if w.startswith("=") and re.sub("[^a-z]", "", "".join(y["sign"] for y in p).lower()) == re.sub("[^a-z]", "", w.lower()):
                        out[id(r)] = ("P", w); break
                if id(r) in out: continue
            out[id(r)] = ("E", "")
    return out


def main():
    fn = sys.argv[1]; control = "--control" in sys.argv
    rows = [r for r in load(fn) if r["line"].startswith("p2_K")]
    if not control:
        mp = {(r["line"], r["position"]): r for r in load(HERE / "retx_p2_map.tsv")}
        targets = set()
        for r in rows:
            m = WAS.search(r["why"] or "")
            if m and m.group(1).startswith("p2_L") and not mp[(m.group(1), m.group(2))]["K"] and "VER-LVN2 eye" not in r["why"]:
                targets.add(id(r))
    else:
        # restore the 9 known duplicates after the nearest preceding present row of their own old line (p2_order rule (2))
        rest = [dict(r) for r in load(HERE / "retired_p2.tsv")]
        for r in rest:
            r["why"] = (r["why"] + "; " if r["why"] else "") + f"LVN-P2B order: was {r['line']}/{r['position']}"
        restore = []
        for r in rest:
            L, P = r["line"], int(r["position"])
            prev = None
            for x in rows:
                m = WAS.search(x["why"] or "")
                if m and m.group(1) == L and int(m.group(2)) < P and (prev is None or int(m.group(2)) > prev[1]):
                    prev = (x, int(m.group(2)))
            restore.append((r, prev[0]))
        ver = {("p2_K15", "18"): ("p2_K15", "17"), ("p2_K30", "4"): ("p2_K30", "3")}
        for v in load(HERE / "retired_verlvn2.tsv"):
            if (v["line"], v["position"]) in ver:
                a = ver[(v["line"], v["position"])]
                restore.append((dict(v), next(x for x in rows if (x["line"], x["position"]) == a)))
        for r, anchor in restore:
            r["line"] = anchor["line"]; rows.insert(rows.index(anchor) + 1, r)
        targets = {id(r) for r, _ in restore}
    res = classify(rows, targets)
    print("line\tsign\tconf\twas\tclass\tdetail")
    for r in rows:
        if id(r) in targets:
            m = WAS.search(r["why"] or ""); c = res[id(r)]
            print(f"{r['line']}\t{r['sign']}\t{r['confidence']}\t{m.group(1) + '/' + m.group(2) if m else ''}\t{c[0]}\t{c[1]}")


if __name__ == "__main__":
    main()
