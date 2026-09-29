#!/usr/bin/env python3
"""VERIFY-F61-V12 (29 Sept 2026): f.61 five-span count and meter under key v8, for four transcription states:
(a) uncorrected; (b) runner 15's corrections file as committed (L07/4 C43, L03/16 PHI insert, L04/2 delete);
(c) the corrections this verifier endorses = (b) + L05/1 LOOPSTEM1 -> LOOPBAR (null) [C1 x3 + C2 x1 = 4/4 R9, PREREG rule 3];
(d) (c) + an LL (null) at the start of L02 before PHI [C4, 3/3 R16; a slip the runner did not propose -- shown, not endorsed for merge].
Meter bands: verify_v8/meter_v8.band (C6 or '-' -> unread/null; 1 letter firm; 2 two-way; more wider). Key v8 cells as FAMILY-13 merged them
(the same cell rule as family/h408_span_miss_apply.meter: 4PI a/n on L11 else unread; VBAR_A g/t, EBR l/y, SBS b/o; ZHOOK/HASH4/4TRI/4STEM from
build_key_v6's f.61 key; everything else the period letters column). Spans: h408's own scorer (f61crib.align, 2000 permuted keys, its seed),
fed this verifier's correction lists.  python3 meter_v12.py [--check]"""
import csv, os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.abspath(f"{HERE}/.."); F = f"{T}/family"
CHECK = "--check" in sys.argv; sys.argv = sys.argv[:1]
sys.path.insert(0, f"{T}/verify_v8"); sys.path.insert(0, F)
import meter_v8 as m8
import h408_span_miss_apply as h
RUNNER = [("L07", "4", "relabel", "C43"), ("L03", "16", "insert", "PHI"), ("L04", "2", "delete", "OTHER")]
MINE = RUNNER + [("L05", "1", "relabel", "LOOPBAR")]
MINE_LL = MINE + [("L02", "0", "insert", "LL")]
LET = {"C43": "a/n", "PHI": "e/r", "LOOPBAR": "-", "LL": "-"}
def meter(corr):
    d = list(csv.DictReader(open(f"{F}/f61_decode_period_v4_frac0.1_sbs.tsv"), delimiter="\t")); k6 = h.m.bk.load_key_v6(ebr="B", f61=True)
    for l, p, act, c in corr:
        if act == "relabel":
            r = next(r for r in d if (r["line"], r["pos"]) == (l, p)); r["class"], r["period_letters"] = c, LET[c]
        elif act == "insert": d.append({"line": l, "pos": p, "class": c, "period_letters": LET[c]})
        elif act == "delete": d = [r for r in d if (r["line"], r["pos"]) != (l, p)]
    def v8(r):
        c = r["class"]
        if c == "4PI": return "a/n" if r["line"] == "L11" else "-"
        if c in ("VBAR_A", "EBR", "SBS"): return {"VBAR_A": "g/t", "EBR": "l/y", "SBS": "b/o"}[c]
        if c in ("ZHOOK", "HASH4", "4TRI", "4STEM"): return "/".join(k6[c])
        return r["period_letters"]
    b = Counter(m8.band(v8(r), r["class"]) for r in d); wid = Counter(r["class"] for r in d if m8.band(v8(r), r["class"]) == "wider")
    return f"firm {b['firm']} / two-way {b['two-way']} / wider {b['wider']} / unread-or-null {b['unread/null']} of {len(d)}; wider: {dict(wid)}"
def spans(corr):
    k = h.b8.load_key_v8(f61=True); lines = h.split_lines(h.load_read()); lines.update(h.f108_lines()); h.relabel(lines)
    ll = h.b.f61_relabel({x: list(v) for x, v in lines.items()})
    for l, p, act, c in sorted(corr, key=lambda r: -int(r[1])):
        if l not in ll: continue
        s = ll[l]; i = int(p)
        if act == "relabel": s[i - 1] = c
        elif act == "insert": assert len(s) == i - 1; s.insert(i - 1, c)
    mt, tot, mean, p95, ge = h.spans(k, ll); return f"{mt}/{tot} = {mt/tot:.3f}; 2000 permuted keys mean {mean:.3f} p95 {p95:.3f}; >= key {ge}/2000"
def main():
    out = []
    for tag, corr in (("(a) uncorrected", []), ("(b) runner 15 corrections file", RUNNER), ("(c) V12 endorsed = (b) + L05/1 LOOPBAR", MINE),
                      ("(d) (c) + L02 opening LL (C4, not endorsed for merge)", MINE_LL)):
        out.append(f"{tag}: spans {spans(corr)}; meter {meter(corr)}")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/meter_v12_result.txt"
    if CHECK:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
