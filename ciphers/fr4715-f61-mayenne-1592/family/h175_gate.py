#!/usr/bin/env python3
"""H175 (runner 6, 28 Sept 2026; pre-registered in passes/PROMPTS_f176_f175.md section H175 before the call): fol. 177r's blind read
against f.176r L01-L04's two passes, h170_gate.py's statistic and gate; wrong texts f.184r @0/@120 and fol. 175r.
  python3 h175_gate.py [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import h170_gate as g
P = f"{HERE}/passes"
def main():
    key = g.load_key(); out = []
    rows = g.rd(f"{P}/f177r_clearA_h175.tsv"); l1 = rows[0]["text"]
    l1 = l1.split("/", 1)[1] if "/" in l1 else (l1.lower().split("pere", 1)[1] if "pere" in l1.lower() else l1)   # salutation dropped (amendment)
    cand = g.fold(l1) + "".join(g.fold(r["text"]) for r in rows[1:])
    f175 = "".join(g.fold(r["text"]) for r in g.rd(f"{P}/f175r_clearA_h170.tsv"))
    w184 = [r["word"] for r in g.rd(f"{P}/f184r_clear_rec.tsv")]
    out.append(f"fol. 177r letters read {len(cand)}"); allp = True
    for tag in "AB":
        seq = g.signs(f"{P}/f176r_signs{tag}_h170.tsv"); N = min(len(cand), int(0.8 * len(seq)))
        t = cand[:N]; wrong = [g.fold(" ".join(w184))[:N], g.fold(" ".join(w184[120:]))[:N], f175[:N]]
        ft = g.frac(t, seq, key); fw = [g.frac(w, seq, key) for w in wrong]
        rng = random.Random(1); cls = list(key); sets = [key[c] for c in cls]; perm = []
        for _ in range(200):
            rng.shuffle(sets); perm.append(g.frac(t, seq, dict(zip(cls, sets))))
        pmax = max(perm); ok = ft > pmax and ft - max(fw) >= 0.10; allp &= ok
        out.append(f"pass {tag}: N {N}; fol.177r {ft:.3f}; wrong f184@0 {fw[0]:.3f} f184@120 {fw[1]:.3f} f175 {fw[2]:.3f}; "
                   f"permuted mean {sum(perm)/200:.3f} p95 {sorted(perm)[189]:.3f} max {pmax:.3f}; {'PASS' if ok else 'FAIL'}")
    out.append(f"GATE (both passes): {'PASS' if allp else 'FAIL'}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h175_gate_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
