#!/usr/bin/env python3
"""Offline test for tools/solver_repo_diff.py's --census mode: no network. Builds tiny throwaway
Bourdeau/Aymeloglu clone directories, a tiny ciphers/ + QUEUE.md, and a 4-row census TSV, then checks
held_by for a cipher-lab hit, a Bourdeau hit (by id), an Aymeloglu hit (by shelfmark), and a genuine
none. Also checks --help exits cleanly.
Run: python3 tools/tests/test_solver_repo_diff.py"""
import csv
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOOL = os.path.join(ROOT, "tools", "solver_repo_diff.py")

fails = 0


def fail(msg):
    global fails
    print(f"FAIL: {msg}")
    fails += 1


with tempfile.TemporaryDirectory() as tmp:
    bour = os.path.join(tmp, "bourdeau")
    aym = os.path.join(tmp, "aymeloglu")
    repo = os.path.join(tmp, "repo")
    os.makedirs(os.path.join(bour, "targetone"))
    os.makedirs(os.path.join(aym))
    os.makedirs(os.path.join(repo, "ciphers", "oursletter"))

    # Bourdeau: a target folder whose profile.json names DECODE id R2000 (id hit; ids_in() only
    # scans profile.json's own JSON blob, matching build_bourdeau_index()'s documented behaviour).
    with open(os.path.join(bour, "targetone", "profile.json"), "w", encoding="utf-8") as f:
        f.write('{"documents": [{"shelfmark": "unrelated shelfmark", "decode_id": "R2000"}], '
                '"title": "Test", "outcome": {"class": "solved"}}')
    with open(os.path.join(bour, "targetone", "NOTES.md"), "w", encoding="utf-8") as f:
        f.write("Read from DECODE R2000, a Simancas legajo item.")

    # Aymeloglu: a TARGETS.md line naming a BnF shelfmark (volume hit).
    with open(os.path.join(aym, "TARGETS.md"), "w", encoding="utf-8") as f:
        f.write("| 1 | Some letter (BnF Français 9999) | 1600 | fr | solved |\n")

    # cipher-lab: a target folder naming its own DECODE id.
    with open(os.path.join(repo, "ciphers", "oursletter", "NOTES.md"), "w", encoding="utf-8") as f:
        f.write("Read from DECODE R3000, our own target.")
    with open(os.path.join(repo, "QUEUE.md"), "w", encoding="utf-8") as f:
        f.write("# queue\n")
    with open(os.path.join(repo, "CATALOG.md"), "w", encoding="utf-8") as f:
        f.write("# catalog\n")

    census = os.path.join(tmp, "census.tsv")
    fields = ["id", "status", "record_type", "holder_raw", "city", "shelfmark_code", "date_range",
              "cleartext_lang", "plaintext_lang", "number_of_pages", "source_page"]
    rows = [
        {"id": "3000", "holder_raw": "cipher-lab's own letter", "shelfmark_code": "OURS_1"},
        {"id": "2000", "holder_raw": "a Simancas legajo item", "shelfmark_code": "AGS_2"},
        {"id": "5000", "holder_raw": "Paris, BnF, Français 9999 fol. 1.", "shelfmark_code": "BNF_Français_9999_001"},
        {"id": "9000", "holder_raw": "an entirely unrelated record, nobody's", "shelfmark_code": "XYZ_1"},
    ]
    with open(census, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t")
        w.writeheader()
        for r in rows:
            full = {k: r.get(k, "") for k in fields}
            w.writerow(full)

    out = os.path.join(tmp, "out.tsv")
    r = subprocess.run(
        [sys.executable, TOOL, "--census", census, "--out", out,
         "--queue", os.path.join(repo, "QUEUE.md"), bour, aym],
        cwd=repo, capture_output=True, text=True,
    )
    if r.returncode != 0:
        fail(f"census run exited {r.returncode}: {r.stderr}")

    held = {}
    if os.path.exists(out):
        with open(out, encoding="utf-8") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                held[row["id"]] = row["held_by"]

    checks = {
        "3000": "ours:oursletter",
        "2000": "bourdeau:targetone",
        "5000": "aymeloglu:TARGETS.md",
        "9000": "none",
    }
    for rid, expected in checks.items():
        got = held.get(rid)
        if got != expected:
            fail(f"held_by[{rid}] = {got!r}, expected {expected!r}")

help_r = subprocess.run([sys.executable, TOOL, "--help"], capture_output=True, text=True)
if help_r.returncode != 0 or "--census" not in help_r.stdout:
    fail(f"--help failed or missing --census: rc={help_r.returncode}")

if fails:
    print(f"{fails} failure(s)")
    sys.exit(1)
print("ok")
