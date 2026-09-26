#!/usr/bin/env python3
"""Orphan check across orchestrator/lane swaps (Usage 8a "rules become tools", owner's ask of 26 Sept
2026: "make sure we don't have any orphaned tasks across orchestrator swaps, and make sure this is
systematized"). Written by parent worker ORPHAN-TOOL for parent 7e.

The gap: a parent hands over (7d->7e->7f) and a lane hands over (B5->B6->B7); each successor adopts
what its predecessor's handoff names, in prose. Nothing mechanically checks that every still-running
or unarchived session, every enabled trigger and every ROOM.md claim without a done line belongs to a
live owner. This script cannot call the session API itself, so it takes the parent's own `list_sessions`
and `list_triggers` tool-call results, saved to disk as JSON, and cross-checks them against ROOM.md and
hub-seed/ASSIGNMENTS.md.

Five checks, each printed one line per problem found:
  (a) ORPHAN SESSION -- a non-archived session whose parent_session_id is archived or absent, not named
      in the last 6 hours of ROOM.md, and not named in any ASSIGNMENTS.md row.
  (b) STALE SESSION -- a non-archived session idle (updated_at) more than 3 hours, with no line in
      ROOM.md naming its id or its title/worker name and containing the word "done".
  (c) ORPHAN TRIGGER -- an enabled trigger whose persistent_session_id is archived or missing from the
      sessions list.
  (d) STALE CLAIM -- a ROOM.md line whose signal starts with "claim" and is older than 6 hours, with no
      later line from the same actor (matched on the text before the first "(", since a claim's and its
      own done line's parenthetical model/session-id annotation often differ) containing the word "done"
      or "handoff" anywhere in the signal (the six-hour rule in CLAUDE.md "Collaborators", tightened for
      automation: CLAUDE.md's fuller text also excuses a claim if the same agent posted ANY later line
      within six hours, which this does not check -- this errs toward flagging, which is the safer
      direction for a check a human reviews before acting).
  (e) UNLEDGERED CLOSE -- an ASSIGNMENTS.md row that names a session the sessions list shows archived,
      whose own Status cell does not start with done/handed/dropped.
  (f) TITLE MISMATCH -- a non-archived session whose title does not start with "LIVE ", or an archived
      session whose title does not start with "ARCHIVED" (the LIVE/ARCHIVED convention in
      .claude/briefs/parent.md "Handing over", 26 Sept 2026; added per RETRO-2026-09-26d item 1's ROOM.md
      ask of 05:17 UTC, so the check survives past the one worker instance that heard it verbally).

Exit codes: 0 clean, 1 if any of (a)-(f) is non-empty.

Usage:
  tools/orphan_check.py --sessions S.json --triggers T.json [--room-file ROOM.md]
                         [--assignments hub-seed/ASSIGNMENTS.md] [--now "2026-09-26 05:00"] [--room]
  tools/orphan_check.py --no-sessions
      Runs only the checks computable from ROOM.md/ASSIGNMENTS.md alone (just (d) -- (a),(b),(c),(e) all
      need the sessions/triggers files and are skipped, vacuously clean) -- for a session that has not
      saved list_sessions/list_triggers to disk this run.

--sessions/--triggers accept the raw tool-result text: a bare JSON list, or a dict carrying the list
under "sessions"/"triggers"/"data"/"items"/"results", optionally wrapped once more under an envelope key
(seen in practice as {"ccr": ...}) -- unwrapped defensively, recursing into the first dict/list value that
yields a list under one of those keys.

--room appends the one-line summary to ROOM.md through tools/room.py (commits and pushes); omit it to
just print and exit.
"""
import argparse
import datetime
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LIST_KEYS = ("sessions", "triggers", "data", "items", "results")
TS_RE = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2})')


def unwrap_list(obj, depth=0):
    """Defensively find the list of records inside a raw tool-result JSON blob (see module docstring)."""
    if isinstance(obj, list):
        return obj
    if isinstance(obj, dict) and depth < 4:
        for k in LIST_KEYS:
            if k in obj:
                got = unwrap_list(obj[k], depth + 1)
                if got:
                    return got
        for v in obj.values():
            if isinstance(v, (list, dict)):
                got = unwrap_list(v, depth + 1)
                if got:
                    return got
    return []


def load_records(path):
    if not path:
        return []
    with open(path, encoding="utf-8") as f:
        raw = json.load(f)
    return unwrap_list(raw)


def sget(rec, *keys, default=None):
    for k in keys:
        if k in rec and rec[k] is not None:
            return rec[k]
    return default


def sess_id(s):
    return str(sget(s, "id", "session_id", "sessionId", default="") or "")


def sess_archived(s):
    if "archived" in s:
        return bool(s["archived"])
    return str(sget(s, "status", default="")).lower() == "archived"


def sess_parent(s):
    p = sget(s, "parent_session_id", "parentSessionId", "parent_id")
    return str(p) if p else None


def sess_updated(s):
    return sget(s, "updated_at", "updatedAt", "last_active_at", "lastActiveAt", "last_activity_at")


def sess_title(s):
    return str(sget(s, "title", "name", default="") or "")


