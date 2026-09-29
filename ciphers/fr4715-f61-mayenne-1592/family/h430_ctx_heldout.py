#!/usr/bin/env python3
"""H430 (runner 16 session_01Vtwc6CEJD2BSnYdzzY4f8W, 29 Sept 2026): the held-out scorer for H423's context chooser, written and pushed BEFORE any
person's gloss exists, so nothing here can be fitted to the answer. H423 failed its power gate on the pooled control (0.763 < 0.80); the only
licence left for choosing f.61's two-way letters (H424) is known letters in f.61's hand that the chooser has never seen. This scores them.

Source implemented: ASKS 88, f.108r L04-L06 (f.61's hand), the person's file scripts/gloss108_person.tsv in H137's format (line, word, first_sign,
last_sign, note; pass A positions of scripts/pass108gA_classes.tsv), placed on the H108 draft exactly as scripts/f61score_gloss108.py places it
(its a_to_draft and draft_classes, imported) but aligned with key v8's cells (build_key_v8.load_key_v8(ebr="A"), the H423 f.108r key).
ASKS 93 (f.211r) and ASKS 99 (f.106r): adapters not written (their desk-pack formats are not fixed yet); they would feed the same score().

Chooser: h423_ctx_chooser.choose, UNCHANGED (fr16 5-gram, ICM from the unigram start); segments = the draft lines cut at any sign with no v8 cell.
Scored cells: a two-letter cell whose gloss letter is one of its two letters. Baselines: the unigram start; the order shuffle (100 reps, seed 430).
GATE (fixed here, before any gloss): PASS iff (1) chooser > unigram with exact McNemar one-sided p < 0.05 on these new cells alone, (2) chooser
accuracy > the order-shuffle p95, (3) no pair with >= 5 new cells where the chooser is below the unigram rule (H427's per-pair lesson).
A PASS licenses H424 for a verifier's decision; a FAIL retires the chooser for f.61 (rule 3: 'untested-by-this-tool', not refuted).
  python3 h430_ctx_heldout.py              -> "waiting" (exit 0) while scripts/gloss108_person.tsv is absent; else h430_ctx_heldout_result.txt
  python3 h430_ctx_heldout.py --selftest   -> a synthetic gloss built from the chooser's own letters must score the chooser 1.000 on > 20 cells
  python3 h430_ctx_heldout.py --check"""
import math, os, random, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.abspath(f"{HERE}/.."); ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
sys.path.insert(0, HERE); sys.path.insert(0, f"{T}/scripts")
import h423_ctx_chooser as c
import build_key_v8 as b8
import f61score_gloss108 as g8
from f61crib import align
GLOSS = f"{T}/scripts/gloss108_person.tsv"
def segments():
    kk = {x: c.cell(v) for x, v in b8.load_key_v8(ebr="A").items()}; D = g8.draft_classes(); segs = []
    for L in ("L04", "L05", "L06"):
        seg = []
        for p in sorted(D[L]):
            cl = D[L][p]
            if not kk.get(cl):
                if seg: segs.append(seg); seg = []
                continue
            seg.append({"c": kk[cl], "t": None, "id": f"f108r {L}/{p} {cl}", "L": L, "p": p, "cls": cl})
        if seg: segs.append(seg)
    return segs, kk
def place(gloss_rows, segs, kk):
    """gloss letters onto the segment cells (H137's placement, v8 cells); returns the number of words placed."""
    m = g8.a_to_draft(); at = {(x["L"], x["p"]): x for s in segs for x in s}; words = 0
    for g in gloss_rows:
        w = "".join(c.fl(ch) for ch in g["word"].strip() if ch.isalpha())
        if not w or g["word"].strip().startswith("?") or g["word"].strip() == "-": continue
        L = g["line"].strip(); dps = sorted({m.get((L, a)) for a in range(int(g["first_sign"]), int(g["last_sign"]) + 1)} - {None})
        dps = [p for p in dps if (L, p) in at]
        if not dps: continue
        words += 1; seq = [at[(L, p)]["cls"] for p in dps]
        for i, j in align(w, seq, kk)[1]:
            at[(L, dps[j])]["t"] = w[i]
    return words
