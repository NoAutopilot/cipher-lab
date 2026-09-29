#!/usr/bin/env python3
"""VERIFY-F61-V5 (29 Sept 2026): the verifier's own alignment of f.176r signs to its period decipherment fol. 177r(-v),
independent of the runner's f61crib.align. Semi-global DP (free end gaps on both sides), numpy column sweep:
  diagonal: +1 if the letter is in the anchor key's set for the sign's class, -1 if the class is in the key and the letter is not,
            0 if the class is not in the key (rare classes, the class left out, a disputed '?' column);
  sign without letter (null / letter the decipherer skipped): -1; letter without sign (abbreviation, decipherer's addition): -1.
Leave-class-out (LCO): to test class X, X is removed from the anchor key, so the letter opposite X is set only by its neighbours.
Controls: the wrong clear fr.3984 f.184r (same length), and 50 anchor keys whose letter sets are permuted across classes (seed 29+k).
  python3 align_v5.py runner [--check]     the runner's A/B passes (consensus, all 47 rows) against the runner's clear read
  python3 align_v5.py verifier [--check]   the verifier's P/Q passes (sample L06-L11, L28-L33) against the verifier's clear read
Writes align_v5_<mode>_result.txt."""
import glob, os, random, sys
from collections import Counter, defaultdict
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); F = os.path.abspath(f"{HERE}/../family")
sys.path.insert(0, F); sys.path.insert(0, os.path.abspath(f"{HERE}/../scripts"))
import h170_gate as g, build_f176_key as b
TEST = ["VBAR_A", "EBR", "HASH4", "4STEM", "DBL", "ZHOOK", "C43", "BETA", "4PI", "CROSS", "4TRI", "PHI", "INF", "VBAR_B", "SBS", "ISH", "LL"]
PROPOSED = {"VBAR_A": "t", "EBR": "l", "HASH4": "d", "4STEM": "p", "DBL": "o", "ZHOOK": "i", "BETA": "m"}
AL = "abcdefghilmnopqrstuxz"
# Tomokiyo's published 11 two-letter cells (keys/key_mayenne_1592.tsv), folded as h170_gate.fold (y -> i, so l/y reads l/i)
CELLS = ["an", "bo", "cp", "dq", "er", "fs", "gt", "hu", "ix", "li", "mz"]
def cell(C):
    n = sum(C.values())
    if not n: return "-", 0.0
    b = max(CELLS, key=lambda c: sum(C[x] for x in c)); return "/".join(b), sum(C[x] for x in b) / n
def dp(text, seq, key):
    n, m = len(text), len(seq); T = np.frombuffer(text.encode(), dtype=np.uint8)
    prev = np.zeros(n + 1); ptr = np.zeros((m + 1, n + 1), dtype=np.int8); idx = np.arange(n + 1)
    cols = [prev.copy()]
    for j, s in enumerate(seq, 1):
        if s in key:
            ok = np.isin(T, np.frombuffer("".join(key[s]).encode(), dtype=np.uint8)); sc = np.where(ok, 1.0, -1.0)
        else: sc = np.zeros(n)
        diag = np.full(n + 1, -1e9); diag[1:] = prev[:-1] + sc
        up = prev - 1.0; best = np.maximum(diag, up); p = np.where(diag >= up, 1, 2).astype(np.int8)
        best[0] = 0.0                                   # free leading letters... (row 0 = no letter used yet) -> free leading signs
        p[0] = 2
        # letter without sign: cur[i] = max(best[i], cur[i-1] - 1) -> cumulative max of best[k] + k, minus i
        cm = np.maximum.accumulate(best + idx) - idx; p = np.where(cm > best, 3, p).astype(np.int8)
        ptr[j] = p; prev = cm
    # free end gaps: best cell in the last column (all signs used) or any column's last row -- take last column max
    i = int(np.argmax(prev)); j = m; pairs = []
    while j > 0 and i > 0:
        p = ptr[j][i]
        if p == 1: pairs.append((i - 1, j - 1)); i -= 1; j -= 1
        elif p == 2: j -= 1
        else: i -= 1
    return pairs[::-1]
def count(text, seq, key, pairs):
    c = defaultdict(Counter); m = t = 0
    for i, j in pairs:
        s = seq[j]; c[s][text[i]] += 1
        if s in key: t += 1; m += text[i] in key[s]
    return c, (m / t if t else 0)
