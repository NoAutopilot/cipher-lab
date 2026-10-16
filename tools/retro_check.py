#!/usr/bin/env python3
"""Close the retrospective loop (16 Oct 2026, mission "Close the Learning Loop").

Thirty retrospectives (RETRO-*.md, 23 Sept to 12 Oct 2026) wrote about 130 proposals. An audit on 16 Oct found the
applied ones landed only when a RETRO-APPLY worker was spawned the same day; after 28 Sept nobody spawned one, and the
same three tool fixes were proposed in three consecutive retrospectives (near_check's date-only cell: 28 P3, 10-05 P2,
10-12 P4; the model-tier exception: 10-05 P1, 10-12 P5; the source_url spawn gate: 25l P3, 10-12 P3) while the
retrospective brief itself says "the orchestrator applies the safe ones". A proposal only a retrospective remembers is
not a loop. This tool reads RETRO-PROPOSALS.tsv (retro, proposal, asks_for, status, evidence, decided_on, by) and the
RETRO-*.md files and reports:

  (a) OPEN proposals older than --max-open-days (default 7) -- the parent applies (briefs/tools/workflows only) or
      escalates each one as an ASKS row in the same check-in;
  (b) a proposal id present in a RETRO-*.md "Proposed changes" section but absent from the register (unregistered);
  (c) the newest RETRO-*.md older than --max-retro-days (default 8): the weekly cadence has lapsed;
  (d) LEDGER.md rows and worker spend since the newest RETRO-*.md's date, against CLAUDE.md's written trigger
      (12 rows / USD 60) -- printed for the record; at the volumes of Oct 2026 (about 1,600 rows a week) the written
      trigger would fire forty times a week, so (c) is the gate and (d) is the evidence for the owner to re-set it.

Exit 0 clean; 2 when (a), (b) or (c) fires (a check-in finding, the same way near_check.py's warnings exit 2).

Usage: tools/retro_check.py [--register RETRO-PROPOSALS.tsv] [--retro-dir .] [--ledger LEDGER.md]
                            [--now "16 Oct 2026"] [--max-open-days 7] [--max-retro-days 8]
Offline test: python3 tools/tests/test_retro_check.py
"""
import argparse
import csv
import datetime
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MONTHS = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
PROPOSAL_RE = re.compile(r'^\*\*(P\d+|rec\d+)\.', re.M)
STATUSES = ("open", "applied", "partial", "declined")


def retro_date(path):
    m = re.search(r'RETRO-(\d{4})-(\d{2})-(\d{2})', os.path.basename(path))
    return datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3))) if m else None


def parse_day(s):
    s = s.strip()
    m = re.match(r'(\d{4})-(\d{2})-(\d{2})', s)
    if m:
        return datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    m = re.match(r'(\d{1,2})\s+([A-Za-z]{3})[a-z]*\.?\s+(\d{4})', s)
    if m and m.group(2).lower() in MONTHS:
        return datetime.date(int(m.group(3)), MONTHS[m.group(2).lower()], int(m.group(1)))
    return None


