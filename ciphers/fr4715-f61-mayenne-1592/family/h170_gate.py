#!/usr/bin/env python3
"""H170 gate (runner 6, 28 Sept 2026; pre-registered in passes/PROMPTS_f176_f175.md, pushed before any call): does fr.3984
fol. 175r render the cipher of fr.3984 f.176r? For each blind sign pass of f.176r L01-L04 separately: F61-CAL DP fraction of
the first N folded letters of fol. 175r (blind read) under key v4, against 200 permuted keys (seed 1) and against two wrong
texts of the same writer and day (fr.3984 f.184r from word 0 and from word 120). Gate per pass: f175 > permuted max AND
f175 - max(wrong) >= 0.10. Writes h170_gate_result.txt; --check fails if the committed result is stale.
  python3 h170_gate.py [--check]   (from the family folder)"""
import csv, os, random, re, sys, unicodedata
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.abspath(f"{HERE}/../scripts"))
from f61crib import align
P = f"{HERE}/passes"
def rd(p): return [r for r in csv.DictReader((l for l in open(p) if not l.startswith("#")), delimiter="\t")]
def fold(t):
    t = unicodedata.normalize("NFKD", t.lower()); t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"\^\S*", "", t)                       # superscripts (abbreviation marks) dropped
    t = t.replace("v", "u").replace("j", "i").replace("y", "i")
    return re.sub(r"[^a-z]", "", t)
def load_key(MIN=2, FRAC=0.1):
    rows = rd(f"{HERE}/key_period_v4.tsv"); tot = Counter(); key = {}
    for r in rows:
        if r["letter"] not in ("-", ""): tot[(r["class"], r["leaf"])] += int(r["n"])
    for r in rows:
        if r["letter"] in ("-", "") or r["class"] in ("PLAIN", "OTHER", "DASH") or int(r["n"]) < MIN: continue
        if int(r["n"]) < FRAC * tot[(r["class"], r["leaf"])]: continue
        c = {"EBR_A": "EBR", "EBR_B": "EBR"}.get(r["class"], r["class"])
        key.setdefault(c, set()).add(r["letter"])
    key["4TRI"] = key.get("4TRI", set()) | key.get("4HOOK", set())
    return {c: tuple(sorted(v)) for c, v in key.items()}
def signs(p):
    seq = []
    for r in rd(p):
        s = {"EBR_A": "EBR", "EBR_B": "EBR"}.get(r["sign"].strip(), r["sign"].strip())
        if s != "PLAIN": seq.append(s)
    return seq
def frac(markup, seq, key): return align(markup, seq, key)[0] / len(markup)
def main():
    key = load_key(); out = []
    clear = "".join(fold(r["text"]) for r in rd(f"{P}/f175r_clearA_h170.tsv"))
    w184 = [r["word"] for r in rd(f"{P}/f184r_clear_rec.tsv")]
    out.append(f"key v4 classes {len(key)}; f175 letters read {len(clear)}")
    allpass = True
    for tag in ("A", "B"):
        seq = signs(f"{P}/f176r_signs{tag}_h170.tsv"); N = min(len(clear), int(0.8 * len(seq)))
        t = clear[:N]; wrong = [fold(" ".join(w184))[:N], fold(" ".join(w184[120:]))[:N]]
        ft = frac(t, seq, key); fw = [frac(w, seq, key) for w in wrong]
        rng = random.Random(1); cls = list(key); sets = [key[c] for c in cls]; perm = []
        for _ in range(200):
            rng.shuffle(sets); perm.append(frac(t, seq, dict(zip(cls, sets))))
        pmax = max(perm); pmean = sum(perm) / len(perm); p95 = sorted(perm)[189]
        cov = sum(1 for s in seq if s in key) / len(seq)
        ok = ft > pmax and ft - max(fw) >= 0.10; allpass &= ok
        out.append(f"pass {tag}: signs {len(seq)} (key coverage {cov:.2f}), N {N}; f175 {ft:.3f}; wrong f184@0 {fw[0]:.3f}, "
                   f"f184@120 {fw[1]:.3f}; permuted mean {pmean:.3f} p95 {p95:.3f} max {pmax:.3f}; gate {'PASS' if ok else 'FAIL'}")
    out.append(f"GATE (both passes): {'PASS' if allpass else 'FAIL'}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h170_gate_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
