"""V-MANTR8 (verifier, 8 Oct 2026): robustness of the MANT-R8 pooled shuffled-key gate -- fresh seeds, 10,000 shuffles, leave-one-frame-out.
Same scorer and shuffle design as shuffle_gate_0375.py (imported verbatim below). Run from the repository root."""
import csv, random, re, sys
from collections import OrderedDict
from pathlib import Path
sys.path.insert(0, "tools")
import judge_plaintext as J
D = Path("ciphers/sachsstaatsarchiv-manteuffel-1712")
key = {}
for r in csv.DictReader((l for l in open(D / "key.tsv") if not l.startswith("#")), delimiter="\t"):
    v = r["value"].split("|")[0].strip()
    if re.fullmatch(r"[a-z]{1,3}", v):
        key[r["code"]] = v
runs = OrderedDict()
for r in csv.DictReader((l for l in open(D / "f0375_08/ciphertext.tsv") if not l.startswith("#")), delimiter="\t"):
    runs.setdefault(r["line"], []).append(r["sign"])
def toks(frame=None, singles=True):
    out = []
    for ln, t in runs.items():
        if frame and f"-{frame}_" not in ln: continue
        if not singles and len(t) < 2: continue
        out += t
    return out
def toks_power():
    out = []
    for r in csv.DictReader(open(D / "f0085_09/reconciled.tsv"), delimiter="\t"):
        if r["run"] in ("9", "10"):
            out += r["codes"].split(".")
    return out
model = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA["fr18"]])
def dec(t, k):
    return "".join(k[x] for x in t if x in k)
def gate(name, t, seed, gated=True):
    real = dec(t, key); sc = model.score(real)
    codes, vals = list(key), list(key.values()); rng = random.Random(seed); sh = []
    for _ in range(1000):
        rng.shuffle(vals); sh.append(model.score(dec(t, dict(zip(codes, vals)))))
    sh.sort(); p99 = sh[int(0.99 * 999)]; ge = sum(s >= sc for s in sh)
    verdict = ("PASS" if ge <= 10 else "FAIL") if gated and len(real) >= 20 else "reported (not gated)"
    print(f"{name}\tletters {len(real)}\treal {sc:.3f}\tshuffle mean {sum(sh)/1000:.3f} p99 {p99:.3f} max {sh[-1]:.3f}\t"
          f"shuffles>=real {ge}/1000\t{verdict}\t{real}")
    return ge <= 10
def ge_of(t, seed, n=1000):
    real = dec(t, key); sc = model.score(real)
    codes, vals = list(key), list(key.values()); rng = random.Random(seed); c = 0
    for _ in range(n):
        rng.shuffle(vals); c += model.score(dec(t, dict(zip(codes, vals)))) >= sc
    return c, len(real)
T = toks()
print("pooled fresh seeds:")
for s in (1, 2, 3, 4, 5, 2026, 1008, 8812, 4242, 777):
    print(" seed", s, ge_of(T, s))
print("pooled 10000 shuffles seed 99:", ge_of(T, 99, 10000))
frames = ("08_0375","08_0214","08_0436","08_0241","08_0435","08_0065","09_0070")
print("leave-one-frame-out (seed 11):")
for f in frames:
    t = []
    for ln, tt in runs.items():
        if f"-{f}_" in ln: continue
        t += tt
    print(" drop", f, ge_of(t, 11))
t = []
for ln, tt in runs.items():
    if "-08_0214_" in ln or "-08_0065_" in ln: continue
    t += tt
print(" drop 0214+0065", ge_of(t, 11))
