#!/usr/bin/env python3
"""Learning-loop metrics for a dated window (16 Oct 2026, mission "Close the Learning Loop", Phase 4).

Four measures the owner asked to compare over a seven-day pilot against a documented baseline, each computed from
records that already exist (LEDGER.md, RETRO-PROPOSALS.tsv, status.json), never from a model's impression:

  1. repeated operational failures -- LEDGER.md rows in the window whose Outcome/Lesson text carries a shape already
     named by a lesson or retrospective: over cap (an explicit "<n>x ... cap" ratio above 1), no repository
     (source_url), duplicate / already done / stood down, brief error, a non-standard outcome code; count and USD;
  2. retrospective proposals decided in the window (RETRO-PROPOSALS.tsv decided_on): applied / declined / open, and
     how many applied rows name a test file (tools/tests/...) in their evidence;
  3. research effort on unsuccessful repeated approaches -- rows whose text says non-test, untested-by-this-tool,
     third attempt, control FAIL or control below gate (count, USD), and targets with three or more N rows in the
     window (the same slug in the Role cell);
  4. verified solves -- status.json results with novelty N3+ and depth D2+ whose depth_date (or date) falls in the
     window, against worker USD in the window (USD per solve; "no solve" when zero -- never a claimed rate).

Row parsing reuses tools/progress_metrics.py (parse_row, load_ledger, load_results), so a layout it cannot read is
skipped and counted, never guessed. Operational measures (1-3) and the solving measure (4) are printed apart: an
operational improvement is not evidence of solving effectiveness.

Usage: tools/learning_metrics.py --from 2026-10-09 --to 2026-10-15 [--json OUT.json] [--compare BASE.json]
       (--to is inclusive). --compare prints each measure beside the baseline file's value.
Offline test: python3 tools/tests/test_learning_metrics.py
"""
import argparse
import csv
import datetime
import json
import os
import re
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import progress_metrics as pm  # noqa: E402

OVER_CAP_RE = re.compile(r'(\d+(?:\.\d+)?)\s*x\s+(?:the\s+|its\s+|a\s+)?(?:\$|USD\s*)?(?:\d+(?:\.\d+)?\s*)?cap', re.I)
SHAPES = {
    "no_repository": re.compile(r'source_url|no repository|without the repository|no repo attached', re.I),
    "duplicate_dispatch": re.compile(r'\bduplicate\b|already (?:done|run|read|transcribed)|stood down|duplicates finished work', re.I),
    "brief_error": re.compile(r"brief(?:'s)? error|the brief's own error|brief mis-?specified", re.I),
    "scratchpad_loss": re.compile(r'scratchpad.*(lost|loss|not committed)|lost .* scratchpad', re.I),
}
REPEAT_RE = re.compile(r'non-test|untested[- ]by[- ]this[- ]tool|third attempt|control FAIL|control below gate|below (?:its|the) gate', re.I)
SLUG_RE = re.compile(r'\b([a-z0-9]+(?:-[a-z0-9]+){1,6}-\d{3,4}(?:-[a-z0-9]+)?|[a-z]{2,8}\d{3,5}-[a-z0-9-]+)\b')
VALID = {"D", "D-", "F", "X", "N", "Q"}


def parse_day(s):
    s = (s or "").strip()
    m = re.match(r'(\d{4})-(\d{2})-(\d{2})', s)
    if m:
        return datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    d = pm.parse_date(s)
    return d if isinstance(d, datetime.date) else None


def in_window(d, start, end):
    return d is not None and start <= d <= end


CRYPTANALYSIS_RE = re.compile(r'family_run|homophonic|anneal|wordcode|nomenclator solver|syllabary|\bmasc\b|vigenere|running[_ -]key|hillclimb|ciphertext-only|key_repair|lattice', re.I)


def dedupe(win):
    """A session id written twice (a running/done pair, a self-ledger row written twice with two costs, a twin for one job)
    double-counts in any total: 38 such ids on 16 Oct 2026, about USD 216 (learning/LEDGER-HISTORY-AUDIT-2026-10-16.md). Keep
    the LAST row per session id that carries a numeric cost; rows without an id are kept as they are."""
    keep = {}
    out = []
    for r in win:
        sid = r.get("session")
        if sid:
            keep[sid] = r if (r.get("cost") is not None or sid not in keep) else keep[sid]
        else:
            out.append(r)
    dropped = sum(1 for r in win if r.get("session")) - len(keep)
    return out + list(keep.values()), dropped


