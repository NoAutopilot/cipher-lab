#!/usr/bin/env python3
"""V-OLD-O5 (verifier, 10 Oct 2026): independent recount of the leaf 4/5/7 S shares and longest S stretches.
Reads only committed files: reading_L457_tokens.tsv (OLD-O2 grades) and depth/wb_tokens_OLDWB.tsv (OLD-WB grades).
Also re-runs OLD-WB's sign-agreement step with the OPPOSITE alignment tie-break (ins > del > diag) as a robustness check.
Digits counted = signs 2/3/4/7/8 per cipher token; a stretch is broken by any non-S cipher token; clear tokens do not break it;
stretches do not cross leaves. --check: exit 1 if the printed numbers differ from the figures recorded in AUDIT 6."""
import csv, os, re, sys
H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPECT = {"o2": (1479, 266, 13), "wb": (1479, 511, 17)}

def load(fn, gcol):
    rows = list(csv.DictReader(open(os.path.join(H, fn)), delimiter="\t"))
    out = []
    for r in rows:
        tok = r["raw_token"]
        if not re.search(r"\d", tok):
            continue
        d = sum(c in "23478" for c in tok)
        out.append((r["block"], d, r[gcol] == "S", r["decode"]))
    return out

def stats(toks):
    tot = sum(d for _, d, _, _ in toks); s = sum(d for _, d, g, _ in toks if g)
    best = (0, ""); cur = 0; words = []; blk = None
    for b, d, g, w in toks:
        if b != blk:
            cur, words, blk = 0, [], b
        if g:
            cur += d; words.append(w)
            if cur > best[0]: best = (cur, b + " " + " ".join(words))
        else:
            cur, words = 0, []
    return tot, s, best

res = {}
for name, fn, col in (("o2", "reading_L457_tokens.tsv", "grade"), ("wb", "depth/wb_tokens_OLDWB.tsv", "grade_WB")):
    toks = load(fn, col)
    for leaf in ("L4", "L5", "L7"):
        t, s, b = stats([x for x in toks if x[0] == leaf])
        print(f"{name} {leaf}: digits {t} S {s} ({100*s/t:.1f}%) longest {b[0]} [{b[1]}]")
    t, s, b = stats(toks)
    print(f"{name} pooled: digits {t} S {s} ({100*s/t:.1f}%) longest {b[0]} [{b[1]}]")
    res[name] = (t, s, b[0])

# robustness: OLD-WB sign agreement with the opposite tie-break
sys.path.insert(0, os.path.join(H, "scripts"))
import decode_L457 as D, wb_stest as W
def align_agree_rev(r, p):
    n, m = len(r), len(p)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1): dp[i][0] = i
    for j in range(m+1): dp[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = min(dp[i-1][j-1] + (r[i-1] != p[j-1]), dp[i-1][j] + 1, dp[i][j-1] + 1)
    ok = [False]*n; i, j = n, m
    while i > 0 and j > 0:
        if dp[i][j] == dp[i][j-1] + 1: j -= 1
        elif dp[i][j] == dp[i-1][j] + 1: i -= 1
        else: ok[i-1] = r[i-1] == p[j-1]; i -= 1; j -= 1
    return ok
W.align_agree = align_agree_rev
struct = W.structure()
ag = sum(1 for _, _, rows in struct for r in rows if r["cipher"] and r["agreed"])
best = 0
for leaf in ("L4", "L5", "L7"):
    cur = 0
    for blk, ln, rows in struct:
        if blk != leaf: continue
        for r in rows:
            if not r["cipher"]: continue
            if r["agreed"]: cur += r["digits"]; best = max(best, cur)
            else: cur = 0
print(f"tie-break ins>del>diag: sign-agreed cipher tokens {ag} (OLD-WB 324); ceiling longest sign-agreed stretch {best} digits (OLD-WB 17)")
if "--check" in sys.argv:
    bad = [k for k in EXPECT if res[k] != EXPECT[k]]
    print("check:", "OK" if not bad else f"STALE {bad}"); sys.exit(1 if bad else 0)
