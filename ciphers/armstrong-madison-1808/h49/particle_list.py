#!/usr/bin/env python3
"""H49: do the target and the Madrid legation cipher share a particle list? Spearman rank correlation between the
target's counts of each value 1-99 (ciphertext.txt) and a reference stream's counts of the same values, over all 99
values; null = the reference's 99 counts permuted over the values (5,000 draws), one-sided p for rho >= observed.
Reference streams: the legation usage (h32/legation_groups.tsv + h42/reads/f373L.tsv + h47/reads/*, the latter with
h47's duplicate-band guard) and, as a negative reference, WE028 usage (h29/erving_groups.tsv, Erving to Monroe 1806).
Positive control (power at the target's own N): 369-group samples drawn from the legation stream itself, scored
against the rest of the stream (50 draws) -- a text in the same code must clear the null.
usage: python3 h49/particle_list.py"""
import csv, difflib, os, random, re
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
def groups_h47():
    out = []
    for fr in ["f284L", "f284R", "f285L", "f285R", "f286L", "f286R"]:
        crops = {}
        for r in csv.DictReader(open(os.path.join(T, "h47", "reads", fr + ".tsv")), delimiter="\t"):
            g = re.sub(r"\D", "", r.get("group") or "")
            if g: crops.setdefault(int(re.sub(r"\D", "", r["crop"]) or 0), []).append(g)
        prev = None
        for c in sorted(crops):
            if prev and len(crops[c]) >= 2 and difflib.SequenceMatcher(None, crops[c], prev).ratio() >= 0.6: continue
            out += crops[c]; prev = crops[c]
    return out
leg = [re.sub(r"\D", "", r["group"]) for r in csv.DictReader(open(os.path.join(T, "h32", "legation_groups.tsv")), delimiter="\t")]
leg += [re.sub(r"\D", "", r["group"]) for r in csv.DictReader(open(os.path.join(T, "h42", "reads", "f373L.tsv")), delimiter="\t")]
leg += groups_h47(); leg = [int(g) for g in leg if g]
we = [int(re.sub(r"\D", "", r["group"])) for r in csv.DictReader(open(os.path.join(T, "h29", "erving_groups.tsv")), delimiter="\t") if re.sub(r"\D", "", r["group"] or "")]
tgt = [int(x) for x in re.findall(r"\b\d{1,4}\b", "".join(l for l in open(os.path.join(T, "ciphertext.txt")) if not l.startswith("#")))]
V = range(1, 100)
def ranks(x):
    o = sorted(range(len(x)), key=lambda i: x[i]); r = [0.0] * len(x); i = 0
    while i < len(o):
        j = i
        while j + 1 < len(o) and x[o[j + 1]] == x[o[i]]: j += 1
        for k in range(i, j + 1): r[o[k]] = (i + j) / 2
        i = j + 1
    return r
def rho(a, b):
    ra, rb = ranks(a), ranks(b); n = len(a); ma = sum(ra) / n; mb = sum(rb) / n
    num = sum((x - ma) * (y - mb) for x, y in zip(ra, rb)); da = sum((x - ma) ** 2 for x in ra) ** .5; db = sum((y - mb) ** 2 for y in rb) ** .5
    return num / (da * db) if da and db else 0.0
def vec(stream): c = Counter(stream); return [c[v] for v in V]
def test(name, a, b, draws=5000, seed=49):
    va, vb = vec(a), vec(b); r = rho(va, vb); rnd = random.Random(seed); null = []
    for _ in range(draws):
        s = vb[:]; rnd.shuffle(s); null.append(rho(va, s))
    null.sort(); p = sum(n >= r for n in null) / draws
    print(f"{name}\tlow-value tokens {sum(va)} vs {sum(vb)}\tdistinct {sum(1 for x in va if x)} vs {sum(1 for x in vb if x)}\trho {r:+.3f}\tnull p95 {null[int(.95*draws)]:+.3f}\tp {p:.4f}")
    return r, null[int(.95 * draws)]
print(f"streams: target {len(tgt)} groups, legation {len(leg)}, WE028 Erving-Monroe {len(we)}")
test("target vs legation", tgt, leg)
test("target vs WE028 usage (negative reference)", tgt, we)
rnd = random.Random(5); passed = 0; rs = []
for _ in range(50):
    i = rnd.randrange(0, len(leg) - 369); samp = leg[i:i + 369]; rest = leg[:i] + leg[i + 369:]
    va, vb = vec(samp), vec(rest); r = rho(va, vb); null = []
    for _ in range(400):
        s = vb[:]; rnd.shuffle(s); null.append(rho(va, s))
    null.sort(); rs.append(r); passed += r > null[int(.95 * 400)]
print(f"control: 369-group windows of the legation stream vs the rest: rho mean {sum(rs)/len(rs):+.3f}, clear their null p95 in {passed}/50")