def compute(rows, results, register_rows, start, end):
    win_all = [r for r in rows if r.get("date") and in_window(r["date"], start, end)]
    win, dropped = dedupe(win_all)
    usd_all = sum(r["cost"] for r in win_all if r.get("cost") is not None and not pm.is_orchestrator(r.get("role", "")))
    usd = sum(r["cost"] for r in win if r.get("cost") is not None and not pm.is_orchestrator(r.get("role", "")))
    crypt_usd = sum(r["cost"] for r in win if r.get("cost") is not None and not pm.is_orchestrator(r.get("role", "")) and CRYPTANALYSIS_RE.search(r.get("role", "") + " " + r.get("lesson", "")[:200]))
    op = Counter()
    op_usd = Counter()
    repeat_n = 0
    repeat_usd = 0.0
    n_by_slug = Counter()
    for r in win:
        text = f"{r.get('outcome', '')} {r.get('lesson', '')}"
        cost = r.get("cost") or 0.0
        m = OVER_CAP_RE.search(text)
        if m and float(m.group(1)) > 1.0:
            op["over_cap"] += 1
            op_usd["over_cap"] += cost
        for k, rx in SHAPES.items():
            if rx.search(text):
                op[k] += 1
                op_usd[k] += cost
        if r.get("outcome_code") and r["outcome_code"] not in VALID:
            op["non_standard_code"] += 1
            op_usd["non_standard_code"] += cost
        if REPEAT_RE.search(text):
            repeat_n += 1
            repeat_usd += cost
        if r.get("outcome_code") == "N":
            sm = SLUG_RE.search(r.get("role", ""))
            if sm:
                n_by_slug[sm.group(1)] += 1
    repeated_targets = {s: n for s, n in n_by_slug.items() if n >= 3}
    reg = Counter()
    reg_tested = 0
    for rr in register_rows:
        d = parse_day(rr.get("decided_on", ""))
        if not in_window(d, start, end):
            continue
        st = (rr.get("status") or "").strip().lower()
        reg[st] += 1
        if st == "applied" and "tools/tests/" in (rr.get("evidence") or ""):
            reg_tested += 1
    solves = []
    by_key = Counter()
    for res in results:
        nov = str(res.get("plaintext_novelty") or res.get("novelty") or "")
        depth = str(res.get("depth") or "")
        if res.get("superseded_by"):
            continue
        if not re.match(r'N[345]', nov) or depth[:2] not in ("D2", "D3", "D4"):
            continue
        d = parse_day(res.get("depth_date") or "") or parse_day(res.get("date") or "")
        if in_window(d, start, end):
            solves.append(res.get("title", "")[:70])
            key = str(res.get("key") or "unrecorded").split()[0].strip(",;")
            by_key[key] += 1
    return {
        "window": [start.isoformat(), end.isoformat()],
        "rows": len(win_all),
        "worker_usd": round(usd, 2),
        "double_written_rows_dropped": dropped,
        "double_counted_usd_removed": round(usd_all - usd, 2),
        "cryptanalysis_share": {"usd": round(crypt_usd, 2), "share": (round(crypt_usd / usd, 3) if usd else 0.0), "bound": 0.15},
        "operational": {k: {"rows": op[k], "usd": round(op_usd[k], 2)} for k in ("over_cap", "no_repository", "duplicate_dispatch", "brief_error", "scratchpad_loss", "non_standard_code")},
        "retro_proposals": {"applied": reg["applied"], "declined": reg["declined"], "partial": reg["partial"], "open": reg["open"], "applied_with_test": reg_tested},
        "repeated_approaches": {"rows": repeat_n, "usd": round(repeat_usd, 2), "targets_with_3plus_N": len(repeated_targets), "targets": dict(sorted(repeated_targets.items(), key=lambda x: -x[1])[:10])},
        "solves": {"n3_d2_new": len(solves), "by_key_source": dict(by_key), "ours_key": by_key.get("ours", 0), "titles": solves,
                   "usd_per_solve": (round(usd / len(solves), 2) if solves else "no solve"),
                   "usd_per_ours_key_solve": (round(usd / by_key["ours"], 2) if by_key.get("ours") else "no solve with our own key")},
    }


