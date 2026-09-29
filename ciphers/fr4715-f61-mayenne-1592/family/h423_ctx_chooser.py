#!/usr/bin/env python3
"""H423/H424 (runner 16, 29 Sept 2026), script-only: a per-cell CONTEXT CHOOSER for two-way cells, known-answer control first.

Instrument (not H33/H57: no model judge, no letter sets wider than the key's cells, no wildcards): each cipher line is cut into
segments (a break at a clear word, a word code, or a sign with no key v8 cell; null signs are dropped, as Tomokiyo drops them);
every cell starts at its letter with the higher fr16 unigram probability; then, sweeping left to right until nothing changes
(iterated conditional modes, at most 50 sweeps), each cell with two or more letters takes the letter that maximises the
fr16 5-gram log-probability (tools/french16_ngram.py, the shared period model: Catherine de Medicis / Marguerite de Valois
letters, 1550s-1600s) of the segment with every other cell held at its current letter. Letters folded j->i, u->v (the model's
own folding). Scored cells: a two-letter cell whose known letter is one of its two letters.

Known-answer leaves (the known letter at a cell never enters the chooser, anywhere):
  f61   f.61's own five Tomokiyo spans (55 letters), span letters HIDDEN, the meter-of-record sequence (h408's meter rows, the
        corrections file applied: L07/4 C43, L03/16 PHI, L04/2 out), the meter's v8 cells; truth by f61crib.align of his markup.
  f108r f.108r L02/L03 (f.61's hand) with Tomokiyo's overlay reprint (84 letters), key v8 (ebr A, as h420), the f.108r
        corrections file applied; truth by the same align.
  f101r fr.3982 f.101r, the period decipherment aligned per sign (passes/f101r_align_v4.tsv, DP-aligned: noisy truth), cells
        from key_v8_cells.tsv (the split class where the blind sort gave one).
  f188r fr.3984 f.188r (Desportes), the same (passes/f188r_align_v4.tsv); an extra other-hand leaf, not named in the brief.
  f.124r is NOT used: its gloss is HELD (two readers agree on 43-49% of words) and its committed alignment's numeric codes do
  not map back onto the committed draft (checked 29 Sept 2026: 45/45 lines differ), so no per-sign known letter can be cited.

Baselines / nulls (gates in HYPOTHESES.md H423, written before the run):
  coin    0.5 per scored cell (exact binomial).
  unigram the chooser's own starting point (the pair's more frequent fr16 letter) -- the chooser must add context over it.
  shuf    the context null that CAN differ: each segment's cells permuted in place (each cell keeps its letters and its known
          letter), chooser rerun; 100 reps (seed 423); p95 of the pooled accuracy.  The brief's 'letter pairs permuted across
          cells' cannot be scored against a known letter (the letter leaves the cell), so the order shuffle stands in for it.
  power   2000 subsamples of 60 scored cells (f.61's two-way count under the corrected meter) from the pooled control (seed 4230):
          share with chooser > unigram (strict) and chooser binomial p < 0.05 vs 0.5.
Target (run only with --target, only after the gate passes): f.61's 60 two-way cells, the letter chosen with the leaf's
per-pair known-answer accuracy beside it, grade M, for a verifier; no key or grade change.
  python3 h423_ctx_chooser.py [--build | --control | --target] [--v12] [--check]"""
import csv, math, os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.abspath(f"{HERE}/.."); ROOT = os.path.abspath(f"{T}/../..")
MODE = next((a for a in sys.argv[1:] if a in ("--build", "--control", "--target")), "--control"); CHECK = "--check" in sys.argv
V12 = "--v12" in sys.argv   # descriptive sensitivity (added after VERIFY-F61-V12 ruled L05/1 = LOOPBAR, a null): f.61's L05/1 dropped as a null
sys.argv = sys.argv[:1]
for p in (HERE, f"{T}/scripts", f"{T}/verify_v9", f"{ROOT}/tools"): sys.path.insert(0, p)
import h408_span_miss_apply as h
import build_key_v8 as b8
from f61crib import align

def fl(c): return {"j": "i", "u": "v"}.get(c.lower(), c.lower())
def cell(letters): return tuple(dict.fromkeys(fl(x) for x in letters))

