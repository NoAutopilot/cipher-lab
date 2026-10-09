"""V-MANT0490L rule-3 shuffle check on MANT-0490L gate (b) (f0490_08/PREREG-V-MANT0490L.md): judge_gate_L.py's block test (fr18, key.tsv
decode vs 1000 permuted keys, seed 490, PASS if real > p95) on 200 order-shuffles (seeds 1-200) of the gutter run's keyed letter tokens.
Run from the repository root: python3 ciphers/sachsstaatsarchiv-manteuffel-1712/f0490_08/vmant0490L_shuffle.py [--check]"""
import csv, random, re, sys, statistics
from pathlib import Path
sys.path.insert(0, "tools")
import judge_plaintext as J
D = Path("ciphers/sachsstaatsarchiv-manteuffel-1712"); F = D / "f0490_08"
key = {}
for r in csv.DictReader((l for l in open(D / "key.tsv") if not l.startswith("#")), delimiter="\t"):
    v = r["value"].split("|")[0].strip()
    if re.fullmatch(r"[a-z]{1,3}", v):
        key[r["code"]] = v
codes = list(key)
T = [r["sign"] for r in csv.DictReader((l for l in open(F / "judge_L/ciphertext.tsv") if not l.startswith("#")), delimiter="\t") if r["sign"] in key]
model = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA["fr18"]])
dec = lambda ts, k: "".join(k[t] for t in ts if t in k)
def test(ts):
    sc = model.score(dec(ts, key)); vals = list(key.values()); rng = random.Random(490); sh = []
    for _ in range(1000):
        rng.shuffle(vals); sh.append(model.score(dec(ts, dict(zip(codes, vals)))))
    sh.sort(); return sc, sh[949], sc > sh[949]
lines = []; r0 = test(T)
lines.append(f"target\ttokens {len(T)}\tletters {len(dec(T, key))}\treal {r0[0]:.3f}\tp95 {r0[1]:.3f}\t{'PASS' if r0[2] else 'FAIL'}\t{dec(T, key)}")
npass = 0; reals = []
for s in range(1, 201):
    ts = T[:]; random.Random(s).shuffle(ts); sc, p95, ok = test(ts); npass += ok; reals.append(sc)
    lines.append(f"shuffle_{s}\treal {sc:.3f}\tp95 {p95:.3f}\t{'PASS' if ok else 'FAIL'}\t{dec(ts, key)}")
lines.insert(1, f"SUMMARY\tshuffled decodes PASS {npass}/200 (void if > 10/200)\tmedian shuffled real {statistics.median(reals):.3f}\tmax {max(reals):.3f}"
                f"\tshuffles >= target real {sum(x >= r0[0] for x in reals)}/200\tverdict {'VOID' if npass > 10 else 'judge usable at N=38'}")
txt = "\n".join(lines) + "\n"; out = F / "vmant0490L_shuffle.out"
if "--check" in sys.argv:
    good = out.read_text() == txt; print("up to date" if good else "STALE"); sys.exit(0 if good else 1)
out.write_text(txt); print("\n".join(lines[:2]))
