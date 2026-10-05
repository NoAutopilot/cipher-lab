#!/usr/bin/env python3
"""Week-on-week progress metrics from LEDGER.md and status.json (METRICS, 5 Oct 2026).

Per ISO week (Monday start) it reports:
  (a) worker spend in USD (sum of parsable Cost cells; orchestrator rows are
      shown in their own column, not counted as worker spend),
  (b) share of workers with outcome D among rows coded D, D-, X or F
      (N and Q rows are counted but left out of the denominator),
  (c) results at depth D2+ added that week (status.json `results` and
      `targets` entries with `depth` D2/D3/D4, dated by their `date` field,
      superseded entries skipped),
  (d) USD of worker spend per new D2+ result (blank when (c) is 0),
  (e) median worker cost by role class (the role cell's leading word, with
      LANE/GAPS/parent prefixes and numbers stripped; top classes only).

LEDGER.md has drifted through many column layouts (6 to 11 cells, a Session
column added on 24 Sept, account and model columns later, free text in the
cost cell). Parsing is by content, not position: the date is the first cell,
the role the second, the model the first cell naming Sonnet/Opus/Fable/Haiku,
the cost cell the first non-id cell after it (prose there counts as no cost),
the outcome the cell right after the cost cell. A row whose date, cost or outcome cannot be read is skipped
from that metric and counted in the "skipped" line; it is never guessed.

Must catch: every layout seen in the file on 5 Oct 2026, "~2 (note)" costs,
"4.35 (2.2x its cap)" costs, rows with no trailing pipe. Must NOT do: count a
cost of "session total about 110" as a worker cost (orchestrator rows go to
their own column), or invent a cost for a row whose cost cell is prose.

Usage: python3 tools/progress_metrics.py [--ledger LEDGER.md] [--status status.json]
       [--tsv] [--roles N]
Offline test: python3 tools/tests/test_progress_metrics.py
"""
import argparse
import datetime
import json
import os
import re
import statistics
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
CODES = {"D", "D-", "F", "X", "N", "Q"}
MODEL_RE = re.compile(r"\b(sonnet|opus|fable|haiku)\b", re.I)
COST_RE = re.compile(r"^~?\s*(?:usd\s*)?\$?(\d+(?:\.\d+)?)\b", re.I)
SESSION_RE = re.compile(r"session_[0-9A-Za-z]+")


def parse_date(s, default_year=2026):
    """'24 Sep', '24 Sept 2026', '3 Oct 2026', '24-25 Sep' (first day) -> date."""
    m = re.match(r"\s*(\d{1,2})(?:-\d{1,2})?\s+([A-Za-z]{3})[a-z]*\.?(?:\s+(\d{4}))?", s or "")
    if not m or m.group(2).lower() not in MONTHS:
        return None
    try:
        return datetime.date(int(m.group(3) or default_year), MONTHS[m.group(2).lower()], int(m.group(1)))
    except ValueError:
        return None


def week_of(d):
    y, w, _ = d.isocalendar()
    return "%d-W%02d" % (y, w)


def role_class(role):
    r = re.sub(r"\(.*?\)", " ", role)
    r = re.sub(r"^(lane\s+\S+\s+|parent\s+worker\s+|acct\d\s+|account[- ]\d\s+)", "", r.strip(), flags=re.I)
    w = re.split(r"[\s:,/]+", r.strip())
    w = w[0] if w and w[0] else "?"
    w = re.sub(r"[\d.]+$", "", w).rstrip("-_") or w
    return w.upper()[:20]


def is_orchestrator(role):
    return bool(re.match(r"\s*(orchestrator|parent orchestrator|lane \S+ orchestrator\b)", role, re.I)) \
        or re.search(r"\borchestrator (wake|self|row)", role, re.I) is not None


def parse_row(line):
    """Return dict(date, role, cost, outcome, orch) with None for unreadable fields, or None if not a data row."""
    if not line.startswith("|"):
        return None
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) < 4 or set(cells[0]) <= set("-: ") or cells[0].lower() == "date":
        return None
    date = parse_date(cells[0])
    role = cells[1]
    start = 2
    for i in range(2, len(cells)):
        if MODEL_RE.search(cells[i]) and len(cells[i]) < 30:
            start = i + 1
            break
    cost = outcome = None
    for i in range(start, len(cells)):
        if SESSION_RE.fullmatch(cells[i]) or re.fullmatch(r"(account|acct)[- ]?\d+|owner|ytbiz", cells[i], re.I):
            continue
        m = COST_RE.match(cells[i])
        cost = float(m.group(1)) if m else None
        if i + 1 < len(cells):
            tok = cells[i + 1].split()[0] if cells[i + 1].split() else ""
            tok = tok.strip("*").rstrip(".,;")
            outcome = tok if tok in CODES else None
        break  # first non-id cell after the model is the cost cell (prose there = no cost); outcome follows it
    return {"date": date, "role": role, "cost": cost, "outcome": outcome, "orch": is_orchestrator(role)}


