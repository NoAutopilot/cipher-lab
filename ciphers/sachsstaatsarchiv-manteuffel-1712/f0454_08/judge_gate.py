"""MANT-0454 gate (b) (f0454_08/PREREG-MANT-0454.md): unglossed letter tokens of 694/08 frame 0454, real key.tsv vs 1000 letter-value-permuted
keys on the fr18 4-gram score (design of ungl09/judge_gate.py, copied; ungl09/ and f0136_09/ not edited).
Power control AT THIS LEAF'S N (rule 3 last paragraph): every window of the positive-control streams (694/09 0085 r9+r10; 0136 unglossed tokens)
truncated to the target's letter count L, 200 permuted keys (seed 7) per window, pass if real > p95; power = share passing; the gate is a TEST
only if power >= 0.80, else "too-short". Gate: real > p95 of 1000 permuted (seed 454). Also reported, not gates: each run's own score; the
repeated-run consistency figure (token-by-token agreement of the two witnesses named in the PREREG).
Run from the repository root: python3 ciphers/sachsstaatsarchiv-manteuffel-1712/f0454_08/judge_gate.py [--check]"""
import csv, random, re, sys
from pathlib import Path
sys.path.insert(0, "tools")
import judge_plaintext as J
D = Path("ciphers/sachsstaatsarchiv-manteuffel-1712"); F = D / "f0454_08"
key = {}
for r in csv.DictReader((l for l in open(D / "key.tsv") if not l.startswith("#")), delimiter="\t"):
    v = r["value"].split("|")[0].strip()
    if re.fullmatch(r"[a-z]{1,3}", v):
        key[r["code"]] = v
def rows(p):
    return list(csv.DictReader((l for l in open(p) if not l.startswith("#")), delimiter="\t"))
def spans(G):
    s = set()
    for g in ("gloss_A.tsv", "gloss_B.tsv"):
        if (G / g).exists():
            for r in csv.DictReader(open(G / g), delimiter="\t"):
                s.update(r["tokids"].split())
    return s
def toks(G, by_run=False):
    glossed = spans(G); out = {}
    for r in rows(G / "ciphertext.tsv"):
        if f"{r['line']}.{r['pos']}" not in glossed:
            out.setdefault(r["line"], []).append(r["sign"])
    return out if by_run else [t for v in out.values() for t in v]
def toks_0085():
    out = []
    for r in csv.DictReader(open(D / "f0085_09/reconciled.tsv"), delimiter="\t"):
        if r["run"] in ("9", "10"):
            out += r["codes"].split(".")
    return out
model = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA["fr18"]])
def dec(ts, k):
    return "".join(k[t] for t in ts if t in k)
codes = list(key)
def perm_scores(ts, n, seed, L=None):
    vals = list(key.values()); rng = random.Random(seed); out = []
    for _ in range(n):
        rng.shuffle(vals); s = dec(ts, dict(zip(codes, vals)))
        out.append(model.score(s[:L] if L else s))
    return sorted(out)
def power(L):
    wins = []
    for st in ([t for t in toks_0085() if t in key], [t for t in toks(D / "f0136_09") if t in key]):
        for i in range(len(st)):
            j = i; n = 0
            while j < len(st) and n < L:
                n += len(key[st[j]]); j += 1
            if n >= L:
                wins.append(st[i:j])
    ok = sum(model.score(dec(w, key)[:L]) > perm_scores(w, 200, 7, L)[189] for w in wins)
    return ok, len(wins)
lines = []
T = toks(F); real = dec(T, key); L = len(real)
if L < 4:
    lines.append(f"leaf_0454\tletters {L}\ttoo-short (L < 4, not scored)\t{real}")
else:
    ok_w, n_w = power(L); pw = ok_w / n_w if n_w else 0.0
    sc = model.score(real); sh = perm_scores(T, 1000, 454)
    p95, p99 = sh[949], sh[989]; ge = sum(s >= sc for s in sh); ok = sc > p95
    verdict = ("PASS" if ok else "FAIL") if pw >= 0.80 else f"too-short (power {pw:.2f} < 0.80; own score {'above' if ok else 'not above'} p95)"
    lines.append(f"leaf_0454\tletters {L}\tpower at L: {ok_w}/{n_w} = {pw:.2f}\treal {sc:.3f}\tpermuted mean {sum(sh)/1000:.3f} p95 {p95:.3f} "
                 f"p99 {p99:.3f} max {sh[-1]:.3f}\tpermuted>=real {ge}/1000\t{verdict}\t{real}")
lines.append("# per run (reported, not gates): run, letters, score, decoded letters")
for run, ts in toks(F, True).items():
    s = dec(ts, key); lines.append(f"{run}\t{len(s)}\t{model.score(s) if len(s) >= 4 else float('nan'):.3f}\t{s}")
R = {r["line"]: [x["sign"] for x in rows(F / "ciphertext.tsv") if x["line"] == r["line"]] for r in rows(F / "ciphertext.tsv")}
pair = [k for k in R if k.endswith(("r03", "r15"))]
if len(pair) == 2:
    a, b = R[pair[0]], R[pair[1]]; same = sum(x == y for x, y in zip(a, b))
    lines.append(f"# repeated run {pair[0]} vs {pair[1]}: {same}/{max(len(a), len(b))} positions agree; {' '.join(a)} | {' '.join(b)}")
txt = "\n".join(lines) + "\n"
if "--check" in sys.argv:
    good = open(F / "judge_gate.out").read() == txt; print("judge_gate.out up to date" if good else "STALE"); sys.exit(0 if good else 1)
open(F / "judge_gate.out", "w").write(txt); print(txt, end="")
