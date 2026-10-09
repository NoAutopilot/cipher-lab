"""MANT-0491 gate (b) (f0491_08/PREREG-MANT0491.md): copy of f0490_08/judge_gate_L.py on f0491_08/judge/ciphertext.tsv, seed 491, plus the
PREREG's shuffled-target control (token order shuffled 1000x, seed 4910, decoded under the REAL key; share above the permuted p95 > 0.05 voids
the judge at this N: "judge cannot decide"). Was: MANT-0490L gate (b) (f0490_08/PREREG-MANT0490L.md): copy of f0474_08/judge_gate.py on the 0490 gutter run (f0490_08/judge_L/ciphertext.tsv), seeds 490(+k), otherwise unchanged. Was: MANT-0474 gate (b) (f0474_08/PREREG-MANT0474.md): copy of f0177_08/judge_gate.py run on the unglossed >= 15-token runs of 694/08 frame 0474 (f0474_08/judge/ciphertext.tsv); seeds 474(+k); otherwise unchanged. Original docstring: unglossed letter tokens of 694/08 frame 0177, real key.tsv vs letter-value-permuted keys
on the fr18 4-gram score (design of f0454_08/judge_gate.py, copied; f0454_08/ not edited). Changes fixed by the PREREG before any number:
(1) NAME-ABBREVIATION groups (a maximal run of exactly 2-3 codes whose sequence occurs as a whole run >= 3 times on the leaf) leave the stream;
(2) block rule: letter count L <= 52 -> leaf scored whole as MANT-0454 (seed 177); L > 52 -> consecutive non-overlapping 52-letter blocks from
the start, each vs 1000 permuted keys (seed 177+k) on the tokens covering the block, score truncated to the block; tail (< 52) reported only.
Power at the scored length from the positive-control streams (694/09 0085 r9+r10; 0136 unglossed), 200 permuted (seed 7) per window, pass if
real > 190th of 200; a TEST only if power >= 0.80. Leaf (b) = PASS (every block), MIXED (some), FAIL (none).
Writes f0177_08/judge_gate.out and f0177_08/token_blocks.tsv (tokid -> block / tail / abbrev / nonletter).
Run from the repository root: python3 ciphers/sachsstaatsarchiv-manteuffel-1712/f0491_08/judge_gate.py [--check]"""
import csv, random, re, sys
from collections import Counter
from pathlib import Path
sys.path.insert(0, "tools")
import judge_plaintext as J
D = Path("ciphers/sachsstaatsarchiv-manteuffel-1712"); F = D / "f0491_08" / "judge"; B = 52
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
# token stream with ids, gloss spans and name-abbreviation groups removed
glossed = spans(F); runs = {}
for r in rows(F / "ciphertext.tsv"):
    runs.setdefault(r["line"], []).append((f"{r['line']}.{r['pos']}", r["sign"]))
seqc = Counter(tuple(c for _, c in v) for v in runs.values() if 2 <= len(v) <= 3)
abbrev = {s for s, n in seqc.items() if n >= 3}
lab = {}; stream = []
for run, v in runs.items():
    isab = tuple(c for _, c in v) in abbrev
    for tid, c in v:
        if tid in glossed: lab[tid] = "gloss"
        elif isab: lab[tid] = "abbrev"
        elif c not in key: lab[tid] = "nonletter"
        else: stream.append((tid, c))
lines = []
for s in sorted(abbrev):
    ctx = [run for run, v in runs.items() if tuple(c for _, c in v) == s]
    lines.append(f"# name-abbreviation group {'.'.join(s)} = '{dec(list(s), key)}' x{len(ctx)}: {' '.join(ctx)}")
T = [c for _, c in stream]; real = dec(T, key); L = len(real)
pos = 0; tokletters = []
for tid, c in stream:
    tokletters.append((tid, pos, pos + len(key[c]))); pos += len(key[c])
verdicts = []
if L < 4:
    lines.append(f"leaf_0491\tletters {L}\ttoo-short (L < 4, not scored)\t{real}")
