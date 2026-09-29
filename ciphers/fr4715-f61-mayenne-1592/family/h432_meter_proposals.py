#!/usr/bin/env python3
"""H432 (runner 16 session_01Vtwc6CEJD2BSnYdzzY4f8W, 29 Sept 2026), script-only: the f.61 meter and five-span count for the states a verifier and
the orchestrator are choosing between, by VERIFY-F61-V12's own functions (verify_v12/meter_v12.meter / .spans, imported, not re-implemented):
(c) V12 endorsed; (c) + H428 L11/8 4STEM -> CROSS (null); (d) = (c) + L02 opening LL (V12 C4 + H428); (e) = (d) + L11/8 CROSS.
Replaces the hand-computed figure in NOTES.md H428. The corrections file is untouched.  python3 h432_meter_proposals.py [--check]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.abspath(f"{HERE}/.."); CHECK = "--check" in sys.argv; sys.argv = sys.argv[:1]
sys.path.insert(0, f"{T}/verify_v12")
import meter_v12 as v
v.LET.setdefault("CROSS", "-")
L118 = [("L11", "8", "relabel", "CROSS")]
def main():
    out = []
    for tag, corr in (("(c) V12 endorsed", v.MINE), ("(c) + H428 L11/8 CROSS", v.MINE + L118), ("(d) (c) + L02 opening LL (V12 C4, H428)", v.MINE_LL),
                      ("(e) (d) + H428 L11/8 CROSS", v.MINE_LL + L118)):
        out.append(f"{tag}: spans {v.spans(corr)}; meter {v.meter(corr)}")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h432_meter_proposals_result.txt"
    if CHECK:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