def load_register(path):
    with open(path, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    for r in rows:
        r["status"] = (r.get("status") or "").strip().lower()
    return rows


def proposals_in_retros(retro_dir, since=None):
    """{(retro_stem, proposal_id)} for every '**Pn.**' heading in a RETRO file's proposals section."""
    found = set()
    for path in sorted(glob.glob(os.path.join(retro_dir, "RETRO-*.md"))):
        d = retro_date(path)
        if since and d and d < since:
            continue
        stem = os.path.basename(path)[:-3]
        text = open(path, encoding="utf-8").read()
        for pid in PROPOSAL_RE.findall(text):
            found.add((stem, pid))
    return found


CRITICAL = {
    "over_claim_X": lambda code, text: code == "X",
    "no_repository": lambda code, text: bool(re.search(r'source_url|no repository|without the repository', text, re.I)),
    "gate_found_blind": lambda code, text: bool(re.search(r'(gate|check|tool).{0,40}\b(blind|silently (?:skipp|miss)|never (?:saw|reach))', text, re.I)),
}
OVER2X = re.compile(r'(\d+(?:\.\d+)?)\s*x\s+(?:the\s+|its\s+|a\s+)?(?:\$|USD\s*)?(?:\d+(?:\.\d+)?\s*)?cap', re.I)


def critical_since(ledger_path, since, register_rows=()):
    """Exception-review triggers (owner, 16 Oct 2026, ASKS 171): rows dated on/after `since` that carry a critical shape --
    an X row, a no-repository death, a gate found blind -- plus a count of rows at 2x their cap or more (three or more
    trigger), and a registered lesson broken again (an applied register row whose asks_for words recur in a later Lesson)."""
    hits = {k: [] for k in CRITICAL}
    hits["over_2x_cap"] = []
    lines = open(ledger_path, encoding="utf-8").read().split("\n")
    for i, line in enumerate(lines, 1):
        if not line.startswith("| ") or line.startswith("| Date"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        d = parse_day(cells[0]) if cells else None
        if d is None or d < since:
            continue
        text = " | ".join(cells[2:])
        code = ""
        for c in cells[3:8]:
            tok = c.split()[0].strip("*.,;") if c.split() else ""
            if tok in ("D", "D-", "F", "X", "N", "Q"):
                code = tok
                break
        for k, f in CRITICAL.items():
            if f(code, text):
                hits[k].append(i)
        m = OVER2X.search(text)
        if m and float(m.group(1)) >= 2.0:
            hits["over_2x_cap"].append(i)
    return hits


def ledger_since(ledger_path, since):
    """(rows, usd) of LEDGER.md data rows dated on or after `since`."""
    rows = 0
    usd = 0.0
    for line in open(ledger_path, encoding="utf-8"):
        if not line.startswith("| ") or line.startswith("| Date"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        d = parse_day(cells[0]) if cells else None
        if d is None or d < since:
            continue
        rows += 1
        for c in cells[2:7]:
            m = re.match(r'^~?(\d+(?:\.\d+)?)(\s|\(|$)', c)
            if m:
                usd += float(m.group(1))
                break
    return rows, usd


def run(register, retro_dir, ledger, now, max_open_days, max_retro_days, register_since=None):
    findings = []
    rows = load_register(register)
    for r in rows:
        if r["status"] not in STATUSES:
            findings.append(f"(b) {r['retro']} {r['proposal']}: status {r['status']!r} is not one of {STATUSES}")
    for r in rows:
        if r["status"] == "open":
            d = parse_day(r.get("decided_on") or "") or retro_date(r["retro"] + ".md")
            if d and (now - d).days > max_open_days:
                findings.append(f"(a) OPEN {(now - d).days} days: {r['retro']} {r['proposal']} -- {r['asks_for']} (apply or escalate as an ASKS row)")
    registered = {(r["retro"], r["proposal"]) for r in rows}
    for stem, pid in sorted(proposals_in_retros(retro_dir, register_since)):
        if (stem, pid) not in registered:
            findings.append(f"(b) unregistered: {stem} {pid} has no RETRO-PROPOSALS.tsv row")
    retros = [p for p in glob.glob(os.path.join(retro_dir, "RETRO-*.md")) if retro_date(p)]
    newest = max((retro_date(p) for p in retros), default=None)
    info = []
    if newest:
        age = (now - newest).days
        if age > max_retro_days:
            findings.append(f"(c) newest retrospective is {age} days old ({newest.isoformat()}); the weekly cadence has lapsed")
        if os.path.exists(ledger):
            n, usd = ledger_since(ledger, newest)
            info.append(f"(d) since {newest.isoformat()}: {n} LEDGER.md rows, about USD {usd:.0f} (cadence: weekly, owner 16 Oct 2026)")
            last_review = max([newest] + [parse_day(r.get("decided_on") or "") for r in rows if (r.get("proposal") or "").startswith("EXC") and parse_day(r.get("decided_on") or "")])
            hits = critical_since(ledger, last_review)
            due = [k for k, v in hits.items() if v and (k != "over_2x_cap" or len(v) >= 3)]
            if due:
                findings.append("(e) exception review due since " + last_review.isoformat() + ": " +
                                "; ".join(f"{k} rows {hits[k][:6]}{'...' if len(hits[k]) > 6 else ''}" for k in due) +
                                " -- run the retrospective brief's 'Exception review' (cap USD 3) and register it as an EXC-<date> row")
    return findings, info


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--register", default=os.path.join(ROOT, "RETRO-PROPOSALS.tsv"))
    ap.add_argument("--retro-dir", default=ROOT)
    ap.add_argument("--ledger", default=os.path.join(ROOT, "LEDGER.md"))
    ap.add_argument("--now", default=None, help='e.g. "16 Oct 2026" or 2026-10-16 (default: today UTC)')
    ap.add_argument("--max-open-days", type=int, default=7)
    ap.add_argument("--max-retro-days", type=int, default=8)
    ap.add_argument("--register-since", default="2026-09-28",
                    help="only RETRO files dated on/after this need every proposal registered (older ones were audited in bulk on 16 Oct 2026)")
    a = ap.parse_args(argv)
    now = parse_day(a.now) if a.now else datetime.datetime.now(datetime.timezone.utc).date()
    if now is None:
        ap.error(f"could not parse --now {a.now!r}")
    since = parse_day(a.register_since) if a.register_since else None
    findings, info = run(a.register, a.retro_dir, a.ledger, now, a.max_open_days, a.max_retro_days, since)
    for line in info:
        print(line)
    for line in findings:
        print(line)
    if findings:
        print(f"retro_check: {len(findings)} finding(s) -- apply, escalate or decide each in this check-in")
        return 2
    print("retro_check: ok -- no open proposal past the window, every proposal registered, cadence kept")
    return 0


if __name__ == "__main__":
    sys.exit(main())
