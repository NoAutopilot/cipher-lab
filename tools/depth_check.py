#!/usr/bin/env python3
"""Reading-depth gate: a unique solve is a verifier class of N3 or better AND a reading depth of D2 or better
(owner's decision, 4 Oct 2026; scale and evidence in research/DECIPHERMENT-STANDARDS-2026-10-04.md; CLAUDE.md rule 4a).

    python3 tools/depth_check.py                 # check status.json, print the headline counts by depth
    python3 tools/depth_check.py --status FILE
    python3 tools/depth_check.py --strict        # also fail on legacy counted results that carry no depth yet

Why it exists. The N-class says how sure we are nobody read the text before; it says nothing about how much of the
text we read. On 4 Oct 2026 three of four N3-N4 classes on Birago leaves (fr.3252 f.47r, fr.3251 f.144r, f.168) had
isolated letters or function words behind them and no statement a reader could quote (LANE-A3V, AUDIT 3 / AUDIT 13).

Depth, set per item by a verifier (never the solver), lowered on any revision:
    D0  a candidate key ranks first; nothing reads                     outward: none
    D1  scattered words, no stretch above the authentication distance  outward: "fragments read"
    D2  >=1 clause above it (or a code value reading in 2 contexts); the verifier wrote one true sentence about the
        content                                                         outward: "partially deciphered (about N%)"
    D3  >=80% of cipher tokens H/C/S, gaps mostly names/codes, external check or AD + matched control
                                                                        outward: "largely deciphered (about N%)"
    D4  every cipher-letter token H/C/S, residue = listed name/code groups only, non-statistical external check and a
        fresh rule-7 re-derivation                                      outward: "deciphered" (+ "N name codes unidentified")

What it checks on each status.json result:
  * `depth`, when present, is one of D0-D4; `decode_status`, when present, matches the depth (D0-1 Non-decrypted,
    D2-3 Partially decrypted, D4 Decrypted); D2+ carries `depth_sentence` (the verifier's one true sentence); D3+
    carries `depth_check` other than none/auth-distance-only for D4; `depth_pct` is 0-100 and >= 80 for D3/D4.
  * A COUNTED result (two audits, class N3+, claim_scope recovered-passages or completed-reading, not superseded)
    dated 4 Oct 2026 or later must carry a depth; one below D2 is reported "class without a reading, not counted".

What it must NOT block (offline tests in tools/tests/test_depth_check.py):
  * results that are not counted (N0-N2, one audit, datasets, catches, negatives, corrections, key-to-known-text):
    depth is optional there and never makes the check fail;
  * legacy counted results dated before 4 Oct 2026 without a depth: listed as "ungraded (legacy)", exit 0 unless
    --strict, so the re-grade can land result by result.

Exit 0 when clean, 1 on any FAIL.
"""
import argparse
import json
import re
import sys
from datetime import date

DEPTHS = ["D0", "D1", "D2", "D3", "D4"]
DECODE = {"D0": "Non-decrypted", "D1": "Non-decrypted", "D2": "Partially decrypted",
          "D3": "Partially decrypted", "D4": "Decrypted"}
COUNTED_SCOPES = {"recovered-passages", "completed-reading"}
CUTOFF = date(2026, 10, 4)
MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}


def parse_date(s):
    m = re.match(r"\s*(\d{1,2})\s+([A-Za-z]{3})[a-z]*\.?\s+(\d{4})", s or "")
    if m:
        return date(int(m.group(3)), MONTHS.get(m.group(2).lower(), 1), int(m.group(1)))
    m = re.match(r"\s*(\d{4})-(\d{2})-(\d{2})", s or "")
    if m:
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    return None


def nclass(r):
    for k in ("novelty", "plaintext_novelty", "grade"):
        m = re.search(r"\bN([0-5])\b", str(r.get(k, "")))
        if m:
            return int(m.group(1))
    return None


def is_counted(r):
    n = nclass(r)
    return (r.get("audit_status") == "two audits" and n is not None and n >= 3
            and r.get("claim_scope") in COUNTED_SCOPES and not r.get("superseded_by"))


def check(results, strict=False):
    fails, notes = [], []
    tally = {d: 0 for d in DEPTHS}
    ungraded = 0
    for i, r in enumerate(results):
        name = (r.get("title") or r.get("document_id") or f"result {i}")[:70]
        d = r.get("depth")
        if d is not None:
            if d not in DEPTHS:
                fails.append(f"{name}: depth {d!r} not in D0-D4")
                continue
            ds = r.get("decode_status")
            if ds is not None and ds != DECODE[d]:
                fails.append(f"{name}: decode_status {ds!r} does not match {d} ({DECODE[d]})")
            pct = r.get("depth_pct")
            if pct is not None and not (0 <= float(pct) <= 100):
                fails.append(f"{name}: depth_pct {pct} outside 0-100")
            if d in ("D2", "D3", "D4") and not str(r.get("depth_sentence", "")).strip():
                fails.append(f"{name}: {d} without depth_sentence (the verifier's one true sentence)")
            if d in ("D3", "D4"):
                if pct is None or float(pct) < 80:
                    fails.append(f"{name}: {d} needs depth_pct >= 80 (got {pct})")
                chk = r.get("depth_check", "none")
                if chk in ("", "none") or (d == "D4" and chk == "auth-distance"):
                    fails.append(f"{name}: {d} needs an external depth_check (got {chk!r})")
        if not is_counted(r):
            continue
        if d is None:
            dt = parse_date(r.get("date", ""))
            if dt is not None and dt >= CUTOFF:
                fails.append(f"{name}: counted result dated {r.get('date')} carries no depth")
            else:
                ungraded += 1
                notes.append(f"ungraded (legacy): {name}")
                if strict:
                    fails.append(f"{name}: legacy counted result without depth (--strict)")
            continue
        tally[d] += 1
        if d in ("D0", "D1"):
            notes.append(f"class without a reading, not counted: {name} ({d})")
    solves = tally["D2"] + tally["D3"] + tally["D4"]
    return fails, notes, tally, ungraded, solves


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--status", default="status.json")
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args(argv)
    results = json.load(open(a.status)).get("results", [])
    fails, notes, tally, ungraded, solves = check(results, a.strict)
    for n in notes:
        print("note:", n)
    for f in fails:
        print("FAIL:", f)
    print(f"unique solves (N3+ and D2+): {solves} -- D4 {tally['D4']}, D3 {tally['D3']}, D2 {tally['D2']}; "
          f"not counted D0/D1: {tally['D0'] + tally['D1']}; legacy ungraded: {ungraded}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
