"""FAM-MANT15 gate (PREREG-MANT15.md): real key vs 1000 shuffled keys on the fr18 4-gram score; power control = 0085 runs 9+10.
Run from the repository root: python3 ciphers/sachsstaatsarchiv-manteuffel-1712/f0015_09/shuffle_gate_0015.py"""
import csv, random, re, sys
from pathlib import Path
sys.path.insert(0, "tools")
import judge_plaintext as J
D = Path("ciphers/sachsstaatsarchiv-manteuffel-1712")
key = {}
for r in csv.DictReader((l for l in open(D / "key.tsv") if not l.startswith("#")), delimiter="\t"):
    v = r["value"].split("|")[0].strip()
    if re.fullmatch(r"[a-z]{1,3}", v):
        key[r["code"]] = v
def toks_target():
    return [r["sign"] for r in csv.DictReader((l for l in open(D / "f0015_09/ciphertext.tsv") if not l.startswith("#")), delimiter="\t")]
def toks_power():
    out = []
    for r in csv.DictReader(open(D / "f0085_09/reconciled.tsv"), delimiter="\t"):
        if r["run"] in ("9", "10"):
            out += r["codes"].split(".")
    return out
model = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA["fr18"]])
def dec(toks, k):
    return "".join(k[t] for t in toks if t in k)
def gate(name, toks, seed):
    real = dec(toks, key); sc = model.score(real)
    codes, vals = list(key), list(key.values()); rng = random.Random(seed); sh = []
    for _ in range(1000):
        rng.shuffle(vals); sh.append(model.score(dec(toks, dict(zip(codes, vals)))))
    sh.sort(); p99 = sh[int(0.99 * 999)]; ge = sum(s >= sc for s in sh)
    rl, nl, _ = model.controls(max(len(real), 20), samples=200)
    print(f"{name}\tletters {len(real)}\treal {sc:.3f}\tshuffle mean {sum(sh)/1000:.3f} p99 {p99:.3f} max {sh[-1]:.3f}\t"
          f"shuffles>=real {ge}/1000\t{'PASS' if ge <= 10 else 'FAIL'}\treal_p05 {J.pct(sorted(rl),0.05):.3f} null_p99 {J.pct(sorted(nl),0.99):.3f}\t{real}")
    return ge <= 10
ok = gate("power_0085_r9r10", toks_power(), 15)
gate("target_0015_0016", toks_target(), 15)
if not ok:
    print("power control below gate: target result is a NON-TEST")