# ---- f.61: the meter of record's rows, corrections applied (h408.meter's own logic, reproduced to keep rows)
def f61_rows():
    import meter_v9 as m
    d = list(csv.DictReader(open(f"{m.F}/f61_decode_period_v4_frac0.1_sbs.tsv"), delimiter="\t")); k6 = m.bk.load_key_v6(ebr="B", f61=True)
    for r in d:
        if (r["line"], r["pos"]) == ("L07", "4"): r["class"], r["period_letters"] = "C43", "a/n"
    d.append({"line": "L03", "pos": "16", "class": "PHI", "period_letters": "e/r"})
    dels = {(r["line"], r["pos"]) for r in h.corr() if r["action"] == "delete"}
    d = [r for r in d if (r["line"], r["pos"]) not in dels]
    def v8(r):
        c = r["class"]
        if c == "4PI": return "a/n" if r["line"] == "L11" else "-"
        if c in ("VBAR_A", "EBR", "SBS"): return {"VBAR_A": "g/t", "EBR": "l/y", "SBS": "b/o"}[c]
        if c in ("ZHOOK", "HASH4", "4TRI", "4STEM"): return "/".join(k6[c])
        return r["period_letters"]
    d.sort(key=lambda r: (r["line"], int(r["pos"])))
    for r in d:
        r["v8"] = v8(r); r["band"] = m.band(r["v8"], r["class"], False, True)
    return d
def f61_leaf():
    rows = f61_rows(); byl = defaultdict(list)
    for r in rows: byl[r["line"]].append(r)
    spans = defaultdict(list)
    for s, l, mk in h.load_spans(): spans[l].append(mk)
    segs = []
    for L in sorted(byl):
        rr = byl[L]; truth = {}
        ids = [f"{L}_{r['pos']}" for r in rr]; key = {i: cell(r["v8"].split("/")) if r["band"] in ("firm", "two-way", "wider") else () for i, r in zip(ids, rr)}
        for mk in spans.get(L, []):
            mm = "".join(fl(c) if c != "-" else "-" for c in mk)
            _, pairs = align(mm, ids, key)
            for i, j in pairs:
                if mm[i] != "-": truth[j] = mm[i]
        seg = []
        for j, r in enumerate(rr):
            if r["band"] == "null" or (r["band"] == "unread" and r["class"] in ("C6", "CA")) or (V12 and (L, r["pos"]) == ("L05", "1")): continue
            if r["band"] == "unread":
                if seg: segs.append(seg); seg = []
                continue
            seg.append({"c": key[ids[j]], "t": truth.get(j), "id": f"f61 {L}/{r['pos']} {r['class']}", "band": r["band"]})
        if seg: segs.append(seg)
    return segs
def f108r_leaf():
    import h417_column_closure as q
    lines = q.split_lines(q.load_read()); lines.update(q.f108_lines()); q.relabel(lines)
    corr = [r for r in csv.DictReader((l for l in open(f"{T}/scripts/f108r_positions_corrections.tsv") if not l.startswith("#")), delimiter="\t")]
    for r in corr: lines["F108_" + r["line"]][int(r["pos"]) - 1] = r["class"]
    k = b8.load_key_v8(ebr="A"); segs = []
    for s, _, mk, _ in (l.rstrip("\n").split("\t") for l in open(f"{T}/scripts/tomokiyo_spans_3983.tsv") if l[0] == "T"):
        L = "F108_" + ("L02" if s == "T1" else "L03"); seq = lines[L]; kk = {c: cell(v) for c, v in k.items()}
        mm = "".join(fl(c) for c in mk if c != " "); _, pairs = align(mm, seq, kk); truth = {j: mm[i] for i, j in pairs}
        seg = []
        for j, c in enumerate(seq):
            if not kk.get(c):
                if seg: segs.append(seg); seg = []
                continue
            seg.append({"c": kk[c], "t": truth.get(j), "id": f"f108r {L}/{j+1} {c}", "band": "two-way" if len(kk[c]) == 2 else ("firm" if len(kk[c]) == 1 else "wider")})
        if seg: segs.append(seg)
    return segs
def cells_v8():
    return {r["class"]: cell(r["letters"].split("/")) for r in csv.DictReader((l for l in open(f"{HERE}/key_v8_cells.tsv") if not l.startswith("#")), delimiter="\t")}
