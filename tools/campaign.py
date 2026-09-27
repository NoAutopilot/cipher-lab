#!/usr/bin/env python3
"""CAMPAIGN.md: one continuously worked target (SPRINT.md). A campaign file has a header block and a hypothesis table.

Header lines (key: value, one per line, before the first table):
  target: <folder>   goal: <one line>   started: <UTC>   daily_budget_usd: <n>   spent_today_usd: <n>   spent_day: <YYYY-MM-DD>
  closed: <empty, or the orchestrator's one-line reason>
Table columns: id | rank | hypothesis | needs | est_usd | status | result
  needs is `nobody` (runnable now), `doc <what>` or `person <who>` (a branch that waits); status is open | running <session> | done | dropped.
Step log: lines under "## Log" appended by runners: <UTC> | <session> | <hypothesis id> | <cost> | <one-line result>.

  python3 tools/campaign.py --check                 every campaign in SPRINT.md: at least one open `nobody` row, spend within budget
  python3 tools/campaign.py --next <folder>         the top open `nobody` row (rank order) as a tab line, or "none"
  python3 tools/campaign.py --spend <folder> <usd>  add to spent_today_usd (resets when spent_day != today)
"""
import os, re, sys, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def today(): return datetime.datetime.utcnow().strftime("%Y-%m-%d")
def sprint_targets():
    t = open(os.path.join(ROOT, "SPRINT.md"), encoding="utf-8").read()
    return re.findall(r"^\| (\S+)(?: \(.*\))? \| campaign", t, re.M)  # the (trigger ... (bound to ...), :NN) note nests parentheses
def parse(folder):
    p = os.path.join(ROOT, "ciphers", folder, "CAMPAIGN.md")
    text = open(p, encoding="utf-8").read()
    hdr = dict(re.findall(r"^(\w+):\s*(.*)$", text.split("\n## ")[0], re.M))
    rows = []
    for line in text.split("\n"):
        if not re.match(r"^\| H\d+ \|", line): continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 7: continue
        rid, rank = cells[0], cells[1]
        result, status, est, needs = cells[-1], cells[-2], cells[-3], cells[-4]
        hyp = " | ".join(cells[2:-4])
        try: rows.append(dict(id=rid, rank=int(rank), hypothesis=hyp, needs=needs, est=float(re.sub(r"[^\d.]", "", est) or 0), status=status, result=result))
        except ValueError: print(f"{folder}: unparsable row {rid}")
    return p, text, hdr, rows
def check():
    ok = True
    for f in sprint_targets():
        try: p, text, hdr, rows = parse(f)
        except FileNotFoundError: print(f"{f}: no CAMPAIGN.md"); ok = False; continue
        runnable = [r for r in rows if r["status"] == "open" and r["needs"].strip() == "nobody"]
        running = [r for r in rows if r["status"].startswith("running")]
        spent = float(hdr.get("spent_today_usd", "0") or 0) if hdr.get("spent_day") == today() else 0.0
        budget = float(hdr.get("daily_budget_usd", "0") or 0)
        flags = []
        if hdr.get("closed", "").strip(): flags.append("CLOSED: " + hdr["closed"])
        if not runnable and not running: flags.append("NO RUNNABLE HYPOTHESIS (the runner must write three before it stops)"); ok = False
        if spent > budget: flags.append(f"over budget {spent:.2f}/{budget:.0f}")
        print(f"{f}: {len(rows)} hypotheses, open-runnable {len(runnable)}, running {len(running)}, done {sum(r['status']=='done' for r in rows)}, dropped {sum(r['status']=='dropped' for r in rows)}, spent today {spent:.2f}/{budget:.0f}" + ("  " + "; ".join(flags) if flags else ""))
    return ok
def nxt(folder):
    p, text, hdr, rows = parse(folder)
    if hdr.get("closed", "").strip(): print("closed: " + hdr["closed"]); return
    spent = float(hdr.get("spent_today_usd", "0") or 0) if hdr.get("spent_day") == today() else 0.0
    if spent >= float(hdr.get("daily_budget_usd", "0") or 0): print("budget spent for today"); return
    r = sorted([r for r in rows if r["status"] == "open" and r["needs"].strip() == "nobody"], key=lambda r: r["rank"])
    print("\t".join(str(r[0][k]) for k in ("id", "rank", "hypothesis", "est")) if r else "none")
def spend(folder, usd):
    p, text, hdr, rows = parse(folder)
    cur = float(hdr.get("spent_today_usd", "0") or 0) if hdr.get("spent_day") == today() else 0.0
    new = cur + float(usd)
    text = re.sub(r"^spent_today_usd:.*$", f"spent_today_usd: {new:.2f}", text, count=1, flags=re.M)
    text = re.sub(r"^spent_day:.*$", f"spent_day: {today()}", text, count=1, flags=re.M)
    open(p, "w", encoding="utf-8").write(text); print(f"spent_today_usd: {new:.2f}")
if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["--check"]: sys.exit(0 if check() else 1)
    elif a[:1] == ["--next"] and len(a) == 2: nxt(a[1])
    elif a[:1] == ["--spend"] and len(a) == 3: spend(a[1], a[2])
    else: print(__doc__)
