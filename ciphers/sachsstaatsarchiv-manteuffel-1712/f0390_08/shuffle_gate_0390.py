"""MANT-08 gate (PREREG-MANT08.md): real key vs 1000 shuffled keys on the fr18 4-gram score, pooled (seed 8) and per frame
(seeds 390/391/395/485; < 20 letters reported, not gated); power control = 694/09 0085 runs 9+10 (as PREREG-MANT15).
Also a variant with singleton codes dropped (reported, not the registered statistic), and the 0391 'bon gre malgre' check.
Run from the repository root: python3 ciphers/sachsstaatsarchiv-manteuffel-1712/f0390_08/shuffle_gate_0390.py"""
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
for r in csv.DictReader((l for l in open(D / "f0390_08/ciphertext.tsv") if not l.startswith("#")), delimiter="\t"):
    runs.setdefault(r["line"], []).append(r["sign"])
def toks(frame=None, singles=True):
    out = []
    for ln, t in runs.items():
        if frame and f"_{frame}_" not in ln: continue
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
gate("pooled_0390_0391_0395_0485", toks(), 8)
for f, s in (("0390", 390), ("0391", 391), ("0395", 395), ("0485", 485)):
    gate(f"frame_{f}", toks(f), s)
gate("variant_runs_only_no_singletons", toks(singles=False), 8, gated=False)
if not ok:
    print("power control below gate: target result is a NON-TEST")
# known-answer check (pre-registered): decode of 0391_r5 vs 'bongremalgre'
def ed(a, b):
    p = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        c = [i]
        for j, cb in enumerate(b, 1):
            c.append(min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (ca != cb)))
        p = c
    return p[-1]
t = runs["694-08_0391_r5"]; ref = "bongremalgre"
real = dec(t, key); rd = ed(real, ref)
codes, vals = list(key), list(key.values()); rng = random.Random(5); sd = []
for _ in range(1000):
    rng.shuffle(vals); sd.append(ed(dec(t, dict(zip(codes, vals))), ref))
sd.sort()
print(f"known_answer_0391_r5\treal '{real}' edit distance to '{ref}' {rd}\tshuffled keys: min {sd[0]} p01 {sd[10]} median {sd[500]}\t"
      f"agreement {len(ref)-rd}/{len(ref)}")