def align_leaf(name):
    cv = cells_v8(); segs = []; seg = []; cur = None
    for r in csv.DictReader((l for l in open(f"{HERE}/passes/{name}_align_v4.tsv") if not l.startswith("#")), delimiter="\t"):
        if r["cipher_line"] != cur:
            if seg: segs.append(seg)
            seg = []; cur = r["cipher_line"]
        if r["kind"] == "clear":
            if seg: segs.append(seg); seg = []
            continue
        c = r["split_v4"] if r["split_v4"] not in ("=", "unsorted", "") else r["value"]
        pc = r["plain_chunk"]
        if pc == "": continue                     # null-or-unaligned: dropped as a null
        if c not in cv or len(pc) > 1:
            if seg: segs.append(seg); seg = []
            continue
        seg.append({"c": cv[c], "t": fl(pc), "id": f"{name} {cur}/{r['idx']} {c}", "band": "two-way" if len(cv[c]) == 2 else ("firm" if len(cv[c]) == 1 else "wider")})
    if seg: segs.append(seg)
    return segs

# ---- chooser
_M = None
def model():
    global _M
    if _M is None:
        import french16_ngram as f; _M = f.load()
    return _M
_U = {}
def uni(c):
    if c not in _U: _U[c] = model().logp(c.upper())
    return _U[c]
def choose(seg):
    m = model(); cur = [max(x["c"], key=uni) for x in seg]
    for _ in range(50):
        ch = False
        for i, x in enumerate(seg):
            if len(x["c"]) < 2: continue
            a, b_ = max(0, i - 4), min(len(seg), i + 5)
            best = max(x["c"], key=lambda L: m.logp("".join(cur[a:i] + [L] + cur[i + 1:b_]).upper()))
            if best != cur[i]: cur[i] = best; ch = True
        if not ch: break
    return cur
def scored(segs):
    return [(si, i) for si, s in enumerate(segs) for i, x in enumerate(s) if len(x["c"]) == 2 and x["t"] in x["c"]]
def run(segs):
    out = [choose(s) for s in segs]
    return {(si, i): out[si][i] == segs[si][i]["t"] for si, i in scored(segs)}, out
def shuffled(segs, rng):
    return [rng.sample(s, len(s)) for s in segs]

def binom_p(k, n, p=0.5):   # one-sided P(X >= k)
    if k <= 0: return 1.0
    t = [math.lgamma(n + 1) - math.lgamma(j + 1) - math.lgamma(n - j + 1) + j * math.log(p) + (n - j) * math.log(1 - p) for j in range(k, n + 1)]
    mx = max(t); return min(1.0, math.exp(mx) * sum(math.exp(x - mx) for x in t))
LEAVES = {"f61": f61_leaf, "f108r": f108r_leaf, "f101r": lambda: align_leaf("f101r"), "f188r": lambda: align_leaf("f188r")}

def build():
    out = []
    for n, fn in LEAVES.items():
        segs = fn(); sc = scored(segs); bands = Counter(x["band"] for s in segs for x in s)
        pairs = Counter("/".join(segs[si][i]["c"]) for si, i in sc)
        out.append(f"{n}: {len(segs)} segments, {sum(map(len, segs))} cells ({dict(bands)}); scored two-way cells with a known letter {len(sc)}; by pair {dict(pairs.most_common())}")
    return out

