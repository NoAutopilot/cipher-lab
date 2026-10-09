#!/usr/bin/env python3
"""Offline test for tools/build_catalogue.py (CATALOGUE-SITE-1, 9 Oct 2026). Fixture rows, all two audits:
  A  N4, D2, recovered passages, register line with a job name in brackets  -> listed, job name gone, safe sentence quoted
  B  N3, D1                                                                 -> listed under fragments read
  C  N2, D2                                                                 -> not listed (below N3)
  R  N4, D2, folder debosnys-x                                              -> never listed (restricted)
Must catch: a job name or session id surviving into a page; a counted row missing; an output path under docs/.
Must NOT block: shelfmarks and edition references with capitals and hyphens ("OR I/32 pt 3", "KHA A 11/XIV B/41-42",
"WVO 5797") survive sanitize(). Run: python3 tools/tests/test_build_catalogue.py"""
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import build_catalogue as bc  # noqa: E402


def row(title, folder, **f):
    r = {"title": title, "kind": "recovery", "grade": "N4", "date": "5 Oct 2026", "line": "x",
         "link": "https://github.com/NoAutopilot/cipher-lab/tree/main/ciphers/" + folder,
         "document_id": "doc " + title, "claim_scope": "recovered-passages", "plaintext_novelty": "N4",
         "mapping_novelty": "N4", "audit_status": "two audits", "depth": "D2", "depth_pct": 40.0,
         "depth_sentence": "The writer names the Landgrave.", "key": "period", "superseded_by": ""}
    r.update(f)
    return r


fails = 0


def check(cond, msg):
    global fails
    if not cond:
        fails += 1
        print("FAIL:", msg)


# sanitize: must catch / must not block
s = bc.sanitize("Partially deciphered (about 67%; D2, DEPTH-MH 8 Oct 2026). Read by AUDIT2-MANT and N8-GRA2 for session_01AbC; "
                "LANE AX (owner account) round 3: OR I/32 pt 3 p.498, KHA A 11/XIV B/41-42, WVO 5797. A check-solved worker made it.")
for bad in ("DEPTH-MH", "AUDIT2-MANT", "N8-GRA2", "session_", "LANE", "worker"):
    check(bad not in s, f"sanitize left {bad!r}: {s}")
for good in ("OR I/32 pt 3 p.498", "KHA A 11/XIV B/41-42", "WVO 5797", "We made it"):
    check(good in s, f"sanitize removed {good!r}: {s}")

with tempfile.TemporaryDirectory() as tmp:
    os.makedirs(os.path.join(tmp, "tools"))
    for f in ("build_dashboard.py", "build_catalogue.py"):
        shutil.copy(os.path.join(ROOT, "tools", f), os.path.join(tmp, "tools"))
    results = [row("Alpha to Beta, WVO 5797", "alpha", line="Partially deciphered (R9-MANTV 6 Oct 2026). Reading: in WVO 5797 two blanks read in part under a period "
                                                       "table; no prior decipherment of these blanks located"),
               row("Bravo fragments", "bravo", depth="D1", plaintext_novelty="N3", grade="N3"),
               row("Charlie", "charlie", plaintext_novelty="N2", grade="N2"),
               row("Restricted", "debosnys-x")]
    json.dump({"results": results, "targets": [{"status": "open"}, {"status": "blocked"}]},
              open(os.path.join(tmp, "status.json"), "w"))
    for fold, st in (("alpha", "partial"), ("bravo", "solved"), ("charlie", "open"), ("debosnys-x", "open")):
        os.makedirs(os.path.join(tmp, "ciphers", fold))
        open(os.path.join(tmp, "ciphers", fold, "NOTES.md"), "w").write(f"# {fold}\n\n{st}\n")
    open(os.path.join(tmp, "ciphers", "alpha", "AUDIT.md"), "w").write(
        "# AUDIT\n\n**Unsafe sentence.** \"The first decipherment of Alpha to Beta, never printed before anywhere at all.\"\n\n"
        "**Safe sentence.** \"In WVO 5797 (Alpha to Beta) two blanks read in part under a period table; no prior decipherment "
        "of these blanks located (VERIFY-X).\"\n")
    p = subprocess.run([sys.executable, "tools/build_catalogue.py", "--out", "out", "--mockup", "mock.html",
                        "--mockup-items", "WVO 5797"], cwd=tmp, capture_output=True, text=True, timeout=60)
    check(p.returncode == 0, f"builder exit {p.returncode}: {p.stderr[-400:]}")
    pages = glob.glob(os.path.join(tmp, "out", "items", "*.html"))
    check(len(pages) == 2, f"expected 2 item pages (A, B), got {len(pages)}")
    idx = open(os.path.join(tmp, "out", "index.html")).read()
    check("Charlie" not in idx and "Restricted" not in idx, "N2 or restricted row listed")
    check("2 targets in work" in idx, "open/blocked targets not reduced to a count")
    allhtml = idx + "".join(open(x).read() for x in pages) + open(os.path.join(tmp, "mock.html")).read()
    check(not re.search(r"R9-MANTV|VERIFY-X|session_", allhtml), "job name survived into a page")
    check("two blanks read in part" in allhtml, "safe sentence not quoted from AUDIT.md")
    check("first decipherment" not in allhtml, "unsafe sentence quoted")
    check("<script" not in allhtml and "http://fonts" not in allhtml, "page carries a script or remote asset")
    check("fragments read" in open([x for x in pages if "bravo" in x][0]).read(), "D1 row not worded 'fragments read'")
    p2 = subprocess.run([sys.executable, "tools/build_catalogue.py", "--out", "docs/catalogue"], cwd=tmp,
                        capture_output=True, text=True, timeout=60)
    check(p2.returncode != 0 and not os.path.exists(os.path.join(tmp, "docs")), "docs/ output not refused")

print("FAIL" if fails else "ok: test_build_catalogue")
sys.exit(1 if fails else 0)
