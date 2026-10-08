"""MANT-R8 gate (f0375_08/PREREG-MANTR8.md; same design as f0390_08/shuffle_gate_0390.py): real key vs 1000 shuffled keys on
the fr18 4-gram score, pooled (seed 375) and per frame (seed = frame number; < 20 letters reported, not gated); power control =
694/09 0085 runs 9+10. Also a variant with singleton codes dropped (reported, not the registered statistic). No known-answer check.
Run from the repository root: python3 ciphers/sachsstaatsarchiv-manteuffel-1712/f0375_08/shuffle_gate_0375.py"""
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
ok = gate("power_0085_r9r10", toks_power(), 15)
gate("pooled_7_frames", toks(), 375)
for f, s in (("08_0375", 375), ("08_0214", 214), ("08_0436", 436), ("08_0241", 241), ("08_0435", 435), ("08_0065", 65),
             ("09_0070", 70)):
    gate(f"frame_{f}", toks(f), s)
gate("variant_runs_only_no_singletons", toks(singles=False), 375, gated=False)
if not ok:
    print("power control below gate: target result is a NON-TEST")