def trig_id(t):
    return str(sget(t, "id", "trigger_id", "triggerId", default="") or "")


def trig_enabled(t):
    if "enabled" in t:
        return bool(t["enabled"])
    return str(sget(t, "status", default="")).lower() in ("enabled", "active")


def trig_session(t):
    p = sget(t, "persistent_session_id", "persistentSessionId", "session_id", "sessionId")
    return str(p) if p else None


def parse_iso(s):
    """Parse an ISO-8601 timestamp (optionally 'Z'-suffixed) to a naive UTC datetime, or None."""
    if not s:
        return None
    try:
        dt = datetime.datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except ValueError:
        return None
    if dt.tzinfo is not None:
        dt = dt.astimezone(datetime.timezone.utc).replace(tzinfo=None)
    return dt


def parse_room_lines(path):
    """Return one dict per non-blank ROOM.md line: {ts, ts_dt, actor, signal, raw}."""
    rows = []
    if not os.path.exists(path):
        return rows
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.strip():
            continue
        parts = line.split(" | ", 2)
        if len(parts) < 3:
            continue
        ts, actor, signal = parts
        m = TS_RE.match(ts.strip())
        ts_dt = datetime.datetime.strptime(m.group(1), "%Y-%m-%d %H:%M") if m else None
        rows.append({"ts": ts.strip(), "ts_dt": ts_dt, "actor": actor.strip(), "signal": signal.strip(), "raw": line})
    return rows


