#!/usr/bin/env python3
"""R8-ROUS3 (6 Oct 2026): registered count-vector gate over the four slip-backed pairs (align/PREREG-R8-ROUS3.md).
Run from the target folder: python3 align/r8rous3_countgate.py > align/r8rous3_countgate.out"""
import random, re, unicodedata
from collections import Counter

PAIRS = [("p1", "ciphertext_f213.txt", "slip_f214r.txt"), ("p2", "ciphertext_f216v.txt", "slip_f217r.txt"),
         ("p3", "ciphertext_f249.txt", "slip_f250.txt"), ("p4", "ciphertext_f266r.txt", "slip_f265r.txt")]
PRIMARY = [("605", "republique"), ("739", "venise"), ("52", "la")]
DRAWS, SEED, ALPHA = 2000, 8, 0.05

def groups(path):
    out = []
    for ln in open(path, encoding="utf-8"):
        if ln.startswith("L"):
            out += [t.split("|")[0] for t in ln.split()[1:]]
    return out

def words(path):
    txt = " ".join(l for l in open(path, encoding="utf-8") if not l.startswith("#"))
    txt = unicodedata.normalize("NFKD", txt.lower())
    txt = "".join(ch for ch in txt if not unicodedata.combining(ch))
    toks = [t for t in re.split(r"[^a-z]+", txt) if t]
    out, i = [], 0
    while i < len(toks):
        if toks[i] == "la" and i + 1 < len(toks) and toks[i + 1] == "reine":
            out.append("la_reine"); i += 2
        else:
            out.append(toks[i]); i += 1
    return out

G = [groups(c) for _, c, _ in PAIRS]
W = [words(s) for _, _, s in PAIRS]
gc = [Counter(g) for g in G]; wc = [Counter(w) for w in W]
vec_c = lambda c, cs=gc: tuple(x[c] for x in cs)
vec_w = lambda w, ws=wc: tuple(x[w] for x in ws)
codes = sorted(set().union(*G), key=int)

def redeal(lists, rng):
    pool = [t for l in lists for t in l]; rng.shuffle(pool); out, i = [], 0
    for l in lists:
        out.append(Counter(pool[i:i + len(l)])); i += len(l)
    return out

rng = random.Random(SEED)
S_draws = [redeal(W, rng) for _ in range(DRAWS)]
G_draws = [redeal(G, rng) for _ in range(DRAWS)]

def score(c, w):
    v, u = vec_c(c), vec_w(w)
    match = v == u and sum(u) >= 3
    unique = [k for k in codes if vec_c(k) == u]
    ps = sum(vec_c(c) == tuple(x[w] for x in d) for d in S_draws) / DRAWS
    pg = sum(tuple(x[c] for x in d) == u for d in G_draws) / DRAWS
    return dict(c=c, w=w, v=v, u=u, match=match, unique=unique == [c], same_vec=unique, ps=ps, pg=pg,
                recovered=match and unique == [c] and ps <= ALPHA and pg <= ALPHA)

def show(r, tag):
    pp = " ".join(f"{PAIRS[i][0]} {r['v'][i]}/{r['u'][i]}" + (" (0/0 non-discr.)" if r['v'][i] == r['u'][i] == 0 else "")
                  for i in range(4))
    print(f"{tag}\t{r['c']}={r['w']}\tcode {r['v']} word {r['u']}\tMATCH {r['match']}\tUNIQUE {r['unique']} "
          f"(codes with word's vector: {r['same_vec'][:8]})\tp_s {r['ps']:.4f}\tp_g {r['pg']:.4f}\t"
          f"{'RECOVERED' if r['recovered'] else '-'}\tper-pair code/word: {pp}")

print("# sizes groups", [len(g) for g in G], "slip tokens", [len(w) for w in W], f"draws {DRAWS} seed {SEED}")
KNOWN = [("22", "de"), ("279", "plus"), ("581", "au"), ("501", "et"), ("31", "la_reine"), ("628", "hongrie"),
         ("172", "quils"), ("379", "interets"), ("208", "se"), ("781", "e")]
elig = [(c, w) for c, w in KNOWN if sum(vec_w(w)) >= 3]
print("# known-answer eligible (word >= 3 across slips):", elig, "; ineligible:", [k for k in KNOWN if k not in elig])
ka = [score(c, w) for c, w in elig]
for r in ka: show(r, "KNOWN")
licensed = any(r["recovered"] for r in ka)
print(f"# known-answer recovered {sum(r['recovered'] for r in ka)}/{len(ka)} -> licence {'MET' if licensed else 'NOT MET'}")
for c, w in PRIMARY:
    r = score(c, w); show(r, "PRIMARY")
    if not r["match"]: verdict = "FAIL"
    elif r["recovered"] and licensed: verdict = "PASS"
    else: verdict = "NON-INFORMATIVE"
    print(f"VERDICT\t{c}={w}\t{verdict}")
# secondary scan
cand = []
wset = sorted({w for x in wc for w in x if sum(vec_w(w)) >= 3})
for w in wset:
    u = vec_w(w); m = [k for k in codes if vec_c(k) == u]
    if len(m) == 1: cand.append((m[0], w))
print(f"# secondary: {len(wset)} words with >= 3 tokens; {len(cand)} with a unique exact code match; threshold {ALPHA}/{max(len(cand),1)}")
thr = ALPHA / max(len(cand), 1)
for c, w in cand:
    r = score(c, w)
    ok = r["ps"] <= thr and r["pg"] <= thr
    show(r, "SEC-LEAD" if ok else "sec")
