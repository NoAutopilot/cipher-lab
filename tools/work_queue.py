#!/usr/bin/env python3
"""WORK-QUEUE.tsv: the single orchestrator's job list, pulled by the dispatcher routine on the other account.

Columns: job_id, account (owner|other|third), brief, model, cap_usd, box_min, status, added, note.
status is one of: queued | claimed <session_id> <UTC> | done <UTC> | bounced <UTC> <reason> | paused <UTC> (PAUSE rows only).
Account aliases: owner == account-1, other == account-2, third == account-3 (--next and auto-fill match either spelling).

  python3 tools/work_queue.py --check                      validate the file (exit 1 on a malformed row)
  python3 tools/work_queue.py --next --account other       print the queued rows for that account, oldest first
  python3 tools/work_queue.py --claim JOB --session ID     mark a row claimed (fails if not queued)
  python3 tools/work_queue.py --done JOB [--note TEXT]     mark a row done
  python3 tools/work_queue.py --bounce JOB --note WHY      mark a row bounced
  python3 tools/work_queue.py --add JOB --account A --brief PATH --model M --cap N --box MIN [--note TEXT]
  python3 tools/work_queue.py --pause ACCOUNT [--note WHY] / --resume ACCOUNT   stop / restart auto-fill for an account

Empty-queue auto-fill (LANE-SYS1, 5 Oct 2026; opt out with --no-autofill). `--next --account A` appends ONE row
DEFAULT-<A>-<YYYYMMDD-HHMM> (brief .claude/briefs/default-lane.md, Opus 5.5, cap 60, box 600, queued, note
"auto-fill: empty queue") and prints it like any queued row when ALL hold, A read through the aliases above:
  (1) no queued row for A; (2) no open lane row for A (job_id LANE-* or DEFAULT-*, status claimed and not stale:
  claimed age < box_min + 360 min, CLAUDE.md's six-hour stale-claim rule); (3) A's newest lane `done`/`bounced`
  stamp is >= 60 min old (a fuzzy minute "13:5x" reads as 13:59, the later bound); (4) no PAUSE-<A> row with
  status paused; (5) no DEFAULT-* row for A added in the last 12 h.
Catches: a dispatcher firing that finds nothing queued and leaves the account idle for hours (5 Oct 2026, the
owner restarting both accounts by hand). Must NOT fill: when a queued row exists, a lane closed < 60 min ago, a lane
is still claimed, PAUSE is set, a default lane was added < 12 h ago, or for account B when only B's queue is empty and
A was asked (tests tools/tests/test_work_queue.py). --next without --account never fills.
Every write is whole-file read-modify-write; rows are never deleted, only their status cell changes.
"""
import argparse, csv, os, sys, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.environ.get("WQ_PATH") or os.path.join(os.path.dirname(HERE), "WORK-QUEUE.tsv")  # WQ_PATH: tests only
COLS = ["job_id", "account", "brief", "model", "cap_usd", "box_min", "status", "added", "note"]
ACCOUNTS = ("owner", "other", "third", "account-1", "account-2", "account-3", "account-4")
ALIAS = {"owner": "account-1", "other": "account-2", "third": "account-3"}
DEFAULT_BRIEF = ".claude/briefs/default-lane.md"

def canon(a): return ALIAS.get(a, a)
def parse_ts(date, hm):
    """'2026-10-04', '12:0x' -> datetime; an x digit reads as 9 (the later bound). None if unparseable."""
    try: return datetime.datetime.strptime(date + " " + hm.replace("x", "9").replace("X", "9")[:5], "%Y-%m-%d %H:%M")
    except (ValueError, TypeError): return None
