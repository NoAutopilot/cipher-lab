#!/usr/bin/env python3
"""Offline test for tools/verify_backlog.py (LANE-SYS1, 5 Oct 2026). Fixtures under a temp dir; no network.

Catches: Audit 1 done + Audit 2 missing (both registers); Audit 2 done + count open; a status.json folder absent from
PROGRESS.tsv listed with a note; register disagreement noted; --check fails on a stale file.
Must NOT: list Audit 1 not done; list correction results; treat a 'not counted' / N0 PROGRESS row or a two-audit
key-to-known-text result as an open count; mis-sort (priority, then oldest first).
Run: python3 tools/tests/test_verify_backlog.py
"""
import json, os, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import verify_backlog as vb  # noqa: E402

HDR = "name\tfolder\tfirm\ttotal\tF\tK\tksrc\ttxt\tR\t1\t2\tC\tS\tsent_star\tnote\tupdated\tsource\n"


def prow(name, folder, a1, a2, c, note, updated):
    return "\t".join([name, folder, "1", "9", "x", "x", "o", "n", "x", a1, a2, c, ".", "", note, updated, "f"]) + "\n"


PROG = ("# comment\n" + HDR
        + prow("NoAudit", "f-none", ".", ".", ".", "", "1 Oct 2026")
        + prow("NeedA2", "f-a", "x", ".", ".", "AUDIT 1 N3", "3 Oct 2026")
        + prow("NeedC", "f-b", "x", "x", ".", "audit 2 N4", "2026-10-02")
        + prow("Decided", "f-c", "x", "x", ".", "N4; class without a reading -- not counted", "4 Oct 2026")
        + prow("KnownN0", "f-d", "x", ".", ".", "audit 1 N0", "26 Sept 2026")
        + prow("Done", "f-e", "x", "x", "x", "N4", "1 Oct 2026"))
RESULTS = {"results": [
    {"link": "https://x/tree/main/ciphers/f-e", "audit_status": "one audit", "claim_scope": "key-to-known-text",
     "date": "24 Sept 2026", "title": "E one audit"},
    {"link": "https://x/tree/main/ciphers/f-z", "audit_status": "two audits", "claim_scope": "recovered-passages",
     "novelty": "N4", "date": "25 Sept 2026", "title": "Z no depth"},
    {"link": "https://x/tree/main/ciphers/f-y", "audit_status": "one audit", "claim_scope": "correction",
     "date": "20 Sept 2026", "title": "Y correction"},
    {"link": "https://x/tree/main/ciphers/f-x", "audit_status": "two audits", "claim_scope": "key-to-known-text",
     "date": "20 Sept 2026", "title": "X known text"},
    {"link": "https://x/tree/main/ciphers/f-w", "claim_scope": "recovered-passages", "date": "20 Sept 2026",
     "title": "W never audited"},
]}


def build():
    d = tempfile.mkdtemp()
    p, s = os.path.join(d, "P.tsv"), os.path.join(d, "s.json")
    open(p, "w").write(PROG)
    json.dump(RESULTS, open(s, "w"))
    return d, p, s, vb.build(vb.load_progress(p), vb.load_results(s))


def by(rows, name):
    return [r for r in rows if r["name"] == name]


def test_catches():
    _, _, _, rows = build()
    assert by(rows, "NeedA2")[0]["missing"] == "both" and by(rows, "NeedA2")[0]["priority"] == "high"
    assert by(rows, "NeedC")[0]["missing"] == "counted" and "depth_check.py" in by(rows, "NeedC")[0]["next_action"]
    z = by(rows, "Z no depth")[0]
    assert z["missing"] == "counted" and "absent from PROGRESS.tsv" in z["note"]
    e = by(rows, "E one audit")[0]
    assert e["missing"] == "audit2" and e["priority"] == "low" and "REGISTERS DISAGREE" in e["note"]


def test_must_not():
    _, _, _, rows = build()
    names = {r["name"] for r in rows}
    assert "NoAudit" not in names and "Y correction" not in names and "X known text" not in names
    assert "W never audited" not in names and "Done" not in names
    dec = by(rows, "Decided")[0]
    assert dec["priority"] == "none" and dec["next_action"].startswith("no verifier action")
    k = by(rows, "KnownN0")[0]
    assert k["missing"] == "audit2" and k["priority"] == "low"


def test_order_and_dates():
    _, _, _, rows = build()
    pr = [r["priority"] for r in rows]
    assert pr == sorted(pr, key={"high": 0, "low": 1, "none": 2}.get)
    high = [r["audit1_date"] for r in rows if r["priority"] == "high"]
    assert high == sorted(high)
    assert vb.parse_date("26 Sept 2026") == "2026-09-26" and vb.parse_date("2026-10-03 15:3x") == "2026-10-03"
    assert vb.parse_date("soon") == ""


def test_check_stale():
    d, p, s, _ = build()
    out = os.path.join(d, "V.tsv")
    assert vb.main(["--progress", p, "--status", s, "--out", out]) == 0
    assert vb.main(["--progress", p, "--status", s, "--out", out, "--check"]) == 0
    open(out, "a").write("extra\trow\n")
    assert vb.main(["--progress", p, "--status", s, "--out", out, "--check"]) == 1


if __name__ == "__main__":
    for f in [test_catches, test_must_not, test_order_and_dates, test_check_stale]:
        f()
    print("ok: 4 tests")
