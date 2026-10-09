#!/usr/bin/env python3
"""Offline tests for tools/prior_work.py --interceptor (MQS-INTERCEPTOR, 9 Oct 2026; CLAUDE.md Usage 8a; pre-registered in
tools/tests/PREREG-MQS-INTERCEPTOR.md). Reads the committed tools/data/interceptor_depots.tsv; no network.
Must catch (known answer): England 1586 -> TNA SP 53 and BL Harley MS 1582 (Mary Stuart, Lasry, Biermann and Tomokiyo
2023 pp.108-109, p.188 n.332); England 1659 -> Thurloe papers (KEYHUNT-2026-10-07.tsv row 464); France 1589 -> BnF
fr.3977 (KEYHUNT row 15).
Must NOT list (null): Spain 1586, England 1700, France 1659, England 1500 -> none of those four depot rows.
Run: python3 tools/tests/test_prior_work_interceptor.py"""
import contextlib, io, os, socket, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "tools"))
import prior_work as pw  # noqa: E402


def _no_net(*a, **k):
    raise AssertionError("network access attempted in an offline test")


socket.socket.connect = _no_net
K = {"sp53": "TNA SP 53", "harley": "BL Harley MS 1582", "thurloe": "Thurloe papers", "fr3977": "BnF fr.3977"}
KNOWN = [("England", 1586, {"sp53", "harley"}), ("england", 1659, {"thurloe"}), ("France", 1589, {"fr3977"})]
NULL = [("Spain", 1586), ("England", 1700), ("France", 1659), ("England", 1500)]


def listed(power, year):
    rows = pw.interceptor_depots(REPO, power, year)
    return {k for k, v in K.items() if any(r["depot"].startswith(v) for r in rows)}


def main():
    fails = 0
    hit = sum(len(want & listed(p, y)) for p, y, want in KNOWN)
    need = sum(len(w) for _, _, w in KNOWN)
    false = sum(len(listed(p, y)) for p, y in NULL)
    print(f"known answer: {hit}/{need} depot rows listed (gate {need}/{need})")
    print(f"null: {false}/{len(NULL) * len(K)} known-answer depot rows listed under mismatched power/date (gate 0)")
    fails += hit != need
    fails += false != 0
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        rc = pw.main(["-", "--interceptor", "England", "--year", "1586"])
    text = out.getvalue()
    if rc != 0 or "SP 53" not in text or "marks nothing searched" not in text:
        print("FAIL cli: exit", rc); fails += 1
    with contextlib.redirect_stdout(io.StringIO()) as o:
        pw.main(["-", "--interceptor", "Venice", "--year", "1586"])
    if "not a negative" not in o.getvalue():
        print("FAIL cli: empty list must say absence is not a negative"); fails += 1
    print("all passed" if not fails else f"{fails} failed")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
