"""MANT-0136 gate (b) (PREREG-MANT-0136.md): unglossed tokens of 694/09 0136, real key vs 1000 letter-value-permuted keys on the fr18
4-gram score (design of f0015_09/shuffle_gate_0015.py); power control = 0085 runs 9+10. Gate: real > p95 of the permuted scores.
Run from the repository root: python3 ciphers/sachsstaatsarchiv-manteuffel-1712/f0136_09/judge_gate.py [--check]"""
import csv, random, re, sys
from pathlib import Path
sys.path.insert(0, "tools")
import judge_plaintext as J
D = Path("ciphers/sachsstaatsarchiv-manteuffel-1712"); F = D / "f0136_09"
key = {}
for r in csv.DictReader((l for l in open(D / "key.tsv") if not l.startswith("#")), delimiter="\t"):
    v = r["value"].split("|")[0].strip()
    if re.fullmatch(r"[a-z]{1,3}", v):
        key[r["code"]] = v
def spans():
    s = set()
    for g in ("gloss_A.tsv", "gloss_B.tsv"):
        for r in csv.DictReader(open(F / g), delimiter="\t"):
            s.update(r["tokids"].split())
    return s
def toks_target():
    glossed = spans(); out = []
    for r in csv.DictReader((l for l in open(F / "ciphertext.tsv") if not l.startswith("#")), delimiter="\t"):
        out += [t for i, t in enumerate(r["settled"].split()) if f"{r['line']}.{i}" not in glossed and t != "|"]
    return [t.strip("?") for t in out]
def toks_power():
    out = []
    for r in csv.DictReader(open(D / "f0085_09/reconciled.tsv"), delimiter="\t"):
        if r["run"] in ("9", "10"):
            out += r["codes"].split(".")
    return out
model = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA["fr18"]])
def dec(toks, k):
    return "".join(k[t] for t in toks if t in k)
lines = []
def gate(name, toks, seed):
    real = dec(toks, key); sc = model.score(real)
    if len(real) < 20:
        lines.append(f"{name}\tletters {len(real)}\tNON-TEST (under 20 letters)\t{real}"); return None
    codes, vals = list(key), list(key.values()); rng = random.Random(seed); sh = []
    for _ in range(1000):
        rng.shuffle(vals); sh.append(model.score(dec(toks, dict(zip(codes, vals)))))
    sh.sort(); p95, p99 = sh[949], sh[989]; ge = sum(s >= sc for s in sh)
    rl, nl, _ = model.controls(max(len(real), 20), samples=200)
    ok = sc > p95
    lines.append(f"{name}\tletters {len(real)}\treal {sc:.3f}\tpermuted mean {sum(sh)/1000:.3f} p95 {p95:.3f} p99 {p99:.3f} max {sh[-1]:.3f}\t"
                 f"permuted>=real {ge}/1000\t{'PASS' if ok else 'FAIL'} (real > p95)\treal_p05 {J.pct(sorted(rl),0.05):.3f} null_p99 {J.pct(sorted(nl),0.99):.3f}\t{real}")
    return ok
pw = gate("power_0085_r9r10", toks_power(), 136)
tg = gate("target_0136_unglossed", toks_target(), 136)
if not pw:
    lines.append("power control below its own p95: target result is a NON-TEST")
txt = "\n".join(lines) + "\n"
if "--check" in sys.argv:
    good = open(F / "judge_gate.out").read() == txt; print("judge_gate.out up to date" if good else "STALE"); sys.exit(0 if good else 1)
open(F / "judge_gate.out", "w").write(txt); print(txt, end="")