else:
    Ls = L if L <= B else B
    ok_w, n_w = power(Ls); pw = ok_w / n_w if n_w else 0.0
    lines.append(f"power\tat {Ls} letters: {ok_w}/{n_w} = {pw:.2f}\t{'TEST' if pw >= 0.80 else 'too-short (power < 0.80): neither PASS nor negative'}")
    nb = 1 if L <= B else L // B
    for k in range(1, nb + 1):
        a, b = (0, L) if L <= B else ((k - 1) * B, k * B)
        tk = [c for (tid, s0, s1), (_, c) in zip(tokletters, stream) if s1 > a and s0 < b]
        s0 = next(s for (tid, s, e) in tokletters if e > a)
        txt_k = dec(tk, key)[a - s0: a - s0 + (b - a)]
        sc = model.score(txt_k); seed = 491 if L <= B else 491 + k
        vals = list(key.values()); rng = random.Random(seed); sh = []
        for _ in range(1000):
            rng.shuffle(vals); sh.append(model.score(dec(tk, dict(zip(codes, vals)))[a - s0: a - s0 + (b - a)]))
        sh.sort(); p95, p99 = sh[949], sh[989]; ge = sum(s >= sc for s in sh); ok = sc > p95
        v = ("PASS" if ok else "FAIL") if pw >= 0.80 else f"too-short (own score {'above' if ok else 'not above'} p95)"
        verdicts.append(v)
        lines.append(f"block_{k}\tletters {a+1}-{b}\treal {sc:.3f}\tpermuted mean {sum(sh)/1000:.3f} p95 {p95:.3f} p99 {p99:.3f} max {sh[-1]:.3f}"
                     f"\tpermuted>=real {ge}/1000\t{v}\t{txt_k}")
    if L > B:
        lines.append(f"tail\tletters {nb*B+1}-{L}\treported only, not gated\t{real[nb*B:]}")
    rng2 = random.Random(4910); shs = []
    for _ in range(1000):
        t2 = T[:]; rng2.shuffle(t2); shs.append(model.score(dec(t2, key)[:B]))
    psh = perm_scores(T, 1000, 491, B)[949]; share = sum(x > psh for x in shs) / 1000
    lines.append(f"shuffled_target\t1000 order shuffles (seed 4910) under the real key: mean {sum(shs)/1000:.3f}, share above permuted p95 "
                 f"({psh:.3f}) {share:.3f}\t{'judge void at this N (judge cannot decide)' if share > 0.05 else 'judge not void'}")
    if share > 0.05: verdicts = ["judge-cannot-decide"]
    if pw < 0.80: leaf = "too-short"
    elif share > 0.05: leaf = "judge cannot decide"
    elif all(v == "PASS" for v in verdicts): leaf = "PASS"
    elif any(v == "PASS" for v in verdicts): leaf = "MIXED"
    else: leaf = "FAIL"
    lines.append(f"leaf_0491\tletters {L}\tblocks {len(verdicts)}\t{leaf}\t{real}")
    sc = model.score(real); sh = perm_scores(T, 1000, 491)
    lines.append(f"# whole leaf (reported, no power behind it if L > 62): real {sc:.3f} permuted mean {sum(sh)/1000:.3f} p95 {sh[949]:.3f} "
                 f"p99 {sh[989]:.3f} permuted>=real {sum(s >= sc for s in sh)}/1000")
lines.append("# per run (reported, not gates): run, letters, score, decoded letters")
for run, ts in toks(F, True).items():
    s = dec(ts, key); lines.append(f"{run}\t{len(s)}\t{model.score(s) if len(s) >= 4 else float('nan'):.3f}\t{s}")
txt = "\n".join(lines) + "\n"
tb = ["tokid\tcode\tblock"]
for run, v in runs.items():
    for tid, c in v:
        if tid in lab: tb.append(f"{tid}\t{c}\t{lab[tid]}"); continue
        _, s0, s1 = next(x for x in tokletters if x[0] == tid)
        if L < 4: blk = "unscored"
        elif L <= B: blk = "block_1"
        else:
            ks = {min(p // B + 1, 10**6) for p in range(s0, s1)}
            ks = {f"block_{k}" if k <= L // B else "tail" for k in ks}
            blk = "+".join(sorted(ks))
        tb.append(f"{tid}\t{c}\t{blk}")
tbt = "\n".join(tb) + "\n"
if "--check" in sys.argv:
    good = open(F / "judge_gate.out").read() == txt and open(F / "token_blocks.tsv").read() == tbt
    print("judge_gate.out/token_blocks.tsv up to date" if good else "STALE"); sys.exit(0 if good else 1)
open(F / "judge_gate.out", "w").write(txt); open(F / "token_blocks.tsv", "w").write(tbt); print(txt, end="")
