#!/usr/bin/env python3
"""Offline test for ciphers/fr2933-salviati-1525/control/codemark_curve.py's --merge option (LANE R7 ATF55V,
25 Sept 2026). No network. Runs `stats --leaves all` against the target's own committed transcription (as
tools/tests/test_decode_key.py does for fr20140-danzay-1557) and checks: (1) without --merge, pooled code+mark
types is 223 and f55v's own count is 93 (the pre-merge baseline in NOTES.md); (2) with the real
merges_f55v.tsv (one merge row, H^o|1 -> H^1|o), pooled drops to 222 and f55v to 92, and every other leaf's
count is unchanged or drops by exactly the leaves that carried an o|1 occurrence; (3) a merge file whose
from_type never occurs in the data is a safe no-op (pooled stays 223); (4) --merge accepts two files and
resolves a merge chained across them (S4^ -> S^ -> wd^, two hops) by folding two distinct pooled types into
one, dropping the pooled count by exactly 2.
Run: python3 tools/tests/test_codemark_curve.py"""
import csv, os, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TARGET = os.path.join(ROOT, "ciphers", "fr2933-salviati-1525")
TOOL = os.path.join(TARGET, "control", "codemark_curve.py")
MERGES = os.path.join(TARGET, "merges_f55v.tsv")

fails = 0


def stats(*extra):
    r = subprocess.run([sys.executable, TOOL, "stats", "--leaves", "all", *extra],
                        capture_output=True, text=True, cwd=TARGET, check=True)
    rows = list(csv.DictReader(r.stdout.splitlines(), delimiter="\t"))
    return {row["leaf"]: int(row["code_mark_types"]) for row in rows}


def check(name, cond):
    global fails
    fails += not cond
    print(("PASS" if cond else "FAIL"), name)


base = stats()
check("baseline pooled = 223 (NOTES.md LANE R6 CM table)", base["pooled"] == 223)
check("baseline f55v = 93", base["f55v"] == 93)

merged = stats("--merge", MERGES)
check("merges_f55v.tsv: pooled 223 -> 222 (one merge row)", merged["pooled"] == base["pooled"] - 1)
check("merges_f55v.tsv: f55v 93 -> 92", merged["f55v"] == base["f55v"] - 1)
check("merges_f55v.tsv: no leaf count increases", all(merged[lf] <= base[lf] for lf in base))
check("merges_f55v.tsv: leaves without an o|1 occurrence are untouched",
      merged["f55r"] == base["f55r"] and merged["f56r"] == base["f56r"] and merged["f57v"] == base["f57v"])

tmp = tempfile.mkdtemp()
try:
    noop = os.path.join(tmp, "noop.tsv")
    with open(noop, "w") as fh:
        fh.write("kind\tfrom_type\tto_type\nmerge\tZZZ^doesnotexist\tS^\n")
    r = stats("--merge", noop)
    check("merge file with an absent from_type is a no-op", r["pooled"] == base["pooled"])

    hop1 = os.path.join(tmp, "hop1.tsv")
    hop2 = os.path.join(tmp, "hop2.tsv")
    with open(hop1, "w") as fh:
        fh.write("kind\tfrom_type\tto_type\nmerge\tS4^\tS^\n")
    with open(hop2, "w") as fh:
        fh.write("kind\tfrom_type\tto_type\nmerge\tS^\twd^\n")
    r = stats("--merge", hop1, hop2)
    check("two-file --merge resolves a 2-hop chain (S4^ -> S^ -> wd^), pooled drops by 2", r["pooled"] == base["pooled"] - 2)
finally:
    import shutil
    shutil.rmtree(tmp)

sys.exit(1 if fails else 0)
