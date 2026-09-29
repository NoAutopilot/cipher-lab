#!/usr/bin/env python3
"""H408 (runner 15 session_01BDhspZ38TdrrXYSvLPTpjc, 29 Sept 2026), script-only: apply scripts/f61_positions_corrections.tsv (H407) to f.61's
reader sequence and rerun (a) the five-span reproduction under key v8's f.61 reading key with build_key_v7's own scorer and 2000 permuted keys
(seed 20260929), and (b) the meter bands (verify_v11/meter_v11 baseline, f.61 4TRI bowl), each beside the uncorrected figure.  [--check]"""
import csv, os, random, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.abspath(f"{HERE}/.."); sys.path.insert(0, HERE); sys.path.insert(0, f"{T}/scripts"); sys.path.insert(0, f"{T}/verify_v9")
CHECK = "--check" in sys.argv; sys.argv = sys.argv[:1]
import build_key_v7 as b, build_key_v8 as b8, meter_v9 as m
from f61crib import align, load_read, load_spans
from f61crib4 import split_lines
from f61joint import f108_lines
from sbs_relabel import relabel
def corr():
    return [r for r in csv.DictReader((l for l in open(f"{T}/scripts/f61_positions_corrections.tsv") if not l.startswith("#")), delimiter="\t")]
def apply_seq(lines):
    for r in sorted(corr(), key=lambda r: -int(r["pos"])):
        s = lines[r["line"]]; p = int(r["pos"])
        if r["action"] == "relabel": s[p - 1] = r["class"]
        elif r["action"] == "insert": assert len(s) == p - 1, (r, len(s)); s.insert(p - 1, r["class"])
    return lines
def spans(k, l61):
    s61 = load_spans(); mt = tot = 0
    for s, l, mk in s61:
        mm = mk.translate(b.FOLD); mt += align(mm, l61[l], k)[0]; tot += sum(1 for c in mm if c != "-")
    labs = sorted(k); vals = [k[x] for x in labs]; rng = random.Random(20260929); cs = []
    for _ in range(2000):
        v = list(vals); rng.shuffle(v); kk = dict(zip(labs, v)); x = 0
        for s, l, mk in s61: x += align(mk.translate(b.FOLD), l61[l], kk)[0]
        cs.append(x)
    cs.sort(); return mt, tot, sum(cs) / 2000 / tot, cs[1899] / tot, sum(x >= mt for x in cs)
def meter(corrected):
    d = list(csv.DictReader(open(f"{m.F}/f61_decode_period_v4_frac0.1_sbs.tsv"), delimiter="\t")); k6 = m.bk.load_key_v6(ebr="B", f61=True)
    if corrected:
        for r in d:
            if (r["line"], r["pos"]) == ("L07", "4"): r["class"], r["period_letters"] = "C43", "a/n"
        d.append({"line": "L03", "pos": "16", "class": "PHI", "period_letters": "e/r"})
    def v8(r):
        c = r["class"]
        if c == "4PI": return "a/n" if r["line"] == "L11" else "-"
        if c in ("VBAR_A", "EBR", "SBS"): return {"VBAR_A": "g/t", "EBR": "l/y", "SBS": "b/o"}[c]
        if c in ("ZHOOK", "HASH4", "4TRI", "4STEM"): return "/".join(k6[c])
        return r["period_letters"]
    c = Counter(m.band(v8(r), r["class"], False, True) for r in d); return c["firm"], c["two-way"], c["wider"], c["null"] + c["unread"], len(d)
def main():
    k = b8.load_key_v8(f61=True); lines = split_lines(load_read()); lines.update(f108_lines()); relabel(lines)
    l0 = b.f61_relabel({x: list(v) for x, v in lines.items()}); l1 = apply_seq({x: list(v) for x, v in l0.items()})
    out = []
    for tag, ll in (("uncorrected", l0), ("with H407's two corrections", l1)):
        mt, tot, mean, p95, ge = spans(k, ll); out.append(f"f.61 five spans, key v8 f.61 reading key, {tag}: {mt}/{tot} = {mt/tot:.3f}; 2000 permuted keys mean {mean:.3f} p95 {p95:.3f}; >= key {ge}/2000")
    for tag, cflag in (("uncorrected", False), ("with H407's two corrections", True)):
        f, t, w, u, n = meter(cflag); out.append(f"meter, key v8 as merged, {tag}: firm {f} / two-way {t} / wider {w} / unread-or-null {u} of {n}")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h408_span_miss_apply_result.txt"
    if CHECK:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
