#!/usr/bin/env python3
"""F61-BEAM-MARGIN (campaign step H117, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only, no model call.
H116 licensed the 4-gram beam as a two-way grading aid (0.776 right on the known spans under the 14-cell map). Here it is
applied to f.61r under key v4 in VERIFY-F61-V4's two-way form (verify_v4/f61r_v4_twoway.txt: firm letter, [a/b/..] period
set, <CLASS> no period pair), with a margin per position and a held-out calibration. Fixed before the first run:
  segments: each line is cut at <CLASS> tokens (no letter is invented for them); a segment is resolved by the beam
            (scripts/f61hash4_108r.py resolve, generalised to sets of any size; fr16 4-gram, width 400).
  margin:   at a set position, best path score minus the best path with that position forced to any other letter of its set.
  known:    Tomokiyo's letters from the file's T: rows (dash and '.' excluded), at set positions whose set holds the letter.
  calibration, leave one span out (S1, S2, S3, S4a+S4b, S5): tau = the smallest margin at which the four training spans'
            positions with margin >= tau are >= 90% right (at least 5 such positions; else no tau for the fold); the held-out
            span's positions with margin >= tau are scored.
  GATE H117: pooled held-out accuracy of above-tau positions >= 0.85 on >= 8 positions. Only on a PASS: tau from all five
            spans is applied to the set positions outside the spans, and the count that clears it is reported (candidate
            grade S for the verifier to weigh, never a reading).
  -> scripts/f61beam_margin_result.txt, scripts/f61beam_margin_positions.tsv [--check]
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); TGT = os.path.dirname(HERE); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61hash4_108r as H
jp, lp = H.jp, H.lp
def parse():
    lines, known, cur = {}, {}, None
    for raw in open(f"{TGT}/verify_v4/f61r_v4_twoway.txt"):
        t = raw.split()
        if not t or raw.startswith("#"): continue
        if re.fullmatch(r"L\d\d", t[0]):
            cur = t[0]; lines[cur] = [None if x.startswith("<") else tuple(jp.fold(c) for c in x.strip("[]").split("/")) for x in t[1:]]
        elif t[0].startswith("T:") and cur:
            span = t[0][2:]
            for k, c in enumerate(t[1:1 + len(lines[cur])]):
                if c not in "-.": known[(cur, k)] = (span, jp.fold(c))
    return lines, known
def best(sets):
    beam = [("", 0.0)]
    for st in sets:
        nb = {}
        for s, v in beam:
            for ch in st:
                t = s + ch; w = v + (lp(t[-4:]) if len(t) >= 4 else 0.0)
                if t[-3:] not in nb or nb[t[-3:]][1] < w: nb[t[-3:]] = (t, w)
        beam = sorted(nb.values(), key=lambda x: -x[1])[:400]
    return beam[0]
def positions(lines, known):
    out = []
    for L, toks in lines.items():
        segs, cur = [], []
        for k, s in enumerate(toks):
            if s is None:
                if cur: segs.append(cur); cur = []
            else: cur.append(k)
        if cur: segs.append(cur)
        for seg in segs:
            sets = [toks[k] for k in seg]; s, v = best(sets)
            for i, k in enumerate(seg):
                if len(sets[i]) < 2: continue
                alt = max(best(sets[:i] + [tuple(c for c in sets[i] if c != s[i])] + sets[i + 1:])[1], -1e9)
                sp, tr = known.get((L, k), (None, None))
                out.append((L, k + 1, "/".join(sets[i]), s[i], round(v - alt, 4), sp or "", tr if tr and tr in sets[i] else ""))
    return out
FOLDS = [("S1",), ("S2",), ("S3",), ("S4a", "S4b"), ("S5",)]
def tau(pts):
    for t in sorted({p[4] for p in pts}):
        a = [p for p in pts if p[4] >= t]
        if len(a) >= 5 and sum(p[3] == p[6] for p in a) / len(a) >= 0.9: return t
    return None
def main():
    lines, known = parse(); P = positions(lines, known); K = [p for p in P if p[6]]
    out = [f"set positions {len(P)}; with a known letter in the set {len(K)}; overall beam accuracy on them {sum(p[3] == p[6] for p in K)}/{len(K)}"]
    ho_r = ho_n = 0
    for f in FOLDS:
        tr = [p for p in K if p[5] not in f]; te = [p for p in K if p[5] in f]; t = tau(tr)
        if t is None: out.append(f"fold {'+'.join(f)}: no tau on the training spans; held-out {len(te)} not scored"); continue
        a = [p for p in te if p[4] >= t]; r = sum(p[3] == p[6] for p in a); ho_r += r; ho_n += len(a)
        out.append(f"fold {'+'.join(f)}: tau {t:.3f}; held-out above tau {r}/{len(a)} (of {len(te)})")
    ok = ho_n >= 8 and ho_r / ho_n >= 0.85
    out.append(f"GATE H117 (pooled held-out >= 0.85 on >= 8): {ho_r}/{ho_n}" + (f" = {ho_r / ho_n:.3f}" if ho_n else "") + f" -> {'PASS' if ok else 'FAIL'}")
    if ok:
        t = tau(K); U = [p for p in P if not p[5]]; c = [p for p in U if t is not None and p[4] >= t]
        out.append(f"applied tau {t:.3f} (all spans): {len(c)} of {len(U)} set positions outside the spans clear it -- candidate S for the verifier: " + ", ".join(f"{p[0]}/{p[1]} {p[3]}" for p in c))
    txt = "\n".join(out) + "\n"
    tsv = "line\tpos\tset\tbeam\tmargin\tspan\ttrue\n" + "".join("\t".join(map(str, p)) + "\n" for p in P)
    rp, tp = f"{HERE}/f61beam_margin_result.txt", f"{HERE}/f61beam_margin_positions.tsv"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt and open(tp).read() == tsv; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); open(tp, "w").write(tsv); print(txt, end="")
if __name__ == "__main__": main()
