#!/usr/bin/env python3
"""WORK-QUEUE.tsv: the single orchestrator's job list, pulled by the dispatcher routine on the other account.

Columns: job_id, account (owner|other|third), brief, model, cap_usd, box_min, status, added, note.
status is one of: queued | claimed <session_id> <UTC> | done <UTC> | bounced <UTC> <reason>.

  python3 tools/work_queue.py --check                      validate the file (exit 1 on a malformed row)
  python3 tools/work_queue.py --next --account other       print the queued rows for that account, oldest first
  python3 tools/work_queue.py --claim JOB --session ID     mark a row claimed (fails if not queued)
  python3 tools/work_queue.py --done JOB [--note TEXT]     mark a row done
  python3 tools/work_queue.py --bounce JOB --note WHY      mark a row bounced
  python3 tools/work_queue.py --add JOB --account A --brief PATH --model M --cap N --box MIN [--note TEXT]
Every write is whole-file read-modify-write; rows are never deleted, only their status cell changes.
"""
import argparse, csv, os, sys, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(os.path.dirname(HERE), "WORK-QUEUE.tsv")
COLS = ["job_id", "account", "brief", "model", "cap_usd", "box_min", "status", "added", "note"]
ACCOUNTS = ("owner", "other", "third", "account-1", "account-2", "account-3", "account-4")

def now(): return datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M")
def load():
    with open(PATH, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    for r in rows:  # a stray trailing tab gives an extra None field: fold it into note, never crash mid-write
        extra = [x for x in (r.pop(None, None) or []) if x]
        if extra: r["note"] = " ".join([r.get("note") or ""] + extra).strip()
    return rows
def save(rows):
    tmp = PATH + ".tmp"  # write whole, then rename: a failure never truncates the shared file
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader(); w.writerows(rows)
    os.replace(tmp, PATH)
def check(rows):
    bad = 0; seen = set()
    for i, r in enumerate(rows, 2):
        errs = []
        if list(r.keys()) != COLS: errs.append("columns")
        if r["job_id"] in seen: errs.append("duplicate job_id")
        seen.add(r["job_id"])
        if r["account"] not in ACCOUNTS: errs.append("account")
        if not os.path.exists(os.path.join(os.path.dirname(HERE), r["brief"])): errs.append("brief missing: " + r["brief"])
        s = r["status"].split()
        if not s or s[0] not in ("queued", "claimed", "done", "bounced"): errs.append("status")
        if s and s[0] == "claimed" and len(s) < 2: errs.append("claimed needs a session id")
        try: float(r["cap_usd"]); int(r["box_min"])
        except ValueError: errs.append("cap/box")
        if errs: bad += 1; print(f"line {i} {r.get('job_id','?')}: " + "; ".join(errs))
    q = sum(1 for r in rows if r["status"].startswith("queued"))
    c = sum(1 for r in rows if r["status"].startswith("claimed"))
    print(f"work_queue: {len(rows)} rows, queued {q}, claimed {c}, malformed {bad}")
    return bad == 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true"); ap.add_argument("--next", action="store_true")
    ap.add_argument("--account", choices=ACCOUNTS); ap.add_argument("--claim"); ap.add_argument("--session")
    ap.add_argument("--done"); ap.add_argument("--bounce"); ap.add_argument("--add"); ap.add_argument("--note", default="")
    ap.add_argument("--brief"); ap.add_argument("--model"); ap.add_argument("--cap"); ap.add_argument("--box")
    a = ap.parse_args(); rows = load()
    if a.check: sys.exit(0 if check(rows) else 1)
    if a.next:
        for r in rows:
            if r["status"].startswith("queued") and (not a.account or r["account"] == a.account):
                print("\t".join(r[c] for c in COLS))
        return
    if a.add:
        if any(r["job_id"] == a.add for r in rows): sys.exit(f"job {a.add} exists")
        if not (a.account and a.brief and a.model and a.cap and a.box): sys.exit("--add needs --account --brief --model --cap --box")
        rows.append({"job_id": a.add, "account": a.account, "brief": a.brief, "model": a.model, "cap_usd": a.cap,
                     "box_min": a.box, "status": "queued", "added": now(), "note": a.note}); save(rows); print("added", a.add); return
    key = a.claim or a.done or a.bounce
    if not key: ap.print_help(); return
    for r in rows:
        if r["job_id"] == key:
            if a.claim:
                if not r["status"].startswith("queued"): sys.exit(f"{key} is {r['status']}, not queued")
                if not a.session: sys.exit("--claim needs --session")
                r["status"] = f"claimed {a.session} {now()}"
            elif a.done: r["status"] = f"done {now()}"
            else:
                if not a.note: sys.exit("--bounce needs --note")
                r["status"] = f"bounced {now()} {a.note}"
            if a.note and not a.bounce: r["note"] = (r["note"] + "; " if r["note"] else "") + a.note
            save(rows); print(r["status"]); return
    sys.exit(f"no job {key}")
if __name__ == "__main__": main()
