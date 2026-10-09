"""MANT-UNGL gate (b) (ungl09/PREREG-MANT-UNGL.md): unglossed letter tokens of 694/09 0046, 0103, 0233, per leaf and pooled, real key.tsv
vs 1000 letter-value-permuted keys on the fr18 4-gram score (design of f0136_09/judge_gate.py, copied, f0136_09/ not edited).
Power control AT EACH N (rule 3 last paragraph): every window of the positive-control streams (0085 r9+r10; 0136 unglossed tokens)
truncated to the target's letter count L, 200 permuted keys (seed 7) per window, pass if real > p95; power = share passing; the gate
is a TEST only if power >= 0.80, else "too-short". Gate: real > p95 of 1000 permuted (seeds 46, 103, 233; pooled 9).
Run from the repository root: python3 ciphers/sachsstaatsarchiv-manteuffel-1712/ungl09/judge_gate.py [--check]"""
import csv, random, re, sys
from pathlib import Path
sys.path.insert(0, "tools")
import judge_plaintext as J
D = Path("ciphers/sachsstaatsarchiv-manteuffel-1712"); U = D / "ungl09"
key = {}
for r in csv.DictReader((l for l in open(D / "key.tsv") if not l.startswith("#")), delimiter="\t"):
    v = r["value"].split("|")[0].strip()
    if re.fullmatch(r"[a-z]{1,3}", v):
        key[r["code"]] = v
def rows(p):
    return list(csv.DictReader((l for l in open(p) if not l.startswith("#")), delimiter="\t"))
def spans(F):
    s = set()
    for g in ("gloss_A.tsv", "gloss_B.tsv"):
        if (F / g).exists():
            for r in csv.DictReader(open(F / g), delimiter="\t"):
                s.update(r["tokids"].split())
    return s
def toks_leaf(frame):
    F = D / f"f{frame}_09"; glossed = spans(F)
    return [r["sign"] for r in rows(F / "ciphertext.tsv") if f"{r['line']}.{r['pos']}" not in glossed]
def toks_0136():
    F = D / "f0136_09"; glossed = spans(F)
    return [r["sign"] for r in rows(F / "ciphertext.tsv") if f"{r['line']}.{r['pos']}" not in glossed]
def toks_0085():
    out = []
    for r in csv.DictReader(open(D / "f0085_09/reconciled.tsv"), delimiter="\t"):
        if r["run"] in ("9", "10"):
            out += r["codes"].split(".")
    return out
model = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA["fr18"]])
def dec(toks, k):
    return "".join(k[t] for t in toks if t in k)
codes = list(key)
def perm_scores(toks, n, seed, L=None):
    vals = list(key.values()); rng = random.Random(seed); out = []
    for _ in range(n):
        rng.shuffle(vals); s = dec(toks, dict(zip(codes, vals)))
        out.append(model.score(s[:L] if L else s))
    return sorted(out)
def power(L):
    wins = []
    for name, st in (("0085", [t for t in toks_0085() if t in key]), ("0136", [t for t in toks_0136() if t in key])):
        for i in range(len(st)):
            j = i; n = 0
            while j < len(st) and n < L:
                n += len(key[st[j]]); j += 1
            if n >= L:
                wins.append(st[i:j])
    ok = 0
    for w in wins:
        sh = perm_scores(w, 200, 7, L)
        ok += model.score(dec(w, key)[:L]) > sh[189]
    return ok, len(wins)
lines = []
def gate(name, toks, seed):
    real = dec(toks, key); L = len(real)
    if L < 4:
        lines.append(f"{name}\tletters {L}\ttoo-short (L < 4, not scored)\t{real}"); return "too-short"
    ok_w, n_w = power(L); pw = ok_w / n_w if n_w else 0.0
    sc = model.score(real); sh = perm_scores(toks, 1000, seed)
    p95, p99 = sh[949], sh[989]; ge = sum(s >= sc for s in sh); ok = sc > p95
    test = pw >= 0.80
    verdict = ("PASS" if ok else "FAIL") if test else f"too-short (power {pw:.2f} < 0.80; own score {'above' if ok else 'not above'} p95)"
    lines.append(f"{name}\tletters {L}\tpower at L: {ok_w}/{n_w} = {pw:.2f}\treal {sc:.3f}\tpermuted mean {sum(sh)/1000:.3f} p95 {p95:.3f} "
                 f"p99 {p99:.3f} max {sh[-1]:.3f}\tpermuted>=real {ge}/1000\t{verdict}\t{real}")
    return verdict
T = {f: toks_leaf(f) for f in ("0046", "0103", "0233")}
for f, sd in (("0046", 46), ("0103", 103), ("0233", 233)):
    gate(f"leaf_{f}", T[f], sd)
gate("pooled_0046_0103_0233", T["0046"] + T["0103"] + T["0233"], 9)
txt = "\n".join(lines) + "\n"
if "--check" in sys.argv:
    good = open(U / "judge_gate.out").read() == txt; print("judge_gate.out up to date" if good else "STALE"); sys.exit(0 if good else 1)
open(U / "judge_gate.out", "w").write(txt); print(txt, end="")
