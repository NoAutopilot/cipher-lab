#!/usr/bin/env python3
"""H430 (runner 16 session_01Vtwc6CEJD2BSnYdzzY4f8W, 29 Sept 2026): the held-out scorer for H423's context chooser, written and pushed BEFORE any
person's gloss exists, so nothing here can be fitted to the answer. H423 failed its power gate on the pooled control (0.763 < 0.80); the only
licence left for choosing f.61's two-way letters (H424) is known letters in f.61's hand that the chooser has never seen. This scores them.

Source implemented: ASKS 88, f.108r L04-L06 (f.61's hand), the person's file scripts/gloss108_person.tsv in H137's format (line, word, first_sign,
last_sign, note; pass A positions of scripts/pass108gA_classes.tsv), placed on the H108 draft exactly as scripts/f61score_gloss108.py places it
(its a_to_draft and draft_classes, imported) but aligned with key v8's cells (build_key_v8.load_key_v8(ebr="A"), the H423 f.108r key).
H433 (same session, 20:4x UTC, still before any gloss exists) adds two sources in their desk packs' fixed formats:
  ASKS 89, f.108v L01-L07 (f.61's hand): scripts/gloss108v_person.tsv (line, word, first_sign, last_sign, note; pass A numbering of
          family/passes/f108v3z_signsA.tsv, PLAIN rows counted), words placed straight onto those pass A positions (PLAIN rows break segments);
  ASKS 93, f.211r L02 (Mayenne's secretary): scripts/gloss211r_person.tsv (kind, text, from_tick, to_tick, note), gloss rows placed on the signs
          of family/passes/f211r_rec/ciphertext_h322.tsv whose tick (images/person_pack_211r/README.md table) lies in [from_tick - 0.5, to_tick + 0.5].
  ASKS 99 (f.106r) asks for hash shapes, not letters: no adapter.
  The gate below is applied to the POOL of new cells from every source whose file exists; per-source figures are reported beside it.
  Transcription filter (H433, pre-registered before any gloss): on f.108r and f.108v a cell is scored only where both sign passes read the same
  class (the drafts' why = agree / agree-flagged: scripts/f61recon108r_draft.tsv, family/passes/f108v3z_draft_full.tsv mapped to pass A order);
  f.61's own transcription is QA'd (26/27 out-of-span codes confirmed, spans 55/55), so an unfiltered f.108v (about half the columns differ
  between passes) would not be a matched test. Unfiltered cells still give context. f.211r (16/18 agreed) is not filtered.

Chooser: h423_ctx_chooser.choose, UNCHANGED (fr16 5-gram, ICM from the unigram start); segments = the draft lines cut at any sign with no v8 cell.
Scored cells: a two-letter cell whose gloss letter is one of its two letters. Baselines: the unigram start; the order shuffle (100 reps, seed 430).
GATE (fixed here, before any gloss): PASS iff (1) chooser > unigram with exact McNemar one-sided p < 0.05 on these new cells alone, (2) chooser
accuracy > the order-shuffle p95, (3) no pair with >= 5 new cells where the chooser is below the unigram rule (H427's per-pair lesson).
A PASS licenses H424 for a verifier's decision. A FAIL retires the chooser for f.61 (rule 3: 'untested-by-this-tool', not refuted) ONLY where the
power of criterion (1) at the pooled N (H434's simulation on f.61's own hand, run here) is >= 0.80; below that a FAIL reads 'untestable at this N
-- keep waiting for more glosses' (H434, written before any gloss: f.108r alone 0.46, f.108v alone 0.66, all three 0.88 at full coverage).
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
GLOSS_V = f"{T}/scripts/gloss108v_person.tsv"; GLOSS_211 = f"{T}/scripts/gloss211r_person.tsv"
AGREE = ("agree", "agree-flagged")
def ab_108r():
    R = g8.rows(f"{T}/scripts/f61recon108r_draft.tsv"); D = g8.draft_classes(); out = {}
    for L in ("L04", "L05", "L06"):
        rr = [r for r in R if r["line"] == L and r["sign"] != "none"]; assert len(rr) == len(D[L]), (L, len(rr), len(D[L]))
        for k, r in enumerate(rr, 1): out[(L, k)] = r["why"] in AGREE
    return out
def ab_108v():
    out = {}; pos = {}
    for r in g8.rows(f"{HERE}/passes/f108v3z_draft_full.tsv"):
        if r["why"] == "gap" and r["alt"].startswith("A:"): continue   # a B-only column: no pass A sign
        pos[r["line"]] = pos.get(r["line"], 0) + 1; out[(r["line"], pos[r["line"]])] = r["why"] in AGREE
    return out
def segments():
    global AB108R
    AB108R = ab_108r()
    kk = {x: c.cell(v) for x, v in b8.load_key_v8(ebr="A").items()}; D = g8.draft_classes(); segs = []
    for L in ("L04", "L05", "L06"):
        seg = []
        for p in sorted(D[L]):
            cl = D[L][p]
            if not kk.get(cl):
                if seg: segs.append(seg); seg = []
                continue
            seg.append({"c": kk[cl], "t": None, "id": f"f108r {L}/{p} {cl}", "L": L, "p": p, "cls": cl, "ab": AB108R.get((L, p), False)})
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
    for x in at.values():
        if not x.get("ab", True): x["t"] = None   # H433 transcription filter
    return words
def segments_108v():
    ab = ab_108v(); kk = {x: c.cell(v) for x, v in b8.load_key_v8(ebr="A").items()}; segs = []; seg = []; cur = None
    for r in g8.rows(f"{HERE}/passes/f108v3z_signsA.tsv"):
        if r["line"] != cur:
            if seg: segs.append(seg)
            seg = []; cur = r["line"]
        if not kk.get(r["sign"]):
            if seg: segs.append(seg); seg = []
            continue
        seg.append({"c": kk[r["sign"]], "t": None, "id": f"f108v {r['line']}/{r['pos']} {r['sign']}", "L": r["line"], "p": int(r["pos"]), "cls": r["sign"], "ab": ab[(r["line"], int(r["pos"]))]})
    if seg: segs.append(seg)
    return segs, kk
def place_108v(gloss_rows, segs, kk):
    at = {(x["L"], x["p"]): x for s in segs for x in s}; words = 0
    for g in gloss_rows:
        w = "".join(c.fl(ch) for ch in g["word"].strip() if ch.isalpha())
        if not w or g["word"].strip().startswith("?") or g["word"].strip() == "-": continue
        L = g["line"].strip(); ps = [p for p in range(int(g["first_sign"]), int(g["last_sign"]) + 1) if (L, p) in at]
        if not ps: continue
        words += 1
        for i, j in align(w, [at[(L, p)]["cls"] for p in ps], kk)[1]: at[(L, ps[j])]["t"] = w[i]
    for x in at.values():
        if not x["ab"]: x["t"] = None   # H433 transcription filter
    return words
def ticks_211r():
    out = {}
    for l in open(f"{T}/images/person_pack_211r/README.md"):
        f = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(f) == 3 and f[0].isdigit(): out[int(f[0])] = float(f[1])
    return out
def segments_211r():
    kk = {x: c.cell(v) for x, v in b8.load_key_v8(ebr="A").items()}; tk = ticks_211r(); segs = []; seg = []
    for r in g8.rows(f"{HERE}/passes/f211r_rec/ciphertext_h322.tsv"):
        p = int(r["position"]); cl = r["sign"]
        if not kk.get(cl):
            if seg: segs.append(seg); seg = []
            continue
        seg.append({"c": kk[cl], "t": None, "id": f"f211r {r['line']}/{p} {cl}", "L": r["line"], "p": p, "cls": cl, "tick": tk.get(p)})
    if seg: segs.append(seg)
    return segs, kk
def place_211r(gloss_rows, segs, kk):
    cells = sorted((x for s in segs for x in s if x["tick"] is not None), key=lambda x: x["tick"]); words = 0
    for g in gloss_rows:
        if g["kind"].strip() != "gloss": continue
        w = "".join(c.fl(ch) for ch in g["text"].strip() if ch.isalpha())
        if not w or g["text"].strip().startswith("?"): continue
        lo, hi = float(g["from_tick"]) - 0.5, float(g["to_tick"]) + 0.5; xs = [x for x in cells if lo <= x["tick"] <= hi]
        if not xs: continue
        words += 1
        for i, j in align(w, [x["cls"] for x in xs], kk)[1]: xs[j]["t"] = w[i]
    return words
SOURCES = {"f108r (ASKS 88)": (GLOSS, lambda: segments(), place), "f108v (ASKS 89)": (GLOSS_V, segments_108v, place_108v),
           "f211r (ASKS 93)": (GLOSS_211, segments_211r, place_211r)}
def binom_p(k, n): return c.binom_p(k, n)
_POP = None
def power_at(N, draws=2000):
    global _POP
    if _POP is None:
        _POP = []
        for nm in ("f61", "f108r"):
            sg = c.LEAVES[nm](); ok, _ = c.run(sg)
            for (si, i), a in ok.items(): _POP.append((a, max(sg[si][i]["c"], key=c.uni) == sg[si][i]["t"]))
    rng = random.Random(434); hit = 0
    for _ in range(draws):
        smp = [rng.choice(_POP) for _ in range(N)]; k = sum(a for a, _ in smp); u = sum(b for _, b in smp)
        b_ = sum(1 for a, b in smp if a and not b); cc = sum(1 for a, b in smp if b and not a); hit += (k > u and b_ + cc > 0 and binom_p(b_, b_ + cc) < 0.05)
    return hit / draws
def score_sources(placed, rng_seed=430):
    """placed: [(name, segs, words)] with known letters set; the gate on the pool, per-source figures beside it."""
    rng = random.Random(rng_seed); out = []; pool = []; bp = defaultdict(lambda: [0, 0, 0]); allok = {}; reps = [0.0] * 100; repn = [0] * 100
    for name, segs, words in placed:
        ok, _ = c.run(segs); sc = c.scored(segs); uni = {x: max(segs[x[0]][x[1]]["c"], key=c.uni) == segs[x[0]][x[1]]["t"] for x in sc}
        n = len(sc); k = sum(ok.values()); u = sum(uni.values())
        out.append(f"{name}: gloss words placed {words}; scored two-way cells {n}; chooser {k}/{n}" + (f" = {k/n:.3f}" if n else "") + f"; unigram {u}/{n}" + (f" = {u/n:.3f}" if n else ""))
        for x in sc:
            pool.append((ok[x], uni[x])); pr = "/".join(segs[x[0]][x[1]]["c"]); bp[pr][0] += 1; bp[pr][1] += ok[x]; bp[pr][2] += uni[x]; allok[(name, x)] = ok[x]
        for r in range(100):
            o2, _ = c.run(c.shuffled(segs, rng)); reps[r] += sum(o2.values()); repn[r] += len(o2)
    n = len(pool); k = sum(a for a, _ in pool); u = sum(b for _, b in pool)
    b_ = sum(1 for a, b in pool if a and not b); c_ = sum(1 for a, b in pool if b and not a); mcn = binom_p(b_, b_ + c_) if b_ + c_ else 1.0
    rr = sorted(reps[r] / repn[r] for r in range(100) if repn[r]); p95 = rr[94] if len(rr) == 100 else 1.0; mean = sum(rr) / len(rr) if rr else 0.0
    below = [p for p, v in bp.items() if v[0] >= 5 and v[1] < v[2]]
    out += [f"POOL: scored two-way cells {n}; chooser {k}/{n}" + (f" = {k/n:.3f}" if n else "") + f"; unigram {u}/{n}" + (f" = {u/n:.3f}" if n else "") +
            f"; discordant {b_}/{c_} (McNemar one-sided p {mcn:.3g}); order shuffle mean {mean:.3f} p95 {p95:.3f}",
            "per pair (N chooser unigram): " + "; ".join(f"{p} {v[0]} {v[1]} {v[2]}" for p, v in sorted(bp.items(), key=lambda kv: -kv[1][0]))]
    g1 = n > 0 and k > u and mcn < 0.05; g2 = n > 0 and k / n > p95; g3 = not below
    pw = power_at(n) if n else 0.0
    out.append(f"power of criterion (1) at N {n} (H434 simulation, f.61's hand, seed 434): {pw:.3f}")
    out.append(f"GATE (pre-registered H430/H433/H434, on the pool): (1) {'PASS' if g1 else 'FAIL'} (2) {'PASS' if g2 else 'FAIL'} (3) {'PASS' if g3 else 'FAIL: ' + ', '.join(below)} -> "
               + ("PASS: H424 may go to a verifier's decision" if g1 and g2 and g3 else
                  ("FAIL: the chooser is retired for f.61 (untested-by-this-tool)" if pw >= 0.80 else "FAIL at power < 0.80: untestable at this N -- keep waiting for more glosses")))
    return "\n".join(out) + "\n", allok
def score(gloss_rows, rng_seed=430):
    segs, kk = segments(); words = place(gloss_rows, segs, kk); txt, ok = score_sources([("f108r (ASKS 88)", segs, words)], rng_seed)
    return txt, {x: v for (_, x), v in ok.items()}, segs
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
    print(txt, end=""); good = n > 20 and k == n; print("SELFTEST f108r", "PASS" if good else "FAIL", f"({k}/{n})")
    # H433 adapters: synthetic glosses from the chooser's own letters, in each pack's format
    sv, kv = segments_108v(); _, cv = c.run(sv); gv = []
    for si, sg in enumerate(sv):
        for k0 in range(0, len(sg) - 3, 4):
            ch = sg[k0:k0 + 4]
            if len({x["L"] for x in ch}) == 1: gv.append({"line": ch[0]["L"], "word": "".join(cv[si][k0:k0 + 4]), "first_sign": str(ch[0]["p"]), "last_sign": str(ch[-1]["p"])})
    wv = place_108v(gv, sv, kv); s2, kk2 = segments_211r(); _, c2 = c.run(s2); g2 = []
    for si, sg in enumerate(s2):
        for k0 in range(0, len(sg), 2):
            ch = [x for x in sg[k0:k0 + 2] if x["tick"] is not None]
            if ch: g2.append({"kind": "gloss", "text": "".join(c2[si][k0 + j] for j, x in enumerate(sg[k0:k0 + 2]) if x["tick"] is not None), "from_tick": str(ch[0]["tick"]), "to_tick": str(ch[-1]["tick"])})
    w2 = place_211r(g2, s2, kk2); t2, ok2 = score_sources([("f108v (ASKS 89)", sv, wv), ("f211r (ASKS 93)", s2, w2)])
    print(t2, end=""); nv = sum(1 for (nm, _) in ok2 if nm.startswith("f108v")); n2 = sum(1 for (nm, _) in ok2 if nm.startswith("f211r"))
    good2 = nv > 50 and n2 >= 3 and all(ok2.values()); print("SELFTEST f108v+f211r", "PASS" if good2 else "FAIL", f"({sum(ok2.values())}/{len(ok2)}; f108v {nv}, f211r {n2})")
    sys.exit(0 if good and good2 else 1)
def main():
    if "--selftest" in ARGS: selftest()
    placed = []
    for name, (path, seg_f, place_f) in SOURCES.items():
        if os.path.exists(path):
            segs, kk = seg_f(); placed.append((name, segs, place_f(g8.rows(path), segs, kk)))
    if not placed: print("waiting: no person's gloss file present (ASKS 88 scripts/gloss108_person.tsv, ASKS 89 scripts/gloss108v_person.tsv, ASKS 93 scripts/gloss211r_person.tsv)"); sys.exit(0)
    txt, _ = score_sources(placed); p = f"{HERE}/h430_ctx_heldout_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if good else "STALE"); sys.exit(0 if good else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
