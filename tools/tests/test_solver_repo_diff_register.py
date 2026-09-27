#!/usr/bin/env python3
"""Offline test for tools/solver_repo_diff.py's --register mode: no network. Builds a tiny register TSV
(archive/shelfmark/folios/sender_recipient, the KEY-ADJACENT.tsv shape) and tiny throwaway Bourdeau/
Aymeloglu clone directories, then checks the three verdicts:
  - full-reading: the row's own folio/item number is confirmed in the matching Bourdeau or Aymeloglu text
    (a Colbert-fonds row spelled three different ways -- '500 de Colbert 401', 'Mélanges de Colbert 155',
    a bare accented 'Colbert' abbreviation elsewhere -- all normalise to the shared volume key).
  - partial: the shelfmark/volume matches but the row's own folio/item is not confirmed anywhere in the
    matching text -- the fr.3983/lebel1593 shape from KEY-ADJACENT.tsv row 23 (savoy), where Bourdeau's
    lebel1593 profile covers different item numbers (11, 62, 100) than this row's folios (26, 130).
  - none: no volume key or DECODE id in common anywhere.
Also checks --help documents --register.
Run: python3 tools/tests/test_solver_repo_diff_register.py"""
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
    os.makedirs(bour)
    os.makedirs(aym)

    # Bourdeau: segur1586 covers "500 de Colbert 401" f.321 -- full-reading via folio match.
    os.makedirs(os.path.join(bour, "segur1586"))
    with open(os.path.join(bour, "segur1586", "profile.json"), "w", encoding="utf-8") as f:
        f.write('{"documents": [{"shelfmark": "irrelevant"}], "title": "Segur", "outcome": {"class": "solved"}}')
    with open(os.path.join(bour, "segur1586", "NOTES.md"), "w", encoding="utf-8") as f:
        f.write("BnF 500 de Colbert 401, f.321, Henry of Navarre to Segur, fully read.")

    # Aymeloglu catalog/decode-catalog.csv: caracciolo item, matched by DECODE id -- full-reading via id.
    with open(os.path.join(aym, "decode-catalog.csv"), "w", encoding="utf-8") as f:
        f.write("id,note\nR9966,Cardinal Caracciolo to Charles V read with Cifrario 38\n")

    # Bourdeau: r3708 names the accented "Mélanges de Colbert 155" spelling and the row's own folio
    # (the register row below spells it "Colbert 155" and "canvas 207-208", the accented form must still
    # match via volume_keys, and "133" must still be found as a folio token deep in NOTES.md).
    os.makedirs(os.path.join(bour, "r3708"))
    with open(os.path.join(bour, "r3708", "profile.json"), "w", encoding="utf-8") as f:
        f.write('{"documents": [{"shelfmark": "irrelevant"}], "title": "Beziers", "outcome": {"class": "solved"}}')
    with open(os.path.join(bour, "r3708", "NOTES.md"), "w", encoding="utf-8") as f:
        f.write("Mélanges de Colbert 155, folio 133 recto-verso, l'Evesque de Beziers, fully read.")

    # Bourdeau: r2276 covers fr.20974 no.1 -- full-reading via folio/item token "1".
    os.makedirs(os.path.join(bour, "r2276"))
    with open(os.path.join(bour, "r2276", "profile.json"), "w", encoding="utf-8") as f:
        f.write('{"documents": [{"shelfmark": "irrelevant"}], "title": "Guise", "outcome": {"class": "solved"}}')
    with open(os.path.join(bour, "r2276", "NOTES.md"), "w", encoding="utf-8") as f:
        f.write("fr.20974 no.1, Duke of Guise correspondence, reads 91.8% of 3920 signs.")

    # Bourdeau: lebel1593 covers fr.3983 nos.11, 62, 100 -- a volume match but NOT this register row's
    # own folios (26, 130), so this must land as 'partial', never 'full-reading' (row 23's own shape).
    os.makedirs(os.path.join(bour, "lebel1593"))
    with open(os.path.join(bour, "lebel1593", "profile.json"), "w", encoding="utf-8") as f:
        f.write('{"documents": [{"shelfmark": "irrelevant"}], "title": "Lebel", "outcome": {"class": "open"}}')
    with open(os.path.join(bour, "lebel1593", "NOTES.md"), "w", encoding="utf-8") as f:
        f.write("BnF fr.3983 nos.11, 62, 100, Lebel to Duke of Savoy, reads ~97-98% of enciphered tokens.")

    register = os.path.join(tmp, "register.tsv")
    fields = ["archive", "shelfmark", "folios", "sender_recipient", "in_repo"]
    rows = [
        # row 2 (full-reading via folio, three-way fonds spelling)
        {"archive": "BnF", "shelfmark": "500 de Colbert 401", "folios": "f.321 (June 1586)",
         "sender_recipient": "Henry of Navarre to Segur"},
        # row 7 (full-reading via folio, accented Mélanges spelling normalising to the register's own
        # bare "Colbert 155" form)
        {"archive": "BnF", "shelfmark": "Melanges de Colbert 155", "folios": "folio 133 recto-verso",
         "sender_recipient": "l'Evesque de Beziers"},
        # row 10 (full-reading via item number "no.7"/"1" style token match)
        {"archive": "BnF", "shelfmark": "fr.20974", "folios": "p.1 (no.1)",
         "sender_recipient": "Duke of Guise correspondence"},
        # row 13 (full-reading via DECODE id)
        {"archive": "Archivo General de Simancas (AGS)", "shelfmark": "EST,LEG,1184,110 (DECODE R9966)",
         "folios": "--", "sender_recipient": "Cardinal Caracciolo to Charles V"},
        # row 23 (savoy): volume matches lebel1593 (fr.3983) but this row's own folios (26, 130) are not
        # among lebel1593's covered items (11, 62, 100) -- partial, not full-reading.
        {"archive": "BnF", "shelfmark": "fr.3983, fr.3984, fr.3985",
         "folios": "f.26, f.130, f.194, f.195 of fr.3983", "sender_recipient": "ambassador Lebel to Duke of Savoy"},
        # a genuine none: no volume key or id shared with anything above.
        {"archive": "TNA", "shelfmark": "SP53/23", "folios": "f.101", "sender_recipient": "nobody in these fixtures"},
    ]
    with open(register, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fields})

    r = subprocess.run(
        [sys.executable, TOOL, "--register", register, bour, aym],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        fail(f"register run exited {r.returncode}: {r.stderr}")

    out_lines = [ln for ln in r.stdout.splitlines() if ln.strip()]
    verdicts = {}
    for ln in out_lines[1:]:
        parts = ln.split("\t")
        verdicts[int(parts[0])] = parts[2]

    checks = {2: "full-reading", 3: "full-reading", 4: "full-reading", 5: "full-reading",
              6: "partial", 7: "none"}
    for line_no, expected in checks.items():
        got = verdicts.get(line_no)
        if got != expected:
            fail(f"verdict[line {line_no}] = {got!r}, expected {expected!r} (full output: {out_lines})")

help_r = subprocess.run([sys.executable, TOOL, "--help"], capture_output=True, text=True)
if help_r.returncode != 0 or "--register" not in help_r.stdout:
    fail(f"--help failed or missing --register: rc={help_r.returncode}")

if fails:
    print(f"{fails} failure(s)")
    sys.exit(1)
print("ok")
