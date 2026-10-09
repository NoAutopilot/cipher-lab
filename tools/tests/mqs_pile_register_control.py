#!/usr/bin/env python3
"""Known-answer control for tools/pile_register.py --refs-scan (MQS-PILE-REGISTER, 9 Oct 2026; preregistered in
tools/tests/PREREG-MQS-PILE-REGISTER.md before this was run).

Edition: Bowdoin and Temple Papers II (MHS Collections 7th ser. vol. VI, 1907), IA OCR on disk at
ciphers/armstrong-madison-1808/sources/h75/bt2_djvu.txt. Ground truth: every 'A TO B.' header followed within three
non-blank lines by a date line (the tool's own parse_dateline). Held out: every letter A -> B whose reply B -> A is printed within
60 days. The scan runs on the held letters' dates (window 0). Recall: share of held-out dates within +-1 day of a
resolved reference. Null: held-out dates moved by a uniform offset in [-90,-7] u [7,90] days, seed 0, 1000 draws.

Usage: python3 tools/tests/mqs_pile_register_control.py [--edition PATH] [--json OUT]
"""
import argparse
import json
import random
import re
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import pile_register as pr  # noqa: E402

EDITION = HERE.parents[1] / "ciphers" / "armstrong-madison-1808" / "sources" / "h75" / "bt2_djvu.txt"
HEADER = re.compile(r"^\s*([A-Z][A-Z .’'&-]{2,40}?)\s+TO\s+([A-Z][A-Z .’'&-]{2,50}?)\.?\s*$")


def ground_truth(text):
    lines = text.splitlines()
    out = []
    for i, l in enumerate(lines):
        m = HEADER.match(l)
        if not m:
            continue
        nxt = [j for j in range(i + 1, min(i + 12, len(lines))) if lines[j].strip()][:3]
        for j in nxt:
            d = pr.parse_dateline(lines[j])
            if d and 1700 <= d.year <= 1830:
                out.append({"from": m.group(1).strip(), "to": m.group(2).strip(), "date": d, "line": j + 1})
                break
    return out


def recall(targets, resolved, tol=1):
    if not targets:
        return 0.0
    return sum(any(abs((t - r).days) <= tol for r in resolved) for t in targets) / len(targets)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--edition", default=str(EDITION))
    ap.add_argument("--json")
    a = ap.parse_args(argv)
    text = Path(a.edition).read_text(encoding="utf-8", errors="replace")
    G = ground_truth(text)
    K = [x for x in G if any(y["from"] == x["to"] and y["to"] == x["from"] and
                             0 < (y["date"] - x["date"]).days <= 60 for y in G)]
    kset = {id(x) for x in K}
    held = [x for x in G if id(x) not in kset]
    held_dates = [x["date"] for x in held]
    kd = [x["date"] for x in K]
    # the scan sees only the held letters' segments: window 0 on held dates, minus any held-out letter's own segment
    # that shares a held date (none expected; counted below)
    shared = sum(d in set(held_dates) for d in kd)
    leads = pr.scan_refs(text, held_dates, window=0, tol=1)
    resolved = [pr.dt.date.fromisoformat(x["refers_to"]) for x in leads]
    real = recall(kd, resolved)
    rng = random.Random(0)
    offs = [o for o in range(-90, 91) if abs(o) >= 7]
    null = [recall([d + pr.dt.timedelta(days=rng.choice(offs)) for d in kd], resolved) for _ in range(1000)]
    null.sort()
    p95 = null[int(0.95 * len(null)) - 1]
    mean = statistics.mean(null)
    gate = real >= 0.25 and real > p95 and real - mean >= 0.15
    res = {"ground_truth_letters": len(G), "held_out_K": len(K), "held": len(held), "held_out_sharing_a_held_date": shared,
           "references_resolved": len(leads), "how": {h: sum(x["how"] == h for x in leads) for h in
                                                      ("explicit", "instant", "ult", "inferred", "today")},
           "recall": round(real, 3), "null_mean": round(mean, 3), "null_p95": round(p95, 3),
           "gate": "PASS" if gate else "FAIL"}
    print(json.dumps(res, indent=1))
    if a.json:
        Path(a.json).write_text(json.dumps(res, indent=1) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
