#!/usr/bin/env python3
"""Offline test: ciphers/na-janssens-java-1811 build_key.py and merge_leaf.py read corrections.tsv (JAV-CORR, 15 Oct 2026).

Must catch: a pass-file row named in corrections.tsv (keyed leaf/order, line label bare or 'keysource-<leaf>') is read at
its corrected code; a stale correction (pass code != token) or one matching no row stops the run.
Must not block: a corrections.tsv row whose `file` is ciphertext.tsv (decode_key.py's exceptions), or one naming another
pass file, leaves the pass untouched. Real-folder check: a keysource rebuild has 420 at leaf 200 and no row 120.
Run: python3 tools/tests/test_janssens_corrections.py
"""
import csv, os, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
T = os.path.join(ROOT, "ciphers", "na-janssens-java-1811")
BUILD, MERGE = os.path.join(T, "scripts", "build_key.py"), os.path.join(T, "scripts", "merge_leaf.py")
CH = ["line", "pos", "token", "corrected", "value", "grade", "read_grade", "source", "reason", "file"]


def wtsv(path, header, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t"); w.writerow(header); w.writerows(rows)


def key(path):
    return {r["code"]: r for r in csv.DictReader(open(path, encoding="utf-8"), delimiter="\t")}


def run(*a):
    return subprocess.run([sys.executable, *a], capture_output=True, text=True)


def corr_rows(token="120", file="pA.tsv;pB.tsv"):
    return [["13", "11", "1194", "1192", "et", "C", "H", "x", "x", "ciphertext.tsv"],
            ["keysource-200", "2", token, "420", "fin", "C", "eye", "x", "x", file]]


def main():
    fails = 0
    def check(ok, msg):
        nonlocal fails
        print(("ok   " if ok else "FAIL ") + msg); fails += (not ok)

    with tempfile.TemporaryDirectory() as d:
        P = ["leaf", "order", "code", "gloss", "note"]
        rows = [["200", "1", "744", "Java", ""], ["200", "2", "120", "Fin.", ""]]
        wtsv(f"{d}/pA.tsv", P, rows); wtsv(f"{d}/pB.tsv", P, rows)
        wtsv(f"{d}/c.tsv", CH, corr_rows())
        r = run(BUILD, f"{d}/pA.tsv", f"{d}/pB.tsv", "--out-dir", d, "--corrections", f"{d}/c.tsv")
        k = key(f"{d}/key.tsv")
        check(r.returncode == 0 and "420" in k and "120" not in k and k["420"]["grade"] == "C", "build_key applies keysource-200:2 120->420")
        r = run(BUILD, f"{d}/pA.tsv", f"{d}/pB.tsv", "--out-dir", d, "--corrections", "")
        check("120" in key(f"{d}/key.tsv"), "build_key --corrections '' leaves the pass as transcribed")
        wtsv(f"{d}/c2.tsv", CH, corr_rows(file="other.tsv"))
        r = run(BUILD, f"{d}/pA.tsv", f"{d}/pB.tsv", "--out-dir", d, "--corrections", f"{d}/c2.tsv")
        check(r.returncode == 0 and "120" in key(f"{d}/key.tsv"), "row naming another file (and the ciphertext.tsv row) not applied")
        wtsv(f"{d}/c3.tsv", CH, corr_rows(token="121"))
        r = run(BUILD, f"{d}/pA.tsv", f"{d}/pB.tsv", "--out-dir", d, "--corrections", f"{d}/c3.tsv")
        check(r.returncode != 0 and "stale correction" in (r.stdout + r.stderr), "stale correction stops build_key")
        # merge_leaf: leaf file named in corrections
        wtsv(f"{d}/leaf200.tsv", P, rows)
        wtsv(f"{d}/c4.tsv", CH, [["200", "2", "120", "420", "fin", "C", "eye", "x", "x", "leaf200.tsv"]])
        wtsv(f"{d}/k.tsv", ["code", "value", "n", "pages", "grade", "note"], [["420", "fin", "1", "192", "C", ""]])
        wtsv(f"{d}/cf.tsv", ["code", "variants", "decision"], [])
        r = run(MERGE, f"{d}/leaf200.tsv", "--key", f"{d}/k.tsv", "--conflicts", f"{d}/cf.tsv", "--corrections", f"{d}/c4.tsv")
        k = key(f"{d}/k.tsv")
        check(r.returncode == 0 and "120" not in k and k["420"]["n"] == "2" and k["420"]["pages"] == "192,200" and k["420"]["grade"] == "C",
              "merge_leaf applies 200:2 120->420 (same value, n+1)")
        wtsv(f"{d}/c5.tsv", CH, [["200", "9", "120", "420", "fin", "C", "eye", "x", "x", "leaf200.tsv"]])
        r = run(MERGE, f"{d}/leaf200.tsv", "--key", f"{d}/k.tsv", "--conflicts", f"{d}/cf.tsv", "--corrections", f"{d}/c5.tsv", "--dry-run")
        check(r.returncode != 0 and "match no pass row" in (r.stdout + r.stderr), "correction matching no row stops merge_leaf")
        # real folder, default corrections.tsv
        r = run(BUILD, os.path.join(T, "keysource_passA.tsv"), os.path.join(T, "keysource_passB.tsv"), "--out-dir", d)
        k = key(f"{d}/key.tsv")
        check(r.returncode == 0 and "120" not in k and "420" in k and "200" in k["420"]["pages"].split(","),
              "real keysource rebuild: 200:119 read as 420, no row 120")
    print("FAILED" if fails else "all ok"); return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
