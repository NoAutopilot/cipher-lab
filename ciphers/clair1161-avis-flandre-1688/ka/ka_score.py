#!/usr/bin/env python3
"""CL1161-KA (ka/PREREG-CL1161-KA.md): c186R token-level known-answer gate against George Lasry's f163r paragraph.
Usage: python3 ka/ka_score.py [--draws 1000]. Global NW (match +2, mismatch -1, gap -2, wildcard 0) of the c186R decode
(lkey/ciphertext_v2.tsv under lkey/key_v2.tsv) to the folded paragraph; per-token chunks; G1 (agreeing tokens vs a key-value
permutation null + a fixed-derangement power check) and G2 (masked conflict classes vs a position null + a qb power check)."""
import sys, csv, random, argparse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'tools'))
import judge_plaintext as J
T = Path(__file__).resolve().parents[1]
ap = argparse.ArgumentParser(); ap.add_argument('--draws', type=int, default=1000); a = ap.parse_args()
def F(s): return J.fold(s).replace('v', 'u').replace('j', 'i')
P = F("""Ce Seigneur a par deulx fois escript et mandé à ceste royne qu'elle laissast passer en silence et
dissimulation beaucoup de choses quant au faict de la religion en ce royaume afin de regaigner sa noblesse et peuple, et que son filz
et elle y puissent regner et commander en plus grand repos.""")
WILD = '\0'
def key(p): return {r['sign']: r['value'] for r in csv.DictReader(open(p), delimiter='\t')}
def toks(p): return [r['sign'] for r in csv.DictReader(open(p), delimiter='\t') if r['line'].startswith('c186R')]
def align(vals):
    """vals: per-token value strings (WILD for a hidden/no-value token). Returns per-token chunks and match count."""
    D, own = [], []
    for i, v in enumerate(vals):
        v = v if v and set(v) == {WILD} else (F(v) or WILD)
        for ch in v: D.append(ch); own.append(i)
    n, m = len(D), len(P)
    S = [[0] * (m + 1) for _ in range(n + 1)]; B = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): S[i][0] = -2 * i; B[i][0] = 1
    for j in range(1, m + 1): S[0][j] = -2 * j; B[0][j] = 2
    for i in range(1, n + 1):
        di = D[i - 1]; Si, Sp, Bi = S[i], S[i - 1], B[i]
        for j in range(1, m + 1):
            s = 0 if di == WILD else (2 if di == P[j - 1] else -1)
            d, u, l = Sp[j - 1] + s, Sp[j] - 2, Si[j - 1] - 2
            if d >= u and d >= l: Si[j], Bi[j] = d, 0
            elif u >= l: Si[j], Bi[j] = u, 1
            else: Si[j], Bi[j] = l, 2
    chunk = [''] * len(vals); i, j, pend, match = n, m, [], 0
    cols = []
    while i > 0 or j > 0:
        b = B[i][j]
        if i > 0 and j > 0 and b == 0: cols.append((i - 1, j - 1)); match += D[i - 1] == P[j - 1]; i -= 1; j -= 1
        elif i > 0 and (j == 0 or b == 1): cols.append((i - 1, None)); i -= 1
        else: cols.append((None, j - 1)); j -= 1
    cols.reverse(); cur = own[0] if own else 0
    for di, pj in cols:
        if di is not None: cur = own[di]
        if pj is not None: chunk[cur] += P[pj]
    return chunk, match
def agree(vals, chunk): return sum(1 for v, c in zip(vals, chunk) if F(v) and c == F(v))
def G1stat(tk, k):
    vals = [k.get(s, '') or '' for s in tk]; ch, mt = align(vals); return agree(vals, ch), mt
tk2, k2 = toks(T / 'lkey/ciphertext_v2.tsv'), key(T / 'lkey/key_v2.tsv')
pct = J.pct
A2, M2 = G1stat(tk2, k2)
rnd = random.Random(1); null = []
signs = sorted(k2)
for _ in range(a.draws):
    v = [k2[s] for s in signs]; rnd.shuffle(v); null.append(G1stat(tk2, dict(zip(signs, v)))[0])
null.sort(); p99 = pct(null, .99)
vw = [k2[s] for s in signs]; wrong = dict(zip(signs, vw[-1:] + vw[:-1])); Aw, Mw = G1stat(tk2, wrong)
print(f"P letters {len(P)}; c186R tokens {len(tk2)}")
print(f"G1 V2: agreeing tokens {A2}/{len(tk2)}, letter matches {M2}/{len(P)}; null({a.draws}) median {pct(null,.5)} p99 {p99} max {null[-1]}")
print(f"G1 GATE V2 > p99: {'PASS' if A2 > p99 else 'FAIL'}")
print(f"G1 power check (fixed derangement): agreeing {Aw}, letters {Mw}: {'FAILs gate (valid)' if not Aw > p99 else 'PASSES gate (G1 INVALID)'}")
tk1, kb = toks(T / 'ciphertext.tsv'), key(T / 'key.tsv')
for name, t, k in (('baseline key.tsv', tk1, kb), ('V1 key_lasry', tk1, key(T / 'lkey/key_lasry.tsv')), ('V2b', tk2, key(T / 'lkey/key_v2b.tsv'))):
    x = G1stat(t, k); print(f"  descriptive {name}: agreeing {x[0]}/{len(t)}, letters {x[1]}")
# G2
def masked(tk, k, pos, L=1):
    vals = [WILD * L if i in pos else (k.get(s, '') or '') for i, s in enumerate(tk)]; return align(vals)[0]
def g2(tk, k, sign, his, ours, seed=2):
    pos = {i for i, s in enumerate(tk) if s == sign}; L = max(len(his), len(ours))
    ch = masked(tk, k, pos, L); got = [ch[i] for i in sorted(pos)]
    nh, no = sum(c == his for c in got), sum(c == ours for c in got)
    r = random.Random(seed); other = [i for i in range(len(tk)) if i not in pos]; nl_h, nl_o = [], []
    for _ in range(a.draws):
        q = set(r.sample(other, len(pos))); c2 = masked(tk, k, q, L)
        nl_h.append(sum(c2[i] == his for i in q)); nl_o.append(sum(c2[i] == ours for i in q))
    ph, po = pct(sorted(nl_h), .99), pct(sorted(nl_o), .99)
    k_ = len(pos)
    if k_ < 3: v = 'undecided (<3 occurrences)'
    elif nh >= 3 and nh >= 2 * no and nh > ph: v = 'SUPPORTS his'
    elif no >= 3 and no >= 2 * nh and no > po: v = 'SUPPORTS ours'
    else: v = 'undecided'
    print(f"G2 {sign}: n={k_} chunks {got}; his '{his}' {nh} (null p99 {ph}), ours '{ours}' {no} (null p99 {po}) -> {v}")
    return v
pq = g2(tk2, k2, 'qb', 'a', 'o')
pw = (pq == 'SUPPORTS his')  # 'his' slot = a (true), 'ours' slot = o (known-wrong)
print(f"G2 power check qb: supports 'a' {pw}; qb=o supported {pq == 'SUPPORTS ours'} -> {'VALID' if pw else 'G2 INVALID'}")
g2(tk2, k2, 'n77', 'de', 'ii'); g2(tk2, k2, 'n48', 'fait', 'od'); g2(tk2, k2, '7', 'b', 'i'); g2(tk2, k2, 'S', 'n', 'u')