def binom_p(k, n): return c.binom_p(k, n)
def score(gloss_rows, rng_seed=430):
    segs, kk = segments(); words = place(gloss_rows, segs, kk); ok, _ = c.run(segs); sc = c.scored(segs)
    uni = {(si, i): max(segs[si][i]["c"], key=c.uni) == segs[si][i]["t"] for si, i in sc}
    n = len(sc); k = sum(ok.values()); u = sum(uni.values())
    b_ = sum(1 for x in sc if ok[x] and not uni[x]); c_ = sum(1 for x in sc if uni[x] and not ok[x]); mcn = binom_p(b_, b_ + c_) if b_ + c_ else 1.0
    rng = random.Random(rng_seed); reps = []
    for _ in range(100):
        o2, _ = c.run(c.shuffled(segs, rng)); reps.append(sum(o2.values()) / max(1, len(o2)))
    p95 = sorted(reps)[94]; bp = defaultdict(lambda: [0, 0, 0])
    for (si, i) in sc:
        pr = "/".join(segs[si][i]["c"]); bp[pr][0] += 1; bp[pr][1] += ok[si, i]; bp[pr][2] += uni[si, i]
    below = [p for p, v in bp.items() if v[0] >= 5 and v[1] < v[2]]
    out = [f"gloss words placed {words}; scored two-way cells {n}",
           f"chooser {k}/{n}" + (f" = {k/n:.3f}" if n else "") + f"; unigram {u}/{n}" + (f" = {u/n:.3f}" if n else "") +
           f"; discordant {b_}/{c_} (McNemar one-sided p {mcn:.3g}); order shuffle mean {sum(reps)/100:.3f} p95 {p95:.3f}",
           "per pair (N chooser unigram): " + "; ".join(f"{p} {v[0]} {v[1]} {v[2]}" for p, v in sorted(bp.items(), key=lambda kv: -kv[1][0]))]
    g1 = n > 0 and k > u and mcn < 0.05; g2 = n > 0 and k / n > p95; g3 = not below
    out.append(f"GATE (pre-registered H430): (1) {'PASS' if g1 else 'FAIL'} (2) {'PASS' if g2 else 'FAIL'} (3) {'PASS' if g3 else 'FAIL: ' + ', '.join(below)} -> "
               + ("PASS: H424 may go to a verifier's decision" if g1 and g2 and g3 else "FAIL: the chooser is retired for f.61 (untested-by-this-tool)"))
    return "\n".join(out) + "\n", ok, segs
def selftest():
    segs, kk = segments(); _, cur = c.run(segs); m = g8.a_to_draft(); inv = {}
    for (L, a), dp in m.items():
        if dp: inv.setdefault((L, dp), a)
    rows = []
    for si, s in enumerate(segs):
        for k0 in range(0, len(s) - 3, 4):
            ch = [(x, cur[si][k0 + j]) for j, x in enumerate(s[k0:k0 + 4]) if (x["L"], x["p"]) in inv]
            if len(ch) < 2 or len({x["L"] for x, _ in ch}) > 1: continue
            rows.append({"line": ch[0][0]["L"], "word": "".join(l for _, l in ch), "first_sign": str(inv[(ch[0][0]["L"], ch[0][0]["p"])]),
                         "last_sign": str(inv[(ch[-1][0]["L"], ch[-1][0]["p"])])})
    txt, ok, _ = score(rows); n = len(ok); k = sum(ok.values())
    print(txt, end=""); good = n > 20 and k == n; print("SELFTEST", "PASS" if good else "FAIL", f"({k}/{n})"); sys.exit(0 if good else 1)
def main():
    if "--selftest" in ARGS: selftest()
    if not os.path.exists(GLOSS): print("waiting: scripts/gloss108_person.tsv not present (ASKS 88)"); sys.exit(0)
    txt, _, _ = score(g8.rows(GLOSS)); p = f"{HERE}/h430_ctx_heldout_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if good else "STALE"); sys.exit(0 if good else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
