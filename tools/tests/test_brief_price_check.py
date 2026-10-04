#!/usr/bin/env python3
"""Offline test for tools/brief_price_check.py (RETRO-2026-10-03-acct3 proposal 2): F36-GLOSS's own brief FAILS; a
gate-fix / print-check brief with no image step passes; a "disk only" brief passes; a correct "vision calls: N x USD r
= X" line under the cap passes; one over the cap fails; wrong arithmetic fails; the "Opus rate unmeasured" wording
passes; report wording alone is not an image step. Run: python3 tools/tests/test_brief_price_check.py"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import brief_price_check as b  # noqa: E402

F36 = os.path.join(ROOT, ".claude/briefs/runs/2026-10-03-acct3-f36-gloss.md")

CASES = [
    ("gate-fix, no image step",
     "# GF-X: gate fix for ciphers/foo. Model Sonnet. Cap $2, box 20 min. Read the standard edition's index, add the "
     "Premise check section, run tools/intake_gate_check.py and paste it. Report request counts per host.", 0),
    ("print check, no image step",
     "# PC-X: run tools/print_check.py ciphers/foo against phrases.txt. Cap USD 1.5. Report vision calls used (none "
     "expected) and the hits table.", 0),
    ("disk only, mentions crops in passing",
     "# FR-X: family_run on disk data. Disk only, no images. Cap $3. The crops folder is not touched; run "
     "tools/family_run.py specs/foo.json --family masc and paste both numbers.", 0),
    ("priced line just over cap (10.5 > 10)",
     "# TR-X: two blind passes over 6 line crops (tools/iiif_lines.py --image f12r.jpg --out crops). Model Sonnet. "
     "Cap $10, box 60 min.\nvision calls: 6 x USD 1.5 + 1 reconciliation = 10.5\n", 1),
    ("priced line under cap (exact)",
     "# TR-Y: blind pass over 6 crops. Cap $10.5. vision calls: 6 x USD 1.5 + 1 reconciliation = 10.5", 0),
    ("priced line over cap",
     "# TR-Z: Opus gloss read of 102 crops x 4 passes. Cap $6.\nvision calls: 408 x USD 1.5 = 612\n", 1),
    ("priced line, wrong arithmetic",
     "# TR-W: blind pass over 4 crops. Cap $10. vision calls: 4 x USD 1.5 = 3", 1),
    ("Opus rate unmeasured wording",
     "# OP-X: Opus blind pass over 2 gloss crops. Cap $6. Opus rate unmeasured: first call measured and reported, "
     "stop if over USD 3.", 0),
    ("image step, no line",
     "# TR-V: transcribe f.12r from crops cut with tools/iiif_lines.py. Cap $4.", 1),
]


def main():
    fails = 0
    with open(F36, encoding="utf-8") as f:
        rc, why, _ = b.check(f.read())
    if rc != 1:
        print(f"FAIL: F36-GLOSS brief should fail, got rc={rc} ({why})")
        fails += 1
    for name, text, want in CASES:
        rc, why, _ = b.check(text)
        if rc != want:
            print(f"FAIL: {name}: want rc={want}, got rc={rc} ({why})")
            fails += 1
    # Floor check (RETRO-2026-10-04-acct1 P2).
    floor_cases = [
        ("A3V2-THUR275 Fable 1.5 (fail)",
         "## A3V2-THUR275 -- thurloe-printed: JUNK_LINE running-head fix and key regeneration (Fable; cap USD 1.5; "
         "box 30 min)\nFix the running head.\n", [("A3V2-THUR275", "Fable", 1.5, 5.0)]),
        ("RUN4-PIS1 Opus 7 (pass)",
         "## RUN4-PIS1 -- fr16045-pisany-rome-1585: kp86 (Opus 5.5; cap USD 7; box 120 min)\nRead.\n", []),
        ("Sonnet cap 1 (pass)",
         "## SW-X -- sweep (Sonnet; cap USD 1; box 20 min)\nSweep.\n", []),
        ("no cap (pass)",
         "## NC-X -- a job with Opus named but no cap figure\nDo it.\n", []),
        ("Opus 2 in body (fail)",
         "## OB-X -- a short job\nOpus 5.5, cap $2, box 20 min.\n", [("OB-X", "Opus", 2.0, 2.5)]),
    ]
    for name, text, want in floor_cases:
        got = b.floor_check(text)
        if got != want:
            print(f"FAIL: floor {name}: want {want}, got {got}")
            fails += 1
    out = subprocess.run([sys.executable, os.path.join(ROOT, "tools/brief_price_check.py"), "--summary", F36],
                         capture_output=True, text=True)
    if out.returncode != 1 or "summary: 1 briefs" not in out.stdout:
        print("FAIL: CLI should exit 1 on F36-GLOSS and print a summary line")
        fails += 1
    if subprocess.run([sys.executable, os.path.join(ROOT, "tools/brief_price_check.py"), "--help"],
                      capture_output=True, text=True).returncode != 0:
        print("FAIL: --help should exit 0")
        fails += 1
    print("ok" if not fails else f"{fails} failure(s)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
