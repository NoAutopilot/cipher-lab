#!/usr/bin/env python3
"""VERIFY-F61-V9 (29 Sept 2026): f.61r meter under key v6 plus the V8-endorsed cells, which is key v7 as merged (F61-FAMILY-11 landed
family/key_period_v7.tsv at 10:17 UTC while this job ran; its own v7 meter figure 12/59/2/26 equals the baseline row here) with the V8-endorsed 4PI split as the baseline, then with and without CA as a null and with and without C6 = e on f.61.
Bands as verify_v8/meter_v8.py (firm / two-way / wider / unread-or-null), plus the unread-or-null band split into 'null' (a published null:
Tomokiyo's dash at every f.61 position of the class, family/key_published_rare.tsv -- CA, LOOPBAR, LL, CROSS) and 'unread' (C6, and 4PI at L01 12).
meter_v8 counts C6 as unread-or-null whatever the key says; here 'C6 = e on f.61' moves its 8 tokens to firm.  python3 meter_v9.py [--check]"""
import csv, os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); F = os.path.abspath(f"{HERE}/../family"); sys.path.insert(0, F)
import build_key_v6 as bk
KEY = ("key v6 loaded (family/key_period_v6.tsv) + the V8 cells = key v7 as merged (F61-FAMILY-11 landed family/key_period_v7.tsv 10:17 UTC while this ran; "
       "its own meter, v7 as merged, is 12/59/2/26 = the baseline row below)")
NULLS = {"CA", "LOOPBAR", "LL", "CROSS"}
def band(letters, cls, c6e, ca_null):
    if cls == "C6": return "firm" if c6e else "unread"
    if letters in ("-", ""): return "null" if (cls in NULLS and (ca_null or cls != "CA")) else ("unread" if cls == "CA" or cls == "4PI" else "null")
    n = len(letters.split("/")); return "firm" if n == 1 else ("two-way" if n == 2 else "wider")
def main():
    d = list(csv.DictReader(open(f"{F}/f61_decode_period_v4_frac0.1_sbs.tsv"), delimiter="\t")); k6 = bk.load_key_v6(ebr="B", f61=True)
    V5 = {"VBAR_A": "g/t", "EBR": "l/y", "SBS": "b/o"}
    def v6(r):
        c = r["class"]
        if c in V5: return V5[c]
        if c in ("ZHOOK", "HASH4", "4TRI", "4STEM"): return "/".join(k6[c])
        return r["period_letters"]
    v8 = lambda r: ("a/n" if r["line"] == "L11" else "-") if r["class"] == "4PI" else v6(r)   # V8: L11 9 a/n grade M, L01 12 unread
    out = [f"meter_v9: {KEY}; {len(d)} signs; bands firm / two-way / wider / unread-or-null [= null + unread]"]
    for tag, f, c6e, ca_null in (("v6 as meter_v8 (CA counted unread, C6 unread-or-null)", v6, False, False),
                                  ("v6 + V8 4PI split (L11 9 a/n M, L01 12 unread) -- baseline", v8, False, False),
                                  ("baseline + CA as null (endorsed here)", v8, False, True),
                                  ("baseline + C6 = e on f.61 (pooled cell applied; NOT endorsed)", v8, True, False),
                                  ("baseline + CA as null + C6 = e on f.61", v8, True, True)):
        c = Counter(band(f(r), r["class"], c6e, ca_null) for r in d)
        out.append(f"{tag}: firm {c['firm']} / two-way {c['two-way']} / wider {c['wider']} / unread-or-null {c['null'] + c['unread']} [null {c['null']} + unread {c['unread']}]")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/meter_v9_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
