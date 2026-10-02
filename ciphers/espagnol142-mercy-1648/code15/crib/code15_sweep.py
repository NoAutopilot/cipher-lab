#!/usr/bin/env python3
"""code15_sweep.py -- crib/ n-gram sweep for code 15 in v04 of BnF Espagnol 144 f.22v (Mercy, 6 June 1648).

Scratch analysis for issue 16 (D. Bourdeau's question, 1 Oct 2026). Read-only on the target's files.

1. Builds a letter 4-gram model (interpolated, add-k) from tools/data/es17c7 (Memorial historico espanol 13-19,
   Jesuit/court newsletters 1634-48: the target's era and register), folded to the cipher's alphabet
   (accents dropped, v->u, j->i, n~->n, c-cedilla->z, k->c, w dropped).
2. CONTROL (rule 3): for every S-graded single cipher token whose +-W-letter window lies inside one cipher run of
   f.22r-v (outside v04), substitutes each of the 22 candidate letters and records the rank of the key's own letter
   and the log-prob margin best-minus-second. Gives the method's top-1 rate and the precision at a given margin.
3. TARGET: v04:9 (the clear 15) with v04:11 read as 32 (n, as transcribed by passes A, B, Bourdeau) and as 31
   (i, as the native crop suggests, code15/crib/v04_31_vs_32_sheet.jpg). Same window, same scoring.
4. v04:19 (the half-cut glyph) followed by L = 0..3 letters lost at the trimmed edge, then v05 "aseramas...":
   brute force over the 15 value and the lost letters, top fills listed.
Writes code15/crib/sweep_result.tsv and prints a summary.
"""
import gzip, math, re, sys, unicodedata, itertools, collections
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
T = ROOT / "ciphers/espagnol142-mercy-1648"
OUT = Path(__file__).resolve().parent
LET = list("abcdefghilmnopqrstuxyz")  # 22 candidates (j,v,k,w folded away; 20 key letters + x, z)
W = 8

def fold(s):
    s = s.lower().replace("ç", "z").replace("ñ", "n")
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.replace("v", "u").replace("j", "i").replace("k", "c").replace("w", "")
    return re.sub(r"[^a-z]+", " ", s)

def build_model():
    txt = []
    for p in sorted((ROOT / "tools/data/es17c7").glob("*.txt.gz")):
        txt.append(fold(gzip.open(p, "rt", encoding="utf-8", errors="replace").read()))
    # letters only, word breaks removed (the cipher has no word division)
    s = re.sub(r"\s+", "", " ".join(txt))
    cnt = [collections.Counter() for _ in range(5)]
    for n in range(1, 5):
        c = cnt[n]
        for i in range(len(s) - n + 1):
            c[s[i:i + n]] += 1
    return cnt, len(s)

def make_scorer(cnt, N):
    lam = (0.02, 0.08, 0.3, 0.6)  # weights for 1..4-gram
    V = 23
    cache = {}
    def lp(ctx, ch):
        key = ctx + ch
        if key in cache:
            return cache[key]
        p = lam[0] * (cnt[1][ch] + 1) / (N + V)
        for n in (2, 3, 4):
            h = (ctx + ch)[-n:]
            if len(h) < n:
                continue
            d = cnt[n - 1][h[:-1]]
            if d:
                p += lam[n - 1] * cnt[n][h] / d
        v = math.log10(p)
        cache[key] = v
        return v
    def score(s):
        return sum(lp(s[max(0, i - 3):i], s[i]) for i in range(len(s)))
    return score

