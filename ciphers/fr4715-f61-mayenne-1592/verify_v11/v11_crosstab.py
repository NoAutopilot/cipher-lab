#!/usr/bin/env python3
"""VERIFY-F61-V11 part A (29 Sept 2026, own code, PREREG.md A): period letter (passes/f101r_align.tsv, grade C) by the runner's bowl answer
(H362 + H365 gate-passing chunks) for f.101r 4TRI, joined per line by difflib on the alignment's code sequence vs the reconciled draft (h364's method,
re-implemented). Sets: all; literal non-conflict (degenerate: the alignment's own key has 4TRI = n); neighbour-anchored (nearest non-4TRI/C43 code row
on each side in the line has status 'agrees'). Within-leaf permutation null of the bowl labels, 10,000 perms, seed 1101.
Also exports letter_map(leaf) for part B.   python3 v11_crosstab.py [--check]"""
import csv, difflib, os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); FAM = f"{HERE}/../family"; P = f"{FAM}/passes"
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def letter_map(leaf):
    al = defaultdict(list)
    for r in rd(f"{P}/{leaf}_align.tsv"):
        if r["kind"] == "code": al[r["cipher_line"]].append(r)
    dr = defaultdict(list)
    for r in rd(f"{P}/rec{leaf}/ciphertext_draft.tsv"): dr[r["line"]].append(r)
    out = {}
    for line, rows in dr.items():
        a = al.get(line, []); sa = [x["value"] for x in a]; sd = [x["sign"] for x in rows]
        for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, sd, sa, autojunk=False).get_opcodes():
            if tag != "equal": continue
            for k in range(i2 - i1):
                j = j1 + k; ar = a[j]; L = ar["plain_chunk"].strip()
                if not L or ar["status"].startswith("null"): continue
                def nb(step):
                    m = j + step
                    while 0 <= m < len(a):
                        if a[m]["value"] not in ("4TRI", "C43"): return a[m]["status"]
                        m += step
                    return None
                anch = nb(-1) == "agrees" and nb(1) == "agrees"
                out[(line, rows[i1 + k]["position"])] = (L, ar["status"].startswith("agrees"), anch)
    return out
cls = lambda L: "c/p/t" if L in ("c", "p", "t") else "a/n" if L in ("a", "n") else "other"
def test(pairs, seed=1101, perms=10000):
    """pairs: list of (bowl yes/no, letter class). returns counts, share, p, P(a/n|no), P(a/n|yes)"""
    pr = [(b, c) for b, c in pairs if b in ("yes", "no") and c in ("c/p/t", "a/n")]
    if not pr: return None
    agree = lambda xs: sum((b == "yes") == (c == "c/p/t") for b, c in xs)
    real = agree(pr); bs = [b for b, _ in pr]; cs = [c for _, c in pr]; rng = random.Random(seed); ge = 0
    for _ in range(perms):
        rng.shuffle(bs); ge += agree(list(zip(bs, cs))) >= real
    t = Counter(pr); n = len(pr)
    pn = t[("no", "a/n")] / max(1, t[("no", "a/n")] + t[("no", "c/p/t")]); py = t[("yes", "a/n")] / max(1, t[("yes", "a/n")] + t[("yes", "c/p/t")])
    return dict(n=n, share=real / n, p=(ge + 1) / (perms + 1), tab=t, pan_no=pn, pan_yes=py)
def readout(r):
    if r is None or r["n"] < 30: return "n < 30"
    if r["share"] >= 0.75 and r["p"] < 0.01: return "tracks"
    if r["share"] < 0.6 or r["p"] > 0.05: return "does not track"
    return "unclear"
def fmt(name, r):
    if r is None: return f"{name}: no tokens"
    t = r["tab"]
    return (f"{name}: n {r['n']}; no&a/n {t[('no','a/n')]} no&c/p/t {t[('no','c/p/t')]} yes&c/p/t {t[('yes','c/p/t')]} yes&a/n {t[('yes','a/n')]}; "
            f"share {r['share']:.3f}, perm p {r['p']:.4f}; P(a/n|no) {r['pan_no']:.2f}, P(a/n|yes) {r['pan_yes']:.2f} -> {readout(r)}")
def runner_labels():
    lab = {}; a = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h362_reply.tsv")}
    for r in rd(f"{FAM}/h362_items.tsv"):
        if r["code"] == "4TRI": lab[(r["line"], r["pos"])] = a.get(r["item"], "missing")
    ctl = {r["item"]: r for r in rd(f"{FAM}/h193_items.tsv")}; items = rd(f"{FAM}/h365_items.tsv")
    for c in sorted({r["chunk"] for r in items}):
        ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h365_reply_{c}.tsv")}
        g = sum((ans.get(m) == "yes") == (r["group"] == "CP") and ans.get(m) in ("yes", "no") for m, r in ctl.items() if r["group"] in ("CP", "AN"))
        if g >= 17:
            for r in items:
                if r["chunk"] == c: lab[(r["line"], r["pos"])] = ans.get(r["item"], "missing")
    return lab
def main():
    lab = runner_labels(); lm = letter_map("f101r"); out = [f"runner bowl labels f.101r: {len(lab)} ({dict(Counter(lab.values()))}); tokens with a period letter: {sum(k in lm for k in lab)}"]
    sets = {"all": lambda v: True, "literal non-conflict": lambda v: v[1], "neighbour-anchored": lambda v: v[2]}
    for nm, f in sets.items():
        pairs = [(b, cls(lm[k][0])) for k, b in lab.items() if k in lm and f(lm[k])]
        lets = Counter(lm[k][0] for k in lab if k in lm and f(lm[k]))
        out.append(fmt(f"A {nm}", test(pairs)) + f"  [letters: {' '.join(f'{x} {y}' for x, y in lets.most_common(6))}]")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/v11_crosstab_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
