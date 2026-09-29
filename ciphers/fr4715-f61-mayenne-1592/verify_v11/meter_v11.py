#!/usr/bin/env python3
"""VERIFY-F61-V11 (29 Sept 2026): f.61r meter (bands as verify_v8/meter_v8.py, null/unread split as verify_v9/meter_v9.py) for the 4TRI bowl split.
Baseline = meter_v9's 'baseline + CA as null' (key v7 as merged + V8 4PI split + V9 CA null). f.61's 6 4TRI tokens (f61 reading cell c/p, as meter_v9)
under the split: (a) bowl not read on f.61 -> each token is either sign: union a/c/n/p; (b) all read bowl -> c/p; (c) all read no-bowl -> a/n.
python3 meter_v11.py [--check]"""
import csv, os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, f"{HERE}/../verify_v9"); import meter_v9 as m
def main():
    d = list(csv.DictReader(open(f"{m.F}/f61_decode_period_v4_frac0.1_sbs.tsv"), delimiter="\t")); k6 = m.bk.load_key_v6(ebr="B", f61=True)
    def v8(r):
        c = r["class"]
        if c == "4PI": return "a/n" if r["line"] == "L11" else "-"
        if c in ("VBAR_A", "EBR", "SBS"): return {"VBAR_A": "g/t", "EBR": "l/y", "SBS": "b/o"}[c]
        if c in ("ZHOOK", "HASH4", "4TRI", "4STEM"): return "/".join(k6[c])
        return r["period_letters"]
    out = [f"meter_v11: f.61r {len(d)} signs, 4TRI tokens {sum(r['class'] == '4TRI' for r in d)} ({' '.join(r['line'] + ':' + r.get('pos', '') for r in d if r['class'] == '4TRI')}); "
           "bands firm / two-way / wider / unread-or-null [null + unread]"]
    for tag, f in (("baseline (v7 as merged + V8 4PI + V9 CA null), no split", v8),
                   ("split, f.61 4TRI bowl not read (each a/c/n/p)", lambda r: "a/c/n/p" if r["class"] == "4TRI" else v8(r)),
                   ("split, f.61 4TRI all bowl (c/p)", lambda r: "c/p" if r["class"] == "4TRI" else v8(r)),
                   ("split, f.61 4TRI all no-bowl (a/n)", lambda r: "a/n" if r["class"] == "4TRI" else v8(r)),
                   ("split, f.61 4TRI as runner 14's H367 read them (L05 14 no-bowl a/n, other five c/p)",
                    lambda r: ("a/n" if (r["line"], r.get("pos")) == ("L05", "14") else "c/p") if r["class"] == "4TRI" else v8(r))):
        c = Counter(m.band(f(r), r["class"], False, True) for r in d)
        out.append(f"{tag}: firm {c['firm']} / two-way {c['two-way']} / wider {c['wider']} / unread-or-null {c['null'] + c['unread']} [null {c['null']} + unread {c['unread']}]")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/meter_v11_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