def load_rows(path):
    """progress_metrics.parse_row for date/role/cost/outcome, plus the row's own text (Outcome and Lesson cells are
    where the repeat shapes are written) -- progress_metrics keeps only the code token."""
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            r = pm.parse_row(line)
            if r is None or r["date"] is None:
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            r["outcome_code"] = r["outcome"]
            r["lesson"] = " | ".join(cells[2:])
            sm = next((c for c in cells if pm.SESSION_RE.fullmatch(c)), None)
            r["session"] = sm
            rows.append(r)
    return rows


def load_register(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def load_results(path):
    if not os.path.exists(path):
        return []
    d = json.load(open(path, encoding="utf-8"))
    return d.get("results", []) if isinstance(d, dict) else []


def render(m, base=None):
    def cmp(key_path, v):
        if base is None:
            return ""
        b = base
        for k in key_path:
            b = b.get(k, {}) if isinstance(b, dict) else {}
        return f"  (baseline {b})" if b != {} else ""
    out = [f"Learning-loop metrics {m['window'][0]} .. {m['window'][1]}: {m['rows']} ledger rows, worker USD {m['worker_usd']} "
           f"(after dropping {m['double_written_rows_dropped']} double-written session rows, USD {m['double_counted_usd_removed']})",
           f"Independent cryptanalysis share of worker spend: {m['cryptanalysis_share']['share']:.1%} (USD {m['cryptanalysis_share']['usd']}; bound {m['cryptanalysis_share']['bound']:.0%}, owner 16 Oct 2026)"]
    out.append("Operational (repeated failure shapes):")
    for k, v in m["operational"].items():
        out.append(f"  {k:20} rows {v['rows']:4d}  USD {v['usd']:8.2f}{cmp(('operational', k), v)}")
    rp = m["retro_proposals"]
    out.append(f"Retrospective proposals decided in window: applied {rp['applied']} (with a test {rp['applied_with_test']}), declined {rp['declined']}, partial {rp['partial']}, open {rp['open']}{cmp(('retro_proposals',), rp)}")
    ra = m["repeated_approaches"]
    out.append(f"Research effort on repeated/unsuccessful approaches: rows {ra['rows']}, USD {ra['usd']}, targets with 3+ N rows {ra['targets_with_3plus_N']} {ra['targets']}{cmp(('repeated_approaches',), ra)}")
    s = m["solves"]
    out.append(f"Solving (kept apart from the above): new N3+/D2+ results {s['n3_d2_new']} by key source {s['by_key_source']}; "
               f"USD per result {s['usd_per_solve']}; with OUR OWN key (cryptanalysis or our alignment, the North Star's nearest honest figure) "
               f"{s['ours_key']}, USD per such solve {s['usd_per_ours_key_solve']}{cmp(('solves',), s)}")
    for t in s["titles"][:10]:
        out.append(f"  - {t}")
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--from", dest="start", required=True)
    ap.add_argument("--to", dest="end", required=True)
    ap.add_argument("--ledger", default=os.path.join(ROOT, "LEDGER.md"))
    ap.add_argument("--status", default=os.path.join(ROOT, "status.json"))
    ap.add_argument("--register", default=os.path.join(ROOT, "RETRO-PROPOSALS.tsv"))
    ap.add_argument("--json", dest="out")
    ap.add_argument("--compare", dest="base")
    a = ap.parse_args(argv)
    start, end = parse_day(a.start), parse_day(a.end)
    if not start or not end:
        ap.error("--from/--to must be YYYY-MM-DD")
    rows = load_rows(a.ledger)
    m = compute(rows, load_results(a.status), load_register(a.register), start, end)
    base = json.load(open(a.base, encoding="utf-8")) if a.base else None
    print(render(m, base))
    if a.out:
        json.dump(m, open(a.out, "w", encoding="utf-8"), indent=1)
        print(f"written {a.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