def parse_assignments_rows(path):
    """Return one dict per ASSIGNMENTS.md table data row: {raw, status} -- status is the last
    non-empty cell, on the assumption (true of hub-seed/ASSIGNMENTS.md's own table) that Status is
    always the rightmost column."""
    rows = []
    if not os.path.exists(path):
        return rows
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.startswith("| ") and not line.startswith("|#"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or re.match(r'^:?-+:?$', cells[0]) or cells[0] in ("#", "Raised"):
            continue
        rows.append({"raw": line, "status": cells[-1] if cells else ""})
    return rows


def check_orphan_sessions(sessions, room_lines, assignments_text, now):
    problems = []
    by_id = {sess_id(s): s for s in sessions if sess_id(s)}
    since = now - datetime.timedelta(hours=6)
    recent_room_text = "\n".join(l["raw"] for l in room_lines if l["ts_dt"] and l["ts_dt"] >= since)
    for s in sessions:
        sid = sess_id(s)
        if not sid or sess_archived(s):
            continue
        parent = sess_parent(s)
        parent_archived_or_absent = (parent is None) or (parent in by_id and sess_archived(by_id[parent]))
        if not parent_archived_or_absent:
            continue
        if sid in recent_room_text or sid in assignments_text:
            continue
        problems.append(
            f"(a) ORPHAN SESSION: {sid} ({sess_title(s) or 'untitled'}) is not archived, its "
            f"parent_session_id is {parent or 'absent'} (archived or absent), and it is named neither "
            f"in ROOM.md's last 6 hours nor in hub-seed/ASSIGNMENTS.md"
        )
    return problems


def check_stale_sessions(sessions, room_lines, now):
    problems = []
    since = now - datetime.timedelta(hours=3)
    for s in sessions:
        if sess_archived(s):
            continue
        sid = sess_id(s)
        if not sid:
            continue
        updated = parse_iso(sess_updated(s))
        if updated is None or updated >= since:
            continue
        title = sess_title(s)
        has_done = any(
            "done" in l["raw"].lower() and (sid.lower() in l["raw"].lower() or (title and title.lower() in l["raw"].lower()))
            for l in room_lines
        )
        if not has_done:
            hours = (now - updated).total_seconds() / 3600
            problems.append(
                f"(b) STALE SESSION: {sid} ({title or 'untitled'}) idle since {sess_updated(s)} "
                f"({hours:.0f}h, over 3h) with no 'done' line in ROOM.md naming it"
            )
    return problems


def check_orphan_triggers(triggers, sessions):
    problems = []
    by_id = {sess_id(s): s for s in sessions if sess_id(s)}
    for t in triggers:
        if not trig_enabled(t):
            continue
        psid = trig_session(t)
        if not psid:
            continue
        if psid not in by_id:
            problems.append(f"(c) ORPHAN TRIGGER: {trig_id(t)} is enabled, bound to session {psid}, not in the sessions list")
        elif sess_archived(by_id[psid]):
            problems.append(f"(c) ORPHAN TRIGGER: {trig_id(t)} is enabled, bound to session {psid}, which is archived")
    return problems


def actor_core(actor):
    """The stable part of a ROOM.md actor field: a claim and its own done line often differ in the
    parenthetical (model, session id) -- 'bSCO (Sonnet)' claims, plain 'bSCO' reports done -- so match
    on the text before the first '(' rather than the full string."""
    return re.split(r'\(', actor, 1)[0].strip().rstrip(":").lower()


def check_stale_claims(room_lines, now):
    problems = []
    for i, l in enumerate(room_lines):
        sig = l["signal"]
        if not sig.lower().startswith("claim"):
            continue
        if l["ts_dt"] is None:
            continue
        age = now - l["ts_dt"]
        if age <= datetime.timedelta(hours=6):
            continue
        # room_lines is file order, i.e. chronological-or-tied (ROOM.md timestamps are minute-grained,
        # so a claim and its own done line often carry the identical minute) -- position, not a strict
        # ts_dt > comparison, is what "later" means here.
        core = actor_core(l["actor"])
        # "done"/"handoff" is matched anywhere in the signal, not only as its first word: a common
        # convention batches a worker's own report behind a "for LANE X: ..." prefix on the same
        # actor line (e.g. "LANE ZX2 ZX2-HEL ... | for LANE ZX2: hellen pool ... -- done: ...").
        resolved = any(
            actor_core(later["actor"]) == core and re.search(r'\b(done|handoff)\b', later["signal"], re.I)
            for later in room_lines[i + 1:]
        )
        if not resolved:
            hours = age.total_seconds() / 3600
            problems.append(
                f"(d) STALE CLAIM: {l['actor']} claimed {sig[:80]!r} at {l['ts']} "
                f"({hours:.0f}h ago, over 6h), no later done/handoff line from the same role"
            )
    return problems


def check_unledgered_closes(assignment_rows, sessions):
    problems = []
    archived_ids = [sess_id(s) for s in sessions if sess_id(s) and sess_archived(s)]
    for row in assignment_rows:
        status_lower = row["status"].lower()
        if status_lower.startswith(("done", "handed", "dropped")):
            continue
        for sid in archived_ids:
            if sid in row["raw"]:
                problems.append(
                    f"(e) UNLEDGERED CLOSE: ASSIGNMENTS.md row referencing archived session {sid} "
                    f"has status {row['status']!r}, not done/handed/dropped: {row['raw'][:100]!r}"
                )
    return problems


def check_title_mismatch(sessions):
    problems = []
    for s in sessions:
        sid = sess_id(s)
        if not sid:
            continue
        title = sess_title(s)
        if sess_archived(s):
            if not title.startswith("ARCHIVED"):
                problems.append(
                    f"(f) TITLE MISMATCH: {sid} is archived but its title {title!r} does not start "
                    f"with 'ARCHIVED' (parent.md 'Handing over')"
                )
        else:
            if not title.startswith("LIVE "):
                problems.append(
                    f"(f) TITLE MISMATCH: {sid} is not archived but its title {title!r} does not start "
                    f"with 'LIVE ' (parent.md 'Handing over')"
                )
    return problems


def run_all(sessions, triggers, room_lines, assignments_text, assignment_rows, now):
    a = check_orphan_sessions(sessions, room_lines, assignments_text, now)
    b = check_stale_sessions(sessions, room_lines, now)
    c = check_orphan_triggers(triggers, sessions)
    d = check_stale_claims(room_lines, now)
    e = check_unledgered_closes(assignment_rows, sessions)
    f = check_title_mismatch(sessions)
    return a, b, c, d, e, f


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sessions", help="path to a saved list_sessions JSON result")
    ap.add_argument("--triggers", help="path to a saved list_triggers JSON result")
    ap.add_argument("--room-file", default=os.path.join(ROOT, "ROOM.md"))
    ap.add_argument("--assignments", default=os.path.join(ROOT, "hub-seed", "ASSIGNMENTS.md"))
    ap.add_argument("--now", help="override 'now', e.g. '2026-09-26 05:00' (default: current UTC time)")
    ap.add_argument("--no-sessions", action="store_true", help="run only the ROOM.md-based check (d); skip (a),(b),(c),(e)")
    ap.add_argument("--room", action="store_true", help="append the summary line to ROOM.md via tools/room.py")
    args = ap.parse_args()

    if not args.no_sessions and not (args.sessions and args.triggers):
        ap.error("--sessions and --triggers are required (or pass --no-sessions to run only the ROOM.md/ASSIGNMENTS.md check)")

    now = datetime.datetime.strptime(args.now, "%Y-%m-%d %H:%M") if args.now else datetime.datetime.utcnow()

    sessions = [] if args.no_sessions else load_records(args.sessions)
    triggers = [] if args.no_sessions else load_records(args.triggers)
    room_lines = parse_room_lines(args.room_file)
    assignments_text = open(args.assignments, encoding="utf-8").read() if os.path.exists(args.assignments) else ""
    assignment_rows = parse_assignments_rows(args.assignments)

    a, b, c, d, e, f = run_all(sessions, triggers, room_lines, assignments_text, assignment_rows, now)

    for group in (a, b, c, d, e, f):
        for p in group:
            print(p)

    summary = (f"orphans: {len(a) + len(b)} sessions, {len(c)} triggers, {len(d)} claims, "
               f"{len(e)} unledgered, {len(f)} title-mismatches")
    print(summary)

    if args.room:
        try:
            subprocess.run([sys.executable, os.path.join(ROOT, "tools", "room.py"), "orphan_check.py", summary], cwd=ROOT)
        except Exception as exc:
            print(f"--room: could not append to ROOM.md: {exc}")

    sys.exit(1 if any((a, b, c, d, e, f)) else 0)


if __name__ == "__main__":
    main()