def control():
    rng = random.Random(423); res = {}; out = []
    for n, fn in LEAVES.items():
        segs = fn(); ok, cur = run(segs); sc = scored(segs)
        unig = {(si, i): max(segs[si][i]["c"], key=uni) == segs[si][i]["t"] for si, i in sc}
        res[n] = (segs, ok, unig)
    # shuffled-context null: per rep, every leaf's segments permuted, pooled accuracy and per-leaf
    reps = defaultdict(list)
    for r in range(100):
        tot = Counter()
        for n, (segs, ok, unig) in res.items():
            ss = shuffled(segs, rng); o2, _ = run(ss); a = sum(o2.values()); reps[n].append(a / max(1, len(o2)))
            tot["k"] += a; tot["n"] += len(o2)
            if n in ("f61", "f108r"): tot["kh"] += a; tot["nh"] += len(o2)
        reps["pooled"].append(tot["k"] / tot["n"]); reps["hand61"].append(tot["kh"] / tot["nh"])
    def p95(v): return sorted(v)[94]
    groups = {"f61": ["f61"], "f108r": ["f108r"], "f101r": ["f101r"], "f188r": ["f188r"], "hand61": ["f61", "f108r"], "pooled": list(res)}
    summ = {}
    for g, ls in groups.items():
        cc = [(res[l][1][c], res[l][2][c]) for l in ls for c in res[l][1]]; n = len(cc); k = sum(a for a, _ in cc); u = sum(b for _, b in cc)
        b_ = sum(1 for a, bb in cc if a and not bb); c_ = sum(1 for a, bb in cc if bb and not a); mcn = binom_p(b_, b_ + c_) if b_ + c_ else 1.0
        summ[g] = (n, k, u, b_, c_, mcn, p95(reps[g]), sum(reps[g]) / 100)
        out.append(f"{g}: N {n}; chooser {k}/{n} = {k/n:.3f} (binomial vs 0.5 p {binom_p(k, n):.2g}); unigram {u}/{n} = {u/n:.3f}; "
                   f"discordant chooser-only {b_} / unigram-only {c_} (exact McNemar one-sided p {mcn:.3g}); shuffled-context mean {summ[g][7]:.3f} p95 {summ[g][6]:.3f}")
    # per pair breakdown, pooled and hand61
    for g in ("hand61", "pooled"):
        bp = defaultdict(lambda: [0, 0, 0])
        for l in groups[g]:
            segs = res[l][0]
            for c, a in res[l][1].items():
                pr = "/".join(segs[c[0]][c[1]]["c"]); bp[pr][0] += 1; bp[pr][1] += a; bp[pr][2] += res[l][2][c]
        out.append(f"per pair ({g}), N chooser unigram: " + "; ".join(f"{p} {v[0]} {v[1]} {v[2]}" for p, v in sorted(bp.items(), key=lambda kv: -kv[1][0])))
    # power at f.61's N (60)
    pool = [(res[l][1][c], res[l][2][c]) for l in res for c in res[l][1]]; prng = random.Random(4230); hit = 0
    for _ in range(2000):
        s = prng.sample(pool, 60); k = sum(a for a, _ in s); u = sum(b for _, b in s)
        hit += (k > u and binom_p(k, 60) < 0.05)
    power = hit / 2000; out.append(f"power at N 60 (2000 subsamples of the pooled control, seed 4230): share with chooser > unigram and binomial p < 0.05 = {power:.3f}")
    hp = [(res[l][1][c], res[l][2][c]) for l in ("f61", "f108r") for c in res[l][1]]; hrng = random.Random(4231); hh = 0
    for _ in range(2000):
        s = [hrng.choice(hp) for _ in range(60)]; k = sum(a for a, _ in s); u = sum(b for _, b in s); hh += (k > u and binom_p(k, 60) < 0.05)
    out.append(f"DESCRIPTIVE ONLY, written after the gate result, NOT a gate: the same power figure from f.61's own hand alone (f61+f108r, 97 cells, 60 drawn with replacement, seed 4231) = {hh/2000:.3f}")
    P, H = summ["pooled"], summ["hand61"]
    g1 = P[5] < 0.05 and P[1] / P[0] > P[6] and binom_p(P[1], P[0]) < 0.01
    g2 = H[1] >= H[2] and H[1] / H[0] > H[6]
    g3 = power >= 0.80
    out.append(f"GATE (pre-registered, HYPOTHESES.md H423): G1 pooled {'PASS' if g1 else 'FAIL'}; G2 f.61 hand {'PASS' if g2 else 'FAIL'}; G3 power {'PASS' if g3 else 'FAIL'} -> "
               + ("PASS: the chooser may be applied to f.61's two-way cells (H424)" if g1 and g2 and g3 else "FAIL: untested-by-this-tool; f.61 not touched"))
    # per-cell record for the f.61 hand
    for l in ("f61", "f108r"):
        segs, ok, unig = res[l]
        out.append(f"{l} per cell (id known chooser-right unigram-right): " + "; ".join(f"{segs[si][i]['id']} {segs[si][i]['t']} {int(a)} {int(unig[si, i])}" for (si, i), a in sorted(ok.items())))
    return out

def main():
    out = build() if MODE == "--build" else control() if MODE == "--control" else None
    if out is None: sys.exit("--target runs only after the gate passes; not written yet")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h423_ctx_chooser_{MODE[2:]}{'_v12' if V12 else ''}_result.txt"
    if CHECK:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