def load_ledger(path):
    rows, skipped = [], Counter()
    with open(path, encoding="utf-8") as f:
        for line in f:
            r = parse_row(line)
            if r is None:
                continue
            if r["date"] is None:
                skipped["date"] += 1
                continue
            if r["cost"] is None:
                skipped["cost"] += 1
            if r["outcome"] is None:
                skipped["outcome"] += 1
            rows.append(r)
    return rows, skipped


def load_results(path):
    with open(path, encoding="utf-8") as f:
        d = json.load(f)
    out, skipped = [], 0
    for x in (d.get("results") or []) + (d.get("targets") or []):
        if not isinstance(x, dict) or x.get("superseded_by"):
            continue
        dep = str(x.get("depth") or "")
        if dep not in ("D2", "D3", "D4"):
            continue
        dt = parse_date(str(x.get("date") or ""))
        if dt is None:
            skipped += 1
            continue
        out.append({"date": dt, "depth": dep})
    return out, skipped


def compute(rows, results, n_roles=4):
    weeks = defaultdict(lambda: {"spend": 0.0, "orch": 0.0, "codes": Counter(), "d2": 0, "costs": defaultdict(list)})
    for r in rows:
        w = weeks[week_of(r["date"])]
        if r["orch"]:
            if r["cost"] is not None:
                w["orch"] += r["cost"]
            continue
        if r["cost"] is not None:
            w["spend"] += r["cost"]
            w["costs"][role_class(r["role"])].append(r["cost"])
        if r["outcome"]:
            w["codes"][r["outcome"]] += 1
    for x in results:
        weeks[week_of(x["date"])]["d2"] += 1
    out = []
    for wk in sorted(weeks):
        w = weeks[wk]
        c = w["codes"]
        denom = c["D"] + c["D-"] + c["X"] + c["F"]
        allcost = [v for vs in w["costs"].values() for v in vs]
        top = sorted(w["costs"].items(), key=lambda kv: -len(kv[1]))[:n_roles]
        out.append({
            "week": wk,
            "workers": sum(len(v) for v in w["costs"].values()),
            "spend": round(w["spend"], 2),
            "orch_spend": round(w["orch"], 2),
            "share_d": round(c["D"] / denom, 3) if denom else None,
            "d_denom": denom,
            "codes": " ".join("%s:%d" % (k, c[k]) for k in ["D", "D-", "X", "F", "N", "Q"] if c[k]),
            "d2_new": w["d2"],
            "usd_per_d2": round(w["spend"] / w["d2"], 2) if w["d2"] else None,
            "median_cost": round(statistics.median(allcost), 2) if allcost else None,
            "median_by_role": "; ".join("%s %.2f (n=%d)" % (k, statistics.median(v), len(v)) for k, v in top),
        })
    return out


COLS = ["week", "workers", "spend", "orch_spend", "share_d", "d_denom", "codes", "d2_new", "usd_per_d2",
        "median_cost", "median_by_role"]


def fmt(v, col=""):
    if v is None:
        return ""
    if isinstance(v, float):
        return ("%.0f%%" % (v * 100)) if col == "share_d" else "%.2f" % v
    return str(v)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ledger", default=os.path.join(ROOT, "LEDGER.md"))
    ap.add_argument("--status", default=os.path.join(ROOT, "status.json"))
    ap.add_argument("--tsv", action="store_true", help="tab-separated output instead of a markdown table")
    ap.add_argument("--roles", type=int, default=4, help="role classes shown in median_by_role (default 4)")
    a = ap.parse_args(argv)
    rows, skipped = load_ledger(a.ledger)
    results, rskip = load_results(a.status)
    table = compute(rows, results, a.roles)
    if a.tsv:
        print("\t".join(COLS))
        for t in table:
            print("\t".join(fmt(t[c], c) for c in COLS))
    else:
        print("| " + " | ".join(COLS) + " |")
        print("|" + "---|" * len(COLS))
        for t in table:
            print("| " + " | ".join(fmt(t[c], c) for c in COLS) + " |")
        print()
    print("rows parsed: %d; skipped: date %d, cost %d (not in spend), outcome %d (not in share_d); "
          "D2+ results without a date: %d" % (len(rows), skipped["date"], skipped["cost"], skipped["outcome"], rskip),
          file=sys.stdout if not a.tsv else sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