def is_lane(r): return r["job_id"].startswith(("LANE-", "DEFAULT-"))
def autofill(rows, account, t=None):
    """Return the DEFAULT row to append for `account`, or None with the reason; never mutates rows."""
    t = t or datetime.datetime.utcnow(); A = canon(account)
    mine = [r for r in rows if canon(r["account"]) == A]
    if any(r["status"].startswith("queued") for r in mine): return None, "queued row exists"
    if any(r["job_id"] == "PAUSE-" + A and r["status"].startswith("paused") for r in mine): return None, "paused"
    last_close = None
    for r in mine:
        if not is_lane(r): continue
        s = r["status"].split()
        if s and s[0] == "claimed":
            ts = parse_ts(*s[2:4]) if len(s) >= 4 else None
            try: box = int(r["box_min"])
            except ValueError: box = 600
            if ts is None or (t - ts).total_seconds() / 60 < box + 360: return None, "lane open: " + r["job_id"]
        elif s and s[0] in ("done", "bounced") and len(s) >= 3:
            ts = parse_ts(s[1], s[2])
            if ts and (last_close is None or ts > last_close): last_close = ts
        if r["job_id"].startswith("DEFAULT-"):
            ad = (r["added"] or "").split()
            ts = parse_ts(*ad[:2]) if len(ad) >= 2 else None
            if ts is None or (t - ts).total_seconds() < 12 * 3600: return None, "default lane < 12 h: " + r["job_id"]
    if last_close and (t - last_close).total_seconds() < 3600: return None, "lane closed < 60 min ago"
    jid = f"DEFAULT-{A}-{t.strftime('%Y%m%d-%H%M')}"
    if any(r["job_id"] == jid for r in rows): return None, "id exists"
    return {"job_id": jid, "account": A, "brief": DEFAULT_BRIEF, "model": "Opus 5.5", "cap_usd": "60", "box_min": "600",
            "status": "queued", "added": t.strftime("%Y-%m-%d %H:%M"), "note": "auto-fill: empty queue"}, "filled"

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
        pause = r["job_id"].startswith("PAUSE-")
        if not pause and not os.path.exists(os.path.join(os.path.dirname(HERE), r["brief"])): errs.append("brief missing: " + r["brief"])
        s = r["status"].split()
        if not s or s[0] not in ("queued", "claimed", "done", "bounced") + (("paused",) if pause else ()): errs.append("status")
        if s and s[0] == "claimed" and len(s) < 2: errs.append("claimed needs a session id")
        try: float(r["cap_usd"]); int(r["box_min"])
        except ValueError: errs.append("cap/box")
        if errs: bad += 1; print(f"line {i} {r.get('job_id','?')}: " + "; ".join(errs))
    q = sum(1 for r in rows if r["status"].startswith("queued"))
    c = sum(1 for r in rows if r["status"].startswith("claimed"))
    print(f"work_queue: {len(rows)} rows, queued {q}, claimed {c}, malformed {bad}")
    return bad == 0

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true"); ap.add_argument("--next", action="store_true")
    ap.add_argument("--account", choices=ACCOUNTS); ap.add_argument("--claim"); ap.add_argument("--session")
    ap.add_argument("--done"); ap.add_argument("--bounce"); ap.add_argument("--add"); ap.add_argument("--note", default="")
    ap.add_argument("--brief"); ap.add_argument("--model"); ap.add_argument("--cap"); ap.add_argument("--box")
    ap.add_argument("--no-autofill", action="store_true", help="--next: never append a DEFAULT row")
    ap.add_argument("--pause", choices=ACCOUNTS); ap.add_argument("--resume", choices=ACCOUNTS)
    a = ap.parse_args(); rows = load()
    if a.check: sys.exit(0 if check(rows) else 1)
    if a.next:
        if a.account and not a.no_autofill:
            new, why = autofill(rows, a.account)
            if new: rows.append(new); save(rows)
            print(f"# autofill: {why}", file=sys.stderr)
        for r in rows:
            if r["status"].startswith("queued") and (not a.account or canon(r["account"]) == canon(a.account)):
                print("\t".join(r[c] for c in COLS))
        return
    if a.pause or a.resume:
        A = canon(a.pause or a.resume); jid = "PAUSE-" + A
        r = next((r for r in rows if r["job_id"] == jid), None)
        if r is None:
            if a.resume: sys.exit(f"no {jid} row")
            r = {"job_id": jid, "account": A, "brief": "-", "model": "-", "cap_usd": "0", "box_min": "0",
                 "status": "", "added": now(), "note": ""}; rows.append(r)
        r["status"] = f"paused {now()}" if a.pause else f"done {now()}"
        if a.note: r["note"] = (r["note"] + "; " if r["note"] else "") + a.note
        save(rows); print(jid, r["status"]); return
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