def load(mode):
    if mode == "runner":
        A, B = b.pass_rows("A"), b.pass_rows("B"); rows = [f"L{k:02d}" for k in range(1, 48)]
        seq = [s for l in rows for s in b.consensus(A[l], B[l])]; text, _ = b.clear_text(); return seq, text, rows
    P = f"{HERE}/passes"; blocks = [("L06-L11", "L05-L12", range(6, 12)), ("L28-L33", "L23-L29", range(28, 34))]; out = []
    for sr, cr, rng in blocks:
        rows_ = {}
        for tag in "PQ":
            d = defaultdict(list)
            for r in g.rd(f"{P}/f176r_signs{tag}_{sr}.tsv"):
                s = {"EBR_A": "EBR", "EBR_B": "EBR"}.get(r["sign"].strip(), r["sign"].strip())
                if s != "PLAIN": d[r["line"].strip()].append(s)
            rows_[tag] = d
        seq = [s for k in rng for s in b.consensus(rows_["P"][f"L{k:02d}"], rows_["Q"][f"L{k:02d}"])]
        text = "".join(g.fold(r["text"]) for r in g.rd(f"{P}/f177r_clearV_{cr}.tsv")); out.append((sr, seq, text))
    return out
def perm_key(key, rng):
    cls = sorted(key); sets = [key[c] for c in cls]; rng.shuffle(sets); return dict(zip(cls, sets))
def analyse(seq, text, label, out, nperm=50):
    key = g.load_key(); key["4TRI"] = key["4TRI"]
    wrong = g.fold(" ".join(r["word"] for r in g.rd(f"{F}/passes/f184r_clear_rec.tsv")))
    wrong = (wrong * (len(text) // len(wrong) + 1))[:len(text)]
    cons = sum(not s.startswith("?") for s in seq)
    fulltrue = count(text, seq, key, dp(text, seq, key)); fullwrong = count(wrong, seq, key, dp(wrong, seq, key))
    out.append(f"== {label}: {len(seq)} signs (consensus {cons}, {cons/len(seq):.2f}), {len(text)} clear letters")
    out.append(f"full key v4 anchors: in-set match true {fulltrue[1]:.3f} / wrong {fullwrong[1]:.3f}")
    out.append("class\tproposed\tn(true)\tLCO true: top letters\tshare(prop)\tLCO wrong: top\tshare(prop) wrong\tperm-key share(prop) mean/p95\tgate\tbest Tomokiyo cell true (share) / wrong (share)")
    fmt = lambda C: " ".join(f"{x}{k}" for x, k in sorted(C.items(), key=lambda t: (-t[1], t[0]))[:5])
    for X in TEST:
        if X not in seq: continue
        k2 = {c: v for c, v in key.items() if c != X}
        ct, _ = count(text, seq, k2, dp(text, seq, k2)); cw, _ = count(wrong, seq, k2, dp(wrong, seq, k2))
        T, W = ct[X], cw[X]; nt, nw = sum(T.values()), sum(W.values())
        top = T.most_common(1)[0][0] if nt else "-"; prop = PROPOSED.get(X, top)
        st = T[prop] / nt if nt else 0; sw = W[prop] / nw if nw else 0
        ps = []
        rng = random.Random(29)
        for k in range(nperm):
            pk = perm_key(k2, random.Random(29 + k)); cp, _ = count(text, seq, pk, dp(text, seq, pk)); P_ = cp[X]; npp = sum(P_.values())
            ps.append(P_[prop] / npp if npp else 0)
        ps.sort(); p95 = ps[int(0.95 * len(ps)) - 1]
        gate = "PASS" if (nt >= 5 and top == prop and st >= 0.5 and sw < st / 2 and st > p95) else ("n<5" if nt < 5 else "FAIL")
        tag = prop if X in PROPOSED else f"({top})"
        ce, cs = cell(T); we, ws = cell(W)
        out.append(f"{X}\t{tag}\t{nt}\t{fmt(T)}\t{st:.2f}\t{fmt(W)}\t{sw:.2f}\t{sum(ps)/len(ps):.2f}/{p95:.2f}\t{gate}\t{ce} ({cs:.2f}) / {we} ({ws:.2f})")
    out.append("")
def main():
    mode = sys.argv[1]; out = [f"# align_v5.py {mode} (VERIFY-F61-V5); columns: LCO = class left out of the anchor key; share(prop) = share of"
                               " the class's aligned positions carrying the proposed letter (runner's key_period_f176.tsv top letter);"
                               " gate = n>=5, top==proposed, share>=0.5, wrong share < half, share > permuted-anchor p95", ""]
    if mode == "runner":
        seq, text, _ = load(mode); analyse(seq, text, "runner passes A/B, f.176r L01-L47, runner clear fol. 177r-v", out, nperm=20)
    else:
        allseq, alltext = [], ""
        for sr, seq, text in load(mode):
            analyse(seq, text, f"verifier passes P/Q {sr}, verifier clear", out); allseq += seq; alltext += text
    res = "\n".join(out) + "\n"; path = f"{HERE}/align_v5_{mode}_result.txt"
    if "--check" in sys.argv:
        sys.exit(0 if open(path).read() == res else "STALE") if os.path.exists(path) else sys.exit("no result file")
    open(path, "w").write(res); print(res)
if __name__ == "__main__": main()