def runs():
    """Cipher runs as lists of (line,pos,letter,grade); f.22v trimmed-edge restorations inserted as pseudo-tokens,
    a run broken where the loss is unrestored."""
    rows = [l.rstrip("\n").split("\t") for l in open(T / "reading_tokens.tsv", encoding="utf-8")][1:]
    lost = {}
    for l in open(ROOT / "sources/cyphersolver/2026-10-01/mercy1648/lost_edge.tsv", encoding="utf-8").readlines()[1:]:
        f = l.rstrip("\n").split("\t")
        lost[f[0]] = f[2]
    out, cur, prev_line = [], [], None
    for line, pos, sign, conf, val, grade in rows:
        if prev_line and line != prev_line and prev_line.startswith("v"):
            L = lost.get(prev_line)
            if L and L != "?":
                cur += [(prev_line, "edge", ch, "R") for ch in L]
            elif L == "?":
                if cur: out.append(cur)
                cur = []
        if not re.fullmatch(r"[a-z]+", val or "") or len(val) != 1:
            # a clear word, a mark, a split/no-letter token: break the run (clear words) or keep (multi-letter)
            if sign.startswith("[PLAIN") or sign.startswith("[MARK") or not val:
                if cur: out.append(cur)
                cur = []
            else:
                for ch in val:
                    cur.append((line, pos, ch, "M"))
        else:
            cur.append((line, pos, val, grade))
        prev_line = line
    if cur: out.append(cur)
    return out

def main():
    cnt, N = build_model()
    score = make_scorer(cnt, N)
    R = runs()
    res = []
    # CONTROL
    ctrl = []
    for run in R:
        s = "".join(t[2] for t in run)
        for i, t in enumerate(run):
            if t[3] != "S" or t[0] == "v04":
                continue
            if i < W or i + W >= len(run):
                continue
            left, right = s[i - W:i], s[i + 1:i + 1 + W]
            sc = sorted(((score(left + c + right), c) for c in LET), reverse=True)
            rank = [c for _, c in sc].index(t[2]) + 1
            ctrl.append((t[0], t[1], t[2], rank, sc[0][1], round(sc[0][0] - sc[1][0], 3)))
    top1 = sum(1 for r in ctrl if r[3] == 1) / len(ctrl)
    top3 = sum(1 for r in ctrl if r[3] <= 3) / len(ctrl)
    print(f"CONTROL: {len(ctrl)} S-graded single tokens with a full +-{W} window; key letter ranked 1st {top1:.3f}, top-3 {top3:.3f}")
    for thr in (0.3, 0.5, 1.0, 1.5):
        sel = [r for r in ctrl if r[5] >= thr]
        if sel:
            print(f"  margin >= {thr}: {len(sel)} positions, top-1 correct {sum(1 for r in sel if r[3]==1)/len(sel):.3f}")
    # TARGET v04:9
    left = "edellayquecorraporsu" + "ma" + "noladire"  # v03 + [ma] restored at the edge + v04:1-8
    for tag, mid in (("v04:11=32 (n, as transcribed)", "tnonysiiu"), ("v04:11=31 (i, crop re-read)", "tionysiiu")):
        rightW = mid[:W]
        sc = sorted(((score(left[-W:] + c + rightW), c) for c in LET), reverse=True)
        print(f"TARGET v04:9, {tag}: window '{left[-W:]}?{rightW}'")
        print("   " + "  ".join(f"{c}:{v:.2f}" for v, c in sc[:8]) + f"   margin {sc[0][0]-sc[1][0]:.2f}")
        for v, c in sc:
            res.append(("v04:9", tag, c, round(v, 3)))
    # v04:19 + lost letters
    right5 = "aseramasconuenient"
    print("v04:19 (cut) + L lost letters + v05 'aseramas...': top fills")
    for tag, pre in (("v04:11=31", "ladirectionysiiu"), ):
        for L in range(0, 4):
            best = []
            for c15 in LET:
                for fill in itertools.product(LET, repeat=L):
                    s = pre + c15 + "".join(fill) + right5[:10]
                    best.append((score(s), c15, "".join(fill)))
            best.sort(reverse=True)
            print(f"  L={L}: " + ", ".join(f"iu[{c}]{f}|a.. {v:.1f}" for v, c, f in best[:6]))
            for v, c, f in best[:20]:
                res.append(("v04:19", f"{tag} L={L}", c + f, round(v, 3)))
    with open(OUT / "sweep_result.tsv", "w") as fh:
        fh.write("where\tvariant\tcandidate\tlog10p\n")
        for r in res:
            fh.write("\t".join(map(str, r)) + "\n")
    with open(OUT / "control_ranks.tsv", "w") as fh:
        fh.write("line\tpos\tkey_letter\trank\tmodel_best\tmargin\n")
        for r in ctrl:
            fh.write("\t".join(map(str, r)) + "\n")

if __name__ == "__main__":
    main()
